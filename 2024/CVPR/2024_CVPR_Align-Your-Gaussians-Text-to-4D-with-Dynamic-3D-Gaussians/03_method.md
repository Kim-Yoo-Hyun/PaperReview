# Method - Align Your Gaussians: Text-to-4D with Dynamic 3D Gaussians and Composed Diffusion Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Ling_Align_Your_Gaussians_Text-to-4D_with_Dynamic_3D_Gaussians_and_Composed_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Ling_Align_Your_Gaussians_Text-to-4D_with_Dynamic_3D_Gaussians_and_Composed_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3.2. Text-to-4D as Compositional Generation), p. 4 (3.2. Text-to-4D as Compositional Generation), p. 3 (2. Background), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Text-to-4D as Compositional Generation)): We disentangle optimization into first synthesizing a static 3D Gaussian-based object θ, and then learning the deformation field Φ to add scene dynamics.

## Method Body Digest

- **p. 5 / 3.2. Text-to-4D as Compositional Generation - extractive PDF cue:** We disentangle optimization into first synthesizing a static 3D Gaussian-based object θ, and then learning the deformation field Φ to add scene dynamics.
- **p. 4 / 3.2. Text-to-4D as Compositional Generation - extractive PDF cue:** All used DMs are latent DMs [70, 86], which means that in practice we first encode renderings of our 4D scenes into the models' latent ...
- **p. 3 / 2. Background - extractive PDF cue:** In the score distillation sampling (SDS) framework, the DM's denoiser is then used to construct a gradient that is backpropagated through the differentiable rendering process ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Furthermore, we use a motion amplification method that carefully scales the gradients from the text-tovideo model and enhances motion.
- **p. 2 / 1. Introduction - extractive PDF cue:** (i) We propose AYG, a system for textto-4D content creation leveraging dynamic 3D Gaussians with deformation fields as 4D representation.
- **p. 4 / 3.2. Text-to-4D as Compositional Generation - extractive PDF cue:** (i) We use the text-to-image model Stable Diffusion (SD) [70], which has been trained on a broad set of imagery and provides a strong general ...
- **p. 6 / 3.2. Text-to-4D as Compositional Generation - extractive PDF cue:** The renderings {˜z˜cj ˜τj}M fed to regular SD can be taken at different times ˜τj and cameras ˜cj than the video model frames, but in ...
- **p. 7 / 3.4. Scaling Align Your Gaussians - extractive PDF cue:** We additionally minimize LInterpol-Reg. = //∆Φ1 -∆interpol Φ12 //2 2 within the overlap region to regularize the optimization process of ∆Φ2.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** We propose Align Your Gaussians (AYG), a novel method for 4D content creation.
- **p. 2 / 1. Introduction - extractive PDF cue:** (iii) To scale AYG, we introduce a novel regularization method and a new motion amplification technique.
- **p. 1 / 1. Introduction - extractive PDF cue:** Generative modeling of dynamic 3D scenes has the potential to revolutionize how we create games, movies, simu- *Equal contribution.

## Source Evidence Cues

