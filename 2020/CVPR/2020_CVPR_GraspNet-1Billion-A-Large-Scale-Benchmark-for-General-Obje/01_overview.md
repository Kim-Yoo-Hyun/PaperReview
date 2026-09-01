# GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; title-token overlap first two pages=0.75); canonical paper source: https://arxiv.org/abs/1912.13470.
> PDF retrieval source: https://arxiv.org/pdf/1912.13470. Reading tracker status/evidence was not changed.

- Year/Venue: 2020 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: CORE
- Tags: Robotics, grasping, Benchmark, 6-DoF grasp
- Official paper: https://arxiv.org/abs/1912.13470
- Full-text retrieval: https://arxiv.org/pdf/1912.13470
- Code/Project: https://graspnet.net/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; title-token overlap first two pages=0.75)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Secondly, it is difficult to obtain large-scale high quality training data [3].를 문제로 두고, Our methodology for building the dataset.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Object grasping is critical for many applications, which is also a challenging computer vision problem.
- **p. 1 / Abstract - extractive body cue:** However, for clustered scene, current researches suffer from the problems of insufficient training data and the lacking of evaluation benchmarks.
- **p. 1 / Abstract - extractive body cue:** In this work, we contribute a large-scale grasp pose detection dataset with an unified evaluation system.
- **p. 1 / Abstract - extractive body cue:** Our dataset contains 87,040 RGBD image with over 370 million grasp poses.
- **p. 1 / Abstract - extractive body cue:** Meanwhile, our evaluation system directly reports whether a grasping is successful or not by analytic computation, which is able to evaluate any kind of grasp ...
- **p. 1 / 1. Introduction - extractive body cue:** Secondly, it is difficult to obtain large-scale high quality training data [3].
- **p. 1 / 1. Introduction - extractive body cue:** The difference in evaluation metrics makes it difficult to compare these methods directly in an unified manner, while evaluating with real robots would dramatically increase ...

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** Our methodology for building the dataset.
- **p. 1 / 1. Introduction - extractive body cue:** Specifically, inspired by previous literature [24], we propose a two-step pipeline to generate tremendous grasp poses for a scene.
- **p. 2 / 3.1. Overview - extractive body cue:** To overcome these issues, we propose a large-scale dataset in clustered scenario with dense and rich annotations for grasp pose prediction named GraspNet.
- **p. 3 / 3.3. Data Annotation - extractive body cue:** Considering all the objects are known, we propose a two stage automated pipeline for grasp pose annotation, which is illustrated in Fig.
- **p. 1 / 1. Introduction - extractive body cue:** Firstly, the grasp pose has different representations including rectangle [23] and 6D pose [24] representation and are evaluated with different metrics [11, 10, 24] correspondingly.
- **p. 1 / 1. Introduction - extractive body cue:** Thanks to our automatic annotation process, we built the first large-scale in-the-wild grasp pose dataset that can serve as a base for training and evaluating ...
- **p. 3 / 3.2. Data Collection - extractive body cue:** The robot arm then moves along a fixed trajectory that covers 256 distinct viewpoints on a quarter sphere.
- **p. 4 / 2 Cams - extractive body cue:** The force-closure metric [20, 24] has been proved effective in grasp evaluation: given a grasp pose, the associated object and a friction coefficient µ, force-closure ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The key of grasping is to detect the grasp pose given visual inputs (image or point cloud) and has drawn many attentions in computer vision community [8, 21]. | standardized observation, action, task state와 evaluation split | p. 1 (1. Introduction), p. 4 (2 Cams) |
| State/latent | grasping, detect, grasp, pose, given, visual, inputs, image, point, cloud, drawn, many | benchmark state/goal와 method decision | p. 1 (1. Introduction), p. 4 (2 Cams), p. 3 (3.2. Data Collection) |
| Output/action | The force-closure metric [20, 24] has been proved effective in grasp evaluation: given a grasp pose, the associated object and a friction coefficient µ, force-closure metric outputs a binary label indicating whether ... | policy/controller trajectory 또는 measured result | p. 4 (2 Cams), p. 3 (3.2. Data Collection), p. 2 (3.1. Overview) |
| Objective/outcome | The difference in evaluation metrics makes it difficult to compare these methods directly in an unified manner, while evaluating with real robots would dramatically increase the evaluation cost. | success metric, robustness, generalization과 reproducibility | p. 1 (1. Introduction), p. 1 (1. Introduction), p. 4 (2 Cams) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** Our methodology for building the dataset.
- **p. 1 / 1. Introduction - extractive body cue:** Specifically, inspired by previous literature [24], we propose a two-step pipeline to generate tremendous grasp poses for a scene.
- **p. 2 / 3.1. Overview - extractive body cue:** To overcome these issues, we propose a large-scale dataset in clustered scenario with dense and rich annotations for grasp pose prediction named GraspNet.
- **p. 3 / 3.3. Data Annotation - extractive body cue:** Considering all the objects are known, we propose a two stage automated pipeline for grasp pose annotation, which is illustrated in Fig.
- **p. 5 / 4.1. Ground-Truth Evaluation - extractive body cue:** Summary of real world success rate of grasping given different grasp score. grasp poses to the camera frame using objects' 6D poses, we paste ArUco ...
- **p. 4 / 3.4. Evaluation - extractive body cue:** Currently, the Cornell dataset [11] has achieved over 99% accuracy.
- **p. 3 / 3.3. Data Annotation - extractive body cue:** To achieve that, high quality mesh models are downsampled such that the sampled points (called grasp points) are uniformly distributed in voxel space.
- **p. 4 / 3.4. Evaluation - extractive body cue:** It might overestimate the performance of grasping algorithm.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 5 (4.1. Ground-Truth Evaluation), p. 4 (3.4. Evaluation) |
| Embodiment/environment | Dataset Split For our 170 scenes, we use 100 for training and 70 for testing. | hardware/simulator version and reset protocol | p. 4 (3.4. Evaluation), p. 4 (3.4. Evaluation) |
| Dataset/benchmark | In this section, we conduct robotic experiments to demonstrate that our ground-truth annotations can align well with real-world grasping. | role, split, size and leakage | p. 4 (3.4. Evaluation), p. 4 (3.4. Evaluation), p. 5 (4. Experiments), p. 2 (3.2. Data Collection) |
| Metric | Summary of real world success rate of grasping given different grasp score. grasp poses to the camera frame using objects' 6D poses, we paste ArUco code on the objects and only label ... | definition, denominator, direction and uncertainty | p. 5 (4.1. Ground-Truth Evaluation), p. 4 (3.4. Evaluation), p. 5 (3.4. Evaluation) |
| Baseline/ablation | Fig 2 illustrates the key components of our dataset. | fair input/data/compute/action matching | p. 2 (3.1. Overview), p. 3 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 3.5. Discussion - extractive body cue:** The previous method that pre-computed ground truth for evaluating grasping, no matter collected by human annotation [11] or simulation [7], cannot cover all feasible solution.
- **p. 5 / 3.5. Discussion - extractive body cue:** Such evaluation method does not assume the representation of the grasp pose, thus is general in practice.
- **p. 3 / 3.3. Data Annotation - extractive body cue:** Collision detection is also conducted to avoid the collision between grasps and background or other object. where Pj i is the 6D pose of object ...
- **p. 3 / 3.3. Data Annotation - extractive body cue:** The 6D poses will then be propagated to the remaining frames by: Pj i = cam-1 i cam0Pj 0, (1) Gripper Depth Sampling Grasp View ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Our methodology for building the dataset. We collect data with real-world sensors and annotate grasp poses for every single object by analytic computation. ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Secondly, it is difficult to obtain large-scale high quality training data [3].를 문제로 두고, Our methodology for building the dataset.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.2. Data Collection) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
