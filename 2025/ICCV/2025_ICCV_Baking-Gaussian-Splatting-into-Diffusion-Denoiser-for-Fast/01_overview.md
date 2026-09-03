# Baking Gaussian Splatting into Diffusion Denoiser for Fast and Scalable Single-stage Image-to-3D Generation and Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Cai_Baking_Gaussian_Splatting_into_Diffusion_Denoiser_for_Fast_and_Scalable_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Cai_Baking_Gaussian_Splatting_into_Diffusion_Denoiser_for_Fast_and_Scalable_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, Gaussian Splatting, Diffusion
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Cai_Baking_Gaussian_Splatting_into_Diffusion_Denoiser_for_Fast_and_Scalable_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Cai_Baking_Gaussian_Splatting_into_Diffusion_Denoiser_for_Fast_and_Scalable_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Without 3D model in the diffusion, these methods cannot enforce view consistency and easily collapse when the prompt view direction changes.를 문제로 두고, Our contributions can be summarized as follows: • We propose a novel framework, DiffusionGS, for 3D object generation and scene reconstruction from single view. • We design a scene-object mixed training strategy ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Existing feedforward image-to-3D methods mainly rely on 2D multi-view diffusion models that cannot guarantee 3D consistency.
- **p. 1 / Abstract - extractive body cue:** These methods easily collapse when changing the prompt view direction and mainly handle object-centric cases.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose a novel single-stage 3D diffusion model, DiffusionGS, for object generation and scene reconstruction from a single view.
- **p. 1 / Abstract - extractive body cue:** DiffusionGS directly outputs 3D Gaussian point clouds at each timestep to enforce view consistency and allow the model to generate robustly given prompt views of ...
- **p. 1 / Abstract - extractive body cue:** Plus, to improve the capability and generality of DiffusionGS, we scale up 3D training data by developing a scene-object mixed training strategy.
- **p. 2 / 1. Introduction - extractive body cue:** Without 3D model in the diffusion, these methods cannot enforce view consistency and easily collapse when the prompt view direction changes.
- **p. 3 / 1. Introduction - extractive body cue:** In particular, we notice previous camera conditioning method Pl¨ucker coordinate [54] shows limitations in capturing depth and 3D geometry.

## Core Idea

- **p. 3 / 1. Introduction - extractive body cue:** Our contributions can be summarized as follows: • We propose a novel framework, DiffusionGS, for 3D object generation and scene reconstruction from single view. • ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these issues, we propose a novel single-stage 3D Gaussian Splatting (3DGS) [27] based diffusion model, DiffusionGS, for 3D object generation and scene reconstruction ...
- **p. 2 / 1. Introduction - extractive body cue:** Thus, our method can better perceive the geometry to reconstruct the scene without using depth estimator.
- **p. 3 / 3. Method - extractive body cue:** 4 depicts the pipeline of our method.
- **p. 4 / 3.1. DiffusionGS - extractive body cue:** 4 (b), the input images concatenated with the viewpoint conditions are patchified, linearly projected, and then concatenated with a positional embedding to derive the input ...
- **p. 5 / 3.1. DiffusionGS - extractive body cue:** Then we use the weighted sum, controlled by λ, of L2 loss and VGG-19 [61] perceptual loss LVGG between the multi-view predicted images ˆ X(0,t) ...
- **p. 6 / 3.2. Scene-Object Mixed Training Strategy - extractive body cue:** Then the overall training objective L is \sma l l \m a thcal {L} = (\m a thcal {L}_{ d e} + \mathcal {L}_{nv}) \cdot ...
- **p. 6 / 3.2. Scene-Object Mixed Training Strategy - extractive body cue:** As the depth range varies across object- and scene-level datasets, we use two MLPs to decode the Gaussian primitives for objects and scenes in mixed ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | One clean image and relative poses are input for inference. | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (3.1. DiffusionGS), p. 4 (3.1. DiffusionGS) |
| State/latent | One, clean, image, relative, poses, input, inference, images, concatenated, viewpoint, conditions, patchified | geometry, map, object/relationship state | p. 5 (3.1. DiffusionGS), p. 4 (3.1. DiffusionGS), p. 5 (3.2. Scene-Object Mixed Training Strategy) |
| Output/action | 4 (b), the input images concatenated with the viewpoint conditions are patchified, linearly projected, and then concatenated with a positional embedding to derive the input tokens of the Transformer backbone, which consists ... | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.1. DiffusionGS), p. 5 (3.2. Scene-Object Mixed Training Strategy), p. 7 (Method) |
| Objective/outcome | (a) When selecting the data for our scene-object mixed training, we impose two angle constraints on the positions and orientations of viewpoint vectors to guarantee the training convergence. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.1. DiffusionGS), p. 5 (3.2. Scene-Object Mixed Training Strategy), p. 5 (3.2. Scene-Object Mixed Training Strategy) |

