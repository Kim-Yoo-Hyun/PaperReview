"""Serve the released single-observation policy with a separate native key stream per rollout."""
import contextvars
import json
from pathlib import Path
import sys

import jax
from openpi.policies import policy_config
from openpi.serving.websocket_policy_server import WebsocketPolicyServer
from openpi.training import config

from run_r1 import CHECKPOINT, MODEL
from serve_first_view import ObservedPolicy


active = contextvars.ContextVar('camera_study_path')


class IndependentKeys:
    def __init__(self, policy):
        self.policy = policy

    def infer(self, obs):
        stream = active.get()
        assert stream['count'] < stream['expected']
        if stream['count'] == 0:
            assert obs['prompt'] == stream['source']
        # The native server calls infer synchronously before awaiting the socket.
        self.policy._rng = stream['rng']
        reply = stream['observed'].infer(obs)
        stream['rng'] = self.policy._rng
        stream['count'] += 1
        return reply


class SessionServer(WebsocketPolicyServer):
    def __init__(self, policy, folder, plan):
        super().__init__(policy=IndependentKeys(policy),host='0.0.0.0',port=8000,metadata=policy.metadata)
        self.native = policy
        self.folder = folder
        self.sessions = {p['session']:p for p in plan}
        assert len(self.sessions) == len(plan)

    async def _handler(self, websocket):
        name = websocket.request.path.removeprefix('/')
        entry = self.sessions.pop(name)
        path = self.folder/entry['receipts']
        with path.open('x', buffering=1) as receipts:
            rng = jax.random.key(entry['key'])
            for _ in range(entry.get('key_offset', 0)):
                rng, _ = jax.random.split(rng)
            stream = dict(rng=rng,count=0,source=entry['source'],expected=entry.get('queries',61),
                          observed=ObservedPolicy(self.native,receipts))
            token = active.set(stream)
            try:
                await super()._handler(websocket)
                assert stream['count'] == stream['expected']
            finally:
                active.reset(token)


if __name__ == '__main__':
    plan = Path(sys.argv[1])
    model = policy_config.create_trained_policy(config.get_config(MODEL),str(CHECKPOINT),default_prompt=None)
    SessionServer(model,plan.parent,json.loads(plan.read_bytes())).serve_forever()
