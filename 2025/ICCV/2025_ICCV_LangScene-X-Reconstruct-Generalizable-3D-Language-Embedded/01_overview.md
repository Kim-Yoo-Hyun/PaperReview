# LangScene-X: Reconstruct Generalizable 3D Language-Embedded Scenes with TriMap Video Diffusion

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Liu_LangScene-X_Reconstruct_Generalizable_3D_Language-Embedded_Scenes_with_TriMap_Video_Diffusion_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Liu_LangScene-X_Reconstruct_Generalizable_3D_Language-Embedded_Scenes_with_TriMap_Video_Diffusion_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, Diffusion
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Liu_LangScene-X_Reconstruct_Generalizable_3D_Language-Embedded_Scenes_with_TriMap_Video_Diffusion_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Liu_LangScene-X_Reconstruct_Generalizable_3D_Language-Embedded_Scenes_with_TriMap_Video_Diffusion_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The primary difficulty is extracting and fusing sufficient multimodal knowledge from limited inputs to achieve coherent 3D scene reconstruction and understanding.를 문제로 두고, To address this, we propose LangScene-X, a novel generative paradigm to build generalizable 3D languageembedded scenes from very sparse views (i.e., as few as two images).를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recovering 3D structures with open-vocabulary scene understanding from 2D images is a fundamental but daunting task.
- **p. 1 / Abstract - extractive body cue:** Recent developments have achieved this by performing per-scene optimization with embedded language information.
- **p. 1 / Abstract - extractive body cue:** However, they heavily rely on the calibrated denseview reconstruction paradigm, thereby suffering from severe rendering artifacts and implausible semantic synthesis when limited views are available.
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce a novel generative framework, coined LangScene-X, to unify and generate 3D consistent multi-modality information for reconstruction and understanding.
- **p. 1 / Abstract - extractive body cue:** Powered by the generative capability of creating more consistent novel †The corresponding author. observations, we can build generalizable 3D languageembedded scenes from only sparse views.
- **p. 2 / 1. Introduction - extractive body cue:** The primary difficulty is extracting and fusing sufficient multimodal knowledge from limited inputs to achieve coherent 3D scene reconstruction and understanding.
- **p. 2 / 1. Introduction - extractive body cue:** Although they can achieve promising results in per-scene optimization with calibrated dense views (usually more than 20 views) as input, they cannot generalize to unseen ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To address this, we propose LangScene-X, a novel generative paradigm to build generalizable 3D languageembedded scenes from very sparse views (i.e., as few as two ...
- **p. 2 / 1. Introduction - extractive body cue:** To reduce the memory cost and enhance scalability for large-scale data, we propose a generalizable Language Quantized Compressor (LQC) trained on largescale datasets, which encodes ...
- **p. 3 / 3.1. Overview of LangScene-X - extractive body cue:** In our framework LangScene-X, we first build the TriMap video diffusion model to generate 3D consistent RGB images, normal maps, and semantic maps from sparse-view ...
- **p. 3 / 3.1. Overview of LangScene-X - extractive body cue:** This eliminates perscene retraining and enables rapid rendering of Gaussians.
- **p. 4 / 3.2. Building the TriMap Video Diffusion - extractive body cue:** Query Mask RGB Normal "Bear" View 2 Novel View VAE Encoder VAE Decoder + RGB & Semantic & Normal Latents Noise Latents * N Blocks ...
- **p. 5 / 3.3. Language Quantized Compressor - extractive body cue:** For learnable embeddings training, we utilize classic dictionary learning algorithms that push embeddings E towards encoder outputs z_e(x ): \m a thc al {L}_ { ...
- **p. 5 / 3.3. Language Quantized Compressor - extractive body cue:** To address it, we directly copy the gradient flow from decoder to encoder networks for encoder-decoder training, where : \ ma t hcal {L }_{\te ...
- **p. 4 / 3.2. Building the TriMap Video Diffusion - extractive body cue:** Then, we encode the condition video with a causal VAE [49] encoder to get a latent vector concatenated with a Gaussian noise of the same ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given N sparse views (i.e., as few as two images) as input, our goal is to reconstruct and understand the underlying 3D scene (i.e., construct the language-embedded surface fields). | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3.1. Overview of LangScene-X), p. 3 (3.1. Overview of LangScene-X) |
| State/latent | Given, sparse, views, images, input, goal, reconstruct, understand, underlying, scene, construct, language-embedded | geometry, map, object/relationship state | p. 3 (3.1. Overview of LangScene-X), p. 3 (3.1. Overview of LangScene-X), p. 4 (3.2. Building the TriMap Video Diffusion) |
| Output/action | In our framework LangScene-X, we first build the TriMap video diffusion model to generate 3D consistent RGB images, normal maps, and semantic maps from sparse-view input (Sec. | point map, pose, scene graph, affordance 또는 query result | p. 3 (3.1. Overview of LangScene-X), p. 4 (3.2. Building the TriMap Video Diffusion), p. 4 (3.2. Building the TriMap Video Diffusion) |
| Objective/outcome | In pratice, we leverage the powerful normal priors \ p rotect \mathbf {N}\in \mathbb {R}^{D\times H\times W\times 3} generated by the TriMap video diffusion, we adopt a progressive normal regularization \protect \mathcal ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.4. Language-Embeded Surface Fields), p. 4 (3.2. Building the TriMap Video Diffusion), p. 5 (3.3. Language Quantized Compressor) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To address this, we propose LangScene-X, a novel generative paradigm to build generalizable 3D languageembedded scenes from very sparse views (i.e., as few as two ...
- **p. 2 / 1. Introduction - extractive body cue:** To reduce the memory cost and enhance scalability for large-scale data, we propose a generalizable Language Quantized Compressor (LQC) trained on largescale datasets, which encodes ...
- **p. 3 / 3.1. Overview of LangScene-X - extractive body cue:** In our framework LangScene-X, we first build the TriMap video diffusion model to generate 3D consistent RGB images, normal maps, and semantic maps from sparse-view ...
- **p. 3 / 3.1. Overview of LangScene-X - extractive body cue:** This eliminates perscene retraining and enables rapid rendering of Gaussians.
- **p. 4 / 3.2. Building the TriMap Video Diffusion - extractive body cue:** Query Mask RGB Normal "Bear" View 2 Novel View VAE Encoder VAE Decoder + RGB & Semantic & Normal Latents Noise Latents * N Blocks ...
- **p. 6 / 4.2. Main Results - extractive body cue:** By comparing with existing state-of-the-art 3D language field techniques (e.g., LangSplat, LangSurf), unified 3D representation method (i.e., LSM), and open-vocabulary methods like LSeg, our method ...
- **p. 6 / 4.1. Experiment Setup - extractive body cue:** For quantitative results, we report the standard metrics in semantic understanding, including open-vocabulary localization accuracy (mAcc) and semantic segmentation (mIoU scores).
- **p. 8 / 4.3. Ablations - extractive body cue:** 51.68 45.07 gressive training in TriMap video diffusion, which achieves more matched points.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4.2. Main Results), p. 6 (4.1. Experiment Setup) |
| Embodiment/environment | The LERF dataset is an in-the-wild dataset captured by a handheld device, while ScanNet is a large scene dataset captured by RGB-D devices in complex indoor scenes. | hardware/simulator version and reset protocol | p. 6 (4.1. Experiment Setup), p. 6 (4.1. Experiment Setup) |
| Dataset/benchmark | 2D Segmentation Results on Scannet [7] Dataset. | role, split, size and leakage | p. 6 (4.1. Experiment Setup), p. 6 (4.1. Experiment Setup), p. 7 (4.2. Main Results), p. 8 (4.2. Main Results) |
| Metric | Table 2. 2D Quantitative Results on ScanNet Dataset. We report the open-vocabulary localization accuracy (%) and 2D semantic segmentation (IoU scores). The bold denotes the best results. Scene Type LSeg [19] LangSplat ... | definition, denominator, direction and uncertainty | p. 6 (Figure/Table caption), p. 8 (4.3. Ablations), p. 6 (4.1. Experiment Setup) |
| Baseline/ablation | To demonstrate our strong capability in building 3D language-embedded scenes from only sparse views, we compare our LangScene-X against four competitive baselines: LSeg [19], LangSplat [34], LangSurf [20], and LSM [8]. | fair input/data/compute/action matching | p. 6 (4.1. Experiment Setup), p. 6 (4.2. Main Results), p. 8 (4.3. Ablations) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** In this paper, we present LangScene-X, a generative framework that builds generalizable 3D language-embedded fields from only sparse views, which unify the information of reconstructing ...
- **p. 8 / 5. Conclusion - extractive body cue:** Specifically, we first train a TriMap video diffusion model through progressive knowledge integration, which can generate 3D consistent RGBs, normals, and semantic maps.
- **p. 8 / 5. Conclusion - extractive body cue:** Then we introduce a language quantized compressor to map high-dimensional language features into efficient feature representations.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The primary difficulty is extracting and fusing sufficient multimodal knowledge from limited inputs to achieve coherent 3D scene reconstruction and understanding.를 문제로 두고, To address this, we propose LangScene-X, a novel generative paradigm to build generalizable 3D languageembedded scenes from very sparse views (i.e., as few as two images).를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.3. Language Quantized Compressor), p. 4 (3.2. Building the TriMap Video Diffusion), p. 5 (3.3. Language Quantized Compressor), p. 4 (3.2. Building the TriMap Video Diffusion) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
