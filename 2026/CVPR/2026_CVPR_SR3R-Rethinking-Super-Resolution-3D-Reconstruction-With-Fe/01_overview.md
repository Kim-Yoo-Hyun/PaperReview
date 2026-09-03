# SR3R: Rethinking Super-Resolution 3D Reconstruction With Feed-Forward Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Feng_SR3R_Rethinking_Super-Resolution_3D_Reconstruction_With_Feed-Forward_Gaussian_Splatting_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_SR3R_Rethinking_Super-Resolution_3D_Reconstruction_With_Feed-Forward_Gaussian_Splatting_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Feng_SR3R_Rethinking_Super-Resolution_3D_Reconstruction_With_Feed-Forward_Gaussian_Splatting_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_SR3R_Rethinking_Super-Resolution_3D_Reconstruction_With_Feed-Forward_Gaussian_Splatting_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This prevents leveraging large-scale cross-scene data to learn 3D-specific SR priors and to train a generalized 3DSR model, thereby inherently limiting reconstruction fidelity, cross-scene generalization, and real-time usage.를 문제로 두고, The main contributions are as follows. • A novel formulation of 3DSR.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D super-resolution (3DSR) aims to reconstruct highresolution (HR) 3D scenes from low-resolution (LR) multiview images.
- **p. 1 / Abstract - extractive body cue:** Existing methods rely on dense LR inputs and per-scene optimization, which restricts the highfrequency priors for constructing HR 3D Gaussian Splatting (3DGS) to those inherited ...
- **p. 1 / Abstract - extractive body cue:** This severely limits reconstruction fidelity, cross-scene generalization, and real-time usability.
- **p. 1 / Abstract - extractive body cue:** We propose to reformulate 3DSR as a direct feedforward mapping from sparse LR views to HR 3DGS representations, enabling the model to autonomously learn 3D-specific ...
- **p. 1 / Abstract - extractive body cue:** This fundamentally changes how 3DSR acquires high-frequency knowledge and enables robust generalization to unseen scenes.
- **p. 2 / 1. Introduction - extractive body cue:** Although this strategy injects high-frequency cues into the HR 3DGS reconstruction, it suffers from several fundamental limitations.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** This removes the reliance on 2DSR pseudo-supervision, allows learning from large-scale multiscene data, and enables cross-scene generalization, substantially improving scalability and efficiency.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** The main contributions are as follows. • A novel formulation of 3DSR.
- **p. 2 / 1. Introduction - extractive body cue:** We propose SR3R, a feed-forward framework that directly reconstructs HR 3DGS from as few as two LR views through a learned mapping network.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** This removes the reliance on 2DSR pseudo-supervision, allows learning from large-scale multiscene data, and enables cross-scene generalization, substantially improving scalability and efficiency.
- **p. 4 / 3.2. Overall Framework - extractive body cue:** The LR input images are upsampled to the target resolution and processed by our mapping network, which consists of a ViT encoder, a feature refinement ...
- **p. 4 / 3.4. LR Image to HR 3DGS Mapping - extractive body cue:** To correct these unreliable 2D features, we introduce a feature refinement module that aligns the encoder tokens ten ∈RN×C with geometry-aware tokens tpre ∈RN×C extracted ...
- **p. 4 / 3.4. LR Image to HR 3DGS Mapping - extractive body cue:** It adopts a transformer-based architecture composed of a ViT encoder, a feature refinement module, a ViT decoder, and a Gaussian offset learning module.
- **p. 5 / 3.4. LR Image to HR 3DGS Mapping - extractive body cue:** The two attention outputs Uo←p and Up←o are then concatenated and fused through a fully connected layer to generate the refined feature token tca.
- **p. 5 / 3.4. LR Image to HR 3DGS Mapping - extractive body cue:** The decoded features are then provided to the Gaussian offset learning module (Section 3.5) to estimate residual corrections from the densified representation GDense to the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | This task has become increasingly critical because state-of-the-art 3D Gaussian Splatting (3DGS)-based reconstruction methods [14, 25] typically require dense and high-resolution input views to recover fine geometric and appearance details. | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| State/latent | task, become, increasingly, critical, because, state-of-the-art, Gaussian, Splatting, DGS, reconstruction, methods, typically | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation) |
| Output/action | Current 3DSR methods [9, 15, 24, 40] typically employ pretrained 2D image or video super-resolution (2DSR) models to generate pseudo-HR images from dense multiview LR inputs, which are then used as supervision ... | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 4 (3.4. LR Image to HR 3DGS Mapping) |
| Objective/outcome | Following [38], we adopt a combination of pixel-wise reconstruction loss (MSE) and perceptual consistency loss (LPIPS) to jointly preserve geometric accuracy and visual fidelity. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (3.6. Training Objective), p. 3 (3.1. Problem Formulation) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** The main contributions are as follows. • A novel formulation of 3DSR.
- **p. 2 / 1. Introduction - extractive body cue:** We propose SR3R, a feed-forward framework that directly reconstructs HR 3DGS from as few as two LR views through a learned mapping network.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** This removes the reliance on 2DSR pseudo-supervision, allows learning from large-scale multiscene data, and enables cross-scene generalization, substantially improving scalability and efficiency.
- **p. 4 / 3.2. Overall Framework - extractive body cue:** The LR input images are upsampled to the target resolution and processed by our mapping network, which consists of a ViT encoder, a feature refinement ...
- **p. 4 / 3.4. LR Image to HR 3DGS Mapping - extractive body cue:** To correct these unreliable 2D features, we introduce a feature refinement module that aligns the encoder tokens ten ∈RN×C with geometry-aware tokens tpre ∈RN×C extracted ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Component-wise ablation on RE10K (4× 3DSR). Modules are added cumulatively to the NoPoSplat baseline. Each component improves performance, and Gaussian Offset Learning yields ...
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Offset w/o PTv3), it significantly improves reconstruction quality while reducing the number of learnable Gaussian parameters, demonstrating its efficiency.
- **p. 7 / 4.3. Zero-Shot Generalization - extractive body cue:** As shown in Table 2, SR3R achieves substantially higher accuracy than all feed-forward baselines in the zero-shot 33390

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 8 (4.4. Ablation Study) |
| Embodiment/environment | We further evaluate the zero-shot generalization ability of SR3R on the DTU dataset, a challenging object-centric benchmark with unseen geometries and illumination conditions. | hardware/simulator version and reset protocol | p. 7 (4.3. Zero-Shot Generalization), p. 6 (4.1. Experimental Setup) |
| Dataset/benchmark | RE10K and ACID are two large-scale datasets, containing indoor real estate walkthrough videos and outdoor natural scenes captured by aerial drones, respectively. | role, split, size and leakage | p. 7 (4.3. Zero-Shot Generalization), p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 8 (4.3. Zero-Shot Generalization) |
| Metric | Adding PointTransformerV3 further boosts accuracy through multi-scale spatial reasoning, producing the full SR3R model with the best performance. | definition, denominator, direction and uncertainty | p. 8 (4.4. Ablation Study), p. 7 (4.3. Zero-Shot Generalization), p. 6 (4.1. Experimental Setup) |
| Baseline/ablation | Table 1. Quantitative comparison of 4× 3DSR on the large-scale RE10K and ACID datasets. SR3R consistently and substantially outperforms all baselines and their upscaled-input versions across PSNR, SSIM, and LPIPS, with only ... | fair input/data/compute/action matching | p. 6 (Figure/Table caption), p. 7 (4.3. Zero-Shot Generalization), p. 7 (4.3. Zero-Shot Generalization) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.2. Comparison with State-of-the-Art - extractive body cue:** These improvements hold for both 3DGS backbones, confirming that our offsetbased refinement and cross-view fusion effectively restore 3D-specific high-frequency structures that 2D upsampling and direct ...
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Applying 2D upsampling reduces excessive softness but still fails to recover reliable high-frequency structures, often introducing ambiguous or hallucinated textures.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Notably, even Bilinear interpolation already surpasses all feed-forward baselines (Table 1), indicating that SR3R does not depend on a particular upsampling design.
- **p. 7 / 4.2. Comparison with State-of-the-Art - extractive body cue:** These results highlight the advantage of learning Gaussian offsets over direct parameter regression, enabling more accurate high-frequency recovery under sparse LR inputs.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This prevents leveraging large-scale cross-scene data to learn 3D-specific SR priors and to train a generalized 3DSR model, thereby inherently limiting reconstruction fidelity, cross-scene generalization, and real-time usage.를 문제로 두고, The main contributions are as follows. • A novel formulation of 3DSR.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation), p. 4 (3.2. Overall Framework), p. 4 (3.4. LR Image to HR 3DGS Mapping) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
