# Evaluation - DreamFusion: Text-to-3D using 2D Diffusion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2209.14988; PDF retrieval source: https://arxiv.org/pdf/2209.14988. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 2 (Figure/Table caption), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 5 (Figure/Table caption)): Geometry significantly improves with each of these choices and full renderings improve by +12.5%.

## Evaluation Body Digest

- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We evaluate the ability of DreamFusion to generate coherent 3D scenes from a variety of text prompts.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We use the 153 prompts from the object-centric COCO validation subset of Dream Fields.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Left: We evaluate components of our unlit renderings on albedo, full shaded and illuminated renderings and textureless illuminated geometry using CLIP L/14 on object-centric COCO.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** The R-Precision is the accuracy with which CLIP (Radford et al., 2021) retrieves the correct caption among a set of distractors given a rendering of ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** This ablation also highlights how the albedo renders can be deceiving: our base model achieves the highest score, but exhibits poor geometry (the dog has ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Comparison of 2D sampling methods from a text-to-image diffusion model with text "a photo of a tree frog wearing a sweater." For score ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 8: Pseudocode for Score Distillation Sampling with an application-specific generator that defines a differentiable mapping from parameters to images. The gradient g is computed ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Right: visualizations of the impact of each ablation for "A bulldog is wearing a black pirate hat." on albedo (top), shaded (middle), and textureless renderings ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 8); A.3 EXPERIMENTAL SETUP (p. 17).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Geometry significantly improves with each of these choices and full renderings improve by +12.5%. | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Despite this, DreamFusion outperforms both baselines on color images, and approaches the performance of ground truth images. | p. 8 (4 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 1: DreamFusion uses a pretrained text-to-image diffusion model to generate realistic 3D models from text prompts. Rendered 3D models are presented from two ... | p. 2 (Figure/Table caption) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Introducing lighting (iii) improves geometry but darker areas (e.g. the hat) remain non-smooth. | p. 9 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Adding in view-dependent prompts (ii) improves geometry, but the surfaces are highly non-smooth and result in poor shaded renders. | p. 9 (4 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We evaluate the ability of DreamFusion to generate coherent 3D scenes from a variety of text prompts.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We use the 153 prompts from the object-centric COCO validation subset of Dream Fields.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Left: We evaluate components of our unlit renderings on albedo, full shaded and illuminated renderings and textureless illuminated geometry using CLIP L/14 on object-centric COCO.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: DreamFusion uses a pretrained text-to-image diffusion model to generate realistic 3D models from text prompts. Rendered 3D models are presented from two views, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Comparison of 2D sampling methods from a text-to-image diffusion model with text "a photo of a tree frog wearing a sweater." For score ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: DreamFusion generates 3D objects from a natural language caption such as "a DSLR photo of a peacock on a surfboard." The scene is ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: DreamFusion can be used to create and refine 3D scenes. Here we iteratively refine an example text prompt, while rendering each generated scene ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Evaluating the coherence of DreamFusion generations with their caption using different CLIP retrieval models. We compare to the ground-truth MS-COCO images in the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Qualitative comparison with baselines. 4
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 6: An ablation study of DreamFusion. Left: We evaluate components of our unlit renderings on albedo, full shaded and illuminated renderings and textureless illuminated ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 7: Pseudocode for ancestral sampling from DDPM where y is the optional conditioning signal e.g. a caption. Typically, tmax = 1 and tmin = ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate the ability of DreamFusion to generate coherent 3D scenes from a variety of text prompts. | embodiment, simulator version and control stack | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Task/environment | We use the 153 prompts from the object-centric COCO validation subset of Dream Fields. | reset, timeout, object/scene variation | p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 5 (1 INTRODUCTION), p. 6 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The R-Precision is the accuracy with which CLIP (Radford et al., 2021) retrieves the correct caption among a set of distractors given a rendering ... | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| This ablation also highlights how the albedo renders can be deceiving: our base model achieves the highest score, but exhibits poor geometry (the dog ... | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| Figure 2: Comparison of 2D sampling methods from a text-to-image diffusion model with text "a photo of a tree frog wearing a sweater." For ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 8: Pseudocode for Score Distillation Sampling with an application-specific generator that defines a differentiable mapping from parameters to images. The gradient g is ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| Right: visualizations of the impact of each ablation for "A bulldog is wearing a black pirate hat." on albedo (top), shaded (middle), and textureless ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| Albedo Shaded Textureless Render Type 0.0 0.2 0.4 0.6 0.8 1.0 R-Precision Base +ViewAug (i) +ViewDep (ii) +Lighting (iii) +Textureless (iv) (i) (ii) (iii) ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| Our computation of R-Precision differs slightly from baselines. | definition/direction/unit from same section | p. 17 (A.3 EXPERIMENTAL SETUP) |
| DreamFusion evaluates at 30◦since it is not prone to this issue, but averages the metric over multiple azimuths to reduce variance. | definition/direction/unit from same section | p. 17 (A.3 EXPERIMENTAL SETUP) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Despite this, DreamFusion outperforms both baselines on color images, and approaches the performance of ground truth images. | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| These include Dream Fields, CLIP-Mesh (which optimizes a mesh with CLIP), and an oracle that evaluates the original captioned image pairs in MS-COCO. | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| Our computation of R-Precision differs slightly from baselines. | comparison identity and matched condition | p. 17 (A.3 EXPERIMENTAL SETUP) |
| The base method (i) without view-dependent prompts results in a multi-faced dog with flat geometry. | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| Rendering without color (iv) helps to smooth the geometry, but also causes some color details like the skull and crossbones to be "carved" into ... | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| Figure 2: Comparison of 2D sampling methods from a text-to-image diffusion model with text "a photo of a tree frog wearing a sweater." For ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 6: An ablation study of DreamFusion. Left: We evaluate components of our unlit renderings on albedo, full shaded and illuminated renderings and textureless ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| 6 shows qualitative results for the ablation. | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| This ablation also highlights how the albedo renders can be deceiving: our base model achieves the highest score, but exhibits poor geometry (the dog ... | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| Rendering without color (iv) helps to smooth the geometry, but also causes some color details like the skull and crossbones to be "carved" into ... | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| Figure 8: Pseudocode for Score Distillation Sampling with an application-specific generator that defines a differentiable mapping from parameters to images. The gradient g is ... | component/input/data sensitivity | p. 15 (Figure/Table caption) |
| Figure 1: DreamFusion uses a pretrained text-to-image diffusion model to generate realistic 3D models from text prompts. Rendered 3D models are presented from two ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| 3.1 NEURAL RENDERING OF A 3D MODEL NeRF is a technique for neural inverse rendering that consists of a volumetric raytracer and a multilayer ... | Geometry significantly improves with each of these choices and full renderings improve by +12.5%. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 2 (Figure/Table caption), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 5 (Figure/Table caption) |
| Primary metric/result | Despite this, DreamFusion outperforms both baselines on color images, and approaches the performance of ground truth images. | numeric claim only at cited anchor | p. 8 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / 4. Optimization - extractive body cue:** We optimize for 15,000 iterations which takes around 1.5 hours.
- **p. 8 / 4. Optimization - extractive body cue:** (2022). †Evaluated with only 1 seed per prompt.
- **p. 17 / A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS - extractive body cue:** We use Distributed Shampoo (Anil et al., 2020) with β1 = 0.9, β2 = 0.9, exponent override = 2, block size = 128, graft type ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Though DreamFusion produces compelling results and outperforms prior work on this task, it still has several limitations. | p. 9 (5 DISCUSSION) |
| body limitation/failure cue | DreamFusion does not require 3D or multi-view training data, and uses only a pre-trained 2D diffusion model (trained on only 2D images) to perform ... | p. 9 (5 DISCUSSION) |
| body limitation/failure cue | Figure 3: DreamFusion generates 3D objects from a natural language caption such as "a DSLR photo of a peacock on a surfboard." The scene ... | p. 5 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We use Distributed Shampoo (Anil et al., 2020) with β1 = 0.9, β2 = 0.9, exponent override = 2, block size = 128, graft ... | p. 17 (A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS) |
| We also compare against an enhanced reimplementation of Dream Fields where we use our own 3D representation (Sec. | p. 8 (4 EXPERIMENTS) |
| While our implementation of Dream Fields performs nearly at chance when evaluating geometry (Geo) with textureless renders, DreamFusion is consistent with captions 58.5% of ... | p. 8 (4 EXPERIMENTS) |
| Representative settings are 5 × 10-2 and 2 × 10-3 for the initial and final values of λΣ, linearly annealed for the first 5k ... | p. 15 (A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS) |
| Our model builds upon mip-NeRF 360 (Barron et al., 2022) (starting from the publicly available implementation 2022), which is an improved version of NeRF ... | p. 15 (A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS) |
| This weight is annealed in starting from 10-4 over the first 5k (out of 15k) steps. | p. 16 (A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS) |
| For the first 1k steps of optimization we set the ambient light color ℓa to 1 and the diffuse light color ℓρ to 0, ... | p. 16 (A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS) |
| In our main results in Table 1, we evaluate all captions with 2 generation seeds unless otherwise noted. | p. 17 (A.3 EXPERIMENTAL SETUP) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 5 DISCUSSION - extractive body cue:** Though DreamFusion produces compelling results and outperforms prior work on this task, it still has several limitations.
- **p. 9 / 5 DISCUSSION - extractive body cue:** DreamFusion does not require 3D or multi-view training data, and uses only a pre-trained 2D diffusion model (trained on only 2D images) to perform 3D ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: DreamFusion generates 3D objects from a natural language caption such as "a DSLR photo of a peacock on a surfboard." The scene is ...

- **Evidence anchors reviewed:** datasets p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), metrics p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 4 (Figure/Table caption), p. 15 (Figure/Table caption), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), baselines p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 17 (A.3 EXPERIMENTAL SETUP), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 4 (Figure/Table caption), results p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 2 (Figure/Table caption), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 5 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
