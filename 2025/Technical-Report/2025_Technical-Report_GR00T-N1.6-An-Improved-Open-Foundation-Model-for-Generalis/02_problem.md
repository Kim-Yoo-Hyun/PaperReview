# Problem - GR00T N1.6: An Improved Open Foundation Model for Generalist Humanoid Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (2 pages; PyMuPDF text; extraction quality: medium); canonical paper source: https://research.nvidia.com/labs/gear/gr00t-n1_6/; PDF retrieval source: https://research.nvidia.com/labs/gear/gr00t-n1_6/. PDF provenance note: official NVIDIA technical page rendered to a task-scoped PDF snapshot; no author-supplied publication PDF identified. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (Discussion), p. 2 (Discussion)): Multi-task language following and out-of-distribution task generalization continue to be challenging for current VLA models.

## PDF Body Digest

- **p. 1 / Introduction - extractive body cue:** We introduce GR00T N1.6, an improved version of the GR00T N1.5 foundation model for humanoid robots.
- **p. 1 / Introduction - extractive body cue:** With several architecture, data and modeling improvements, we find that N1.6 outperforms N1.5 on both simulated manipulation benchmarks and on real bimanual YAM, Agibot Genie-1 ...
- **p. 1 / Introduction - extractive body cue:** We expect users of N1.6 should observe better post-training performance compared to N1.5.
- **p. 2 / Discussion - extractive body cue:** Multi-task language following and out-of-distribution task generalization continue to be challenging for current VLA models.
- **p. 2 / Discussion - extractive body cue:** More fine-grained subtask annotation can improve language following, but not yet reaching robust generalization.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Multi-task language following and out-of-distribution task generalization continue to be challenging for current VLA models. | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | Predicts state-relative action chunks for most embodiments, rather than absolute joint angles or EEF positions. | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF body |
| State / latent | Predicts, state-relative, action, chunks, most, embodiments, rather, absolute, joint, angles | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | More, fine-grained, subtask, annotation, improve, language, following, reaching | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: Predicts, state-relative, action, chunks, most, embodiments, rather, absolute, joint, angles | p. 1 (Model and Data Improvements), p. 1 (Model and Data Improvements), p. 2 (Discussion) |
| Decision / output variable | joint/whole-body action; body terms: introduce, GR00T, improved, version, foundation, model, humanoid, robots | p. 1 (Introduction) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: VLM, trained, general, vision-language, tasks, embodied, reasoning, like | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (Model and Data Improvements) |
| Success / guarantee | motion/task success and recovery | p. 1 (Discussion), p. 1 (Discussion), p. 2 (Discussion) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / Discussion - extractive body cue:** More fine-grained subtask annotation can improve language following, but not yet reaching robust generalization.

## What the Paper Changes

PDF body contribution framing (p. 1 (Introduction)): We introduce GR00T N1.6, an improved version of the GR00T N1.5 foundation model for humanoid robots.

- additional contribution cue 없음

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 2 | More fine-grained subtask annotation can improve language following, but not yet reaching robust generalization. | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Test-time and train-time RTC provide performance boosts to motion smoothness and robustness during asynchronous rollouts. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (Model and Data Improvements), p. 1 (Model and Data Improvements), p. 2 (Discussion), p. 2 (Discussion). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (Discussion), p. 2 (Discussion), interface p. 1 (Model and Data Improvements), p. 1 (Model and Data Improvements), p. 2 (Discussion), p. 2 (Discussion), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
