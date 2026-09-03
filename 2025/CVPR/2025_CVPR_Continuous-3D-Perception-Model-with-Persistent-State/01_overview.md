# Continuous 3D Perception Model with Persistent State

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2501.12387.
> PDF retrieval source: https://arxiv.org/pdf/2501.12387. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D reconstruction, SLAM, representation
- Official paper: https://arxiv.org/abs/2501.12387
- Full-text retrieval: https://arxiv.org/pdf/2501.12387
- Code/Project: https://cut3r.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 The learned prior enables our method to address challenges encountered by traditional methods (e.g., dynamic objects, sparse observations, degenerate camera motion), while the ability to continuously update allows it to process new ...를 문제로 두고, The learned prior enables our method to address challenges encountered by traditional methods (e.g., dynamic objects, sparse observations, degenerate camera motion), while the ability to continuously update allows it to process new ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present a unified framework capable of solving a broad range of 3D tasks.
- **p. 1 / Abstract - extractive body cue:** Our approach features a stateful recurrent model that continuously updates its state representation with each new observation.
- **p. 1 / Abstract - extractive body cue:** Given a stream of images, this evolving state can be used to generate metric-scale pointmaps (per-pixel 3D points) for each new input in an online ...
- **p. 1 / Abstract - extractive body cue:** These pointmaps reside within a common coordinate system, and can be accumulated into a coherent, dense scene reconstruction that updates as new images arrive.
- **p. 1 / Abstract - extractive body cue:** Our model, called CUT3R (Continuous Updating Transformer for 3D Reconstruction), captures rich priors of real-world scenes: not only can it predict accurate pointmaps from image ...
- **p. 1 / 1. Introduction - extractive body cue:** The learned prior enables our method to address challenges encountered by traditional methods (e.g., dynamic objects, sparse observations, degenerate camera motion), while the ability to ...
- **p. 1 / 1. Introduction - extractive body cue:** We achieve these capabilities by integrating data-driven priors with a recurrent update mechanism.

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** The learned prior enables our method to address challenges encountered by traditional methods (e.g., dynamic objects, sparse observations, degenerate camera motion), while the ability to ...
- **p. 2 / 1. Introduction - extractive body cue:** Our framework is designed to be general and flexible, making it well-suited for training on an extensive collection of datasets and adaptable to diverse inference ...
- **p. 1 / 1. Introduction - extractive body cue:** Building on these insights, we introduce an online 3D perception framework that unifies three key capabilities: 1) reconstructing 3D scenes from few observations, 2) continuously ...
- **p. 2 / 1. Introduction - extractive body cue:** We also show that our method can infer previously unseen structures and continuously refine the reconstruction as new observations arrive.
- **p. 3 / 3.1. State-Input Interaction Mechanism - extractive body cue:** Our method takes a stream of images as input.
- **p. 5 / 3.4. Training Strategy - extractive body cue:** We use a ViT-Large model [22] for the image encoder Encoderi, initialized with DUSt3R encoder pretrained weights, and ViT-Base for the decoders.
- **p. 4 / 3.2. Querying the State with Unseen Views - extractive body cue:** Given a query raymap R, we first encode it into token representations Fr using a separate transformer Encoderr: Fr = Encoderr(R).
- **p. 3 / 3. Method - extractive body cue:** As a new image comes in through the model, it interacts with the latent state representation, which encodes the understanding of the current 3D scene.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Following the state-image interaction, explicit 3D pointmaps and camera poses are extracted for each view. | camera/depth stream, pose, map와 language goal | p. 3 (3. Method), p. 3 (3.1. State-Input Interaction Mechanism) |
| State/latent | Following, state-image, interaction, explicit, pointmaps, camera, poses, extracted, view, denotes, image, tokens | robot pose, free-space/semantic map와 local goal | p. 3 (3. Method), p. 3 (3.1. State-Input Interaction Mechanism), p. 4 (3.1. State-Input Interaction Mechanism) |
| Output/action | F ′ t denotes the image tokens enriched with state information. z is a learnable "pose token" prepended to the image tokens, whose output z′ t captures image-level information related to the ... | collision-free trajectory 또는 velocity command | p. 3 (3.1. State-Input Interaction Mechanism), p. 4 (3.1. State-Input Interaction Mechanism), p. 4 (3.2. Querying the State with Unseen Views) |
| Objective/outcome | These two stages are trained on 224×224 images to reduce computational costs, following DUSt3R [107]. | goal reach, safety, localization error와 replanning latency | p. 5 (3.4. Training Strategy), p. 5 (3.3. Training Objective), p. 3 (3.1. State-Input Interaction Mechanism) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** The learned prior enables our method to address challenges encountered by traditional methods (e.g., dynamic objects, sparse observations, degenerate camera motion), while the ability to ...
- **p. 2 / 1. Introduction - extractive body cue:** Our framework is designed to be general and flexible, making it well-suited for training on an extensive collection of datasets and adaptable to diverse inference ...
- **p. 1 / 1. Introduction - extractive body cue:** Building on these insights, we introduce an online 3D perception framework that unifies three key capabilities: 1) reconstructing 3D scenes from few observations, 2) continuously ...
- **p. 2 / 1. Introduction - extractive body cue:** We also show that our method can infer previously unseen structures and continuously refine the reconstruction as new observations arrive.
- **p. 3 / 3.1. State-Input Interaction Mechanism - extractive body cue:** Our method takes a stream of images as input.
- **p. 7 / 4.3. 3D Reconstruction - extractive body cue:** Our method significantly outperforms the other online approach Spann3R [101], and achieves comparable or sometimes better results than the top optimization-based method, DUSt3RGA, while operating ...
- **p. 6 / 4.1. Monocular and Video Depth Estimation - extractive body cue:** Our method achieves the best overall performance among all online methods. global alignment they use assumes that the scene is static, and enforcing multi-view consistency ...
- **p. 8 / 4.4. Analysis - extractive body cue:** 5, revisiting improves performance compared to the online version, especially for accuracy.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 7 (4.3. 3D Reconstruction), p. 6 (4.1. Monocular and Video Depth Estimation) |
| Embodiment/environment | For this experiment, we use the validation set of the MapFree [3] and ARKitScenes datasets, both with metric camera pose annotations. | hardware/simulator version and reset protocol | p. 8 (4.4. Analysis), p. 5 (4.1. Monocular and Video Depth Estimation) |
| Dataset/benchmark | MonST3R finetunes DUSt3R on dynamic datasets to handle dynamic scenes, while Spann3R extends DUSt3R to support varying number of images via additional spatial memory and operates online, similar to our method. | role, split, size and leakage | p. 8 (4.4. Analysis), p. 5 (4.1. Monocular and Video Depth Estimation), p. 5 (4. Experiments), p. 6 (4.3. 3D Reconstruction) |
| Metric | We evaluate scene-level reconstruction on the 7-scenes [83] and NRGBD [4] datasets using accuracy (Acc), completion (Comp), and normal consistency (NC) metrics, as in prior works [4, 101, 102, 107, 132]. | definition, denominator, direction and uncertainty | p. 6 (4.3. 3D Reconstruction), p. 8 (4.4. Analysis), p. 5 (4.1. Monocular and Video Depth Estimation) |
| Baseline/ablation | We present a subset of baselines here; please refer to the supplementary material for full comparisons. | fair input/data/compute/action matching | p. 6 (4.1. Monocular and Video Depth Estimation), p. 5 (4.1. Monocular and Video Depth Estimation), p. 5 (4.1. Monocular and Video Depth Estimation) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4.2. Camera Pose Estimation - extractive body cue:** Unlike most visual odometry methods [17, 34, 96], our method does not require any camera calibration.
- **p. 6 / 4.2. Camera Pose Estimation - extractive body cue:** Most prior approaches do so through test-time optimization, as seen in RobustCVD [47] and CasualSAM [128], which jointly estimate camera parameters and dense depth maps ...
- **p. 16 / Figure/Table caption - extractive body cue:** Table 6. Training Datasets. We provide more details of our training datasets. We classify a dataset as dynamic if annotations exist for moving objects like ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 The learned prior enables our method to address challenges encountered by traditional methods (e.g., dynamic objects, sparse observations, degenerate camera motion), while the ability to continuously update allows it to process new ...를 문제로 두고, The learned prior enables our method to address challenges encountered by traditional methods (e.g., dynamic objects, sparse observations, degenerate camera motion), while the ability to continuously update allows it to process new ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.4. Training Strategy), p. 4 (3.2. Querying the State with Unseen Views) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
