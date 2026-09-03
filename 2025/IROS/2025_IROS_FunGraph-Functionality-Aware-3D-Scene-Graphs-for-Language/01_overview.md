# FunGraph: Functionality Aware 3D Scene Graphs for Language-Prompted Scene Interaction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2503.07909.
> PDF retrieval source: https://arxiv.org/pdf/2503.07909. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / IROS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, Graph Reasoning
- Official paper: https://arxiv.org/abs/2503.07909
- Full-text retrieval: https://arxiv.org/pdf/2503.07909
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 One of the key challenges in modeling intra-object relationships is accurately perceiving functional object parts.를 문제로 두고, 3 provides an overview of our method.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The concept of 3D scene graphs is increasingly recognized as a powerful semantic and hierarchical representation of the environment.
- **p. 1 / Abstract - extractive body cue:** Current approaches often address this at a coarse, object-level resolution.
- **p. 1 / Abstract - extractive body cue:** In contrast, our goal is to develop a representation that enables robots to directly interact with their environment by identifying both the location of functional ...
- **p. 1 / Abstract - extractive body cue:** To achieve this, we focus on detecting and storing objects at a finer resolution, focusing on affordance-relevant parts.
- **p. 1 / Abstract - extractive body cue:** The primary challenge lies in the scarcity of data that extends beyond instance-level detection and the inherent difficulty of capturing detailed object features using robotic ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** One of the key challenges in modeling intra-object relationships is accurately perceiving functional object parts.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address this challenge, we utilize SceneFun3D [5], a large-scale dataset that provides sensory data and 3D annotations for functional interactive elements in household environments.

## Core Idea

- **p. 3 / III. METHOD - extractive body cue:** 3 provides an overview of our method.
- **p. 3 / III. METHOD - extractive body cue:** The input to the proposed method consists of a series of RGB-D observations, I = {I1, I2, . . . , IN}, and corresponding camera ...
- **p. 4 / III. METHOD - extractive body cue:** Overview of our functionality-aware 3D scene graph generation pipeline, which consists of three stages: (1) Detection, where instance segmentation and feature extraction are performed to ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Specifically, our contributions are: • A method to detect functional interactive elements from images, predict their affordances, and assign contextualized descriptions. • A framework, FunGraph, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Therefore, our approach involves generating 2D data for detector fine-tuning and analyzing its impact in 3D.
- **p. 5 / III. METHOD - extractive body cue:** As a general-purpose semantic segmentation model we use SAM2 [14], and as VLM GPT-4o [43].
- **p. 4 / III. METHOD - extractive body cue:** After each successful merge, the point cloud of node n is denoised using DBSCAN and downsampled to reduce redundancy, and then the semantic features are ...
- **p. 4 / III. METHOD - extractive body cue:** Each object is associated with a label c[i] j and semantic features f [i] j extracted using the CLIP model from the bounding-box cropped image.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The input to the proposed method consists of a series of RGB-D observations, I = {I1, I2, . . . , IN}, and corresponding camera poses, P = {P 1, P 2, ... | camera/depth stream, pose, map와 language goal | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| State/latent | input, consists, series, RGB-D, observations, corresponding, camera, poses, Because, cm-resolution, LiDARs, detailed | robot pose, free-space/semantic map와 local goal | p. 3 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Output/action | Because cm-resolution LiDARs are not detailed enough and mm-resolution 3D scanners are cost-prohibitive in many robotic applications, we assume a collection of registered RGB-D observations as input and propose to detect functional ... | collision-free trajectory 또는 velocity command | p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 2 (III. METHOD) |
| Objective/outcome | Because cm-resolution LiDARs are not detailed enough and mm-resolution 3D scanners are cost-prohibitive in many robotic applications, we assume a collection of registered RGB-D observations as input and propose to detect functional ... | goal reach, safety, localization error와 replanning latency | p. 3 (III. METHOD), p. 4 (III. METHOD) |

## Main Claims and Actual Contribution

- **p. 3 / III. METHOD - extractive body cue:** 3 provides an overview of our method.
- **p. 3 / III. METHOD - extractive body cue:** The input to the proposed method consists of a series of RGB-D observations, I = {I1, I2, . . . , IN}, and corresponding camera ...
- **p. 4 / III. METHOD - extractive body cue:** Overview of our functionality-aware 3D scene graph generation pipeline, which consists of three stages: (1) Detection, where instance segmentation and feature extraction are performed to ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Specifically, our contributions are: • A method to detect functional interactive elements from images, predict their affordances, and assign contextualized descriptions. • A framework, FunGraph, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Therefore, our approach involves generating 2D data for detector fine-tuning and analyzing its impact in 3D.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Given that the measured performance on the different splits of the same datasets are in a similar range, we carefully conclude that our proposed method ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** The results, however, show that the return of ConceptGraphs is still less accurate, indicating that the inclusion of functional elements and object-part relations in the ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** To achieve this, we convert our 3D scene graph representation into a JSON format, retaining information about each node's ID, 3D center of mass, 3D ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Embodiment/environment | The train-validation split of the dataset is 80/20, with the split ensuring that train and validation images come from different scenes. | hardware/simulator version and reset protocol | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Dataset/benchmark | Given that the measured performance on the different splits of the same datasets are in a similar range, we carefully conclude that our proposed method achieves similar results to SOTA approaches that ... | role, split, size and leakage | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Metric | Another source of error is not directly related to the method: indeed, the poses P provided in the dataset [5] are not always accurate, generating artifacts in the merging process and penalizing ... | definition, denominator, direction and uncertainty | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Baseline/ablation | As a baseline, we run YOLO-Worldv8.2 [40] and Grounding Dino [41] in a zero-shot fashion. | fair input/data/compute/action matching | p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / VI. CONCLUSIONS - extractive body cue:** It does not rely on segmenting a pre-existing highquality point cloud, which makes it also suitable for robotics applications with affordable RGB-D sensing.
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4. Illustration of our context-based label refinement. The VLM is queried to contextualize functional elements with their associated parent objects. The handle on the ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** As is evident from the numbers, ConceptGraphs does not account for the
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We note that the exact numerical results are difficult to compare, as [5] does not release either the model checkpoints or the full train/test split.

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 One of the key challenges in modeling intra-object relationships is accurately perceiving functional object parts.를 문제로 두고, 3 provides an overview of our method.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 5 (III. METHOD), p. 4 (III. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
