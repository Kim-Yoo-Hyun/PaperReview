# Distilling Diffusion Models to Efficient 3D LiDAR Scene Completion

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: Shengyuan Zhang, An Zhao, Ling Yang, Zejian Li, Chenye Meng, Haoran Xu, Tianrun Chen, AnYang Wei, Perry Pengyun GU, Lingyun Sun
- 저자 판본: ICCV 게재본의 아홉 번째 저자 표기는 Perry Pengyun GU다. [표제면](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.pdf#page=1) · [학회 서지](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.html)
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: LiDAR, Diffusion, Generation, 3D Vision, distillation, shape completion
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.pdf)

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

ScoreLiDAR는 부분 LiDAR 스캔에서 장면 전체를 완성하는 확산 모델을 더 적은 반복으로 동작하는 모델에 증류한다. [PDF 1쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.pdf#page=1) · [PDF 4쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.pdf#page=4)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Diffusion models have been applied to 3D LiDAR scene completion due to their strong training stability and high completion quality.
- **p. 1 / Abstract - extractive body cue:** However, the slow sampling speed limits the practical application of diffusion-based scene completion models since autonomous vehicles require an efficient perception of surrounding environments.
- **p. 1 / Abstract - extractive body cue:** This paper proposes a novel distillation method tailored for 3D LiDAR scene completion models, dubbed ScoreLiDAR, which achieves efficient yet high-quality scene completion.
- **p. 1 / Abstract - extractive body cue:** ScoreLiDAR enables the distilled model to sample in significantly fewer steps after distillation.
- **p. 1 / Abstract - extractive body cue:** To improve completion quality, we also introduce a novel Structural Loss, which encourages the distilled model to capture the geometric structure of the 3D LiDAR ...
- **p. 2 / 1. Introduction - extractive body cue:** ScoreLiDAR aims to tackle the unique 3D distribution alignment challenge in LiDAR scene completion.
- **원문 대조:** LiDiff 배경 설명에서는 x^0=0인 noise offset을 각 원래 point p_m에 더한다. 결과는 p_m+sqrt(1−ᾱ^t)·ε^t 형태이며, point cloud 전체를 원점 주변으로 축소하는 식과 구분한다. ([PDF p. 3](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.pdf#page=3), §3.2, Eq. (6)).

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In this work, we propose ScoreLiDAR, a novel distillation method tailored for 3D LiDAR scene completion diffusion models, which enables efficient and high-quality scene completion ...
- **p. 2 / 1. Introduction - extractive body cue:** Finally, we introduce a Structural Loss consisting of a scene-wise term and a point-wise term constraining the key landmark points and their relative configuration.
- **p. 4 / 4. Method - extractive body cue:** Then, we introduce the structural loss to improve the distillation process with both scene-wise loss and point-wise loss in Sec.
- **p. 5 / 4.2. Structural loss - extractive body cue:** Thus, we introduce a structural loss to further refine the distillation process and improve the completion quality.
- **p. 5 / 4.2. Structural loss - extractive body cue:** Thus, we introduce the point-wise loss to capture the relative structural information between different points in the 3D LiDAR scene.
- **p. 3 / 3.1. Brief introduction of diffusion models - extractive body cue:** The diffusion model ϵθ predicts the noise according to xt, c, t and is then optimized by calculating the ℓ2 loss between the predicted and ...
- **p. 3 / 3.2. 3D LiDAR scene completion diffusion models - extractive body cue:** In this case, the training loss of the diffusion model is given by: LDM = Et,ϵ h
- **p. 6 / 4.3. Optimization procedure - extractive body cue:** Then, Gstu is optimized with the following objective Lstu = LKL + Lstructural (18) We set λscene = 0.5 and λpoint = 0.01 defaultly.

## Observation, State, and Output Interface

| 항목 | 원문에서 확인한 범위 |
|---|---|
| 입력 | 부분 라이다 스캔 |
| 표현 | 거리·깊이 기반 장면 특징과 증류한 모델 |
| 출력 | 밀도를 높인 완성 라이다 장면 |
| 평가 | SemanticKITTI의 기하 정확도와 샘플링 시간 |

[원문 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.pdf#page=3) · [원문 7쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.pdf#page=7)

## Main Claims and Actual Contribution

- 교사의 분포를 따르는 증류에 장면 구조 손실을 더해, 샘플링 단계를 줄일 때도 완성한 점군의 기하를 보존하도록 학습한다. [PDF 4쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.pdf#page=5)
- SemanticKITTI에서 완성 품질과 프레임당 시간을 함께 비교하고 구조 손실을 제거했을 때의 변화를 측정했다. [PDF 6쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.pdf#page=7)

## Evaluation Scope

SemanticKITTI 표 1에서 정제 단계를 포함한 프레임당 샘플링 시간은 LiDiff 30.55초, ScoreLiDAR 5.37초다. 같은 행에서 Chamfer 거리와 JSD는 낮아졌고 EMD는 23.16에서 23.26으로 높아졌다. [PDF 6쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.pdf#page=6)

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusion - extractive body cue:** Thus, further exploration is required to find a more effective method to improve the training process of ScoreLiDAR and avoid the limitations of the teacher ...
- **p. 7 / 5.2. Ablation study - extractive body cue:** We compared the scene completion performances of the proposed ScoreLiDAR with a variant that does not incorporate structural loss.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 3 (3.2. 3D LiDAR scene completion diffusion models), p. 4 (4. Method), p. 3 (3.1. Brief introduction of diffusion models)이다.

## 검색 태그 근거

부분 라이다 스캔에서 전체 장면을 복원하는 확산 교사의 결과를 짧은 단계의 학생 모델로 증류한다. SemanticKITTI에서 형상 완성 품질과 샘플링 시간을 평가했다. [원문 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.pdf#page=3) · [원문 7쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.pdf#page=7)
