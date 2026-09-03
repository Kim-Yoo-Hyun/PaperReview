# Where2Act: From Pixels to Actions for Articulated 3D Objects

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2101.02692.
> PDF retrieval source: https://arxiv.org/pdf/2101.02692. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: Robotics, 3D Vision, affordance, articulated objects, active perception, point cloud
- Official paper: https://arxiv.org/abs/2101.02692
- Full-text retrieval: https://arxiv.org/pdf/2101.02692
- Code/Project: https://cs.stanford.edu/~kaichun/where2act/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 We therefore limit our work to considering the plausible short-term interactions that an agent can perform given the current state of the object.를 문제로 두고, In summary, our contributions are: • we formulate the task of inferring affordances for manipulating 3D articulated objects by predicting per-pixel action likelihoods and proposals; • we propose an approach that can ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** One of the fundamental goals of visual perception is to allow agents to meaningfully interact with their environment.
- **p. 1 / Abstract - extractive body cue:** In this paper, we take a step towards that long-term goal - we extract highly localized actionable information related to elementary actions such as pushing ...
- **p. 1 / Abstract - extractive body cue:** For example, given a drawer, our network predicts that applying a pulling force on the handle opens the drawer.
- **p. 1 / Abstract - extractive body cue:** We propose, discuss, and evaluate novel network architectures that given image and depth data, predict the set of actions possible at each pixel, and the ...
- **p. 1 / Abstract - extractive body cue:** We propose a learning-from-interaction framework with an online data sampling strategy that allows us to train the network in simulation (SAPIEN) and generalizes across categories.
- **p. 2 / 1. Introduction - extractive body cue:** We therefore limit our work to considering the plausible short-term interactions that an agent can perform given the current state of the object.
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are: • we formulate the task of inferring affordances for manipulating 3D articulated objects by predicting per-pixel action likelihoods and proposals; ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are: • we formulate the task of inferring affordances for manipulating 3D articulated objects by predicting per-pixel action likelihoods and proposals; ...
- **p. 2 / 1. Introduction - extractive body cue:** We empirically show that our method successfully learns to predict possible actions for novel objects, and does so even for previously unseen categories.
- **p. 3 / 4. Method - extractive body cue:** We propose a learning-from-interaction approach to tackle this task.
- **p. 3 / 4.1. Network Modules - extractive body cue:** To decode the per-pixel actionable information, we propose three decoding heads: (c) an actionability scoring module Da that predicts a score ap ∈[0,1]; (d) an ...
- **p. 4 / 4.2. Collecting Training Data - extractive body cue:** Instead, we propose to let the agent learn by interacting with objects in simulation.
- **p. 3 / 4.1. Network Modules - extractive body cue:** For the 3D experiments, we use PointNet++ segmentation network [34] and implementation [47] with 4 set abstraction layers with single-scale grouping for the encoder and ...
- **p. 4 / 4.3. Training and Losses - extractive body cue:** We empirically find it beneficial to first train the action scoring module Ds and then train the three decoders jointly.
- **p. 4 / 4.2. Collecting Training Data - extractive body cue:** We employ a hybrid data sampling strategy where we first sample large amount of offline random interaction trajectories to bootstrap the learning and then adaptively ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Taking as input a single RGB image or a partial 3D point cloud, we employ an encoder-decoder backbone to extract per-pixel features and design three decoding branches to predict the 'actionable information'. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (4. Method), p. 1 (1. Introduction) |
| State/latent | Taking, input, single, RGB, image, partial, point, cloud, employ, encoder-decoder, backbone, extract | geometry, map, object/relationship state | p. 3 (4. Method), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | Given as input an articulated 3D object, we learn to propose the actionable information for different robotic manipulation primitives (e.g. pushing, pulling): (a) the predicted actionability scores over pixels; (b) the proposed ... | point map, pose, scene graph, affordance 또는 query result | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (4.1. Network Modules) |
| Objective/outcome | After adjusting the relative loss scales to the same level, we obtain the final objective function L = Ls +Lr +100×La. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (4.3. Training and Losses), p. 5 (4.3. Training and Losses), p. 4 (4.1. Network Modules) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are: • we formulate the task of inferring affordances for manipulating 3D articulated objects by predicting per-pixel action likelihoods and proposals; ...
- **p. 2 / 1. Introduction - extractive body cue:** We empirically show that our method successfully learns to predict possible actions for novel objects, and does so even for previously unseen categories.
- **p. 3 / 4. Method - extractive body cue:** We propose a learning-from-interaction approach to tackle this task.
- **p. 3 / 4.1. Network Modules - extractive body cue:** To decode the per-pixel actionable information, we propose three decoding heads: (c) an actionability scoring module Da that predicts a score ap ∈[0,1]; (d) an ...
- **p. 4 / 4.2. Collecting Training Data - extractive body cue:** Instead, we propose to let the agent learn by interacting with objects in simulation.
- **p. 7 / 5.2. Metrics and Baselines - extractive body cue:** We observe that 3D-ours achieves the best performance. validates that our network learns geometric features more than local normals and curvatures.
- **p. 7 / 5.2. Metrics and Baselines - extractive body cue:** An ablated version Ours w/o OS further proves the improvement provided by the proposed online adaptive data sampling (OS) strategy.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. The Proposed Where2Act Task. Given as input an ar- ticulated 3D object, we learn to propose the actionable information for different robotic manipulation ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (5.2. Metrics and Baselines), p. 7 (5.2. Metrics and Baselines) |
| Embodiment/environment | Equipped with a large-scale PartNetMobility dataset, SAPIEN [49] provides a physics-rich simulation environment that supports robot actuators interacting with 2,346 3D CAD models from 46 object categories. | hardware/simulator version and reset protocol | p. 5 (5.1. Framework and Settings), p. 5 (5.1. Framework and Settings) |
| Dataset/benchmark | We visualize our action scoring predictions given certain gripper orientations over three real-world 3D scans from the Replica dataset [42] and Google Scanned Objects [38, 35], as well as on two 2D ... | role, split, size and leakage | p. 5 (5.1. Framework and Settings), p. 5 (5.1. Framework and Settings), p. 8 (5.4. Real-world Data), p. 6 (5.1. Framework and Settings) |
| Metric | Figure 1. The Proposed Where2Act Task. Given as input an ar- ticulated 3D object, we learn to propose the actionable information for different robotic manipulation primitives (e.g. pushing, pulling): (a) the predicted ... | definition, denominator, direction and uncertainty | p. 1 (Figure/Table caption), p. 6 (5.2. Metrics and Baselines), p. 8 (5.3. Results and Analysis) |
| Baseline/ablation | We propose two quantitative metrics for evaluating performance of our proposed method, compared with three baseline methods and one ablated version of our method. | fair input/data/compute/action matching | p. 6 (5.2. Metrics and Baselines), p. 6 (5.2. Metrics and Baselines), p. 5 (5.1. Framework and Settings) |

