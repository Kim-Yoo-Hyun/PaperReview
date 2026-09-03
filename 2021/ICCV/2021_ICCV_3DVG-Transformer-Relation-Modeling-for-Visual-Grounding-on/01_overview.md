# 3DVG-Transformer: Relation Modeling for Visual Grounding on Point Clouds

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2021/html/Zhao_3DVG-Transformer_Relation_Modeling_for_Visual_Grounding_on_Point_Clouds_ICCV_2021_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2021/papers/Zhao_3DVG-Transformer_Relation_Modeling_for_Visual_Grounding_on_Point_Clouds_ICCV_2021_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D visual grounding, Graph Reasoning, Transformer
- Official paper: https://openaccess.thecvf.com/content/ICCV2021/html/Zhao_3DVG-Transformer_Relation_Modeling_for_Visual_Grounding_on_Point_Clouds_ICCV_2021_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2021/papers/Zhao_3DVG-Transformer_Relation_Modeling_for_Visual_Grounding_on_Point_Clouds_ICCV_2021_paper.pdf
- Code/Project: https://github.com/zlccccc/3DVG-Transformer
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Moreover, due to the relatively small scales of recent visual grounding datasets, the existing methods also suffer from the overfitting problem, which also prevents these methods from learning a generalizable visual grounding ...를 문제로 두고, 3.1, we present an overview of our method.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Visual grounding on 3D point clouds is an emerging vision and language task that benefits various applications in understanding the 3D visual world.
- **p. 1 / Abstract - extractive body cue:** By formulating this task as a grounding-by-detection problem, lots of recent works focus on how to exploit more powerful detectors and comprehensive language features, but ...
- **p. 1 / Abstract - extractive body cue:** Inspired by the well-known transformer architecture, we propose a relation-aware visual grounding method on 3D point clouds, named as 3DVGTransformer, to fully utilize the contextual ...
- **p. 1 / Abstract - extractive body cue:** We validate that our 3DVG-Transformer outperforms the state-of-the-art methods by a large margin, on two point cloud-based visual grounding datasets, ScanRefer and Nr3D/Sr3D from ReferIt3D, ...
- **p. 1 / 1. Introduction - extractive body cue:** As one emerging 3D visual understanding task, visual grounding on point clouds, also called as referring 3D object localization, aims to locate the desired objects ...
- **p. 1 / 1. Introduction - extractive body cue:** Moreover, due to the relatively small scales of recent visual grounding datasets, the existing methods also suffer from the overfitting problem, which also prevents these ...
- **p. 1 / 1. Introduction - extractive body cue:** [7] proposed to tackle visual grounding on 3D point clouds by formulating it as a grounding-by-detection problem, together with two newly developed datasets (i.e., ScanRefer ...

## Core Idea

- **p. 3 / 3. Methodology - extractive body cue:** 3.1, we present an overview of our method.
- **p. 3 / 3. Methodology - extractive body cue:** 3.4, we introduce the objective function of our method, which also includes a pair of feature augmentation strategies for alleviating overfitting.
- **p. 2 / 1. Introduction - extractive body cue:** The contribution of this work is three-fold: (1) A simple and strong visual grounding framework (referred to as 3DVG-Transformer) specifically designed for point clouds, which ...
- **p. 1 / 1. Introduction - extractive body cue:** To this end, we propose a relation-aware visual grounding method on 3D point clouds, named as 3DVGTransformer.
- **p. 1 / 1. Introduction - extractive body cue:** While our method follows the ground-bydetection strategy from ScanRefer [6], we additionally exploit various relations among proposals at both the object proposal generation stage and ...
- **p. 4 / 3.2. Relation-enhanced Proposal Generation - extractive body cue:** The network structure of our coordinate-guided contextual aggregation module (a), which consists of 2 transformer layers (the multi-level feature fusion module is omitted here).
- **p. 4 / 3.2. Relation-enhanced Proposal Generation - extractive body cue:** The first one is a self-attention block that exploits the relations among the spatial neighbors of the input clusters, which is then followed by an ...
- **p. 5 / 3.3. Cross-modal Proposal Disambiguation - extractive body cue:** After feeding the word features Fword into an independent self-attention module, we propose a multiplex attention module to fuse the word features and the proposal ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The goal of visual grounding on 3D point clouds is to localize the object of interest (i.e., the target object) in each point cloud, and output an axis-aligned bounding box with the ... | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3.1. Overview), p. 3 (3.2. Relation-enhanced Proposal Generation) |
| State/latent | goal, visual, grounding, point, clouds, localize, object, interest, target, cloud, output, axis-aligned | geometry, map, object/relationship state | p. 3 (3.1. Overview), p. 3 (3.2. Relation-enhanced Proposal Generation), p. 1 (1. Introduction) |
| Output/action | However, these intermediate outputs only capture local point cloud features that describe the candidate objects, so they are not aware of the relations with other 2930 | point map, pose, scene graph, affordance 또는 query result | p. 3 (3.2. Relation-enhanced Proposal Generation), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Objective/outcome | 3.4, we introduce the objective function of our method, which also includes a pair of feature augmentation strategies for alleviating overfitting. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (3. Methodology), p. 5 (3.4. Loss Function), p. 5 (3.4. Loss Function) |

