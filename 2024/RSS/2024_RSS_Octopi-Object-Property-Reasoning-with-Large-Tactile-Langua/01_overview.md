# Octopi: Object Property Reasoning with Large Tactile-Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2405.02794.
> PDF retrieval source: https://arxiv.org/pdf/2405.02794. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RSS
- Authors: Samson Yu, Kelvin Lin, Anxing Xiao, Jiafei Duan, Harold Soh
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, tactile sensing, Vision-Language, object properties, multimodal reasoning
- Official paper: https://arxiv.org/abs/2405.02794
- Full-text retrieval: https://arxiv.org/pdf/2405.02794
- Code/Project: https://octopi-tactile-lvlm.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Octopi는 촉각 영상을 언어 모델과 결합해 물체의 물리적 속성을 예측하고 이에 대한 질문에 답한다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Physical reasoning is important for effective robot manipulation.
- **p. 1 / Abstract - extractive body cue:** Recent work has investigated both vision and language modalities for physical reasoning; vision can reveal information about objects in the environment and language serves as ...
- **p. 1 / Abstract - extractive body cue:** Although these works have demonstrated success on a variety of physical reasoning tasks, they are limited to physical properties that can be inferred from visual ...
- **p. 1 / Abstract - extractive body cue:** In this work, we investigate combining tactile perception with language, which enables embodied systems to obtain physical properties through interaction and apply commonsense reasoning.
- **p. 1 / Abstract - extractive body cue:** We contribute a new dataset PHYSICLEAR, which comprises both physical/property reasoning tasks and annotated tactile videos obtained using a GelSight tactile sensor.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To bridge this gap, we contribute the PHYSICLEAR dataset, which comprises GelSight images on a variety of real world objects, along with object labels and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Using commonsense reasoning, OCTOPI infers that it is ripe and fulfils the user's request. domain gap between natural images that typical LVLMs are trained with ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** PHYSICLEAR and OCTOPI (with key contributions starred).
- **p. 2 / I. INTRODUCTION - extractive body cue:** Dataset Property Label Availability Property Diversity Object Diversity Material Diversity Hardness Dataset (2016) [59] Yes (only hardness) Yes Yes Medium Clothing Dataset (2018) [61] Yes ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In experiments, we show that OCTOPI is able to use its tactile modality to predict object properties and reason about scenarios including avocado ripeness.
- **p. 1 / Abstract - extractive body cue:** In this work, we investigate combining tactile perception with language, which enables embodied systems to obtain physical properties through interaction and apply commonsense reasoning.
- **p. 4 / III. PHYSICLEAR - TACTILE AND PHYSICAL - extractive body cue:** Our framework consists of CLIP's visual encoder, a projection module with two linear layers, and Vicuna v1.5 as the LLM.
- **p. 4 / IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED - extractive body cue:** We leverage the capabilities of pre-trained vision models, notably the CLIP [39] visual encoder ViT-L/14, as the foundation for our tactile encoder to derive meaningful ...
- **p. 1 / Abstract - extractive body cue:** We then introduce OCTOPI, a system that leverages both tactile representation learning and large vision-language models to predict and reason about tactile inputs with minimal ...
- **p. 6 / IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED - extractive body cue:** Tactile Feature Alignment We discard the fine-tuned CLIP's classification layers and use the outputs from its visual encoder as output embeddings.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | All five tasks use tactile data and natural language instructions as inputs (Table IV). | tactile image/force, vision과 proprioceptive history | p. 4 (III. PHYSICLEAR - TACTILE AND PHYSICAL), p. 1 (I. INTRODUCTION) |
| State/latent | five, tasks, tactile, data, natural, language, instructions, inputs, Table, sensor, OCTOPI, identifies | contact geometry, force state 또는 latent dynamics | p. 4 (III. PHYSICLEAR - TACTILE AND PHYSICAL), p. 1 (I. INTRODUCTION), p. 1 (Abstract) |
| Output/action | Using inputs from its tactile sensor, OCTOPI identifies the left avocado as softer. | grasp/contact action, force command 또는 object motion | p. 1 (I. INTRODUCTION), p. 1 (Abstract), p. 3 (III. PHYSICLEAR - TACTILE AND PHYSICAL) |
| Objective/outcome | Finally, we add three separate classification heads to ViFiCLIP, each of which predicts a label for one property (i.e. hardness, roughness or bumpiness), and train all three classification heads simultaneously using the ... | slip/contact success, force/pose error와 robustness | p. 6 (IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED), p. 6 (3) Can OCTOPI's understanding of the physical properties) |

