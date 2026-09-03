# Evaluation - ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p066.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p066.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (Figure/Table caption)): Fig. 10. Analysis of dataset size, waning horizon, and scion aorm on the performance of x. (a) Dataset Size: Mean Per Joint Position Eror (MPIPE) is evaluted for both in-distbution ...

## Evaluation Body Digest

- **p. 3 / 3) Extensive experiments in both simulation and real-world - extractive body cue:** This process ensures accurate motion retargeting and produces the cleuned robot trajectory dataset DG as shown in Figure 3 ().
- **p. 3 / 3) Extensive experiments in both simulation and real-world - extractive body cue:** ) Retargeting SMPL Motions to Robot Motions: With the cleaned dataset D&at in SMPL format, we retarget the motions into robot motions following the shape-and-motion ...
- **p. 3 / 3) Extensive experiments in both simulation and real-world - extractive body cue:** settings demonstrate that ASAP effectively reduces dyrnamies mismatch, enabling highly agile motions on robots and significantly reducing motion tracking errors.
- **p. 3 / 3) Extensive experiments in both simulation and real-world - extractive body cue:** b) Simulation-based Data Cleaning: Since the reconstruction process can introduce noise and errors [25], some estimated motions may not be physically feasible, making them unsuitable ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. The humanoid robot (Unite G1) demonstrates diver signature celebration ivolving a jump with & ISD-degree mid-air Kobe Bryan' famous fadeaway jump shot involving ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 10. Analysis of dataset size, waning horizon, and scion aorm on the performance of x. (a) Dataset Size: Mean Per Joint Position Eror (MPIPE) ...
- **p. 11 / C. Does ASAP Fine-Tuning Outperform Random Action Noise - extractive body cue:** Such structured discrepancies cannot be effectively captured by merely adding uniform action noise.
- **p. 12 / B. Offine and Online System Identification for Roboties - extractive body cue:** + Hardware Constraints: Agile whole-body motions exert significant stress on robots, leading to motor overheating, and hardware failure during data collection.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** 3) Extensive experiments in both simulation and real-world (p. 3).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Fig. 10. Analysis of dataset size, waning horizon, and scion aorm on the performance of x. (a) Dataset Size: Mean Per Joint Position Eror ... | p. 10 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 3 / 3) Extensive experiments in both simulation and real-world - extractive body cue:** This process ensures accurate motion retargeting and produces the cleuned robot trajectory dataset DG as shown in Figure 3 ().
- **p. 3 / 3) Extensive experiments in both simulation and real-world - extractive body cue:** ) Retargeting SMPL Motions to Robot Motions: With the cleaned dataset D&at in SMPL format, we retarget the motions into robot motions following the shape-and-motion ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. The humanoid robot (Unite G1) demonstrates diver signature celebration ivolving a jump with & ISD-degree mid-air Kobe Bryan' famous fadeaway jump shot involving ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 9. We deploy the pretrined policy of a forward jump motion tacking task, challenging the [Small Ualtee G1 rabot fora forward leap over Im,
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 10. Analysis of dataset size, waning horizon, and scion aorm on the performance of x. (a) Dataset Size: Mean Per Joint Position Eror (MPIPE) ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This process ensures accurate motion retargeting and produces the cleuned robot trajectory dataset DG as shown in Figure 3 (). | embodiment, simulator version and control stack | p. 3 (3) Extensive experiments in both simulation and real-world), p. 3 (3) Extensive experiments in both simulation and real-world) |
| Task/environment | ) Retargeting SMPL Motions to Robot Motions: With the cleaned dataset D&at in SMPL format, we retarget the motions into robot motions following the ... | reset, timeout, object/scene variation | p. 3 (3) Extensive experiments in both simulation and real-world) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 5 (B. Training Delta Action Model), p. 2 (Abstract) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 2 (Abstract), p. 3 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| settings demonstrate that ASAP effectively reduces dyrnamies mismatch, enabling highly agile motions on robots and significantly reducing motion tracking errors. | definition/direction/unit from same section | p. 3 (3) Extensive experiments in both simulation and real-world) |
| b) Simulation-based Data Cleaning: Since the reconstruction process can introduce noise and errors [25], some estimated motions may not be physically feasible, making them ... | definition/direction/unit from same section | p. 3 (3) Extensive experiments in both simulation and real-world) |
| Fig. 1. The humanoid robot (Unite G1) demonstrates diver signature celebration ivolving a jump with & ISD-degree mid-air Kobe Bryan' famous fadeaway jump shot ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 10. Analysis of dataset size, waning horizon, and scion aorm on the performance of x. (a) Dataset Size: Mean Per Joint Position Eror ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 10. Analysis of dataset size, waning horizon, and scion aorm on the performance of x. (a) Dataset Size: Mean Per Joint Position Eror ... | comparison identity and matched condition | p. 10 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 10. Analysis of dataset size, waning horizon, and scion aorm on the performance of x. (a) Dataset Size: Mean Per Joint Position Eror ... | component/input/data sensitivity | p. 10 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| mnparal- or result in overly conservative policies that sacrifice a yaper, we present ASAP | Fig. 10. Analysis of dataset size, waning horizon, and scion aorm on the performance of x. (a) Dataset Size: Mean Per Joint Position Eror ... | PDF body cue; verify exact table/figure and matched conditions | p. 10 (Figure/Table caption) |
| Primary metric/result | not separately recovered | numeric claim only at cited anchor | 본문 anchor 없음 |

