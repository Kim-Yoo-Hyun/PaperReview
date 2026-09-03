# Egocentric Action-aware Inertial Localization in Point Clouds with Vision-Language Guidance

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_Egocentric_Action-aware_Inertial_Localization_in_Point_Clouds_with_Vision-Language_Guidance_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Egocentric_Action-aware_Inertial_Localization_in_Point_Clouds_with_Vision-Language_Guidance_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_Egocentric_Action-aware_Inertial_Localization_in_Point_Clouds_with_Vision-Language_Guidance_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Egocentric_Action-aware_Inertial_Localization_in_Point_Clouds_with_Vision-Language_Guidance_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The other challenge lies in the complexity of human actions.를 문제로 두고, In summary, our main contributions are as follows: • We introduce EAIL, a novel inertial localization framework that leverages egocentric action cues from headmounted IMU signals to localize target individuals within a ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** This paper presents a novel inertial localization framework named Egocentric Action-aware Inertial Localization (EAIL), which leverages egocentric action cues from headmounted IMU signals to localize ...
- **p. 1 / Abstract - extractive body cue:** Human inertial localization is challenging due to IMU sensor noise that causes trajectory drift over time.
- **p. 1 / Abstract - extractive body cue:** The diversity of human actions further complicates IMU signal processing by introducing various motion patterns.
- **p. 1 / Abstract - extractive body cue:** Nevertheless, we observe that some actions captured by the head-mounted IMU correlate with spatial environmental structures (e.g., bending down to look inside an oven, washing ...
- **p. 1 / Abstract - extractive body cue:** The proposed EAIL framework learns such correlations via hierarchical multi-modal alignment with vision-language guidance.
- **p. 1 / 1. Introduction - extractive body cue:** The other challenge lies in the complexity of human actions.
- **p. 2 / 1. Introduction - extractive body cue:** motion signals can complicate IMU signal processing and make inertial localization further difficult.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions are as follows: • We introduce EAIL, a novel inertial localization framework that leverages egocentric action cues from headmounted IMU ...
- **p. 2 / 1. Introduction - extractive body cue:** In this work, we present a novel framework named Egocentric Action-aware Inertial Localization (EAIL; see also Fig.
- **p. 1 / 1. Introduction - extractive body cue:** Compared to vision-based localization methods [28, 39], inertial localization enables user tracking in an energy-efficient and privacy-preserving manner.
- **p. 3 / 3. Problem Setting - extractive body cue:** In contrast, our approach incorporates the 3D point cloud P, enabling localization without requiring environment-specific training.
- **p. 5 / 4.2.2. Location-aware action recognition - extractive body cue:** We then blend these spatial features with IMU features {FM t }T t=1 through addition.
- **p. 5 / 4.2.2. Location-aware action recognition - extractive body cue:** The training is supervised by a cross-entropy loss: L_{ac t i o n } =

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In summary, our main contributions are as follows: • We introduce EAIL, a novel inertial localization framework that leverages egocentric action cues from headmounted IMU signals to localize target individuals within a ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| State/latent | summary, main, contributions, follows, introduce, EAIL, novel, inertial, localization, framework, leverages, egocentric | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Output/action | Extensive evaluations on the EgoExo4D dataset [18] validate that our framework achieves state-of-the-art performance in both inertial localization and inertial action recognition compared to [24, 41, 66, 69]. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Objective/outcome | The training is supervised by a cross-entropy loss: L_{ac t i o n } = | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (4.2.2. Location-aware action recognition), p. 5 (4.2.2. Location-aware action recognition) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions are as follows: • We introduce EAIL, a novel inertial localization framework that leverages egocentric action cues from headmounted IMU ...
- **p. 2 / 1. Introduction - extractive body cue:** In this work, we present a novel framework named Egocentric Action-aware Inertial Localization (EAIL; see also Fig.
- **p. 1 / 1. Introduction - extractive body cue:** Compared to vision-based localization methods [28, 39], inertial localization enables user tracking in an energy-efficient and privacy-preserving manner.
- **p. 3 / 3. Problem Setting - extractive body cue:** In contrast, our approach incorporates the 3D point cloud P, enabling localization without requiring environment-specific training.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Inertial Localization Results. We evaluate the accuracy using two metrics: the localization success rate (%) at various error distance thresholds and the Relative ...
- **p. 8 / 5.4. Ablation Studies - extractive body cue:** 4, using only IMU signals, we achieve results comparable to IMU2CLIP [41].
- **p. 8 / 5.4. Ablation Studies - extractive body cue:** In contrast, integrating point cloud features with predicted location attention with IMU features provides a clear performance improvement.
- **p. 5 / 5.1. Experimental Setup - extractive body cue:** Evaluation Metrics For the localization task, we report the success rate (%) at error distance thresholds of 0.2 m, 0.4 m, and 0.6 m following ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (Figure/Table caption), p. 8 (5.4. Ablation Studies) |
| Embodiment/environment | These scores are assessed under two setups: "seen rooms" where the localization is performed in the environments present in the training dataset and "unseen rooms" where environments are otherwise new. | hardware/simulator version and reset protocol | p. 5 (5.1. Experimental Setup), p. 5 (5.1. Experimental Setup) |
| Dataset/benchmark | This demonstrates the broad applicability and flexibility of our approach in real-world environments. | role, split, size and leakage | p. 5 (5.1. Experimental Setup), p. 5 (5.1. Experimental Setup), p. 7 (5.4. Ablation Studies), p. 6 (5.2. Inertial Localization Results) |
| Metric | We evaluate the accuracy using two metrics: the localization success rate (%) at various error distance thresholds and the Relative Score (RS) metric for localization likelihood prediction (methods that do not generate ... | definition, denominator, direction and uncertainty | p. 6 (5.2. Inertial Localization Results), p. 5 (5.1. Experimental Setup), p. 5 (5.1. Experimental Setup) |
| Baseline/ablation | Baselines RoNIN [22] learns to predict velocity from IMU signals. | fair input/data/compute/action matching | p. 5 (5.2. Inertial Localization Results), p. 6 (5.2. Inertial Localization Results), p. 6 (5.3. Inertial Action Recognition Results) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 5.4. Ablation Studies - extractive body cue:** Furthermore, even in scenarios where action caption annotations are unavailable in the training set, our method does not fail, ensuring reasonable accuracy without relying on ...
- **p. 8 / 6. Limitations and Future Directions - extractive body cue:** While our method can robustly exploit head-mounted IMU signals for human localization within pre-built point clouds, it does hinge on several factors that present avenues ...
- **p. 8 / 6. Limitations and Future Directions - extractive body cue:** Finally, our experiments are based on IMU data from head-mounted devices, and substantially different sensor placements (e.g., ankle or wrist) may necessitate model adaptations for ...
- **p. 6 / 5.2. Inertial Localization Results - extractive body cue:** Nevertheless, its lack of spatial awareness still leads to reduced accuracy, whereas our approach leverages point cloud structures to deliver robust inertial localization across diverse ...
- **p. 7 / 5.4. Ablation Studies - extractive body cue:** To accomplish this, we leverage the power of robust pre-trained and prealigned vision-language models, such as [43, 50].

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The other challenge lies in the complexity of human actions.를 문제로 두고, In summary, our main contributions are as follows: • We introduce EAIL, a novel inertial localization framework that leverages egocentric action cues from headmounted IMU signals to localize target individuals within a ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (3. Problem Setting), p. 5 (4.2.2. Location-aware action recognition) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
