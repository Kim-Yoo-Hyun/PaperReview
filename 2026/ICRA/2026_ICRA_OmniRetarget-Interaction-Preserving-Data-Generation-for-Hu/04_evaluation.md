# Evaluation - OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2509.26633; PDF retrieval source: https://arxiv.org/pdf/2509.26633. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 12 (Figure/Table caption), p. 3 (Figure/Table caption), p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 6 (Figure/Table caption)): Fig. 7: Artifacts resulting from the retargeting baselines. trained on our augmented data instead yield reliable success (see video for comparison). Admittedly, additional reward engineering could help, but it contradicts ...

## Evaluation Body Digest

- **p. 1 / I. INTRODUCTION - extractive body cue:** The quest to enable humanoid robots to perform complex whole-body scene- and object-interaction tasks has long been constrained by a fundamental data bottleneck.
- **p. 1 / Abstract - extractive body cue:** Moreover, preserving task-relevant interactions enables efficient data augmentation, from a single demonstration to different robot embodiments, terrains, and object configurations.
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 10: Histograms from the downstream RL evaluation showing the failure patterns for the baselines in different tasks. VideoMimic, which fails systematically due to poor ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Artifacts resulting from the retargeting baselines. trained on our augmented data instead yield reliable success (see video for comparison). Admittedly, additional reward engineering ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** While deep reinforcement learning (RL) has shown remarkable success in robot control, efficient exploration is highly sensitive to reward engineering [3].
- **p. 1 / Abstract - extractive body cue:** Such high-quality data enables proprioceptive RL policies to successfully execute longhorizon (up to 30 seconds) parkour and loco-manipulation skills on a Unitree G1 humanoid, trained ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: OMNIRETARGET overview. Human demonstrations are retargeted to the robot via interaction-mesh-based constrained optimization. Each spatial and shape augmentation is solved as a new ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Cross-embodiment robot-object-terrain interaction. Drake [52], which correctly handles the differential geometry of rotations on the S3 manifold [53]. Our interaction-mesh-based kinematic pipeline is ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** V. EXPERIMENTAL RESULTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 7: Artifacts resulting from the retargeting baselines. trained on our augmented data instead yield reliable success (see video for comparison). Admittedly, additional reward ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 10: Histograms from the downstream RL evaluation showing the failure patterns for the baselines in different tasks. VideoMimic, which fails systematically due to ... | p. 12 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 2: OMNIRETARGET overview. Human demonstrations are retargeted to the robot via interaction-mesh-based constrained optimization. Each spatial and shape augmentation is solved as a ... | p. 3 (Figure/Table caption) |
| Abstract | EMPIRICAL / REAL-ROBOT OR HARDWARE | We comprehensively evaluate OMNIRETARGET by retargeting motions from OMOMO [1], LAFAN1 [2], and our in-house MoCap datasets, generating over 8-hour trajectories that achieve better ... | p. 1 (Abstract) |
| I. INTRODUCTION | EMPIRICAL / REAL-ROBOT OR HARDWARE | While deep reinforcement learning (RL) has shown remarkable success in robot control, efficient exploration is highly sensitive to reward engineering [3]. | p. 1 (I. INTRODUCTION) |

## Dataset / Benchmark Role

