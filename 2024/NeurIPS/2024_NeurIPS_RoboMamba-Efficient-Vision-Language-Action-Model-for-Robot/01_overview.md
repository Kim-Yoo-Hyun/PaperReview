# RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.neurips.cc/paper_files/paper/2024/hash/46a126492ea6fb87410e55a58df2e189-Abstract-Conference.html.
> PDF retrieval source: https://proceedings.neurips.cc/paper_files/paper/2024/hash/46a126492ea6fb87410e55a58df2e189-Abstract-Conference.html. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / NeurIPS
- Authors: Jiaming Liu, Mengzhen Liu, Zhenyu Wang, Pengju An, Xiaoqi Li, Kaichen Zhou, Senqiao Yang, Renrui Zhang, Yandong Guo, Shanghang Zhang
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, VLA, Mamba, SE(3) pose, efficient inference, manipulation
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2024/hash/46a126492ea6fb87410e55a58df2e189-Abstract-Conference.html
- Full-text retrieval: https://proceedings.neurips.cc/paper_files/paper/2024/hash/46a126492ea6fb87410e55a58df2e189-Abstract-Conference.html
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RoboMamba는 시각 인코더와 상태 공간 언어모델을 정렬하고 소형 행동 헤드를 학습해 조작에 필요한 6D 자세를 예측한다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2024/file/46a126492ea6fb87410e55a58df2e189-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** A fundamental objective in robot manipulation is to enable models to comprehend visual scenes and execute actions.
- **p. 1 / Abstract - extractive body cue:** Although existing Vision-Language-Action (VLA) models for robots can handle a range of basic tasks, they still face challenges in two areas: (1) insufficient reasoning ability ...
- **p. 1 / Abstract - extractive body cue:** The recently proposed state space model (SSM) known as Mamba demonstrates promising capabilities in non-trivial sequence modeling with linear inference complexity.
- **p. 1 / Abstract - extractive body cue:** Inspired by this, we introduce RoboMamba, an end-to-end robotic VLA model that leverages Mamba to deliver both robotic reasoning and action capabilities, while maintaining efficient ...
- **p. 1 / Abstract - extractive body cue:** Specifically, we first integrate the vision encoder with Mamba, aligning visual tokens with language embedding through co-training, empowering our model with visual common sense and ...
- **p. 2 / 1.1 Hz - extractive body cue:** While existing MLLM-based policies can handle a range of basic tasks, they still face challenges in two aspects.
- **p. 2 / 1.1 Hz - extractive body cue:** As shown in Figure 1 (reasoning example), this deficiency presents challenges for fine-tuned robot MLLMs when they encounter complex reasoning tasks.

## Core Idea

- **p. 3 / 1.1 Hz - extractive body cue:** In summary, our contributions are as follows: • We introduce RoboMamba, an efficient VLA model that integrates a vision encoder with the linear-complexity Mamba LLM, ...
- **p. 2 / 1.1 Hz - extractive body cue:** Drawing inspiration from this, we raise a question: "Can we develop an efficient robotic VLA model that possesses strong reasoning capabilities while also acquiring robot ...
- **p. 2 / 1.1 Hz - extractive body cue:** Subsequently, we introduce an efficient fine-tuning strategy to equip RoboMamba with pose prediction abilities, requiring a few dozen minutes to fine-tune a simple policy head ...
- **p. 1 / Abstract - extractive body cue:** Inspired by this, we introduce RoboMamba, an end-to-end robotic VLA model that leverages Mamba to deliver both robotic reasoning and action capabilities, while maintaining efficient ...
- **p. 2 / 1 Introduction - extractive body cue:** Manipulation Q: Given <image> Predict the contact point and orientation for pulling the {object} Question: Predict the contact point … RoboMamba Mamba Language Model Tokenizer ...
- **p. 1 / Abstract - extractive body cue:** Specifically, we first integrate the vision encoder with Mamba, aligning visual tokens with language embedding through co-training, empowering our model with visual common sense and ...
- **p. 3 / 1.1 Hz - extractive body cue:** Moreover, RoboMamba achieves an inference speed that is 3 times faster than previous robotic VLA models [29, 15].

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In summary, our contributions are as follows: • We introduce RoboMamba, an efficient VLA model that integrates a vision encoder with the linear-complexity Mamba LLM, which possesses visual common sense and robotic-related ... | image/video, language instruction, proprioception과 history | p. 3 (1.1 Hz), p. 3 (1.1 Hz) |
| State/latent | summary, contributions, follows, introduce, RoboMamba, efficient, VLA, model, integrates, vision, encoder, linear-complexity | language-grounded task state와 action-policy context | p. 3 (1.1 Hz), p. 3 (1.1 Hz), p. 1 (1 Introduction) |
| Output/action | With its strong reasoning abilities, RoboMamba achieves state-of-the-art (SOTA) manipulation performance in the SAPIEN simulation [28], requiring only a 7MB policy head and a few dozen minutes of fine-tuning on a single ... | continuous action, pose 또는 action chunk | p. 3 (1.1 Hz), p. 1 (1 Introduction), p. 2 (1.1 Hz) |
| Objective/outcome | A fundamental objective in robot manipulation is to enable models to comprehend visual scenes and execute actions. | instruction following, task success, generalization과 latency | p. 1 (Abstract), p. 1 (Abstract), p. 2 (1.1 Hz) |

