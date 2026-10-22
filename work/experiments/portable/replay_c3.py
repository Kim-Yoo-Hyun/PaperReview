"""Docker-only replay of saved C3 score diagnostics, without models or downloads."""
import argparse
import hashlib
import json
import platform
from pathlib import Path

import numpy as np

EXPECTED_RAW = "99c6fef4fab42610c3839a6dd6ac57db0169002a88af588a848bdfff32d612e4"
EXPECTED_REFERENCES = {
    "logits_analysis.json": "e019ac32f213de9d1920021eff3ee739b7ebb4dd090733185d77e0faccf8f7ff",
    "tail_audit.json": "5459a445259213bca572f0290b952df768708d3f5dcce3d2907d320e1ed37893",
}


def checked_hash(path, expected):
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != expected:
        raise ValueError(f"Evidence hash mismatch: {path.name}")
    return digest


def probabilities(logits, temperature):
    z = logits.astype(np.float64) / temperature
    p = np.exp(z - z.max(axis=-1, keepdims=True))
    return p / p.sum(axis=-1, keepdims=True)


def scores(p, labels):
    """Exact finite-sum traces; no reward weighting or backbone gradient."""
    cp = np.bincount(labels, weights=p, minlength=2)
    if np.any(cp <= 0):
        raise ValueError("Both command classes must have positive probability")
    q = np.stack([p * (labels == c) / cp[c] for c in range(2)])
    raw_score = np.eye(p.size) - p
    class_score = q - p
    raw = float(p @ np.square(raw_score).sum(axis=1))
    marginal = float(cp @ np.square(class_score).sum(axis=1))
    if marginal > raw + 1e-12:
        raise ValueError("Marginal score trace exceeds raw trace")
    alias = p.copy()
    for c in range(2):
        ix = np.flatnonzero(labels == c)
        alias[ix[p[ix].argmax()]] = 0
    return raw, marginal, float(alias.sum())


def analyze(raw):
    expected = {"action_logits": (16, 56, 256), "gripper_hidden": (16, 8, 4096),
                "action_hidden_squared_norm": (16, 56)}
    for key, shape in expected.items():
        if raw[key].shape != shape or not np.isfinite(raw[key]).all():
            raise ValueError(f"Invalid evidence array: {key}")
    # Checkpoint-specific mapping from original audit_tail.py's native decoder audit.
    # Ordered action tokens 31744..31999; indices 0..64 vs 65..255.
    # This is NOT a generic mapping for other VLA checkpoints/controllers.
    labels = (np.arange(256) >= 65).astype(int)
    hidden = raw["gripper_hidden"].astype(np.float64)
    all_norm = raw["action_hidden_squared_norm"].astype(np.float64)
    output = {}
    for temperature in (1.0, 1.6):
        all_p = probabilities(raw["action_logits"], temperature)
        rows = []
        for obs in range(16):
            for slot in range(8):
                a, b, alias = scores(all_p[obs, 7 * slot + 6], labels)
                scale = float(hidden[obs, slot] @ hidden[obs, slot]) / temperature**2
                rows.append((a, b, a * scale, b * scale, alias, slot))
        arr = np.array(rows)
        total = arr.sum(axis=0)
        all_trace = np.sum(all_p * (1 - 2 * all_p + np.square(all_p).sum(-1, keepdims=True)), axis=-1)
        joint = float((all_trace * all_norm / temperature**2).sum())
        removed = arr[:, 2] - arr[:, 3]
        output[str(temperature)] = {
            "aggregate_score_trace_reduction_percent": 100 * (total[0] - total[1]) / total[0],
            "aggregate_head_score_trace_reduction_percent": 100 * (total[2] - total[3]) / total[2],
            "gripper_share_of_factorized_chunk_head_score_trace_percent": 100 * total[2] / joint,
            "factorized_chunk_head_score_trace_reduction_percent": 100 * (total[2] - total[3]) / joint,
            "mean_alias_mass": float(arr[:, 4].mean()),
            "alias_mass_above_0.01_count": int((arr[:, 4] > .01).sum()),
            "last_slot_share_of_removed_head_score_trace": float(removed[arr[:, 5] == 7].sum() / removed.sum()),
        }
    return output


def verify(actual, primary, tail):
    comparisons = 0
    for temperature, metrics in actual.items():
        for key, value in metrics.items():
            if key == "mean_alias_mass":
                expected = primary["temperatures"][temperature]["summary"]["alias_mass"]["mean"]
            elif key == "alias_mass_above_0.01_count":
                expected = tail["temperatures"][temperature]["alias_threshold_counts"]["0.01"]
            elif key == "last_slot_share_of_removed_head_score_trace":
                expected = tail["temperatures"][temperature][key]
            else:
                expected = primary["temperatures"][temperature][key]
            if not np.isclose(value, expected, rtol=1e-9, atol=1e-10):
                raise ValueError(f"Oracle mismatch: T={temperature}, {key}: {value} != {expected}")
            comparisons += 1
    return comparisons


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence", type=Path, default=Path("/evidence"))
    args = parser.parse_args()
    p = args.evidence
    digest = checked_hash(p / "native_logits.npz", EXPECTED_RAW)
    for name, expected in EXPECTED_REFERENCES.items():
        checked_hash(p / name, expected)
    with np.load(p / "native_logits.npz", allow_pickle=False) as raw:
        result = analyze(raw)
    checks = verify(result, json.loads((p / "logits_analysis.json").read_text()),
                    json.loads((p / "tail_audit.json").read_text()))
    print(json.dumps({"status": "PASS", "scope": "saved-logit score diagnostics only",
                      "raw_sha256": digest, "reference_comparisons": checks,
                      "numpy": np.__version__, "architecture": platform.machine(),
                      "robot_rollouts": 0, "model_forward_calls": 0, "training_updates": 0,
                      "temperatures": result}, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
