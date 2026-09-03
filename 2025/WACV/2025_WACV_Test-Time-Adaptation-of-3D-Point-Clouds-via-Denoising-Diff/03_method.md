# Method - Test-Time Adaptation of 3D Point Clouds via Denoising Diffusion Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/WACV2025/html/Dastmalchi_Test-Time_Adaptation_of_3D_Point_Clouds_via_Denoising_Diffusion_Models_WACV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/WACV2025/papers/Dastmalchi_Test-Time_Adaptation_of_3D_Point_Clouds_via_Denoising_Diffusion_Models_WACV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.1. Preliminaries), p. 5 (3.3. Denoising Diffusion-based Adaption Method), p. 4 (3.1. Preliminaries), p. 5 (3.3. Denoising Diffusion-based Adaption Method), p. 3 (3.1. Preliminaries), p. 3 (3. Method)): In the first stage, the encoders and the decoder are simultaneously trained to maximize the variational lower bound over the data log-likelihood: LELBO = Ep(x),qz(z0/x),qh(h0/x,z0) h log pd (x / ...

## Method Body Digest

- **p. 4 / 3.1. Preliminaries - extractive body cue:** In the first stage, the encoders and the decoder are simultaneously trained to maximize the variational lower bound over the data log-likelihood: LELBO = Ep(x),qz(z0/x),qh(h0/x,z0) ...
- **p. 5 / 3.3. Denoising Diffusion-based Adaption Method - extractive body cue:** Additionally, given that the initial shape latent z0, obtained from the input point cloud, potentially leads to inaccurate guidance for the denoising network, we propose ...
- **p. 4 / 3.1. Preliminaries - extractive body cue:** The LION model leverages a VAE network composed of two hierarchical encoders and one decoder.
- **p. 5 / 3.3. Denoising Diffusion-based Adaption Method - extractive body cue:** Shape Latent Encoder 𝑞𝑧 Latent Point Encoder 𝑞ℎ Decoder 𝑝𝑑 Denoising Diffusion Network tw + 𝐳0 𝐡tw 𝐡𝟎 𝐫 𝛆 ෤𝐱 𝐱 𝐡0 ∇𝐡tlcd λ ...
- **p. 3 / 3.1. Preliminaries - extractive body cue:** Similarly, the generative process is modeled as a Gaussian transition with a learned 1568
- **p. 3 / 3. Method - extractive body cue:** We have a classifier pc and a diffusion model ϵθ, both trained on original point clouds x ∈Rn×3 from a source domain Qs, where a ...
- **p. 4 / 3.1. Preliminaries - extractive body cue:** In the second stage, the two latent diffusion models are trained on the encodings z0 and h0 sampled from qz(z0/x) and qh(h0/z0, x), minimizing the ...
- **p. 4 / 3.2. Model Overview - extractive body cue:** In addition, the shape latent z0 is updated in the direction of the SCD gradient to improve the conditional signal it provides to the diffusion ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we introduce a novel, training-free test-time adaptation method called 3D Denoising Diffusion TestTime Adaptation (3DD-TTA).
- **p. 2 / 1. Introduction - extractive body cue:** (3) We introduced a modified Chamfer distance, named Selective Chamfer Distance (SCD), to increase the fidelity during the reverse diffusion process.
- **p. 5 / 3.3. Denoising Diffusion-based Adaption Method - extractive body cue:** We introduce and employ the gradient of the Selective Chamfer distance (SCD) denoted as lλ cd, with respect to htw-1 as the regularization term: R ...

## Source Evidence Cues

