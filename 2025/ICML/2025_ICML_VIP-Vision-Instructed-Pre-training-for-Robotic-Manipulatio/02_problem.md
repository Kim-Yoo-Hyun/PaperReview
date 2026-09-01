# Problem - VIP: Vision Instructed Pre-training for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ccUNMIbpcf; PDF retrieval source: https://openreview.net/pdf/fc80bd3b42c458d1d871411db0d2aec7f70c9c37.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): 1, the text instructed policy fails to concentrate on the green block specified in the text instruction, and the robot hand often grasps a block in a false color.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** The effectiveness of scaling up training data in robotic manipulation is still limited.
- **p. 1 / Abstract - extractive PDF cue:** A primary challenge in manipulation is the tasks are diverse, and the trained policy would be confused if the task targets are not specified clearly.
- **p. 1 / Abstract - extractive PDF cue:** Existing works primarily rely on text instruction to describe targets.
- **p. 1 / Abstract - extractive PDF cue:** However, we reveal that current robotic data cannot train policies to understand text instruction effectively, and vision is much more comprehensible.
- **p. 1 / Abstract - extractive PDF cue:** Therefore, we introduce utilizing vision instruction to specify targets.
- **p. 1 / 1. Introduction - extractive PDF cue:** 1, the text instructed policy fails to concentrate on the green block specified in the text instruction, and the robot hand often grasps a block ...
- **p. 1 / 1. Introduction - extractive PDF cue:** However, we find that existing manipulation data is not diverse sufficiently to train a policy to own this capability, which demands millions of image-text pairs ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | 1, the text instructed policy fails to concentrate on the green block specified in the text instruction, and the robot hand often ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | A natural idea of using vision instruction is feeding the policy with future images besides the current observation, and the policy is ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | natural, idea, vision, instruction, feeding, policy, future, images, besides, current | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Vision, Observation, Text, Instruction, Pick, green, block, Instructed | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: natural, idea, vision, instruction, feeding, policy, future, images, besides, current | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Decision / output variable | action, pose, option or chunk a; body terms: specify, manipulation, procedures, clearly, while, maintaining, acceptable, computational | p. 2 (1. Introduction), p. 3 (3.1. Vision Intructed Pre-training), p. 5 (3.3. Vision Instruction after Pre-train) |
| Objective / loss / cost | policy/action modeling objective; cue terms: optimize, pre-trained, policy, minimizing, loss, constructed, Therefore, employing | p. 4 (3.1. Vision Intructed Pre-training), p. 5 (3.2. Sparse Point Flow) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.1. Vision Intructed Pre-training), p. 4 (3.2. Sparse Point Flow), p. 5 (3.2. Sparse Point Flow) |
| Success / guarantee | instruction-conditioned task success | p. 7 (4.1. VIP Effectiveness), p. 7 (4.1. VIP Effectiveness), p. 8 (4.3. Method Analysis) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** However, we find that existing manipulation data is not diverse sufficiently to train a policy to own this capability, which demands millions of image-text pairs ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To handle the lack of sparse point flows, we progressively remove them during pre-training by random masking.
- **p. 2 / 1. Introduction - extractive PDF cue:** This design gradually boosts the action prediction challenge and helps the policy learn more meaningful representation (Oquab et al., 2024).

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 3 (3.1. Vision Intructed Pre-training), p. 5 (3.3. Vision Instruction after Pre-train), p. 5 (3.3. Vision Instruction after Pre-train), p. 2 (1. Introduction)): To specify the manipulation procedures clearly while maintaining an acceptable computational burden, we propose to represent the intermediate action information with sparse point flows.

- **p. 3 / 3.1. Vision Intructed Pre-training - extractive PDF cue:** A data sample for robotic manipulation pre-training consists of two parts, a video sequence V = {I1, I2, · · · , IT } and ...
- **p. 5 / 3.3. Vision Instruction after Pre-train - extractive PDF cue:** 2, the vision instruction in pretraining consists of two parts, the future frame and sparse point flows.
- **p. 5 / 3.3. Vision Instruction after Pre-train - extractive PDF cue:** To bridge this gap, we propose to replace the future frame in pre-training as the cropped image region of the object to manipulate during fine-tuning ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Additionally, this design enables us to specify the object manipulation order dynamically.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Robustness analysis of VIRT to different disturbances, e.g., brightness change, vision noise, and image blur. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | For ConvMLP, its primary problem is its output head is a naive MLP, which is fast but fails ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | This part analyzes the robustness of VIRT to different unseen environment disturbances. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | According to the results, we can find that solely using a future image or sparse point flows does ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1. Vision Intructed Pre-training). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1. Vision Intructed Pre-training), objective p. 4 (3.1. Vision Intructed Pre-training), p. 5 (3.2. Sparse Point Flow).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
