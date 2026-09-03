# Evaluation - PTAM: Parallel Tracking and Mapping for Small AR Workspaces

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.robots.ox.ac.uk/~gk/PTAM/; PDF retrieval source: https://www.robots.ox.ac.uk/~gk/publications/KleinMurray2007ISMAR.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (7 RESULTS), p. 8 (7 RESULTS), p. 6 (7 RESULTS), p. 6 (7 RESULTS), p. 1 (Figure/Table caption)): At the same time, the use of a larger number of features reduces visible tracking jitter and improves performance when some features are occluded or otherwise corrupted.

## Evaluation Body Digest

- **p. 8 / 7 RESULTS - extractive body cue:** This system requires fairly powerful computing hardware and this has so far limited live experiments to a single office; we expect that with some optimisations ...
- **p. 8 / 7 RESULTS - extractive body cue:** In practice, this means that our system allows a user to ‘zoom in' much closer (and more rapidly) to objects in the environment.
- **p. 6 / 7 RESULTS - extractive body cue:** The camera then moves rapidly around the mapped scene.
- **p. 6 / 7 RESULTS - extractive body cue:** The camera performs various panning motions to produce an overview of the scene, and then zooms closer to some areas to increase detail in the ...
- **p. 7 / 7 RESULTS - extractive body cue:** Certain parts of the scene are clearly distinguishable, e.g. the keyboard and the frisbee.
- **p. 8 / 7 RESULTS - extractive body cue:** This game demonstrates tracking accuracy.
- **p. 8 / 7 RESULTS - extractive body cue:** For both trajectories, the error is predominantly in the z-direction (whose scale is exaggerated in the plot) although EKF-SLAM also fractionally underestimates the angle between ...
- **p. 6 / 7 RESULTS - extractive body cue:** 7.3 Synthetic comparison with EKF-SLAM To evaluate the system's accuracy, we compare it to an implementation [30] of EKF-SLAM based on Davison's SceneLib library with

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 7 RESULTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 7 RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | At the same time, the use of a larger number of features reduces visible tracking jitter and improves performance when some features are occluded ... | p. 8 (7 RESULTS) |
| 7 RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Frames are tracked in a relatively constant 20ms by our system, whereas EKF-SLAM scales quadratically from 3ms when the map is empty to 40ms ... | p. 8 (7 RESULTS) |
| 7 RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | All results were obtained with identical tunable parameters. | p. 6 (7 RESULTS) |
| 7 RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | 7.1 Tracking performance on live video An example of the system's operation is provided in the accompanying video file1. | p. 6 (7 RESULTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1: Typical operation of the system: Here, a desktop is tracked. The on-line generated map contains close to 3000 point features, of which ... | p. 1 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / 7 RESULTS - extractive body cue:** This system requires fairly powerful computing hardware and this has so far limited live experiments to a single office; we expect that with some optimisations ...
- **p. 8 / 7 RESULTS - extractive body cue:** In practice, this means that our system allows a user to ‘zoom in' much closer (and more rapidly) to objects in the environment.
- **p. 6 / 7 RESULTS - extractive body cue:** The camera then moves rapidly around the mapped scene.
- **p. 6 / 7 RESULTS - extractive body cue:** The camera performs various panning motions to produce an overview of the scene, and then zooms closer to some areas to increase detail in the ...
- **p. 7 / 7 RESULTS - extractive body cue:** Certain parts of the scene are clearly distinguishable, e.g. the keyboard and the frisbee.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Typical operation of the system: Here, a desktop is tracked. The on-line generated map contains close to 3000 point features, of which the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: The asynchronous mapping thread. After initialisation, this thread runs in an endless loop, occasionally receiving new frames from the tracker. 6.1 Map initialisation ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Tracking timings for a map of size M=4000. Table 1 shows a break-down of the time required to track a typi- cal frame. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2: Bundle adjustment timings with various map sizes. The above timings are mean quantities. As the map grows be- yond 100 keyframes, global bundle ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: The map and keyframes produced in the desk video. Top: two views of the map with point features and keyframes drawn. Certain parts ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Map size (right axis) and tracking timings (left axis) for the desk video included in the video attachment. The timing spike occurs when ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Comparison with EKF-SLAM on a synthetic sequence. The left image shows the map produced by the system described here, the centre image shows ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 6: The system can easily track across multiple scales. Here, the map is initialised at the top-right scale; the user moves closer in and ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This system requires fairly powerful computing hardware and this has so far limited live experiments to a single office; we expect that with some ... | embodiment, simulator version and control stack | p. 8 (7 RESULTS), p. 8 (7 RESULTS) |
| Task/environment | In practice, this means that our system allows a user to ‘zoom in' much closer (and more rapidly) to objects in the environment. | reset, timeout, object/scene variation | p. 8 (7 RESULTS), p. 6 (7 RESULTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 4 (3. A small number (50) of the coarsest-scale features are), p. 5 (3. A small number (50) of the coarsest-scale features are) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 3 (1 INTRODUCTION), p. 4 (3. A small number (50) of the coarsest-scale features are) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| This game demonstrates tracking accuracy. | definition/direction/unit from same section | p. 8 (7 RESULTS) |
| For both trajectories, the error is predominantly in the z-direction (whose scale is exaggerated in the plot) although EKF-SLAM also fractionally underestimates the angle ... | definition/direction/unit from same section | p. 8 (7 RESULTS) |
| 7.3 Synthetic comparison with EKF-SLAM To evaluate the system's accuracy, we compare it to an implementation [30] of EKF-SLAM based on Davison's SceneLib library ... | definition/direction/unit from same section | p. 6 (7 RESULTS) |
| Figure 1: Typical operation of the system: Here, a desktop is tracked. The on-line generated map contains close to 3000 point features, of which ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| This is beyond our "small workspace" design goal and at this map size the system's ability to add new keyframes and map points is ... | definition/direction/unit from same section | p. 6 (7 RESULTS) |
| Bottom: the 57 keyframes used to generate the map. | definition/direction/unit from same section | p. 7 (7 RESULTS) |
| Top: two views of the map with point features and keyframes drawn. | definition/direction/unit from same section | p. 7 (7 RESULTS) |
| Figure 6: The system can easily track across multiple scales. Here, the map is initialised at the top-right scale; the user moves closer in ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared with bundle adjustment, the processing time required for epipolar search and occasional data association refinement is small. | comparison identity and matched condition | p. 6 (7 RESULTS) |
| Trajectories compared to ground truth are shown on the right. | comparison identity and matched condition | p. 8 (7 RESULTS) |
| Table 2: Bundle adjustment timings with various map sizes. The above timings are mean quantities. As the map grows be- yond 100 keyframes, global ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| z Ground truth EKF-SLAM Proposed method Figure 5: Comparison with EKF-SLAM on a synthetic sequence. | comparison identity and matched condition | p. 8 (7 RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This video represents the size of a typical working volume which the system can handle without great difficulty. | component/input/data sensitivity | p. 6 (7 RESULTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| While this has previously been attempted by adapting SLAM algorithms developed for robotic exploration, we propose a system specifically designed to track a hand-held ... | At the same time, the use of a larger number of features reduces visible tracking jitter and improves performance when some features are occluded ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (7 RESULTS), p. 8 (7 RESULTS), p. 6 (7 RESULTS), p. 6 (7 RESULTS), p. 1 (Figure/Table caption) |
| Primary metric/result | Frames are tracked in a relatively constant 20ms by our system, whereas EKF-SLAM scales quadratically from 3ms when the map is empty to 40ms ... | numeric claim only at cited anchor | p. 8 (7 RESULTS) |

- Numeric sentences retained from the body:
- **p. 6 / 7 RESULTS - extractive body cue:** The camera explores a cluttered desk and its immediate surroundings over 1656 frames of live video input.
- **p. 6 / 7 RESULTS - extractive body cue:** At the end of the sequence the map consists of 57 keyframes and 4997 point features: from finest level to coarsest level, the feature distributions ...
- **p. 6 / 7 RESULTS - extractive body cue:** For most of the sequence, tracking can be performed in around 20ms despite the map increasing in size.
- **p. 6 / 7 RESULTS - extractive body cue:** Also, around frame 1530, tracking takes around 30ms per frame during normal operation; this is when the camera moves far away from the desk at ...
- **p. 6 / 7 RESULTS - extractive body cue:** Keyframe preparation 2.2 ms Feature projection 3.5 ms Patch search 9.8 ms Iterative pose update 3.7 ms Total 19.2 ms Table 1: Tracking timings for ...
- **p. 6 / 7 RESULTS - extractive body cue:** A more practical limit at which the system remains well usable is around 6000 points and 150 keyframes.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 8 LIMITATIONS AND FUTURE WORK This section describes some of the known issues with the system presented. | p. 8 (7 RESULTS) |
| body limitation/failure cue | AR applications are usable as soon as the map has been initialised from stereo; mapping proceeds in the background in a manner transparent to ... | p. 8 (7 RESULTS) |
| body limitation/failure cue | Figure 6: The system can easily track across multiple scales. Here, the map is initialised at the top-right scale; the user moves closer in ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | As the map grows beyond 100 keyframes, global bundle adjustment cannot keep up with exploration and is almost always aborted, converging only when the ... | p. 6 (7 RESULTS) |
| body limitation/failure cue | Timings of individual mapping steps are difficult to obtain, they vary wildly not only with map size but also scene structure (both global and ... | p. 6 (7 RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| This system requires fairly powerful computing hardware and this has so far limited live experiments to a single office; we expect that with some ... | p. 8 (7 RESULTS) |
| We consider this to be compatible with a large number of workspace-related AR applications, where the user is anyway often tethered to a computer. | p. 1 (1 INTRODUCTION) |
| We propose to split tracking and mapping into two separate tasks, processed in parallel threads on a dual-core computer: one thread deals with the ... | p. 1 (ABSTRACT) |
| Also, since modern computers now typically come with more than one processing core, we can split tracking and mapping into two separately-scheduled threads. | p. 2 (1 INTRODUCTION) |
| Finally, our implementation of an AR application which takes place on a planar playing field may invite a comparison with [25] in which the ... | p. 2 (1 INTRODUCTION) |
| Further, we run the FAST-10 [23] corner detector on each pyramid level. | p. 3 (3. A small number (50) of the coarsest-scale features are) |
| A final pose estimate for the frame is computed from all the matches found. | p. 3 (3. A small number (50) of the coarsest-scale features are) |
| The map-making steps are now individually described in detail. | p. 4 (3. A small number (50) of the coarsest-scale features are) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 7 RESULTS - extractive body cue:** 8 LIMITATIONS AND FUTURE WORK This section describes some of the known issues with the system presented.
- **p. 8 / 7 RESULTS - extractive body cue:** AR applications are usable as soon as the map has been initialised from stereo; mapping proceeds in the background in a manner transparent to the ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 6: The system can easily track across multiple scales. Here, the map is initialised at the top-right scale; the user moves closer in and ...
- **p. 6 / 7 RESULTS - extractive body cue:** As the map grows beyond 100 keyframes, global bundle adjustment cannot keep up with exploration and is almost always aborted, converging only when the camera ...
- **p. 6 / 7 RESULTS - extractive body cue:** Timings of individual mapping steps are difficult to obtain, they vary wildly not only with map size but also scene structure (both global and local); ...

- **Evidence anchors reviewed:** datasets p. 8 (7 RESULTS), p. 8 (7 RESULTS), p. 6 (7 RESULTS), p. 6 (7 RESULTS), p. 7 (7 RESULTS), metrics p. 8 (7 RESULTS), p. 8 (7 RESULTS), p. 6 (7 RESULTS), p. 1 (Figure/Table caption), p. 6 (7 RESULTS), p. 7 (7 RESULTS), baselines p. 6 (7 RESULTS), p. 8 (7 RESULTS), p. 6 (Figure/Table caption), p. 8 (7 RESULTS), results p. 8 (7 RESULTS), p. 8 (7 RESULTS), p. 6 (7 RESULTS), p. 6 (7 RESULTS), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
