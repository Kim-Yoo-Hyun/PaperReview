# G4Splat: Geometry-Guided Gaussian Splatting with Generative Prior

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=kdPmsMVhZf.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/247273. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: Junfeng Ni, Yixin Chen, Zhifei Yang, Yu Liu, Ruijie Lu, Song-Chun Zhu, Siyuan Huang
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, Diffusion, Generation, 3D Vision
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/e0ac27bf3327c9cb99cc5f548db4f73a-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2026/file/e0ac27bf3327c9cb99cc5f548db4f73a-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 27. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../work/sources/pdf_note_review_followup_2026-10-23.json).

## Why This Paper Is Here

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 First, lacking reliable geometric supervision, these methods produce poor reconstruction quality even in observed regions with sparse input views, which undermines the geometric basis essential for inpainting unobserved areas.를 문제로 두고, Our main contributions are summarized as follows: • We propose a novel method that leverages the plane representation to derive scale-accurate geometric constraints, substantially improving 3D scene reconstruction even in unobserved reg ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Despite recent advances in leveraging generative prior from pre-trained diffusion models for 3D scene reconstruction, existing methods still face two critical limitations.
- **p. 1 / ABSTRACT - extractive body cue:** First, due to the lack of reliable geometric supervision, they struggle to produce high-quality reconstructions even in observed regions, let alone in unobserved areas.
- **p. 1 / ABSTRACT - extractive body cue:** Second, they lack effective mechanisms to mitigate multiview inconsistencies in the generated images, leading to severe shape-appearance ambiguities and degraded scene geometry.
- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we identify accurate geometry as the fundamental prerequisite for effectively exploiting generative models to enhance 3D scene reconstruction.
- **p. 1 / ABSTRACT - extractive body cue:** We first propose to leverage the prevalence of planar structures to derive accurate metric-scale depth maps, providing reliable supervision in both observed and unobserved regions.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** First, lacking reliable geometric supervision, these methods produce poor reconstruction quality even in observed regions with sparse input views, which undermines the geometric basis essential ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Second, these methods lack effective mechanisms to mitigate multi-view inconsistencies in diffusion model outputs, which lead to degraded scene recovery due to severe shape-appearance ambiguities ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our main contributions are summarized as follows: • We propose a novel method that leverages the plane representation to derive scale-accurate geometric constraints, substantially improving ...
- **p. 5 / 3.1 BACKGROUND - extractive body cue:** Our method addresses key issues in prior approaches: (a) MAtCha produces noticeable errors in non-overlapping regions (highlighted by circles); (b) masks derived from alpha maps ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To this end, we introduce G4SPLAT, which first leverages the prevalence of planar structures in man-made environments, consistent with the Manhattan world assumption (Coughlan & ...
- **p. 4 / 3 METHOD - extractive body cue:** We propose G4SPLAT, a method that integrates accurate geometry guidance with generative priors to enhance 3D scene reconstruction.
- **p. 4 / 3 METHOD - extractive body cue:** Next, we present our plane-aware geometry modeling in Section 3.2, followed by the geometry-guided generative pipeline in Section 3.3.
- **p. 6 / 3.1 BACKGROUND - extractive body cue:** 3.4 OVERALL TRAINING STRATEGY Our training pipeline consists of two stages: an initialization stage and a geometry-guided generative training loop.
- **p. 4 / 3 METHOD - extractive body cue:** We begin by introducing the base model MAtCha (Guédon et al., 2025) and the overall training objective in Section 3.1.
- **p. 4 / 3.1 BACKGROUND - extractive body cue:** Given N input images {Ii}N i=1 with its associated camera poses, the overall training objective of MAtCha combines an RGB reconstruction loss Lrgb, the original ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Building on 2DGS, MAtCha (Guédon et al., 2025) introduces a chart alignment procedure that optimizes the chart parameters for each input view based on the outputs of MASt3R-SfM (Duisterhof et al., 2025). | conditioning observation와 noisy/intermediate sample | p. 4 (3.1 BACKGROUND), p. 6 (3.1 BACKGROUND) |
| State/latent | Building, DGS, MAtCha, introduces, chart, alignment, procedure, optimizes, parameters, input, view, outputs | latent/noise variable와 conditional distribution | p. 4 (3.1 BACKGROUND), p. 6 (3.1 BACKGROUND), p. 4 (3.1 BACKGROUND) |
| Output/action | The Gaussian parameters are then initialized from the resulting point cloud and optimized using these plane-aware depth maps, producing a baseline model with accurate geometry in the regions observed by the input ... | generated sample, action chunk 또는 trajectory | p. 6 (3.1 BACKGROUND), p. 4 (3.1 BACKGROUND), p. 5 (3.1 BACKGROUND) |
| Objective/outcome | The selection process is guided by three objectives: maximizing coverage of plane points, minimizing distance to the plane, and encouraging alignment between the viewing direction and the plane normal. | distribution fit, multimodality, sample quality와 latency | p. 6 (3.1 BACKGROUND), p. 4 (3.1 BACKGROUND), p. 4 (3 METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our main contributions are summarized as follows: • We propose a novel method that leverages the plane representation to derive scale-accurate geometric constraints, substantially improving ...
- **p. 5 / 3.1 BACKGROUND - extractive body cue:** Our method addresses key issues in prior approaches: (a) MAtCha produces noticeable errors in non-overlapping regions (highlighted by circles); (b) masks derived from alpha maps ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To this end, we introduce G4SPLAT, which first leverages the prevalence of planar structures in man-made environments, consistent with the Manhattan world assumption (Coughlan & ...
- **p. 4 / 3 METHOD - extractive body cue:** We propose G4SPLAT, a method that integrates accurate geometry guidance with generative priors to enhance 3D scene reconstruction.
- **p. 4 / 3 METHOD - extractive body cue:** Next, we present our plane-aware geometry modeling in Section 3.2, followed by the geometry-guided generative pipeline in Section 3.3.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Our method significantly outperforms all baselines across both reconstruction and rendering metrics.
- **p. 10 / 4.2 RESULTS - extractive body cue:** Adding plane-aware geometry modeling (PM), either alone or in combination with generative prior (GP), significantly improves geometry reconstruction.
- **p. 25 / C.7 IMPLEMENTATION DETAILS - extractive body cue:** G4Splat outperforms baselines in both visible and unobserved regions, producing superior geometry with improved smoothness and minimal Gaussian artifacts.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4 EXPERIMENTS), p. 10 (4.2 RESULTS) |
| Embodiment/environment | The real-world datasets include 6 scenes from ScanNet++ (Yeshwanth et al., 2023), 3 scenes from DeepBlending (Hedman et al., 2018) and 9 scenes from Mip-NeRF 360 (Barron et al., 2022). | hardware/simulator version and reset protocol | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Dataset/benchmark | As the Mip-NeRF 360 dataset lacks ground-truth meshes, we evaluate only the rendering performance for those scenes; for the remaining three datasets, we report the full suite of metrics. | role, split, size and leakage | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4.2 RESULTS) |
| Metric | Table A4는 CD=(Accuracy+Completeness)/2, 두 방향 nearest-point L1 distance 평균, F-score=2PR/(P+R)를 정의한다. Precision/recall은 L1 distance<0.05인 비율이다. | 이 표의 L1 norm·0.05 threshold를 보존; 다른 CD 정의와 혼용하지 않음 | PDF p. 27 Table A4 |
| Baseline/ablation | Our method significantly outperforms all baselines across both reconstruction and rendering metrics. | fair input/data/compute/action matching | p. 8 (4 EXPERIMENTS), p. 9 (4.2 RESULTS), p. 9 (4.2 RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Additionally, we present more experimental results in Appendix A, failure cases and discuss the method's limitations in Appendix D.
- **p. 24 / C.7 IMPLEMENTATION DETAILS - extractive body cue:** D FAILURE CASES AND LIMITATIONS In this section, we present and analyze representative failure cases.
- **p. 9 / 4.2 RESULTS - extractive body cue:** In contrast, other methods that leverage generative prior exhibit notable limitations.
- **p. 9 / 4.2 RESULTS - extractive body cue:** For example, Difix3D+ attains relatively good quality in observed regions but fails to handle unobserved areas.
- **p. 10 / 4.2 RESULTS - extractive body cue:** This indicates that directly introducing generative prior fails to perform as expected and leads to shape-appearance ambiguities.
- **p. 10 / 4.2 RESULTS - extractive body cue:** This stems from our design that applies tailored supervision on regions according to their geometric characteristics: for planar regions, reconstruction is improved by leveraging accurate ...
- **p. 25 / C.7 IMPLEMENTATION DETAILS - extractive body cue:** A5(b) illustrates another limitation: our approach struggles with heavily occluded regions, such as the chairs partially blocked by a table.

## Why Read It

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 First, lacking reliable geometric supervision, these methods produce poor reconstruction quality even in observed regions with sparse input views, which undermines the geometric basis essential for inpainting unobserved areas.를 문제로 두고, Our main contributions are summarized as follows: • We propose a novel method that leverages the plane representation to derive scale-accurate geometric constraints, substantially improving 3D scene reconstruction even in unobserved reg ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (3.1 BACKGROUND), p. 4 (3.1 BACKGROUND), p. 5 (3.1 BACKGROUND), p. 6 (3.1 BACKGROUND) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
