# Evaluation - GRaD-Nav: Efficiently Learning Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2503.03984; PDF retrieval source: https://arxiv.org/pdf/2503.03984. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (IV. EXPERIMENTAL RESULTS), p. 7 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS), p. 6 (IV. EXPERIMENTAL RESULTS), p. 7 (IV. EXPERIMENTAL RESULTS)): The experiment results show that our proposed method achieves the highest training and evaluation rewards as well as success rate on both trajectories among all methods.

## Evaluation Body Digest

- **p. 7 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** 7: Robot hardware experiments of drone flying through middle gate.
- **p. 7 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** 5: Comparison on drone's first person perspective image rendered with 3DGS in simulator (left) and captured with Intel Realsense D435 camera in real robot deployment ...
- **p. 5 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** It is to be noted that BPTT samples the whole trajectory for policy updating, meaning the horizon length equals the episode length, which can take ...
- **p. 5 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** 2: Sample efficiency and wall-clock time comparison benchmark of different algorithms on drone's vision-based end-to-end navigation policy training.
- **p. 6 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** 3: Example success trajectories in hybrid simulation environments achieved by the proposed method.
- **p. 6 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** Without any prior environmentalrelated information like the map's name, gate position, or reference trajectory, the policy can only access the first person perspective RGB information ...
- **p. 6 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** Our ablation test metrics include: (i) training reward, (ii) test reward, and (iii) test success rate.
- **p. 6 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** Right gate Methods Training reward Evaluation reward Success rate Training reward Evaluation reward Success rate w/o visual obs.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** IV. EXPERIMENTAL RESULTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTAL RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The experiment results show that our proposed method achieves the highest training and evaluation rewards as well as success rate on both trajectories among ... | p. 6 (IV. EXPERIMENTAL RESULTS) |
| IV. EXPERIMENTAL RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | By comparing three methods' real robot test performance in Table V, we can conclude that (i) the sim-to-real gap of our method is reasonably ... | p. 7 (IV. EXPERIMENTAL RESULTS) |
| IV. EXPERIMENTAL RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The experiment results in Fig.2 show that (i) non-differentiable RL can struggle to train a satisfactory policy for this end-to-end visual navigation task within ... | p. 5 (IV. EXPERIMENTAL RESULTS) |
| IV. EXPERIMENTAL RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | 3: Example success trajectories in hybrid simulation environments achieved by the proposed method. | p. 6 (IV. EXPERIMENTAL RESULTS) |
| IV. EXPERIMENTAL RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Methods Success rate (sim. / real) Left gate Middle gate Right gate w/o RGB; w/ depth 4/10 / 1/10 7/10 / 1/10 5/10 / ... | p. 7 (IV. EXPERIMENTAL RESULTS) |

## Dataset / Benchmark Role