## Main Claims and Actual Contribution

- PhysiCLeAR에는 GelSight 촉각 영상과 물성 판단을 위한 주석이 들어 있다.
- 중간 물성 예측이 촉각 기반 질의응답에 미치는 영향을 평가한다.

[원문 초록](https://arxiv.org/abs/2405.02794)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (VI. EXPERIMENTAL RESULTS), p. 8 (VI. EXPERIMENTAL RESULTS) |
| Embodiment/environment | To address the above questions, we evaluated OCTOPI using (i) accuracy on the physical understanding tasks in PHYSICLEAR's test set, (ii) accuracy on scenario reasoning tasks, (iii) task success rate on a ... | hardware/simulator version and reset protocol | p. 6 (VI. EXPERIMENTAL RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS) |
| Dataset/benchmark | PG-InstructBLIP was trained to infer a predetermined set of physical properties from visual images of real objects in the EgoObjects dataset [65]. | role, split, size and leakage | p. 6 (VI. EXPERIMENTAL RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS), p. 8 (VI. EXPERIMENTAL RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS) |
| Metric | To address the above questions, we evaluated OCTOPI using (i) accuracy on the physical understanding tasks in PHYSICLEAR's test set, (ii) accuracy on scenario reasoning tasks, (iii) task success rate on a ... | definition, denominator, direction and uncertainty | p. 6 (VI. EXPERIMENTAL RESULTS), p. 8 (VI. EXPERIMENTAL RESULTS), p. 8 (VI. EXPERIMENTAL RESULTS) |
| Baseline/ablation | OCTOPI13b outperforms OCTOPI-7b by 6.96% on PC, 9.33% on PSS and 16.04% on POM. | fair input/data/compute/action matching | p. 7 (VI. EXPERIMENTAL RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS), p. 8 (VI. EXPERIMENTAL RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 8 / VI. EXPERIMENTAL RESULTS - extractive body cue:** This suggests that OCTOPI-13b's physical property prediction capability is robust to differences in tactile exploratory procedures.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. PHYSICLEAR - TACTILE AND PHYSICAL), p. 4 (IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED), p. 1 (Abstract)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** To bridge this gap, we contribute the PHYSICLEAR dataset, which comprises GelSight images on a variety of real world objects, along with object labels and part annotations. (p. 1, I. INTRODUCTION).
- **Actual contribution:** PHYSICLEAR and OCTOPI (with key contributions starred). (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** To address the above questions, we evaluated OCTOPI using (i) accuracy on the physical understanding tasks in PHYSICLEAR's test set, (ii) accuracy on scenario reasoning tasks, (iii) task success rate ... (p. 6, VI. EXPERIMENTAL RESULTS).
- **Explicit failure boundary:** The choice of these specific properties was also informed by the data collection methodology [27], tailored to the limitations and strengths of the GelSight sensor, including considerations for its sensitivity ... (p. 3, III. PHYSICLEAR - TACTILE AND PHYSICAL).

## 원문과 공개 자료

- 게재본 표제면에 따라 Lin Kelvin → Kelvin Lin로 반영했다. [표제면](https://www.roboticsproceedings.org/rss20/p066.pdf#page=1)
- 코드 · 촉각 입력과 언어 모델을 정렬하는 훈련 코드 · train_llm.py [배포 파일](https://raw.githubusercontent.com/clear-nus/octopi/b7f0b0b56a5be950a10c46aa40277dfd51050eab/train_llm.py)
- 가중치 · 7B 구성의 촉각 인코더 · encoder.pt [배포 파일](https://drive.google.com/file/d/1Lb3Hv-Q6gNTbpeabvRj3La035qm6A7WX/view)
- 데이터 · PhysiCLeAR 데이터에서 나무 자에 접촉한 실제 GelSight 영상 · dataset/wood_ruler_3.mov [배포 파일](https://raw.githubusercontent.com/clear-nus/octopi/b7f0b0b56a5be950a10c46aa40277dfd51050eab/dataset/wood_ruler_3.mov)
