# Evaluation - Isaac Gym: High Performance GPU Based Physics Simulation For Robot Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (32 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://research.nvidia.com/labs/srl/publication/makoviychuk-2021-isaac/; PDF retrieval source: https://research.nvidia.com/labs/srl/publication/makoviychuk-2021-isaac/. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 31 (A.4.2 OpenAI Observations), p. 15 (Figure/Table caption), p. 7 (Figure/Table caption), p. 19 (4. Robotic Hands), p. 20 (4. Robotic Hands), p. 4 (Figure/Table caption)): LSTMs Using sequence networks like LSTMs improve the performance and we find that we are able to achieve 37 consecutive successful cube rotations after training in just under 6 hours.

## Evaluation Body Digest

- **p. 12 / 4. Robotic Hands - extractive body cue:** • Shadow • Allegro • Trifinger While Ant and Humanoid are relatively simple environments popularised by MuJoCo continuous control benchmarks, the strength of our simulator ...
- **p. 16 / 4. Robotic Hands - extractive body cue:** With 4096 environments, we can train the full task on NVIDIA RTX A6000 and transfer to the real robot in under 20 minutes.
- **p. 16 / 4. Robotic Hands - extractive body cue:** For sim-to-real transfer we extend the reward function, add noise to the observations, randomize the friction coefficient of the ground, randomly push the robots during ...
- **p. 20 / 4. Robotic Hands - extractive body cue:** 7 Summary We show that Isaac Gym is a high performance and high-fidelity framework that allows blistering fast training on many challenging simulated robotic environments ...
- **p. 31 / A.4.1 Randomizations - extractive body cue:** Parameter Scaling factor range Additive term range object dimensions uniform([0.95, 1.05]) object and robot link masses uniform([0.5, 1.5]) surface friction coefficients uniform([0.7, 1.3]) robot joint ...
- **p. 10 / 2 Background - extractive body cue:** 3 Physics Simulation Robots are simulated using PhysX [13] reduced coordinate articulations.
- **p. 11 / 2 Background - extractive body cue:** Benchmark results on the simulation performance and training results are presented in the subsequent sections.
- **p. 17 / 4. Robotic Hands - extractive body cue:** 6.4 Robotic Hands Figure 13: The three in-hand manipulation environments implemented in Isaac Gym: Shadow Hand, Trifinger, and Allegro.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| A.4.2 OpenAI Observations | BENCHMARK / DATASET | LSTMs Using sequence networks like LSTMs improve the performance and we find that we are able to achieve 37 consecutive successful cube rotations after ... | p. 31 (A.4.2 OpenAI Observations) |
| Figure/Table caption | BENCHMARK / DATASET | Figure 9: Locomotion environments and the corresponding reward curves. improvements continue to happen as more experience is collected. Additionally, we find that the horizon ... | p. 15 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Figure 3: (a) Traditional RL experience collection pipelines often use CPU based physics engines which quickly become the bottleneck. (b) In contrast, Isaac Gym ... | p. 7 (Figure/Table caption) |
| 4. Robotic Hands | BENCHMARK / DATASET | [5] show results only with 1 seed, comparing their result with our best seed we note that 37 consecutive successes with LSTM experiments can ... | p. 19 (4. Robotic Hands) |
| 4. Robotic Hands | BENCHMARK / DATASET | We also transfer results from simulation to the real world and note that our mean success rate in the real world is 55%. | p. 20 (4. Robotic Hands) |

## Dataset / Benchmark Role

