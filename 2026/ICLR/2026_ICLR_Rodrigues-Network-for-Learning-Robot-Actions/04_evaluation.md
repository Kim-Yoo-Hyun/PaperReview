# Evaluation - Rodrigues Network for Learning Robot Actions

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=IZHk6BXBST; PDF retrieval source: https://arxiv.org/pdf/2506.02618. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS)): Our network achieves a notable performance improvement while significantly reducing the number of parameters (39.5M vs. ours: 10.7M).

## Evaluation Body Digest

- **p. 7 / 5 EXPERIMENTS - extractive body cue:** In real-world robot learning scenarios, neural backbones typically process observations in 3D Cartesian space (e.g., point clouds) and output control commands as target joint angles.
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** (ii) Can this inductive bias improve the understanding and prediction of robot actions in realistic task scenarios?
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** We evaluate our Rodrigues Network on a set of different tasks, ranging from forward kinematics and motion prediction (Section 5.1), to imitation learning in robotics ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** This task uses a 6-DoF UR5 robotic arm.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Benchmark We construct a suite of five manipulation tasks from ManiSkill (Mu et al., 2021) using a 7-DoF Franka arm with a 1-DoF Panda gripper, ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** We integrate the Rodrigues Network as a backbone into the Diffusion Policy (Chi et al., 2023), one of the state-of-the-art imitation learning frameworks, and test ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Therefore, our approach is not limited to robotic applications, demonstrating its versatility and applicability to graphics-related tasks as well.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Many state-of-the-art networks in robot learning build upon architectural designs originally developed for other domains, such as vision and language.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** 5 EXPERIMENTS (p. 6); C EXPERIMENT SETTINGS (p. 15); 6 Evaluation (p. 16).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our network achieves a notable performance improvement while significantly reducing the number of parameters (39.5M vs. ours: 10.7M). | p. 9 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results and analysis As shown in Table 2, Diffusion Policy (Chi et al., 2023) with the Rodrigues Network backbone achieves overall state-of-the-art performance, demonstrating ... | p. 8 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Performance is measured by running 100 evaluation rollouts in simulation, and all models are trained with 5 random seeds to report the mean and ... | p. 8 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Figure 3a, the Rodrigues Network achieves significantly lower prediction error than competing architectures, indicating superior precision in modeling forward kinematics. | p. 6 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The Rodrigues network achieves significantly lower error (left) with faster convergence during training (right). | p. 7 (5 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 7 / 5 EXPERIMENTS - extractive body cue:** In real-world robot learning scenarios, neural backbones typically process observations in 3D Cartesian space (e.g., point clouds) and output control commands as target joint angles.
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** (ii) Can this inductive bias improve the understanding and prediction of robot actions in realistic task scenarios?
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** We evaluate our Rodrigues Network on a set of different tasks, ranging from forward kinematics and motion prediction (Section 5.1), to imitation learning in robotics ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** This task uses a 6-DoF UR5 robotic arm.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Benchmark We construct a suite of five manipulation tasks from ManiSkill (Mu et al., 2021) using a 7-DoF Franka arm with a 1-DoF Panda gripper, ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** We integrate the Rodrigues Network as a backbone into the Diffusion Policy (Chi et al., 2023), one of the state-of-the-art imitation learning frameworks, and test ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Therefore, our approach is not limited to robotic applications, demonstrating its versatility and applicability to graphics-related tasks as well.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Many state-of-the-art networks in robot learning build upon architectural designs originally developed for other domains, such as vision and language.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: We introduce the Neural Rodrigues Operator, a learnable extension of the classical Rodrigues' Rotation Formula from robot control, where the original coefficients are ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: Rodrigues Block. It comprises three components: a Rodrigues Layer for passing infor- mation from joints to links, constructed with our Multi-Channel Neural Rodrigues ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Fitting forward kinematics with different network backbones (MSE↓). The Rodrigues network achieves significantly lower error (left) with faster convergence during training (right). MLP ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Visualization of forward kinematics prediction on an example configuration. Errors are plotted on each link with color scales, with darker colors indicating larger ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Motion prediction in Cartesian space with trainset size = 105. Backbone ErrorT (mm) ErrorR (◦) Errorθ (◦) MSE (1e-6) Train MSE (1e-6) MLP
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Results for motion prediction in Cartesian space. 5.2 ROBOTIC MANIPULATION WITH IMITATION LEARNING Next, we evaluate whether our method benefits realistic robotic applications. ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Baseline comparisons on the imitation learning benchmark. Simulated success rate.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Baseline comparisons on the FreiHAND dataset. We use the standard protocol and report metrics on 3D joint and 3D mesh accuracy. PA-MPVPE and ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In real-world robot learning scenarios, neural backbones typically process observations in 3D Cartesian space (e.g., point clouds) and output control commands as target joint ... | embodiment, simulator version and control stack | p. 7 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS) |
| Task/environment | (ii) Can this inductive bias improve the understanding and prediction of robot actions in realistic task scenarios? | reset, timeout, object/scene variation | p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 2 (1 INTRODUCTION), p. 4 (3.1 BACKGROUND) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 5 (3.1 BACKGROUND), p. 5 (3.1 BACKGROUND) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Performance is measured by running 100 evaluation rollouts in simulation, and all models are trained with 5 random seeds to report the mean and ... | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| Table 2: Baseline comparisons on the imitation learning benchmark. Simulated success rate. | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| As shown in Figure 3a, the Rodrigues Network achieves significantly lower prediction error than competing architectures, indicating superior precision in modeling forward kinematics. | definition/direction/unit from same section | p. 6 (5 EXPERIMENTS) |
| As shown in Table 1, the Rodrigues Network achieves the lowest training loss and test errors when trained on a pre-collected dataset of 105 ... | definition/direction/unit from same section | p. 7 (5 EXPERIMENTS) |
| 103 104 105 106 Trainset size 10 5 10 4 10 3 Test MSE Test error vs trainset size MLP GCN BoT Transformer Rodrigues ... | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| Errors are plotted on each link with color scales, with darker colors indicating larger errors. | definition/direction/unit from same section | p. 7 (5 EXPERIMENTS) |
| We use the standard protocol and report metrics on 3D joint and 3D mesh accuracy. | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| Moreover, its training loss decreases much faster (Figure 3b), demonstrating better data efficiency. | definition/direction/unit from same section | p. 6 (5 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to the strongest baseline, HaMeR, our approach outperforms both the results reported in the original paper and our reproduced implementation. | comparison identity and matched condition | p. 9 (5 EXPERIMENTS) |
| Notably, its test MSE is lower than the train MSE of all baseline models, indicating that the Rodrigues Network not only fits the data ... | comparison identity and matched condition | p. 7 (5 EXPERIMENTS) |
| Method PushCube PickCube StackCube PegInsertionSide PlugCharger Average Transformer-DP 0.98 ±0.02 0.63 ±0.05 0.38 ±0.02 0.18 ±0.05 0.04 ±0.02 0.44 UNet-DP 1.00 ±0.00 0.85 ±0.03 ... | comparison identity and matched condition | p. 9 (5 EXPERIMENTS) |
| GCN baselines produce visible artifacts, and all four baseline methods accumulate substantial error near the fingertips. | comparison identity and matched condition | p. 7 (5 EXPERIMENTS) |
| Baseline architectures include the U-Net and Transformer designs from the original Diffusion Policy paper. | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |
| We integrate the Rodrigues Network as a backbone into the Diffusion Policy (Chi et al., 2023), one of the state-of-the-art imitation learning frameworks, and ... | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Additional studies on ablations and hyperparameter sensitivity are provided in the supplementary material. | component/input/data sensitivity | p. 6 (5 EXPERIMENTS) |
| Notably, its test MSE is lower than the train MSE of all baseline models, indicating that the Rodrigues Network not only fits the data ... | component/input/data sensitivity | p. 7 (5 EXPERIMENTS) |
| Table 11: Ablation studies for motion prediction in Cartesian space with trainset size = 105. We remove the Rodrigues Layer (R Layer), Joint Layer ... | component/input/data sensitivity | p. 21 (Figure/Table caption) |
| These synthetic tasks provide a clean environment to directly evaluate network expressivity without other factors. | component/input/data sensitivity | p. 6 (5 EXPERIMENTS) |
| To isolate the impact of the neural backbone, we keep the outer framework and all other components fixed, modifying only the denoising network. | component/input/data sensitivity | p. 8 (5 EXPERIMENTS) |
| Our method replaces these with the Rodrigues Network, which takes the current observation, denoising timestep, and a noisy action as inputs and predicts the ... | component/input/data sensitivity | p. 8 (5 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To this end, we propose the Neural Rodrigues Operator, a learnable generalization of the classical forward kinematics operation, designed to inject kinematics-aware inductive bias ... | Our network achieves a notable performance improvement while significantly reducing the number of parameters (39.5M vs. ours: 10.7M). | PDF body cue; verify exact table/figure and matched conditions | p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Primary metric/result | Results and analysis As shown in Table 2, Diffusion Policy (Chi et al., 2023) with the Rodrigues Network backbone achieves overall state-of-the-art performance, demonstrating ... | numeric claim only at cited anchor | p. 8 (5 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** The network is given the first 8 frames of joint angles and tasked with predicting the remaining 8, also in joint space.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** As shown in Table 1, the Rodrigues Network achieves the lowest training loss and test errors when trained on a pre-collected dataset of 105 trajectories.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Backbone ErrorT (mm) ErrorR (◦) Errorθ (◦) MSE (1e-6) Train MSE (1e-6) MLP 3.49 ±0.33 0.46 ±0.05 0.17 ±0.00 22.52 ±0.95 12.47 ±0.73 GCN 3.55 ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** For each task, we collect 100-500 demonstration trajectories using motion planning, with each trajectory spanning 200 steps.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Method PushCube PickCube StackCube PegInsertionSide PlugCharger Average Transformer-DP 0.98 ±0.02 0.63 ±0.05 0.38 ±0.02 0.18 ±0.05 0.04 ±0.02 0.44 UNet-DP 1.00 ±0.00 0.85 ±0.03 0.37 ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Second, we showcase our effectiveness in realistic robot-learning scenarios with imitation learning on 5 robot manipulation tasks.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Our method replaces these with the Rodrigues Network, which takes the current observation, denoising timestep, and a noisy action as inputs and predicts the ... | p. 8 (5 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Additional studies on ablations and hyperparameter sensitivity are provided in the supplementary material. | p. 6 (5 EXPERIMENTS) |
| For model hyperparameters and training settings, please refer to Sections C.1 and D.1 of the supplementary material. | p. 6 (5 EXPERIMENTS) |
| Refer to Sections C.2 and D.2 of the supplementary for details on training, model parameter count control, and runtime comparisons. | p. 7 (5 EXPERIMENTS) |
| Implementation details are provided in Section D.3 of the supplementary material. | p. 8 (5 EXPERIMENTS) |
| These results suggest that the benefits of the Rodrigues Decoder are task-dependent. | p. 8 (5 EXPERIMENTS) |
| Compared to the strongest baseline, HaMeR, our approach outperforms both the results reported in the original paper and our reproduced implementation. | p. 9 (5 EXPERIMENTS) |
| Additionally, we show our network achieving state-of-the-art results in human hand pose estimation from images, where the articulated actor is no longer a robot, ... | p. 2 (1 INTRODUCTION) |
| Given the pose of the base link P0, the poses of the descendant links can be computed recursively from parents to children. | p. 3 (3.1 BACKGROUND) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Our method replaces these with the Rodrigues Network, which takes the current observation, denoising timestep, and a noisy action as inputs and predicts the corresponding ...

- **Evidence anchors reviewed:** datasets p. 7 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), metrics p. 8 (5 EXPERIMENTS), p. 9 (Figure/Table caption), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), baselines p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), results p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
