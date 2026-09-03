# Method - HandDiff: 3D Hand Pose Estimation with Diffusion on Image-Point Cloud

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Cheng_HandDiff_3D_Hand_Pose_Estimation_with_Diffusion_on_Image-Point_Cloud_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Cheng_HandDiff_3D_Hand_Pose_Estimation_with_Diffusion_on_Image-Point_Cloud_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3. The Proposed Hand Pose Diffusion Model), p. 3 (3.2. Joint-wise Local Feature-conditioned Denoiser), p. 5 (3.3. Training), p. 5 (3.3. Training)): The depth image and the N points are first supplied into a local condition encoder that extracts local and global features.

## Method Body Digest

- **p. 3 / 3. The Proposed Hand Pose Diffusion Model - extractive body cue:** The depth image and the N points are first supplied into a local condition encoder that extracts local and global features.
- **p. 3 / 3.2. Joint-wise Local Feature-conditioned Denoiser - extractive body cue:** (1) The denoiser consists of the following elements: 1) a local feature sampler, 2) a joint indicator & timestep embedding, 3) a kinematic correspondence-aware aggregation ...
- **p. 5 / 3.3. Training - extractive body cue:** Following previous regression works [9, 35], we adopt a smooth L1 loss to supervise training because of its less sensitivity to outliers.
- **p. 5 / 3.3. Training - extractive body cue:** Besides, the joint-wise conditions have to be initialized through training.
- **p. 5 / 3.3. Training - extractive body cue:** (7) By using the smooth L1 loss, we supervise the approximated joint distribution by the following joint loss function:
- **p. 1 / 1. Introduction - extractive body cue:** The model extracts features from input depth images and corresponding point clouds as joint-wise and local conditions to guide the iterative denoising process that recovers ...
- **p. 2 / 1. Introduction - extractive body cue:** The following is a summary of our primary contributions: • We propose a novel diffusion-based model for hand pose estimation that utilizes the depth image ...
- **p. 2 / 1. Introduction - extractive body cue:** To fully exploit the potential of the diffusion model in hand pose estimation, we propose HandDiff, a novel approach that incrementally refines the noise distribution ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** The following is a summary of our primary contributions: • We propose a novel diffusion-based model for hand pose estimation that utilizes the depth image ...
- **p. 2 / 1. Introduction - extractive body cue:** This model progressively denoises a noise distribution, accurately determining the 3D coordinates of hand joints. • We propose a novel joint-wise local feature-aware denoising module ...
- **p. 3 / 3.2. Joint-wise Local Feature-conditioned Denoiser - extractive body cue:** In order to differentiate between different joints and levels of noise, we introduce a joint indicator and a time-step embedding, respectively.

## Source Evidence Cues

