# Isaac Gym: High Performance GPU Based Physics Simulation For Robot Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (32 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://research.nvidia.com/labs/srl/publication/makoviychuk-2021-isaac/.
> PDF retrieval source: https://research.nvidia.com/labs/srl/publication/makoviychuk-2021-isaac/. Reading tracker status/evidence was not changed.

- Year/Venue: 2021 / NeurIPS Datasets and Benchmarks
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, simulation, GPU, Reinforcement Learning, NVIDIA
- Official paper: https://research.nvidia.com/labs/srl/publication/makoviychuk-2021-isaac/
- Full-text retrieval: https://research.nvidia.com/labs/srl/publication/makoviychuk-2021-isaac/
- Code/Project: not identified
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-02 (32 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 benchmark 문제를 이해하기 위해 읽는다. 본문은 However, some bottlenecks were still not addressed in the work - simulation was on GPU but physics state was copied back to CPU.를 문제로 두고, To address these bottlenecks, we present Isaac Gym - an end-to-end high performance robotics simulation platform.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Isaac Gym offers a high performance learning platform to train policies for wide variety of robotics tasks directly on GPU.
- **p. 1 / Abstract - extractive body cue:** Both physics simulation and the neural network policy training reside on GPU and communicate by directly passing data from physics buffers to PyTorch tensors without ...
- **p. 1 / Abstract - extractive body cue:** This leads to blazing fast training times for complex robotics tasks on a single GPU with 2-3 orders of magnitude improvements compared to conventional RL ...
- **p. 4 / 1 Introduction - extractive body cue:** However, some bottlenecks were still not addressed in the work - simulation was on GPU but physics state was copied back to CPU.
- **p. 7 / 2 Background - extractive body cue:** There are, however, performance bottlenecks with this strategy.
- **p. 4 / 1 Introduction - extractive body cue:** Therefore, scalability of deep reinforcement learning in robotics is faced with two critical bottlenecks: 1) enormous computational requirements and 2) limited simulation speed.
- **p. 5 / 1 Introduction - extractive body cue:** To address these bottlenecks, we present Isaac Gym - an end-to-end high performance robotics simulation platform.

## Core Idea

- **p. 5 / 1 Introduction - extractive body cue:** To address these bottlenecks, we present Isaac Gym - an end-to-end high performance robotics simulation platform.
- **p. 9 / 2 Background - extractive body cue:** Rigid body state consists of position, orientation (quaternion), linear velocity, and angular velocity.
- **p. 5 / 1 Introduction - extractive body cue:** It runs an end-to-end GPU accelerated training pipeline, which allows researchers to overcome the aforementioned limitations and achieves 2-3 orders of magnitude of training speed-up ...
- **p. 9 / 2 Background - extractive body cue:** In the code snippet below we show how to access them through the API. # Acquire tensor descriptors # - Raw storage buffer independent of ...
- **p. 6 / 2 Background - extractive body cue:** Isaac Gym was developed to maximize the throughput of physics-based machine learning algorithms with particular emphasis on simulations that require large numbers of environment instances ...
- **p. 30 / A.3 Hyperparameters for Training PPO - extractive body cue:** Environment # Environments KL Threshold Mini-batch Size Horizon Length # PPO Epochs Hidden Units Training Steps Ant 4096 8e-3 32768 16 4 256, 128, 64 ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Observation tensors can be used as inputs to a policy network and the resulting action tensors can be directly fed back into the physics system. | standardized observation, action, task state와 evaluation split | p. 5 (1 Introduction), p. 10 (2 Background) |
| State/latent | Observation, tensors, inputs, policy, network, resulting, action, directly, back, physics, system, Control | benchmark state/goal와 method decision | p. 5 (1 Introduction), p. 10 (2 Background), p. 5 (1 Introduction) |
| Output/action | 2.3.3 Physics Control Tensors Physics simulation inputs include forces, torques, and PD controls such as position and velocity targets. | policy/controller trajectory 또는 measured result | p. 10 (2 Background), p. 5 (1 Introduction), p. 7 (2 Background) |
| Objective/outcome | The SH OpenAI LSTM experiment uses an LSTM layer of 1024 hidden dims followed by MLP of 512 dims, and a fixed learning rate of 1e-4 for the value function. | success metric, robustness, generalization과 reproducibility | p. 30 (A.3 Hyperparameters for Training PPO) |

## Main Claims and Actual Contribution

