# Insights — Sparsh: Self-supervised touch representations for vision-based tactile sensing

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2410.24090; PDF retrieval source: https://arxiv.org/pdf/2410.24090. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** In this work, we introduce a family of touch representations for vision-based tactile sensors trained with SSL.
- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are as follows: 1.
- **p. 1 / Abstract - extractive body cue:** We present Sparsh, a family of SSL models that can support various vision-based tactile sensors, alleviating the need for custom labels through pre-training on 460k+ ...
- **p. 8 / 8 Discussion - extractive body cue:** We evaluated five SSL approaches (see Figure 2) comparing their performance against task and sensor specific models through TacBench, a benchmark of six touch-centric tasks ...
- **p. 2 / 1 Introduction - extractive body cue:** For example, feature extractors trained on GelSight with markers may not transfer to other sensors, and encoders optimized for texture recognition [15] may not be ...
- **p. 8 / 8 Discussion - extractive body cue:** Open-source tactile datasets we considered in this study predominantly feature discrete contact interactions.
- **p. 8 / 8 Discussion - extractive body cue:** Notably, models pre-trained in latent space perform better in downstream tasks when fully fine-tuned, especially in regression tasks like force and pose estimation.
- **Contribution anchor:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 8 (8 Discussion), p. 2 (1 Introduction), p. 8 (8 Discussion)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** Curation of new & existing datasets, unlabeled for SSL and labeled for benchmarking.
- **p. 2 / 1 Introduction - extractive body cue:** Pulling together additional unlabeled data points from the existing datasets we train our models on a total of 460k+ tactile images.
- **p. 25 / Figure/Table caption - extractive body cue:** Figure 13: Failure case where the ground truth does not reflect slip since it relies on an experimental coefficient of friction. Despite the inaccuracies in ...
- **p. 24 / Figure/Table caption - extractive body cue:** Figure 12: Contrast between Sparsh (VJEPA) and E2E for a test trajectory with a spherical probe sliding on the DIGIT sensor. Sparsh (VJEPA), even though ...
- **p. 28 / Figure/Table caption - extractive body cue:** Table 11: Mean and variance of distance traversed (in cm) before failure for policies based on Sparsh and E2E. Results over 10 randomized novel starting ...
- **p. 8 / 8 Discussion - extractive body cue:** Both models perform similarly in bead maze test demonstrations, which require implicit knowledge of shear forces and slip.
- **p. 8 / 8 Discussion - extractive body cue:** Using as little as 10% or 1% of the labeled data for force estimation and slip detection still yields acceptable results (e.g. force error below ...
- **Boundary to test:** Figure 13: Failure case where the ground truth does not reflect slip since it relies on an experimental coefficient of friction. Despite the inaccuracies in the friction boundary for this trajectory, Sparsh ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this work, we introduce a family of touch representations for vision-based tactile sensors trained with SSL. | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | Figure 4: Summary of results comparing Sparsh and E2E on [T1]-[T6] tasks in TacBench across varying amounts of labeled data. Pre-training with SSL yields general touch representations that work across several tasks ... | p. 7 (Figure/Table caption), p. 8 (8 Discussion) |
| Failure/limitation | Figure 13: Failure case where the ground truth does not reflect slip since it relies on an experimental coefficient of friction. Despite the inaccuracies in the friction boundary for this trajectory, Sparsh ... | p. 25 (Figure/Table caption), p. 24 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `tactile image/force, vision과 proprioceptive history → contact geometry, force state 또는 latent dynamics → grasp/contact action, force command 또는 object motion`.
- 이 논문의 재사용 가능한 지점은 Vision-based tactile sensors [1, 2, 3, 4] have emerged as the leading form factor capable of capturing images of physical interactions at the sensor-objectenvironment interface, often inaccessible through vision.를 In particular, we find Sparsh (DINO) is well suited for physics-based tasks like force and pose estimation, while Sparsh (IJEPA) performs better at touch semantic understanding like slip state, stability of a ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 contact geometry, force state 또는 latent dynamics가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 13: Failure case where the ground truth does not reflect slip since it relies on an experimental coefficient of friction. Despite the inaccuracies in the friction boundary for this trajectory, Sparsh ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this work, we introduce a family of touch representations for vision-based tactile sensors trained with SSL.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, tactile sensing, self-supervised learning, foundation model, contact`.
- **Reading predecessor in the generated track queue:** FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Octopi: Object Property Reasoning with Large Tactile-Language Models (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 13: Failure case where the ground truth does not reflect slip since it relies on an experimental coefficient of friction. Despite the inaccuracies in the friction boundary for this trajectory, Sparsh ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Finally, we construct TacBench, a benchmark consisting of six touch-centric tasks that cover the space of relevant problems on tactile properties such as force estimation and slip detection, on perception such as ....
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 2: (a) We curate new and existing datasets of vision-based tactile sensors to train touch representations by adapting state-of-the-art SSL vision methods to the tactile domain, namely (b) Masked Autoencoder (MAE) ....
4. Report the body metric and its denominator/aggregation: Table 11: Mean and variance of distance traversed (in cm) before failure for policies based on Sparsh and E2E. Results over 10 randomized novel starting locations on the bead maze. In Table ....
5. Re-run the body-reported ablation/failure condition: Table 2: Number of parameters and inference time for Sparsh backbones All the models are pretrained without a [cls] token. For DINO, which decodes the [cls] token into classes, we repurpose ViT ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction); the primary result is directionally consistent at p. 7 (Figure/Table caption), p. 8 (8 Discussion), p. 1 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 introduce, family, touch mechanism이 Figure 2: (a) We curate new and existing datasets of vision-based tactile sensors to train touch ... 대비 Table 11: Mean and variance of distance traversed (in cm) before failure for policies based on Sparsh and ...을 개선하고, Figure 13: Failure case where the ground truth does not reflect slip since it relies on ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
