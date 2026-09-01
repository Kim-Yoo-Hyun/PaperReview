# Evaluation - SurRoL: An Open-source Reinforcement Learning Centered and dVRK Compatible Platform for Surgical Robot Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ieeexplore.ieee.org/document/9635867; PDF retrieval source: https://arxiv.org/pdf/2108.13035. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS)): By contrast, the policy trained in the Interact manner with improved physics simulation is more robust to environment changes with a high success rate.

## Evaluation Body Digest

- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** 1) Experiment Setup: In our RL environments, we set up the manipulation workspace for robots and objects to interact within.
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** The physical evaluation environments are set the same with only successful episodes for both policies in simulation to ensure fair comparisons.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** The average success rates for goal-based tasks and episode returns for the reward-based task (ActiveTrack) are shown over three random seeds, with one epoch equalling ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** From the results, though HER(+DEMO) performs well for robots with relatively large grippers and error tolerance [32], it performs poorly with tiny surgical instruments and ...
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** 3) Demonstration using Scripted Policies: To demonstrate our manipulation tasks, we design scripted policies with heuristics given the ground-truth states available in the simulation, with ...
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** The success rates are reported based on 50 episodes for each method, as shown in Table.
- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** In this section, we focus on the proposed learning-based tasks and want to answer the following questions: 1) Do the tasks in our simulation platform ...
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** The policy generates joint position actions in step, converted from corresponding cVc expressed in the camera frame, and center the cube in the captured image ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 4).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / SIMULATION | By contrast, the policy trained in the Interact manner with improved physics simulation is more robust to environment changes with a high success rate. | p. 7 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SIMULATION | The success rates and episode returns are used as the evaluation metrics for goal-based and reward-based tasks, respectively, as in [32], [9], [10]. | p. 5 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SIMULATION | The mean success rate and standard deviation of three trained policies for the two manners are presented based on the evaluation of 200 episodes ... | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SIMULATION | Epoch 30 40 50 10 20 0.0 0.2 0.4 0.6 0.8 1.0 Success Rate BiPegTransfer with Variants (1) Approach (2) Pick (3) Lift (4) ... | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SIMULATION | The success rates are reported based on 50 episodes for each method, as shown in Table. | p. 7 (IV. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** 1) Experiment Setup: In our RL environments, we set up the manipulation workspace for robots and objects to interact within.
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** The physical evaluation environments are set the same with only successful episodes for both policies in simulation to ensure fair comparisons.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** The average success rates for goal-based tasks and episode returns for the reward-based task (ActiveTrack) are shown over three random seeds, with one epoch equalling ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** From the results, though HER(+DEMO) performs well for robots with relatively large grippers and error tolerance [32], it performs poorly with tiny surgical instruments and ...
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** 3) Demonstration using Scripted Policies: To demonstrate our manipulation tasks, we design scripted policies with heuristics given the ground-truth states available in the simulation, with ...
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** The success rates are reported based on 50 episodes for each method, as shown in Table.
- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** In this section, we focus on the proposed learning-based tasks and want to answer the following questions: 1) Do the tasks in our simulation platform ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1. Our SurRoL is able to support more surgical opera- tion scenarios by incorporating more single-handed/bimanual PSM(s) and ECM control tasks. Further, the designed ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1. System design of SurRoL. SurRoL provides dVRK compatible simulation environments for surgical robot learning (left), with Gym-like interfaces for reinforcement learning algorithm development ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2. PSM and ECM kinematics. a) PSM is a 6-DoF actuated robot with instruments. b) ECM is a 4-DoF actuated robot with the camera ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 3. Examples of the demonstration. To demonstrate the proposed tasks and overcome the sample complexity, we provide the scripted policy for each and collect ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 4. Example of the reward-based environment ECM ActiveTrack. Each time environment resets, waypoints are sampled in the workspace randomly, generating the moving path online ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 5. Evaluation results for ten proposed tasks. The average success rates for goal-based tasks and episode returns for the reward-based task (ActiveTrack) are shown ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 6. Analysis of the BiPegTransfer using HER+DEMO. We analyze the difficulty for long-range skill learning by segmenting the bimanual peg transfer task into multiple ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 7. Different levels of physical interaction. The object is attached to the jaw if the tip-object distance is below a certain threshold with limited ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 1) Experiment Setup: In our RL environments, we set up the manipulation workspace for robots and objects to interact within. | embodiment, simulator version and control stack | p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Task/environment | The physical evaluation environments are set the same with only successful episodes for both policies in simulation to ensure fair comparisons. | reset, timeout, object/scene variation | p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 2 (III. METHODS), p. 1 (I. INTRODUCTION) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 5. Evaluation results for ten proposed tasks. The average success rates for goal-based tasks and episode returns for the reward-based task (ActiveTrack) are ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| The policy generates joint position actions in step, converted from corresponding cVc expressed in the camera frame, and center the cube in the captured ... | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| The mean success rate and standard deviation of three trained policies for the two manners are presented based on the evaluation of 200 episodes ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| The success rates are reported based on 50 episodes for each method, as shown in Table. | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| Few experiences with high reward lead the learning to diverge in the early stage, as the policy gradually finds that random actions produce similar ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Example of the reward-based environment ECM ActiveTrack. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Fig. 1. Our SurRoL is able to support more surgical opera- tion scenarios by incorporating more single-handed/bimanual PSM(s) and ECM control tasks. Further, the ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 3. Examples of the demonstration. To demonstrate the proposed tasks and overcome the sample complexity, we provide the scripted policy for each and ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 4) Evaluation Results: A summary of the evaluation results for RL baselines is shown in Fig. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| Fig. 2. PSM and ECM kinematics. a) PSM is a 6-DoF actuated robot with instruments. b) ECM is a 4-DoF actuated robot with the ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| We also observe that in StaticTrack, the learned policy can smoothly center the target object without the jittering effect, which is non-trivial for the ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| The physical evaluation environments are set the same with only successful episodes for both policies in simulation to ensure fair comparisons. | comparison identity and matched condition | p. 7 (IV. EXPERIMENTS) |
| Fig. 1. System design of SurRoL. SurRoL provides dVRK compatible simulation environments for surgical robot learning (left), with Gym-like interfaces for reinforcement learning algorithm ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We also observe that in StaticTrack, the learned policy can smoothly center the target object without the jittering effect, which is non-trivial for the ... | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| For ECM goalbased tasks without instrument-object physical interaction, the agent can successfully capture the complicated actionobservation relationship using HER, even for MisOrient and StaticTrack, ... | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| Epoch 30 40 50 10 20 0.0 0.2 0.4 0.6 0.8 1.0 Success Rate BiPegTransfer with Variants (1) Approach (2) Pick (3) Lift (4) ... | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| We further analyze the most challenging long-range BiPegTransfer failed even with imitation learning by constructing several variants with different levels of simplification. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions are summarized as follows: • We design an open-source surgical robot learning simulation platform centered on reinforcement learning for surgical skills, ... | By contrast, the policy trained in the Interact manner with improved physics simulation is more robust to environment changes with a high success rate. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Primary metric/result | The success rates and episode returns are used as the evaluation metrics for goal-based and reward-based tasks, respectively, as in [32], [9], [10]. | numeric claim only at cited anchor | p. 5 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** 2) Profiling Analysis: Our SurRoL can run at a real-time rate, at about 150Hz simulation in the reaching tasks with position control and random actions, ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** Epoch 30 40 50 10 20 Epoch 30 40 50 10 20 Epoch 30 40 50 10 20 Epoch 30 40 50 10 20 Epoch ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** The average success rates for goal-based tasks and episode returns for the reward-based task (ActiveTrack) are shown over three random seeds, with one epoch equalling ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** After combining HER and demonstration (HER+DEMO) with Q-filtered behavior cloning [35], the agents manage to solve many challenging tasks with physicsrich simulation within 50 epochs ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** The mean success rate and standard deviation of three trained policies for the two manners are presented based on the evaluation of 200 episodes per ...
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** With 4-DoF actions to adjust the PSM position and the jaw's open/close state, the learned GauzeRetrieve policy can pick and retrieve the gauze to the ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | By visually inspecting the training progress, we find that the agents can quickly learn to approach the object such as the needle and attempt ... | p. 5 (IV. EXPERIMENTS) |
| body limitation/failure cue | Meanwhile, the needle picking point is restricted to the jaw tip to avoid unsafe jaw collisions with the holding surface. | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | Besides, we find some failure cases resulting from dynamics discrepancies between the simulation and the real world, also observed in [14]. | p. 7 (IV. EXPERIMENTS) |
| body limitation/failure cue | Fig. 7. Different levels of physical interaction. The object is attached to the jaw if the tip-object distance is below a certain threshold with ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | However, in PSM settings, HER alone cannot solve all tasks within the given time horizon, mainly due to the tiny object and physically rich ... | p. 5 (IV. EXPERIMENTS) |
| body limitation/failure cue | Surprisingly, even with the correct grasping points, HER+DEMO fails to learn the picking action, which shows the extreme exploration difficulties during learning (Fig. | p. 6 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Most of the training and testing experiments are performed on a desktop with Ubuntu 18.04, Inter 3.6GHz CPU with 32GB RAM, and an Nvidia ... | p. 5 (IV. EXPERIMENTS) |
| 2) Profiling Analysis: Our SurRoL can run at a real-time rate, at about 150Hz simulation in the reaching tasks with position control and random ... | p. 5 (IV. EXPERIMENTS) |
| The average success rates for goal-based tasks and episode returns for the reward-based task (ActiveTrack) are shown over three random seeds, with one epoch ... | p. 6 (IV. EXPERIMENTS) |
| After combining HER and demonstration (HER+DEMO) with Q-filtered behavior cloning [35], the agents manage to solve many challenging tasks with physicsrich simulation within 50 ... | p. 6 (IV. EXPERIMENTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** By visually inspecting the training progress, we find that the agents can quickly learn to approach the object such as the needle and attempt to ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** Meanwhile, the needle picking point is restricted to the jaw tip to avoid unsafe jaw collisions with the holding surface.
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** Besides, we find some failure cases resulting from dynamics discrepancies between the simulation and the real world, also observed in [14].
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 7. Different levels of physical interaction. The object is attached to the jaw if the tip-object distance is below a certain threshold with limited ...
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** However, in PSM settings, HER alone cannot solve all tasks within the given time horizon, mainly due to the tiny object and physically rich interaction ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** Surprisingly, even with the correct grasping points, HER+DEMO fails to learn the picking action, which shows the extreme exploration difficulties during learning (Fig.

- **PDF anchors reviewed:** datasets p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), metrics p. 6 (Figure/Table caption), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), baselines p. 5 (IV. EXPERIMENTS), p. 3 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 2 (Figure/Table caption), results p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
