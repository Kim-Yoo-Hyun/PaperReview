# Open3DSG: Open-Vocabulary 3D Scene Graphs from Point Clouds with Queryable Objects and Open-Set Relationships

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Koch_Open3DSG_Open-Vocabulary_3D_Scene_Graphs_from_Point_Clouds_with_Queryable_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Koch_Open3DSG_Open-Vocabulary_3D_Scene_Graphs_from_Point_Clouds_with_Queryable_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Scene Graph, open-vocabulary, Graph Reasoning
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Koch_Open3DSG_Open-Vocabulary_3D_Scene_Graphs_from_Point_Clouds_with_Queryable_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Koch_Open3DSG_Open-Vocabulary_3D_Scene_Graphs_from_Point_Clouds_with_Queryable_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Open-vocabulary 3D scene understanding methods propose a solution towards these challenges by training a model not on a fixed label set but rather aligning the 3D model with 2D foundation models [14, ...를 문제로 두고, We highlight the following three contributions: • We are the first to present a method to create an interactive graph representation of a scene from a 3D point cloud, which can be ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Current approaches for 3D scene graph prediction rely on labeled datasets to train models for a fixed set of known object classes and relationship categories.
- **p. 1 / Abstract - extractive body cue:** We present Open3DSG, an alternative approach to learn 3D scene graph prediction in an open world without requiring labeled scene graph data.
- **p. 1 / Abstract - extractive body cue:** We co-embed the features from a 3D scene graph prediction backbone with the feature space of powerful open world 2D vision language foundation models.
- **p. 1 / Abstract - extractive body cue:** This enables us to predict 3D scene graphs from 3D point clouds in a zero-shot manner by querying object classes from an open vocabulary and ...
- **p. 1 / Abstract - extractive body cue:** Open3DSG is the first 3D point cloud method to predict not only explicit open-vocabulary object classes, but also open-set relationships that are not limited to ...
- **p. 1 / 1. Introduction - extractive body cue:** Open-vocabulary 3D scene understanding methods propose a solution towards these challenges by training a model not on a fixed label set but rather aligning the ...
- **p. 2 / 1. Introduction - extractive body cue:** This limitation makes it challenging to adopt 2D VLMs for scene graph predictions where compositional relationships are the core part.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** We highlight the following three contributions: • We are the first to present a method to create an interactive graph representation of a scene from ...
- **p. 1 / 1. Introduction - extractive body cue:** We present Open3DSG the first approach for learning to predict open-vocabulary 3D scene graphs from 3D point clouds.
- **p. 1 / 1. Introduction - extractive body cue:** The advantage of our method is that it can be queried and prompted for any instance in the scene, such as the TV and Wall, ...
- **p. 3 / 3. Method - extractive body cue:** An overview of our method is shown in Fig.
- **p. 3 / 3. Method - extractive body cue:** The overall goal of our approach is to distill the knowledge of 2D vision-language models into a 3D graph neural network (GNN) to predict open-vocabulary ...
- **p. 3 / 3. Method - extractive body cue:** We first construct an initial graph representation (Sec.
- **p. 3 / 3. Method - extractive body cue:** These features are then aligned to the ones extracted via the 3D GNN (Sec.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 3.1), and in parallel, we extract vision-language features from aligned 2D images (Sec. | camera/depth stream, pose, map와 language goal | p. 3 (3. Method), p. 3 (3. Method) |
| State/latent | parallel, extract, vision-language, features, aligned, images, Sec, overall, goal, distill, knowledge, models | robot pose, free-space/semantic map와 local goal | p. 3 (3. Method), p. 3 (3. Method), p. 1 (1. Introduction) |
| Output/action | The overall goal of our approach is to distill the knowledge of 2D vision-language models into a 3D graph neural network (GNN) to predict open-vocabulary 3D scene graphs in a 2-step process. | collision-free trajectory 또는 velocity command | p. 3 (3. Method), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Objective/outcome | goal reach, safety, localization error와 replanning latency | goal reach, safety, localization error와 replanning latency | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** We highlight the following three contributions: • We are the first to present a method to create an interactive graph representation of a scene from ...
- **p. 1 / 1. Introduction - extractive body cue:** We present Open3DSG the first approach for learning to predict open-vocabulary 3D scene graphs from 3D point clouds.
- **p. 1 / 1. Introduction - extractive body cue:** The advantage of our method is that it can be queried and prompted for any instance in the scene, such as the TV and Wall, ...
- **p. 3 / 3. Method - extractive body cue:** An overview of our method is shown in Fig.
- **p. 3 / 3. Method - extractive body cue:** The overall goal of our approach is to distill the knowledge of 2D vision-language models into a 3D graph neural network (GNN) to predict open-vocabulary ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We also evaluate the performance of NegCLIP [52] which is supposed to have improved compositional understanding.
- **p. 7 / 4.2. Closed-set 3D scene graph prediction - extractive body cue:** The caption-based approach also achieves considerably lower performances compared to our method.
- **p. 7 / 4.2. Closed-set 3D scene graph prediction - extractive body cue:** However, Open3DSG achieves comparable results to the first supervised 3D scene graph prediction method 3DSSG.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4.1. Experimental Setup), p. 7 (4.2. Closed-set 3D scene graph prediction) |
| Embodiment/environment | However, since 3DSSG is the only dataset to provide ground truth scene graph labels, we evaluate our distilled model quantitatively on it. | hardware/simulator version and reset protocol | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Dataset/benchmark | 1 we compare our new zero-shot openvocabulary 3D scene graph prediction approach with both fully-supervised as well as other zero-shot baselines on the 3DSSG [44] dataset. | role, split, size and leakage | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Closed-set 3D scene graph prediction), p. 7 (4.2. Closed-set 3D scene graph prediction) |
| Metric | We observe that while fully supervised methods demonstrate impressive accuracy on common object and predicate classes, their recall drops drastically for rare tail classes. | definition, denominator, direction and uncertainty | p. 7 (4.2. Closed-set 3D scene graph prediction), p. 8 (4.3. Ablation studies), p. 6 (4.1. Experimental Setup) |
| Baseline/ablation | We outperform all our supervised baselines on object, predicate and relationship prediction. | fair input/data/compute/action matching | p. 7 (4.2. Closed-set 3D scene graph prediction), p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4.5. Limitations - extractive body cue:** While closed-vocabulary evaluations are valuable, they cannot highlight the huge potential of open-vocabulary methods such as ours.
- **p. 8 / 5. Conclusion - extractive body cue:** In future work, we see potential in improving relationship prediction even further to achieve even better and more reliable openvocabulary 3D scene graph predictions that ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** However, since we predict relationships in a generative manner, we cannot provide fixed queries for our relationship prediction.
- **p. 7 / 4.2. Closed-set 3D scene graph prediction - extractive body cue:** We demonstrate that a naive CLIP-based approach is ill-suited for relationship prediction, but also a two-step approach similar to our method by combining OpenSeg [11] ...
- **p. 7 / 4.2. Closed-set 3D scene graph prediction - extractive body cue:** This demonstrates the core advantage of our zero-shot open-vocabulary approach that it performs robustly on a wide variety of objects and predicates.

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Open-vocabulary 3D scene understanding methods propose a solution towards these challenges by training a model not on a fixed label set but rather aligning the 3D model with 2D foundation models [14, ...를 문제로 두고, We highlight the following three contributions: • We are the first to present a method to create an interactive graph representation of a scene from a 3D point cloud, which can be ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method), p. 3 (3. Method), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Closed-set 3D scene graph prediction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
