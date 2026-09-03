# Problem - DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (33 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2602.06949; PDF retrieval source: https://arxiv.org/abs/2602.06949. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction)): Additionally, existing datasets predominantly consist of expert demonstrations, lacking the stochasticity in intentions necessary for learning strong action controllability.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Being able to simulate the outcomes of actions in varied environments will revolutionize the development of generalist agents at scale.
- **p. 1 / Abstract - extractive body cue:** However, modeling these world dynamics, especially for dexterous robotics tasks, poses significant challenges due to limited data coverage and scarce action labels.
- **p. 1 / Abstract - extractive body cue:** As an endeavor towards this end, we introduce DreamDojo, a foundation world model that learns diverse interactions and dexterous controls from 44k hours of egocentric ...
- **p. 1 / Abstract - extractive body cue:** Our data mixture represents the largest video dataset to date for world model pretraining, spanning a wide range of daily scenarios with diverse objects and ...
- **p. 1 / Abstract - extractive body cue:** To address the scarcity of action labels, we introduce continuous latent actions as unified proxy actions, enhancing interaction knowledge transfer from unlabeled videos.
- **p. 2 / 1. Introduction - extractive body cue:** Additionally, existing datasets predominantly consist of expert demonstrations, lacking the stochasticity in intentions necessary for learning strong action controllability.
- **p. 3 / 1. Introduction - extractive body cue:** DreamDojo can robustly generalize to various objects and environments, facilitating large-scale policy evaluation without real-world deployment.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Additionally, existing datasets predominantly consist of expert demonstrations, lacking the stochasticity in intentions necessary for learning strong action controllability. | uncertain robot state와 safe/unsafe operating region | body wording is the source claim |
| Observation / input | First, instead of using the absolute robot joint poses, we transform them into relative actions by rebaselining the inputs with the pose ... | observation, uncertainty/risk estimate와 task command | exact sensor/frame/preprocessing from PDF body |
| State / latent | First, instead, absolute, robot, joint, poses, transform, them, relative, actions | safe set, recovery state 또는 constraint margin | notation and tensor shape require body check |
| Output / action | objective, interactive, world, model, infer, future, states, actions | shielded, recovery 또는 safe action | exact unit/frame/decoder require body check |
| Target outcome | low violation/failure probability with useful intervention | task return과 violation/failure probability | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | state/history and risk h(s); body terms: First, instead, absolute, robot, joint, poses, transform, them, relative, actions | p. 5 (3.3.1. Model Architecture), p. 2 (1. Introduction), p. 3 (2. Preliminary) |
| Decision / output variable | filtered/recovery action u_safe; body terms: scaling, human, videos, introducing, continuous, latent, actions, unified | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Overview) |
| Objective / loss / cost | task utility subject to safety constraint; cue terms: supervise, student, prediction, randomly, select, window, size, receives | p. 8 (3.3.4. Distillation), p. 8 (3.3.4. Distillation), p. 7 (3.3.2. Pretraining from Human Videos), p. 7 (3.3.2. Pretraining from Human Videos) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (3.3.2. Pretraining from Human Videos), p. 4 (3.2. DreamDojo-HV Dataset), p. 6 (3.3.2. Pretraining from Human Videos) |
| Success / guarantee | low violation/failure probability with useful intervention | p. 13 (4.7. Downstream Applications), p. 13 (4.7. Downstream Applications), p. 14 (4.7. Downstream Applications) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we introduce continuous latent actions (Gao et al., 2025) as unified proxy actions for all videos.
- **p. 3 / 1. Introduction - extractive body cue:** DreamDojo can robustly generalize to various objects and environments, facilitating large-scale policy evaluation without real-world deployment.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Overview), p. 5 (3.3.1. Model Architecture), p. 3 (1. Introduction)): By scaling up human videos and introducing continuous latent actions as unified proxy, we present DreamDojo, the first world model of its kind that shows zero-shot generalization to unseen objects ...

- **p. 2 / 1. Introduction - extractive body cue:** In this work, we introduce DreamDojo, a foundation world model for open-world dexterous robot tasks.
- **p. 3 / 3.1. Overview - extractive body cue:** Our whole training procedure consists of three phases: 3
- **p. 5 / 3.3.1. Model Architecture - extractive body cue:** To realize precise action following, we propose two improvements based on the original architecture.
- **p. 3 / 1. Introduction - extractive body cue:** It also enables live teleoperation and online model-based planning.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 15 | Additionally, when conducting policy evaluation, the absolute success rates in DreamDojo are often higher than their real counterparts, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | As a result, training on these datasets often fails to preserve the model's abilities when extending to out-of-distribution ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 15 | Future work should explore how to cover broader action distribution, e.g., using policy rollouts (Ho et al., 2025; ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | To address this limitation, one might consider increasing the scale of real robot data. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

safety writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (3.3.1. Model Architecture), p. 2 (1. Introduction), p. 3 (2. Preliminary), p. 3 (2. Preliminary). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), interface p. 5 (3.3.1. Model Architecture), p. 2 (1. Introduction), p. 3 (2. Preliminary), p. 3 (2. Preliminary), objective p. 8 (3.3.4. Distillation), p. 8 (3.3.4. Distillation), p. 7 (3.3.2. Pretraining from Human Videos), p. 7 (3.3.2. Pretraining from Human Videos).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (33 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** To address these challenges, we introduce continuous latent actions (Gao et al., 2025) as unified proxy actions for all videos. (p. 2, 1. Introduction).
- **Formulation-changing contribution:** By scaling up human videos and introducing continuous latent actions as unified proxy, we present DreamDojo, the first world model of its kind that shows zero-shot generalization to unseen objects ... (p. 2, 1. Introduction).
- **Assumption/failure evidence:** Additionally, when conducting policy evaluation, the absolute success rates in DreamDojo are often higher than their real counterparts, indicating a limitation in accurately generating nuanced failures. (p. 15, 5. Conclusion).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
