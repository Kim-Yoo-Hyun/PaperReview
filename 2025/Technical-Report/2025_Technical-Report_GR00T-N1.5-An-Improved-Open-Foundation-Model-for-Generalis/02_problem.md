# Problem - GR00T N1.5: An Improved Open Foundation Model for Generalist Humanoid Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (3 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://research.nvidia.com/labs/gear/gr00t-n1_5/; PDF retrieval source: https://research.nvidia.com/labs/gear/gr00t-n1_5/. PDF provenance note: official NVIDIA technical page rendered to a task-scoped PDF snapshot; no author-supplied publication PDF identified. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (Introduction), p. 1 (Architecture), p. 2 (Generalization to novel behaviors using Neural Trajectories), p. 2 (Learning to manipulate novel objects from human ego videos), p. 3 (Post-training on Unitree G1)): We expect users of N1.5 should observe better performance compared to N1, in particular improved generalization and better language following ability.

## PDF Body Digest

- **p. 1 / Introduction - extractive body cue:** We introduce GR00T N1.5, an upgraded version of the GR00T N1 foundation model for humanoid robots.
- **p. 1 / Introduction - extractive body cue:** With several architecture, data and modeling improvements, we find that N1.5 outperforms N1 on both simulated manipulation benchmarks and on the real GR-1 robot, detailed ...
- **p. 1 / Introduction - extractive body cue:** We expect users of N1.5 should observe better performance compared to N1, in particular improved generalization and better language following ability.
- **p. 1 / Architecture - extractive body cue:** We found that these modifications greatly improved language following and generalization.
- **p. 2 / Generalization to novel behaviors using Neural Trajectories - extractive body cue:** GR00T N1 showed only weak generalization to new verbs, only repeating the tasks contained in pretraining
- **p. 2 / Learning to manipulate novel objects from human ego videos - extractive body cue:** To evaluate the model's generalization ability, we evaluate pick and place performance using a set of 10 novel objects not seen during pretraining.
- **p. 3 / Post-training on Unitree G1 - extractive body cue:** We observe that the post-trained GR00T N1.5 achieves much higher success rate than N1 for previously seen objects (toy fruits seen in the GR-1 pretraining ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | We expect users of N1.5 should observe better performance compared to N1, in particular improved generalization and better language following ability. | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions. | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF body |
| State / latent | vision-language, embeddings, VLM, then, cross-attended, DiT, processes, state, noised, actions | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | Setting, GR00T, Language, following, rate, Overall, success, find | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: vision-language, embeddings, VLM, then, cross-attended, DiT, processes, state, noised, actions | p. 1 (Architecture), p. 1 (Architecture), p. 2 (Real GR-1 language following) |
| Decision / output variable | joint/whole-body action; body terms: introduce, GR00T, upgraded, version, foundation, model, humanoid, robots | p. 1 (Introduction), p. 2 (Learning to manipulate novel objects from human ego videos), p. 2 (Learning to manipulate novel objects from human ego videos) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: Joint, Policy, Learning, World, Modeling, Objective, FLARE, loss | p. 1 (Architecture), p. 1 (Architecture) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (Architecture), p. 1 (Architecture), p. 3 (Post-training on Unitree G1) |
| Success / guarantee | motion/task success and recovery | p. 2 (Architecture validation), p. 2 (Real GR-1 language following), p. 3 (Generalization to novel behaviors using Neural Trajectories) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / Architecture - extractive body cue:** We found that these modifications greatly improved language following and generalization.
- **p. 2 / Generalization to novel behaviors using Neural Trajectories - extractive body cue:** GR00T N1 showed only weak generalization to new verbs, only repeating the tasks contained in pretraining
- **p. 2 / Learning to manipulate novel objects from human ego videos - extractive body cue:** To evaluate the model's generalization ability, we evaluate pick and place performance using a set of 10 novel objects not seen during pretraining.
- **p. 3 / Post-training on Unitree G1 - extractive body cue:** We observe that the post-trained GR00T N1.5 achieves much higher success rate than N1 for previously seen objects (toy fruits seen in the GR-1 pretraining ...

## What the Paper Changes

PDF body contribution framing (p. 1 (Introduction), p. 2 (Learning to manipulate novel objects from human ego videos), p. 2 (Learning to manipulate novel objects from human ego videos), p. 3 (Post-training on Unitree G1)): We introduce GR00T N1.5, an upgraded version of the GR00T N1 foundation model for humanoid robots.

- **p. 2 / Learning to manipulate novel objects from human ego videos - extractive body cue:** Novel Objects As shown in the FLARE project, future latent representation alignment enables learning directly from human ego videos.
- **p. 2 / Learning to manipulate novel objects from human ego videos - extractive body cue:** This allows learning to manipulate novel objects from human videos and minimal robot demonstrations.
- **p. 3 / Post-training on Unitree G1 - extractive body cue:** Model / GR00T N1, 1K Demos / GR00T N1.5, 1K Demos / GR00T N1.5, 1K Demos Task / Place 1 of 2 fruits onto plate; ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 3 | Although these new verbs can be considered "zero-shot" in the sense that we never collected teleoperation data for ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (Architecture), p. 1 (Architecture), p. 2 (Real GR-1 language following), p. 2 (Learning to manipulate novel objects from human ego videos). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (Introduction), p. 1 (Architecture), p. 2 (Generalization to novel behaviors using Neural Trajectories), p. 2 (Learning to manipulate novel objects from human ego videos), p. 3 (Post-training on Unitree G1), interface p. 1 (Architecture), p. 1 (Architecture), p. 2 (Real GR-1 language following), p. 2 (Learning to manipulate novel objects from human ego videos), objective p. 1 (Architecture), p. 1 (Architecture).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
