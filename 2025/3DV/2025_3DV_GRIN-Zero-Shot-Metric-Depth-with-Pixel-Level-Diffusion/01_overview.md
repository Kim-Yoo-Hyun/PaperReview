# GRIN: Zero-Shot Metric Depth with Pixel-Level Diffusion

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/.
> PDF retrieval source: https://openreview.net/attachment?id=VSG65wVNuL&name=pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / 3DV
- Authors: Vitor Campagnolo Guizilini, Pavel Tokmakov, Achal Dave, Rares Andrei Ambrus
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Diffusion, Generation, depth, 3D Vision
- Official paper: https://3dvconf.github.io/2025/schedule_updated2.csv
- Full-text retrieval: https://arxiv.org/pdf/2409.09896.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 The challenges with this approach are two-fold: (i) the choice of priors themselves, that should Figure 1.를 문제로 두고, In summary, our contributions are as follows: • We introduce GRIN, a novel diffusion-based monocular depth estimation framework designed to (i) ingest sparse training data, enabling the use of larger and more ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D reconstruction from a single image is a long-standing problem in computer vision.
- **p. 1 / Abstract - extractive body cue:** Learning-based methods address its inherent scale ambiguity by leveraging increasingly large labeled and unlabeled datasets, to produce geometric priors capable of generating accurate predictions across ...
- **p. 1 / Abstract - extractive body cue:** As a result, state of the art approaches show impressive performance in zero-shot relative and metric depth estimation.
- **p. 1 / Abstract - extractive body cue:** Recently, diffusion models have exhibited remarkable scalability and generalizable properties in their learned representations.
- **p. 1 / Abstract - extractive body cue:** However, because these models repurpose tools originally designed for image generation, they can only operate on dense ground-truth, which is not available for most depth ...
- **p. 1 / 1. Introduction - extractive body cue:** The challenges with this approach are two-fold: (i) the choice of priors themselves, that should Figure 1.
- **p. 1 / 1. Introduction - extractive body cue:** In order to fully leverage these geometric priors we turn to diffusion models [31], due to their scalability to large-scale diverse datasets and strong regression ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are as follows: • We introduce GRIN, a novel diffusion-based monocular depth estimation framework designed to (i) ingest sparse training data, ...
- **p. 2 / 1. Introduction - extractive body cue:** We propose several key modifications to this original framework to apply it to the task of depth estimation, including the use of 3D geometric positional ...
- **p. 3 / 3. Diffusion Preliminaries - extractive body cue:** Capitalizing on these benefits, in the next section we introduce our approach for zero shot metric depth estimation with pixel-level diffusion.
- **p. 3 / 3. Diffusion Preliminaries - extractive body cue:** (b) A RIN model consists of B blocks, each receiving latent Zb and input Xb tokens from the previous block and returning updated Zb+1 and ...
- **p. 4 / 4.1. Sparse Unstructured Training - extractive body cue:** To address these limitations we propose a combination of local and global conditioning which promote training with unstructured sparse data while still maintaining dense scene-level ...
- **원문 대조:** Log-depth 공간에서 주입 잡음 N_t에 noise schedule γ(t)를 적용한 값과 예측 잡음의 차이에 L2 손실을 적용한다. N_t는 표준 정규분포, t는 U(0,1)에서 샘플링한다. ([PDF p. 5](https://arxiv.org/pdf/2409.09896#page=5), §4.4 Training Procedure).
- **p. 5 / 4.4. Training Procedure - extractive body cue:** To improve iteration speed, we also randomly discard a percentage of valid local vectors, thus only supervising on a subset of L pixels, which leads ...
- **p. 4 / 4.1. Sparse Unstructured Training - extractive body cue:** Concretely, during training, we assume ground-truth in the form of a 2D grid D ∈RH×W with N < HW valid pixels.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (a) Latent tokens Zin read from input tokens Xin, are processed via a series of self-attention layers, and written back to output tokens Xout. | conditioning observation와 noisy/intermediate sample | p. 3 (3. Diffusion Preliminaries), p. 2 (1. Introduction) |
| State/latent | Latent, tokens, Zin, read, input, Xin, processed, series, self-attention, layers, written, back | latent/noise variable와 conditional distribution | p. 3 (3. Diffusion Preliminaries), p. 2 (1. Introduction), p. 3 (3. Diffusion Preliminaries) |
| Output/action | In summary, our contributions are as follows: • We introduce GRIN, a novel diffusion-based monocular depth estimation framework designed to (i) ingest sparse training data, enabling the use of larger and more ... | generated sample, action chunk 또는 trajectory | p. 2 (1. Introduction), p. 3 (3. Diffusion Preliminaries), p. 1 (1. Introduction) |
| Training objective | 원문 대조: Log-depth 공간에서 주입 잡음 N_t에 noise schedule γ(t)를 적용한 값과 예측 잡음의 차이에 L2 손실을 적용한다. N_t는 표준 정규분포, t는 U(0,1)에서 샘플링한다. ([PDF p. 5](https://arxiv.org/pdf/2409.09896#page=5), §4.4 Training Procedure) | Noise regression; latency 결과는 별도 근거 필요 | [PDF p. 5](https://arxiv.org/pdf/2409.09896#page=5), §4.4 Training Procedure |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are as follows: • We introduce GRIN, a novel diffusion-based monocular depth estimation framework designed to (i) ingest sparse training data, ...
- **p. 2 / 1. Introduction - extractive body cue:** We propose several key modifications to this original framework to apply it to the task of depth estimation, including the use of 3D geometric positional ...
- **p. 3 / 3. Diffusion Preliminaries - extractive body cue:** Capitalizing on these benefits, in the next section we introduce our approach for zero shot metric depth estimation with pixel-level diffusion.
- **p. 3 / 3. Diffusion Preliminaries - extractive body cue:** (b) A RIN model consists of B blocks, each receiving latent Zb and input Xb tokens from the previous block and returning updated Zb+1 and ...
- **p. 4 / 4.1. Sparse Unstructured Training - extractive body cue:** To address these limitations we propose a combination of local and global conditioning which promote training with unstructured sparse data while still maintaining dense scene-level ...
- **p. 7 / 5.3. Zero-Shot Metric Depth Estimation - extractive body cue:** We believe GRIN could be modified to operate in a similar setting, which would potentially further improve performance, however this is left for future work.
- **p. 7 / 5.4. Zero-Shot Relative Depth Estimation - extractive body cue:** Results of this experiment are shown in Table 2, indicating that GRIN also outperforms the current state-of-the-art in relative depth estimation across multiple datasets, with ...
- **p. 8 / 5.5. Fine-Tuning Experiments - extractive body cue:** Results are shown in Table 3, indicating that GRIN also outperforms other metric depth estimation methods that use in-domain training data.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (5.3. Zero-Shot Metric Depth Estimation), p. 7 (5.4. Zero-Shot Relative Depth Estimation) |
| Embodiment/environment | We trained GRIN using a diverse combination of indoor and outdoor datasets from both real-world and syn | hardware/simulator version and reset protocol | p. 5 (5.1. Training Datasets), p. 6 (5.1. Training Datasets) |
| Dataset/benchmark | The remaining 80k steps used all training datasets, shuffled to ensure a similar ratio of indoor and outdoor samples per batch, as well as real-world and synthetic samples. | role, split, size and leakage | p. 5 (5.1. Training Datasets), p. 6 (5.1. Training Datasets), p. 6 (5.2. Implementation Details), p. 7 (5.3. Zero-Shot Metric Depth Estimation) |
| Metric | We believe GRIN could be modified to operate in a similar setting, which would potentially further improve performance, however this is left for future work. | definition, denominator, direction and uncertainty | p. 7 (5.3. Zero-Shot Metric Depth Estimation), p. 8 (5.4. Zero-Shot Relative Depth Estimation), p. 8 (5.4. Zero-Shot Relative Depth Estimation) |
| Baseline/ablation | Results of this experiment are shown in Table 2, indicating that GRIN also outperforms the current state-of-the-art in relative depth estimation across multiple datasets, with the added benefit that it can also ... | fair input/data/compute/action matching | p. 7 (5.4. Zero-Shot Relative Depth Estimation), p. 6 (5.1. Training Datasets), p. 7 (5.3. Zero-Shot Metric Depth Estimation) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 6. Conclusion - extractive body cue:** Interestingly, these uncertainty maps also accurately detect failure cases of our model, such as the mirror on the bottom of the second column, due to ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Zero-shot metric monocular depth estimation results on various indoor and outdoor datasets. Numbers in italics indicate results obtained by evaluating specific methods on ...
- **p. 9 / 6. Conclusion - extractive body cue:** We then provide additional architecture details in Section C, and in Section D we discuss potential limitations of our architecture.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Recurrent Interface Networks (RIN) architecture. (a) Latent tokens Zin read from input tokens Xin, are processed via a series of self-attention layers, and ...
- **p. 7 / 5.3. Zero-Shot Metric Depth Estimation - extractive body cue:** We believe GRIN could be modified to operate in a similar setting, which would potentially further improve performance, however this is left for future work.
- **p. 7 / 5.4. Zero-Shot Relative Depth Estimation - extractive body cue:** In this setting, camera intrinsics are not required, since the model does not need to reason over physical 3D properties of the environment, focusing instead ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Diagram of GRIN for monocular depth estimation. An input image I with intrinsics K is used to condition the diffusion process both locally, ...

## Why Read It

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 The challenges with this approach are two-fold: (i) the choice of priors themselves, that should Figure 1.를 문제로 두고, In summary, our contributions are as follows: • We introduce GRIN, a novel diffusion-based monocular depth estimation framework designed to (i) ingest sparse training data, enabling the use of larger and more ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Diffusion Preliminaries), p. 4 (4.1. Sparse Unstructured Training) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
