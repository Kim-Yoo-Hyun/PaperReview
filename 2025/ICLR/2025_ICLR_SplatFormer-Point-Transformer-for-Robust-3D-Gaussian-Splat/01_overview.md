# SplatFormer: Point Transformer for Robust 3D Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/8cbde11e5e271ef9ff67fc9f292e43ed-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/111734. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: Yutong Chen, Marko Mihajlovic, Xiyi Chen, Yiming Wang, Sergey Prokudin, Siyu Tang
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, point cloud, 3D Vision, Transformer
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/8cbde11e5e271ef9ff67fc9f292e43ed-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2025/file/8cbde11e5e271ef9ff67fc9f292e43ed-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://proceedings.iclr.cc/paper_files/paper/2025/file/8cbde11e5e271ef9ff67fc9f292e43ed-Paper-Conference.pdf)

## Why This Paper Is Here

SplatFormer는 기존 가우시안 장면을 점 집합으로 처리해 학습 카메라 분포에서 크게 벗어난 시점의 렌더링을 개선한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/8cbde11e5e271ef9ff67fc9f292e43ed-Paper-Conference.pdf#page=1) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/8cbde11e5e271ef9ff67fc9f292e43ed-Paper-Conference.pdf#page=6)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** 3D Gaussian Splatting (3DGS) has recently transformed photorealistic reconstruction, achieving high visual fidelity and real-time performance.
- **p. 1 / ABSTRACT - extractive body cue:** However, rendering quality significantly deteriorates when test views deviate from the camera angles used during training, posing a major challenge for applications in immersive free-viewpoint ...
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we conduct a comprehensive evaluation of 3DGS and related novel view synthesis methods under out-ofdistribution (OOD) test camera scenarios.
- **p. 1 / ABSTRACT - extractive body cue:** By creating diverse test cases with synthetic and real-world datasets, we demonstrate that most existing methods, including those incorporating various regularization techniques and data-driven priors, ...
- **p. 1 / ABSTRACT - extractive body cue:** To address this limitation, we introduce SplatFormer, the first point transformer model specifically designed to operate on Gaussian splats.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** 1, existing NVS methods perform poorly on the OOD views when restricted to low-elevation inputs, highlighting the need for a novel approach to address this ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Existing NVS methods, including MipNeRF360 (Barron et al., 2022), and those designed for sparse inputs like LaRa (Chen et al., 2024a), face challenges in this ...

## Core Idea

- **p. 3 / 1 INTRODUCTION - extractive body cue:** In summary, we make the following contributions: • We introduce OOD-NVS, a new experimental protocol specifically designed to evaluate the performance of NVS methods when ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To meet these needs, we propose SplatFormer, a novel learning-based feed-forward 3D transformer designed to operate on Gaussian splats.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Existing NVS methods, including MipNeRF360 (Barron et al., 2022), and those designed for sparse inputs like LaRa (Chen et al., 2024a), face challenges in this ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our results demonstrate that existing methods struggle to generalize under the OOD-NVS protocol; • We propose SplatFormer, a novel learning-based model that refines flawed 3D ...
- **p. 15 / B IMPLEMENTATION DETAILS - extractive body cue:** Each MLP branch consists of four linear layers, with hidden dimensions of 512 and ReLU activations for all but the last layer.
- **p. 15 / B IMPLEMENTATION DETAILS - extractive body cue:** The feature decoder is composed of five separate MLP branches, which are responsible for predicting the residuals for the means, opacity, quaternion, scales, and spherical ...
- **p. 16 / B IMPLEMENTATION DETAILS - extractive body cue:** For the training of our full model, we use 8 RTX4090s with one scene per GPU, set gradient accumulation steps as 4, and train for ...
- **p. 15 / B IMPLEMENTATION DETAILS - extractive body cue:** The point transformer encoder begins with an MLP embedding layer, followed by five down-pooling and four up-pooling stages, ultimately producing features with a dimensionality of ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | It outputs residuals that are added to the input Gaussian attributes. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| State/latent | outputs, residuals, added, input, Gaussian, attributes, While, initial, representation, effectively, integrates, multi-view | geometry, map, object/relationship state | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Output/action | While this initial 3D representation effectively integrates multi-view information from the captured images, we observe that the shapes, appearances, and spatial structure of the Gaussian splats become biased toward the input view ... | point map, pose, scene graph, affordance 또는 query result | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 16 (B IMPLEMENTATION DETAILS) |
| Objective/outcome | To reduce computational costs, we terminate the optimization early at 10k steps, where evaluation performance levels off. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 16 (B IMPLEMENTATION DETAILS), p. 16 (B IMPLEMENTATION DETAILS) |

