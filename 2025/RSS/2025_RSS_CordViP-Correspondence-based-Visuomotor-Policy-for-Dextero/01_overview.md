# CordViP: Correspondence-based Visuomotor Policy for Dexterous Manipulation in Real-World

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p110.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p110.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, 3D perception, dexterous manipulation, correspondence, contact maps, bimanual
- Official paper: https://www.roboticsproceedings.org/rss21/p110.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p110.pdf
- Code/Project: https://aureleopku.github.io/CordViP
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (17 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 As a result, CordViP not only effectively addresses occlusion challenges during dexterous manipulation but also significantly improves the model's ability to comprehend spatial interactions and collaborative dynamics.를 문제로 두고, To this end, we propose the interaction-aware generation of 3D point clouds, enabling the reconstruction of crucial spatial information,를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Achieving humanclevel dexterity in robots is a key ‘objective in the field of robotic manipulation, Recent advance ments in 3D-based imitation learning have shown promising ...
- **p. 1 / Abstract - extractive body cue:** However, obtaining high-quality 3D representations presents two key problems: (1) the quality of point clouds captured by a single-view camera is significantly affected by factors ...
- **p. 1 / Abstract - extractive body cue:** To eliminate these limitations, we propose CordViP, a novel framework that ‘constructs and learns correspondences by leveraging the robust 6D pose estimation of objects and ...
- **p. 1 / Abstract - extractive body cue:** Specifically, We first introduce the interaction-aware point clouds, which ‘establish correspondences between the object and the hand. ‘These point clouds are then used for our ...
- **p. 1 / Abstract - extractive body cue:** where we also incorporate object-centric contact maps and hand arm coordination information, effectively capturing both spatial
- **p. 3 / A. Problem Formulation - extractive body cue:** As a result, CordViP not only effectively addresses occlusion challenges during dexterous manipulation but also significantly improves the model's ability to comprehend spatial interactions and ...
- **p. 3 / A. Problem Formulation - extractive body cue:** robot's observations and A represents the corresponding actions, allowing the robot to generalize beyond the taining data distribution.

## Core Idea

- **p. 3 / B. Interaction-aware Generation of 3D Point Clouds - extractive body cue:** To this end, we propose the interaction-aware generation of 3D point clouds, enabling the reconstruction of crucial spatial information,
- **p. 14 / B. Implementation Details - extractive body cue:** The PointNet consists of three fully connected layers, each followed by LayerNorm for normalization and ReLU activation
- **p. 15 / B. Implementation Details - extractive body cue:** For our method, we use only RGB and depth data to track the ‘object's pose.
- **p. 5 / C. Comact and Coordination-Enhanced Feature Extraction - extractive body cue:** This pre-training approach enables the encoder to learn the interactions and relationships within the environment.
- **p. 15 / B. Implementation Details - extractive body cue:** We collect both the robot's state and actions using joint angles in radians, including the 6-DOF joints of the robotic the 16-DOF joints of the ...
- **p. 5 / C. Comact and Coordination-Enhanced Feature Extraction - extractive body cue:** Similarly, we also predict the action sequence of the hand using point clouds and the arm state, We use MSE loss to compute the loss ...
- **p. 5 / C. Comact and Coordination-Enhanced Feature Extraction - extractive body cue:** To help the robot system learn the features of hand-arm coordination, we also propose & correspondence-based design for action prediction. ‘The arm and hand states ...
- **p. 14 / B. Implementation Details - extractive body cue:** The features are then processed through the same Transformer architecture for cross-attention, enabling feature fusion.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In our approach, each observation o, is composed. of the object's point cloud P..), the hand's point cloud Phands and the robot's joint states, including a 6-Dof arm and 16Dof hand configuration. | RGB-D/point cloud, object state와 contact/task observation | p. 3 (A. Problem Formulation), p. 15 (B. Implementation Details) |
| State/latent | observation, composed, object, point, cloud, hand, Phands, robot, joint, states, including, Dof | object geometry, affordance, contact mode 또는 end-effector state | p. 3 (A. Problem Formulation), p. 15 (B. Implementation Details), p. 4 (C. Comact and Coordination-Enhanced Feature Extraction) |
| Output/action | ‘The BCRNNSD is trained for 3000 epochs with horizon=10, n_obs_steps=1, n_action_steps=l, where the observations are replaced from images to point clouds. | grasp, pose, force 또는 end-effector trajectory | p. 15 (B. Implementation Details), p. 4 (C. Comact and Coordination-Enhanced Feature Extraction), p. 5 (C. Comact and Coordination-Enhanced Feature Extraction) |
| Objective/outcome | On the one hand, real-world point cloud data, typically captured using stereo cameras or low-cost RGB-D scanners, suffers from geometric and semantic loss due to factors such as light reflection, material transparency, ... | task completion, contact success, pose/force error와 generalization | p. 3 (B. Interaction-aware Generation of 3D Point Clouds), p. 5 (C. Comact and Coordination-Enhanced Feature Extraction), p. 3 (B. Interaction-aware Generation of 3D Point Clouds) |

## Main Claims and Actual Contribution

- **p. 3 / B. Interaction-aware Generation of 3D Point Clouds - extractive body cue:** To this end, we propose the interaction-aware generation of 3D point clouds, enabling the reconstruction of crucial spatial information,
- **p. 14 / B. Implementation Details - extractive body cue:** The PointNet consists of three fully connected layers, each followed by LayerNorm for normalization and ReLU activation
- **p. 15 / B. Implementation Details - extractive body cue:** For our method, we use only RGB and depth data to track the ‘object's pose.
- **p. 5 / C. Comact and Coordination-Enhanced Feature Extraction - extractive body cue:** This pre-training approach enables the encoder to learn the interactions and relationships within the environment.
- **p. 15 / B. Implementation Details - extractive body cue:** We collect both the robot's state and actions using joint angles in radians, including the 6-DOF joints of the robotic the 16-DOF joints of the ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We propose CordViP, a correspondence-based visuomotor policy for dexterous manipulation in the real world. (a) Left: We present the interaction-aware point clouds, which ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** ‘+ What role does each of the system components play enhancing its overall performance (Section IV-E, IV-F)?
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Experimental results of efficiency. We train ACT, DP, DP3, and CordViP on the PickPlace and FlipCup tasks wi an increasing number of demonstrations.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 1 (Figure/Table caption), p. 5 (IV. EXPERIMENTS) |
| Embodiment/environment | ‘We conduct comprehensive real-world experiments to answer the following questions: | hardware/simulator version and reset protocol | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Dataset/benchmark | consists of a 6-Dof URS robot arm and a 16-Dof Leap Hand | role, split, size and leakage | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (A. Experiment Setup), p. 6 (A. Experiment Setup) |
| Metric | Fig. 1: We propose CordViP, a correspondence-based visuomotor policy for dexterous manipulation in the real world. (a) Left: We present the interaction-aware point clouds, which demonstrate robustness to different viewpoints while estab ... | definition, denominator, direction and uncertainty | p. 1 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 15 (B. Implementation Details) |
| Baseline/ablation | The Diffusion Policy baseline utilizes ResNetI8 as the visual encoder and employs CNN-based backbones. | fair input/data/compute/action matching | p. 15 (B. Implementation Details), p. 15 (B. Implementation Details), p. 4 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 10 / V. CONCLUSIONS AND LimiTATIONS - extractive body cue:** Despite the exceptional performance demonstrated by CordViP, there are still certain limitations that could be explored in future work.
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 8: Failure case. (a) Case / is a failure case from the
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We propose CordViP, a correspondence-based visuomotor policy for dexterous manipulation in the real world. (a) Left: We present the interaction-aware point clouds, which ...
- **p. 15 / B. Implementation Details - extractive body cue:** We utilize FoundationPose (60] to perform robust 6D pose estimation for various objects across tasks.

## Why Read It

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 As a result, CordViP not only effectively addresses occlusion challenges during dexterous manipulation but also significantly improves the model's ability to comprehend spatial interactions and collaborative dynamics.를 문제로 두고, To this end, we propose the interaction-aware generation of 3D point clouds, enabling the reconstruction of crucial spatial information,를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (A. Problem Formulation), p. 3 (A. Problem Formulation), p. 5 (C. Comact and Coordination-Enhanced Feature Extraction), p. 5 (C. Comact and Coordination-Enhanced Feature Extraction), p. 14 (B. Implementation Details), p. 14 (B. Implementation Details) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
