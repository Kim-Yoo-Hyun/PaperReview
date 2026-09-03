# Evaluation - GR00T N1.5: An Improved Open Foundation Model for Generalist Humanoid Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (3 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://research.nvidia.com/labs/gear/gr00t-n1_5/; PDF retrieval source: https://research.nvidia.com/labs/gear/gr00t-n1_5/. PDF provenance note: official NVIDIA technical page rendered to a task-scoped PDF snapshot; no author-supplied publication PDF identified. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 3 (Discussion), p. 2 (Architecture validation), p. 2 (Real GR-1 language following), p. 3 (Generalization to novel behaviors using Neural Trajectories), p. 1 (Introduction), p. 1 (Architecture)): It achieves higher success rate, can use more diverse data sources, and has significantly improved language following capabilities.

## Evaluation Body Digest

- **p. 1 / Introduction - extractive body cue:** With several architecture, data and modeling improvements, we find that N1.5 outperforms N1 on both simulated manipulation benchmarks and on the real GR-1 robot, detailed ...
- **p. 3 / Post-training on Unitree G1 - extractive body cue:** We post-train GR00T N1 and N1.5 on 1K teleoperation episodes collected on the Unitree G1 robot.
- **p. 2 / Learning to manipulate novel objects from human ego videos - extractive body cue:** Demonstrations using a novel object, captured from a GoPro (left) and the GR-1 robot (right).
- **p. 2 / Learning to manipulate novel objects from human ego videos - extractive body cue:** This allows learning to manipulate novel objects from human videos and minimal robot demonstrations.
- **p. 3 / Post-training on Unitree G1 - extractive body cue:** Model / GR00T N1, 1K Demos / GR00T N1.5, 1K Demos / GR00T N1.5, 1K Demos Task / Place 1 of 2 fruits onto plate; ...
- **p. 1 / Introduction - extractive body cue:** We introduce GR00T N1.5, an upgraded version of the GR00T N1 foundation model for humanoid robots.
- **p. 2 / Architecture validation - extractive body cue:** We find that the N1.5 architecture achieves significantly higher success rates on both benchmarks, indicating stronger language-conditioned control ability.
- **p. 2 / Real GR-1 language following - extractive body cue:** Although both policies consistently pick and place some fruit onto the plate, N1.5 has a much higher language following rate, leading to a higher overall ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** Experimental Results (p. 1).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Discussion | EMPIRICAL / SIMULATION | It achieves higher success rate, can use more diverse data sources, and has significantly improved language following capabilities. | p. 3 (Discussion) |
| Architecture validation | EMPIRICAL / SIMULATION | We find that the N1.5 architecture achieves significantly higher success rates on both benchmarks, indicating stronger language-conditioned control ability. | p. 2 (Architecture validation) |
| Real GR-1 language following | EMPIRICAL / SIMULATION | Setting / GR00T N1 / GR00T N1.5 Language following rate / 46.6% / 93.3% Overall success rate / 43.3% / 83.0% We find that ... | p. 2 (Real GR-1 language following) |
| Generalization to novel behaviors using Neural Trajectories | EMPIRICAL / SIMULATION | We find that GR00T N1.5 achieved a 38.3% success rate across 12 DreamGen tasks, versus 13.1% for GR00T N1. | p. 3 (Generalization to novel behaviors using Neural Trajectories) |
| Introduction | EMPIRICAL / SIMULATION | With several architecture, data and modeling improvements, we find that N1.5 outperforms N1 on both simulated manipulation benchmarks and on the real GR-1 robot, ... | p. 1 (Introduction) |

## Dataset / Benchmark Role

