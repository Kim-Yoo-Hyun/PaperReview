# ActiveGS: Active Scene Reconstruction using Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2412.17769.
> PDF retrieval source: https://arxiv.org/pdf/2412.17769. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RA-L
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting
- Official paper: https://arxiv.org/abs/2412.17769
- Full-text retrieval: https://arxiv.org/pdf/2412.17769
- Code/Project: https://github.com/dmar-bonn/active-gs
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, this is difficult without ground truth information at novel viewpoints.를 문제로 두고, We introduce ActiveGS, a novel framework for active scene reconstruction using GS for autonomous robotic tasks.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robotics applications often rely on scene reconstructions to enable downstream tasks.
- **p. 1 / Abstract - extractive body cue:** In this work, we tackle the challenge of actively building an accurate map of an unknown scene using an RGB-D camera on a mobile platform.
- **p. 1 / Abstract - extractive body cue:** We propose a hybrid map representation that combines a Gaussian splatting map with a coarse voxel map, leveraging the strengths of both representations: the high-fidelity ...
- **p. 1 / Abstract - extractive body cue:** At the core of our framework is an effective confidence modelling technique for the Gaussian splatting map to identify under-reconstructed areas, while utilising spatial information ...
- **p. 1 / Abstract - extractive body cue:** By actively collecting scene information in under-reconstructed and unexplored areas for map updates, our approach achieves superior Gaussian splatting reconstruction results compared to state-of-the-art approaches.
- **p. 2 / A CTIVE exploration and reconstruction of unknown - extractive body cue:** However, this is difficult without ground truth information at novel viewpoints.
- **p. 2 / A CTIVE exploration and reconstruction of unknown - extractive body cue:** Incorporating GS into an active scene reconstruction pipeline presents significant challenges.

## Core Idea

- **p. 3 / III. OUR APPROACH - extractive body cue:** We introduce ActiveGS, a novel framework for active scene reconstruction using GS for autonomous robotic tasks.
- **p. 3 / III. OUR APPROACH - extractive body cue:** An overview of our framework is shown in Fig.
- **p. 4 / III. OUR APPROACH - extractive body cue:** A candidate viewpoint pc i ∈R5 is defined by its 3D position, yaw, and pitch angles in our framework.
- **p. 4 / III. OUR APPROACH - extractive body cue:** To address this, we introduce additional candidate viewpoints based on regions of interest (ROI) defined in the voxel map.
- **p. 1 / Body text (section not recovered) - extractive body cue:** By integrating confidence modelling into the Gaussian splatting pipeline, our approach enables targeted view planning to build a high-fidelity Gaussian splatting map.
- **p. 4 / III. OUR APPROACH - extractive body cue:** The normal loss Ln = Dcos(N, eN) + TV (N) consists of the cosine distance Dcos between the rendered normal map and the normal map ...
- **p. 2 / A CTIVE exploration and reconstruction of unknown - extractive body cue:** To tackle the first challenge, we propose a simple yet effective confidence modelling technique for Gaussian primitives based on viewpoint distribution, enabling view planning for ...
- **p. 3 / III. OUR APPROACH - extractive body cue:** To actively guide view planning to reconstruct the scene in a targeted manner, we propose using our confidence modelling technique in the GS map and ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given posed RGB-D measurements as input, we update a coarse voxel map to model the spatial occupancy and incrementally train a GS map for high-fidelity scene reconstruction. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (III. OUR APPROACH), p. 3 (III. OUR APPROACH) |
| State/latent | Given, posed, RGB-D, measurements, input, update, coarse, voxel, model, spatial, occupancy, incrementally | geometry, map, object/relationship state | p. 3 (III. OUR APPROACH), p. 3 (III. OUR APPROACH), p. 4 (III. OUR APPROACH) |
| Output/action | Our GS map is based on Gaussian surfel [4], a state-ofthe-art 2D GS representation. | point map, pose, scene graph, affordance 또는 query result | p. 3 (III. OUR APPROACH), p. 4 (III. OUR APPROACH), p. 4 (III. OUR APPROACH) |
| Objective/outcome | While these approaches demonstrate promising results, the rather costly volumetric rendering procedure during online incremental mapping poses limitations for NeRF-based active scene reconstruction. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 2 (A CTIVE exploration and reconstruction of unknown), p. 3 (III. OUR APPROACH), p. 4 (III. OUR APPROACH) |

## Main Claims and Actual Contribution

- **p. 3 / III. OUR APPROACH - extractive body cue:** We introduce ActiveGS, a novel framework for active scene reconstruction using GS for autonomous robotic tasks.
- **p. 3 / III. OUR APPROACH - extractive body cue:** An overview of our framework is shown in Fig.
- **p. 4 / III. OUR APPROACH - extractive body cue:** A candidate viewpoint pc i ∈R5 is defined by its 3D position, yaw, and pitch angles in our framework.
- **p. 4 / III. OUR APPROACH - extractive body cue:** To address this, we introduce additional candidate viewpoints based on regions of interest (ROI) defined in the voxel map.
- **p. 1 / Body text (section not recovered) - extractive body cue:** By integrating confidence modelling into the Gaussian splatting pipeline, our approach enables targeted view planning to build a high-fidelity Gaussian splatting map.
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** Our approach achieves the best performance in both rendering and mesh quality across all test scenes, supporting our first claim that it outperforms state-of-the-art NeRF ...
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** Our experimental results support our three claims: (i) we show that our ActiveGS framework outperforms state-of-theart NeRF-based and GS-based active scene reconstruction methods; (ii) we ...
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** We consider ROI-based sampling to achieve targeted candidate viewpoint generation as described in Sec.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION) |
| Embodiment/environment | Our experimental results support our three claims: (i) we show that our ActiveGS framework outperforms state-of-theart NeRF-based and GS-based active scene reconstruction methods; (ii) we show that our confidence modelling of Gaussian ... | hardware/simulator version and reset protocol | p. 5 (IV. EXPERIMENTAL EVALUATION), p. 7 (IV. EXPERIMENTAL EVALUATION) |
| Dataset/benchmark | We conduct our simulation experiments using the Habitat simulator [29] and the Replica dataset [33]. | role, split, size and leakage | p. 5 (IV. EXPERIMENTAL EVALUATION), p. 7 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 7 (IV. EXPERIMENTAL EVALUATION) |
| Metric | The ablation study comparing Ours and Ours (w/o ROI) demonstrates the benefits of ROI-based sampling for targeted inspection, reflected by higher means and smaller standard deviations in both evaluation metrics. | definition, denominator, direction and uncertainty | p. 7 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION) |
| Baseline/ablation | Our ActiveGS outperforms baselines in all test scenes. | fair input/data/compute/action matching | p. 6 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION) |

## Explicit Limitations and Failure Boundary

- **p. 7 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** Unlike simulation experiments, we do not account for the pitch angle of viewpoints in this experiment due to control limitations.
- **p. 7 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** Given the limited on-board resources, we run ActiveGS on our desktop PC, where it receives RGB-D and pose data from the UAV for map updates ...
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** The camera has a depth sensing range of [0.1, 5.0] m and Gaussian noise in the depth measurements with linearly increased standard deviation σ = ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, this is difficult without ground truth information at novel viewpoints.를 문제로 두고, We introduce ActiveGS, a novel framework for active scene reconstruction using GS for autonomous robotic tasks.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (A CTIVE exploration and reconstruction of unknown), p. 1 (Abstract), p. 2 (A CTIVE exploration and reconstruction of unknown), p. 1 (A CTIVE exploration and reconstruction of unknown), p. 3 (III. OUR APPROACH), p. 4 (III. OUR APPROACH) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
