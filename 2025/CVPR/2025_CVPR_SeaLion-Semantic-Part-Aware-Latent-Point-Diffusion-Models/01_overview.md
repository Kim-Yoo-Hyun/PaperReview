# SeaLion: Semantic Part-Aware Latent Point Diffusion Models for 3D Generation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_SeaLion_Semantic_Part-Aware_Latent_Point_Diffusion_Models_for_3D_Generation_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Zhu_SeaLion_Semantic_Part-Aware_Latent_Point_Diffusion_Models_for_3D_Generation_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: semantic, alignment, Diffusion, Generation, point cloud, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_SeaLion_Semantic_Part-Aware_Latent_Point_Diffusion_Models_for_3D_Generation_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Zhu_SeaLion_Semantic_Part-Aware_Latent_Point_Diffusion_Models_for_3D_Generation_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 However, they still lack the ability to generate semantic labels.를 문제로 두고, In summary, the contributions of this work are: • We propose a novel generative model named SeaLion, capable of generating high-quality and diverse point clouds with accurate semantic segmentation labels. • We ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Denoising diffusion probabilistic models have achieved significant success in point cloud generation, enabling numerous downstream applications, such as generative data augmentation and 3D model editing.
- **p. 1 / Abstract - extractive body cue:** However, little attention has been given to generating point clouds with pointwise segmentation labels, as well as to developing evaluation metrics for this task.
- **p. 1 / Abstract - extractive body cue:** Therefore, in this paper, we present SeaLion, a novel diffusion model designed to generate high-quality and diverse point clouds with fine-grained segmentation labels.
- **p. 1 / Abstract - extractive body cue:** Specifically, we introduce the semantic part-aware latent point diffusion technique, which leverages the intermediate features of the generative models to jointly predict the noise for ...
- **p. 1 / Abstract - extractive body cue:** To effectively evaluate the quality of generated point clouds, we introduce a novel point cloud pairwise distance calculation method named part-aware Chamfer distance (p-CD).
- **p. 1 / 1. Introduction - extractive body cue:** However, they still lack the ability to generate semantic labels.
- **p. 2 / 1. Introduction - extractive body cue:** However, this method fails to measure the part-topart coherence within a shape.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, the contributions of this work are: • We propose a novel generative model named SeaLion, capable of generating high-quality and diverse point clouds ...
- **p. 2 / 1. Introduction - extractive body cue:** We propose a novel evaluation metric named part-aware Chamfer distance (p-CD) to address these limitations and to quantify the pairwise distance between two segmentation-labeled point ...
- **p. 4 / 3.2. Model Architecture of SeaLion - extractive body cue:** Based on the semantic part-aware latent point diffusion technique, we introduce a novel point cloud generative model named SeaLion.
- **p. 3 / 3. Methodology - extractive body cue:** Next, we introduce the architecture of SeaLion, and illustrate its usage as a part-aware 3D edition tool.
- **p. 3 / 3.1. Semantic Part-Aware Latent Point Diffusion - extractive body cue:** Inspired by the insight that DDPMs can serve as powerful representation learners for discriminative tasks like segmentation [2], we propose semantic part-aware latent point diffusion ...
- **p. 5 / 3.2. Model Architecture of SeaLion - extractive body cue:** The global encoder ϕz consists of PVConv blocks, set abstraction layers, a max pooling layer, and a multi-layer perceptron.
- **p. 4 / 3.1. Semantic Part-Aware Latent Point Diffusion - extractive body cue:** Compared to the traditional twostep method, which first generates unlabeled point clouds and then assigns pseudo segmentation labels using a pretrained segmentation model, our approach ...
- **p. 5 / 3.3. Part-aware 3D Shape Edition Tool - extractive body cue:** In this process, the unfrozen latent points are perturbed for τ steps (τ < T) and then denoised for the same number of steps.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In summary, the contributions of this work are: • We propose a novel generative model named SeaLion, capable of generating high-quality and diverse point clouds with accurate semantic segmentation labels. • We ... | conditioning observation와 noisy/intermediate sample | p. 2 (1. Introduction), p. 3 (3.1. Semantic Part-Aware Latent Point Diffusion) |
| State/latent | summary, contributions, novel, generative, model, named, SeaLion, capable, generating, high-quality, diverse, point | latent/noise variable와 conditional distribution | p. 2 (1. Introduction), p. 3 (3.1. Semantic Part-Aware Latent Point Diffusion), p. 4 (3.2. Model Architecture of SeaLion) |
| Output/action | The generative model acquires semantic part awareness by being trained to reconstruct input point clouds guided by segmentation encodings, forming a basis for extracting segmentation information from the latent feature h0 in ... | generated sample, action chunk 또는 trajectory | p. 3 (3.1. Semantic Part-Aware Latent Point Diffusion), p. 4 (3.2. Model Architecture of SeaLion), p. 1 (1. Introduction) |
| Objective/outcome | In the first stage, we train the components of hierarchical VAE, including ϕz, ϕh, and ξh, to maximize a variational lower bound on the data log-likelihood (ELBO): \la bel {e q :elbo} ... | distribution fit, multimodality, sample quality와 latency | p. 4 (3.1. Semantic Part-Aware Latent Point Diffusion), p. 4 (3.1. Semantic Part-Aware Latent Point Diffusion), p. 3 (3.1. Semantic Part-Aware Latent Point Diffusion) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, the contributions of this work are: • We propose a novel generative model named SeaLion, capable of generating high-quality and diverse point clouds ...
- **p. 2 / 1. Introduction - extractive body cue:** We propose a novel evaluation metric named part-aware Chamfer distance (p-CD) to address these limitations and to quantify the pairwise distance between two segmentation-labeled point ...
- **p. 4 / 3.2. Model Architecture of SeaLion - extractive body cue:** Based on the semantic part-aware latent point diffusion technique, we introduce a novel point cloud generative model named SeaLion.
- **p. 3 / 3. Methodology - extractive body cue:** Next, we introduce the architecture of SeaLion, and illustrate its usage as a part-aware 3D edition tool.
- **p. 3 / 3.1. Semantic Part-Aware Latent Point Diffusion - extractive body cue:** Inspired by the insight that DDPMs can serve as powerful representation learners for discriminative tasks like segmentation [2], we propose semantic part-aware latent point diffusion ...
- **p. 7 / 4.2. Experimental Results - extractive body cue:** The results show that SeaLion outperforms DiffFacto on the primary metric 1-NNA-P and achieves competitive performance on the other metrics.
- **p. 8 / 4.3. Experimental Analysis - extractive body cue:** The experimental results presented in Table 4 demonstrate that SeaLion outperforms DiffFacto when trained with 10% labeled data, and its performance further improves after incorporating ...
- **p. 7 / 4.2. Experimental Results - extractive body cue:** The prediction accuracy improves as t decreases from T to 0. lamp categories, SeaLion outperforms DiffFacto by an average of 13.33% on 1-NNA (p-CD), 11.61% ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4.2. Experimental Results), p. 8 (4.3. Experimental Analysis) |
| Embodiment/environment | IntrA [34] is a real-world dataset containing 3D intracranial aneurysm point clouds reconstructed from MRI. | hardware/simulator version and reset protocol | p. 6 (4.1. Experimental Setup), p. 5 (3.4. Evaluation Metrics) |
| Dataset/benchmark | The dataset contains 116 aneurysm segments manually annotated by medical experts. | role, split, size and leakage | p. 6 (4.1. Experimental Setup), p. 5 (3.4. Evaluation Metrics), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Experimental Results) |
| Metric | The intra-part score measures the quality of the independently generated parts and the overall point cloud by averaging the results across all parts. | definition, denominator, direction and uncertainty | p. 5 (3.4. Evaluation Metrics), p. 5 (3.4. Evaluation Metrics), p. 6 (3.4. Evaluation Metrics) |
| Baseline/ablation | The results demonstrate that SeaLion outperforms both DiffFacto and the two-step approach, which combines the state-of-the-art generative and segmentation models, Lion and SPoTr. | fair input/data/compute/action matching | p. 6 (4.2. Experimental Results), p. 6 (4.2. Experimental Results), p. 7 (4.2. Experimental Results) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 3.4. Evaluation Metrics - extractive body cue:** However, both intra-part and inter-part scores have limitations in evaluating the generation of segmentation-labeled point clouds.
- **p. 5 / 3.4. Evaluation Metrics - extractive body cue:** As discussed in [32, 37], COV quantifies generation diversity and is sensitive to mode collapse, but it fails to evaluate the quality of G.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** As discussed in [32], 1-NNA measures both generation quality and diversity by computing the distribution similarity between R and G, while COV and MMD have ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** Additionally, we report the results of 1-NNA-P, COV-P, and MMD-P [23] for the airplane and chair categories in ShapeNet for comparison to DiffFacto, despite the ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. (a) Training: The generative model develops semantic part awareness by being trained to reconstruct input point clouds x guided by segmentation encodings y, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Data flow in the point-level diffusion module ϵh. The input, perturbed latent points ht at step t, is down-sampled and transformed to common ...
- **p. 7 / 4.2. Experimental Results - extractive body cue:** In SeaLion, the diffusion ϵh predicts both noise and segmentation during the generation process.

## Why Read It

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 However, they still lack the ability to generate semantic labels.를 문제로 두고, In summary, the contributions of this work are: • We propose a novel generative model named SeaLion, capable of generating high-quality and diverse point clouds with accurate semantic segmentation labels. • We ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Semantic Part-Aware Latent Point Diffusion), p. 4 (3.2. Model Architecture of SeaLion) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
