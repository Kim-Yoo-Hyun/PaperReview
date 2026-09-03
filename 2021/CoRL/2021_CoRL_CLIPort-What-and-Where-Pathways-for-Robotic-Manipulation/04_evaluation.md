# Evaluation - CLIPort: What and Where Pathways for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2109.12098; PDF retrieval source: https://arxiv.org/pdf/2109.12098. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 22 (Figure/Table caption), p. 7 (4 Results), p. 8 (4 Results), p. 8 (4 Results), p. 6 (4 Results)): Table 1. Language-Conditioned Test Results. Task success scores (mean %) from 100 evaluation instances vs. # of training demonstrations (1, 10, 100, or 1000). The challenges pertaining to each task ...

## Evaluation Body Digest

- **p. 6 / 4 Results - extractive body cue:** For packing objects, we use 56 tabletop objects from the Google Scanned Objects dataset [61] and split them into 37 seen and 19 unseen objects.
- **p. 8 / 4 Results - extractive body cue:** In summary, unbiased datasets containing both a good coverage of expected skills and invariances, and a decent number of training demonstrations, are crucial for good ...
- **p. 6 / 4 Results - extractive body cue:** The setup provides a systematic and reproducible environment for evaluation, especially for benchmarking the ability to ground semantic concepts like colors and object categories.
- **p. 8 / 4 Results - extractive body cue:** 4.3 Real-Robot Experiments Task # Train (Samples) # Test Succ. % Stack Blocks 5 (13) 10 70.0 Put Blocks in Bowl 5 (10) 10 65.0 ...
- **p. 7 / 4 Results - extractive body cue:** In realistic scenarios, we want the robot to be capable of any task, not just one task.
- **p. 7 / 4 Results - extractive body cue:** We hypothesize that this is because longer-horizon tasks get less coverage of input-action pairs in the dataset.
- **p. 8 / 4 Results - extractive body cue:** Success rates (%) of a multi-task model trained an evaluated 9 real-world tasks (see Figure 1).
- **p. 6 / 4 Results - extractive body cue:** We adopt the 0 (fail) to 100 (success) scores proposed in the Ravens benchmark [2].

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 Results (p. 6); B Evaluation Workflow and Validation Results (p. 18).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1. Language-Conditioned Test Results. Task success scores (mean %) from 100 evaluation instances vs. # of training demonstrations (1, 10, 100, or 1000). ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 6. Demo-Conditioned Tasks. Validation task success scores (mean %) from 100 evaluation instances vs. # of demonstration episodes (1, 10, 100, or 1000) ... | p. 22 (Figure/Table caption) |
| 4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Tasks that require generalizing to novel colors, shapes, and objects are more difficult and all our agents achieve relatively lower performance on these tasks, ... | p. 7 (4 Results) |
| 4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results indicate that such explicit transfers result in significant improvements. | p. 8 (4 Results) |
| 4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Success rates (%) of a multi-task model trained an evaluated 9 real-world tasks (see Figure 1). | p. 8 (4 Results) |

## Dataset / Benchmark Role

