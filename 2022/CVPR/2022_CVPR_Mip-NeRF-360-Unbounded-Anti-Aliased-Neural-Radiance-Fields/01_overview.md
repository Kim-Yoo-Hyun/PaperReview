# Mip-NeRF 360: Unbounded Anti-Aliased Neural Radiance Fields

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2111.12077.
> PDF retrieval source: https://arxiv.org/pdf/2111.12077. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / CVPR
- Authors: Jonathan T. Barron, Ben Mildenhall, Dor Verbin, Pratul P. Srinivasan, Peter Hedman
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: NeRF, 3D Vision, representation, geometry
- Official paper: https://arxiv.org/abs/2111.12077
- Full-text retrieval: https://arxiv.org/pdf/2111.12077
- Code/Project: https://jonbarron.info/mipnerf360/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

Mip-NeRF 360은 카메라가 한 지점 주위를 돌며 촬영한 장면에서 가까운 물체와 먼 배경을 함께 표현해 새 시점을 합성한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2022/papers/Barron_Mip-NeRF_360_Unbounded_Anti-Aliased_Neural_Radiance_Fields_CVPR_2022_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Though neural radiance fields (NeRF) have demonstrated impressive view synthesis results on objects and small bounded regions of space, they struggle on "unbounded" scenes, where ...
- **p. 1 / Abstract - extractive body cue:** In this setting, existing NeRF-like models often produce blurry or low-resolution renderings (due to the unbalanced detail and scale of nearby and distant objects), are ...
- **p. 1 / Abstract - extractive body cue:** We present an extension of mip-NeRF (a NeRF variant that addresses sampling and aliasing) that uses a non-linear scene parameterization, online distillation, and a novel ...
- **p. 1 / Abstract - extractive body cue:** Our model, which we dub "mip-NeRF 360" as we target scenes in which the camera rotates 360 degrees around a point, reduces meansquared error by ...
- **p. 1 / Abstract - extractive body cue:** Neural Radiance Fields (NeRF) synthesize highly realistic renderings of scenes by encoding the volumetric density and color of a scene within the weights of a ...
- **p. 2 / 3. Ambiguity. The content of unbounded scenes may lie - extractive body cue:** One fundamental challenge in dealing with unbounded scenes is that such scenes are often large and detailed.
- **p. 2 / 3. Ambiguity. The content of unbounded scenes may lie - extractive body cue:** The idea of accelerating ray-tracing through a hierarchical data structure such as octrees [43] or bounding volume hierarchies [42] is well-explored in the rendering literature, ...

## Core Idea

