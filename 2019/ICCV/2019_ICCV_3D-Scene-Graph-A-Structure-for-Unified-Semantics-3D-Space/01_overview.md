# 3D Scene Graph: A Structure for Unified Semantics, 3D Space, and Camera

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1910.02527.
> PDF retrieval source: https://arxiv.org/pdf/1910.02527. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2019 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Scene Graph, semantic, geometry, Graph Reasoning
- Official paper: https://arxiv.org/abs/1910.02527
- Full-text retrieval: https://arxiv.org/pdf/1910.02527
- Code/Project: https://3dscenegraph.stanford.edu/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 This gives free computation for various attributes and relationships. • We propose a two-step robustification approach to optimizing semantic recognition using imperfect existing detectors, which allows the automation of a mainly manual ...를 문제로 두고, The input to our method is the typical output of 3D scanners and consists of 3D mesh models, registered RGB panoramas and the corresponding camera parameters, such as the data in Matterport3D ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** A comprehensive semantic understanding of a scene is important for many applications - but in what space should diverse semantic information (e.g., objects, scene categories, ...
- **p. 1 / Abstract - extractive body cue:** Aspiring to have one unified structure that hosts diverse types of semantics, we follow the Scene Graph paradigm in 3D, generating a 3D Scene Graph.
- **p. 1 / Abstract - extractive body cue:** Given a 3D mesh and registered panoramic images, we construct a graph that spans the entire building and includes semantics on objects (e.g., class, material, ...
- **p. 1 / Abstract - extractive body cue:** However, this process is prohibitively labor heavy if done manually.
- **p. 1 / Abstract - extractive body cue:** To alleviate this we devise a semi-automatic framework that employs existing detection methods and enhances them using two main constraints: I. framing of query images ...
- **p. 2 / 1. Introduction - extractive body cue:** This gives free computation for various attributes and relationships. • We propose a two-step robustification approach to optimizing semantic recognition using imperfect existing detectors, which ...

## Core Idea

- **p. 4 / 3. 3D Scene Graph Structure - extractive body cue:** The input to our method is the typical output of 3D scanners and consists of 3D mesh models, registered RGB panoramas and the corresponding camera ...
- **p. 2 / 1. Introduction - extractive body cue:** This gives free computation for various attributes and relationships. • We propose a two-step robustification approach to optimizing semantic recognition using imperfect existing detectors, which ...
- **p. 1 / 1. Introduction - extractive body cue:** 3D Scene Graph: It consists of 4 layers, that represent semantics, 3D space and camera.
- **p. 2 / 1. Introduction - extractive body cue:** The contributions of this paper can be summarized as: • We extend the scene graph idea in [27] to 3D space and ground semantic information ...
- **p. 3 / C S1 - extractive body cue:** The Gibson database [44], consists of several hundreds of 3D mesh models with registered panoramic images.
- **p. 4 / 4. Constructing the 3D Scene Graph - extractive body cue:** In our experiments (Section 5), we used the best reported performing Mask RCNN network [18] and got results only for detections with a confidence score ...
- **p. 2 / 1. Introduction - extractive body cue:** To construct the 3D Scene Graph, we combine stateof-the-art algorithms in a mainly automatic approach to semantic recognition.
- **p. 1 / Abstract - extractive body cue:** To alleviate this we devise a semi-automatic framework that employs existing detection methods and enhances them using two main constraints: I. framing of query images ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The input to our method is the typical output of 3D scanners and consists of 3D mesh models, registered RGB panoramas and the corresponding camera parameters, such as the data in Matterport3D ... | camera/depth stream, pose, map와 language goal | p. 4 (3. 3D Scene Graph Structure), p. 5 (4. Constructing the 3D Scene Graph) |
| State/latent | input, typical, output, scanners, consists, mesh, models, registered, RGB, panoramas, corresponding, camera | robot pose, free-space/semantic map와 local goal | p. 4 (3. 3D Scene Graph Structure), p. 5 (4. Constructing the 3D Scene Graph), p. 2 (1. Introduction) |
| Output/action | To aggregate the casted votes, we formulate a weighted majority voting scheme based on how close an observation point is to a surface, following the heuristic that the closer the background chair ... | collision-free trajectory 또는 velocity command | p. 5 (4. Constructing the 3D Scene Graph), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | To alleviate this we devise a semi-automatic framework that employs existing detection methods and enhances them using two main constraints: I. framing of query images sampled on panoramas to maximize the performance ... | goal reach, safety, localization error와 replanning latency | p. 1 (Abstract), p. 4 (4. Constructing the 3D Scene Graph), p. 3 (C S1) |

## Main Claims and Actual Contribution

- **p. 4 / 3. 3D Scene Graph Structure - extractive body cue:** The input to our method is the typical output of 3D scanners and consists of 3D mesh models, registered RGB panoramas and the corresponding camera ...
- **p. 2 / 1. Introduction - extractive body cue:** This gives free computation for various attributes and relationships. • We propose a two-step robustification approach to optimizing semantic recognition using imperfect existing detectors, which ...
- **p. 1 / 1. Introduction - extractive body cue:** 3D Scene Graph: It consists of 4 layers, that represent semantics, 3D space and camera.
- **p. 2 / 1. Introduction - extractive body cue:** The contributions of this paper can be summarized as: • We extend the scene graph idea in [27] to 3D space and ground semantic information ...
- **p. 3 / C S1 - extractive body cue:** The Gibson database [44], consists of several hundreds of 3D mesh models with registered panoramic images.
- **p. 7 / 5.2. Evaluation of Automated Pipeline - extractive body cue:** Similar improvements can be seen in the case of 3D (Figure 7).
- **p. 6 / 5.2. Evaluation of Automated Pipeline - extractive body cue:** The panorama results are obtained after applying both robustification mechanisms.
- **p. 6 / 5.2. Evaluation of Automated Pipeline - extractive body cue:** And these in 3D: • Mask R-CNN [18] and Pano Projection: The panorama results of Mask R-CNN are projected on the 3D mesh surfaces with ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (5.2. Evaluation of Automated Pipeline), p. 6 (5.2. Evaluation of Automated Pipeline) |
| Embodiment/environment | The semantic categories used come from the COCO dataset [33] for objects, MINC [8] for materials, and DTD [12] for textures. | hardware/simulator version and reset protocol | p. 6 (5.1. Dataset Statistics), p. 6 (5.2. Evaluation of Automated Pipeline) |
| Dataset/benchmark | To this end, we perform another set of experiments using BlitzNet [15], a network with faster inference but worse reported performance on the COCO dataset (AP 34.1). | role, split, size and leakage | p. 6 (5.1. Dataset Statistics), p. 6 (5.2. Evaluation of Automated Pipeline), p. 7 (5.2. Evaluation of Automated Pipeline), p. 8 (5.3. 2D Scene Graph Prediction) |
| Metric | This suggests that the robustification mechanisms can provide similar value in increasing the performance of standard detectors and correct errors, regardless of initial predictions. | definition, denominator, direction and uncertainty | p. 7 (5.2. Evaluation of Automated Pipeline), p. 8 (5.3. 2D Scene Graph Prediction), p. 7 (5.2. Evaluation of Automated Pipeline) |
| Baseline/ablation | Baselines: We compare the following approaches in 2D: • Mask R-CNN [18]: We run Mask R-CNN on 6 rectilinear images sampled on the panorama with no overlap. | fair input/data/compute/action matching | p. 6 (5.2. Evaluation of Automated Pipeline), p. 7 (5.2. Evaluation of Automated Pipeline), p. 7 (5.2. Evaluation of Automated Pipeline) |

## Explicit Limitations and Failure Boundary

- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. Semantic statistics for bed: (a) Number of object instances in buildings. (b) Distribution of its surface coverage. (c) Nearest object instance in 3D ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. 3D Scene Graph: It consists of 4 layers, that represent semantics, 3D space and camera. Elements are nodes in the graph and have ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Framing: Examples of sampled rectilinear images using the framing robustification mechanism are shown in the dashed colored boxes. Detections (b) on individual frames ...
- **p. 6 / 5.2. Evaluation of Automated Pipeline - extractive body cue:** The panorama results are obtained after applying both robustification mechanisms.
- **p. 7 / 5.2. Evaluation of Automated Pipeline - extractive body cue:** We want to further understand the behavior of the two robustification mechanisms when using a less accurate detector.
- **p. 7 / 5.2. Evaluation of Automated Pipeline - extractive body cue:** This suggests that the robustification mechanisms can provide similar value in increasing the performance of standard detectors and correct errors, regardless of initial predictions.
- **p. 8 / 5.3. 2D Scene Graph Prediction - extractive body cue:** We focus on relationship classification and provide results on: (a) spatial order and (b) relative volume classification, as well as on (c) amodal mask segmentation ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 This gives free computation for various attributes and relationships. • We propose a two-step robustification approach to optimizing semantic recognition using imperfect existing detectors, which allows the automation of a mainly manual ...를 문제로 두고, The input to our method is the typical output of 3D scanners and consists of 3D mesh models, registered RGB panoramas and the corresponding camera parameters, such as the data in Matterport3D ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 3 (C S1), p. 4 (4. Constructing the 3D Scene Graph), p. 4 (3. 3D Scene Graph Structure), p. 2 (1. Introduction), p. 1 (Abstract) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