- **p. 6 / 4 Results - extractive body cue:** For packing objects, we use 56 tabletop objects from the Google Scanned Objects dataset [61] and split them into 37 seen and 19 unseen objects.
- **p. 8 / 4 Results - extractive body cue:** In summary, unbiased datasets containing both a good coverage of expected skills and invariances, and a decent number of training demonstrations, are crucial for good ...
- **p. 6 / 4 Results - extractive body cue:** The setup provides a systematic and reproducible environment for evaluation, especially for benchmarking the ability to ground semantic concepts like colors and object categories.
- **p. 8 / 4 Results - extractive body cue:** 4.3 Real-Robot Experiments Task # Train (Samples) # Test Succ. % Stack Blocks 5 (13) 10 70.0 Put Blocks in Bowl 5 (10) 10 65.0 ...
- **p. 7 / 4 Results - extractive body cue:** In realistic scenarios, we want the robot to be capable of any task, not just one task.
- **p. 7 / 4 Results - extractive body cue:** We hypothesize that this is because longer-horizon tasks get less coverage of input-action pairs in the dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. Language-Conditioned Manipulation Tasks: CLIPORT is a broad framework applicable to a wide range of language-conditioned manipulation tasks in tabletop settings. We conduct large-scale ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. CLIPORT Two-Stream Architecture. An overview of the semantic and spatial streams. The semantic stream uses a frozen CLIP ResNet50 [1] to encode RGB ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Average scores across seen and unseen splits for all tasks in Table 1. Table 1 presents results from our large-scale experiments in Ravens ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Language-Conditioned Test Results. Task success scores (mean %) from 100 evaluation instances vs. # of training demonstrations (1, 10, 100, or 1000). The ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Affordance predictions from CLIPORT (multi) models in sim (left two) and real settings (right three). More examples in Appendix H. Transferring Attributes across ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. Success rates (%) of a multi-task model trained an evaluated 9 real-world tasks (see Figure 1). Samples indicate total image-action pairs, e.g 1 ...
- **p. 14 / Figure/Table caption - extractive body cue:** Table 3. Language-conditioned tasks in Ravens [2] with their associated challenges. We extend the Ravens benchmark [2] to 10 language-conditioned. 8 out of 10 tasks ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 5. Success Metric: The correct shape is inside the bounds of the brown box. A.3 Assembling Kits Seq Example: Figure 1(c). 14

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For packing objects, we use 56 tabletop objects from the Google Scanned Objects dataset [61] and split them into 37 seen and 19 unseen ... | embodiment, simulator version and control stack | p. 6 (4 Results), p. 8 (4 Results) |
| Task/environment | In summary, unbiased datasets containing both a good coverage of expected skills and invariances, and a decent number of training demonstrations, are crucial for ... | reset, timeout, object/scene variation | p. 8 (4 Results), p. 6 (4 Results) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (Abstract), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Success rates (%) of a multi-task model trained an evaluated 9 real-world tasks (see Figure 1). | definition/direction/unit from same section | p. 8 (4 Results) |
| We adopt the 0 (fail) to 100 (success) scores proposed in the Ravens benchmark [2]. | definition/direction/unit from same section | p. 6 (4 Results) |
| Task success scores (mean %) from 100 evaluation instances vs. # of training demonstrations (1, 10, 100, or 1000). | definition/direction/unit from same section | p. 7 (4 Results) |
| The score assigns partial credit based on the task, e.g. | definition/direction/unit from same section | p. 6 (4 Results) |
| See Figure 3 for an overview with average scores. learning (i.e. n ≥10) in lieu of semantic stream alternatives like ImageNet-trained ResNet50 [62] with ... | definition/direction/unit from same section | p. 7 (4 Results) |
| In summary, unbiased datasets containing both a good coverage of expected skills and invariances, and a decent number of training demonstrations, are crucial for ... | definition/direction/unit from same section | p. 8 (4 Results) |
| Figure 6. Average validation scores across seen and unseen splits for all tasks in Table 4. 18 | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| Table 5. Ablations and Baselines. Evaluation scores (mean %) for stack-block-pyramid-seq and packing-google-objects-seq tasks from 100 evaluation runs. Stacking block pyramids involves both semantic ... | definition/direction/unit from same section | p. 21 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We perform experiments both in simulation and hardware aimed at answering the following questions: 1) How effective is the language-conditioned two-stream architecture for fine-grained ... | comparison identity and matched condition | p. 6 (4 Results) |
| In addition to these baselines, we present various ablations and alternative one-stream and twostream models in Appendix F. | comparison identity and matched condition | p. 6 (4 Results) |
| Table 5. Ablations and Baselines. Evaluation scores (mean %) for stack-block-pyramid-seq and packing-google-objects-seq tasks from 100 evaluation runs. Stacking block pyramids involves both semantic ... | comparison identity and matched condition | p. 21 (Figure/Table caption) |
| Additionally, we notice that CLIPORT (single) is also less prone to overfitting compared to Transporter-only. | comparison identity and matched condition | p. 7 (4 Results) |
| Surprisingly, CLIPORT (multi) outperforms single-task CLIPORT (single) models in 41/72 = 57% of the evaluations in Table 1. | comparison identity and matched condition | p. 7 (4 Results) |
| Figure 9. Data Augmentation: SE(2) transform applied to RGB-D input. The left image shows the original input, and the right image shows the transformed ... | comparison identity and matched condition | p. 21 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 5. Ablations and Baselines. Evaluation scores (mean %) for stack-block-pyramid-seq and packing-google-objects-seq tasks from 100 evaluation runs. Stacking block pyramids involves both semantic ... | component/input/data sensitivity | p. 21 (Figure/Table caption) |
| CLIP-only shows what can be achieved by fine-tuning a pre-trained semantic model for manipulation without spatial information, particularly depth. | component/input/data sensitivity | p. 6 (4 Results) |
| In addition to these baselines, we present various ablations and alternative one-stream and twostream models in Appendix F. | component/input/data sensitivity | p. 6 (4 Results) |
| This supports our premise that language is a strong conditioning mechanism for reusing concepts from other tasks without learning them from scratch. | component/input/data sensitivity | p. 7 (4 Results) |
| As evidenced in towers-of-hanoi-seq-unseen-colors task in Table 1, Transporter-only suffers from a performance drop because of rings with unseen colors despite the fact that ... | component/input/data sensitivity | p. 7 (4 Results) |
| Table 3. Language-conditioned tasks in Ravens [2] with their associated challenges. We extend the Ravens benchmark [2] to 10 language-conditioned. 8 out of 10 ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We propose 10 language-conditioned tasks with 1000s of unique instances per task that require both semantic and spatial reasoning (see Figure 1 a-j). | Table 1. Language-Conditioned Test Results. Task success scores (mean %) from 100 evaluation instances vs. # of training demonstrations (1, 10, 100, or 1000). ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 22 (Figure/Table caption), p. 7 (4 Results), p. 8 (4 Results), p. 8 (4 Results), p. 6 (4 Results) |
| Primary metric/result | Table 6. Demo-Conditioned Tasks. Validation task success scores (mean %) from 100 evaluation instances vs. # of demonstration episodes (1, 10, 100, or 1000) ... | numeric claim only at cited anchor | p. 22 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 4 Results - extractive body cue:** 8 of the 10 tasks have two variants, denoted by seen and unseen, depending on whether the task has unseen attributes (e.g. color) at test ...
- **p. 6 / 4 Results - extractive body cue:** 3/5 ⇒60.0 for packing 3 out of 5 objects specified in the instructions, or 30/56 ⇒53.6 for pushing 30 out of 56 particles into the ...
- **p. 6 / 4 Results - extractive body cue:** We report scores on 100 evaluation runs for agents trained with n = 1, 10, 100, 1000 demonstrations.
- **p. 7 / 4 Results - extractive body cue:** CLIPORT (multi) models are trained on seen splits of all 10 tasks with 1T, 10T, 100T, and 1000T demonstrations where T = 10.
- **p. 7 / 4 Results - extractive body cue:** We investigate this through CLIPORT (multi) in Table 1 with one multi-task model trained on all 10 tasks.
- **p. 8 / 4 Results - extractive body cue:** For instance, on the put-blocks-inbowls-unseen-colors task for n = 1000, CLIPORT (multi)'s performance increases from 45.8 to 75.7.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | As such, it cannot handle complex partially-observable scenes, or output continuous control for multi-fingered hands, or predict task-completion (see Appendix I for an extended ... | p. 8 (5 Conclusion) |
| body limitation/failure cue | Although Transporter-only does not receive any language goals, it shows what can be achieved through chance by exploiting the most likely actions seen during ... | p. 6 (4 Results) |
| body limitation/failure cue | Future works could use better sampling methods that balance tasks according to their average time horizon. | p. 7 (4 Results) |
| body limitation/failure cue | Each camera has a resolution of 640 × 480 and is noiseless. | p. 6 (4 Results) |
| body limitation/failure cue | It also validates a trait of data-driven approaches where training on lots of diverse data leads to more robust and generalizable representations [1, 63]. | p. 7 (4 Results) |
| body limitation/failure cue | We estimate that for more robust real-world performance at least 50 to 100 training demonstrations are necessary, as evident in Figure 3. | p. 8 (4 Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Transporter has been applied to a wide range of rearragement tasks from industrial packing [2] to manipulating deformable objects [6]. | p. 2 (1 Introduction) |
| The benchmark, code, and pre-trained models are available at: cliport.github.io. | p. 3 (1 Introduction) |
| We perform experiments both in simulation and hardware aimed at answering the following questions: 1) How effective is the language-conditioned two-stream architecture for fine-grained ... | p. 6 (4 Results) |
| Although pre-trained CLIP has been exposed to the attribute ‘pink', it could correspond to different concepts in the physical setting depending on factors like ... | p. 7 (4 Results) |
| We validated our results in hardware with a Franka Panda manipulator. | p. 8 (4 Results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5 Conclusion - extractive body cue:** As such, it cannot handle complex partially-observable scenes, or output continuous control for multi-fingered hands, or predict task-completion (see Appendix I for an extended discussion).
- **p. 6 / 4 Results - extractive body cue:** Although Transporter-only does not receive any language goals, it shows what can be achieved through chance by exploiting the most likely actions seen during training.
- **p. 7 / 4 Results - extractive body cue:** Future works could use better sampling methods that balance tasks according to their average time horizon.
- **p. 6 / 4 Results - extractive body cue:** Each camera has a resolution of 640 × 480 and is noiseless.
- **p. 7 / 4 Results - extractive body cue:** It also validates a trait of data-driven approaches where training on lots of diverse data leads to more robust and generalizable representations [1, 63].
- **p. 8 / 4 Results - extractive body cue:** We estimate that for more robust real-world performance at least 50 to 100 training demonstrations are necessary, as evident in Figure 3.

- **Evidence anchors reviewed:** datasets p. 6 (4 Results), p. 8 (4 Results), p. 6 (4 Results), p. 8 (4 Results), p. 7 (4 Results), p. 7 (4 Results), metrics p. 8 (4 Results), p. 6 (4 Results), p. 7 (4 Results), p. 6 (4 Results), p. 7 (4 Results), p. 8 (4 Results), baselines p. 6 (4 Results), p. 6 (4 Results), p. 21 (Figure/Table caption), p. 7 (4 Results), p. 7 (4 Results), p. 21 (Figure/Table caption), results p. 7 (Figure/Table caption), p. 22 (Figure/Table caption), p. 7 (4 Results), p. 8 (4 Results), p. 8 (4 Results), p. 6 (4 Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (24 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Table 1. Language-Conditioned Test Results. Task success scores (mean %) from 100 evaluation instances vs. # of training demonstrations (1, 10, 100, or 1000). The challenges pertaining to each task ... (p. 7, Figure/Table caption).
- **Metric evidence:** Task success scores (mean %) from 100 evaluation instances vs. # of training demonstrations (1, 10, 100, or 1000). (p. 7, 4 Results).
- **Baseline/ablation evidence:** In addition to these baselines, we present various ablations and alternative one-stream and twostream models in Appendix F. (p. 6, 4 Results).
- **Failure/negative evidence:** While language-grounding for manipulation has been explored in the past [7, 8, 9, 10], these pipelines are limited by object-centric representations that cannot handle granular or deformable objects and often ... (p. 1, 1 Introduction).