- **p. 1 / Abstract - extractive body cue:** We present an extension of mip-NeRF (a NeRF variant that addresses sampling and aliasing) that uses a non-linear scene parameterization, online distillation, and a novel ...
- **p. 1 / Abstract - extractive body cue:** In this work, we present an extension to mip-NeRF we call "mip-NeRF 360" that is capable of producing realistic renderings of these unbounded scenes, as ...
- **p. 6 / 4. Regularization for Interval-Based Models - extractive body cue:** Here we presents a regularizer that, as shown in Figure 5, prevents floaters and background collapse more effectively than the approach used by NeRF of ...
- **p. 3 / 3. Ambiguity. The content of unbounded scenes may lie - extractive body cue:** Additionally, these regularizers are designed for the point samples used by NeRF, while our approach is designed to work with the continuous weights defined along ...
- **p. 2 / 3. Ambiguity. The content of unbounded scenes may lie - extractive body cue:** A learned "proposer" network was explored in NeRF in Detail [1] but only achieves a speedup of 25%, while our approach accelerates training by 300%.
- **p. 7 / 5. Optimization - extractive body cue:** For Lrecon we use Charbonnier loss [10]: p (x -x∗)2 + ϵ2 with ϵ = 0.001, which achieves slightly more stable optimization than the mean ...
- **p. 6 / 4. Regularization for Interval-Based Models - extractive body cue:** This reformulation also provides some intuition for how this loss behaves: the first term minimizes the weighted distances between all pairs of interval midpoints, and ...
- **p. 6 / 4. Regularization for Interval-Based Models - extractive body cue:** + 1 3 X i w2 i (si+1 -si) (15) In this form, our distortion loss is trivial to compute.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | These features are used as input to an MLP parameterized by weights ΘNeRF that outputs a density τ and color c: ∀Ti ∈t, (τi, ci) = MLP(γ(r(Ti)); ΘNeRF) . | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3. Ambiguity. The content of unbounded scenes may lie), p. 2 (3. Ambiguity. The content of unbounded scenes may lie) |
| State/latent | features, input, MLP, parameterized, weights, NeRF, outputs, density, color, example, could, recreate | geometry, map, object/relationship state | p. 3 (3. Ambiguity. The content of unbounded scenes may lie), p. 2 (3. Ambiguity. The content of unbounded scenes may lie), p. 2 (3. Ambiguity. The content of unbounded scenes may lie) |
| Output/action | For example, a NeRF could recreate all input images by simply reconstructing each im2 | point map, pose, scene graph, affordance 또는 query result | p. 2 (3. Ambiguity. The content of unbounded scenes may lie), p. 2 (3. Ambiguity. The content of unbounded scenes may lie), p. 3 (3. Ambiguity. The content of unbounded scenes may lie) |
| Training objective | 원문 대조: 학습 손실은 재구성 항 L_recon, λ로 가중한 distortion 항 L_dist, 두 proposal 단계(k=0,1)의 L_prop 합으로 구성되며 batch의 ray에 대해 평균한다. 이 식 자체는 정량 평가 결과가 아니다. ([PDF p. 6](https://arxiv.org/pdf/2111.12077#page=6), §5 Optimization, Eq. (16)) | Rendering loss; robot-task utility는 이 식에서 확인되지 않음 | [PDF p. 6](https://arxiv.org/pdf/2111.12077#page=6), §5 Optimization, Eq. (16) |

## Main Claims and Actual Contribution

- 먼 공간을 유계 좌표로 수축해 근경에 더 많은 표현 해상도를 배정한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2022/papers/Barron_Mip-NeRF_360_Unbounded_Anti-Aliased_Neural_Radiance_Fields_CVPR_2022_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2022/papers/Barron_Mip-NeRF_360_Unbounded_Anti-Aliased_Neural_Radiance_Fields_CVPR_2022_paper.pdf#page=4)
- 제안 네트워크로 광선 위 표본을 배치하고 거리 왜곡 손실로 여러 깊이에 흩어지는 렌더링 가중치를 억제한다. [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2022/papers/Barron_Mip-NeRF_360_Unbounded_Anti-Aliased_Neural_Radiance_Fields_CVPR_2022_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2022/papers/Barron_Mip-NeRF_360_Unbounded_Anti-Aliased_Neural_Radiance_Fields_CVPR_2022_paper.pdf#page=6)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (6. Results), p. 8 (6. Results) |
| Embodiment/environment | We evaluate our model on a novel dataset: 9 scenes (5 outdoors and 4 indoors) each containing a complex central object or area and a detailed background. | hardware/simulator version and reset protocol | p. 7 (6. Results), p. 7 (6. Results) |
| Dataset/benchmark | (a) A test-set image from our dataset's stump scene, with (b) our model's rendered image and depth map (median ray termination distance [37]). | role, split, size and leakage | p. 7 (6. Results), p. 7 (6. Results), p. 8 (6. Results), p. 8 (6. Results) |
| Metric | E) Removing the proposal MLP and training our model using mip-NeRF's approach (applying Lrecon at all coarse scales instead of using our Lprop) worsens both speed and accuracy, justifying our supervision strategy. | definition, denominator, direction and uncertainty | p. 8 (6. Results), p. 7 (6. Results), p. 7 (6. Results) |
| Baseline/ablation | Though mip-NeRF 360 significantly outperforms mip-NeRF and other prior work, it is not perfect. | fair input/data/compute/action matching | p. 8 (6. Results), p. 8 (6. Results), p. 18 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 15 / Figure/Table caption - extractive body cue:** Figure 12. A visualization of our model with Stable View Synthesis [41] on scenes from the Tanks and Temples dataset [25]. Image quality is roughly ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7. (a) A test-set image from our dataset's stump scene, with (b) our model's rendered image and depth map (median ray termination distance [37]). ...
- **p. 7 / 6. Results - extractive body cue:** Our model has several advantages over SVS and Deep Blending in addition to image quality: those models require external training data while our model does ...
- **p. 8 / 6. Results - extractive body cue:** D) Removing the proposal MLP and using a single MLP to model both the scene and the proposal weights does not degrade performance but increases ...
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 8. The axis-aligned positional encoding used by mip- NeRF [3] does not capture the covariance of the Gaussian be- ing encoded. Here we plot ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. Our regularizer suppresses "floaters" (pieces of semi- transparent material floating in space, which are easy to identify in the depth map) and prevents ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (Abstract), p. 2 (3. Ambiguity. The content of unbounded scenes may lie), p. 3 (3. Ambiguity. The content of unbounded scenes may lie), p. 7 (5. Optimization)이다.