- Numeric sentences retained from the body:
- **p. 5 / B. Training Delta Action Model - extractive body cue:** Team Weight Term Weight Pe ‘DoF position Hnits 10.0 Dab veloc mits 3.0 Torque limits 0.1 Temnination ~200.0 Repulariza ‘Adlon aie ---001 Action norm 02 ...
- **p. 10 / A. Key Factors in Training Delta Action Models - extractive body cue:** (b) Training Horizon: Opealoop MPIPE cheatmap) improves across evaluation poits as aining horizons increase, achieving the lowest eror at 15s.
- **p. 10 / A. Key Factors in Training Delta Action Models - extractive body cue:** However, closedloop MPIPE (red bam) shows sweet spot ata taining horizon of 10s, beyond which no further improvements are observed.
- **p. 10 / A. Key Factors in Training Delta Action Models - extractive body cue:** However, the improvement in closed-loop performance saturates, with a marginal decrease ‘of only 0.65% when scaling from 4300 to 43000 samples, suggesting limited additional benefit ...
- **p. 10 / A. Key Factors in Training Delta Action Models - extractive body cue:** As shown in Figure 10 (b), longer training horizons generally improve open-loop performance, with a horizon of 1.55 achieving the lowest errors across evaluation points ...
- **p. 10 / A. Key Factors in Training Delta Action Models - extractive body cue:** The best closed-loop results are observed at a training horizon of 110s, indicating that excessively long horizons do not provide additional benefits for fine-tuned policy.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Such structured discrepancies cannot be effectively captured by merely adding uniform action noise. | p. 11 (C. Does ASAP Fine-Tuning Outperform Random Action Noise) |
| body limitation/failure cue | + Hardware Constraints: Agile whole-body motions exert significant stress on robots, leading to motor overheating, and hardware failure during data collection. | p. 12 (B. Offine and Online System Identification for Roboties) |
| body limitation/failure cue | While ASAP demonstrates promising results in bridging the sim-to-real gap for agile humanoid control, our framework has several real-world limitations that highlights critical challenges ... | p. 12 (B. Offine and Online System Identification for Roboties) |
| body limitation/failure cue | However, the performance of the action noise approach (MPJPE of 150) does not match the precision achieved by ASAP (MPIPE of 126). | p. 11 (C. Does ASAP Fine-Tuning Outperform Random Action Noise) |
| body limitation/failure cue | However, this trend ‘does not consistently extend to closed-loop performance. | p. 10 (A. Key Factors in Training Delta Action Models) |
| body limitation/failure cue | b) Simulation-based Data Cleaning: Since the reconstruction process can introduce noise and errors [25], some estimated motions may not be physically feasible, making them ... | p. 3 (3) Extensive experiments in both simulation and real-world) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 4) To facilitate smooth transfer between simulators, we develop and open-source a multi-simulstor training and evaluation codebase for help accelerate further research. | p. 3 (3) Extensive experiments in both simulation and real-world) |
| 2) A reward signal is computed to minimize the diserepancy between the simulated state s,.1 and the recorded real-world state sf, with an additional ... | p. 5 (B. Training Delta Action Model) |
| 13, Visualization of saacGym-to-saacSim 7° ouput magnitde, We compute the average absolute value of each joit over the 4300-<pisode dataset. | p. 11 (0.038 Hip piten) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 11 / C. Does ASAP Fine-Tuning Outperform Random Action Noise - extractive body cue:** Such structured discrepancies cannot be effectively captured by merely adding uniform action noise.
- **p. 12 / B. Offine and Online System Identification for Roboties - extractive body cue:** + Hardware Constraints: Agile whole-body motions exert significant stress on robots, leading to motor overheating, and hardware failure during data collection.
- **p. 12 / B. Offine and Online System Identification for Roboties - extractive body cue:** While ASAP demonstrates promising results in bridging the sim-to-real gap for agile humanoid control, our framework has several real-world limitations that highlights critical challenges in ...
- **p. 11 / C. Does ASAP Fine-Tuning Outperform Random Action Noise - extractive body cue:** However, the performance of the action noise approach (MPJPE of 150) does not match the precision achieved by ASAP (MPIPE of 126).
- **p. 10 / A. Key Factors in Training Delta Action Models - extractive body cue:** However, this trend ‘does not consistently extend to closed-loop performance.
- **p. 3 / 3) Extensive experiments in both simulation and real-world - extractive body cue:** b) Simulation-based Data Cleaning: Since the reconstruction process can introduce noise and errors [25], some estimated motions may not be physically feasible, making them unsuitable ...

- **Evidence anchors reviewed:** datasets p. 3 (3) Extensive experiments in both simulation and real-world), p. 3 (3) Extensive experiments in both simulation and real-world), metrics p. 3 (3) Extensive experiments in both simulation and real-world), p. 3 (3) Extensive experiments in both simulation and real-world), p. 1 (Figure/Table caption), p. 10 (Figure/Table caption), baselines p. 10 (Figure/Table caption), results p. 10 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** This process ensures accurate motion retargeting and produces the cleuned robot trajectory dataset DG as shown in Figure 3 (). (p. 3, 3) Extensive experiments in both simulation and real-world).
- **Metric evidence:** settings demonstrate that ASAP effectively reduces dyrnamies mismatch, enabling highly agile motions on robots and significantly reducing motion tracking errors. (p. 3, 3) Extensive experiments in both simulation and real-world).
- **Baseline/ablation evidence:** Fig. 10. Analysis of dataset size, waning horizon, and scion aorm on the performance of x. (a) Dataset Size: Mean Per Joint Position Eror (MPIPE) is evaluted for both in-distbution ... (p. 10, Figure/Table caption).
- **Failure/negative evidence:** For instance, when imitating a jumping motion, the policy often fails early in training and learns 10 remain on the ground to avoid landing penalties. (p. 4, B. Phase-based Motion Tracking Policy Training).
