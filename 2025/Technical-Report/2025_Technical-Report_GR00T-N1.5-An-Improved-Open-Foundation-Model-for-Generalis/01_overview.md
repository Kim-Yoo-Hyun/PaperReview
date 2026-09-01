# GR00T N1.5: An Improved Open Foundation Model for Generalist Humanoid Robots

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: official NVIDIA technical page body (no public PDF identified) checked on 2026-09-02 (1 source page(s); official NVIDIA technical page body (no public PDF identified)); canonical paper source: https://research.nvidia.com/labs/gear/gr00t-n1_5/.
> Body source: https://research.nvidia.com/labs/gear/gr00t-n1_5/. Reading tracker status/evidence was not changed.

> Evidence boundary: selected official source-body statements; no PDF was identified at review time.

- Year/Venue: 2025 / Technical Report
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, humanoid, foundation model, Flow Matching, world model, robot data
- Official paper: https://research.nvidia.com/labs/gear/gr00t-n1_5/
- Full-text retrieval: https://research.nvidia.com/labs/gear/gr00t-n1_5/
- Code/Project: https://github.com/NVIDIA/Isaac-GR00T
- Paper type: theory_or_foundation
- Source audit: official NVIDIA technical page body (no public PDF identified) checked on 2026-09-02 (1 source page(s); official NVIDIA technical page body (no public PDF identified))

## Why This Paper Is Here

VLA and generalist robot policies의 humanoid 문제를 이해하기 위해 읽는다. 본문은 Novel object generalization performance.를 문제로 두고, We introduce GR00T N1.5, an upgraded version of the GR00T N1 foundation model for humanoid robots.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots - extractive body cue:** GR00T N1.5 Policy rollout with language prompt: "Pick the apple from table to plate"
- **p. 1 / GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots - extractive body cue:** We introduce GR00T N1.5, an upgraded version of the GR00T N1 foundation model for humanoid robots.
- **p. 1 / GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots - extractive body cue:** With several architecture, data and modeling improvements, we find that N1.5 outperforms N1 on both simulated manipulation benchmarks and on the real GR-1 robot, detailed ...
- **p. 1 / GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots - extractive body cue:** We expect users of N1.5 should observe better performance compared to N1, in particular improved generalization and better language following ability.
- **p. 1 / Model and Data Updates - extractive body cue:** As with N1, GR00T N1.5 uses an NVIDIA Eagle VLM to encode text and visual observations.
- **p. 1 / Learning to manipulate novel objects from human ego videos - extractive body cue:** Novel object generalization performance.
- **p. 1 / Model and Data Updates - extractive body cue:** We found that these modifications greatly improved language following and generalization.

## Core Idea

- **p. 1 / GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots - extractive body cue:** We introduce GR00T N1.5, an upgraded version of the GR00T N1 foundation model for humanoid robots.
- **p. 1 / Learning to manipulate novel objects from human ego videos - extractive body cue:** As shown in the FLARE project , future latent representation alignment enables learning directly from human ego videos.
- **p. 1 / Joint Policy Learning and World Modeling Objective - extractive body cue:** We used FLARE loss coefficient 0.2 for both pretraining and posttraining.
- **p. 1 / Model and Data Updates - extractive body cue:** The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions.

## Observation, State, and Output Interface

| Role | official source body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions. | proprioception, reference pose/motion, visual or language command | p. 1 (Model and Data Updates), p. 1 (GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots) |
| State/latent | vision-language, embeddings, VLM, then, cross-attended, DiT, processes, state, noised, actions, GR00T, Policy | whole-body pose, balance/contact state와 skill/mode | p. 1 (Model and Data Updates), p. 1 (GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots), p. 1 (Joint Policy Learning and World Modeling Objective) |
| Output/action | GR00T N1.5 Policy rollout with language prompt: "Pick the apple from table to plate" | joint/whole-body action, motion target 또는 task trajectory | p. 1 (GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots) |
| Objective/outcome | We attribute these improvements to the improved grounding capabilities, usage of the FLARE loss and the diverse data from DreamGen. | tracking, balance, skill/task success와 recovery | p. 1 (Post-training on Unitree G1), p. 1 (Joint Policy Learning and World Modeling Objective) |

## Main Claims and Actual Contribution

- **p. 1 / GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots - extractive body cue:** We introduce GR00T N1.5, an upgraded version of the GR00T N1 foundation model for humanoid robots.
- **p. 1 / Learning to manipulate novel objects from human ego videos - extractive body cue:** As shown in the FLARE project , future latent representation alignment enables learning directly from human ego videos.
- **p. 1 / Post-training on Unitree G1 - extractive body cue:** It achieves higher success rate, can use more diverse data sources, and has significantly improved language following capabilities.
- **p. 1 / Architecture validation - extractive body cue:** We find that the N1.5 architecture achieves significantly higher success rates on both benchmarks, indicating stronger language-conditioned control ability.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 1 (Post-training on Unitree G1), p. 1 (Architecture validation) |
| Embodiment/environment | In order to tune the model architecture for N1.5, we trained policies from scratch on two sim robot benchmarks requiring language following: Language Table and a set of five simulated GR-1 tasks ... | hardware/simulator version and reset protocol | p. 1 (Architecture validation), p. 1 (Post-training on Unitree G1) |
| Dataset/benchmark | In order to tune the model architecture for N1.5, we trained policies from scratch on two sim robot benchmarks requiring language following: Language Table and a set of five simulated GR-1 tasks ... | role, split, size and leakage | p. 1 (Architecture validation), p. 1 (Post-training on Unitree G1) |
| Metric | We find that GR00T N1.5 achieved a 38.3% success rate across 12 DreamGen tasks, versus 13.1% for GR00T N1. | definition, denominator, direction and uncertainty | p. 1 (Generalization to novel behaviors using Neural Trajectories), p. 1 (Post-training on Unitree G1) |
| Baseline/ablation | We expect users of N1.5 should observe better performance compared to N1, in particular improved generalization and better language following ability. | fair input/data/compute/action matching | p. 1 (GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots), p. 1 (GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots), p. 1 (Joint Policy Learning and World Modeling Objective) |

## Explicit Limitations and Failure Boundary

- **p. 1 / Generalization to novel behaviors using Neural Trajectories - extractive body cue:** Although these new verbs can be considered "zero-shot" in the sense that we never collected teleoperation data for these tasks, we still train explicitly on ...
- **p. 1 / Model and Data Updates - extractive body cue:** The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions.

## Why Read It

VLA and generalist robot policies의 humanoid 문제를 이해하기 위해 읽는다. 본문은 Novel object generalization performance.를 문제로 두고, We introduce GR00T N1.5, an upgraded version of the GR00T N1 foundation model for humanoid robots.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (Learning to manipulate novel objects from human ego videos), p. 1 (Model and Data Updates), p. 1 (Joint Policy Learning and World Modeling Objective), p. 1 (Model and Data Updates), p. 1 (Post-training on Unitree G1), p. 1 (Architecture validation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
