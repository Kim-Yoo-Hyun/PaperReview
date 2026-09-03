# Problem - Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p013.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p013.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Ivrropuction), p. 3 (1. Ivrropuction), p. 1 (1. Ivrropuction), p. 1 (1. Ivrropuction), p. 2 (1. Ivrropuction)): However, due to the limited rendering quality and diversity of simulators, these approaches often encounter the "sim-to-teal" gap and suffer from poor generalization across diverse navigation tasks (27, 5, 38].

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Embodied Navigation is a fundamental capability for intelligent robots, requiring robots to follow human commands ‘and moye autonomously within physical environments.
- **p. 1 / Abstract - extractive body cue:** Despite Significant advancements, most existing navigation approaches are tailored to specific navigation tasks, such as instruction following, searching objects, answering questions, tracking people, and more.
- **p. 1 / Abstract - extractive body cue:** However, the increasing demands on advanced embodied
- **p. 1 / Abstract - extractive body cue:** ractical navigation mm tasks naturally ‘and benefits from the synergy between these tasks.
- **p. 1 / Abstract - extractive body cue:** To this end, we present Uni 2 video-based vision-language-action (VLA) ‘model to unify different paradigms of navigation tasks and improve navigation performance by encouraging the ...
- **p. 2 / 1. Ivrropuction - extractive body cue:** However, due to the limited rendering quality and diversity of simulators, these approaches often encounter the "sim-to-teal" gap and suffer from poor generalization across diverse ...
- **p. 3 / 1. Ivrropuction - extractive body cue:** However, it faces efficiency challenges in longhorizon tasks.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, due to the limited rendering quality and diversity of simulators, these approaches often encounter the "sim-to-teal" gap and suffer from poor ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | This VLA model can directly take natural language instructions and RGB video streams as inputs and output low-level robotic actions in an ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | VLA, model, directly, take, natural, language, instructions, RGB, video, streams | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | Navigation, task, definition, define, general-purpose, Uni-NaVid_as, follows, time | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: VLA, model, directly, take, natural, language, instructions, RGB, video, streams | p. 1 (Abstract), p. 2 (1. Ivrropuction), p. 3 (1. Ivrropuction) |
| Decision / output variable | path/waypoint/velocity; body terms: However, goal, train, evaluate, mainstream, datasets, clearly, justify | p. 3 (1. Ivrropuction), p. 2 (1. Ivrropuction), p. 1 (Abstract) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Following, training, strategy, VLM, optimize, trainable, parameters, only | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (B. Training Strategy of Uni-NaVid) |
| Success / guarantee | goal reach with collision-free execution | p. 7 (VI. EXPERIMENT), p. 8 (B. Individual Task Results), p. 8 (B. Individual Task Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 3 / 1. Ivrropuction - extractive body cue:** However, it faces efficiency challenges in longhorizon tasks.
- **p. 1 / 1. Ivrropuction - extractive body cue:** Developing a versatile navigation model presents significant challenges, as it requires the unification of navigation task
- **p. 1 / 1. Ivrropuction - extractive body cue:** However, na igation tasks vary significantly, and most existing studies are designed for specific tasks, e.g., vision-and-language navigation (42, 44], object goal navigation [12], embodied ...
- **p. 2 / 1. Ivrropuction - extractive body cue:** However, due t0 the low frequency of LLM inference, they simplify the problem to some extent by adopting discretized modeling approaches.

## What the Paper Changes

PDF body contribution framing (p. 3 (1. Ivrropuction), p. 2 (1. Ivrropuction), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1. Ivrropuction)): However, our goal is to train and ‘evaluate our method on mainstream datasets to clearly justify the performance of our approach.

- **p. 2 / 1. Ivrropuction - extractive body cue:** ‘We conduct extensive experiments on benchmarks across the aforementioned four navigation tasks and compared our method with strong baselines specifically designed for each task.
- **p. 1 / Abstract - extractive body cue:** To efficiently process extensive RGB video streams, we propose an online token merge strategy that spatially and {temporally consolidates similar visual information which improves the ...
- **p. 1 / Abstract - extractive body cue:** To this end, we present Uni 2 video-based vision-language-action (VLA) ‘model to unify different paradigms of navigation tasks and improve navigation performance by encouraging the ...
- **p. 2 / 1. Ivrropuction - extractive body cue:** To this end, we propose an online token merging mechanism to compress near historical frames with a relatively low ratio while compressing far

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | standard evaluation metrics [4], including success rate (SR), oracle success rate (OS), success weighted by path length (SPL) ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | Despite the promising results, Uni-NaVid has several limitations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | This limitation could be alleviated by extending the moel to predict | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | gies, while also highlighting robust open-world understanding capabilities. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (Abstract), p. 2 (1. Ivrropuction), p. 3 (1. Ivrropuction), p. 3 (1. Ivrropuction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Ivrropuction), p. 3 (1. Ivrropuction), p. 1 (1. Ivrropuction), p. 1 (1. Ivrropuction), p. 2 (1. Ivrropuction), interface p. 1 (Abstract), p. 2 (1. Ivrropuction), p. 3 (1. Ivrropuction), p. 3 (1. Ivrropuction), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, due t0 the low frequency of LLM inference, they simplify the problem to some extent by adopting discretized modeling approaches. (p. 2, 1. Ivrropuction).
- **Formulation-changing contribution:** However, our goal is to train and ‘evaluate our method on mainstream datasets to clearly justify the performance of our approach. (p. 3, 1. Ivrropuction).
- **Assumption/failure evidence:** Despite the promising results, Uni-NaVid has several limitations. (p. 11, C. Qualitative Results in Real-World).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
