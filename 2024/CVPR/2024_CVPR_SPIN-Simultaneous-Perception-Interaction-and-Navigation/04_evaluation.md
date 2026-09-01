# Evaluation - SPIN: Simultaneous Perception, Interaction and Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Uppal_SPIN_Simultaneous_Perception_Interaction_and_Navigation_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Uppal_SPIN_Simultaneous_Perception_Interaction_and_Navigation_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.3. Simulation results), p. 7 (4.3. Simulation results), p. 8 (4.3. Simulation results), p. 8 (4.3. Simulation results), p. 5 (4. Results and Analysis), p. 5 (4. Results and Analysis)): Ours achieves ≈ 68% higher success rate than the FixCam baseline with the 18139

## Evaluation Body Digest

- **p. 5 / 4. Results and Analysis - extractive body cue:** While simulation benchmarks are useful for fair comparison with baselines as well as reproducibility, real-world experimenting is essential for determining the efficacy of our system ...
- **p. 7 / 4.3. Simulation results - extractive body cue:** The simulation benchmarks have 6 scenes, 2 of each easy, medium and hard environments.
- **p. 5 / 4. Results and Analysis - extractive body cue:** For this, we test our system on various real-world environments as shown in Figure 1 and benchmark its performance on 2 real-world setups as described ...
- **p. 7 / 4.2. Real-world results - extractive body cue:** We test on two real-world scenes - an academic lab and an open study area with couches and a kitchenette next to it with both ...
- **p. 6 / 4.1. Emergent Behavior - extractive body cue:** We see several such behaviors during real-world experimentation which were neither planned nor specifically trained for in simulation but emerge as a result of a ...
- **p. 8 / 4.3. Simulation results - extractive body cue:** Our method is significantly better than the Mapping baseline because the systematic noise in the object locations makes it hard for the robot to avoid ...
- **p. 6 / 4. Results and Analysis - extractive body cue:** (a) While our simulation lacks dynamic obstacles, the robot can still evade them because the policy continuously adjusts its plan.
- **p. 8 / 4.3. Simulation results - extractive body cue:** Active vision is needed necessary for the robot to move effectively through a cluttered environment.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mobile base와 one/two-arm manipulation environment.
- **Input boundary:** egocentric RGB-D, language/task goal, base-arm proprioception.
- **Output/decision under evaluation:** base motion plus arm/gripper action.
- **Primary target:** long-horizon task success, reachability, collision과 recovery.
- **Detected evaluation headings:** 3. Experimental Setup (p. 5); 4. Results and Analysis (p. 5); 4.2. Real-world results (p. 7); 4.3. Simulation results (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Simulation results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Ours achieves ≈ 68% higher success rate than the FixCam baseline with the 18139 | p. 7 (4.3. Simulation results) |
| 4.3. Simulation results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method achieves ≈33% higher success rate than the NoPointNet baseline since permutation invariant scandots latent makes the optimization problem easier and also generalizes ... | p. 7 (4.3. Simulation results) |
| 4.3. Simulation results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Finally, we compare between the decoupled (DVO) and coupled (CVO) variants of our method and find that they achieve similar performance. | p. 8 (4.3. Simulation results) |
| 4.3. Simulation results | EMPIRICAL / REAL-ROBOT OR HARDWARE | We report the success rate of our method compared with the baseline. | p. 8 (4.3. Simulation results) |
| 4. Results and Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | (2) Can an active visual agent outperform a classical agent that relies on pre-built maps? | p. 5 (4. Results and Analysis) |

## Dataset / Benchmark Role

- **p. 5 / 4. Results and Analysis - extractive body cue:** While simulation benchmarks are useful for fair comparison with baselines as well as reproducibility, real-world experimenting is essential for determining the efficacy of our system ...
- **p. 7 / 4.3. Simulation results - extractive body cue:** The simulation benchmarks have 6 scenes, 2 of each easy, medium and hard environments.
- **p. 5 / 4. Results and Analysis - extractive body cue:** For this, we test our system on various real-world environments as shown in Figure 1 and benchmark its performance on 2 real-world setups as described ...
- **p. 7 / 4.2. Real-world results - extractive body cue:** We test on two real-world scenes - an academic lab and an open study area with couches and a kitchenette next to it with both ...
- **p. 6 / 4.1. Emergent Behavior - extractive body cue:** We see several such behaviors during real-world experimentation which were neither planned nor specifically trained for in simulation but emerge as a result of a ...
- **p. 8 / 4.3. Simulation results - extractive body cue:** Our method is significantly better than the Mapping baseline because the systematic noise in the object locations makes it hard for the robot to avoid ...
- **p. 6 / 4. Results and Analysis - extractive body cue:** (a) While our simulation lacks dynamic obstacles, the robot can still evade them because the policy continuously adjusts its plan.
- **p. 8 / 4.3. Simulation results - extractive body cue:** Active vision is needed necessary for the robot to move effectively through a cluttered environment.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Learning to SPIN: Our robot learns to simultaneously perceive, manipulate, and navigate cluttered unstructured environments in a whole-body fashion. The robot has an ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Human and robot illustration of whole-body navigation through the clutter. robot did not see during training time. Our approach presents a radical hypothesis ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. We learn a policy that uses ego-vision to simultaneously perceive, interact, and navigate in cluttered environments. We propose two methods: (1) Coupled Visuomotor ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. We illustrate one scenario of the simulation benchmark here with many obstacles in a narrow passage. The agent learns to develop whole-body coordination ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. (Left) We compute visible scandots by projecting them to the camera frame and checking if they lie within the image plane (Right) the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6. Types of emergent behavior exhibited by SPIN (a) dynamic obstacle avoidance (b) whole-body movement (c) adaptive rerouting. these questions in Section 4.3. Our ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. We evaluate the success rate on 10 random environments with an average of 3 fixed seeds across all difficulty scenarios based on obstacle ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. We compare our method against a classical mapping and planning baseline for navigation in cluttered scenes with both static as well as dynamic ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | While simulation benchmarks are useful for fair comparison with baselines as well as reproducibility, real-world experimenting is essential for determining the efficacy of our ... | embodiment, simulator version and control stack | p. 5 (4. Results and Analysis), p. 7 (4.3. Simulation results) |
| Task/environment | The simulation benchmarks have 6 scenes, 2 of each easy, medium and hard environments. | reset, timeout, object/scene variation | p. 7 (4.3. Simulation results), p. 5 (4. Results and Analysis) |
| Observation/sensor | egocentric RGB-D, language/task goal, base-arm proprioception | calibration, preprocessing, privileged input | p. 4 (2. Method), p. 4 (2. Method) |
| Output/decision | base motion plus arm/gripper action | action frame, controller and termination | p. 5 (2.2. Phase 2 - From Scandots to Depth), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 2 we compare success rate and average number of collisions. | definition/direction/unit from same section | p. 7 (4.2. Real-world results) |
| Ours achieves ≈ 68% higher success rate than the FixCam baseline with the 18139 | definition/direction/unit from same section | p. 7 (4.3. Simulation results) |
| We report the success rate of our method compared with the baseline. | definition/direction/unit from same section | p. 8 (4.3. Simulation results) |
| We first teleoperate the robot for 3-5 minutes to construct a map using the onboard 2D RPLidar using gmapping. | definition/direction/unit from same section | p. 5 (3. Experimental Setup) |
| Static Obstacles Dynamic Obstacles Scenario 1 Ours Classical Ours Classical Average Success 0.8 0.6 0.6 0.0 Average # Collisions 1.0 0.4 1.6 1.2 Scenario ... | definition/direction/unit from same section | p. 8 (4.3. Simulation results) |
| The learned policy operates at 10Hz and we do velocity control for the robot base and position control for all the other joints. | definition/direction/unit from same section | p. 5 (3. Experimental Setup) |
| We illustrate three such scenarios in Figure 6. | definition/direction/unit from same section | p. 6 (4.1. Emergent Behavior) |
| As highlighted in several frames, Figure 6a depicts robustness to adversarially placed dynamic obstacles that constantly block the path of the robot. | definition/direction/unit from same section | p. 6 (4.1. Emergent Behavior) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We report the success rate of our method compared with the baseline. | comparison identity and matched condition | p. 8 (4.3. Simulation results) |
| While simulation benchmarks are useful for fair comparison with baselines as well as reproducibility, real-world experimenting is essential for determining the efficacy of our ... | comparison identity and matched condition | p. 5 (4. Results and Analysis) |
| (2) Can an active visual agent outperform a classical agent that relies on pre-built maps? | comparison identity and matched condition | p. 5 (4. Results and Analysis) |
| Overall, our method is able to succeed 20-40% more than the classical baseline. | comparison identity and matched condition | p. 7 (4.2. Real-world results) |
| Ours achieves ≈ 68% higher success rate than the FixCam baseline with the 18139 | comparison identity and matched condition | p. 7 (4.3. Simulation results) |
| For the classical baseline, we teleoperate the robot for 2-3 min. camera pointing straight ahead. | comparison identity and matched condition | p. 8 (4.3. Simulation results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This is used to test whether reactive navigation is superior to planning. • NoPointNet: Instead of passing object scandots through a permutation-invariant PointNet architecture, ... | component/input/data sensitivity | p. 5 (3. Experimental Setup) |
| Our method achieves ≈33% higher success rate than the NoPointNet baseline since permutation invariant scandots latent makes the optimization problem easier and also generalizes ... | component/input/data sensitivity | p. 7 (4.3. Simulation results) |
| Finally, we compare between the decoupled (DVO) and coupled (CVO) variants of our method and find that they achieve similar performance. | component/input/data sensitivity | p. 8 (4.3. Simulation results) |
| The classical performs reasonably in static environments, it quickly breaks with dynamic obstacles like humans walking around, whereas our method shows more robust reactivity ... | component/input/data sensitivity | p. 8 (4.3. Simulation results) |
| Figure 4. We illustrate one scenario of the simulation benchmark here with many obstacles in a narrow passage. The agent learns to develop whole-body ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We find that our method outperforms classical methods and baselines which do not use active vision. | Ours achieves ≈ 68% higher success rate than the FixCam baseline with the 18139 | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.3. Simulation results), p. 7 (4.3. Simulation results), p. 8 (4.3. Simulation results), p. 8 (4.3. Simulation results), p. 5 (4. Results and Analysis), p. 5 (4. Results and Analysis) |
| Primary metric/result | Our method achieves ≈33% higher success rate than the NoPointNet baseline since permutation invariant scandots latent makes the optimization problem easier and also generalizes ... | numeric claim only at cited anchor | p. 7 (4.3. Simulation results) |

- Numeric sentences retained from the body:
- **p. 5 / 3. Experimental Setup - extractive body cue:** The robot has 10 actuated joints which include 2 degrees of freedom for the camera, 2 for base rotation and translation, 2 for the arm, ...
- **p. 5 / 3. Experimental Setup - extractive body cue:** The learned policy operates at 10Hz and we do velocity control for the robot base and position control for all the other joints.
- **p. 5 / 3. Experimental Setup - extractive body cue:** We train using IsaacGymEnvs [26] using 8192 environments which takes 6 hours of training for phase 1 and 10 hours of training time for phase ...
- **p. 7 / 4.3. Simulation results - extractive body cue:** The simulation benchmarks have 6 scenes, 2 of each easy, medium and hard environments.
- **p. 7 / 4.3. Simulation results - extractive body cue:** The evaluation metrics are reported as an average of 10 episodes with random agent and obstacle initialization across 3 seeds.
- **p. 7 / 4.3. Simulation results - extractive body cue:** For each scenario, we report the success rate and average episode length across 10 rollouts.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 4. We illustrate one scenario of the simulation benchmark here with many obstacles in a narrow passage. The agent learns to develop whole-body ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | What are the limitations of the latter? | p. 5 (4. Results and Analysis) |
| body limitation/failure cue | We observe that in cases when there is no feasible path for the robot to navigate through, it also learns to stop and look ... | p. 6 (4.1. Emergent Behavior) |
| body limitation/failure cue | 2 we compare success rate and average number of collisions. | p. 7 (4.2. Real-world results) |
| body limitation/failure cue | It has the emergent ability to avoid a new obstacle in space, whereas the classical baseline relies on the pre-built map and fails entirely. | p. 7 (4.2. Real-world results) |
| body limitation/failure cue | Static Obstacles Dynamic Obstacles Scenario 1 Ours Classical Ours Classical Average Success 0.8 0.6 0.6 0.0 Average # Collisions 1.0 0.4 1.6 1.2 Scenario ... | p. 8 (4.3. Simulation results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We train using IsaacGymEnvs [26] using 8192 environments which takes 6 hours of training for phase 1 and 10 hours of training time for ... | p. 5 (3. Experimental Setup) |
| (Left) We compute visible scandots by projecting them to the camera frame and checking if they lie within the image plane (Right) the stretch ... | p. 5 (3. Experimental Setup) |
| Since rendering depth images directly from the robot camera is expensive, we must instead use an ersatz version that contains the same information and ... | p. 3 (2. Method) |
| In the first one, we learn mobile manipulation behaviors via RL using a cheapto-compute variant of depth and in phase 2 we train a ... | p. 3 (2. Method) |
| Indeed, we observe that this requires billions of samples inside a GPU-accelerated simulator to optimize which may not always be feasible in practice. | p. 4 (2. Method) |
| We run the planner to only plan the base motion. | p. 7 (4.2. Real-world results) |
| The evaluation metrics are reported as an average of 10 episodes with random agent and obstacle initialization across 3 seeds. | p. 7 (4.3. Simulation results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. We illustrate one scenario of the simulation benchmark here with many obstacles in a narrow passage. The agent learns to develop whole-body coordination ...
- **p. 5 / 4. Results and Analysis - extractive body cue:** What are the limitations of the latter?
- **p. 6 / 4.1. Emergent Behavior - extractive body cue:** We observe that in cases when there is no feasible path for the robot to navigate through, it also learns to stop and look around ...
- **p. 7 / 4.2. Real-world results - extractive body cue:** 2 we compare success rate and average number of collisions.
- **p. 7 / 4.2. Real-world results - extractive body cue:** It has the emergent ability to avoid a new obstacle in space, whereas the classical baseline relies on the pre-built map and fails entirely.
- **p. 8 / 4.3. Simulation results - extractive body cue:** Static Obstacles Dynamic Obstacles Scenario 1 Ours Classical Ours Classical Average Success 0.8 0.6 0.6 0.0 Average # Collisions 1.0 0.4 1.6 1.2 Scenario 2 ...

- **PDF anchors reviewed:** datasets p. 5 (4. Results and Analysis), p. 7 (4.3. Simulation results), p. 5 (4. Results and Analysis), p. 7 (4.2. Real-world results), p. 6 (4.1. Emergent Behavior), p. 8 (4.3. Simulation results), metrics p. 7 (4.2. Real-world results), p. 7 (4.3. Simulation results), p. 8 (4.3. Simulation results), p. 5 (3. Experimental Setup), p. 8 (4.3. Simulation results), p. 5 (3. Experimental Setup), baselines p. 8 (4.3. Simulation results), p. 5 (4. Results and Analysis), p. 5 (4. Results and Analysis), p. 7 (4.2. Real-world results), p. 7 (4.3. Simulation results), p. 8 (4.3. Simulation results), results p. 7 (4.3. Simulation results), p. 7 (4.3. Simulation results), p. 8 (4.3. Simulation results), p. 8 (4.3. Simulation results), p. 5 (4. Results and Analysis), p. 5 (4. Results and Analysis).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
