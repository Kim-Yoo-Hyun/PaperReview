# HAD: Hallucination-Aware Diffusion Priors for 3D Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_HAD_Hallucination-Aware_Diffusion_Priors_for_3D_Reconstruction_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_HAD_Hallucination-Aware_Diffusion_Priors_for_3D_Reconstruction_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_HAD_Hallucination-Aware_Diffusion_Priors_for_3D_Reconstruction_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_HAD_Hallucination-Aware_Diffusion_Priors_for_3D_Reconstruction_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 We then summarize our contributions as below: • We identify a critical limitation where diffusion priors, while alleviating data sparsity in 3D reconstruction, introduce hallucination issues that compromise fidelity to input views ...를 문제로 두고, To the best of our knowledge, this is the first work to study hallucination score modeling in this context. • We introduce a multi-sampling strategy into HAD that generates and fuses multiple ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Diffusion priors have recently demonstrated strong capability in enhancing the quality of sparse-view 3D reconstruction by augmenting training views at novel viewpoints, but they inevitably ...
- **p. 1 / Abstract - extractive body cue:** To address this challenge, we propose Hallucination-Aware Diffusion prior (HAD), which estimates pixel-wise hallucination score maps for augmented images by leveraging multi-view reasoning capabilities from ...
- **p. 1 / Abstract - extractive body cue:** These hallucination scores enable selective masking of unreliable pixels during the progressive 3D reconstruction procedure, preventing the introduction of nonexistent artifacts into the 3D model.
- **p. 1 / Abstract - extractive body cue:** To further enhance performance, we create multiple versions of augmented images at each novel view by conditioning the diffusion prior on different input views, which ...
- **p. 1 / Abstract - extractive body cue:** We show that our method substantially reduces hallucination artifacts in diffusion-assisted 3D reconstruction, thereby achieving state-of-the-art performance across mul- *Work done at Amazon. †Corresponding author. ...
- **p. 2 / 1. Introduction - extractive body cue:** We then summarize our contributions as below: • We identify a critical limitation where diffusion priors, while alleviating data sparsity in 3D reconstruction, introduce hallucination ...
- **p. 2 / 1. Introduction - extractive body cue:** To address this limitation, we propose incorporating hallucination awareness into the augmented views.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To the best of our knowledge, this is the first work to study hallucination score modeling in this context. • We introduce a multi-sampling strategy ...
- **p. 2 / 1. Introduction - extractive body cue:** We then summarize our contributions as below: • We identify a critical limitation where diffusion priors, while alleviating data sparsity in 3D reconstruction, introduce hallucination ...
- **p. 5 / 4.2.3. Multi-Sampling Strategy - extractive body cue:** To further enhance HAD, we propose a multi-sampling strategy that creates multiple versions of augmented views and fuses them to produce higher-quality novel views for ...
- **p. 5 / 4.2. Hallucination-Aware Diffusion Prior - extractive body cue:** To enhance novel view synthesis quality, we propose the hallucination-aware diffusion prior (HAD) to augment images rendered at novel views and optimize the 3DGS model ...
- **p. 1 / 1. Introduction - extractive body cue:** One approach to address data sparsity is to leverage generative diffusion priors to augment novel-view data by removing artifacts from rendered images through denoising conditioned ...
- **p. 5 / 4.2.2. Hallucination Score Estimation - extractive body cue:** Specifically, the hallucination score network consists of two components: a multi-view feature encoder V that processes multiple input views, and a score estimation branch S ...
- **p. 5 / 4.1. 3DGS training - extractive body cue:** Specifically, unlike Difix3D [41], which employs a two-phase training strategy that first fully trains a 3DGS model and then progressively updates it with diffusion priors ...
- **p. 4 / 4. Methodology - extractive body cue:** N}}, where I and C denote the RGB images and camera poses respectively, our goal is to reconstruct a high-fidelity 3DGS model capable of producing ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | A feedforward NVS network is a generalizable network that takes multiple views as input and outputs a 3D feature, enabling the rendering of images from novel viewpoints. | conditioning observation와 noisy/intermediate sample | p. 3 (3. Preliminary), p. 5 (4.2.2. Hallucination Score Estimation) |
| State/latent | feedforward, NVS, network, generalizable, takes, multiple, views, input, outputs, feature, enabling, rendering | latent/noise variable와 conditional distribution | p. 3 (3. Preliminary), p. 5 (4.2.2. Hallucination Score Estimation), p. 5 (4.2.2. Hallucination Score Estimation) |
| Output/action | Thus, the multi-view encoder V outputs features aggregated at the novel view pose ˜c from the input views. | generated sample, action chunk 또는 trajectory | p. 5 (4.2.2. Hallucination Score Estimation), p. 5 (4.2.2. Hallucination Score Estimation), p. 4 (4. Methodology) |
| Objective/outcome | We formulate the 3DGS training as arg min Φ λinputLinput + λnovelLnovel (6) where Linput and Lnovel are the rendering losses for input views and augmented novel views, respectively, λinput and λnovel ... | distribution fit, multimodality, sample quality와 latency | p. 4 (4.1. 3DGS training), p. 4 (4.1. 3DGS training), p. 5 (4.2.2. Hallucination Score Estimation) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To the best of our knowledge, this is the first work to study hallucination score modeling in this context. • We introduce a multi-sampling strategy ...
- **p. 2 / 1. Introduction - extractive body cue:** We then summarize our contributions as below: • We identify a critical limitation where diffusion priors, while alleviating data sparsity in 3D reconstruction, introduce hallucination ...
- **p. 5 / 4.2.3. Multi-Sampling Strategy - extractive body cue:** To further enhance HAD, we propose a multi-sampling strategy that creates multiple versions of augmented views and fuses them to produce higher-quality novel views for ...
- **p. 5 / 4.2. Hallucination-Aware Diffusion Prior - extractive body cue:** To enhance novel view synthesis quality, we propose the hallucination-aware diffusion prior (HAD) to augment images rendered at novel views and optimize the 3DGS model ...
- **p. 1 / 1. Introduction - extractive body cue:** One approach to address data sparsity is to leverage generative diffusion priors to augment novel-view data by removing artifacts from rendered images through denoising conditioned ...
- **p. 8 / 5.4. Ablation studies - extractive body cue:** We select 3 views to achieve a trade-off between marginal improvement and computational overhead.
- **p. 8 / 5.4. Ablation studies - extractive body cue:** We demonstrate that our hallucination score network, with the pretrained multiview encoder, achieves the best performance.
- **p. 7 / 5.3. Cross-domain evaluation - extractive body cue:** 2, similar to the in-domain evaluation, our method achieves state-of-the-art performance.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (5.4. Ablation studies), p. 8 (5.4. Ablation studies) |
| Embodiment/environment | We first curate training dataset of randomly selected 116 scenes from benchmark dataset for hallucination score network training. | hardware/simulator version and reset protocol | p. 6 (5.1. Experimental Setup), p. 6 (5.1. Experimental Setup) |
| Dataset/benchmark | Method (GSplat-MCMC) PSNR ↑ SSIM ↑ LPIPS ↓ Gsplat-MCMC 26.280 0.869 0.101 Difix3D 26.770 0.874 0.0926 Ours 26.969 0.876 0.0921 estimation on our curated dataset of 114 training scenes and 26 testing ... | role, split, size and leakage | p. 6 (5.1. Experimental Setup), p. 6 (5.1. Experimental Setup), p. 8 (5.4. Ablation studies), p. 7 (5.3. Cross-domain evaluation) |
| Metric | Table 6. Different hallucination score estimators. We use Mean Absolute Error (MAE) of the predicted hallucination score maps as our evaluation metric. We demonstrate that our hallucination score network, with the pretrained ... | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 8 (5.4. Ablation studies), p. 6 (5.1. Experimental Setup) |
| Baseline/ablation | Our method outperforms the baselines by a large margin across all metrics. | fair input/data/compute/action matching | p. 6 (5.2. In-domain evaluation), p. 7 (5.3. Cross-domain evaluation), p. 6 (5.2. In-domain evaluation) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusion and Future Work - extractive body cue:** In this work, we identify and address a critical limitation in diffusion-assisted 3D reconstruction: while diffusion priors effectively alleviate data sparsity, they introduce hallucinated content ...
- **p. 8 / 6. Conclusion and Future Work - extractive body cue:** An interesting direction for future work is to scale up the training of our model by removing the need for complex data requirementsfor instance, using ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of framework - We train 3DGS with input images and HAD-augmented novel views. HAD combines a pretrained diffusion prior (which generates images ...
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** We primarily use Peak Signal-toNoise Ratio (PSNR), structural (SSIM [39]) and perceptual (LPIPS [50]) similarities as metrics to quantify the performance of novel view synthesis.
- **p. 7 / 5.2. In-domain evaluation - extractive body cue:** Notably, while the post-rendering improves the photorealism metric (LPIPS), it degrades fidelity metrics (PSNR and SSIM) for both Difix3D and our method.

## Why Read It

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 We then summarize our contributions as below: • We identify a critical limitation where diffusion priors, while alleviating data sparsity in 3D reconstruction, introduce hallucination issues that compromise fidelity to input views ...를 문제로 두고, To the best of our knowledge, this is the first work to study hallucination score modeling in this context. • We introduce a multi-sampling strategy into HAD that generates and fuses multiple ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (3. Preliminary), p. 3 (3. Preliminary), p. 5 (4.2.2. Hallucination Score Estimation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
