# Evaluation - Hold My Beer: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=Bl2VfU9NhF; PDF retrieval source: https://arxiv.org/pdf/2505.24198. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), p. 15 (Figure/Table caption), p. 16 (Figure/Table caption), p. 17 (A.2 More Analysis on Frequency Ablation)): Figure 5: Top: Humanoid carring bottle of water without spillage during tepping. Bottom: Hu- manoid disturbance rejection with EE stability. ping are insufficient for tasks requiring precise EE stability. While ...

## Evaluation Body Digest

- **p. 17 / A.2 More Analysis on Frequency Ablation - extractive body cue:** Across both simulation and real-world environments, our experiments show that a 50 Hz lower-body control frequency consistently achieves stable locomotion, regardless of the upper-body control ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of the SoFTA framework: The framework employs two distinct agents that share the same observation but act within separate action spaces at ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Top: Humanoid carring bottle of water without spillage during tepping. Bottom: Hu- manoid disturbance rejection with EE stability. ping are insufficient for tasks ...
- **p. 16 / Figure/Table caption - extractive body cue:** Table 6: Domain randomization parameters used during training. Rewards Design We show the grouped SoFTA task reward components in Table 8. Notice that the termination ...
- **p. 15 / Figure/Table caption - extractive body cue:** Table 4: Comparison of actor and critic observations with scaling factors. Privileged observations used only by the critic are shaded and marked in red. During ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Reward Curves of EE-term and locomotion-term during Training. Benefit from Two-Agent Reward Group Sepa
- **p. 17 / Figure/Table caption - extractive body cue:** Table 7: Reward terms categorized by body group, including task rewards and penalties with corre- sponding expressions and weights. C means the contact sequence. Hat ...
- **p. 18 / A.2 More Analysis on Frequency Ablation - extractive body cue:** We observe that increasing the upper-body control frequency reduces recovery time (defined as the time when the error first falls below 1 e of its ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5: Top: Humanoid carring bottle of water without spillage during tepping. Bottom: Hu- manoid disturbance rejection with EE stability. ping are insufficient for ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1: Simulation Results: EE stability is evaluated in Isaac Gym across various tasks. SoFTA consistently outperforms the baselines in most metrics, demonstrating superior ... | p. 5 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2: Real-World Results: EE stability evaluated in Real World across diverse task settings. SoFTA consistently outperforms baselines, especially in Acc-Z metric. Jointly Learn ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 4: Comparison of actor and critic observations with scaling factors. Privileged observations used only by the critic are shaded and marked in red. ... | p. 15 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 6: Domain randomization parameters used during training. Rewards Design We show the grouped SoFTA task reward components in Table 8. Notice that the ... | p. 16 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 17 / A.2 More Analysis on Frequency Ablation - extractive body cue:** Across both simulation and real-world environments, our experiments show that a 50 Hz lower-body control frequency consistently achieves stable locomotion, regardless of the upper-body control ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control with SoFTA: (A) Carrying bottles of drink during a 1m/s large-step walk. (B) Liquid surface ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of the SoFTA framework: The framework employs two distinct agents that share the same observation but act within separate action spaces at ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1: Simulation Results: EE stability is evaluated in Isaac Gym across various tasks. SoFTA consistently outperforms the baselines in most metrics, demonstrating superior EE ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2: Real-World Results: EE stability evaluated in Real World across diverse task settings. SoFTA consistently outperforms baselines, especially in Acc-Z metric. Jointly Learn Locomotion ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Reward Curves of EE-term and locomotion-term during Training. Benefit from Two-Agent Reward Group Sepa
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Emergent Compensation Behavior. 4.2 Real-World Results To answer Q2 (What capabilities does SoFTA enable in real world?), we assess EE stability in three ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Top: Humanoid carring bottle of water without spillage during tepping. Bottom: Hu- manoid disturbance rejection with EE stability. ping are insufficient for tasks ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6: Humanoid as Camera Stabilizer to record videos. Case 2: Humanoid as Camera Stabilizer. Figure 6 shows video footage recorded by the robot during ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Across both simulation and real-world environments, our experiments show that a 50 Hz lower-body control frequency consistently achieves stable locomotion, regardless of the upper-body ... | embodiment, simulator version and control stack | p. 17 (A.2 More Analysis on Frequency Ablation) |
| Task/environment | not recovered | reset, timeout, object/scene variation | 본문 anchor 없음 |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 15 (A.1 Training Details), p. 15 (A.1 Training Details) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 17 (A.1 Training Details), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 2: Overview of the SoFTA framework: The framework employs two distinct agents that share the same observation but act within separate action spaces ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 5: Top: Humanoid carring bottle of water without spillage during tepping. Bottom: Hu- manoid disturbance rejection with EE stability. ping are insufficient for ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 6: Domain randomization parameters used during training. Rewards Design We show the grouped SoFTA task reward components in Table 8. Notice that the ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| Table 9: Response time and maximum error magnitudes under different upper-body frequencies. Across both simulation and real-world environments, our experiments show that a 50 ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| Table 4: Comparison of actor and critic observations with scaling factors. Privileged observations used only by the critic are shaded and marked in red. ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| Figure 3: Reward Curves of EE-term and locomotion-term during Training. Benefit from Two-Agent Reward Group Sepa | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 7: Reward terms categorized by body group, including task rewards and penalties with corre- sponding expressions and weights. C means the contact sequence. ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| We observe that increasing the upper-body control frequency reduces recovery time (defined as the time when the error first falls below 1 e of ... | definition/direction/unit from same section | p. 18 (A.2 More Analysis on Frequency Ablation) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 1: Simulation Results: EE stability is evaluated in Isaac Gym across various tasks. SoFTA consistently outperforms the baselines in most metrics, demonstrating superior ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Table 2: Real-World Results: EE stability evaluated in Real World across diverse task settings. SoFTA consistently outperforms baselines, especially in Acc-Z metric. Jointly Learn ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Figure 5: Top: Humanoid carring bottle of water without spillage during tepping. Bottom: Hu- manoid disturbance rejection with EE stability. ping are insufficient for ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 1: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control with SoFTA: (A) Carrying bottles of drink during a 1m/s large-step walk. (B) Liquid ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Figure 6: Humanoid as Camera Stabilizer to record videos. Case 2: Humanoid as Camera Stabilizer. Figure 6 shows video footage recorded by the robot ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 4: Comparison of actor and critic observations with scaling factors. Privileged observations used only by the critic are shaded and marked in red. ... | comparison identity and matched condition | p. 15 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 1: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control with SoFTA: (A) Carrying bottles of drink during a 1m/s large-step walk. (B) Liquid ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| 0.00 0.02 0.04 0.06 0.08 0.10 Time(s) 0.4 0.2 0.0 0.2 0.4 Joint shoulder_pitch Target Pos Upper-body 50 Hz Upper-body 100 Hz Base Vel(0.3m/s) ... | component/input/data sensitivity | p. 18 (A.2 More Analysis on Frequency Ablation) |
| Figure 2: Overview of the SoFTA framework: The framework employs two distinct agents that share the same observation but act within separate action spaces ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Figure 6: Humanoid as Camera Stabilizer to record videos. Case 2: Humanoid as Camera Stabilizer. Figure 6 shows video footage recorded by the robot ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Figure 5: Top: Humanoid carring bottle of water without spillage during tepping. Bottom: Hu- manoid disturbance rejection with EE stability. ping are insufficient for ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Table 8: PPO Multi-Actor-Critic Training Configuration A.2 More Analysis on Frequency Ablation Methods Response Time (s) ↓ Max Acc (m/s2) ↓ Max Vel (m/s) ... | component/input/data sensitivity | p. 17 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our key contributions are: • We introduce SoFTA, a novel slow-fast two-agent RL framework that decouples control for locomotion and EE stabilization in both ... | Figure 5: Top: Humanoid carring bottle of water without spillage during tepping. Bottom: Hu- manoid disturbance rejection with EE stability. ping are insufficient for ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), p. 15 (Figure/Table caption), p. 16 (Figure/Table caption), p. 17 (A.2 More Analysis on Frequency Ablation) |
| Primary metric/result | Table 1: Simulation Results: EE stability is evaluated in Isaac Gym across various tasks. SoFTA consistently outperforms the baselines in most metrics, demonstrating superior ... | numeric claim only at cited anchor | p. 5 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 17 / A.2 More Analysis on Frequency Ablation - extractive body cue:** Across both simulation and real-world environments, our experiments show that a 50 Hz lower-body control frequency consistently achieves stable locomotion, regardless of the upper-body control ...
- **p. 18 / A.2 More Analysis on Frequency Ablation - extractive body cue:** As shown in Figure 9 (top), higher-frequency policies (100 Hz) react faster to base motion changes and recover balance quicker.
- **p. 18 / A.2 More Analysis on Frequency Ablation - extractive body cue:** 0.00 0.02 0.04 0.06 0.08 0.10 Time(s) 0.4 0.2 0.0 0.2 0.4 Joint shoulder_pitch Target Pos Upper-body 50 Hz Upper-body 100 Hz Base Vel(0.3m/s) 0.00 ...
- **p. 16 / A.1 Training Details - extractive body cue:** Component Range / Value command lin vel x: U (-1, 1) m/s y: U (-1, 1) m/s command ang vel U (-1, 1) rad/s command ...
- **p. 16 / A.1 Training Details - extractive body cue:** The factor scurrent starts at 0.5 and is adjusted dynamically-multiplied by 0.9999 when episode length is under 0.4s, and by 1.0001 when it exceeds 2.1s, ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 7: Max Acc under Different Control Frequencies in Simulation and Real World: Higher values reflect reduced stability. N/A indicates unstable or failed trials ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | 6 Limitation Despite its strong performance, SoFTA still faces several limitations. | p. 9 (5 Conclusion) |
| body limitation/failure cue | First, while it significantly reduces EE acceleration, the achieved stability still falls short of human-level performance. | p. 9 (5 Conclusion) |
| body limitation/failure cue | We observe that increasing the upper-body control frequency reduces recovery time (defined as the time when the error first falls below 1 e of ... | p. 18 (A.2 More Analysis on Frequency Ablation) |
| body limitation/failure cue | Figure 5: Top: Humanoid carring bottle of water without spillage during tepping. Bottom: Hu- manoid disturbance rejection with EE stability. ping are insufficient for ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Figure 4: Emergent Compensation Behavior. 4.2 Real-World Results To answer Q2 (What capabilities does SoFTA enable in real world?), we assess EE stability in ... | p. 6 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Parameter Value General PPO Settings Gamma (γ) 0.99 GAE Lambda (λ) 0.95 Value Loss Coef 1.0 Entropy Coef 0.01 Actor Learning Rate 1 × ... | p. 17 (A.1 Training Details) |
| From this gait period, we compute 15 | p. 15 (A.1 Training Details) |
| Observations are stacked over five timesteps to provide short-term temporal context. | p. 15 (A.1 Training Details) |
| In implementation, we set λacc = 0.25, λacc = 0.0044. | p. 17 (A.1 Training Details) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7: Max Acc under Different Control Frequencies in Simulation and Real World: Higher values reflect reduced stability. N/A indicates unstable or failed trials in ...
- **p. 9 / 5 Conclusion - extractive body cue:** 6 Limitation Despite its strong performance, SoFTA still faces several limitations.
- **p. 9 / 5 Conclusion - extractive body cue:** First, while it significantly reduces EE acceleration, the achieved stability still falls short of human-level performance.
- **p. 18 / A.2 More Analysis on Frequency Ablation - extractive body cue:** We observe that increasing the upper-body control frequency reduces recovery time (defined as the time when the error first falls below 1 e of its ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Top: Humanoid carring bottle of water without spillage during tepping. Bottom: Hu- manoid disturbance rejection with EE stability. ping are insufficient for tasks ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Emergent Compensation Behavior. 4.2 Real-World Results To answer Q2 (What capabilities does SoFTA enable in real world?), we assess EE stability in three ...

- **Evidence anchors reviewed:** datasets p. 17 (A.2 More Analysis on Frequency Ablation), metrics p. 4 (Figure/Table caption), p. 7 (Figure/Table caption), p. 16 (Figure/Table caption), p. 17 (Figure/Table caption), p. 15 (Figure/Table caption), p. 6 (Figure/Table caption), baselines p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (Figure/Table caption), p. 7 (Figure/Table caption), p. 15 (Figure/Table caption), results p. 7 (Figure/Table caption), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), p. 15 (Figure/Table caption), p. 16 (Figure/Table caption), p. 17 (A.2 More Analysis on Frequency Ablation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
