# ReferSplat: Referring Segmentation in 3D Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=reuShgiHdg.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/165044. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, Gaussian Splatting
- Official paper: https://openreview.net/forum?id=reuShgiHdg
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/165044
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, these methods face significant limitations when applied to R3DGS.를 문제로 두고, To bridge this gap, we introduce a new task: Referring 3D Gaussian Splatting Segmentation (R3DGS), which focuses on segmenting objects in a 3D Gaussian scene based on natural language expressions that typically ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce Referring 3D Gaussian Splatting Segmentation (R3DGS), a new task that aims to segment target objects in a 3D Gaussian scene based on natural ...
- **p. 1 / Abstract - extractive body cue:** This task requires the model to identify newly described objects that may be occluded or not directly visible in a novel view, posing a significant ...
- **p. 1 / Abstract - extractive body cue:** Developing this capability is crucial for advancing embodied AI.
- **p. 1 / Abstract - extractive body cue:** To support research in this area, we construct the first R3DGS dataset, Ref-LERF.
- **p. 1 / Abstract - extractive body cue:** Our analysis reveals that 3D multimodal understanding and spatial relationship modeling are key challenges for R3DGS.
- **p. 2 / 1. Introduction - extractive body cue:** However, these methods face significant limitations when applied to R3DGS.
- **p. 1 / 1. Introduction - extractive body cue:** To bridge this gap, we introduce a new task: Referring 3D Gaussian Splatting Segmentation (R3DGS), which focuses on segmenting objects in a 3D Gaussian scene ...

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** To bridge this gap, we introduce a new task: Referring 3D Gaussian Splatting Segmentation (R3DGS), which focuses on segmenting objects in a 3D Gaussian scene ...
- **p. 2 / 1. Introduction - extractive body cue:** To enhance spatial reasoning, we introduce a Position-aware Cross-Modal Interaction module that extracts position features for both Gaussians and language descriptions.
- **p. 2 / 1. Introduction - extractive body cue:** In this work, we propose ReferSplat, an end-to-end framework that models 3D Gaussian points with natural language expressions in a spatially aware paradigm for Referring ...
- **p. 3 / 3.2. Problem Statement and Method Overview - extractive body cue:** To infuse languageawareness into the 3D Gaussians, we introduce a new property called referring features.
- **p. 4 / 3.3. 3D Gaussian Referring Fields - extractive body cue:** 2, our method surpasses existing approaches, establishing a superior referring segmentation framework in 3D Gaussian scenes.
- **p. 5 / 3.4. Position-aware Cross-Modal Interaction - extractive body cue:** To address these issues, we propose a Position-aware CrossModal Interaction module that injects position information into the cross-modal attention mechanism to facilitate interactions between textual ...
- **p. 5 / 3.4. Position-aware Cross-Modal Interaction - extractive body cue:** To integrate position information, we first extract position features from 3D Gaussian representations.
- **p. 4 / 3.3. 3D Gaussian Referring Fields - extractive body cue:** Inspired by methods that incorporate semantic feature vectors to construct semantic-aware fields (Qin et al., 2024; Zhou et al., 2024b; Qu et al., 2024), we ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | While the proposed Position-aware Cross-Modal Interaction module effectively captures the relationship between Gaussian representations and text descriptions, distinguishing between languages with similar meanings but referring to diffe ... | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (3.5. Gaussian-Text Contrastive Learning), p. 2 (1. Introduction) |
| State/latent | While, Position-aware, Cross-Modal, Interaction, module, effectively, captures, relationship, between, Gaussian, representations, text | geometry, map, object/relationship state | p. 5 (3.5. Gaussian-Text Contrastive Learning), p. 2 (1. Introduction), p. 4 (3.3. 3D Gaussian Referring Fields) |
| Output/action | During inference, output masks are obtained by matching the input open-vocabulary class names with the rendered feature, as shown in Fig. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 4 (3.3. 3D Gaussian Referring Fields), p. 4 (3.3. 3D Gaussian Referring Fields) |
| Objective/outcome | The total training objective is: Lloss = Lbce + λLcon, (10) where λ is used for balancing the contrastive loss Lcon. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (3.5. Gaussian-Text Contrastive Learning), p. 4 (3.3. 3D Gaussian Referring Fields), p. 5 (3.4. Position-aware Cross-Modal Interaction) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** To bridge this gap, we introduce a new task: Referring 3D Gaussian Splatting Segmentation (R3DGS), which focuses on segmenting objects in a 3D Gaussian scene ...
- **p. 2 / 1. Introduction - extractive body cue:** To enhance spatial reasoning, we introduce a Position-aware Cross-Modal Interaction module that extracts position features for both Gaussians and language descriptions.
- **p. 2 / 1. Introduction - extractive body cue:** In this work, we propose ReferSplat, an end-to-end framework that models 3D Gaussian points with natural language expressions in a spatially aware paradigm for Referring ...
- **p. 3 / 3.2. Problem Statement and Method Overview - extractive body cue:** To infuse languageawareness into the 3D Gaussians, we introduce a new property called referring features.
- **p. 4 / 3.3. 3D Gaussian Referring Fields - extractive body cue:** 2, our method surpasses existing approaches, establishing a superior referring segmentation framework in 3D Gaussian scenes.
- **p. 8 / 4.6. Analysis of Computation Costs - extractive body cue:** Results show that ReferSplat achieves significantly lower computational complexity and faster inference speed than LangSplat (Qin et al., 2024).
- **p. 7 / 4.3. Ablation Study - extractive body cue:** 2 show that our method significantly outperforms all baselines, demonstrating that the proposed 3D Referring Feature Fields effectively models the relationship between 3D Gaussians and ...
- **p. 7 / 4.3. Ablation Study - extractive body cue:** When integrating all components (index 3), referred to as ReferSplat, we achieve a substantial performance gain, reaching a new state-of-the-art.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4.6. Analysis of Computation Costs), p. 7 (4.3. Ablation Study) |
| Embodiment/environment | The LERF dataset (Kerr et al., 2023) is collected using the Polycam iPhone app and consists of four diverse, complex, real-world scenes. | hardware/simulator version and reset protocol | p. 6 (4.1. Ref-LERF Dataset and Evaluation Metrics), p. 7 (4.3. Ablation Study) |
| Dataset/benchmark | This demonstrates that Ref-LERF places a stronger emphasis on spatial reasoning and detailed object understanding compared to previous datasets. | role, split, size and leakage | p. 6 (4.1. Ref-LERF Dataset and Evaluation Metrics), p. 7 (4.3. Ablation Study), p. 6 (4.1. Ref-LERF Dataset and Evaluation Metrics), p. 8 (4.6. Analysis of Computation Costs) |
| Metric | In contrast, alternative approaches-such as using the top-1 prediction, propagating the first-frame mask with SAM2 (Ravi et al., 2025), or selecting masks solely based on IoU without confidence weighting-yield inferior results. | definition, denominator, direction and uncertainty | p. 7 (4.3. Ablation Study), p. 6 (4.1. Ref-LERF Dataset and Evaluation Metrics), p. 7 (4.3. Ablation Study) |
| Baseline/ablation | 1, incorporating PCMI (index 1) improves mIoU by 5.1% and 4.3%, respectively compared to the baseline, which is our constructed Referring Feature Fields. | fair input/data/compute/action matching | p. 7 (4.3. Ablation Study), p. 7 (4.3. Ablation Study), p. 6 (4.1. Ref-LERF Dataset and Evaluation Metrics) |

