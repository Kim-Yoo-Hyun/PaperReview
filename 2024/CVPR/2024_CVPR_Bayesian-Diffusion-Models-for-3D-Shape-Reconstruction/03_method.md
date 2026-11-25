# Method - Bayesian Diffusion Models for 3D Shape Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Xu_Bayesian_Diffusion_Models_for_3D_Shape_Reconstruction_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Xu_Bayesian_Diffusion_Models_for_3D_Shape_Reconstruction_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

- **원문 대조:** 식 (1)은 data-driven conditional log-density와 prior log-density의 gradient를 더하고 Gaussian noise를 주입하는 Langevin update를 제시한다. 이는 Bayesian 결합의 설명이며 최종 구현은 뒤의 diffusion prior integration과 구분한다. ([PDF p. 3](https://openaccess.thecvf.com/content/CVPR2024/papers/Xu_Bayesian_Diffusion_Models_for_3D_Shape_Reconstruction_CVPR_2024_paper.pdf#page=3), §3.1 Bayesian Inference with Stochastic Gradient Langevin Dynamics, Eq. (1)).

## Method Body Digest

- **p. 3 / 3.1. Bayesian Inference with Stochastic Gradient - extractive body cue:** Therefore, the inference for the optimal prediction y∗can then be carried via Markov Chain Monte Carlo (MCMC) [3] using stochastic gradient Langevin dynamics [71]: ∆yt ...
- **p. 3 / 3. Method - extractive body cue:** In the following section, we introduce the Bayesian Diffusion Models, the framework of which is illustrated in Fig.
- **원문 대조:** Prior diffusion model의 noise 예측은 reverse Markov transition p(y^t ∣ y^{t+1})을 통해 point-cloud 분포를 갱신한다. Reconstruction model의 image-conditioned transition과 구분해 두 경로의 정보를 결합한다. ([PDF p. 4](https://openaccess.thecvf.com/content/CVPR2024/papers/Xu_Bayesian_Diffusion_Models_for_3D_Shape_Reconstruction_CVPR_2024_paper.pdf#page=4), §3.3 Bayesian Diffusion Model).
- **p. 4 / 3.4. Point Cloud Prior Integration - extractive body cue:** Therefore, we employ step-wise interaction between a generative diffusion model and a reconstruction model, facilitating closer integration of point cloud priors.
- **p. 3 / 3.1. Bayesian Inference with Stochastic Gradient - extractive body cue:** 3 shows the basic Bayes formulation and demonstrates the stochastic gradient Langevin inference result.
- **p. 3 / 3.1. Bayesian Inference with Stochastic Gradient - extractive body cue:** 2) a mere summation for the gradients ∇log pγ(y/x) and ∇log p(yt) limits the level of interaction between the bottom-up and top-down processes.
- **p. 4 / 3.3. Bayesian Diffusion Model - extractive body cue:** 2, we use an inaccessible function Φ to incorporate the prior diffusion gradient into the reconstruction diffusion gradient.
- **p. 4 / 3.2. Denoising Diffusion Probabilistic Models - extractive body cue:** Bayesian Prediction Bayesian Diffusion Model Process Top-down (prior) Bottom-up (data-driven) … Fusion Fusion Stochastic Gradient Langevin … Prior Data-driven Figure 3.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** The contribution of our paper is summarized as follows: • We present Bayesian Diffusion Models (BDM), a new statistical inference algorithm that couples diffusionbased bottom-up ...
- **p. 3 / 3.1. Bayesian Inference with Stochastic Gradient - extractive body cue:** For the 3D shape reconstruction task, the output y consists of a set of 3D points.
- **p. 3 / 3. Method - extractive body cue:** In the following section, we introduce the Bayesian Diffusion Models, the framework of which is illustrated in Fig.

## Source Evidence Cues

- **p. 3 / 3.1. Bayesian Inference with Stochastic Gradient - extractive body cue:** Therefore, the inference for the optimal prediction y∗can then be carried via Markov Chain Monte Carlo (MCMC) [3] using stochastic gradient Langevin dynamics [71]: ∆yt ...
- **p. 3 / 3. Method - extractive body cue:** In the following section, we introduce the Bayesian Diffusion Models, the framework of which is illustrated in Fig.
- **원문 대조:** Prior diffusion model의 noise 예측은 reverse Markov transition p(y^t ∣ y^{t+1})을 통해 point-cloud 분포를 갱신한다. Reconstruction model의 image-conditioned transition과 구분해 두 경로의 정보를 결합한다. ([PDF p. 4](https://openaccess.thecvf.com/content/CVPR2024/papers/Xu_Bayesian_Diffusion_Models_for_3D_Shape_Reconstruction_CVPR_2024_paper.pdf#page=4), §3.3 Bayesian Diffusion Model).
- **p. 4 / 3.4. Point Cloud Prior Integration - extractive body cue:** Therefore, we employ step-wise interaction between a generative diffusion model and a reconstruction model, facilitating closer integration of point cloud priors.
- **Detected method headings:** 3. Method (p. 3); 3.2. Denoising Diffusion Probabilistic Models (p. 3); 3.3. Bayesian Diffusion Model (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | Therefore, the inference for the optimal prediction y∗can then be carried via Markov Chain Monte Carlo (MCMC) [3] using stochastic gradient Langevin ... | p. 3 (3.1. Bayesian Inference with Stochastic Gradient), p. 3 (3. Method) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | In the following section, we introduce the Bayesian Diffusion Models, the framework of which is illustrated in Fig. | p. 3 (3. Method), p. 4 (3.3. Bayesian Diffusion Model) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | The noise predicted by the model at every timestep drives the spatial distribution according to the Markov Chain state transition probability p ... | p. 4 (3.3. Bayesian Diffusion Model), p. 4 (3.4. Point Cloud Prior Integration) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.1. Bayesian Inference with Stochastic Gradient - extractive body cue:** 3 shows the basic Bayes formulation and demonstrates the stochastic gradient Langevin inference result.
- **p. 3 / 3.1. Bayesian Inference with Stochastic Gradient - extractive body cue:** 2) a mere summation for the gradients ∇log pγ(y/x) and ∇log p(yt) limits the level of interaction between the bottom-up and top-down processes.
- **p. 4 / 3.3. Bayesian Diffusion Model - extractive body cue:** 2, we use an inaccessible function Φ to incorporate the prior diffusion gradient into the reconstruction diffusion gradient.
- **p. 4 / 3.2. Denoising Diffusion Probabilistic Models - extractive body cue:** Bayesian Prediction Bayesian Diffusion Model Process Top-down (prior) Bottom-up (data-driven) … Fusion Fusion Stochastic Gradient Langevin … Prior Data-driven Figure 3.
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 3 (3.1. Bayesian Inference with Stochastic Gradient), p. 3 (3.1. Bayesian Inference with Stochastic Gradient), p. 4 (3.3. Bayesian Diffusion Model), p. 4 (3.2. Denoising Diffusion Probabilistic Models).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | task, predict, point, clouds, given, input, image, Therefore, employ, step-wise, interaction, between, generative, diffusion | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | task, predict, point, clouds, given, input, image, Therefore, employ, step-wise | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | contribution, summarized, follows, present, Bayesian, Diffusion, Models, BDM, statistical, inference | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | basic, Bayes, formulation, demonstrates, stochastic, gradient, Langevin, inference, result, mere | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Bayesian Inference with Stochastic Gradient - extractive body cue:** 1, our task is to predict y (a set of point clouds) for a given input x ∈Rq (an input image).
- **p. 4 / 3.4. Point Cloud Prior Integration - extractive body cue:** Therefore, we employ step-wise interaction between a generative diffusion model and a reconstruction model, facilitating closer integration of point cloud priors.
- **p. 4 / 3.4. Point Cloud Prior Integration - extractive body cue:** In particular, we feed the intermediate point cloud from our reconstruction model into the prior model, forward it through a certain number of timesteps in ...
- **p. 1 / 1. Introduction - extractive body cue:** Input Image PC2 (baseline) BDM-M (ours) BDM-B (ours) Figure 1.
- **p. 2 / 1. Introduction - extractive body cue:** BDM demonstrates the state-of-the-art results on the single image 3D shape reconstruction benchmarks.
- **p. 3 / 3.1. Bayesian Inference with Stochastic Gradient - extractive body cue:** For the 3D shape reconstruction task, the output y consists of a set of 3D points.
- **p. 1 / 1. Introduction - extractive body cue:** Although still being an active subject [22] in study, the top-down/prior information has not been widely adopted in the big-data/deep-learning era, where an immediate improvement ...
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | In particular, we feed the intermediate point cloud from our reconstruction model into the prior model, forward it through a certain number ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | Specifically, it is designed to estimate q(yt-1/yt), which is the offset of the points from its position at timestep t. | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not recovered | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | This integration occurs every 32 steps, both in the early stage and in the late stage of denoising. | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3.1. Bayesian Inference with Stochastic Gradient - extractive body cue:** Therefore, the inference for the optimal prediction y∗can then be carried via Markov Chain Monte Carlo (MCMC) [3] using stochastic gradient Langevin dynamics [71]: ∆yt ...
- **p. 7 / 4.3. Efficiency and Fairness Analysis - extractive body cue:** 3, we present BDM's parameters, runtime and GPU memory when doing inference with batch size of 1.
- **p. 5 / 4. Experiment - extractive body cue:** Training of generative models was conducted on 4 NVIDIA A5000 GPUs, while we trained reconstruction models utilizing a single NVIDIA A5000 GPU.

## Method-Specific Formal Details

- **Body-defined terms:** Therefore, inference, optimal, prediction, then, carried, Markov, Chain, Monte, Carlo, MCMC, stochastic, gradient, Langevin, dynamics, yt/x, data-driven, prior, where, denotes.
- **Relevant PDF headings:** 3. Method (p. 3); 3.2. Denoising Diffusion Probabilistic Models (p. 3); 3.3. Bayesian Diffusion Model (p. 4).

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | Qualitative comparisons on the real-world Pix3D dataset. | p. 7 (4.2. Qualitative Results), p. 5 (4. Experiment) |
| Denoiser / vector field | For the training of the reconstruction diffusion model, we select PC2 and CCD-3DR as two baselines and follow the recipe of CCD-3DR. | p. 5 (4. Experiment), p. 6 (4. Experiment) |
| Sampling / downstream interface | It can be seen that our method effectively improves the performance and achieves state-ofthe-art. | p. 6 (4.1. Quantitative Results), p. 6 (4.1. Quantitative Results) |

## Failure and Ablation Link

- **p. 7 / 4.4. Ablation Study - extractive body cue:** To validate the effectiveness and rationality of our BDM, we conduct several ablation studies to explore the impact of the timing, duration and intensity to ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 6. Ablation on the ratio of prior integration. This table com- pares the effects of different prior integration ratios on CD and F1.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Ablation on the timing of prior integration. This table presents the impact of applying prior integration during the early, middle, and late stages ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. Initially, a concise overview of denoising diffu- sion models, particularly focusing on point cloud diffusion models, is presented. This is followed by an ...
- **p. 8 / 5. Conclusion and Limitations - extractive body cue:** BDM overcomes the limitations in the traditional MCMC-based Bayesian inference that requires having the explicit distributions in performing stochastic gradient Langevin dynamics by tightly coupling ...
- **p. 8 / 4.4. Ablation Study - extractive body cue:** contrasts with the middle stage integration, which even degrades the performance of the baseline on F1.

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3.1. Bayesian Inference with Stochastic Gradient), p. 3 (3. Method), p. 4 (3.3. Bayesian Diffusion Model), p. 4 (3.4. Point Cloud Prior Integration), objective p. 3 (3.1. Bayesian Inference with Stochastic Gradient), p. 3 (3.1. Bayesian Inference with Stochastic Gradient), p. 4 (3.3. Bayesian Diffusion Model), p. 4 (3.2. Denoising Diffusion Probabilistic Models), temporal p. 4 (3.4. Point Cloud Prior Integration), p. 3 (3.2. Denoising Diffusion Probabilistic Models), p. 3 (3.1. Bayesian Inference with Stochastic Gradient), p. 4 (3.3. Bayesian Diffusion Model), p. 5 (4. Experiment), p. 5 (4. Experiment).
