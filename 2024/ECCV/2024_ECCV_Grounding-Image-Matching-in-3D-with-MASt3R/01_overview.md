# Grounding Image Matching in 3D with MASt3R

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2406.09756.
> PDF retrieval source: https://arxiv.org/pdf/2406.09756. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: Vincent Leroy, Yohann Cabon, Jérôme Revaud
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D geometry, matching, camera pose
- Official paper: https://arxiv.org/abs/2406.09756
- Full-text retrieval: https://arxiv.org/pdf/2406.09756
- Code/Project: https://github.com/naver/mast3r
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

MASt3R는 DUSt3R의 3차원 점 지도에 픽셀별 대응 특징을 더해 시점이 다른 영상에서도 더 정밀한 대응점을 찾는다. [PDF 1쪽](https://arxiv.org/pdf/2406.09756v1#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Image Matching is a core component of all best-performing algorithms and pipelines in 3D vision.
- **p. 1 / Abstract - extractive body cue:** Yet despite matching being fundamentally a 3D problem, intrinsically linked to camera pose and scene geometry, it is typically treated as a 2D problem.
- **p. 1 / Abstract - extractive body cue:** This makes sense as the goal of matching is to establish correspondences between 2D pixel fields, but also seems like a potentially hazardous choice.
- **p. 1 / Abstract - extractive body cue:** In this work, we take a different stance and propose to cast matching as a 3D task with DUSt3R, a recent and powerful 3D reconstruction ...
- **p. 1 / Abstract - extractive body cue:** Based on pointmaps regression, this method displayed impressive robustness in matching views with extreme viewpoint changes, yet with limited accuracy.
- **p. 2 / 1. Introduction - extractive body cue:** We argue that this is because, so far, practically all matching approaches have been treating matching as a 2D problem in image space.
- **p. 2 / 1. Introduction - extractive body cue:** Yet, correspondences obtained naively from this 3D output currently outperform all other keypoint- and matching-based methods on the Map-free benchmark.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** First, we propose MASt3R, a 3D-aware matching approach building on the recently released DUSt3R framework.
- **p. 2 / 1. Introduction - extractive body cue:** To get pixel-accurate matches, we propose a coarse-to-fine matching scheme during which matching is performed at several scales.
- **p. 4 / 3.2. Matching prediction head and loss - extractive body cue:** For these reasons, we propose to add a second head that outputs two dense feature maps 𝐷1 and 𝐷2 ∈ℝ𝐻×𝑊×𝑑of dimensional 𝑑: 𝐷1 = Head1 ...
- **p. 5 / 3.3. Fast reciprocal matching - extractive body cue:** Finally, the output set of correspondences consists of the concatenation of all reciprocal pairs M𝑘= Ð 𝑡M𝑡 𝑘.
- **p. 4 / 3.1. The DUSt3R framework - extractive body cue:** Compared to the DUSt3R framework which we build upon, our contributions are highlighted in blue.
- **p. 3 / 3. Method - extractive body cue:** We then introduce an optimized matching scheme specially devised to deal with dense feature maps in 3.3, that we use for coarse-to-fine matching in section ...
- **p. 4 / 3.1. The DUSt3R framework - extractive body cue:** (2) Then, two intertwined decoders process these representations jointly, exchanging information via crossattention to ‘understand' the spatial relationship between viewpoints and the global 3D geometry ...
- **p. 5 / 3.2. Matching prediction head and loss - extractive body cue:** Finally, both regression and matching losses are combined to get the final training objective: Ltotal = Lconf + 𝛽Lmatch (12)

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 2, aims at jointly performing 3D scene reconstruction and matching given two input images. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3. Method), p. 3 (3.1. The DUSt3R framework) |
| State/latent | aims, jointly, performing, scene, reconstruction, matching, given, input, images, transformer-based, network, predicts | geometry, map, object/relationship state | p. 3 (3. Method), p. 3 (3.1. The DUSt3R framework), p. 4 (3.1. The DUSt3R framework) |
| Output/action | A transformer-based network predicts a local 3D reconstruction given two input images, in the form of two dense 3D point-clouds 𝑋1,1 and 𝑋2,1, denoted as pointmaps in the following. | point map, pose, scene graph, affordance 또는 query result | p. 3 (3.1. The DUSt3R framework), p. 4 (3.1. The DUSt3R framework), p. 4 (3.2. Matching prediction head and loss) |
| Objective/outcome | Note that this matching objective is essentially a cross-entropy classification loss: contrary to regression in eq. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.2. Matching prediction head and loss), p. 5 (3.2. Matching prediction head and loss), p. 3 (3. Method) |

