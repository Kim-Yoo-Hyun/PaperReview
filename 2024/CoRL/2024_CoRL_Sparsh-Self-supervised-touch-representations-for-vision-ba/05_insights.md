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

- **Paper-specific interface:** We present Sparsh, a family of SSL models that can support various vision-based tactile sensors, alleviating the need for custom labels through pre-training on 460k+ tactile images with masking and ... (p. 1, Abstract).
- **Paper-specific mechanism:** Our contributions are as follows: 1. (p. 2, 1 Introduction).
- **Evidence boundary:** the reported outcome is Figure 4: Summary of results comparing Sparsh and E2E on [T1]-[T6] tasks in TacBench across varying amounts of labeled data. Pre-training with SSL yields general touch representations that work across ... (p. 7, Figure/Table caption); the relevant task/metric cue is Figure 12: Contrast between Sparsh (VJEPA) and E2E for a test trajectory with a spherical probe sliding on the DIGIT sensor. Sparsh (VJEPA), even though trained only on 33% of ... (p. 24, Figure/Table caption). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** In Figure 13, we illustrate a failure case for Sparsh (VJEPA), as its results do not align with the ground truth. (p. 24, Model).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, tactile sensing, self-supervised learning, foundation model, contact`.
- **Reading predecessor in the generated track queue:** FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Octopi: Object Property Reasoning with Large Tactile-Language Models (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 13: Failure case where the ground truth does not reflect slip since it relies on an experimental coefficient of friction. Despite the inaccuracies in the friction boundary for this trajectory, Sparsh ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: We present Sparsh, a family of SSL models that can support various vision-based tactile sensors, alleviating the need for custom labels through pre-training on 460k+ tactile images with masking and ... (p. 1, Abstract); preserve the objective/update rule: For example, feature extractors trained on GelSight with markers may not transfer to other sensors, and encoders optimized for texture recognition [15] may not be suitable for tasks that require ... (p. 2, 1 Introduction).
2. Use the paper-reported task/data/environment cue: Finally, we construct TacBench, a benchmark consisting of six touch-centric tasks that cover the space of relevant problems on tactile properties such as force estimation and slip detection, on perception ... (p. 2, 1 Introduction).
3. Compare against the reported or matched baseline: Table 13: Performance of Sparsh across TacBench and comparison between SSL approaches. E Sparsh ablations E.1 TacBench evaluations via fine-tuning Fine-tuning the Sparsh encoders is another method of assessing the ... (p. 29, Figure/Table caption).
4. Report the body metric with its denominator and aggregation: Figure 12: Contrast between Sparsh (VJEPA) and E2E for a test trajectory with a spherical probe sliding on the DIGIT sensor. Sparsh (VJEPA), even though trained only on 33% of ... (p. 24, Figure/Table caption).
5. Re-run the reported ablation or stress/failure condition: Table 2: Number of parameters and inference time for Sparsh backbones All the models are pretrained without a [cls] token. For DINO, which decodes the [cls] token into classes, we ... (p. 18, Figure/Table caption); if none is reported, design one around: In Figure 13, we illustrate a failure case for Sparsh (VJEPA), as its results do not align with the ground truth. (p. 24, Model).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1 Introduction), p. 2 (1 Introduction), match the reported outcome at p. 7 (Figure/Table caption), p. 1 (Figure/Table caption), p. 24 (Figure/Table caption), and measure the boundary at p. 24 (Model), p. 28 (Model).

## Falsifiable research question

Under the paper's stated interface (We present Sparsh, a family of SSL models that can support various vision-based tactile sensors, alleviating the need for custom labels through ...), does the paper-specific mechanism (Our contributions are as follows: 1.) retain the reported evaluation outcome (Figure 12: Contrast between Sparsh (VJEPA) and E2E for a test trajectory with a spherical probe sliding on ...) when tested against the paper's strongest explicit boundary (In Figure 13, we illustrate a failure case for Sparsh (VJEPA), as its results do not align with ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Figure 12: Contrast between Sparsh (VJEPA) and E2E for a test trajectory with a spherical probe sliding on ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (31 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Our contributions are as follows: 1. (p. 2, 1 Introduction).
- **Paper-supported outcome:** Figure 4: Summary of results comparing Sparsh and E2E on [T1]-[T6] tasks in TacBench across varying amounts of labeled data. Pre-training with SSL yields general touch representations that work across ... (p. 7, Figure/Table caption).
- **Strongest explicit boundary:** In Figure 13, we illustrate a failure case for Sparsh (VJEPA), as its results do not align with the ground truth. (p. 24, Model).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
