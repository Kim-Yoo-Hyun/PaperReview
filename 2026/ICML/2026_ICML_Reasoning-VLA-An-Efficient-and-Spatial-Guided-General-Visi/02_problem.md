# Problem - Reasoning-VLA: An Efficient and Spatial-Guided General Vision-Language-Action Reasoning Model for Autonomous Driving

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=c4iSIrb6Iv; PDF retrieval source: https://openreview.net/pdf/2958fe5249a1a673a414d689de7784b306b2a02a.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): 2) Current VLA methods lack robust generalization to new vehicle platforms or unseen driving scenarios.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models have recently shown strong decision-making capabilities in autonomous driving.
- **p. 1 / Abstract - extractive body cue:** However, existing VLAs often struggle with achieving efficient inference and generalizing to novel autonomous vehicle configurations and driving scenarios.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose Reasoning-VLA, a general and fast action-generation VLA framework.
- **p. 1 / Abstract - extractive body cue:** The proposed model employs a set of learnable action queries, initialized via Gaussian sampling from ground-truth trajectories within the training corpus.
- **p. 1 / Abstract - extractive body cue:** These learnable queries interact with reasoning-enhanced vision-language features to generate continuous action trajectories in parallel.
- **p. 1 / 1. Introduction - extractive body cue:** 2) Current VLA methods lack robust generalization to new vehicle platforms or unseen driving scenarios.
- **p. 1 / 1. Introduction - extractive body cue:** These limitations hinder their generalization ability to new driving scenarios.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | 2) Current VLA methods lack robust generalization to new vehicle platforms or unseen driving scenarios. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | VLM Question CoT Reasoning Prompt Refinement Parallel Action VLto A Interaction Ego Status Prompt ...... <answer></answer> N Hidden States Gaussian Distribution Initializing ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | VLM, Question, CoT, Reasoning, Prompt, Refinement, Parallel, Action, VLto, Interaction | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Most, existing, Vision-Language-Action, VLA, methods, either, rely, specialized | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: VLM, Question, CoT, Reasoning, Prompt, Refinement, Parallel, Action, VLto, Interaction | p. 2 (1. Introduction), p. 4 (3.5. Action Refinement Module), p. 3 (3.2. The Structure of Reasoning-VLA) |
| Decision / output variable | action, pose, option or chunk a; body terms: summarize, main, contributions, follows, Reasoning-VLA, efficient, fast, VLA | p. 2 (1. Introduction), p. 3 (3. Method), p. 1 (1. Introduction) |
| Objective / loss / cost | policy/action modeling objective; cue terms: design, establishes, dynamic, constraint, optimization, objective, ensures, physically | p. 5 (3.7. Reward Functions), p. 5 (3.7. Reward Functions) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (3.7. Reward Functions), p. 4 (3.2. The Structure of Reasoning-VLA), p. 4 (3.5. Action Refinement Module) |
| Success / guarantee | instruction-conditioned task success | p. 7 (5.1. Experiment Setups), p. 7 (5.2.2. Closed-loop Evaluation), p. 8 (5.2.2. Closed-loop Evaluation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** These limitations hinder their generalization ability to new driving scenarios.
- **p. 2 / 1. Introduction - extractive body cue:** To summarize, the main contributions are as follows: • We propose Reasoning-VLA, an efficient and fast VLA framework that employs learnable action queries to interact ...
- **p. 2 / 1. Introduction - extractive body cue:** Extensive experiments demonstrate that Reasoning-VLA significantly improves generalization ability, planning performance, and inference speed compared with existing VLA approaches.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 3 (3. Method), p. 1 (1. Introduction), p. 3 (3. Method), p. 4 (3.5. Action Refinement Module)): To summarize, the main contributions are as follows: • We propose Reasoning-VLA, an efficient and fast VLA framework that employs learnable action queries to interact with reasoning-enhanced vision-language representations, enabling ...

- **p. 3 / 3. Method - extractive body cue:** In the following sections, we present a detailed description of our approach to developing a VLA framework for autonomous driving and highlight key insights.
- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we propose ReasoningVLA, an efficient and generalist VLA framework that establishes a new state-of-the-art for autonomous driving.
- **p. 3 / 3. Method - extractive body cue:** 1, the Reasoning-VLA framework comprises three main components: (1) a reasoningenhanced vision-language model (VLM) backbone, (2) an action module that interacts with the VLM and ...
- **p. 4 / 3.5. Action Refinement Module - extractive body cue:** To further enhance the representation quality and accuracy of the predicted action trajectories, we introduce an Action Refinement Module (ARM).

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | Figure 3. Statistical distribution of the unified dataset. However, these constraints exert a non-negligible influence on the vehicle's ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Methods NeuroNCAP Score ↑ Collision Rate (%) ↓ Stationary Frontal Side Avg. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | The generalized model, Reasoning-VLA-7B, substantially outperforms prior methods in terms of NeuroNCAP Score and Collision Rate, achieving an ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | NAVSIM[9] 0.05 0.18 0.43 0.22 0.04 0.18 0.41 0.21 nuScenes[4] 0.06 0.23 0.48 0.26 0.05 0.20 0.44 0.23 ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1. Introduction), p. 4 (3.5. Action Refinement Module), p. 3 (3.2. The Structure of Reasoning-VLA), p. 4 (3.3.1. Learnable Action Queries). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 2 (1. Introduction), p. 4 (3.5. Action Refinement Module), p. 3 (3.2. The Structure of Reasoning-VLA), p. 4 (3.3.1. Learnable Action Queries), objective p. 5 (3.7. Reward Functions), p. 5 (3.7. Reward Functions).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
