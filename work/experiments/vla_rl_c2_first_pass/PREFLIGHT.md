# C2 first-pass gate audit

- Frozen before payload inspection: 2026-10-21 KST.
- Purpose: close the first feasibility/identifiability decision; this is not a policy-effect experiment.
- Research contract: [C2 protocol](../../research_candidates/2026-10-20_vla_rl/C2_PROTOCOL.md).

## Scope and budget

1. Verify all eight task inventories and available episode/seed metadata at dataset revision `bbb1e266ed585f1557773de5a3f1e3b4cd944f97`.
2. Inspect actual payloads from **training tasks only**, initially episodes 0, 24, and 49 per task. Selection is fixed before reading outcomes. Expand only if needed to resolve a gate. No model training or hyperparameter selection uses holdout payloads.
3. Check recorded keys, time alignment, finite joint/state values, and whether source/waypoint object poses and final-state predicates can be reconstructed without unvalidated perception or replay. Keep unknown labels unknown. Filename/collector success does not prove each C2 predicate.
4. Inspect instruction/seed metadata and planner traces. Do not execute arbitrary pickle globals. Check whether all relevant initial object states are available before claiming matched scenes or no leakage.
5. Probe the **reference** SAPIEN/mplib/cuRobo route in Docker. A package/platform failure closes that native route, not all possible future CPU ports. Do not replace the benchmark with a toy policy.

Data/dependencies/source caches remain inside a task-specific Docker container. Host retains authored probe scripts and small evidence reports only. Container limit: 4 CPU, 4 GiB RAM; payload cap 1 GiB total and 128 MiB per file, with range reads preferred if required. Each network call has a timeout; no broad training sweep, weights download, or simulator asset download before the native gate passes.

## Decision rules fixed before payload inspection

- **Proceed to policy comparison** only if labels, actual train/evaluation grouping, a compatible native checkpoint, and an executable simulator are established.
- If object trajectories/constraint evidence cannot be recovered, close G0 as **exact predicate labels unavailable through the inspected release without additional replay/annotation**. This does not claim RGB is intrinsically uninformative. Joint/EEF trajectories are not substituted for manipulated-object trajectories.
- If the reference native runtime is unavailable, close G1 as **failed for the tested configuration**, leaving policy competence and RL effects unmeasured.
- If factual data are successful demonstrations only, do not claim goal-only versus complete reward contrast without verified violations or valid training-only instruction relabels.
- On failure of these gates, give an explicit go/no-go investment recommendation based on literature overlap, evidence availability, and local cost. A negative investment recommendation does not falsify the scientific hypothesis.