- **p. 7 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** 7: Robot hardware experiments of drone flying through middle gate.
- **p. 7 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** 5: Comparison on drone's first person perspective image rendered with 3DGS in simulator (left) and captured with Intel Realsense D435 camera in real robot deployment ...
- **p. 5 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** It is to be noted that BPTT samples the whole trajectory for policy updating, meaning the horizon length equals the episode length, which can take ...
- **p. 5 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** 2: Sample efficiency and wall-clock time comparison benchmark of different algorithms on drone's vision-based end-to-end navigation policy training.
- **p. 6 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** 3: Example success trajectories in hybrid simulation environments achieved by the proposed method.
- **p. 6 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** Without any prior environmentalrelated information like the map's name, gate position, or reference trajectory, the policy can only access the first person perspective RGB information ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 2: Sample efficiency and wall-clock time comparison benchmark of different algorithms on drone's vision-based end-to-end navigation policy training.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 3: Example success trajectories in hybrid simulation environments achieved by the proposed method. The left one is "middle gate" and the right one is ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 4: A generalizable policy flying through gates positioned at varying locations with diverse distractor objects in the scene. The colored trajectory represents the drone's ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 5: Comparison on drone's first person perspective image rendered with 3DGS in simulator (left) and captured with In- tel Realsense D435 camera in real ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 6: The drone's first-person views at three different stages during the real-robot experiment, along with the PCA visualization of the latent vector zt from ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 7: Robot hardware experiments of drone flying through middle gate. TABLE V: Experimental results of generalizable policies trained using different methods. In simulation experiments, ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 7: Robot hardware experiments of drone flying through middle gate. | embodiment, simulator version and control stack | p. 7 (IV. EXPERIMENTAL RESULTS), p. 7 (IV. EXPERIMENTAL RESULTS) |
| Task/environment | 5: Comparison on drone's first person perspective image rendered with 3DGS in simulator (left) and captured with Intel Realsense D435 camera in real robot ... | reset, timeout, object/scene variation | p. 7 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 1 (I. INTRODUCTION), p. 3 (III. METHOD) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 2 (II. BACKGROUND), p. 2 (II. BACKGROUND) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Our ablation test metrics include: (i) training reward, (ii) test reward, and (iii) test success rate. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTAL RESULTS) |
| Right gate Methods Training reward Evaluation reward Success rate Training reward Evaluation reward Success rate w/o visual obs. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTAL RESULTS) |
| By comparing three methods' real robot test performance in Table V, we can conclude that (i) the sim-to-real gap of our method is reasonably ... | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTAL RESULTS) |
| Methods Success rate (sim. / real) Left gate Middle gate Right gate w/o RGB; w/ depth 4/10 / 1/10 7/10 / 1/10 5/10 / ... | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTAL RESULTS) |
| 0 1 2 3 4 5 6 7 Simulation Steps (106) 1e6 0 1000 2000 3000 4000 Reward 3.5 hours 22 hours 15 hours ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTAL RESULTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Without CENet, our method can still train a policy network that achieves high rewards compared to other ablation cases. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTAL RESULTS) |
| Training efficiency comparison with other methods To validate GRaD-Nav's training efficiency, we compared our method with other differentiable and nondifferentiable RL algorithms. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTAL RESULTS) |
| The experiment results in Fig.2 show that (i) non-differentiable RL can struggle to train a satisfactory policy for this end-to-end visual navigation task within ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENTAL RESULTS) |
| Our ablation test metrics include: (i) training reward, (ii) test reward, and (iii) test success rate. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTAL RESULTS) |
| In real-world experiments, the drone was initialized under the same conditions for each test, and success was determined by whether it flew through the ... | comparison identity and matched condition | p. 7 (IV. EXPERIMENTAL RESULTS) |
| 5: Comparison on drone's first person perspective image rendered with 3DGS in simulator (left) and captured with Intel Realsense D435 camera in real robot ... | comparison identity and matched condition | p. 7 (IV. EXPERIMENTAL RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Without CENet, our method can still train a policy network that achieves high rewards compared to other ablation cases. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTAL RESULTS) |
| Ablation study of our methods To validate that each module of our method is not redundant but necessary for safe navigation, and to determine ... | component/input/data sensitivity | p. 5 (IV. EXPERIMENTAL RESULTS) |
| 4 demonstrates the generalizable policy's variant trajectories in different environments. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTAL RESULTS) |
| In real-world experiments, the drone was initialized under the same conditions for each test, and success was determined by whether it flew through the ... | component/input/data sensitivity | p. 7 (IV. EXPERIMENTAL RESULTS) |
| 5: Comparison on drone's first person perspective image rendered with 3DGS in simulator (left) and captured with Intel Realsense D435 camera in real robot ... | component/input/data sensitivity | p. 7 (IV. EXPERIMENTAL RESULTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions are: • We introduce a simulator for training robot vision-based control policies by integrating 3DGS for high-fidelity visuals with a differentiable ... | The experiment results show that our proposed method achieves the highest training and evaluation rewards as well as success rate on both trajectories among ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (IV. EXPERIMENTAL RESULTS), p. 7 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS), p. 6 (IV. EXPERIMENTAL RESULTS), p. 7 (IV. EXPERIMENTAL RESULTS) |
| Primary metric/result | By comparing three methods' real robot test performance in Table V, we can conclude that (i) the sim-to-real gap of our method is reasonably ... | numeric claim only at cited anchor | p. 7 (IV. EXPERIMENTAL RESULTS) |

