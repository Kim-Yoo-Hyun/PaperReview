# Triplane Meets Gaussian Splatting: Fast and Generalizable Single-View 3D Reconstruction with Transformers

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Zou_Triplane_Meets_Gaussian_Splatting_Fast_and_Generalizable_Single-View_3D_Reconstruction_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Zou_Triplane_Meets_Gaussian_Splatting_Fast_and_Generalizable_Single-View_3D_Reconstruction_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Zou_Triplane_Meets_Gaussian_Splatting_Fast_and_Generalizable_Single-View_3D_Reconstruction_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Zou_Triplane_Meets_Gaussian_Splatting_Fast_and_Generalizable_Single-View_3D_Reconstruction_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, the inherent ambiguity and lack of information in single images pose a substantial challenge in accurately recovering the complete, ∗Intern at VAST † Corresponding authors This CVPR paper is the Open ...를 문제로 두고, Our approach consists of two networks for reconstructing the point cloud and triplane from the input image, employing a fully transformer-based architecture for both.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent advancements in 3D reconstruction from single images have been driven by the evolution of generative models.
- **p. 1 / Abstract - extractive body cue:** Prominent among these are methods based on Score Distillation Sampling (SDS) and the adaptation of diffusion models in the 3D domain.
- **p. 1 / Abstract - extractive body cue:** Despite their progress, these techniques often face limitations due to slow optimization or rendering processes, leading to extensive training and optimization times.
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce a novel approach for single-view reconstruction that efficiently generates a 3D model from a single image via feedforward inference.
- **p. 1 / Abstract - extractive body cue:** Our method utilizes two transformerbased networks, namely a point decoder and a triplane decoder, to reconstruct 3D objects using a hybrid TriplaneGaussian intermediate representation.
- **p. 1 / 1. Introduction - extractive body cue:** However, the inherent ambiguity and lack of information in single images pose a substantial challenge in accurately recovering the complete, ∗Intern at VAST † Corresponding ...
- **p. 1 / 1. Introduction - extractive body cue:** Digitizing 3D objects from single 2D images represents a crucial and longstanding challenge in both computer vision and graphics, with wide applications in augmented reality ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our approach consists of two networks for reconstructing the point cloud and triplane from the input image, employing a fully transformer-based architecture for both.
- **p. 3 / 3. Method - extractive body cue:** In the subsequent sections, we present our approach for 3D object reconstruction from single-view images.
- **p. 2 / 1. Introduction - extractive body cue:** Our method employs a hybrid explicit-and-implicit 3D representation, facilitating fast and high-quality 3D reconstruction and novel view synthesis.
- **p. 3 / 3. Method - extractive body cue:** We introduce a new hybrid 3D representation that combines explicit point cloud geometry and implicit triplane features, allowing for efficient rendering without compromising on qual10326
- **p. 4 / 3.1. Hybrid Triplane-Gaussian - extractive body cue:** In response, we introduce TriplaneGaussian, a new hybrid 3D representation that merges the benefits of both triplane and point cloud approaches for 3D Gaussian representation.
- **p. 4 / 3. Method - extractive body cue:** In order to deduce the hybrid representation from a singe-view input, we first employ a transformerbased point cloud decoder to predict coarse points from image ...
- **p. 5 / 3.2. Reconstruction from Single-View Images - extractive body cue:** In our framework, we use a set of feature tokens {fi}p and {fi}t for the latent features of two different 3D representations, i.e., points and ...
- **p. 4 / 3. Method - extractive body cue:** Subsequently, a triplane decoder takes these points along with the image features and outputs the triplane features.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | This design enables interaction between latent features and input image features through cross-attention, ensuring scalability and supporting large-scale, category-agnostic training for enhanced real-world object generalizability Moreov ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 4 (3.1. Hybrid Triplane-Gaussian) |
| State/latent | design, enables, interaction, between, latent, features, input, image, through, cross-attention, ensuring, scalability | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 4 (3.1. Hybrid Triplane-Gaussian), p. 4 (3.2. Reconstruction from Single-View Images) |
| Output/action | Given an input camera pose π and a point cloud P, the local projection feature can be calculated by the projection function P, where fl = P(π, P). | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.1. Hybrid Triplane-Gaussian), p. 4 (3.2. Reconstruction from Single-View Images), p. 5 (3.2. Reconstruction from Single-View Images) |
| Objective/outcome | Specifically, we concatenate the triplane feature ft with projected local features fl from explicit geometry as f in Equation 1. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.1. Hybrid Triplane-Gaussian), p. 4 (3.1. Hybrid Triplane-Gaussian), p. 5 (3.3. Training) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our approach consists of two networks for reconstructing the point cloud and triplane from the input image, employing a fully transformer-based architecture for both.
- **p. 3 / 3. Method - extractive body cue:** In the subsequent sections, we present our approach for 3D object reconstruction from single-view images.
- **p. 2 / 1. Introduction - extractive body cue:** Our method employs a hybrid explicit-and-implicit 3D representation, facilitating fast and high-quality 3D reconstruction and novel view synthesis.
- **p. 3 / 3. Method - extractive body cue:** We introduce a new hybrid 3D representation that combines explicit point cloud geometry and implicit triplane features, allowing for efficient rendering without compromising on qual10326
- **p. 4 / 3.1. Hybrid Triplane-Gaussian - extractive body cue:** In response, we introduce TriplaneGaussian, a new hybrid 3D representation that merges the benefits of both triplane and point cloud approaches for 3D Gaussian representation.
- **p. 7 / 4.5. Runtime Efficiency - extractive body cue:** We can find that our method has achieved significant improvements in speed for both reconstruction and rendering processes compared to other baselines, benefiting from feed-forward ...
- **p. 7 / 4.6. Ablation Study - extractive body cue:** Our TriplaneGaussian, leveraging the projection-aware condition with explicit geometry, excels in producing more detailed texture compared to Triplane-NeRF, as illustrated in the red box of ...
- **p. 6 / 4.1. Implementation Details - extractive body cue:** Our approach achieves both quality and consistency across different novel views.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 7 (4.5. Runtime Efficiency), p. 7 (4.6. Ablation Study) |
| Embodiment/environment | Qualitative comparisons of novel view synthesis from reconstructed object between our method and other baselines on the GSO dataset. | hardware/simulator version and reset protocol | p. 6 (4.1. Implementation Details), p. 6 (4.1. Implementation Details) |
| Dataset/benchmark | However, for some multiview datasets, obtaining accurate and complete groundtruth 3D models is not an easy task. | role, split, size and leakage | p. 6 (4.1. Implementation Details), p. 6 (4.1. Implementation Details), p. 8 (4.6. Ablation Study), p. 5 (4.1. Implementation Details) |
| Metric | Quantitative Comparison for single view 3D reconstruction on the GSO dataset, in terms of Chamfer Distance ×10-3, Volume IoU and runtime efficiency. | definition, denominator, direction and uncertainty | p. 7 (4.3. Single View Reconstruction), p. 7 (4.6. Ablation Study), p. 8 (4.6. Ablation Study) |
| Baseline/ablation | We can find that our method has achieved significant improvements in speed for both reconstruction and rendering processes compared to other baselines, benefiting from feed-forward fashion and efficient rasterization. | fair input/data/compute/action matching | p. 7 (4.5. Runtime Efficiency), p. 6 (4.1. Implementation Details), p. 6 (4.1. Implementation Details) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4.1. Implementation Details - extractive body cue:** One-2-345 [35] trains a robust multi-view reconstruction model which takes multi-view images generated from a 2D diffusion model (e.g., Zero-1-2-3).
- **p. 7 / 4.4. Novel View Synthesis - extractive body cue:** Additionally, by leveraging the transformer architecture and local feature projection, our model exhibits robust generalization to unseen objects while preserving intricate textures.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, the inherent ambiguity and lack of information in single images pose a substantial challenge in accurately recovering the complete, ∗Intern at VAST † Corresponding authors This CVPR paper is the Open ...를 문제로 두고, Our approach consists of two networks for reconstructing the point cloud and triplane from the input image, employing a fully transformer-based architecture for both.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3. Method), p. 5 (3.2. Reconstruction from Single-View Images) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
