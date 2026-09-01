# Evaluation - DeXtreme: Transfer of Agile In-hand Manipulation from Simulation to Reality

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://research.nvidia.com/publication/2023-06_dextreme-transfer-agile-hand-manipulation-simulation-reality; PDF retrieval source: https://research.nvidia.com/publication/2023-06_dextreme-transfer-agile-hand-manipulation-simulation-reality. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 14 (3 Results), p. 14 (3 Results), p. 13 (3 Results), p. 15 (3 Results), p. 15 (3 Results), p. 26 (Figure/Table caption)): We demonstrate performance which significantly improves upon the best vision policies 8Although [8] focused on the Rubik's cube, they also trained for block reorientation (pp.

## Evaluation Body Digest

- **p. 14 / 3 Results - extractive body cue:** We believe such inter-day variations are important to benchmark in robotics [20] and have endeavoured to highlight this specifically in this challenging task.
- **p. 13 / Experiment - extractive body cue:** We benchmark the pose on a test set consisting of 50K images and provide results in Table 6.
- **p. 13 / Experiment - extractive body cue:** Translation Error X Y Z Sim 5.3±0.11◦ 1.9±0.1 mm 4.1±0.2 mm 6.9±0.4 mm Table 6: Rotation and translation error on test dataset with 90% confidence ...
- **p. 14 / 3 Results - extractive body cue:** It is worth noting that, while in simulations, state information is derived directly from physics buffers, in all real-world experiments we use the pose estimator ...
- **p. 15 / 3 Results - extractive body cue:** Additionally, we also benchmark our results beyond the basic experiment of goal reaching by making the policy hold the cube at a target orientation N ...
- **p. 15 / 3 Results - extractive body cue:** Successes 0 38.4 5 35.3 10 33.3 20 27.3 Table 8: Performance in simulation with ADR policies with respect to N.
- **p. 15 / 3 Results - extractive body cue:** This also lets us separate the drop in performance due to LSTM instability from pose estimation errors in the real world.
- **p. 15 / 3 Results - extractive body cue:** We hypothesise that this maybe due to (a) better accuracy of the state information from the PhaseSpace markers (b) higher frame-rate of state observations with ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** 3 Results (p. 2); Experiment (p. 13); 3 Results (p. 13).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 3 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | We demonstrate performance which significantly improves upon the best vision policies 8Although [8] focused on the Rubik's cube, they also trained for block reorientation ... | p. 14 (3 Results) |
| 3 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | We note that due to differences in physics engines and hand morphology, our simulation average consecutive successes are not directly comparable, but we achieve ... | p. 14 (3 Results) |
| 3 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | In the following section, we present the results we achieved in object reorientation in the simulations and then real world using the methods described ... | p. 13 (3 Results) |
| 3 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our policies do not achieve the average successes seen in [8] with ADR (XXL) with state information. | p. 15 (3 Results) |
| 3 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Therefore, holding the cube for N frames in a row ensures that the goal was not achieved by chance, highlighting the robustness of the ... | p. 15 (3 Results) |

## Dataset / Benchmark Role

