# Object-X: Learning to Reconstruct Multi-Modal 3D Object Representations

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://neurips.cc/virtual/2025/poster/116149.
> PDF retrieval source: https://arxiv.org/pdf/2506.04789. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: Gaia Di Lorenzo, Federico Tombari, Marc Pollefeys, Daniel Barath
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision
- Official paper: https://neurips.cc/virtual/2025/poster/116149
- Published PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/259774803d1f4302cb0a1eff47562888-Paper-Conference.pdf
- Full-text retrieval at original review: https://arxiv.org/pdf/2506.04789
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

Object-X는 영상·점군·텍스트로부터 물체별 임베딩을 만들고 이를 3차원 재구성이나 위치 식별에 다시 사용한다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/259774803d1f4302cb0a1eff47562888-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Learning effective multi-modal 3D representations of objects is essential for numerous applications, such as augmented reality and robotics.
- **p. 1 / Abstract - extractive body cue:** Existing methods often rely on task-specific embeddings that are tailored either for semantic understanding or geometric reconstruction.
- **p. 1 / Abstract - extractive body cue:** As a result, these embeddings typically cannot be decoded into explicit geometry and simultaneously reused across tasks.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose Object-X, a versatile multi-modal object representation framework capable of encoding rich object embeddings (e.g., images, point cloud, text) and decoding ...
- **p. 1 / Abstract - extractive body cue:** Object-X operates by geometrically grounding the captured modalities in a 3D voxel grid and learning an unstructured embedding fusing the information from the voxels with ...
- **p. 3 / 1 Introduction - extractive body cue:** However, a key limitation is that these embeddings typically lack a generative or reconstructive capability; they cannot be decoded back into explicit object geometry or ...
- **p. 2 / 1 Introduction - extractive body cue:** However, a critical limitation persists: existing object embeddings are generally learned for specific tasks and cannot be decoded to reconstruct the explicit, high-fidelity appearance and ...

## Core Idea

- **p. 4 / 1 Introduction - extractive body cue:** 3 Learning Versatile Object Embeddings We propose Object-X, taking a reconstructed scene with a 3D object segmentation as input and learning a compact and descriptive ...
- **p. 5 / 1 Introduction - extractive body cue:** Specifically, we introduce a decompression function fdecomp that maps w back to a predicted ˆz = {ˆzi, pi}L i=1.
- **p. 10 / Method - extractive body cue:** Our method, along with SceneGraphLoc and the recent CrossOver [23], uses a ViT to extract per-patch object embeddings from the query image.
- **p. 10 / Method - extractive body cue:** Unlike SGAligner, explicitly trained for this task using point cloud and object-level modalities, our method relies solely on the proposed Object-X embedding trained with reconstruction ...
- **p. 3 / 1 Introduction - extractive body cue:** The embedding is trained with a masked mean squared error loss to ensure accurate reconstruction of the SLat, which in turn enables decoding into 3D ...
- **p. 9 / Method - extractive body cue:** Object-X is then applied to obtain the object embedding from this input which is then fed directly into our decoder.
- **p. 9 / Method - extractive body cue:** In contrast, Object-X focuses on reconstruction rather than generation, leveraging voxel-grounded latent representations to maintain geometric consistency even under large appearance or domain shifts.
- **p. 10 / Method - extractive body cue:** In constrast to the baselines, Object-X is used without training on this task.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 3 Learning Versatile Object Embeddings We propose Object-X, taking a reconstructed scene with a 3D object segmentation as input and learning a compact and descriptive embedding for each object from their associated ... | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (1 Introduction), p. 4 (1 Introduction) |
| State/latent | Learning, Versatile, Object, Embeddings, Object-X, taking, reconstructed, scene, segmentation, input, compact, descriptive | geometry, map, object/relationship state | p. 4 (1 Introduction), p. 4 (1 Introduction), p. 2 (1 Introduction) |
| Output/action | 3.1 Structured Latents from Multi-View Images Let a set of object instances O be given, where each object o = (P, I, M, A, . . . ) ∈O is associated with ... | point map, pose, scene graph, affordance 또는 query result | p. 4 (1 Introduction), p. 2 (1 Introduction), p. 9 (Method) |
| Objective/outcome | Unlike SGAligner, explicitly trained for this task using point cloud and object-level modalities, our method relies solely on the proposed Object-X embedding trained with reconstruction and localization losses, without finetuning for sc ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 10 (Method), p. 9 (Method), p. 9 (Method) |

## Main Claims and Actual Contribution

- 복셀 격자에서 양식별 관측을 공간적으로 대응시킨 뒤 물체 특징으로 집계해 Gaussian 기반 형상·외관을 복원한다. [PDF 3쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/259774803d1f4302cb0a1eff47562888-Paper-Conference.pdf#page=3) · [PDF 4쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/259774803d1f4302cb0a1eff47562888-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/259774803d1f4302cb0a1eff47562888-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/259774803d1f4302cb0a1eff47562888-Paper-Conference.pdf#page=6)
- 재구성의 시각·기하 품질과 물체 표현을 이용한 장면 정렬·위치 추정을 평가하고 저장 공간을 비교했다. [PDF 7쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/259774803d1f4302cb0a1eff47562888-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/259774803d1f4302cb0a1eff47562888-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/259774803d1f4302cb0a1eff47562888-Paper-Conference.pdf#page=9) · [PDF 10쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/259774803d1f4302cb0a1eff47562888-Paper-Conference.pdf#page=10)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Embodiment/environment | Since the test set lacks such annotations, we reorganized the original validation split, allocating 34 scenes (17 rooms) for validation and 123 scenes (30 rooms) for testing. | hardware/simulator version and reset protocol | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Dataset/benchmark | Since we train on 3RScan, comparisons on this dataset may be unfavorable to DepthSplat. | role, split, size and leakage | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Metric | We report NVS scores (SSIM, PSNR, LPIPS), geometric accuracy (Accuracy, Completion, and F1 score at a 0.05 m threshold), per-object run-time (secs), and storage (MB). | definition, denominator, direction and uncertainty | p. 7 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments) |
| Baseline/ablation | Even without training, we achieve the highest novel view synthesis scores compared to the baselines, being the closest to the reference 3DGS reconstruction. | fair input/data/compute/action matching | p. 8 (4 Experiments), p. 8 (4 Experiments), p. 23 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 5 Conclusion - extractive body cue:** Despite these advances, Object-X has limitations.
- **p. 10 / 5 Conclusion - extractive body cue:** Furthermore, while promising in zero-shot scenarios for tasks like single-image object reconstruction, performance does not yet consistently match that of optimized task-specific methods.
- **p. 7 / 4 Experiments - extractive body cue:** Scenes, where SceneGraphFusion fails to generate annotations, are excluded.
- **p. 7 / 4 Experiments - extractive body cue:** Since ScanNet does not provide scene graph annotations, we apply SceneGraphFusion [30] on RGB-D sequences to generate 3D instance segmentations and object relationships (used for ...
- **p. 8 / 4 Experiments - extractive body cue:** We omit geometric results for DepthSplat [32], which failed to produce reasonable geometry.
- **p. 8 / 4 Experiments - extractive body cue:** This reduces storage compared to full 3DGS but introduces a trade-off: reconstruction takes longer, and the quality may be slightly degraded.
- **p. 23 / Figure/Table caption - extractive body cue:** Figure 8: Qualitative comparison for full-scene composition. We compare the proposed Object-X to standard 3DGS [28] optimized on all unmasked scene images, and two 12-view ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 3 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 9 (Method)이다.
