# Problem - CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): We outline the robot arm for better visualization. structions, leading to better generalization capabilities when fine-tuned for downstream testing scenarios.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Vision-language-action models (VLAs) have shown potential in leveraging pretrained vision-language models and diverse robot demonstrations for learning generalizable sensorimotor control.
- **p. 1 / Abstract - extractive body cue:** While this paradigm effectively utilizes largescale data from both robotic and non-robotic sources, current VLAs primarily focus on direct input-output mappings, lacking the intermediate reasoning ...
- **p. 1 / Abstract - extractive body cue:** As a result, existing VLAs lack temporal planning or reasoning capabilities.
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce a method that incorporates explicit visual chain-ofthought (CoT) reasoning into vision-language-action models (VLAs) by predicting future image frames autoregressively as ...
- **p. 1 / Abstract - extractive body cue:** We introduce CoT-VLA, a state-ofthe-art 7B VLA that can understand and generate visual and action tokens.
- **p. 1 / 1. Introduction - extractive body cue:** We outline the robot arm for better visualization. structions, leading to better generalization capabilities when fine-tuned for downstream testing scenarios.
- **p. 1 / 1. Introduction - extractive body cue:** Prior VLA models (top) directly predict robot actions from task inputs without explicit reasoning steps and only use action-annotated robot demonstration data for training.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | We outline the robot arm for better visualization. structions, leading to better generalization capabilities when fine-tuned for downstream testing scenarios. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | One promising direction is vision-language-action (VLA) models, which leverage the rich understanding capabilities of pretrained vision-language models (VLMs) to map natural language ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | One, promising, direction, vision-language-action, VLA, models, leverage, rich, understanding, capabilities | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Algorithm, CoT-VLA, test-time, closed-loop, control, Require, Model, initial | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: One, promising, direction, vision-language-action, VLA, models, leverage, rich, understanding, capabilities | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (10. For complete dataset specifications and training hyper) |
| Decision / output variable | action, pose, option or chunk a; body terms: contributions, include, introduce, visual, chain-of-thought, reasoning, through, subgoal | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. The Base Vision-Language Model) |
| Objective / loss / cost | policy/action modeling objective; cue terms: During, training, minimize, cross-entropy, loss, action, predictions, math | p. 4 (3.3. Training Procedures), p. 4 (3.3. Training Procedures) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.3. Training Procedures), p. 4 (3.3. Training Procedures), p. 5 (10. For complete dataset specifications and training hyper) |
| Success / guarantee | instruction-conditioned task success | p. 6 (4.2. Evaluations Results), p. 6 (4.2. Evaluations Results), p. 5 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** Prior VLA models (top) directly predict robot actions from task inputs without explicit reasoning steps and only use action-annotated robot demonstration data for training.
- **p. 2 / 1. Introduction - extractive body cue:** Through extensive experiments in both simulation benchmarks [37] and real-world experiments[48, 60], we demonstrate that our visual chain-of-thought reasoning helps improve policy performance compared to ...
- **p. 2 / 1. Introduction - extractive body cue:** Rather than directly predicting actions, our method first generates a subgoal image that represents the robot's planned state in pixel space, and then conditions its ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. The Base Vision-Language Model)): Our key contributions include: • We introduce a method of visual chain-of-thought reasoning through subgoal image generation as an intermediate reasoning step for robotic control. • We introduce a system ...

- **p. 2 / 1. Introduction - extractive body cue:** Rather than directly predicting actions, our method first generates a subgoal image that represents the robot's planned state in pixel space, and then conditions its ...
- **p. 4 / 3.2. The Base Vision-Language Model - extractive body cue:** This enables autoregressive image and video generation while significantly enhancing the understanding capabilities of VLMs that leverage discrete visual features.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Table 3. Better visual reasoning helps. Success rates compar- ing CoT-VLA using generated versus ground-truth goal images on ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Conclusion, Limitations and Future Work In this work, we introduce CoT-VLA, bridging visionlanguage-action models with chain-of-thought reasoning by ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | By analyzing rollout videos of failure cases, we found that baseline methods occasionally overfit to visual cues while ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Compared to OpenVLA [29], CoT-VLA shows slightly lower success rates in visual and language generalization tasks due to ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (10. For complete dataset specifications and training hyper), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (10. For complete dataset specifications and training hyper), p. 2 (1. Introduction), objective p. 4 (3.3. Training Procedures), p. 4 (3.3. Training Procedures).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