## Main Claims and Actual Contribution

- 3차원 회귀와 함께 조밀한 지역 기술자를 출력하는 헤드를 학습시키고, 영상 간 특징 대응에 별도의 손실을 부여했다. [PDF 3쪽](https://arxiv.org/pdf/2406.09756v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2406.09756v1#page=4)
- 상호 최근접 대응을 빠르게 찾는 알고리즘을 제안하고, 사전 장면 지도 없이 카메라 위치를 찾는 평가에서 대응 방식별 성능을 비교했다. [PDF 5쪽](https://arxiv.org/pdf/2406.09756v1#page=5) · [PDF 7쪽](https://arxiv.org/pdf/2406.09756v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2406.09756v1#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4.2. Map-free localization), p. 7 (4.2. Map-free localization) |
| Embodiment/environment | These datasets feature diverse scene types: indoor, outdoor, synthetic, real-world, object-centric, etc. | hardware/simulator version and reset protocol | p. 6 (4.1. Training), p. 6 (4. Experimental results) |
| Dataset/benchmark | We start our experiments with the Map-free relocalization benchmark [5], an extremely challenging dataset aiming at localizing the camera in metric space given a single reference image without any map. | role, split, size and leakage | p. 6 (4.1. Training), p. 6 (4. Experimental results), p. 7 (4.2. Map-free localization), p. 9 (4.4. Visual localization) |
| Metric | In table 3 we report the average accuracy, completeness and Chamfer distances error metrics as provided by the authors of the benchmarks. | definition, denominator, direction and uncertainty | p. 9 (4.5. Multiview 3D reconstruction), p. 7 (4.2. Map-free localization), p. 7 (4.2. Map-free localization) |
| Baseline/ablation | MASt3R not only outperforms the DUSt3R baseline but also compete with the best methods, all without leveraging camera calibration nor poses for matching, neither having seen this camera setup before. | fair input/data/compute/action matching | p. 9 (4.5. Multiview 3D reconstruction), p. 7 (4.2. Map-free localization), p. 7 (4.2. Map-free localization) |

## Explicit Limitations and Failure Boundary

- **p. 14 / 5. Conclusion - extractive body cue:** A second cycle (or more) thus cannot exist in G𝑖. □ Lemma B.2.
- **p. 14 / 5. Conclusion - extractive body cue:** All nodes, i.e. pixels, belong to G since we add an edge for each pixel's nearest neighbor, but note that all pixels cannot reach all ...
- **p. 16 / 5. Conclusion - extractive body cue:** 9, it is clearly visible that the FRM provides a sampling biased towards finding reciprocal matches with large basins (bottom), since a greater number of ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Qualitative examples on the Map-free dataset. Top row: Pairs with strong viewpoint changes. Third one is a failure case. For clarity, we only ...
- **p. 7 / 4.1. Training - extractive body cue:** If we cannot find enough correspondences, we pad with random false correspondences so that the likelihood of finding a true match remains constant.
- **p. 10 / 5. Conclusion - extractive body cue:** We successfully improved DUSt3R with matching, getting the best of both worlds: enhanced robustness, while attaining and even surpassing what could be done with pixel ...
- **p. 11 / 5. Conclusion - extractive body cue:** MASt3R is particularly precise and robust, giving sharp and dense details.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 3 (3. Method), p. 4 (3.2. Matching prediction head and loss), p. 4 (3.1. The DUSt3R framework), p. 5 (3.2. Matching prediction head and loss)이다.
