# Evaluation - Learning Vision-Based Bipedal Locomotion for Challenging Terrain

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2309.14594; PDF retrieval source: https://arxiv.org/pdf/2309.14594. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (Figure/Table caption), p. 5 (VI. SIMULATION RESULTS), p. 6 (VI. SIMULATION RESULTS), p. 6 (VI. SIMULATION RESULTS), p. 1 (Figure/Table caption)): Fig. 6: Depth image from simulation and real world, with corre- sponding real predicted heightmap and simulation heightmap. mode of terrains. For more difficult terrain modes, however, policies w/o Learned ...

## Evaluation Body Digest

- **p. 6 / VI. SIMULATION RESULTS - extractive PDF cue:** Episodes with foot collision indicates the number of episodes that have one or more foot collision events occurred during rollouts, and such random collision events ...
- **p. 5 / VI. SIMULATION RESULTS - extractive PDF cue:** When looking at policy w/o Foot Collision Reward in simulation, the policy learns to deal with collisions and treat the collisions as potentially useful proprioceptive ...
- **p. 6 / VI. SIMULATION RESULTS - extractive PDF cue:** Model Architecture Reconstruction Loss (MAE) [cm] LSTM 2.806 Transformer 4.221 MLP 4.932 LSTM (w/o robot states) 4.448 loop performance in simulation shown in Figure 7-B.
- **p. 5 / VI. SIMULATION RESULTS - extractive PDF cue:** For example, the robot will walk up high step-ups by sliding the foot along the vertical surface of the terrain.
- **p. 5 / VI. SIMULATION RESULTS - extractive PDF cue:** Although foot collisions lead to frequent failures, policy w/o Foot Collision Reward has a similar success rate as Ours.
- **p. 5 / VI. SIMULATION RESULTS - extractive PDF cue:** In Success Rate, all policies have approximately the same performance at easy Fig.
- **p. 6 / VI. SIMULATION RESULTS - extractive PDF cue:** In Success Rate, all predictors produce similar performance over each terrain mode.
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 4: Types of terrain used in training. a real robot. In particular, we use a three component reward function where all components are weighted ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** legged robot, terrain과 contact dynamics.
- **Input boundary:** proprioception, terrain/perception observation과 velocity command.
- **Output/decision under evaluation:** joint target, torque, footstep 또는 locomotion action.
- **Primary target:** velocity/progress, stability, energy와 terrain generalization.
- **Detected evaluation headings:** VI. SIMULATION RESULTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 6: Depth image from simulation and real world, with corre- sponding real predicted heightmap and simulation heightmap. mode of terrains. For more difficult ... | p. 5 (Figure/Table caption) |
| VI. SIMULATION RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | In Success Rate, all policies have approximately the same performance at easy Fig. | p. 5 (VI. SIMULATION RESULTS) |
| VI. SIMULATION RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | In Success Rate, all predictors produce similar performance over each terrain mode. | p. 6 (VI. SIMULATION RESULTS) |
| VI. SIMULATION RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Success rate indicates the robot does not fall down for 10 seconds of rollouts. | p. 6 (VI. SIMULATION RESULTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 1: Our fully learned controller integrates vision and locomotion for reactive and agile gaits over terrains. The proposed approach enables bipedal robot Cassie ... | p. 1 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / VI. SIMULATION RESULTS - extractive PDF cue:** Episodes with foot collision indicates the number of episodes that have one or more foot collision events occurred during rollouts, and such random collision events ...
- **p. 5 / VI. SIMULATION RESULTS - extractive PDF cue:** When looking at policy w/o Foot Collision Reward in simulation, the policy learns to deal with collisions and treat the collisions as potentially useful proprioceptive ...
- **p. 6 / VI. SIMULATION RESULTS - extractive PDF cue:** Model Architecture Reconstruction Loss (MAE) [cm] LSTM 2.806 Transformer 4.221 MLP 4.932 LSTM (w/o robot states) 4.448 loop performance in simulation shown in Figure 7-B.
- **p. 5 / VI. SIMULATION RESULTS - extractive PDF cue:** For example, the robot will walk up high step-ups by sliding the foot along the vertical surface of the terrain.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: Our fully learned controller integrates vision and locomotion for reactive and agile gaits over terrains. The proposed approach enables bipedal robot Cassie traversing ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 2: Overview of the locomotion policy with vision module. Figure 2 illustrates our overall system, which has two main components: 1) a locomotion policy, ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 3: Policy consists of a blind policy and a vision-based modulator. cos (2π(ϕt + γi t)). Here i ∈[left, right] indicates the leg, ϕ ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 4: Types of terrain used in training. a real robot. In particular, we use a three component reward function where all components are weighted ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 5: Predictor architecture. Heightmap is captured from hardware. Network Architecture and Losses Figure 5 shows the network architecture, which consists of two stages. For ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 6: Depth image from simulation and real world, with corre- sponding real predicted heightmap and simulation heightmap. mode of terrains. For more difficult terrain ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 7: A. Ablation study on policy with simulation heightmap. B. Ablation study on policy with different heightmap predictor architectures. Each ablation study uses data ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Episodes with foot collision indicates the number of episodes that have one or more foot collision events occurred during rollouts, and such random collision ... | embodiment, simulator version and control stack | p. 6 (VI. SIMULATION RESULTS), p. 5 (VI. SIMULATION RESULTS) |
| Task/environment | When looking at policy w/o Foot Collision Reward in simulation, the policy learns to deal with collisions and treat the collisions as potentially useful ... | reset, timeout, object/scene variation | p. 5 (VI. SIMULATION RESULTS), p. 6 (VI. SIMULATION RESULTS) |
| Observation/sensor | proprioception, terrain/perception observation과 velocity command | calibration, preprocessing, privileged input | p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 1 (I. INTRODUCTION) |
| Output/decision | joint target, torque, footstep 또는 locomotion action | action frame, controller and termination | p. 2 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Although foot collisions lead to frequent failures, policy w/o Foot Collision Reward has a similar success rate as Ours. | definition/direction/unit from same section | p. 5 (VI. SIMULATION RESULTS) |
| Fig. 7: A. Ablation study on policy with simulation heightmap. B. Ablation study on policy with different heightmap predictor architectures. Each ablation study uses ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| In Success Rate, all policies have approximately the same performance at easy Fig. | definition/direction/unit from same section | p. 5 (VI. SIMULATION RESULTS) |
| In Success Rate, all predictors produce similar performance over each terrain mode. | definition/direction/unit from same section | p. 6 (VI. SIMULATION RESULTS) |
| Fig. 4: Types of terrain used in training. a real robot. In particular, we use a three component reward function where all components are ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Fig. 5: Predictor architecture. Heightmap is captured from hardware. Network Architecture and Losses Figure 5 shows the network architecture, which consists of two stages. ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Fig. 1: Our fully learned controller integrates vision and locomotion for reactive and agile gaits over terrains. The proposed approach enables bipedal robot Cassie ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 2: Overview of the locomotion policy with vision module. Figure 2 illustrates our overall system, which has two main components: 1) a locomotion ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Episodes with foot collision shows that, compared to Ours, other policies have significantly more foot collisions events. | comparison identity and matched condition | p. 5 (VI. SIMULATION RESULTS) |
| In Episodes with foot collision, compared to LSTM, other models show worse performance and produce more collision events. | comparison identity and matched condition | p. 6 (VI. SIMULATION RESULTS) |
| In Termination due to foot collision, compared to LSTM, other models fails with higher chances from unfavorable foot collisions. | comparison identity and matched condition | p. 6 (VI. SIMULATION RESULTS) |
| Additionally, the comparison also includes an LSTM model, LSTM w/o robot states, that does not use robot states as input. | comparison identity and matched condition | p. 5 (VI. SIMULATION RESULTS) |
| Fig. 4: Types of terrain used in training. a real robot. In particular, we use a three component reward function where all components are ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Policy Performance We use the trained policy, along with a number of different policy setups, to evaluate the performance in simulation for the ablation ... | component/input/data sensitivity | p. 5 (VI. SIMULATION RESULTS) |
| We also implemented other architectures to use for ablations, including an MLP model and a transformer-based model, and they all have robot states and ... | component/input/data sensitivity | p. 5 (VI. SIMULATION RESULTS) |
| Ablation study on policy with different heightmap predictor architectures. | component/input/data sensitivity | p. 6 (VI. SIMULATION RESULTS) |
| Each ablation study uses data collected from a range of terrains defined in Table I. | component/input/data sensitivity | p. 6 (VI. SIMULATION RESULTS) |
| Fig. 2: Overview of the locomotion policy with vision module. Figure 2 illustrates our overall system, which has two main components: 1) a locomotion ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| Fig. 4: Types of terrain used in training. a real robot. In particular, we use a three component reward function where all components are ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The relative encoding means that the heights vary as the robot moves up and down during its gait, but enables us to avoid using ... | Fig. 6: Depth image from simulation and real world, with corre- sponding real predicted heightmap and simulation heightmap. mode of terrains. For more difficult ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (Figure/Table caption), p. 5 (VI. SIMULATION RESULTS), p. 6 (VI. SIMULATION RESULTS), p. 6 (VI. SIMULATION RESULTS), p. 1 (Figure/Table caption) |
| Primary metric/result | In Success Rate, all policies have approximately the same performance at easy Fig. | numeric claim only at cited anchor | p. 5 (VI. SIMULATION RESULTS) |

