# VoxFormer: Sparse Voxel Transformer for Camera-based 3D Semantic Scene Completion

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2302.12251.
> PDF retrieval source: https://arxiv.org/pdf/2302.12251. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / CVPR
- Authors: Yiming Li, Zhiding Yu, Christopher Choy, Chaowei Xiao, Jose M. Alvarez, Sanja Fidler, Chen Feng, Anima Anandkumar
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: semantic, alignment, 3D Vision
- Official paper: https://arxiv.org/abs/2302.12251
- Full-text retrieval: https://arxiv.org/pdf/2302.12251
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

VoxFormer는 카메라 영상에서 관측 가능한 점유 복셀을 먼저 고르고 이를 출발점으로 보이지 않는 영역까지 3차원 의미 점유를 예측한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2023/papers/Li_VoxFormer_Sparse_Voxel_Transformer_for_Camera-Based_3D_Semantic_Scene_Completion_CVPR_2023_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Humans can easily imagine the complete 3D geometry of occluded objects and scenes.
- **p. 1 / Abstract - extractive body cue:** This appealing ability is vital for recognition and understanding.
- **p. 1 / Abstract - extractive body cue:** To enable such capability in AI systems, we propose VoxFormer, a Transformerbased semantic scene completion framework that can output complete 3D volumetric semantics from only ...
- **p. 1 / Abstract - extractive body cue:** Our framework adopts a two-stage design where we start from a sparse set of visible and occupied voxel queries from depth estimation, followed by a ...
- **p. 1 / Abstract - extractive body cue:** A key idea of this design is that the visual features on 2D images correspond only to the visible scene structures rather than the occluded ...
- **p. 1 / 1. Introduction - extractive body cue:** However, obtaining accurate and complete 3D information of the real world is difficult, since the task is challenged by the lack of sensing resolution and ...
- **p. 1 / 1. Introduction - extractive body cue:** However, there is still a significant performance gap between state-of-the-art SSC methods [2] and human perception in driving scenes.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions in this work can be summarized as follows: • A novel two-stage framework that lifts images into a complete 3D voxelized semantic scene. ...
- **p. 2 / 1. Introduction - extractive body cue:** VoxFormer consists of class-agnostic query proposal (stage-1) and class-specific semantic segmentation (stage2), where stage-1 proposes a sparse set of occupied voxels, and stage-2 completes the ...
- **p. 3 / 3.2. Overall Architecture - extractive body cue:** Our framework is a two-stage cascade composed of class-agnostic proposals and class-specific segmentation similar to [68]: stage-1 generates class-agnostic query proposals, and stage-2 uses an ...
- **p. 4 / 3.3. Predefined Parameters - extractive body cue:** Note that our framework supports the input of single or multiple images. computations.
- **p. 4 / 3.3. Predefined Parameters - extractive body cue:** The estimated depth after correction enables the class-agnostic query proposal stage: the query located at an occupied position will be selected to carry out deformable ...
- **p. 3 / 3.1. Preliminary - extractive body cue:** Motivated by reconstruction-beforehallucination and sparsity-in-3D-space, we build a twostage framework: stage-1 based on CNN proposes a sparse set of voxel queries from image depth to ...
- **p. 5 / 3.3. Predefined Parameters - extractive body cue:** Then we use deformable self-attention to get the refined voxel features ˆF3D ∈R×h×w×z×d: DSA(F3D, F3D) = DA(f, p, F3D), (5) where f could be either ...
- **p. 5 / 3.3. Predefined Parameters - extractive body cue:** Finally, we perform a weighted sum of the sampled features as the output of deformable cross-attention (DCA): DCA(qp, F2D) = 1 /Vt/ X t∈Vt DA(qp, ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | More specifically, we use as input current and previous images denoted by It = {It, It-1, ...}, and use as output a voxel grid Yt ∈ {c0, c1, ..., cM}H×W ×Z defined ... | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3.1. Preliminary), p. 3 (3.1. Preliminary) |
| State/latent | More, specifically, input, current, previous, images, denoted, It-1, output, voxel, grid, defined | geometry, map, object/relationship state | p. 3 (3.1. Preliminary), p. 3 (3.1. Preliminary), p. 4 (3.3. Predefined Parameters) |
| Output/action | Motivated by reconstruction-beforehallucination and sparsity-in-3D-space, we build a twostage framework: stage-1 based on CNN proposes a sparse set of voxel queries from image depth to attend to images since the image features ... | point map, pose, scene graph, affordance 또는 query result | p. 3 (3.1. Preliminary), p. 4 (3.3. Predefined Parameters), p. 2 (1. Introduction) |
| Objective/outcome | We train stage-2 with a weighted cross-entropy loss. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.6. Training Loss), p. 5 (3.6. Training Loss), p. 3 (3.1. Preliminary) |

