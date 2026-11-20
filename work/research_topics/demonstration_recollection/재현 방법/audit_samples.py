"""Check public demonstration recordings. All URLs and content hashes are fixed."""

import argparse
import csv
import hashlib
import io
import json
import pickle
import pickletools
import tarfile
from urllib.parse import quote
from urllib.request import Request, urlopen

import h5py
import numpy as np
import pyarrow.parquet as pq


def verify(content, digest, source):
    if hashlib.sha256(content).hexdigest() != digest:
        raise ValueError(f"SHA-256 mismatch for {source}")
    return content


def download(url, digest):
    with urlopen(url, timeout=60) as response:
        return verify(response.read(), digest, url)


DROID = (
    ("IPRL/success/2024-01-01/Mon_Jan__1_10:01:44_2024", "1710758024584422",
     "1369dc6e3c3b77dfb688ccbd83e082f8c5ea088f822f696f0a24edaa5919f01a"),
    ("CLVR/success/2023-05-09/Tue_May__9_01:17:11_2023", "1710756920770938",
     "ca0fcb5202a4e42677e137269d8a3bd90b9c0a12c3237a25555cada41e01010f"),
    ("TRI/failure/2023-08-10/Thu_Aug_10_08:59:17_2023", "1710759897902315",
     "33f495327646503038aaad6d978bb57b9959ae2d2db950b3dfcae122bd2236d1"),
)


def droid():
    base = "https://storage.googleapis.com/gresearch/robotics/droid_raw/1.0.1/"
    results = {}
    for path, generation, digest in DROID:
        url = f"{base}{quote(path)}/trajectory.h5?generation={generation}"
        with h5py.File(io.BytesIO(download(url, digest)), "r") as sample:
            obs = sample["observation"]
            command = sample["action"]
            enabled = ~obs["timestamp/skip_action"][:].astype(bool)
            np.testing.assert_array_equal(enabled, obs["controller_info/movement_enabled"][:])
            desired = command["target_cartesian_position"][:, :3]
            measured = obs["robot_state/cartesian_position"][:, :3]
            raw = 5.0 * (desired[enabled] - measured[enabled])
            magnitude = np.linalg.norm(raw, axis=1)
            reconstructed = raw / np.maximum(1.0, magnitude[:, None])
            logged = command["cartesian_velocity"][:, :3]
            np.testing.assert_allclose(reconstructed, logged[enabled], atol=1e-12, rtol=0)
            np.testing.assert_array_equal(logged[~enabled], np.zeros_like(logged[~enabled]))
            results[path.split("/")[0]] = {
                "frames": len(enabled), "enabled": int(enabled.sum()),
                "saturated_translation": int((magnitude > 1).sum()),
                "max_abs_error": float(np.max(np.abs(reconstructed - logged[enabled]))),
            }
    return results


SHARED = (
    "https://raw.githubusercontent.com/VT-Collab/repeated-shared-autonomy/"
    "0bca58cbdcaf07f13b92a2d02deab8ea59b4c376/IROS2021/robot-experiments/user_study/user/user1/"
)


def read_lists(path, digest):
    data = download(SHARED + path, digest)
    # The four pinned files contain only nested lists and IEEE floats.
    allowed = {"APPENDS", "BINFLOAT", "EMPTY_LIST", "FRAME", "MARK", "MEMOIZE", "PROTO", "STOP"}
    if any(op.name not in allowed for op, _, _ in pickletools.genops(data)):
        raise ValueError(f"Unexpected pickle opcode in {path}")
    return pickle.loads(data)


def shared():
    demo = read_lists("demos/final_n_1.pkl", "e10a2bf049b24b53c1203c6df93adc0aa49374f81bb0ee331393d46cf8520e70")
    run = read_lists("runs/final_n_1.pkl", "ac6f9df022fe28cc88dc16e07aa56319e352045f4fe8b3571ce2e178974ec703")
    blend = read_lists("policy_blending/n_1.pkl", "8cc83979b3ad7ae1a8a7dcc85d0793bf953b0fd9d60e12e058bf6466c8a22bf3")
    direct = read_lists("demos/n1.pkl", "0aba78a160abe755c47799914f2bb73e2d53a9dfd4c73e9d7c364480ba01a564")
    np.testing.assert_array_equal(np.asarray(demo)[:, 7:], [row[1] for row in run])
    result = {"paired_joint_rows": len(run), "direct_demo_shape": np.shape(direct)}
    for name, rows in (("learned_assistance", run), ("policy_blending", blend)):
        times, positions, user, robot, weights = zip(*rows)
        if any(np.shape(values) != (len(rows), 7) for values in (positions, user, robot)):
            raise ValueError(f"Invalid control record for {name}")
        result[name] = {
            "rows": len(rows), "nonzero_user": int((np.linalg.norm(user, axis=1) > 1e-12).sum()),
            "median_interval_s": float(np.median(np.diff(times))),
            "weight_range": [min(weights), max(weights)],
        }
    return result


