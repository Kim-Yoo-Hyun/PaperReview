# Spatially Guided Training for Vision-Language-Action Model

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (40 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2026/hash/37294f033582ac0064bf90fa557c2573-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/247957. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: Jinhui Ye, Fangjing Wang, Ning Gao, Junqiu Yu, Yangkun Zhu, Bin Wang, Jinyu Zhang, Weiyang Jin, Yanwei Fu, Feng Zheng, Yilun Chen, Jiangmiao Pang
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics, 3D Vision
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/37294f033582ac0064bf90fa557c2573-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2026/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (40 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

ST4VLA는 대상 위치와 이동 경로를 먼저 학습한 공간 표현이 로봇의 저수준 행동 생성을 안내하도록 훈련한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Large vision-language models (VLMs) excel at multimodal understanding but fall short when extended to embodied tasks, where instructions must be transformed into low-level motor actions.
- **p. 1 / ABSTRACT - extractive body cue:** We introduce ST4VLA, a dual-system Vision-Language-Action framework that leverages Spatial Guided Training to align action learning with spatial priors in VLMs.
- **p. 1 / ABSTRACT - extractive body cue:** ST4VLA includes two stages: (i) spatial grounding pre-training, which equips the VLM with transferable priors via scalable point, box, and trajectory prediction from both web-scale ...
- **p. 1 / ABSTRACT - extractive body cue:** This design preserves spatial grounding during policy learning and promotes consistent optimization across spatial and action objectives.
- **p. 1 / ABSTRACT - extractive body cue:** Empirically, ST4VLA achieves substantial improvements over vanilla VLA, with performance increasing from 66.1 to 84.6 on Google Robot and from 54.7 to 73.2 on WidowX ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, a critical gap remains when transferring these capabilities to the physical domain, because robots must not only understand what an instruction means but also ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Prior work has approached this challenge through hierarchical robotic systems Huang et al.

## Core Idea

- **p. 3 / 1 INTRODUCTION - extractive body cue:** In contrast, simple spatial prompting effectively mitigates these issues (Section 3.1). • We propose ST4VLA, a spatially guided training framework that explicitly aligns action optimization ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** 2 METHODS We propose ST4VLA, a spatially guided training framework that bridges spatial understanding with embodied control through a novel two-stage training recipe 2.2.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address the fundamental gap between multimodal understanding and embodied control, we propose ST4VLA, a dual-system vision-language-action framework that explicitly integrates spatial priors into robot ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** (2025) showing that direct gradient flow between action and VLM modules may distort multimodal knowledge, we introduce a gradient decay factor within the querying transformer.
- **p. 1 / ABSTRACT - extractive body cue:** We introduce ST4VLA, a dual-system Vision-Language-Action framework that leverages Spatial Guided Training to align action learning with spatial priors in VLMs.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We propose a new a dual-system, end-to-end VLA framework based on Qwen2.5-VL, which can foster alignment between the optimization dynamics of the spatial grounding objective ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Given a task instruction, the VLM planner produces latent plans through explicit spatial prompting, which then effectively guides the action expert to generate control signals. ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Spatial Planning Prompt VL-Input Sub-Task Planning Action Action VLM Planner DiT Actor Latent Planning Data Model Deployment Point Grounding A: The image shows a person ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Noisy Actions Actions DiT - Actor Conditioned State (opt) Your task is to {instruction}. | image/video, language instruction, proprioception과 history | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| State/latent | Noisy, Actions, DiT, Actor, Conditioned, State, Your, task, instruction, Spatial, Planning, Prompt | language-grounded task state와 action-policy context | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT) |
| Output/action | Spatial Planning Prompt VL-Input Sub-Task Planning Action Action VLM Planner DiT Actor Latent Planning Data Model Deployment Point Grounding A: The image shows a person standing in a bathroom, facing away from ... | continuous action, pose 또는 action chunk | p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 3 (1 INTRODUCTION) |
| Objective/outcome | This work makes the following contributions: • We observe that directly fine-tuning a VLM with an action expert as a VLA model leads to a collapse of spatial priors, and that na¨ıve ... | instruction following, task success, generalization과 latency | p. 3 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION) |

## Main Claims and Actual Contribution

- 웹·로봇 자료에서 점, 상자, 궤적 예측을 사전학습하고 행동 후학습에서도 공간 프롬프트를 사용해 행동 모듈과 연결했다. [PDF 3쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf#page=3) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf#page=4)
- SimplerEnv의 Google Robot·WidowX 조건을 비교하고, 별도의 실물 과제에서 물체와 언어 지시 변화에 대한 일반화를 평가했다. [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf#page=6) · [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 20 (Figure/Table caption) |
| Embodiment/environment | 3.4 EVALUATION IN REAL-WORLD CLUTTERED-SCENE PICK-AND-PLACE We use the Franka Research 3 robot to evaluate the generalization performance of our model and baselines on the real-world pick-and-place tasks. | hardware/simulator version and reset protocol | p. 7 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS) |
| Dataset/benchmark | Compared with prior state-of-the-art models, it attains a 5.9% gain in Google Robot Visual Matching, a 5.3% gain in Visual Aggregation, and a 9.8% gain on the WidowX benchmark. | role, split, size and leakage | p. 7 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS) |
| Metric | Figure 3: Ablation study on the effect of auxiliary spatial prompting during co-training. From left to right: (a) perception performance (IoU@0.5 on RefCOCO-g); (b) manipulation performance (Average Success Rate on WidowX); (c) ... | definition, denominator, direction and uncertainty | p. 5 (Figure/Table caption), p. 7 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS) |
| Baseline/ablation | Figure 4: Success rate (%) across different generalization settings on 200 simulated instruction- following pick-and-place tasks. Results. Since both baseline methods, π0 Black et al. (2024) and GR00T N1.5 Bjorck et al. ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 20 (Figure/Table caption), p. 5 (3 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 36 / Figure/Table caption - extractive body cue:** Figure 23: Failure case study. To better understand the limitations of ST4VLA, we analyze representative failure cases during real-world instruction-following pick-and-place tasks. As shown in ...
- **p. 38 / Figure/Table caption - extractive body cue:** Figure 25: Simulation data synthesis pipeline. The pipeline generates diverse robotic manipulation data from a large asset library, converts intermediate representations into VQA data, and ...
- **p. 5 / 3 EXPERIMENTS - extractive body cue:** Vanilla co-training partially preserves perception but exhibits unstable oscillations in both metrics.
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** To address these limitations, we construct a large-scale simulation benchmark in Isaac-Sim by GenManip Gao et al.
- **p. 8 / 3 EXPERIMENTS - extractive body cue:** Results in Figure 5 show that ST4VLA consistently surpasses GR00T N1.5 and π0, reliably grounding high-level goals into executable steps, adapting to disturbances, and dynamically ...
- **p. 9 / 4 RELATED WORK - extractive body cue:** (2025a) also adopts spatial pre-training, though it does not explicitly leverage spatial prompting to guide action generation.
- **p. 4 / 3 EXPERIMENTS - extractive body cue:** We conduct comprehensive experiments to evaluate whether aligning the optimization dynamics of multimodal grounding and action policy objectives enables robust robot manipulation.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)이다.
