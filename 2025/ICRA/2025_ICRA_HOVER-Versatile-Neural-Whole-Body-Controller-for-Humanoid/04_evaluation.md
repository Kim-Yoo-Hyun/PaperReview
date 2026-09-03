# Evaluation - HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://research.nvidia.com/labs/lpr/publication/he2025hover/; PDF retrieval source: https://research.nvidia.com/labs/lpr/publication/he2025hover/. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 4 (III. EXPERIMENT), p. 5 (III. EXPERIMENT), p. 5 (III. EXPERIMENT), p. 6 (III. EXPERIMENT), p. 6 (III. EXPERIMENT), p. 2 (Figure/Table caption)): In this section, we present extensive experimental results in both IsaacGym [23] and the real-world Unitree H1 [24] robot to address the following questions: • Q1: Can HOVER as a ...

## Evaluation Body Digest

- **p. 4 / III. EXPERIMENT - extractive body cue:** In this section, we present extensive experimental results in both IsaacGym [23] and the real-world Unitree H1 [24] robot to address the following questions: • ...
- **p. 5 / III. EXPERIMENT - extractive body cue:** Real-World Evaluation To address Q3 (does HOVER transfer to real-world hardware and execute versatile multi-mode control?), we conduct quantitative tracking experiments and locomotion tests for ...
- **p. 4 / III. EXPERIMENT - extractive body cue:** In simulation, we evaluate using the retargeted AMASS dataset ˆQ.
- **p. 5 / III. EXPERIMENT - extractive body cue:** For example, the performance of HOVER under ExBody mode is evaluated with a fixed mask to match ExBody mode across the entire dataset ˆQ.
- **p. 6 / III. EXPERIMENT - extractive body cue:** 5: Real-World Evaluations on different control modes.
- **p. 6 / III. EXPERIMENT - extractive body cue:** The results demonstrate that HOVER can smoothly track motions across different modes, showcasing its robustness for real-world scenarios (e.g., when there are occlusions in the ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: We assess the tracking accuracy of two multi-mode control policies-HOVER (green) and Multi-Mode RL (purple)-across eight distinct humanoid control modes. The comparison is ...
- **p. 5 / III. EXPERIMENT - extractive body cue:** We scale the tracking error via Emax-E(.) Emax-Emin for visualization, where larger radar webs indicate better tracking performance.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** III. EXPERIMENT (p. 4).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| III. EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | In this section, we present extensive experimental results in both IsaacGym [23] and the real-world Unitree H1 [24] robot to address the following questions: ... | p. 4 (III. EXPERIMENT) |
| III. EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results show that HOVER achieves consistently lower tracking error across 32/32 metrics and modes. | p. 5 (III. EXPERIMENT) |
| III. EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results in Table IV show that HOVER consistently outperforms specialists in terms of tracking metrics that are trained for specific command configurations. | p. 5 (III. EXPERIMENT) |
| III. EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results that are statistically significant are highlighted in bold across 5 tests. | p. 6 (III. EXPERIMENT) |
| III. EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results demonstrate that HOVER can smoothly track motions across different modes, showcasing its robustness for real-world scenarios (e.g., when there are occlusions in ... | p. 6 (III. EXPERIMENT) |

## Dataset / Benchmark Role

- **p. 4 / III. EXPERIMENT - extractive body cue:** In this section, we present extensive experimental results in both IsaacGym [23] and the real-world Unitree H1 [24] robot to address the following questions: • ...
- **p. 5 / III. EXPERIMENT - extractive body cue:** Real-World Evaluation To address Q3 (does HOVER transfer to real-world hardware and execute versatile multi-mode control?), we conduct quantitative tracking experiments and locomotion tests for ...
- **p. 4 / III. EXPERIMENT - extractive body cue:** In simulation, we evaluate using the retargeted AMASS dataset ˆQ.
- **p. 5 / III. EXPERIMENT - extractive body cue:** For example, the performance of HOVER under ExBody mode is evaluated with a fixed mask to match ExBody mode across the entire dataset ˆQ.
- **p. 6 / III. EXPERIMENT - extractive body cue:** 5: Real-World Evaluations on different control modes.
- **p. 6 / III. EXPERIMENT - extractive body cue:** The results demonstrate that HOVER can smoothly track motions across different modes, showcasing its robustness for real-world scenarios (e.g., when there are occlusions in the ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: HOVER enables versatile humanoid control with a unified multi-mode command space. The versatile multi-mode command space supports kinematic position tracking (blue), local joint ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: Overview of HOVER distillation process. The HOVER policy is distilled from the Oracle policy through proprioception and command masking. The task commands for ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 3. We hypothesize that this is due to the policy leveraging shared physical knowledge across modes, such as maintaining balance, human-like motion, and precise ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 3: Comparison between prior work specialists (blue) and our generalist policy (green) under corresponding modes. The metrics used are: upper/lower joint error (rad), global/local ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: We assess the tracking accuracy of two multi-mode control policies-HOVER (green) and Multi-Mode RL (purple)-across eight distinct humanoid control modes. The comparison is ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Real-World Evaluations on different control modes. Additionally, we conduct a real-test teleoperation demo with Vision Pro, randomly masking out the positions of the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6: HOVER shows robustness under control mode switches during locomotion and real-time teleoperation tests. serves for locomotion ability, and is used for navigation and ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In this section, we present extensive experimental results in both IsaacGym [23] and the real-world Unitree H1 [24] robot to address the following questions: ... | embodiment, simulator version and control stack | p. 4 (III. EXPERIMENT), p. 5 (III. EXPERIMENT) |
| Task/environment | Real-World Evaluation To address Q3 (does HOVER transfer to real-world hardware and execute versatile multi-mode control?), we conduct quantitative tracking experiments and locomotion tests ... | reset, timeout, object/scene variation | p. 5 (III. EXPERIMENT), p. 4 (III. EXPERIMENT) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 4 (II. METHOD), p. 2 (II. METHOD) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 3 (II. METHOD), p. 3 (II. METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 4: We assess the tracking accuracy of two multi-mode control policies-HOVER (green) and Multi-Mode RL (purple)-across eight distinct humanoid control modes. The comparison ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| We scale the tracking error via Emax-E(.) Emax-Emin for visualization, where larger radar webs indicate better tracking performance. | definition/direction/unit from same section | p. 5 (III. EXPERIMENT) |
| Figure 3. We hypothesize that this is due to the policy leveraging shared physical knowledge across modes, such as maintaining balance, human-like motion, and ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Fig. 3: Comparison between prior work specialists (blue) and our generalist policy (green) under corresponding modes. The metrics used are: upper/lower joint error (rad), ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| We calculate tracking error in terms of kinematic pose, joint angles, and root twist and rotations. | definition/direction/unit from same section | p. 4 (III. EXPERIMENT) |
| We evaluate policy's ability to imitate the reference motion by compare the tracking error of the global body position Eg-mpjpe (mm), the root-relative mean ... | definition/direction/unit from same section | p. 4 (III. EXPERIMENT) |
| The results demonstrate that HOVER can smoothly track motions across different modes, showcasing its robustness for real-world scenarios (e.g., when there are occlusions in ... | definition/direction/unit from same section | p. 6 (III. EXPERIMENT) |
| Fig. 6: HOVER shows robustness under control mode switches during locomotion and real-time teleoperation tests. serves for locomotion ability, and is used for navigation ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| To address Q2 (does HOVER outperform other methods of training a multi-mode humanoid controller?), we compare HOVER with a multi-mode RL baseline that follows ... | comparison identity and matched condition | p. 5 (III. EXPERIMENT) |
| In every command mode, HOVER outperforms prior work specialist controllers in at least 7 out of the 12 metrics, as highlighted by the bold ... | comparison identity and matched condition | p. 5 (III. EXPERIMENT) |
| For each control mode, we provide only the relevant observation input to the controller and train the specialist baseline with RL. | comparison identity and matched condition | p. 4 (III. EXPERIMENT) |
| To address Q2, we compare with another multi-mode RL policy, which follows the same masking process on the goal commands, but trains the baseline ... | comparison identity and matched condition | p. 4 (III. EXPERIMENT) |
| Fig. 2: Overview of HOVER distillation process. The HOVER policy is distilled from the Oracle policy through proprioception and command masking. The task commands ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| Fig. 3: Comparison between prior work specialists (blue) and our generalist policy (green) under corresponding modes. The metrics used are: upper/lower joint error (rad), ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Furthermore, this means that even when focusing on a single control mode without considering multi-mode versatility, distilling from an oracle policy still surpasses RL-trained ... | component/input/data sensitivity | p. 5 (III. EXPERIMENT) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To summarize, our contributions are threefold: 1) we present HOVER, a unified neural controller for humanoid whole-body control supporting multiple control modes; 2) we ... | In this section, we present extensive experimental results in both IsaacGym [23] and the real-world Unitree H1 [24] robot to address the following questions: ... | PDF body cue; verify exact table/figure and matched conditions | p. 4 (III. EXPERIMENT), p. 5 (III. EXPERIMENT), p. 5 (III. EXPERIMENT), p. 6 (III. EXPERIMENT), p. 6 (III. EXPERIMENT), p. 2 (Figure/Table caption) |
| Primary metric/result | The results show that HOVER achieves consistently lower tracking error across 32/32 metrics and modes. | numeric claim only at cited anchor | p. 5 (III. EXPERIMENT) |

- Numeric sentences retained from the body:
- **p. 5 / III. EXPERIMENT - extractive body cue:** Method Eg-mpjpe-mode ↓Empjpe-mode ↓Eacc-mode ↓ Evel-mode ↓ Left Hand Mode - Upper: kinematic position tracking (left hand), Lower: N/A Specialist 189±1.526 147±1.324 5.82±0.029 11.2±0.089 HOVER ...
- **p. 6 / III. EXPERIMENT - extractive body cue:** Method Eg-mpjpe ↓ Empjpe ↓ Eupper-j ↓ Eroot-rpy ↓ ExBody Mode ExBody (Specialist) 51.3 ±0.279 39.3 ±0.214 0.131 ±0.001 0.036 ±0.001 HOVER (Ours) 48.9 ±0.470 ...
- **p. 3 / II. METHOD - extractive body cue:** Following [9], we stack these terms over the last 25 steps to represent the student's proprioceptive input.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Future work will explore further developing an automated mode-switching module for real-world applications. | p. 6 (V. CONCLUSIONS) |
| body limitation/failure cue | The results demonstrate that HOVER can smoothly track motions across different modes, showcasing its robustness for real-world scenarios (e.g., when there are occlusions in ... | p. 6 (III. EXPERIMENT) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The mean values of the metrics are computed across all motion sequences from dataset ˆQ. | p. 4 (III. EXPERIMENT) |
| In this section, we present extensive experimental results in both IsaacGym [23] and the real-world Unitree H1 [24] robot to address the following questions: ... | p. 4 (III. EXPERIMENT) |
| Real-World Evaluation To address Q3 (does HOVER transfer to real-world hardware and execute versatile multi-mode control?), we conduct quantitative tracking experiments and locomotion tests ... | p. 5 (III. EXPERIMENT) |
| The retargeting procedure from human motion dataset [17] to humanoid motion dataset has three steps: Step-1: We first compute the keypoints positions of the ... | p. 3 (II. METHOD) |
| Following [9], we stack these terms over the last 25 steps to represent the student's proprioceptive input. | p. 3 (II. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / V. CONCLUSIONS - extractive body cue:** Future work will explore further developing an automated mode-switching module for real-world applications.
- **p. 6 / III. EXPERIMENT - extractive body cue:** The results demonstrate that HOVER can smoothly track motions across different modes, showcasing its robustness for real-world scenarios (e.g., when there are occlusions in the ...

- **Evidence anchors reviewed:** datasets p. 4 (III. EXPERIMENT), p. 5 (III. EXPERIMENT), p. 4 (III. EXPERIMENT), p. 5 (III. EXPERIMENT), p. 6 (III. EXPERIMENT), p. 6 (III. EXPERIMENT), metrics p. 5 (Figure/Table caption), p. 5 (III. EXPERIMENT), p. 2 (Figure/Table caption), p. 2 (Figure/Table caption), p. 4 (III. EXPERIMENT), p. 4 (III. EXPERIMENT), baselines p. 5 (III. EXPERIMENT), p. 5 (III. EXPERIMENT), p. 4 (III. EXPERIMENT), p. 4 (III. EXPERIMENT), p. 2 (Figure/Table caption), p. 2 (Figure/Table caption), results p. 4 (III. EXPERIMENT), p. 5 (III. EXPERIMENT), p. 5 (III. EXPERIMENT), p. 6 (III. EXPERIMENT), p. 6 (III. EXPERIMENT), p. 2 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** In this section, we present extensive experimental results in both IsaacGym [23] and the real-world Unitree H1 [24] robot to address the following questions: • Q1: Can HOVER as a ... (p. 4, III. EXPERIMENT).
- **Metric evidence:** We scale the tracking error via Emax-E(.) Emax-Emin for visualization, where larger radar webs indicate better tracking performance. (p. 5, III. EXPERIMENT).
- **Baseline/ablation evidence:** In every command mode, HOVER outperforms prior work specialist controllers in at least 7 out of the 12 metrics, as highlighted by the bold values in Table III. (p. 5, III. EXPERIMENT).
- **Failure/negative evidence:** The results demonstrate that HOVER can smoothly track motions across different modes, showcasing its robustness for real-world scenarios (e.g., when there are occlusions in the reference motions). (p. 6, III. EXPERIMENT).
