# Problem - AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Li_AT-VLA_Adaptive_Tactile_Injection_for_Enhanced_Feedback_Reaction_in_Vision-Language-Action_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_AT-VLA_Adaptive_Tactile_Injection_for_Enhanced_Feedback_Reaction_in_Vision-Language-Action_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): Since pretrained open-source manipulation datasets rarely include tactile information, researchers [4, 21, 43] often address this limitation by incorporating these modalities during downstream tasks finetuning.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models have significantly advanced the capabilities of robotic agents in executing diverse tasks; however, they still face challenges in contactrich manipulation scenarios that ...
- **p. 1 / Abstract - extractive body cue:** To address this limitation, recent studies have attempted to incorporate tactile signals during downstream tasks, enabling pretrained VLAs to interpret tactile feedback.
- **p. 1 / Abstract - extractive body cue:** Nevertheless, introducing new modalities during finetuning, which are rarely present in the pretrain stage, may disrupt the pretrained capabilities of VLAs.
- **p. 1 / Abstract - extractive body cue:** In addition, the inherently slow inference speed of VLAs hampers real-time responsiveness and limits the effective utilization of tactile feedback for action adjustment.
- **p. 1 / Abstract - extractive body cue:** To overcome these challenges, we propose Adaptive Tactile Vision-Language-Action (AT-VLA), which introduces a novel Adaptive Tactile Injection mechanism.
- **p. 2 / 1. Introduction - extractive body cue:** Since pretrained open-source manipulation datasets rarely include tactile information, researchers [4, 21, 43] often address this limitation by incorporating these modalities during downstream tasks finetuning.
- **p. 2 / 1. Introduction - extractive body cue:** 4) Unlike prior tactilebased policies that heavily rely on tactile inputs, AT-VLA, although trained with tactile feedback, maintains strong performance even in the absence of ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Since pretrained open-source manipulation datasets rarely include tactile information, researchers [4, 21, 43] often address this limitation by incorporating these modalities during ... | contact-rich manipulation scene | body wording is the source claim |
| Observation / input | 2, the policy πθ takes as input the image observations I = {Ih, Ir, Il} from the head camera, right wrist camera, ... | tactile image/force, vision과 proprioceptive history | exact sensor/frame/preprocessing from PDF body |
| State / latent | policy, takes, input, image, observations, head, camera, right, wrist, left | contact geometry, force state 또는 latent dynamics | notation and tensor shape require body check |
| Output / action | Adaptive, Tactile, Vision-Language-Action, AT-VLA, first, time, achieves, balance | grasp/contact action, force command 또는 object motion | exact unit/frame/decoder require body check |
| Target outcome | slip/contact success and safe interaction | slip/contact success, force/pose error와 robustness | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | visual/tactile/proprioceptive contact history; body terms: policy, takes, input, image, observations, head, camera, right, wrist, left | p. 3 (3.1. Framework of AT-VLA), p. 4 (3.2. Adaptive Tactile Injection), p. 2 (1. Introduction) |
| Decision / output variable | contact-aware action/force; body terms: main, contributions, follows, Adaptive, Tactile, Injection, making, first | p. 2 (1. Introduction), p. 4 (3.2. Adaptive Tactile Injection), p. 5 (3.3. Effective Tactile Reaction Dual-Stream) |
| Objective / loss / cost | contact prediction/control error; cue terms: objectives, trained, simultaneously, under, overall, supervision, balance, different | p. 5 (3.4. Training Objectives and Inference Pipeline), p. 4 (3.1. Framework of AT-VLA), p. 4 (3.2. Adaptive Tactile Injection), p. 5 (3.3. Effective Tactile Reaction Dual-Stream) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.2. Adaptive Tactile Injection), p. 4 (3.1. Framework of AT-VLA), p. 5 (3.3. Effective Tactile Reaction Dual-Stream) |
| Success / guarantee | slip/contact success and safe interaction | p. 6 (4.2. Contact-rich Task Evaluation), p. 6 (4.2. Contact-rich Task Evaluation), p. 5 (4.1. Setup) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** 4) Unlike prior tactilebased policies that heavily rely on tactile inputs, AT-VLA, although trained with tactile feedback, maintains strong performance even in the absence of ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 4 (3.2. Adaptive Tactile Injection), p. 5 (3.3. Effective Tactile Reaction Dual-Stream), p. 2 (1. Introduction), p. 4 (3.1. Framework of AT-VLA)): Our main contributions are as follows: 1) We propose Adaptive Tactile Injection, making the first attempt to balance pretrained knowledge with the learning of newly introduced tactile representations.

- **p. 4 / 3.2. Adaptive Tactile Injection - extractive body cue:** Therefore, to address these issues, we propose the Adaptive Tactile Injection module, which dynamically controls when and where tactile feedback is injected and enables the ...
- **p. 5 / 3.3. Effective Tactile Reaction Dual-Stream - extractive body cue:** Concretely, we propose a Tactile Generation strategy, which enables the model to forecast both the 3D normal and tangential forces for the next time step.
- **p. 2 / 1. Introduction - extractive body cue:** Specifically, a learnable Tactile Gate is designed to automatically modulate the contribution of each modality across different manipulation phases, determining whether tactile features should be ...
- **p. 4 / 3.1. Framework of AT-VLA - extractive body cue:** To enable the model to handle contact-rich tasks, we introduce an additional tactile encoder.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | In contrast, our model, although capable of grasping the lid, does not always guarantee a sufficiently firm grip, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Failure to do so may cause the zipper to get stuck or jammed. b). | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | We found that training them on the full sequence often leads to failures during the grasping stage, which ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Figure 4. Visualization. We visualize the execution progress of four typical contact-rich tasks. is crucial for real-world robotic ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

tactile writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3.1. Framework of AT-VLA), p. 4 (3.2. Adaptive Tactile Injection), p. 2 (1. Introduction), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 3 (3.1. Framework of AT-VLA), p. 4 (3.2. Adaptive Tactile Injection), p. 2 (1. Introduction), p. 2 (1. Introduction), objective p. 5 (3.4. Training Objectives and Inference Pipeline), p. 4 (3.1. Framework of AT-VLA), p. 4 (3.2. Adaptive Tactile Injection), p. 5 (3.3. Effective Tactile Reaction Dual-Stream).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** Since pretrained open-source manipulation datasets rarely include tactile information, researchers [4, 21, 43] often address this limitation by incorporating these modalities during downstream tasks finetuning. (p. 2, 1. Introduction).
- **Formulation-changing contribution:** Our main contributions are as follows: 1) We propose Adaptive Tactile Injection, making the first attempt to balance pretrained knowledge with the learning of newly introduced tactile representations. (p. 2, 1. Introduction).
- **Assumption/failure evidence:** In contrast, our model, although capable of grasping the lid, does not always guarantee a sufficiently firm grip, occasionally leading to failure cases where the gripper slips during unscrewing. (p. 6, 4.2. Contact-rich Task Evaluation).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