## Main Claims and Actual Contribution

- **p. 3 / 3. Methodology - extractive body cue:** 3.1, we present an overview of our method.
- **p. 3 / 3. Methodology - extractive body cue:** 3.4, we introduce the objective function of our method, which also includes a pair of feature augmentation strategies for alleviating overfitting.
- **p. 2 / 1. Introduction - extractive body cue:** The contribution of this work is three-fold: (1) A simple and strong visual grounding framework (referred to as 3DVG-Transformer) specifically designed for point clouds, which ...
- **p. 1 / 1. Introduction - extractive body cue:** To this end, we propose a relation-aware visual grounding method on 3D point clouds, named as 3DVGTransformer.
- **p. 1 / 1. Introduction - extractive body cue:** While our method follows the ground-bydetection strategy from ScanRefer [6], we additionally exploit various relations among proposals at both the object proposal generation stage and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative results from ScanRefer [6] and our 3DVG-Transformer. The GT boxes are marked in blue. If one predicted box has an IoU score ...
- **p. 7 / 4.2. Comparisons with the state-of-the-art methods - extractive body cue:** The proposed 3DVGTransformer achieves the overall accuracy of 40.8% and 51.4% on Nr3D and Sr3D respectively, which outperforms all the baseline methods by a large ...
- **p. 8 / 4.3. Ablation Study and Analysis - extractive body cue:** As shown in Table 4, the best results are achieved by using our default strategy, while the localization accuracies without using the coordinate-guided attention strategy ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 7 (4.2. Comparisons with the state-of-the-art methods) |
| Embodiment/environment | To fully evaluate our method, we compare our method with the baseline methods on both the validation set and the online test set available at the ScanRefer's benchmark website1. - Nr3D and ... | hardware/simulator version and reset protocol | p. 5 (4.1. Datasets and Implementation Details), p. 5 (4.1. Datasets and Implementation Details) |
| Dataset/benchmark | The results of our method under the "2D+3D" setting were also evaluated on the test dataset from the ScanRefer online benchmark under both settings. | role, split, size and leakage | p. 5 (4.1. Datasets and Implementation Details), p. 5 (4.1. Datasets and Implementation Details), p. 7 (4.2. Comparisons with the state-of-the-art methods), p. 6 (4.1. Datasets and Implementation Details) |
| Metric | If one predicted box has an IoU score higher than 0.5, this box is marked in green, otherwise it is marked in red. | definition, denominator, direction and uncertainty | p. 7 (4.2. Comparisons with the state-of-the-art methods), p. 5 (4.1. Datasets and Implementation Details), p. 5 (4.1. Datasets and Implementation Details) |
| Baseline/ablation | In Table 1 and Table 2, our 3DVG-Transformer is compared with several baseline methods on both ScanRefer and Nr3D/Sr3D datasets, which include the 2D-based methods SCRC [1] and One-stage [41], the instance ... | fair input/data/compute/action matching | p. 6 (4.2. Comparisons with the state-of-the-art methods), p. 7 (4.2. Comparisons with the state-of-the-art methods), p. 7 (4.2. Comparisons with the state-of-the-art methods) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.2. Comparisons with the state-of-the-art methods - extractive body cue:** The failure cases of ScanRefer indicate that this baseline method cannot well model complex relations and distinguish ambiguous objects.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. The network structure of our coordinate-guided contex- tual aggregation module (a), which consists of 2 transformer lay- ers (the multi-level feature fusion module ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Moreover, due to the relatively small scales of recent visual grounding datasets, the existing methods also suffer from the overfitting problem, which also prevents these methods from learning a generalizable visual grounding ...를 문제로 두고, 3.1, we present an overview of our method.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 4 (3.2. Relation-enhanced Proposal Generation), p. 4 (3.2. Relation-enhanced Proposal Generation), p. 5 (3.3. Cross-modal Proposal Disambiguation), p. 5 (3.3. Cross-modal Proposal Disambiguation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
