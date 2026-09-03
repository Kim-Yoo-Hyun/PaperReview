# Insights — Open X-Embodiment: Robotic Learning Datasets and RT-X Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2310.08864; PDF retrieval source: https://arxiv.org/pdf/2310.08864. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** Addressing goal (1), our empirical contribution is to demonstrate that several recent robotic learning methods, with minimal modification, can utilize X-embodiment data and enable positive ...
- **p. 3 / III. THE OPEN X-EMBODIMENT REPOSITORY - extractive body cue:** We introduce the Open X-Embodiment Repository (robotics-transformer-x.github.io) - an open-source repository which includes large-scale data along with pre-trained model checkpoints for X-embodied robot learning research.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We show that the resulting models, which we call RT-X, can improve over policies trained only on data from the evaluation domain, exhibiting better generalization ...
- **p. 4 / 5 Hz - extractive body cue:** RT-1-X is an architecture designed for robotics, with a FiLM [116] conditioned EfficientNet [117] and a Transformer [118].
- **p. 4 / IV. RT-X DESIGN - extractive body cue:** Although both architectures are described in detail in their original papers [8, 9], we provide a short summary of each below: RT-1 [8] is a ...
- **p. 4 / IV. RT-X DESIGN - extractive body cue:** Policy architectures We consider two model architectures in our experiments: (1) RT-1 [8], an efficient Transformer-based architecture designed for robotic control, and (2) RT-2 [9] ...
- **p. 4 / IV. RT-X DESIGN - extractive body cue:** These tokens are fed into a decoder-only Transformer, which outputs the tokenized actions.
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 3 (III. THE OPEN X-EMBODIMENT REPOSITORY), p. 2 (I. INTRODUCTION), p. 4 (5 Hz), p. 4 (IV. RT-X DESIGN), p. 4 (IV. RT-X DESIGN)

### Strongest assumption and failure boundary