## Explicit Limitations and Failure Boundary

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Comparison of (a) existing open-vocabulary 3DGS seg- mentation pipeline and (b) the proposed ReferSplat for R3DGS. 3D scene representation learning. During inference, output ...
- **p. 9 / 6. Limitation and Future Work - extractive body cue:** 1) Our current method does not account for dynamic factors, which are crucial for real-world applications.
- **p. 9 / 6. Limitation and Future Work - extractive body cue:** 2) While we focus on 3D referring segmentation in Gaussian Splatting, our method does not incorporate 3D visual grounding.
- **p. 8 / 4.4. Results on the Ref-LERF Dataset - extractive body cue:** Our 3D Gaussian Referring Fields enable the model to recognize occluded or non-visible objects by leveraging multi-view 3D scene knowledge-an inherent limitation of 2D-based methods.
- **p. 8 / 4.8. Impact of Referring Feature Dimension - extractive body cue:** Smaller dimensions (e.g., 1 or 4) lack the capacity to store discriminative features, while larger dimensions (e.g., 32) introduce redundancy and noise, degrading performance.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, these methods face significant limitations when applied to R3DGS.를 문제로 두고, To bridge this gap, we introduce a new task: Referring 3D Gaussian Splatting Segmentation (R3DGS), which focuses on segmenting objects in a 3D Gaussian scene based on natural language expressions that typically ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Problem Statement and Method Overview), p. 5 (3.4. Position-aware Cross-Modal Interaction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
