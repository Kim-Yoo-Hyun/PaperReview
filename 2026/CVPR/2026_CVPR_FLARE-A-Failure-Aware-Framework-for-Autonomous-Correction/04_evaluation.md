# Evaluation - FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_FLARE_A_Failure-Aware_Framework_for_Autonomous_Correction_and_Recovery_in_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_FLARE_A_Failure-Aware_Framework_for_Autonomous_Correction_and_Recovery_in_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (Figure/Table caption), p. 6 (4. Experiment), p. 7 (5.1. Analysis of Perturbation & Bridging), p. 7 (Figure/Table caption), p. 8 (5.2. Ablations and Analysis for Reset skills learning), p. 8 (5.2. Ablations and Analysis for Reset skills learning)): Table 1. Our method achieves state-of-the-art performance on 8 out of 9 tasks. On the remaining task, Threading D0, although we do not obtain the best result, our approach still ...

## Evaluation Body Digest

- **p. 7 / 4. Experiment - extractive body cue:** Real-world Validation To verify FLARE's effectiveness and address concerns about privileged simulation states, we conducted real-world experiments on a Piper arm with RealSense D435i (top/wrist ...
- **p. 6 / 4. Experiment - extractive body cue:** The successor to the π0 VLA model [4], which demonstrates improved generalization by training on diverse, multi-environment datasets.
- **p. 7 / 4. Experiment - extractive body cue:** Success rates of real-world manipulation tasks.
- **p. 6 / 4. Experiment - extractive body cue:** The ‘D' suffix in the task names (e.g., D0, D1) denotes the range of object randomization during scene initialization and therefore reflects task difficulty.
- **p. 8 / 5.2. Ablations and Analysis for Reset skills learning - extractive body cue:** The effective failure analysis provides highquality reset dataset for further demonstration collection.
- **p. 8 / 5.2. Ablations and Analysis for Reset skills learning - extractive body cue:** 5b, the robot must reset the coffee machine lid before adjusting the coffee pod pose; thus, the effective reset object is the lid.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Our method achieves state-of-the-art performance on 8 out of 9 tasks. On the remaining task, Threading D0, although we do not obtain the ...
- **p. 8 / 5.2. Ablations and Analysis for Reset skills learning - extractive body cue:** The reduced success rate indicates room for further augmentation and model training, which could potentially enhance errorcorrection performance.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** 4. Experiment (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1. Our method achieves state-of-the-art performance on 8 out of 9 tasks. On the remaining task, Threading D0, although we do not obtain ... | p. 6 (Figure/Table caption) |
| 4. Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | In this case, our method still achieves comparable performance, even when multiple baselines (PhoenixHuman, π0.5) reach a 100% success rate. | p. 6 (4. Experiment) |
| 5.1. Analysis of Perturbation & Bridging | EMPIRICAL / REAL-ROBOT OR HARDWARE | The best performance is achieved when r = 30◦and t = 0.7 in 0 10 20 30 40 50 60 70 80 Rotation Angle ... | p. 7 (5.1. Analysis of Perturbation & Bridging) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2. Success rates of real-world manipulation tasks. Our method outperforms the baseline in two challenging settings. Real-World Task (40 trials) π0.5 (Baseline) Ours ... | p. 7 (Figure/Table caption) |
| 5.2. Ablations and Analysis for Reset skills learning | EMPIRICAL / REAL-ROBOT OR HARDWARE | The reduced success rate indicates room for further augmentation and model training, which could potentially enhance errorcorrection performance. | p. 8 (5.2. Ablations and Analysis for Reset skills learning) |

## Dataset / Benchmark Role

- **p. 7 / 4. Experiment - extractive body cue:** Real-world Validation To verify FLARE's effectiveness and address concerns about privileged simulation states, we conducted real-world experiments on a Piper arm with RealSense D435i (top/wrist ...
- **p. 6 / 4. Experiment - extractive body cue:** The successor to the π0 VLA model [4], which demonstrates improved generalization by training on diverse, multi-environment datasets.
- **p. 7 / 4. Experiment - extractive body cue:** Success rates of real-world manipulation tasks.
- **p. 6 / 4. Experiment - extractive body cue:** The ‘D' suffix in the task names (e.g., D0, D1) denotes the range of object randomization during scene initialization and therefore reflects task difficulty.
- **p. 8 / 5.2. Ablations and Analysis for Reset skills learning - extractive body cue:** The effective failure analysis provides highquality reset dataset for further demonstration collection.
- **p. 8 / 5.2. Ablations and Analysis for Reset skills learning - extractive body cue:** 5b, the robot must reset the coffee machine lid before adjusting the coffee pod pose; thus, the effective reset object is the lid.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. FLARE: Failure-Aware Resilience in VLA. Previous methods are brittle, failing from minor perturbations (ID errors) or catastrophic states (OOD errors), and do not ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. The overall framework of our method. We first collect the failure data with the VLA model trained with regular demonstrations. Then we perform ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Comparison of experimental results across 9 manipulation tasks in RoboMimic Simulation. The ‘D' suffix in the task names denotes the range of object ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Our method achieves state-of-the-art performance on 8 out of 9 tasks. On the remaining task, Threading D0, although we do not obtain the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Success rates of real-world manipulation tasks. Our method outperforms the baseline in two challenging settings. Real-World Task (40 trials) π0.5 (Baseline) Ours (FLARE) ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Real-world experimental setup and execution trajecto- ries. Top: The "Stack Three Blocks" task. Bottom: The "Insert U-shaped Block" task. Real-world Validation To verify ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. The sensitivity of two hyper-parameters, rotation r and translation t for perturbation & bridging. Our method achieves best performance when r = 30◦and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. The failure case for Coffee and ThreePieceAssembly respectively. (a) Reset coffee pod; (b) Reset coffee machine lid; (c) Reset the T-shaped block; (d) ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Real-world Validation To verify FLARE's effectiveness and address concerns about privileged simulation states, we conducted real-world experiments on a Piper arm with RealSense D435i ... | embodiment, simulator version and control stack | p. 7 (4. Experiment), p. 6 (4. Experiment) |
| Task/environment | The successor to the π0 VLA model [4], which demonstrates improved generalization by training on diverse, multi-environment datasets. | reset, timeout, object/scene variation | p. 6 (4. Experiment), p. 7 (4. Experiment) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 5 (3.4. Unified Training and Closed-Loop Inference), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 1. Our method achieves state-of-the-art performance on 8 out of 9 tasks. On the remaining task, Threading D0, although we do not obtain ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| The reduced success rate indicates room for further augmentation and model training, which could potentially enhance errorcorrection performance. | definition/direction/unit from same section | p. 8 (5.2. Ablations and Analysis for Reset skills learning) |
| Table 4. The reset skill success rate and demonstration generation efficiency on two manipulation tasks. The Reset Object 1 is coffee machine lid/T-shaped block, ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| In this case, our method still achieves comparable performance, even when multiple baselines (PhoenixHuman, π0.5) reach a 100% success rate. | definition/direction/unit from same section | p. 6 (4. Experiment) |
| Success rates of real-world manipulation tasks. | definition/direction/unit from same section | p. 7 (4. Experiment) |
| As illustrated, larger rotations and translations produce demonstrations with higher variance and therefore yield higher task success rates, but at the cost of reduced ... | definition/direction/unit from same section | p. 7 (5.1. Analysis of Perturbation & Bridging) |
| Figure 2. The overall framework of our method. We first collect the failure data with the VLA model trained with regular demonstrations. Then we ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 1. FLARE: Failure-Aware Resilience in VLA. Previous methods are brittle, failing from minor perturbations (ID errors) or catastrophic states (OOD errors), and do ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| More notably, our method even outperforms Phoenix-Human, demonstrating the comprehensive advantage of our framework over prior selfreflection approaches-even when compared to a baseline supplied ... | comparison identity and matched condition | p. 6 (4. Experiment) |
| Our method outperforms the baseline in two challenging settings. | comparison identity and matched condition | p. 7 (4. Experiment) |
| Table 1. Our method achieves state-of-the-art performance on 8 out of 9 tasks. On the remaining task, Threading D0, although we do not obtain ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| 4, our method consistently outperforms all baselines, including Phoenix and π0.5. | comparison identity and matched condition | p. 7 (5.1. Analysis of Perturbation & Bridging) |
| The performance comparison for our method and two variants, Ours w/o Reset and Ours-Oracle. | comparison identity and matched condition | p. 8 (5.2. Ablations and Analysis for Reset skills learning) |
| The retry/reset classification accuracy reaches 88% and 96% for the two tasks, demonstrating the strong video reasoning capabilities of state-of-the-art multimodal LLMs. | comparison identity and matched condition | p. 8 (5.2. Ablations and Analysis for Reset skills learning) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To assess the necessity of this component, we ablate the reset skill entirely and also evaluate a variant of our framework that replaces the ... | component/input/data sensitivity | p. 7 (5.2. Ablations and Analysis for Reset skills learning) |
| Table 3. The performance comparison for our method and two variants, Ours w/o Reset and Ours-Oracle. Ours w/o Reset only applies the perturbation & ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| We fine-tuned the language model and action expert of π0.5 [15] using LoRA [14], training with the Adam optimizer at a constant learning rate ... | component/input/data sensitivity | p. 6 (4. Experiment) |
| We attribute this to the decoupling effect of our perturbation-and-bridging strategy, which enhances the VLA model's robustness to environmental variations. | component/input/data sensitivity | p. 6 (4. Experiment) |
| The best performance is achieved when r = 30◦and t = 0.7 in 0 10 20 30 40 50 60 70 80 Rotation Angle ... | component/input/data sensitivity | p. 7 (5.1. Analysis of Perturbation & Bridging) |
| Task Reset/Retry Reset Object Timestamp Coffee 88% 88% 78% ThreePiece Assembly 96% 78% 66% components: retry/reset classification, reset-object identification, and timestamp identification. | component/input/data sensitivity | p. 8 (5.2. Ablations and Analysis for Reset skills learning) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To this end, we propose FLARE, a Failure-Aware Retry/Reset framework designed to transform brittle VLAs into resilient embodied agents (Fig. | Table 1. Our method achieves state-of-the-art performance on 8 out of 9 tasks. On the remaining task, Threading D0, although we do not obtain ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (Figure/Table caption), p. 6 (4. Experiment), p. 7 (5.1. Analysis of Perturbation & Bridging), p. 7 (Figure/Table caption), p. 8 (5.2. Ablations and Analysis for Reset skills learning), p. 8 (5.2. Ablations and Analysis for Reset skills learning) |
| Primary metric/result | In this case, our method still achieves comparable performance, even when multiple baselines (PhoenixHuman, π0.5) reach a 100% success rate. | numeric claim only at cited anchor | p. 6 (4. Experiment) |

- Numeric sentences retained from the body:
- **p. 6 / 4. Experiment - extractive body cue:** A LLaVAv1.5 is finetuned to predict subgoals at 5Hz, which are utilized as the condition for diffusion policy. • Motion-conditioned policy [39].
- **p. 6 / 4. Experiment - extractive body cue:** Our method achieves state-of-the-art performance on 8 out of 9 tasks.
- **p. 7 / 4. Experiment - extractive body cue:** Real-World Task (40 trials) π0.5 (Baseline) Ours (FLARE) Stack Three Blocks 62.5% 75.0% Insert U-shaped Block 45.0% 55.0% Figure 3.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 2. The overall framework of our method. We first collect the failure data with the VLA model trained with regular demonstrations. Then we ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | We presented FLARE, a failure-aware framework that endows VLA agents with robust autonomy through a dual Retry/Reset paradigm. | p. 8 (6. Conclusion) |
| body limitation/failure cue | While current hardware limits the correction of highly complex object poses, our findings confirm that treating failure recovery as a distinct, learned capability is ... | p. 8 (6. Conclusion) |
| body limitation/failure cue | Figure 1. FLARE: Failure-Aware Resilience in VLA. Previous methods are brittle, failing from minor perturbations (ID errors) or catastrophic states (OOD errors), and do ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Table 1. Comparison of experimental results across 9 manipulation tasks in RoboMimic Simulation. The ‘D' suffix in the task names denotes the range of ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | For "reset" skills, we used Gemini-2.5-Pro to analyze failure videos. | p. 6 (4. Experiment) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We fine-tuned the language model and action expert of π0.5 [15] using LoRA [14], training with the Adam optimizer at a constant learning rate ... | p. 6 (4. Experiment) |
| All results are averaged over 50 evaluation trials per task following [39]. | p. 6 (4. Experiment) |
| Real-World Task (40 trials) π0.5 (Baseline) Ours (FLARE) Stack Three Blocks 62.5% 75.0% Insert U-shaped Block 45.0% 55.0% Figure 3. | p. 7 (4. Experiment) |
| The Sensitivity of Hyper-Parameters In this section, we investigate two key hyperparameters in our perturbation & bridging augmentation strategy: the rotation r and the ... | p. 7 (5.1. Analysis of Perturbation & Bridging) |
| For timestamp identification, we compute accuracy by checking whether the identified frame corresponds to the correct reset object. | p. 8 (5.2. Ablations and Analysis for Reset skills learning) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. The overall framework of our method. We first collect the failure data with the VLA model trained with regular demonstrations. Then we perform ...
- **p. 8 / 6. Conclusion - extractive body cue:** We presented FLARE, a failure-aware framework that endows VLA agents with robust autonomy through a dual Retry/Reset paradigm.
- **p. 8 / 6. Conclusion - extractive body cue:** While current hardware limits the correction of highly complex object poses, our findings confirm that treating failure recovery as a distinct, learned capability is essential ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. FLARE: Failure-Aware Resilience in VLA. Previous methods are brittle, failing from minor perturbations (ID errors) or catastrophic states (OOD errors), and do not ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Comparison of experimental results across 9 manipulation tasks in RoboMimic Simulation. The ‘D' suffix in the task names denotes the range of object ...
- **p. 6 / 4. Experiment - extractive body cue:** For "reset" skills, we used Gemini-2.5-Pro to analyze failure videos.

- **Evidence anchors reviewed:** datasets p. 7 (4. Experiment), p. 6 (4. Experiment), p. 7 (4. Experiment), p. 6 (4. Experiment), p. 8 (5.2. Ablations and Analysis for Reset skills learning), p. 8 (5.2. Ablations and Analysis for Reset skills learning), metrics p. 6 (Figure/Table caption), p. 8 (5.2. Ablations and Analysis for Reset skills learning), p. 8 (Figure/Table caption), p. 6 (4. Experiment), p. 7 (4. Experiment), p. 7 (5.1. Analysis of Perturbation & Bridging), baselines p. 6 (4. Experiment), p. 7 (4. Experiment), p. 6 (Figure/Table caption), p. 7 (5.1. Analysis of Perturbation & Bridging), p. 8 (5.2. Ablations and Analysis for Reset skills learning), p. 8 (5.2. Ablations and Analysis for Reset skills learning), results p. 6 (Figure/Table caption), p. 6 (4. Experiment), p. 7 (5.1. Analysis of Perturbation & Bridging), p. 7 (Figure/Table caption), p. 8 (5.2. Ablations and Analysis for Reset skills learning), p. 8 (5.2. Ablations and Analysis for Reset skills learning).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Table 1. Comparison of experimental results across 9 manipulation tasks in RoboMimic Simulation. The ‘D' suffix in the task names denotes the range of object randomization in scene initialization. The ... (p. 6, Figure/Table caption).
- **Metric evidence:** In this case, our method still achieves comparable performance, even when multiple baselines (PhoenixHuman, π0.5) reach a 100% success rate. (p. 6, 4. Experiment).
- **Baseline/ablation evidence:** More notably, our method even outperforms Phoenix-Human, demonstrating the comprehensive advantage of our framework over prior selfreflection approaches-even when compared to a baseline supplied with correct human guidance. (p. 6, 4. Experiment).
- **Failure/negative evidence:** This leads to a critical failure: when a minor perturbation creates a state with a valid se t but a novel sr t, the policy incorrectly interprets this valid state ... (p. 3, 3.1. Problem Formulation).
