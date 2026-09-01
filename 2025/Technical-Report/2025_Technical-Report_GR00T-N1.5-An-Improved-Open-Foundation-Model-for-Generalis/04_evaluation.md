# Evaluation - GR00T N1.5: An Improved Open Foundation Model for Generalist Humanoid Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: official NVIDIA technical page body (no public PDF identified) checked on 2026-09-02 (1 source page(s); official NVIDIA technical page body (no public PDF identified); extraction quality: high); canonical paper source: https://research.nvidia.com/labs/gear/gr00t-n1_5/; body source: https://research.nvidia.com/labs/gear/gr00t-n1_5/. The note is an evidence-anchored official source body analysis; exact tables/equations or section details remain at the cited source anchors. Evidence boundary: selected official source body statements and source anchors were used; no PDF was identified at review time. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

official source body evaluation/result cue (p. 1 (Post-training on Unitree G1), p. 1 (Architecture validation)): It achieves higher success rate, can use more diverse data sources, and has significantly improved language following capabilities.

## Evaluation Body Digest

- **p. 1 / Architecture validation - extractive body cue:** In order to tune the model architecture for N1.5, we trained policies from scratch on two sim robot benchmarks requiring language following: Language Table and ...
- **p. 1 / Post-training on Unitree G1 - extractive body cue:** We post-train GR00T N1 and N1.5 on 1K teleoperation episodes collected on the Unitree G1 robot.
- **p. 1 / Generalization to novel behaviors using Neural Trajectories - extractive body cue:** We find that GR00T N1.5 achieved a 38.3% success rate across 12 DreamGen tasks, versus 13.1% for GR00T N1.
- **p. 1 / Post-training on Unitree G1 - extractive body cue:** It achieves higher success rate, can use more diverse data sources, and has significantly improved language following capabilities.
- **p. 1 / Architecture validation - extractive body cue:** We find that the N1.5 architecture achieves significantly higher success rates on both benchmarks, indicating stronger language-conditioned control ability.
- **p. 1 / Generalization to novel behaviors using Neural Trajectories - extractive body cue:** Although these new verbs can be considered "zero-shot" in the sense that we never collected teleoperation data for these tasks, we still train explicitly on ...
- **p. 1 / Model and Data Updates - extractive body cue:** The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** Experimental Results (p. 1).

## Experimental Matrix

| Body section | Type | official source body experiment/result cue | Anchor |
|---|---|---|---|
| Post-training on Unitree G1 | EMPIRICAL / SIMULATION | It achieves higher success rate, can use more diverse data sources, and has significantly improved language following capabilities. | p. 1 (Post-training on Unitree G1) |
| Architecture validation | EMPIRICAL / SIMULATION | We find that the N1.5 architecture achieves significantly higher success rates on both benchmarks, indicating stronger language-conditioned control ability. | p. 1 (Architecture validation) |

## Dataset / Benchmark Role

- **p. 1 / Architecture validation - extractive body cue:** In order to tune the model architecture for N1.5, we trained policies from scratch on two sim robot benchmarks requiring language following: Language Table and ...
- **p. 1 / Post-training on Unitree G1 - extractive body cue:** We post-train GR00T N1 and N1.5 on 1K teleoperation episodes collected on the Unitree G1 robot.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- figure/table caption cue 없음

## Embodiment / Environment

