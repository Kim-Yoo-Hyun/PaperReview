# Problem - DreamFusion: Text-to-3D using 2D Diffusion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2209.14988; PDF retrieval source: https://arxiv.org/pdf/2209.14988. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 5 (1 INTRODUCTION)): This work showed that pretrained 2D image-text models may be used for 3D synthesis, though 3D objects produced by this approach tend to lack realism and accuracy.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive PDF cue:** Recent breakthroughs in text-to-image synthesis have been driven by diffusion models trained on billions of image-text pairs.
- **p. 1 / ABSTRACT - extractive PDF cue:** Adapting this approach to 3D synthesis would require large-scale datasets of labeled 3D data and efficient architectures for denoising 3D data, neither of which currently ...
- **p. 1 / ABSTRACT - extractive PDF cue:** In this work, we circumvent these limitations by using a pretrained 2D text-to-image diffusion model to perform text-to-3D synthesis.
- **p. 1 / ABSTRACT - extractive PDF cue:** We introduce a loss based on probability density distillation that enables the use of a 2D diffusion model as a prior for optimization of a ...
- **p. 1 / ABSTRACT - extractive PDF cue:** Using this loss in a DeepDream-like procedure, we optimize a randomly-initialized 3D model (a Neural Radiance Field, or NeRF) via gradient descent such that its ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** This work showed that pretrained 2D image-text models may be used for 3D synthesis, though 3D objects produced by this approach tend to lack realism ...
- **p. 4 / 1 INTRODUCTION - extractive PDF cue:** To understand the difficulties of this approach, consider the gradient of LDiff: ∇θLDiff(φ, x = g(θ)) = Et,ϵ " w(t) (ˆϵφ(zt; y, t) -ϵ) / ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This work showed that pretrained 2D image-text models may be used for 3D synthesis, though 3D objects produced by this approach tend ... | high-dimensional data 또는 robot action-trajectory distribution | body wording is the source claim |
| Observation / input | GANs can learn controllable 3D generators from photographs of a single object category, by placing an adversarial loss on 2D image renderings ... | conditioning observation와 noisy/intermediate sample | exact sensor/frame/preprocessing from PDF |
| State / latent | GANs, learn, controllable, generators, photographs, single, object, category, placing, adversarial | latent/noise variable와 conditional distribution | notation and tensor shape require body check |
| Output / action | synthesize, scene, text, initialize, NeRF-like, model, random, weights | generated sample, action chunk 또는 trajectory | exact unit/frame/decoder require body check |
| Target outcome | sample quality, diversity and latency | distribution fit, multimodality, sample quality와 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | data x₀, noisy state x_t, condition c; body terms: GANs, learn, controllable, generators, photographs, single, object, category, placing, adversarial | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 5 (1 INTRODUCTION) |
| Decision / output variable | sample/action x̂ or trajectory; body terms: NEURAL, RENDERING, MODEL, NeRF, technique, inverse, consists, volumetric | p. 5 (1 INTRODUCTION), p. 6 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Objective / loss / cost | distribution/denoising/flow objective; cue terms: Here, gradient, loss, leads, same, update, optimizing, training | p. 17 (A.4 DERIVING THE SCORE DISTILLATION SAMPLING LOSS AND GRADIENTS), p. 17 (A.4 DERIVING THE SCORE DISTILLATION SAMPLING LOSS AND GRADIENTS), p. 16 (A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS), p. 7 (3. Diffusion loss with view-dependent conditioning), p. 7 (3. Diffusion loss with view-dependent conditioning), p. 16 (A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (3. Diffusion loss with view-dependent conditioning), p. 7 (3. Diffusion loss with view-dependent conditioning), p. 16 (A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS) |
| Success / guarantee | sample quality, diversity and latency | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 4 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 4 / 1 INTRODUCTION - extractive PDF cue:** To understand the difficulties of this approach, consider the gradient of LDiff: ∇θLDiff(φ, x = g(θ)) = Et,ϵ " w(t) (ˆϵφ(zt; y, t) -ϵ) / ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** 3D assets are currently designed by hand in modeling software like Blender and Maya3D, a process requiring a great deal of time and expertise.
- **p. 4 / 1 INTRODUCTION - extractive PDF cue:** Concurrent work from Graikos et al.
- **p. 5 / 1 INTRODUCTION - extractive PDF cue:** 3 THE DREAMFUSION ALGORITHM Now that we have demonstrated how a diffusion model can be used as a loss within a generic continuous optimization problem ...

## What the Paper Changes

PDF contribution framing (p. 5 (1 INTRODUCTION), p. 6 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 5 (1 INTRODUCTION)): 3.1 NEURAL RENDERING OF A 3D MODEL NeRF is a technique for neural inverse rendering that consists of a volumetric raytracer and a multilayer perceptron (MLP).

- **p. 6 / 1 INTRODUCTION - extractive PDF cue:** While our method can generate some complex scenes, we find that it is helpful to only query the NeRF scene representation within a fixed bounding ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** The resulting Score Distillation Sampling (SDS) method enables sampling via optimization in differentiable image parameterizations.
- **p. 4 / 1 INTRODUCTION - extractive PDF cue:** Though conditional diffusion sampling enables quite a bit of flexibility (e.g. inpainting), diffusion models trained on pixels have traditionally been used to sample only pixels.
- **p. 5 / 1 INTRODUCTION - extractive PDF cue:** SDS produces detail comparable to ancestral sampling, but enables new transfer learning applications because it operates in parameter space.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Though DreamFusion produces compelling results and outperforms prior work on this task, it still has several limitations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | DreamFusion does not require 3D or multi-view training data, and uses only a pre-trained 2D diffusion model (trained ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Figure 3: DreamFusion generates 3D objects from a natural language caption such as "a DSLR photo of a ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

generative writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 5 (1 INTRODUCTION), p. 6 (1 INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 5 (1 INTRODUCTION), interface p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 5 (1 INTRODUCTION), p. 6 (1 INTRODUCTION), objective p. 17 (A.4 DERIVING THE SCORE DISTILLATION SAMPLING LOSS AND GRADIENTS), p. 17 (A.4 DERIVING THE SCORE DISTILLATION SAMPLING LOSS AND GRADIENTS), p. 16 (A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS), p. 7 (3. Diffusion loss with view-dependent conditioning), p. 7 (3. Diffusion loss with view-dependent conditioning), p. 16 (A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
