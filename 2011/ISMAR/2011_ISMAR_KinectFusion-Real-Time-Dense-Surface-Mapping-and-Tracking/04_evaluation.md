# Evaluation - KinectFusion: Real-Time Dense Surface Mapping and Tracking

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.microsoft.com/en-us/research/publication/kinectfusion-real-time-dense-surface-mapping-and-tracking/; PDF retrieval source: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ismar2011.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS)): Rapid accumulation of errors results in the non-circular trajectory and poor reconstruction is apparent (though see later Figure 11 where frame-skipping is shown to improve this).

## Evaluation Body Digest

- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Finally, for comparison, a new longer dataset of MN frames was processed, where a user moved the sensor over the scene without precise repetition.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** The main failure case in standard indoor scenes is when the sensor is faced by a large planar scene which fills most of its field ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 6 CONCLUSIONS The availability of commodity depth sensors such as Kinect has the potential to revolutionise the fields of robotics and human-computer interaction.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We highlight these two frames, and they are seen almost overlapping (red and black) alongside excellent trajectory and scene reconstruction quality.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** The Kinect sensor was placed in a fixed location observing a tabletop scene mounted on a turntable.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** For the purposes of our system, if the reconstruction volume is set to span solely the region of the rotating scene, the resulting depth image ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Rapid accumulation of errors results in the non-circular trajectory and poor reconstruction is apparent (though see later Figure 11 where frame-skipping is shown to improve ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Our video demonstrates a good variety of agile motion tracking successfully through even rapid motion.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Rapid accumulation of errors results in the non-circular trajectory and poor reconstruction is apparent (though see later Figure 11 where frame-skipping is shown to ... | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | We have conducted a number of experiments to investigate the performance of our system. | p. 7 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | But the frame-model tracking results in drift-free operation without explicit global optimisation. | p. 9 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our video demonstrates a good variety of agile motion tracking successfully through even rapid motion. | p. 9 (4 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Finally, for comparison, a new longer dataset of MN frames was processed, where a user moved the sensor over the scene without precise repetition.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** The main failure case in standard indoor scenes is when the sensor is faced by a large planar scene which fills most of its field ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 6 CONCLUSIONS The availability of commodity depth sensors such as Kinect has the potential to revolutionise the fields of robotics and human-computer interaction.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We highlight these two frames, and they are seen almost overlapping (red and black) alongside excellent trajectory and scene reconstruction quality.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** The Kinect sensor was placed in a fixed location observing a tabletop scene mounted on a turntable.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** For the purposes of our system, if the reconstruction volume is set to span solely the region of the rotating scene, the resulting depth image ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Example output from our system, generated in real-time with a handheld Kinect depth camera and no other sensing infrastructure. Normal maps (colour) and ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: A larger scale reconstruction obtained in real-time. with such sensors are obvious, but algorithms to date have not fully leveraged the fidelity and ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Overall system workflow. Surface reconstruction update: The global scene fusion pro- cess, where given the pose determined by tracking the depth data from ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4: A slice through the truncated signed distance volume showing the truncated function F > µ (white), the smooth distance field around the surface ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Reconstructed of a scene showing raycasting of the TSDF (left) without and (middle and right) with interpolation of the TSDF at the surface ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6: Demonstration of the space skipping ray casting. (Left) pixel iteration count are shown where for each pixel the ray is tra- versed in ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7: Example of point-plane outliers as person steps into par- tially reconstructed scene (left). Outliers from compatibility checks (Equation 17) using a surface measurement ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 8: Circular motion experiment to highlight the SLAM characteristics of our system as the sensor orbits a table. For each column, the top row ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Finally, for comparison, a new longer dataset of MN frames was processed, where a user moved the sensor over the scene without precise repetition. | embodiment, simulator version and control stack | p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Task/environment | The main failure case in standard indoor scenes is when the sensor is faced by a large planar scene which fills most of its ... | reset, timeout, object/scene variation | p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 2 (2 BACKGROUND), p. 4 (3.1 Preliminaries) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 6 (3.1 Preliminaries), p. 4 (3 METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Rapid accumulation of errors results in the non-circular trajectory and poor reconstruction is apparent (though see later Figure 11 where frame-skipping is shown to ... | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| Our video demonstrates a good variety of agile motion tracking successfully through even rapid motion. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| The key concepts in our real-time tracking and mapping system are (1) always up-to-date surface representation fusing all registered data from previous scans using ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| We have conducted a number of experiments to investigate the performance of our system. | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| These and other aspects, such as the system's ability to keep track during very rapid motion, are illustrated extensively in our submitted video. | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| This is clearly demonstrated in Figure 11 where we sub-sample the N frames to use every 8th frame only. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| Figure 4: A slice through the truncated signed distance volume showing the truncated function F > µ (white), the smooth distance field around the ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 1: Example output from our system, generated in real-time with a handheld Kinect depth camera and no other sensing infrastructure. Normal maps (colour) ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Note that this can be compared with the reconstruction from the same number of MN different frames of the same scene obtained from hand-held ... | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| There is a drastic reduction in drift compared to Figure 8(a) where all frames are used. | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| Finally, for comparison, a new longer dataset of MN frames was processed, where a user moved the sensor over the scene without precise repetition. | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| 4.1 Metrically Consistent Reconstruction Our tracking and mapping system provides a constant time algorithm for a given area of reconstruction, and we are interested ... | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| But the frame-model tracking results in drift-free operation without explicit global optimisation. | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| Figure 1: Example output from our system, generated in real-time with a handheld Kinect depth camera and no other sensing infrastructure. Normal maps (colour) ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 4.1 Metrically Consistent Reconstruction Our tracking and mapping system provides a constant time algorithm for a given area of reconstruction, and we are interested ... | component/input/data sensitivity | p. 7 (4 EXPERIMENTS) |
| Finally, for comparison, a new longer dataset of MN frames was processed, where a user moved the sensor over the scene without precise repetition. | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| While the turntable experiments demonstrate interesting convergence of the system without an explicit global optimisation, the real power in integrating every frame of data ... | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| But the frame-model tracking results in drift-free operation without explicit global optimisation. | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| Figure 5: Reconstructed of a scene showing raycasting of the TSDF (left) without and (middle and right) with interpolation of the TSDF at the ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| 4.2 Processing Time Figure 13 shows results from an experiment where timings were taken of the main system components and the reconstruction voxel resolution ... | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper we present a detailed method with analysis of what we believe is the first system which permits real-time, dense volumetric reconstruction ... | Rapid accumulation of errors results in the non-circular trajectory and poor reconstruction is apparent (though see later Figure 11 where frame-skipping is shown to ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Primary metric/result | We have conducted a number of experiments to investigate the performance of our system. | numeric claim only at cited anchor | p. 7 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** The turntable was then spun through a full rotation as depth data was captured over ≈19 seconds, resulting in N = 560 frames.
- **p. 4 / 3 METHOD - extractive body cue:** Rk Tg,k Rk Tg,k-1 Input Measurement Pose Estimation Update Reconstruction Surface Prediction Compute Surface Nertex and Normal Maps ICP of Predicted and Measured Surface Integrate ...
- **p. 5 / 3.1 Preliminaries - extractive body cue:** However, we have found that approximation within the truncation region for 100s or more fused TSDFs from multiple viewpoints (as performed here) converges towards an ...
- **p. 5 / 3.1 Preliminaries - extractive body cue:** (For a 640x480 depth stream at 30fps the equivalent of over 9 million new point measurements are made per second).
- **p. 5 / 3.1 Preliminaries - extractive body cue:** Although a large number of voxels can be visited that will not project into the current image, the simplicity of the kernel means operation time ...
- **p. 7 / 3.1 Preliminaries - extractive body cue:** Writing the update eTz inc as a parameter vector, x = (β,γ,α,tx,ty,tz)⊤∈R6 (19) and updating the current global frame vertex estimates for all pixels {u/Ω(u)̸ ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 4.3 Observations and Failure Modes Our system is robust to a wide range of practical conditions in terms of scene structure and camera motion. | p. 9 (4 EXPERIMENTS) |
| body limitation/failure cue | Both outcomes will lead to a reduced quality reconstruction and tracking failure. | p. 7 (3.1 Preliminaries) |
| body limitation/failure cue | The main failure case in standard indoor scenes is when the sensor is faced by a large planar scene which fills most of its ... | p. 9 (4 EXPERIMENTS) |
| body limitation/failure cue | If either test fails, the system is placed into re-localisation mode. | p. 7 (3.1 Preliminaries) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Although efficient algorithms exist for computing the true discrete SDF for a given set of point measurements (complexity is linear in the the number ... | p. 5 (3.1 Preliminaries) |
| (21) An iteration is obtained by solving: min x∈R6 ∑ Ωk(u)̸=null ∥E∥2 2 (22) E = ˆNg k-1(ˆu)⊤ G(u)x+ eVg k(u)-ˆVg k-1(ˆu)  (23) ... | p. 7 (3.1 Preliminaries) |
| Frames 1...N were fused together within the TSDF using sensor pose estimates obtained with our frame-to-frame only ICP implementation. | p. 7 (4 EXPERIMENTS) |
| An important aspect of a useful system is its ability to scale with available GPU memory and processing resources. | p. 8 (4 EXPERIMENTS) |
| Simulation works on the TSDF volumetric representation, and runs on the GPU alongside tracking and mapping, all in real-time. | p. 9 (4 EXPERIMENTS) |
| 6 CONCLUSIONS The availability of commodity depth sensors such as Kinect has the potential to revolutionise the fields of robotics and human-computer interaction. | p. 9 (4 EXPERIMENTS) |
| Our GPU based implementation uses all the available data at frame-rate. | p. 4 (3 METHOD) |
| 3.4 Surface Prediction from Ray Casting the TSDF With the most up-to-date reconstruction available comes the ability to compute a dense surface prediction by ... | p. 5 (3.1 Preliminaries) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 4.3 Observations and Failure Modes Our system is robust to a wide range of practical conditions in terms of scene structure and camera motion.
- **p. 7 / 3.1 Preliminaries - extractive body cue:** Both outcomes will lead to a reduced quality reconstruction and tracking failure.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** The main failure case in standard indoor scenes is when the sensor is faced by a large planar scene which fills most of its field ...
- **p. 7 / 3.1 Preliminaries - extractive body cue:** If either test fails, the system is placed into re-localisation mode.

- **Evidence anchors reviewed:** datasets p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), metrics p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), baselines p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 1 (Figure/Table caption), results p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
