# GR00T N1.5: An Improved Open Foundation Model for Generalist Humanoid Robots

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (3 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://research.nvidia.com/labs/gear/gr00t-n1_5/. PDF provenance note: official NVIDIA technical page rendered to a task-scoped PDF snapshot; no author-supplied publication PDF identified.
> PDF retrieval source: https://research.nvidia.com/labs/gear/gr00t-n1_5/. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / Technical Report
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, humanoid, foundation model, Flow Matching, world model, robot data
- Official paper: https://research.nvidia.com/labs/gear/gr00t-n1_5/
- Full-text retrieval: https://research.nvidia.com/labs/gear/gr00t-n1_5/
- Code/Project: https://github.com/NVIDIA/Isaac-GR00T
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (3 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 humanoid 문제를 이해하기 위해 읽는다. 본문은 We expect users of N1.5 should observe better performance compared to N1, in particular improved generalization and better language following ability.를 문제로 두고, We introduce GR00T N1.5, an upgraded version of the GR00T N1 foundation model for humanoid robots.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Introduction - extractive body cue:** We introduce GR00T N1.5, an upgraded version of the GR00T N1 foundation model for humanoid robots.
- **p. 1 / Introduction - extractive body cue:** With several architecture, data and modeling improvements, we find that N1.5 outperforms N1 on both simulated manipulation benchmarks and on the real GR-1 robot, detailed ...
- **p. 1 / Introduction - extractive body cue:** We expect users of N1.5 should observe better performance compared to N1, in particular improved generalization and better language following ability.
- **p. 1 / Architecture - extractive body cue:** We found that these modifications greatly improved language following and generalization.
- **p. 2 / Generalization to novel behaviors using Neural Trajectories - extractive body cue:** GR00T N1 showed only weak generalization to new verbs, only repeating the tasks contained in pretraining
- **p. 2 / Learning to manipulate novel objects from human ego videos - extractive body cue:** To evaluate the model's generalization ability, we evaluate pick and place performance using a set of 10 novel objects not seen during pretraining.
- **p. 3 / Post-training on Unitree G1 - extractive body cue:** We observe that the post-trained GR00T N1.5 achieves much higher success rate than N1 for previously seen objects (toy fruits seen in the GR-1 pretraining ...

## Core Idea

- **p. 1 / Introduction - extractive body cue:** We introduce GR00T N1.5, an upgraded version of the GR00T N1 foundation model for humanoid robots.
- **p. 2 / Learning to manipulate novel objects from human ego videos - extractive body cue:** Novel Objects As shown in the FLARE project, future latent representation alignment enables learning directly from human ego videos.
- **p. 2 / Learning to manipulate novel objects from human ego videos - extractive body cue:** This allows learning to manipulate novel objects from human videos and minimal robot demonstrations.
- **p. 3 / Post-training on Unitree G1 - extractive body cue:** Model / GR00T N1, 1K Demos / GR00T N1.5, 1K Demos / GR00T N1.5, 1K Demos Task / Place 1 of 2 fruits onto plate; ...
- **p. 1 / Architecture - extractive body cue:** We used FLARE loss coefficient 0.2 for both pretraining and posttraining.
- **p. 1 / Architecture - extractive body cue:** The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions.
- **p. 2 / Architecture validation - extractive body cue:** We find that the N1.5 architecture achieves significantly higher success rates on both benchmarks, indicating stronger language-conditioned control ability.
- **p. 2 / Data-limited post-training in simulated environments - extractive body cue:** Following the GR00T N1 evaluation protocol, we evaluate N1.5's performance in data-limited post-training.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions. | proprioception, reference pose/motion, visual or language command | p. 1 (Architecture), p. 1 (Architecture) |
| State/latent | vision-language, embeddings, VLM, then, cross-attended, DiT, processes, state, noised, actions, find, adding | whole-body pose, balance/contact state와 skill/mode | p. 1 (Architecture), p. 1 (Architecture), p. 2 (Real GR-1 language following) |
| Output/action | We find that adding FLARE both improves policy performance and unlocks the ability to learn from human videos. | joint/whole-body action, motion target 또는 task trajectory | p. 1 (Architecture), p. 2 (Real GR-1 language following), p. 2 (Learning to manipulate novel objects from human ego videos) |
| Objective/outcome | Joint Policy Learning and World Modeling Objective | tracking, balance, skill/task success와 recovery | p. 1 (Architecture), p. 1 (Architecture), p. 3 (Post-training on Unitree G1) |

## Main Claims and Actual Contribution

- **p. 1 / Introduction - extractive body cue:** We introduce GR00T N1.5, an upgraded version of the GR00T N1 foundation model for humanoid robots.
- **p. 2 / Learning to manipulate novel objects from human ego videos - extractive body cue:** Novel Objects As shown in the FLARE project, future latent representation alignment enables learning directly from human ego videos.
- **p. 2 / Learning to manipulate novel objects from human ego videos - extractive body cue:** This allows learning to manipulate novel objects from human videos and minimal robot demonstrations.
- **p. 3 / Post-training on Unitree G1 - extractive body cue:** Model / GR00T N1, 1K Demos / GR00T N1.5, 1K Demos / GR00T N1.5, 1K Demos Task / Place 1 of 2 fruits onto plate; ...
- **p. 3 / Discussion - extractive body cue:** It achieves higher success rate, can use more diverse data sources, and has significantly improved language following capabilities.
- **p. 2 / Architecture validation - extractive body cue:** We find that the N1.5 architecture achieves significantly higher success rates on both benchmarks, indicating stronger language-conditioned control ability.
- **p. 2 / Real GR-1 language following - extractive body cue:** Setting / GR00T N1 / GR00T N1.5 Language following rate / 46.6% / 93.3% Overall success rate / 43.3% / 83.0% We find that N1.5 ...
- **p. 3 / Generalization to novel behaviors using Neural Trajectories - extractive body cue:** We find that GR00T N1.5 achieved a 38.3% success rate across 12 DreamGen tasks, versus 13.1% for GR00T N1.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 3 (Discussion), p. 2 (Architecture validation) |
| Embodiment/environment | With several architecture, data and modeling improvements, we find that N1.5 outperforms N1 on both simulated manipulation benchmarks and on the real GR-1 robot, detailed below. | hardware/simulator version and reset protocol | p. 1 (Introduction), p. 3 (Post-training on Unitree G1) |
| Dataset/benchmark | Demonstrations using a novel object, captured from a GoPro (left) and the GR-1 robot (right). | role, split, size and leakage | p. 1 (Introduction), p. 3 (Post-training on Unitree G1), p. 2 (Learning to manipulate novel objects from human ego videos), p. 2 (Learning to manipulate novel objects from human ego videos) |
| Metric | We find that the N1.5 architecture achieves significantly higher success rates on both benchmarks, indicating stronger language-conditioned control ability. | definition, denominator, direction and uncertainty | p. 2 (Architecture validation), p. 2 (Real GR-1 language following), p. 3 (Generalization to novel behaviors using Neural Trajectories) |
| Baseline/ablation | We expect users of N1.5 should observe better performance compared to N1, in particular improved generalization and better language following ability. | fair input/data/compute/action matching | p. 1 (Introduction), p. 1 (Introduction), p. 1 (Architecture) |

## Explicit Limitations and Failure Boundary

- **p. 3 / Generalization to novel behaviors using Neural Trajectories - extractive body cue:** Although these new verbs can be considered "zero-shot" in the sense that we never collected teleoperation data for these tasks, we still train explicitly on ...
- **p. 1 / Architecture - extractive body cue:** The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions.

## Why Read It

VLA and generalist robot policies의 humanoid 문제를 이해하기 위해 읽는다. 본문은 We expect users of N1.5 should observe better performance compared to N1, in particular improved generalization and better language following ability.를 문제로 두고, We introduce GR00T N1.5, an upgraded version of the GR00T N1 foundation model for humanoid robots.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (Introduction), p. 1 (Architecture), p. 2 (Generalization to novel behaviors using Neural Trajectories), p. 2 (Learning to manipulate novel objects from human ego videos), p. 3 (Post-training on Unitree G1), p. 1 (Architecture) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
