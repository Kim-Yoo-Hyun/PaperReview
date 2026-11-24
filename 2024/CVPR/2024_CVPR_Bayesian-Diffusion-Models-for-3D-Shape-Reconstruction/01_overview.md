# Bayesian Diffusion Models for 3D Shape Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Xu_Bayesian_Diffusion_Models_for_3D_Shape_Reconstruction_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Xu_Bayesian_Diffusion_Models_for_3D_Shape_Reconstruction_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: Haiyang Xu, Yu Lei, Zeyuan Chen, Xiang Zhang, Yue Zhao, Yilin Wang, Zhuowen Tu
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Xu_Bayesian_Diffusion_Models_for_3D_Shape_Reconstruction_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Xu_Bayesian_Diffusion_Models_for_3D_Shape_Reconstruction_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/CVPR2024/papers/Xu_Bayesian_Diffusion_Models_for_3D_Shape_Reconstruction_CVPR_2024_paper.pdf)

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

Bayesian Diffusion Models는 단일 영상의 증거와 학습한 3D 형상 사전분포를 결합해 한 뷰에서 결정하기 어려운 물체의 점군을 복원한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Xu_Bayesian_Diffusion_Models_for_3D_Shape_Reconstruction_CVPR_2024_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Xu_Bayesian_Diffusion_Models_for_3D_Shape_Reconstruction_CVPR_2024_paper.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present Bayesian Diffusion Models (BDM), a prediction algorithm that performs effective Bayesian inference by tightly coupling the top-down (prior) information with the bottom-up (data-driven) ...
- **p. 1 / Abstract - extractive body cue:** We show the effectiveness of BDM on the 3D shape reconstruction task.
- **p. 1 / Abstract - extractive body cue:** Compared to prototypical deep learning data-driven approaches trained on paired (supervised) data-labels (e.g. image-point clouds) datasets, our BDM brings in rich prior information from standalone ...
- **p. 1 / Abstract - extractive body cue:** As opposed to the standard Bayesian frameworks where explicit prior and likelihood are required for the inference, BDM performs seamless information fusion via coupled diffusion ...
- **p. 1 / Abstract - extractive body cue:** The specialty of our BDM lies in its capability to engage the active and effective information exchange and fusion of the top-down and bottom-up processes ...
- **p. 1 / 1. Introduction - extractive body cue:** Our BDM brings rich prior knowledge into the shape reconstruction process, fixing the incorrect predictions by the baseline (top row).
- **p. 1 / 1. Introduction - extractive body cue:** The topdown prior [20, 66] can therefore provide a strong regularization and inductive bias to the bottom-up process that has been trained from the data ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** The contribution of our paper is summarized as follows: • We present Bayesian Diffusion Models (BDM), a new statistical inference algorithm that couples diffusionbased bottom-up ...
- **p. 3 / 3.1. Bayesian Inference with Stochastic Gradient - extractive body cue:** For the 3D shape reconstruction task, the output y consists of a set of 3D points.
- **p. 3 / 3. Method - extractive body cue:** In the following section, we introduce the Bayesian Diffusion Models, the framework of which is illustrated in Fig.
- **p. 4 / 3.4. Point Cloud Prior Integration - extractive body cue:** As below we introduce two fusion methods: BDM-M (Merging) and BDM-B (Blending).
- **p. 4 / 3.2. Denoising Diffusion Probabilistic Models - extractive body cue:** We present the standard Bayesian formulation and the one using stochastic gradient Langevin on the top part, while our proposed BDM on the bottom. q(yt-1/yt, ...
- **p. 3 / 3.1. Bayesian Inference with Stochastic Gradient - extractive body cue:** Therefore, the inference for the optimal prediction y∗can then be carried via Markov Chain Monte Carlo (MCMC) [3] using stochastic gradient Langevin dynamics [71]: ∆yt ...
- **원문 대조:** Prior diffusion model의 noise 예측은 reverse Markov transition p(y^t ∣ y^{t+1})을 통해 point-cloud 분포를 갱신한다. Reconstruction model의 image-conditioned transition과 구분해 두 경로의 정보를 결합한다. ([PDF p. 4](https://openaccess.thecvf.com/content/CVPR2024/papers/Xu_Bayesian_Diffusion_Models_for_3D_Shape_Reconstruction_CVPR_2024_paper.pdf#page=4), §3.3 Bayesian Diffusion Model).
- **p. 4 / 3.4. Point Cloud Prior Integration - extractive body cue:** Therefore, we employ step-wise interaction between a generative diffusion model and a reconstruction model, facilitating closer integration of point cloud priors.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 1, our task is to predict y (a set of point clouds) for a given input x ∈Rq (an input image). | conditioning observation와 noisy/intermediate sample | p. 3 (3.1. Bayesian Inference with Stochastic Gradient), p. 4 (3.4. Point Cloud Prior Integration) |
| State/latent | task, predict, point, clouds, given, input, image, Therefore, employ, step-wise, interaction, between | latent/noise variable와 conditional distribution | p. 3 (3.1. Bayesian Inference with Stochastic Gradient), p. 4 (3.4. Point Cloud Prior Integration), p. 4 (3.4. Point Cloud Prior Integration) |
| Output/action | Therefore, we employ step-wise interaction between a generative diffusion model and a reconstruction model, facilitating closer integration of point cloud priors. | generated sample, action chunk 또는 trajectory | p. 4 (3.4. Point Cloud Prior Integration), p. 4 (3.4. Point Cloud Prior Integration), p. 1 (1. Introduction) |
| Objective/outcome | 3 shows the basic Bayes formulation and demonstrates the stochastic gradient Langevin inference result. | distribution fit, multimodality, sample quality와 latency | p. 3 (3.1. Bayesian Inference with Stochastic Gradient), p. 3 (3.1. Bayesian Inference with Stochastic Gradient), p. 4 (3.3. Bayesian Diffusion Model) |

## Main Claims and Actual Contribution

- 영상 조건부 상향식 모델과 형상 사전분포를 학습한 하향식 모델의 역확산 과정을 결합하는 방법을 제시했다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Xu_Bayesian_Diffusion_Models_for_3D_Shape_Reconstruction_CVPR_2024_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Xu_Bayesian_Diffusion_Models_for_3D_Shape_Reconstruction_CVPR_2024_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Xu_Bayesian_Diffusion_Models_for_3D_Shape_Reconstruction_CVPR_2024_paper.pdf#page=5)
- 합성 및 실제 물체 영상에서 형상 오차를 비교하고 훈련 자료의 양이 달라질 때 점군 거리와 F-score의 변화를 분석했다. [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Xu_Bayesian_Diffusion_Models_for_3D_Shape_Reconstruction_CVPR_2024_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Xu_Bayesian_Diffusion_Models_for_3D_Shape_Reconstruction_CVPR_2024_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Xu_Bayesian_Diffusion_Models_for_3D_Shape_Reconstruction_CVPR_2024_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4.1. Quantitative Results), p. 6 (4.1. Quantitative Results) |
| Embodiment/environment | Qualitative comparisons on the real-world Pix3D dataset. | hardware/simulator version and reset protocol | p. 7 (4.2. Qualitative Results), p. 5 (4. Experiment) |
| Dataset/benchmark | Pix3D comprises diverse real-world image-shape pairs with meticulously annotated 2D-3D alignments. | role, split, size and leakage | p. 7 (4.2. Qualitative Results), p. 5 (4. Experiment), p. 5 (4. Experiment), p. 6 (4. Experiment) |
| Metric | In this metric, a reconstructed point is deemed accurately predicted if its nearest distance to the points in the ground truth point cloud is within the specified threshold, which presents a measure ... | definition, denominator, direction and uncertainty | p. 6 (4.1. Quantitative Results), p. 6 (4.1. Quantitative Results), p. 8 (4.6. Human Evaluation) |
| Baseline/ablation | For the training of the reconstruction diffusion model, we select PC2 and CCD-3DR as two baselines and follow the recipe of CCD-3DR. | fair input/data/compute/action matching | p. 5 (4. Experiment), p. 6 (4. Experiment), p. 6 (4. Experiment) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion and Limitations - extractive body cue:** BDM overcomes the limitations in the traditional MCMC-based Bayesian inference that requires having the explicit distributions in performing stochastic gradient Langevin dynamics by tightly coupling ...
- **p. 8 / 4.4. Ablation Study - extractive body cue:** contrasts with the middle stage integration, which even degrades the performance of the baseline on F1.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Bayesian Inference with Stochastic Gradient), p. 3 (3. Method)이다.
