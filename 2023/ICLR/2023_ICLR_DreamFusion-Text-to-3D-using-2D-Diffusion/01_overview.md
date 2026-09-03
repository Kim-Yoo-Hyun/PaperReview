# DreamFusion: Text-to-3D using 2D Diffusion

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2209.14988.
> PDF retrieval source: https://arxiv.org/pdf/2209.14988. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, Diffusion, Generation, text-to-3D
- Official paper: https://arxiv.org/abs/2209.14988
- Full-text retrieval: https://arxiv.org/pdf/2209.14988
- Code/Project: https://dreamfusion3d.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 This work showed that pretrained 2D image-text models may be used for 3D synthesis, though 3D objects produced by this approach tend to lack realism and accuracy.를 문제로 두고, 3.1 NEURAL RENDERING OF A 3D MODEL NeRF is a technique for neural inverse rendering that consists of a volumetric raytracer and a multilayer perceptron (MLP).를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Recent breakthroughs in text-to-image synthesis have been driven by diffusion models trained on billions of image-text pairs.
- **p. 1 / ABSTRACT - extractive body cue:** Adapting this approach to 3D synthesis would require large-scale datasets of labeled 3D data and efficient architectures for denoising 3D data, neither of which currently ...
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we circumvent these limitations by using a pretrained 2D text-to-image diffusion model to perform text-to-3D synthesis.
- **p. 1 / ABSTRACT - extractive body cue:** We introduce a loss based on probability density distillation that enables the use of a 2D diffusion model as a prior for optimization of a ...
- **p. 1 / ABSTRACT - extractive body cue:** Using this loss in a DeepDream-like procedure, we optimize a randomly-initialized 3D model (a Neural Radiance Field, or NeRF) via gradient descent such that its ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** This work showed that pretrained 2D image-text models may be used for 3D synthesis, though 3D objects produced by this approach tend to lack realism ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** To understand the difficulties of this approach, consider the gradient of LDiff: ∇θLDiff(φ, x = g(θ)) = Et,ϵ " w(t) (ˆϵφ(zt; y, t) -ϵ) / ...

## Core Idea