- Numeric sentences retained from the body:
- **p. 5 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** The experiment results in Fig.2 show that (i) non-differentiable RL can struggle to train a satisfactory policy for this end-to-end visual navigation task within 1 ...
- **p. 5 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** 0 1 2 3 4 5 6 7 Simulation Steps (106) 1e6 0 1000 2000 3000 4000 Reward 3.5 hours 22 hours 15 hours Algorithms ...
- **p. 6 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** 3720.1 3761.4 ± 60.1 0/10 4162.4 4148.3 ± 76.3 0/10 w/o RGB; w/ depth 3828.6 3805.7 ± 45.9 0/10 4168.2 4161.7 ± 27.5 0/10 w/o ...
- **p. 6 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** We train each policy with the same reward function as in Table II and the same hyperparameters setting as Table VI for 600 epochs.
- **p. 6 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** The onboard policy inference frequency is 30 Hz.
- **p. 3 / III. METHOD - extractive PDF cue:** When parallel simulating 128 drones flying in a highly unstructured and cluttered area (room size ≈100 m2, 3DGS model size ≈ 1.5GB), setting the simulated ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Limitations: Our method relies on hand-crafted reward shaping (e.g., trajectory waypoints), limiting it to singletask execution like gate traversal. | p. 7 (V. CONCLUSIONS) |
| body limitation/failure cue | All of the failure cases without CENet on two trajectories "crash" due to unsuccessful obstacle avoidance. | p. 6 (IV. EXPERIMENTAL RESULTS) |
| body limitation/failure cue | Future work includes (i) multi-task training with language input, (ii) improving generalization via stronger backbones and diverse environments, and (iii) extending to contact-rich tasks ... | p. 7 (V. CONCLUSIONS) |
| body limitation/failure cue | As visual perception is our navigation policy's major sensor input, it is not surprising that the policy without visual observation cannot conduct successful navigation. | p. 6 (IV. EXPERIMENTAL RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We trained the policy in each environment for 5 times, 100 epochs per time; we return the learning rate to the initial value during ... | p. 5 (4) Curriculum training for generalizable navigation pol) |
| We train each policy with the same reward function as in Table II and the same hyperparameters setting as Table VI for 600 epochs. | p. 6 (IV. EXPERIMENTAL RESULTS) |
| The experiment results in Fig.2 show that (i) non-differentiable RL can struggle to train a satisfactory policy for this end-to-end visual navigation task within ... | p. 5 (IV. EXPERIMENTAL RESULTS) |
| Training reward is the highest reward policy achieved during training time. | p. 6 (IV. EXPERIMENTAL RESULTS) |
| 7: Robot hardware experiments of drone flying through middle gate. | p. 7 (IV. EXPERIMENTAL RESULTS) |
| 6: The drone's first-person views at three different stages during the real-robot experiment, along with the PCA visualization of the latent vector zt from ... | p. 7 (IV. EXPERIMENTAL RESULTS) |
| 3) Implementation datails: We used a standard opensource codebase, Nerfstudio [34] as our 3DGS training and inference platform. | p. 3 (III. METHOD) |
| When parallel simulating 128 drones flying in a highly unstructured and cluttered area (room size ≈100 m2, 3DGS model size ≈ 1.5GB), setting the ... | p. 3 (III. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / V. CONCLUSIONS - extractive PDF cue:** Limitations: Our method relies on hand-crafted reward shaping (e.g., trajectory waypoints), limiting it to singletask execution like gate traversal.
- **p. 6 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** All of the failure cases without CENet on two trajectories "crash" due to unsuccessful obstacle avoidance.
- **p. 7 / V. CONCLUSIONS - extractive PDF cue:** Future work includes (i) multi-task training with language input, (ii) improving generalization via stronger backbones and diverse environments, and (iii) extending to contact-rich tasks such ...
- **p. 6 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** As visual perception is our navigation policy's major sensor input, it is not surprising that the policy without visual observation cannot conduct successful navigation.

- **PDF anchors reviewed:** datasets p. 7 (IV. EXPERIMENTAL RESULTS), p. 7 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS), p. 6 (IV. EXPERIMENTAL RESULTS), p. 6 (IV. EXPERIMENTAL RESULTS), metrics p. 6 (IV. EXPERIMENTAL RESULTS), p. 6 (IV. EXPERIMENTAL RESULTS), p. 7 (IV. EXPERIMENTAL RESULTS), p. 7 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS), baselines p. 6 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS), p. 6 (IV. EXPERIMENTAL RESULTS), p. 7 (IV. EXPERIMENTAL RESULTS), p. 7 (IV. EXPERIMENTAL RESULTS), results p. 6 (IV. EXPERIMENTAL RESULTS), p. 7 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS), p. 6 (IV. EXPERIMENTAL RESULTS), p. 7 (IV. EXPERIMENTAL RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
