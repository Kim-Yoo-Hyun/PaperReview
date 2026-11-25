# Evaluation - Failure Prediction with Statistical Guarantees for Vision-Based Robot Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2202.05894; PDF retrieval source: https://arxiv.org/pdf/2202.05894. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 8 (V. EXPERIMENTAL RESULTS), p. 7 (Figure/Table caption), p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS)): In order to evaluate the failure predictor on policies with different task success rates, we choose three different policies saved at different epochs during training.

## Evaluation Body Digest

- **p. 8 / V. EXPERIMENTAL RESULTS - extractive body cue:** In order to create different environments for the robot, we obtained 50 mugs of diverse geometries from the ShapeNet dataset [49].
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** We also validate the guarantees by evaluating the predictors on test environments in both simulation and on hardware.
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** We train the failure predictor in simulation and apply it on a hardware platform with a Parrot Swing drone (Fig.
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** In this example, we consider a robot arm performing the task of grasping a mug (Fig.
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** We first verify our failure predictors in simulation before testing them on the hardware setup.
- **p. 8 / V. EXPERIMENTAL RESULTS - extractive body cue:** Camera observation (depth not shown) at the last three steps in a trial in the grasping task on the hardware platform.
- **p. 8 / V. EXPERIMENTAL RESULTS - extractive body cue:** In order to evaluate the failure predictor on policies with different task success rates, we choose three different policies saved at different epochs during training.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3. Results of conformal prediction on the toy problem in Sec. IV-C, which hold in expectation over training samples S and a test case ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** V. EXPERIMENTAL RESULTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTAL RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | In order to evaluate the failure predictor on policies with different task success rates, we choose three different policies saved at different epochs during ... | p. 8 (V. EXPERIMENTAL RESULTS) |
| V. EXPERIMENTAL RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We aim to examine the improvement in safety of the policy with the addition of the failure predictor; thus, we test in settings that ... | p. 7 (V. EXPERIMENTAL RESULTS) |
| V. EXPERIMENTAL RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | 5 in the drone example, we achieve strong bounds on conditional misclassification Fig. | p. 8 (V. EXPERIMENTAL RESULTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 5. The dashed lines show the resulting failure predictor's FNR and FPR when the importance of a false negative is varied. The solid ... | p. 7 (Figure/Table caption) |
| V. EXPERIMENTAL RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | In this section, we evaluate our bounds and failure prediction performance in simulation and also present extensive hardware expriments. | p. 6 (V. EXPERIMENTAL RESULTS) |

## Dataset / Benchmark Role

- **p. 8 / V. EXPERIMENTAL RESULTS - extractive body cue:** In order to create different environments for the robot, we obtained 50 mugs of diverse geometries from the ShapeNet dataset [49].
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** We also validate the guarantees by evaluating the predictors on test environments in both simulation and on hardware.
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** We train the failure predictor in simulation and apply it on a hardware platform with a Parrot Swing drone (Fig.
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** In this example, we consider a robot arm performing the task of grasping a mug (Fig.
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** We first verify our failure predictors in simulation before testing them on the hardware setup.
- **p. 8 / V. EXPERIMENTAL RESULTS - extractive body cue:** Camera observation (depth not shown) at the last three steps in a trial in the grasping task on the hardware platform.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. We train a failure predictor which guarantees (with high probability) detection of a failure ahead of time. A policy is tasked with avoiding ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2. Continuum of optimal predictors (red) for varying class population ratios (successes and failures). The failure predictor can perform badly (i.e., on the bottom ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3. Results of conformal prediction on the toy problem in Sec. IV-C, which hold in expectation over training samples S and a test case ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4. (Left) Representative motion primitives for the policy used in the standard setting in the navigation task. (Right) Representative motion primitives from the policy ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5. The dashed lines show the resulting failure predictor's FNR and FPR when the importance of a false negative is varied. The solid lines ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6. (a) Simulation environment in PyBullet simulator (virtual wrist- mounted camera not shown). (b) Real environment with an arm and a wrist- mounted camera ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7. Camera observation (depth not shown) at the last three steps in a trial in the grasping task on the hardware platform. (Top) A ...
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 8. The dashed lines show the resulting failure predictor's FNR and FPR when the importance of a false negative is varied when training in ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In order to create different environments for the robot, we obtained 50 mugs of diverse geometries from the ShapeNet dataset [49]. | embodiment, simulator version and control stack | p. 8 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |
| Task/environment | We also validate the guarantees by evaluating the predictors on test environments in both simulation and on hardware. | reset, timeout, object/scene variation | p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 3 (III. PROBLEM FORMULATION), p. 1 (I. INTRODUCTION) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In order to evaluate the failure predictor on policies with different task success rates, we choose three different policies saved at different epochs during ... | definition/direction/unit from same section | p. 8 (V. EXPERIMENTAL RESULTS) |
| Fig. 3. Results of conformal prediction on the toy problem in Sec. IV-C, which hold in expectation over training samples S and a test ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Through extensive simulation and hardware experiments, we aim to demonstrate strong guarantees on (class-conditional) misclassification error of trained predictors. | definition/direction/unit from same section | p. 6 (V. EXPERIMENTAL RESULTS) |
| We choose the failure predictors with the tightest guaranteed total error rate (i.e. tightest upper bound from (8)). | definition/direction/unit from same section | p. 7 (V. EXPERIMENTAL RESULTS) |
| We obtain strong bounds on the failure predictors' errors, with closely-matching empirical performance along all points along the curve. | definition/direction/unit from same section | p. 7 (V. EXPERIMENTAL RESULTS) |
| (Top) A true-positive trial, where the predictor outputs failure at the last step, and then the right finger of the gripper hits the mug ... | definition/direction/unit from same section | p. 8 (V. EXPERIMENTAL RESULTS) |
| Fig. 2. Continuum of optimal predictors (red) for varying class population ratios (successes and failures). The failure predictor can perform badly (i.e., on the ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Across all three settings, we achieve tight guarantees on failure prediction compared to the true expected failure rate of the policies. | comparison identity and matched condition | p. 8 (V. EXPERIMENTAL RESULTS) |
| When the failure predictor stops the rollout due to a prediction of failure, we re-run the trial without the failure predictor to determine the ... | comparison identity and matched condition | p. 7 (V. EXPERIMENTAL RESULTS) |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| When the failure predictor stops the rollout due to a prediction of failure, we re-run the trial without the failure predictor to determine the ... | component/input/data sensitivity | p. 7 (V. EXPERIMENTAL RESULTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our primary contribution is to develop an approach for learning a failure predictor with guaranteed bounds on error rates, given a black-box control policy ... | In order to evaluate the failure predictor on policies with different task success rates, we choose three different policies saved at different epochs during ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 8 (V. EXPERIMENTAL RESULTS), p. 7 (Figure/Table caption), p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |
| Primary metric/result | We aim to examine the improvement in safety of the policy with the addition of the failure predictor; thus, we test in settings that ... | numeric claim only at cited anchor | p. 7 (V. EXPERIMENTAL RESULTS) |

- Numeric sentences retained from the body:
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** The network receives a new image at a frequency of 20Hz and stacks the four most recent images as input to predict failure or no ...
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** We note TABLE II RESULTS FOR FAILURE PREDICTION ON NAVIGATION TASK Setting Standard Occluded Obstacle True Expected Failure (Sim) 0.253 0.514 Misclassification Bound 0.128 0.154 ...
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** We run 15 trials in each of the settings and show the misclassification error of the failure predictors along with the guarantee on the misclassification ...
- **p. 8 / V. EXPERIMENTAL RESULTS - extractive body cue:** The policy takes a 100×150 pixels RGB-D image from the camera and outputs the desired pose relative to the current pose, (∆x, ∆y, ∆z, ∆ψ), ...
- **p. 8 / V. EXPERIMENTAL RESULTS - extractive body cue:** The results of 30 trials for each setting are shown in Table III (Real).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Bound on Class-Conditional Misclassification Error The example above shows that minimizing the total misclassification error can fail to perform well when the relative importance ... | p. 5 (IV. FAILURE PREDICTION WITH GUARANTEED ERROR) |
| body limitation/failure cue | Thus, if the policy designer has access to a single training dataset to learn a failure predictor, conformal prediction does not guarantee that the ... | p. 6 (IV. FAILURE PREDICTION WITH GUARANTEED ERROR) |
| body limitation/failure cue | We note TABLE II RESULTS FOR FAILURE PREDICTION ON NAVIGATION TASK Setting Standard Occluded Obstacle True Expected Failure (Sim) 0.253 0.514 Misclassification Bound 0.128 ... | p. 7 (V. EXPERIMENTAL RESULTS) |
| body limitation/failure cue | Fig. 1. We train a failure predictor which guarantees (with high probability) detection of a failure ahead of time. A policy is tasked with ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Since the gripper does not reach the mug in the first two out of five steps of the rollout, we only train the failure ... | p. 8 (V. EXPERIMENTAL RESULTS) |
| body limitation/failure cue | BOUNDS Our approach for learning failure predictors with guaranteed error bounds relies on a reduction to results from the PACBayes generalization theory from supervised ... | p. 3 (IV. FAILURE PREDICTION WITH GUARANTEED ERROR) |

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Camera observation (depth not shown) at the last three steps in a trial in the grasping task on the hardware platform. | p. 8 (V. EXPERIMENTAL RESULTS) |
| We then record the resulting trajectories using a Vicon motion capture system and use these trajectories for our simulation experiments (in order to emulate ... | p. 6 (V. EXPERIMENTAL RESULTS) |
| When the failure predictor stops the rollout due to a prediction of failure, we re-run the trial without the failure predictor to determine the ... | p. 7 (V. EXPERIMENTAL RESULTS) |
| We run 15 trials in each of the settings and show the misclassification error of the failure predictors along with the guarantee on the ... | p. 7 (V. EXPERIMENTAL RESULTS) |
| 7 shows the RGB images from the camera and failure predictions at the last three steps of two trials. | p. 8 (V. EXPERIMENTAL RESULTS) |
| Thus these motion primitives capture noise in the hardware dynamics and help to bridge the sim-to-real gap. | p. 6 (V. EXPERIMENTAL RESULTS) |
| Let rf : E × Π →X T × YT denote the function that ‘rolls out' the system with the given policy and the ... | p. 3 (III. PROBLEM FORMULATION) |
| Thus there are four possible outcomes: (1) true positive (1∩1), predicting 1 at least once before failure; (2) true negative (0 ∩0), never predicting ... | p. 3 (III. PROBLEM FORMULATION) |

## Limitations and Verification Questions

- **p. 5 / IV. FAILURE PREDICTION WITH GUARANTEED ERROR - extractive body cue:** Bound on Class-Conditional Misclassification Error The example above shows that minimizing the total misclassification error can fail to perform well when the relative importance of ...
- **p. 6 / IV. FAILURE PREDICTION WITH GUARANTEED ERROR - extractive body cue:** Thus, if the policy designer has access to a single training dataset to learn a failure predictor, conformal prediction does not guarantee that the expected ...
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** We note TABLE II RESULTS FOR FAILURE PREDICTION ON NAVIGATION TASK Setting Standard Occluded Obstacle True Expected Failure (Sim) 0.253 0.514 Misclassification Bound 0.128 0.154 ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. We train a failure predictor which guarantees (with high probability) detection of a failure ahead of time. A policy is tasked with avoiding ...
- **p. 8 / V. EXPERIMENTAL RESULTS - extractive body cue:** Since the gripper does not reach the mug in the first two out of five steps of the rollout, we only train the failure predictor ...
- **p. 3 / IV. FAILURE PREDICTION WITH GUARANTEED ERROR - extractive body cue:** BOUNDS Our approach for learning failure predictors with guaranteed error bounds relies on a reduction to results from the PACBayes generalization theory from supervised learning; ...

- **Evidence anchors reviewed:** datasets p. 8 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 8 (V. EXPERIMENTAL RESULTS), metrics p. 8 (V. EXPERIMENTAL RESULTS), p. 6 (Figure/Table caption), p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 8 (V. EXPERIMENTAL RESULTS), baselines p. 8 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), results p. 8 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 8 (V. EXPERIMENTAL RESULTS), p. 7 (Figure/Table caption), p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS).

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)
