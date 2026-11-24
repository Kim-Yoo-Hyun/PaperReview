# PlaceIt3D: Language-Guided Object Placement in Real 3D Scenes

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Abdelreheem_PlaceIt3D_Language-Guided_Object_Placement_in_Real_3D_Scenes_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Abdelreheem_PlaceIt3D_Language-Guided_Object_Placement_in_Real_3D_Scenes_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: Ahmed Abdelreheem, Filippo Aleotti, Jamie Watson, Zawar Qureshi, Abdelrahman Eldesokey, Peter Wonka, Gabriel Brostow, Sara Vicente, Guillermo Garcia-Hernando
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Abdelreheem_PlaceIt3D_Language-Guided_Object_Placement_in_Real_3D_Scenes_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Abdelreheem_PlaceIt3D_Language-Guided_Object_Placement_in_Real_3D_Scenes_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/ICCV2025/papers/Abdelreheem_PlaceIt3D_Language-Guided_Object_Placement_in_Real_3D_Scenes_ICCV_2025_paper.pdf)

## Why This Paper Is Here

PlaceIt3D는 스캔한 실내 장면과 3D 물체 자산, 자연어 지시를 받아 물체를 놓을 위치를 찾는 과제와 평가 자료를 제시한다. [PDF 1쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Abdelreheem_PlaceIt3D_Language-Guided_Object_Placement_in_Real_3D_Scenes_ICCV_2025_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Abdelreheem_PlaceIt3D_Language-Guided_Object_Placement_in_Real_3D_Scenes_ICCV_2025_paper.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce the task of Language-Guided Object Placement in Real 3D Scenes.
- **p. 1 / Abstract - extractive body cue:** Given a 3D reconstructed point-cloud scene, a 3D asset, and a natural-language instruction, the goal is to place the asset so that the instruction is ...
- **p. 1 / Abstract - extractive body cue:** The task demands tackling four intertwined challenges: (a) one-to-many ambiguity in valid placements; (b) precise geometric and physical reasoning; (c) joint understanding across the scene, ...
- **p. 1 / Abstract - extractive body cue:** The first three challenges mirror the complexities of synthetic scene generation, while the metadata-free, noisy-scan scenario is inherited from language-guided 3D visual grounding.
- **p. 1 / Abstract - extractive body cue:** We inaugurate this task by introducing a benchmark and evaluation protocol, releasing a dataset for training multi-modal large language models (MLLMs), and establishing a first ...
- **p. 2 / 1. Introduction - extractive body cue:** We study language-guided 3D asset placement in reconstructed scenes, a problem closest to grounding and to synthetic scene generation, yet distinct in that it requires ...
- **p. 2 / 1. Introduction - extractive body cue:** Many constraints are geometric and cannot be resolved from 2D projections alone.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To advance research in this area, we make three key contributions, summarized here: • We introduce PLACEIT3D-benchmark for languageguided placement with 3,500 evaluation examples, each ...
- **p. 2 / 1. Introduction - extractive body cue:** Like the benchmark, it uses ScanNet scenes and PartObjaverse-Tiny assets. • We propose PLACEWIZARD, a proto-method for this task built on recent 3D LLMs [25].
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we focus on the novel task of languageguided 3D object placement in a reconstructed real 3D scene.
- **p. 6 / 4.4. Losses - extractive body cue:** We use a combination of Binary Cross Entropy (BCE) and Dice [43] losses when comparing a ground truth mask ¯ M with a predicted mask ...
- **p. 6 / 4.4. Losses - extractive body cue:** Finally, our total loss is defined as \Lo = \Lo _ {seg}(\bar {\mas k }_{l oc}, \mask _{loc}) + \Lo _{rot} + \Lo _{seg}(\bar {\mask ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | As in the shoe example, the goal is to find a valid placement of the object among multiple configurations that satisfy the instruction. | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (1. Introduction), p. 1 (1. Introduction) |
| State/latent | shoe, example, goal, find, valid, placement, object, among, multiple, configurations, satisfy, instruction | geometry, map, object/relationship state | p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | At two to three years old, neurotypical children learn to follow two-step instructions like "Get your shoes and put them on the shelf" [42]. | point map, pose, scene graph, affordance 또는 query result | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | We use a combination of Binary Cross Entropy (BCE) and Dice [43] losses when comparing a ground truth mask ¯ M with a predicted mask M, so \Lo _{ se g }(\b ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (4.4. Losses), p. 6 (4.4. Losses) |

## Main Claims and Actual Contribution

- 물리적으로 가능한 위치와 장면 그래프로 지시가 허용하는 배치 영역을 만들고, 후보 위치가 언어 조건과 공간 제약을 만족하는지 평가하는 기준을 정의했다. [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Abdelreheem_PlaceIt3D_Language-Guided_Object_Placement_in_Real_3D_Scenes_ICCV_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Abdelreheem_PlaceIt3D_Language-Guided_Object_Placement_in_Real_3D_Scenes_ICCV_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Abdelreheem_PlaceIt3D_Language-Guided_Object_Placement_in_Real_3D_Scenes_ICCV_2025_paper.pdf#page=5)
- PlaceWizard는 장면 점군·자산·언어 특징을 결합해 가능한 위치를 예측하며, 규칙 기반 및 언어 모델 기반 배치와 비교했다. [PDF 5쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Abdelreheem_PlaceIt3D_Language-Guided_Object_Placement_in_Real_3D_Scenes_ICCV_2025_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Abdelreheem_PlaceIt3D_Language-Guided_Object_Placement_in_Real_3D_Scenes_ICCV_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Abdelreheem_PlaceIt3D_Language-Guided_Object_Placement_in_Real_3D_Scenes_ICCV_2025_paper.pdf#page=7)

## Evaluation Scope

평가의 입력은 장면 메시, 물체 자산과 지시문이고 출력은 3D 이동과 수직축 회전이다. 성능은 예측 배치가 지정된 공간 제약을 충족하는 비율로 집계한다. [PDF 4쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Abdelreheem_PlaceIt3D_Language-Guided_Object_Placement_in_Real_3D_Scenes_ICCV_2025_paper.pdf#page=4) · [PDF 7쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Abdelreheem_PlaceIt3D_Language-Guided_Object_Placement_in_Real_3D_Scenes_ICCV_2025_paper.pdf#page=7)

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Limitations and Future Work - extractive body cue:** Our novel task formulation currently has several limitations.
- **p. 8 / 6. Limitations and Future Work - extractive body cue:** Despite these limitations, we believe our work lays the groundwork for further research in this area.
- **p. 7 / 5.1. Quantitative results - extractive body cue:** Due to its frequent failure to accurately detect floor regions, we substitute in ground truth floor masks, while other anchor objects are selected based on ...
- **p. 7 / 5.1. Quantitative results - extractive body cue:** In contrast, the rule-based system, which leverages both asset and scene meshes, can produce more plausible placements, albeit at the cost of expensive collision checks ...
- **p. 4 / 3.2.2. Benchmark metrics - extractive body cue:** This is a strict metric that reflects the robustness of the placement method under full constraint satisfaction. • Language Adherence Success: The percentage of placements ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 6 (4.4. Losses), p. 8 (5.1.1. Ablations), p. 8 (Figure/Table caption)이다.
