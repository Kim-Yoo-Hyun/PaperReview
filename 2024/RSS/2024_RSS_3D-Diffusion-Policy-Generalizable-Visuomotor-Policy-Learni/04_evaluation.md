# Evaluation - 3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p067.html; PDF retrieval source: https://arxiv.org/pdf/2403.03954.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 4 (Figure/Table caption), p. 5 (IV. SIMULATION EXPERIMENTS), p. 5 (IV. SIMULATION EXPERIMENTS), p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 4 (IV. SIMULATION EXPERIMENTS)): Fig. 2: Overview of 3D Diffusion Policy (DP3). Above: In the training phase, DP3 simultaneously trains its perception module and decision-making process in an end-to-end manner using expert demonstrations. During ...

## Evaluation Body Digest

- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** Simulation Benchmark (72 Tasks) Domain Robo Object Simulator ActD #Task #Demo Adroit Shadow Rigid/Art MuJoCo 28 3 10 Bi-DexHands Shadow Rigid/Art IsaacGym 52 6 10 ...
- **p. 7 / V. REAL WORLD EXPERIMENTS - extractive body cue:** Experiment Setup Real robot benchmark.
- **p. 4 / IV. SIMULATION EXPERIMENTS - extractive body cue:** This discrepancy underscores two key aspects: (a) the importance of real robot experiments and (b) the necessity of large-scale diverse simulation tasks for more sci
- **p. 4 / IV. SIMULATION EXPERIMENTS - extractive body cue:** Though the simulation environments are increasingly realistic nowadays [34, 73, 65, 85], a notable gap between simulation and real-world scenarios persists [80, 30, 7].
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** Therefore, for simulation experiments, we collect in total 72 tasks from 7 domains, covering diverse robotic skills.
- **p. 7 / V. REAL WORLD EXPERIMENTS - extractive body cue:** Our real-world setup and everyday objects used in our tasks are shown in Figure 8.
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** The success rates for experts are given in Appendix C.
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** We report the mean and std of success rates across 3 seeds.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** IV. SIMULATION EXPERIMENTS (p. 4); V. REAL WORLD EXPERIMENTS (p. 7); C. More Simulation Experiments (p. 15).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 2: Overview of 3D Diffusion Policy (DP3). Above: In the training phase, DP3 simultaneously trains its perception module and decision-making process in an ... | p. 4 (Figure/Table caption) |
| IV. SIMULATION EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We observe that DP3 achieves a success rate exceeding 90% in TABLE III: Task suite of DP3, including Adroit [49], BiDexHands [8], DexArt [5], ... | p. 5 (IV. SIMULATION EXPERIMENTS) |
| IV. SIMULATION EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The success rates for experts are given in Appendix C. | p. 5 (IV. SIMULATION EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 5: Learning efficiency. We sample 12 simulation tasks and show the learning curves of DP3 and Diffusion Policy. DP3 demonstrates a rapid convergence ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 6: Efficient scaling with demonstrations. We sample 10 simulation tasks and train DP3 and Diffusion Policy with an increasing number of demonstrations. DP3 ... | p. 6 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** Simulation Benchmark (72 Tasks) Domain Robo Object Simulator ActD #Task #Demo Adroit Shadow Rigid/Art MuJoCo 28 3 10 Bi-DexHands Shadow Rigid/Art IsaacGym 52 6 10 ...
- **p. 7 / V. REAL WORLD EXPERIMENTS - extractive body cue:** Experiment Setup Real robot benchmark.
- **p. 4 / IV. SIMULATION EXPERIMENTS - extractive body cue:** This discrepancy underscores two key aspects: (a) the importance of real robot experiments and (b) the necessity of large-scale diverse simulation tasks for more sci
- **p. 4 / IV. SIMULATION EXPERIMENTS - extractive body cue:** Though the simulation environments are increasingly realistic nowadays [34, 73, 65, 85], a notable gap between simulation and real-world scenarios persists [80, 30, 7].
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** Therefore, for simulation experiments, we collect in total 72 tasks from 7 domains, covering diverse robotic skills.
- **p. 7 / V. REAL WORLD EXPERIMENTS - extractive body cue:** Our real-world setup and everyday objects used in our tasks are shown in Figure 8.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: 3D Diffusion Policy (DP3) is a visual imitation learning algorithm that marries 3D visual representations with diffusion policies, achieving surprising effectiveness in diverse ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Overview of 3D Diffusion Policy (DP3). Above: In the training phase, DP3 simultaneously trains its perception module and decision-making process in an end-to-end ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Generalization in 3D space with few data. We use MetaWorld Reach as an example task, given only 5 demonstra- tions (visualized by •). ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: 3D visual observations in simulation. We sample some simulated tasks and show the downsampled point clouds in these tasks. Expert demonstrations. Human-teleoperated data ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. In contrast, Diffusion Policy tends to converge at a much slower pace or converge into sub-optimal
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Learning efficiency. We sample 12 simulation tasks and show the learning curves of DP3 and Diffusion Policy. DP3 demonstrates a rapid convergence towards ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6: Efficient scaling with demonstrations. We sample 10 simulation tasks and train DP3 and Diffusion Policy with an increasing number of demonstrations. DP3 addresses ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Learning curves of DP3 with sample prediction and epsilon prediction. With sample prediction, DP3 generally converges faster, while epsilon prediction is also competitive. ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Simulation Benchmark (72 Tasks) Domain Robo Object Simulator ActD #Task #Demo Adroit Shadow Rigid/Art MuJoCo 28 3 10 Bi-DexHands Shadow Rigid/Art IsaacGym 52 6 ... | embodiment, simulator version and control stack | p. 5 (IV. SIMULATION EXPERIMENTS), p. 7 (V. REAL WORLD EXPERIMENTS) |
| Task/environment | Experiment Setup Real robot benchmark. | reset, timeout, object/scene variation | p. 7 (V. REAL WORLD EXPERIMENTS), p. 4 (IV. SIMULATION EXPERIMENTS) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 4 (III. METHOD), p. 3 (III. METHOD) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 6 (2) Learning efficiency. While we train all the algorithms) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The success rates for experts are given in Appendix C. | definition/direction/unit from same section | p. 5 (IV. SIMULATION EXPERIMENTS) |
| We report the mean and std of success rates across 3 seeds. | definition/direction/unit from same section | p. 5 (IV. SIMULATION EXPERIMENTS) |
| Fig. 2: Overview of 3D Diffusion Policy (DP3). Above: In the training phase, DP3 simultaneously trains its perception module and decision-making process in an ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| This discrepancy underscores two key aspects: (a) the importance of real robot experiments and (b) the necessity of large-scale diverse simulation tasks for more ... | definition/direction/unit from same section | p. 4 (IV. SIMULATION EXPERIMENTS) |
| Fig. 5: Learning efficiency. We sample 12 simulation tasks and show the learning curves of DP3 and Diffusion Policy. DP3 demonstrates a rapid convergence ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Fig. 6: Efficient scaling with demonstrations. We sample 10 simulation tasks and train DP3 and Diffusion Policy with an increasing number of demonstrations. DP3 ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Fig. 1: 3D Diffusion Policy (DP3) is a visual imitation learning algorithm that marries 3D visual representations with diffusion policies, achieving surprising effectiveness in ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 9: Randomization in collected demonstrations for real- world tasks. Roll-Up: The shape of the plasticine and the vegetables on it varies in each ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| To this end, our main baseline is the image-based diffusion policy [10], simply referred to as Diffusion Policy. | comparison identity and matched condition | p. 5 (IV. SIMULATION EXPERIMENTS) |
| Fig. 2: Overview of 3D Diffusion Policy (DP3). Above: In the training phase, DP3 simultaneously trains its perception module and decision-making process in an ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |
| Fig. 6: Efficient scaling with demonstrations. We sample 10 simulation tasks and train DP3 and Diffusion Policy with an increasing number of demonstrations. DP3 ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Additionally, we incorporate comparisons with IBC [11], BCRNN [35], and their 3D variations. | comparison identity and matched condition | p. 5 (IV. SIMULATION EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| no ablation sentence selected | not reported; proposed stress test only | verify ablation section |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To this end, we introduce 3D Diffusion Policy (DP3), which mainly consists of two critical parts: (a) Perception. | Fig. 2: Overview of 3D Diffusion Policy (DP3). Above: In the training phase, DP3 simultaneously trains its perception module and decision-making process in an ... | PDF body cue; verify exact table/figure and matched conditions | p. 4 (Figure/Table caption), p. 5 (IV. SIMULATION EXPERIMENTS), p. 5 (IV. SIMULATION EXPERIMENTS), p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 4 (IV. SIMULATION EXPERIMENTS) |
| Primary metric/result | We observe that DP3 achieves a success rate exceeding 90% in TABLE III: Task suite of DP3, including Adroit [49], BiDexHands [8], DexArt [5], ... | numeric claim only at cited anchor | p. 5 (IV. SIMULATION EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** Therefore, for simulation experiments, we collect in total 72 tasks from 7 domains, covering diverse robotic skills.
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** However, given that these algorithms showed limited effectiveness in our challenging tasks, we evaluate them on only 10 tasks (see Table II).
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** We run 3 seeds for each experiment with seed number 0, 1, 2.
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** For each seed, we evaluate 20 episodes every 200 training epochs and then compute the average of the highest 5 success rates.
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** We report the mean and std of success rates across 3 seeds.
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** Simulation Benchmark (72 Tasks) Domain Robo Object Simulator ActD #Task #Demo Adroit Shadow Rigid/Art MuJoCo 28 3 10 Bi-DexHands Shadow Rigid/Art IsaacGym 52 6 10 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 3: Generalization in 3D space with few data. We use MetaWorld Reach as an example task, given only 5 demonstra- tions (visualized by ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Fig. 6: Efficient scaling with demonstrations. We sample 10 simulation tasks and train DP3 and Diffusion Policy with an increasing number of demonstrations. DP3 ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | For instance, the image-based diffusion policy excels in the Drill task but fails entirely in Roll-Up. | p. 8 (2) Dumpling. The Allegro hand first wraps the plasticine) |
| body limitation/failure cue | It is noteworthy that the depthbased diffusion policy also does not incorporate color as input. | p. 8 (2) Dumpling. The Allegro hand first wraps the plasticine) |
| body limitation/failure cue | Fig. 1: 3D Diffusion Policy (DP3) is a visual imitation learning algorithm that marries 3D visual representations with diffusion policies, achieving surprising effectiveness in ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Accurate transformation isn't necessary due to the robustness of our network. | p. 9 (2) Dumpling. The Allegro hand first wraps the plasticine) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For each seed, we evaluate 20 episodes every 200 training epochs and then compute the average of the highest 5 success rates. | p. 5 (IV. SIMULATION EXPERIMENTS) |
| We run 3 seeds for each experiment with seed number 0, 1, 2. | p. 5 (IV. SIMULATION EXPERIMENTS) |
| We train 1000 epochs for MetaWorld tasks due to its simplicity and 3000 epochs for other simulated and real-world tasks, with batch size 128 ... | p. 4 (III. METHOD) |
| We then encode point clouds into compact 3D representations with a lightweight MLP network, as shown in Figure 2. | p. 3 (III. METHOD) |
| DP3 perceives the environments with point cloud data and processes these visual observations with an efficient point encoder into visual features; (b) Decision. | p. 3 (III. METHOD) |
| The 3D variants use our DP3 Encoder for a fair comparison. | p. 4 (III. METHOD) |
| We replace the visual observation and the corresponding encoder in DP3 to evaluate different 3D representations. | p. 6 (2) Learning efficiency. While we train all the algorithms) |
| The RGBD and depth images are processed using the same image encoder as Diffusion Policy, while voxel representations employ the VoxelCNN, as implemented in ... | p. 6 (2) Learning efficiency. While we train all the algorithms) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Generalization in 3D space with few data. We use MetaWorld Reach as an example task, given only 5 demonstra- tions (visualized by •). ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6: Efficient scaling with demonstrations. We sample 10 simulation tasks and train DP3 and Diffusion Policy with an increasing number of demonstrations. DP3 addresses ...
- **p. 8 / 2) Dumpling. The Allegro hand first wraps the plasticine - extractive body cue:** For instance, the image-based diffusion policy excels in the Drill task but fails entirely in Roll-Up.
- **p. 8 / 2) Dumpling. The Allegro hand first wraps the plasticine - extractive body cue:** It is noteworthy that the depthbased diffusion policy also does not incorporate color as input.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: 3D Diffusion Policy (DP3) is a visual imitation learning algorithm that marries 3D visual representations with diffusion policies, achieving surprising effectiveness in diverse ...
- **p. 9 / 2) Dumpling. The Allegro hand first wraps the plasticine - extractive body cue:** Accurate transformation isn't necessary due to the robustness of our network.

- **Evidence anchors reviewed:** datasets p. 5 (IV. SIMULATION EXPERIMENTS), p. 7 (V. REAL WORLD EXPERIMENTS), p. 4 (IV. SIMULATION EXPERIMENTS), p. 4 (IV. SIMULATION EXPERIMENTS), p. 5 (IV. SIMULATION EXPERIMENTS), p. 7 (V. REAL WORLD EXPERIMENTS), metrics p. 5 (IV. SIMULATION EXPERIMENTS), p. 5 (IV. SIMULATION EXPERIMENTS), p. 4 (Figure/Table caption), p. 4 (IV. SIMULATION EXPERIMENTS), p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), baselines p. 5 (IV. SIMULATION EXPERIMENTS), p. 4 (Figure/Table caption), p. 6 (Figure/Table caption), p. 5 (IV. SIMULATION EXPERIMENTS), results p. 4 (Figure/Table caption), p. 5 (IV. SIMULATION EXPERIMENTS), p. 5 (IV. SIMULATION EXPERIMENTS), p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 4 (IV. SIMULATION EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
