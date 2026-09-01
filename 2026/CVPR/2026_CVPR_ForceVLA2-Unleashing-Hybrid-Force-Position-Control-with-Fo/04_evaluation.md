# Evaluation - ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Li_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (5.2. Main Experiment Results), p. 7 (5.2. Main Experiment Results), p. 6 (5. Experiments), p. 8 (5.2. Main Experiment Results), p. 8 (5.3. Ablation Study), p. 7 (5.2. Main Experiment Results)): 1, ForceVLA2 significantly outperforms all baselines, achieving a 66% average success rate across all tasks.

## Evaluation Body Digest

- **p. 6 / 5.1. Experiment Setting - extractive body cue:** Our experimental benchmark consists of 5 contact-rich manipulation tasks within the proposed ForceVLA2-Dataset: Press the bottle, Clean the vase, Clean the board, Retrieve the plate, ...
- **p. 5 / 4. ForceVLA2-Dataset - extractive body cue:** Demonstrations were collected using a 7-DOF Flexiv Rizon 4s robotic arm equipped with a DH Robotics AG-95 adaptive gripper.
- **p. 5 / 4. ForceVLA2-Dataset - extractive body cue:** The collected dataset constitutes a multi-modal corpus encompassing visual, proprioceptive, task-prompt, force-prompt, and force modalities.
- **p. 6 / 4. ForceVLA2-Dataset - extractive body cue:** (a) ForceVLA2-Dataset is the first dataset with force prompts for task decomposition and the only one providing force-control supervision.
- **p. 7 / 5.2. Main Experiment Results - extractive body cue:** 5, for force-intensive tasks such as clean board and bottle pressing, excessive contact force can easily push the robot into overload.
- **p. 8 / 5.2. Main Experiment Results - extractive body cue:** 6, during the bottle pressing task, when the robot arm is about to press the bottle, we abruptly lower the base.
- **p. 8 / 5.2. Main Experiment Results - extractive body cue:** 70.0 30.0 60.0 0.0 20.0 36.0 ✓ 85.0 40.0 85.0 0.0 40.0 50.0↑14 ✓ ✓ 80.0 75.0 70.0 35.0 70.0 66.0↑16 In addition to outperforming ...
- **p. 7 / 5.2. Main Experiment Results - extractive body cue:** ForceVLA2 exhibits robust position and orientation following, and in object search tasks, it can still perform successful re-grasps even when visual observations fail. on force-sensitive ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** contact-rich manipulation scene.
- **Input boundary:** tactile image/force, vision과 proprioceptive history.
- **Output/decision under evaluation:** grasp/contact action, force command 또는 object motion.
- **Primary target:** slip/contact success, force/pose error와 robustness.
- **Detected evaluation headings:** 4. ForceVLA2-Dataset (p. 5); 5. Experiments (p. 6); 5.1. Experiment Setting (p. 6); 5.2. Main Experiment Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Main Experiment Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | 1, ForceVLA2 significantly outperforms all baselines, achieving a 66% average success rate across all tasks. | p. 6 (5.2. Main Experiment Results) |
| 5.2. Main Experiment Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | The ACP achieves a success rate of only 16.0%, primarily due to its limited generalization capabilities. | p. 7 (5.2. Main Experiment Results) |
| 5. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The experiments address the following research questions: • Q1: How does ForceVLA2 perform in real-world contact-rich manipulation tasks, and what specific advantages and technical ... | p. 6 (5. Experiments) |
| 5.2. Main Experiment Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Entries indicate success rate (%). gray : baseline results. | p. 8 (5.2. Main Experiment Results) |
| 5.3. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results show a consistent increase in success rate as more modules are introduced, confirming the effectiveness of our overall architectural design. | p. 8 (5.3. Ablation Study) |

## Dataset / Benchmark Role

