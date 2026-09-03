# Method - Generative Gaussian Splatting: Generating 3D Scenes with Video Diffusion Priors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Schwarz_Generative_Gaussian_Splatting_Generating_3D_Scenes_with_Video_Diffusion_Priors_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Schwarz_Generative_Gaussian_Splatting_Generating_3D_Scenes_with_Video_Diffusion_Priors_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3.2. Integrating 3D Constraints), p. 3 (3.1. Pose-Conditional Image-To-Video Architecture), p. 4 (3.2. Integrating 3D Constraints), p. 5 (3.4. Splat Conditional Model), p. 4 (3.3. Decoding Latent Gaussian Splats), p. 5 (3.4. Splat Conditional Model)): Similarly to PixelSplat [5], we use the epipolar transformer to correlate features along epipolar lines via attention.

## Method Body Digest

- **p. 3 / 3.2. Integrating 3D Constraints - extractive body cue:** Similarly to PixelSplat [5], we use the epipolar transformer to correlate features along epipolar lines via attention.
- **p. 3 / 3.1. Pose-Conditional Image-To-Video Architecture - extractive body cue:** The camera encoder processes the Pl¨ucker embeddings {Pm} of the poses {pm} and outputs multi-scale camera embeddings, which are then used to condition the diffusion ...
- **p. 4 / 3.2. Integrating 3D Constraints - extractive body cue:** The images are first encoded into a latent representation {zm 0 }, which is then partitioned into K reference images and L target images.
- **p. 5 / 3.4. Splat Conditional Model - extractive body cue:** Since our model also predicts perpixel splats of relatively small size during inference, this method of approximating the 3D representation proves effective for conditional training.
- **p. 4 / 3.3. Decoding Latent Gaussian Splats - extractive body cue:** The decoder first increases the resolution of the input feature maps with a 2D upsampler.
- **p. 5 / 3.4. Splat Conditional Model - extractive body cue:** The resulting 3D representation is rendered from the target views, and the outputs are concatenated channelwise with the noisy image latents.
- **p. 4 / 3.2. Integrating 3D Constraints - extractive body cue:** This loss function minimizes the Euclidean distance between the predicted mean, µk, of each per-pixel splat and its corresponding ground truth 3D coordinate.
- **p. 3 / 3.2. Integrating 3D Constraints - extractive body cue:** 2 (right), the feature maps are further refined by a block fv with skip connections to the input. fv outputs ˆvm, i.e., the weighted sum ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** We summarize our main contributions as follows: • We propose an approach that directly integrates an explicit 3D representation with a pre-trained latent video diffusion ...
- **p. 3 / 3.2. Integrating 3D Constraints - extractive body cue:** To address this limitation, we introduce a stronger bias in the model to learn correct spatial relationships between frames.
- **p. 3 / 3. Method - extractive body cue:** We introduce Generative Gaussian Splatting (GGS) which directly synthesizes 3D-consistent scenes from one or more posed reference images.

## Source Evidence Cues

