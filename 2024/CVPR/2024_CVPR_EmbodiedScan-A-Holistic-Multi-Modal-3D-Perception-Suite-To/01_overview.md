# EmbodiedScan: A Holistic Multi-Modal 3D Perception Suite Towards Embodied AI

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Wang_EmbodiedScan_A_Holistic_Multi-Modal_3D_Perception_Suite_Towards_Embodied_AI_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Wang_EmbodiedScan_A_Holistic_Multi-Modal_3D_Perception_Suite_Towards_Embodied_AI_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, Embodied AI, Dataset
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Wang_EmbodiedScan_A_Holistic_Multi-Modal_3D_Perception_Suite_Towards_Embodied_AI_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Wang_EmbodiedScan_A_Holistic_Multi-Modal_3D_Perception_Suite_Towards_Embodied_AI_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Regarding data, earlier datasets targeting egocentric RGB-D inputs are either too small [12, 45] or lack comprehensive annotations [6, 51] to support the aforemenThis CVPR paper is the Open Access version, provided ...를 문제로 두고, Building upon this database, we introduce a baseline framework named Embodied Perceptron.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In the realm of computer vision and robotics, embodied agents are expected to explore their environment and carry out human instructions.
- **p. 1 / Abstract - extractive body cue:** This necessitates the ability to fully understand 3D scenes given their first-person observations and contextualize them into language for interaction.
- **p. 1 / Abstract - extractive body cue:** However, traditional research focuses more on scene-level input and output setups from a global view.
- **p. 1 / Abstract - extractive body cue:** To address the gap, we introduce EmbodiedScan, a multi-modal, ego-centric 3D perception dataset and benchmark for holistic 3D scene understanding.
- **p. 1 / Abstract - extractive body cue:** It encompasses over 5k scans encapsulating 1M ego-centric RGB-D views, 1M language prompts, 160k 3D-oriented boxes spanning over 760 categories, some of which partially align ...
- **p. 1 / 1. Introduction - extractive body cue:** Regarding data, earlier datasets targeting egocentric RGB-D inputs are either too small [12, 45] or lack comprehensive annotations [6, 51] to support the aforemenThis CVPR ...
- **p. 1 / 1. Introduction - extractive body cue:** It commences its journey devoid of any prior knowledge about the scene, guided only by an initial instruction.

## Core Idea

