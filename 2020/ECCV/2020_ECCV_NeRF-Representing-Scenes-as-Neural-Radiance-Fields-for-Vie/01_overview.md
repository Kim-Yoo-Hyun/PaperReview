# NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2003.08934.
> PDF retrieval source: https://arxiv.org/pdf/2003.08934. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: NeRF, 3D reconstruction, representation
- Official paper: https://arxiv.org/abs/2003.08934
- Full-text retrieval: https://arxiv.org/pdf/2003.08934
- Code/Project: https://github.com/bmild/nerf
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 In this work, we address the long-standing problem of view synthesis in a new way by directly optimizing parameters of a continuous 5D scene representation to minimize the error of rendering a ...를 문제로 두고, We address these issues by transforming input 5D coordinates with a positional encoding that enables the MLP to represent higher frequency functions, and we propose a hierarchical sampling procedure to reduce the ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** In this work, we address the long-standing problem of view synthesis in a new way by directly optimizing parameters of a continuous 5D scene representation ...
- **p. 1 / 1 Introduction - extractive body cue:** We represent a static scene as a continuous 5D function that outputs the radiance emitted in each direction (θ, φ) at each point (x, y, ...
- **p. 1 / 1 Introduction - extractive body cue:** Our method optimizes a deep fully-connected neural network without any convolutional layers (often referred to as a multilayer perceptron or MLP) to represent this function ...
- **p. 1 / 1 Introduction - extractive body cue:** To render this neural radiance field (NeRF) ⋆.
- **p. 2 / 1 Introduction - extractive body cue:** Input Images Optimize NeRF Render new views Fig.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** We address these issues by transforming input 5D coordinates with a positional encoding that enables the MLP to represent higher frequency functions, and we propose ...
- **p. 1 / 1 Introduction - extractive body cue:** Our method optimizes a deep fully-connected neural network without any convolutional layers (often referred to as a multilayer perceptron or MLP) to represent this function ...
- **p. 2 / 1 Introduction - extractive body cue:** Crucially, our method overcomes the prohibitive storage costs of discretized voxel grids when modeling complex scenes at high-resolutions.
- **p. 17 / A Additional Implementation Details - extractive body cue:** Volume Bounds Our method renders views by querying the neural radiance field representation at continuous 5D coordinates along camera rays.
- **p. 3 / 1 Introduction - extractive body cue:** As far as we know, this paper presents the first continuous neural scene representation that is able to render high-resolution photorealistic novel views of real ...
- **p. 17 / A Additional Implementation Details - extractive body cue:** Training Details For real scene data, we regularize our network by adding random Gaussian noise with zero mean and unit variance to the output σ ...
- **p. 18 / A Additional Implementation Details - extractive body cue:** An additional layer outputs the volume density σ (which is rectified using a ReLU to ensure that the output volume density is nonnegative) and a ...
- **p. 18 / A Additional Implementation Details - extractive body cue:** A final layer (with a sigmoid activation) outputs the emitted RGB radiance at position x, as viewed by a ray with direction d. dataset requires ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Here, we visualize the set of 100 input views of the synthetic Drums scene randomly captured on a surrounding hemisphere, and we show two novel views rendered from our optimized NeRF representation. ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1 Introduction), p. 18 (A Additional Implementation Details) |
| State/latent | Here, visualize, input, views, synthetic, Drums, scene, randomly, captured, surrounding, hemisphere, novel | geometry, map, object/relationship state | p. 2 (1 Introduction), p. 18 (A Additional Implementation Details), p. 2 (1 Introduction) |
| Output/action | Input vectors are shown in green, intermediate hidden layers are shown in blue, output vectors are shown in red, and the number inside each block signifies the vector's dimension. | point map, pose, scene graph, affordance 또는 query result | p. 18 (A Additional Implementation Details), p. 2 (1 Introduction), p. 14 (9) Complete Model) |
| Objective/outcome | Training Details For real scene data, we regularize our network by adding random Gaussian noise with zero mean and unit variance to the output σ values (before passing them through the ReLU) ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 17 (A Additional Implementation Details) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** We address these issues by transforming input 5D coordinates with a positional encoding that enables the MLP to represent higher frequency functions, and we propose ...
- **p. 1 / 1 Introduction - extractive body cue:** Our method optimizes a deep fully-connected neural network without any convolutional layers (often referred to as a multilayer perceptron or MLP) to represent this function ...
- **p. 2 / 1 Introduction - extractive body cue:** Crucially, our method overcomes the prohibitive storage costs of discretized voxel grids when modeling complex scenes at high-resolutions.
- **p. 17 / A Additional Implementation Details - extractive body cue:** Volume Bounds Our method renders views by querying the neural radiance field representation at continuous 5D coordinates along camera rays.
- **p. 3 / 1 Introduction - extractive body cue:** As far as we know, this paper presents the first continuous neural scene representation that is able to render high-resolution photorealistic novel views of real ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 1: Our method quantitatively outperforms prior work on datasets of both synthetic and real images. We report PSNR/SSIM (higher is better) and LPIPS [50] ...
- **p. 9 / 6 Results - extractive body cue:** 8 and 6) show that our method outperforms prior work, and provide extensive ablation studies to validate our design choices (Table 2).
- **p. 9 / 6 Results - extractive body cue:** We urge the reader to view our supplementary video to better appreciate our method's significant improvement over baseline methods when rendering smooth paths of novel ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 10 (Figure/Table caption), p. 9 (6 Results) |
| Embodiment/environment | This dataset consists of 8 scenes captured with a handheld cellphone (5 taken from the LLFF paper and 3 that we capture), captured with 20 to 62 images, and hold out 1/8 ... | hardware/simulator version and reset protocol | p. 10 (6 Results), p. 10 (6 Results) |
| Dataset/benchmark | 5: Comparisons on test-set views for scenes from our new synthetic dataset generated with a physically-based renderer. | role, split, size and leakage | p. 10 (6 Results), p. 10 (6 Results), p. 11 (6 Results), p. 18 (A Additional Implementation Details) |
| Metric | We additionally generate our own dataset containing pathtraced images of eight objects that exhibit complicated geometry and realistic non-Lambertian materials. | definition, denominator, direction and uncertainty | p. 9 (6 Results), p. 10 (6 Results), p. 10 (6 Results) |
| Baseline/ablation | We thoroughly outperform both baselines that also optimize a separate network per scene (NV and SRN) in all scenarios. | fair input/data/compute/action matching | p. 13 (6.3 Discussion), p. 9 (6 Results), p. 10 (6 Results) |

