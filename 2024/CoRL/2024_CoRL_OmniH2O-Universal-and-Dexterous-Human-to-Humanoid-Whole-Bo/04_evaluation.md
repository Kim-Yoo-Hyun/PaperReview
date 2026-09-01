# Evaluation - OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=oL1WEZQal8; PDF retrieval source: https://arxiv.org/pdf/2406.08858. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (1 Introduction), p. 7 (Figure/Table caption), p. 21 (Figure/Table caption), p. 8 (1 Introduction), p. 24 (Figure/Table caption), p. 6 (Figure/Table caption)): We draw two key conclusions: (1) The Diffusion Policy significantly outperforms vanilla BC with ResNet; (2) In our LfD training, predicting a sequence of actions is crucial, as it enables ...

## Evaluation Body Digest

- **p. 8 / 1 Introduction - extractive body cue:** We benchmark a variety of imitation learning algorithms on four tasks in our collected dataset (shown in Figure 7), including Diffusion Policy [58] with Denoising ...
- **p. 8 / 1 Introduction - extractive body cue:** (d) Rock-Paper-Scissors (b) Squat (a) Catch-Release (c) Hammer-Catch Figure 7: OmniH2O autonomously conducts four tasks using LfD models trained with our collected data. minutes of ...
- **p. 8 / 1 Introduction - extractive body cue:** To evaluate πLfD, we report the average MSE loss and the success rate in Table 3, where we average the metrics across all tasks.
- **p. 8 / 1 Introduction - extractive body cue:** Metrics All Tasks (a) Ablation on Data size 25%data 50%data 100%data MSE Loss 1.30E-2 7.48E-3 5.25E-4 Succ rate 4/10 6.5/10 8/10 (b) Ablation on Sequence ...
- **p. 21 / Figure/Table caption - extractive body cue:** Table 15: Reward components and weights: penalty rewards for preventing undesired behaviors for sim-to-real transfer, regularization to refine motion, and task reward to achieve successful ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: OmniH2O shows superior robustness against human strikes and different outdoor terrains. History Steps and Architecture. Real-world evaluation in Table 2(b) also shows that ...
- **p. 24 / Figure/Table caption - extractive body cue:** Table 17: Quantitative LfD autonomous agents performance for 4 tasks. Metrics Catch-Release Squat Hammer-Catch Rock-Paper-Scissors (a) Ablation on Data size 25%data
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: (a) OmniH2O enables teleoperating a full-size humanoid robot (Unitree H1) to complete tasks that require both high-precision manipulation and locomotion. (b) OmniH2O also ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 1 Introduction | EMPIRICAL / REAL-ROBOT OR HARDWARE | We draw two key conclusions: (1) The Diffusion Policy significantly outperforms vanilla BC with ResNet; (2) In our LfD training, predicting a sequence of ... | p. 8 (1 Introduction) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5: OmniH2O shows superior robustness against human strikes and different outdoor terrains. History Steps and Architecture. Real-world evaluation in Table 2(b) also shows ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 15: Reward components and weights: penalty rewards for preventing undesired behaviors for sim-to-real transfer, regularization to refine motion, and task reward to achieve ... | p. 21 (Figure/Table caption) |
| 1 Introduction | EMPIRICAL / REAL-ROBOT OR HARDWARE | To evaluate πLfD, we report the average MSE loss and the success rate in Table 3, where we average the metrics across all tasks. | p. 8 (1 Introduction) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 17: Quantitative LfD autonomous agents performance for 4 tasks. Metrics Catch-Release Squat Hammer-Catch Rock-Paper-Scissors (a) Ablation on Data size 25%data | p. 24 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / 1 Introduction - extractive body cue:** We benchmark a variety of imitation learning algorithms on four tasks in our collected dataset (shown in Figure 7), including Diffusion Policy [58] with Denoising ...
- **p. 8 / 1 Introduction - extractive body cue:** (d) Rock-Paper-Scissors (b) Squat (a) Catch-Release (c) Hammer-Catch Figure 7: OmniH2O autonomously conducts four tasks using LfD models trained with our collected data. minutes of ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: (a) OmniH2O enables teleoperating a full-size humanoid robot (Unitree H1) to complete tasks that require both high-precision manipulation and locomotion. (b) OmniH2O also ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: (a) Source motion; (b) Retar- geted motion; (c) Standing variant; (d) Squatting variant. Human Motion Retargeting. We train our motion imitation policy using ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: (a) OmniH2O retargets large-scale human motions and filters out infeasible motions for humanoids. (b) Our sim-to-real policy is distilled through supervised learning from ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Simulation motion imitation evaluation of OmniH2O and baselines on dataset ˆ Q. All sequences Successful sequences
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2: Real-world motion tracking evaluation on 20 standing motions in ˆ Q Tested sequences
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: OmniH2O policy tracks motion goals from a language-based human motion generative model [57]. (a) Disturbances (b) Outdoor Terrains
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: OmniH2O shows superior robustness against human strikes and different outdoor terrains. History Steps and Architecture. Real-world evaluation in Table 2(b) also shows that ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: OmniH2O sends egocentric RGB views to GPT-4o and executes the selected motion primitives. (d) Rock-Paper-Scissors (b) Squat (a) Catch-Release (c) Hammer-Catch

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We benchmark a variety of imitation learning algorithms on four tasks in our collected dataset (shown in Figure 7), including Diffusion Policy [58] with ... | embodiment, simulator version and control stack | p. 8 (1 Introduction), p. 8 (1 Introduction) |
| Task/environment | (d) Rock-Paper-Scissors (b) Squat (a) Catch-Release (c) Hammer-Catch Figure 7: OmniH2O autonomously conducts four tasks using LfD models trained with our collected data. minutes ... | reset, timeout, object/scene variation | p. 8 (1 Introduction) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 8 (1 Introduction), p. 3 (1 Introduction) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 5 (1 Introduction), p. 6 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| To evaluate πLfD, we report the average MSE loss and the success rate in Table 3, where we average the metrics across all tasks. | definition/direction/unit from same section | p. 8 (1 Introduction) |
| Metrics All Tasks (a) Ablation on Data size 25%data 50%data 100%data MSE Loss 1.30E-2 7.48E-3 5.25E-4 Succ rate 4/10 6.5/10 8/10 (b) Ablation on ... | definition/direction/unit from same section | p. 8 (1 Introduction) |
| Table 15: Reward components and weights: penalty rewards for preventing undesired behaviors for sim-to-real transfer, regularization to refine motion, and task reward to achieve ... | definition/direction/unit from same section | p. 21 (Figure/Table caption) |
| Figure 5: OmniH2O shows superior robustness against human strikes and different outdoor terrains. History Steps and Architecture. Real-world evaluation in Table 2(b) also shows ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 17: Quantitative LfD autonomous agents performance for 4 tasks. Metrics Catch-Release Squat Hammer-Catch Rock-Paper-Scissors (a) Ablation on Data size 25%data | definition/direction/unit from same section | p. 24 (Figure/Table caption) |
| Figure 1: (a) OmniH2O enables teleoperating a full-size humanoid robot (Unitree H1) to complete tasks that require both high-precision manipulation and locomotion. (b) OmniH2O ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Table 1: Simulation motion imitation evaluation of OmniH2O and baselines on dataset ˆ Q. All sequences Successful sequences | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 16: Here we describe the range of dynamics randomization for simulated dynamics randomization, ex- ternal perturbation, and terrain, which are important for sim-to-real ... | definition/direction/unit from same section | p. 22 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 8: The illustration of using ZED camera VIO module, and the comparison of the velocity estimation of VIO with neural state estimators. H ... | comparison identity and matched condition | p. 22 (Figure/Table caption) |
| Table 1: Simulation motion imitation evaluation of OmniH2O and baselines on dataset ˆ Q. All sequences Successful sequences | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Compared to directly using the πLfD to output joint actuation, we leverage the trained motor skills in πOmniH2O, which drastically reduces the number of ... | comparison identity and matched condition | p. 8 (1 Introduction) |
| We draw two key conclusions: (1) The Diffusion Policy significantly outperforms vanilla BC with ResNet; (2) In our LfD training, predicting a sequence of ... | comparison identity and matched condition | p. 8 (1 Introduction) |
| Figure 9: The ablation of data augmentation. I Additional Physical Teleoperation Results Additional VR-based and RGB-based teleoperation demo are shown in Figure 10. 22 | comparison identity and matched condition | p. 22 (Figure/Table caption) |
| Table 17: Quantitative LfD autonomous agents performance for 4 tasks. Metrics Catch-Release Squat Hammer-Catch Rock-Paper-Scissors (a) Ablation on Data size 25%data | comparison identity and matched condition | p. 24 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 8: The illustration of using ZED camera VIO module, and the comparison of the velocity estimation of VIO with neural state estimators. H ... | component/input/data sensitivity | p. 22 (Figure/Table caption) |
| Figure 2: (a) Source motion; (b) Retar- geted motion; (c) Standing variant; (d) Squatting variant. Human Motion Retargeting. We train our motion imitation policy ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| Table 3: Quantitative LfD average per- formance on 4 tasks over 10 runs. Metrics All Tasks (a) Ablation on Data size 25%data 50%data 100%data | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Metrics All Tasks (a) Ablation on Data size 25%data 50%data 100%data MSE Loss 1.30E-2 7.48E-3 5.25E-4 Succ rate 4/10 6.5/10 8/10 (b) Ablation on ... | component/input/data sensitivity | p. 8 (1 Introduction) |
| Figure 9: The ablation of data augmentation. I Additional Physical Teleoperation Results Additional VR-based and RGB-based teleoperation demo are shown in Figure 10. 22 | component/input/data sensitivity | p. 22 (Figure/Table caption) |
| Table 17: Quantitative LfD autonomous agents performance for 4 tasks. Metrics Catch-Release Squat Hammer-Catch Rock-Paper-Scissors (a) Ablation on Data size 25%data | component/input/data sensitivity | p. 24 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In conclusion, our contributions are as follows: (1) We propose a pipeline to train a robust humanoid control policy that supports whole-body dexterous loco-manipulation ... | We draw two key conclusions: (1) The Diffusion Policy significantly outperforms vanilla BC with ResNet; (2) In our LfD training, predicting a sequence of ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (1 Introduction), p. 7 (Figure/Table caption), p. 21 (Figure/Table caption), p. 8 (1 Introduction), p. 24 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Primary metric/result | Figure 5: OmniH2O shows superior robustness against human strikes and different outdoor terrains. History Steps and Architecture. Real-world evaluation in Table 2(b) also shows ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 8 / 1 Introduction - extractive body cue:** Metrics All Tasks (a) Ablation on Data size 25%data 50%data 100%data MSE Loss 1.30E-2 7.48E-3 5.25E-4 Succ rate 4/10 6.5/10 8/10 (b) Ablation on Sequence ...
- **p. 6 / 1 Introduction - extractive body cue:** In Table 1(b), we experiment with varying history steps (0, 5, 25, 50) and find that 25 steps achieve the best balance between performance and ...
- **p. 6 / 1 Introduction - extractive body cue:** 4.1.2 Real-world Motion-Tracking Results Table 2: Real-world motion tracking evaluation on 20 standing motions in ˆ Q Tested sequences Method State Dimensions Eg-mpjpe ↓Empjpe ↓Eacc ...
- **p. 7 / 1 Introduction - extractive body cue:** Real-world evaluation in Table 2(b) also shows that our choice of 25 steps of history achieves the best performance.
- **p. 7 / 1 Introduction - extractive body cue:** Our dataset includes paired RGBD images from the head-mounted camera, the motion goals of H1's head and hands with respect to the root, and joint ...
- **p. 8 / 1 Introduction - extractive body cue:** Metrics All Tasks (a) Ablation on Data size 25%data 50%data 100%data MSE Loss 1.30E-2 7.48E-3 5.25E-4 Succ rate 4/10 6.5/10 8/10 (b) Ablation on Sequence ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Another limitation is safety; although the OmniH2O policy has shown great robustness, we do not have guarantees or safety checks for extreme disturbances or ... | p. 8 (1 Introduction) |
| body limitation/failure cue | 5 Limitations and Future Work Summary. | p. 8 (1 Introduction) |
| body limitation/failure cue | 2 Unable to finish the real-world test due to falling on the ground. | p. 6 (1 Introduction) |
| body limitation/failure cue | OmniH2O demonstrates great robustness under disturbances and unstructured terrains. | p. 7 (1 Introduction) |
| body limitation/failure cue | (a) Disturbances (b) Outdoor Terrains Figure 5: OmniH2O shows superior robustness against human strikes and different outdoor terrains. | p. 7 (1 Introduction) |
| body limitation/failure cue | In Table 1(d), we find that linear velocity information does not boost performance in simulation, but it introduces significant challenges in real-world deployment (details ... | p. 6 (1 Introduction) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Detailed state-space composition (Appendix C), ablation setup (Appendix B), hyperparameters (Appendix K), and hardware configuration (Appendix A) are summarized in the Appendix. | p. 5 (1 Introduction) |
| One major drawback of H2O is that the humanoid tends to take small adjustment steps instead of standing still. | p. 3 (1 Introduction) |
| To encourage standing still and taking large steps during locomotion, we propose a key reward function max feet height for each step. | p. 4 (1 Introduction) |
| Using the reference pose ˆq1:T and simulated humanoid states sp 1:T , we can compute the privileged states sg-privileged t , sp-privileged t ←(sp ... | p. 5 (1 Introduction) |
| Ablation on History Steps/Architecture. | p. 6 (1 Introduction) |
| In Table 1(b), we experiment with varying history steps (0, 5, 25, 50) and find that 25 steps achieve the best balance between performance ... | p. 6 (1 Introduction) |
| Real-world evaluation in Table 2(b) also shows that our choice of 25 steps of history achieves the best performance. | p. 7 (1 Introduction) |
| The training hyperparameters are in Appendix L. | p. 8 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 1 Introduction - extractive body cue:** Another limitation is safety; although the OmniH2O policy has shown great robustness, we do not have guarantees or safety checks for extreme disturbances or out-of-distribution ...
- **p. 8 / 1 Introduction - extractive body cue:** 5 Limitations and Future Work Summary.
- **p. 6 / 1 Introduction - extractive body cue:** 2 Unable to finish the real-world test due to falling on the ground.
- **p. 7 / 1 Introduction - extractive body cue:** OmniH2O demonstrates great robustness under disturbances and unstructured terrains.
- **p. 7 / 1 Introduction - extractive body cue:** (a) Disturbances (b) Outdoor Terrains Figure 5: OmniH2O shows superior robustness against human strikes and different outdoor terrains.
- **p. 6 / 1 Introduction - extractive body cue:** In Table 1(d), we find that linear velocity information does not boost performance in simulation, but it introduces significant challenges in real-world deployment (details illustrated ...

- **PDF anchors reviewed:** datasets p. 8 (1 Introduction), p. 8 (1 Introduction), metrics p. 8 (1 Introduction), p. 8 (1 Introduction), p. 21 (Figure/Table caption), p. 7 (Figure/Table caption), p. 24 (Figure/Table caption), p. 1 (Figure/Table caption), baselines p. 22 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (1 Introduction), p. 8 (1 Introduction), p. 22 (Figure/Table caption), p. 24 (Figure/Table caption), results p. 8 (1 Introduction), p. 7 (Figure/Table caption), p. 21 (Figure/Table caption), p. 8 (1 Introduction), p. 24 (Figure/Table caption), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
