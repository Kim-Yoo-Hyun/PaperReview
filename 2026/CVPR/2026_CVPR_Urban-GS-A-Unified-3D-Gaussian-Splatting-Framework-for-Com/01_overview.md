# Urban-GS: A Unified 3D Gaussian Splatting Framework for Compact and High-Fidelity Aerial-to-Street Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Urban-GS_A_Unified_3D_Gaussian_Splatting_Framework_for_Compact_and_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Urban-GS_A_Unified_3D_Gaussian_Splatting_Framework_for_Compact_and_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Urban-GS_A_Unified_3D_Gaussian_Splatting_Framework_for_Compact_and_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Urban-GS_A_Unified_3D_Gaussian_Splatting_Framework_for_Compact_and_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: system
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 In this work, we propose Urban-GS, a novel framework that resolves the above challenges to deliver compact, high-fidelity unified aerial-to-street reconstruction.를 문제로 두고, This method resolves densification conflicts, enabling joint contributions and enhancing overall reconstruction fidelity. • A Contribution-based Anchor Pruning method that enables reliable and efficient removal of redundant anchors in m ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recently, 3D Gaussian Splatting (3DGS) has revolutionized radiance field reconstruction, enabling efficient and highfidelity novel view synthesis.
- **p. 1 / Abstract - extractive body cue:** However, seamless integration of both aerial and street view images to model urban scenes remains a significant challenge for 3DGS.
- **p. 1 / Abstract - extractive body cue:** This joint setting suffers from extreme view coverage disparity, complex multi-scale details, and imbalanced viewpoint distributions.
- **p. 1 / Abstract - extractive body cue:** In this work, we present Urban-GS, a novel framework built upon Gaussian Splatting for the compact unified reconstruction and high-fidelity rendering of urban scenes from ...
- **p. 1 / Abstract - extractive body cue:** Specifically, we first develop an Aerial-Street Joint Adaptive Densification method to resolve the densification conflicts arising from large view coverage disparity.
- **p. 2 / 1. Introduction - extractive body cue:** In this work, we propose Urban-GS, a novel framework that resolves the above challenges to deliver compact, high-fidelity unified aerial-to-street reconstruction.
- **p. 2 / 1. Introduction - extractive body cue:** This limitation highlights the necessity of jointly reconstructing scenes using aerial and street view imagery, as the complementary perspectives offered by these two modalities are ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** This method resolves densification conflicts, enabling joint contributions and enhancing overall reconstruction fidelity. • A Contribution-based Anchor Pruning method that enables reliable and efficient removal ...
- **p. 2 / 1. Introduction - extractive body cue:** To summarize, the main contributions of our method are: • An in-depth analysis of the densification conflicts in aerial-street scene reconstruction, and a corresponding Aerial-Street ...
- **p. 4 / 4. Methods - extractive body cue:** 4.2, we present a contribution-based anchor pruning strategy adopted in Urban-GS to mitigate the excessive memory consumption caused by capturing multi-scale scene details.
- **p. 5 / 4.2. Contribution-based Anchor Pruning - extractive body cue:** To address this issue, we propose a contributionweighted mask regularization term.
- **p. 6 / 4.3. Global-to-Local Optimization - extractive body cue:** Efficiency comparison between our method and Horizon-GS [10] on the Horizon-GS dataset. stage.
- **p. 4 / 4. Methods - extractive body cue:** In this section, we first analyze the conflicts during gradient accumulation in unified aerial-street modeling (Sec.
- **p. 5 / 4.3. Global-to-Local Optimization - extractive body cue:** In the global training stage, the entire view set is used for scene modeling based on the methods described in Sec.
- **p. 5 / 4.2. Contribution-based Anchor Pruning - extractive body cue:** To achieve this goal, we integrate the structured 3D Gaussian representation [23] with probabilistic masks [17] and progressively prune redundant anchors throughout the training process.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Concurrently, the drastic variation in projection areas across different views arises precisely from the large variation in observation distances inherent to the joint aerial-street view set. | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (4.1. Aerial-Street Joint Adaptive Densification), p. 4 (4.1. Aerial-Street Joint Adaptive Densification) |
| State/latent | Concurrently, drastic, variation, projection, areas, across, different, views, arises, precisely, large, observation | geometry, map, object/relationship state | p. 4 (4.1. Aerial-Street Joint Adaptive Densification), p. 4 (4.1. Aerial-Street Joint Adaptive Densification), p. 5 (4.2. Contribution-based Anchor Pruning) |
| Output/action | Counterintuitively, involving richer inputs in the densification process yields poorer performance than using a single view type, which indicates the presence of gradient conflicts between aerial and street views. | point map, pose, scene graph, affordance 또는 query result | p. 4 (4.1. Aerial-Street Joint Adaptive Densification), p. 5 (4.2. Contribution-based Anchor Pruning), p. 5 (4.2. Contribution-based Anchor Pruning) |
| Objective/outcome | Quantitative comparison across accumulating gradients for densification from aerial views only, street views only and merged views on Colosseum scene [10]. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (4.1. Aerial-Street Joint Adaptive Densification), p. 6 (4.3. Global-to-Local Optimization), p. 4 (4.1. Aerial-Street Joint Adaptive Densification) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** This method resolves densification conflicts, enabling joint contributions and enhancing overall reconstruction fidelity. • A Contribution-based Anchor Pruning method that enables reliable and efficient removal ...
- **p. 2 / 1. Introduction - extractive body cue:** To summarize, the main contributions of our method are: • An in-depth analysis of the densification conflicts in aerial-street scene reconstruction, and a corresponding Aerial-Street ...
- **p. 4 / 4. Methods - extractive body cue:** 4.2, we present a contribution-based anchor pruning strategy adopted in Urban-GS to mitigate the excessive memory consumption caused by capturing multi-scale scene details.
- **p. 5 / 4.2. Contribution-based Anchor Pruning - extractive body cue:** To address this issue, we propose a contributionweighted mask regularization term.
- **p. 6 / 4.3. Global-to-Local Optimization - extractive body cue:** Efficiency comparison between our method and Horizon-GS [10] on the Horizon-GS dataset. stage.
- **p. 8 / 5.3. Ablations Study and Analysis - extractive body cue:** 5 and 8 show that additional iterations under uniform sampling yield no significant performance improvement, whereas our proposed strategy achieves a more noticeable gain.
- **p. 7 / 5.2. Experiment Results and Analysis - extractive body cue:** 2, our method outperforms the performance of all baselines on the HorizonGS dataset.
- **p. 7 / 5.2. Experiment Results and Analysis - extractive body cue:** The above experimental results quantitatively validate that our method achieves superior reconstruction quality and efficiency.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (5.3. Ablations Study and Analysis), p. 7 (5.2. Experiment Results and Analysis) |
| Embodiment/environment | Following Horizon-GS [10], we conduct comprehensive evaluations across 7 scenes containing both aerial and street views, sourced from the UC-GS dataset [40], and Horizon-GS dataset [10]. | hardware/simulator version and reset protocol | p. 6 (5.1. Experimental Setup), p. 7 (5.1. Experimental Setup) |
| Dataset/benchmark | Quantitative comparison on UC-GS dataset [40]. | role, split, size and leakage | p. 6 (5.1. Experimental Setup), p. 7 (5.1. Experimental Setup), p. 7 (5.2. Experiment Results and Analysis), p. 8 (5.3. Ablations Study and Analysis) |
| Metric | For the global training stage, we set the learning rate of the mask scores to 0.01 and λm to 0.003, while retaining other parameter settings consistent with Horizon-GS [10]. | definition, denominator, direction and uncertainty | p. 6 (5.1. Experimental Setup), p. 8 (5.3. Ablations Study and Analysis), p. 8 (5.3. Ablations Study and Analysis) |
| Baseline/ablation | 2, our method outperforms the performance of all baselines on the HorizonGS dataset. | fair input/data/compute/action matching | p. 7 (5.2. Experiment Results and Analysis), p. 7 (5.2. Experiment Results and Analysis), p. 1 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. The overview pipeline of Urban-GS. Top (Gloabal Training): We start by initializing LOD-structured anchors from SfM- derived points of the aerial-to-street urban scene, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Efficiency comparison between our method and Horizon-GS [10] on the Horizon-GS dataset. stage. For each selected target unstable view vus, we con- struct ...
- **p. 8 / 5.3. Ablations Study and Analysis - extractive body cue:** This limitation is evident in its struggles in the unified aerial-street setting.
- **p. 8 / 5.3. Ablations Study and Analysis - extractive body cue:** However, this approach fundamentally fails to account for the contribution variations caused by drastic changes in projection areas.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Average position gradient (a) and average projection radius (b) for two sets of neural Gaussians over the densification process. Left plots: Analysis of ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 In this work, we propose Urban-GS, a novel framework that resolves the above challenges to deliver compact, high-fidelity unified aerial-to-street reconstruction.를 문제로 두고, This method resolves densification conflicts, enabling joint contributions and enhancing overall reconstruction fidelity. • A Contribution-based Anchor Pruning method that enables reliable and efficient removal of redundant anchors in m ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 4 (4. Methods), p. 5 (4.3. Global-to-Local Optimization), p. 5 (4.2. Contribution-based Anchor Pruning) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
