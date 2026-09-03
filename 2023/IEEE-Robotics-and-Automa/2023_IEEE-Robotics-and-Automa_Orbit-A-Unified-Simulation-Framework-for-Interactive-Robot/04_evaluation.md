# Evaluation - Orbit: A Unified Simulation Framework for Interactive Robot Learning Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/LRA.2023.3270034; PDF retrieval source: https://doi.org/10.1109/LRA.2023.3270034. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 7 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 5 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 6 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 7 (V. EXEMPLAR WORKFLOWS WITH ORBIT)): The success rate and trajectory lengths are reported over 100 trials.

## Evaluation Body Digest

- **p. 7 / VI. DISCUSSION - extractive body cue:** It readily comes with different robotic platforms, sensors, CPU and GPU-based motion generators, and benchmark tasks that aim to provide a batteries-included experience for roboticists.
- **p. 7 / VI. DISCUSSION - extractive body cue:** In this paper, we proposed ORBIT: an interactive and intuitive framework to simplify environment designing, enable easy task specifications, and lower the entry barrier into ...
- **p. 5 / V. EXEMPLAR WORKFLOWS WITH ORBIT - extractive body cue:** Owing to highquality physics, sensor simulation, and rendering, ORBIT is useful for multiple robotics challenges in both perception and decision-making.
- **p. 5 / V. EXEMPLAR WORKFLOWS WITH ORBIT - extractive body cue:** ORBIT provides a data collection interface that is useful for interacting with environments using I/O devices and collecting data similar to roboturk [38].
- **p. 6 / V. EXEMPLAR WORKFLOWS WITH ORBIT - extractive body cue:** After confirming the grasp pose, the robot executes the motion and lifts the object.
- **p. 6 / V. EXEMPLAR WORKFLOWS WITH ORBIT - extractive body cue:** 9: Using the simulator as a digital twin to compute and apply the same commands on the simulated and real robot via ZMQ connection.
- **p. 6 / V. EXEMPLAR WORKFLOWS WITH ORBIT - extractive body cue:** The success rate and trajectory lengths are reported over 100 trials.
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: ORBIT's abstractions comprise World, analogous to the real world, and Agent, the computation graph behind the embodied system. The nodes in the agent's ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. EXEMPLAR WORKFLOWS WITH ORBIT | BENCHMARK / DATASET | The success rate and trajectory lengths are reported over 100 trials. | p. 6 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |
| V. EXEMPLAR WORKFLOWS WITH ORBIT | BENCHMARK / DATASET | In contrast, GPU-based parallelization scales better to a larger number of environments and achieves a throughput of ∼10x faster for rigid body environments (Fig. | p. 7 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |
| V. EXEMPLAR WORKFLOWS WITH ORBIT | BENCHMARK / DATASET | Although we ensure the same parameter settings for PPO in the frameworks, we notice a difference in their performance and training time due to ... | p. 5 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |
| V. EXEMPLAR WORKFLOWS WITH ORBIT | BENCHMARK / DATASET | Setup BC / BC-RNN 234 / 249 1.00 / 1.00 No Change 307 / 251 0.89 / 1.00 G 321 / 286 0.47 / ... | p. 6 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |
| V. EXEMPLAR WORKFLOWS WITH ORBIT | BENCHMARK / DATASET | However, increasing the number of nodes or points (pts) in the cloth mesh adversely affects its performance. | p. 7 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |

## Dataset / Benchmark Role

- **p. 7 / VI. DISCUSSION - extractive body cue:** It readily comes with different robotic platforms, sensors, CPU and GPU-based motion generators, and benchmark tasks that aim to provide a batteries-included experience for roboticists.
- **p. 7 / VI. DISCUSSION - extractive body cue:** In this paper, we proposed ORBIT: an interactive and intuitive framework to simplify environment designing, enable easy task specifications, and lower the entry barrier into ...
- **p. 5 / V. EXEMPLAR WORKFLOWS WITH ORBIT - extractive body cue:** Owing to highquality physics, sensor simulation, and rendering, ORBIT is useful for multiple robotics challenges in both perception and decision-making.
- **p. 5 / V. EXEMPLAR WORKFLOWS WITH ORBIT - extractive body cue:** ORBIT provides a data collection interface that is useful for interacting with environments using I/O devices and collecting data similar to roboturk [38].
- **p. 6 / V. EXEMPLAR WORKFLOWS WITH ORBIT - extractive body cue:** After confirming the grasp pose, the robot executes the motion and lifts the object.
- **p. 6 / V. EXEMPLAR WORKFLOWS WITH ORBIT - extractive body cue:** 9: Using the simulator as a digital twin to compute and apply the same commands on the simulated and real robot via ZMQ connection.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: ORBIT framework provides a large set of robots, sensors, rigid and deformable objects, motion generators, and teleoperation interfaces. Through these, we aim to ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: ORBIT's abstractions comprise World, analogous to the real world, and Agent, the computation graph behind the embodied system. The nodes in the agent's ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 4: Illustration of actuator groups for a legged mobile manipula- tor. This allows decomposing a complex system into sub-groups and defining of specific transmission ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 5: Overview of features included in ORBIT. We provide models of different sensors, robotic platforms, objects from different datasets, motion generators, and teleoperation devices. ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 6: Demonstration of the designed tasks using hand-crafted state machines and task-space controllers. Leveraging recent advances in physics engines, we support high-fidelity simulation of ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 7: Example showing RL integration. We include wrappers to various RL frameworks. Additionally, it is possible to easily switch action spaces for training policies ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 8: Interactive grasp and motion planning demonstration using ORBIT. The World comprises objects for table-top manipulation. The user can select an object from the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 9: Using the simulator as a digital twin to compute and apply the same commands on the simulated and real robot via ZMQ connection. ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | It readily comes with different robotic platforms, sensors, CPU and GPU-based motion generators, and benchmark tasks that aim to provide a batteries-included experience for ... | embodiment, simulator version and control stack | p. 7 (VI. DISCUSSION), p. 7 (VI. DISCUSSION) |
| Task/environment | In this paper, we proposed ORBIT: an interactive and intuitive framework to simplify environment designing, enable easy task specifications, and lower the entry barrier ... | reset, timeout, object/scene variation | p. 7 (VI. DISCUSSION), p. 5 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 1 (I. INTRODUCTION) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 2 (2) It provides a batteries-included experience for roboti), p. 2 (2) It provides a batteries-included experience for roboti) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The success rate and trajectory lengths are reported over 100 trials. | definition/direction/unit from same section | p. 6 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |
| Fig. 3: ORBIT's abstractions comprise World, analogous to the real world, and Agent, the computation graph behind the embodied system. The nodes in the ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| V-D follows a similar practice to show realism in the rigid body simulation, we discuss the accuracy of deformable body simulation through a controlled ... | definition/direction/unit from same section | p. 7 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |
| The simulated data is obtained using the FEM-solver [23] in Isaac Sim over different hexahedral mesh resolutions (m). obtain the contact forces and use ... | definition/direction/unit from same section | p. 7 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |
| Fig. 5: Overview of features included in ORBIT. We provide models of different sensors, robotic platforms, objects from different datasets, motion generators, and teleoperation ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Although we ensure the same parameter settings for PPO in the frameworks, we notice a difference in their performance and training time due to ... | definition/direction/unit from same section | p. 5 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |
| Fig. 6: Demonstration of the designed tasks using hand-crafted state machines and task-space controllers. Leveraging recent advances in physics engines, we support high-fidelity simulation ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| We demonstrate this paradigm for several tasks in Fig. | definition/direction/unit from same section | p. 6 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We provide wrappers to rlgames [35], RSL-rl [34], and stable-baselines-3 [36]. | comparison identity and matched condition | p. 5 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |
| Since RSL-rl and rl-games are optimized for GPU, we observe a training speed of 50,00075,000 frames per second (FPS) with 2048 environments, while with ... | comparison identity and matched condition | p. 5 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |
| 0.5 1.0 1.5 Steps ×107 7 8 9 10 Average Return PPO on Franka-Reach Stable Baselines3 RL Games RSL RL 0.5 1.0 1.5 2.0 ... | comparison identity and matched condition | p. 6 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |
| CPU-based vectorization is limited to the available memory and scales poorly compared to GPU-accelerated simulation. | comparison identity and matched condition | p. 7 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |
| ORBIT exploits the latest state-of-the-art simulation capabilities through Isaac Sim and extends them further to incorporate different actuator and sensor noise models into the ... | comparison identity and matched condition | p. 7 (VI. DISCUSSION) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Effect of cloth mesh resolution 294 pts 574 pts 2203 pts 8623 pts Fig. | component/input/data sensitivity | p. 7 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |
| The traditional Sense-Model-Plan-Act (SMPA) methodology decomposes the complex problem of reasoning and control into possible sub-components. | component/input/data sensitivity | p. 6 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions are as follows: | The success rate and trajectory lengths are reported over 100 trials. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 7 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 5 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 6 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 7 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |
| Primary metric/result | In contrast, GPU-based parallelization scales better to a larger number of environments and achieves a throughput of ∼10x faster for rigid body environments (Fig. | numeric claim only at cited anchor | p. 7 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |

- Numeric sentences retained from the body:
- **p. 5 / V. EXEMPLAR WORKFLOWS WITH ORBIT - extractive body cue:** Since RSL-rl and rl-games are optimized for GPU, we observe a training speed of 50,00075,000 frames per second (FPS) with 2048 environments, while with stable-baselines3, ...
- **p. 5 / V. EXEMPLAR WORKFLOWS WITH ORBIT - extractive body cue:** For each of the four settings of initial and desired object positions (fixed or random start and desired positions), we collect 2000 trajectories.
- **p. 6 / V. EXEMPLAR WORKFLOWS WITH ORBIT - extractive body cue:** 0.5 1.0 1.5 Steps ×107 7 8 9 10 Average Return PPO on Franka-Reach Stable Baselines3 RL Games RSL RL 0.5 1.0 1.5 2.0 Steps ...
- **p. 6 / V. EXEMPLAR WORKFLOWS WITH ORBIT - extractive body cue:** The success rate and trajectory lengths are reported over 100 trials.
- **p. 6 / V. EXEMPLAR WORKFLOWS WITH ORBIT - extractive body cue:** To abide by the real-time safety constraints, we use a quintic interpolator to upsample the 60 Hz joint commands from the simulator to 1000 Hz ...
- **p. 6 / V. EXEMPLAR WORKFLOWS WITH ORBIT - extractive body cue:** To make the policy robust, we randomize the base mass (22 ± 5 kg) and add simulated random pushes.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | ORBIT exploits the latest state-of-the-art simulation capabilities through Isaac Sim and extends them further to incorporate different actuator and sensor noise models into the ... | p. 7 (VI. DISCUSSION) |
| body limitation/failure cue | To make the policy robust, we randomize the base mass (22 ± 5 kg) and add simulated random pushes. | p. 6 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Although we ensure the same parameter settings for PPO in the frameworks, we notice a difference in their performance and training time due to ... | p. 5 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |
| CPU-based vectorization is limited to the available memory and scales poorly compared to GPU-accelerated simulation. | p. 7 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |
| Frameworks that rely on CPU-vectorization ([2], [4], [10]) show an increase in throughput with the number of environments. | p. 7 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |
| Recently, NVIDIA released a new simulator Omniverse Isaac Sim [16] that aims to fulfill these gaps through GPU-accelerated real-time PBR and state-of-the-art physics engine. | p. 1 (I. INTRODUCTION) |
| ORBIT allows training reinforcement learning policies and collecting large demonstration datasets from hand-crafted or expert solutions in a matter of minutes by leveraging GPU-based ... | p. 1 (Abstract) |
| V), show sim-to-real experiments for locomotion and manipulation, and evaluate the obtained accuracy and simulation throughput in Sec. | p. 2 (2) It provides a batteries-included experience for roboti) |
| Compared to existing frameworks, we show that ORBIT is able to obtain up to ∼10x and ∼3x the throughput for rigid and deformable body ... | p. 2 (2) It provides a batteries-included experience for roboti) |
| Since RSL-rl and rl-games are optimized for GPU, we observe a training speed of 50,00075,000 frames per second (FPS) with 2048 environments, while with ... | p. 5 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / VI. DISCUSSION - extractive body cue:** ORBIT exploits the latest state-of-the-art simulation capabilities through Isaac Sim and extends them further to incorporate different actuator and sensor noise models into the simulation, ...
- **p. 6 / V. EXEMPLAR WORKFLOWS WITH ORBIT - extractive body cue:** To make the policy robust, we randomize the base mass (22 ± 5 kg) and add simulated random pushes.

- **Evidence anchors reviewed:** datasets p. 7 (VI. DISCUSSION), p. 7 (VI. DISCUSSION), p. 5 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 5 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 6 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 6 (V. EXEMPLAR WORKFLOWS WITH ORBIT), metrics p. 6 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 3 (Figure/Table caption), p. 7 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 7 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 4 (Figure/Table caption), p. 5 (V. EXEMPLAR WORKFLOWS WITH ORBIT), baselines p. 5 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 5 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 6 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 7 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 7 (VI. DISCUSSION), results p. 6 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 7 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 5 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 6 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 7 (V. EXEMPLAR WORKFLOWS WITH ORBIT).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
