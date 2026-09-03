# ComPC: Completing a 3D Point Cloud with 2D Diffusion Priors

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=SoUwcVplq4.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/114366. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: ARCHIVE
- Tags: Diffusion, Generation, point cloud, 3D Vision
- Official paper: https://openreview.net/forum?id=SoUwcVplq4
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/114366
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 generative 문제를 이해하기 위해 읽는다. 본문은 However, they face challenges in handling data that differs from what they were trained on, such as unseen object categories or real-world scans.를 문제로 두고, Our main contributions can be summarized as below: • We propose the Partial Gaussian Initialization to generate a reference image for partial points, which is observed from an estimated reference viewpoint; • ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our main contributions can be summarized as below: • We propose the Partial Gaussian Initialization to generate a reference image for partial points, which is ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** In view of the above-mentioned issues, we propose a novel test-time point cloud completion framework that eliminates the need for any extra manually provided information ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Inspired by the capability of novel view synthetic diffusion model, e.g., Zero 1-to-3 (Liu et al., 2023), we propose to use the reference image as ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** In this study, we propose to leverage 3D Gaussian Splatting (GS) (Kerbl et al., 2023) to bridge point clouds with priors from 2D diffusion models.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Due to the efficient rendering from 3D GS, and stronger priors from Zero 1-to-3, our method can achieve much higher optimization efficiency than SDS-Complete (Kasten ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** The results demonstrate that the Preservation Constraint improves performance compared to standard view-dependent diffusion guidance.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** The results show that the normal map consistently outperforms other methods.
- **p. 16 / A.7 EVALUATION ON MULTI-MODAL METRICS - extractive body cue:** Our method achieves superior performance on UHD and MMD metrics, further validating its effectiveness for 3D point cloud completion.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

Planning and control의 generative 문제를 이해하기 위해 읽는다. 본문은 However, they face challenges in handling data that differs from what they were trained on, such as unseen object categories or real-world scans.를 문제로 두고, Our main contributions can be summarized as below: • We propose the Partial Gaussian Initialization to generate a reference image for partial points, which is observed from an estimated reference viewpoint; • ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (3 METHODOLOGY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
