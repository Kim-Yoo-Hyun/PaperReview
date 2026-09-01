# Evaluation - Certifiably-Correct Mapping for Safe Navigation Despite Odometry Drift

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (24 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p007.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p007.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 12 (Figure/Table caption)): Although recent advances have achieved significant accuracy improvements (11, 12, 13, 14, 15}, formal error analysis is often lacking.

## Evaluation Body Digest

- **p. 1 / Abstract - extractive body cue:** Real-world experiments with a robotic rover show that, while baseline methods result in collisions with previously mapped obstacles, the proposed framework enables the rover to ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** «+ Finally, we demonstrate the approach in a real-world experiment on a robotic rover.
- **p. 1 / Abstract - extractive body cue:** Simulations using the Replica dataset highlight the efficacy of our methods compared to state of-the-art techniques.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** With these improvements, robots have been deployed in increasingly complex environments, relying heavily on Visual Inertial Odometry (VIOYSLAM pose estimates and obstacle ‘maps to navigate ...
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Although recent advances have achieved significant accuracy improvements (11, 12, 13, 14, 15}, formal error analysis is often lacking.
- **p. 1 / Abstract - extractive body cue:** By deflating the safe region based on the incremental odometry error at each timestep, we ensure that the map remains accurate and reliable locally around ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Localization and Mapping (SLAM) systems now report translation error rates below 1% (19, 20], enabling more reliable navigation in real-world scenarios.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** The primary goals of these advancements have been to enhance localization and mapping accuracy, improve robustness under diverse environmental conditions, and develop algorithms with lower ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** Results (p. 8); 5. Rover Experimental Seup. (2) Block diagram. The human is (p. 11).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 1. INTRODUCTION | EMPIRICAL / REAL-ROBOT OR HARDWARE | Although recent advances have achieved significant accuracy improvements (11, 12, 13, 14, 15}, formal error analysis is often lacking. | p. 1 (1. INTRODUCTION) |
| 1. INTRODUCTION | EMPIRICAL / REAL-ROBOT OR HARDWARE | The primary goals of these advancements have been to enhance localization and mapping accuracy, improve robustness under diverse environmental conditions, and develop algorithms with ... | p. 2 (1. INTRODUCTION) |
| 1. INTRODUCTION | EMPIRICAL / REAL-ROBOT OR HARDWARE | Perception methods have seen significant advancements lover the past few decades, driven by improvements in algorithms, sensors, and computational capabilities (17, 18]. | p. 2 (1. INTRODUCTION) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 6. Rover Experimental Results. (,b) shows snapshots of the reconstructed obstacle map and de estimated rover pose with (a) the baseline method and ... | p. 12 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 1 / Abstract - extractive body cue:** Real-world experiments with a robotic rover show that, while baseline methods result in collisions with previously mapped obstacles, the proposed framework enables the rover to ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** «+ Finally, we demonstrate the approach in a real-world experiment on a robotic rover.
- **p. 1 / Abstract - extractive body cue:** Simulations using the Replica dataset highlight the efficacy of our methods compared to state of-the-art techniques.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** With these improvements, robots have been deployed in increasingly complex environments, relying heavily on Visual Inertial Odometry (VIOYSLAM pose estimates and obstacle ‘maps to navigate ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Overview of notation and objectives. (a) depicts the operating favioament, where the world W is the union of the fe space and the ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 2. Two approaches to constructing an obstacle map. (Top row) An RGBD camera provides (a) the fist person RGB image, and (b) the depth ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 3. Visualization ofa snapshot ofthe o
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 4. Visualization ofthe maps generated using the baseline and certified ESDF methods on the of fice3 eavironment In (a) we see the ground.ruth imesh. ...
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 6. Rover Experimental Results. (,b) shows snapshots of the reconstructed obstacle map and de estimated rover pose with (a) the baseline method and (©) ...
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 7. Experimental domain used in Figure 8

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Real-world experiments with a robotic rover show that, while baseline methods result in collisions with previously mapped obstacles, the proposed framework enables the rover ... | embodiment, simulator version and control stack | p. 1 (Abstract), p. 2 (1. INTRODUCTION) |
| Task/environment | «+ Finally, we demonstrate the approach in a real-world experiment on a robotic rover. | reset, timeout, object/scene variation | p. 2 (1. INTRODUCTION), p. 1 (Abstract) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Although recent advances have achieved significant accuracy improvements (11, 12, 13, 14, 15}, formal error analysis is often lacking. | definition/direction/unit from same section | p. 1 (1. INTRODUCTION) |
| By deflating the safe region based on the incremental odometry error at each timestep, we ensure that the map remains accurate and reliable locally ... | definition/direction/unit from same section | p. 1 (Abstract) |
| Localization and Mapping (SLAM) systems now report translation error rates below 1% (19, 20], enabling more reliable navigation in real-world scenarios. | definition/direction/unit from same section | p. 2 (1. INTRODUCTION) |
| The primary goals of these advancements have been to enhance localization and mapping accuracy, improve robustness under diverse environmental conditions, and develop algorithms with ... | definition/direction/unit from same section | p. 2 (1. INTRODUCTION) |
| Fig. 2. Two approaches to constructing an obstacle map. (Top row) An RGBD camera provides (a) the fist person RGB image, and (b) the ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Fig. 4. Visualization ofthe maps generated using the baseline and certified ESDF methods on the of fice3 eavironment In (a) we see the ground.ruth ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Fig. 6. Rover Experimental Results. (,b) shows snapshots of the reconstructed obstacle map and de estimated rover pose with (a) the baseline method and ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Simulations using the Replica dataset highlight the efficacy of our methods compared to state of-the-art techniques. | comparison identity and matched condition | p. 1 (Abstract) |
| Real-world experiments with a robotic rover show that, while baseline methods result in collisions with previously mapped obstacles, the proposed framework enables the rover ... | comparison identity and matched condition | p. 1 (Abstract) |
| Unlike baseline methods which result in collisions, our approach prevents crashes by deflating the safe regions appropriately. | comparison identity and matched condition | p. 2 (1. INTRODUCTION) |
| + We prove the correctness and applicability ofthis frame~ \work on two popular and state-of-the-art mapping frameworks: the polytopic SFCs of [8] and the ... | comparison identity and matched condition | p. 2 (1. INTRODUCTION) |
| Fig. 4. Visualization ofthe maps generated using the baseline and certified ESDF methods on the of fice3 eavironment In (a) we see the ground.ruth ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| Fig. 6. Rover Experimental Results. (,b) shows snapshots of the reconstructed obstacle map and de estimated rover pose with (a) the baseline method and ... | comparison identity and matched condition | p. 12 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Without quantified error bounds, guaranteeing the safety of a closed-loop robotic system remains a challenge. | component/input/data sensitivity | p. 1 (1. INTRODUCTION) |
| Instead, by deflating a safe region Sj, the region that is certifiably safe shrinks, eventually becomes an empty set, and is removed from memory ... | component/input/data sensitivity | p. 2 (1. INTRODUCTION) |
| Accurate perception, state estimation and mapping, are essential for safe robotic navigation as planners and con- {rollers rely on these components for safety-critical decisions. | component/input/data sensitivity | p. 1 (Abstract) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In Section IV and V we introduce the deflation mechanism for both map representations, In Section VI we propose methods to use the certified ... | Although recent advances have achieved significant accuracy improvements (11, 12, 13, 14, 15}, formal error analysis is often lacking. | PDF body cue; verify exact table/figure and matched conditions | p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 12 (Figure/Table caption) |
| Primary metric/result | The primary goals of these advancements have been to enhance localization and mapping accuracy, improve robustness under diverse environmental conditions, and develop algorithms with ... | numeric claim only at cited anchor | p. 2 (1. INTRODUCTION) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | However, existing mapping approaches often assume perfect pose estimates, an unrealistic assumption that ean lead to incorrect fbstacle maps and therefore collisions. | p. 1 (Abstract) |
| body limitation/failure cue | Real-world experiments with a robotic rover show that, while baseline methods result in collisions with previously mapped obstacles, the proposed framework enables the rover ... | p. 1 (Abstract) |
| body limitation/failure cue | The rover uses an onboard safety filter to prevent collisions. | p. 2 (1. INTRODUCTION) |
| body limitation/failure cue | Unlike baseline methods which result in collisions, our approach prevents crashes by deflating the safe regions appropriately. | p. 2 (1. INTRODUCTION) |
| body limitation/failure cue | Fig. 6. Rover Experimental Results. (,b) shows snapshots of the reconstructed obstacle map and de estimated rover pose with (a) the baseline method and ... | p. 12 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Code: haps.//gihubs coms abcerifahly-comrect- mapping 2 Video: htps://yout beg MIDKTlouss | p. 1 (1. INTRODUCTION) |
| In these systems, raw measurements are typically processed by a frontend into a more compact representation, while a backend uses nonlinear optimization methods to ... | p. 2 (1. INTRODUCTION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 1 / Abstract - extractive body cue:** However, existing mapping approaches often assume perfect pose estimates, an unrealistic assumption that ean lead to incorrect fbstacle maps and therefore collisions.
- **p. 1 / Abstract - extractive body cue:** Real-world experiments with a robotic rover show that, while baseline methods result in collisions with previously mapped obstacles, the proposed framework enables the rover to ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** The rover uses an onboard safety filter to prevent collisions.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Unlike baseline methods which result in collisions, our approach prevents crashes by deflating the safe regions appropriately.
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 6. Rover Experimental Results. (,b) shows snapshots of the reconstructed obstacle map and de estimated rover pose with (a) the baseline method and (©) ...

- **PDF anchors reviewed:** datasets p. 1 (Abstract), p. 2 (1. INTRODUCTION), p. 1 (Abstract), p. 2 (1. INTRODUCTION), metrics p. 1 (1. INTRODUCTION), p. 1 (Abstract), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 5 (Figure/Table caption), p. 9 (Figure/Table caption), baselines p. 1 (Abstract), p. 1 (Abstract), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 9 (Figure/Table caption), p. 12 (Figure/Table caption), results p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 12 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