- **p. 3 / 3. The Proposed Hand Pose Diffusion Model - extractive body cue:** The depth image and the N points are first supplied into a local condition encoder that extracts local and global features.
- **p. 3 / 3.2. Joint-wise Local Feature-conditioned Denoiser - extractive body cue:** (1) The denoiser consists of the following elements: 1) a local feature sampler, 2) a joint indicator & timestep embedding, 3) a kinematic correspondence-aware aggregation ...
- **p. 5 / 3.3. Training - extractive body cue:** Following previous regression works [9, 35], we adopt a smooth L1 loss to supervise training because of its less sensitivity to outliers.
- **p. 5 / 3.3. Training - extractive body cue:** Besides, the joint-wise conditions have to be initialized through training.
- **Detected method headings:** 3. The Proposed Hand Pose Diffusion Model (p. 3); 4.3. Comparison with State-of-the-Art Methods (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | The depth image and the N points are first supplied into a local condition encoder that extracts local and global features. | p. 3 (3. The Proposed Hand Pose Diffusion Model), p. 3 (3.2. Joint-wise Local Feature-conditioned Denoiser) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | (1) The denoiser consists of the following elements: 1) a local feature sampler, 2) a joint indicator & timestep embedding, 3) a ... | p. 3 (3.2. Joint-wise Local Feature-conditioned Denoiser), p. 5 (3.3. Training) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | Following previous regression works [9, 35], we adopt a smooth L1 loss to supervise training because of its less sensitivity to outliers. | p. 5 (3.3. Training), p. 5 (3.3. Training) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.3. Training - extractive body cue:** (7) By using the smooth L1 loss, we supervise the approximated joint distribution by the following joint loss function:
- **p. 5 / 3.3. Training - extractive body cue:** Following previous regression works [9, 35], we adopt a smooth L1 loss to supervise training because of its less sensitivity to outliers.
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 5 (3.3. Training), p. 5 (3.3. Training).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | model, extracts, features, input, depth, images, corresponding, point, clouds, joint-wise, local, conditions, guide, iterative | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | model, extracts, features, input, depth, images, corresponding, point, clouds, joint-wise | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | following, summary, primary, contributions, novel, diffusion-based, model, hand, pose, estimation | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | smooth, loss, supervise, approximated, joint, distribution, following, function, previous, regression | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1. Introduction - extractive body cue:** The model extracts features from input depth images and corresponding point clouds as joint-wise and local conditions to guide the iterative denoising process that recovers ...
- **p. 2 / 1. Introduction - extractive body cue:** The following is a summary of our primary contributions: • We propose a novel diffusion-based model for hand pose estimation that utilizes the depth image ...
- **p. 2 / 1. Introduction - extractive body cue:** To fully exploit the potential of the diffusion model in hand pose estimation, we propose HandDiff, a novel approach that incrementally refines the noise distribution ...
- **p. 3 / 3. The Proposed Hand Pose Diffusion Model - extractive body cue:** HandDiff is a diffusion model that takes a 3D normal distribution and a hand depth image as input and produces the coordinates of the hand ...
- **p. 3 / 3. The Proposed Hand Pose Diffusion Model - extractive body cue:** The input to HandDiff is a hand depth image Din ∈RH×W with a set of sampled 3D point coordinates Pin ∈RN×3, and the outputs are ...
- **p. 1 / 1. Introduction - extractive body cue:** Based on this inspiration, we apply the diffusion model in generating hand keypoint locations conditioned on the hand depth image/point cloud input, as illustrated in ...
- **p. 5 / 3.3. Training - extractive body cue:** Subsequently, the noisy joint distribution is supplied to the proposed denoiser to recover the clean joint distribution eJ(0/t), under the joint-wise conditions as well as ...
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | In addition, the computation time and memory of the model are 98 ms and 2.2GB per frame, respectively, for 10 timesteps (1 ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | The diffusion timestep was set to 500 with a cosine variance scheduler. | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | In addition, the computation time and memory of the model are 98 ms and 2.2GB per frame, respectively, for 10 timesteps (1 ... | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | In addition, the computation time and memory of the model are 98 ms and 2.2GB per frame, respectively, for 10 timesteps (1 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.3. Training - extractive body cue:** Following previous regression works [9, 35], we adopt a smooth L1 loss to supervise training because of its less sensitivity to outliers.
- **p. 5 / 3.3. Training - extractive body cue:** Besides, the joint-wise conditions have to be initialized through training.
- **p. 5 / 4.1. Experiment Settings - extractive body cue:** We trained the model for 30 epochs with a learning rate decay of 0.1 after every 10 epochs.
- **p. 5 / 4.1. Experiment Settings - extractive body cue:** For training, we used the AdamW optimizer [26] with beta1 = 0.5, beta2 = 0.999, and learning rate α = 0.001.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** depth, image, points, first, supplied, local, condition, encoder, extracts, global, features, denoiser, consists, following, elements, feature, sampler, joint, indicator, timestep.
- **Relevant PDF headings:** 3. The Proposed Hand Pose Diffusion Model (p. 3); 4.3. Comparison with State-of-the-Art Methods (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | This dataset defines four official dataset split protocols: S0 - seen subjects, camera views, grasped objects; S1 - unseen subjects; S2 - ... | p. 5 (4.2. Datasets and Evaluation Metrics), p. 7 (4.3. Comparison with State-of-the-Art Methods) |
| Denoiser / vector field | As shown in Table 2, HandDiff outperforms previous SOTA methods in all four protocols. | p. 7 (4.3. Comparison with State-of-the-Art Methods), p. 7 (4.3. Comparison with State-of-the-Art Methods) |
| Sampling / downstream interface | The results also demonstrate that the proposed HandDiff significantly outperforms other 2D image-based methods by large margins since HandDiff directly performs the ... | p. 6 (4.3. Comparison with State-of-the-Art Methods), p. 5 (4.2. Datasets and Evaluation Metrics) |

## Failure and Ablation Link

- **p. 7 / 4.4. Ablation Study - extractive body cue:** We conducted extensive ablation experiments to evaluate the contribution of each component proposed in our model.
- **p. 7 / 4.4. Ablation Study - extractive body cue:** Based on this baseline, we incrementally adopt the proposed components and conduct ablations as follows: 1) using local conditions (LC); 2) using joint indicator (JI); ...
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Ablations of different modalities of conditions.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** All the ablation models are trained and tested on the DexYCB dataset .
- **p. 8 / 5. Conclusion - extractive body cue:** However, a limitation of HandDiff is its inability to handle scenarios with interacting hands.
- **p. 8 / 5. Conclusion - extractive body cue:** Future research avenues could explore extensions to bipartite graph learning and skeleton-based analysis to address these limitations and further enhance the model's capabilities.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. The pipeline of the proposed HandDiff. HandDiff takes the normalized point cloud transformed from a 2D depth image as the input. The PointNet-based ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3. The Proposed Hand Pose Diffusion Model), p. 3 (3.2. Joint-wise Local Feature-conditioned Denoiser), p. 5 (3.3. Training), p. 5 (3.3. Training), objective p. 5 (3.3. Training), p. 5 (3.3. Training), temporal p. 8 (4.4. Ablation Study), p. 5 (4.1. Experiment Settings), p. 8 (4.4. Ablation Study), p. 3 (3.2. Joint-wise Local Feature-conditioned Denoiser), p. 5 (3.3. Training), p. 6 (16.05 21.22 27.01 17.93 20.55 RGB).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
