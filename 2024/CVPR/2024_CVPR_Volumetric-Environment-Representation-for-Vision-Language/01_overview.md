# Volumetric Environment Representation for Vision-Language Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Liu_Volumetric_Environment_Representation_for_Vision-Language_Navigation_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Liu_Volumetric_Environment_Representation_for_Vision-Language_Navigation_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: Rui Liu, Wenguan Wang, Yi Yang
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: Vision-Language Navigation, 3D geometry, representation
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Liu_Volumetric_Environment_Representation_for_Vision-Language_Navigation_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Liu_Volumetric_Environment_Representation_for_Vision-Language_Navigation_CVPR_2024_paper.pdf
- Code/Project: https://github.com/DefaultRui/VLN-VER
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 4. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../work/sources/pdf_note_review_followup_2026-10-23.json).

## Why This Paper Is Here

VER는 여러 시점의 영상을 3차원 복셀 상태로 통합해 언어 지시에 따른 다음 이동을 결정하는 표현이다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Liu_Volumetric_Environment_Representation_for_Vision-Language_Navigation_CVPR_2024_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-language navigation (VLN) requires an agent to navigate through an 3D environment based on visual observations and natural language instructions.
- **p. 1 / Abstract - extractive body cue:** It is clear that the pivotal factor for successful navigation lies in the comprehensive scene understanding.
- **p. 1 / Abstract - extractive body cue:** Previous VLN agents employ monocular frameworks to extract 2D features of perspective views directly.
- **p. 1 / Abstract - extractive body cue:** Though straightforward, they struggle for capturing 3D geometry and semantics, leading to a partial and incomplete environment representation.
- **p. 1 / Abstract - extractive body cue:** To achieve a comprehensive 3D representation with fine-grained details, we introduce a Volumetric Environment Representation (VER), which voxelizes the physical world into structured 3D cells.
- **p. 1 / 1. Introduction - extractive body cue:** Thus, they encounter challenges in capturing 3D geometry and semantics in complex scenes.
- **p. 1 / 1. Introduction - extractive body cue:** As a result, they lack of explicit environment representations and struggle to access their past states during long-time exploration [61, 82].

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In this article, we propose a Volumetric Environment Representation (VER) that quantizes the physical world into structured 3D cells (Fig.
- **p. 2 / 1. Introduction - extractive body cue:** As a response, we propose a coarse-to-fine VER extraction architecture, which uses learnable up-sampling operations to construct the representations progressively.
- **p. 3 / 3. Approach - extractive body cue:** For brevity, we present the technical description in the context of R2R [3].
- **p. 3 / 3. Approach - extractive body cue:** To achieve comprehensive scene understanding, we introduce VER, which voxelizes the 3D world into structured 3D cells (Fig.
- **p. 4 / 3.2. Volume State Estimation - extractive body cue:** MLT consists of stacked selfattention blocks.
- **p. 4 / 3.2. Volume State Estimation - extractive body cue:** The environment representation is first reshaped as F 3d′ t ∈ RDe×XY Z, and then adopt multi-layer transformers (MLT) to model the relations between E ...
- **p. 3 / 3.1. Environment Encoder - extractive body cue:** We introduce cross-view attention (CVA) to aggregate their features (F 2d for each view) into a unified volumetric representation F 3d with a group of ...
- **PDF p. 4, §3.2 Eq. (4) (DOC-QA2 원문 대조):** Language와 volume features를 결합해 갱신한 F̄ₜ³ᵈ에 MLP와 Softmax를 적용하여 pₜ³ᵈ∈[0,1]^(X×Y×Z)의 spatial state probability를 얻는다. 이 식은 volume state estimation이며 motion execution/recovery command가 아니다.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Early VLN approaches [3, 23] typically learn the navigation policy through the sequence-to-sequence (Seq2Seq) framework [72], which directly maps instructions and multi-view perspective observations to actions. | camera/depth stream, pose, map와 language goal | p. 1 (1. Introduction), p. 4 (3.2. Volume State Estimation) |
| State/latent | Early, VLN, approaches, typically, learn, navigation, policy, through, sequence-to-sequence, Seq2Seq, framework, directly | robot pose, free-space/semantic map와 local goal | p. 1 (1. Introduction), p. 4 (3.2. Volume State Estimation), p. 5 (3.4. Annotation Generation) |
| Output/action | At step t, the next intermediate state st+1 =(xt+1, yt+1, zt+1) is determined by the instruction embeddings E and VER F 3d t for reaching the goal state sT (0<t<T). | collision-free trajectory 또는 velocity command | p. 4 (3.2. Volume State Estimation), p. 5 (3.4. Annotation Generation), p. 6 (3.5. Implementation Details) |
| Objective/outcome | A combination of the L1 loss and the IoU loss [67] is used as the training objective. | goal reach, safety, localization error와 replanning latency | p. 4 (3.1. Environment Encoder), p. 6 (3.5. Implementation Details), p. 6 (3.5. Implementation Details) |

## Main Claims and Actual Contribution

- 다시점 2차원 특징을 공간 셀에 모으고 점유·방 구조·물체 경계 상자를 함께 예측하도록 학습한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Liu_Volumetric_Environment_Representation_for_Vision-Language_Navigation_CVPR_2024_paper.pdf#page=3) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Liu_Volumetric_Environment_Representation_for_Vision-Language_Navigation_CVPR_2024_paper.pdf#page=5)
- 이동하면서 구축한 표현의 현재 상태와 에피소드 기억을 함께 사용해 다음 행동을 선택하고 내비게이션에서 평가했다. [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Liu_Volumetric_Environment_Representation_for_Vision-Language_Navigation_CVPR_2024_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Liu_Volumetric_Environment_Representation_for_Vision-Language_Navigation_CVPR_2024_paper.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 7 (4.2. Diagnostic Experiment) |
| Embodiment/environment | The dataset is split into train, val seen, val unseen, and test unseen sets, which mainly focus on the generalization capability in unseen environments. | hardware/simulator version and reset protocol | p. 6 (4.1. Performance on VLN), p. 8 (4.3. Analysis on 3D Representation Learning) |
| Dataset/benchmark | The experiments are conducted on three datasets. | role, split, size and leakage | p. 6 (4.1. Performance on VLN), p. 8 (4.3. Analysis on 3D Representation Learning), p. 6 (4.1. Performance on VLN), p. 7 (4.1. Performance on VLN) |
| Metric | For R2R, Success Rate (SR), Trajectory Length (TL), Oracle Success Rate (OSR), Success rate weighted by Path Length (SPL), and Navigation Error (NE) are used. | definition, denominator, direction and uncertainty | p. 6 (4.1. Performance on VLN), p. 7 (4.1. Performance on VLN), p. 8 (4.3. Analysis on 3D Representation Learning) |
| Baseline/ablation | For R2R, Success Rate (SR), Trajectory Length (TL), Oracle Success Rate (OSR), Success rate weighted by Path Length (SPL), and Navigation Error (NE) are used. | fair input/data/compute/action matching | p. 6 (4.1. Performance on VLN), p. 7 (4.1. Performance on VLN), p. 7 (4.1. Performance on VLN) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** In this paper, we propose a Volumetric Environment Representation (VER), which aggregates the perspective features into structured 3D cells.
- **p. 8 / 5. Conclusion - extractive body cue:** Through coarse-to-fine feature extraction, we can efficiently perform several 3D perception tasks.
- **p. 8 / 5. Conclusion - extractive body cue:** Based on this comprehensive representation, we develop the volume state for local action prediction and the episodic memory for retrieving the global context.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 4 (3.2. Volume State Estimation), p. 3 (3.1. Environment Encoder), p. 5 (3.4. Annotation Generation)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Thus, they encounter challenges in capturing 3D geometry and semantics in complex scenes. (p. 1, 1. Introduction).
- **Actual contribution:** In this article, we propose a Volumetric Environment Representation (VER) that quantizes the physical world into structured 3D cells (Fig. (p. 2, 1. Introduction).
- **Evaluation boundary:** Table 3. Quantitative results on R4R [39] (more details in §4.1). (RGS), and Remote Grounding Success weighted by Path Length (RGSPL) are also employed for object grounding. For R4R, Coverage ... (p. 7, Figure/Table caption).
- **Explicit failure boundary:** From Table 5, the limited range of neighborhood is insufficient to represent the candidate viewpoint for navigation (e.g., 75.80% → 73.75% of SR on R2R). (p. 7, 4.2. Diagnostic Experiment).

## 원문과 공개 자료

- 코드 · 공식 배포 중 3차원 복셀 환경 표현 구성요소 · projects/mmdet3d_plugin/bevformer/detectors/voxelformer.py [배포 파일](https://raw.githubusercontent.com/DefaultRui/VLN-VER/d925dfa3c815779c3b6b131ccc3ccf9df1fbfc3a/projects/mmdet3d_plugin/bevformer/detectors/voxelformer.py)
