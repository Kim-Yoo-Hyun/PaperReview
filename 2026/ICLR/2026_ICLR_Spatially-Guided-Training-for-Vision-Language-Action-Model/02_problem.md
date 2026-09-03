# Problem - Spatially Guided Training for Vision-Language-Action Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (40 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=eKhOrQWAVJ; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/247957. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): However, a critical gap remains when transferring these capabilities to the physical domain, because robots must not only understand what an instruction means but also determine where and how to ...

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** Large vision-language models (VLMs) excel at multimodal understanding but fall short when extended to embodied tasks, where instructions must be transformed into low-level motor actions.
- **p. 1 / ABSTRACT - extractive body cue:** We introduce ST4VLA, a dual-system Vision-Language-Action framework that leverages Spatial Guided Training to align action learning with spatial priors in VLMs.
- **p. 1 / ABSTRACT - extractive body cue:** ST4VLA includes two stages: (i) spatial grounding pre-training, which equips the VLM with transferable priors via scalable point, box, and trajectory prediction from both web-scale ...
- **p. 1 / ABSTRACT - extractive body cue:** This design preserves spatial grounding during policy learning and promotes consistent optimization across spatial and action objectives.
- **p. 1 / ABSTRACT - extractive body cue:** Empirically, ST4VLA achieves substantial improvements over vanilla VLA, with performance increasing from 66.1 to 84.6 on Google Robot and from 54.7 to 73.2 on WidowX ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, a critical gap remains when transferring these capabilities to the physical domain, because robots must not only understand what an instruction means but also ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Prior work has approached this challenge through hierarchical robotic systems Huang et al.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, a critical gap remains when transferring these capabilities to the physical domain, because robots must not only understand what an instruction ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Noisy Actions Actions DiT - Actor Conditioned State (opt) Your task is to {instruction}. | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | Noisy, Actions, DiT, Actor, Conditioned, State, Your, task, instruction, Spatial | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Large, vision-language, models, VLMs, excel, multimodal, understanding, fall | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Noisy, Actions, DiT, Actor, Conditioned, State, Your, task, instruction, Spatial | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT) |
| Decision / output variable | action, pose, option or chunk a; body terms: contrast, simple, spatial, prompting, effectively, mitigates, issues, Section | p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective / loss / cost | policy/action modeling objective; cue terms: makes, following, contributions, observe, directly, fine-tuning, VLM, action | p. 3 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 4 (1 INTRODUCTION) |
| Success / guarantee | instruction-conditioned task success | p. 5 (Figure/Table caption), p. 7 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive body cue:** Prior work has approached this challenge through hierarchical robotic systems Huang et al.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address the fundamental gap between multimodal understanding and embodied control, we propose ST4VLA, a dual-system vision-language-action framework that explicitly integrates spatial priors into robot ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** ST4VLA substantially improves generalization to unseen objects, novel instructions, and out-of-distribution environments, outperforming strong baselines such as π0 Black et al.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The rigid separation between symbolic task structures and low-level motor control makes it difficult to scale automatically to complex and diverse tasks, and particularly limits ...

## What the Paper Changes

PDF body contribution framing (p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 1 (ABSTRACT)): In contrast, simple spatial prompting effectively mitigates these issues (Section 3.1). • We propose ST4VLA, a spatially guided training framework that explicitly aligns action optimization with spatial grounding objectives, preserving ...

- **p. 3 / 1 INTRODUCTION - extractive body cue:** 2 METHODS We propose ST4VLA, a spatially guided training framework that bridges spatial understanding with embodied control through a novel two-stage training recipe 2.2.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address the fundamental gap between multimodal understanding and embodied control, we propose ST4VLA, a dual-system vision-language-action framework that explicitly integrates spatial priors into robot ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** (2025) showing that direct gradient flow between action and VLM modules may distort multimodal knowledge, we introduce a gradient decay factor within the querying transformer.
- **p. 1 / ABSTRACT - extractive body cue:** We introduce ST4VLA, a dual-system Vision-Language-Action framework that leverages Spatial Guided Training to align action learning with spatial priors in VLMs.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 36 | Figure 23: Failure case study. To better understand the limitations of ST4VLA, we analyze representative failure cases during ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 38 | Figure 25: Simulation data synthesis pipeline. The pipeline generates diverse robotic manipulation data from a large asset library, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Vanilla co-training partially preserves perception but exhibits unstable oscillations in both metrics. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | To address these limitations, we construct a large-scale simulation benchmark in Isaac-Sim by GenManip Gao et al. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 3 (1 INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 3 (1 INTRODUCTION), objective p. 3 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