- **p. 1 / Introduction - extractive body cue:** With several architecture, data and modeling improvements, we find that N1.5 outperforms N1 on both simulated manipulation benchmarks and on the real GR-1 robot, detailed ...
- **p. 3 / Post-training on Unitree G1 - extractive body cue:** We post-train GR00T N1 and N1.5 on 1K teleoperation episodes collected on the Unitree G1 robot.
- **p. 2 / Learning to manipulate novel objects from human ego videos - extractive body cue:** Demonstrations using a novel object, captured from a GoPro (left) and the GR-1 robot (right).
- **p. 2 / Learning to manipulate novel objects from human ego videos - extractive body cue:** This allows learning to manipulate novel objects from human videos and minimal robot demonstrations.
- **p. 3 / Post-training on Unitree G1 - extractive body cue:** Model / GR00T N1, 1K Demos / GR00T N1.5, 1K Demos / GR00T N1.5, 1K Demos Task / Place 1 of 2 fruits onto plate; ...
- **p. 1 / Introduction - extractive body cue:** We introduce GR00T N1.5, an upgraded version of the GR00T N1 foundation model for humanoid robots.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- figure/table caption cue 없음

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | With several architecture, data and modeling improvements, we find that N1.5 outperforms N1 on both simulated manipulation benchmarks and on the real GR-1 robot, ... | embodiment, simulator version and control stack | p. 1 (Introduction), p. 3 (Post-training on Unitree G1) |
| Task/environment | We post-train GR00T N1 and N1.5 on 1K teleoperation episodes collected on the Unitree G1 robot. | reset, timeout, object/scene variation | p. 3 (Post-training on Unitree G1), p. 2 (Learning to manipulate novel objects from human ego videos) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 1 (Architecture), p. 1 (Architecture) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 2 (Real GR-1 language following), p. 2 (Learning to manipulate novel objects from human ego videos) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We find that the N1.5 architecture achieves significantly higher success rates on both benchmarks, indicating stronger language-conditioned control ability. | definition/direction/unit from same section | p. 2 (Architecture validation) |
| Although both policies consistently pick and place some fruit onto the plate, N1.5 has a much higher language following rate, leading to a higher ... | definition/direction/unit from same section | p. 2 (Real GR-1 language following) |
| We find that GR00T N1.5 achieved a 38.3% success rate across 12 DreamGen tasks, versus 13.1% for GR00T N1. | definition/direction/unit from same section | p. 3 (Generalization to novel behaviors using Neural Trajectories) |
| It achieves higher success rate, can use more diverse data sources, and has significantly improved language following capabilities. | definition/direction/unit from same section | p. 3 (Discussion) |
| Model / Size / GR-1 grounding IoU (â†‘) / RefCOCOg-val IoU (â†‘) Qwen2.5VL / 3B / 35.5 / 85.2 Left: Example annotations from our ... | definition/direction/unit from same section | p. 1 (Architecture) |
| We used FLARE loss coefficient 0.2 for both pretraining and posttraining. | definition/direction/unit from same section | p. 1 (Architecture) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We expect users of N1.5 should observe better performance compared to N1, in particular improved generalization and better language following ability. | comparison identity and matched condition | p. 1 (Introduction) |
| With several architecture, data and modeling improvements, we find that N1.5 outperforms N1 on both simulated manipulation benchmarks and on the real GR-1 robot, ... | comparison identity and matched condition | p. 1 (Introduction) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We used FLARE loss coefficient 0.2 for both pretraining and posttraining. | component/input/data sensitivity | p. 1 (Architecture) |
| Our pretraining mixture included internal GR-1 data, OpenXE, simulated GR-1 (a.k.a. | component/input/data sensitivity | p. 1 (Architecture) |
| GR00T N1 showed only weak generalization to new verbs, only repeating the tasks contained in pretraining | component/input/data sensitivity | p. 2 (Generalization to novel behaviors using Neural Trajectories) |
| To evaluate the model's generalization ability, we evaluate pick and place performance using a set of 10 novel objects not seen during pretraining. | component/input/data sensitivity | p. 2 (Learning to manipulate novel objects from human ego videos) |
| We observe that the post-trained GR00T N1.5 achieves much higher success rate than N1 for previously seen objects (toy fruits seen in the GR-1 ... | component/input/data sensitivity | p. 3 (Post-training on Unitree G1) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce GR00T N1.5, an upgraded version of the GR00T N1 foundation model for humanoid robots. | It achieves higher success rate, can use more diverse data sources, and has significantly improved language following capabilities. | PDF body cue; verify exact table/figure and matched conditions | p. 3 (Discussion), p. 2 (Architecture validation), p. 2 (Real GR-1 language following), p. 3 (Generalization to novel behaviors using Neural Trajectories), p. 1 (Introduction), p. 1 (Architecture) |
| Primary metric/result | We find that the N1.5 architecture achieves significantly higher success rates on both benchmarks, indicating stronger language-conditioned control ability. | numeric claim only at cited anchor | p. 2 (Architecture validation) |

- Numeric sentences retained from the body:
- **p. 1 / Introduction - extractive body cue:** With several architecture, data and modeling improvements, we find that N1.5 outperforms N1 on both simulated manipulation benchmarks and on the real GR-1 robot, detailed ...
- **p. 2 / Architecture validation - extractive body cue:** benchmarks requiring language following: Language Table and a set of five simulated GR-1 tasks requring language ("Sim GR-1 Language").
- **p. 2 / Data-limited post-training in simulated environments - extractive body cue:** In the case of Sim GR-1, we can evaluate both fewshot and 0-shot, since the the pretraining mixture includes other Sim GR-1 tasks with the ...
- **p. 2 / Real GR-1 language following - extractive body cue:** Setting / GR00T N1 / GR00T N1.5 Language following rate / 46.6% / 93.3% Overall success rate / 43.3% / 83.0% We find that N1.5 ...
- **p. 2 / Learning to manipulate novel objects from human ego videos - extractive body cue:** Demonstrations using a novel object, captured from a GoPro (left) and the GR-1 robot (right).
- **p. 3 / Post-training on Unitree G1 - extractive body cue:** Model / GR00T N1, 1K Demos / GR00T N1.5, 1K Demos / GR00T N1.5, 1K Demos Task / Place 1 of 2 fruits onto plate; ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Although these new verbs can be considered "zero-shot" in the sense that we never collected teleoperation data for these tasks, we still train explicitly ... | p. 3 (Generalization to novel behaviors using Neural Trajectories) |
| body limitation/failure cue | The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions. | p. 1 (Architecture) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We trained GR00T N1.5 for 250K steps on 1K H100 GPUs with global batch size 16384. | p. 1 (Architecture) |
| As in N1, we used AdamW with cosine learning rate schedule with warmup ratio 0.05. | p. 1 (Architecture) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / Generalization to novel behaviors using Neural Trajectories - extractive body cue:** Although these new verbs can be considered "zero-shot" in the sense that we never collected teleoperation data for these tasks, we still train explicitly on ...
- **p. 1 / Architecture - extractive body cue:** The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions.

- **Evidence anchors reviewed:** datasets p. 1 (Introduction), p. 3 (Post-training on Unitree G1), p. 2 (Learning to manipulate novel objects from human ego videos), p. 2 (Learning to manipulate novel objects from human ego videos), p. 3 (Post-training on Unitree G1), p. 1 (Introduction), metrics p. 2 (Architecture validation), p. 2 (Real GR-1 language following), p. 3 (Generalization to novel behaviors using Neural Trajectories), p. 3 (Discussion), p. 1 (Architecture), p. 1 (Architecture), baselines p. 1 (Introduction), p. 1 (Introduction), results p. 3 (Discussion), p. 2 (Architecture validation), p. 2 (Real GR-1 language following), p. 3 (Generalization to novel behaviors using Neural Trajectories), p. 1 (Introduction), p. 1 (Architecture).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