- **p. 4 / 3.1. Preliminaries - extractive body cue:** In the first stage, the encoders and the decoder are simultaneously trained to maximize the variational lower bound over the data log-likelihood: LELBO = Ep(x),qz(z0/x),qh(h0/x,z0) ...
- **p. 5 / 3.3. Denoising Diffusion-based Adaption Method - extractive body cue:** Additionally, given that the initial shape latent z0, obtained from the input point cloud, potentially leads to inaccurate guidance for the denoising network, we propose ...
- **p. 4 / 3.1. Preliminaries - extractive body cue:** The LION model leverages a VAE network composed of two hierarchical encoders and one decoder.
- **p. 5 / 3.3. Denoising Diffusion-based Adaption Method - extractive body cue:** Shape Latent Encoder 𝑞𝑧 Latent Point Encoder 𝑞ℎ Decoder 𝑝𝑑 Denoising Diffusion Network tw + 𝐳0 𝐡tw 𝐡𝟎 𝐫 𝛆 ෤𝐱 𝐱 𝐡0 ∇𝐡tlcd λ ...
- **p. 3 / 3.1. Preliminaries - extractive body cue:** Similarly, the generative process is modeled as a Gaussian transition with a learned 1568
- **p. 3 / 3. Method - extractive body cue:** We have a classifier pc and a diffusion model ϵθ, both trained on original point clouds x ∈Rn×3 from a source domain Qs, where a ...
- **Detected method headings:** 3. Method (p. 3); 3.2. Model Overview (p. 4); 3.3. Denoising Diffusion-based Adaption Method (p. 4); 4.1. Datasets and Corruption Methods (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | In the first stage, the encoders and the decoder are simultaneously trained to maximize the variational lower bound over the data log-likelihood: ... | p. 4 (3.1. Preliminaries), p. 5 (3.3. Denoising Diffusion-based Adaption Method) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | Additionally, given that the initial shape latent z0, obtained from the input point cloud, potentially leads to inaccurate guidance for the denoising ... | p. 5 (3.3. Denoising Diffusion-based Adaption Method), p. 4 (3.1. Preliminaries) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | The LION model leverages a VAE network composed of two hierarchical encoders and one decoder. | p. 4 (3.1. Preliminaries), p. 5 (3.3. Denoising Diffusion-based Adaption Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.1. Preliminaries - extractive body cue:** In the second stage, the two latent diffusion models are trained on the encodings z0 and h0 sampled from qz(z0/x) and qh(h0/z0, x), minimizing the ...
- **p. 4 / 3.2. Model Overview - extractive body cue:** In addition, the shape latent z0 is updated in the direction of the SCD gradient to improve the conditional signal it provides to the diffusion ...
- **p. 5 / 3.3. Denoising Diffusion-based Adaption Method - extractive body cue:** During denoising, both shape latent and latent points are updated to minimize the SCD distancelλ cd.
- **p. 5 / 3.3. Denoising Diffusion-based Adaption Method - extractive body cue:** We introduce and employ the gradient of the Selective Chamfer distance (SCD) denoted as lλ cd, with respect to htw-1 as the regularization term: R ...
- **p. 3 / 3.1. Preliminaries - extractive body cue:** In this process, Gaussian noise is progressively added to the data in a Markovian manner, and the model is trained to recover the original data ...
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 4 (3.2. Model Overview), p. 4 (3.1. Preliminaries), p. 5 (3.3. Denoising Diffusion-based Adaption Method), p. 5 (3.3. Denoising Diffusion-based Adaption Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Additionally, given, initial, shape, latent, obtained, input, point, cloud, potentially, leads, inaccurate, guidance, denoising | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | Additionally, given, initial, shape, latent, obtained, input, point, cloud, potentially | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | introduce, novel, training-free, test-time, adaptation, called, Denoising, Diffusion, TestTime, DD-TTA | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | second, stage, latent, diffusion, models, trained, encodings, sampled, z0/x, h0/z0 | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3.3. Denoising Diffusion-based Adaption Method - extractive body cue:** Additionally, given that the initial shape latent z0, obtained from the input point cloud, potentially leads to inaccurate guidance for the denoising network, we propose ...
- **p. 4 / 3.1. Preliminaries - extractive body cue:** Finally, the decoder denoted by pd(x/z0, h0) takes the shape latent and latent points as inputs and maps them back to the point cloud.
- **p. 4 / 3.1. Preliminaries - extractive body cue:** The first encoder, denoted as qz(z0/x), converts the input point cloud x into an abstract latent vector z0 ∈RDz, referred to as the shape latent.
- **p. 5 / 3.3. Denoising Diffusion-based Adaption Method - extractive body cue:** 1: Input: Corrupted point cloud ˜x, shape encoder qz(.), latent point encoder qh(.), decoder pd(.), diffusion prior ϵh(.), and source classifier pc(.) 2: z0 ∼qz ...
- **p. 2 / 1. Introduction - extractive body cue:** After perturbation, the CD distributions for all corruption types overlap, demonstrating corruption independence. focus on updating the source model parameters and risk inducing forgetting, [9, ...
- **p. 2 / 1. Introduction - extractive body cue:** (4) We conduct extensive experiments validating the approach on ShapeNet [3] ModelNet40 [52], and ScanObjectNN [44] achieving new state-of-the-art results.
- **p. 1 / 1. Introduction - extractive body cue:** Reconstruction of corrupted point clouds using the proposed 3DD-TTA method. between training and testing samples is minimal.
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | The latent points h0 are then perturbed with Gaussian noise ϵ ∈N(0, I) at the tw time step using Eq. | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | Subsequently, the latent points of the previous time step (htw-1) are estimated using the DDIM [38] sampling technique, guided by a regularization ... | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not recovered | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.1. Preliminaries - extractive body cue:** In the first stage, the encoders and the decoder are simultaneously trained to maximize the variational lower bound over the data log-likelihood: LELBO = Ep(x),qz(z0/x),qh(h0/x,z0) ...
- **p. 3 / 3. Method - extractive body cue:** We have a classifier pc and a diffusion model ϵθ, both trained on original point clouds x ∈Rn×3 from a source domain Qs, where a ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** first, stage, encoders, decoder, simultaneously, trained, maximize, variational, lower, bound, over, data, log-likelihood, LELBO, z0/x, h0/x, zDKL, hDKL, Here, denote.
- **Relevant PDF headings:** 3. Method (p. 3); 3.2. Model Overview (p. 4); 3.3. Denoising Diffusion-based Adaption Method (p. 4); 4.1. Datasets and Corruption Methods (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | ScanObjectNN-c: ScanObjectNN [44], a real-world point cloud dataset with 15 categories, is corrupted using the same open-source code as ModelNet40-c [40], introducing ... | p. 6 (4.1. Datasets and Corruption Methods), p. 7 (4.3. Results) |
| Denoiser / vector field | In addition, our 3DD-TTA outperforms other TTA frameworks on density-based corruptions such as cut-out and density increase. | p. 6 (4.3. Results), p. 6 (4.3. Results) |
| Sampling / downstream interface | In addition, our 3DD-TTA outperforms other TTA frameworks on density-based corruptions such as cut-out and density increase. | p. 6 (4.3. Results), p. 6 (4.3. Results) |

## Failure and Ablation Link

- **p. 6 / 4.3. Results - extractive body cue:** This limitation is due to the trainingfree nature of the model, making it challenging to reverse transformations to their original shape without additional training.
- **p. 7 / 4.4. Ablation Study - extractive body cue:** Number of Denoising Steps for Reconstruction: While the denoising diffusion network in the original LION [45] model was trained with 1000 time steps, we posit ...
- **p. 6 / 4.2. Baselines - extractive body cue:** The baselines include: (1) SHOT [17], which minimizes output entropy; (2) T3A [14], which learns class-specific prototypes to replace the pre-trained classifier; (3) TENT [47], ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. In the TTA setting, the source model encounters corrupted 3D point clouds with an unknown distribution shift, requiring adaptation without prior knowledge of ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Reconstruction of corrupted point clouds using the pro- posed 3DD-TTA method. between training and testing samples is minimal. However, real-world scenarios often feature ...
- **p. 6 / 4.3. Results - extractive body cue:** However, the model faces limitations in addressing the transformation-based deformations like shear and rotation.
- **p. 6 / 4.3. Results - extractive body cue:** This limitation is due to the trainingfree nature of the model, making it challenging to reverse transformations to their original shape without additional training.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.1. Preliminaries), p. 5 (3.3. Denoising Diffusion-based Adaption Method), p. 4 (3.1. Preliminaries), p. 5 (3.3. Denoising Diffusion-based Adaption Method), p. 3 (3.1. Preliminaries), p. 3 (3. Method), objective p. 4 (3.1. Preliminaries), p. 4 (3.2. Model Overview), p. 5 (3.3. Denoising Diffusion-based Adaption Method), p. 5 (3.3. Denoising Diffusion-based Adaption Method), p. 3 (3.1. Preliminaries), temporal p. 4 (3.2. Model Overview), p. 4 (3.3. Denoising Diffusion-based Adaption Method), p. 5 (3.3. Denoising Diffusion-based Adaption Method), p. 6 (4. Experiments), p. 6 (4. Experiments), p. 7 (4.4. Ablation Study).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
