# Instant Neural Graphics Primitives with a Multiresolution Hash Encoding

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2201.05989.
> PDF retrieval source: https://arxiv.org/pdf/2201.05989. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / SIGGRAPH
- Authors: Thomas Müller, Alex Evans, Christoph Schied, Alexander Keller
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: NeRF, 3D Vision, representation, efficiency
- Official paper: https://arxiv.org/abs/2201.05989
- Full-text retrieval: https://arxiv.org/pdf/2201.05989
- Code/Project: https://nvlabs.github.io/instant-ngp/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 2017], where they help the neural network to identify the location it is currently processing.를 문제로 두고, Our method-Figure 2 (e,f)-combines both ideas to reduce waste.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Computer graphics primitives are fundamentally represented by mathematical functions that parameterize appearance.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The quality and performance characteristics of the mathematical representation are crucial for visual fidelity: we desire representations that remain fast and compact while capturing high-frequency, ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Functions represented by multi-layer perceptrons (MLPs), used as neural graphics primitives, have been shown to match these criteria (to varying degree), for example as representations ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The important commonality of the these approaches is an encoding that maps neural network inputs to a higher-dimensional space, which is key for extracting high ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Most successful among these encodings are trainable, task-specific data structures [Liu et al.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** 2017], where they help the neural network to identify the location it is currently processing.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The hash tables thus automatically prioritize the sparse areas with the most important fine scale detail.

## Core Idea

- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our method-Figure 2 (e,f)-combines both ideas to reduce waste.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** To illustrate the trade-offs and to motivate our method, Figure 2 shows the effect on reconstruction quality of a neural radiance field for several different ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This enables the use of smaller, more efficient MLPs.
- **p. 13 / B IMPLEMENTATION DETAILS OF NGLOD - extractive body cue:** We obtained the most favorable performance vs. quality trade-off at a roughly equal number of trainable parameters as our method, through the following configuration: (1) ...
- **원문 대조:** 해상도를 기하급수적으로 늘리면 N_min부터 N_max까지의 범위를 O(log(N_max/N_min))개 level로 포괄할 수 있다. 이는 해시 인코딩의 다중 해상도 구성에 관한 설명이다. ([PDF p. 5](https://arxiv.org/pdf/2201.05989#page=5), Implicit hash collision resolution).
- **p. 13 / B IMPLEMENTATION DETAILS OF NGLOD - extractive body cue:** 2021] such that it closely resembles that of our hash encoding, only differing in the underlying data structure; i.e. using the vertices of an octree ...
- **p. 13 / B IMPLEMENTATION DETAILS OF NGLOD - extractive body cue:** This results in a notable difference to the original NGLOD: the looked-up feature vectors are concatenated rather than summed, which in our implementation serendipitously resulted ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (4) Neural radiance and density fields (NeRF): the MLP learns the 3D density and 5D light field of a given scene from image observations and corresponding perspective transforms. | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| State/latent | Neural, radiance, density, fields, NeRF, MLP, learns, light, field, given, scene, image | geometry, map, object/relationship state | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Output/action | 2021], and to look-up and (optionally) interpolate these parameters depending on the input vector x ∈R𝑑. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Objective/outcome | The last point is important for two reasons: first, it matches the coarsest resolution of our hash tables 24 = 16 = 𝑁min, and second, it prevents a performance bottleneck that would ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 13 (B IMPLEMENTATION DETAILS OF NGLOD) |

## Main Claims and Actual Contribution

- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our method-Figure 2 (e,f)-combines both ideas to reduce waste.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** To illustrate the trade-offs and to motivate our method, Figure 2 shows the effect on reconstruction quality of a neural radiance field for several different ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This enables the use of smaller, more efficient MLPs.
- **p. 13 / B IMPLEMENTATION DETAILS OF NGLOD - extractive body cue:** We obtained the most favorable performance vs. quality trade-off at a roughly equal number of trainable parameters as our method, through the following configuration: (1) ...
- **원문 대조:** 해상도를 기하급수적으로 늘리면 N_min부터 N_max까지의 범위를 O(log(N_max/N_min))개 level로 포괄할 수 있다. 이는 해시 인코딩의 다중 해상도 구성에 관한 설명이다. ([PDF p. 5](https://arxiv.org/pdf/2201.05989#page=5), Implicit hash collision resolution).
- **p. 10 / 24.2 M - extractive body cue:** It approaches NeRF's quality after training for just ∼5 min, yet is outperformed by our full method after training for 5 s-15 s, amounting to ...
- **p. 9 / 24.2 M - extractive body cue:** Due to the small size and efficient implementation of the MLP, it is only 15% more expensive-well worth the significantly improved quality. function, which we ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. A demonstration of the reconstruction quality of different encodings and parametric data structures for storing trainable feature embeddings. Each configuration was trained for ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 10 (24.2 M), p. 9 (24.2 M) |
| Embodiment/environment | At HD resolutions, synthetic and even real-world scenes can be trained in seconds and rendered at 60 FPS, without the need of caching of the MLP outputs [Garbin et al. | hardware/simulator version and reset protocol | p. 9 (24.2 M), p. 7 (5 EXPERIMENTS) |
| Dataset/benchmark | Other scenes behave almost identically. | role, split, size and leakage | p. 9 (24.2 M), p. 7 (5 EXPERIMENTS), p. 9 (24.2 M), p. 10 (24.2 M) |
| Metric | Fig. 4. The main curves plot test error over training time for varying hash table size 𝑇which determines the number of trainable encoding parameters. Increasing 𝑇improves reconstruction, at the cost of higher ... | definition, denominator, direction and uncertainty | p. 5 (Figure/Table caption), p. 5 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Baseline/ablation | As baseline, we compare with NGLOD [Takikawa et al. | fair input/data/compute/action matching | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 10 (24.2 M) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 24.2 M - extractive body cue:** The MLP allows for resolving specular details and reduces the amount of background noise caused by hash collisions.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Lookups along the hierarchy of this octree act similarly to our multiresolution cascade of grids: they are a collision-free analog to our technique, with a ...
- **p. 8 / 24.2 M - extractive body cue:** However, it also exhibits visually undesirable surface roughness that we attribute to randomly distributed hash collisions.
- **p. 9 / 24.2 M - extractive body cue:** Since NGLOD is essentially a collision-free analog to our hash encoding, we attribute this artifact to hash collisions.
- **p. 10 / 24.2 M - extractive body cue:** While the linear layer is capable of reproducing view-dependent effects, the quality is significantly compromised as compared to the MLP, which is better able to ...
- **p. 11 / 24.2 M - extractive body cue:** Microstructure due to hash collisions.
- **p. 11 / 24.2 M - extractive body cue:** The graininess is a result of hash collisions that the MLP is unable to fully compensate for.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 2017], where they help the neural network to identify the location it is currently processing.를 문제로 두고, Our method-Figure 2 (e,f)-combines both ideas to reduce waste.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 6 (1 INTRODUCTION), p. 13 (B IMPLEMENTATION DETAILS OF NGLOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
