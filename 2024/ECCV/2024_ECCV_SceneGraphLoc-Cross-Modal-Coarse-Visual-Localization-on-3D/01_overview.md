# SceneGraphLoc: Cross-Modal Coarse Visual Localization on 3D Scene Graphs

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1255_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01255.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, Graph Reasoning
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1255_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01255.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 The challenge with current state-of-the-art image-based coarse localization methods, such as AnyLoc [55], is their dependency on extensive image databases, which are not only storage-heavy but also slow to query, despite optimizations ...를 문제로 두고, This method enables the creation of small, efficient databases and significantly accelerates the coarse localization process.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** Coarse visual localization, or place recognition, is a fundamental component in computer vision and robotics applications, defined as the task of identifying the approximate location ...
- **p. 2 / 1 Introduction - extractive body cue:** The training phase is represented by orange arrows, while blue arrows denote the inference phase.
- **p. 2 / 1 Introduction - extractive body cue:** During training, a query image and its associated 3D scene graph form a positive sample within a contrastive learning framework, where negative samples are generated ...
- **p. 2 / 1 Introduction - extractive body cue:** The objective is to learn the embeddings of both the graph and the image so that embeddings of the positive pair are drawn closer, whereas ...
- **p. 2 / 1 Introduction - extractive body cue:** In the inference phase, the task involves assigning the correct scene graph to a given query image from a selection of multiple graphs, achieved by ...
- **p. 2 / 1 Introduction - extractive body cue:** The challenge with current state-of-the-art image-based coarse localization methods, such as AnyLoc [55], is their dependency on extensive image databases, which are not only storage-heavy ...
- **p. 2 / 1 Introduction - extractive body cue:** This paper addresses the novel challenge of localizing a query image within a database that is represented not by conventional images but by the 3D ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** This method enables the creation of small, efficient databases and significantly accelerates the coarse localization process.
- **p. 3 / 1 Introduction - extractive body cue:** The primary contributions of this paper are as follows: 1.
- **p. 1 / Body text (section not recovered) - extractive body cue:** We introduce the task of localizing an input image within a multi-modal reference map represented by a collection of 3D scene graphs.
- **p. 2 / 1 Introduction - extractive body cue:** This paper addresses the novel challenge of localizing a query image within a database that is represented not by conventional images but by the 3D ...
- **p. 3 / 1 Introduction - extractive body cue:** Introducing a novel problem: cross-modal localization of a query image within 3D scene graphs incorporating a mixture of modalities.
- **p. 2 / 1 Introduction - extractive body cue:** The training phase is represented by orange arrows, while blue arrows denote the inference phase.
- **p. 2 / 1 Introduction - extractive body cue:** The challenge with current state-of-the-art image-based coarse localization methods, such as AnyLoc [55], is their dependency on extensive image databases, which are not only storage-heavy ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** This strategy significantly outperforms other cross-modal methods, even without incorporating images into the map representation.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We introduce the task of localizing an input image within a multi-modal reference map represented by a collection of 3D scene graphs. | camera/depth stream, pose, map와 language goal | p. 1 (Body text (section not recovered)), p. 1 (Body text (section not recovered)) |
| State/latent | introduce, task, localizing, input, image, within, multi-modal, reference, represented, collection, scene, graphs | robot pose, free-space/semantic map와 local goal | p. 1 (Body text (section not recovered)), p. 1 (Body text (section not recovered)), p. 3 (1 Introduction) |
| Output/action | Given these modalities, the proposed method SceneGraphLoc learns a fixed-sized embedding for each node (i.e., representing object instances) in the scene graph, enabling effective matching with the objects visible in the input ... | collision-free trajectory 또는 velocity command | p. 1 (Body text (section not recovered)), p. 3 (1 Introduction), p. 2 (1 Introduction) |
| Objective/outcome | The objective is to learn the embeddings of both the graph and the image so that embeddings of the positive pair are drawn closer, whereas those of the negative pair are pushed ... | goal reach, safety, localization error와 replanning latency | p. 2 (1 Introduction), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** This method enables the creation of small, efficient databases and significantly accelerates the coarse localization process.
- **p. 3 / 1 Introduction - extractive body cue:** The primary contributions of this paper are as follows: 1.
- **p. 1 / Body text (section not recovered) - extractive body cue:** We introduce the task of localizing an input image within a multi-modal reference map represented by a collection of 3D scene graphs.
- **p. 2 / 1 Introduction - extractive body cue:** This paper addresses the novel challenge of localizing a query image within a database that is represented not by conventional images but by the 3D ...
- **p. 3 / 1 Introduction - extractive body cue:** Introducing a novel problem: cross-modal localization of a query image within 3D scene graphs incorporating a mixture of modalities.
- **p. 12 / 4 Experiments - extractive body cue:** SceneGraphLoc, even when excluding the image modality (I), outperforms other cross-modal strategies significantly.
- **p. 13 / 4 Experiments - extractive body cue:** LidarCLIP shows a small improvement in accuracy.
- **p. 12 / 4 Experiments - extractive body cue:** Incorporating images significantly enhances its performance, positioning it close to that of image-based approaches but with three orders of magnitude smaller storage requirements.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 12 (4 Experiments), p. 13 (4 Experiments) |
| Embodiment/environment | The 3RScan dataset [123] comprises 1335 annotated indoor scenes, representing 432 distinct rooms, with 1178 scenes (385 rooms) allocated for training and 157 (47 rooms) designated for validation. | hardware/simulator version and reset protocol | p. 11 (4 Experiments), p. 12 (4 Experiments) |
| Dataset/benchmark | SceneGraphLoc 13 Table 3: Average time (ms) of obtaining the query image embedding (teq) and of the retrieval from 10, 50, and all scenes from the 3RScan [123] and ScanNet [21] datasets. | role, split, size and leakage | p. 11 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), p. 11 (4 Experiments) |
| Metric | To evaluate the accuracy of a method, we focus on the recall of scene selection. | definition, denominator, direction and uncertainty | p. 11 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments) |
| Baseline/ablation | For comparison with state-of-the-art visual localization methods requiring large image databases, we included CVNet [63] and AnyLoc [55]. | fair input/data/compute/action matching | p. 10 (4 Experiments), p. 10 (4 Experiments), p. 12 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 14 / 5 Conclusion - extractive body cue:** In conclusion, we introduce SceneGraphLoc, a novel method for solving the novel problem of localizing an input image within a 3D scene graph-based multi-modal reference ...
- **p. 14 / 5 Conclusion - extractive body cue:** This approach outperforms existing cross-modal methods by a large margin.
- **p. 14 / 5 Conclusion - extractive body cue:** It achieves comparable accuracy to state-of-the-art image-based techniques with significantly lower storage requirements and faster processing speeds.

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 The challenge with current state-of-the-art image-based coarse localization methods, such as AnyLoc [55], is their dependency on extensive image databases, which are not only storage-heavy but also slow to query, despite optimizations ...를 문제로 두고, This method enables the creation of small, efficient databases and significantly accelerates the coarse localization process.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 1 (Body text (section not recovered)), p. 1 (Body text (section not recovered)) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