- **p. 2 / I. INTRODUCTION - extractive body cue:** However, these lessons are difficult to apply in robotics: any single robotic domain might be too narrow, and while computer vision and NLP can leverage ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** How can we overcome these challenges in robotics and move the field of robotic learning toward large data regime that has been so successful in ...
- **p. 5 / V. EXPERIMENTAL RESULTS - extractive body cue:** In the largedataset setting, the RT-1-X model does not outperform the RT-1 baseline trained on only the embodiment-specific dataset, which indicates underfitting for that model ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** DISCUSSION, FUTURE WORK, AND OPEN PROBLEMS We presented a consolidated dataset that combines data from 22 robotic embodiments collected through a collaboration between 21 institutions, ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** 5: To assess transfer between embodiments, we evaluate the RT-2-X model on out-of-distribution skills.
- **Boundary to test:** In the largedataset setting, the RT-1-X model does not outperform the RT-1 baseline trained on only the embodiment-specific dataset, which indicates underfitting for that model class.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Addressing goal (1), our empirical contribution is to demonstrate that several recent robotic learning methods, with minimal modification, can utilize X-embodiment data and enable positive transfer. | p. 2 (I. INTRODUCTION), p. 3 (III. THE OPEN X-EMBODIMENT REPOSITORY) |
| Reported outcome | Our results showed that the RT-1X policy has a 50% higher success rate than the original, state-of-the-art methods contributed by different collaborating institutions, while the bigger vision-language-modelbased version (RT-2-X) demonst ... | p. 6 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS) |
| Failure/limitation | In the largedataset setting, the RT-1-X model does not outperform the RT-1 baseline trained on only the embodiment-specific dataset, which indicates underfitting for that model class. | p. 5 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** 3: RT-1-X and RT-2-X both take images and a text instruction as input and output discretized end-effector actions. (p. 4, 5 Hz).
- **Paper-specific mechanism:** We show that the resulting models, which we call RT-X, can improve over policies trained only on data from the evaluation domain, exhibiting better generalization and new capabilities. (p. 2, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is Our results showed that the RT-1X policy has a 50% higher success rate than the original, state-of-the-art methods contributed by different collaborating institutions, while the bigger vision-language-modelbased version (RT-2-X) demonst ... (p. 6, V. EXPERIMENTAL RESULTS); the relevant task/metric cue is Our results showed that the RT-1X policy has a 50% higher success rate than the original, state-of-the-art methods contributed by different collaborating institutions, while the bigger vision-language-modelbased version (RT-2-X) demonst ... (p. 6, V. EXPERIMENTAL RESULTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** do not study generalization to new robots, and provide a decision criterion for when positive transfer does or does not happen. (p. 7, V. EXPERIMENTAL RESULTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `VLA and generalist robot policies`; tags: `Robotics, Dataset, Imitation Learning`.
- **Reading predecessor in the generated track queue:** VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Octo: An Open-Source Generalist Robot Policy (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In the largedataset setting, the RT-1-X model does not outperform the RT-1 baseline trained on only the embodiment-specific dataset, which indicates underfitting for that model class.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: 3: RT-1-X and RT-2-X both take images and a text instruction as input and output discretized end-effector actions. (p. 4, 5 Hz); preserve the objective/update rule: Training and inference details Both models use a standard categorical cross-entropy objective over their output space (discrete buckets for RT1 and all possible language tokens for RT-2). (p. 4, IV. RT-X DESIGN).
2. Use the paper-reported task/data/environment cue: Our experiments answer three questions about the effect of X-embodiment training: (1) Can policies trained on our X-embodiment dataset effectively enable positive transfer, such that co-training on data collected on ... (p. 5, V. EXPERIMENTAL RESULTS).
3. Compare against the reported or matched baseline: In the largedataset setting, the RT-1-X model does not outperform the RT-1 baseline trained on only the embodiment-specific dataset, which indicates underfitting for that model class. (p. 5, V. EXPERIMENTAL RESULTS).
4. Report the body metric with its denominator and aggregation: Our results showed that the RT-1X policy has a 50% higher success rate than the original, state-of-the-art methods contributed by different collaborating institutions, while the bigger vision-language-modelbased version (RT-2-X) demonst ... (p. 6, V. EXPERIMENTAL RESULTS).
5. Re-run the reported ablation or stress/failure condition: Our experiments answer three questions about the effect of X-embodiment training: (1) Can policies trained on our X-embodiment dataset effectively enable positive transfer, such that co-training on data collected on ... (p. 5, V. EXPERIMENTAL RESULTS); if none is reported, design one around: do not study generalization to new robots, and provide a decision criterion for when positive transfer does or does not happen. (p. 7, V. EXPERIMENTAL RESULTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), match the reported outcome at p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), and measure the boundary at p. 7 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS).

## Falsifiable research question

Under the paper's stated interface (3: RT-1-X and RT-2-X both take images and a text instruction as input and output discretized end-effector actions.), does the paper-specific mechanism (We show that the resulting models, which we call RT-X, can improve over policies trained only on data from the evaluation domain, ...) retain the reported evaluation outcome (Our results showed that the RT-1X policy has a 50% higher success rate than the original, state-of-the-art methods ...) when tested against the paper's strongest explicit boundary (do not study generalization to new robots, and provide a decision criterion for when positive transfer does or ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Our results showed that the RT-1X policy has a 50% higher success rate than the original, state-of-the-art methods ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** We show that the resulting models, which we call RT-X, can improve over policies trained only on data from the evaluation domain, exhibiting better generalization and new capabilities. (p. 2, I. INTRODUCTION).
- **Paper-supported outcome:** Our results showed that the RT-1X policy has a 50% higher success rate than the original, state-of-the-art methods contributed by different collaborating institutions, while the bigger vision-language-modelbased version (RT-2-X) demonst ... (p. 6, V. EXPERIMENTAL RESULTS).
- **Strongest explicit boundary:** do not study generalization to new robots, and provide a decision criterion for when positive transfer does or does not happen. (p. 7, V. EXPERIMENTAL RESULTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
