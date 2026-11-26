# ComPC: Completing a 3D Point Cloud with 2D Diffusion Priors

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/804f1fac094d7b751410b50066da3a63-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/114366. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: Tianxin Huang, Zhiwen Yan, Yuyang Zhao, Gim Hee Lee
- 저자 판본: ICLR 게재본과 대조해 마지막 저자의 이름을 Gim Hee Lee로 풀어 썼다. [표제면](https://proceedings.iclr.cc/paper_files/paper/2025/file/804f1fac094d7b751410b50066da3a63-Paper-Conference.pdf#page=1) · [학회 서지](https://proceedings.iclr.cc/paper_files/paper/2025/hash/804f1fac094d7b751410b50066da3a63-Abstract-Conference.html)
- Primary track: Planning and control
- Tier: ARCHIVE
- Tags: Diffusion, Generation, point cloud, 3D Vision, shape completion
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/804f1fac094d7b751410b50066da3a63-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2025/file/804f1fac094d7b751410b50066da3a63-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://proceedings.iclr.cc/paper_files/paper/2025/file/804f1fac094d7b751410b50066da3a63-Paper-Conference.pdf)

## Why This Paper Is Here

ComPC는 범주별 완성 모델을 새로 훈련하지 않고, 사전학습된 2D 확산 모델을 사용해 일부만 관측한 물체 점군의 빈 영역을 복원한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/804f1fac094d7b751410b50066da3a63-Paper-Conference.pdf#page=1) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/804f1fac094d7b751410b50066da3a63-Paper-Conference.pdf#page=4)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** 3D point clouds directly collected from objects through sensors are often incomplete due to self-occlusion.
- **p. 1 / ABSTRACT - extractive body cue:** Conventional methods for completing these partial point clouds rely on manually organized training sets and are usually limited to object categories seen during training.
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we propose a test-time framework for completing partial point clouds across unseen categories without any requirement for training.
- **p. 1 / ABSTRACT - extractive body cue:** Leveraging point rendering via Gaussian Splatting, we develop techniques of Partial Gaussian Initialization, Zero-shot Fractal Completion, and Point Cloud Extraction that utilize priors from pre-trained ...
- **p. 1 / ABSTRACT - extractive body cue:** Experimental results on both synthetic and real-world scanned point clouds demonstrate that our approach outperforms existing methods in completing a variety of objects.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, they face challenges in handling data that differs from what they were trained on, such as unseen object categories or real-world scans.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, a notable limitation of the method proposed by SDS-complete (Kasten et al., 2024) is its dependency on manually created text prompts for each point ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our main contributions can be summarized as below: • We propose the Partial Gaussian Initialization to generate a reference image for partial points, which is ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** In view of the above-mentioned issues, we propose a novel test-time point cloud completion framework that eliminates the need for any extra manually provided information ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Inspired by the capability of novel view synthetic diffusion model, e.g., Zero 1-to-3 (Liu et al., 2023), we propose to use the reference image as ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** In this study, we propose to leverage 3D Gaussian Splatting (GS) (Kerbl et al., 2023) to bridge point clouds with priors from 2D diffusion models.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Due to the efficient rendering from 3D GS, and stronger priors from Zero 1-to-3, our method can achieve much higher optimization efficiency than SDS-Complete (Kasten ...
- **p. 4 / 3 METHODOLOGY - extractive body cue:** Specifically, we use Iin to guide the optimization of 3D Gaussians Gm by borrowing priors from the 2D diffusion model in Zero 1-to-3 (Liu et ...
- **p. 4 / 3 METHODOLOGY - extractive body cue:** To introduce priors from pretrained 2D diffusion models, we use 3D Gaussian Splatting (GS) to achieve differentiable rendering from 3D point clouds to 2D images.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our main contributions can be summarized as below: • We propose the Partial Gaussian Initialization to generate a reference image for partial points, which is observed from an estimated reference viewpoint; • ... | conditioning observation와 noisy/intermediate sample | p. 2 (1 INTRODUCTION), p. 4 (3 METHODOLOGY) |
| State/latent | main, contributions, summarized, below, Partial, Gaussian, Initialization, generate, reference, image, points, observed | latent/noise variable와 conditional distribution | p. 2 (1 INTRODUCTION), p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY) |
| Output/action | For any point cloud to be completed, we first determine an reference camera pose Vp, that captures its most completed observation. | generated sample, action chunk 또는 trajectory | p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 5 (3 METHODOLOGY) |
| Objective/outcome | Given that the centers of Gin are anchored to Pin, we can estimate Vp by minimizing: Vp = arg min Vn CD(Pin[h(Gin, Vn)], Pin) + w0 · Depth(Pin, Vn), (1) where CD(·, ... | distribution fit, multimodality, sample quality와 latency | p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY) |

## Main Claims and Actual Contribution

- 관측 점군으로 가우시안을 초기화하고 여러 뷰의 확산 단서로 비어 있는 영역을 채운 뒤 완성된 표면에서 균일한 점군을 추출한다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/804f1fac094d7b751410b50066da3a63-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/804f1fac094d7b751410b50066da3a63-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/804f1fac094d7b751410b50066da3a63-Paper-Conference.pdf#page=6)
- 합성 부분 관측과 실제 Redwood 스캔에서 복원 형상을 비교하고 형상 생성과 점 추출 단계를 각각 평가했다. [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/804f1fac094d7b751410b50066da3a63-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/804f1fac094d7b751410b50066da3a63-Paper-Conference.pdf#page=8) · [PDF 10쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/804f1fac094d7b751410b50066da3a63-Paper-Conference.pdf#page=10)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Embodiment/environment | By introducing abundant priors from 2D diffusion model (Liu et al., 2023), our method can achieve robust completion for objects across different datasets. | hardware/simulator version and reset protocol | p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Dataset/benchmark | AdaPoinTr SVDFormer PoinTr PointAttN Ours Input GT Figure 16: Qualitative comparison on objects from ShapeNet (Chang et al., 2015) dataset. | role, split, size and leakage | p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 19 (A.10 EVALUATION ON LIDAR POINTS), p. 8 (4 EXPERIMENTS) |
| Metric | 4.3 ABLATION STUDY FOR COLORIZATION STRATEGIES IN PGI To confirm the necessity of using normal map for colorization in Partial Gaussian Initialization, we compare their performances against other strategies including using depth ... | definition, denominator, direction and uncertainty | p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Baseline/ablation | We compare our approach with state-of-the-art supervised methods including PointAttN(Wang et al., 2024), PoinTr (Yu et al., 2021), SVDFormer (Zhu et al., 2023), AdaPoinTr (Yu et al., 2023), SeedFormer (Zhou et al., ... | fair input/data/compute/action matching | p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 5 CONCLUSION - extractive body cue:** LIMITATION Our method shares similar limitations as claimed by SDS-complete (Kasten et al., 2024).
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 12: Some failure cases. AdaPoinTr SVDFormer Ours Input GT 0.0 0.001
- **p. 10 / 5 CONCLUSION - extractive body cue:** As a test-time completion method, although our method does not require any training, the optimization on the test data would take relatively long time cost.
- **p. 15 / A.4 FAILURE CASES - extractive body cue:** We will explore it in our future work.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Existing fully-supervised methods may perform inferior even on the in-domain objects as illustrated in Table 2, which reveals their limitation on datasets differing from the ...
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 13: Qualitative comparisons under different noise perturbations. Std denotes the Standard deviation of added noises. The green box marks a local area of a ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Different point cloud completion methods. (a) Existing network-based completion methods; (b) Test-time SDS-complete (Kasten et al., 2024) with text prompts to guide Neural ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (3 METHODOLOGY)이다.

## 검색 태그 근거

부분 점군에서 만든 참조 뷰를 2D 확산 사전분포에 넣어 장면의 비어 있는 부분을 채우고 완성 점군을 추출한다. 영상은 부분 점군의 렌더링으로 제공된다. [원문 3쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/804f1fac094d7b751410b50066da3a63-Paper-Conference.pdf#page=3) · [원문 7쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/804f1fac094d7b751410b50066da3a63-Paper-Conference.pdf#page=7)
