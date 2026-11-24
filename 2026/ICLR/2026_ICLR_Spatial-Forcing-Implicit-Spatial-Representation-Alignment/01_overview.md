# Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2026/hash/d676c05a8fb93ad9231508d95567c498-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/248008. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: Fuhao Li, Wenxuan Song, Han Zhao, Jingbo Wang, Pengxiang Ding, Donglin Wang, Long ZENG, Haoang Li
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, 3D Vision
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/d676c05a8fb93ad9231508d95567c498-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2026/file/d676c05a8fb93ad9231508d95567c498-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

Spatial Forcing은 3차원 기반 모델을 교사로 사용해 RGB 기반 VLA가 행동 예측에 필요한 장면 기하를 내부 특징에 담도록 학습한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/d676c05a8fb93ad9231508d95567c498-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Vision-language-action (VLA) models have recently shown strong potential in enabling robots to follow language instructions and execute precise actions.
- **p. 1 / ABSTRACT - extractive body cue:** However, most VLAs are built upon vision-language models pretrained solely on 2D data, which lack accurate spatial awareness and hinder their ability to operate in ...
- **p. 1 / ABSTRACT - extractive body cue:** Existing solutions attempt to incorporate explicit 3D sensor inputs such as depth maps or point clouds, but these approaches face challenges due to sensor noise, ...
- **p. 1 / ABSTRACT - extractive body cue:** Alternative methods that estimate 3D cues from 2D images also suffer from the limited performance of depth estimators.
- **p. 1 / ABSTRACT - extractive body cue:** We propose Spatial Forcing (SF), a simple yet effective alignment strategy that implicitly forces VLA models to develop spatial comprehension capabilities without relying on explicit ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, some limitations make it difficult to develop a universal and scalable 3D strategy for this paradigm: (1) Reliable 3D
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, the VLM backbones of these 2D VLA models are pretrained solely on 2D visual modalities and lack precise spatial awareness (Wang et al., 2025c), ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To bridge the gap, we propose Spatial Forcing (SF), a simple yet effective alignment strategy that implicitly forces VLA models to acquire spatial-aware knowledge.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Additional experiments on training iterations and dataset sizes indicate that our method realizes 3.8× training while also exhibiting data efficiency with significantly less data.
- **p. 3 / 2.1 PRELIMINARIES - extractive body cue:** The text modality consists of task instructions, which are converted into M linguistic tokens {xL t }M t=1 by a text tokenizer.
- **p. 3 / 2.1 PRELIMINARIES - extractive body cue:** The vision modality consists of multi-view images captured by robots, which are transformed into N visual tokens {xV t }N t=1 through pretrained visual encoders ...
- **p. 5 / 2.1 PRELIMINARIES - extractive body cue:** We evaluate our methods on diverse tasks.
- **원문 대조:** Preliminary formulation에서 action token은 visual token, language token, 앞선 action token에 조건화해 생성된다. 이는 VLA 기본 interface 설명이며 Spatial Forcing의 representation-alignment objective 자체와 구분한다. ([PDF p. 3](https://arxiv.org/pdf/2510.12276#page=3), §2.1 Preliminaries, Eq. (1)).
- **p. 4 / 2.1 PRELIMINARIES - extractive body cue:** To provide the signals with rich spatial information, we first input a set of multi-view images I into the pretrained 3D foundation model VGGT f ...
- **p. 5 / 2.1 PRELIMINARIES - extractive body cue:** The final training objective combines both the standard training loss for action generation and the 3D foundation model alignment loss with a weighting factor α: ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | To provide the signals with rich spatial information, we first input a set of multi-view images I into the pretrained 3D foundation model VGGT f 3D, which outputs the pixel-level spatial representations ... | image/video, language instruction, proprioception과 history | p. 4 (2.1 PRELIMINARIES), p. 1 (1 INTRODUCTION) |
| State/latent | provide, signals, rich, spatial, information, first, input, multi-view, images, pretrained, foundation, model | language-grounded task state와 action-policy context | p. 4 (2.1 PRELIMINARIES), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Output/action | Recently, vision-language-action (VLA) models (Brohan et al., 2022; Zitkovich et al., 2023; Bjorck et al., 2025; Black et al., 2024), capable of instruction following and robotic action execution, have attracted significant attention. | continuous action, pose 또는 action chunk | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective/outcome | The final training objective combines both the standard training loss for action generation and the 3D foundation model alignment loss with a weighting factor α: LSF = Laction + αLalign. | instruction following, task success, generalization과 latency | p. 5 (2.1 PRELIMINARIES), p. 3 (2.1 PRELIMINARIES), p. 3 (2.1 PRELIMINARIES) |

## Main Claims and Actual Contribution

- 기하 교사가 생성한 표현과 VLA 중간층의 시각 특징을 정렬하는 손실을 정책 훈련에 더해, 실행할 때 명시적인 깊이 입력이 필요하지 않게 했다. [PDF 3쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/d676c05a8fb93ad9231508d95567c498-Paper-Conference.pdf#page=3) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/d676c05a8fb93ad9231508d95567c498-Paper-Conference.pdf#page=4)
- 시뮬레이션과 실제 조작에서 행동 성능을 비교하고, 정렬 대상과 학습 자료 규모를 바꿔 기하 감독의 효과를 분석했다. [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/d676c05a8fb93ad9231508d95567c498-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/d676c05a8fb93ad9231508d95567c498-Paper-Conference.pdf#page=6) · [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/d676c05a8fb93ad9231508d95567c498-Paper-Conference.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (2.1 PRELIMINARIES), p. 6 (Figure/Table caption) |
| Embodiment/environment | Given the scarcity of real-world data, this capability is particularly valuable for robotic applications. | hardware/simulator version and reset protocol | p. 8 (2.1 PRELIMINARIES), p. 8 (2.1 PRELIMINARIES) |
| Dataset/benchmark | This ability is critical for real-world deployment. | role, split, size and leakage | p. 8 (2.1 PRELIMINARIES), p. 8 (2.1 PRELIMINARIES), p. 9 (2.1 PRELIMINARIES), p. 9 (2.1 PRELIMINARIES) |
| Metric | (b) We report the success rate vs. training data before and after representation alignment. | definition, denominator, direction and uncertainty | p. 7 (2.1 PRELIMINARIES), p. 8 (2.1 PRELIMINARIES), p. 8 (2.1 PRELIMINARIES) |
| Baseline/ablation | Figure 4: Comparisons with state-of-the-art methods on RoboTwin 2.0 benchmark. LIBERO. Each task is evaluated for 500 trials under random seeds. Tab. 1 shows that SF gets the best performance across all ... | fair input/data/compute/action matching | p. 6 (Figure/Table caption), p. 5 (Figure/Table caption), p. 4 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 2.1 PRELIMINARIES - extractive body cue:** We take OpenVLA-OFT (Kim et al., 2025) as the base model and conduct experiments on the LIBERO benchmark with a single H100 because of limitations ...
- **p. 9 / 5 RELATED WORK - extractive body cue:** However, the reconstruction supervision may not be suitable for VLAs to learn effective representations, as it fails to filter out redundant details (LeCun, 2022; Assran ...
- **p. 6 / 2.1 PRELIMINARIES - extractive body cue:** SigLIP excels at semantic understanding through robust imagetext alignment, whereas DINOv2 offers stronger visual grounding owing to its fine-grained spatial representations.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (2.1 PRELIMINARIES)이다.
