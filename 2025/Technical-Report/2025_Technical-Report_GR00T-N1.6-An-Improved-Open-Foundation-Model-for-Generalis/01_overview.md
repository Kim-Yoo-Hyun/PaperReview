# GR00T N1.6: An Improved Open Foundation Model for Generalist Humanoid Robots

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: official NVIDIA technical page body (no public PDF identified) checked on 2026-09-02 (1 source page(s); official NVIDIA technical page body (no public PDF identified)); canonical paper source: https://research.nvidia.com/labs/gear/gr00t-n1_6/.
> Body source: https://research.nvidia.com/labs/gear/gr00t-n1_6/. Reading tracker status/evidence was not changed.

> Evidence boundary: selected official source-body statements; no PDF was identified at review time.

- Year/Venue: 2025 / Technical Report
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, humanoid, foundation model, whole-body control, long-horizon, robot data
- Official paper: https://research.nvidia.com/labs/gear/gr00t-n1_6/
- Full-text retrieval: https://research.nvidia.com/labs/gear/gr00t-n1_6/
- Code/Project: https://github.com/NVIDIA/Isaac-GR00T
- Paper type: theory_or_foundation
- Source audit: official NVIDIA technical page body (no public PDF identified) checked on 2026-09-02 (1 source page(s); official NVIDIA technical page body (no public PDF identified))

## Why This Paper Is Here

VLA and generalist robot policies의 humanoid 문제를 이해하기 위해 읽는다. 본문은 Multi-task language following and out-of-distribution task generalization continue to be challenging for current VLA models.를 문제로 두고, We introduce GR00T N1.6, an improved version of the GR00T N1.5 foundation model for humanoid robots.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / GR00T N1.6 An Improved Open Foundation Model for Generalist Humanoid Robots - extractive body cue:** We introduce GR00T N1.6, an improved version of the GR00T N1.5 foundation model for humanoid robots.
- **p. 1 / GR00T N1.6 An Improved Open Foundation Model for Generalist Humanoid Robots - extractive body cue:** With several architecture, data and modeling improvements, we find that N1.6 outperforms N1.5 on both simulated manipulation benchmarks and on real bimanual YAM, Agibot Genie-1 ...
- **p. 1 / GR00T N1.6 An Improved Open Foundation Model for Generalist Humanoid Robots - extractive body cue:** We expect users of N1.6 should observe better post-training performance compared to N1.5.
- **p. 1 / Model and Data Improvements - extractive body cue:** Base VLM: We use an internal NVIDIA Cosmos-2B VLM variant.
- **p. 1 / Model and Data Improvements - extractive body cue:** The VLM supports flexible resolution and can encode images in their native aspect ratio without padding.
- **p. 1 / Unitree G1 Locomanipulation Demo Videos - extractive body cue:** Multi-task language following and out-of-distribution task generalization continue to be challenging for current VLA models.
- **p. 1 / Unitree G1 Locomanipulation Demo Videos - extractive body cue:** More fine-grained subtask annotation can improve language following, but not yet reaching robust generalization.

## Core Idea

- **p. 1 / GR00T N1.6 An Improved Open Foundation Model for Generalist Humanoid Robots - extractive body cue:** We introduce GR00T N1.6, an improved version of the GR00T N1.5 foundation model for humanoid robots.
- **p. 1 / Model and Data Improvements - extractive body cue:** Predicts state-relative action chunks for most embodiments, rather than absolute joint angles or EEF positions.

## Observation, State, and Output Interface