- Numeric sentences retained from the body:
- **p. 5 / VI. SIMULATION RESULTS - extractive PDF cue:** For each policy setup, we collect 1000 episodes per terrain mode and compute three metrics as shown in Figure 7-A.
- **p. 3 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive PDF cue:** The RL policy operates at 50Hz and outputs PD setpoints for all motors, which are provided to a PD controller operating at 2kHz.
- **p. 3 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive PDF cue:** Episode termination conditions include: 1) roll or pitch angle of the floating base is greater than 15 degrees; 2) the norm of linear velocities of ...
- **p. 4 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive PDF cue:** In addition, the torque command sent to the simulator is delayed randomly up to 3ms.
- **p. 4 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive PDF cue:** The heightmap is passed into the policy with a randomized amount of delay up to 100ms, in order to account for faster locomotion speeds.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 7: A. Ablation study on policy with simulation heightmap. B. Ablation study on policy with different heightmap predictor architectures. Each ablation study uses ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | These random foot collisions with the terrain could lead to failures. | p. 5 (VI. SIMULATION RESULTS) |
| body limitation/failure cue | Indeed, Terminations due to foot collision indicates that collisions account for most failure cases overall. | p. 5 (VI. SIMULATION RESULTS) |
| body limitation/failure cue | In Termination due to foot collision, compared to LSTM, other models fails with higher chances from unfavorable foot collisions. | p. 6 (VI. SIMULATION RESULTS) |
| body limitation/failure cue | Fig. 4: Types of terrain used in training. a real robot. In particular, we use a three component reward function where all components are ... | p. 4 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The policy input includes: 1) proprioceptive information containing the orientation (in quaternion) and angular velocity of the floating base, and position and velocity for ... | p. 2 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY) |
| Each episode runs for a maximum of 400 timesteps, which is 8 seconds of simulated time. | p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY) |
| After the initial command, once during each episode the command is randomly changed at a time randomly sampled from [200, 250] timesteps. | p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY) |
| Terrain Parameter Range Range for Evaluation Easy Hard Ridge height [m] [0.05, 0.6] [0.05, 0.5] [0.5, 0.6] Stair height [m] [0.05, 0.2] [0.05, 0.1] ... | p. 4 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY) |
| For each policy setup, we collect 1000 episodes per terrain mode and compute three metrics as shown in Figure 7-A. | p. 5 (VI. SIMULATION RESULTS) |
| LSTM has implicit history, Transformer has a fixed window size of 0.6 seconds to allow reasonable inference during runtime, and MLP does not have ... | p. 5 (VI. SIMULATION RESULTS) |
| Episodes with foot collision indicates the number of episodes that have one or more foot collision events occurred during rollouts, and such random collision ... | p. 6 (VI. SIMULATION RESULTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 7: A. Ablation study on policy with simulation heightmap. B. Ablation study on policy with different heightmap predictor architectures. Each ablation study uses data ...
- **p. 5 / VI. SIMULATION RESULTS - extractive PDF cue:** These random foot collisions with the terrain could lead to failures.
- **p. 5 / VI. SIMULATION RESULTS - extractive PDF cue:** Indeed, Terminations due to foot collision indicates that collisions account for most failure cases overall.
- **p. 6 / VI. SIMULATION RESULTS - extractive PDF cue:** In Termination due to foot collision, compared to LSTM, other models fails with higher chances from unfavorable foot collisions.
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 4: Types of terrain used in training. a real robot. In particular, we use a three component reward function where all components are weighted ...

- **PDF anchors reviewed:** datasets p. 6 (VI. SIMULATION RESULTS), p. 5 (VI. SIMULATION RESULTS), p. 6 (VI. SIMULATION RESULTS), p. 5 (VI. SIMULATION RESULTS), metrics p. 5 (VI. SIMULATION RESULTS), p. 6 (Figure/Table caption), p. 5 (VI. SIMULATION RESULTS), p. 6 (VI. SIMULATION RESULTS), p. 4 (Figure/Table caption), p. 4 (Figure/Table caption), baselines p. 5 (VI. SIMULATION RESULTS), p. 6 (VI. SIMULATION RESULTS), p. 6 (VI. SIMULATION RESULTS), p. 5 (VI. SIMULATION RESULTS), p. 4 (Figure/Table caption), results p. 5 (Figure/Table caption), p. 5 (VI. SIMULATION RESULTS), p. 6 (VI. SIMULATION RESULTS), p. 6 (VI. SIMULATION RESULTS), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
