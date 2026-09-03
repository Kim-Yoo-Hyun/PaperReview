# Lift, Splat, Shoot: Encoding Images from Arbitrary Camera Rigs by Implicitly Unprojecting to 3D

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2008.05711.
> PDF retrieval source: https://arxiv.org/pdf/2008.05711. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, BEV, sensor fusion, camera
- Official paper: https://arxiv.org/abs/2008.05711
- Full-text retrieval: https://arxiv.org/pdf/2008.05711
- Code/Project: https://github.com/nv-tlabs/lift-splat-shoot
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 As a result, the model cannot learn in a data-driven way what the best way is to fuse information across cameras.를 문제로 두고, In this section, we present our approach for learning bird's-eye-view representations of scenes from image data captured by an arbitrary camera rig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 2 / 1 Introduction - extractive body cue:** Computer vision algorithms generally take as input an image and output either a prediction that is coordinate-frame agnostic - such as in classification [19,30,16,17] - ...
- **p. 2 / 1 Introduction - extractive body cue:** This paradigm does not match the setting for perception in self-driving outof-the-box.
- **p. 2 / 1 Introduction - extractive body cue:** In self-driving, multiple sensors are given as input, each with a different coordinate frame, and perception models are ultimately tasked with producing predictions in a ...
- **p. 2 / 1 Introduction - extractive body cue:** There are many simple, practical strategies for extending the single-image paradigm to the multi-view setting.
- **p. 2 / 1 Introduction - extractive body cue:** For instance, for the problem of 3D object detection from n cameras, one can apply a single-image detector to all input images individually, then rotate ...
- **p. 2 / 1 Introduction - extractive body cue:** As a result, the model cannot learn in a data-driven way what the best way is to fuse information across cameras.
- **p. 2 / 1 Introduction - extractive body cue:** It also means backpropagation cannot be used to automatically improve the perception system using feedback from the downstream planner.

## Core Idea

- **p. 4 / 3 Method - extractive body cue:** In this section, we present our approach for learning bird's-eye-view representations of scenes from image data captured by an arbitrary camera rig.
- **p. 2 / 1 Introduction - extractive body cue:** We propose a model named "Lift-Splat" that preserves the 3 symmetries identified above by design while also being end-to-end differentiable.
- **p. 2 / 1 Introduction - extractive body cue:** In Section 3.3, we propose a method for "shooting" proposal trajectories into this reference plane for interpretable end-to-end motion planning.
- **p. 3 / 1 Introduction - extractive body cue:** We present empirical evidence in Sec 5 that our model learns an effective mechanism for fusing information from a distribution of possible inputs.
- **p. 6 / 3 Method - extractive body cue:** 3.3 Shoot: Motion Planning Key aspect of our Lift-Splat model is that it enables end-to-end cost map learning for motion planning from camera-only input.
- **p. 5 / 3 Method - extractive body cue:** 3.1 Lift: Latent Depth Distribution The first stage of our model operates on each image in the camera rig in isolation.
- **p. 7 / 3 Method - extractive body cue:** For labels, given a ground-truth trajectory, we compute the nearest neighbor in L2 distance to the template trajectories T then train with the cross entropy ...
- **p. 8 / 3 Method - extractive body cue:** The "cumulative sum trick" is the observation that sum pooling can be performed by sorting all points according to bin id, performing a cumulative sum ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Computer vision algorithms generally take as input an image and output either a prediction that is coordinate-frame agnostic - such as in classification [19,30,16,17] - or a prediction in the same coordinate ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| State/latent | Computer, vision, algorithms, generally, take, input, image, output, either, prediction, coordinate-frame, agnostic | geometry, map, object/relationship state | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (3 Method) |
| Output/action | An equivalent way to state this property is that the definition of the ego-frame can be rotated/translated and the output will rotate/translate with it. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1 Introduction), p. 5 (3 Method), p. 6 (3 Method) |
| Objective/outcome | This definition of p(τi/o) enables us to learn an interpretable spatial cost function without defining a hard-margin loss as in NMP [41]. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 7 (3 Method), p. 7 (3 Method), p. 6 (3 Method) |

## Main Claims and Actual Contribution