- **p. 3 / 3.2. Integrating 3D Constraints - extractive body cue:** Similarly to PixelSplat [5], we use the epipolar transformer to correlate features along epipolar lines via attention.
- **p. 3 / 3.1. Pose-Conditional Image-To-Video Architecture - extractive body cue:** The camera encoder processes the Pl¨ucker embeddings {Pm} of the poses {pm} and outputs multi-scale camera embeddings, which are then used to condition the diffusion ...
- **p. 4 / 3.2. Integrating 3D Constraints - extractive body cue:** The images are first encoded into a latent representation {zm 0 }, which is then partitioned into K reference images and L target images.
- **p. 5 / 3.4. Splat Conditional Model - extractive body cue:** Since our model also predicts perpixel splats of relatively small size during inference, this method of approximating the 3D representation proves effective for conditional training.
- **p. 4 / 3.3. Decoding Latent Gaussian Splats - extractive body cue:** The decoder first increases the resolution of the input feature maps with a 2D upsampler.
- **p. 5 / 3.4. Splat Conditional Model - extractive body cue:** The resulting 3D representation is rendered from the target views, and the outputs are concatenated channelwise with the noisy image latents.
- **Detected method headings:** 3. Method (p. 3); 3.1. Pose-Conditional Image-To-Video Architecture (p. 3); 3.4. Splat Conditional Model (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | Similarly to PixelSplat [5], we use the epipolar transformer to correlate features along epipolar lines via attention. | p. 3 (3.2. Integrating 3D Constraints), p. 3 (3.1. Pose-Conditional Image-To-Video Architecture) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | The camera encoder processes the Pl¨ucker embeddings {Pm} of the poses {pm} and outputs multi-scale camera embeddings, which are then used to ... | p. 3 (3.1. Pose-Conditional Image-To-Video Architecture), p. 4 (3.2. Integrating 3D Constraints) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | The images are first encoded into a latent representation {zm 0 }, which is then partitioned into K reference images and L ... | p. 4 (3.2. Integrating 3D Constraints), p. 5 (3.4. Splat Conditional Model) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.2. Integrating 3D Constraints - extractive body cue:** This loss function minimizes the Euclidean distance between the predicted mean, µk, of each per-pixel splat and its corresponding ground truth 3D coordinate.
- **p. 3 / 3.2. Integrating 3D Constraints - extractive body cue:** 2 (right), the feature maps are further refined by a block fv with skip connections to the input. fv outputs ˆvm, i.e., the weighted sum ...
- **p. 3 / 3.2. Integrating 3D Constraints - extractive body cue:** To better regularize the 3D representation, we add reconstruction losses LLR and Lnv,LR on the rendered low-resolution images of the input views {ˆIm LR} and ...
- **p. 4 / 3.3. Decoding Latent Gaussian Splats - extractive body cue:** The decoder is trained in a second stage, using the same losses as in Eq.
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 3 (3.2. Integrating 3D Constraints), p. 3 (3.2. Integrating 3D Constraints), p. 4 (3.3. Decoding Latent Gaussian Splats), p. 4 (3.2. Integrating 3D Constraints).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | summarize, main, contributions, follows, directly, integrates, explicit, representation, pre-trained, latent, video, diffusion, backbone, thereby | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | summarize, main, contributions, follows, directly, integrates, explicit, representation, pre-trained, latent | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | summarize, main, contributions, follows, directly, integrates, explicit, representation, pre-trained, latent | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | loss, function, minimizes, Euclidean, distance, between, predicted, mean, per-pixel, splat | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** We summarize our main contributions as follows: • We propose an approach that directly integrates an explicit 3D representation with a pre-trained latent video diffusion ...
- **p. 3 / 3. Method - extractive body cue:** The video model was trained with v-prediction, and conditioned on a single input image by concatenation of the reference latent to the input sequence, as ...
- **p. 2 / 1. Introduction - extractive body cue:** challenge is that state-of-the-art diffusion models operate on a compressed latent space, which is spatially approximately aligned with the input images but itself is not ...
- **p. 3 / 3.2. Integrating 3D Constraints - extractive body cue:** 2 (right), the feature maps are further refined by a block fv with skip connections to the input. fv outputs ˆvm, i.e., the weighted sum ...
- **p. 4 / 3.2. Integrating 3D Constraints - extractive body cue:** Model Architecture: Our approach, GGS, directly synthesizes a 3D representation, which is parameterized by a set of Gaussian splats {gm}, from a set of posed ...
- **p. 4 / 3.2. Integrating 3D Constraints - extractive body cue:** We render both feature maps {f m} and low-resolution images {Im LR} for the input views, as well as low-resolution images for J novel views ...
- **p. 5 / 3.4. Splat Conditional Model - extractive body cue:** The resulting 3D representation is rendered from the target views, and the outputs are concatenated channelwise with the noisy image latents.
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | For memory efficiency, we freeze the diffusion model and train the 3D decoder at a fixed timestep t = 0, i.e., we ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | For view interpolation, the reference images are the first and last frame of the sequence, which is the common setting in regression-based ... | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | For memory efficiency, we freeze the diffusion model and train the 3D decoder at a fixed timestep t = 0, i.e., we ... | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | RealEstate10K comprises sequences of approximately 30-100 frames from 10,000 real estate recordings, featuring smooth camera trajectories with minimal roll or pitch. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.4. Splat Conditional Model - extractive body cue:** Since our model also predicts perpixel splats of relatively small size during inference, this method of approximating the 3D representation proves effective for conditional training.
- **p. 6 / 4. Experiments - extractive body cue:** Our models were trained on 8 Nvidia A100 80GB GPUs with a batch size of 1 per GPU, using the AdamW optimizer [31] with a ...
- **p. 6 / 4. Experiments - extractive body cue:** Inference is performed with a discrete Euler scheduler using 30 steps.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Similarly, PixelSplat, epipolar, transformer, correlate, features, along, lines, attention, camera, encoder, processes, ucker, embeddings, poses, outputs, multi-scale, then, condition, diffusion.
- **Relevant PDF headings:** 3. Method (p. 3); 3.1. Pose-Conditional Image-To-Video Architecture (p. 3); 3.4. Splat Conditional Model (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | Despite the similar name, ScanNet++ features different cameras and scenes from ScanNet, allowing us to assess the generalization of our method in ... | p. 5 (4. Experiments), p. 5 (4. Experiments) |
| Denoiser / vector field | Baseline Comparison Given One Reference Image: We show results for the strongest baselines CameraCtrl [15] and ViewCrafter[76] together with our approach without ... | p. 7 (4.2. Scene Synthesis From Two Images), p. 6 (4.2. Scene Synthesis From Two Images) |
| Sampling / downstream interface | On RealEstate10K, our approach significantly improves image quality and 3D consistency over the baselines. | p. 6 (4.1. Scene Synthesis From a Single Image), p. 8 (4.3. Autoregressive Scene Synthesis) |

## Failure and Ablation Link

- **p. 8 / 4.4. Ablation Studies - extractive body cue:** Ablation Studies: We investigate the effectiveness of our design choices on RealEstate10K using two reference images. imation with a Gaussian distribution works better when depth ...
- **p. 5 / 4. Experiments - extractive body cue:** Following [68], we also use a variant of RealEstate10K with rescaled camera poses to be approximately metric.
- **p. 5 / 4. Experiments - extractive body cue:** For a fair comparison of a model with and without an intermediate 3D representation, we train our own purely pose-conditional model (Ours-No3D) as described in ...
- **p. 6 / 4. Experiments - extractive body cue:** The ablation studies are reported after training the models for 75K iterations.
- **p. 6 / 4.2. Scene Synthesis From Two Images - extractive body cue:** Additionally, we train a refined variant, for which we initialize Splatfacto with the generated splats and run it for 5,000 iterations per scene to obtain ...
- **p. 7 / 4.3. Autoregressive Scene Synthesis - extractive body cue:** To extend our model from two to an arbitrary number of input views, we train a conditional variant to autoregressively generate a full scene ( ...
- **p. 7 / 4.2. Scene Synthesis From Two Images - extractive body cue:** Baseline Comparison Given One Reference Image: We show results for the strongest baselines CameraCtrl [15] and ViewCrafter[76] together with our approach without (Ours-No3D) and with ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3.2. Integrating 3D Constraints), p. 3 (3.1. Pose-Conditional Image-To-Video Architecture), p. 4 (3.2. Integrating 3D Constraints), p. 5 (3.4. Splat Conditional Model), p. 4 (3.3. Decoding Latent Gaussian Splats), p. 5 (3.4. Splat Conditional Model), objective p. 4 (3.2. Integrating 3D Constraints), p. 3 (3.2. Integrating 3D Constraints), p. 3 (3.2. Integrating 3D Constraints), p. 4 (3.3. Decoding Latent Gaussian Splats), temporal p. 4 (3.3. Decoding Latent Gaussian Splats), p. 5 (4. Experiments), p. 5 (4. Experiments), p. 3 (3.1. Pose-Conditional Image-To-Video Architecture), p. 3 (3.2. Integrating 3D Constraints), p. 4 (3.3. Decoding Latent Gaussian Splats).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
