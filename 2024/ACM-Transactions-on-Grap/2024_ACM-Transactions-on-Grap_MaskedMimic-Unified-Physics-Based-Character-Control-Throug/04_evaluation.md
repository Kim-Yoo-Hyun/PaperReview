# Evaluation - MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://research.nvidia.com/labs/par/maskedmimic/; PDF retrieval source: https://research.nvidia.com/labs/par/maskedmimic/. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 15 (8 RESULTS), p. 11 (8 RESULTS), p. 9 (7.2 Evaluation), p. 10 (7.2 Evaluation), p. 11 (8 RESULTS), p. 12 (8 RESULTS)): While MaskedMimic demonstrates high success rates in generating diverse motions, there are three notable areas for improvement in terms of motion quality.

## Evaluation Body Digest

- **p. 9 / 7.2 Evaluation - extractive body cue:** To evaluate the effectiveness of our framework, we construct a benchmark consisting of common tasks introduced by prior systems.
- **p. 10 / 7.2 Evaluation - extractive body cue:** In this task, we focus on sitting on a set of held-out objects.
- **p. 11 / 8 RESULTS - extractive body cue:** Additionally, MaskedMimic is designed to tackle a wide range of tasks across diverse scenes, which likely contributes to the model's enhanced generalization capabilities.
- **p. 12 / 8 RESULTS - extractive body cue:** For each task, we report the average performance statistics recorded across 5000 random episodes.
- **p. 12 / 8 RESULTS - extractive body cue:** MaskedMimic, irregular terrain: We evaluate our models from both training stages on the task of tracking motions from the AMASS dataset across irregular terrains.
- **p. 14 / 8 RESULTS - extractive body cue:** The object interaction motions in the SAMP dataset [Hassan et al.
- **p. 10 / 7.2 Evaluation - extractive body cue:** Performing new tasks often requires generalization to new and unseen scenarios.
- **p. 11 / 8 RESULTS - extractive body cue:** This multi-task, multienvironment training approach appears to foster a more robust and adaptable model, enabling it to perform well on unseen data and scenarios.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** 7.2 Evaluation (p. 9); 8 RESULTS (p. 10).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 8 RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | While MaskedMimic demonstrates high success rates in generating diverse motions, there are three notable areas for improvement in terms of motion quality. | p. 15 (8 RESULTS) |
| 8 RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | We attribute these performance improvements to our architecture and data augmentation techniques. | p. 11 (8 RESULTS) |
| 7.2 Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | For each tasks, we report a success rate metric and an error rate metric. | p. 9 (7.2 Evaluation) |
| 7.2 Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | This test establishes the baseline capability for motion generation, both in terms of success rates and tracking quality, and allows comparison to prior systems ... | p. 10 (7.2 Evaluation) |
| 8 RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | We report metrics on the 3 available sensors, measuring success rate for tracking the head and hands, in addition to the MPJPE measured on ... | p. 11 (8 RESULTS) |

## Dataset / Benchmark Role

- **p. 9 / 7.2 Evaluation - extractive body cue:** To evaluate the effectiveness of our framework, we construct a benchmark consisting of common tasks introduced by prior systems.
- **p. 10 / 7.2 Evaluation - extractive body cue:** In this task, we focus on sitting on a set of held-out objects.
- **p. 11 / 8 RESULTS - extractive body cue:** Additionally, MaskedMimic is designed to tackle a wide range of tasks across diverse scenes, which likely contributes to the model's enhanced generalization capabilities.
- **p. 12 / 8 RESULTS - extractive body cue:** For each task, we report the average performance statistics recorded across 5000 random episodes.
- **p. 12 / 8 RESULTS - extractive body cue:** MaskedMimic, irregular terrain: We evaluate our models from both training stages on the task of tracking motions from the AMASS dataset across irregular terrains.
- **p. 14 / 8 RESULTS - extractive body cue:** The object interaction motions in the SAMP dataset [Hassan et al.
- **p. 10 / 7.2 Evaluation - extractive body cue:** Performing new tasks often requires generalization to new and unseen scenarios.
- **p. 11 / 8 RESULTS - extractive body cue:** This multi-task, multienvironment training approach appears to foster a more robust and adaptable model, enabling it to perform well on unseen data and scenarios.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. We present MaskedMimic, a versatile control model that enables physically simulated characters to generate diverse behaviors from flexible user- specified constraints. MaskedMimic can ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. Partial motion plans. MaskedMimic synthesizes full-body physics-based character animations. It achieves this by inpainting conditioned on multi-modal partial objectives. (a) The character climbs ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3. The MaskedMimic framework: The first phase produces a fully- constrained controller 𝜋FC. This full-body tracker is trained using reinforce- ment learning to imitate ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. Training scene (screenshot): The top region consists of standard flat terrain, enabling the controller to reproduce the original motions in a setting that ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Given partial constraints, such as target positions for joints, text commands, or object locations, MaskedMimic generates diverse full-body motions that satisfy those constraints. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 5. MaskedMimic VAE Architecture. We observe that randomly re-sampling the mask on each step reduces the ambiguity the model encounters during training. There- fore, ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 6. Motion tracking: MaskedMimic generates full-body motion when tracking signals extracted from unseen kinematic motions. Precise fighting and dancing moves when tracking full-body information, ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 1. Full-body tracking, flat terrain: Tracking full-body kinematic recordings from the AMASS dataset [Mahmood et al. 2019]. We highlight be best performing model on ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To evaluate the effectiveness of our framework, we construct a benchmark consisting of common tasks introduced by prior systems. | embodiment, simulator version and control stack | p. 9 (7.2 Evaluation), p. 10 (7.2 Evaluation) |
| Task/environment | In this task, we focus on sitting on a set of held-out objects. | reset, timeout, object/scene variation | p. 10 (7.2 Evaluation), p. 11 (8 RESULTS) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 4 (3 PRELIMINARIES), p. 5 (3. Inference) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 4 (3 PRELIMINARIES), p. 5 (3. Inference) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We evaluate versions of the model with key components removed (Section 6), and measure the impact on the average success rate and error (i.e. ... | definition/direction/unit from same section | p. 14 (8 RESULTS) |
| For each tasks, we report a success rate metric and an error rate metric. | definition/direction/unit from same section | p. 9 (7.2 Evaluation) |
| We report metrics on the 3 available sensors, measuring success rate for tracking the head and hands, in addition to the MPJPE measured on ... | definition/direction/unit from same section | p. 11 (8 RESULTS) |
| As shown in Table 4, MaskedMimic exhibits similar success rates and tracking errors across both the train and test sets, when evaluated on randomly ... | definition/direction/unit from same section | p. 12 (8 RESULTS) |
| By providing the model with more flexibility in the goal inputs and not tightly constraining the near-term goals, the success rate increases and tracking ... | definition/direction/unit from same section | p. 13 (8 RESULTS) |
| This test establishes the baseline capability for motion generation, both in terms of success rates and tracking quality, and allows comparison to prior systems ... | definition/direction/unit from same section | p. 10 (7.2 Evaluation) |
| We observed a tradeoff between user control and success rate. | definition/direction/unit from same section | p. 13 (8 RESULTS) |
| While MaskedMimic demonstrates high success rates in generating diverse motions, there are three notable areas for improvement in terms of motion quality. | definition/direction/unit from same section | p. 15 (8 RESULTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| This test establishes the baseline capability for motion generation, both in terms of success rates and tracking quality, and allows comparison to prior systems ... | comparison identity and matched condition | p. 10 (7.2 Evaluation) |
| [2024], consisting of 3 baselines: PULSE [Luo et al. | comparison identity and matched condition | p. 10 (7.2 Evaluation) |
| Our fully-constrained tracker FC outperforms PHC+ [Luo et al. | comparison identity and matched condition | p. 11 (8 RESULTS) |
| Specifically, foot tracking presents a greater challenge compared to hand tracking. | comparison identity and matched condition | p. 12 (8 RESULTS) |
| Despite not being explicitly trained on this task, MaskedMimic outperforms other models by a significant margin when evaluated on tracking target trajectories extracted from ... | comparison identity and matched condition | p. 12 (8 RESULTS) |
| The superior performance of our model suggests that, in the context of full-body tracking, a welldesigned unified network can effectively capture the diversity of ... | comparison identity and matched condition | p. 11 (8 RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 6. Objects + ablation: We evaluate MaskedMimic and conduct an ablation on various design decisions. Experiments are conducted on the sitting task with ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| The superior performance of our model suggests that, in the context of full-body tracking, a welldesigned unified network can effectively capture the diversity of ... | component/input/data sensitivity | p. 11 (8 RESULTS) |
| This form of goal-engineering (akin to prompt-engineering for language models) enables MaskedMimic to perform a range of new tasks, without additional task-specific training. | component/input/data sensitivity | p. 10 (7.2 Evaluation) |
| Fig. 3. The MaskedMimic framework: The first phase produces a fully- constrained controller 𝜋FC. This full-body tracker is trained using reinforce- ment learning to ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Fig. 4. Training scene (screenshot): The top region consists of standard flat terrain, enabling the controller to reproduce the original motions in a setting ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| By conditioning MaskedMimic on different goals at each stage of the task, the controller can be directed to perform a wide range of tasks ... | component/input/data sensitivity | p. 12 (8 RESULTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our framework consists of two stages. | While MaskedMimic demonstrates high success rates in generating diverse motions, there are three notable areas for improvement in terms of motion quality. | PDF body cue; verify exact table/figure and matched conditions | p. 15 (8 RESULTS), p. 11 (8 RESULTS), p. 9 (7.2 Evaluation), p. 10 (7.2 Evaluation), p. 11 (8 RESULTS), p. 12 (8 RESULTS) |
| Primary metric/result | We attribute these performance improvements to our architecture and data augmentation techniques. | numeric claim only at cited anchor | p. 11 (8 RESULTS) |

- Numeric sentences retained from the body:
- **p. 10 / 7.2 Evaluation - extractive body cue:** 7.3 Tasks By training MaskedMimic on randomly masked input goals, the model learns a versatile interface that can be easily used to direct the controller ...
- **p. 10 / 7.2 Evaluation - extractive body cue:** The character is first initialized at a random location between 2 and 10 meters away from the object.
- **p. 12 / 8 RESULTS - extractive body cue:** When the character is more than 0.4m from the target position, we only provide the distant target at 0.8s as input to the model, thereby ...
- **p. 13 / 8 RESULTS - extractive body cue:** We consider a trial as failed if the orientation deviates by more than 45 degrees, and we report the speed error in cm/s, measured along ...
- **p. 13 / 8 RESULTS - extractive body cue:** 8.3 Object Interaction and Ablation The previous tasks were solved by leveraging any-joint-any-time constraints.
- **p. 13 / 8 RESULTS - extractive body cue:** First, when the character is further than 2 meters from the target object, we utilize any-joint-any-time control.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 9 LIMITATIONS AND FUTURE WORK Although MaskedMimic presents a unified model for controlling physically simulated humanoids, there remains a number of limitations with our ... | p. 15 (8 RESULTS) |
| body limitation/failure cue | 2023, 2024], reducing the tracking failure rate on unseen motions by 62.5%. | p. 11 (8 RESULTS) |
| body limitation/failure cue | In addition to a lower failure rate, our controller also supports a wider range of motions, irregular terrains, and object interactions. | p. 11 (8 RESULTS) |
| body limitation/failure cue | Fig. 3. The MaskedMimic framework: The first phase produces a fully- constrained controller 𝜋FC. This full-body tracker is trained using reinforce- ment learning to ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | We hypothesize that this limitation stems from the naive mapping of motions from flat to irregular terrains based on the root-to-floor distance normalization. | p. 15 (8 RESULTS) |
| body limitation/failure cue | Notably, MaskedMimic does not produce a single solution. | p. 14 (8 RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The encoder is used solely for training, and is not utilized at runtime. | p. 7 (3. Inference) |
| The development of virtual characters capable of following dynamic user instructions and interacting with diverse scenes has been a significant challenge in computer graphics. | p. 2 (1 INTRODUCTION) |
| We represent a motion as a sequence of poses 𝑞𝑡, where each pose 𝑞𝑡= (𝑝𝑡,𝜃𝑡) is encoded with a redundant representation consisting of the ... | p. 4 (3 PRELIMINARIES) |
| (6) The encoder is modeled as a residual to the prior [Yao et al. | p. 7 (3. Inference) |
| Each input modality is tokenized (encoded) using a modality-specific encoder 𝑒𝑖(·). | p. 8 (3. Inference) |
| We provide pseudo-code of our mask sampling strategy in the supplementary material. | p. 8 (3. Inference) |
| We consider a trial "failed" if at any frame the average joint deviation is larger than 0.5m [Luo et al. | p. 10 (8 RESULTS) |
| MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting • 11 (a) Full-body tracking: punching (b) Full-body tracking: dancing (c) VR tracking: cartwheel (d) ... | p. 11 (8 RESULTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 15 / 8 RESULTS - extractive body cue:** 9 LIMITATIONS AND FUTURE WORK Although MaskedMimic presents a unified model for controlling physically simulated humanoids, there remains a number of limitations with our model.
- **p. 11 / 8 RESULTS - extractive body cue:** 2023, 2024], reducing the tracking failure rate on unseen motions by 62.5%.
- **p. 11 / 8 RESULTS - extractive body cue:** In addition to a lower failure rate, our controller also supports a wider range of motions, irregular terrains, and object interactions.
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3. The MaskedMimic framework: The first phase produces a fully- constrained controller 𝜋FC. This full-body tracker is trained using reinforce- ment learning to imitate ...
- **p. 15 / 8 RESULTS - extractive body cue:** We hypothesize that this limitation stems from the naive mapping of motions from flat to irregular terrains based on the root-to-floor distance normalization.
- **p. 14 / 8 RESULTS - extractive body cue:** Notably, MaskedMimic does not produce a single solution.

- **Evidence anchors reviewed:** datasets p. 9 (7.2 Evaluation), p. 10 (7.2 Evaluation), p. 11 (8 RESULTS), p. 12 (8 RESULTS), p. 12 (8 RESULTS), p. 14 (8 RESULTS), metrics p. 14 (8 RESULTS), p. 9 (7.2 Evaluation), p. 11 (8 RESULTS), p. 12 (8 RESULTS), p. 13 (8 RESULTS), p. 10 (7.2 Evaluation), baselines p. 10 (7.2 Evaluation), p. 10 (7.2 Evaluation), p. 11 (8 RESULTS), p. 12 (8 RESULTS), p. 12 (8 RESULTS), p. 11 (8 RESULTS), results p. 15 (8 RESULTS), p. 11 (8 RESULTS), p. 9 (7.2 Evaluation), p. 10 (7.2 Evaluation), p. 11 (8 RESULTS), p. 12 (8 RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (21 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** This test establishes the baseline capability for motion generation, both in terms of success rates and tracking quality, and allows comparison to prior systems for motion tracking. (p. 10, 7.2 Evaluation).
- **Metric evidence:** We evaluate versions of the model with key components removed (Section 6), and measure the impact on the average success rate and error (i.e. average minimal distance from a valid ... (p. 14, 8 RESULTS).
- **Baseline/ablation evidence:** This test establishes the baseline capability for motion generation, both in terms of success rates and tracking quality, and allows comparison to prior systems for motion tracking. (p. 10, 7.2 Evaluation).
- **Failure/negative evidence:** 9 LIMITATIONS AND FUTURE WORK Although MaskedMimic presents a unified model for controlling physically simulated humanoids, there remains a number of limitations with our model. (p. 15, 8 RESULTS).