- **p. 14 / 3 Results - extractive body cue:** We believe such inter-day variations are important to benchmark in robotics [20] and have endeavoured to highlight this specifically in this challenging task.
- **p. 13 / Experiment - extractive body cue:** We benchmark the pose on a test set consisting of 50K images and provide results in Table 6.
- **p. 13 / Experiment - extractive body cue:** Translation Error X Y Z Sim 5.3±0.11◦ 1.9±0.1 mm 4.1±0.2 mm 6.9±0.4 mm Table 6: Rotation and translation error on test dataset with 90% confidence ...
- **p. 14 / 3 Results - extractive body cue:** It is worth noting that, while in simulations, state information is derived directly from physics buffers, in all real-world experiments we use the pose estimator ...
- **p. 15 / 3 Results - extractive body cue:** Additionally, we also benchmark our results beyond the basic experiment of goal reaching by making the policy hold the cube at a target orientation N ...
- **p. 15 / 3 Results - extractive body cue:** Successes 0 38.4 5 35.3 10 33.3 20 27.3 Table 8: Performance in simulation with ADR policies with respect to N.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: The DeXtreme system using an Allegro Hand in action in the real world.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: The hardware setup used in this work, unlike [1], is not housed in a cage, and our system is robust enough to perform ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: High level overview of the training and inference systems. 5
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Observations of the policy and value networks. The input vector is 50D in size for policy and 265D for the value function. We ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Reward terms are computed, multiplied by their weight, and summed to produce the reward at each timestep. d represents the rotational distance from ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Domain randomisation parameter ranges for policy learning simulator [6], which models contacts differently than MuJoCo's soft-contact model [7] used in [1]. Isaac Gym ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Parameter range adjustments, pi_lo and pi_hi, with ADR based on the performance of policy at the boundaries Qi_lo and Qi_hi with respect to ...
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 5: The functioning of the Random Network Adversary Then each step we sample a variable m ∼Bern(·; p), and the cube pose becomes: pose_obs ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We believe such inter-day variations are important to benchmark in robotics [20] and have endeavoured to highlight this specifically in this challenging task. | embodiment, simulator version and control stack | p. 14 (3 Results), p. 13 (Experiment) |
| Task/environment | We benchmark the pose on a test set consisting of 50K images and provide results in Table 6. | reset, timeout, object/scene variation | p. 13 (Experiment), p. 13 (Experiment) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 6 (2 Method), p. 4 (2 Method) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 6 (2 Method), p. 10 (2 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| This also lets us separate the drop in performance due to LSTM instability from pose estimation errors in the real world. | definition/direction/unit from same section | p. 15 (3 Results) |
| Table 6: Rotation and translation error on test dataset with 90% confidence intervals. Training setup and inference: We use a torchvision Mask-RCNN [17]-inspired network ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| We hypothesise that this maybe due to (a) better accuracy of the state information from the PhaseSpace markers (b) higher frame-rate of state observations ... | definition/direction/unit from same section | p. 15 (3 Results) |
| Table 2: Reward terms are computed, multiplied by their weight, and summed to produce the reward at each timestep. d represents the rotational distance ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Our real-world quantitative results measuring average consecutive successes are illustrated in Table 7. | definition/direction/unit from same section | p. 14 (3 Results) |
| We demonstrate performance which significantly improves upon the best vision policies 8Although [8] focused on the Rubik's cube, they also trained for block reorientation ... | definition/direction/unit from same section | p. 14 (3 Results) |
| We then follow it up with tests of policy robustness in reality and simulation. | definition/direction/unit from same section | p. 13 (3 Results) |
| Table 1: Observations of the policy and value networks. The input vector is 50D in size for policy and 265D for the value function. ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 11: Our hardware setup compared against the one used in OpenAI et al. [1] and OpenAI et al. [8]. Note that the experiment ... | comparison identity and matched condition | p. 25 (Figure/Table caption) |
| Our ablation studies in Section 3.2 do test the strength of the pose estimator for manipulation in the real world. | comparison identity and matched condition | p. 13 (Experiment) |
| In the basic experiment of goal reaching without the hold, the cube may shoot past the target, making it difficult to tell if the ... | comparison identity and matched condition | p. 15 (3 Results) |
| Table 9: We compare our block reorientation results against the previous work of OpenAI et al. [1] and OpenAI et al. [8]. It is ... | comparison identity and matched condition | p. 16 (Figure/Table caption) |
| Table 10: Compute budget comparisons for block reorientation task of our work against the previous work. The costs are estimated from the AWS EC2 ... | comparison identity and matched condition | p. 25 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Our ablation studies in Section 3.2 do test the strength of the pose estimator for manipulation in the real world. | component/input/data sensitivity | p. 13 (Experiment) |
| In the basic experiment of goal reaching without the hold, the cube may shoot past the target, making it difficult to tell if the ... | component/input/data sensitivity | p. 15 (3 Results) |
| Figure 2: The hardware setup used in this work, unlike [1], is not housed in a cage, and our system is robust enough to ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| We use three separate machines to run various components. | component/input/data sensitivity | p. 14 (3 Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| 2.1 Task We propose a method for performing object reorientation on an anthropomorphic hand. | We demonstrate performance which significantly improves upon the best vision policies 8Although [8] focused on the Rubik's cube, they also trained for block reorientation ... | PDF body cue; verify exact table/figure and matched conditions | p. 14 (3 Results), p. 14 (3 Results), p. 13 (3 Results), p. 15 (3 Results), p. 15 (3 Results), p. 26 (Figure/Table caption) |
| Primary metric/result | We note that due to differences in physics engines and hand morphology, our simulation average consecutive successes are not directly comparable, but we achieve ... | numeric claim only at cited anchor | p. 14 (3 Results) |

- Numeric sentences retained from the body:
- **p. 13 / Experiment - extractive body cue:** Translation Error X Y Z Sim 5.3±0.11◦ 1.9±0.1 mm 4.1±0.2 mm 6.9±0.4 mm Table 6: Rotation and translation error on test dataset with 90% confidence ...
- **p. 13 / Experiment - extractive body cue:** The network runs on three cameras at an inference rate of 20Hz on an NVIDIA RTX 3090 GPU and a 32-core AMD Ryzen Threadripper CPU.
- **p. 13 / Experiment - extractive body cue:** However, because the policy was trained with a control frequency of 30Hz in simulation, the pose estimator was locked to run at 15Hz to ensure ...
- **p. 13 / 3 Results - extractive body cue:** For all of our experiments, we use a simulation dt of 1 60s and a control dt of 1 30s.
- **p. 14 / 3 Results - extractive body cue:** Training with manual DR takes roughly 32 hours to converge on 8 NVIDIA A40s generating a combined (across all GPUs) frame rate of 700K frames/sec.
- **p. 14 / 3 Results - extractive body cue:** With a dt = 1 60, this amounts to 32×700000 60×24×365 which is ∼42 years of real-world experience.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 4: Parameter range adjustments, pi_lo and pi_hi, with ADR based on the performance of policy at the boundaries Qi_lo and Qi_hi with respect ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | However, these often fail to reproduce the agile dexterity present in human hands, as the limitations of such a sequential approach to control place ... | p. 18 (4 Related work) |
| body limitation/failure cue | These approaches work well while an object maintains no-slip 10While extrinsics change with different camera configurations, the intrinsics remain the same. | p. 17 (4 Related work) |
| body limitation/failure cue | 5 Limitations Despite our best efforts, the gap between simulations and the real world is still noticeable. | p. 18 (4 Related work) |
| body limitation/failure cue | We suspect that this is because, despite the extreme levels of randomisation we do, there is a "null space" of possible policies which perform ... | p. 17 (Method) |
| body limitation/failure cue | Figure 2: The hardware setup used in this work, unlike [1], is not housed in a cage, and our system is robust enough to ... | p. 4 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The network runs on three cameras at an inference rate of 20Hz on an NVIDIA RTX 3090 GPU and a 32-core AMD Ryzen Threadripper ... | p. 13 (Experiment) |
| However, because the policy was trained with a control frequency of 30Hz in simulation, the pose estimator was locked to run at 15Hz to ... | p. 13 (Experiment) |
| We use a high-performance PPO implementation from rl-games [11] with the following hyperparameters: discount factor γ=0.998 3, clipping ϵ=0.2. | p. 6 (2 Method) |
| Isaac Gym gives the advantage of being able to simulate thousands of robots in parallel on a single GPU, mitigating the need for large ... | p. 7 (2 Method) |
| As we are doing simulation on GPU rather than CPU, instead of using a new network per environment-episode and wasting memory on thousands of ... | p. 11 (2 Method) |
| We run 10 trials per policy [1] to benchmark the average consecutive successes. | p. 14 (3 Results) |
| While in some experiments the learning rate was updated adaptively based on a fixed KL threshold 0.016, our best result was obtained using linear ... | p. 6 (2 Method) |
| DR type Pose estimation type Training time Cons. | p. 16 (Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Parameter range adjustments, pi_lo and pi_hi, with ADR based on the performance of policy at the boundaries Qi_lo and Qi_hi with respect to ...
- **p. 18 / 4 Related work - extractive body cue:** However, these often fail to reproduce the agile dexterity present in human hands, as the limitations of such a sequential approach to control place corresponding ...
- **p. 17 / 4 Related work - extractive body cue:** These approaches work well while an object maintains no-slip 10While extrinsics change with different camera configurations, the intrinsics remain the same.
- **p. 18 / 4 Related work - extractive body cue:** 5 Limitations Despite our best efforts, the gap between simulations and the real world is still noticeable.
- **p. 17 / Method - extractive body cue:** We suspect that this is because, despite the extreme levels of randomisation we do, there is a "null space" of possible policies which perform similarly ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: The hardware setup used in this work, unlike [1], is not housed in a cage, and our system is robust enough to perform ...

- **PDF anchors reviewed:** datasets p. 14 (3 Results), p. 13 (Experiment), p. 13 (Experiment), p. 14 (3 Results), p. 15 (3 Results), p. 15 (3 Results), metrics p. 15 (3 Results), p. 13 (Figure/Table caption), p. 15 (3 Results), p. 7 (Figure/Table caption), p. 14 (3 Results), p. 14 (3 Results), baselines p. 25 (Figure/Table caption), p. 13 (Experiment), p. 15 (3 Results), p. 16 (Figure/Table caption), p. 25 (Figure/Table caption), results p. 14 (3 Results), p. 14 (3 Results), p. 13 (3 Results), p. 15 (3 Results), p. 15 (3 Results), p. 26 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
