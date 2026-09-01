# Method - DreamFusion: Text-to-3D using 2D Diffusion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2209.14988; PDF retrieval source: https://arxiv.org/pdf/2209.14988. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 7 (3. Diffusion loss with view-dependent conditioning), p. 16 (A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS), p. 17 (A.4 DERIVING THE SCORE DISTILLATION SAMPLING LOSS AND GRADIENTS), p. 15 (A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS), p. 16 (A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS), p. 8 (4. Optimization)): We use the pretrained 64 × 64 base text-to-image model from Saharia et al.

## Method Body Digest

- **p. 7 / 3. Diffusion loss with view-dependent conditioning - extractive PDF cue:** We use the pretrained 64 × 64 base text-to-image model from Saharia et al.
- **p. 16 / A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS - extractive PDF cue:** We use the orientation loss proposed by Ref-NeRF (Verbin et al., 2022) to encourage normal vectors of the density field to face toward the camera ...
- **p. 17 / A.4 DERIVING THE SCORE DISTILLATION SAMPLING LOSS AND GRADIENTS - extractive PDF cue:** We use this loss to find modes of the score functions that are present across all noise levels in the diffusion process.
- **p. 15 / A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS - extractive PDF cue:** Representative settings are 5 × 10-2 and 2 × 10-3 for the initial and final values of λΣ, linearly annealed for the first 5k steps ...
- **p. 16 / A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS - extractive PDF cue:** For the first 1k steps of optimization we set the ambient light color ℓa to 1 and the diffuse light color ℓρ to 0, which ...
- **p. 8 / 4. Optimization - extractive PDF cue:** Metrics shown in parentheses may be overfit, as the same CLIP model is used during training and eval.
- **p. 17 / A.4 DERIVING THE SCORE DISTILLATION SAMPLING LOSS AND GRADIENTS - extractive PDF cue:** (2022) also sample diffusion models by optimization, thereby allowing parameterized samples.
- **p. 17 / A.4 DERIVING THE SCORE DISTILLATION SAMPLING LOSS AND GRADIENTS - extractive PDF cue:** Here we show how the gradient of this loss leads to the same update as optimizing the training loss LDiff, but without the term corresponding ...

## Design Rationale

- **p. 5 / 1 INTRODUCTION - extractive PDF cue:** 3.1 NEURAL RENDERING OF A 3D MODEL NeRF is a technique for neural inverse rendering that consists of a volumetric raytracer and a multilayer perceptron ...
- **p. 6 / 1 INTRODUCTION - extractive PDF cue:** While our method can generate some complex scenes, we find that it is helpful to only query the NeRF scene representation within a fixed bounding ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** The resulting Score Distillation Sampling (SDS) method enables sampling via optimization in differentiable image parameterizations.

## Source Evidence Cues