| Role | official source body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Predicts state-relative action chunks for most embodiments, rather than absolute joint angles or EEF positions. | proprioception, reference pose/motion, visual or language command | p. 1 (Model and Data Improvements), p. 1 (Model and Data Improvements) |
| State/latent | Predicts, state-relative, action, chunks, most, embodiments, rather, absolute, joint, angles, EEF, positions | whole-body pose, balance/contact state와 skill/mode | p. 1 (Model and Data Improvements), p. 1 (Model and Data Improvements), p. 1 (GR00T N1.6 An Improved Open Foundation Model for Generalist Humanoid Robots) |
| Output/action | The VLM is trained on both general vision-language tasks and embodied reasoning tasks like next action prediction. | joint/whole-body action, motion target 또는 task trajectory | p. 1 (Model and Data Improvements) |
| Objective/outcome | The VLM is trained on both general vision-language tasks and embodied reasoning tasks like next action prediction. | tracking, balance, skill/task success와 recovery | p. 1 (Model and Data Improvements) |

## Main Claims and Actual Contribution

- **p. 1 / GR00T N1.6 An Improved Open Foundation Model for Generalist Humanoid Robots - extractive body cue:** We introduce GR00T N1.6, an improved version of the GR00T N1.5 foundation model for humanoid robots.
- **p. 1 / Unitree G1 Locomanipulation Demo Videos - extractive body cue:** When scaling up real-world experiments, we incorporate various lessons learned from the robot learning community to improve model success rates during rollouts.
- **p. 1 / GR00T N1.6 An Improved Open Foundation Model for Generalist Humanoid Robots - extractive body cue:** With several architecture, data and modeling improvements, we find that N1.6 outperforms N1.5 on both simulated manipulation benchmarks and on real bimanual YAM, Agibot Genie-1 ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 1 (Unitree G1 Locomanipulation Demo Videos), p. 1 (GR00T N1.6 An Improved Open Foundation Model for Generalist Humanoid Robots) |
| Embodiment/environment | In the following robot experiments, we further post-train on small task-specific datasets; typically 10K-30K steps with global batch size 1K or less. | hardware/simulator version and reset protocol | p. 1 (Unitree G1 Locomanipulation Demo Videos), p. 1 (Unitree G1 Locomanipulation Demo Videos) |
| Dataset/benchmark | In the following robot experiments, we further post-train on small task-specific datasets; typically 10K-30K steps with global batch size 1K or less. | role, split, size and leakage | p. 1 (Unitree G1 Locomanipulation Demo Videos), p. 1 (Unitree G1 Locomanipulation Demo Videos) |
| Metric | When scaling up real-world experiments, we incorporate various lessons learned from the robot learning community to improve model success rates during rollouts. | definition, denominator, direction and uncertainty | p. 1 (Unitree G1 Locomanipulation Demo Videos), p. 1 (Unitree G1 Locomanipulation Demo Videos) |
| Baseline/ablation | We expect users of N1.6 should observe better post-training performance compared to N1.5. | fair input/data/compute/action matching | p. 1 (GR00T N1.6 An Improved Open Foundation Model for Generalist Humanoid Robots), p. 1 (GR00T N1.6 An Improved Open Foundation Model for Generalist Humanoid Robots), p. 1 (Model and Data Improvements) |

## Explicit Limitations and Failure Boundary

- **p. 1 / Unitree G1 Locomanipulation Demo Videos - extractive body cue:** More fine-grained subtask annotation can improve language following, but not yet reaching robust generalization.
- **p. 1 / Unitree G1 Locomanipulation Demo Videos - extractive body cue:** Test-time and train-time RTC provide performance boosts to motion smoothness and robustness during asynchronous rollouts.

## Why Read It

VLA and generalist robot policies의 humanoid 문제를 이해하기 위해 읽는다. 본문은 Multi-task language following and out-of-distribution task generalization continue to be challenging for current VLA models.를 문제로 두고, We introduce GR00T N1.6, an improved version of the GR00T N1.5 foundation model for humanoid robots.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (Unitree G1 Locomanipulation Demo Videos), p. 1 (Unitree G1 Locomanipulation Demo Videos), p. 1 (GR00T N1.6 An Improved Open Foundation Model for Generalist Humanoid Robots), p. 1 (Model and Data Improvements), p. 1 (Unitree G1 Locomanipulation Demo Videos), p. 1 (GR00T N1.6 An Improved Open Foundation Model for Generalist Humanoid Robots) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
