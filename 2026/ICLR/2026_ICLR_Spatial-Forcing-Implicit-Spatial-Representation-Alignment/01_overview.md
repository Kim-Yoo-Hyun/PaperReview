# Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=euMVC1DO4k.
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
- Source audit: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, some limitations make it difficult to develop a universal and scalable 3D strategy for this paradigm: (1) Reliable 3D를 문제로 두고, To bridge the gap, we propose Spatial Forcing (SF), a simple yet effective alignment strategy that implicitly forces VLA models to acquire spatial-aware knowledge.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To bridge the gap, we propose Spatial Forcing (SF), a simple yet effective alignment strategy that implicitly forces VLA models to acquire spatial-aware knowledge.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Additional experiments on training iterations and dataset sizes indicate that our method realizes 3.8× training while also exhibiting data efficiency with significantly less data.
- **p. 3 / 2.1 PRELIMINARIES - extractive body cue:** The text modality consists of task instructions, which are converted into M linguistic tokens {xL t }M t=1 by a text tokenizer.
- **p. 3 / 2.1 PRELIMINARIES - extractive body cue:** The vision modality consists of multi-view images captured by robots, which are transformed into N visual tokens {xV t }N t=1 through pretrained visual encoders ...
- **p. 5 / 2.1 PRELIMINARIES - extractive body cue:** We evaluate our methods on diverse tasks.
- **p. 9 / 2.1 PRELIMINARIES - extractive body cue:** 6 shows that our SF achieves higher success rates across all tasks, showing considerable improvements in data efficiency.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Comparisons with state-of-the-art methods on RoboTwin 2.0 benchmark. LIBERO. Each task is evaluated for 500 trials under random seeds. Tab. 1 shows that ...
- **p. 8 / 2.1 PRELIMINARIES - extractive body cue:** It also achieves 25.8% higher success rates in terms of the same data amounts and reaches 5.9× more efficient in terms of the same success ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, some limitations make it difficult to develop a universal and scalable 3D strategy for this paradigm: (1) Reliable 3D를 문제로 두고, To bridge the gap, we propose Spatial Forcing (SF), a simple yet effective alignment strategy that implicitly forces VLA models to acquire spatial-aware knowledge.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (2.1 PRELIMINARIES), p. 3 (2.1 PRELIMINARIES) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
