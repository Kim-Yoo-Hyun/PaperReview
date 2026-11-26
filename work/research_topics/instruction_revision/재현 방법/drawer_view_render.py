"""Render the native LIBERO cameras from detached MuJoCo data at another drawer width."""
from copy import copy

import mujoco
import numpy as np
from resteer.sim import libero
from robosuite.environments.robot_env import IMAGE_CONVENTION_MAPPING, macros

from atomic_control import capture_state, digest
from drawer_sim import observe, state_hash
from verify_atomic import CAMERAS
from verify_middle_aperture import contact_geometry, targets


class DrawerViews:
    def __init__(self, env, drawer):
        self.env = env
        self.model = env.sim.model._model
        self.live = env.sim.data._data
        self.context = env.sim._render_context_offscreen
        self.scene = mujoco.MjvScene(self.model, maxgeom=self.context.scn.maxgeom)
        self.scene.flags[:] = self.context.scn.flags
        self.camera = copy(self.context.cam)
        self.camera.type = mujoco.mjtCamera.mjCAMERA_FIXED
        self.names = tuple(s.removesuffix('_image') for s in libero.CAMERA_OBSERVABLES)
        self.width, self.height = env.env.camera_widths[0], env.env.camera_heights[0]
        assert all(w == self.width for w in env.env.camera_widths)
        assert all(h == self.height for h in env.env.camera_heights)
        self.viewport = mujoco.MjrRect(0, 0, self.width, self.height)
        model = self.model
        joint = model.joint(f'wooden_cabinet_1_{drawer}_level').id
        self.body = model.body(f'wooden_cabinet_1_cabinet_{drawer}').id
        assert model.jnt_bodyid[joint] == self.body and model.jnt_type[joint] == mujoco.mjtJoint.mjJNT_SLIDE
        assert not np.any(model.body_parentid == self.body)
        assert not np.any(model.cam_bodyid == self.body) and not np.any(model.light_bodyid == self.body)
        self.joint = joint
        self.qpos = int(model.jnt_qposadr[joint])
        self.geoms = np.flatnonzero(model.geom_bodyid == self.body)
        self.sites = np.flatnonzero(model.site_bodyid == self.body)

    def rgb(self, data):
        ctx = self.context
        ctx.gl_ctx.make_current()
        rgb = {}
        for name, observable in zip(self.names, libero.CAMERA_OBSERVABLES, strict=True):
            self.camera.fixedcamid = self.model.camera(name).id
            mujoco.mjv_updateScene(self.model, data, ctx.vopt, ctx.pert, self.camera,
                                   mujoco.mjtCatBit.mjCAT_ALL, self.scene)
            mujoco.mjr_render(self.viewport, self.scene, ctx.con)
            image = ctx.read_pixels(self.width, self.height)
            rgb[observable] = image[::IMAGE_CONVENTION_MAPPING[macros.IMAGE_CONVENTION]]
        resolution = libero.POLICY_RESOLUTION
        return {cam: libero.image_tools.convert_to_uint8(libero.image_tools.resize_with_pad(im, resolution, resolution))
                for cam, im in zip(CAMERAS, libero.camera_images(rgb), strict=True)}

    def images(self, query, sample, opposite_qpos=None):
        assert state_hash(capture_state(self.env)) == sample['physics']
        detached = copy(self.live)
        assert not np.shares_memory(detached.qpos, self.live.qpos)
        # A GPU raster can occasionally differ at an edge even for two native
        # renders. Keep the first observation when possible. If it cannot be
        # matched, reacquire the native cameras without stepping the simulation.
        mismatches = []
        for observation in range(3):
            if observation:
                fresh, check = observe(self.env, None, False, query['prompt'])
                assert check['physics'] == sample['physics'] and check['state'] == sample['state']
                query.update({c: fresh[c] for c in CAMERAS})
                sample['live'] = check['live']
            for _ in range(4):
                own = self.rgb(detached)
                diff = {c: int(np.any(own[c] != query[c], axis=2).sum()) for c in CAMERAS}
                if not any(diff.values()):
                    break
                mismatches.append(dict(observation=observation, native=sample['live'],
                                       detached={c: digest(own[c]) for c in CAMERAS}, pixels=diff))
            else:
                continue
            break
        else:
            raise RuntimeError(f'No matching native/detached camera pair at unchanged physics: {mismatches}')
        host_qpos = float(detached.qpos[self.qpos])
        delivered = own
        if opposite_qpos is not None:
            # After an integration step the renderer uses cached world poses. Recompute
            # only the selected slide in a second copy, preserving every other rendered pose.
            kinematics = copy(detached)
            kinematics.qpos[self.qpos] = opposite_qpos
            mujoco.mj_kinematics(self.model, kinematics)
            detached.qpos[self.qpos] = opposite_qpos
            for name, indices in (('xpos', self.body), ('xipos', self.body), ('xanchor', self.joint),
                                  ('geom_xpos', self.geoms), ('site_xpos', self.sites)):
                getattr(detached, name)[indices] = getattr(kinematics, name)[indices]
            delivered = self.rgb(detached)
        after = state_hash(capture_state(self.env))
        assert sample['physics'] == after
        record = dict(self_rgb={c: digest(own[c]) for c in CAMERAS},
                      sent={c: digest(delivered[c]) for c in CAMERAS},
                      changed_pixels={c: int(np.any(own[c] != delivered[c], axis=2).sum()) for c in CAMERAS},
                      host_qpos=host_qpos, render_qpos=float(detached.qpos[self.qpos]), host_after=after)
        if mismatches:
            record.update(mismatches=mismatches, native_reacquisitions=observation)
        return delivered, record


class ViewSchedule:
    def __init__(self, env, scene, *, drawer, width, limit, bank, opposite_bank, indices=None, duration=None,
                 initial_attempts=1):
        self.renderer = DrawerViews(env, drawer)
        self.geometry = contact_geometry(scene.geometry)
        self.qpos = scene.slides[drawer]['closed'] - width
        assert (indices is None) != (duration is None)
        self.indices = frozenset(range(duration) if indices is None else indices)
        self.limit = limit
        self.bank, self.opposite_bank = bank, opposite_bank
        self.initial_attempts = initial_attempts

    def apply(self, index, query, sample, rows):
        if index >= self.limit:
            return
        contact = any(set(targets(r, self.geometry)) - {'other'} for r in rows)
        exchange = index in self.indices and not contact
        reference = self.opposite_bank if exchange else self.bank
        retries = []
        for attempt in range(self.initial_attempts if index == 0 else 1):
            if attempt:
                fresh, state = observe(self.renderer.env, None, False, query['prompt'])
                assert (state['physics'], state['state']) == (sample['physics'], sample['state'])
                query.update({c: fresh[c] for c in CAMERAS})
                sample['live'] = state['live']
            rgb, record = self.renderer.images(query, sample, self.qpos if exchange else None)
            if index or (sample['live'] == self.bank and record['sent'] == reference):
                break
            retries.append(record)
        else:
            raise RuntimeError(f'Initial host or delivered image differs from native width reference: {retries}')
        if retries:
            record['reference_retries'] = retries
        if exchange or (not self.indices and not contact):
            query.update(rgb)
        sample['render'] = dict(record, exchange=exchange)

    @staticmethod
    def compare_replay(sample, previous):
        current, old = sample.get('render'), previous.get('render')
        if current is None or old is None:
            assert old is current
            return False
        assert all(current[k] == old[k] for k in ('host_qpos', 'render_qpos', 'host_after', 'exchange'))
        return any(current[k] != old[k] for k in ('self_rgb', 'sent', 'changed_pixels'))
