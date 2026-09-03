# Method - TIGER: Time-Varying Denoising Model for 3D Point Cloud Generation with Diffusion Process

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Ren_TIGER_Time-Varying_Denoising_Model_for_3D_Point_Cloud_Generation_with_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Ren_TIGER_Time-Varying_Denoising_Model_for_3D_Point_Cloud_Generation_with_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3. Method), p. 4 (3.3. Latent Point Cloud Transformer), p. 4 (3.2. Noisy Point Cloud Encoder), p. 3 (3.2. Noisy Point Cloud Encoder), p. 5 (3.4. Time Mask Generator), p. 7 (Method)): Then, we dive into the details of our time-varying two-stream architecture, including the encoder part, latent point Transformer, time mask generator, and decoder part.

## Method Body Digest

- **p. 3 / 3. Method - extractive body cue:** Then, we dive into the details of our time-varying two-stream architecture, including the encoder part, latent point Transformer, time mask generator, and decoder part.
- **p. 4 / 3.3. Latent Point Cloud Transformer - extractive body cue:** Following [29], we use dual PatchNorm to project the latent point cloud into tokens, which place LayerNorm before and after an MLP layer for more ...
- **p. 4 / 3.2. Noisy Point Cloud Encoder - extractive body cue:** Specifically, a noisy point cloud encoder E : RN×3 →RM×d transforms the noisy point cloud Xt ∈RN×3 at timestep t into a latent point cloud ...
- **p. 3 / 3.2. Noisy Point Cloud Encoder - extractive body cue:** This representation works well with both CNN and Transformer architecture as we can downsample the voxel-grid following [11] to 9464
- **p. 5 / 3.4. Time Mask Generator - extractive body cue:** We apply a depth-2 PVCNN [30] to get local feature Xc ∈ RM×D and our latent point cloud Transformer to get global feature Xtr ∈RM×D.
- **p. 7 / Method - extractive body cue:** 2, our model trains much faster than LION, with only a quarter of its training time and a third of its inference time.
- **p. 5 / 3.4. Time Mask Generator - extractive body cue:** Time mask generator module scales the local and global features by the time variable.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** In training, we optimize the MSE loss: Lsimple = Et∼[1,T ]∥µ -µθ(Xt, t)∥2 2 = Et∼[1,T ]∥ϵ -ϵθ(Xt, t)∥2 2, (3) where ϵ is the ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions include: • We propose a novel two-stream denoising model, which uses timestep to optimally reweigh the global feature from Transformer and the ...
- **p. 1 / 1. Introduction - extractive body cue:** We propose to merge these two properties across different timesteps in the diffusion process. plore and develop efficient and effective model architectures for 3D point ...
- **p. 4 / 3.3. Latent Point Cloud Transformer - extractive body cue:** We propose two novel 3D space continuous position encoding methods: Phase Shift Position Encoding (PSPE) and Baseλ Position Encoding (BλPE).

## Source Evidence Cues