## Main Claims and Actual Contribution

- **p. 3 / 1. Introduction - extractive body cue:** Our contributions can be summarized as follows: • We propose a novel framework, DiffusionGS, for 3D object generation and scene reconstruction from single view. • ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these issues, we propose a novel single-stage 3D Gaussian Splatting (3DGS) [27] based diffusion model, DiffusionGS, for 3D object generation and scene reconstruction ...
- **p. 2 / 1. Introduction - extractive body cue:** Thus, our method can better perceive the geometry to reconstruct the scene without using depth estimator.
- **p. 3 / 3. Method - extractive body cue:** 4 depicts the pipeline of our method.
- **p. 4 / 3.1. DiffusionGS - extractive body cue:** 4 (b), the input images concatenated with the viewpoint conditions are patchified, linearly projected, and then concatenated with a positional embedding to derive the input ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Ablation study. Results on the GSO [13] dataset are listed. the highest score while enjoying over 5× and 10× infer- ence speed compared ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Single-view object generation (upper) and scene reconstruction (lower) results of our method. For single-view object generation, the prompt views are shown in the ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Single-view object generation results of our method on GSO [13], wild images, and text-to-images prompted by stable diffusion or FLUX. Our DiffusionGS can ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 1 (Figure/Table caption) |
| Embodiment/environment | Then we finetune the model on the object- and scene-level datasets with 64 A100 GPUs for 80K and 54K iterations at the per-GPU batch size of 8 and 16. | hardware/simulator version and reset protocol | p. 6 (4. Experiment), p. 6 (4. Experiment) |
| Dataset/benchmark | Then we finetune the model on the object- and scene-level datasets with 64 A100 GPUs for 80K and 54K iterations at the per-GPU batch size of 8 and 16. | role, split, size and leakage | p. 6 (4. Experiment), p. 6 (4. Experiment) |
| Metric | Figure 6. Visual comparison of single-view object generation on ABO, GSO, real-camera image, and text-to-image prompted by FLUX. Our method can generate more fine-grained details with accurate geometry. DiffSplat is based on ... | definition, denominator, direction and uncertainty | p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (4. Experiment) |
| Baseline/ablation | Table 2. Ablation study. Results on the GSO [13] dataset are listed. the highest score while enjoying over 5× and 10× infer- ence speed compared to the SOTA 3D diffusion DMV3D and ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Single-view scene reconstruction of our method on indoor and outdoor scenes. The depth maps are rendered by GS point clouds. DiffusionGS to both ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7. Visual results of single-view scene reconstruction. We train the feedforward methods with the same scene data for fairness. Previous methods yield blurry images ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Single-view object generation (upper) and scene reconstruction (lower) results of our method. For single-view object generation, the prompt views are shown in the ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Single-view object generation results of our method on GSO [13], wild images, and text-to-images prompted by stable diffusion or FLUX. Our DiffusionGS can ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. Pipeline. (a) When selecting the data for our scene-object mixed training, we impose two angle constraints on the positions and orientations of viewpoint ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 9. Visual analysis. (a) studies the effect of mixed training. (b) shows generation diversity. (c) shows the comparison with MIDI [22]. and black spots ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Without 3D model in the diffusion, these methods cannot enforce view consistency and easily collapse when the prompt view direction changes.를 문제로 두고, Our contributions can be summarized as follows: • We propose a novel framework, DiffusionGS, for 3D object generation and scene reconstruction from single view. • We design a scene-object mixed training strategy ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 3 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 4 (3.1. DiffusionGS), p. 5 (3.1. DiffusionGS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
