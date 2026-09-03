# UniDepth: Universal Monocular Metric Depth Estimation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2403.18913.
> PDF retrieval source: https://arxiv.org/pdf/2403.18913. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: depth, 3D Vision
- Official paper: https://arxiv.org/abs/2403.18913
- Full-text retrieval: https://arxiv.org/pdf/2403.18913
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, relying only on this single additional module clearly results in challenges related to training stability and scale ambiguity.를 문제로 두고, We introduce UniDepth, a novel approach that directly predicts 3D points in a scene with only one image as input.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Accurate monocular metric depth estimation (MMDE) is crucial to solving downstream tasks in 3D perception and modeling.
- **p. 1 / Abstract - extractive body cue:** However, the remarkable accuracy of recent MMDE methods is confined to their training domains.
- **p. 1 / Abstract - extractive body cue:** These methods fail to generalize to unseen domains even in the presence of moderate domain gaps, which hinders their practical applicability.
- **p. 1 / Abstract - extractive body cue:** We propose a new model, UniDepth, capable of reconstructing metric 3D scenes from solely single images across domains.
- **p. 1 / Abstract - extractive body cue:** Departing from the existing MMDE methods, UniDepth directly predicts metric 3D points from the input image at inference time without any additional information, striving for ...
- **p. 2 / 1. Introduction - extractive body cue:** However, relying only on this single additional module clearly results in challenges related to training stability and scale ambiguity.
- **p. 1 / 1. Introduction - extractive body cue:** Unlike existing methods, UniDepth delivers metric 3D predictions for any scene solely from a single image, waiving the need for extra information about scene or ...

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** We introduce UniDepth, a novel approach that directly predicts 3D points in a scene with only one image as input.
- **p. 2 / 1. Introduction - extractive body cue:** Additionally, we introduce a geometric invariance loss to enhance the robustness of depth estimation.
- **p. 2 / 1. Introduction - extractive body cue:** We propose an effective pseudo-spherical representation of the output space to disentangle the camera and depth dimensions of this space.
- **p. 4 / 3.3. Geometric Invariance Loss - extractive body cue:** To this end, we propose a geometric invariance loss to enforce the consistency of camera-prompted depth features of the same scene from different acquisition sensors.
- **p. 1 / 1. Introduction - extractive body cue:** Our approach, named UniDepth, is the first that attempts to solve this challenging task without restrictions on scene composition and setup and distinguishes itself through ...
- **p. 4 / 3.3. Geometric Invariance Loss - extractive body cue:** Otherwise, the loss would enforce consistency across features that inherently carry distinct camera information.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We introduce UniDepth, a novel approach that directly predicts 3D points in a scene with only one image as input. | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (1. Introduction), p. 1 (1. Introduction) |
| State/latent | introduce, UniDepth, novel, directly, predicts, points, scene, only, image, input, However, delivering | geometry, map, object/relationship state | p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | However, delivering reliable metric scaled depth outputs is necessary to perform 3D reconstruction effectively, thus motivating the challenging and inherently illposed task of Monocular Metric Depth Estimation (MMDE). | point map, pose, scene graph, affordance 또는 query result | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | The bi-directional loss can be computed as: 1 2(Lcon(D1/E1, D2/E2)+Lcon(D2/E2, D1/E1)). | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.3. Geometric Invariance Loss), p. 4 (3.3. Geometric Invariance Loss) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** We introduce UniDepth, a novel approach that directly predicts 3D points in a scene with only one image as input.
- **p. 2 / 1. Introduction - extractive body cue:** Additionally, we introduce a geometric invariance loss to enhance the robustness of depth estimation.
- **p. 2 / 1. Introduction - extractive body cue:** We propose an effective pseudo-spherical representation of the output space to disentangle the camera and depth dimensions of this space.
- **p. 4 / 3.3. Geometric Invariance Loss - extractive body cue:** To this end, we propose a geometric invariance loss to enforce the consistency of camera-prompted depth features of the same scene from different acquisition sensors.
- **p. 1 / 1. Introduction - extractive body cue:** Our approach, named UniDepth, is the first that attempts to solve this challenging task without restrictions on scene composition and setup and distinguishes itself through ...
- **p. 6 / 4.2. Comparison with the State of the Art - extractive body cue:** Importantly, the KITTI Depth Prediction Benchmark, which provides a perfectly fair evaluation, underscores the excellent zero-shot performance of our method and its robustness compared to ...
- **p. 6 / 4.2. Comparison with the State of the Art - extractive body cue:** Experiments show that not only is the performance preserved for most of the test sets, but UniDepth with the bootstrapped camera can also outperform models ...
- **p. 8 / 4.3. Ablation Study - extractive body cue:** This approach hurts generalization, as evidenced by ARelC in the out-of-domain evaluation, despite the slight improvement in in-domain ARelC.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4.2. Comparison with the State of the Art), p. 6 (4.2. Comparison with the State of the Art) |
| Embodiment/environment | The resulting dataset amounts roughly to 3M real-world images with different cameras and domains, compared to, e.g. | hardware/simulator version and reset protocol | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup) |
| Dataset/benchmark | Method δ0.5 δ1 FA A.Rel RMS RMSlog CD SIlog Higher is better Lower is better BTS [28] 86.9 96.2 82.0 5.63 2.43 0.089 0.42 8.18 AdaBins [3] 86.2 96.3 81.5 5.85 2.38 ... | role, split, size and leakage | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup), p. 6 (4.2. Comparison with the State of the Art), p. 8 (4.3. Ablation Study) |
| Metric | Importantly, the KITTI Depth Prediction Benchmark, which provides a perfectly fair evaluation, underscores the excellent zero-shot performance of our method and its robustness compared to the current MMDE SotA methods, as UniDepth ... | definition, denominator, direction and uncertainty | p. 6 (4.2. Comparison with the State of the Art), p. 5 (4.1. Experimental Setup), p. 8 (4.3. Ablation Study) |
| Baseline/ablation | The Oracle model demonstrates more robust scale-dependent performance during zero-shot testing compared to the Full model, highlighting how the proposed task is inherently more demanding. | fair input/data/compute/action matching | p. 7 (4.3. Ablation Study), p. 8 (Figure/Table caption), p. 6 (4.2. Comparison with the State of the Art) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4.3. Ablation Study - extractive body cue:** This limitation is underscored by the marked variability observed for test sets strongly out-of-distribution, such as KITTI, when comparing the utilization or absence of camera ...
- **p. 8 / 5. Conclusion - extractive body cue:** The designed self-prompting camera allows camera-free test time application and renders the model more robust against camera noise.
- **p. 6 / 4.2. Comparison with the State of the Art - extractive body cue:** This pitfall is demonstrated by the drop in scale-dependent metrics, e.g.
- **p. 6 / 4.2. Comparison with the State of the Art - extractive body cue:** Moreover, ZoeDepth, which has a capacity similar to our ViT-based approach and is pre-trained on the diverse MiDaS dataset [42], shows limitations in general zero-shot ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Impact of noise in camera intrinsics. The amount of relative distortion (εCAM(%)) of the intrinsics is shown on the x- axis, while δ0.5 ...
- **p. 7 / 4.3. Ablation Study - extractive body cue:** The Oracle model demonstrates more robust scale-dependent performance during zero-shot testing compared to the Full model, highlighting how the proposed task is inherently more demanding.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, relying only on this single additional module clearly results in challenges related to training stability and scale ambiguity.를 문제로 두고, We introduce UniDepth, a novel approach that directly predicts 3D points in a scene with only one image as input.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.3. Geometric Invariance Loss), p. 4 (3.3. Geometric Invariance Loss) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