| Dimension | official source body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In order to tune the model architecture for N1.5, we trained policies from scratch on two sim robot benchmarks requiring language following: Language Table ... | embodiment, simulator version and control stack | p. 1 (Architecture validation), p. 1 (Post-training on Unitree G1) |
| Task/environment | We post-train GR00T N1 and N1.5 on 1K teleoperation episodes collected on the Unitree G1 robot. | reset, timeout, object/scene variation | p. 1 (Post-training on Unitree G1) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 1 (Model and Data Updates), p. 1 (GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | 본문 anchor 없음 |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We find that GR00T N1.5 achieved a 38.3% success rate across 12 DreamGen tasks, versus 13.1% for GR00T N1. | definition/direction/unit from same section | p. 1 (Generalization to novel behaviors using Neural Trajectories) |
| It achieves higher success rate, can use more diverse data sources, and has significantly improved language following capabilities. | definition/direction/unit from same section | p. 1 (Post-training on Unitree G1) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We expect users of N1.5 should observe better performance compared to N1, in particular improved generalization and better language following ability. | comparison identity and matched condition | p. 1 (GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots) |
| With several architecture, data and modeling improvements, we find that N1.5 outperforms N1 on both simulated manipulation benchmarks and on the real GR-1 robot, ... | comparison identity and matched condition | p. 1 (GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Distribution of training data in GR00T N1.5 pretraining. | component/input/data sensitivity | p. 1 (Joint Policy Learning and World Modeling Objective) |
| The VLM model is frozen during both pretraining and finetuning. | component/input/data sensitivity | p. 1 (Model and Data Updates) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce GR00T N1.5, an upgraded version of the GR00T N1 foundation model for humanoid robots. | It achieves higher success rate, can use more diverse data sources, and has significantly improved language following capabilities. | official source body cue; verify exact table/figure and matched conditions | p. 1 (Post-training on Unitree G1), p. 1 (Architecture validation) |
| Primary metric/result | We find that the N1.5 architecture achieves significantly higher success rates on both benchmarks, indicating stronger language-conditioned control ability. | numeric claim only at cited anchor | p. 1 (Architecture validation) |

- Numeric sentences retained from the body:
- **p. 1 / GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots - extractive body cue:** With several architecture, data and modeling improvements, we find that N1.5 outperforms N1 on both simulated manipulation benchmarks and on the real GR-1 robot, detailed ...
- **p. 1 / Architecture validation - extractive body cue:** In order to tune the model architecture for N1.5, we trained policies from scratch on two sim robot benchmarks requiring language following: Language Table and ...
- **p. 1 / Data-limited post-training in simulated environments - extractive body cue:** In the case of Sim GR-1, we can evaluate both fewshot and 0-shot, since the the pretraining mixture includes other Sim GR-1 tasks with the ...
- **p. 1 / Real GR-1 language following - extractive body cue:** We find that N1.5 significantly improves over N1 in terms of its ability to follow language commands on the real GR-1 robot.
- **p. 1 / Learning to manipulate novel objects from human ego videos - extractive body cue:** Demonstrations using a novel object, captured from a GoPro (left) and the GR-1 robot (right).
- **p. 1 / GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots - extractive body cue:** With several architecture, data and modeling improvements, we find that N1.5 outperforms N1 on both simulated manipulation benchmarks and on the real GR-1 robot, detailed ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Although these new verbs can be considered "zero-shot" in the sense that we never collected teleoperation data for these tasks, we still train explicitly ... | p. 1 (Generalization to novel behaviors using Neural Trajectories) |
| body limitation/failure cue | The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions. | p. 1 (Model and Data Updates) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We trained GR00T N1.5 for 250K steps on 1K H100 GPUs with global batch size 16384. | p. 1 (Joint Policy Learning and World Modeling Objective) |
| As in N1, we used AdamW with cosine learning rate schedule with warmup ratio 0.05. | p. 1 (Joint Policy Learning and World Modeling Objective) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 1 / Generalization to novel behaviors using Neural Trajectories - extractive body cue:** Although these new verbs can be considered "zero-shot" in the sense that we never collected teleoperation data for these tasks, we still train explicitly on ...
- **p. 1 / Model and Data Updates - extractive body cue:** The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions.

- **Evidence anchors reviewed:** datasets p. 1 (Architecture validation), p. 1 (Post-training on Unitree G1), metrics p. 1 (Generalization to novel behaviors using Neural Trajectories), p. 1 (Post-training on Unitree G1), baselines p. 1 (GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots), p. 1 (GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots), results p. 1 (Post-training on Unitree G1), p. 1 (Architecture validation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
