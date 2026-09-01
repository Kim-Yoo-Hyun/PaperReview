# VISTA: Open-Vocabulary, Task-Relevant Robot Exploration with Online Semantic Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html.
> PDF retrieval source: https://arxiv.org/pdf/2507.01125. Reading tracker status/evidence was not changed.

- Year/Venue: 2026 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: Robotics, Gaussian Splatting, semantic
- Official paper: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html
- Full-text retrieval: https://arxiv.org/pdf/2507.01125
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Prior work in robot exploration broadly uses traditional 3D scene representations, such as occupancy grids and voxel grids.를 문제로 두고, We present VISTA, an algorithm for Viewpoint-based Image Selection with Semantic Task Awareness.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present VISTA (Viewpoint-based Image selection with Semantic Task Awareness), an active exploration method for robots to plan informative trajectories that improve 3D map quality ...
- **p. 1 / Abstract - extractive body cue:** Given an open-vocabulary search instruction (e.g., "find a person"), VISTA enables a robot to explore its environment to search for the object of interest, while ...
- **p. 1 / Abstract - extractive body cue:** The robot navigates its environment by planning receding-horizon trajectories that prioritize semantic similarity to the query and exploration of unseen regions of the environment.
- **p. 1 / Abstract - extractive body cue:** To evaluate trajectories, VISTA introduces a novel, efficient viewpoint-semantic coverage metric that quantifies both the geometric view diversity and task relevance in the 3D scene.
- **p. 1 / Abstract - extractive body cue:** On static datasets, our coverage metric outperforms state-of-the-art baselines, FisherRF and Bayes' Rays, in computation speed and reconstruction quality.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Prior work in robot exploration broadly uses traditional 3D scene representations, such as occupancy grids and voxel grids.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In each voxel, the geometric uncertainty is the minimum angular separation between the test viewpoint and all view angles from which that voxel has appeared ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** We present VISTA, an algorithm for Viewpoint-based Image Selection with Semantic Task Awareness.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We introduce: 1) an efficient information metric that combines view angle diversity and semantic task relevance stored on a voxel grid that can be recursively ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Through an experimental campaign with a total of 36 hardware executions, we show that VISTA outperforms state-of-the-art baselines, achieving 6x better success rates in environments ...
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** This explicit representation not only enables Gaussian Splatting to avoid unnecessary computation involving empty space, but it also enables the utilization of fast tile-based rasterization.
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** The robot's motion is then modeled as a planar single integrator with a heading angle in the yaw direction.
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** We consider a robotic exploration problem in which a robot has an onboard, forward-facing RGB-D camera with reliable state estimation.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | As the robot moves, it collects full pose odometry information along with RGB and depth images in order to train a 3DGS map of the environment. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (III. PROBLEM FORMULATION), p. 2 (I. INTRODUCTION) |
| State/latent | robot, moves, collects, full, pose, odometry, information, along, RGB, depth, images, order | geometry, map, object/relationship state | p. 3 (III. PROBLEM FORMULATION), p. 2 (I. INTRODUCTION), p. 3 (III. PROBLEM FORMULATION) |
| Output/action | the robot's environment online using a Gaussian Splatting (3DGS) representation [5].1 To enable open-vocabulary, taskrelevant robot exploration, VISTA distills semantic features from vision-language models, e.g., CLIP [1], into the 3DGS ... | point map, pose, scene graph, affordance 또는 query result | p. 2 (I. INTRODUCTION), p. 3 (III. PROBLEM FORMULATION), p. 2 (I. INTRODUCTION) |
| Objective/outcome | As the map updates, we assume that the motion of the robot is restricted in the z, ϕ, and θ axes. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (III. PROBLEM FORMULATION) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** We present VISTA, an algorithm for Viewpoint-based Image Selection with Semantic Task Awareness.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We introduce: 1) an efficient information metric that combines view angle diversity and semantic task relevance stored on a voxel grid that can be recursively ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Through an experimental campaign with a total of 36 hardware executions, we show that VISTA outperforms state-of-the-art baselines, achieving 6x better success rates in environments ...
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** This explicit representation not only enables Gaussian Splatting to avoid unnecessary computation involving empty space, but it also enables the utilization of fast tile-based rasterization.
- **p. 6 / V. RESULTS - extractive body cue:** On the more challenging map domain, we find that our method has a significant improvement over the baseline methods, where our method has a 100% ...
- **p. 6 / V. RESULTS - extractive body cue:** Our geometric information gain metric significantly outperforms baselines FisherRF and Bayes Rays in the next best view selection task for about 50K iterations in three ...
- **p. 5 / V. RESULTS - extractive body cue:** We find that VISTA achieves the highest PSNR and SSIM scores and the lowest LPIPS score across all scenes.
- **p. 5 / V. RESULTS - extractive body cue:** For example, the best-competing method, FisherRF, requires almost twice as many training iterations to achieve the same photometric scores as VISTA, in the Poster

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (V. RESULTS), p. 6 (V. RESULTS) |
| Embodiment/environment | We evaluate each method across six scenes: three benchmark scenes in Nerfstudio (Plane, Kitchen, and Poster) and three additional datasets (Flight, Clutter, and Adirondacks), shown in Fig. | hardware/simulator version and reset protocol | p. 5 (V. RESULTS), p. 5 (V. RESULTS) |
| Dataset/benchmark | Spot Quadruped Hardware Experiments For our second hardware platform, we use a Boston Dynamics Spot quadruped robot fitted with RGB-D cameras and onboard odometry. | role, split, size and leakage | p. 5 (V. RESULTS), p. 5 (V. RESULTS), p. 6 (V. RESULTS), p. 6 (V. RESULTS) |
| Metric | We evaluate all methods on success rate (SR), time to reach (TTR), and success weighted by inverse path length (SPL), as done in [43] and [44]. | definition, denominator, direction and uncertainty | p. 6 (V. RESULTS), p. 6 (V. RESULTS), p. 5 (V. RESULTS) |
| Baseline/ablation | The results suggest that our method is able to outperform both baselines on both maps because we reason about both semantic and geometric information gain. | fair input/data/compute/action matching | p. 6 (V. RESULTS), p. 6 (V. RESULTS), p. 5 (V. RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 5 / V. RESULTS - extractive body cue:** We evaluate each method using the standard metrics: Peak-Signal-Noise-Ratio (PSNR), Learned Perceptuation Image Patch Similarity (LPIPS), and Structural Similarity Index Measure (SSIM).
- **p. 6 / V. RESULTS - extractive body cue:** Through these experiments, we find that all methods have some successes on the easy low-occlusion map domain.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4. The top row shows our three environments and two robots, with the search object in a green circle. The second row shows an ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Prior work in robot exploration broadly uses traditional 3D scene representations, such as occupancy grids and voxel grids.를 문제로 두고, We present VISTA, an algorithm for Viewpoint-based Image Selection with Semantic Task Awareness.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. PROBLEM FORMULATION), p. 3 (III. PROBLEM FORMULATION), p. 6 (V. RESULTS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