## Main Claims and Actual Contribution

- 깊이 추정으로 희소한 복셀 질의를 만든 뒤 자기어텐션으로 주변 전체 복셀에 정보를 전파한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2023/papers/Li_VoxFormer_Sparse_Voxel_Transformer_for_Camera-Based_3D_Semantic_Scene_Completion_CVPR_2023_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2023/papers/Li_VoxFormer_Sparse_Voxel_Transformer_for_Camera-Based_3D_Semantic_Scene_Completion_CVPR_2023_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2023/papers/Li_VoxFormer_Sparse_Voxel_Transformer_for_Camera-Based_3D_Semantic_Scene_Completion_CVPR_2023_paper.pdf#page=5)
- SemanticKITTI에서 공간 점유와 의미 클래스 복원을 따로 측정하고 깊이 기반 질의 선택 방식을 비교했다. [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2023/papers/Li_VoxFormer_Sparse_Voxel_Transformer_for_Camera-Based_3D_Semantic_Scene_Completion_CVPR_2023_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2023/papers/Li_VoxFormer_Sparse_Voxel_Transformer_for_Camera-Based_3D_Semantic_Scene_Completion_CVPR_2023_paper.pdf#page=6) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2023/papers/Li_VoxFormer_Sparse_Voxel_Transformer_for_Camera-Based_3D_Semantic_Scene_Completion_CVPR_2023_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 7 (4.2. Performance), p. 6 (4.2. Performance) |
| Embodiment/environment | SemanticKITTI SSC benchmark is interested in a volume of 51.2m ahead of the car, 25.6m to left and right side, and 6.4m in height. | hardware/simulator version and reset protocol | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup) |
| Dataset/benchmark | We report the results within different ranges on the validation set, and the results within the full range on the hidden test set are in the supplementary. | role, split, size and leakage | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Performance) |
| Metric | Meanwhile, the semantic score is also improved by 9.29% without sacrificing IoU. | definition, denominator, direction and uncertainty | p. 6 (4.2. Performance), p. 7 (4.2. Performance), p. 6 (4.2. Performance) |
| Baseline/ablation | We compare VoxFormer against the state-of-the-art SSC methods with public resources: (1) a camera-based SSC method MonoScene [4] based on 2D-to-3D feature projection, (2) LiDAR-based SSC methods including JS3CNet [8], LMSCNet [6], ... | fair input/data/compute/action matching | p. 6 (4.1. Experimental Setup), p. 7 (4.2. Performance), p. 7 (4.2. Performance) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** In this paper, we present VoxFormer, a strong camerabased 3D semantic scene completion (SSC) framework composed of (1) class-agnostic query proposal based on depth estimation ...
- **p. 8 / 5. Conclusion - extractive body cue:** VoxFormer outperforms the state-of-the-art camera-based method and even performs on par with LiDAR-based methods at close range.
- **p. 8 / 5. Conclusion - extractive body cue:** We hope VoxFormer can motivate further research in camera-based SSC and its applications in AV perception.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 3 (3.1. Preliminary), p. 5 (3.3. Predefined Parameters)이다.