- **p. 1 / Abstract - extractive body cue:** Building upon this database, we introduce a baseline framework named Embodied Perceptron.
- **p. 1 / Abstract - extractive body cue:** To address the gap, we introduce EmbodiedScan, a multi-modal, ego-centric 3D perception dataset and benchmark for holistic 3D scene understanding.
- **p. 6 / 4.1. Multi-Modal 3D Encoder - extractive body cue:** Given the multi-level sparse visual features F S k and text features from the text encoder, we use a multi-modal fusion transformer model [20, 61] ...
- **p. 5 / 4.1. Multi-Modal 3D Encoder - extractive body cue:** Next, we first present how we aggregate multi-view inputs and then introduce different fusion approaches for dense and sparse feature extraction.
- **p. 6 / 4.2. Sparse & Dense Decoder - extractive body cue:** We use cross-entropy loss and sceneclass affinity loss [55] for training.
- **p. 1 / Abstract - extractive body cue:** This necessitates the ability to fully understand 3D scenes given their first-person observations and contextualize them into language for interaction.
- **p. 4 / 3.2. Annotation - extractive body cue:** We used the Segment Anything Model (SAM) [22] and a customized annotation tool based on [24] (Fig.
- **p. 5 / 4.1. Multi-Modal 3D Encoder - extractive body cue:** For the sparse case, we use multi-level features as seeds instead of a single dense feature map to predict 3D objects.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given this dataset, we can take multi-modality input, including RGB images, point clouds derived from depth maps as well as language prompts, to extract multi-modal representations and perform different downstream tasks. | standardized observation, action, task state와 evaluation split | p. 4 (4. Embodied Perceptron), p. 1 (1. Introduction) |
| State/latent | Given, dataset, take, multi-modality, input, including, RGB, images, point, clouds, derived, depth | benchmark state/goal와 method decision | p. 4 (4. Embodied Perceptron), p. 1 (1. Introduction), p. 1 (Abstract) |
| Output/action | Most previous studies have primarily revolved around scene-level input and output problems from a global view [13, 34, 40], i.e., taking reconstructed 3D point clouds or meshes as inputs and predicting 3D ... | policy/controller trajectory 또는 measured result | p. 1 (1. Introduction), p. 1 (Abstract), p. 4 (3.1. Data Collection & Processing) |
| Objective/outcome | Training objectives include the original classification loss, centerness loss, and a disentangled Chamfer Distance (CD) loss for eight corners [3, 44]. | success metric, robustness, generalization과 reproducibility | p. 6 (4.2. Sparse & Dense Decoder), p. 6 (4.2. Sparse & Dense Decoder), p. 5 (4. Embodied Perceptron) |

## Main Claims and Actual Contribution

- **p. 1 / Abstract - extractive body cue:** Building upon this database, we introduce a baseline framework named Embodied Perceptron.
- **p. 1 / Abstract - extractive body cue:** To address the gap, we introduce EmbodiedScan, a multi-modal, ego-centric 3D perception dataset and benchmark for holistic 3D scene understanding.
- **p. 7 / 5.1. Fundamental 3D Perception Benchmarks - extractive body cue:** Substituting this with our decoder design markedly improves performance.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. EmbodiedScan annotation and statistics. (a) UI for 3D box annotation. We select keyframes and generate their SAM masks with corresponding axis-aligned boxes. With ...
- **p. 7 / 5.1. Fundamental 3D Perception Benchmarks - extractive body cue:** Nevertheless, all models have substantial potential for improvement, demonstrating the challenges of this new dataset and setup.
- **p. 8 / 5.2. Language-Grounded Benchmark - extractive body cue:** Our baseline outperforms all due to the strong multi-modal encoder.
- **p. 8 / 5.1. Fundamental 3D Perception Benchmarks - extractive body cue:** Similarly, our method outperforms others, providing a solid baseline for future studies.
- **p. 2 / Dataset - extractive body cue:** Detailed analysis further underscores the value of EmbodiedScan and highlights the primary challenges posed by this new setup.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 7 (5.1. Fundamental 3D Perception Benchmarks), p. 3 (Figure/Table caption) |
| Embodiment/environment | To bridge this divide, we introduce a multi-modal, egocentric 3D perception dataset and benchmark for holistic 3D scene understanding, termed EmbodiedScan, aimed at facilitating real-world embodied AI applications (Fig. | hardware/simulator version and reset protocol | p. 2 (Dataset), p. 2 (Dataset) |
| Dataset/benchmark | We remove four categories, {wall, ceiling, floor, object} in our 3D detection benchmark and divide the remaining 284 categories into three splits, {head, common, tail} with {90, 94, 100} classes. | role, split, size and leakage | p. 2 (Dataset), p. 2 (Dataset), p. 4 (3.3. Statistics), p. 6 (5. Benchmark) |
| Metric | For metrics, we use the 3D IoU-based average precision (AP) with thresholds of 0.25 and 0.5 for 3D detection and visual grounding. | definition, denominator, direction and uncertainty | p. 6 (5. Benchmark), p. 7 (5.1. Fundamental 3D Perception Benchmarks), p. 2 (Dataset) |
| Baseline/ablation | Our baseline outperforms all due to the strong multi-modal encoder. | fair input/data/compute/action matching | p. 8 (5.2. Language-Grounded Benchmark), p. 8 (5.1. Fundamental 3D Perception Benchmarks), p. 2 (Dataset) |

## Explicit Limitations and Failure Boundary

- **p. 2 / Dataset - extractive body cue:** On the other hand, since we cannot trivially obtain the reconstruction of a new environment, models trained with scene-level input are not directly applicable in ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Dataset composition. Embodied- Scan is composed of three data sources and has similar scans, images, objects, and cate- gories in each of them. ...
- **p. 4 / 3.2. Annotation - extractive body cue:** 3a) to address limitations in existing 3D box annotations, i.e., lack of orientation and small object annotations.
- **p. 4 / 3.3. Statistics - extractive body cue:** Generated language prompts following SR3D fall into five types of spatial object-to-object relations: Horizontal Proximity, Vertical Proximity, Support, Allocentric, and Between.
- **p. 6 / 5. Benchmark - extractive body cue:** Due to the space limitation, please refer to the appendix for implementation details of different baselines, and more quantitative and qualitative results including an "in-the-wild" ...
- **p. 7 / 5.1. Fundamental 3D Perception Benchmarks - extractive body cue:** Unlike continuous settings, multi-view 3D perception does not predefine the order of views but provides all views to the model for scene-level results.

## Why Read It

Robotics-enabling 3D perception의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Regarding data, earlier datasets targeting egocentric RGB-D inputs are either too small [12, 45] or lack comprehensive annotations [6, 51] to support the aforemenThis CVPR paper is the Open Access version, provided ...를 문제로 두고, Building upon this database, we introduce a baseline framework named Embodied Perceptron.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 6 (4.1. Multi-Modal 3D Encoder), p. 5 (4.1. Multi-Modal 3D Encoder), p. 6 (4.2. Sparse & Dense Decoder), p. 1 (Abstract) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
