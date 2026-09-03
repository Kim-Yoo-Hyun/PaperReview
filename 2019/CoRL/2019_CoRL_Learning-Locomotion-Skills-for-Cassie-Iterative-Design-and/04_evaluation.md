# Evaluation - Learning Locomotion Skills for Cassie: Iterative Design and Sim-to-Real

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.cs.ubc.ca/~van/papers/2019-CORL-cassie/index.html; PDF retrieval source: https://arxiv.org/pdf/1903.09537. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 1 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP)): Fig. 1: Cassie walking on a treadmill with a neural network policy. gradient updates that combine the supervised learning samples and conventional DRL policy-gradient samples, we allow for the iterative ...

## Evaluation Body Digest

- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** Rapid deployment and testing is aided by the simulator using the same network-based interface as the physical robot, which means that tests can be moved ...
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** Hardware Tests We deploy a selection of trained policies on a physical Cassie robot.
- **p. 4 / V. EXPERIMENTAL SETUP - extractive body cue:** The simulator includes a detailed model of the robot's rigid-bodydynamics, including the reflected inertia of the robot's motors, as well as empirically measured noise and ...
- **p. 4 / V. EXPERIMENTAL SETUP - extractive body cue:** 3, is designed and built by Agility Robotics.
- **p. 4 / V. EXPERIMENTAL SETUP - extractive body cue:** Training Framework We adopt the framework used in [41] for training several initial policies πe, where we reward the agent for producing motion that approximately ...
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** We further note that finetuning a policy based on a new reward function often results in undesired changes to the policy as it can readily ...
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** [25], where each rollout is started from some states sampled from the reference motions and is terminated when the height of the pelvis is less ...
- **p. 4 / V. EXPERIMENTAL SETUP - extractive body cue:** A benefit of the fixed covariance is that because of the noise constantly injected into the system during training, the resulting policy will adapt itself ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** legged robot, terrain과 contact dynamics.
- **Input boundary:** proprioception, terrain/perception observation과 velocity command.
- **Output/decision under evaluation:** joint target, torque, footstep 또는 locomotion action.
- **Primary target:** velocity/progress, stability, energy와 terrain generalization.
- **Detected evaluation headings:** V. EXPERIMENTAL SETUP (p. 4).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 1: Cassie walking on a treadmill with a neural network policy. gradient updates that combine the supervised learning samples and conventional DRL policy-gradient ... | p. 1 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 5: Network sizes impact the final result for reinforce- ment learning. We observe that larger network sizes typically learn faster and yield more ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 7: Comparison of the norm of the angular velocity of the pelvis before and after optimization. We extend this iterative-improvement approach to an ... | p. 7 (Figure/Table caption) |
| V. EXPERIMENTAL SETUP | EMPIRICAL / REAL-ROBOT OR HARDWARE | Several intermediate policies are also successfully tested on the robot, but are not shown due to videoduration constraints. | p. 5 (V. EXPERIMENTAL SETUP) |
| V. EXPERIMENTAL SETUP | EMPIRICAL / REAL-ROBOT OR HARDWARE | We further note that finetuning a policy based on a new reward function often results in undesired changes to the policy as it can ... | p. 5 (V. EXPERIMENTAL SETUP) |

## Dataset / Benchmark Role

- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** Rapid deployment and testing is aided by the simulator using the same network-based interface as the physical robot, which means that tests can be moved ...
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** Hardware Tests We deploy a selection of trained policies on a physical Cassie robot.
- **p. 4 / V. EXPERIMENTAL SETUP - extractive body cue:** The simulator includes a detailed model of the robot's rigid-bodydynamics, including the reflected inertia of the robot's motors, as well as empirically measured noise and ...
- **p. 4 / V. EXPERIMENTAL SETUP - extractive body cue:** 3, is designed and built by Agility Robotics.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Cassie walking on a treadmill with a neural network policy. gradient updates that combine the supervised learning samples and conventional DRL policy-gradient samples, ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: A walking policy produces a limit cycle, represented by the blue closed curve, and the green arrows indicate the required feedback to return ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Left: The bipedal robot Cassie used for evaluation. The red arrows indicate the axes of actuated joints, the yellow arrows indicate passive joints ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Our policy design process. Four tracking-based policies are used as a starting point. DASS samples are passed from one policy to the next ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Network sizes impact the final result for reinforce- ment learning. We observe that larger network sizes typically learn faster and yield more stable ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6: Joint angles of the left knee in the expert (teacher) dataset, as collected via policy cloning or DASS. Behavior cloning only visits a ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Comparison of the norm of the angular velocity of the pelvis before and after optimization. We extend this iterative-improvement approach to an tracking-based ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: Phase portrait for all the joints on the left leg during step in place. The blue curve is before optimizing for less joint ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Rapid deployment and testing is aided by the simulator using the same network-based interface as the physical robot, which means that tests can be ... | embodiment, simulator version and control stack | p. 5 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP) |
| Task/environment | Hardware Tests We deploy a selection of trained policies on a physical Cassie robot. | reset, timeout, object/scene variation | p. 5 (V. EXPERIMENTAL SETUP), p. 4 (V. EXPERIMENTAL SETUP) |
| Observation/sensor | proprioception, terrain/perception observation과 velocity command | calibration, preprocessing, privileged input | p. 3 (IV. METHODS), p. 3 (IV. METHODS) |
| Output/decision | joint target, torque, footstep 또는 locomotion action | action frame, controller and termination | p. 2 (III. PRELIMINARIES), p. 2 (III. PRELIMINARIES) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Training Framework We adopt the framework used in [41] for training several initial policies πe, where we reward the agent for producing motion that ... | definition/direction/unit from same section | p. 4 (V. EXPERIMENTAL SETUP) |
| We further note that finetuning a policy based on a new reward function often results in undesired changes to the policy as it can ... | definition/direction/unit from same section | p. 5 (V. EXPERIMENTAL SETUP) |
| [25], where each rollout is started from some states sampled from the reference motions and is terminated when the height of the pelvis is ... | definition/direction/unit from same section | p. 5 (V. EXPERIMENTAL SETUP) |
| A benefit of the fixed covariance is that because of the noise constantly injected into the system during training, the resulting policy will adapt ... | definition/direction/unit from same section | p. 4 (V. EXPERIMENTAL SETUP) |
| Fig. 1: Cassie walking on a treadmill with a neural network policy. gradient updates that combine the supervised learning samples and conventional DRL policy-gradient ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 2: A walking policy produces a limit cycle, represented by the blue closed curve, and the green arrows indicate the required feedback to ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Fig. 5: Network sizes impact the final result for reinforce- ment learning. We observe that larger network sizes typically learn faster and yield more ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Fig. 7: Comparison of the norm of the angular velocity of the pelvis before and after optimization. We extend this iterative-improvement approach to an ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 5: Network sizes impact the final result for reinforce- ment learning. We observe that larger network sizes typically learn faster and yield more ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Fig. 7: Comparison of the norm of the angular velocity of the pelvis before and after optimization. We extend this iterative-improvement approach to an ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| At each level, all policies are trained from scratch instead of fine-tuning the previous policies. | component/input/data sensitivity | p. 5 (V. EXPERIMENTAL SETUP) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this section, we present our method for collecting stateaction pairs as a dataset for imitation learning, and how this dataset can be used ... | Fig. 1: Cassie walking on a treadmill with a neural network policy. gradient updates that combine the supervised learning samples and conventional DRL policy-gradient ... | PDF body cue; verify exact table/figure and matched conditions | p. 1 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP) |
| Primary metric/result | Fig. 5: Network sizes impact the final result for reinforce- ment learning. We observe that larger network sizes typically learn faster and yield more ... | numeric claim only at cited anchor | p. 6 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 4 / V. EXPERIMENTAL SETUP - extractive body cue:** It stands approximately 1 meter tall and has a total mass of 31 kg, with most of the weight concentrated in the pelvis.
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** [25], where each rollout is started from some states sampled from the reference motions and is terminated when the height of the pelvis is less ...
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** The policy updates its output joint PD targets once every 30 ms based on the latest state data and sends the targets back to the ...
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** The embedded computer executes a PD control loop for each joint at the full 2 kHz rate, with targets updating every 30 ms based on ...
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** The network link between two computers introduces an additional 1-2 ms of latency beyond running the simulator and policy on the same machine, and many ...
- **p. 6 / VI. POLICY COMPRESSION AND DISTILLATION - extractive body cue:** With as little as 600 samples, we can recover a stepping in place policy with a (16, 16) hidden layer size.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The final policies obtained are robust to unmodeled noise and enable us to transfer them from simulation to the physical robot without difficulty. | p. 8 (VIII. CONCLUSION AND DISCUSSION) |
| body limitation/failure cue | We hypothesize the robustness stems from learning stochastic policies that operate at a low control rate, allowing the final policies to adapt to other ... | p. 8 (VIII. CONCLUSION AND DISCUSSION) |
| body limitation/failure cue | [25], where each rollout is started from some states sampled from the reference motions and is terminated when the height of the pelvis is ... | p. 5 (V. EXPERIMENTAL SETUP) |
| body limitation/failure cue | A benefit of the fixed covariance is that because of the noise constantly injected into the system during training, the resulting policy will adapt ... | p. 4 (V. EXPERIMENTAL SETUP) |
| body limitation/failure cue | Fig. 5: Network sizes impact the final result for reinforce- ment learning. We observe that larger network sizes typically learn faster and yield more ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | Fig. 2: A walking policy produces a limit cycle, represented by the blue closed curve, and the green arrows indicate the required feedback to ... | p. 3 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| This process runs at 2 kHz on an embedded computer directly connected to the robot's hardware. | p. 5 (V. EXPERIMENTAL SETUP) |
| The same filtering and estimation code as used on hardware is used internally in the simulator, rather than giving the policy direct access to ... | p. 5 (V. EXPERIMENTAL SETUP) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / VIII. CONCLUSION AND DISCUSSION - extractive body cue:** The final policies obtained are robust to unmodeled noise and enable us to transfer them from simulation to the physical robot without difficulty.
- **p. 8 / VIII. CONCLUSION AND DISCUSSION - extractive body cue:** We hypothesize the robustness stems from learning stochastic policies that operate at a low control rate, allowing the final policies to adapt to other noise.
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** [25], where each rollout is started from some states sampled from the reference motions and is terminated when the height of the pelvis is less ...
- **p. 4 / V. EXPERIMENTAL SETUP - extractive body cue:** A benefit of the fixed covariance is that because of the noise constantly injected into the system during training, the resulting policy will adapt itself ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Network sizes impact the final result for reinforce- ment learning. We observe that larger network sizes typically learn faster and yield more stable ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: A walking policy produces a limit cycle, represented by the blue closed curve, and the green arrows indicate the required feedback to return ...

- **Evidence anchors reviewed:** datasets p. 5 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP), p. 4 (V. EXPERIMENTAL SETUP), p. 4 (V. EXPERIMENTAL SETUP), metrics p. 4 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP), p. 4 (V. EXPERIMENTAL SETUP), p. 1 (Figure/Table caption), p. 3 (Figure/Table caption), baselines p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), results p. 1 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
