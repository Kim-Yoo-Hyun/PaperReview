# DextAIRity: Deformable Manipulation Can be a Breeze

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2203.01197.
> PDF retrieval source: https://arxiv.org/pdf/2203.01197. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, deformable object, cloth manipulation, air flow, dexterous manipulation, real-world control
- Official paper: https://arxiv.org/abs/2203.01197
- Full-text retrieval: https://arxiv.org/pdf/2203.01197
- Code/Project: https://dextairity.cs.columbia.edu/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 However, despite the potential advantages of air-based manipulation, it is an open and challenging problem.를 문제로 두고, Our system setup consists of (a) three UR5 robot arms, two of which are equipped with parallel-jaw grippers and one with a commodity centrifugal air pump.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** This paper introduces DextAIRity, an approach to manipulate deformable objects using active airflow.
- **p. 1 / Abstract - extractive body cue:** In contrast to conventional contact-based quasi-static manipulations, DextAIRity allows the system to apply dense forces on out-ofcontact surfaces, expands the system's reach range, and provides ...
- **p. 1 / Abstract - extractive body cue:** These properties are particularly advantageous when manipulating under-actuated deformable objects with large surface areas or volumes.
- **p. 1 / Abstract - extractive body cue:** We demonstrate the effectiveness of DextAIRity through two challenging deformable object manipulation tasks: cloth unfolding and bag opening.
- **p. 1 / Abstract - extractive body cue:** We present a self-supervised learning framework that learns to effectively perform a target task through a sequence of grasping or air-based blowing actions.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, despite the potential advantages of air-based manipulation, it is an open and challenging problem.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Both challenges motivate a self-supervised closed-loop solution for DextAIRity that could learn and improve from data.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our system setup consists of (a) three UR5 robot arms, two of which are equipped with parallel-jaw grippers and one with a commodity centrifugal air ...
- **p. 4 / IV. METHOD - extractive body cue:** The blowing network consists of an image encoder (7-layer convolution network) and an action encoder (3-layer MLP), followed by a 3-layer MLP to produce the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This property particularly is useful when the target object has a large volume or surface area - spreading a large piece of cloth for instance ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The primary contribution of this work is to suggest a new approach for deformable object manipulation utilizing directed airstreams, DextAIRity.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Instead of applying force through sparse contact positions, DextAIRity allows the system to simultaneously apply dense forces to a 3D space.
- **p. 5 / IV. METHOD - extractive body cue:** We use the same blowing network architecture as in the unfolding task, but with a few modifications in action parameterization, reward signal, and directly train ...
- **p. 4 / IV. METHOD - extractive body cue:** We use DeepLabv3 [5] with random initialization as network architecture.
- **p. 5 / IV. METHOD - extractive body cue:** In total, we collected 4,400 (4,000 for training, 400 for validation) interactions over the course of 10 hours and trained the blowing network 50 epochs ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Observation Blowing Scores Blowing Network max Execution Cloth unfolding Grasp (a) Grasping Policy (Cloth Unfolding) Stretch Place Initial State Bag opening ×8 rotations Observation Grasping Scores max Selected Grasp Grasping Network … ... | RGB-D/point cloud, object state와 contact/task observation | p. 4 (IV. METHOD), p. 5 (IV. METHOD) |
| State/latent | Observation, Blowing, Scores, Network, Execution, Cloth, unfolding, Grasp, Grasping, Policy, Stretch, Place | object geometry, affordance, contact mode 또는 end-effector state | p. 4 (IV. METHOD), p. 5 (IV. METHOD), p. 4 (IV. METHOD) |
| Output/action | At each blowing step, a top-down depth observation as input and the blowing action with the highest score will be executed. | grasp, pose, force 또는 end-effector trajectory | p. 5 (IV. METHOD), p. 4 (IV. METHOD), p. 2 (I. INTRODUCTION) |
| Objective/outcome | In total, we collected 4,400 (4,000 for training, 400 for validation) interactions over the course of 10 hours and trained the blowing network 50 epochs with a standard Cross Entropy loss. | task completion, contact success, pose/force error와 generalization | p. 5 (IV. METHOD), p. 4 (IV. METHOD), p. 4 (IV. METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our system setup consists of (a) three UR5 robot arms, two of which are equipped with parallel-jaw grippers and one with a commodity centrifugal air ...
- **p. 4 / IV. METHOD - extractive body cue:** The blowing network consists of an image encoder (7-layer convolution network) and an action encoder (3-layer MLP), followed by a 3-layer MLP to produce the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This property particularly is useful when the target object has a large volume or surface area - spreading a large piece of cloth for instance ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The primary contribution of this work is to suggest a new approach for deformable object manipulation utilizing directed airstreams, DextAIRity.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Instead of applying force through sparse contact positions, DextAIRity allows the system to simultaneously apply dense forces to a 3D space.
- **p. 7 / V. EVALUATION - extractive body cue:** II shows performance averaged over 10 test episodes; our policy achieves over 80% on all cloth types, outperforming [FlingBot] and [Pick&Place] by roughly 60% and ...
- **p. 8 / V. EVALUATION - extractive body cue:** In contrast, [DextAIRity] achieves 60% success rate at the first interaction step and achieved a final success rate, after 4 blowing steps, of 88%.
- **p. 8 / V. EVALUATION - extractive body cue:** We found that dynamic action [Shake] generally fails to open the bag while [DextAIRity-fixed] achieved a roughly 50% success rate on the testing bags.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (V. EVALUATION), p. 8 (V. EVALUATION) |
| Embodiment/environment | For both tasks, we evaluate task completion rate and ability to generalize to unseen cloths and bags on a real-world robot platform. | hardware/simulator version and reset protocol | p. 5 (V. EVALUATION), p. 6 (V. EVALUATION) |
| Dataset/benchmark | Simulation Task Generation: We generate five tasks for training and evaluation in simulation: • (Train) Normal Rect contains rectangular cloths that are smaller in size than the robot's reach range. | role, split, size and leakage | p. 5 (V. EVALUATION), p. 6 (V. EVALUATION), p. 5 (V. EVALUATION), p. 6 (V. EVALUATION) |
| Metric | Bag opening Task-performance for bag opening is measured by two metrics: 1) success rate: p = 1 N ∑N 1 sgn(Ai ≥ˆA), and 2) normalized bag area: ¯A = 1 N ∑N ... | definition, denominator, direction and uncertainty | p. 7 (V. EVALUATION), p. 8 (V. EVALUATION), p. 8 (V. EVALUATION) |
| Baseline/ablation | As a result, coverage of X-Large Rect increases +23.0%, +13.3%, +1.6%, and +0.3% at each blow step compared to the fixed-policy ablation. | fair input/data/compute/action matching | p. 6 (V. EVALUATION), p. 6 (V. EVALUATION), p. 7 (V. EVALUATION) |