- **p. 5 / 3.2. Text-to-4D as Compositional Generation - extractive PDF cue:** We disentangle optimization into first synthesizing a static 3D Gaussian-based object θ, and then learning the deformation field Φ to add scene dynamics.
- **p. 4 / 3.2. Text-to-4D as Compositional Generation - extractive PDF cue:** All used DMs are latent DMs [70, 86], which means that in practice we first encode renderings of our 4D scenes into the models' latent ...
- **p. 3 / 2. Background - extractive PDF cue:** In the score distillation sampling (SDS) framework, the DM's denoiser is then used to construct a gradient that is backpropagated through the differentiable rendering process ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Furthermore, we use a motion amplification method that carefully scales the gradients from the text-tovideo model and enhances motion.
- **p. 2 / 1. Introduction - extractive PDF cue:** (i) We propose AYG, a system for textto-4D content creation leveraging dynamic 3D Gaussians with deformation fields as 4D representation.
- **p. 4 / 3.2. Text-to-4D as Compositional Generation - extractive PDF cue:** (i) We use the text-to-image model Stable Diffusion (SD) [70], which has been trained on a broad set of imagery and provides a strong general ...
- **p. 6 / 3.2. Text-to-4D as Compositional Generation - extractive PDF cue:** The renderings {˜z˜cj ˜τj}M fed to regular SD can be taken at different times ˜τj and cameras ˜cj than the video model frames, but in ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | We disentangle optimization into first synthesizing a static 3D Gaussian-based object θ, and then learning the deformation field Φ to add scene ... | p. 5 (3.2. Text-to-4D as Compositional Generation), p. 4 (3.2. Text-to-4D as Compositional Generation) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | All used DMs are latent DMs [70, 86], which means that in practice we first encode renderings of our 4D scenes into ... | p. 4 (3.2. Text-to-4D as Compositional Generation), p. 3 (2. Background) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | In the score distillation sampling (SDS) framework, the DM's denoiser is then used to construct a gradient that is backpropagated through the ... | p. 3 (2. Background), p. 2 (1. Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / 3.4. Scaling Align Your Gaussians - extractive PDF cue:** We additionally minimize LInterpol-Reg. = //∆Φ1 -∆interpol Φ12 //2 2 within the overlap region to regularize the optimization process of ∆Φ2.
- **p. 2 / 1. Introduction - extractive PDF cue:** Afterwards, we compose the gradients of a text-to-video and a text-to-image model; the gradients of the text-to-video model optimize the deformation field to capture temporal ...
- **p. 3 / 2. Background - extractive PDF cue:** Initially proposed for 3D scene reconstruction, 3D Gaussian Splatting uses gradient-based thresholding to densify areas that need more Gaussians to capture fine details, and unnecessary ...
- **p. 3 / 2. Background - extractive PDF cue:** In the score distillation sampling (SDS) framework, the DM's denoiser is then used to construct a gradient that is backpropagated through the differentiable rendering process ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Furthermore, we use a motion amplification method that carefully scales the gradients from the text-tovideo model and enhances motion.
- **p. 4 / 3.2. Text-to-4D as Compositional Generation - extractive PDF cue:** All used DMs are latent DMs [70, 86], which means that in practice we first encode renderings of our 4D scenes into the models' latent ...
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 3 (2. Background), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (2. Background), p. 4 (3.2. Text-to-4D as Compositional Generation), p. 5 (3.2. Text-to-4D as Compositional Generation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Compared, previous, pursue, novel, compositional, generation-based, combine, text-to-image, text-to-video, D-aware, multiview, diffusion, models, provide | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | Compared, previous, pursue, novel, compositional, generation-based, combine, text-to-image, text-to-video, D-aware | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | Align, Your, Gaussians, AYG, novel, content, creation, scale, introduce, regularization | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | additionally, minimize, LInterpol-Reg, interpol, within, overlap, region, regularize, optimization, process | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Abstract - extractive PDF cue:** Compared to previous work, we pursue a novel compositional generation-based approach, and combine text-to-image, text-to-video, and 3D-aware multiview diffusion models to provide feedback during 4D ...
- **p. 4 / 3.2. Text-to-4D as Compositional Generation - extractive PDF cue:** This video DM provides temporal feedback when rendering 2D frame sequences from our dynamic 4D scenes.
- **p. 6 / 3.3. AYG's Score Distillation in Practice - extractive PDF cue:** Inspired by this observation and aiming to avoid ProlificDreamer's cumbersome fine-tuning, we instead propose to simply set δvid/im gen = 0 entirely and optimize with ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Afterwards, we compose the gradients of a text-to-video and a text-to-image model; the gradients of the text-to-video model optimize the deformation field to capture temporal ...
- **p. 5 / 3.2. Text-to-4D as Compositional Generation - extractive PDF cue:** To this end, we compose the text-to-image and text-to-video DMs and formally minimize a reverse KLD of the form KL  qΦ  {zci τi}F ...
- **p. 1 / Abstract - extractive PDF cue:** These techniques allow us to synthesize vivid dynamic scenes, outperform previous work qualitatively and quantitatively and achieve state-of-the-art text-to-4D performance.
- **p. 2 / 1. Introduction - extractive PDF cue:** 1), achieving stateof-the-art text-to-4D performance.
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | We can also create sequences that loop endlessly by enforcing that the last frame of a later sequence matches the first frame ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | This video DM provides temporal feedback when rendering 2D frame sequences from our dynamic 4D scenes. | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not recovered | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.2. Text-to-4D as Compositional Generation - extractive PDF cue:** (i) We use the text-to-image model Stable Diffusion (SD) [70], which has been trained on a broad set of imagery and provides a strong general ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** disentangle, optimization, first, synthesizing, static, Gaussian-based, object, then, learning, deformation, field, scene, dynamics, DMs, latent, means, practice, encode, renderings, scenes.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | Finally, due to the explicit nature of the dynamic 3D Gaussians, AYG's 4D representation, multiple animated 4D objects can be easily composed ... | p. 8 (4. Experiments), p. 8 (4. Experiments) |
| Denoiser / vector field | AYG outperforms MAV3D on all metrics, achieving state-of-the-art text-to-4D performance (we also evaluated R-Precision [32, 58] on a larger prompt set used ... | p. 8 (4. Experiments), p. 8 (4. Experiments) |
| Sampling / downstream interface | AYG outperforms MAV3D on all metrics, achieving state-of-the-art text-to-4D performance (we also evaluated R-Precision [32, 58] on a larger prompt set used ... | p. 8 (4. Experiments), p. 8 (4. Experiments) |

## Failure and Ablation Link

- **p. 8 / 4. Experiments - extractive PDF cue:** Some components have different effects with respect to 3D appearance and motion, but we generally see that all components matter significantly in terms of overall ...
- **p. 8 / 4. Experiments - extractive PDF cue:** Next, we performed an ablation study on AYG's different components.
- **p. 8 / 5. Conclusions - extractive PDF cue:** Overcoming this limitation would be an exciting avenue for future work.
- **p. 8 / 5. Conclusions - extractive PDF cue:** AYG currently cannot easily produce topological changes of the dynamic objects.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3.2. Text-to-4D as Compositional Generation), p. 4 (3.2. Text-to-4D as Compositional Generation), p. 3 (2. Background), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Text-to-4D as Compositional Generation), objective p. 7 (3.4. Scaling Align Your Gaussians), p. 2 (1. Introduction), p. 3 (2. Background), p. 3 (2. Background), p. 2 (1. Introduction), p. 4 (3.2. Text-to-4D as Compositional Generation), temporal p. 8 (4. Experiments), p. 4 (3.2. Text-to-4D as Compositional Generation), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 7 (4. Experiments), p. 8 (4. Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
