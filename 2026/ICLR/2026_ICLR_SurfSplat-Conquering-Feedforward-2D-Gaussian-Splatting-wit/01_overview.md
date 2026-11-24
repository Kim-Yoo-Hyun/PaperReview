# SurfSplat: Conquering Feedforward 2D Gaussian Splatting with Surface Continuity Priors

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2026/hash/3a10c46572628d58cb44fb705f25cbbf-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/247825. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: Bing He, Jingnan Gao, Yunuo Chen, Gang Chen, Ning Cao, Zhengxue Cheng, Li Song, Wenjun Zhang
- 저자 판본: ICLR 게재본은 Gang Chen을 네 번째, Ning Cao를 다섯 번째 저자로 싣는다. 학회 웹 서지에는 두 이름의 순서가 뒤바뀌어 있다. [표제면](https://proceedings.iclr.cc/paper_files/paper/2026/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf#page=1) · [학회 서지](https://proceedings.iclr.cc/paper_files/paper/2026/hash/3a10c46572628d58cb44fb705f25cbbf-Abstract-Conference.html)
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/3a10c46572628d58cb44fb705f25cbbf-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2026/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://proceedings.iclr.cc/paper_files/paper/2026/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

SurfSplat은 소수의 입력 뷰에서 픽셀별 2D 가우시안을 예측할 때 인접 표면의 연속성을 이용해 기하와 고해상도 렌더링을 개선한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf#page=1) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf#page=4)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Reconstructing 3D scenes from sparse images remains a challenging task due to the difficulty of recovering accurate geometry and texture without optimization.
- **p. 1 / ABSTRACT - extractive body cue:** Recent approaches leverage generalizable models to generate 3D scenes using 3D Gaussian Splatting (3DGS) primitive.
- **p. 1 / ABSTRACT - extractive body cue:** However, they often fail to produce continuous surfaces and instead yield discrete, color-biased point clouds that appear plausible at normal resolution but reveal severe artifacts ...
- **p. 1 / ABSTRACT - extractive body cue:** To address this issue, we present SurfSplat, a feedforward framework based on 2D Gaussian Splatting (2DGS) primitive, which provides stronger anisotropy and higher geometric precision.
- **p. 1 / ABSTRACT - extractive body cue:** By incorporating a surface continuity prior and a forced alpha blending strategy, SurfSplat reconstructs coherent geometry together with faithful textures.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Furthermore, most datasets lack out-of-distribution viewpoints for reliable assessment.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, we observe that existing feedforward methods tend to generate degraded 3D scenes.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, the main contributions of this work are as follows: • We propose SurfSplat, a feedforward network that reconstructs 3D scenes using 2D Gaussian ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our model leverages a surface continuity prior and forced alpha blending to significantly improve reconstruction quality. • We introduce HRRC, a high-resolution rendering-based metric that ...
- **p. 6 / 3.1 PRELIMINARIES - extractive body cue:** 3.6 HIGH-RESOLUTION RENDERING CONSISTENCY (HRRC) To better evaluate the geometric fidelity of reconstructed 3D scenes, we propose a novel evaluation metric: High-Resolution Rendering Consistency (HRRC).
- **p. 5 / 3.1 PRELIMINARIES - extractive body cue:** To address these issues, we start by an observation: most visible geometry in real-world scenes consists of smooth, continuous surfaces.
- **p. 6 / 3.1 PRELIMINARIES - extractive body cue:** To address this, we propose a forced alpha blending strategy that explicitly constrains each Gaussian's opacity.
- **p. 4 / 3.1 PRELIMINARIES - extractive body cue:** In the multi-view branch, input images are first converted into low-resolution feature maps, which are then processed by multiple layers of self- and cross-attention Vaswani ...
- **p. 4 / 3.1 PRELIMINARIES - extractive body cue:** To integrate these complementary sources effectively, we adopt a dual-path for feature extraction within our model architecture.
- **원문 대조:** Multi-view branch는 strided-convolution backbone과 여섯 self/cross-attention layer를 거쳐 view별 H/s×W/s×C feature를 출력한다. 이는 reconstruction encoder의 중간 표현이며 robot-planning handoff의 직접 근거가 아니다. ([PDF p. 15](https://arxiv.org/pdf/2602.02000#page=15), Appendix A.1 Encoder Architecture).

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | This behavior rapidly boosts image quality for near-input viewpoints, but under the alpha-blending rendering rule, occluded Gaussians contribute minimally to the output: C = X i∈N ciαi i-1 Y j=1 (1 -αj), ... | RGB-D, image set, point cloud, depth와 camera pose | p. 6 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES) |
| State/latent | behavior, rapidly, boosts, image, quality, near-input, viewpoints, under, alpha-blending, rendering, rule, occluded | geometry, map, object/relationship state | p. 6 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES) |
| Output/action | Given a collection of V input images {Iv}V v=1 with corresponding camera intrinsics {kv}V v=1 and poses {Tv}V v=1, the network fθ predicts Gaussian parameters for each pixel as: fθ : {(Iv, ... | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES) |
| Objective/outcome | The fused features are subsequently used to construct cost volumes Chen et al. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES) |

## Main Claims and Actual Contribution

- 입력 영상에서 인접한 표면 요소의 위치를 이용해 가우시안의 회전과 크기를 서로 일관되게 추정한다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf#page=6)
- 렌더링 해상도를 높였을 때 재구성이 일관적인지 측정하는 HRRC를 제안하고 표준 뷰 합성 지표와 함께 비교했다. [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT) |
| Embodiment/environment | Both datasets provide precomputed camera poses and we adhere to the official train-test splits used in prior work. | hardware/simulator version and reset protocol | p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT) |
| Dataset/benchmark | 4.1 MAIN RESULTS Table 1: Novel view synthesis performance on the RealEstate10k dataset. | role, split, size and leakage | p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 8 (4 EXPERIMENT) |
| Metric | This observation highlights a key limitation of conventional NVS metrics and underscores the value of our proposed HRRC metric, which drops significantly when surface continuity is not enforced. | definition, denominator, direction and uncertainty | p. 9 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 7 (4 EXPERIMENT) |
| Baseline/ablation | We compare our method to state-of-the-art sparse-view generalizable methods for novel view synthesis, including PixelSplat Charatan et al. | fair input/data/compute/action matching | p. 8 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 7 (4 EXPERIMENT) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 5 CONCLUSION - extractive body cue:** These limitations open opportunities for future research on joint pose elimination and compact, adaptive representations.
- **p. 10 / 5 CONCLUSION - extractive body cue:** By introducing a surface continuity prior and a forced alpha blending strategy, our method addresses key limitations of previous approaches, eliminating surface discontinuities and overcoming ...
- **p. 8 / 4 EXPERIMENT - extractive body cue:** These artifacts reveal the limitations of previous feedforward 3DGS 8
- **p. 9 / 4 EXPERIMENT - extractive body cue:** This observation highlights a key limitation of conventional NVS metrics and underscores the value of our proposed HRRC metric, which drops significantly when surface continuity ...
- **p. 9 / 4 EXPERIMENT - extractive body cue:** Notably, DepthSplat, despite using the same encoder backbone as our method, fails to generate coherent geometry or consistent surface details, which highlights the effectiveness of ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 6 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES)이다.
