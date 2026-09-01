# Where2Explore: Few-shot Affordance Learning for Unseen Novel Categories of Articulated Objects

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2309.07473.
> PDF retrieval source: https://arxiv.org/pdf/2309.07473. Reading tracker status/evidence was not changed.

- Year/Venue: 2023 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: Robotics, 3D Vision, active exploration, affordance, articulated objects, few-shot learning
- Official paper: https://arxiv.org/abs/2309.07473
- Full-text retrieval: https://arxiv.org/pdf/2309.07473
- Code/Project: https://sites.google.com/view/where2explore/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This limitation hinders the efficiency and safety of real-world applications of robots.를 문제로 두고, The results demonstrate our framework's capability to efficiently explore novel categories by exploiting geometric similarity.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Articulated object manipulation is a fundamental yet challenging task in robotics.
- **p. 1 / Abstract - extractive body cue:** Due to significant geometric and semantic variations across object categories, previous manipulation models struggle to generalize to novel categories.
- **p. 1 / Abstract - extractive body cue:** Few-shot learning is a promising solution for alleviating this issue by allowing robots to perform a few interactions with unseen objects.
- **p. 1 / Abstract - extractive body cue:** However, extant approaches often necessitate costly and inefficient test-time interactions with each unseen instance.
- **p. 1 / Abstract - extractive body cue:** Recognizing this limitation, we observe that despite their distinct shapes, different categories often share similar local geometries essential for manipulation, such as pullable handles and ...
- **p. 1 / 1 Introduction - extractive body cue:** This limitation hinders the efficiency and safety of real-world applications of robots.
- **p. 1 / 1 Introduction - extractive body cue:** However, due to the significant variance in the objects' structure, 3D geometry, and articulation types across categories, developing efficient perception and manipulation systems that can ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** The results demonstrate our framework's capability to efficiently explore novel categories by exploiting geometric similarity.
- **p. 2 / 1 Introduction - extractive body cue:** We evaluate our framework by training our model on constrained object categories and applying few-shot learning to novel categories with limited shapes.
- **p. 5 / 4 Method - extractive body cue:** As shown in the right part of figure 2, when faced with a novel category, our framework will first predict the similarity of the objects.
- **p. 3 / 4 Method - extractive body cue:** Next, we introduce the ‘similarity module' to form a representation that connects the geometries in the supporting set with geometries across category boundaries.
- **p. 3 / 4 Method - extractive body cue:** As shown in Figure 2, we propose the ‘Where2Explore' framework to explicitly leverage the similar semantics on local geometries shared across different categories for cross-category ...
- **p. 6 / 4 Method - extractive body cue:** 4.4 Network Architecture and Training Strategy Our network consists of two modules - the affordance module and the similarity module.
- **p. 6 / 4 Method - extractive body cue:** We use a PointNet++ segmentation network [29] encoder for extracting features from 3D partial point clouds.
- **p. 4 / 4 Method - extractive body cue:** To achieve the first property, as shown in the middle of Figure 3, we propose a ‘similarity module' to predict the semantic similarity.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The similarity module is designed to take a partial point cloud of an object Oi ∈R3×N, a set of action directions and gripper orientations {Ri} on each point, and is required to ... | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (4 Method), p. 4 (4 Method) |
| State/latent | similarity, module, designed, take, partial, point, cloud, object, action, directions, gripper, orientations | geometry, map, object/relationship state | p. 4 (4 Method), p. 4 (4 Method), p. 5 (4 Method) |
| Output/action | Given a specific action Ri on a point pi of a partial point cloud Oi, the affordance module is required to predict whether the given action will result in a part motion. | point map, pose, scene graph, affordance 또는 query result | p. 4 (4 Method), p. 5 (4 Method), p. 5 (4 Method) |
| Objective/outcome | To train the similarity module, we use an L1 loss to measure the distance between Similarity prediction and the ground truth accuracy. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (4 Method), p. 6 (4 Method), p. 5 (4 Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** The results demonstrate our framework's capability to efficiently explore novel categories by exploiting geometric similarity.
- **p. 2 / 1 Introduction - extractive body cue:** We evaluate our framework by training our model on constrained object categories and applying few-shot learning to novel categories with limited shapes.
- **p. 5 / 4 Method - extractive body cue:** As shown in the right part of figure 2, when faced with a novel category, our framework will first predict the similarity of the objects.
- **p. 3 / 4 Method - extractive body cue:** Next, we introduce the ‘similarity module' to form a representation that connects the geometries in the supporting set with geometries across category boundaries.
- **p. 3 / 4 Method - extractive body cue:** As shown in Figure 2, we propose the ‘Where2Explore' framework to explicitly leverage the similar semantics on local geometries shared across different categories for cross-category ...
- **p. 7 / 5 Experiments - extractive body cue:** For both the F-score and sample success rate, we use the average score of the four different training category combinations.
- **p. 8 / 5 Experiments - extractive body cue:** Our framework also achieves comparable performance compared with Full-data, which is trained on all categories with abundant data.
- **p. 7 / 5 Experiments - extractive body cue:** We calculate the sample success rate by randomly selecting one action predicted as successful by the affordance module, performing the interaction, and observing the result.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (5 Experiments), p. 8 (5 Experiments) |
| Embodiment/environment | Similarity-guided Exploration 1 Part motion Franka Emika Panda Robot Similarity prediction Azure Kinect DK 2 No part motion 3 Fail to grasp Manipulation After Exploration Similarity prediction Adapted affordance Pulling Part motion ... | hardware/simulator version and reset protocol | p. 9 (5 Experiments), p. 7 (5 Experiments) |
| Dataset/benchmark | We also perform few-shot learning on each novel category separately to match the real-world scenario. | role, split, size and leakage | p. 9 (5 Experiments), p. 7 (5 Experiments), p. 6 (5 Experiments), p. 6 (5 Experiments) |
| Metric | For both the F-score and sample success rate, we use the average score of the four different training category combinations. | definition, denominator, direction and uncertainty | p. 7 (5 Experiments), p. 7 (5 Experiments), p. 8 (Figure/Table caption) |
| Baseline/ablation | Table 3: Ablations on the exploration strategy using different interaction budget (1, 2, 5). We also conduct few-shot affordance learning on representative categories separately to match the real-world scenario. Table 2 presents ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (5 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5 Experiments - extractive body cue:** Compared with AdaAfford, which fails to generalize to novel categories, our framework could still propose reasonable exploration strategies on novel categories leveraging local similarity.
- **p. 9 / 5 Experiments - extractive body cue:** Although Affordance fails to directly generalize to novel categories (Left) via interacting on low-similarity areas (Middle), our framework could learn the semantic information on them ...
- **p. 9 / 5 Experiments - extractive body cue:** While affordance fails to directly generalize to novel objects (Left), the similarity module can still discover areas that contain uncertain yet important semantic information to ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 4: Few-shot learning on novel categories using different interaction budget (1, 2, 5). B More Experimental Results and Analysis We visualize more similarity-guided exploration ...
- **p. 7 / 5 Experiments - extractive body cue:** Compared to the AdaAfford, our results suggest that instance-level exploration strategies which focus on dynamic information for a single object fail to generalize well across ...
- **p. 8 / 5 Experiments - extractive body cue:** Compared with other exploration strategies Explore-random and Explore-noSim that fail to discover important local areas, our strategy is dramatically more effective and efficient.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This limitation hinders the efficiency and safety of real-world applications of robots.를 문제로 두고, The results demonstrate our framework's capability to efficiently explore novel categories by exploiting geometric similarity.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 6 (4 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
