"""Record the decoded request and JAX key around each call to the released policy."""
import hashlib
import json
from pathlib import Path
import sys

import jax
import numpy as np
from openpi.policies import policy_config
from openpi.serving.websocket_policy_server import WebsocketPolicyServer
from openpi.training import config

from run_r1 import CHECKPOINT, MODEL
from verify_atomic import CAMERAS


class ObservedPolicy:
    def __init__(self, policy, receipts):
        self.policy = policy
        self.receipts = receipts

    def infer(self, obs):
        assert set(obs) == {*CAMERAS, 'prompt', 'observation/state'}
        record = {'prompt':obs['prompt'], 'proprioception':np.asarray(obs['observation/state']).tolist(),
                  'rgb_sha256':{}, 'rng_before':jax.random.key_data(self.policy._rng).tolist()}
        for camera in CAMERAS:
            pixels = np.asarray(obs[camera])
            assert pixels.dtype == np.uint8 and pixels.shape == (224,224,3)
            record['rgb_sha256'][camera] = hashlib.sha256(pixels.tobytes()).hexdigest()
        reply = self.policy.infer(obs)
        actions = np.asarray(reply['actions'], dtype='<f8')
        assert actions.shape == (10,7)
        record['actions_sha256'] = hashlib.sha256(actions.tobytes()).hexdigest()
        record['rng_after'] = jax.random.key_data(self.policy._rng).tolist()
        self.receipts.write(json.dumps(record, separators=(',', ':'), allow_nan=False)+'\n')
        return reply


if __name__ == '__main__':
    policy = policy_config.create_trained_policy(config.get_config(MODEL), str(CHECKPOINT), default_prompt=None)
    with Path(sys.argv[1]).open('x', buffering=1) as receipts:
        WebsocketPolicyServer(policy=ObservedPolicy(policy, receipts), host='0.0.0.0',
                              port=8000, metadata=policy.metadata).serve_forever()