- **p. 5 / 1 INTRODUCTION - extractive body cue:** 3.1 NEURAL RENDERING OF A 3D MODEL NeRF is a technique for neural inverse rendering that consists of a volumetric raytracer and a multilayer perceptron ...
- **p. 6 / 1 INTRODUCTION - extractive body cue:** While our method can generate some complex scenes, we find that it is helpful to only query the NeRF scene representation within a fixed bounding ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** The resulting Score Distillation Sampling (SDS) method enables sampling via optimization in differentiable image parameterizations.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Though conditional diffusion sampling enables quite a bit of flexibility (e.g. inpainting), diffusion models trained on pixels have traditionally been used to sample only pixels.
- **p. 5 / 1 INTRODUCTION - extractive body cue:** SDS produces detail comparable to ancestral sampling, but enables new transfer learning applications because it operates in parameter space.
- **p. 7 / 3. Diffusion loss with view-dependent conditioning - extractive body cue:** We use the pretrained 64 × 64 base text-to-image model from Saharia et al.
- **p. 16 / A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS - extractive body cue:** We use the orientation loss proposed by Ref-NeRF (Verbin et al., 2022) to encourage normal vectors of the density field to face toward the camera ...
- **p. 17 / A.4 DERIVING THE SCORE DISTILLATION SAMPLING LOSS AND GRADIENTS - extractive body cue:** We use this loss to find modes of the score functions that are present across all noise levels in the diffusion process.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | GANs can learn controllable 3D generators from photographs of a single object category, by placing an adversarial loss on 2D image renderings of the output 3D object or scene (Henzler et al., ... | conditioning observation와 noisy/intermediate sample | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| State/latent | GANs, learn, controllable, generators, photographs, single, object, category, placing, adversarial, loss, image | latent/noise variable와 conditional distribution | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 5 (1 INTRODUCTION) |
| Output/action | Originally, NeRF was found to work well for "classic" 3D reconstruction tasks: many images of a scene are provided as input to a model, and a NeRF is optimized to recover the ... | generated sample, action chunk 또는 trajectory | p. 1 (1 INTRODUCTION), p. 5 (1 INTRODUCTION), p. 6 (1 INTRODUCTION) |
| Objective/outcome | Here we show how the gradient of this loss leads to the same update as optimizing the training loss LDiff, but without the term corresponding to the Jacobian of the diffusion U-Net. | distribution fit, multimodality, sample quality와 latency | p. 17 (A.4 DERIVING THE SCORE DISTILLATION SAMPLING LOSS AND GRADIENTS), p. 17 (A.4 DERIVING THE SCORE DISTILLATION SAMPLING LOSS AND GRADIENTS), p. 18 (A.4 DERIVING THE SCORE DISTILLATION SAMPLING LOSS AND GRADIENTS) |

## Main Claims and Actual Contribution

- **p. 5 / 1 INTRODUCTION - extractive body cue:** 3.1 NEURAL RENDERING OF A 3D MODEL NeRF is a technique for neural inverse rendering that consists of a volumetric raytracer and a multilayer perceptron ...
- **p. 6 / 1 INTRODUCTION - extractive body cue:** While our method can generate some complex scenes, we find that it is helpful to only query the NeRF scene representation within a fixed bounding ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** The resulting Score Distillation Sampling (SDS) method enables sampling via optimization in differentiable image parameterizations.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Though conditional diffusion sampling enables quite a bit of flexibility (e.g. inpainting), diffusion models trained on pixels have traditionally been used to sample only pixels.
- **p. 5 / 1 INTRODUCTION - extractive body cue:** SDS produces detail comparable to ancestral sampling, but enables new transfer learning applications because it operates in parameter space.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Geometry significantly improves with each of these choices and full renderings improve by +12.5%.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Despite this, DreamFusion outperforms both baselines on color images, and approaches the performance of ground truth images.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: DreamFusion uses a pretrained text-to-image diffusion model to generate realistic 3D models from text prompts. Rendered 3D models are presented from two views, ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Embodiment/environment | We evaluate the ability of DreamFusion to generate coherent 3D scenes from a variety of text prompts. | hardware/simulator version and reset protocol | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Dataset/benchmark | Left: We evaluate components of our unlit renderings on albedo, full shaded and illuminated renderings and textureless illuminated geometry using CLIP L/14 on object-centric COCO. | role, split, size and leakage | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Metric | The R-Precision is the accuracy with which CLIP (Radford et al., 2021) retrieves the correct caption among a set of distractors given a rendering of the scene. | definition, denominator, direction and uncertainty | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 4 (Figure/Table caption) |
| Baseline/ablation | Despite this, DreamFusion outperforms both baselines on color images, and approaches the performance of ground truth images. | fair input/data/compute/action matching | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 17 (A.3 EXPERIMENTAL SETUP) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 5 DISCUSSION - extractive body cue:** Though DreamFusion produces compelling results and outperforms prior work on this task, it still has several limitations.
- **p. 9 / 5 DISCUSSION - extractive body cue:** DreamFusion does not require 3D or multi-view training data, and uses only a pre-trained 2D diffusion model (trained on only 2D images) to perform 3D ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: DreamFusion generates 3D objects from a natural language caption such as "a DSLR photo of a peacock on a surfboard." The scene is ...

## Why Read It

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 This work showed that pretrained 2D image-text models may be used for 3D synthesis, though 3D objects produced by this approach tend to lack realism and accuracy.를 문제로 두고, 3.1 NEURAL RENDERING OF A 3D MODEL NeRF is a technique for neural inverse rendering that consists of a volumetric raytracer and a multilayer perceptron (MLP).를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 5 (1 INTRODUCTION), p. 7 (3. Diffusion loss with view-dependent conditioning) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
