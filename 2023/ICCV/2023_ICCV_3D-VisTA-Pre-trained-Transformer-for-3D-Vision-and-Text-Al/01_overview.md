# 3D-VisTA: Pre-trained Transformer for 3D Vision and Text Alignment

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2308.04352.
> PDF retrieval source: https://arxiv.org/pdf/2308.04352. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / ICCV
- Authors: Ziyu Zhu, Xiaojian Ma, Yixin Chen, Zhidong Deng, Siyuan Huang, Qing Li
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision-Language, alignment, Transformer
- Official paper: https://arxiv.org/abs/2308.04352
- Full-text retrieval: https://arxiv.org/pdf/2308.04352
- Code/Project: https://3d-vista.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The lack of a simple and unified approach creates a significant gap in developing a general-purpose 3D-VL model.를 문제로 두고, Our main contributions can be summarized as follows: • We propose 3D-VisTA, a simple and unified Transformer for aligning 3D vision and text.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D vision-language grounding (3D-VL) is an emerging field that aims to connect the 3D physical world with natural language, which is crucial for achieving embodied ...
- **p. 1 / Abstract - extractive body cue:** Current 3D-VL models rely heavily on sophisticated modules, auxiliary losses, and optimization tricks, which calls for a simple and unified model.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose 3D-VisTA, a pre-trained Transformer for 3D Vision and Text Alignment that can be easily adapted to various downstream tasks.
- **p. 1 / Abstract - extractive body cue:** 3D-VisTA simply utilizes self-attention layers for both single-modal modeling and multi-modal fusion without any sophisticated task-specific design.
- **p. 1 / Abstract - extractive body cue:** To further enhance its performance on 3D-VL tasks, we construct ScanScribe, the first large-scale 3D scene-text pairs dataset for 3D-VL pre-training.
- **p. 1 / 1. Introduction - extractive body cue:** The lack of a simple and unified approach creates a significant gap in developing a general-purpose 3D-VL model.
- **p. 1 / 1. Introduction - extractive body cue:** To fill such gap, we introduce 3D-VisTA, a Transformerbased model for 3D Vision and Text Alignment that can be easily adapted to various downstream tasks.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions can be summarized as follows: • We propose 3D-VisTA, a simple and unified Transformer for aligning 3D vision and text.
- **p. 1 / 1. Introduction - extractive body cue:** To fill such gap, we introduce 3D-VisTA, a Transformerbased model for 3D Vision and Text Alignment that can be easily adapted to various downstream tasks.
- **p. 2 / 1. Introduction - extractive body cue:** Inspired by the success of large-scale pre-training in NLP [15, 41, 42, 6, 52, 31], CV [22, 17, 21, 25, 38], and 2D-VL [30, 2, ...
- **원문 대조:** 기존 3D vision-language 모델은 한두 downstream task와 task-specific 설계에 집중하는 경향이 있다고 설명한다. 왼쪽 column 끝 문장이 오른쪽 column으로 이어지며, 사이에 끼어든 인턴·교신저자 각주는 연구 내용에서 제외했다. ([PDF p. 1](https://arxiv.org/pdf/2308.04352#page=1), §1 Introduction, two-column continuation).
- **p. 4 / 3.4. Self-supervised Pre-training - extractive body cue:** Our final pre-training objective is obtained by simply adding the losses of the proxy tasks above: Lpre-train = LMLM + LMOM + LSTM (5) Notably, ...
- **p. 4 / 3.4. Self-supervised Pre-training - extractive body cue:** However, we mask a 3D object token by only replacing its point features and semantic embedding (i.e., "fi + Wcci" in Eq.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | More specifically, we extract the output corresponds to [CLS] as the global representation of the input scene-text pair, and feed it into a two-layer MLP to predict if the scene and the ... | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3.4. Self-supervised Pre-training), p. 2 (1. Introduction) |
| State/latent | More, specifically, extract, output, corresponds, CLS, global, representation, input, scene-text, pair, feed | geometry, map, object/relationship state | p. 4 (3.4. Self-supervised Pre-training), p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Output/action | It effectively learns the 3D point cloud and text alignment and further simplifies and improves downstream task fine-tuning. • We fine-tune 3D-VisTA and achieve state-of-the-art performances on various 3D-VL tasks, ranging from ... | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | Our final pre-training objective is obtained by simply adding the losses of the proxy tasks above: Lpre-train = LMLM + LMOM + LSTM (5) Notably, the proposed pre-training scheme is self-supervised and ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.4. Self-supervised Pre-training) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions can be summarized as follows: • We propose 3D-VisTA, a simple and unified Transformer for aligning 3D vision and text.
- **p. 1 / 1. Introduction - extractive body cue:** To fill such gap, we introduce 3D-VisTA, a Transformerbased model for 3D Vision and Text Alignment that can be easily adapted to various downstream tasks.
- **p. 2 / 1. Introduction - extractive body cue:** Inspired by the success of large-scale pre-training in NLP [15, 41, 42, 6, 52, 31], CV [22, 17, 21, 25, 38], and 2D-VL [30, 2, ...
- **원문 대조:** 기존 3D vision-language 모델은 한두 downstream task와 task-specific 설계에 집중하는 경향이 있다고 설명한다. 왼쪽 column 끝 문장이 오른쪽 column으로 이어지며, 사이에 끼어든 인턴·교신저자 각주는 연구 내용에서 제외했다. ([PDF p. 1](https://arxiv.org/pdf/2308.04352#page=1), §1 Introduction, two-column continuation).
- **p. 6 / Figure/Table caption - extractive body cue:** Table 4: Grounding accuracy (%) on Nr3D and Sr3D with ground-truth object proposals. ∆denotes the performance difference between 3D-VisTA and 3D-VisTA (scratch). 3D-VisTA achieves competitive ...
- **p. 6 / 5.1. Experimental Settings - extractive body cue:** Mask3D significantly improves the grounding accuracy by providing more accurate object proposals.
- **p. 7 / 5.2. Downstream Task Results - extractive body cue:** Pre-training on ScanScribe significantly improves the performance of 3D-VisTA.
- **p. 7 / 5.2. Downstream Task Results - extractive body cue:** Pretraining improves the results of most question types.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (Figure/Table caption), p. 6 (5.1. Experimental Settings) |
| Embodiment/environment | We evaluate our model on three datasets for this task: ScanRefer [8], Nr3D, and Sr3D [1]. | hardware/simulator version and reset protocol | p. 5 (5.1. Experimental Settings), p. 5 (5.1. Experimental Settings) |
| Dataset/benchmark | Of note, 3DVisTA is trained on these datasets simply using the task losses, without any auxiliary losses or optimization tricks, | role, split, size and leakage | p. 5 (5.1. Experimental Settings), p. 5 (5.1. Experimental Settings), p. 6 (5.2. Downstream Task Results), p. 8 (5.4. Qualitative Studies and Additional Results) |
| Metric | Mask3D significantly improves the grounding accuracy by providing more accurate object proposals. | definition, denominator, direction and uncertainty | p. 6 (5.1. Experimental Settings), p. 5 (5.1. Experimental Settings), p. 6 (Figure/Table caption) |
| Baseline/ablation | 3D-VisTA achieves competitive results with SOTA on Nr3D and outperforms SOTA on Sr3D. | fair input/data/compute/action matching | p. 6 (5.1. Experimental Settings), p. 6 (5.2. Downstream Task Results), p. 7 (5.2. Downstream Task Results) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusion - extractive body cue:** This paper proposes 3D-VisTA, a simple yet effective architecture for 3D-VL tasks.
- **p. 8 / 6. Conclusion - extractive body cue:** The model simply uses selfattention layers and can be easily adapted to various downstream tasks, without requiring any auxiliary loss or optimization trick.
- **p. 8 / 6. Conclusion - extractive body cue:** We also introduce ScanScribe, the first largescale 3D scene-text pairs dataset for 3D-VL pre-training.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The lack of a simple and unified approach creates a significant gap in developing a general-purpose 3D-VL model.를 문제로 두고, Our main contributions can be summarized as follows: • We propose 3D-VisTA, a simple and unified Transformer for aligning 3D vision and text.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.4. Self-supervised Pre-training), p. 4 (3.4. Self-supervised Pre-training), p. 6 (Figure/Table caption) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