- **p. 5 / 1 Introduction - extractive body cue:** To address these bottlenecks, we present Isaac Gym - an end-to-end high performance robotics simulation platform.
- **p. 9 / 2 Background - extractive body cue:** Rigid body state consists of position, orientation (quaternion), linear velocity, and angular velocity.
- **p. 5 / 1 Introduction - extractive body cue:** It runs an end-to-end GPU accelerated training pipeline, which allows researchers to overcome the aforementioned limitations and achieves 2-3 orders of magnitude of training speed-up ...
- **p. 9 / 2 Background - extractive body cue:** In the code snippet below we show how to access them through the API. # Acquire tensor descriptors # - Raw storage buffer independent of ...
- **p. 6 / 2 Background - extractive body cue:** Isaac Gym was developed to maximize the throughput of physics-based machine learning algorithms with particular emphasis on simulations that require large numbers of environment instances ...
- **p. 31 / A.4.2 OpenAI Observations - extractive body cue:** LSTMs Using sequence networks like LSTMs improve the performance and we find that we are able to achieve 37 consecutive successful cube rotations after training ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 9: Locomotion environments and the corresponding reward curves. improvements continue to happen as more experience is collected. Additionally, we find that the horizon length ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: (a) Traditional RL experience collection pipelines often use CPU based physics engines which quickly become the bottleneck. (b) In contrast, Isaac Gym not ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 31 (A.4.2 OpenAI Observations), p. 15 (Figure/Table caption) |
| Embodiment/environment | • Shadow • Allegro • Trifinger While Ant and Humanoid are relatively simple environments popularised by MuJoCo continuous control benchmarks, the strength of our simulator really shines when training on environments that ... | hardware/simulator version and reset protocol | p. 12 (4. Robotic Hands), p. 16 (4. Robotic Hands) |
| Dataset/benchmark | For sim-to-real transfer we extend the reward function, add noise to the observations, randomize the friction coefficient of the ground, randomly push the robots during the episode and add an actuator network ... | role, split, size and leakage | p. 12 (4. Robotic Hands), p. 16 (4. Robotic Hands), p. 16 (4. Robotic Hands), p. 20 (4. Robotic Hands) |
| Metric | 6.4.2 TriFinger 0 25000 50000 75000 Time (sec) 2500 5000 7500 10000 12500 15000 Reward Steps (millions) 0 4194 (a) Reward 0 20000 40000 60000 80000 Time (sec) 0 20 40 60 ... | definition, denominator, direction and uncertainty | p. 19 (4. Robotic Hands), p. 11 (2 Background), p. 20 (4. Robotic Hands) |
| Baseline/ablation | As observed in Figure 6 and Figure 7, the training times are increased by an order of magnitude compared to the Ant in Figure 5. | fair input/data/compute/action matching | p. 13 (4. Robotic Hands), p. 13 (4. Robotic Hands), p. 17 (4. Robotic Hands) |

## Explicit Limitations and Failure Boundary

- **p. 11 / 2 Background - extractive body cue:** Parameter Description Delta time (dt) Controls time-step size Gravity Controls the gravity in the scene Collision filtering Filters collisions between shapes Position iterations Biased (velocity ...
- **p. 20 / 4. Robotic Hands - extractive body cue:** Initial Grasp Initial Lifting Reorientation Drop & Regrasp Lift Fine correction Time (a) Flick to reorient 2nd reorientation Drop & Regrasp Lift + in-hand reorientation ...
- **p. 27 / Figure/Table caption - extractive body cue:** Table 8: Observations used for ANYmal training. For rough terrain locomotion with sim-to-real, we extend the observations with 140 terrain heights around the robot's base ...
- **p. 27 / A.2.2 Locomotion environments - extractive body cue:** Reward Symbol Definition Weight Linear velocity tracking Rvel,xy φ(v∗ b,xy -vb,xy) 1dt Angular velocity tracking Rvel,yaw φ(ω∗ b,z -ωb,z) 0.5dt Linear velocity penalty Rvel,z -v2 ...
- **p. 10 / 2 Background - extractive body cue:** Setting new DOF states does not affect the root state.
- **p. 18 / 4. Robotic Hands - extractive body cue:** Also note that this variant does not use any randomisations.
- **p. 20 / 4. Robotic Hands - extractive body cue:** Interestingly, despite having fewer degrees of freedom this hand does not achieve as high consecutive successes as Shadow hand.

## Why Read It

RL, IL, offline learning, and robot data의 benchmark 문제를 이해하기 위해 읽는다. 본문은 However, some bottlenecks were still not addressed in the work - simulation was on GPU but physics state was copied back to CPU.를 문제로 두고, To address these bottlenecks, we present Isaac Gym - an end-to-end high performance robotics simulation platform.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 4 (1 Introduction), p. 7 (2 Background), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 5 (1 Introduction), p. 30 (A.3 Hyperparameters for Training PPO) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
