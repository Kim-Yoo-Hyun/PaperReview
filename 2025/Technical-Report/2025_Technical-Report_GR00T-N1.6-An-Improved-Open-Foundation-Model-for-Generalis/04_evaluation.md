# Evaluation - GR00T N1.6: An Improved Open Foundation Model for Generalist Humanoid Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (2 pages; PyMuPDF text; extraction quality: medium); canonical paper source: https://research.nvidia.com/labs/gear/gr00t-n1_6/; PDF retrieval source: https://research.nvidia.com/labs/gear/gr00t-n1_6/. PDF provenance note: official NVIDIA technical page rendered to a task-scoped PDF snapshot; no author-supplied publication PDF identified. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 1 (Discussion), p. 1 (Introduction), p. 2 (Discussion), p. 2 (Discussion)): When scaling up real-world experiments, we incorporate various lessons learned from the robot learning community to improve model success rates during rollouts.

## Evaluation Body Digest

- **p. 1 / Experiments - extractive body cue:** In the following robot experiments, we further post-train on small task-specific datasets; typically 10K-30K steps with global batch size 1K or less.
- **p. 1 / Discussion - extractive body cue:** For GR00T N1.6, we conduct more complex real-world robot experiments than GR00T N1.5, requiring long-horizon reasoning, dexterity, and multi-tasking abilities.
- **p. 2 / Discussion - extractive body cue:** We expect users to benefit from improved performance in bimanual manipulation and locomanipulation tasks.
- **p. 2 / Discussion - extractive body cue:** More fine-grained subtask annotation can improve language following, but not yet reaching robust generalization.
- **p. 1 / Discussion - extractive body cue:** When scaling up real-world experiments, we incorporate various lessons learned from the robot learning community to improve model success rates during rollouts.
- **p. 1 / Discussion - extractive body cue:** However, with small datasets, relative actions are prone to error accumulation, which impacts correction ability.
- **p. 2 / Discussion - extractive body cue:** Test-time and train-time RTC provide performance boosts to motion smoothness and robustness during asynchronous rollouts.
- **p. 1 / Introduction - extractive body cue:** With several architecture, data and modeling improvements, we find that N1.6 outperforms N1.5 on both simulated manipulation benchmarks and on real bimanual YAM, Agibot Genie-1 ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** Experiments (p. 1).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Discussion | EMPIRICAL / REAL-ROBOT OR HARDWARE | When scaling up real-world experiments, we incorporate various lessons learned from the robot learning community to improve model success rates during rollouts. | p. 1 (Discussion) |
| Introduction | EMPIRICAL / REAL-ROBOT OR HARDWARE | With several architecture, data and modeling improvements, we find that N1.6 outperforms N1.5 on both simulated manipulation benchmarks and on real bimanual YAM, Agibot ... | p. 1 (Introduction) |
| Discussion | EMPIRICAL / REAL-ROBOT OR HARDWARE | We expect users to benefit from improved performance in bimanual manipulation and locomanipulation tasks. | p. 2 (Discussion) |
| Discussion | EMPIRICAL / REAL-ROBOT OR HARDWARE | Overall, GR00T N1.6 represents an improvement over GR00T N1.5 across diverse embodiments. | p. 2 (Discussion) |

## Dataset / Benchmark Role

