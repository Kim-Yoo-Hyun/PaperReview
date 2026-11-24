# Total-Decom: Decomposed 3D Scene Reconstruction with Minimal Interaction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Lyu_Total-Decom_Decomposed_3D_Scene_Reconstruction_with_Minimal_Interaction_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Lyu_Total-Decom_Decomposed_3D_Scene_Reconstruction_with_Minimal_Interaction_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: Xiaoyang Lyu, Chirui Chang, Peng Dai, Yang-Tian Sun, Xiaojuan Qi
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D reconstruction, geometry, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Lyu_Total-Decom_Decomposed_3D_Scene_Reconstruction_with_Minimal_Interaction_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Lyu_Total-Decom_Decomposed_3D_Scene_Reconstruction_with_Minimal_Interaction_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/CVPR2024/papers/Lyu_Total-Decom_Decomposed_3D_Scene_Reconstruction_with_Minimal_Interaction_CVPR_2024_paper.pdf)

## Why This Paper Is Here

Total-Decom은 실내 장면에서 사용자가 소수의 점을 선택하면 그 물체의 3D 형상을 배경과 분리하고 가려졌던 배경을 복원한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Lyu_Total-Decom_Decomposed_3D_Scene_Reconstruction_with_Minimal_Interaction_CVPR_2024_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Lyu_Total-Decom_Decomposed_3D_Scene_Reconstruction_with_Minimal_Interaction_CVPR_2024_paper.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Scene reconstruction from multi-view images is a fundamental problem in computer vision and graphics.
- **p. 1 / Abstract - extractive body cue:** Recent neural implicit surface reconstruction methods have achieved high-quality results; however, editing and manipulating the 3D geometry of reconstructed scenes remains challenging due to the ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we present Total-Decom, a novel method for decomposed 3D reconstruction with minimal human interaction.
- **p. 1 / Abstract - extractive body cue:** Our approach seamlessly integrates the Segment Anything Model (SAM) with hybrid implicitexplicit neural surface representations and a mesh-based
- **p. 1 / Abstract - extractive body cue:** Total-Decom requires minimal human annotations while providing users with real-time control over the granularity and quality of decomposition.
- **p. 2 / 1. Introduction - extractive body cue:** Moreover, even with ground-truth instance labels, the existing state-of-the-art method [37] still fails to produce satisfactory results, with multiple objects missing, as shown by the ...
- **p. 2 / 1. Introduction - extractive body cue:** 7, due to the inherent difficulties in separating all objects using implicit representations.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In sum, our main contributions are as follows: • We introduce a novel pipeline that seamlessly integrates the segment anything model with hybrid implicit-explicit neural ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we introduce Total-Decom, a novel method designed for decomposed 3D reconstruction with minimal human interaction.
- **p. 3 / 3. Empirical Study on General Visual Features - extractive body cue:** Consequently, we propose a novel approach that leverages SAM features and a mesh-based region-growing method to decompose a 3D scene with minimal human an20862
- **p. 4 / 4. Overview - extractive body cue:** To achieve this, we propose a novel pipeline that integrates SAM into a hybrid implicit-explicit surface representation, combined with a mesh-based region-growing method to effectively ...
- **p. 1 / Abstract - extractive body cue:** We extensively evaluate our method on benchmark datasets and demonstrate its potential for downstream applications, such as animation and scene editing.
- **p. 4 / 5. Neural Implicit Feature Distillation and Sur - extractive body cue:** Then, we use the volume rendering formula [13] to obtain outputs E of the target pixel, ˆE(r) = M X i=1 T r i αiˆer ...
- **p. 5 / 5. Neural Implicit Feature Distillation and Sur - extractive body cue:** Additionally, we use the L2 loss Lf to optimize the rendered generalized feature ˆF(r) for distilling the F(r) from the SAM encoder.
- **p. 4 / 4. Overview - extractive body cue:** 5, we first adopt an implicit neural surface representation to achieve dense and complete 3D reconstruction from images while incorporating object-aware information by distilling image ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In this paper, we present Total-Decom, a novel method for decomposed 3D reconstruction with minimal human interaction. | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (Abstract), p. 2 (1. Introduction) |
| State/latent | present, Total-Decom, novel, decomposed, reconstruction, minimal, human, interaction, stage, integrate, object-aware, information | geometry, map, object/relationship state | p. 1 (Abstract), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | At this stage, we also integrate object-aware information by distilling image features from the SAM model for follow-up efficient interaction and accurate decomposition. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (5. Neural Implicit Feature Distillation and Sur) |
| Objective/outcome | Thanks to the segmentation capability of SAM and our feature rendering design, this interactive process also allows users to obtain the desired objects at different granularities while minimizing human interactions and avoiding ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 2 (1. Introduction), p. 4 (4. Overview), p. 5 (5. Neural Implicit Feature Distillation and Sur) |

