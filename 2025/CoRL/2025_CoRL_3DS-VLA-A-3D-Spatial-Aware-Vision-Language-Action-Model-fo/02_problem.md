# Problem - 3DS-VLA: A 3D Spatial-Aware Vision Language Action Model for Robust Multi-Task Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v305/li25g.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/li25g/li25g.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction)): All these limitations lead us to consider: "How can we build a robust VLA model that incorporates comprehensive 3D spatial awareness?" To address the above challenges, as shown in Fig.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Recently, 2D vision-language-action (VLA) models have made significant strides in multi-task manipulation.
- **p. 1 / Abstract - extractive body cue:** However, these models struggle to reason about 3D spatial relationships from 2D image inputs.
- **p. 1 / Abstract - extractive body cue:** Although an increasing number of 3D imitation learning approaches explicitly integrate 3D information, they face challenges such as the lack of generalized 3D pretrained models ...
- **p. 1 / Abstract - extractive body cue:** Meanwhile, existing policies typically focus on the perception-to-action learning paradigm, lacking an explicit understanding of the spatial and temporal relationships between the robot and its ...
- **p. 1 / Abstract - extractive body cue:** To address this, we propose 3DS-VLA, which enhances pretrained 2D vision-language models (VLMs) with comprehensive 3D awareness, enabling the prediction of robust end-effector poses.
- **p. 2 / 1 Introduction - extractive body cue:** All these limitations lead us to consider: "How can we build a robust VLA model that incorporates comprehensive 3D spatial awareness?" To address the above ...
- **p. 1 / 1 Introduction - extractive body cue:** However, since robots operate in a complex 3D world, they face challenges in perceiving 3D geometry and reasoning about spatial context solely from 2D image ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | All these limitations lead us to consider: "How can we build a robust VLA model that incorporates comprehensive 3D spatial awareness?" To ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | It takes visual inputs ot = {it, pt}, where it is the image and pt is the point cloud, while language l, ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | takes, visual, inputs, where, image, point, cloud, while, language, keypoints | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Previous, VLA, models, observations, end-effector, poses, often, overlook | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: takes, visual, inputs, where, image, point, cloud, while, language, keypoints | p. 3 (3 Method), p. 3 (3 Method), p. 5 (3 Method) |
| Decision / output variable | action, pose, option or chunk a; body terms: contributions, follows, DS-VLA, equipping, pretrained, VLMs, comprehensive, awareness | p. 2 (1 Introduction), p. 4 (3 Method), p. 2 (1 Introduction) |
| Objective / loss / cost | policy/action modeling objective; cue terms: model, supports, output, DoF, end-effector, pose, single, dual | p. 3 (3 Method), p. 3 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 4 (3 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method) |
| Success / guarantee | instruction-conditioned task success | p. 6 (4 Experiment), p. 7 (4 Experiment), p. 7 (4 Experiment) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** However, since robots operate in a complex 3D world, they face challenges in perceiving 3D geometry and reasoning about spatial context solely from 2D image ...
- **p. 1 / 1 Introduction - extractive body cue:** However, unlike 2D policy models that have access to large-scale datasets, the scarcity of large-scale 3D data limits these methods' scalability in complex robotic environments.
- **p. 2 / 1 Introduction - extractive body cue:** Yet, robotic manipulation requires intricate environmental interactions, and such methods [32, 33, 34, 35, 36] often lack a broader understanding of the robot's action with ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 4 (3 Method), p. 2 (1 Introduction), p. 3 (3 Method), p. 4 (3 Method)): Our contributions are as follows: 1) We propose 3DS-VLA, equipping pretrained 2D VLMs with comprehensive 3D awareness for robust end-effector pose prediction.

- **p. 4 / 3 Method - extractive body cue:** Therefore, we propose a 2D-to-3D positional alignment mechanism that allows the original 2D PEs, which are interpretable to pretrained models, to encode semantically aligned 2D ...
- **p. 2 / 1 Introduction - extractive body cue:** 1 (left), we propose 3DS-VLA, which equips pretrained 2D vision-language models (2D VLMs) with 3D spatial awareness for robust action generation.
- **p. 3 / 3 Method - extractive body cue:** 3.1 Task Formulation and Model Architecture Given a dataset D = {τ1, . . . , τN} of N expert demonstrations, each demonstration τ is ...
- **p. 4 / 3 Method - extractive body cue:** The model π consists of a 2D visual encoder, LLM (LLaMA) [63], a cross-modality projection module [62], and LoRA adapters [64].

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | This makes the pipeline prone to failure if the underlying models are inaccurate-for example, if GroundingDINO [71] misses ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Compared with 2D VLA methods, we observe frequent failures during the critical final stage of 3D contact. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Please refer to Appendix for more details: Section 7.2 for visualization of tasks in RLBench and real world ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 16 | Figure 6: Visualization of real-world tasks. The tasks are shown in key-frame flow. The primary failure mode is ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3 Method), p. 3 (3 Method), p. 5 (3 Method), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), interface p. 3 (3 Method), p. 3 (3 Method), p. 5 (3 Method), p. 2 (1 Introduction), objective p. 3 (3 Method), p. 3 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 4 (3 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, since robots operate in a complex 3D world, they face challenges in perceiving 3D geometry and reasoning about spatial context solely from 2D image observations [12, 13, 14]. (p. 1, 1 Introduction).
- **Formulation-changing contribution:** Our contributions are as follows: 1) We propose 3DS-VLA, equipping pretrained 2D VLMs with comprehensive 3D awareness for robust end-effector pose prediction. (p. 2, 1 Introduction).
- **Assumption/failure evidence:** This makes the pipeline prone to failure if the underlying models are inaccurate-for example, if GroundingDINO [71] misses critical keypoints on the cup handle that needs to be grasped, or ... (p. 8, 4 Experiment).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
