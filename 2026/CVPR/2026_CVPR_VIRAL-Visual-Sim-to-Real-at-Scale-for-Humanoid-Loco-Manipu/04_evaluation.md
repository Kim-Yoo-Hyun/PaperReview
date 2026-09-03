# Evaluation - VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/He_VIRAL_Visual_Sim-to-Real_at_Scale_for_Humanoid_Loco-Manipulation_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/He_VIRAL_Visual_Sim-to-Real_at_Scale_for_Humanoid_Loco-Manipulation_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (3.1. Robustness), p. 6 (Figure/Table caption), p. 5 (3. Real-World Results of VIRAL), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (Figure/Table caption)): These results show that although expert-level success remains challenging, VIRAL achieves near-expert success performance while being faster than the expert, and it substantially outperforms non-experts in both reliability and efficienc ...

## Evaluation Body Digest

- **p. 6 / 3.2. Generalization - extractive body cue:** We assess real-world generalization by systematically varying the environment along multiple factors, including tray start position, robot start pose, table height, lighting, table cloth, table ...
- **p. 6 / 3.1. Robustness - extractive body cue:** Real-world generalization of VIRAL RGB-based policy under variations in tray and object position, robot start pose, table height and type, tablecloth color, lighting, and object ...
- **p. 5 / 3. Real-World Results of VIRAL - extractive body cue:** In this section, we present real-world humanoid locomanipulation results achieved by VIRAL.
- **p. 5 / 3.1. Robustness - extractive body cue:** Across 59 consecutive real-world trials, VIRAL succeeds in 54, demonstrating strong reliability under extended deployment.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 14. Scaling compute for teacher training. Rewards (left) and success rates (right) for 1-16 GPUs. More GPUs yield faster convergence and better asymptotic performance.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 9. Ablations of teacher policy training. Training rewards (left) and success rates (right) for the full method (RSI + delta ac- tion), without demonstration ...
- **p. 6 / 3.1. Robustness - extractive body cue:** As shown in Figure 7, the expert attains a 100% success rate with a 21.4 s cycle time, slightly higher than the 20.2 s cycle ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 15. Scaling compute for student policy training. Distil- lation loss (left) and success rate (right) when training with 1-64 GPUs. Larger GPU counts provide ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** 3. Real-World Results of VIRAL (p. 5); 4. Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 3.1. Robustness | EMPIRICAL / REAL-ROBOT OR HARDWARE | These results show that although expert-level success remains challenging, VIRAL achieves near-expert success performance while being faster than the expert, and it substantially outperforms ... | p. 6 (3.1. Robustness) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 8. Real-world generalization of VIRAL RGB-based policy under variations in tray and object position, robot start pose, table height and type, tablecloth color, ... | p. 6 (Figure/Table caption) |
| 3. Real-World Results of VIRAL | EMPIRICAL / REAL-ROBOT OR HARDWARE | In this section, we present real-world humanoid locomanipulation results achieved by VIRAL. | p. 5 (3. Real-World Results of VIRAL) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 15. Scaling compute for student policy training. Distil- lation loss (left) and success rate (right) when training with 1-64 GPUs. Larger GPU counts ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 14. Scaling compute for teacher training. Rewards (left) and success rates (right) for 1-16 GPUs. More GPUs yield faster convergence and better asymptotic ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 3.2. Generalization - extractive body cue:** We assess real-world generalization by systematically varying the environment along multiple factors, including tray start position, robot start pose, table height, lighting, table cloth, table ...
- **p. 6 / 3.1. Robustness - extractive body cue:** Real-world generalization of VIRAL RGB-based policy under variations in tray and object position, robot start pose, table height and type, tablecloth color, lighting, and object ...
- **p. 5 / 3. Real-World Results of VIRAL - extractive body cue:** In this section, we present real-world humanoid locomanipulation results achieved by VIRAL.
- **p. 5 / 3.1. Robustness - extractive body cue:** Across 59 consecutive real-world trials, VIRAL succeeds in 54, demonstrating strong reliability under extended deployment.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Center: Unitree G1 humanoid performing loco-manipulation, walking between tables to place and pick objects for 54 loops with our RGB-based sim-to-real policy. Surrounding: ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. VIRAL teacher-student pipeline. Phase 1: In simulation, a privileged RL teacher policy ωteacher receives full-state proprioception and exteroception of the task information and ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Visual randomization on image, lighting, material, and camera-extrinsics randomization for sim-to-real robustness. Reference State Initialization
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. Frames of reference state initialization for teacher RL. skills for high-DoF humanoids with RL typically demands heavy reward engineering still often yields suboptimal ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. System identification of the dexterous hand. Real-sim overlays (top) and joint position trajectories (bottom) before and after SysID, showing markedly improved alignment. Real ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 6. Real-to-sim camera extrinsics alignment. Real view versus simulated views before and after alignment. Sim-to-Real Element #2: FOV Alignment and Random- ization. We match ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 7. Real-world performance comparison: VIRAL matches expert-level reliability, outperforms non-experts, and op- erates faster than the expert teleoperator. ure 3) to ensure that the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 8. Real-world generalization of VIRAL RGB-based policy under variations in tray and object position, robot start pose, table height and type, tablecloth color, lighting, ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We assess real-world generalization by systematically varying the environment along multiple factors, including tray start position, robot start pose, table height, lighting, table cloth, ... | embodiment, simulator version and control stack | p. 6 (3.2. Generalization), p. 6 (3.1. Robustness) |
| Task/environment | Real-world generalization of VIRAL RGB-based policy under variations in tray and object position, robot start pose, table height and type, tablecloth color, lighting, and ... | reset, timeout, object/scene variation | p. 6 (3.1. Robustness), p. 5 (3. Real-World Results of VIRAL) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 3 (2.1. Key Elements of Teacher Training) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 2 (1. Introduction), p. 3 (2.1. Key Elements of Teacher Training) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 14. Scaling compute for teacher training. Rewards (left) and success rates (right) for 1-16 GPUs. More GPUs yield faster convergence and better asymptotic ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 9. Ablations of teacher policy training. Training rewards (left) and success rates (right) for the full method (RSI + delta ac- tion), without ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| As shown in Figure 7, the expert attains a 100% success rate with a 21.4 s cycle time, slightly higher than the 20.2 s ... | definition/direction/unit from same section | p. 6 (3.1. Robustness) |
| Figure 15. Scaling compute for student policy training. Distil- lation loss (left) and success rate (right) when training with 1-64 GPUs. Larger GPU counts ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 4. Frames of reference state initialization for teacher RL. skills for high-DoF humanoids with RL typically demands heavy reward engineering still often yields ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| We evaluate the robustness of the learned student policy on a continuous loco-manipulation task in which the humanoid repeatedly walks between two tables, places ... | definition/direction/unit from same section | p. 5 (3.1. Robustness) |
| Figure 7. Real-world performance comparison: VIRAL matches expert-level reliability, outperforms non-experts, and op- erates faster than the expert teleoperator. ure 3) to ensure that ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Figure 3. Visual randomization on image, lighting, material, and camera-extrinsics randomization for sim-to-real robustness. Reference State Initialization | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| These results show that although expert-level success remains challenging, VIRAL achieves near-expert success performance while being faster than the expert, and it substantially outperforms ... | comparison identity and matched condition | p. 6 (3.1. Robustness) |
| Figure 7. Real-world performance comparison: VIRAL matches expert-level reliability, outperforms non-experts, and op- erates faster than the expert teleoperator. ure 3) to ensure that ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Across these variations, VIRAL consistently completes the task without additional tuning, indicating strong robustness. | comparison identity and matched condition | p. 6 (3.2. Generalization) |
| Figure 2. VIRAL teacher-student pipeline. Phase 1: In simulation, a privileged RL teacher policy ωteacher receives full-state proprioception and exteroception of the task information ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| Figure 10. Ablation of vision backbone for student policy. | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 11. Ablation of ratio of DAgger/BC of student policy. | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 9. Ablations of teacher policy training. Training rewards (left) and success rates (right) for the full method (RSI + delta ac- tion), without ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Figure 2. VIRAL teacher-student pipeline. Phase 1: In simulation, a privileged RL teacher policy ωteacher receives full-state proprioception and exteroception of the task information ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| Across these variations, VIRAL consistently completes the task without additional tuning, indicating strong robustness. | component/input/data sensitivity | p. 6 (3.2. Generalization) |
| Figure 10. Ablation of vision backbone for student policy. | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Figure 11. Ablation of ratio of DAgger/BC of student policy. | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Figure 16. Ablation of object generalization of teacher policy. | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Proprioception consists of oprop-priv t = [vt, ωt, gt, at→1, qt, ˙qt, f finger t ] where vt, ωt are base linear and angular ... | These results show that although expert-level success remains challenging, VIRAL achieves near-expert success performance while being faster than the expert, and it substantially outperforms ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (3.1. Robustness), p. 6 (Figure/Table caption), p. 5 (3. Real-World Results of VIRAL), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (Figure/Table caption) |
| Primary metric/result | Figure 8. Real-world generalization of VIRAL RGB-based policy under variations in tray and object position, robot start pose, table height and type, tablecloth color, ... | numeric claim only at cited anchor | p. 6 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 3. Real-World Results of VIRAL - extractive body cue:** Perception is provided by an Intel RealSense D435i, and all policy inference is performed on a desktop workstation with an Intel i9-14900K CPU and an ...
- **p. 5 / 3.1. Robustness - extractive body cue:** We also compare VIRAL with two human teleoperators: an expert with over 1000 hours of G1 teleoperation experience and a non-expert teleoperator with approximately one ...
- **p. 6 / 3.1. Robustness - extractive body cue:** As shown in Figure 7, the expert attains a 100% success rate with a 21.4 s cycle time, slightly higher than the 20.2 s cycle ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Note that VIRAL framework does not have designs overfitting to specific WBC policy, and can be extended to other humanoid WBC controllers [44, 78]. | p. 3 (2.1. Key Elements of Teacher Training) |
| body limitation/failure cue | With a stable and robust WBC policy as an API layer, the action space of VIRAL policy is limited to a safe and reliable ... | p. 3 (2.1. Key Elements of Teacher Training) |
| body limitation/failure cue | Visual randomization on image, lighting, material, and camera-extrinsics randomization for sim-to-real robustness. | p. 4 (2.1. Key Elements of Teacher Training) |
| body limitation/failure cue | The distinction between DAgger and BC lies solely in the source of observations: teacher rollouts provide clean, near-optimal demonstrations that rapidly imprint strong priors ... | p. 4 (2.2. Key Elements of Student Training) |
| body limitation/failure cue | To enhance robustness and improve sim-toreal transfer, we apply extensive visual and physical randomization during training (Figure 3). | p. 5 (2.3. Key Elements of Sim-to-Real Transfer) |
| body limitation/failure cue | We randomize image quality (brightness, contrast, hue, saturation, Gaussian noise, and blur), camera extrinsics to account for small pose shifts, and camera latency to ... | p. 5 (2.3. Key Elements of Sim-to-Real Transfer) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| This implementation preserves the simplicity of single-GPU training while enabling near-linear scaling to large clusters for high-throughput visual sim-to-real learning. | p. 5 (2.2. Key Elements of Student Training) |
| To scale up visual simulation training throughput, we implement a customized version of TRL [68] with support of Accelerate [22] for efficient scaling across ... | p. 5 (2.2. Key Elements of Student Training) |
| The teacher is trained with PPO [59] with a custom implementation of TRL [68] to train across GPUs in a distributed manner. | p. 3 (2.1. Key Elements of Teacher Training) |
| For the student's vision backbone, we adopt a state-of-the-art image encoder [61] to extract high-quality RGB features, which are fused with proprioceptive to the ... | p. 4 (2.2. Key Elements of Student Training) |
| The resulting student observation ostudent therefore integrates both visual embeddings and the proprioception available on real hardware, enabling the policy to reason over rich ... | p. 4 (2.2. Key Elements of Student Training) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / 2.1. Key Elements of Teacher Training - extractive body cue:** Note that VIRAL framework does not have designs overfitting to specific WBC policy, and can be extended to other humanoid WBC controllers [44, 78].
- **p. 3 / 2.1. Key Elements of Teacher Training - extractive body cue:** With a stable and robust WBC policy as an API layer, the action space of VIRAL policy is limited to a safe and reliable region ...
- **p. 4 / 2.1. Key Elements of Teacher Training - extractive body cue:** Visual randomization on image, lighting, material, and camera-extrinsics randomization for sim-to-real robustness.
- **p. 4 / 2.2. Key Elements of Student Training - extractive body cue:** The distinction between DAgger and BC lies solely in the source of observations: teacher rollouts provide clean, near-optimal demonstrations that rapidly imprint strong priors on ...
- **p. 5 / 2.3. Key Elements of Sim-to-Real Transfer - extractive body cue:** To enhance robustness and improve sim-toreal transfer, we apply extensive visual and physical randomization during training (Figure 3).
- **p. 5 / 2.3. Key Elements of Sim-to-Real Transfer - extractive body cue:** We randomize image quality (brightness, contrast, hue, saturation, Gaussian noise, and blur), camera extrinsics to account for small pose shifts, and camera latency to model ...

