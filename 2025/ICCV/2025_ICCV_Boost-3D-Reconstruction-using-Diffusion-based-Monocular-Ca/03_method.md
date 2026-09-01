# Method - Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Deng_Boost_3D_Reconstruction_using_Diffusion-based_Monocular_Camera_Calibration_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Deng_Boost_3D_Reconstruction_using_Diffusion-based_Monocular_Camera_Calibration_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3.4. Downstream 3D vision tasks), p. 5 (3.4. Downstream 3D vision tasks), p. 3 (3. Method), p. 4 (3.2. Camera Image Representation), p. 3 (3.1. Preliminaries on Diffusion Model), p. 4 (3.3. Camera Intrinsic Estimation)): Then, the latent features are sent to the UNet to predict the latent depth features ˆzd, and the final depth predictions ˆd are obtained via the decoder of the VAE.

## Method Body Digest

- **p. 5 / 3.4. Downstream 3D vision tasks - extractive PDF cue:** Then, the latent features are sent to the UNet to predict the latent depth features ˆzd, and the final depth predictions ˆd are obtained via ...
- **p. 5 / 3.4. Downstream 3D vision tasks - extractive PDF cue:** Specifically, we first encode RGB image and our designed camera image ˆc via VAE encoder into latent space, noting that no noise is added to ...
- **p. 3 / 3. Method - extractive PDF cue:** To efficiently and losslessly integrate camera intrinsics prediction with diffusion models [53], we introduce Camera Image (Fig.
- **p. 4 / 3.2. Camera Image Representation - extractive PDF cue:** To enhance the camera representation, we propose a simple yet effective solution by incorporating the grayscale image g of the input x into the dense ...
- **p. 3 / 3.1. Preliminaries on Diffusion Model - extractive PDF cue:** [53] introduced latent diffusion models (LDMs), which operate the diffusion process in the latent space of a pretrained variational autoencoder (VAE) [34] with an encoder ...
- **p. 4 / 3.3. Camera Intrinsic Estimation - extractive PDF cue:** After completing the multi-step denoising process using the U-Net, the denoised camera latent representation ˆzc is sent to the frozen VAE decoder, yielding the final ...
- **p. 3 / 3.1. Preliminaries on Diffusion Model - extractive PDF cue:** The whole diffusion model is optimized by minimizing the denoising score matching objective, defined as Ez,ϵ,t  ∥ϵ -ϵθ(zt, t)∥2 2  .
- **p. 3 / 3.1. Preliminaries on Diffusion Model - extractive PDF cue:** By minimizing this objective, the denoising network learns to accurately estimate the noise, thereby effectively reversing the diffusion process and reconstructing the original data distribution.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** To summarize, our main contributions are: • We introduce the Camera Image, a novel image-based representation specifically designed to encode camera intrinsic, optimized to use ...
- **p. 4 / 3.2. Camera Image Representation - extractive PDF cue:** To address this challenge, we propose a novel imagebased representation, called "Camera Image", which encodes the camera intrinsic parameters into a 3-channel color image (refer ...
- **p. 1 / 1. Introduction - extractive PDF cue:** 1, we present two portrait This ICCV paper is the Open Access version, provided by the Computer Vision Foundation.

## Source Evidence Cues

- **p. 5 / 3.4. Downstream 3D vision tasks - extractive PDF cue:** Then, the latent features are sent to the UNet to predict the latent depth features ˆzd, and the final depth predictions ˆd are obtained via ...
- **p. 5 / 3.4. Downstream 3D vision tasks - extractive PDF cue:** Specifically, we first encode RGB image and our designed camera image ˆc via VAE encoder into latent space, noting that no noise is added to ...
- **p. 3 / 3. Method - extractive PDF cue:** To efficiently and losslessly integrate camera intrinsics prediction with diffusion models [53], we introduce Camera Image (Fig.
- **p. 4 / 3.2. Camera Image Representation - extractive PDF cue:** To enhance the camera representation, we propose a simple yet effective solution by incorporating the grayscale image g of the input x into the dense ...
- **p. 3 / 3.1. Preliminaries on Diffusion Model - extractive PDF cue:** [53] introduced latent diffusion models (LDMs), which operate the diffusion process in the latent space of a pretrained variational autoencoder (VAE) [34] with an encoder ...
- **p. 4 / 3.3. Camera Intrinsic Estimation - extractive PDF cue:** After completing the multi-step denoising process using the U-Net, the denoised camera latent representation ˆzc is sent to the frozen VAE decoder, yielding the final ...
- **Detected method headings:** 2.2. Diffusion Models in 3D tasks (p. 3); 3. Method (p. 3); 3.1. Preliminaries on Diffusion Model (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Then, the latent features are sent to the UNet to predict the latent depth features ˆzd, and the final depth predictions ˆd ... | p. 5 (3.4. Downstream 3D vision tasks), p. 5 (3.4. Downstream 3D vision tasks) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Specifically, we first encode RGB image and our designed camera image ˆc via VAE encoder into latent space, noting that no noise ... | p. 5 (3.4. Downstream 3D vision tasks), p. 3 (3. Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | To efficiently and losslessly integrate camera intrinsics prediction with diffusion models [53], we introduce Camera Image (Fig. | p. 3 (3. Method), p. 4 (3.2. Camera Image Representation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.1. Preliminaries on Diffusion Model - extractive PDF cue:** The whole diffusion model is optimized by minimizing the denoising score matching objective, defined as Ez,ϵ,t  ∥ϵ -ϵθ(zt, t)∥2 2  .
- **p. 3 / 3.1. Preliminaries on Diffusion Model - extractive PDF cue:** By minimizing this objective, the denoising network learns to accurately estimate the noise, thereby effectively reversing the diffusion process and reconstructing the original data distribution.
- **p. 4 / 3.3. Camera Intrinsic Estimation - extractive PDF cue:** The U-Net is targeted to predict the added noise, and the final loss function is expressed as: \mathcal {L} = \ma thbb {E } _ ...
- **p. 5 / 3.3. Camera Intrinsic Estimation - extractive PDF cue:** Stable Diffusion U-Net t 𝒄𝒄 𝒙𝒙 𝒛𝒛𝒙𝒙 𝒛𝒛c Concat 𝒛𝒛𝒕𝒕 𝒄𝒄 𝒛𝒛𝒙𝒙 𝝐𝝐 ෝ𝝐𝝐 Predicted Noise 𝝐𝝐 Added Noise Training Objective
- **p. 5 / 3.4. Downstream 3D vision tasks - extractive PDF cue:** Given the depth labels d with its sparse mask M, the training loss is given by: \mat h cal {L}_{\t ex t {depth} } = ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3. Method), p. 3 (3.1. Preliminaries on Diffusion Model), p. 4 (3.3. Camera Intrinsic Estimation), p. 5 (3.3. Camera Intrinsic Estimation), p. 5 (3.4. Downstream 3D vision tasks).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | input, RGB, image, incidence, Camera, reference, enhance, representation, simple, effective, solution, incorporating, grayscale, dense | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | input, RGB, image, incidence, Camera, reference, enhance, representation, simple, effective | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summarize, main, contributions, introduce, Camera, Image, novel, image-based, representation, specifically | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | whole, diffusion, model, optimized, minimizing, denoising, score, matching, objective, defined | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. Camera Image Representation - extractive PDF cue:** We show the input RGB image, the incidence map and our proposed Camera Image for reference.
- **p. 4 / 3.2. Camera Image Representation - extractive PDF cue:** To enhance the camera representation, we propose a simple yet effective solution by incorporating the grayscale image g of the input x into the dense ...
- **p. 3 / 3. Method - extractive PDF cue:** Given a single input image x ∈RH×W ×3, our objective is to recover its camera intrinsic matrix K.
- **p. 3 / 3.1. Preliminaries on Diffusion Model - extractive PDF cue:** For any given input image x, the corresponding latent code is generated by the VAE encoder: z = E(x).
- **p. 5 / 3.3. Camera Intrinsic Estimation - extractive PDF cue:** The input image x and the camera image c are first encoded into latent space using a frozen VAE encoder.
- **p. 5 / 3.4. Downstream 3D vision tasks - extractive PDF cue:** By leveraging the proposed camera calibration method, we repurpose diffusionbased image generators for accurate metric depth estimation.
- **p. 2 / 1. Introduction - extractive PDF cue:** Subsequently, we train a diffusion model that takes a single image as input and generates the Camera Image, followed by a RANSAC algorithm to solve ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | The forward diffusion process incrementally adds noise to these latents following zt := αtz + σtϵ, where ϵ ∼N(0, I), and αt ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | This is achieved by predicting the noise component ϵθ(zt, t) at each diffusion step. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3.1. Preliminaries on Diffusion Model - extractive PDF cue:** [53] introduced latent diffusion models (LDMs), which operate the diffusion process in the latent space of a pretrained variational autoencoder (VAE) [34] with an encoder ...
- **p. 7 / 4.5. Ablation Study - extractive PDF cue:** Ablation NYU-v2 KITTI δ1 ↑ SIlog ↓ A.Rel ↓ δ1 ↑ SIlog ↓ A.Rel ↓ Full Model 85.8 8.17 13.5 89.1 13.3 11.7 w.o Real ...
- **p. 8 / 4.5. Ablation Study - extractive PDF cue:** Additionally, prior methods that froze the VAE decoder during one-step training have shown to be inadequate for metric depth estimation, as demonstrated in our experiments.
- **p. 4 / 3.3. Camera Intrinsic Estimation - extractive PDF cue:** This code is concatenated with zx, serving as the input for the pretrained U-Net.
- **p. 5 / 3.3. Camera Intrinsic Estimation - extractive PDF cue:** Pre-trained Latent Encoder ℰ Add Noise by Timestamp 𝑡𝑡
- **p. 5 / 3.4. Downstream 3D vision tasks - extractive PDF cue:** Note that both U-Net U and the VAE decoder D are trained to allow predictions in any range.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Then, latent, features, sent, UNet, predict, depth, final, predictions, obtained, decoder, VAE, Specifically, first, encode, RGB, image, designed, camera, encoder.
- **Relevant PDF headings:** 2.2. Diffusion Models in 3D tasks (p. 3); 3. Method (p. 3); 3.1. Preliminaries on Diffusion Model (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | For camera intrinsic estimation, the training data is sourced from a variety of datasets, including NuScenes [7], KITTI [19], CityScapes [11], NYUv2 ... | p. 5 (4.1. Experimental Setup), p. 6 (4.2. Camera Intrinsic Evaluation) |
| Semantic / temporal fusion | Our work significantly outperforms strong baselines such as Metric3D [85] by a large margin, and achieves comparable performance with the SOTA work ... | p. 6 (4.3. Depth Evaluation), p. 6 (4.1. Experimental Setup) |
| Robot query / planning handoff | Our work significantly outperforms strong baselines such as Metric3D [85] by a large margin, and achieves comparable performance with the SOTA work ... | p. 6 (4.3. Depth Evaluation), p. 7 (4.4. More 3D Vision Tasks) |

## Failure and Ablation Link

- **p. 7 / 4.5. Ablation Study - extractive PDF cue:** We evaluate the effectiveness of our proposed camera image representation and multi-resolution noise strategy through an ablation study on the GSV dataset [2], which includes ...
- **p. 6 / 4.4. More 3D Vision Tasks - extractive PDF cue:** [73] on our self-captured images with and without our estimated intrinsics.
- **p. 6 / 4.3. Depth Evaluation - extractive PDF cue:** Despite being designed for metric depth, our model achieves performance comparable to methods tailored for affine-invariant depth.
- **p. 7 / 4.5. Ablation Study - extractive PDF cue:** Ablation on Metric Depth Estimation.
- **p. 8 / 4.5. Ablation Study - extractive PDF cue:** Zero-shot qualitative affine-invariant depth results.
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. The overview training framework of DM-Calib. The input image x and the camera image c are first encoded into latent space using a ...
- **p. 8 / 5. Conclusion - extractive PDF cue:** Future work could address ultra-wide-angle images by incorporating more diverse training data and improve inference efficiency by developing a few-step diffusion [42] model to further ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3.4. Downstream 3D vision tasks), p. 5 (3.4. Downstream 3D vision tasks), p. 3 (3. Method), p. 4 (3.2. Camera Image Representation), p. 3 (3.1. Preliminaries on Diffusion Model), p. 4 (3.3. Camera Intrinsic Estimation), objective p. 3 (3.1. Preliminaries on Diffusion Model), p. 3 (3.1. Preliminaries on Diffusion Model), p. 4 (3.3. Camera Intrinsic Estimation), p. 5 (3.3. Camera Intrinsic Estimation), p. 5 (3.4. Downstream 3D vision tasks), temporal p. 3 (3.1. Preliminaries on Diffusion Model), p. 3 (3.1. Preliminaries on Diffusion Model), p. 4 (3.3. Camera Intrinsic Estimation), p. 4 (3.2. Camera Image Representation), p. 5 (3.3. Camera Intrinsic Estimation), p. 5 (3.4. Downstream 3D vision tasks).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