- **p. 7 / 3. Diffusion loss with view-dependent conditioning - extractive PDF cue:** We use the pretrained 64 × 64 base text-to-image model from Saharia et al.
- **p. 16 / A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS - extractive PDF cue:** We use the orientation loss proposed by Ref-NeRF (Verbin et al., 2022) to encourage normal vectors of the density field to face toward the camera ...
- **p. 17 / A.4 DERIVING THE SCORE DISTILLATION SAMPLING LOSS AND GRADIENTS - extractive PDF cue:** We use this loss to find modes of the score functions that are present across all noise levels in the diffusion process.
- **p. 15 / A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS - extractive PDF cue:** Representative settings are 5 × 10-2 and 2 × 10-3 for the initial and final values of λΣ, linearly annealed for the first 5k steps ...
- **p. 16 / A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS - extractive PDF cue:** For the first 1k steps of optimization we set the ambient light color ℓa to 1 and the diffuse light color ℓρ to 0, which ...
- **p. 8 / 4. Optimization - extractive PDF cue:** Metrics shown in parentheses may be overfit, as the same CLIP model is used during training and eval.
- **p. 17 / A.4 DERIVING THE SCORE DISTILLATION SAMPLING LOSS AND GRADIENTS - extractive PDF cue:** (2022) also sample diffusion models by optimization, thereby allowing parameterized samples.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | We use the pretrained 64 × 64 base text-to-image model from Saharia et al. | p. 7 (3. Diffusion loss with view-dependent conditioning), p. 16 (A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | We use the orientation loss proposed by Ref-NeRF (Verbin et al., 2022) to encourage normal vectors of the density field to face ... | p. 16 (A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS), p. 17 (A.4 DERIVING THE SCORE DISTILLATION SAMPLING LOSS AND GRADIENTS) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | We use this loss to find modes of the score functions that are present across all noise levels in the diffusion process. | p. 17 (A.4 DERIVING THE SCORE DISTILLATION SAMPLING LOSS AND GRADIENTS), p. 15 (A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 17 / A.4 DERIVING THE SCORE DISTILLATION SAMPLING LOSS AND GRADIENTS - extractive PDF cue:** Here we show how the gradient of this loss leads to the same update as optimizing the training loss LDiff, but without the term corresponding ...
- **p. 17 / A.4 DERIVING THE SCORE DISTILLATION SAMPLING LOSS AND GRADIENTS - extractive PDF cue:** Putting these together, we can use a "sticking-the-landing"-style gradient of our loss by thinking of ϵ as a control variate for ˆϵ: ∇θLSDS = Et,zt/x ...
- **p. 18 / A.4 DERIVING THE SCORE DISTILLATION SAMPLING LOSS AND GRADIENTS - extractive PDF cue:** GAN-like amortized samplers can be learned by minimizing the Stein discrepancy (Hu et al., 2018; Grathwohl et al., 2020), where the optimal critic resembles the ...
- **p. 7 / 3. Diffusion loss with view-dependent conditioning - extractive PDF cue:** Given the rendered image and sampled timestep t, we sample noise ϵ and compute the gradient of the NeRF parameters according to Eqn.
- **p. 7 / 3. Diffusion loss with view-dependent conditioning - extractive PDF cue:** This is much larger than image sampling methods, and is likely required due to the mode-seeking nature of our objective which results in oversmoothing at ...
- **p. 16 / A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS - extractive PDF cue:** If orientation loss is too high, surfaces become oversmoothed.
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 17 (A.4 DERIVING THE SCORE DISTILLATION SAMPLING LOSS AND GRADIENTS), p. 17 (A.4 DERIVING THE SCORE DISTILLATION SAMPLING LOSS AND GRADIENTS), p. 16 (A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS), p. 7 (3. Diffusion loss with view-dependent conditioning), p. 7 (3. Diffusion loss with view-dependent conditioning), p. 16 (A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | GANs, learn, controllable, generators, photographs, single, object, category, placing, adversarial, loss, image, renderings, output | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | GANs, learn, controllable, generators, photographs, single, object, category, placing, adversarial | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | NEURAL, RENDERING, MODEL, NeRF, technique, inverse, consists, volumetric, raytracer, multilayer | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | Here, gradient, loss, leads, same, update, optimizing, training, LDiff, without | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** GANs can learn controllable 3D generators from photographs of a single object category, by placing an adversarial loss on 2D image renderings of the output ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Originally, NeRF was found to work well for "classic" 3D reconstruction tasks: many images of a scene are provided as input to a model, and ...
- **p. 5 / 1 INTRODUCTION - extractive PDF cue:** To synthesize a scene from text, we initialize a NeRF-like model with random weights, then repeatedly render views of that NeRF from random camera positions ...
- **p. 6 / 1 INTRODUCTION - extractive PDF cue:** While our method can generate some complex scenes, we find that it is helpful to only query the NeRF scene representation within a fixed bounding ...
- **p. 6 / 1 INTRODUCTION - extractive PDF cue:** These densities and colors are then alpha-composited from the back of the ray towards the camera, producing the final rendered RGB value for the pixel: ...
- **p. 7 / 3. Diffusion loss with view-dependent conditioning - extractive PDF cue:** We therefore found it beneficial to append view-dependent text to the provided input text based on the location of the randomly sampled camera.
- **p. 15 / A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS - extractive PDF cue:** In NeRF, each 3D input point is mapped to a higher dimensional space using a sinusoidal positional encoding function (Vaswani et al., 2017).
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | Theoretically, with enough timesteps, the optimal reverse process step is also Gaussian and related to an optimal MSE denoiser (Sohl-Dickstein et al., ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | The forward process is typically a Gaussian distribution that transitions from the previous less noisy latent at timestep t to a noisier ... | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not recovered | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | We use Distributed Shampoo (Anil et al., 2020) with β1 = 0.9, β2 = 0.9, exponent override = 2, block size = ... | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 3. Diffusion loss with view-dependent conditioning - extractive PDF cue:** We use the pretrained 64 × 64 base text-to-image model from Saharia et al.
- **p. 8 / 4. Optimization - extractive PDF cue:** Metrics shown in parentheses may be overfit, as the same CLIP model is used during training and eval.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** pretrained, base, text-to-image, model, Saharia, orientation, loss, Ref-NeRF, Verbin, encourage, normal, vectors, density, field, face, toward, camera, when, they, visible.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | We evaluate the ability of DreamFusion to generate coherent 3D scenes from a variety of text prompts. | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Denoiser / vector field | Despite this, DreamFusion outperforms both baselines on color images, and approaches the performance of ground truth images. | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Sampling / downstream interface | Geometry significantly improves with each of these choices and full renderings improve by +12.5%. | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 6: An ablation study of DreamFusion. Left: We evaluate components of our unlit renderings on albedo, full shaded and illuminated renderings and textureless illuminated ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** 6 shows qualitative results for the ablation.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** This ablation also highlights how the albedo renders can be deceiving: our base model achieves the highest score, but exhibits poor geometry (the dog has ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Rendering without color (iv) helps to smooth the geometry, but also causes some color details like the skull and crossbones to be "carved" into the ...
- **p. 15 / Figure/Table caption - extractive PDF cue:** Figure 8: Pseudocode for Score Distillation Sampling with an application-specific generator that defines a differentiable mapping from parameters to images. The gradient g is computed ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: DreamFusion uses a pretrained text-to-image diffusion model to generate realistic 3D models from text prompts. Rendered 3D models are presented from two views, ...
- **p. 9 / 5 DISCUSSION - extractive PDF cue:** Though DreamFusion produces compelling results and outperforms prior work on this task, it still has several limitations.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 7 (3. Diffusion loss with view-dependent conditioning), p. 16 (A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS), p. 17 (A.4 DERIVING THE SCORE DISTILLATION SAMPLING LOSS AND GRADIENTS), p. 15 (A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS), p. 16 (A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS), p. 8 (4. Optimization), objective p. 17 (A.4 DERIVING THE SCORE DISTILLATION SAMPLING LOSS AND GRADIENTS), p. 17 (A.4 DERIVING THE SCORE DISTILLATION SAMPLING LOSS AND GRADIENTS), p. 18 (A.4 DERIVING THE SCORE DISTILLATION SAMPLING LOSS AND GRADIENTS), p. 7 (3. Diffusion loss with view-dependent conditioning), p. 7 (3. Diffusion loss with view-dependent conditioning), p. 16 (A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS), temporal p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 7 (3. Diffusion loss with view-dependent conditioning), p. 15 (A APPENDIX).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
