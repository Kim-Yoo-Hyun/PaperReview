"""D1 formulation diagnostic, stdlib only. Run inside Docker, not a VLA test."""
import hashlib
import json
import random
from fractions import Fraction as F
from pathlib import Path


def observe(x, bp, bv):
    return (x + bp, x + bv)


def main():
    # Freeze before execution: 4 offsets x 3 history lengths x 8 seeds.
    # Delta-position dynamics; physical world goal=0; no trusted initial pose,
    # visual world landmark, hard stop, or torque/contact signal is available.
    counts = {k: 0 for k in ["pairs", "identical_histories", "different_goal_actions",
                            "anchor_resolves", "relative_goal_actions_equal",
                            "single_fault_innovation_separable", "compound_aliases",
                            "physical_displacement_aliases_at_onset"]}
    max_gap = F(0)
    for delta in map(F, [1, 2, 4, 8]):
        for horizon in [1, 4, 16]:
            for seed in range(8):
                rng = random.Random(seed)
                xa, xb = F(0), delta
                ha, hb = [], []
                # A: proprio offset only. B: camera offset only, different x0.
                for _ in range(horizon):
                    command = F(rng.randint(-3, 3))
                    ha.append((command, *observe(xa, delta, F(0))))
                    hb.append((command, *observe(xb, F(0), -delta)))
                    xa += command
                    xb += command
                ha.append(observe(xa, delta, F(0)))
                hb.append(observe(xb, F(0), -delta))
                counts["pairs"] += 1
                counts["identical_histories"] += ha == hb
                counts["different_goal_actions"] += (-xa != -xb)
                max_gap = max(max_gap, abs(xa - xb))
                # A known, stationary world landmark L=0 in the SAME camera
                # supplies l=L+bv. x=v-l, then bp=p-x. This is extra evidence.
                for x, bp, bv in [(xa, delta, F(0)), (xb, F(0), -delta)]:
                    p, v = observe(x, bp, bv)
                    landmark = bv
                    assert v - landmark == x
                    assert p - (v - landmark) == bp
                counts["anchor_resolves"] += 1
                # If target and robot undergo the same translation, relative
                # goal control needs no fault identity despite state ambiguity.
                target_a, target_b = F(10), F(10) + delta
                counts["relative_goal_actions_equal"] += target_a - xa == target_b - xb
                # With TRUSTED pre-onset state, synchronized p/v, and exactly
                # one additive fault, subtract command from observed increments.
                signatures = {"policy_state": (delta, F(0)),
                              "vision": (F(0), delta),
                              "actuation": (delta, delta)}
                counts["single_fault_innovation_separable"] += len(set(signatures.values())) == 3
                # Two simultaneous observation offsets alias an actuation step.
                counts["compound_aliases"] += (
                    signatures["policy_state"][0] + signatures["vision"][0],
                    signatures["policy_state"][1] + signatures["vision"][1]
                ) == signatures["actuation"]
                counts["physical_displacement_aliases_at_onset"] += (delta, delta) == signatures["actuation"]
    assert all(v == 96 for v in counts.values()), counts
    result = {"kind": "synthetic_identifiability_counterexample", "version": 1,
              "frozen_grid": {"offset_mm": [1, 2, 4, 8], "history_steps": [1, 4, 16], "seeds": list(range(8))},
              "counts": counts, "maximum_required_action_gap_mm": float(max_gap),
              "interpretation": "No-anchor absolute-goal fault identification is not generally possible; a trusted anchor resolves this toy exactly; relative-goal control may not need identification; single-fault innovations already admit a simple residual baseline.",
              "not_established": ["VLA input use", "physical prevalence", "real robot observability", "policy improvement", "new algorithm novelty"],
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
