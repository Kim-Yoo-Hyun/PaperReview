"""Select camera channels after the native observation has been matched to a detached render."""
from drawer_view_render import ViewSchedule
from atomic_control import digest
from verify_atomic import CAMERAS


class RoutedViews:
    def __init__(self, native_renderer, channels):
        self.native = native_renderer
        self.env = native_renderer.env
        self.channels = tuple(channels)

    def images(self, query, sample, opposite_qpos=None):
        images, record = self.native.images(query, sample, opposite_qpos)
        active = self.channels if opposite_qpos is not None else ()
        record['narrow_rgb'] = dict(record['sent']) if active else {}
        record['narrow_changed_pixels'] = dict(record['changed_pixels']) if active else {}
        record['selected'] = list(active)
        # Matching may reacquire both native images. Read the retained channel
        # from the matched observation after that call, including any retries.
        if active:
            images = {c:images[c] if c in active else query[c] for c in CAMERAS}
            record['changed_pixels'] = {c:record['changed_pixels'][c] if c in active else 0 for c in CAMERAS}
            record['sent'] = {c:digest(images[c]) for c in CAMERAS}
        return images, record


def schedule(env, scene, *, host, narrow, channels, indices, width):
    reference = {c:(narrow if c in channels else host)[c] for c in CAMERAS}
    view = ViewSchedule(env,scene,drawer='bottom',width=width,limit=4,bank=host,
                        opposite_bank=reference,indices=indices if channels else [], initial_attempts=8)
    view.renderer = RoutedViews(view.renderer,channels)
    return view