- **p. 1 / I. INTRODUCTION - extractive body cue:** The quest to enable humanoid robots to perform complex whole-body scene- and object-interaction tasks has long been constrained by a fundamental data bottleneck.
- **p. 1 / Abstract - extractive body cue:** Moreover, preserving task-relevant interactions enables efficient data augmentation, from a single demonstration to different robot embodiments, terrains, and object configurations.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: OMNIRETARGET enables reinforcement learning policies to learn complex, long-horizon loco-manipulation skills in challenging environments that transfer zero-shot from simulation to a Unitree G1 ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: OMNIRETARGET overview. Human demonstrations are retargeted to the robot via interaction-mesh-based constrained optimization. Each spatial and shape augmentation is solved as a new ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Cross-embodiment robot-object-terrain interaction. Drake [52], which correctly handles the differential geometry of rotations on the S3 manifold [53]. Our interaction-mesh-based kinematic pipeline is ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: OMNIRETARGET generates systematic variations of (a) terrain height, (b) object initial pose, and (c) object shape from a single human demonstration, with optimized ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Additional hardware results showing diverse, agile and human-like behaviors. • Observation noise: ±0.05 for orientation in Rot6D, ±0.5 m/s and ±0.2 rad/s for ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Hardware results showing a high-dynamic wall-flip motion. The robot reaches a maximum linear velocity of 3.5 m/s and a peak angular velocity of ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Artifacts resulting from the retargeting baselines. trained on our augmented data instead yield reliable success (see video for comparison). Admittedly, additional reward engineering ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 8: The Laplacian coorinate should stay the same when the object rotates 180◦. offset ∆pobj and rotational offset ∆θobj that are applied at the ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The quest to enable humanoid robots to perform complex whole-body scene- and object-interaction tasks has long been constrained by a fundamental data bottleneck. | embodiment, simulator version and control stack | p. 1 (I. INTRODUCTION), p. 1 (Abstract) |
| Task/environment | Moreover, preserving task-relevant interactions enables efficient data augmentation, from a single demonstration to different robot embodiments, terrains, and object configurations. | reset, timeout, object/scene variation | p. 1 (Abstract) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 1 (Body text (section not recovered)), p. 1 (I. INTRODUCTION) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | 본문 anchor 없음 |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 10: Histograms from the downstream RL evaluation showing the failure patterns for the baselines in different tasks. VideoMimic, which fails systematically due to ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| Fig. 7: Artifacts resulting from the retargeting baselines. trained on our augmented data instead yield reliable success (see video for comparison). Admittedly, additional reward ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| While deep reinforcement learning (RL) has shown remarkable success in robot control, efficient exploration is highly sensitive to reward engineering [3]. | definition/direction/unit from same section | p. 1 (I. INTRODUCTION) |
| Such high-quality data enables proprioceptive RL policies to successfully execute longhorizon (up to 30 seconds) parkour and loco-manipulation skills on a Unitree G1 humanoid, ... | definition/direction/unit from same section | p. 1 (Abstract) |
| Fig. 2: OMNIRETARGET overview. Human demonstrations are retargeted to the robot via interaction-mesh-based constrained optimization. Each spatial and shape augmentation is solved as a ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Fig. 3: Cross-embodiment robot-object-terrain interaction. Drake [52], which correctly handles the differential geometry of rotations on the S3 manifold [53]. Our interaction-mesh-based kinematic pipeline ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Fig. 4: OMNIRETARGET generates systematic variations of (a) terrain height, (b) object initial pose, and (c) object shape from a single human demonstration, with ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 7: Artifacts resulting from the retargeting baselines. trained on our augmented data instead yield reliable success (see video for comparison). Admittedly, additional reward ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| We comprehensively evaluate OMNIRETARGET by retargeting motions from OMOMO [1], LAFAN1 [2], and our in-house MoCap datasets, generating over 8-hour trajectories that achieve better ... | comparison identity and matched condition | p. 1 (Abstract) |
| Fig. 10: Histograms from the downstream RL evaluation showing the failure patterns for the baselines in different tasks. VideoMimic, which fails systematically due to ... | comparison identity and matched condition | p. 12 (Figure/Table caption) |
| Fig. 2: OMNIRETARGET overview. Human demonstrations are retargeted to the robot via interaction-mesh-based constrained optimization. Each spatial and shape augmentation is solved as a ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 2: OMNIRETARGET overview. Human demonstrations are retargeted to the robot via interaction-mesh-based constrained optimization. Each spatial and shape augmentation is solved as a ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address this, we introduce OMNIRETARGET, an interactionpreserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial ... | Fig. 7: Artifacts resulting from the retargeting baselines. trained on our augmented data instead yield reliable success (see video for comparison). Admittedly, additional reward ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 12 (Figure/Table caption), p. 3 (Figure/Table caption), p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 6 (Figure/Table caption) |
| Primary metric/result | Fig. 10: Histograms from the downstream RL evaluation showing the failure patterns for the baselines in different tasks. VideoMimic, which fails systematically due to ... | numeric claim only at cited anchor | p. 12 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 1 / Body text (section not recovered) - extractive body cue:** Thanks to the high-quality interaction-preserving motion retargeting, these policies are trained and deployed in a minimal and unified way: it involves only 5 rewards, 4 ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** Thanks to the high-quality interaction-preserving motion retargeting, these policies are trained and deployed in a minimal and unified way: it involves only 5 rewards, 4 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 10: Histograms from the downstream RL evaluation showing the failure patterns for the baselines in different tasks. VideoMimic, which fails systematically due to ... | p. 12 (Figure/Table caption) |
| body limitation/failure cue | Fig. 3: Cross-embodiment robot-object-terrain interaction. Drake [52], which correctly handles the differential geometry of rotations on the S3 manifold [53]. Our interaction-mesh-based kinematic pipeline ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Fig. 5: Additional hardware results showing diverse, agile and human-like behaviors. • Observation noise: ±0.05 for orientation in Rot6D, ±0.5 m/s and ±0.2 rad/s ... | p. 6 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All code, retargeted datasets, and trained policies will be publicly released. | p. 1 (Abstract) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 10: Histograms from the downstream RL evaluation showing the failure patterns for the baselines in different tasks. VideoMimic, which fails systematically due to poor ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Cross-embodiment robot-object-terrain interaction. Drake [52], which correctly handles the differential geometry of rotations on the S3 manifold [53]. Our interaction-mesh-based kinematic pipeline is ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Additional hardware results showing diverse, agile and human-like behaviors. • Observation noise: ±0.05 for orientation in Rot6D, ±0.5 m/s and ±0.2 rad/s for ...

- **Evidence anchors reviewed:** datasets p. 1 (I. INTRODUCTION), p. 1 (Abstract), metrics p. 12 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (I. INTRODUCTION), p. 1 (Abstract), p. 3 (Figure/Table caption), p. 4 (Figure/Table caption), baselines p. 7 (Figure/Table caption), p. 1 (Abstract), p. 12 (Figure/Table caption), p. 3 (Figure/Table caption), results p. 7 (Figure/Table caption), p. 12 (Figure/Table caption), p. 3 (Figure/Table caption), p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
