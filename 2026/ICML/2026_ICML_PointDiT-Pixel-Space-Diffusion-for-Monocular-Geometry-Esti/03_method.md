# Method - PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=hQWwTWGAyu; PDF retrieval source: https://openreview.net/pdf/859969c4505c940b506d06cb01ee1bce1e5d07d0.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3.3. Training), p. 3 (3. Approach), p. 5 (3.2. Architecture), p. 4 (3.2. Architecture), p. 4 (3.2. Architecture), p. 6 (3.4. Inference)): This creates a train-test discrepancy, since inference always starts at t = 0, and the model may then struggle to initiate the flow trajectory from the prior (Lin et al., ...

## Method Body Digest

- **p. 5 / 3.3. Training - extractive body cue:** This creates a train-test discrepancy, since inference always starts at t = 0, and the model may then struggle to initiate the flow trajectory from ...
- **p. 3 / 3. Approach - extractive body cue:** To model the inherent ambiguities of this single-image setting, we propose a flow matching framework parameterized by a Vision Transformer (ViT) (Dosovitskiy, 2020; Peebles & ...
- **p. 5 / 3.2. Architecture - extractive body cue:** The sequence is then processed by a stack of Transformer blocks (Dosovitskiy, 2020; Li & He, 2026), each comprising multi-head self-attention and an MLP.
- **p. 4 / 3.2. Architecture - extractive body cue:** This yields a composite image representation Tc ∈RN×4D, where D is the perlayer feature dimension.
- **p. 4 / 3.2. Architecture - extractive body cue:** Crucially, unlike previous flow matching models that typically predict the velocity, our network is trained to predict the clean point map.
- **p. 6 / 3.4. Inference - extractive body cue:** We further observe that our model can serve as a deterministic estimator at inference time, by initializing from all zeros instead of random noise (Table ...
- **p. 3 / 3.1. Point Map Generation with Flow Matching - extractive body cue:** We adopt the flow matching formulation to model point map generation from a single image.
- **p. 5 / 3.3. Training - extractive body cue:** The final optimization objective is the weighted sum: L = Lfm + λLrel, (7) where λ = 0.1 is the loss weight.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Inspired by JiT (Li & He, 2026), we introduce a minimalist pixel-space diffusion framework that trains directly on the raw point map space.
- **p. 3 / 3. Approach - extractive body cue:** Our method learns to transport a simple Gaussian noise distribution to the data distribution of point maps, conditioned on the input image.
- **p. 3 / 3. Approach - extractive body cue:** To model the inherent ambiguities of this single-image setting, we propose a flow matching framework parameterized by a Vision Transformer (ViT) (Dosovitskiy, 2020; Peebles & ...

## Source Evidence Cues

- **p. 5 / 3.3. Training - extractive body cue:** This creates a train-test discrepancy, since inference always starts at t = 0, and the model may then struggle to initiate the flow trajectory from ...
- **p. 3 / 3. Approach - extractive body cue:** To model the inherent ambiguities of this single-image setting, we propose a flow matching framework parameterized by a Vision Transformer (ViT) (Dosovitskiy, 2020; Peebles & ...
- **p. 5 / 3.2. Architecture - extractive body cue:** The sequence is then processed by a stack of Transformer blocks (Dosovitskiy, 2020; Li & He, 2026), each comprising multi-head self-attention and an MLP.
- **p. 4 / 3.2. Architecture - extractive body cue:** This yields a composite image representation Tc ∈RN×4D, where D is the perlayer feature dimension.
- **p. 4 / 3.2. Architecture - extractive body cue:** Crucially, unlike previous flow matching models that typically predict the velocity, our network is trained to predict the clean point map.
- **p. 6 / 3.4. Inference - extractive body cue:** We further observe that our model can serve as a deterministic estimator at inference time, by initializing from all zeros instead of random noise (Table ...
- **p. 3 / 3.1. Point Map Generation with Flow Matching - extractive body cue:** We adopt the flow matching formulation to model point map generation from a single image.
- **Detected method headings:** 3. Approach (p. 3); 3.2. Architecture (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | This creates a train-test discrepancy, since inference always starts at t = 0, and the model may then struggle to initiate the ... | p. 5 (3.3. Training), p. 3 (3. Approach) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | To model the inherent ambiguities of this single-image setting, we propose a flow matching framework parameterized by a Vision Transformer (ViT) (Dosovitskiy, ... | p. 3 (3. Approach), p. 5 (3.2. Architecture) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | The sequence is then processed by a stack of Transformer blocks (Dosovitskiy, 2020; Li & He, 2026), each comprising multi-head self-attention and ... | p. 5 (3.2. Architecture), p. 4 (3.2. Architecture) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.3. Training - extractive body cue:** The final optimization objective is the weighted sum: L = Lfm + λLrel, (7) where λ = 0.1 is the loss weight.
- **p. 5 / 3.3. Training - extractive body cue:** Although our network Fθ is parameterized to predict the clean point map ˆx, we optimize it in velocity space (v-loss), following JiT (Li & He, ...
- **p. 3 / 3.1. Point Map Generation with Flow Matching - extractive body cue:** Flow matching learns an Ordinary Differential Equation (ODE) that continuously transforms a prior noise distribution p0 into the data distribution p1.
- **p. 4 / 3.1. Point Map Generation with Flow Matching - extractive body cue:** Specifically, we learn a conditional vector field vθ(zt, t/c) that predicts the target velocity defined in Equation (2).
- **p. 4 / 3.1. Point Map Generation with Flow Matching - extractive body cue:** Since this radius is only a synthetic proxy for the true depth, we down-weight sky pixels in the training loss rather than masking them out ...
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 5 (3.3. Training), p. 3 (3.1. Point Map Generation with Flow Matching), p. 4 (3.1. Point Map Generation with Flow Matching), p. 4 (3.1. Point Map Generation with Flow Matching), p. 5 (3.3. Training).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Formally, given, input, image, goal, estimate, corresponding, point, pixel, encodes, spatial, coordinates, network, takes | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | Formally, given, input, image, goal, estimate, corresponding, point, pixel, encodes | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | Inspired, JiT, introduce, minimalist, pixel-space, diffusion, framework, trains, directly, point | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | final, optimization, objective, weighted, Lfm, Lrel, where, loss, weight, Although | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3. Approach - extractive body cue:** Formally, given an input image c ∈RH×W ×3, our goal is to estimate the corresponding point map x ∈ RH×W ×3, in which each pixel ...
- **p. 4 / 3.2. Architecture - extractive body cue:** The network takes the noisy point map zt, the current time step t, and the conditioning image c as input.
- **p. 4 / 3.1. Point Map Generation with Flow Matching - extractive body cue:** We extend this framework to model the conditional distribution p(x/c), where c is the input RGB image and x is the target dense point map.
- **p. 5 / 3.4. Inference - extractive body cue:** We attribute this to the per-pixel alignment between the predicted point map and the conditioning image: each output location is 5
- **p. 1 / 1. Introduction - extractive body cue:** DINOv3 Linear Embed … … Linear Predict Transformer Block ×L Noisy Point Map Input Image Clean Point Map Unpatchify Patchify … Point Tokens DINOv3 Tokens ...
- **p. 3 / 3. Approach - extractive body cue:** Our method learns to transport a simple Gaussian noise distribution to the data distribution of point maps, conditioned on the input image.
- **p. 5 / 3.4. Inference - extractive body cue:** At each step t, we predict the clean data ˆx, derive the velocity ˆvt, and update the state: zt+∆t ←zt + ∆t · ˆvt.
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | To further demonstrate the benefits of the generative flow matching formulation, we train a deterministic regressor by fixing both the time step ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | Because the logitnormal sampler maps the timestep through a sigmoid, it is nearly impossible to draw an exact 0 during training. | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not recovered | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.3. Training - extractive body cue:** This creates a train-test discrepancy, since inference always starts at t = 0, and the model may then struggle to initiate the flow trajectory from ...
- **p. 4 / 3.2. Architecture - extractive body cue:** Crucially, unlike previous flow matching models that typically predict the velocity, our network is trained to predict the clean point map.
- **p. 6 / 3.4. Inference - extractive body cue:** We further observe that our model can serve as a deterministic estimator at inference time, by initializing from all zeros instead of random noise (Table ...
- **p. 8 / 4.4. Evaluation Results - extractive body cue:** Supporting a variable number of inference steps with one network underscores the flexibility of our approach.
- **p. 8 / 4.4. Evaluation Results - extractive body cue:** Thanks to its flow matching formulation, PointDiT can also benefit from additional inference steps using the same model.
- **p. 10 / 4.5. Ablation and Analysis - extractive body cue:** To save compute, the 512 × 512 models in this part are fine-tuned on a 6dataset subset (Hypersim, VKITTI2, UrbanSyn, Synscapes, TartanAir, and OmniWorldGame; 1.48M ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** creates, train-test, discrepancy, since, inference, always, starts, model, then, struggle, initiate, flow, trajectory, prior, Lin, inherent, ambiguities, single-image, setting, matching.
- **Relevant PDF headings:** 3. Approach (p. 3); 3.2. Architecture (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | By default we train on the 256 × 256 SceneNet-RGBD dataset and report the average metrics on the seven unseen test sets ... | p. 8 (4.5. Ablation and Analysis), p. 6 (4.2. Implementation Details) |
| Denoiser / vector field | For a fair comparison, we benchmark against several state-of-the-art baselines, evaluating their publicly available pre-trained weights under the same preprocessing and cropping ... | p. 7 (4.3. Evaluation Setup and Metrics), p. 7 (Figure/Table caption) |
| Sampling / downstream interface | Figure 3. Different diffusion sampling steps. Our single-step diffusion already significantly outperforms prior works, and in- creasing the sampling steps further enhances ... | p. 7 (Figure/Table caption), p. 7 (4.4. Evaluation Results) |

## Failure and Ablation Link

- **p. 10 / 4.5. Ablation and Analysis - extractive body cue:** The ablation results discussed so far use only the flow matching loss (Equation (5)), which is already highly effective at recovering high-quality geometry.
- **p. 6 / 4.2. Implementation Details - extractive body cue:** All variants are pre-trained at 256 × 256 for 30 epochs (including a 5-epoch warmup) and then fine-tuned at 512×512, scaling the number of GPUs ...
- **p. 7 / 4.3. Evaluation Setup and Metrics - extractive body cue:** Our model predicts affine-invariant point maps, from which affine-invariant depth maps are obtained by extracting the z-component of each point.
- **p. 9 / 4.5. Ablation and Analysis - extractive body cue:** Even without any pretrained image backbone (i.e., with plain linear embeddings), our model already achieves decent results.
- **p. 6 / 4.2. Implementation Details - extractive body cue:** We use the same patch size of 16 for all variants.
- **p. 7 / 4.4. Evaluation Results - extractive body cue:** PointDiTL attains comparable boundary quality at lower cost, and our smallest variant, PointDiT-B, stays competitive with fewer parameters.
- **p. 14 / Figure/Table caption - extractive body cue:** Table 6. Training cost. Number of epochs, H100 GPUs, and wall-clock time for the pre-training (256 × 256) and fine-tuning (512 × 512) stages of ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3.3. Training), p. 3 (3. Approach), p. 5 (3.2. Architecture), p. 4 (3.2. Architecture), p. 4 (3.2. Architecture), p. 6 (3.4. Inference), objective p. 5 (3.3. Training), p. 5 (3.3. Training), p. 3 (3.1. Point Map Generation with Flow Matching), p. 4 (3.1. Point Map Generation with Flow Matching), p. 4 (3.1. Point Map Generation with Flow Matching), temporal p. 8 (4.5. Ablation and Analysis), p. 9 (4.5. Ablation and Analysis), p. 9 (4.5. Ablation and Analysis), p. 4 (3.2. Architecture), p. 4 (3.1. Point Map Generation with Flow Matching), p. 5 (3.3. Training).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
