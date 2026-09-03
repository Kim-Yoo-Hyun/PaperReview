# Evaluation - Sparsh: Self-supervised touch representations for vision-based tactile sensing

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2410.24090; PDF retrieval source: https://arxiv.org/pdf/2410.24090. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 8 (8 Discussion), p. 1 (Figure/Table caption), p. 8 (8 Discussion), p. 26 (Figure/Table caption), p. 27 (Figure/Table caption)): Figure 4: Summary of results comparing Sparsh and E2E on [T1]-[T6] tasks in TacBench across varying amounts of labeled data. Pre-training with SSL yields general touch representations that work across ...

## Evaluation Body Digest

- **p. 2 / 1 Introduction - extractive body cue:** Finally, we construct TacBench, a benchmark consisting of six touch-centric tasks that cover the space of relevant problems on tactile properties such as force estimation ...
- **p. 2 / 1 Introduction - extractive body cue:** Curation of new & existing datasets, unlabeled for SSL and labeled for benchmarking.
- **p. 1 / Abstract - extractive body cue:** Such sensors have led to many recent advances in robot manipulation as they markedly complement vision, yet solutions today often rely on task and sensor ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** We find Sparsh pre-trained with self-supervision on a dataset of 460k+ tactile images can generalize across many tasks (right) and sensors (left) outperforming task and ...
- **p. 8 / 8 Discussion - extractive body cue:** Further research is needed to understand how to effectively leverage pre-trained touch representations in behavioral cloning for robot manipulation tasks.
- **p. 8 / 8 Discussion - extractive body cue:** On average, Sparsh achieves a 95.1% improvement compared to an end-to-end approach when all models have access to only 33% -50% of the labeled dataset ...
- **p. 28 / Figure/Table caption - extractive body cue:** Table 11: Mean and variance of distance traversed (in cm) before failure for policies based on Sparsh and E2E. Results over 10 randomized novel starting ...
- **p. 24 / Figure/Table caption - extractive body cue:** Figure 12: Contrast between Sparsh (VJEPA) and E2E for a test trajectory with a spherical probe sliding on the DIGIT sensor. Sparsh (VJEPA), even though ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** contact-rich manipulation scene.
- **Input boundary:** tactile image/force, vision과 proprioceptive history.
- **Output/decision under evaluation:** grasp/contact action, force command 또는 object motion.
- **Primary target:** slip/contact success, force/pose error와 robustness.
- **Detected evaluation headings:** C.3 Dataset splits (p. 18).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 4: Summary of results comparing Sparsh and E2E on [T1]-[T6] tasks in TacBench across varying amounts of labeled data. Pre-training with SSL yields ... | p. 7 (Figure/Table caption) |
| 8 Discussion | SYSTEM / EVALUATION SCOPE UNRESOLVED | On average, Sparsh achieves a 95.1% improvement compared to an end-to-end approach when all models have access to only 33% -50% of the labeled ... | p. 8 (8 Discussion) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 1: We present Sparsh, a family of general touch representations, and TacBench, a standardized benchmark of six touch-centric tasks ([T1]-[T6]) covering prominent problems ... | p. 1 (Figure/Table caption) |
| 8 Discussion | SYSTEM / EVALUATION SCOPE UNRESOLVED | In contrast, partial fine-tuning offers minor improvements, aligning closely with the performance of frozen models. | p. 8 (8 Discussion) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 14: Confusion matrix on test data for ∆Tx, ∆Ty, ∆Yaw for E2E, Sparsh (DINO) and Sparsh (IJEPA) trained on 33% of the available ... | p. 26 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 2 / 1 Introduction - extractive body cue:** Finally, we construct TacBench, a benchmark consisting of six touch-centric tasks that cover the space of relevant problems on tactile properties such as force estimation ...
- **p. 2 / 1 Introduction - extractive body cue:** Curation of new & existing datasets, unlabeled for SSL and labeled for benchmarking.
- **p. 1 / Abstract - extractive body cue:** Such sensors have led to many recent advances in robot manipulation as they markedly complement vision, yet solutions today often rely on task and sensor ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** We find Sparsh pre-trained with self-supervision on a dataset of 460k+ tactile images can generalize across many tasks (right) and sensors (left) outperforming task and ...
- **p. 8 / 8 Discussion - extractive body cue:** Further research is needed to understand how to effectively leverage pre-trained touch representations in behavioral cloning for robot manipulation tasks.
- **p. 8 / 8 Discussion - extractive body cue:** On average, Sparsh achieves a 95.1% improvement compared to an end-to-end approach when all models have access to only 33% -50% of the labeled dataset ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: We present Sparsh, a family of general touch representations, and TacBench, a standardized benchmark of six touch-centric tasks ([T1]-[T6]) covering prominent problems in ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: (a) We curate new and existing datasets of vision-based tactile sensors to train touch representations by adapting state-of-the-art SSL vision methods to the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Real labeled data collection setup for TacBench tasks (a) [T1] Force estimation and [T2] Slip detection, (b) [T3] Pose estimation, and (c) [T6] ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Summary of results comparing Sparsh and E2E on [T1]-[T6] tasks in TacBench across varying amounts of labeled data. Pre-training with SSL yields general ...
- **p. 17 / Figure/Table caption - extractive body cue:** Table 1: Training hyperparameters for Sparsh models. All models run for 150 epochs with optimizer AdamW, a weight decay cosine schedule from 0.04 to 0.4, ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 5: Visualization of reconstructed tactile images using the online probe to monitor SSL training of Sparsh models. Sparsh (MAE) Sparsh (DINO) Sparsh (IJEPA) Sparsh ...
- **p. 18 / Figure/Table caption - extractive body cue:** Table 2: Number of parameters and inference time for Sparsh backbones All the models are pretrained without a [cls] token. For DINO, which decodes the ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 6: Set of objects for collecting sliding contact trajectories in the Touch-Slide dataset. Similarly, all objects used for downstream tasks were not used for ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Finally, we construct TacBench, a benchmark consisting of six touch-centric tasks that cover the space of relevant problems on tactile properties such as force ... | embodiment, simulator version and control stack | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Task/environment | Curation of new & existing datasets, unlabeled for SSL and labeled for benchmarking. | reset, timeout, object/scene variation | p. 2 (1 Introduction), p. 1 (Abstract) |
| Observation/sensor | tactile image/force, vision과 proprioceptive history | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 8 (8 Discussion) |
| Output/decision | grasp/contact action, force command 또는 object motion | action frame, controller and termination | p. 2 (1 Introduction), p. 8 (8 Discussion) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 11: Mean and variance of distance traversed (in cm) before failure for policies based on Sparsh and E2E. Results over 10 randomized novel ... | definition/direction/unit from same section | p. 28 (Figure/Table caption) |
| Figure 12: Contrast between Sparsh (VJEPA) and E2E for a test trajectory with a spherical probe sliding on the DIGIT sensor. Sparsh (VJEPA), even ... | definition/direction/unit from same section | p. 24 (Figure/Table caption) |
| Table 7: Performance of models on slip detection task under different budgets of training data. We use F1 score as metric, given that it ... | definition/direction/unit from same section | p. 24 (Figure/Table caption) |
| Figure 14: Confusion matrix on test data for ∆Tx, ∆Ty, ∆Yaw for E2E, Sparsh (DINO) and Sparsh (IJEPA) trained on 33% of the available ... | definition/direction/unit from same section | p. 26 (Figure/Table caption) |
| Table 8: Accuracy and 95% confidence interval for pose estimation task following the regression-by- classification paradigm. Relative pose between object and ring finger. Metrics ... | definition/direction/unit from same section | p. 25 (Figure/Table caption) |
| Table 9: Accuracy and 95% confidence interval for grasp stability classification over different budget sizes of training data, using Feeling of Success dataset. Results ... | definition/direction/unit from same section | p. 27 (Figure/Table caption) |
| Table 10: Accuracy for textile classification over 20 classes using GelSight with markers dataset under different budget of labeled data. Results over 26k tactile ... | definition/direction/unit from same section | p. 28 (Figure/Table caption) |
| These include the high precision required to keep the bead in place, the impossibility of error recovery once grip is lost, and trajectory drift ... | definition/direction/unit from same section | p. 8 (8 Discussion) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 2: (a) We curate new and existing datasets of vision-based tactile sensors to train touch representations by adapting state-of-the-art SSL vision methods to ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| We find Sparsh pre-trained with self-supervision on a dataset of 460k+ tactile images can generalize across many tasks (right) and sensors (left) outperforming task ... | comparison identity and matched condition | p. 1 (Body text (section boundary not confidently recovered)) |
| In evaluations, we find that SSL pre-training for touch representation outperforms task and sensor-specific end-to-end training by 95.1% on average over TacBench, and Sparsh ... | comparison identity and matched condition | p. 1 (Abstract) |
| Figure 4: Summary of results comparing Sparsh and E2E on [T1]-[T6] tasks in TacBench across varying amounts of labeled data. Pre-training with SSL yields ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| On average Sparsh (DINO) outperforms Sparsh (IJEPA) by 5.6% across the benchmark. | comparison identity and matched condition | p. 8 (8 Discussion) |
| On average, Sparsh achieves a 95.1% improvement compared to an end-to-end approach when all models have access to only 33% -50% of the labeled ... | comparison identity and matched condition | p. 8 (8 Discussion) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 2: Number of parameters and inference time for Sparsh backbones All the models are pretrained without a [cls] token. For DINO, which decodes ... | component/input/data sensitivity | p. 18 (Figure/Table caption) |
| Table 7: Performance of models on slip detection task under different budgets of training data. We use F1 score as metric, given that it ... | component/input/data sensitivity | p. 24 (Figure/Table caption) |
| Figure 17: Additional evaluations of Sparsh representations on TacBench. We compare frozen Sparsh ViT-base (most left), Sparsh fully and partially fine-tuned (middle) and finally ... | component/input/data sensitivity | p. 31 (Figure/Table caption) |
| Table 13: Performance of Sparsh across TacBench and comparison between SSL approaches. E Sparsh ablations E.1 TacBench evaluations via fine-tuning Fine-tuning the Sparsh encoders ... | component/input/data sensitivity | p. 29 (Figure/Table caption) |
| However, this can be inefficient and results in repeated effort across different type of sensors like GelSight 2017 [1] (with markers) and DIGIT [3] ... | component/input/data sensitivity | p. 2 (1 Introduction) |
| Figure 2: (a) We curate new and existing datasets of vision-based tactile sensors to train touch representations by adapting state-of-the-art SSL vision methods to ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, we introduce a family of touch representations for vision-based tactile sensors trained with SSL. | Figure 4: Summary of results comparing Sparsh and E2E on [T1]-[T6] tasks in TacBench across varying amounts of labeled data. Pre-training with SSL yields ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 8 (8 Discussion), p. 1 (Figure/Table caption), p. 8 (8 Discussion), p. 26 (Figure/Table caption), p. 27 (Figure/Table caption) |
| Primary metric/result | On average, Sparsh achieves a 95.1% improvement compared to an end-to-end approach when all models have access to only 33% -50% of the labeled ... | numeric claim only at cited anchor | p. 8 (8 Discussion) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 13: Failure case where the ground truth does not reflect slip since it relies on an experimental coefficient of friction. Despite the inaccuracies ... | p. 25 (Figure/Table caption) |
| body limitation/failure cue | Figure 12: Contrast between Sparsh (VJEPA) and E2E for a test trajectory with a spherical probe sliding on the DIGIT sensor. Sparsh (VJEPA), even ... | p. 24 (Figure/Table caption) |
| body limitation/failure cue | Table 11: Mean and variance of distance traversed (in cm) before failure for policies based on Sparsh and E2E. Results over 10 randomized novel ... | p. 28 (Figure/Table caption) |
| body limitation/failure cue | Both models perform similarly in bead maze test demonstrations, which require implicit knowledge of shear forces and slip. | p. 8 (8 Discussion) |
| body limitation/failure cue | Using as little as 10% or 1% of the labeled data for force estimation and slip detection still yields acceptable results (e.g. force error ... | p. 8 (8 Discussion) |
| body limitation/failure cue | Table 8: Accuracy and 95% confidence interval for pose estimation task following the regression-by- classification paradigm. Relative pose between object and ring finger. Metrics ... | p. 25 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Specifically, we provide a recipe to adapt masking-based objectives from computer vision to the tactile domain, and train general-purpose touch encoders by curating a ... | p. 2 (1 Introduction) |
| Performance in the plot (middle) is with task decoders using 33% labeled data (except [T6] that uses 50%). | p. 1 (Body text (section boundary not confidently recovered)) |
| To tackle this we turn to self-supervised learning (SSL) that has demonstrated remarkable performance in computer vision. | p. 1 (Abstract) |
| Taking inspiration from self-supervised learning (SSL) methods in computer vision, we extend these approaches to the tactile sensing domain and build a benchmark for ... | p. 2 (1 Introduction) |
| Fine-tuning Sparsh encoders is another method of assessing the quality of pre-trained representations. | p. 8 (8 Discussion) |
| Our aim is to enable efforts to compile larger tactile datasets that include additional vision-based tactile sensors and leverage the benefits of scaling up ... | p. 8 (8 Discussion) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 25 / Figure/Table caption - extractive body cue:** Figure 13: Failure case where the ground truth does not reflect slip since it relies on an experimental coefficient of friction. Despite the inaccuracies in ...
- **p. 24 / Figure/Table caption - extractive body cue:** Figure 12: Contrast between Sparsh (VJEPA) and E2E for a test trajectory with a spherical probe sliding on the DIGIT sensor. Sparsh (VJEPA), even though ...
- **p. 28 / Figure/Table caption - extractive body cue:** Table 11: Mean and variance of distance traversed (in cm) before failure for policies based on Sparsh and E2E. Results over 10 randomized novel starting ...
- **p. 8 / 8 Discussion - extractive body cue:** Both models perform similarly in bead maze test demonstrations, which require implicit knowledge of shear forces and slip.
- **p. 8 / 8 Discussion - extractive body cue:** Using as little as 10% or 1% of the labeled data for force estimation and slip detection still yields acceptable results (e.g. force error below ...
- **p. 25 / Figure/Table caption - extractive body cue:** Table 8: Accuracy and 95% confidence interval for pose estimation task following the regression-by- classification paradigm. Relative pose between object and ring finger. Metrics computed ...

- **Evidence anchors reviewed:** datasets p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Body text (section boundary not confidently recovered)), p. 8 (8 Discussion), p. 8 (8 Discussion), metrics p. 28 (Figure/Table caption), p. 24 (Figure/Table caption), p. 24 (Figure/Table caption), p. 26 (Figure/Table caption), p. 25 (Figure/Table caption), p. 27 (Figure/Table caption), baselines p. 3 (Figure/Table caption), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Abstract), p. 7 (Figure/Table caption), p. 8 (8 Discussion), p. 8 (8 Discussion), results p. 7 (Figure/Table caption), p. 8 (8 Discussion), p. 1 (Figure/Table caption), p. 8 (8 Discussion), p. 26 (Figure/Table caption), p. 27 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (31 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 4: Summary of results comparing Sparsh and E2E on [T1]-[T6] tasks in TacBench across varying amounts of labeled data. Pre-training with SSL yields general touch representations that work across ... (p. 7, Figure/Table caption).
- **Metric evidence:** Figure 12: Contrast between Sparsh (VJEPA) and E2E for a test trajectory with a spherical probe sliding on the DIGIT sensor. Sparsh (VJEPA), even though trained only on 33% of ... (p. 24, Figure/Table caption).
- **Baseline/ablation evidence:** Table 13: Performance of Sparsh across TacBench and comparison between SSL approaches. E Sparsh ablations E.1 TacBench evaluations via fine-tuning Fine-tuning the Sparsh encoders is another method of assessing the ... (p. 29, Figure/Table caption).
- **Failure/negative evidence:** In Figure 13, we illustrate a failure case for Sparsh (VJEPA), as its results do not align with the ground truth. (p. 24, Model).
