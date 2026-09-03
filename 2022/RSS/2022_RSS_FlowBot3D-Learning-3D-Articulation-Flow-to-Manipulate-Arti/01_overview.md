# FlowBot3D: Learning 3D Articulation Flow to Manipulate Articulated Objects

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2205.04382.
> PDF retrieval source: https://arxiv.org/pdf/2205.04382. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: Robotics, 3D Vision, scene flow, articulated objects, point cloud, manipulation
- Official paper: https://arxiv.org/abs/2205.04382
- Full-text retrieval: https://arxiv.org/pdf/2205.04382
- Code/Project: https://flowbot3d.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Due to the large number of categories of such objects and intra-class variations of the objects' structure and kinematics, it is difficult to train efficient perception and manipulation systems that can generalize ...를 문제로 두고, In this paper, we present FlowBot3D, a deep 3D visionbased robotic system that predicts dense per-point motion of an articulated object in 3D space, and leverages this prediction to produce actions that ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We explore a novel method to perceive and manipulate 3D articulated objects that generalizes to enable a robot to articulate unseen classes of objects.
- **p. 1 / Abstract - extractive body cue:** We propose a visionbased system that learns to predict the potential motions of the parts of a variety of articulated objects to guide downstream motion ...
- **p. 1 / Abstract - extractive body cue:** To predict the object motions, we train a neural network to output a dense vector field representing the point-wise motion direction of the points in ...
- **p. 1 / Abstract - extractive body cue:** We then deploy an analytical motion planner based on this vector field to achieve a policy that yields maximum articulation.
- **p. 1 / Abstract - extractive body cue:** We train a single vision model entirely in simulation across all categories of objects, and we demonstrate the capability of our system to generalize to ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Due to the large number of categories of such objects and intra-class variations of the objects' structure and kinematics, it is difficult to train efficient ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** While humans can rapidly adapt to novel articulated objects, constructing robotic manipulation agents that can generalize in the same way poses significant challenges, since the ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present FlowBot3D, a deep 3D visionbased robotic system that predicts dense per-point motion of an articulated object in 3D space, and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these challenges, we propose to separate this problem into one of "affordance learning" and "motion planning." If a robot can predict the potential ...
- **p. 2 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** We first present the theoretical grounding behind the intuition of our method, and we slowly relax assumptions and approximations to create a system that articulates ...
- **p. 4 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** A General Policy using 3D Articulation Flow Algorithm 1 The FlowBot3D articulation manipulation policy Require: θ ←parameters of a trained flow prediction network (O0) ←Initial ...
- **p. 4 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** We know that the ideal attachment point is the location on a part where the flow has the highest magnitude in order to achieve the ...
- **p. 5 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** During each step of training, we select an object in the dataset, randomize the state S of the object, and compute a new supervised pair ...
- **p. 2 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** Our objective is to choose a contact point and force direction (p∗, F∗) that maximizes the acceleration a of the articulation's child link.
- **p. 4 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** For robot control, we use a sampling-based planner, MoveIt!

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | A General Policy using 3D Articulation Flow Algorithm 1 The FlowBot3D articulation manipulation policy Require: θ ←parameters of a trained flow prediction network (O0) ←Initial observation ˆF0 ←fθ(O0, [M0]), Predict the initial ... | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (III. METHOD - FROM THEORY TO PRACTICE), p. 4 (III. METHOD - FROM THEORY TO PRACTICE) |
| State/latent | General, Policy, Articulation, Flow, Algorithm, FlowBot3D, manipulation, Require, parameters, trained, prediction, network | geometry, map, object/relationship state | p. 4 (III. METHOD - FROM THEORY TO PRACTICE), p. 4 (III. METHOD - FROM THEORY TO PRACTICE), p. 3 (III. METHOD - FROM THEORY TO PRACTICE) |
| Output/action | Given the estimate of the 3D articulation flow ˆF0, we now describe a general, closed-loop policy which takes flow as input and actuates an articulated object. | point map, pose, scene graph, affordance 또는 query result | p. 4 (III. METHOD - FROM THEORY TO PRACTICE), p. 3 (III. METHOD - FROM THEORY TO PRACTICE), p. 3 (III. METHOD - FROM THEORY TO PRACTICE) |
| Objective/outcome | Our objective is to choose a contact point and force direction (p∗, F∗) that maximizes the acceleration a of the articulation's child link. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 2 (III. METHOD - FROM THEORY TO PRACTICE), p. 4 (III. METHOD - FROM THEORY TO PRACTICE), p. 4 (III. METHOD - FROM THEORY TO PRACTICE) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present FlowBot3D, a deep 3D visionbased robotic system that predicts dense per-point motion of an articulated object in 3D space, and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these challenges, we propose to separate this problem into one of "affordance learning" and "motion planning." If a robot can predict the potential ...
- **p. 2 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** We first present the theoretical grounding behind the intuition of our method, and we slowly relax assumptions and approximations to create a system that articulates ...
- **p. 4 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** A General Policy using 3D Articulation Flow Algorithm 1 The FlowBot3D articulation manipulation policy Require: θ ←parameters of a trained flow prediction network (O0) ←Initial ...
- **p. 4 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** We know that the ideal attachment point is the location on a part where the flow has the highest magnitude in order to achieve the ...
- **p. 8 / IV. RESULTS - extractive body cue:** Notice that even with occlusions, such as in the intermediate mini-fridge observation, the network is able to predict reasonable 3D articulation flow vectors for downstream ...
- **p. 7 / IV. RESULTS - extractive body cue:** First, our formulation of FlowBot3D has a very high success rate across all categories, including test categories, which are completely novel types of objects (but ...
- **p. 6 / IV. RESULTS - extractive body cue:** At test time, we select the contact point based on ground-truth 3DAF, and after contact 4We could not yet compare directly to UMPNet, as their ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (IV. RESULTS), p. 7 (IV. RESULTS) |
| Embodiment/environment | Real-World Experiments To evaluate the performance of FlowBot3D when executed in a real robotic environment, we design a set of of realworld experiments in which we attempt to articulate a variety of ... | hardware/simulator version and reset protocol | p. 7 (IV. RESULTS), p. 2 (4) Simulated experiments to test the performance of our) |
| Dataset/benchmark | The PartNet-Mobility dataset contains 46 categories of articulated objects; following UMPNet [39], we consider a subset of PartNet-Mobility containing 21 classes, split into 11 training categories (499 training objects, 128 testing obje ... | role, split, size and leakage | p. 7 (IV. RESULTS), p. 2 (4) Simulated experiments to test the performance of our), p. 5 (IV. RESULTS), p. 2 (4) Simulated experiments to test the performance of our) |
| Metric | First, our formulation of FlowBot3D has a very high success rate across all categories, including test categories, which are completely novel types of objects (but may contain similar parts and articulation structures). | definition, denominator, direction and uncertainty | p. 7 (IV. RESULTS), p. 7 (IV. RESULTS), p. 6 (IV. RESULTS) |
| Baseline/ablation | The best BC baseline, DAgger Oracle + F, is only able to fully articulate objects 33% of the time. | fair input/data/compute/action matching | p. 7 (IV. RESULTS), p. 7 (IV. RESULTS), p. 6 (IV. RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 8 / IV. RESULTS - extractive body cue:** Notice that even with occlusions, such as in the intermediate mini-fridge observation, the network is able to predict reasonable 3D articulation flow vectors for downstream ...
- **p. 7 / IV. RESULTS - extractive body cue:** UMPNet Pybullet Environment: The simulation environment used in the original UMPNet evaluations [39] is a PyBullet-based environment with different physical and collision parameters.
- **p. 8 / IV. RESULTS - extractive body cue:** Each object falls into one of either the training or test classes we selected from the PartNet-Mobility.
- **p. 7 / IV. RESULTS - extractive body cue:** Normal Direction estimation suffers from occlusion issues and the normal is not always the correct direction to actuate the object (for example, for the spherical-shaped ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Due to the large number of categories of such objects and intra-class variations of the objects' structure and kinematics, it is difficult to train efficient perception and manipulation systems that can generalize ...를 문제로 두고, In this paper, we present FlowBot3D, a deep 3D visionbased robotic system that predicts dense per-point motion of an articulated object in 3D space, and leverages this prediction to produce actions that ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (III. METHOD - FROM THEORY TO PRACTICE), p. 5 (III. METHOD - FROM THEORY TO PRACTICE), p. 2 (III. METHOD - FROM THEORY TO PRACTICE), p. 4 (III. METHOD - FROM THEORY TO PRACTICE) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Due to the large number of categories of such objects and intra-class variations of the objects' structure and kinematics, it is difficult to train efficient perception and manipulation systems that ... (p. 1, I. INTRODUCTION).
- **Actual contribution:** In this paper, we present FlowBot3D, a deep 3D visionbased robotic system that predicts dense per-point motion of an articulated object in 3D space, and leverages this prediction to produce ... (p. 1, I. INTRODUCTION).
- **Evaluation boundary:** Real-World Experiments To evaluate the performance of FlowBot3D when executed in a real robotic environment, we design a set of of realworld experiments in which we attempt to articulate a ... (p. 7, IV. RESULTS).
- **Explicit failure boundary:** However, the remaining failure modes raise questions we would like to explore in future work. (p. 9, V. CONCLUSION).
