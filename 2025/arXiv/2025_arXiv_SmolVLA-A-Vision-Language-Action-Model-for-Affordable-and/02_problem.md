# Problem - SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2506.01844; PDF retrieval source: https://arxiv.org/pdf/2506.01844. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction)): To address this limitation, a growing body of work has begun exploring robotics foundation models in the form of vision-language-action (VLA) models (Team et al., 2024; O'Neill et al., 2024; ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Vision-language models (VLMs) pretrained on large-scale multimodal datasets encode rich visual and linguistic knowledge, making them a strong foundation for robotics.
- **p. 1 / Abstract - extractive body cue:** Rather than training robotic policies from scratch, recent approaches adapt VLMs into vision-language-action (VLA) models that enable natural language-driven perception and control.
- **p. 1 / Abstract - extractive body cue:** However, existing VLAs are typically massive-often with billions of parameters-leading to high training costs and limited real-world deployability.
- **p. 1 / Abstract - extractive body cue:** Moreover, they rely on academic and industrial datasets, overlooking the growing availability of community-collected data from affordable robotic platforms.
- **p. 1 / Abstract - extractive body cue:** In this work, we present SmolVLA, a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance.
- **p. 2 / 1 Introduction - extractive body cue:** To address this limitation, a growing body of work has begun exploring robotics foundation models in the form of vision-language-action (VLA) models (Team et al., ...
- **p. 2 / 1 Introduction - extractive body cue:** Early results suggest promising gains in generalization capabilities (Black et al., 2024; Brohan et al., 2023).

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | To address this limitation, a growing body of work has begun exploring robotics foundation models in the form of vision-language-action (VLA) models ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | These models take multimodal inputs-such as visual observations and natural language instructions-and predict the corresponding robotic actions. | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | models, take, multimodal, inputs-such, visual, observations, natural, language, instructions-and, predict | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Self-Attention, Cross-Attention, Task, Grasp, object, State, Noisy, Actions | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: models, take, multimodal, inputs-such, visual, observations, natural, language, instructions-and, predict | p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract) |
| Decision / output variable | action, pose, option or chunk a; body terms: present, SmolVLA, compact, efficient, vision-language, agent, optimized, training | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract) |
| Objective / loss / cost | policy/action modeling objective; cue terms: While, encouraging, efforts, like, OpenVLA, Kim, RT-2-X, Neill | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction) |
| Success / guarantee | instruction-conditioned task success | p. 8 (4 Experiments), p. 12 (4 Experiments), p. 8 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** Early results suggest promising gains in generalization capabilities (Black et al., 2024; Brohan et al., 2023).

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract)): We present SmolVLA, a compact and efficient vision-language agent optimized for training on consumer-grade GPUs and deployment on CPUs.

- **p. 2 / 1 Introduction - extractive body cue:** In this work, we introduce SmolVLA, an open-source initiative featuring a compact yet capable VLA model, released alongside reproducible and efficient training and inference recipes.
- **p. 1 / Abstract - extractive body cue:** SmolVLA consists of a compact pretrained vision-language model, discarding the last L -N layers (scissors icon).
- **p. 1 / Abstract - extractive body cue:** In this work, we present SmolVLA, a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 14 | 5.1 Limitations We identify several limitations remaining in our contribution. | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | The robot exhibits greater robustness to shifts in object positions and external disturbances, and overall is capable to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | Success Rate (%) - Real World Policy In Distribution Out of Distribution Single-task Training ACT 70 40 SmolVLA ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | Similarly, on SO101 (see Table 4), SmolVLA surpasses ACT in both in-distribution and out-of-distribution (OOD) settings. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
