# Problem - HAD: Hallucination-Aware Diffusion Priors for 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_HAD_Hallucination-Aware_Diffusion_Priors_for_3D_Reconstruction_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_HAD_Hallucination-Aware_Diffusion_Priors_for_3D_Reconstruction_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (3. Preliminary), p. 3 (3. Preliminary)): We then summarize our contributions as below: • We identify a critical limitation where diffusion priors, while alleviating data sparsity in 3D reconstruction, introduce hallucination issues that compromise fidelity to ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Diffusion priors have recently demonstrated strong capability in enhancing the quality of sparse-view 3D reconstruction by augmenting training views at novel viewpoints, but they inevitably ...
- **p. 1 / Abstract - extractive PDF cue:** To address this challenge, we propose Hallucination-Aware Diffusion prior (HAD), which estimates pixel-wise hallucination score maps for augmented images by leveraging multi-view reasoning capabilities from ...
- **p. 1 / Abstract - extractive PDF cue:** These hallucination scores enable selective masking of unreliable pixels during the progressive 3D reconstruction procedure, preventing the introduction of nonexistent artifacts into the 3D model.
- **p. 1 / Abstract - extractive PDF cue:** To further enhance performance, we create multiple versions of augmented images at each novel view by conditioning the diffusion prior on different input views, which ...
- **p. 1 / Abstract - extractive PDF cue:** We show that our method substantially reduces hallucination artifacts in diffusion-assisted 3D reconstruction, thereby achieving state-of-the-art performance across mul- *Work done at Amazon. †Corresponding author. ...
- **p. 2 / 1. Introduction - extractive PDF cue:** We then summarize our contributions as below: • We identify a critical limitation where diffusion priors, while alleviating data sparsity in 3D reconstruction, introduce hallucination ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To address this limitation, we propose incorporating hallucination awareness into the augmented views.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | We then summarize our contributions as below: • We identify a critical limitation where diffusion priors, while alleviating data sparsity in 3D ... | high-dimensional data 또는 robot action-trajectory distribution | body wording is the source claim |
| Observation / input | A feedforward NVS network is a generalizable network that takes multiple views as input and outputs a 3D feature, enabling the rendering ... | conditioning observation와 noisy/intermediate sample | exact sensor/frame/preprocessing from PDF |
| State / latent | feedforward, NVS, network, generalizable, takes, multiple, views, input, outputs, feature | latent/noise variable와 conditional distribution | notation and tensor shape require body check |
| Output / action | leverage, multi-view, reasoning, capability, existing, novel, view, synthesis | generated sample, action chunk 또는 trajectory | exact unit/frame/decoder require body check |
| Target outcome | sample quality, diversity and latency | distribution fit, multimodality, sample quality와 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | data x₀, noisy state x_t, condition c; body terms: feedforward, NVS, network, generalizable, takes, multiple, views, input, outputs, feature | p. 3 (3. Preliminary), p. 5 (4.2.2. Hallucination Score Estimation), p. 5 (4.2.2. Hallucination Score Estimation) |
| Decision / output variable | sample/action x̂ or trajectory; body terms: best, knowledge, first, study, hallucination, score, modeling, context | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (4.2.3. Multi-Sampling Strategy) |
| Objective / loss / cost | distribution/denoising/flow objective; cue terms: formulate, DGS, training, inputLinput, novelLnovel, where, Linput, Lnovel | p. 4 (4.1. 3DGS training), p. 4 (4.1. 3DGS training), p. 5 (4.2.2. Hallucination Score Estimation), p. 5 (4.1. 3DGS training), p. 6 (4.2.3. Multi-Sampling Strategy) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (4.2.2. Hallucination Score Estimation), p. 5 (4.1. 3DGS training), p. 6 (4.2.3. Multi-Sampling Strategy) |
| Success / guarantee | sample quality, diversity and latency | p. 8 (Figure/Table caption), p. 8 (5.4. Ablation studies), p. 6 (5.1. Experimental Setup) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** To address this limitation, we propose incorporating hallucination awareness into the augmented views.
- **p. 1 / 1. Introduction - extractive PDF cue:** One approach to address data sparsity is to leverage generative diffusion priors to augment novel-view data by removing artifacts from rendered images through denoising conditioned ...
- **p. 3 / 3. Preliminary - extractive PDF cue:** Recent advances have demonstrated that diffusion-based priors are highly effective for improving 3D reconstruction and scene enhancement [8, 11, 26, 28, 41].
- **p. 3 / 3. Preliminary - extractive PDF cue:** We briefly describe the preliminaries for 3D Gaussian Splatting (3DGS) - the 3D pipeline that we use to validate our HAD, feedforward novel view synthesis ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (4.2.3. Multi-Sampling Strategy), p. 5 (4.2. Hallucination-Aware Diffusion Prior), p. 1 (1. Introduction)): To the best of our knowledge, this is the first work to study hallucination score modeling in this context. • We introduce a multi-sampling strategy into HAD that generates and ...

- **p. 2 / 1. Introduction - extractive PDF cue:** We then summarize our contributions as below: • We identify a critical limitation where diffusion priors, while alleviating data sparsity in 3D reconstruction, introduce hallucination ...
- **p. 5 / 4.2.3. Multi-Sampling Strategy - extractive PDF cue:** To further enhance HAD, we propose a multi-sampling strategy that creates multiple versions of augmented views and fuses them to produce higher-quality novel views for ...
- **p. 5 / 4.2. Hallucination-Aware Diffusion Prior - extractive PDF cue:** To enhance novel view synthesis quality, we propose the hallucination-aware diffusion prior (HAD) to augment images rendered at novel views and optimize the 3DGS model ...
- **p. 1 / 1. Introduction - extractive PDF cue:** One approach to address data sparsity is to leverage generative diffusion priors to augment novel-view data by removing artifacts from rendered images through denoising conditioned ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | In this work, we identify and address a critical limitation in diffusion-assisted 3D reconstruction: while diffusion priors effectively ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | An interesting direction for future work is to scale up the training of our model by removing the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Figure 2. Overview of framework - We train 3DGS with input images and HAD-augmented novel views. HAD combines ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | We primarily use Peak Signal-toNoise Ratio (PSNR), structural (SSIM [39]) and perceptual (LPIPS [50]) similarities as metrics to ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

generative writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3. Preliminary), p. 5 (4.2.2. Hallucination Score Estimation), p. 5 (4.2.2. Hallucination Score Estimation), p. 4 (4. Methodology). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (3. Preliminary), p. 3 (3. Preliminary), interface p. 3 (3. Preliminary), p. 5 (4.2.2. Hallucination Score Estimation), p. 5 (4.2.2. Hallucination Score Estimation), p. 4 (4. Methodology), objective p. 4 (4.1. 3DGS training), p. 4 (4.1. 3DGS training), p. 5 (4.2.2. Hallucination Score Estimation), p. 5 (4.1. 3DGS training), p. 6 (4.2.3. Multi-Sampling Strategy).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
