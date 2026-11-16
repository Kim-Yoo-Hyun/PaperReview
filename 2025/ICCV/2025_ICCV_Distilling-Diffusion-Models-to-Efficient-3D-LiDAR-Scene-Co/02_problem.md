# Problem - Distilling Diffusion Models to Efficient 3D LiDAR Scene Completion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 3 (3.2. 3D LiDAR scene completion diffusion models), p. 2 (1. Introduction)): ScoreLiDAR aims to tackle the unique 3D distribution alignment challenge in LiDAR scene completion.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Diffusion models have been applied to 3D LiDAR scene completion due to their strong training stability and high completion quality.
- **p. 1 / Abstract - extractive body cue:** However, the slow sampling speed limits the practical application of diffusion-based scene completion models since autonomous vehicles require an efficient perception of surrounding environments.
- **p. 1 / Abstract - extractive body cue:** This paper proposes a novel distillation method tailored for 3D LiDAR scene completion models, dubbed ScoreLiDAR, which achieves efficient yet high-quality scene completion.
- **p. 1 / Abstract - extractive body cue:** ScoreLiDAR enables the distilled model to sample in significantly fewer steps after distillation.
- **p. 1 / Abstract - extractive body cue:** To improve completion quality, we also introduce a novel Structural Loss, which encourages the distilled model to capture the geometric structure of the 3D LiDAR ...
- **p. 2 / 1. Introduction - extractive body cue:** ScoreLiDAR aims to tackle the unique 3D distribution alignment challenge in LiDAR scene completion.
- **원문 대조:** LiDiff 배경 설명에서는 x^0=0인 noise offset을 각 원래 point p_m에 더한다. 결과는 p_m+sqrt(1−ᾱ^t)·ε^t 형태이며, point cloud 전체를 원점 주변으로 축소하는 식과 구분한다. ([PDF p. 3](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.pdf#page=3), §3.2, Eq. (6)).

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | ScoreLiDAR aims to tackle the unique 3D distribution alignment challenge in LiDAR scene completion. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Given the input x0 and the condition c (optional), the noisy data xt can be calculated by Eq. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Given, input, condition, optional, noisy, data, calculated, LiDAR, scan, ground | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | sparse, scan, noisy, completed, scene, input, because, student | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Given, input, condition, optional, noisy, data, calculated, LiDAR, scan, ground | p. 3 (3.1. Brief introduction of diffusion models), p. 3 (3.2. 3D LiDAR scene completion diffusion models), p. 4 (3.2. 3D LiDAR scene completion diffusion models) |
| Decision / output variable | geometry/map/query r; body terms: ScoreLiDAR, novel, distillation, tailored, LiDAR, scene, completion, diffusion | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (4. Method) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: solve, issue, introduce, scene-wise, loss, minimizes, distance, between | p. 4 (4.1. Distillation for 3D LiDAR scene completion), p. 5 (4.2. Structural loss), p. 3 (3.2. 3D LiDAR scene completion diffusion models), p. 3 (3.1. Brief introduction of diffusion models), p. 4 (3.2. 3D LiDAR scene completion diffusion models), p. 5 (4.2. Structural loss) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (4.3. Optimization procedure), p. 4 (4. Method), p. 3 (3.1. Brief introduction of diffusion models) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (5.2. Ablation study), p. 7 (5.3. Qualitative analysis), p. 2 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **원문 대조:** LiDiff 배경 설명에서는 x^0=0인 noise offset을 각 원래 point p_m에 더한다. 결과는 p_m+sqrt(1−ᾱ^t)·ε^t 형태이며, point cloud 전체를 원점 주변으로 축소하는 식과 구분한다. ([PDF p. 3](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.pdf#page=3), §3.2, Eq. (6)).
- **p. 2 / 1. Introduction - extractive body cue:** Prior studies [15, 19, 34, 35] demonstrated that the bidirectional gradient guidance mechanism can effectively accelerate 3D rendering speed.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (4. Method), p. 5 (4.2. Structural loss), p. 5 (4.2. Structural loss)): In this work, we propose ScoreLiDAR, a novel distillation method tailored for 3D LiDAR scene completion diffusion models, which enables efficient and high-quality scene completion (Fig.

- **p. 2 / 1. Introduction - extractive body cue:** Finally, we introduce a Structural Loss consisting of a scene-wise term and a point-wise term constraining the key landmark points and their relative configuration.
- **p. 4 / 4. Method - extractive body cue:** Then, we introduce the structural loss to improve the distillation process with both scene-wise loss and point-wise loss in Sec.
- **p. 5 / 4.2. Structural loss - extractive body cue:** Thus, we introduce a structural loss to further refine the distillation process and improve the completion quality.
- **p. 5 / 4.2. Structural loss - extractive body cue:** Thus, we introduce the point-wise loss to capture the relative structural information between different points in the 3D LiDAR scene.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Thus, further exploration is required to find a more effective method to improve the training process of ScoreLiDAR ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | We compared the scene completion performances of the proposed ScoreLiDAR with a variant that does not incorporate structural ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3.1. Brief introduction of diffusion models), p. 3 (3.2. 3D LiDAR scene completion diffusion models), p. 4 (3.2. 3D LiDAR scene completion diffusion models), p. 5 (4.2. Structural loss). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 3 (3.2. 3D LiDAR scene completion diffusion models), p. 2 (1. Introduction), interface p. 3 (3.1. Brief introduction of diffusion models), p. 3 (3.2. 3D LiDAR scene completion diffusion models), p. 4 (3.2. 3D LiDAR scene completion diffusion models), p. 5 (4.2. Structural loss), objective p. 4 (4.1. Distillation for 3D LiDAR scene completion), p. 5 (4.2. Structural loss), p. 3 (3.2. 3D LiDAR scene completion diffusion models), p. 3 (3.1. Brief introduction of diffusion models), p. 4 (3.2. 3D LiDAR scene completion diffusion models), p. 5 (4.2. Structural loss).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
