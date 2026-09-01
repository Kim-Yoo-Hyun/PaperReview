# Gaussian Splatting Visual MPC for Granular Media Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf.
> PDF retrieval source: https://arxiv.org/pdf/2410.09740v3. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, Gaussian Splatting
- Official paper: https://www.proceedings.com/content/081/081087webtoc.pdf
- Full-text retrieval: https://arxiv.org/pdf/2410.09740v3
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, these models often underperform compared to linear dynamics models due to a lack of inductive biases.를 문제로 두고, We form the node features of the GNN as (ci t,σi t ,Ri t,gi t,si t) for node vi t. f consists of node encoder fenc with node representation ¯vi from vi ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent advancements in learned 3D representations have enabled significant progress in solving complex robotic manipulation tasks, particularly for rigid-body objects.
- **p. 1 / Abstract - extractive body cue:** However, manipulating granular materials such as beans, nuts, and rice remains challenging due to the intricate physics of particle interactions, high-dimensional and partially observable state, ...
- **p. 1 / Abstract - extractive body cue:** Current deep latent dynamics models often struggle to generalize in granular material manipulation due to a lack of inductive biases.
- **p. 1 / Abstract - extractive body cue:** In this work, we propose a novel approach that learns a visual dynamics model over Gaussian splatting representations of scenes and leverages this model for ...
- **p. 1 / Abstract - extractive body cue:** Our method enables efficient optimization for complex manipulation tasks on piles of granular media.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, these models often underperform compared to linear dynamics models due to a lack of inductive biases.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Several factors contribute to the difficulty of granular material manipulation.

## Core Idea

- **p. 3 / IV. OUR APPROACH - extractive body cue:** We form the node features of the GNN as (ci t,σi t ,Ri t,gi t,si t) for node vi t. f consists of node encoder ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method takes a few multi-view images of a scene and their corresponding camera poses as input, and (a) converts them into their Gaussian splatting ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our contribution: We use the Gaussian splats representing the scene at each time as a state vector that can be manipulated via MPC, effectively lowering ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our model successfully enables solutions of complex planning tasks.
- **p. 2 / I. INTRODUCTION - extractive body cue:** This representation enables robots to optimize their actions, anticipate challenges, and adapt to dynamic environments.
- **p. 3 / IV. OUR APPROACH - extractive body cue:** The trajectory optimization problem over a horizon T can be defined as follows: u0:T-1 = argminu0:T-1c(ZT,Ztarget) (6) Z0 = h(O0), Ztarget = h(Otarget), Zt+1 = ...
- **p. 4 / IV. OUR APPROACH - extractive body cue:** In the end, we obtain a set of Gaussians that represents the next image: ˆZt+1 = {(ci t,αi t , ˆR i t+1, ˆgi t+1,si ...
- **p. 4 / IV. OUR APPROACH - extractive body cue:** After the first action in the sequence is executed by the robot, we re-run the planning algorithm to generate a new action sequence.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (b) The dynamics model f predicts the temporal evolution of the Gaussian Splatting representation Zt with input action ut. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (III. PRELIMINARIES), p. 3 (IV. OUR APPROACH) |
| State/latent | dynamics, model, predicts, temporal, evolution, Gaussian, Splatting, representation, input, action, Problem, Formulation | geometry, map, object/relationship state | p. 3 (III. PRELIMINARIES), p. 3 (IV. OUR APPROACH), p. 1 (I. INTRODUCTION) |
| Output/action | Problem Formulation Given multi-view RGBD observations Otarget = {ov,mv}N v=1 of the target pattern of the granular material, where ov represents the RGBD image and mv indicates the corresponding camera pose, we ... | point map, pose, scene graph, affordance 또는 query result | p. 3 (IV. OUR APPROACH), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective/outcome | This optimization process aims to acquire the sequence of actions {ut} to minimize the cost function c(ZT,Ztarget). | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (IV. OUR APPROACH), p. 4 (IV. OUR APPROACH), p. 3 (IV. OUR APPROACH) |

## Main Claims and Actual Contribution

- **p. 3 / IV. OUR APPROACH - extractive body cue:** We form the node features of the GNN as (ci t,σi t ,Ri t,gi t,si t) for node vi t. f consists of node encoder ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method takes a few multi-view images of a scene and their corresponding camera poses as input, and (a) converts them into their Gaussian splatting ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our contribution: We use the Gaussian splats representing the scene at each time as a state vector that can be manipulated via MPC, effectively lowering ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our model successfully enables solutions of complex planning tasks.
- **p. 2 / I. INTRODUCTION - extractive body cue:** This representation enables robots to optimize their actions, anticipate challenges, and adapt to dynamic environments.
- **p. 5 / V. EXPERIMENTAL RESULTS - extractive body cue:** Manipulation Results TABLE I MANIPULATION SUCCESS RATE IN SIMULATION (MAX = 1.0) Collection Splitting Redistributing NeRF-dy [38] 0.67 0.43 0.31 Dyn-Res [16] 0.79 0.72 0.67 ...
- **p. 5 / V. EXPERIMENTAL RESULTS - extractive body cue:** Our approach achieves higher performance than NeRF-dy while requiring fewer views.
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** Qualitative results from real-world experiments.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS) |
| Embodiment/environment | (b) The granular materials used in real-world experiments include coffee beans, peanuts, pistachios, and almonds. transfer our model trained in the simulation environment to our real-world experiment setup. | hardware/simulator version and reset protocol | p. 4 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS) |
| Dataset/benchmark | In simulation, we perform 100 trials, while for real-world experiments, we conduct 20 trials. | role, split, size and leakage | p. 4 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), p. 4 (V. EXPERIMENTAL RESULTS) |
| Metric | We use two metrics to evaluate the frameworks. • Success rate: success is defined as moving all materials to the target region. • State error: in simulation experiments, we also measure the ... | definition, denominator, direction and uncertainty | p. 5 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), p. 4 (V. EXPERIMENTAL RESULTS) |
| Baseline/ablation | Manipulation Results TABLE I MANIPULATION SUCCESS RATE IN SIMULATION (MAX = 1.0) Collection Splitting Redistributing NeRF-dy [38] 0.67 0.43 0.31 Dyn-Res [16] 0.79 0.72 0.67 NFD [29] 0.89 0.74 0.46 DVF [17] ... | fair input/data/compute/action matching | p. 5 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 4 (V. EXPERIMENTAL RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 6 / VI. LIMITATIONS - extractive body cue:** This limitation stems from the difficulty in accurately reconstructing such tiny particles using Gaussian splatting, which struggles to maintain precision at smaller scales.
- **p. 6 / VII. CONCLUSION - extractive body cue:** Future work could extend this framework to other non-rigid materials, further enhancing the capabilities of robotic systems in dynamic tasks.

## Why Read It

Manipulation, contact, tactile, and dexterity의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, these models often underperform compared to linear dynamics models due to a lack of inductive biases.를 문제로 두고, We form the node features of the GNN as (ci t,σi t ,Ri t,gi t,si t) for node vi t. f consists of node encoder fenc with node representation ¯vi from vi ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (IV. OUR APPROACH), p. 3 (IV. OUR APPROACH) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
