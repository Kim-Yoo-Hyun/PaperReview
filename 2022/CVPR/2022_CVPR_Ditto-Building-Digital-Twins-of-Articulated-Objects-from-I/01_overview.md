# Ditto: Building Digital Twins of Articulated Objects from Interaction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2202.08227.
> PDF retrieval source: https://arxiv.org/pdf/2202.08227. Reading tracker status/evidence was not changed.

- Year/Venue: 2022 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: Robotics, 3D Vision, digital twin, articulated objects, interaction, implicit representation
- Official paper: https://arxiv.org/abs/2202.08227
- Full-text retrieval: https://arxiv.org/pdf/2202.08227
- Code/Project: https://ut-austin-rpl.github.io/Ditto/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, they infer part-level geometry on the point cloud which cannot be used for physical simulation, because physical simulation requires compact geometry of the object such as the mesh for collision computation.를 문제로 두고, Given visual observations before and after interaction, our method jointly reconstructs the part-level geometry and articulation model of the object.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Digitizing physical objects into the virtual world has the potential to unlock new research and applications in embodied AI and mixed reality.
- **p. 1 / Abstract - extractive body cue:** This work focuses on recreating interactive digital twins of real-world articulated objects, which can be directly imported into virtual environments.
- **p. 1 / Abstract - extractive body cue:** We introduce Ditto to learn articulation model estimation and 3D geometry reconstruction of an articulated object through interactive perception.
- **p. 1 / Abstract - extractive body cue:** Given a pair of visual observations of an articulated object before and after interaction, Ditto reconstructs part-level geometry and estimates the articulation model of the ...
- **p. 1 / Abstract - extractive body cue:** We employ implicit neural representations for joint geometry and articulation modeling.
- **p. 2 / 1. Introduction - extractive body cue:** However, they infer part-level geometry on the point cloud which cannot be used for physical simulation, because physical simulation requires compact geometry of the object ...
- **p. 1 / 1. Introduction - extractive body cue:** A promising path towards closing the reality gap is digitizing physical objects and recreating them in virtual environments.

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** Given visual observations before and after interaction, our method jointly reconstructs the part-level geometry and articulation model of the object.
- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we apply our method to real-world articulated objects for recreating digital twins.
- **p. 2 / 1. Introduction - extractive body cue:** We introduce Ditto (Digital twin of articulated objects), an implicit neural representation-based model that jointly predicts part-level geometry and kinematic articulation between the parts.
- **p. 3 / 4. Method - extractive body cue:** Ditto consists of a two-stream encoder that fuses two input point clouds and multiple implicit decoders for geometry and articulation.
- **p. 5 / 4.3. Training - extractive body cue:** Our method does not assume known joint types during inference.
- **p. 4 / 4.2. Implicit Decoders - extractive body cue:** First, we use an implicit decoder to predict joint type pjtype: \begin {a li gned } f_{\theta _\text {type}}(\mathbf {p}_\text {in}, \psi _{\mathbf {p}_\text {in}}^c) ...
- **p. 4 / 4.1. Two-Stream Encoder - extractive body cue:** Then we use two PointNet++ decoder νgeo and νart to propagate the fused subsampled point features into dense features aligned with the original points f_ ...
- **p. 5 / 4.3. Training - extractive body cue:** The loss for training consists of two parts: the geometry loss and the joint loss.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The input to our method is a pair of point cloud observations P1, P2 ∈RN×3 of the articulated object before and after an interaction. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3. Problem Formulation), p. 3 (3. Problem Formulation) |
| State/latent | input, pair, point, cloud, observations, articulated, object, before, after, interaction, study, problem | geometry, map, object/relationship state | p. 3 (3. Problem Formulation), p. 3 (3. Problem Formulation), p. 4 (4.2. Implicit Decoders) |
| Output/action | We study the problem of recreating interactive digital twins of articulated objects from a pair of sensory observations before and after an interaction. | point map, pose, scene graph, affordance 또는 query result | p. 3 (3. Problem Formulation), p. 4 (4.2. Implicit Decoders), p. 4 (4.2. Implicit Decoders) |
| Objective/outcome | For joint type prediction, we also apply the standard binary cross entropy loss. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (4.3. Training), p. 3 (4. Method), p. 5 (4.3. Training) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** Given visual observations before and after interaction, our method jointly reconstructs the part-level geometry and articulation model of the object.
- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we apply our method to real-world articulated objects for recreating digital twins.
- **p. 2 / 1. Introduction - extractive body cue:** We introduce Ditto (Digital twin of articulated objects), an implicit neural representation-based model that jointly predicts part-level geometry and kinematic articulation between the parts.
- **p. 3 / 4. Method - extractive body cue:** Ditto consists of a two-stream encoder that fuses two input point clouds and multiple implicit decoders for geometry and articulation.
- **p. 5 / 4.3. Training - extractive body cue:** Our method does not assume known joint types during inference.
- **p. 8 / 5.5. Ablation Studies - extractive body cue:** 1, Ditto achieves superior or at least on-par performance on all metrics.
- **p. 7 / 5.4. Articulated Object Reconstruction - extractive body cue:** On both datasets, Ditto gets significantly better results on all metrics compared with the baselines.
- **p. 7 / 5.4. Articulated Object Reconstruction - extractive body cue:** In contrast, Ditto achieves precise part-level geometry reconstruction as well as accurate joint estimation.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 8 (5.5. Ablation Studies), p. 7 (5.4. Articulated Object Reconstruction) |
| Embodiment/environment | Reconstructed unseen articulated objects in Shape2Motion [55] (top) and synthetic [1] (bottom) dataset. | hardware/simulator version and reset protocol | p. 7 (5.2. Baselines), p. 6 (5.1. Datasets) |
| Dataset/benchmark | We conduct experiments on two 3D articulated object datasets, the synthetic objects dataset provided by Abbatematteo et al. | role, split, size and leakage | p. 7 (5.2. Baselines), p. 6 (5.1. Datasets), p. 6 (5.1. Datasets), p. 8 (5.4. Articulated Object Reconstruction) |
| Metric | For the revolute joint, we also measure the axis position error (Pos Err) using the minimum distance between the predicted and ground truth rotation axis. | definition, denominator, direction and uncertainty | p. 7 (5.3. Evaluation Metrics), p. 8 (5.5. Ablation Studies), p. 7 (5.3. Evaluation Metrics) |
| Baseline/ablation | On both datasets, Ditto gets significantly better results on all metrics compared with the baselines. | fair input/data/compute/action matching | p. 7 (5.4. Articulated Object Reconstruction), p. 6 (5.2. Baselines), p. 6 (5.2. Baselines) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 5.4. Articulated Object Reconstruction - extractive body cue:** Failure of joint estimation also harms segmentation prediction because the joint parameter decoders and the segmentation decoder share the same feature planes.
- **p. 8 / 5.4. Articulated Object Reconstruction - extractive body cue:** 3, A-SDF fails to reconstruct the shape details of unseen objects, especially the objects with prismatic joints.
- **p. 8 / 5.5. Ablation Studies - extractive body cue:** We observe that using the same 3D and 2D features for geometry and articulation makes training unstable, and 2D features would harm the reconstruction due ...
- **p. 7 / 5.4. Articulated Object Reconstruction - extractive body cue:** In comparison, Ditto does not suffer from such a bottleneck as an end-to-end method.
- **p. 6 / 5.1. Datasets - extractive body cue:** Even though we use multi-view depth images, the point cloud may still be incomplete due to the self-occlusion of the objects.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, they infer part-level geometry on the point cloud which cannot be used for physical simulation, because physical simulation requires compact geometry of the object such as the mesh for collision computation.를 문제로 두고, Given visual observations before and after interaction, our method jointly reconstructs the part-level geometry and articulation model of the object.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (3. Problem Formulation), p. 4 (4.2. Implicit Decoders) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