- **p. 6 / 5.1. Experiment Setting - extractive body cue:** Our experimental benchmark consists of 5 contact-rich manipulation tasks within the proposed ForceVLA2-Dataset: Press the bottle, Clean the vase, Clean the board, Retrieve the plate, ...
- **p. 5 / 4. ForceVLA2-Dataset - extractive body cue:** Demonstrations were collected using a 7-DOF Flexiv Rizon 4s robotic arm equipped with a DH Robotics AG-95 adaptive gripper.
- **p. 5 / 4. ForceVLA2-Dataset - extractive body cue:** The collected dataset constitutes a multi-modal corpus encompassing visual, proprioceptive, task-prompt, force-prompt, and force modalities.
- **p. 6 / 4. ForceVLA2-Dataset - extractive body cue:** (a) ForceVLA2-Dataset is the first dataset with force prompts for task decomposition and the only one providing force-control supervision.
- **p. 7 / 5.2. Main Experiment Results - extractive body cue:** 5, for force-intensive tasks such as clean board and bottle pressing, excessive contact force can easily push the robot into overload.
- **p. 8 / 5.2. Main Experiment Results - extractive body cue:** 6, during the bottle pressing task, when the robot arm is about to press the bottle, we abruptly lower the base.
- **p. 8 / 5.2. Main Experiment Results - extractive body cue:** 70.0 30.0 60.0 0.0 20.0 36.0 ✓ 85.0 40.0 85.0 0.0 40.0 50.0↑14 ✓ ✓ 80.0 75.0 70.0 35.0 70.0 66.0↑16 In addition to outperforming ...
- **p. 7 / 5.2. Main Experiment Results - extractive body cue:** ForceVLA2 exhibits robust position and orientation following, and in object search tasks, it can still perform successful re-grasps even when visual observations fail. on force-sensitive ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. ForceVLA2 concept. Contact-rich manipulation requires force regulation, beyond visual and state observations (left). ForceVLA2 integrates force information across multiple scales, enabling rich modeling ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Framework of ForceVLA2. ForceVLA2 takes multi-view images, task and force prompts, and proprioceptive states (EE pose and force) as input. Force is injected ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. The illustration of ForceVLA2-Dataset. (a) ForceVLA2-Dataset is the first dataset with force prompts for task decomposition and the only one providing force-control supervision. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. The dataset collection system. A Flexiv arm is driven by manually controlled GELLO [39] to accomplish dexterous tasks and record images, force, as ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Qualitative results on typical manipulation tasks (compared with ForceVLA and π serials). ForceVLA2 completes these tasks with higher success rates and faster execution ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6. Additional tests on following and re-targeting. ForceVLA2 exhibits robust position and orientation following, and in object search tasks, it can still perform successful ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1. Success rates (%) comparison of different methods. π0 w/ F: π0 with native force input. Each value represents the success rate over 20 ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. Ablation Study of Different Modules in the ForceVLA2 Model. FP: Force Prompt. ME: Multimodal En- coder. CM: Cross-Scale MoE module. Entries indicate success ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Our experimental benchmark consists of 5 contact-rich manipulation tasks within the proposed ForceVLA2-Dataset: Press the bottle, Clean the vase, Clean the board, Retrieve the ... | embodiment, simulator version and control stack | p. 6 (5.1. Experiment Setting), p. 5 (4. ForceVLA2-Dataset) |
| Task/environment | Demonstrations were collected using a 7-DOF Flexiv Rizon 4s robotic arm equipped with a DH Robotics AG-95 adaptive gripper. | reset, timeout, object/scene variation | p. 5 (4. ForceVLA2-Dataset), p. 5 (4. ForceVLA2-Dataset) |
| Observation/sensor | tactile image/force, vision과 proprioceptive history | calibration, preprocessing, privileged input | p. 5 (4. ForceVLA2-Dataset), p. 4 (3.1. Long-Horizon Force Awareness via Prompting) |
| Output/decision | grasp/contact action, force command 또는 object motion | action frame, controller and termination | p. 3 (3. ForceVLA2 Framework), p. 3 (3.1. Long-Horizon Force Awareness via Prompting) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 1, ForceVLA2 significantly outperforms all baselines, achieving a 66% average success rate across all tasks. | definition/direction/unit from same section | p. 6 (5.2. Main Experiment Results) |
| The primary evaluation metric is the success rate (%), determined by conducting 20 independent trials for each task. | definition/direction/unit from same section | p. 6 (5.1. Experiment Setting) |
| The ACP achieves a success rate of only 16.0%, primarily due to its limited generalization capabilities. | definition/direction/unit from same section | p. 7 (5.2. Main Experiment Results) |
| ForceVLA2 completes these tasks with higher success rates and faster execution while avoiding arm overload, demonstrating superior compliance. | definition/direction/unit from same section | p. 7 (5.2. Main Experiment Results) |
| Each value represents the success rate over 20 trials. | definition/direction/unit from same section | p. 8 (5.2. Main Experiment Results) |
| Entries indicate success rate (%). gray : baseline results. | definition/direction/unit from same section | p. 8 (5.2. Main Experiment Results) |
| Figure 1. ForceVLA2 concept. Contact-rich manipulation requires force regulation, beyond visual and state observations (left). ForceVLA2 integrates force information across multiple scales, enabling rich ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. Framework of ForceVLA2. ForceVLA2 takes multi-view images, task and force prompts, and proprioceptive states (EE pose and force) as input. Force is ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 1, ForceVLA2 significantly outperforms all baselines, achieving a 66% average success rate across all tasks. | comparison identity and matched condition | p. 6 (5.2. Main Experiment Results) |
| 70.0 30.0 60.0 0.0 20.0 36.0 ✓ 85.0 40.0 85.0 0.0 40.0 50.0↑14 ✓ ✓ 80.0 75.0 70.0 35.0 70.0 66.0↑16 In addition to ... | comparison identity and matched condition | p. 8 (5.2. Main Experiment Results) |
| Compared with models without force inputs, ForceVLA2 and ForceVLA, which incorporate force feedback, show remarkable improvements 8916 | comparison identity and matched condition | p. 6 (5.2. Main Experiment Results) |
| Qualitative results on typical manipulation tasks (compared with ForceVLA and π serials). | comparison identity and matched condition | p. 7 (5.2. Main Experiment Results) |
| Among the compared methods, ForceVLA2 actively adjusts its interaction forces and successfully completes these tasks, whereas other VLAs lack sufficient reactive adjustment capabilities. | comparison identity and matched condition | p. 7 (5.2. Main Experiment Results) |
| Entries indicate success rate (%). gray : baseline results. | comparison identity and matched condition | p. 8 (5.2. Main Experiment Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In particular, we conduct an ablation on the CrossScale MoE module by varying its modality inputs and outputs to verify the effectiveness of our ... | component/input/data sensitivity | p. 8 (5.3. Ablation Study) |
| Component-wise ablations on FP, CM, and ME (Q2). | component/input/data sensitivity | p. 8 (5.3. Ablation Study) |
| Compared with models without force inputs, ForceVLA2 and ForceVLA, which incorporate force feedback, show remarkable improvements 8916 | component/input/data sensitivity | p. 6 (5.2. Main Experiment Results) |
| The experiments address the following research questions: • Q1: How does ForceVLA2 perform in real-world contact-rich manipulation tasks, and what specific advantages and technical ... | component/input/data sensitivity | p. 6 (5. Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are summarized as follows: • We introduce ForceVLA2, the first end-to-end hybrid force-position control framework with force awareness for VLAs, enhancing contact-rich ... | 1, ForceVLA2 significantly outperforms all baselines, achieving a 66% average success rate across all tasks. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (5.2. Main Experiment Results), p. 7 (5.2. Main Experiment Results), p. 6 (5. Experiments), p. 8 (5.2. Main Experiment Results), p. 8 (5.3. Ablation Study), p. 7 (5.2. Main Experiment Results) |
| Primary metric/result | The ACP achieves a success rate of only 16.0%, primarily due to its limited generalization capabilities. | numeric claim only at cited anchor | p. 7 (5.2. Main Experiment Results) |

- Numeric sentences retained from the body:
- **p. 5 / 4. ForceVLA2-Dataset - extractive body cue:** Demonstrations were collected using a 7-DOF Flexiv Rizon 4s robotic arm equipped with a DH Robotics AG-95 adaptive gripper.
- **p. 5 / 4. ForceVLA2-Dataset - extractive body cue:** A 6D force/torque sensor attached to the end-effector recorded interaction forces at 300 Hz, while the robot joint states and end-effector (EE) 6D poses were ...
- **p. 5 / 4. ForceVLA2-Dataset - extractive body cue:** All visual streams were resized to 480×640 resolution, normalized, and timestamp-synchronized prior to storage.
- **p. 5 / 4. ForceVLA2-Dataset - extractive body cue:** The resulting dataset comprises 1000 trajectories and approximately 500K synchronized timesteps.
- **p. 6 / 4. ForceVLA2-Dataset - extractive body cue:** Current state: Wipe the board with 0.9 task progress." Force Position Wipe the board.
- **p. 8 / 5.2. Main Experiment Results - extractive body cue:** Each value represents the success rate over 20 trials.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The model also consistently reduces failures caused by arm overload and unstable contact, and ablation studies show monotonically improved performance as force prompts, the ... | p. 8 (6. Conclusion) |
| body limitation/failure cue | In contrast, other VLAs slowly chase the new EE 6D pose, leading to failure to maintain stable contact. | p. 8 (5.2. Main Experiment Results) |
| body limitation/failure cue | ForceVLA2 exhibits robust position and orientation following, and in object search tasks, it can still perform successful re-grasps even when visual observations fail. on ... | p. 7 (5.2. Main Experiment Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The primary evaluation metric is the success rate (%), determined by conducting 20 independent trials for each task. | p. 6 (5.1. Experiment Setting) |
| Each value represents the success rate over 20 trials. | p. 8 (5.2. Main Experiment Results) |
| Additional experiments focusing on the Multimodal Encoder are provided in the Appendix C. | p. 8 (5.3. Ablation Study) |
| Consequently, VLAs have beThis CVPR paper is the Open Access version, provided by the Computer Vision Foundation. | p. 1 (1. Introduction) |
| The text prompt provides a global description of the task, while the force prompt encodes the current subtask state. | p. 3 (3.1. Long-Horizon Force Awareness via Prompting) |
| Specifically, the visual tokens Ev ∈RNv×Dmodel are first processed through a visual encoder f(·): Zv = f(Ev) ∈ RNv×Dmodel. | p. 3 (3.1. Long-Horizon Force Awareness via Prompting) |
| The proprioceptive state, represented by the EE 6D pose, is expressed as p ∈R7 and encoded through another linear layer ϕP : EP = ... | p. 4 (3.2. Short-Horizon Force-to-Control Loop) |
| A dynamic gating network computes token-wise routing weights w = [wV , wS, wF ], and activates the most relevant expert for each token: ... | p. 4 (3.2.2. Adaptive Routing and Decoding) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6. Conclusion - extractive body cue:** The model also consistently reduces failures caused by arm overload and unstable contact, and ablation studies show monotonically improved performance as force prompts, the CrossScale ...
- **p. 8 / 5.2. Main Experiment Results - extractive body cue:** In contrast, other VLAs slowly chase the new EE 6D pose, leading to failure to maintain stable contact.
- **p. 7 / 5.2. Main Experiment Results - extractive body cue:** ForceVLA2 exhibits robust position and orientation following, and in object search tasks, it can still perform successful re-grasps even when visual observations fail. on force-sensitive ...

- **PDF anchors reviewed:** datasets p. 6 (5.1. Experiment Setting), p. 5 (4. ForceVLA2-Dataset), p. 5 (4. ForceVLA2-Dataset), p. 6 (4. ForceVLA2-Dataset), p. 7 (5.2. Main Experiment Results), p. 8 (5.2. Main Experiment Results), metrics p. 6 (5.2. Main Experiment Results), p. 6 (5.1. Experiment Setting), p. 7 (5.2. Main Experiment Results), p. 7 (5.2. Main Experiment Results), p. 8 (5.2. Main Experiment Results), p. 8 (5.2. Main Experiment Results), baselines p. 6 (5.2. Main Experiment Results), p. 8 (5.2. Main Experiment Results), p. 6 (5.2. Main Experiment Results), p. 7 (5.2. Main Experiment Results), p. 7 (5.2. Main Experiment Results), p. 8 (5.2. Main Experiment Results), results p. 6 (5.2. Main Experiment Results), p. 7 (5.2. Main Experiment Results), p. 6 (5. Experiments), p. 8 (5.2. Main Experiment Results), p. 8 (5.3. Ablation Study), p. 7 (5.2. Main Experiment Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
