# Evaluation - Opening the Sim-to-Real Door for Humanoid Pixel-to-Action Policy Transfer

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Xue_Opening_the_Sim-to-Real_Door_for_Humanoid_Pixel-to-Action_Policy_Transfer_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Xue_Opening_the_Sim-to-Real_Door_for_Humanoid_Pixel-to-Action_Policy_Transfer_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 7 (3.2. Effect of Photorealistic Visual Randomization), p. 6 (3.1. Surpassing Human-Teleop Baseline), p. 6 (3.1. Surpassing Human-Teleop Baseline), p. 3 (Figure/Table caption), p. 5 (Figure/Table caption)): Figure 7. Training progress of student policy bootstrapping with improvements in task success rate. The dashed lines are teacher policy success rates. cies can consistently achieve 80-90% success rate, the ...

## Evaluation Body Digest

- **p. 6 / 3.1. Surpassing Human-Teleop Baseline - extractive body cue:** Real-world visuals are unseen during training.
- **p. 6 / 3. Experiment - extractive body cue:** In this section, we will establish real-world comparison with human baselines.
- **p. 7 / 3.1. Surpassing Human-Teleop Baseline - extractive body cue:** Qualitatively, teleoperators often fail to gauge the spring-loaded force of the door handle and the door hinge, or whether the robot is leaning with the ...
- **p. 7 / 3.4. Effect of Staged Reset Exploration - extractive body cue:** A buffer size of 10, for example, stores the ten most recent snapshots of the simulation state when an environment enters a stage.
- **p. 6 / 3.1. Surpassing Human-Teleop Baseline - extractive body cue:** Success rate and completion time are evaluated at when the robot traverses through the door and reaches a point 1 m beyond the door frame ...
- **p. 6 / 3.1. Surpassing Human-Teleop Baseline - extractive body cue:** We hypothesize that the current whole-body teleoperation technology, due to its unintuitive nature, create a gap in both efficiency and success rate compared to direct ...
- **p. 7 / 3.3. Performance Boost in GRPO Fine-Tuning - extractive body cue:** The dashed lines are teacher policy success rates. cies can consistently achieve 80-90% success rate, the initial student policy performance stales at 50-70%, suggesting a ...
- **p. 7 / 3.3. Performance Boost in GRPO Fine-Tuning - extractive body cue:** Success rates (%) under visual randomization settings.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** 3. Experiment (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 7. Training progress of student policy bootstrapping with improvements in task success rate. The dashed lines are teacher policy success rates. cies can ... | p. 7 (Figure/Table caption) |
| 3.2. Effect of Photorealistic Visual Randomization | EMPIRICAL / REAL-ROBOT OR HARDWARE | This setting achieves a commendable success rate of 65.8-70%. | p. 7 (3.2. Effect of Photorealistic Visual Randomization) |
| 3.1. Surpassing Human-Teleop Baseline | EMPIRICAL / REAL-ROBOT OR HARDWARE | We hypothesize that the current whole-body teleoperation technology, due to its unintuitive nature, create a gap in both efficiency and success rate compared to ... | p. 6 (3.1. Surpassing Human-Teleop Baseline) |
| 3.1. Surpassing Human-Teleop Baseline | EMPIRICAL / REAL-ROBOT OR HARDWARE | Left: success rate (the higher the better). | p. 6 (3.1. Surpassing Human-Teleop Baseline) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 3. DoorMan training pipeline. All phases are done inter- actively with IsaacLab. In Phase 1, we train a teacher policy with privileged observations. ... | p. 3 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 3.1. Surpassing Human-Teleop Baseline - extractive body cue:** Real-world visuals are unseen during training.
- **p. 6 / 3. Experiment - extractive body cue:** In this section, we will establish real-world comparison with human baselines.
- **p. 7 / 3.1. Surpassing Human-Teleop Baseline - extractive body cue:** Qualitatively, teleoperators often fail to gauge the spring-loaded force of the door handle and the door hinge, or whether the robot is leaning with the ...
- **p. 7 / 3.4. Effect of Staged Reset Exploration - extractive body cue:** A buffer size of 10, for example, stores the ten most recent snapshots of the simulation state when an environment enters a stage.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. DoorMan, a simulation-trained, RGB-only humanoid loco-manipulation policy, opens diverse doors in the real world.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Real-world generalization of DoorMan. Top: diverse handle visuals and physical shapes. Middle: diverse wall panel visuals. Bottom: pushing and pulling open doors naturalistically. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. DoorMan training pipeline. All phases are done inter- actively with IsaacLab. In Phase 1, we train a teacher policy with privileged observations. In ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Overview of the staged-reset exploration scheme. When entering a new stage, a snapshot of the simulation is cached into the buffer. When the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. Procedurally generated doors used to train DoorMan, covering panel designs, latching mechanisms, lighting, materials, etc. Each parallelized environment is trained on a unique ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6. Average performance on all door opening tasks. Left: success rate (the higher the better). Right: task fluency in terms of time taken to ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Success rates (%) under visual randomization settings. Vi- sual Setup denotes the type of visual variation: Solid-color Rand. means uniform recoloring without textures; ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7. Training progress of student policy bootstrapping with improvements in task success rate. The dashed lines are teacher policy success rates. cies can consistently ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Real-world visuals are unseen during training. | embodiment, simulator version and control stack | p. 6 (3.1. Surpassing Human-Teleop Baseline), p. 6 (3. Experiment) |
| Task/environment | In this section, we will establish real-world comparison with human baselines. | reset, timeout, object/scene variation | p. 6 (3. Experiment), p. 7 (3.1. Surpassing Human-Teleop Baseline) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 4 (2.1. Visual RL and Teacher-Student Distillation), p. 3 (2.1. Visual RL and Teacher-Student Distillation) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 3 (2.1. Visual RL and Teacher-Student Distillation), p. 1 (Body text (section not recovered)) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Success rate and completion time are evaluated at when the robot traverses through the door and reaches a point 1 m beyond the door ... | definition/direction/unit from same section | p. 6 (3.1. Surpassing Human-Teleop Baseline) |
| We hypothesize that the current whole-body teleoperation technology, due to its unintuitive nature, create a gap in both efficiency and success rate compared to ... | definition/direction/unit from same section | p. 6 (3.1. Surpassing Human-Teleop Baseline) |
| The dashed lines are teacher policy success rates. cies can consistently achieve 80-90% success rate, the initial student policy performance stales at 50-70%, suggesting ... | definition/direction/unit from same section | p. 7 (3.3. Performance Boost in GRPO Fine-Tuning) |
| Success rates (%) under visual randomization settings. | definition/direction/unit from same section | p. 7 (3.3. Performance Boost in GRPO Fine-Tuning) |
| Figure 4. Overview of the staged-reset exploration scheme. When entering a new stage, a snapshot of the simulation is cached into the buffer. When ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Figure 3. DoorMan training pipeline. All phases are done inter- actively with IsaacLab. In Phase 1, we train a teacher policy with privileged observations. ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 8. Teacher training progress with different reset buffer sizes of 0, 10 and 100. reset buffer, as the policy finds it difficult to ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In this section, we will establish real-world comparison with human baselines. | comparison identity and matched condition | p. 6 (3. Experiment) |
| We hypothesize that the current whole-body teleoperation technology, due to its unintuitive nature, create a gap in both efficiency and success rate compared to ... | comparison identity and matched condition | p. 6 (3.1. Surpassing Human-Teleop Baseline) |
| In addition, DoorMan shines in terms of task fluency, outperforming experts by 23.8% and non-experts by 31.7%. | comparison identity and matched condition | p. 7 (3.1. Surpassing Human-Teleop Baseline) |
| We design an ablation study on the visual diversity during training, starting with no visual randomization, where objects are coated in a default gray ... | comparison identity and matched condition | p. 7 (3.2. Effect of Photorealistic Visual Randomization) |
| Figure 4. Overview of the staged-reset exploration scheme. When entering a new stage, a snapshot of the simulation is cached into the buffer. When ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Finally, we run ablation study to investigate the effect of staged reset exploration on the stability of teacher training. | component/input/data sensitivity | p. 7 (3.4. Effect of Staged Reset Exploration) |
| We design an ablation study on the visual diversity during training, starting with no visual randomization, where objects are coated in a default gray ... | component/input/data sensitivity | p. 7 (3.2. Effect of Photorealistic Visual Randomization) |
| We will also investigate the effect of varies components in our pipeline, including visual randomization, staged reset, and fine-tuning. | component/input/data sensitivity | p. 6 (3. Experiment) |
| Figure 5. Procedurally generated doors used to train DoorMan, covering panel designs, latching mechanisms, lighting, materials, etc. Each parallelized environment is trained on a ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To summarize, the main contributions of our work are: • We present the first end-to-end humanoid sim-to-real policy capable of diverse articulated loco-manipulation from ... | Figure 7. Training progress of student policy bootstrapping with improvements in task success rate. The dashed lines are teacher policy success rates. cies can ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 7 (3.2. Effect of Photorealistic Visual Randomization), p. 6 (3.1. Surpassing Human-Teleop Baseline), p. 6 (3.1. Surpassing Human-Teleop Baseline), p. 3 (Figure/Table caption), p. 5 (Figure/Table caption) |
| Primary metric/result | This setting achieves a commendable success rate of 65.8-70%. | numeric claim only at cited anchor | p. 7 (3.2. Effect of Photorealistic Visual Randomization) |

- Numeric sentences retained from the body:
- **p. 6 / 3.1. Surpassing Human-Teleop Baseline - extractive body cue:** In all experiments, the robot is randomly placed to be 1 meter in front of the door and facing the center of the door.
- **p. 3 / 2.1. Visual RL and Teacher-Student Distillation - extractive body cue:** The policy also needs to be inferenced consistently at 50 Hz, which requires efficient neural network architectures.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 8. Teacher training progress with different reset buffer sizes of 0, 10 and 100. reset buffer, as the policy finds it difficult to ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | The exploration fails when not using the 6648 | p. 7 (3.4. Effect of Staged Reset Exploration) |
| body limitation/failure cue | Trained entirely in photorealistic simulation, the resulting policy achieves robust zero-shot performance on articulated-object interaction tasks, including diverse door configurations, and exceeds human teleoperation ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | Qualitatively, teleoperators often fail to gauge the spring-loaded force of the door handle and the door hinge, or whether the robot is leaning with ... | p. 7 (3.1. Surpassing Human-Teleop Baseline) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 1-6) is evaluated on 120 unseen-door trials. | p. 7 (3.3. Performance Boost in GRPO Fine-Tuning) |
| Finally, we run ablation study to investigate the effect of staged reset exploration on the stability of teacher training. | p. 7 (3.4. Effect of Staged Reset Exploration) |
| Recent progress in GPU-accelerated, photorealistic simulation has opened a scalable data-generation path for robot learning, where massive physics and visual randomization allow policies to ... | p. 1 (Abstract) |
| Seemingly simple household interactions, such as pulling a drawer, twisting a knob, or unlatching a gate, all require precise perception-action This CVPR paper is ... | p. 1 (1. Introduction) |
| Many rely on depth sensing, object-centric features, or hard-coded motion primitives on wheeled platforms [6, 42, 44]. | p. 2 (1. Introduction) |
| Recent advances in simulation, hardware, and RL have enabled strong sim-to-real results in locomotion [4, 25, 32, 41, 45, 52], motion imitation [16, 23, ... | p. 2 (1. Introduction) |
| Next, we distill the teacher into an RGB-based student using DAgger [33], fusing a vision encoder with proprioception under aggressive visual randomization. | p. 3 (1. Introduction) |
| The vision encoder is jointly fine-tuned with the policy. | p. 4 (2.1. Visual RL and Teacher-Student Distillation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 8. Teacher training progress with different reset buffer sizes of 0, 10 and 100. reset buffer, as the policy finds it difficult to enter ...
- **p. 7 / 3.4. Effect of Staged Reset Exploration - extractive body cue:** The exploration fails when not using the 6648
- **p. 8 / 5. Conclusion - extractive body cue:** Trained entirely in photorealistic simulation, the resulting policy achieves robust zero-shot performance on articulated-object interaction tasks, including diverse door configurations, and exceeds human teleoperation baselines ...
- **p. 7 / 3.1. Surpassing Human-Teleop Baseline - extractive body cue:** Qualitatively, teleoperators often fail to gauge the spring-loaded force of the door handle and the door hinge, or whether the robot is leaning with the ...

- **Evidence anchors reviewed:** datasets p. 6 (3.1. Surpassing Human-Teleop Baseline), p. 6 (3. Experiment), p. 7 (3.1. Surpassing Human-Teleop Baseline), p. 7 (3.4. Effect of Staged Reset Exploration), metrics p. 6 (3.1. Surpassing Human-Teleop Baseline), p. 6 (3.1. Surpassing Human-Teleop Baseline), p. 7 (3.3. Performance Boost in GRPO Fine-Tuning), p. 7 (3.3. Performance Boost in GRPO Fine-Tuning), p. 5 (Figure/Table caption), p. 3 (Figure/Table caption), baselines p. 6 (3. Experiment), p. 6 (3.1. Surpassing Human-Teleop Baseline), p. 7 (3.1. Surpassing Human-Teleop Baseline), p. 7 (3.2. Effect of Photorealistic Visual Randomization), p. 5 (Figure/Table caption), results p. 7 (Figure/Table caption), p. 7 (3.2. Effect of Photorealistic Visual Randomization), p. 6 (3.1. Surpassing Human-Teleop Baseline), p. 6 (3.1. Surpassing Human-Teleop Baseline), p. 3 (Figure/Table caption), p. 5 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
