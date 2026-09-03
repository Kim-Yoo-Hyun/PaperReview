# GS-LRM: Large Reconstruction Model for 3D Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3212_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03212.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3212_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03212.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Reconstructing a 3D scene from image captures is both a central problem and a long-standing challenge in computer vision.를 문제로 두고, In this section, we present the technical details of our method, including the architecture of our transformer-based model (Sec.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** Reconstructing a 3D scene from image captures is both a central problem and a long-standing challenge in computer vision.
- **p. 1 / 1 Introduction - extractive body cue:** Traditionally, high-quality 3D reconstruction relies on complex photogrammetry systems [23, 48,50] and requires a dense set of multi-view images.
- **p. 1 / 1 Introduction - extractive body cue:** Recent advancements in neural representations and differentiable rendering [9, 30, 40, 41] have shown superior reconstruction and rendering quality, by optimizing renderings on a per-scene ...
- **p. 1 / 1 Introduction - extractive body cue:** However, these methods are slow and still require a large number of input views.
- **p. 1 / 1 Introduction - extractive body cue:** Recently, transformer-based 3D large reconstruction models (LRMs) have been proposed, learning general 3D reconstruction priors from vast collections of 3D objects and achieving sparse-view 3D ...
- **p. 1 / 1 Introduction - extractive body cue:** This leads to challenges in training and rendering speeds, preserving fine details, and scaling to large scenes beyond object-centric inputs. *

## Core Idea

- **p. 4 / 3 Method - extractive body cue:** In this section, we present the technical details of our method, including the architecture of our transformer-based model (Sec.
- **p. 2 / 1 Introduction - extractive body cue:** To this end, we propose GS-LRM, a novel transformer-based large reconstruction model that predicts 3D Gaussian primitives [30] from sparse input images, enabling fast and ...
- **p. 5 / 3 Method - extractive body cue:** 2) and consists of Pre-LayerNorm [3], multi-head Self-Attention [60] and MLP.
- **p. 2 / 1 Introduction - extractive body cue:** The core of our approach is a simple and scalable transformer-based network architecture that predicts per-pixel Gaussians.
- **p. 6 / 3 Method - extractive body cue:** This property allows us to better handle high-frequency details in the inputs and large-scale scene captures.
- **p. 6 / 3 Method - extractive body cue:** We empirically find that the perceptual loss in [14] based on VGG-19 network [53] provides a more stable training than LPIPS [73] used in [27,32,61,66], ...
- **p. 4 / 3 Method - extractive body cue:** Multi-view image tokens are then concatenated and passed through a sequence of transformer blocks consisting of self-attention and MLP layers.
- **p. 5 / 3 Method - extractive body cue:** GS-LRM: Large Reconstruction Model for 3D Gaussian Splatting 5 Per-pixel Gaussians Transformer Block (×𝐿) MLP + Self-Att + Linear & Unpatchify Merged Gaussians Image + ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Unlike previous LRMs that require careful designs of additional (triplane) NeRF tokens for reconstruction, we align input (2D images) and output (3D Gaussians) in the same pixel space, predicting one Gaussian per ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1 Introduction), p. 6 (3 Method) |
| State/latent | Unlike, previous, LRMs, require, careful, designs, additional, triplane, NeRF, tokens, reconstruction, align | geometry, map, object/relationship state | p. 2 (1 Introduction), p. 6 (3 Method), p. 4 (3 Method) |
| Output/action | The final output of our model is simply the merge of 3D Gaussians from all N input views. | point map, pose, scene graph, affordance 또는 query result | p. 6 (3 Method), p. 4 (3 Method), p. 2 (1 Introduction) |
| Objective/outcome | 3.2 Loss Functions During training, we render the images at the M supervision views using the predicted Gaussian splats, and minimize the image reconstruction loss. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (3 Method), p. 6 (3 Method) |

## Main Claims and Actual Contribution

- **p. 4 / 3 Method - extractive body cue:** In this section, we present the technical details of our method, including the architecture of our transformer-based model (Sec.
- **p. 2 / 1 Introduction - extractive body cue:** To this end, we propose GS-LRM, a novel transformer-based large reconstruction model that predicts 3D Gaussian primitives [30] from sparse input images, enabling fast and ...
- **p. 5 / 3 Method - extractive body cue:** 2) and consists of Pre-LayerNorm [3], multi-head Self-Attention [60] and MLP.
- **p. 2 / 1 Introduction - extractive body cue:** The core of our approach is a simple and scalable transformer-based network architecture that predicts per-pixel Gaussians.
- **p. 6 / 3 Method - extractive body cue:** This property allows us to better handle high-frequency details in the inputs and large-scale scene captures.
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 5: We compare scene-level GS-LRM with the best-performing baseline pixel- Splat [8]. We can observe that our model is better in sharpness (leftmost column), ...
- **p. 10 / 4 Experiments - extractive body cue:** 1, our approach achieves the best quantitative results on the RealEstate10k
- **p. 7 / 4 Experiments - extractive body cue:** We outperform relevant baselines by a large margin in both scenarios.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 10 (Figure/Table caption), p. 10 (4 Experiments) |
| Embodiment/environment | We follow the standard training/testing split for the dataset, which is also used in pixelSplat [8]. | hardware/simulator version and reset protocol | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Dataset/benchmark | In this section, we first describe the training and testing datasets (Sec. | role, split, size and leakage | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 6 (4 Experiments), p. 10 (4 Experiments) |
| Metric | The dataset contains 80K video clips curated from 10K YouTube videos. | definition, denominator, direction and uncertainty | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments) |
| Baseline/ablation | We outperform relevant baselines by a large margin in both scenarios. | fair input/data/compute/action matching | p. 7 (4 Experiments), p. 9 (4 Experiments), p. 11 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 13 / 4 Experiments - extractive body cue:** 4.6 Limitations Although our method shows high-quality reconstruction results from posed sparse images, there are still a few limitations to be addressed in future work.
- **p. 14 / 5 Conclusion - extractive body cue:** We hope that our work can inspire more future work in the space of data-driven feed-forward 3D reconstruction.
- **p. 8 / 4 Experiments - extractive body cue:** The Triplane-LRM cannot reconstruct high-frequency details (top left and top right) and thin structures (bottom left) well.
- **p. 14 / 4 Experiments - extractive body cue:** Please refer to our project page for the video and interactive rendering results. the view frustum, which means that unseen regions cannot be reconstructed.
- **p. 9 / 4 Experiments - extractive body cue:** We also tried to compare against another baseline SparseNeuS [36]; however, we found that it failed to produce plausible reconstructions given 4 highly sparse inputs; ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Reconstructing a 3D scene from image captures is both a central problem and a long-standing challenge in computer vision.를 문제로 두고, In this section, we present the technical details of our method, including the architecture of our transformer-based model (Sec.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 6 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 4 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