## Main Claims and Actual Contribution

- 시각·언어 공동 학습으로 추론 표현을 얻은 뒤 소수의 정책 파라미터를 조정해 자세 예측에 사용한다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2024/file/46a126492ea6fb87410e55a58df2e189-Paper-Conference.pdf#page=1) · [PDF 5쪽](https://proceedings.neurips.cc/paper_files/paper/2024/file/46a126492ea6fb87410e55a58df2e189-Paper-Conference.pdf#page=5)
- 일반·로봇 추론 벤치마크와 시뮬레이션·실물의 자세 예측을 평가하고 추론 속도도 비교했다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2024/file/46a126492ea6fb87410e55a58df2e189-Paper-Conference.pdf#page=1) · [PDF 7쪽](https://proceedings.neurips.cc/paper_files/paper/2024/file/46a126492ea6fb87410e55a58df2e189-Paper-Conference.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4 Experiment), p. 9 (4 Experiment) |
| Embodiment/environment | Datasets (Stage 2) For the dataset used in the robot manipulation fine-tuning stage, we follow the data collection process of previous works [61, 15], adopting the SAPIEN engine [28] to set up ... | hardware/simulator version and reset protocol | p. 7 (4 Experiment), p. 7 (4 Experiment) |
| Dataset/benchmark | To comprehensively compare RoboMamba's robotic-related reasoning abilities, we benchmark it against LLaMA-AdapterV2 [45] and TinyLLaVA [83] on the RoboVQA [27] validation set. | role, split, size and leakage | p. 7 (4 Experiment), p. 7 (4 Experiment), p. 8 (4 Experiment), p. 10 (4 Experiment) |
| Metric | To measure the model's performance, we use the classical manipulation success rate, defined as the ratio of successfully manipulated samples to the total test samples. | definition, denominator, direction and uncertainty | p. 7 (4 Experiment), p. 9 (Figure/Table caption), p. 7 (4 Experiment) |
| Baseline/ablation | We choose LLaMA-AdapterV2 as a baseline because it serves as the base model for the current state-of-the-art (SOTA) robot MLLM, ManipLLM [15]. | fair input/data/compute/action matching | p. 8 (4 Experiment), p. 7 (4 Experiment), p. 8 (4 Experiment) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 4 Experiment - extractive body cue:** Prediction of past and future actions is crucial in robotic manipulation, as it not only enables effective rethinking of past failure actions but also enhances ...
- **p. 10 / 4 Experiment - extractive body cue:** Meanwhile, as shown in Figure 5, we also visualize the failure cases of RoboMamba's predictions in both reasoning and manipulation tasks.
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 6: The visualization of reasoning failure cases. In the bottom right corner of the image, we re-select the qualitative results from our real-world demonstration. ...
- **p. 17 / A Appendix - extractive body cue:** Due to space limitations, we provide additional details of the proposed method in this supplementary material.
- **p. 9 / 4 Experiment - extractive body cue:** The results confirm our finding: fine-tuning an MLLM to learn robot skills does not require extensive resources; it only requires that the MLLM possesses strong ...
- **p. 8 / 4 Experiment - extractive body cue:** Specifically, our model achieves satisfactory results on the POPE benchmark, helping to reduce failed robot actions caused by hallucinations.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1.1 Hz), p. 1 (1 Introduction), p. 3 (1.1 Hz), p. 1 (Abstract), p. 2 (1 Introduction)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (26 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** While existing MLLM-based policies can handle a range of basic tasks, they still face challenges in two aspects. (p. 2, 1.1 Hz).
- **Actual contribution:** Drawing inspiration from this, we raise a question: "Can we develop an efficient robotic VLA model that possesses strong reasoning capabilities while also acquiring robot manipulation skills in a cost-effective ... (p. 2, 1.1 Hz).
- **Evaluation boundary:** 4.5 Real-world experiments As shown in Figure 4, we visualize RoboMamba's reasoning results across various robotic downstream tasks. (p. 10, 4 Experiment).
- **Explicit failure boundary:** Or a speech-to-text system might not be used reliably to provide closed captions for online lectures because it fails to handle technical jargon. • The authors should discuss the computational ... (p. 21, 2. Limitations).
