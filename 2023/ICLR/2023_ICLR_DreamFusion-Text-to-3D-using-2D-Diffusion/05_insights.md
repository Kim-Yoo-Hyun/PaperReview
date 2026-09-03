# Insights — DreamFusion: Text-to-3D using 2D Diffusion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2209.14988; PDF retrieval source: https://arxiv.org/pdf/2209.14988. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 5 / 1 INTRODUCTION - extractive body cue:** 3.1 NEURAL RENDERING OF A 3D MODEL NeRF is a technique for neural inverse rendering that consists of a volumetric raytracer and a multilayer perceptron ...
- **p. 6 / 1 INTRODUCTION - extractive body cue:** While our method can generate some complex scenes, we find that it is helpful to only query the NeRF scene representation within a fixed bounding ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** The resulting Score Distillation Sampling (SDS) method enables sampling via optimization in differentiable image parameterizations.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Though conditional diffusion sampling enables quite a bit of flexibility (e.g. inpainting), diffusion models trained on pixels have traditionally been used to sample only pixels.
- **p. 5 / 1 INTRODUCTION - extractive body cue:** SDS produces detail comparable to ancestral sampling, but enables new transfer learning applications because it operates in parameter space.
- **p. 7 / 3. Diffusion loss with view-dependent conditioning - extractive body cue:** We use the pretrained 64 × 64 base text-to-image model from Saharia et al.
- **p. 16 / A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS - extractive body cue:** We use the orientation loss proposed by Ref-NeRF (Verbin et al., 2022) to encourage normal vectors of the density field to face toward the camera ...
- **Contribution anchor:** p. 5 (1 INTRODUCTION), p. 6 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 5 (1 INTRODUCTION), p. 7 (3. Diffusion loss with view-dependent conditioning)

### Strongest assumption and failure boundary

- **p. 3 / 1 INTRODUCTION - extractive body cue:** This work showed that pretrained 2D image-text models may be used for 3D synthesis, though 3D objects produced by this approach tend to lack realism ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** To understand the difficulties of this approach, consider the gradient of LDiff: ∇θLDiff(φ, x = g(θ)) = Et,ϵ " w(t) (ˆϵφ(zt; y, t) -ϵ) / ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** 3D assets are currently designed by hand in modeling software like Blender and Maya3D, a process requiring a great deal of time and expertise.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Concurrent work from Graikos et al.
- **p. 5 / 1 INTRODUCTION - extractive body cue:** 3 THE DREAMFUSION ALGORITHM Now that we have demonstrated how a diffusion model can be used as a loss within a generic continuous optimization problem ...
- **p. 9 / 5 DISCUSSION - extractive body cue:** Though DreamFusion produces compelling results and outperforms prior work on this task, it still has several limitations.
- **p. 9 / 5 DISCUSSION - extractive body cue:** DreamFusion does not require 3D or multi-view training data, and uses only a pre-trained 2D diffusion model (trained on only 2D images) to perform 3D ...
- **Boundary to test:** Though DreamFusion produces compelling results and outperforms prior work on this task, it still has several limitations.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | 3.1 NEURAL RENDERING OF A 3D MODEL NeRF is a technique for neural inverse rendering that consists of a volumetric raytracer and a multilayer perceptron (MLP). | p. 5 (1 INTRODUCTION), p. 6 (1 INTRODUCTION) |
| Reported outcome | Geometry significantly improves with each of these choices and full renderings improve by +12.5%. | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Failure/limitation | Though DreamFusion produces compelling results and outperforms prior work on this task, it still has several limitations. | p. 9 (5 DISCUSSION), p. 9 (5 DISCUSSION) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `conditioning observation와 noisy/intermediate sample → latent/noise variable와 conditional distribution → generated sample, action chunk 또는 trajectory`.
- 이 논문의 재사용 가능한 지점은 GANs can learn controllable 3D generators from photographs of a single object category, by placing an adversarial loss on 2D image renderings of the output 3D object or scene (Henzler et al., ...를 Originally, NeRF was found to work well for "classic" 3D reconstruction tasks: many images of a scene are provided as input to a model, and a NeRF is optimized to recover the ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 latent/noise variable와 conditional distribution가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Though DreamFusion produces compelling results and outperforms prior work on this task, it still has several limitations.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: 3.1 NEURAL RENDERING OF A 3D MODEL NeRF is a technique for neural inverse rendering that consists of a volumetric raytracer and a multilayer perceptron (MLP).
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `3D Vision, Diffusion, Generation, text-to-3D`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Though DreamFusion produces compelling results and outperforms prior work on this task, it still has several limitations.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We evaluate the ability of DreamFusion to generate coherent 3D scenes from a variety of text prompts..
3. Compare against the body-reported baseline or a matched simpler baseline: Despite this, DreamFusion outperforms both baselines on color images, and approaches the performance of ground truth images..
4. Report the body metric and its denominator/aggregation: The R-Precision is the accuracy with which CLIP (Radford et al., 2021) retrieves the correct caption among a set of distractors given a rendering of the scene..
5. Re-run the body-reported ablation/failure condition: Figure 6: An ablation study of DreamFusion. Left: We evaluate components of our unlit renderings on albedo, full shaded and illuminated renderings and textureless illuminated geometry using CLIP L/14 on object-centric COCO. ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 7 (3. Diffusion loss with view-dependent conditioning), p. 16 (A.2 NERF DETAILS AND TRAINING HYPERPARAMETERS), p. 17 (A.4 DERIVING THE SCORE DISTILLATION SAMPLING LOSS AND GRADIENTS); the primary result is directionally consistent at p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 2 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 NEURAL, RENDERING, MODEL mechanism이 Despite this, DreamFusion outperforms both baselines on color images, and approaches the performance of ground truth ... 대비 The R-Precision is the accuracy with which CLIP (Radford et al., 2021) retrieves the correct caption among a ...을 개선하고, Though DreamFusion produces compelling results and outperforms prior work on this task, it still has several ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