## Explicit Limitations and Failure Boundary

- **p. 14 / 7 Conclusion - extractive body cue:** Another direction for future work is interpretability: sampled representations such as voxel grids and meshes admit reasoning about the expected quality of rendered views and ...
- **p. 11 / 6 Results - extractive body cue:** Neural Volumes cannot capture the details on the Microphone's grille or Lego's gears, and it completely fails to recover the geometry of Ship's rigging.
- **p. 13 / 6.3 Discussion - extractive body cue:** LLFF specifically provides a "sampling guideline" to not exceed 64 pixels of disparity between input views, so it frequently fails to estimate correct geometry in ...
- **p. 10 / 6 Results - extractive body cue:** The real dataset consists of handheld forward-facing captures of 8 realworld scenes (NV cannot be evaluated on this data because it only reconstructs objects inside ...
- **p. 14 / Figure/Table caption - extractive body cue:** Table 2: An ablation study of our model. Metrics are averaged over the 8 scenes from our realistic synthetic dataset. See Sec. 6.4 for detailed ...
- **p. 23 / Figure/Table caption - extractive body cue:** Table 3: Per-scene quantitative results from the DeepVoxels [41] dataset. The "scenes" in this dataset are all diffuse objects with simple geometry, rendered from texture-mapped ...
- **p. 17 / A Additional Implementation Details - extractive body cue:** Training Details For real scene data, we regularize our network by adding random Gaussian noise with zero mean and unit variance to the output σ ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 In this work, we address the long-standing problem of view synthesis in a new way by directly optimizing parameters of a continuous 5D scene representation to minimize the error of rendering a ...를 문제로 두고, We address these issues by transforming input 5D coordinates with a positional encoding that enables the MLP to represent higher frequency functions, and we propose a hierarchical sampling procedure to reduce the ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 17 (A Additional Implementation Details), p. 18 (A Additional Implementation Details), p. 18 (A Additional Implementation Details), p. 14 (9) Complete Model), p. 17 (A Additional Implementation Details) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
