# Spatially Guided Training for Vision-Language-Action Model

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (40 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=eKhOrQWAVJ.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/247957. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics, 3D Vision
- Official paper: https://openreview.net/forum?id=eKhOrQWAVJ
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/247957
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (40 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, a critical gap remains when transferring these capabilities to the physical domain, because robots must not only understand what an instruction means but also determine where and how to act in ...를 문제로 두고, In contrast, simple spatial prompting effectively mitigates these issues (Section 3.1). • We propose ST4VLA, a spatially guided training framework that explicitly aligns action optimization with spatial grounding objectives, preserving ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 3 / 1 INTRODUCTION - extractive body cue:** In contrast, simple spatial prompting effectively mitigates these issues (Section 3.1). • We propose ST4VLA, a spatially guided training framework that explicitly aligns action optimization ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** 2 METHODS We propose ST4VLA, a spatially guided training framework that bridges spatial understanding with embodied control through a novel two-stage training recipe 2.2.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address the fundamental gap between multimodal understanding and embodied control, we propose ST4VLA, a dual-system vision-language-action framework that explicitly integrates spatial priors into robot ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** (2025) showing that direct gradient flow between action and VLM modules may distort multimodal knowledge, we introduce a gradient decay factor within the querying transformer.
- **p. 1 / ABSTRACT - extractive body cue:** We introduce ST4VLA, a dual-system Vision-Language-Action framework that leverages Spatial Guided Training to align action learning with spatial priors in VLMs.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Success rate (%) across different generalization settings on 200 simulated instruction- following pick-and-place tasks. Results. Since both baseline methods, π0 Black et al. ...
- **p. 20 / Figure/Table caption - extractive body cue:** Table 5. Compared to previous strong baselines, such as GR00T N1 and π0, the ST4VLA framework achieves notable improvements, particularly on the spatial and long-horizon ...
- **p. 6 / 3 EXPERIMENTS - extractive body cue:** Compared to the Vanilla VLA based on QwenVL-2.5-3B-Instruct, ST4VLA achieves substantial improvements: a 14.6% increase in Google Robot Visual Matching and a 12.4% increase in ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, a critical gap remains when transferring these capabilities to the physical domain, because robots must not only understand what an instruction means but also determine where and how to act in ...를 문제로 두고, In contrast, simple spatial prompting effectively mitigates these issues (Section 3.1). • We propose ST4VLA, a spatially guided training framework that explicitly aligns action optimization with spatial grounding objectives, preserving ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
