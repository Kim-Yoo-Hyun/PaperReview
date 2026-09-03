# Neural Descriptor Fields: SE(3)-Equivariant Object Representations for Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2112.05124.
> PDF retrieval source: https://arxiv.org/pdf/2112.05124. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, equivariant, 3D geometry, manipulation
- Official paper: https://arxiv.org/abs/2112.05124
- Full-text retrieval: https://arxiv.org/pdf/2112.05124
- Code/Project: https://github.com/anthonysimeonov/ndf_robot
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 This enables imitation from few demonstrations, but current approaches-which operate in 2D-suffer several key limitations.를 문제로 두고, We present a novel representation that models dense correspondence across object instances at the level of points and local coordinate frames.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present Neural Descriptor Fields (NDFs), an object representation that encodes both points and relative poses between an object and a target (such as a ...
- **p. 1 / Abstract - extractive body cue:** We employ this representation for object manipulation, where given a task demonstration, we want to repeat the same task on a new object instance from ...
- **p. 1 / Abstract - extractive body cue:** We propose to achieve this objective by searching (via optimization) for the pose whose descriptor matches that observed in the demonstration.
- **p. 1 / Abstract - extractive body cue:** NDFs are conveniently trained in a self-supervised fashion via a 3D auto-encoding task that does not rely on expert-labeled keypoints.
- **p. 1 / Abstract - extractive body cue:** Further, NDFs are SE(3)-equivariant, guaranteeing performance that generalizes across all possible 3D object translations and rotations.
- **p. 2 / I. INTRODUCTION - extractive body cue:** This enables imitation from few demonstrations, but current approaches-which operate in 2D-suffer several key limitations.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We propose a novel method to encode dense correspondence across object instances, dubbed Neural Descriptor Fields (NDF), that effectively overcomes the limitations of prior work: ...

## Core Idea

- **p. 2 / II. METHOD - extractive body cue:** We present a novel representation that models dense correspondence across object instances at the level of points and local coordinate frames.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Using this novel formulation, we propose a system that can imitate pick-and-place tasks for a category of objects from only a small handful of demonstrations.
- **p. 5 / II. METHOD - extractive body cue:** 4), this encoding enables us to transfer a local frame with a reference pose ˆT when provided with a new point cloud by finding the ...
- **p. 3 / II. METHOD - extractive body cue:** We propose to parameterize f via a neural network.
- **p. 3 / II. METHOD - extractive body cue:** As we will see, this continuous, differentiable formulation enables us to find correspondence across object instances via simple first-order optimization.
- **p. 3 / II. METHOD - extractive body cue:** We then discuss how to apply this novel representation for transferring grasp and place poses from a set of pick-andplace demonstrations: We first show how ...
- **p. 3 / II. METHOD - extractive body cue:** These latent codes are obtained as the output of a PointNet [32]- based point cloud encoder E that takes as input a point cloud P, ...
- **p. 7 / II. METHOD - extractive body cue:** In Table II, we analyze the effect of parameterizing NDFs with features from a randomly initialized occupancy network, as well as with only the first- ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | These latent codes are obtained as the output of a PointNet [32]- based point cloud encoder E that takes as input a point cloud P, leading to a conditional occupancy function: Φ(x, ... | RGB-D/point cloud, object state와 contact/task observation | p. 3 (II. METHOD), p. 3 (II. METHOD) |
| State/latent | latent, codes, obtained, output, PointNet, point, cloud, encoder, takes, input, leading, conditional | object geometry, affordance, contact mode 또는 end-effector state | p. 3 (II. METHOD), p. 3 (II. METHOD), p. 4 (II. METHOD) |
| Output/action | Neural Point Descriptor Fields Our key idea is to represent an object as a function f that maps a 3D coordinate x to a spatial descriptor z = f(x) of that 3D ... | grasp, pose, force 또는 end-effector trajectory | p. 3 (II. METHOD), p. 4 (II. METHOD), p. 4 (II. METHOD) |
| Objective/outcome | We initialize T = (R, t) at random and optimize the translation t and rotation R (parameterized via axis-angle) to minimize the L1 distance between the descriptors of ˆT and T: ¯T ... | task completion, contact success, pose/force error와 generalization | p. 5 (II. METHOD), p. 2 (II. METHOD), p. 3 (II. METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / II. METHOD - extractive body cue:** We present a novel representation that models dense correspondence across object instances at the level of points and local coordinate frames.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Using this novel formulation, we propose a system that can imitate pick-and-place tasks for a category of objects from only a small handful of demonstrations.
- **p. 5 / II. METHOD - extractive body cue:** 4), this encoding enables us to transfer a local frame with a reference pose ˆT when provided with a new point cloud by finding the ...
- **p. 3 / II. METHOD - extractive body cue:** We propose to parameterize f via a neural network.
- **p. 3 / II. METHOD - extractive body cue:** As we will see, this continuous, differentiable formulation enables us to find correspondence across object instances via simple first-order optimization.
- **p. 6 / II. METHOD - extractive body cue:** For objects in arbitrary poses (bottom row), DON's performance suffers, while NDFs maintains higher success rates due to their equivariance to SE(3) transformations. to achieve ...
- **p. 6 / II. METHOD - extractive body cue:** For objects in upright poses (top row), NDFs perform on par with DON on grasp success rate, but outperforms DON on overall pick-and-place success rate.
- **p. 7 / II. METHOD - extractive body cue:** We find that while the performance of NDFs decreases significantly in the singledemonstration case, it still significantly outperforms DON, and more demonstrations yield significant performance ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (II. METHOD), p. 6 (II. METHOD) |
| Embodiment/environment | Next, we consider a harder setting: while the demonstrations are all performed on upright-posed objects, the robot must subsequently execute the task on objects in arbitrary SE(3) poses. | hardware/simulator version and reset protocol | p. 7 (II. METHOD), p. 5 (II. METHOD) |
| Dataset/benchmark | On first glance, this would require setting up a training objective for correspondence matching, and consequently, collection and labeling of a custom dataset. | role, split, size and leakage | p. 7 (II. METHOD), p. 5 (II. METHOD), p. 3 (II. METHOD), p. 3 (II. METHOD) |
| Metric | For objects in arbitrary poses (bottom row), DON's performance suffers, while NDFs maintains higher success rates due to their equivariance to SE(3) transformations. to achieve success rate above 10%. | definition, denominator, direction and uncertainty | p. 6 (II. METHOD), p. 7 (II. METHOD), p. 5 (II. METHOD) |
| Baseline/ablation | For objects in upright poses (top row), NDFs perform on par with DON on grasp success rate, but outperforms DON on overall pick-and-place success rate. | fair input/data/compute/action matching | p. 6 (II. METHOD), p. 7 (II. METHOD), p. 7 (II. METHOD) |

## Explicit Limitations and Failure Boundary

- **p. 8 / VI. DISCUSSION AND CONCLUSION - extractive body cue:** Several limitations and avenues for future work remain.
- **p. 6 / II. METHOD - extractive body cue:** (Bottom) In contrast, placing query points near the bottom of the mug leads to a transferred pose that is biased toward the bottom of the ...
- **p. 7 / II. METHOD - extractive body cue:** We find that DON's failures are usually a function of either insufficient precision in keypoint predictions, or failed registration of testtime keypoints to the demonstration ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 8: Qualitative Examples of Grasp Predictions - Both DON and NDF predict successful grasps on upright mugs. When mugs exhibit arbitrary poses, DON fails ...
- **p. 8 / VI. DISCUSSION AND CONCLUSION - extractive body cue:** Furthermore, we assume the placement target remains static: future work may explore similarly inferring an object-centric representation of the placement target.
- **p. 3 / II. METHOD - extractive body cue:** This is an attractive property, as at test time, we regularly only observe partial point clouds of objects due to occlusions.
- **p. 5 / II. METHOD - extractive body cue:** While we provide an in-depth evaluation in the experiments section, this result is representative in that the end-effector reliably and robustly converges to the correct ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 This enables imitation from few demonstrations, but current approaches-which operate in 2D-suffer several key limitations.를 문제로 두고, We present a novel representation that models dense correspondence across object instances at the level of points and local coordinate frames.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (II. METHOD), p. 3 (II. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (9 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, the ability of current methods to learn from demonstrations is severely limited. (p. 1, I. INTRODUCTION).
- **Actual contribution:** We present a novel representation that models dense correspondence across object instances at the level of points and local coordinate frames. (p. 2, II. METHOD).
- **Evaluation boundary:** For objects in arbitrary poses (bottom row), DON's performance suffers, while NDFs maintains higher success rates due to their equivariance to SE(3) transformations. to achieve success rate above 10%. (p. 6, II. METHOD).
- **Explicit failure boundary:** We find that DON's failures are usually a function of either insufficient precision in keypoint predictions, or failed registration of testtime keypoints to the demonstration keypoints. (p. 7, II. METHOD).
