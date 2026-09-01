# Evaluation - Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2605.27886; PDF retrieval source: https://arxiv.org/pdf/2605.27886. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.4. Ablation and Comparison of VTLA), p. 8 (4.4. Ablation and Comparison of VTLA), p. 6 (4.1. Cross-Platform Data Validation), p. 6 (4.1. Cross-Platform Data Validation), p. 7 (4.2. Tactile Data Diversity Analysis), p. 5 (Figure/Table caption)): Adding explicit force supervision enables precise force prediction and substantially improves performance under gentle conditions.

## Evaluation Body Digest

- **p. 6 / 4.1. Cross-Platform Data Validation - extractive body cue:** Specifically, we select four subtasks from the LIBERO benchmark suite and compare the success rates of the original MuJoCo-based dataset with those of our replayed ...
- **p. 6 / 4.1. Cross-Platform Data Validation - extractive body cue:** When using the same robot kinematics and control policy as in the original dataset, our baseline configuration yields a success rate distribution that closely matches ...
- **p. 7 / 4.2. Tactile Data Diversity Analysis - extractive body cue:** This subset includes 9 tasks from the Object dataset, each executed under two force conditions specified by linguistic adverbs.
- **p. 7 / 4.2. Tactile Data Diversity Analysis - extractive body cue:** We collect three datasets over the task group, differing only in force magnitude and gripper actuation strategy.
- **p. 8 / 4.4. Ablation and Comparison of VTLA - extractive body cue:** To compare and conduct ablation experiments on different tactile injection methods and force control strategies, we evaluate tasks from Dataset B.
- **p. 8 / 4.3. Effectiveness of Hybrid Controller - extractive body cue:** In Tabero Object task 1, the predicted force is shown in blue and the measured force in red: (a) 100% force, (b) 25% force, (c) ...
- **p. 6 / 4.1. Cross-Platform Data Validation - extractive body cue:** Cross-platform data validation: Task success rates across four LIBERO subtasks.
- **p. 6 / 4.1. Cross-Platform Data Validation - extractive body cue:** We validate the fidelity of data migration from MuJoCo to Isaac Lab by evaluating both task success rates and distributional consistency.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 4. Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.4. Ablation and Comparison of VTLA | BENCHMARK / DATASET | Adding explicit force supervision enables precise force prediction and substantially improves performance under gentle conditions. | p. 8 (4.4. Ablation and Comparison of VTLA) |
| 4.4. Ablation and Comparison of VTLA | BENCHMARK / DATASET | When tactile tokens such as images or force fields are provided, the policy gains basic force modulation ability and achieves nontrivial success. | p. 8 (4.4. Ablation and Comparison of VTLA) |
| 4.1. Cross-Platform Data Validation | BENCHMARK / DATASET | Cross-platform data validation: Task success rates across four LIBERO subtasks. | p. 6 (4.1. Cross-Platform Data Validation) |
| 4.1. Cross-Platform Data Validation | BENCHMARK / DATASET | We validate the fidelity of data migration from MuJoCo to Isaac Lab by evaluating both task success rates and distributional consistency. | p. 6 (4.1. Cross-Platform Data Validation) |
| 4.2. Tactile Data Diversity Analysis | BENCHMARK / DATASET | Furthermore, the sharp drop in success rate from 25% to 10% Figure 6. | p. 7 (4.2. Tactile Data Diversity Analysis) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Cross-Platform Data Validation - extractive body cue:** Specifically, we select four subtasks from the LIBERO benchmark suite and compare the success rates of the original MuJoCo-based dataset with those of our replayed ...
- **p. 6 / 4.1. Cross-Platform Data Validation - extractive body cue:** When using the same robot kinematics and control policy as in the original dataset, our baseline configuration yields a success rate distribution that closely matches ...
- **p. 7 / 4.2. Tactile Data Diversity Analysis - extractive body cue:** This subset includes 9 tasks from the Object dataset, each executed under two force conditions specified by linguistic adverbs.
- **p. 7 / 4.2. Tactile Data Diversity Analysis - extractive body cue:** We collect three datasets over the task group, differing only in force magnitude and gripper actuation strategy.
- **p. 8 / 4.4. Ablation and Comparison of VTLA - extractive body cue:** To compare and conduct ablation experiments on different tactile injection methods and force control strategies, we evaluate tasks from Dataset B.
- **p. 8 / 4.3. Effectiveness of Hybrid Controller - extractive body cue:** In Tabero Object task 1, the predicted force is shown in blue and the measured force in red: (a) 100% force, (b) 25% force, (c) ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. Overview of the proposed framework. Motivation: Current vision-language-action (VLA) systems and robotic arm-gripper setups based on synthetic data lack force feedback mechanisms, causing ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the High-Fidelity Multimodal Data Gen- eration Pipeline. We take open-source trajectories and task setups originally developed for other platforms, such as ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Tabero-VTLA system overview. VTLA system: tactile inputs are encoded by specialized modules and fused with vision and language. Real-time force feedback system: the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Tabero Simulation Platform. Tabero replicates the LIBERO task environments, enables data reuse, enhances the visual fidelity of simulated data, and makes it possible ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Cross-platform data validation: Task success rates across four LIBERO subtasks. We compare the original MuJoCo dataset, our replay in Isaac Lab with identical ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Force Distribution Across Different Task Suites and Force Control Modes. The force distribution charts show the applied forces under various control modes across ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6. Different force magnitudes of tactile images and corresponding camera images are illustrated. The left two columns in the figure represent the first category ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Training results on three datasets METRIC A 100% / 25% B 100% / 10% C 100% / 10% SR 0.87 / 0.79 0.86 ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Specifically, we select four subtasks from the LIBERO benchmark suite and compare the success rates of the original MuJoCo-based dataset with those of our ... | embodiment, simulator version and control stack | p. 6 (4.1. Cross-Platform Data Validation), p. 6 (4.1. Cross-Platform Data Validation) |
| Task/environment | When using the same robot kinematics and control policy as in the original dataset, our baseline configuration yields a success rate distribution that closely ... | reset, timeout, object/scene variation | p. 6 (4.1. Cross-Platform Data Validation), p. 7 (4.2. Tactile Data Diversity Analysis) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 5 (3.5. Decoupled Force-Position Hybrid Controller), p. 4 (3.2. Cross-Modal Data Acquisition) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 5 (3.5. Decoupled Force-Position Hybrid Controller), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Cross-platform data validation: Task success rates across four LIBERO subtasks. | definition/direction/unit from same section | p. 6 (4.1. Cross-Platform Data Validation) |
| We validate the fidelity of data migration from MuJoCo to Isaac Lab by evaluating both task success rates and distributional consistency. | definition/direction/unit from same section | p. 6 (4.1. Cross-Platform Data Validation) |
| Furthermore, the sharp drop in success rate from 25% to 10% Figure 6. | definition/direction/unit from same section | p. 7 (4.2. Tactile Data Diversity Analysis) |
| For unseen adverbs such as "lightly" and "forcefully", the model produces intermediate forces that align with their meanings, though success rates decrease. | definition/direction/unit from same section | p. 8 (4.5. Semantic Force Generalization) |
| MODELS F SR G SR F AG G AG NONE 0.00 0.00 0.0 0.0 IMG 0.37 0.01 3.0 1.1 FIELD 0.40 0.01 2.9 2.0 ... | definition/direction/unit from same section | p. 8 (4.4. Ablation and Comparison of VTLA) |
| Different force magnitudes of tactile images and corresponding camera images are illustrated. | definition/direction/unit from same section | p. 7 (4.2. Tactile Data Diversity Analysis) |
| Table 12. Task completion performance and force data of the tactile gripper at 100% tactile force TASK n RATIO (%) MAX STEPS AG AA ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| Figure 1. Overview of the proposed framework. Motivation: Current vision-language-action (VLA) systems and robotic arm-gripper setups based on synthetic data lack force feedback mechanisms, ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compare a baseline using binary gripper control against our approach, which explicitly sets different force parameters during execution, the results are shown in ... | comparison identity and matched condition | p. 6 (4.2. Tactile Data Diversity Analysis) |
| When using the same robot kinematics and control policy as in the original dataset, our baseline configuration yields a success rate distribution that closely ... | comparison identity and matched condition | p. 6 (4.1. Cross-Platform Data Validation) |
| We conduct four ablation studies on the gripper controller: (a) full force with hybrid control, (b) reduced force with hybrid control, (c) reduced force ... | comparison identity and matched condition | p. 7 (4.3. Effectiveness of Hybrid Controller) |
| Therefore, in subsequent ablation tests, we constructed a Tabero subset to analyze the policy's performance under extreme conditions. | comparison identity and matched condition | p. 7 (4.2. Tactile Data Diversity Analysis) |
| Ablation study on tactile modalities. | comparison identity and matched condition | p. 8 (4.4. Ablation and Comparison of VTLA) |
| To compare and conduct ablation experiments on different tactile injection methods and force control strategies, we evaluate tasks from Dataset B. | comparison identity and matched condition | p. 8 (4.4. Ablation and Comparison of VTLA) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We conduct four ablation studies on the gripper controller: (a) full force with hybrid control, (b) reduced force with hybrid control, (c) reduced force ... | component/input/data sensitivity | p. 7 (4.3. Effectiveness of Hybrid Controller) |
| We adapt a base VLA model using LoRA to incorporate tactile marker fields (Dataset A and B), while a vision-language-only variant is trained on ... | component/input/data sensitivity | p. 7 (4.2. Tactile Data Diversity Analysis) |
| 1 highlight the sensitivity of contact-rich tasks to end-effector design and force regulation. | component/input/data sensitivity | p. 6 (4.1. Cross-Platform Data Validation) |
| Figure 7. Ablation study on gripper force control. GF stands for gripper force. In Tabero Object task 1, the predicted force is shown in ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| All models, excluding the ablation architectures, were fine-tuned via LoRA with an identical set of hyperparameters, detailed parameters reported in the Appendix A. | component/input/data sensitivity | p. 8 (4.4. Ablation and Comparison of VTLA) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our work makes the following contributions: The Tabero benchmark, which enables scalable visiontactile-language data generation by replaying open-source trajectories in a high-fidelity ... | Adding explicit force supervision enables precise force prediction and substantially improves performance under gentle conditions. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.4. Ablation and Comparison of VTLA), p. 8 (4.4. Ablation and Comparison of VTLA), p. 6 (4.1. Cross-Platform Data Validation), p. 6 (4.1. Cross-Platform Data Validation), p. 7 (4.2. Tactile Data Diversity Analysis), p. 5 (Figure/Table caption) |
| Primary metric/result | When tactile tokens such as images or force fields are provided, the policy gains basic force modulation ability and achieves nontrivial success. | numeric claim only at cited anchor | p. 8 (4.4. Ablation and Comparison of VTLA) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Cross-Platform Data Validation - extractive body cue:** TASK MUJOCO ISAAC T-100 T-25 T-10 SPATIAL 0.86 0.83 0.42 0.24 0.07 OBJECT 0.91 0.77 0.84 0.87 0.73 GOAL 0.76 0.78 0.55 0.44 0.30 10 ...
- **p. 7 / 4.2. Tactile Data Diversity Analysis - extractive body cue:** This subset includes 9 tasks from the Object dataset, each executed under two force conditions specified by linguistic adverbs.
- **p. 4 / 3.2. Cross-Modal Data Acquisition - extractive body cue:** All cameras are rendered in parallel using tiled rendering, and all modalities, including visual, tactile, force, language instructions, and executed actions, are sampled synchronously at ...
- **p. 4 / 3.4. Tabero-VTLA - extractive body cue:** The input consists of H + 1 frames: the first frame captures the undeformed marker layout, and the subsequent H frames record 2D marker positions ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 2, removing tactile feedback leads to complete failure in force modulation, highlighting its critical role in gentle manipulation. | p. 7 (4.2. Tactile Data Diversity Analysis) |
| body limitation/failure cue | Future work could explore reinforcement learning to balance these objectives. | p. 8 (5. Conclusions) |
| body limitation/failure cue | Nevertheless, Our current framework does not jointly optimize for both task success and minimal interaction force. | p. 8 (5. Conclusions) |
| body limitation/failure cue | Figure 4. Tabero Simulation Platform. Tabero replicates the LIBERO task environments, enables data reuse, enhances the visual fidelity of simulated data, and makes it ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | Dataset B also employs continuous control but reduces the force to 10%, representing an extreme low-force regime where slippage is likely. | p. 7 (4.2. Tactile Data Diversity Analysis) |
| body limitation/failure cue | This degradation is especially pronounced in tasks requiring delicate manipulation, where lower grip forces strongly correlate with reduced success. | p. 6 (4.1. Cross-Platform Data Validation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The hyperparameters of our controller are presented in Appendix B. | p. 7 (4.3. Effectiveness of Hybrid Controller) |
| All models, excluding the ablation architectures, were fine-tuned via LoRA with an identical set of hyperparameters, detailed parameters reported in the Appendix A. | p. 8 (4.4. Ablation and Comparison of VTLA) |
| None = No tactile input; Img = Tactile image input; Field = Force field input; Force E = Force input via MLP encoder; Force ... | p. 8 (4.4. Ablation and Comparison of VTLA) |
| Leveraging the GPU-accelerated parallel rendering capabilities of Isaac Lab, we build a real-time, synchronized multimodal data acquisition system (Fig. | p. 3 (3.2. Cross-Modal Data Acquisition) |
| Detailed architecture and hyperparameters are provided in Appendix A. | p. 4 (3.4. Tabero-VTLA) |
| Implementation details and parameter settings are provided in the Appendix A. | p. 4 (3.4. Tabero-VTLA) |
| The final joint velocity command ˙q is then computed via differential inverse kinematics. | p. 5 (3.5. Decoupled Force-Position Hybrid Controller) |
| VTLA system: tactile inputs are encoded by specialized modules and fused with vision and language. | p. 5 (3.5. Decoupled Force-Position Hybrid Controller) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.2. Tactile Data Diversity Analysis - extractive body cue:** 2, removing tactile feedback leads to complete failure in force modulation, highlighting its critical role in gentle manipulation.
- **p. 8 / 5. Conclusions - extractive body cue:** Future work could explore reinforcement learning to balance these objectives.
- **p. 8 / 5. Conclusions - extractive body cue:** Nevertheless, Our current framework does not jointly optimize for both task success and minimal interaction force.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Tabero Simulation Platform. Tabero replicates the LIBERO task environments, enables data reuse, enhances the visual fidelity of simulated data, and makes it possible ...
- **p. 7 / 4.2. Tactile Data Diversity Analysis - extractive body cue:** Dataset B also employs continuous control but reduces the force to 10%, representing an extreme low-force regime where slippage is likely.
- **p. 6 / 4.1. Cross-Platform Data Validation - extractive body cue:** This degradation is especially pronounced in tasks requiring delicate manipulation, where lower grip forces strongly correlate with reduced success.

- **PDF anchors reviewed:** datasets p. 6 (4.1. Cross-Platform Data Validation), p. 6 (4.1. Cross-Platform Data Validation), p. 7 (4.2. Tactile Data Diversity Analysis), p. 7 (4.2. Tactile Data Diversity Analysis), p. 8 (4.4. Ablation and Comparison of VTLA), p. 8 (4.3. Effectiveness of Hybrid Controller), metrics p. 6 (4.1. Cross-Platform Data Validation), p. 6 (4.1. Cross-Platform Data Validation), p. 7 (4.2. Tactile Data Diversity Analysis), p. 8 (4.5. Semantic Force Generalization), p. 8 (4.4. Ablation and Comparison of VTLA), p. 7 (4.2. Tactile Data Diversity Analysis), baselines p. 6 (4.2. Tactile Data Diversity Analysis), p. 6 (4.1. Cross-Platform Data Validation), p. 7 (4.3. Effectiveness of Hybrid Controller), p. 7 (4.2. Tactile Data Diversity Analysis), p. 8 (4.4. Ablation and Comparison of VTLA), p. 8 (4.4. Ablation and Comparison of VTLA), results p. 8 (4.4. Ablation and Comparison of VTLA), p. 8 (4.4. Ablation and Comparison of VTLA), p. 6 (4.1. Cross-Platform Data Validation), p. 6 (4.1. Cross-Platform Data Validation), p. 7 (4.2. Tactile Data Diversity Analysis), p. 5 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