- **p. 1 / Experiments - extractive body cue:** In the following robot experiments, we further post-train on small task-specific datasets; typically 10K-30K steps with global batch size 1K or less.
- **p. 1 / Discussion - extractive body cue:** For GR00T N1.6, we conduct more complex real-world robot experiments than GR00T N1.5, requiring long-horizon reasoning, dexterity, and multi-tasking abilities.
- **p. 2 / Discussion - extractive body cue:** We expect users to benefit from improved performance in bimanual manipulation and locomanipulation tasks.
- **p. 2 / Discussion - extractive body cue:** More fine-grained subtask annotation can improve language following, but not yet reaching robust generalization.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- figure/table caption cue 없음

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In the following robot experiments, we further post-train on small task-specific datasets; typically 10K-30K steps with global batch size 1K or less. | embodiment, simulator version and control stack | p. 1 (Experiments), p. 1 (Discussion) |
| Task/environment | For GR00T N1.6, we conduct more complex real-world robot experiments than GR00T N1.5, requiring long-horizon reasoning, dexterity, and multi-tasking abilities. | reset, timeout, object/scene variation | p. 1 (Discussion), p. 2 (Discussion) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 1 (Model and Data Improvements), p. 1 (Model and Data Improvements) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 2 (Discussion), p. 2 (Discussion) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| When scaling up real-world experiments, we incorporate various lessons learned from the robot learning community to improve model success rates during rollouts. | definition/direction/unit from same section | p. 1 (Discussion) |
| However, with small datasets, relative actions are prone to error accumulation, which impacts correction ability. | definition/direction/unit from same section | p. 1 (Discussion) |
| Test-time and train-time RTC provide performance boosts to motion smoothness and robustness during asynchronous rollouts. | definition/direction/unit from same section | p. 2 (Discussion) |
| We expect users to benefit from improved performance in bimanual manipulation and locomanipulation tasks. | definition/direction/unit from same section | p. 2 (Discussion) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We expect users of N1.6 should observe better post-training performance compared to N1.5. | comparison identity and matched condition | p. 1 (Introduction) |
| With several architecture, data and modeling improvements, we find that N1.6 outperforms N1.5 on both simulated manipulation benchmarks and on real bimanual YAM, Agibot ... | comparison identity and matched condition | p. 1 (Introduction) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Removes N1.5's post-VLM 4-layer transformer adapter. | component/input/data sensitivity | p. 1 (Model and Data Improvements) |
| Architectural changes: Base VLM: We use an internal NVIDIA Cosmos-2B VLM variant. | component/input/data sensitivity | p. 1 (Model and Data Improvements) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce GR00T N1.6, an improved version of the GR00T N1.5 foundation model for humanoid robots. | When scaling up real-world experiments, we incorporate various lessons learned from the robot learning community to improve model success rates during rollouts. | PDF body cue; verify exact table/figure and matched conditions | p. 1 (Discussion), p. 1 (Introduction), p. 2 (Discussion), p. 2 (Discussion) |
| Primary metric/result | With several architecture, data and modeling improvements, we find that N1.6 outperforms N1.5 on both simulated manipulation benchmarks and on real bimanual YAM, Agibot ... | numeric claim only at cited anchor | p. 1 (Introduction) |

- Numeric sentences retained from the body:
- **p. 1 / Model and Data Improvements - extractive body cue:** Uses 2x larger DiT (32 layers vs 16 layers in N1.5).
- **p. 1 / Model and Data Improvements - extractive body cue:** Instead, we unfreeze the top 4 layers of the VLM during pretraining.
- **p. 1 / Model and Data Improvements - extractive body cue:** Uses 2x larger DiT (32 layers vs 16 layers in N1.5).
- **p. 1 / Model and Data Improvements - extractive body cue:** Instead, we unfreeze the top 4 layers of the VLM during pretraining.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | More fine-grained subtask annotation can improve language following, but not yet reaching robust generalization. | p. 2 (Discussion) |
| body limitation/failure cue | Test-time and train-time RTC provide performance boosts to motion smoothness and robustness during asynchronous rollouts. | p. 2 (Discussion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In the following robot experiments, we further post-train on small task-specific datasets; typically 10K-30K steps with global batch size 1K or less. | p. 1 (Experiments) |
| The VLM supports flexible resolution and can encode images in their native aspect ratio without padding. | p. 1 (Model and Data Improvements) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Discussion - extractive body cue:** More fine-grained subtask annotation can improve language following, but not yet reaching robust generalization.
- **p. 2 / Discussion - extractive body cue:** Test-time and train-time RTC provide performance boosts to motion smoothness and robustness during asynchronous rollouts.

- **Evidence anchors reviewed:** datasets p. 1 (Experiments), p. 1 (Discussion), p. 2 (Discussion), p. 2 (Discussion), metrics p. 1 (Discussion), p. 1 (Discussion), p. 2 (Discussion), p. 2 (Discussion), baselines p. 1 (Introduction), p. 1 (Introduction), results p. 1 (Discussion), p. 1 (Introduction), p. 2 (Discussion), p. 2 (Discussion).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
