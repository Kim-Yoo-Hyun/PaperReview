# Method - Marigold: Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (33 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2312.02145; PDF retrieval source: https://arxiv.org/pdf/2312.02145. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3.4. Inference), p. 4 (3.2. Network Architecture), p. 4 (3.1. Generative Formulation), p. 3 (3.1. Generative Formulation), p. 3 (3.1. Generative Formulation), p. 5 (3.4. Inference)): Capitalizing on that, we propose the following test-time ensembling scheme, capable of combining multiple inference passes over the same input.

## Method Body Digest

- **p. 5 / 3.4. Inference - extractive PDF cue:** Capitalizing on that, we propose the following test-time ensembling scheme, capable of combining multiple inference passes over the same input.
- **p. 4 / 3.2. Network Architecture - extractive PDF cue:** One of our main objectives is training efficiency since diffusion models are often extremely resource-intensive to train.
- **p. 4 / 3.1. Generative Formulation - extractive PDF cue:** The adapted inference procedure involves one extra step - the decoder D reconstructing the data ˆd from the estimated clean latent z(d) 0 : ˆd ...
- **p. 3 / 3.1. Generative Formulation - extractive PDF cue:** At training time, parameters θ are updated by taking a data pair (x, d) from the training set, noising d with sampled noise ϵ at ...
- **p. 3 / 3.1. Generative Formulation - extractive PDF cue:** The canonical standard noise objective L is given as follows [20]: \mathcal {L} = \ma t hb b {E} _ {\depth _0, \noise \sim \mathcal ...
- **p. 5 / 3.4. Inference - extractive PDF cue:** The final depth map is decoded from the latent code using the VAE decoder and postprocessed by averaging channels.
- **p. 5 / 3.4. Inference - extractive PDF cue:** The proposed objective minimizes the distances between each pair of scaled and shifted predictions ( ˆd′i, ˆd′j), where ˆd′ = ˆd × ˆs + ˆt.
- **p. 4 / 3.1. Generative Formulation - extractive PDF cue:** We fine-tune just the U-Net by optimizing the standard diffusion objective relative to the depth latent code.

## Design Rationale

- **p. 5 / 3.4. Inference - extractive PDF cue:** Capitalizing on that, we propose the following test-time ensembling scheme, capable of combining multiple inference passes over the same input.
- **p. 2 / 1. Introduction - extractive PDF cue:** To summarize, our contributions are: 1.
- **p. 5 / 3.4. Inference - extractive PDF cue:** This scheme enables a flexible trade-off between computation efficiency and prediction quality by choosing N accordingly.

## Source Evidence Cues

- **p. 5 / 3.4. Inference - extractive PDF cue:** Capitalizing on that, we propose the following test-time ensembling scheme, capable of combining multiple inference passes over the same input.
- **p. 4 / 3.2. Network Architecture - extractive PDF cue:** One of our main objectives is training efficiency since diffusion models are often extremely resource-intensive to train.
- **p. 4 / 3.1. Generative Formulation - extractive PDF cue:** The adapted inference procedure involves one extra step - the decoder D reconstructing the data ˆd from the estimated clean latent z(d) 0 : ˆd ...
- **p. 3 / 3.1. Generative Formulation - extractive PDF cue:** At training time, parameters θ are updated by taking a data pair (x, d) from the training set, noising d with sampled noise ϵ at ...
- **p. 3 / 3.1. Generative Formulation - extractive PDF cue:** The canonical standard noise objective L is given as follows [20]: \mathcal {L} = \ma t hb b {E} _ {\depth _0, \noise \sim \mathcal ...
- **p. 5 / 3.4. Inference - extractive PDF cue:** The final depth map is decoded from the latent code using the VAE decoder and postprocessed by averaging channels.
- **Detected method headings:** 2.2. Diffusion Models (p. 3); 2.4. Foundation Models (p. 3); 3. Method (p. 3); 3.2. Network Architecture (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Capitalizing on that, we propose the following test-time ensembling scheme, capable of combining multiple inference passes over the same input. | p. 5 (3.4. Inference), p. 4 (3.2. Network Architecture) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | One of our main objectives is training efficiency since diffusion models are often extremely resource-intensive to train. | p. 4 (3.2. Network Architecture), p. 4 (3.1. Generative Formulation) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The adapted inference procedure involves one extra step - the decoder D reconstructing the data ˆd from the estimated clean latent z(d) ... | p. 4 (3.1. Generative Formulation), p. 3 (3.1. Generative Formulation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.1. Generative Formulation - extractive PDF cue:** At training time, parameters θ are updated by taking a data pair (x, d) from the training set, noising d with sampled noise ϵ at ...
- **p. 5 / 3.4. Inference - extractive PDF cue:** The proposed objective minimizes the distances between each pair of scaled and shifted predictions ( ˆd′i, ˆd′j), where ˆd′ = ˆd × ˆs + ˆt.
- **p. 4 / 3.1. Generative Formulation - extractive PDF cue:** We fine-tune just the U-Net by optimizing the standard diffusion objective relative to the depth latent code.
- **p. 5 / 3.3. Fine-Tuning Protocol - extractive PDF cue:** If our assumption about the possibility of finetuning a generalizable depth estimation from a text-to-image LDM is correct, then synthetic depth gives the cleanest set ...
- **p. 3 / 3.1. Generative Formulation - extractive PDF cue:** The canonical standard noise objective L is given as follows [20]: \mathcal {L} = \ma t hb b {E} _ {\depth _0, \noise \sim \mathcal ...
- **p. 4 / 3.3. Fine-Tuning Protocol - extractive PDF cue:** As with the depth normalization rationale, this decision has two objective reasons.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3.1. Generative Formulation), p. 5 (3.4. Inference), p. 5 (3.3. Fine-Tuning Protocol), p. 3 (3.1. Generative Formulation), p. 4 (3.3. Fine-Tuning Protocol), p. 4 (3.1. Generative Formulation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, encoder, designed, channel, RGB, inputs, receives, single-channel, depth, replicate, three, channels, simulate, image | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Given, encoder, designed, channel, RGB, inputs, receives, single-channel, depth, replicate | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Capitalizing, following, test-time, ensembling, scheme, capable, combining, multiple, inference, passes | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | training, time, parameters, updated, taking, data, pair, noising, sampled, noise | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. Network Architecture - extractive PDF cue:** Given that the encoder, which is designed for 3-channel (RGB) inputs, receives a single-channel depth map, we replicate the depth map into three channels to ...
- **p. 4 / 3.2. Network Architecture - extractive PDF cue:** To implement the conditioning of the latent denoiser ϵθ(z(d) t , z(x), t) on input image x, we concatenate the image and depth latent codes ...
- **p. 5 / 3.3. Fine-Tuning Protocol - extractive PDF cue:** The multi-resolution noise is composed by superimposing several random Gaussian noise images of different scales, all upsampled to the U-Net input resolution.
- **p. 5 / 3.4. Inference - extractive PDF cue:** We encode the input image into the latent space, initialize depth latent as standard Gaussian noise, and progressively denoise it with the same schedule as ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Marigold, a state-of-the-art, versatile monocular depth estimation module that offers excellent performance across a wide variety of natural images.
- **p. 2 / 1. Introduction - extractive PDF cue:** Empowered by the underlying diffusion prior of natural images, Marigold exhibits excellent zero-shot generalization: Without ever having seen real depth maps, it attains state-ofthe-art performance ...
- **p. 3 / 3.1. Generative Formulation - extractive PDF cue:** We pose monocular depth estimation as a conditional denoising diffusion generation task and train Marigold to model the conditional distribution D(d / x) over depth ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | At training time, parameters θ are updated by taking a data pair (x, d) from the training set, noising d with sampled ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | In the forward process, which starts at d0 := d from the conditional distribution, Gaussian noise is gradually added at levels t ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | To fit one GPU, we accumulate gradients for 16 steps. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.4. Inference - extractive PDF cue:** Capitalizing on that, we propose the following test-time ensembling scheme, capable of combining multiple inference passes over the same input.
- **p. 4 / 3.2. Network Architecture - extractive PDF cue:** One of our main objectives is training efficiency since diffusion models are often extremely resource-intensive to train.
- **p. 4 / 3.1. Generative Formulation - extractive PDF cue:** The adapted inference procedure involves one extra step - the decoder D reconstructing the data ˆd from the estimated clean latent z(d) 0 : ˆd ...
- **p. 3 / 3.1. Generative Formulation - extractive PDF cue:** At training time, parameters θ are updated by taking a data pair (x, d) from the training set, noising d with sampled noise ϵ at ...
- **p. 3 / 3.1. Generative Formulation - extractive PDF cue:** The canonical standard noise objective L is given as follows [20]: \mathcal {L} = \ma t hb b {E} _ {\depth _0, \noise \sim \mathcal ...
- **p. 5 / 4.1. Implementation - extractive PDF cue:** At inference time, we apply the DDIM scheduler [49] and only sample 50 steps.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Capitalizing, following, test-time, ensembling, scheme, capable, combining, multiple, inference, passes, over, same, input, One, main, objectives, training, efficiency, since, diffusion.
- **Relevant PDF headings:** 2.2. Diffusion Models (p. 3); 2.4. Foundation Models (p. 3); 3. Method (p. 3); 3.2. Network Architecture (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | In the case of the ScanNet dataset, we randomly sampled 800 images from the 312 official validation scenes for testing. | p. 6 (4.2. Evaluation), p. 6 (4.2. Evaluation) |
| Semantic / temporal fusion | Table 1. Quantitative comparison of Marigold with SOTA affine-invariant depth estimators on several zero-shot benchmarks. All metrics† are presented in percentage terms; ... | p. 6 (Figure/Table caption), p. 6 (4.2. Evaluation) |
| Robot query / planning handoff | 2, training with multi-resolution noise significantly improves the depth prediction accuracy over using standard Gaussian noise. | p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies) |

## Failure and Ablation Link

- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative comparison of Marigold with SOTA affine-invariant depth estimators on several zero-shot benchmarks. All metrics† are presented in percentage terms; bold numbers are ...
- **p. 6 / 4.2. Evaluation - extractive PDF cue:** It also shows that our fine-tuning protocol was successful in adapting Stable Diffusion for this task without unlearning such visual priors.
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** We evaluate the effect of the re-spaced inference denoising steps driven by the DDIM scheduler [49].
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** Refer to supplementary sections for extra ablations and discussion.
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of the Marigold fine-tuning protocol. Start- ing from pretrained Stable Diffusion, we encode the image x and depth d into the latent ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We present Marigold, a diffusion model and associated fine-tuning protocol for monocular depth estimation. Its core principle is to leverage the rich visual ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Overview of the Marigold inference scheme. Given an input image x, we encode it with the original Stable Diffusion VAE into the latent ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3.4. Inference), p. 4 (3.2. Network Architecture), p. 4 (3.1. Generative Formulation), p. 3 (3.1. Generative Formulation), p. 3 (3.1. Generative Formulation), p. 5 (3.4. Inference), objective p. 3 (3.1. Generative Formulation), p. 5 (3.4. Inference), p. 4 (3.1. Generative Formulation), p. 5 (3.3. Fine-Tuning Protocol), p. 3 (3.1. Generative Formulation), p. 4 (3.3. Fine-Tuning Protocol), temporal p. 3 (3.1. Generative Formulation), p. 3 (3.1. Generative Formulation), p. 4 (3.1. Generative Formulation), p. 4 (3.1. Generative Formulation), p. 5 (4.1. Implementation), p. 5 (4.1. Implementation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
