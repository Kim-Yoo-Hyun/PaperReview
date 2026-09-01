# Problem - World Action Models are Zero-shot Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (36 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2602.15922; PDF retrieval source: https://arxiv.org/pdf/2602.15922. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 3 (1. Introduction)): Although VLM priors encode what to do at a semantic level, they lack representations of how actions should be executed with precise spatial awareness, aligned with geometry, dynamics, and motor ...

## PDF Body Digest

- **p. 2 / Abstract - extractive PDF cue:** State-of-the-art Vision-Language-Action (VLA) models excel at semantic generalization but struggle to generalize to unseen physical motions in novel environments.
- **p. 2 / Abstract - extractive PDF cue:** We introduce DreamZero, a World Action Model (WAM) built upon a pretrained video diffusion backbone.
- **p. 2 / Abstract - extractive PDF cue:** Unlike VLAs, WAMs learn physical dynamics by predicting future world states and actions, using video as a dense representation of how the world evolves.
- **p. 2 / Abstract - extractive PDF cue:** By jointly modeling video and action, DreamZero learns diverse skills effectively from heterogeneous robot data without relying on repetitive demonstrations.
- **p. 2 / Abstract - extractive PDF cue:** This results in over 2× improvement in generalization to new tasks and environments compared to state-of-the-art VLAs in realrobot experiments.
- **p. 2 / 1. Introduction - extractive PDF cue:** Although VLM priors encode what to do at a semantic level, they lack representations of how actions should be executed with precise spatial awareness, aligned ...
- **p. 2 / 1. Introduction - extractive PDF cue:** While VLAs successfully inherit linguistic priors to generalize across diverse language instructions, especially manipulating diverse objects (Brohan et al., 2023), their generalization to novel environments ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Although VLM priors encode what to do at a semantic level, they lack representations of how actions should be executed with precise ... | uncertain robot state와 safe/unsafe operating region | body wording is the source claim |
| Observation / input | DreamZero jointly predicts video o𝑙:𝑙+𝐻and actions a𝑙:𝑙+𝐻conditioned on language instruction c, proprioceptive state q𝑙and visual observation including the current and the past ... | observation, uncertainty/risk estimate와 task command | exact sensor/frame/preprocessing from PDF |
| State / latent | DreamZero, jointly, predicts, video, actions, conditioned, language, instruction, proprioceptive, state | safe set, recovery state 또는 constraint margin | notation and tensor shape require body check |
| Output / action | Autoregressive, generation, possesses, following, advantages, enables, faster, inference | shielded, recovery 또는 safe action | exact unit/frame/decoder require body check |
| Target outcome | low violation/failure probability with useful intervention | task return과 violation/failure probability | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | state/history and risk h(s); body terms: DreamZero, jointly, predicts, video, actions, conditioned, language, instruction, proprioceptive, state | p. 6 (3.1. Model Architecture), p. 2 (1. Introduction), p. 7 (3.1. Model Architecture) |
| Decision / output variable | filtered/recovery action u_safe; body terms: Second, more, surprisingly, DreamZero, enables, few-shot, embodiment, adaptation | p. 3 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction) |
| Objective / loss / cost | task utility subject to safety constraint; cue terms: When, cosine, similarity, between, successive, velocities, exceeds, threshold | p. 7 (3.1. Model Architecture), p. 7 (3.1. Model Architecture), p. 8 (3.2.3. System-level Optimizations), p. 9 (3.2.4. Implementation-level Optimizations), p. 8 (3.1. Model Architecture) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 9 (3.2.4. Implementation-level Optimizations), p. 9 (3.2.4. Implementation-level Optimizations), p. 8 (3.2.3. System-level Optimizations) |
| Success / guarantee | low violation/failure probability with useful intervention | p. 16 (Figure/Table caption), p. 13 (5.1. Main Results), p. 12 (4.1. Pretraining) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** While VLAs successfully inherit linguistic priors to generalize across diverse language instructions, especially manipulating diverse objects (Brohan et al., 2023), their generalization to novel environments ...
- **p. 3 / 1. Introduction - extractive PDF cue:** We further find that diverse distribution of the training data is essential for generalization, outperforming multi-task repetitive data with the same amount of hours.
- **p. 3 / 1. Introduction - extractive PDF cue:** Moreover, the environment generalization of DreamZero is retained even after task-specific post-training, outperforming state-of-the-art VLAs by 10% on average task progress.

## What the Paper Changes

PDF contribution framing (p. 3 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 2 (1. Introduction), p. 7 (3.1. Model Architecture)): Second, and more surprisingly, we show that DreamZero enables few-shot embodiment adaptation: a model pretrained on AgiBot G1 adapts to an entirely new robot (YAM) with only 30 minutes of ...

- **p. 2 / 1. Introduction - extractive PDF cue:** In this paper, we present DreamZero, a 14B robot foundation model built upon a pretrained image-tovideo diffusion backbone (Team Wan, 2025).
- **p. 3 / 1. Introduction - extractive PDF cue:** To address the computational overhead inherent to video diffusion models, we introduce a suite of optimizations spanning three categories: (1) algorithmic improvements, including decoupled video ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Consequently, we observe that this enables (1) effective learning from robot data that are heterogeneous trajectories collected during the execution of useful behaviors in real-world ...
- **p. 7 / 3.1. Model Architecture - extractive PDF cue:** We introduce autoregressive modeling only for the video modality to avoid error propagation coming from closed-loop action prediction.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 19 | While DreamZero generalizes broadly across tasks and environments, it inherits limitations common to behavior cloning on tasks requiring ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | Figure 9: Zero-shot Generalization to Unseen Tasks. DreamZero achieves non-trivial task progress on 10 tasks absent from training, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 18 | We leave this direction as future work. | reported limitation/failure wording; scope must be verified |
| body cue at p. 18 | We leave deep investigation on scaling laws for WAMs as future work. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

safety writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 6 (3.1. Model Architecture), p. 2 (1. Introduction), p. 7 (3.1. Model Architecture), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 3 (1. Introduction), interface p. 6 (3.1. Model Architecture), p. 2 (1. Introduction), p. 7 (3.1. Model Architecture), p. 2 (1. Introduction), objective p. 7 (3.1. Model Architecture), p. 7 (3.1. Model Architecture), p. 8 (3.2.3. System-level Optimizations), p. 9 (3.2.4. Implementation-level Optimizations), p. 8 (3.1. Model Architecture).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
