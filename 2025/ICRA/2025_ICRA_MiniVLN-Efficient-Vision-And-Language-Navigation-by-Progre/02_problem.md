# Problem - MiniVLN: Efficient Vision-And-Language Navigation by Progressive Knowledge Distillation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2409.18800v1. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (III. PRELIMINARIES), p. 3 (III. PRELIMINARIES)): Our findings indicate that two-stage distillation is more effective in bridging the performance gap between the teacher model and the student model compared to single-stage distillation. • MiniVLN achieves comparable ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** In recent years, Embodied Artificial Intelligence (Embodied AI) has advanced rapidly, yet the increasing size of models conflicts with the limited computational capabilities of Embodied ...
- **p. 1 / Abstract - extractive PDF cue:** To address this challenge, we aim to achieve both high model performance and practical deployability.
- **p. 1 / Abstract - extractive PDF cue:** Specifically, we focus on Vision-and-Language Navigation (VLN), a core task in Embodied AI.
- **p. 1 / Abstract - extractive PDF cue:** This paper introduces a two-stage knowledge distillation framework, producing a student model, MiniVLN, and showcasing the significant potential of distillation techniques in developing lightweight models.
- **p. 1 / Abstract - extractive PDF cue:** The proposed method aims to capture fine-grained knowledge during the pretraining phase and navigation-specific knowledge during the fine-tuning phase.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Our findings indicate that two-stage distillation is more effective in bridging the performance gap between the teacher model and the student model compared to single-stage ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** AutoVLN [5] automatically generates a large-scale VLN dataset that significantly boosts model generalization.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Our findings indicate that two-stage distillation is more effective in bridging the performance gap between the teacher model and the student model ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | The agent must learn a policy π that predicts the next action based on the instruction I, the agent's navigation history, and ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | agent, must, learn, policy, predicts, next, action, instruction, navigation, history | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | While, fine-tuning, phase, agent, iteratively, predicts, actions, according | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: agent, must, learn, policy, predicts, next, action, instruction, navigation, history | p. 3 (III. PRELIMINARIES), p. 2 (III. PRELIMINARIES), p. 3 (IV. METHOD) |
| Decision / output variable | path/waypoint/velocity; body terms: main, contributions, introduce, MiniVLN, high-performance, lowcomplexity, model, specifically | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Val, Unseen, Test, Param, SPL, PREVALENT, RecBERT, HAMT | p. 3 (IV. METHOD), p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 5 (IV. METHOD), p. 5 (IV. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 5 (IV. METHOD) |
| Success / guarantee | goal reach with collision-free execution | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** AutoVLN [5] automatically generates a large-scale VLN dataset that significantly boosts model generalization.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** ScaleVLN [37], leveraging 1200+ environments and synthesizing 4.9 million instruction-trajectory pairs, exhibits significant improvements in generalization and achieves stateof-the-art results.
- **p. 2 / III. PRELIMINARIES - extractive PDF cue:** At time step t, the agent receives a panoramic observation Ot = {ot,i, at,i}K i=1 from its current viewpoint Vt.
- **p. 3 / III. PRELIMINARIES - extractive PDF cue:** Nt comprises visited nodes, the current node, and ghost nodes representing navigable but unvisited nodes.

## What the Paper Changes

PDF contribution framing (p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (IV. METHOD), p. 4 (IV. METHOD)): In this work, our main contributions are: • We introduce MiniVLN, a high-performance and lowcomplexity model specifically designed for deployment on resource-constrained devices. • To the best of our knowledge, ...

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Our method incorporates knowledge distillation in both the pre-training and fine-tuning stages, leading to the final student model MiniVLN.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** In contrast to approaches [14], [32] that apply distillation solely during the pre-training phase or only during the finetuning phase, we introduce a two-stage distillation ...
- **p. 3 / IV. METHOD - extractive PDF cue:** On this premise, we propose MiniVLN with two distinct distillation strategies tailored for each training phase.
- **p. 4 / IV. METHOD - extractive PDF cue:** Distillation Loss The language encoder and panorama encoder in Scalepre consists of NL = 9 and NP = 2 transformer blocks respectively.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| no explicit assumption/failure cue | domain stress test only | not a paper claim |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (III. PRELIMINARIES), p. 2 (III. PRELIMINARIES), p. 3 (IV. METHOD), p. 4 (IV. METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (III. PRELIMINARIES), p. 3 (III. PRELIMINARIES), interface p. 3 (III. PRELIMINARIES), p. 2 (III. PRELIMINARIES), p. 3 (IV. METHOD), p. 4 (IV. METHOD), objective p. 3 (IV. METHOD), p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 5 (IV. METHOD), p. 5 (IV. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