- **Evidence anchors reviewed:** datasets p. 6 (3.2. Generalization), p. 6 (3.1. Robustness), p. 5 (3. Real-World Results of VIRAL), p. 5 (3.1. Robustness), metrics p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 6 (3.1. Robustness), p. 8 (Figure/Table caption), p. 4 (Figure/Table caption), p. 5 (3.1. Robustness), baselines p. 6 (3.1. Robustness), p. 5 (Figure/Table caption), p. 6 (3.2. Generalization), p. 2 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), results p. 6 (3.1. Robustness), p. 6 (Figure/Table caption), p. 5 (3. Real-World Results of VIRAL), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 8. Real-world generalization of VIRAL RGB-based policy under variations in tray and object position, robot start pose, table height and type, tablecloth color, lighting, and object category. Videos are ... (p. 6, Figure/Table caption).
- **Metric evidence:** As shown in Figure 7, the expert attains a 100% success rate with a 21.4 s cycle time, slightly higher than the 20.2 s cycle time of VIRAL. (p. 6, 3.1. Robustness).
- **Baseline/ablation evidence:** Across these variations, VIRAL consistently completes the task without additional tuning, indicating strong robustness. (p. 6, 3.2. Generalization).
- **Failure/negative evidence:** We find that compute scale is critical: scaling simulation to tens of GPUs (up to 64) makes both teacher and student training reliable, while low-compute regimes often fail. (p. 1, Abstract).