## Main Claims and Actual Contribution

- 장면 표현에 2D 분할 모델의 특징을 학습시켜 사용자가 찍은 점과 같은 물체의 표면을 찾고 메시를 분리한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Lyu_Total-Decom_Decomposed_3D_Scene_Reconstruction_with_Minimal_Interaction_CVPR_2024_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Lyu_Total-Decom_Decomposed_3D_Scene_Reconstruction_with_Minimal_Interaction_CVPR_2024_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Lyu_Total-Decom_Decomposed_3D_Scene_Reconstruction_with_Minimal_Interaction_CVPR_2024_paper.pdf#page=5)
- 객체 제거로 드러나는 배경을 완성하고 분해한 물체를 옮기거나 제거하는 장면 편집과 기하 복원을 평가했다. [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Lyu_Total-Decom_Decomposed_3D_Scene_Reconstruction_with_Minimal_Interaction_CVPR_2024_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Lyu_Total-Decom_Decomposed_3D_Scene_Reconstruction_with_Minimal_Interaction_CVPR_2024_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Lyu_Total-Decom_Decomposed_3D_Scene_Reconstruction_with_Minimal_Interaction_CVPR_2024_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Lyu_Total-Decom_Decomposed_3D_Scene_Reconstruction_with_Minimal_Interaction_CVPR_2024_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (7.2. Results), p. 7 (7.1. Experiment Setup) |
| Embodiment/environment | To further demonstrate the robustness of our method, we also use the ScanNet [6] as the real-world dataset which provides 1513 scenes. | hardware/simulator version and reset protocol | p. 7 (7.1. Experiment Setup), p. 7 (7.2. Results) |
| Dataset/benchmark | Visualized assessments on different datasets. | role, split, size and leakage | p. 7 (7.1. Experiment Setup), p. 7 (7.2. Results), p. 8 (7.2. Results), p. 8 (7.2. Results) |
| Metric | The reconstruction results are mainly evaluated by Chamfer-L1 and F-Score. | definition, denominator, direction and uncertainty | p. 7 (7.1. Experiment Setup), p. 7 (7.2. Results), p. 4 (Figure/Table caption) |
| Baseline/ablation | We mainly compared our approach with the ObjSDF++, the state-of-the-art method that decomposes the scene structure with pseudo geometry priors as far as we know. | fair input/data/compute/action matching | p. 7 (7.2. Results), p. 7 (7.1. Experiment Setup), p. 3 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Comparison on different decomposition methods with SAM feature. SAM + region growing represents object extraction with our method. SAM + similarity indicates object ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Visualization for distilled generalized features. ever, these methods rely heavily on accurate multi-view consistent ground-truth instance-level labels and cannot ef- fectively preserve all ...
- **p. 7 / 7.1. Experiment Setup - extractive body cue:** Since this type of method does not introduce geometric constraints, we mainly compare the way of decomposition.
- **p. 7 / 7.1. Experiment Setup - extractive body cue:** To further demonstrate the robustness of our method, we also use the ScanNet [6] as the real-world dataset which provides 1513 scenes.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 1 (1. Introduction), p. 4 (5. Neural Implicit Feature Distillation and Sur), p. 5 (5. Neural Implicit Feature Distillation and Sur)이다.