## Explicit Limitations and Failure Boundary

- **p. 8 / VI. LIMITATIONS AND PRACTICAL CONSIDERATIONS - extractive body cue:** While in this paper we demonstrate the effectiveness of directed air to manipulate deformable objects, we discuss a few limitations and practical considerations of deploying ...
- **p. 6 / V. EVALUATION - extractive body cue:** The failure of [FlingBot] is due to its limited move speed, which needs to Large Rect X-Large Rect Shirt Dress Pick&Place 36.2 / 13.1 38.0 ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 10: Failure Cases. (a) A corner is inadvertently rolled up due to Eddy effects. (b) Multiple layers of the fabric are mistakenly grasped. (c) ...
- **p. 6 / V. EVALUATION - extractive body cue:** Overall, we find that quasi-static pick-and-place actions are generally inefficient for cloth unfolding and, while dynamic actions such as flinging can drastically improve efficiency, however, ...
- **p. 7 / V. EVALUATION - extractive body cue:** 7, suggests [FlingBot] can successfully unfold shirts with width within the reach range but it fails (see the pink dress) when items become much longer.
- **p. 7 / V. EVALUATION - extractive body cue:** 7) suggest that even on out of distribution clothing, our learned grasping policy attempts to grasp cloth corners and the blowing policy preferentially directs air ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 However, despite the potential advantages of air-based manipulation, it is an open and challenging problem.를 문제로 두고, Our system setup consists of (a) three UR5 robot arms, two of which are equipped with parallel-jaw grippers and one with a commodity centrifugal air pump.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 5 (IV. METHOD), p. 4 (IV. METHOD), p. 4 (IV. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
