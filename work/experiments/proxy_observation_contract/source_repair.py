"""Fetch exact public source or construct an unapplied, hash-checked repair patch."""
import argparse
import ast
import difflib
import hashlib
import json
from pathlib import Path
import urllib.request

HERE = Path(__file__).resolve().parent
ENV = 'src/robomme/robomme_env/VideoUnmask.py'
GOAL = 'src/robomme/robomme_env/utils/task_goal.py'
BUILDER = 'src/robomme/env_record_wrapper/episode_config_resolver.py'
HELPER = 'src/robomme/robomme_env/utils/proxy_fixture.py'


def replace_once(text, old, new):
    if text.count(old) != 1:
        raise ValueError('Expected exactly one source anchor: ' + old[:80])
    return text.replace(old, new, 1)


def source_lock():
    return json.loads((HERE / 'sources.lock.json').read_text())['sources']


def fetch(destination):
    destination.mkdir(parents=True, exist_ok=True)
    for row in source_lock():
        target = destination / row['path']
        if target.exists():
            data = target.read_bytes()
        else:
            with urllib.request.urlopen(row['url'], timeout=30) as response:
                data = response.read()
        if hashlib.sha256(data).hexdigest() != row['sha256']:
            raise ValueError('Pinned source digest mismatch: ' + row['path'])
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)


def repair(source_root):
    original = {}
    for row in source_lock():
        data = (source_root / row['path']).read_bytes()
        if hashlib.sha256(data).hexdigest() != row['sha256']:
            raise ValueError('Pinned source digest mismatch: ' + row['path'])
        original[row['path']] = data.decode()
    modified = dict(original)
    text = modified[ENV]
    text = replace_once(text, 'from .utils.difficulty import normalize_robomme_difficulty',
                        'from .utils.difficulty import normalize_robomme_difficulty\nfrom .utils.proxy_fixture import resolve_fixture')
    text = replace_once(text, '        self.use_demonstrationwrapper=False',
                        '        proxy_fixture_input = kwargs.pop("proxy_fixture", None)\n        self.use_demonstrationwrapper=False')
    text = replace_once(text, '        super().__init__(*args, robot_uids=robot_uids, **kwargs)',
                        '        self.proxy_fixture = resolve_fixture(proxy_fixture_input, seed, self.difficulty)\n'
                        '        if self.proxy_fixture is not None and (self.robomme_failure_recovery or robot_uids != "panda_wristcam"):\n'
                        '            raise ValueError("Proxy fixture requires Panda wristcam without injected recovery")\n'
                        '        super().__init__(*args, robot_uids=robot_uids, **kwargs)')
    text = replace_once(text, '        shuffle_indices = torch.randperm(len(cube_colors), generator=generator).tolist()',
                        '        if self.proxy_fixture is None:\n'
                        '            shuffle_indices = torch.randperm(len(cube_colors), generator=generator).tolist()\n'
                        '        else:\n'
                        '            if len(self.spawned_bins) != 3:\n'
                        '                raise ValueError("Fixture did not spawn exactly three bins")\n'
                        '            shuffle_indices = self.proxy_fixture["color_permutation"]')
    text = replace_once(text, '        self.color_names = color_names',
                        '        self.color_names = color_names\n'
                        '        self.proxy_target_index = 0 if self.proxy_fixture is None else self.proxy_fixture["target_bin_index"]\n'
                        '        self.proxy_target_bin = self.spawned_bins[self.proxy_target_index]\n'
                        '        self.proxy_target_color = self.color_names[self.proxy_target_index]')
    begin = text.index('        tasks = [')
    end = text.index("        if self.configs[self.difficulty]['pick']>1:", begin)
    block = text[begin:end]
    if block.count('self.bin_0') != 4 or block.count('self.color_names[0]') != 2:
        raise ValueError('Unexpected task binding shape')
    text = text[:begin] + block.replace('self.bin_0', 'self.proxy_target_bin').replace('self.color_names[0]', 'self.proxy_target_color') + text[end:]
    text = replace_once(text, '        test=[bin for bin in self.spawned_bins if bin != self.bin_0]',
                        '        test=[bin for bin in self.spawned_bins if bin != self.proxy_target_bin]')
    modified[ENV] = text
    text = modified[GOAL]
    begin, end = text.index('    elif env == "VideoUnmask":'), text.index('    elif env == "VideoUnmaskSwap":')
    block = replace_once(text[begin:end], '        cube_0_color = color_names[0]',
                         '        cube_0_color = color_names[getattr(self.env.unwrapped, "proxy_target_index", 0)]')
    modified[GOAL] = text[:begin] + block + text[end:]
    text = modified[BUILDER]
    modified[BUILDER] = replace_once(text, '        seed_desc = seed if seed is not None else "default"',
        '        metadata = get_episode_metadata(self.metadata_index, self.env_id, episode_idx)\n'
        '        fixture = metadata.get("proxy_fixture") if metadata else None\n'
        '        if fixture is not None:\n'
        '            if self.env_id != "VideoUnmask" or self.action_space != "joint_angle":\n'
        '                raise ValueError("Proxy fixture requires VideoUnmask joint_angle")\n'
        '            env_kwargs["proxy_fixture"] = fixture\n'
        '        seed_desc = seed if seed is not None else "default"')
    modified[HELPER] = (HERE / 'fixture_api.py').read_text()
    for path, content in modified.items():
        ast.parse(content, filename=path)
        compile(content, path, 'exec')  # Parse/compile only; upstream module not imported.
    return original, modified


def patch_text(original, modified):
    chunks = []
    for path, content in sorted(modified.items()):
        chunks.extend(difflib.unified_diff(original.get(path, '').splitlines(keepends=True),
                                         content.splitlines(keepends=True),
                                         fromfile='a/' + path if path in original else '/dev/null', tofile='b/' + path))
    return ''.join(chunks)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['fetch'])
    parser.add_argument('directory', type=Path)
    args = parser.parse_args()
    fetch(args.directory)
