# VTGaussian-SLAM: RGBD SLAM for Large Scale Scenes with Splatting View-Tied 3D Gaussians

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v267/hu25h.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/168040. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICML
- Authors: Pengchong Hu, Zhizhong Han
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, Gaussian Splatting, SLAM
- Official paper: https://proceedings.mlr.press/v267/hu25h.html
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25h/hu25h.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/hu25h/hu25h.pdf)

## Why This Paper Is Here

VTGaussian-SLAM은 RGB-D 키프레임의 깊이 픽셀에 가우시안을 묶어 큰 장면의 카메라 자세와 지도를 제한된 GPU 메모리에서 갱신한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/hu25h/hu25h.pdf#page=1) · [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/hu25h/hu25h.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Jointly estimating camera poses and mapping scenes from RGBD images is a fundamental task in simultaneous localization and mapping (SLAM).
- **p. 1 / Abstract - extractive body cue:** State-of-the-art methods employ 3D Gaussians to represent a scene, and render these Gaussians through splatting for higher efficiency and better rendering.
- **p. 1 / Abstract - extractive body cue:** However, these methods cannot scale up to extremely large scenes, due to the inefficient tracking and mapping strategies that need to optimize all 3D Gaussians ...
- **p. 1 / Abstract - extractive body cue:** To resolve this issue, we propose novel tracking and mapping strategies to work with a novel 3D representation, dubbed view-tied 3D Gaussians, for RGBD SLAM ...
- **p. 1 / Abstract - extractive body cue:** View-tied 3D Gaussians is a kind of simplified Gaussians, which is tied to depth pixels, without needing to learn locations, rotations, and multi-dimensional variances.
- **p. 1 / 1. Introduction - extractive body cue:** This obstacle makes 3DGS still hard to scale up to extremely large scenes in SLAM, remaining the challenge of improving the rendering quality, tracking accuracy, ...
- **p. 1 / 1. Introduction - extractive body cue:** To overcome this challenge, we propose an RGBD SLAM system with splatting view-tied 3D Gaussians.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are listed below. • We propose view-tied Gaussian splatting that significantly reduces storage but improves rendering quality with 3DGS in SLAM. • ...
- **p. 1 / 1. Introduction - extractive body cue:** Our method introduces a novel point-based volume representation, dubbed view-tied 3D Gaussians, to represent the color and 1
- **p. 1 / 1. Introduction - extractive body cue:** To overcome this challenge, we propose an RGBD SLAM system with splatting view-tied 3D Gaussians.
- **p. 3 / 3.2. View-tied Gaussians - extractive body cue:** Our view-tied Gaussians aim to achieve memory efficiency in SLAM, which enables us to improve the rendering quality by using many more Gaussians to represent ...
- **p. 3 / 3.2. View-tied Gaussians - extractive body cue:** This not only enables us to use more Gaussians to represent local details, but also removes the need to maintain the appearance and geometry consistency ...
- **p. 5 / 3.4. Mapping Scenes - extractive body cue:** We minimize the rendering errors with respect to observations, min {g}k ρ//Vi-V ′ i //1+τLS(Vi, V ′ i )+σUi//Di-D′ i//1, (2) where LS is the ...
- **p. 4 / 3.3. Tracking Cameras - extractive body cue:** At each frame out of a 2000 frame video, the average error of relative pose to the previous frame is pretty small, while the average ...
- **p. 4 / 3.3. Tracking Cameras - extractive body cue:** Although better renderings are helpful for more accurate camera pose estimations, the higher accuracy is merely meaningful relative to the neighboring frames, resulting in a ...

## Observation, State, and Output Interface

| 항목 | 원문에서 확인한 범위 |
|---|---|
| 입력 | RGB-D 프레임과 키프레임 |
| 표현 | 키프레임의 관측에 연결된 가우시안 |
| 출력 | 추정한 카메라 자세와 조밀한 지도 |
| 평가 | 궤적의 절대 오차와 재구성 품질 |

[방법 3쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/hu25h/hu25h.pdf#page=3) · [평가 8쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/hu25h/hu25h.pdf#page=8)

## Main Claims and Actual Contribution

- 가우시안의 위치·회전·축별 분산을 전부 독립 변수로 저장하는 비용을 줄이고 현재 뷰와 겹치는 영역을 추적·매핑에 사용한다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/hu25h/hu25h.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/hu25h/hu25h.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/hu25h/hu25h.pdf#page=5)
- 카메라 궤적 오차와 재구성 깊이·렌더링 품질을 구분해 평가하고 큰 장면에서 지도 표현 및 갱신 방식의 영향을 비교했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/hu25h/hu25h.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/hu25h/hu25h.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/hu25h/hu25h.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4.1. Comparisons), p. 8 (4.2. Ablation Studies and Analysis) |
| Embodiment/environment | TUM-RGBD, ScanNet, and ScanNet++ are real-world datasets. | hardware/simulator version and reset protocol | p. 5 (4. Experiments and Analysis), p. 5 (4. Experiments and Analysis) |
| Dataset/benchmark | 1, mapping scenes with rendered images in Tab. | role, split, size and leakage | p. 5 (4. Experiments and Analysis), p. 5 (4. Experiments and Analysis), p. 6 (4.1. Comparisons), p. 6 (4.1. Comparisons) |
| Metric | Then we measure the reconstruction performance with F1-score, the harmonic mean of the Precision (P) and Recall (R), using a distance threshold of 1 cm for all evaluations. | definition, denominator, direction and uncertainty | p. 6 (4. Experiments and Analysis), p. 5 (4. Experiments and Analysis), p. 6 (4. Experiments and Analysis) |
| Baseline/ablation | Compared to previous GS-based SLAM methods, our method can use many more Gaussians tied at each pixel on depth images to fit sudden color change without needing to maintain the consistency of ... | fair input/data/compute/action matching | p. 7 (4.1. Comparisons), p. 6 (4.1. Comparisons), p. 6 (4. Experiments and Analysis) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4.2. Ablation Studies and Analysis - extractive body cue:** We cannot use a large number of Gaussians 8
- **p. 7 / 4.1. Comparisons - extractive body cue:** However, relying on data-driven priors, LoopSplat (Zhu et al., 2024) reported more accurate camera tracking in terms of average accuracy, while our method does not ...
- **p. 23 / Figure/Table caption - extractive body cue:** Table 22. Impact of depth noise and movability of Gaussians on the rendering performance in PSNR ↑, SSIM ↑, and LPIPS ↓on Replica (Straub et ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.4. Mapping Scenes), p. 4 (3.3. Tracking Cameras)이다.

## 검색 태그 근거

키프레임의 RGB-D 픽셀에 가우시안을 묶고, 렌더링 오차로 카메라 자세와 지도를 갱신한다. Replica 등에서 궤적과 장면 복원을 비교했다. [원문 3쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/hu25h/hu25h.pdf#page=3) · [원문 8쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/hu25h/hu25h.pdf#page=8)
