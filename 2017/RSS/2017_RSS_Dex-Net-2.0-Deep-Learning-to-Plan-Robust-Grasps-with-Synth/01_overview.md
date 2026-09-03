# Dex-Net 2.0: Deep Learning to Plan Robust Grasps with Synthetic Point Clouds and Analytic Grasp Metrics

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1703.09312.
> PDF retrieval source: https://arxiv.org/pdf/1703.09312. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2017 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, grasping, synthetic data, analytic grasp metric
- Official paper: https://arxiv.org/abs/1703.09312
- Full-text retrieval: https://arxiv.org/pdf/1703.09312
- Code/Project: https://berkeleyautomation.github.io/dex-net/
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 Reliable robotic grasping is challenging due to imprecision in sensing and actuation, which leads to uncertainty about properties such as object shape, pose, material properties, and mass.를 문제로 두고, Our primary contributions are: 1) the Dexterity Network (Dex-Net) 2.0, a dataset associating 6.7 million point clouds and analytic grasp quality metrics with parallel-jaw grasps planned using robust quasi-static GWS analysis on ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** To reduce data collection time for deep learning of robust robotic grasp plans, we explore training from a synthetic dataset of 6.7 million point clouds, ...
- **p. 1 / Abstract - extractive body cue:** We use the resulting dataset, DexNet 2.0, to train a Grasp Quality Convolutional Neural Network (GQ-CNN) model that rapidly predicts the probability of success of ...
- **p. 1 / Abstract - extractive body cue:** Experiments with over 1,000 trials on an ABB YuMi comparing grasp planning methods on singulated objects suggest that a GQ-CNN trained with only synthetic data ...
- **p. 1 / Abstract - extractive body cue:** The Dex-Net 2.0 grasp planner also has the highest success rate on a dataset of 10 novel rigid objects and achieves 99% precision (one false ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Reliable robotic grasping is challenging due to imprecision in sensing and actuation, which leads to uncertainty about properties such as object shape, pose, material properties, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** (Right) The GQ-CNN rapidly determines the most robust grasp candidate, which is executed with the ABB YuMi robot. not generalize well to new objects, and ...
- **p. 2 / III. PROBLEM STATEMENT - extractive body cue:** We consider the problem of planning a robust planar parallel-jaw grasp for a singulated rigid object resting on a table based on point clouds from ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our primary contributions are: 1) the Dexterity Network (Dex-Net) 2.0, a dataset associating 6.7 million point clouds and analytic grasp quality metrics with parallel-jaw grasps ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We find that the Dex-Net 2.0 grasp planner is 3× faster than the registration-based method, 93% successful on objects seen in training (the highest of ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** Learning Q rather than directly learning the policy allows us to enforce task-specific constraints without having to update the learned model.
- **p. 5 / V. GRASP PLANNING - extractive body cue:** The Dex-Net 2.0 grasp planner uses the robust grasping policy πθ(y) = argmaxu∈CQθ(u, y) illustrated in Fig.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We learn a function that takes as input a candidate grasp and a depth image and outputs an estimate of robustness [27, 56], or probability of success under uncertainty in sensing and ... | RGB-D/point cloud, object state와 contact/task observation | p. 2 (III. PROBLEM STATEMENT), p. 3 (III. PROBLEM STATEMENT) |
| State/latent | learn, function, takes, input, candidate, grasp, depth, image, outputs, estimate, robustness, probability | object geometry, affordance, contact mode 또는 end-effector state | p. 2 (III. PROBLEM STATEMENT), p. 3 (III. PROBLEM STATEMENT), p. 3 (III. PROBLEM STATEMENT) |
| Output/action | Let y = RH×W + be a 2.5D point cloud represented as a depth image with height H and width W taken by a camera with known intrinsics [18], and let Tc ... | grasp, pose, force 또는 end-effector trajectory | p. 3 (III. PROBLEM STATEMENT), p. 3 (III. PROBLEM STATEMENT), p. 1 (I. INTRODUCTION) |
| Objective/outcome | The set C is a discrete set of antipodal candidate grasps [6] sampled uniformly at random in image space for surface normals defined by the depth image gradients. | task completion, contact success, pose/force error와 generalization | p. 5 (V. GRASP PLANNING) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our primary contributions are: 1) the Dexterity Network (Dex-Net) 2.0, a dataset associating 6.7 million point clouds and analytic grasp quality metrics with parallel-jaw grasps ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We find that the Dex-Net 2.0 grasp planner is 3× faster than the registration-based method, 93% successful on objects seen in training (the highest of ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** Learning Q rather than directly learning the policy allows us to enforce task-specific constraints without having to update the learned model.
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** We found that GQ planned grasps 3× faster than REG and achieved a high 93% success rate and 94% precision.
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** The results also suggest that training on the full Dex-Net 2.0 dataset was necessary to achieve higher than 90% success.
- **p. 8 / VI. EXPERIMENTS - extractive body cue:** IGQ REG GQ-Adv-Phys GQ-Adv GQ-S GQ Success Rate (%) 60±13 52±14 68±13 74±12 72±12 80±11 Precision (%) N/A N/A 68 87 92 100 Robust Grasp ...
- **p. 8 / VI. EXPERIMENTS - extractive body cue:** Performance decreases with smaller training datasets, but the GQ-CNN methods outperform the image-based grasp quality metrics (IGQ) and point cloud registration (REG).
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** 2) Precision: The success rate on grasps that are have an estimated robustness higher than 50%.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS) |
| Embodiment/environment | To benchmark the architecture outside of our datasets, we trained on the Cornell Grasping Dataset [31] (containing 8,019 examples) and achieved a 93.0% recognition rate using grayscale images and an 80-20 imagewise ... | hardware/simulator version and reset protocol | p. 7 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS) |
| Dataset/benchmark | We used four different GQ-CNN training datasets to study the effect on performance, each with a 80-20 image-wise training and validation split: 1) Adv-Synth: Synthetic images and grasps for the adversarial objects ... | role, split, size and leakage | p. 7 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 8 (VI. EXPERIMENTS) |
| Metric | Comparions of Methods GQ-CNN Parameter Sensitivity Random IGQ ML-RF ML-SVM REG GQ-L-Adv GQ-S-Adv GQ-Adv GQ-Adv-Phys GQ-Adv-FC GQ-Adv-LowU GQ-Adv-HighU Success Rate (%) 58±11 70±10 75±9 80±9 95±5 93±6 85±8 83±8 80±9 83±8 78±9 ... | definition, denominator, direction and uncertainty | p. 7 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS) |
| Baseline/ablation | Grasp Planning Methods Used for Comparison We compared a number of grasp planning methods on simulated and real data. | fair input/data/compute/action matching | p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 8 / I. Failure Modes - extractive body cue:** The most common failure modes were related to: (left) missing sensor data for an important part of the object geometry, such as thin parts of ...
- **p. 8 / I. Failure Modes - extractive body cue:** A second type of failure occured due to collisions with the object.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Dex-Net 2.0 pipeline for training dataset generation. (Left) The database contains 1,500 3D object mesh models. (Top) For each object, we sample hundreds ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: (Left) Architecture of the Grasp Quality Convolutional Neural Network (GQ-CNN). Planar grasp candidates u = (i, j, ϕ, z) are generated from a ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 9: (Left) Grasp robustness predicted by a Grasp Quality Convolutional Neural Network (GQ-CNN) trained with Dex-Net 2.0 over the space of depth images and ...
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** We chose objects based on geometric features under three constraints: (a) small enough to fit within the workspace, (b) weight less than 0.25kg, the payload ...
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** We hypothesize that vertical filters help to detect antipodal contact normals and the coarse oriented gradients estimate collisions.

## Why Read It

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 Reliable robotic grasping is challenging due to imprecision in sensing and actuation, which leads to uncertainty about properties such as object shape, pose, material properties, and mass.를 문제로 두고, Our primary contributions are: 1) the Dexterity Network (Dex-Net) 2.0, a dataset associating 6.7 million point clouds and analytic grasp quality metrics with parallel-jaw grasps planned using robust quasi-static GWS analysis on ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (III. PROBLEM STATEMENT), p. 2 (III. PROBLEM STATEMENT), p. 3 (III. PROBLEM STATEMENT), p. 5 (V. GRASP PLANNING) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