- **p. 4 / 3 Method - extractive body cue:** In this section, we present our approach for learning bird's-eye-view representations of scenes from image data captured by an arbitrary camera rig.
- **p. 2 / 1 Introduction - extractive body cue:** We propose a model named "Lift-Splat" that preserves the 3 symmetries identified above by design while also being end-to-end differentiable.
- **p. 2 / 1 Introduction - extractive body cue:** In Section 3.3, we propose a method for "shooting" proposal trajectories into this reference plane for interpretable end-to-end motion planning.
- **p. 3 / 1 Introduction - extractive body cue:** We present empirical evidence in Sec 5 that our model learns an effective mechanism for fusing information from a distribution of possible inputs.
- **p. 6 / 3 Method - extractive body cue:** 3.3 Shoot: Motion Planning Key aspect of our Lift-Splat model is that it enables end-to-end cost map learning for motion planning from camera-only input.
- **p. 10 / Figure/Table caption - extractive body cue:** Table 2: Map IOU in BEV frame 5.2 Segmentation We demonstrate that our Lift-Splat model is able to learn semantic 3D repre- sentations given supervision ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: We visualize the "lift" step of our model. For each pixel, we predict a categorical distribution over depth α ∈△D-1 (left) and a ...
- **p. 11 / 6 DOF localization and rasterize - extractive body cue:** In Table 3, we show that the performance of our model for car segmentation improves when additional cameras are available at test time without any ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 10 (Figure/Table caption), p. 4 (Figure/Table caption) |
| Embodiment/environment | 5 Experiments and Results We use the nuScenes [2] and Lyft Level 5 [13] datasets to evaluate our approach. nuScenes is a large dataset of point cloud data and image data from ... | hardware/simulator version and reset protocol | p. 8 (3 Method), p. 10 (6 DOF localization and rasterize) |
| Dataset/benchmark | IOU 4 26.53 4 + 1fl 27.35 4 + 1bl 27.27 4 + 1bl + 1fl 27.94 Table 3: We train on images from only 4 of the 6 cameras in the ... | role, split, size and leakage | p. 8 (3 Method), p. 10 (6 DOF localization and rasterize), p. 11 (6 DOF localization and rasterize), p. 12 (6 DOF localization and rasterize) |
| Metric | Table 2: Map IOU in BEV frame 5.2 Segmentation We demonstrate that our Lift-Splat model is able to learn semantic 3D repre- sentations given supervision in the bird's-eye-view frame. Results on the ... | definition, denominator, direction and uncertainty | p. 10 (Figure/Table caption), p. 10 (6 DOF localization and rasterize), p. 6 (3 Method) |
| Baseline/ablation | We outperform these baselines on all tasks, as shown in Tables 1 and 2. | fair input/data/compute/action matching | p. 9 (6 DOF localization and rasterize), p. 10 (6 DOF localization and rasterize), p. 13 (6 DOF localization and rasterize) |

## Explicit Limitations and Failure Boundary

- **p. 14 / 6 Conclusion - extractive body cue:** We present methods for training our model that make the network robust to simple models of calibration noise.
- **p. 14 / 6 Conclusion - extractive body cue:** Our model does not have access to the speed of the car so it is compelling that the model predicts low-speed trajectories near crosswalks and ...
- **p. 10 / 6 DOF localization and rasterize - extractive body cue:** 5.3 Robustness Because the bird's-eye-view CNN learns from data how to fuse information across cameras, we can train the model to be robust to simple ...
- **p. 11 / 6 DOF localization and rasterize - extractive body cue:** On the left, we show that by training with a large amount of noise in the extrinsics (blue), the network becomes more robust to extrinsic ...
- **p. 9 / 6 DOF localization and rasterize - extractive body cue:** The Lyft dataset does not come with a canonical train/val split.
- **p. 9 / 6 DOF localization and rasterize - extractive body cue:** We follow an architecture similar to MonoLayout [21] which also trains a CNN to output bird's-eye-view labels from images only but does not leverage inductive ...
- **p. 10 / 6 DOF localization and rasterize - extractive body cue:** For high amounts of extrinsic noise, our model sustains its good performance.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 As a result, the model cannot learn in a data-driven way what the best way is to fuse information across cameras.를 문제로 두고, In this section, we present our approach for learning bird's-eye-view representations of scenes from image data captured by an arbitrary camera rig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 6 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