## Main Claims and Actual Contribution

- 기존 가우시안을 점 트랜스포머에 입력해 속성을 갱신하고, 훈련 뷰 주변에서는 보이지 않던 왜곡을 줄이도록 여러 장면에서 학습한다. [PDF 3쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/8cbde11e5e271ef9ff67fc9f292e43ed-Paper-Conference.pdf#page=3) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/8cbde11e5e271ef9ff67fc9f292e43ed-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/8cbde11e5e271ef9ff67fc9f292e43ed-Paper-Conference.pdf#page=6)
- 합성 및 실제 자료에서 일반 보간 뷰와 분포 밖 카메라 뷰를 구분해 비교하고 다른 데이터셋에 전이되는지도 시험했다. [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/8cbde11e5e271ef9ff67fc9f292e43ed-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/8cbde11e5e271ef9ff67fc9f292e43ed-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/8cbde11e5e271ef9ff67fc9f292e43ed-Paper-Conference.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS) |
| Embodiment/environment | Following the OOD-NVS protocol, we rendered 20 objects from Google Scanned Objects (GSO) (Downs et al., 2022) and captured 4 real-world scenes. | hardware/simulator version and reset protocol | p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Dataset/benchmark | Even on the real-world dataset, despite being trained exclusively on synthetic data, SplatFormer reduces artifacts. | role, split, size and leakage | p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Metric | To demonstrate this, we evaluate NVS with elevations ϕ ∈[10◦, 90◦] in Objaverse-OOD scenes and compare SplatFormer to 3DGS (Fig. | definition, denominator, direction and uncertainty | p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS) |
| Baseline/ablation | Our method also outperforms MipNeRF360 and 2DGS, the best-performing baselines in Objaverse-OOD (Tab. | fair input/data/compute/action matching | p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 6 CONCLUSION - extractive body cue:** In this work, we introduced a new out-of-distribution (OOD) novel view synthesis test scenario and demonstrated that most neural rendering methods, including those using regularization ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** Our method has several limitations that provide directions for future work.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: Limitations of 3DGS in OOD-NVS setup. We observe that the quality of novel views obtained via 3DGS significantly deteriorates as the test camera ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Finally, we discuss the limitations of our approach and potential directions for future research.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Method Overview. We introduce SplatFormer, a generalizable 3D point transformer network designed for feed-forward refinement of Gaussian splats, enabling robust out-of-distribution novel-view synthesis ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** While 3DGS performance degrades significantly as the viewing angle deviates from the input views, our method provides more robust synthesis for target views in the ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Our method does not overfit to the extreme top views present in the SplatFormer training set but generalizes across a range of views, transitioning from ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 15 (B IMPLEMENTATION DETAILS)이다.

## 검색 태그 근거

이미 구축한 장면 가우시안을 속성이 붙은 3D 점 집합으로 보고 점 트랜스포머로 정제한다. 훈련 카메라에서 멀리 벗어난 뷰의 렌더링 오류를 평가했다. [원문 4쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/8cbde11e5e271ef9ff67fc9f292e43ed-Paper-Conference.pdf#page=4) · [원문 8쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/8cbde11e5e271ef9ff67fc9f292e43ed-Paper-Conference.pdf#page=8)