- **p. 3 / 3. Method - extractive body cue:** Then, we dive into the details of our time-varying two-stream architecture, including the encoder part, latent point Transformer, time mask generator, and decoder part.
- **p. 4 / 3.3. Latent Point Cloud Transformer - extractive body cue:** Following [29], we use dual PatchNorm to project the latent point cloud into tokens, which place LayerNorm before and after an MLP layer for more ...
- **p. 4 / 3.2. Noisy Point Cloud Encoder - extractive body cue:** Specifically, a noisy point cloud encoder E : RN×3 →RM×d transforms the noisy point cloud Xt ∈RN×3 at timestep t into a latent point cloud ...
- **p. 3 / 3.2. Noisy Point Cloud Encoder - extractive body cue:** This representation works well with both CNN and Transformer architecture as we can downsample the voxel-grid following [11] to 9464
- **p. 5 / 3.4. Time Mask Generator - extractive body cue:** We apply a depth-2 PVCNN [30] to get local feature Xc ∈ RM×D and our latent point cloud Transformer to get global feature Xtr ∈RM×D.
- **p. 7 / Method - extractive body cue:** 2, our model trains much faster than LION, with only a quarter of its training time and a third of its inference time.
- **p. 5 / 3.4. Time Mask Generator - extractive body cue:** Time mask generator module scales the local and global features by the time variable.
- **Detected method headings:** 3. Method (p. 3); Method (p. 6); 4.2. Comparison with SoTA methods (p. 6); Method (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | Then, we dive into the details of our time-varying two-stream architecture, including the encoder part, latent point Transformer, time mask generator, and ... | p. 3 (3. Method), p. 4 (3.3. Latent Point Cloud Transformer) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | Following [29], we use dual PatchNorm to project the latent point cloud into tokens, which place LayerNorm before and after an MLP ... | p. 4 (3.3. Latent Point Cloud Transformer), p. 4 (3.2. Noisy Point Cloud Encoder) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | Specifically, a noisy point cloud encoder E : RN×3 →RM×d transforms the noisy point cloud Xt ∈RN×3 at timestep t into a ... | p. 4 (3.2. Noisy Point Cloud Encoder), p. 3 (3.2. Noisy Point Cloud Encoder) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.1. Problem Formulation - extractive body cue:** In training, we optimize the MSE loss: Lsimple = Et∼[1,T ]∥µ -µθ(Xt, t)∥2 2 = Et∼[1,T ]∥ϵ -ϵθ(Xt, t)∥2 2, (3) where ϵ is the ...
- **p. 4 / 3.3. Latent Point Cloud Transformer - extractive body cue:** We maximize the phase shift difference ( 4π 3 ) of different axes to distinguish them and combine Sine and Cosine to guarantee the linear ...
- **p. 5 / 3.4. Time Mask Generator - extractive body cue:** With this constraint, the trade-off of local and global features can be learned by the network.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** By giving a sequence of pre-defined noising scales β1, β2, ..., βT , the transition probability can be expressed as : q(Xt/Xt-1) = N( p ...
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 3 (3.1. Problem Formulation), p. 5 (3.4. Time Mask Generator).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | main, contributions, include, novel, two-stream, denoising, model, uses, timestep, optimally, reweigh, global, feature, Transformer | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | main, contributions, include, novel, two-stream, denoising, model, uses, timestep, optimally | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | main, contributions, include, novel, two-stream, denoising, model, uses, timestep, optimally | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | training, optimize, MSE, loss, Lsimple, where, ground, truth, noise, prediction | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions include: • We propose a novel two-stream denoising model, which uses timestep to optimally reweigh the global feature from Transformer and the ...
- **p. 4 / 3.2. Noisy Point Cloud Encoder - extractive body cue:** We use furthest point sampling algorithm [11] to downsample the input noisy point cloud Xt ∈RN×3 into a sparser point cloud Xs t ∈RM×3 (M ...
- **p. 1 / 1. Introduction - extractive body cue:** Once trained, the model can be used to generate new point clouds by iterating the reverse process over a sequence of time steps, with each ...
- **p. 2 / 1. Introduction - extractive body cue:** Empirically we show that TIGER achieves state-ofthe-art (SoTA) performance in 3D point cloud generation.
- **p. 5 / 3.4. Time Mask Generator - extractive body cue:** We apply a depth-2 PVCNN [30] to get local feature Xc ∈ RM×D and our latent point cloud Transformer to get global feature Xtr ∈RM×D.
- **p. 6 / Method - extractive body cue:** TIGER generates high-quality and diverse 3D point clouds. where WD×3 is the projection matrix to map the noise into 3D space and Xt is the ...
- **p. 1 / 1. Introduction - extractive body cue:** However, compared to 2D images, the cost and complexity of acquiring 3D point clouds make it crucial to exFigure 1.
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | Once trained, the model can be used to generate new point clouds by iterating the reverse process over a sequence of time ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | To validate our motivation of reweighing the local and global features from ConvNet and Transformer at different time steps, we visualize the ... | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not recovered | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.3. Latent Point Cloud Transformer - extractive body cue:** Following [29], we use dual PatchNorm to project the latent point cloud into tokens, which place LayerNorm before and after an MLP layer for more ...
- **p. 7 / Method - extractive body cue:** 2, our model trains much faster than LION, with only a quarter of its training time and a third of its inference time.
- **p. 7 / Method - extractive body cue:** Training Time (GPU hours) Inference Time (s) PVD [55] 142 8.46 LION [53] 550 27.12 Tiger 164 9.73 Table 2.
- **p. 7 / Method - extractive body cue:** 2, our model trains much faster than LION, with only a quarter of its training time and a third of its inference time.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Then, dive, details, time-varying, two-stream, architecture, including, encoder, part, latent, point, Transformer, time, mask, generator, decoder, Following, dual, PatchNorm, project.
- **Relevant PDF headings:** 3. Method (p. 3); Method (p. 6); 4.2. Comparison with SoTA methods (p. 6); Method (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | It is noteworthy that in order to compare with LION, which uses a different dataset splitting strategy (sampling from the first 10, ... | p. 6 (4.2. Comparison with SoTA methods), p. 6 (4.1. Experimental Setup) |
| Denoiser / vector field | Figure 7. Our generation results (right) compared to baseline models (left). TIGER generates high-quality and diverse 3D point clouds. where WD×3 is ... | p. 6 (Figure/Table caption), p. 6 (4.2. Comparison with SoTA methods) |
| Sampling / downstream interface | Furthermore, our proposed position encoding methods, PSPE and BλPE, significantly improve performance compared to no position encoding or learnable position encoding. | p. 7 (4.3. Ablation and Analysis), p. 6 (4.2. Comparison with SoTA methods) |

## Failure and Ablation Link

- **p. 7 / 4.3. Ablation and Analysis - extractive body cue:** Ablation of Transformer backbones, position encoding, and self-attention strategies.
- **p. 7 / 4.3. Ablation and Analysis - extractive body cue:** In this ablation, we also compare the performance of our time masking with scalar value setting and channel-wise value setting.
- **p. 8 / 5. Conclusions - extractive body cue:** Although we generate high-quality and natural samples, we cannot control the category of the generated shape.
- **p. 8 / 5. Conclusions - extractive body cue:** But future works can increase the backbone efficiency by proposing time-varying properties with only one network.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Illustration of our time-varying two-stream architecture (TIGER). The network's input is a noisy point cloud Xt at timestep t, and the goal is ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 7. Our generation results (right) compared to baseline models (left). TIGER generates high-quality and diverse 3D point clouds. where WD×3 is the projection matrix ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3. Method), p. 4 (3.3. Latent Point Cloud Transformer), p. 4 (3.2. Noisy Point Cloud Encoder), p. 3 (3.2. Noisy Point Cloud Encoder), p. 5 (3.4. Time Mask Generator), p. 7 (Method), objective p. 3 (3.1. Problem Formulation), p. 4 (3.3. Latent Point Cloud Transformer), p. 5 (3.4. Time Mask Generator), p. 3 (3.1. Problem Formulation), temporal p. 1 (1. Introduction), p. 8 (4.3. Ablation and Analysis), p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation), p. 4 (3.2. Noisy Point Cloud Encoder), p. 5 (3.4. Time Mask Generator).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
