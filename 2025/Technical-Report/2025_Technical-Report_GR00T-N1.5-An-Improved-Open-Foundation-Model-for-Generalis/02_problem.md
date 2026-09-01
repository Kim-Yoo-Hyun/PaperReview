# Problem - GR00T N1.5: An Improved Open Foundation Model for Generalist Humanoid Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: official NVIDIA technical page body (no public PDF identified) checked on 2026-09-02 (1 source page(s); official NVIDIA technical page body (no public PDF identified); extraction quality: high); canonical paper source: https://research.nvidia.com/labs/gear/gr00t-n1_5/; body source: https://research.nvidia.com/labs/gear/gr00t-n1_5/. The note is an evidence-anchored official source body analysis; exact tables/equations or section details remain at the cited source anchors. Evidence boundary: selected official source body statements and source anchors were used; no PDF was identified at review time. Reading tracker status/evidence was not changed.

## Problem in One Sentence

official source body framing (p. 1 (Learning to manipulate novel objects from human ego videos), p. 1 (Model and Data Updates)): Novel object generalization performance.

## PDF Body Digest

- **p. 1 / GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots - extractive body cue:** GR00T N1.5 Policy rollout with language prompt: "Pick the apple from table to plate"
- **p. 1 / GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots - extractive body cue:** We introduce GR00T N1.5, an upgraded version of the GR00T N1 foundation model for humanoid robots.
- **p. 1 / GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots - extractive body cue:** With several architecture, data and modeling improvements, we find that N1.5 outperforms N1 on both simulated manipulation benchmarks and on the real GR-1 robot, detailed ...
- **p. 1 / GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots - extractive body cue:** We expect users of N1.5 should observe better performance compared to N1, in particular improved generalization and better language following ability.
- **p. 1 / Model and Data Updates - extractive body cue:** As with N1, GR00T N1.5 uses an NVIDIA Eagle VLM to encode text and visual observations.
- **p. 1 / Learning to manipulate novel objects from human ego videos - extractive body cue:** Novel object generalization performance.
- **p. 1 / Model and Data Updates - extractive body cue:** We found that these modifications greatly improved language following and generalization.

## System and Scope

| Dimension | official source body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Novel object generalization performance. | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions. | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from official source body |
| State / latent | vision-language, embeddings, VLM, then, cross-attended, DiT, processes, state, noised, actions | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | introduce, GR00T, upgraded, version, foundation, model, humanoid, robots | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | official source body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: vision-language, embeddings, VLM, then, cross-attended, DiT, processes, state, noised, actions | p. 1 (Model and Data Updates), p. 1 (GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots) |
| Decision / output variable | joint/whole-body action; body terms: introduce, GR00T, upgraded, version, foundation, model, humanoid, robots | p. 1 (GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots), p. 1 (Learning to manipulate novel objects from human ego videos) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: attribute, improvements, improved, grounding, capabilities, usage, FLARE, loss | p. 1 (Joint Policy Learning and World Modeling Objective), p. 1 (Joint Policy Learning and World Modeling Objective) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (Post-training on Unitree G1), p. 1 (Joint Policy Learning and World Modeling Objective) |
| Success / guarantee | motion/task success and recovery | p. 1 (Generalization to novel behaviors using Neural Trajectories), p. 1 (Post-training on Unitree G1) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited official source body anchors.

## Bottleneck in Prior Work

- **p. 1 / Model and Data Updates - extractive body cue:** We found that these modifications greatly improved language following and generalization.

## What the Paper Changes

official source body contribution framing (p. 1 (GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots), p. 1 (Learning to manipulate novel objects from human ego videos)): We introduce GR00T N1.5, an upgraded version of the GR00T N1 foundation model for humanoid robots.

- **p. 1 / Learning to manipulate novel objects from human ego videos - extractive body cue:** As shown in the FLARE project , future latent representation alignment enables learning directly from human ego videos.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 1 | Although these new verbs can be considered "zero-shot" in the sense that we never collected teleoperation data for ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (Model and Data Updates), p. 1 (GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (Learning to manipulate novel objects from human ego videos), p. 1 (Model and Data Updates), interface p. 1 (Model and Data Updates), p. 1 (GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots), objective p. 1 (Joint Policy Learning and World Modeling Objective), p. 1 (Joint Policy Learning and World Modeling Objective).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
