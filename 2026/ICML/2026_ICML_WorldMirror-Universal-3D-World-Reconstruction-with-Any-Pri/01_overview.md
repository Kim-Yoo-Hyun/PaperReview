# WorldMirror: Universal 3D World Reconstruction with Any-Prior Prompting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=HFNJOpXHfm.
> PDF retrieval source: https://openreview.net/pdf/d37648c3826e3031b270765b6a36790ab19140f8.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D reconstruction, 3D Vision
- Official paper: https://openreview.net/forum?id=HFNJOpXHfm
- Full-text retrieval: https://openreview.net/pdf/d37648c3826e3031b270765b6a36790ab19140f8.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Pow3R (Jang et al., 2025) enables prior-conditioned binocular reconstruction but outputs only point maps, while VGGT (Wang et al., 2025a) predicts multiple geometric quantities but lacks the ability to incorporate auxiliary inputs.를 문제로 두고, We summarize our contributions as follows: (1) We present WorldMirror, a unified end-to-end framework for 3D geometry that jointly addresses flexible prior conditioning and comprehensive multi-task prediction within a single model.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present WorldMirror, a unified feed-forward model for comprehensive 3D geometric prediction tasks.
- **p. 1 / Abstract - extractive body cue:** Unlike existing methods constrained to image-only inputs or customized for a specific task, our framework flexibly integrates diverse geometric priors, including camera poses, intrinsics, and ...
- **p. 1 / Abstract - extractive body cue:** Remarkably, prior injection yields universal gains across all tasks, suggesting that input flexibility and multi-task prediction are mutually reinforcing.
- **p. 1 / Abstract - extractive body cue:** WorldMirror achieves state-of-the-art performance across diverse benchmarks from camera, point map, depth, and surface normal estimation
- **p. 1 / 1. Introduction - extractive body cue:** Visual geometry learning is fundamental to augmented reality, robotics, and autonomous navigation.
- **p. 2 / 1. Introduction - extractive body cue:** Pow3R (Jang et al., 2025) enables prior-conditioned binocular reconstruction but outputs only point maps, while VGGT (Wang et al., 2025a) predicts multiple geometric quantities but ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we introduce WorldMirror, a unified end-to-end framework that performs comprehensive 3D tasks while flexibly leveraging any available geometric modalities.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** We summarize our contributions as follows: (1) We present WorldMirror, a unified end-to-end framework for 3D geometry that jointly addresses flexible prior conditioning and comprehensive ...
- **p. 2 / 1. Introduction - extractive body cue:** (3) We introduce a Unified Spatial Prediction architecture with a decoupled sequential training that effectively coordinates multi-task training across camera poses, depth, normals, point maps, ...
- **p. 3 / 3. Method - extractive body cue:** We introduce two core components: (1) Multi-modal Tokenization (Sec.
- **p. 4 / 3.1. Multi-modal Tokenization - extractive body cue:** Besides real photos, our method generalizes well to AI-created videos spanning diverse styles. dropped tokens to zero.
- **p. 4 / 3.2. Unified Spatial Prediction - extractive body cue:** To address these issues, we introduce a decoupled modeling strategy that separates geometry prediction from appearance reconstruction, along with a curriculum learning scheme that progressively ...
- **p. 4 / 3.2. Unified Spatial Prediction - extractive body cue:** Inspired by the architecture used in VGGT (Wang et al., 2025a), we construct a Transformer backbone with a global-local attention mechanism and multi-head decoders for ...
- **p. 3 / 3. Method - extractive body cue:** 3.2), a multi-task architecture with curriculum learning that produces comprehensive geometric outputs, including point maps, camera poses, depth maps, surface normals, and 3D Gaussians.
- **p. 5 / 3.2. Unified Spatial Prediction - extractive body cue:** We then incorporate the normal prediction task into the joint training scheme.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (2) We propose Multi-modal Tokenization, which treats multiple input types including RGB images, camera intrinsics, poses, and depth as tokens, enabling seamless integration of these geometric priors without architectural modifications. | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 3 (3. Method) |
| State/latent | Multi-modal, Tokenization, treats, multiple, input, types, including, RGB, images, camera, intrinsics, poses | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 3 (3. Method), p. 3 (3. Method) |
| Output/action | 3.1), which encodes diverse input modalities, including camera intrinsics, poses, and depth maps, into a unified token sequence; and (2) Unified Spatial Prediction (Sec. | point map, pose, scene graph, affordance 또는 query result | p. 3 (3. Method), p. 3 (3. Method), p. 5 (3.2. Unified Spatial Prediction) |
| Objective/outcome | Our model is trained end-to-end by minimizing a composite loss function L that integrates supervision for all prediction 5 | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (4. Model Training), p. 4 (3.1. Multi-modal Tokenization), p. 5 (3.2. Unified Spatial Prediction) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** We summarize our contributions as follows: (1) We present WorldMirror, a unified end-to-end framework for 3D geometry that jointly addresses flexible prior conditioning and comprehensive ...
- **p. 2 / 1. Introduction - extractive body cue:** (3) We introduce a Unified Spatial Prediction architecture with a decoupled sequential training that effectively coordinates multi-task training across camera poses, depth, normals, point maps, ...
- **p. 3 / 3. Method - extractive body cue:** We introduce two core components: (1) Multi-modal Tokenization (Sec.
- **p. 4 / 3.1. Multi-modal Tokenization - extractive body cue:** Besides real photos, our method generalizes well to AI-created videos spanning diverse styles. dropped tokens to zero.
- **p. 4 / 3.2. Unified Spatial Prediction - extractive body cue:** To address these issues, we introduce a decoupled modeling strategy that separates geometry prediction from appearance reconstruction, along with a curriculum learning scheme that progressively ...
- **p. 8 / 5.1. Evaluation on Different Tasks - extractive body cue:** 3 shows substantial improvements over existing methods, demonstrating that multi-task learning with shared representations can outperform specialized single-task approaches.
- **p. 7 / 5.1. Evaluation on Different Tasks - extractive body cue:** Incorporating priors further improves results; using all priors yields 58.1% and 53.1% accuracy gains on 7-Scenes and NRGBD over our no-prior baseline, demonstrating effective prior ...
- **p. 7 / 5.1. Evaluation on Different Tasks - extractive body cue:** 2, our method achieves superior zero-shot performance on RealEstate10K and TUM-dynamics, while remaining competitive on Sintel despite limited outdoor dynamic scenes data involved in the ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (5.1. Evaluation on Different Tasks), p. 7 (5.1. Evaluation on Different Tasks) |
| Embodiment/environment | We evaluate point map reconstruction on scene-level datasets, including 7-Scenes (Shotton et al., 2013), NRGBD (Azinovi´c et al., 2022) and objectlevel dataset DTU (Jensen et al., 2014), using the same sequence mappings ... | hardware/simulator version and reset protocol | p. 7 (5.1. Evaluation on Different Tasks), p. 7 (5. Experiments) |
| Dataset/benchmark | Results are averaged over ETH3D and DTU datasets with 10 views as input. ‘Single token' offers both superior performance and high efficiency. | role, split, size and leakage | p. 7 (5.1. Evaluation on Different Tasks), p. 7 (5. Experiments), p. 8 (5.1. Evaluation on Different Tasks), p. 8 (5.1. Evaluation on Different Tasks) |
| Metric | 1, our method without priors already surpasses VGGT and π3, with 10.4% and 17.8% accuracy gains on 7-Scenes and DTU. | definition, denominator, direction and uncertainty | p. 7 (5.1. Evaluation on Different Tasks), p. 7 (5.1. Evaluation on Different Tasks), p. 17 (Figure/Table caption) |
| Baseline/ablation | Incorporating priors further improves results; using all priors yields 58.1% and 53.1% accuracy gains on 7-Scenes and NRGBD over our no-prior baseline, demonstrating effective prior utilization. | fair input/data/compute/action matching | p. 7 (5.1. Evaluation on Different Tasks), p. 8 (5.3. Comparison with Prior-guided Methods), p. 8 (5.3. Comparison with Prior-guided Methods) |

## Explicit Limitations and Failure Boundary

- **p. 16 / Figure/Table caption - extractive body cue:** Table 12. Robustness evaluation of WorldMirror with noisy priors on 7-Scenes and DTU datasets. The model exhibits graceful degradation under various noise conditions. Prior Type ...
- **p. 8 / 5.1. Evaluation on Different Tasks - extractive body cue:** Trained with dynamic resolutions, our model generalizes robustly across varying resolutions and consistently surpasses baselines.
- **p. 23 / Figure/Table caption - extractive body cue:** Figure 11. Visual Comparisons of In-The-Wild Multi-View 3D Reconstruction. WorldMirror delivers superior reconstruction fidelity with in-the-wild images as input, generating more plausible results in challenging ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Pow3R (Jang et al., 2025) enables prior-conditioned binocular reconstruction but outputs only point maps, while VGGT (Wang et al., 2025a) predicts multiple geometric quantities but lacks the ability to incorporate auxiliary inputs.를 문제로 두고, We summarize our contributions as follows: (1) We present WorldMirror, a unified end-to-end framework for 3D geometry that jointly addresses flexible prior conditioning and comprehensive multi-task prediction within a single model.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 4 (3.2. Unified Spatial Prediction), p. 4 (3.2. Unified Spatial Prediction), p. 3 (3. Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
