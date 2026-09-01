# Problem - Dex-Net 2.0: Deep Learning to Plan Robust Grasps with Synthetic Point Clouds and Analytic Grasp Metrics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1703.09312; PDF retrieval source: https://arxiv.org/pdf/1703.09312. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (III. PROBLEM STATEMENT), p. 2 (III. PROBLEM STATEMENT), p. 3 (III. PROBLEM STATEMENT)): Reliable robotic grasping is challenging due to imprecision in sensing and actuation, which leads to uncertainty about properties such as object shape, pose, material properties, and mass.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** To reduce data collection time for deep learning of robust robotic grasp plans, we explore training from a synthetic dataset of 6.7 million point clouds, ...
- **p. 1 / Abstract - extractive PDF cue:** We use the resulting dataset, DexNet 2.0, to train a Grasp Quality Convolutional Neural Network (GQ-CNN) model that rapidly predicts the probability of success of ...
- **p. 1 / Abstract - extractive PDF cue:** Experiments with over 1,000 trials on an ABB YuMi comparing grasp planning methods on singulated objects suggest that a GQ-CNN trained with only synthetic data ...
- **p. 1 / Abstract - extractive PDF cue:** The Dex-Net 2.0 grasp planner also has the highest success rate on a dataset of 10 novel rigid objects and achieves 99% precision (one false ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Reliable robotic grasping is challenging due to imprecision in sensing and actuation, which leads to uncertainty about properties such as object shape, pose, material properties, ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** (Right) The GQ-CNN rapidly determines the most robust grasp candidate, which is executed with the ABB YuMi robot. not generalize well to new objects, and ...
- **p. 2 / III. PROBLEM STATEMENT - extractive PDF cue:** We consider the problem of planning a robust planar parallel-jaw grasp for a singulated rigid object resting on a table based on point clouds from ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Reliable robotic grasping is challenging due to imprecision in sensing and actuation, which leads to uncertainty about properties such as object shape, ... | rigid/articulated object와 robot manipulator contact scene | body wording is the source claim |
| Observation / input | We learn a function that takes as input a candidate grasp and a depth image and outputs an estimate of robustness [27, ... | RGB-D/point cloud, object state와 contact/task observation | exact sensor/frame/preprocessing from PDF |
| State / latent | learn, function, takes, input, candidate, grasp, depth, image, outputs, estimate | object geometry, affordance, contact mode 또는 end-effector state | notation and tensor shape require body check |
| Output / action | Let, joint, distribution, grasp, success, grasps, states, point | grasp, pose, force 또는 end-effector trajectory | exact unit/frame/decoder require body check |
| Target outcome | completion, contact success and robustness | task completion, contact success, pose/force error와 generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | object geometry/contact state; body terms: learn, function, takes, input, candidate, grasp, depth, image, outputs, estimate | p. 2 (III. PROBLEM STATEMENT), p. 3 (III. PROBLEM STATEMENT), p. 3 (III. PROBLEM STATEMENT) |
| Decision / output variable | grasp/pose/force/trajectory; body terms: primary, contributions, Dexterity, Network, Dex-Net, dataset, associating, million | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. PROBLEM STATEMENT) |
| Objective / loss / cost | task/contact/pose objective; cue terms: discrete, antipodal, candidate, grasps, sampled, uniformly, random, image | p. 5 (V. GRASP PLANNING), p. 5 (V. GRASP PLANNING) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (V. GRASP PLANNING) |
| Success / guarantee | completion, contact success and robustness | p. 7 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** (Right) The GQ-CNN rapidly determines the most robust grasp candidate, which is executed with the ABB YuMi robot. not generalize well to new objects, and ...
- **p. 2 / III. PROBLEM STATEMENT - extractive PDF cue:** We consider the problem of planning a robust planar parallel-jaw grasp for a singulated rigid object resting on a table based on point clouds from ...
- **p. 2 / III. PROBLEM STATEMENT - extractive PDF cue:** We learn a function that takes as input a candidate grasp and a depth image and outputs an estimate of robustness [27, 56], or probability ...
- **p. 3 / III. PROBLEM STATEMENT - extractive PDF cue:** Let the robustness of a grasp given an observation [5, 56] be the expected value of the metric, or probability of success under uncertainty in ...

## What the Paper Changes

PDF contribution framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. PROBLEM STATEMENT)): Our primary contributions are: 1) the Dexterity Network (Dex-Net) 2.0, a dataset associating 6.7 million point clouds and analytic grasp quality metrics with parallel-jaw grasps planned using robust quasi-static GWS ...

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** We find that the Dex-Net 2.0 grasp planner is 3× faster than the registration-based method, 93% successful on objects seen in training (the highest of ...
- **p. 3 / III. PROBLEM STATEMENT - extractive PDF cue:** Learning Q rather than directly learning the policy allows us to enforce task-specific constraints without having to update the learned model.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | The most common failure modes were related to: (left) missing sensor data for an important part of the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | A second type of failure occured due to collisions with the object. | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Fig. 3: Dex-Net 2.0 pipeline for training dataset generation. (Left) The database contains 1,500 3D object mesh models. ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Fig. 4: (Left) Architecture of the Grasp Quality Convolutional Neural Network (GQ-CNN). Planar grasp candidates u = (i, ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (III. PROBLEM STATEMENT), p. 3 (III. PROBLEM STATEMENT), p. 3 (III. PROBLEM STATEMENT), p. 1 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (III. PROBLEM STATEMENT), p. 2 (III. PROBLEM STATEMENT), p. 3 (III. PROBLEM STATEMENT), interface p. 2 (III. PROBLEM STATEMENT), p. 3 (III. PROBLEM STATEMENT), p. 3 (III. PROBLEM STATEMENT), p. 1 (I. INTRODUCTION), objective p. 5 (V. GRASP PLANNING), p. 5 (V. GRASP PLANNING).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