- **p. 12 / 4. Robotic Hands - extractive body cue:** • Shadow • Allegro • Trifinger While Ant and Humanoid are relatively simple environments popularised by MuJoCo continuous control benchmarks, the strength of our simulator ...
- **p. 16 / 4. Robotic Hands - extractive body cue:** With 4096 environments, we can train the full task on NVIDIA RTX A6000 and transfer to the real robot in under 20 minutes.
- **p. 16 / 4. Robotic Hands - extractive body cue:** For sim-to-real transfer we extend the reward function, add noise to the observations, randomize the friction coefficient of the ground, randomly push the robots during ...
- **p. 20 / 4. Robotic Hands - extractive body cue:** 7 Summary We show that Isaac Gym is a high performance and high-fidelity framework that allows blistering fast training on many challenging simulated robotic environments ...
- **p. 31 / A.4.1 Randomizations - extractive body cue:** Parameter Scaling factor range Additive term range object dimensions uniform([0.95, 1.05]) object and robot link masses uniform([0.5, 1.5]) surface friction coefficients uniform([0.7, 1.3]) robot joint ...
- **p. 10 / 2 Background - extractive body cue:** 3 Physics Simulation Robots are simulated using PhysX [13] reduced coordinate articulations.
- **p. 11 / 2 Background - extractive body cue:** Benchmark results on the simulation performance and training results are presented in the subsequent sections.
- **p. 17 / 4. Robotic Hands - extractive body cue:** 6.4 Robotic Hands Figure 13: The three in-hand manipulation environments implemented in Isaac Gym: Shadow Hand, Trifinger, and Allegro.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1: Isaac Gym allows high performance training on a variety of robotics environments. We benchmark on 8 different environments that offer a wide range ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: An illustration of the Isaac Gym pipeline. The Tensor API provides an interface to Python code to step the PhysX backend, as well ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: (a) Traditional RL experience collection pipelines often use CPU based physics engines which quickly become the bottleneck. (b) In contrast, Isaac Gym not ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Tensors associated with the scene composed of multiple copies of the same environment simulating different variations all running in parallel. Each actor (e.g. ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 1: Physics state tensors. NA is the total number of actors, NB is the total number of rigid bodies (including articulation links), ND is ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 2: Physics control tensors. NB is the total number of rigid bodies (including articulation links) and ND is the total number of degrees of ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 3: Parameters exposed to tune the simulator. 4 Environments We implemented a diverse set of environments covering different application areas. Here we describe a ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 4: Simulation setup for the environments. 12

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | • Shadow • Allegro • Trifinger While Ant and Humanoid are relatively simple environments popularised by MuJoCo continuous control benchmarks, the strength of our ... | embodiment, simulator version and control stack | p. 12 (4. Robotic Hands), p. 16 (4. Robotic Hands) |
| Task/environment | With 4096 environments, we can train the full task on NVIDIA RTX A6000 and transfer to the real robot in under 20 minutes. | reset, timeout, object/scene variation | p. 16 (4. Robotic Hands), p. 16 (4. Robotic Hands) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 5 (1 Introduction), p. 10 (2 Background) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 5 (1 Introduction), p. 7 (2 Background) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 6.4.2 TriFinger 0 25000 50000 75000 Time (sec) 2500 5000 7500 10000 12500 15000 Reward Steps (millions) 0 4194 (a) Reward 0 20000 40000 ... | definition/direction/unit from same section | p. 19 (4. Robotic Hands) |
| Parameter Description Delta time (dt) Controls time-step size Gravity Controls the gravity in the scene Collision filtering Filters collisions between shapes Position iterations Biased ... | definition/direction/unit from same section | p. 11 (2 Background) |
| We also transfer results from simulation to the real world and note that our mean success rate in the real world is 55%. | definition/direction/unit from same section | p. 20 (4. Robotic Hands) |
| Following [22], a logistic kernel is used to convert tracking error in euclidean space into a bounded reward function, with K(x) = (eax + ... | definition/direction/unit from same section | p. 30 (A.2.3 Robotic Hands) |
| We find that the environment reaches performant dexterity of 10 consecutive successes at reward of 3000 in just 5 minutes.1 Further performance 1The experiments ... | definition/direction/unit from same section | p. 14 (4. Robotic Hands) |
| Figure 9: Locomotion environments and the corresponding reward curves. improvements continue to happen as more experience is collected. Additionally, we find that the horizon ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| Table 8: Observations used for ANYmal training. For rough terrain locomotion with sim-to-real, we extend the observations with 140 terrain heights around the robot's ... | definition/direction/unit from same section | p. 27 (Figure/Table caption) |
| Reward Symbol Definition Weight Linear velocity tracking Rvel,xy φ(v∗ b,xy -vb,xy) 1dt Angular velocity tracking Rvel,yaw φ(ω∗ b,z -ωb,z) 0.5dt Linear velocity penalty Rvel,z ... | definition/direction/unit from same section | p. 27 (A.2.2 Locomotion environments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As observed in Figure 6 and Figure 7, the training times are increased by an order of magnitude compared to the Ant in Figure ... | comparison identity and matched condition | p. 13 (4. Robotic Hands) |
| We verified this by training on another set of environment and horizon length combinations where horizon length was increased by a factor of 2 ... | comparison identity and matched condition | p. 13 (4. Robotic Hands) |
| OSC [25] is a task-space compliant controller that has been shown to enable faster policy learning compared to joint-space controllers [26] and learn contact-rich ... | comparison identity and matched condition | p. 17 (4. Robotic Hands) |
| Figure 3: (a) Traditional RL experience collection pipelines often use CPU based physics engines which quickly become the bottleneck. (b) In contrast, Isaac Gym ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| This allows resetting a subset of environments without affecting the rest. | comparison identity and matched condition | p. 10 (2 Background) |
| CUDA interoperability allows copying the data directly without ever going through the host. | comparison identity and matched condition | p. 10 (2 Background) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| However, it achieves the same effect on convergence as having sub-stepped the simulation without the computational expense. | component/input/data sensitivity | p. 11 (2 Background) |
| Figure 3: (a) Traditional RL experience collection pipelines often use CPU based physics engines which quickly become the bottleneck. (b) In contrast, Isaac Gym ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| This allows resetting a subset of environments without affecting the rest. | component/input/data sensitivity | p. 10 (2 Background) |
| CUDA interoperability allows copying the data directly without ever going through the host. | component/input/data sensitivity | p. 10 (2 Background) |
| We find that the environment reaches performant dexterity of 10 consecutive successes at reward of 3000 in just 5 minutes.1 Further performance 1The experiments ... | component/input/data sensitivity | p. 14 (4. Robotic Hands) |
| Also note that this variant does not use any randomisations. | component/input/data sensitivity | p. 18 (4. Robotic Hands) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address these bottlenecks, we present Isaac Gym - an end-to-end high performance robotics simulation platform. | LSTMs Using sequence networks like LSTMs improve the performance and we find that we are able to achieve 37 consecutive successful cube rotations after ... | PDF body cue; verify exact table/figure and matched conditions | p. 31 (A.4.2 OpenAI Observations), p. 15 (Figure/Table caption), p. 7 (Figure/Table caption), p. 19 (4. Robotic Hands), p. 20 (4. Robotic Hands), p. 4 (Figure/Table caption) |
| Primary metric/result | Figure 9: Locomotion environments and the corresponding reward curves. improvements continue to happen as more experience is collected. Additionally, we find that the horizon ... | numeric claim only at cited anchor | p. 15 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 12 / 4. Robotic Hands - extractive body cue:** Key Experimental Details • Unless stated otherwise, all experiments are done on a system with a single NVIDIA A100 GPU and a single 3.7GHz Intel ...
- **p. 12 / 4. Robotic Hands - extractive body cue:** Environment Control Type Simulation dt Control dt Action Dims Ant Joint Torques 1/120 s 1/60 s 8 Humanoid Joint Torques 1/120 s 1/60 s 21 ...
- **p. 13 / 4. Robotic Hands - extractive body cue:** 5.1 Ant 100 101 102 103 Time (sec) 0 2000 4000 6000 8000 Reward 0 2 4 6 Training Steps ×107 200000 400000 600000 FPS ...
- **p. 13 / 4. Robotic Hands - extractive body cue:** We also note in Figure 6 that as the number of agents is increased, in this case, from 256 to 4096, the training time needed ...
- **p. 14 / 4. Robotic Hands - extractive body cue:** 100 101 102 103 104 Time (sec) 0 2000 4000 6000 8000 Reward 0 1 2 3 Training Steps ×108 50000 100000 150000 200000 250000 ...
- **p. 14 / 4. Robotic Hands - extractive body cue:** 100 101 102 103 104 Time (sec) 0 2000 4000 6000 8000 Reward 0 2 4 6 Training Steps ×108 100000 200000 300000 FPS on ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Parameter Description Delta time (dt) Controls time-step size Gravity Controls the gravity in the scene Collision filtering Filters collisions between shapes Position iterations Biased ... | p. 11 (2 Background) |
| body limitation/failure cue | Initial Grasp Initial Lifting Reorientation Drop & Regrasp Lift Fine correction Time (a) Flick to reorient 2nd reorientation Drop & Regrasp Lift + in-hand ... | p. 20 (4. Robotic Hands) |
| body limitation/failure cue | Table 8: Observations used for ANYmal training. For rough terrain locomotion with sim-to-real, we extend the observations with 140 terrain heights around the robot's ... | p. 27 (Figure/Table caption) |
| body limitation/failure cue | Reward Symbol Definition Weight Linear velocity tracking Rvel,xy φ(v∗ b,xy -vb,xy) 1dt Angular velocity tracking Rvel,yaw φ(ω∗ b,z -ωb,z) 0.5dt Linear velocity penalty Rvel,z ... | p. 27 (A.2.2 Locomotion environments) |
| body limitation/failure cue | Setting new DOF states does not affect the root state. | p. 10 (2 Background) |
| body limitation/failure cue | Also note that this variant does not use any randomisations. | p. 18 (4. Robotic Hands) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Environment # Environments KL Threshold Mini-batch Size Horizon Length # PPO Epochs Hidden Units Training Steps Ant 4096 8e-3 32768 16 4 256, 128, ... | p. 30 (A.3 Hyperparameters for Training PPO) |
| Key Experimental Details • Unless stated otherwise, all experiments are done on a system with a single NVIDIA A100 GPU and a single 3.7GHz ... | p. 12 (4. Robotic Hands) |
| Below we provide the code snippet to compute the reward as used in our implementation. | p. 28 (A.2.3 Robotic Hands) |
| The SH OpenAI LSTM experiment uses an LSTM layer of 1024 hidden dims followed by MLP of 512 dims, and a fixed learning rate ... | p. 30 (A.3 Hyperparameters for Training PPO) |
| This implementation vectorizes observations and actions on GPU allowing us to take advantage of the parallelization provided by the simulator. | p. 11 (2 Background) |
| All environments are trained using the Proximal Policy Optimization algorithm [19], using rl_games, a highly-optimized GPU end-to-end implementation from [20]. | p. 11 (2 Background) |
| The implementation provided by Peng et al., 2021 [17] requires about 1 day (30 hours) on 16 CPU cores to simulate a similar number ... | p. 17 (4. Robotic Hands) |
| 7 Summary We show that Isaac Gym is a high performance and high-fidelity framework that allows blistering fast training on many challenging simulated robotic ... | p. 20 (4. Robotic Hands) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 11 / 2 Background - extractive body cue:** Parameter Description Delta time (dt) Controls time-step size Gravity Controls the gravity in the scene Collision filtering Filters collisions between shapes Position iterations Biased (velocity ...
- **p. 20 / 4. Robotic Hands - extractive body cue:** Initial Grasp Initial Lifting Reorientation Drop & Regrasp Lift Fine correction Time (a) Flick to reorient 2nd reorientation Drop & Regrasp Lift + in-hand reorientation ...
- **p. 27 / Figure/Table caption - extractive body cue:** Table 8: Observations used for ANYmal training. For rough terrain locomotion with sim-to-real, we extend the observations with 140 terrain heights around the robot's base ...
- **p. 27 / A.2.2 Locomotion environments - extractive body cue:** Reward Symbol Definition Weight Linear velocity tracking Rvel,xy φ(v∗ b,xy -vb,xy) 1dt Angular velocity tracking Rvel,yaw φ(ω∗ b,z -ωb,z) 0.5dt Linear velocity penalty Rvel,z -v2 ...
- **p. 10 / 2 Background - extractive body cue:** Setting new DOF states does not affect the root state.
- **p. 18 / 4. Robotic Hands - extractive body cue:** Also note that this variant does not use any randomisations.

- **PDF anchors reviewed:** datasets p. 12 (4. Robotic Hands), p. 16 (4. Robotic Hands), p. 16 (4. Robotic Hands), p. 20 (4. Robotic Hands), p. 31 (A.4.1 Randomizations), p. 10 (2 Background), metrics p. 19 (4. Robotic Hands), p. 11 (2 Background), p. 20 (4. Robotic Hands), p. 30 (A.2.3 Robotic Hands), p. 14 (4. Robotic Hands), p. 15 (Figure/Table caption), baselines p. 13 (4. Robotic Hands), p. 13 (4. Robotic Hands), p. 17 (4. Robotic Hands), p. 7 (Figure/Table caption), p. 10 (2 Background), p. 10 (2 Background), results p. 31 (A.4.2 OpenAI Observations), p. 15 (Figure/Table caption), p. 7 (Figure/Table caption), p. 19 (4. Robotic Hands), p. 20 (4. Robotic Hands), p. 4 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
