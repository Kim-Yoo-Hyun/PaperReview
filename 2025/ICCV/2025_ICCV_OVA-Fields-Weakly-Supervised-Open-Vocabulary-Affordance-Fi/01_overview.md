# OVA-Fields: Weakly Supervised Open-Vocabulary Affordance Fields for Robot Operational Part Detection

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Su_OVA-Fields_Weakly_Supervised_Open-Vocabulary_Affordance_Fields_for_Robot_Operational_Part_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Su_OVA-Fields_Weakly_Supervised_Open-Vocabulary_Affordance_Fields_for_Robot_Operational_Part_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics, semantic
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Su_OVA-Fields_Weakly_Supervised_Open-Vocabulary_Affordance_Fields_for_Robot_Operational_Part_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Su_OVA-Fields_Weakly_Supervised_Open-Vocabulary_Affordance_Fields_for_Robot_Operational_Part_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 The first challenge is that current models mainly predict affordances for single objects [5, 6, 25, 36], relying on isolated 2D images or high-quality 3D point clouds that require precise scanning and ...를 문제로 두고, Here, we introduce our framework, OVA-Fields, which enables accurate affordance detection in 3D scenes based on natural language queries.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In recent years, affordance detection has become essential for robotic manipulation in real-world scenes, where robots must autonomously interpret commands and perform actions.
- **p. 1 / Abstract - extractive body cue:** Current methods often focus on individual point cloud objects or simple semantic queries, limiting their effectiveness in diverse scenes and complex instructions.
- **p. 1 / Abstract - extractive body cue:** To address this, we introduce OVA-Fields, a framework for affordance detection in 3D scenes with complex semantics.
- **p. 1 / Abstract - extractive body cue:** By integrating multilevel geometric encoding and enhanced semantic affordance embeddings, OVA-Fields maps user commands directly to operational parts, embedding enriched affordance information into the 3D ...
- **p. 1 / Abstract - extractive body cue:** Experimental results demonstrate that OVA-Fields achieves 52.4% mIoU on complex semantic real-world scenes and 90% success rate in real-world robot manipulation tasks (e.g., "take out ...
- **p. 1 / 1. Introduction - extractive body cue:** The first challenge is that current models mainly predict affordances for single objects [5, 6, 25, 36], relying on isolated 2D images or high-quality 3D ...
- **p. 2 / 1. Introduction - extractive body cue:** The second challenge is that existing affordance detection models often fail to handle complex user instructions effectively [1, 2, 9, 15, 19, 42, 44], limiting ...

## Core Idea

- **p. 3 / 3. Methods - extractive body cue:** Here, we introduce our framework, OVA-Fields, which enables accurate affordance detection in 3D scenes based on natural language queries.
- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as follows: • We propose OVA-Fields, a novel framework for affordance detection in 3D real-world scenes.
- **p. 1 / 1. Introduction - extractive body cue:** Our framework directly maps the user's open-vocabulary semantic queries to actionable affordance locations in the complex 3D scenes, allowing robots to identify and interact with ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we introduce the OVA-Fields framework, a robot-centric affordance detection framework that operates robustly with sparse and noisy sensor inputs.
- **p. 3 / 3.1. Multi-Modal Affordance Perception - extractive body cue:** 2a), our method first extracts pixel embeddings from each RGB image.
- **p. 3 / 3.2. Spatial Feature Extraction and Feature Fusion - extractive body cue:** Through a series of processing steps, the OVA-Fields then produces a high-dimensional feature representation for each coordinate point, which incorporates both rich visual information and ...
- **p. 4 / 3.2. Spatial Feature Extraction and Feature Fusion - extractive body cue:** First, the Multi-modal Affordance Perception (MAP) module extracts visual and affordance features (Sec.
- **p. 4 / 3.2. Spatial Feature Extraction and Feature Fusion - extractive body cue:** These spatial and affordance embeddings are then combined through element-wise addition into a feature fc, which is processed by a multi-head attention mechanism.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In the OVA-Fields, our approach uses a sequence of RGB-D images, along with pose data and camera intrinsics, as input to build a point cloud and generate global coordinates. | image/video, language instruction, proprioception과 history | p. 3 (3.2. Spatial Feature Extraction and Feature Fusion), p. 2 (1. Introduction) |
| State/latent | OVA-Fields, uses, sequence, RGB-D, images, along, pose, data, camera, intrinsics, input, build | language-grounded task state와 action-policy context | p. 3 (3.2. Spatial Feature Extraction and Feature Fusion), p. 2 (1. Introduction), p. 4 (3.2. Spatial Feature Extraction and Feature Fusion) |
| Output/action | This module detects key parts like handles with low computational cost, supporting robust and scalable real robot manipulation. • We enable seamless integration between semantic commands and affordance locations, translating user input ... | continuous action, pose 또는 action chunk | p. 2 (1. Introduction), p. 4 (3.2. Spatial Feature Extraction and Feature Fusion), p. 5 (3.3. Query Mapping) |
| Objective/outcome | This loss maximizes the similarity between the correct affordance and point features while minimizing it for incorrect affordances. | instruction following, task success, generalization과 latency | p. 4 (3.2. Spatial Feature Extraction and Feature Fusion), p. 5 (3.2. Spatial Feature Extraction and Feature Fusion), p. 3 (3.1. Multi-Modal Affordance Perception) |

## Main Claims and Actual Contribution

- **p. 3 / 3. Methods - extractive body cue:** Here, we introduce our framework, OVA-Fields, which enables accurate affordance detection in 3D scenes based on natural language queries.
- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as follows: • We propose OVA-Fields, a novel framework for affordance detection in 3D real-world scenes.
- **p. 1 / 1. Introduction - extractive body cue:** Our framework directly maps the user's open-vocabulary semantic queries to actionable affordance locations in the complex 3D scenes, allowing robots to identify and interact with ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we introduce the OVA-Fields framework, a robot-centric affordance detection framework that operates robustly with sparse and noisy sensor inputs.
- **p. 3 / 3.1. Multi-Modal Affordance Perception - extractive body cue:** 2a), our method first extracts pixel embeddings from each RGB image.
- **p. 8 / 5. Real Robot Experiments - extractive body cue:** The case of "grab the cup" reveals that although affordance detection reaches 90% spatial accuracy, the current pipeline achieves a 20% success rate for containers ...
- **p. 6 / 4.3. Ablation Study - extractive body cue:** The performance gap demonstrates that the hierarchical integration of semantic and visual features significantly improves affordance detection robustness in real-world environments.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Performance comparison of various models on the Affordance detection task for different objects. From these two indicators, the OVA-Fields consistently outperforms the baselines, ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (5. Real Robot Experiments), p. 6 (4.3. Ablation Study) |
| Embodiment/environment | Our experimental dataset comprises multi-source RGB-D sequences captured using consumer-grade devices (Apple iPad Pro with LiDAR) and benchmark datasets to systematically evaluate cross-environment generalization. | hardware/simulator version and reset protocol | p. 5 (4.1. Experiment Settings), p. 5 (4.1. Experiment Settings) |
| Dataset/benchmark | This shows that the SR module is crucial for improving affordance detection accuracy for detecting smaller items, probably making it better suited for real-world robotic tasks. | role, split, size and leakage | p. 5 (4.1. Experiment Settings), p. 5 (4.1. Experiment Settings), p. 6 (4.3. Ablation Study), p. 7 (4.3. Ablation Study) |
| Metric | All variants share identical training protocols on the Lab and Home dataset and are evaluated on two metrics: mIoU and instruction grounding accuracy (the success rate of locating referent parts in manipulation ... | definition, denominator, direction and uncertainty | p. 7 (4.3. Ablation Study), p. 8 (5. Real Robot Experiments), p. 8 (5. Real Robot Experiments) |
| Baseline/ablation | In the context of fine-grained affordance detection, our model consistently outperforms baseline approaches. | fair input/data/compute/action matching | p. 5 (4.2. Numerical and Visual Comparisons), p. 6 (4.2. Numerical and Visual Comparisons), p. 8 (5. Real Robot Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusion - extractive body cue:** The key limitations emerge in handling articulated objects (e.g., doors/drawers).
- **p. 8 / 6. Conclusion - extractive body cue:** Although grasp positions are reliably detected, the current implementation cannot infer required force application directions or kinematic movement patterns essential for operating hinge-based mechanisms.
- **p. 5 / 4.2. Numerical and Visual Comparisons - extractive body cue:** This approach demonstrates particular strength in multimodal feature fusion, as 89.3% of failure cases in singlemodality baselines result from either geometric oversimplification or semantic ambiguity.
- **p. 6 / 4.3. Ablation Study - extractive body cue:** Our dynamic weighting shows that static blending fails to handle feature conflicts in open-vocabulary settings.
- **p. 5 / 4.2. Numerical and Visual Comparisons - extractive body cue:** The method maintains robustness under ScanNet's realworld noise conditions, achieving 27.6% precision at 13.2% mIoU compared to CLIP-FO3D's 21.2% precision with 15.3% mIoU.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Method Overview. OVA-Fields integrates feature fusion and training in three key steps. First, the Multi-modal Affordance Perception (MAP) module extracts visual and affordance ...
- **p. 6 / 4.3. Ablation Study - extractive body cue:** The performance gap demonstrates that the hierarchical integration of semantic and visual features significantly improves affordance detection robustness in real-world environments.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 The first challenge is that current models mainly predict affordances for single objects [5, 6, 25, 36], relying on isolated 2D images or high-quality 3D point clouds that require precise scanning and ...를 문제로 두고, Here, we introduce our framework, OVA-Fields, which enables accurate affordance detection in 3D scenes based on natural language queries.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.2. Spatial Feature Extraction and Feature Fusion), p. 4 (3.2. Spatial Feature Extraction and Feature Fusion) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
