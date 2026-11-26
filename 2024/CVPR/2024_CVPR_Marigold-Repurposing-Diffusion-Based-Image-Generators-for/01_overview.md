# Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (33 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2312.02145.
> PDF retrieval source: https://arxiv.org/pdf/2312.02145. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: Bingxin Ke, Anton Obukhov, Shengyu Huang, Nando Metzger, Rodrigo Caye Daudt, Konrad Schindler
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Diffusion, monocular depth, 3D Vision
- Official paper: https://arxiv.org/abs/2312.02145
- Full-text retrieval: https://arxiv.org/pdf/2312.02145
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (33 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

Marigold는 사전학습된 텍스트·영상 확산 모델을 재사용해 단안 RGB 영상의 스케일과 오프셋에 불변인 깊이를 추정한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Ke_Repurposing_Diffusion-Based_Image_Generators_for_Monocular_Depth_Estimation_CVPR_2024_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Monocular depth estimation is a fundamental computer vision task.
- **p. 1 / Abstract - extractive body cue:** Recovering 3D depth from a single image is geometrically ill-posed and requires scene understanding, so it is not surprising that the rise of deep learning ...
- **p. 1 / Abstract - extractive body cue:** The impressive progress of monocular depth estimators has mirrored the growth in model capacity, from relatively modest CNNs to large Transformer architectures.
- **p. 1 / Abstract - extractive body cue:** Still, monocular depth estimators tend to struggle when presented with images with unfamiliar content and layout, since their knowledge of the visual world is restricted ...
- **p. 1 / Abstract - extractive body cue:** This motivates us to explore whether the extensive priors captured in recent generative diffusion models can enable better, more generalizable depth estimation.
- **p. 2 / 1. Introduction - extractive body cue:** Empowered by the underlying diffusion prior of natural images, Marigold exhibits excellent zero-shot generalization: Without ever having seen real depth maps, it attains state-ofthe-art performance ...
- **p. 1 / 1. Introduction - extractive body cue:** Clearly, undoing the projection from the 3D world to a 2D image is a geometrically ill-posed problem and can 1.

## Core Idea

- **p. 5 / 3.4. Inference - extractive body cue:** Capitalizing on that, we propose the following test-time ensembling scheme, capable of combining multiple inference passes over the same input.
- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our contributions are: 1.
- **p. 5 / 3.4. Inference - extractive body cue:** This scheme enables a flexible trade-off between computation efficiency and prediction quality by choosing N accordingly.
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we set out to explore this option and develop Marigold, a latent diffusion model (LDM) based on Stable Diffusion [38], along with ...
- **p. 4 / 3.3. Fine-Tuning Protocol - extractive body cue:** This normalization allows Marigold to focus on pure affine-invariant depth estimation.
- **p. 4 / 3.2. Network Architecture - extractive body cue:** One of our main objectives is training efficiency since diffusion models are often extremely resource-intensive to train.
- **p. 4 / 3.1. Generative Formulation - extractive body cue:** The adapted inference procedure involves one extra step - the decoder D reconstructing the data ˆd from the estimated clean latent z(d) 0 : ˆd ...
- **p. 3 / 3.1. Generative Formulation - extractive body cue:** At training time, parameters θ are updated by taking a data pair (x, d) from the training set, noising d with sampled noise ϵ at ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given that the encoder, which is designed for 3-channel (RGB) inputs, receives a single-channel depth map, we replicate the depth map into three channels to simulate an RGB image. | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3.2. Network Architecture), p. 4 (3.2. Network Architecture) |
| State/latent | Given, encoder, designed, channel, RGB, inputs, receives, single-channel, depth, replicate, three, channels | geometry, map, object/relationship state | p. 4 (3.2. Network Architecture), p. 4 (3.2. Network Architecture), p. 5 (3.3. Fine-Tuning Protocol) |
| Output/action | To implement the conditioning of the latent denoiser ϵθ(z(d) t , z(x), t) on input image x, we concatenate the image and depth latent codes into a single input zt = cat(z(d) ... | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.2. Network Architecture), p. 5 (3.3. Fine-Tuning Protocol), p. 5 (3.4. Inference) |
| Objective/outcome | At training time, parameters θ are updated by taking a data pair (x, d) from the training set, noising d with sampled noise ϵ at a random timestep t, computing the noise ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (3.1. Generative Formulation), p. 5 (3.4. Inference), p. 4 (3.1. Generative Formulation) |

## Main Claims and Actual Contribution

- 영상과 깊이를 잠재공간에 인코딩해 합성 RGB·깊이 쌍으로 조건부 잡음 제거를 학습한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Ke_Repurposing_Diffusion-Based_Image_Generators_for_Monocular_Depth_Estimation_CVPR_2024_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Ke_Repurposing_Diffusion-Based_Image_Generators_for_Monocular_Depth_Estimation_CVPR_2024_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Ke_Repurposing_Diffusion-Based_Image_Generators_for_Monocular_Depth_Estimation_CVPR_2024_paper.pdf#page=5)
- 추론 표본을 정렬·결합하는 방식과 여러 실측 데이터셋에서 추가 학습 없이 얻은 깊이 오차를 평가했다. [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Ke_Repurposing_Diffusion-Based_Image_Generators_for_Monocular_Depth_Estimation_CVPR_2024_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Ke_Repurposing_Diffusion-Based_Image_Generators_for_Monocular_Depth_Estimation_CVPR_2024_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Ke_Repurposing_Diffusion-Based_Image_Generators_for_Monocular_Depth_Estimation_CVPR_2024_paper.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies) |
| Embodiment/environment | In the case of the ScanNet dataset, we randomly sampled 800 images from the 312 official validation scenes for testing. | hardware/simulator version and reset protocol | p. 6 (4.2. Evaluation), p. 6 (4.2. Evaluation) |
| Dataset/benchmark | When fine-tuned on a single synthetic dataset, the pretrained LDM can already be adapted for monocular depth estimation to a certain degree, while the more diverse and photorealistic data leads to better ... | role, split, size and leakage | p. 6 (4.2. Evaluation), p. 6 (4.2. Evaluation), p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies) |
| Metric | All metrics† are presented in percentage terms; bold numbers are the best, underscored second best. | definition, denominator, direction and uncertainty | p. 6 (4.1. Implementation), p. 6 (4.2. Evaluation), p. 8 (4.3. Ablation Studies) |
| Baseline/ablation | Table 1. Quantitative comparison of Marigold with SOTA affine-invariant depth estimators on several zero-shot benchmarks. All metrics† are presented in percentage terms; bold numbers are the best, underscored second best. Our method ... | fair input/data/compute/action matching | p. 6 (Figure/Table caption), p. 6 (4.2. Evaluation), p. 1 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** Future research directions to overcome current limitations include improving inference efficiency, ensuring that similar inputs yield consistent outputs despite the model's generative nature, and better ...
- **p. 5 / 4.1. Implementation - extractive body cue:** During training, we apply the DDPM noise scheduler [20] with 1000 diffusion steps.
- **p. 5 / 4.1. Implementation - extractive body cue:** For the final prediction, we aggregate results from 10 inference runs with varying starting noise.
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** We investigate the impact of three types of noise during the training phase.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 1 (1. Introduction), p. 5 (3.4. Inference), p. 4 (3.2. Network Architecture), p. 4 (3.1. Generative Formulation)이다.
