# Problem - XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (45 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://icml.cc/virtual/2026/oral/71118; PDF retrieval source: https://openreview.net/pdf/181715f87df4dd5677ebf2619dcb456e071c95dd.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): Despite VLM advancements, two challenges persist: (i) Precision Gap: Mapping high-dimensional observations to precise low-level actions is difficult due to multimodal uncertainty; even centimeter-level errors lead to failure in dexterou ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Recent progress in large-scale robotic datasets and vision-language models (VLMs) has advanced research on vision-language-action (VLA) models.
- **p. 1 / Abstract - extractive body cue:** However, existing VLA models still face two fundamental challenges: (i) producing precise low-level actions from high-dimensional ob
- **p. 1 / Abstract - extractive body cue:** 1Beijing Innovation Center of Humanoid Robotics, Beijing, China 2State Key Laboratory of Multimedia Information Processing, School of Computer Science.
- **p. 1 / Abstract - extractive body cue:** Existing methods often encode latent variables from either visual dynamics or robotic actions to guide policy learning, but they fail to fully exploit the complementary ...
- **p. 1 / Abstract - extractive body cue:** In this work, we present X Robotic Model 1 (XR-1), a novel framework for versatile and scalable VLA learning across diverse robots, tasks, and environments.
- **p. 2 / 1. Introduction - extractive body cue:** Despite VLM advancements, two challenges persist: (i) Precision Gap: Mapping high-dimensional observations to precise low-level actions is difficult due to multimodal uncertainty; even centimeter-level errors ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, prior research (Cui et al., 2023; Shafiullah et al., 2022; Lee et al., 2024; Xie et al., 2025; Zheng et al., ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Despite VLM advancements, two challenges persist: (i) Precision Gap: Mapping high-dimensional observations to precise low-level actions is difficult due to multimodal uncertainty; ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | At each inference step t, the policy π receives a language instruction l and multimodal observations o = ⟨c, m⟩, where c ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | inference, step, policy, receives, language, instruction, multimodal, observations, where, denotes | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | implementation, proprioceptive, states, condition, input, policy, follows, standard | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: inference, step, policy, receives, language, instruction, multimodal, observations, where, denotes | p. 4 (3.1. Overview), p. 4 (3.1. Overview), p. 5 (3.1. Overview) |
| Decision / output variable | action, pose, option or chunk a; body terms: main, contributions, summarized, follows, Robotic, Model, XR-1, scalable | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Overview) |
| Objective / loss / cost | policy/action modeling objective; cue terms: Training, follows, standard, VQ-VAE, objectives, Van, Den, Oord | p. 5 (3.1. Overview), p. 5 (3.1. Overview), p. 4 (3.1. Overview) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.1. Overview), p. 4 (3.1. Overview), p. 4 (3.1. Overview) |
| Success / guarantee | instruction-conditioned task success | p. 6 (4.1. Experiment Setup), p. 7 (4.1. Experiment Setup), p. 8 (4.3. Ablation Study) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, prior research (Cui et al., 2023; Shafiullah et al., 2022; Lee et al., 2024; Xie et al., 2025; Zheng et al., ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Overview), p. 5 (3.1. Overview), p. 5 (3.1. Overview)): Our main contributions are summarized as follows: • We propose X Robotic Model 1 (XR-1), a scalable three-stage framework for VLA learning that effectively leverages heterogeneous data sources, including Internet-scale ...

- **p. 2 / 1. Introduction - extractive body cue:** Addressing the limitations of unimodal representations and inspired by human supramodal cognition, we propose X Robotic Model 1 (XR-1) to achieve cross-data exploitation and cross-embodiment ...
- **p. 4 / 3.1. Overview - extractive body cue:** We introduce XR-1, a scalable framework for cross-robot VLA learning (Figure 2), structured in three stages.
- **p. 5 / 3.1. Overview - extractive body cue:** To unify both modalities, we introduce a VQ-VAE codebook e ∈Rd×f with d discrete entries of dimension f.
- **p. 5 / 3.1. Overview - extractive body cue:** To mitigate this gap, we introduce an alignment loss that constrains visual codes to remain consistent with their motion counterparts: Lalign = DKL(q(ze mo) ∥q(ze ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | We presented X Robotic Model 1 (XR-1), a unified framework for versatile and scalable vision-language-action learning that addresses ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Failure analyses for baselines and XR-1 are provided in Appendix I and Appendix J, respectively, showing that XR-1 ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 30 | Figure 15. Visualizing UVMC across different embodiments (Dual-Arm Franka and Dual-Arm UR) using t-SNE. an intermediate feature supervision ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 31 | Figure 16. Failure cases of baseline methods. Miss Miss Drop XR-1 Precision Deficiency: TK2-CollectScrews | reported limitation/failure wording; scope must be verified |

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (3.1. Overview), p. 4 (3.1. Overview), p. 5 (3.1. Overview), p. 5 (3.1. Overview). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 4 (3.1. Overview), p. 4 (3.1. Overview), p. 5 (3.1. Overview), p. 5 (3.1. Overview), objective p. 5 (3.1. Overview), p. 5 (3.1. Overview), p. 4 (3.1. Overview).

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)