HARMONIC = {
    "control_mode.txt": "4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865",
    "ada_joy.csv": "7e711a16e55b7ad4d4aa4e579fe19d04b3deeca817ba516c345a5f9fd0c49a23",
    "input_info.csv": "caf7678f1e4f95ccdad75e102e3af29441fb7452b599b9bc006d6be26aa5eb3f",
    "assistance_info.csv": "1eff80c06b5ee1ce98fd77d80cfff670e945e4c4def80427343080417bdc1368",
    "joint_positions.csv": "f3eca6bc89cb416aaea6b0c77c8dffe49d2ae1cabff3f5d8a7f82949d3bc1da8",
    "robot_position.csv": "85a708a5d9688180cf59611f1124d679e08f7fc6a5f159687f26efeca7fa8008",
}


def harmonic():
    url = "https://drive.usercontent.google.com/download?id=1G4_fGdH0fB_8JCHj4vCEfcaej-oXs7M4&export=download&confirm=t"
    request = Request(url, headers={"Range": "bytes=0-167772159", "User-Agent": "Mozilla/5.0"})
    directory = "harmonic_0.5.0/p100/run/005/text_data"
    results, streams = {}, {}
    prefixes = {"input_info.csv": "twist_", "assistance_info.csv": "exec_twist_"}
    with urlopen(request, timeout=60) as response:
        if response.status != 206 or response.getheader("Content-Range") != "bytes 0-167772159/4567474452":
            raise ValueError("Unexpected HARMONIC archive or byte range")
        with tarfile.open(fileobj=response, mode="r|gz") as archive:
            for member in archive:
                folder, _, name = member.name.rpartition("/")
                if folder != directory or name not in HARMONIC or not member.isfile():
                    continue
                data = verify(archive.extractfile(member).read(), HARMONIC[name], name)
                if name == "control_mode.txt":
                    results[name] = int(data)
                else:
                    reader = csv.DictReader(io.StringIO(data.decode()))
                    if name in prefixes:
                        axes = [prefixes[name] + axis for axis in ("x", "y", "z", "r", "p", "yaw")]
                        rows = list(reader)
                        times = [row["timestamp"] for row in rows]
                        twists = np.asarray([[float(row[axis]) for axis in axes] for row in rows])
                        streams[name] = times, twists
                        results[name] = len(rows)
                    else:
                        results[name] = sum(1 for _ in reader)
                if results.keys() == HARMONIC.keys():
                    break
    if results.keys() != HARMONIC.keys():
        raise ValueError("Incomplete HARMONIC trial")
    request_times, user = streams["input_info.csv"]
    applied_times, applied = streams["assistance_info.csv"]
    if request_times != applied_times or len(set(request_times)) != len(request_times):
        raise ValueError("Twist samples cannot be paired uniquely by their timestamps")
    if not np.isfinite(user).all() or not np.isfinite(applied).all():
        raise ValueError("Non-finite twist sample")
    results["paired_by_timestamp"] = len(request_times)
    results["nonzero_user_twist"] = int((np.abs(user).max(axis=1) > 1e-8).sum())
    results["different_twist"] = int((np.abs(user - applied).max(axis=1) > 1e-8).sum())
    return results


def copilot():
    base = ("https://huggingface.co/datasets/shashuo0104/0128_gearmesh_res_nn_same_trial/"
            "resolve/4a8310fdbd932bf721c458c2408d064bef9a7843/")
    digest = "a33e1187bdaaee7277f16170688be167811ba418cd323ab55c4af98982f48759"
    shard = pq.ParquetFile(io.BytesIO(download(base + "data/chunk-000/file-000.parquet?download=true", digest)))
    columns = ["episode_index", "frame_index", "timestamp", "action", "observation.state", "next.done", "task_index"]
    table = shard.read(columns=columns)
    episode = table.filter(table["episode_index"].to_numpy() == 0)
    np.testing.assert_array_equal(episode["frame_index"].to_numpy(), np.arange(len(episode)))
    np.testing.assert_allclose(episode["timestamp"].to_numpy(), np.arange(len(episode)) / 15, rtol=0, atol=2e-6)
    return {
        "export_fields": shard.schema_arrow.names, "episode": 0, "rows": len(episode),
        "action_shape": np.shape(episode["action"].to_pylist()),
        "state_shape": np.shape(episode["observation.state"].to_pylist()),
        "last_time_s": episode["timestamp"][-1].as_py(),
    }


def geometry():
    url = ("https://raw.githubusercontent.com/epfl-lasa/Learn_Equality_Constraints_from_Demonstrations/"
           "3e12fc5d2475b67bf8fc32c790085a2e7bcd1708/datasets/real_iiwa/tasks/RealKuka/processed/train_sets/"
           "human_demo_paper_toolz_arc3mm_cropped_v001.npz")
    data = download(url, "adf7012b48a26ecaa84d07358bb9d96311c005e4e4d40200dc87deada9cde113")
    with np.load(io.BytesIO(data), allow_pickle=False) as sample:
        return {key: sample[key].shape for key in ("source_x", "x", "tool_z", "target_tool_z", "monotonic_time_ns")}


if __name__ == "__main__":
    audits = {"droid": droid, "shared": shared, "harmonic": harmonic, "copilot": copilot, "geometry": geometry}
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", nargs="?", choices=["all", *audits], default="all")
    selected = parser.parse_args().source
    for name, audit in audits.items():
        if selected in ("all", name):
            print(json.dumps({name: audit()}, ensure_ascii=False), flush=True)