## Explicit Limitations and Failure Boundary

- **p. 12 / Figure/Table caption - extractive body cue:** Figure 7. Failure Cases. We visualize some interesting failure cases, which demonstrate the difficulty of the task and some am- biguous cases that are hard ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. We visualize (a) the actionability scoring and (b) the action proposal predictions on an example cabinet with a door that can be slipped ...
- **p. 8 / 6. Conclusion - extractive body cue:** Finally, our method does not explicitly model the part segmentation and part motion axis, which may be incorporated in the future works to further improve ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. The Proposed Where2Act Task. Given as input an ar- ticulated 3D object, we learn to propose the actionable information for different robotic manipulation ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Network Architecture. Our network takes an 2D image or a 3D partial scan as input and extract per-pixel feature fp using (a) Unet ...
- **p. 6 / 5.2. Metrics and Baselines - extractive body cue:** With random interactions, there are many more failed interaction trials than the successful ones.
- **p. 6 / 5.1. Framework and Settings - extractive body cue:** Notice that the pulling actions may degrade to the pushing ones if the gripper grasps nothing but just touches/scratches the surface.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 We therefore limit our work to considering the plausible short-term interactions that an agent can perform given the current state of the object.를 문제로 두고, In summary, our contributions are: • we formulate the task of inferring affordances for manipulating 3D articulated objects by predicting per-pixel action likelihoods and proposals; • we propose an approach that can ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Problem Statement), p. 3 (4.1. Network Modules), p. 3 (4.1. Network Modules), p. 4 (4.3. Training and Losses) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** We formulate a new challenging problem Where2Act - inferring per-pixel ‘actionable information' for manipulating 3D articulated objects. (p. 3, 3. Problem Statement).
- **Actual contribution:** In summary, our contributions are: • we formulate the task of inferring affordances for manipulating 3D articulated objects by predicting per-pixel action likelihoods and proposals; • we propose an approach ... (p. 2, 1. Introduction).
- **Evaluation boundary:** Figure 4. We visualize the per-pixel action scoring predictions over the articulated parts given certain gripper orientations for interaction. In each set of results, the left two shapes shown in ... (p. 7, Figure/Table caption).
- **Explicit failure boundary:** With random interactions, there are many more failed interaction trials than the successful ones. (p. 6, 5.2. Metrics and Baselines).
