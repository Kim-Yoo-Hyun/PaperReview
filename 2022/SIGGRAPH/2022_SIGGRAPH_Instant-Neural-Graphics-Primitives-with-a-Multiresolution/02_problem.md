# Problem - Instant Neural Graphics Primitives with a Multiresolution Hash Encoding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2201.05989; PDF retrieval source: https://arxiv.org/pdf/2201.05989. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 6 (1 INTRODUCTION)): 2017], where they help the neural network to identify the location it is currently processing.

## PDF Body Digest

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Computer graphics primitives are fundamentally represented by mathematical functions that parameterize appearance.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The quality and performance characteristics of the mathematical representation are crucial for visual fidelity: we desire representations that remain fast and compact while capturing high-frequency, ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Functions represented by multi-layer perceptrons (MLPs), used as neural graphics primitives, have been shown to match these criteria (to varying degree), for example as representations ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The important commonality of the these approaches is an encoding that maps neural network inputs to a higher-dimensional space, which is key for extracting high ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Most successful among these encodings are trainable, task-specific data structures [Liu et al.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** 2017], where they help the neural network to identify the location it is currently processing.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The hash tables thus automatically prioritize the sparse areas with the most important fine scale detail.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | 2017], where they help the neural network to identify the location it is currently processing. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | (4) Neural radiance and density fields (NeRF): the MLP learns the 3D density and 5D light field of a given scene from ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Neural, radiance, density, fields, NeRF, MLP, learns, light, field, given | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | trained, output, dense, feature, grids, leaf, node, around | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Neural, radiance, density, fields, NeRF, MLP, learns, light, field, given | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Decision / output variable | geometry/map/query r; body terms: method-Figure, combines, ideas, reduce, waste, illustrate, trade-offs, motivate | p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: last, point, important, reasons, first, matches, coarsest, resolution | p. 13 (B IMPLEMENTATION DETAILS OF NGLOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 13 (B IMPLEMENTATION DETAILS OF NGLOD) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 5 (Figure/Table caption), p. 5 (Figure/Table caption), p. 8 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive body cue:** The hash tables thus automatically prioritize the sparse areas with the most important fine scale detail.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** 2020] and several concurrent works [Sun et al.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Unlike prior work that used spatial hashing [Teschner et al.
- **p. 6 / 1 INTRODUCTION - extractive body cue:** 2021] and the spherical harmonics basis in NeRF, similar to concurrent work [Verbin et al.

## What the Paper Changes

PDF body contribution framing (p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 13 (B IMPLEMENTATION DETAILS OF NGLOD), p. 5 (1 INTRODUCTION)): Our method-Figure 2 (e,f)-combines both ideas to reduce waste.

- **p. 3 / 1 INTRODUCTION - extractive body cue:** To illustrate the trade-offs and to motivate our method, Figure 2 shows the effect on reconstruction quality of a neural radiance field for several different ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This enables the use of smaller, more efficient MLPs.
- **p. 13 / B IMPLEMENTATION DETAILS OF NGLOD - extractive body cue:** We obtained the most favorable performance vs. quality trade-off at a roughly equal number of trainable parameters as our method, through the following configuration: (1) ...
- **원문 대조:** 해상도를 기하급수적으로 늘리면 N_min부터 N_max까지의 범위를 O(log(N_max/N_min))개 level로 포괄할 수 있다. 이는 해시 인코딩의 다중 해상도 구성에 관한 설명이다. ([PDF p. 5](https://arxiv.org/pdf/2201.05989#page=5), Implicit hash collision resolution).

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | The MLP allows for resolving specular details and reduces the amount of background noise caused by hash collisions. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Lookups along the hierarchy of this octree act similarly to our multiresolution cascade of grids: they are a ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | However, it also exhibits visually undesirable surface roughness that we attribute to randomly distributed hash collisions. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Since NGLOD is essentially a collision-free analog to our hash encoding, we attribute this artifact to hash collisions. | reported limitation/failure wording; scope must be verified |

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 6 (1 INTRODUCTION), interface p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), objective p. 13 (B IMPLEMENTATION DETAILS OF NGLOD).

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)
