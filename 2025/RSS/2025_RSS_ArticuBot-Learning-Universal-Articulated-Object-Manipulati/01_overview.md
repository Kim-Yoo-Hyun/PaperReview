# ArticuBot: Learning Universal Articulated Object Manipulation Policy via Large Scale Simulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p156.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p156.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, mobile manipulation, simulation, articulated objects
- Official paper: https://www.roboticsproceedings.org/rss21/p156.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p156.pdf
- Code/Project: https://www.roboticsproceedings.org/rss21/p156.html
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 However, few have demonstrated generalization to manipulating many different articulated objects in the real world without simplifying assumptions (e.g, using a suction gripper (10).를 문제로 두고, Instead, we propose to use a hilrarchical policy representation, which consists of 4 high-level policy and a low-level policy.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** This paper presents ArticuBot, in which a learned policy enables a robotics system to open diverse cate egories of unseen articulated objects in the real ...
- **p. 1 / Abstract - extractive body cue:** This task has long been challenging for robotics due to the large variations in the geometry, size, and articulation types of such objects.
- **p. 1 / Abstract - extractive body cue:** Our system, ArticuBot, consists of three parts: generating, a large number of demonstrations in physics-based simulation, distilling all generated demonstrations into a point cloud-based neural ...
- **p. 1 / Abstract - extractive body cue:** demonstrations over 322 training articulated objects.
- **p. 1 / Abstract - extractive body cue:** For policy learning, we propose a novel hierarchical policy representation,
- **p. 2 / 1. INTRODUCTION - extractive body cue:** However, few have demonstrated generalization to manipulating many different articulated objects in the real world without simplifying assumptions (e.g, using a suction gripper (10).
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Many prior works have studied the problem of articulated object' manipulation [58 31, 10, 19, 21, 53, 15, 32].

## Core Idea

- **p. 5 / B. Policy Learning with a Hierarchical Policy Representation - extractive body cue:** Instead, we propose to use a hilrarchical policy representation, which consists of 4 high-level policy and a low-level policy.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** ‘+ We present a weighted displacement policy representation that scales up well with the number of demonstrations, outperforming alternative policy representations.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** 1 for a visualization of some of the different real-world articulated objects that our policy is able to open, In summary, our contributions are:
- **p. 3 / B. Sim2real Policy Learning - extractive body cue:** In contrast, we train a single model that ean be applied to opening various categories of articulated objects Besides, their system requires a specialized gripper, ...
- **p. 4 / 2. Hierarchical Policy Learning -- Low-level Policy Architecture - extractive body cue:** Middle: We propose a weighted displacement model for the high-level policy, which predicts the sub-goal end-effector pose.
- **p. 4 / 2. Hierarchical Policy Learning -- Low-level Policy Architecture - extractive body cue:** Bottom: We propose a goal-conditioned 3D diffusion policy for the low-level policy, which first applies attention between the current end-effector points, the scene points, and ...
- **p. 7 / B. Policy Learning with a Hierarchical Policy Representation - extractive body cue:** The final latent embedding used for diffusion is the concatenation of the above two features: [fpoo™, fom"! yess, po This latent embedding is used ‘as ...
- **p. 8 / B. Is a Hierarchical Policy Needed? - extractive body cue:** takes 3D point cloud as input and outputs delta endeffector transformations as the actions. + DP3 Transformer, which replaces the simplified PointNet encoder in DP3 ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | takes 3D point cloud as input and outputs delta endeffector transformations as the actions. + DP3 Transformer, which replaces the simplified PointNet encoder in DP3 with a transformer-based encoder (the same one ... | egocentric RGB-D, language/task goal, base-arm proprioception | p. 8 (B. Is a Hierarchical Policy Needed?), p. 7 (B. Policy Learning with a Hierarchical Policy Representation) |
| State/latent | takes, point, cloud, input, outputs, delta, endeffector, transformations, actions, DP3, Transformer, replaces | map/object/contact state와 base-arm coordination decision | p. 8 (B. Is a Hierarchical Policy Needed?), p. 7 (B. Policy Learning with a Hierarchical Policy Representation), p. 4 (2. Hierarchical Policy Learning -- Low-level Policy Architecture) |
| Output/action | The final latent embedding used for diffusion is the concatenation of the above two features: [fpoo™, fom"! yess, po This latent embedding is used ‘as the conditioning for an action generation UNet ... | base motion plus arm/gripper action | p. 7 (B. Policy Learning with a Hierarchical Policy Representation), p. 4 (2. Hierarchical Policy Learning -- Low-level Policy Architecture), p. 5 (B. Policy Learning with a Hierarchical Policy Representation) |
| Objective/outcome | Formally, the high-level policy 7! is learned via minimizing the following loss: | long-horizon task success, reachability, collision과 recovery | p. 5 (B. Policy Learning with a Hierarchical Policy Representation), p. 5 (B. Policy Learning with a Hierarchical Policy Representation), p. 4 (2. Hierarchical Policy Learning -- Low-level Policy Architecture) |

## Main Claims and Actual Contribution

- **p. 5 / B. Policy Learning with a Hierarchical Policy Representation - extractive body cue:** Instead, we propose to use a hilrarchical policy representation, which consists of 4 high-level policy and a low-level policy.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** ‘+ We present a weighted displacement policy representation that scales up well with the number of demonstrations, outperforming alternative policy representations.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** 1 for a visualization of some of the different real-world articulated objects that our policy is able to open, In summary, our contributions are:
- **p. 3 / B. Sim2real Policy Learning - extractive body cue:** In contrast, we train a single model that ean be applied to opening various categories of articulated objects Besides, their system requires a specialized gripper, ...
- **p. 4 / 2. Hierarchical Policy Learning -- Low-level Policy Architecture - extractive body cue:** Middle: We propose a weighted displacement model for the high-level policy, which predicts the sub-goal end-effector pose.
- **p. 12 / B. Table-Top Franka Arm Results - extractive body cue:** If we compute the normalized opening performance for ArticuBot only in cases where the grasp is successful (Le., the same starting conditions as FlowBot3D), the ...
- **p. 12 / C. Mobile X-Arm Results - extractive body cue:** As shown, ArticuBot achieves a grasping success rate of 0.9 and normalized opening performance of 0.54, showing it can
- **p. 13 / C. Mobile X-Arm Results - extractive body cue:** 5) Objects in real kitchens and lounges are usually occluded by neighboring objects, and we believe that adding this type of occlusion could further improve ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 12 (B. Table-Top Franka Arm Results), p. 12 (C. Mobile X-Arm Results) |
| Embodiment/environment | Although our training data includes multi-door objects, demonstrations are generated for opening the closest door to the initial pose of the robot. | hardware/simulator version and reset protocol | p. 13 (C. Mobile X-Arm Results), p. 7 (V. SIMULATION RESULTS) |
| Dataset/benchmark | 8 (zoom-in for better views) visualizes ArticuBot's predictions on some of the real-world test objects. | role, split, size and leakage | p. 13 (C. Mobile X-Arm Results), p. 7 (V. SIMULATION RESULTS), p. 12 (B. Table-Top Franka Arm Results), p. 12 (B. Table-Top Franka Arm Results) |
| Metric | As shown, ArticuBot achieves a grasping success rate of 0.9 and normalized opening performance of 0.54, showing it can | definition, denominator, direction and uncertainty | p. 12 (C. Mobile X-Arm Results), p. 12 (B. Table-Top Franka Arm Results), p. 13 (C. Mobile X-Arm Results) |
| Baseline/ablation | ‘The results forall test objects and compared methods in lab A are shown in Fig. | fair input/data/compute/action matching | p. 12 (B. Table-Top Franka Arm Results), p. 12 (B. Table-Top Franka Arm Results), p. 13 (C. Mobile X-Arm Results) |

## Explicit Limitations and Failure Boundary

- **p. 13 / C. Mobile X-Arm Results - extractive body cue:** See Appendix L for visualizations of some of the failure cases of ArticuBot, and some basic failure recovery abilities of ArticuBot.
- **p. 13 / C. Mobile X-Arm Results - extractive body cue:** We leave addressing these limitations as important future work.
- **p. 12 / B. Table-Top Franka Arm Results - extractive body cue:** Common failure ceases for table-top experiments include: 1, The robot arm runs to joint limits while opening the object, due to the limited space of ...
- **p. 12 / B. Table-Top Franka Arm Results - extractive body cue:** The major failure case for FlowBot3D is that the predicted flow is in the wrong direction, e.g., it predicts upwards flows for ‘opening a microwave ...
- **p. 11 / A. Setups - extractive body cue:** We do not input the optional segmentation mask for the target link to open for FlowBot3D, as such masks are not readily available in the ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 However, few have demonstrated generalization to manipulating many different articulated objects in the real world without simplifying assumptions (e.g, using a suction gripper (10).를 문제로 두고, Instead, we propose to use a hilrarchical policy representation, which consists of 4 high-level policy and a low-level policy.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 4 (2. Hierarchical Policy Learning -- Low-level Policy Architecture), p. 5 (B. Policy Learning with a Hierarchical Policy Representation), p. 7 (B. Policy Learning with a Hierarchical Policy Representation), p. 8 (B. Is a Hierarchical Policy Needed?) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
