# CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: Qingqing Zhao, Yao Lu, Moo Jin Kim, Zipeng Fu, Zhuoyang Zhang, Yecheng Wu, Zhaoshuo Li, Qianli Ma, Song Han, Chelsea Finn, Ankur Handa, Tsung-Yi Lin, Gordon Wetzstein, Ming-Yu Liu, Donglai Xiang
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Chain-of-Thought, Robotics
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf) 기준이다.

## Why This Paper Is Here

CoT-VLA는 언어 지시를 받은 로봇이 도달할 중간 목표 이미지를 먼저 생성한 뒤 이를 조건으로 짧은 행동열을 예측한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-language-action models (VLAs) have shown potential in leveraging pretrained vision-language models and diverse robot demonstrations for learning generalizable sensorimotor control.
- **p. 1 / Abstract - extractive body cue:** While this paradigm effectively utilizes largescale data from both robotic and non-robotic sources, current VLAs primarily focus on direct input-output mappings, lacking the intermediate reasoning ...
- **p. 1 / Abstract - extractive body cue:** As a result, existing VLAs lack temporal planning or reasoning capabilities.
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce a method that incorporates explicit visual chain-ofthought (CoT) reasoning into vision-language-action models (VLAs) by predicting future image frames autoregressively as ...
- **p. 1 / Abstract - extractive body cue:** We introduce CoT-VLA, a state-ofthe-art 7B VLA that can understand and generate visual and action tokens.
- **p. 1 / 1. Introduction - extractive body cue:** We outline the robot arm for better visualization. structions, leading to better generalization capabilities when fine-tuned for downstream testing scenarios.
- **p. 1 / 1. Introduction - extractive body cue:** Prior VLA models (top) directly predict robot actions from task inputs without explicit reasoning steps and only use action-annotated robot demonstration data for training.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our key contributions include: • We introduce a method of visual chain-of-thought reasoning through subgoal image generation as an intermediate reasoning step for robotic control. ...
- **p. 2 / 1. Introduction - extractive body cue:** Rather than directly predicting actions, our method first generates a subgoal image that represents the robot's planned state in pixel space, and then conditions its ...
- **p. 4 / 3.2. The Base Vision-Language Model - extractive body cue:** This enables autoregressive image and video generation while significantly enhancing the understanding capabilities of VLMs that leverage discrete visual features.
- **p. 4 / 3.2. The Base Vision-Language Model - extractive body cue:** We use the VILA-U model trained on 256 × 256 resolution images, where each image is encoded into 16 × 16 × 4 tokens with ...
- **p. 4 / 3.2. The Base Vision-Language Model - extractive body cue:** VILA-U utilizes residual quantization [32] to improve the representational capacity of discrete visual features - incorporating a depth transformer, as introduced in RQ-VAE [32], to ...
- **p. 5 / 10. For complete dataset specifications and training hyper - extractive body cue:** Algorithm 1 CoT-VLA test-time closed-loop control Require: CoT-VLA Model Pθ, initial state sobs 0 , language instruction l 0: t ←0 0: while True do ...
- **p. 5 / 10. For complete dataset specifications and training hyper - extractive body cue:** During this phase, we optimize the LLM backbone, projector, and depth transformer while keeping the vision tower frozen, maintaining the same training setup as the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | One promising direction is vision-language-action (VLA) models, which leverage the rich understanding capabilities of pretrained vision-language models (VLMs) to map natural language instructions and visual observations to robot actions ... | image/video, language instruction, proprioception과 history | p. 1 (1. Introduction), p. 2 (1. Introduction) |
| State/latent | One, promising, direction, vision-language-action, VLA, models, leverage, rich, understanding, capabilities, pretrained, vision-language | language-grounded task state와 action-policy context | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (10. For complete dataset specifications and training hyper) |
| Output/action | Rather than directly predicting actions, our method first generates a subgoal image that represents the robot's planned state in pixel space, and then conditions its action on both the current observation and ... | continuous action, pose 또는 action chunk | p. 2 (1. Introduction), p. 5 (10. For complete dataset specifications and training hyper), p. 2 (1. Introduction) |
| Objective/outcome | During training, we minimize the cross-entropy loss for action predictions: \math c a l | instruction following, task success, generalization과 latency | p. 4 (3.3. Training Procedures), p. 4 (3.3. Training Procedures), p. 5 (10. For complete dataset specifications and training hyper) |

## Main Claims and Actual Contribution

- 하나의 모형 안에서 중간 목표 영상 생성과 행동 예측에 서로 다른 어텐션 패턴을 적용했다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf#page=4)
- 시뮬레이션과 실제 로봇 조작에서 중간 목표 생성을 포함한 정책을 비교하고 영상 자료 및 학습 구성의 역할을 조사했다. [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Embodiment/environment | We conduct evaluations across three complementary settings: the LIBERO benchmark [37] for evaluation in simulation environments, the Bridge-V2 platform [60] with its dataset of 45k robot demonstrations, and the Franka-Tabletop setup wit ... | hardware/simulator version and reset protocol | p. 5 (4.1. Experimental Setup), p. 5 (4. Experiments) |
| Dataset/benchmark | Pretraining Our training pipeline has two stages, pretraining VILA-U on the OpenX dataset augmented with actionless video data (Section 3.3), and task-specific post-training on robot demonstration data. | role, split, size and leakage | p. 5 (4.1. Experimental Setup), p. 5 (4. Experiments), p. 7 (4.3. Ablation Study), p. 6 (4.1. Experimental Setup) |
| Metric | Success rates are reported with means and standard error. | definition, denominator, direction and uncertainty | p. 6 (4.2. Evaluations Results), p. 6 (4.2. Evaluations Results), p. 5 (Figure/Table caption) |
| Baseline/ablation | Our experiments aim to addresses following questions: • How does our system perform compared to state-of-the-art baselines across multiple benchmarks and embodiments? | fair input/data/compute/action matching | p. 5 (4. Experiments), p. 6 (4.2. Evaluations Results), p. 6 (4.2. Evaluations Results) |

## Explicit Limitations and Failure Boundary

- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Better visual reasoning helps. Success rates compar- ing CoT-VLA using generated versus ground-truth goal images on out-of-distribution tasks. Results demonstrate that improved visual ...
- **p. 8 / 4.4. Better Visual Reasoning Helps - extractive body cue:** Conclusion, Limitations and Future Work In this work, we introduce CoT-VLA, bridging visionlanguage-action models with chain-of-thought reasoning by introducing intermediate visual goals as explicit reasoning ...
- **p. 6 / 4.2. Evaluations Results - extractive body cue:** By analyzing rollout videos of failure cases, we found that baseline methods occasionally overfit to visual cues while disregarding language instructions.
- **p. 6 / 4.2. Evaluations Results - extractive body cue:** Compared to OpenVLA [29], CoT-VLA shows slightly lower success rates in visual and language generalization tasks due to grasping failures from action chunking (see Section ...
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** Following [29], we evaluate on four tasks designed in [29] to evaluate visual robustness (varying distractors), motion generalization (novel object positions), semantic generalization (unseen language ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. The Base Vision-Language Model)이다.
