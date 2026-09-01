# Evaluation - Demonstrating MOSART: Opening Articulated Structures in the Real World

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (25 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p033.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p033.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (IV. EXPERIMENTS), p. 3 (Figure/Table caption), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (Figure/Table caption)): Overall, our system achieves a 61% success rate across 31 unseen cabinets and drawers in unseen real world environments.

## Evaluation Body Digest

- **p. 7 / IV. EXPERIMENTS - extractive body cue:** In each test, the robot is placed approximately 1.5m from the target object with the camera oriented so as to have the target ‘object in ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We work with the Stretch RE2 robot.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** For most successful trials, the robot opens the drawer / cupboard completely (ie. drawers by 35cm and cupboards by 90°) in a graceful manner (see ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Overall, our system achieves a 61% success rate across 31 unseen cabinets and drawers in unseen real world environments.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Accuracy of APM predictions on images collected during our large-scale real world evaluation.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Contact Correction. (a) shows a grasping attempt with No contact correction, whereas (b) shows the grasping attempt with contact correction. Due to compounding ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 8. 59% of failures (ie. 7 failures) are due to perception, including various kinds of failures, such as failure to detect meshed cabinets (2/7), ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** This includes evaluating the quality of our MaskRCNN-based perception module (as well as a Detic-based perception model) on real world images, comparing APM to two ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mobile base와 one/two-arm manipulation environment.
- **Input boundary:** egocentric RGB-D, language/task goal, base-arm proprioception.
- **Output/decision under evaluation:** base motion plus arm/gripper action.
- **Primary target:** long-horizon task success, reachability, collision과 recovery.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Overall, our system achieves a 61% success rate across 31 unseen cabinets and drawers in unseen real world environments. | p. 7 (IV. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 2: MOSART Design. The perception module outputs 3D articulation parameters in the robot frame using RGB-D images. The robot then navigates to the ... | p. 3 (Figure/Table caption) |
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | We first present ‘our end-to-end system test results, evaluating MOSART on 31 novel drawers and cupboards across 10 buildings (Section IV-A), To see how ... | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Accuracy of APM predictions on images collected during our large-scale real world evaluation. | p. 7 (IV. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 5: Contact Correction. (a) shows a grasping attempt with No contact correction, whereas (b) shows the grasping attempt with contact correction. Due to ... | p. 6 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / IV. EXPERIMENTS - extractive body cue:** In each test, the robot is placed approximately 1.5m from the target object with the camera oriented so as to have the target ‘object in ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We work with the Stretch RE2 robot.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** For most successful trials, the robot opens the drawer / cupboard completely (ie. drawers by 35cm and cupboards by 90°) in a graceful manner (see ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: MOSART Design. The perception module outputs 3D articulation parameters in the robot frame using RGB-D images. The robot then navigates to the target ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Overview of the Articulation-parameter Prediction Module (APM). Given an RGB image our modified Mask RCNN detects articulated objects and predicts the articulation type, ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Topdown Navigation Targets and Corrective Mo- tions. We show the topdown navigation targets relative 10 the handle for each articulation type. For left-hinged ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Contact Correction. (a) shows a grasping attempt with No contact correction, whereas (b) shows the grasping attempt with contact correction. Due to compounding ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Comparison to OPDMulti [76]. We perform a quali the same six images presented in F
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 7: Diverse Handles. We test MOSART on 6 diverse hhandles on 3 test objects. MOSART succeeds on all 18 trials
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 8. 59% of failures (ie. 7 failures) are due to perception, including various kinds of failures, such as failure to detect meshed cabinets (2/7), ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 8: Failure Cases. Bar chart characterizing the various failure modes of MOSART for opening drawers and cabinets, 59% of failures are due to perception ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In each test, the robot is placed approximately 1.5m from the target object with the camera oriented so as to have the target ‘object ... | embodiment, simulator version and control stack | p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Task/environment | We work with the Stretch RE2 robot. | reset, timeout, object/scene variation | p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Observation/sensor | egocentric RGB-D, language/task goal, base-arm proprioception | calibration, preprocessing, privileged input | p. 4 (A. Predicting Articulation Parameters), p. 3 (A. Predicting Articulation Parameters) |
| Output/decision | base motion plus arm/gripper action | action frame, controller and termination | p. 2 (1. Iyrropucrion), p. 3 (1. Iyrropucrion) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Overall, our system achieves a 61% success rate across 31 unseen cabinets and drawers in unseen real world environments. | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| Accuracy of APM predictions on images collected during our large-scale real world evaluation. | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| Fig. 5: Contact Correction. (a) shows a grasping attempt with No contact correction, whereas (b) shows the grasping attempt with contact correction. Due to ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Figure 8. 59% of failures (ie. 7 failures) are due to perception, including various kinds of failures, such as failure to detect meshed cabinets ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| This includes evaluating the quality of our MaskRCNN-based perception module (as well as a Detic-based perception model) on real world images, comparing APM to ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| Fig. 8: Failure Cases. Bar chart characterizing the various failure modes of MOSART for opening drawers and cabinets, 59% of failures are due to ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| This includes evaluating the quality of our MaskRCNN-based perception module (as well as a Detic-based perception model) on real world images, comparing APM to ... | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| Fig. 6: Comparison to OPDMulti [76]. We perform a quali the same six images presented in F | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This includes evaluating the quality of our MaskRCNN-based perception module (as well as a Detic-based perception model) on real world images, comparing APM to ... | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We considered two broad ways of putting together such a system: a modular approach and an end-to-end learning approach, bat ultimately favored a modular ... | Overall, our system achieves a 61% success rate across 31 unseen cabinets and drawers in unseen real world environments. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (IV. EXPERIMENTS), p. 3 (Figure/Table caption), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (Figure/Table caption) |
| Primary metric/result | Fig. 2: MOSART Design. The perception module outputs 3D articulation parameters in the robot frame using RGB-D images. The robot then navigates to the ... | numeric claim only at cited anchor | p. 3 (Figure/Table caption) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Other failures were during execution, where the handle would slip out, and during navigation, where navigating ‘on carpets was less accurate than on tiles. | p. 10 (Discussion) |
| body limitation/failure cue | Finally, there are limitations of the embodiment we use (e.g. it cannot reach cabinets high up, or exert enough force to pull open fridge ... | p. 9 (V. Limitations) |
| body limitation/failure cue | Figure 8. 59% of failures (ie. 7 failures) are due to perception, including various kinds of failures, such as failure to detect meshed cabinets ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | Grasping failures accounted for approximately 25% of all observed failures, underscoring the inherent difficulty of achieving precise, last-centimeter adjustments required for successful grasping. | p. 10 (Discussion) |
| body limitation/failure cue | We then study the generalization of our pipeline to other articulation types and diverse handles (Section IV-E), before wwe analyze the failure modes of ... | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | Section IV-F° provides a extensive discussion of the failure modes | p. 7 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For most successful trials, the robot opens the drawer / cupboard completely (ie. drawers by 35cm and cupboards by 90°) in a graceful manner ... | p. 7 (IV. EXPERIMENTS) |
| We introduce variation in the starting pose of the robot to test the robustness of the approach but use the same starting pose when ... | p. 7 (IV. EXPERIMENTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / Discussion - extractive body cue:** Other failures were during execution, where the handle would slip out, and during navigation, where navigating ‘on carpets was less accurate than on tiles.
- **p. 9 / V. Limitations - extractive body cue:** Finally, there are limitations of the embodiment we use (e.g. it cannot reach cabinets high up, or exert enough force to pull open fridge doors).
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 8. 59% of failures (ie. 7 failures) are due to perception, including various kinds of failures, such as failure to detect meshed cabinets (2/7), ...
- **p. 10 / Discussion - extractive body cue:** Grasping failures accounted for approximately 25% of all observed failures, underscoring the inherent difficulty of achieving precise, last-centimeter adjustments required for successful grasping.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We then study the generalization of our pipeline to other articulation types and diverse handles (Section IV-E), before wwe analyze the failure modes of our ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Section IV-F° provides a extensive discussion of the failure modes

- **PDF anchors reviewed:** datasets p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), metrics p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (Figure/Table caption), p. 9 (Figure/Table caption), p. 6 (IV. EXPERIMENTS), p. 10 (Figure/Table caption), baselines p. 6 (IV. EXPERIMENTS), p. 8 (Figure/Table caption), results p. 7 (IV. EXPERIMENTS), p. 3 (Figure/Table caption), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
