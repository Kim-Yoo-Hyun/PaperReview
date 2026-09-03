# MAPo: Motion-Aware Partitioning of Deformable 3D Gaussian Splatting for High-Fidelity Dynamic Scene Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Jiao_MAPo_Motion-Aware_Partitioning_of_Deformable_3D_Gaussian_Splatting_for_High-Fidelity_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Jiao_MAPo_Motion-Aware_Partitioning_of_Deformable_3D_Gaussian_Splatting_for_High-Fidelity_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Jiao_MAPo_Motion-Aware_Partitioning_of_Deformable_3D_Gaussian_Splatting_for_High-Fidelity_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Jiao_MAPo_Motion-Aware_Partitioning_of_Deformable_3D_Gaussian_Splatting_for_High-Fidelity_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Despite promising results, these methods suffer from two critical limitations inherent in their deformation framework: • Bottleneck in Motion Modeling Capacity: As shown in Fig.를 문제로 두고, Our key contributions are summarized as follows: • We propose MAPo, a novel framework for high-fidelity dynamic scene reconstruction based on a dynamic scorebased partitioning strategy.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D Gaussian Splatting, known for enabling high-quality static scene reconstruction with fast rendering, is increasingly being applied to multi-view dynamic scene reconstruction.
- **p. 1 / Abstract - extractive body cue:** A common strategy involves learning a deformation field to model the temporal changes of a canonical set of 3D Gaussians.
- **p. 1 / Abstract - extractive body cue:** However, these deformation-based methods often produce blurred renderings and lose fine motion details in highly dynamic regions due to the inherent limitations of a single, ...
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we introduce Motion-Aware Partitioning of Deformable 3D Gaussian Splatting (MAPo), a novel framework for high-fidelity dynamic scene reconstruction.
- **p. 1 / Abstract - extractive body cue:** Its core is a dynamic scorebased partitioning strategy that distinguishes between highand low-dynamic 3D Gaussians.
- **p. 2 / 1. Introduction - extractive body cue:** Despite promising results, these methods suffer from two critical limitations inherent in their deformation framework: • Bottleneck in Motion Modeling Capacity: As shown in Fig.
- **p. 1 / 1. Introduction - extractive body cue:** However, the inherent reliance on dense spatial sampling and costly Multilayer Perceptron (MLP) querying leads to significant limitations in both training efficiency and rendering speed.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our key contributions are summarized as follows: • We propose MAPo, a novel framework for high-fidelity dynamic scene reconstruction based on a dynamic scorebased partitioning ...
- **p. 5 / 4.2. Cross-Frame Consistency Loss - extractive body cue:** To ensure temporal smoothness, we introduce the cross-frame consistency loss Lcross, which consists of two components: Lcurrent and Lgt.
- **p. 4 / 4. Method - extractive body cue:** Our approach consists of two main components: a dynamic score-based partitioning strategy and a cross-frame consistency loss.
- **p. 2 / 1. Introduction - extractive body cue:** To tackle these issues, we introduce MAPo, a novel framework for high-fidelity dynamic scene reconstruction.
- **p. 4 / 4. Method - extractive body cue:** The overview of our method is shown in Fig.
- **p. 5 / 4.2. Cross-Frame Consistency Loss - extractive body cue:** Since Lcurrent only enforces self-consistency between adjacent segments without an external reference, continuous optimization can cause them to converge to a consistent but over-smoothed state, ...
- **p. 4 / 4. Method - extractive body cue:** Subsequently, we describe our cross-frame consistency loss, which is designed to address the visual discontinuities caused by partitioning.
- **p. 6 / 4.2. Cross-Frame Consistency Loss - extractive body cue:** We apply Lcross only for training views whose frame indices are within 5 frames of any partition boundary.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We use the harmonic mean to fuse \protect \tilde {r}_ i and \protect \tilde {v}_ i, as it requires both inputs to be high for a high output. | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (4.1.1. Dynamic Score Calculation), p. 5 (4.2. Cross-Frame Consistency Loss) |
| State/latent | harmonic, mean, fuse, protect, tilde, requires, inputs, high, output, Since, Lcurrent, only | geometry, map, object/relationship state | p. 5 (4.1.1. Dynamic Score Calculation), p. 5 (4.2. Cross-Frame Consistency Loss), p. 1 (1. Introduction) |
| Output/action | Since Lcurrent only enforces self-consistency between adjacent segments without an external reference, continuous optimization can cause them to converge to a consistent but over-smoothed state, leading to perceptible blurring in dynami ... | point map, pose, scene graph, affordance 또는 query result | p. 5 (4.2. Cross-Frame Consistency Loss), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | Subsequently, they are excluded from computations involving the deformation network during rendering while their attributes remain optimizable, significantly reducing computational costs. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (4.1.3. Static 3D Gaussian Partitioning), p. 6 (4.2. Cross-Frame Consistency Loss), p. 4 (4. Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our key contributions are summarized as follows: • We propose MAPo, a novel framework for high-fidelity dynamic scene reconstruction based on a dynamic scorebased partitioning ...
- **p. 5 / 4.2. Cross-Frame Consistency Loss - extractive body cue:** To ensure temporal smoothness, we introduce the cross-frame consistency loss Lcross, which consists of two components: Lcurrent and Lgt.
- **p. 4 / 4. Method - extractive body cue:** Our approach consists of two main components: a dynamic score-based partitioning strategy and a cross-frame consistency loss.
- **p. 2 / 1. Introduction - extractive body cue:** To tackle these issues, we introduce MAPo, a novel framework for high-fidelity dynamic scene reconstruction.
- **p. 4 / 4. Method - extractive body cue:** The overview of our method is shown in Fig.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Overview. (a-b) Deformation-based methods often blur details in regions with complex or rapid motion. (c) Our MAPo significantly improves rendering quality in these ...
- **p. 7 / 5.3.1. Quantitative Comparisons - extractive body cue:** 2, our method consistently achieves SOTA rendering quality across both datasets while avoiding prohibitive computational overhead, thus offering a compelling balance between high fidelity and ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 9. Ablation study on the Lcross. We visualize how Lcross improves temporal consistency and rendering quality across a par- tition boundary (frames 74-75). The ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 1 (Figure/Table caption), p. 7 (5.3.1. Quantitative Comparisons) |
| Embodiment/environment | We evaluate our method on two real-world dynamic scene datasets: N3DV [15] and Meet Room [14]. | hardware/simulator version and reset protocol | p. 6 (5.1. Dataset and Metrics), p. 6 (5.1. Dataset and Metrics) |
| Dataset/benchmark | 2, our method consistently achieves SOTA rendering quality across both datasets while avoiding prohibitive computational overhead, thus offering a compelling balance between high fidelity and practical resource usage. | role, split, size and leakage | p. 6 (5.1. Dataset and Metrics), p. 6 (5.1. Dataset and Metrics), p. 7 (5.3.1. Quantitative Comparisons) |
| Metric | Figure 3. An overview of MAPo. (a) 3DGs' deformation process. (b) Compute the dynamic score of 3DGs from history positions during training. (c) High-dynamic 3DGs are recursively temporally partitioned, and low-dynamic ones ... | definition, denominator, direction and uncertainty | p. 4 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (Figure/Table caption) |
| Baseline/ablation | In addition to these SOTA baselines, we additionally introduce a simple segmentation baseline, E-D3DGS (seg), for comparison to highlight the advantages of our approach. | fair input/data/compute/action matching | p. 7 (5.3.1. Quantitative Comparisons), p. 7 (5.3.2. Qualitative Comparisons), p. 6 (5.1. Dataset and Metrics) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 5.3.2. Qualitative Comparisons - extractive body cue:** The comparison highlights that baseline methods often produce degraded results in areas with complex or rapid motion.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Despite promising results, these methods suffer from two critical limitations inherent in their deformation framework: • Bottleneck in Motion Modeling Capacity: As shown in Fig.를 문제로 두고, Our key contributions are summarized as follows: • We propose MAPo, a novel framework for high-fidelity dynamic scene reconstruction based on a dynamic scorebased partitioning strategy.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (4.2. Cross-Frame Consistency Loss), p. 4 (4. Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
