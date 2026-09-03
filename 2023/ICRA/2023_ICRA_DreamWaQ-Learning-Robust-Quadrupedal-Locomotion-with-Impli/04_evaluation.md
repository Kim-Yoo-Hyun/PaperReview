# Evaluation - DreamWaQ: Learning Robust Quadrupedal Locomotion with Implicit Terrain Imagination via Deep Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2301.10602; PDF retrieval source: https://arxiv.org/pdf/2301.10602. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (Figure/Table caption), p. 5 (III. EXPERIMENTS), p. 2 (3) A robustness and durability evaluation of the learned), p. 4 (III. EXPERIMENTS), p. 4 (III. EXPERIMENTS), p. 6 (Figure/Table caption)): Fig. 5: Estimation error of CENet and EstimatorNet. The superiority of CENet is highlighted when the robot's feet stumbled by stairs. barplot, as shown in Fig. 4. The significance of ...

## Evaluation Body Digest

- **p. 4 / III. EXPERIMENTS - extractive body cue:** Real-World Experimental Setup Real-world experiments were conducted using a Unitree A1 [26] robot.
- **p. 5 / III. EXPERIMENTS - extractive body cue:** The robot's trajectory was measured using a real-time kinematic (RTK) GPS [39] with a frequency of 10 Hz, mounted on top of the robot.
- **p. 5 / III. EXPERIMENTS - extractive body cue:** Explicit Estimation Comparison We simulated the robot walking in a stairs environment to compare the CENet with EstimatorNet in terms of their squared estimation error, ...
- **p. 2 / 3) A robustness and durability evaluation of the learned - extractive body cue:** To the best of our knowledge, this is the first time a Unitree A1, which is significantly smaller that an ANYmal robot, has been demonstrated ...
- **p. 4 / III. EXPERIMENTS - extractive body cue:** An additional onboard PC with a battery added a payload of approximately 500 g to the robot.
- **p. 2 / 3) A robustness and durability evaluation of the learned - extractive body cue:** policy in the real world was conducted through walking in diverse outdoor environments.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Learning curves of different algorithms. The results shown are obtained from ten different random seeds. The curves and shaded regions indicate the mean ...
- **p. 4 / III. EXPERIMENTS - extractive body cue:** We measured absolute tracking error (ATE) as the performance metric and constructed a

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** legged robot, terrain과 contact dynamics.
- **Input boundary:** proprioception, terrain/perception observation과 velocity command.
- **Output/decision under evaluation:** joint target, torque, footstep 또는 locomotion action.
- **Primary target:** velocity/progress, stability, energy와 terrain generalization.
- **Detected evaluation headings:** 3) A robustness and durability evaluation of the learned (p. 2); III. EXPERIMENTS (p. 4).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 5: Estimation error of CENet and EstimatorNet. The superiority of CENet is highlighted when the robot's feet stumbled by stairs. barplot, as shown ... | p. 5 (Figure/Table caption) |
| III. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The robust performance was achieved through the interplay between accurate estimation and robust policy learning of DreamWaQ. | p. 5 (III. EXPERIMENTS) |
| 3) A robustness and durability evaluation of the learned | EMPIRICAL / REAL-ROBOT OR HARDWARE | Section III presents the experimental setting, results, and an in-depth comparative analysis of the proposed and baseline methods. | p. 2 (3) A robustness and durability evaluation of the learned) |
| III. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results shown are obtained from ten different random seeds. | p. 4 (III. EXPERIMENTS) |
| III. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We measured absolute tracking error (ATE) as the performance metric and constructed a | p. 4 (III. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 4 / III. EXPERIMENTS - extractive body cue:** Real-World Experimental Setup Real-world experiments were conducted using a Unitree A1 [26] robot.
- **p. 5 / III. EXPERIMENTS - extractive body cue:** The robot's trajectory was measured using a real-time kinematic (RTK) GPS [39] with a frequency of 10 Hz, mounted on top of the robot.
- **p. 5 / III. EXPERIMENTS - extractive body cue:** Explicit Estimation Comparison We simulated the robot walking in a stairs environment to compare the CENet with EstimatorNet in terms of their squared estimation error, ...
- **p. 2 / 3) A robustness and durability evaluation of the learned - extractive body cue:** To the best of our knowledge, this is the first time a Unitree A1, which is significantly smaller that an ANYmal robot, has been demonstrated ...
- **p. 4 / III. EXPERIMENTS - extractive body cue:** An additional onboard PC with a battery added a payload of approximately 500 g to the robot.
- **p. 2 / 3) A robustness and durability evaluation of the learned - extractive body cue:** policy in the real world was conducted through walking in diverse outdoor environments.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Overview of DreamWaQ. By learning a locomotion policy in a simulation, the robot can walk through challenging terrains such as stairs with zero-shot ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: The architecture of CENet consists of a body velocity estimation model and an auto-encoder model that shares a unified encoder. The shared encoder ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Learning curves of different algorithms. The results shown are obtained from ten different random seeds. The curves and shaded regions indicate the mean ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Command tracking error represented as a boxplot. ve x and ve y are forward and lateral velocity tracking errors, respectively, measured in m/s. ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5: Estimation error of CENet and EstimatorNet. The superiority of CENet is highlighted when the robot's feet stumbled by stairs. barplot, as shown in ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6: Foot reflex against uncertainties due to (a) stumbling and (b) slipping in unstructured terrains. Real-time experiment videos are available online1. A B Start ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 7: The outdoor trajectory for testing the performance of the DreamWaQ policy was recorded using an RTK-GPS mounted on the robot. Course A consists ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Real-World Experimental Setup Real-world experiments were conducted using a Unitree A1 [26] robot. | embodiment, simulator version and control stack | p. 4 (III. EXPERIMENTS), p. 5 (III. EXPERIMENTS) |
| Task/environment | The robot's trajectory was measured using a real-time kinematic (RTK) GPS [39] with a frequency of 10 Hz, mounted on top of the robot. | reset, timeout, object/scene variation | p. 5 (III. EXPERIMENTS), p. 5 (III. EXPERIMENTS) |
| Observation/sensor | proprioception, terrain/perception observation과 velocity command | calibration, preprocessing, privileged input | p. 2 (II. DREAMWAQ), p. 2 (II. DREAMWAQ) |
| Output/decision | joint target, torque, footstep 또는 locomotion action | action frame, controller and termination | p. 3 (II. DREAMWAQ), p. 3 (II. DREAMWAQ) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 3: Learning curves of different algorithms. The results shown are obtained from ten different random seeds. The curves and shaded regions indicate the ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| We measured absolute tracking error (ATE) as the performance metric and constructed a | definition/direction/unit from same section | p. 4 (III. EXPERIMENTS) |
| 4: Command tracking error represented as a boxplot. ve x and ve y are forward and lateral velocity tracking errors, respectively, measured in m/s. ... | definition/direction/unit from same section | p. 5 (III. EXPERIMENTS) |
| Long-Distance Walk We deployed the robot on two challenging outdoor courses to demonstrate the robustness of DreamWaQ. | definition/direction/unit from same section | p. 5 (III. EXPERIMENTS) |
| To the best of our knowledge, this is the first time a Unitree A1, which is significantly smaller that an ANYmal robot, has been ... | definition/direction/unit from same section | p. 2 (3) A robustness and durability evaluation of the learned) |
| Fig. 7: The outdoor trajectory for testing the performance of the DreamWaQ policy was recorded using an RTK-GPS mounted on the robot. Course A ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Fig. 1: Overview of DreamWaQ. By learning a locomotion policy in a simulation, the robot can walk through challenging terrains such as stairs with ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared Methods For a comparative evaluation, we compared the following algorithms with access to proprioceptions only: 1) Baseline [12]: The policy was trained without ... | comparison identity and matched condition | p. 4 (III. EXPERIMENTS) |
| 4, indicating that DreamWaQ consistently outperforms the baselines. | comparison identity and matched condition | p. 5 (III. EXPERIMENTS) |
| Moreover, despite walking without exteroception, DreamWaQ performs almost as well as the oracle policy that has direct access to the surrounding terrain's height map. | comparison identity and matched condition | p. 4 (III. EXPERIMENTS) |
| Section III presents the experimental setting, results, and an in-depth comparative analysis of the proposed and baseline methods. | comparison identity and matched condition | p. 2 (3) A robustness and durability evaluation of the learned) |
| Algorithm Max. push (m/s) Survival rate (%) Baseline 0.511 ± 0.053 20.51 ± 6.44 AdaptationNet 0.714 ± 0.096 82.37 ± 2.49 EstimatorNet 0.871 ± ... | comparison identity and matched condition | p. 5 (III. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 4) DreamWaQ w/o AdaBoot: The proposed method without adaptive bootstrapping. | component/input/data sensitivity | p. 4 (III. EXPERIMENTS) |
| 3) EstimatorNet [24]: The policy was concurrently trained with an estimator network that explicitly estimates the body state without a context estimation. | component/input/data sensitivity | p. 4 (III. EXPERIMENTS) |
| Moreover, the proposed AdaBoot method also increases robustness without sacrificing the base performance. | component/input/data sensitivity | p. 5 (III. EXPERIMENTS) |
| Owing to the robust and accurate CENet, the robot had no problem in its body velocity estimation and could continue its journey without any ... | component/input/data sensitivity | p. 5 (III. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we proposed a framework called Dream Walking for Quadrupedal Robots (DreamWaQ), that trains a robust locomotion policy for quadrupedal robots with ... | Fig. 5: Estimation error of CENet and EstimatorNet. The superiority of CENet is highlighted when the robot's feet stumbled by stairs. barplot, as shown ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (Figure/Table caption), p. 5 (III. EXPERIMENTS), p. 2 (3) A robustness and durability evaluation of the learned), p. 4 (III. EXPERIMENTS), p. 4 (III. EXPERIMENTS), p. 6 (Figure/Table caption) |
| Primary metric/result | The robust performance was achieved through the interplay between accurate estimation and robust policy learning of DreamWaQ. | numeric claim only at cited anchor | p. 5 (III. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 4 / III. EXPERIMENTS - extractive body cue:** During inference, the policy runs synchronously with the CENet at 50 Hz.
- **p. 4 / III. EXPERIMENTS - extractive body cue:** The desired joint angles were tracked using a PD controller with proportional and derivative gains of Kp = 28 and Kd = 0.7, respectively at ...
- **p. 5 / III. EXPERIMENTS - extractive body cue:** Algorithm Max. push (m/s) Survival rate (%) Baseline 0.511 ± 0.053 20.51 ± 6.44 AdaptationNet 0.714 ± 0.096 82.37 ± 2.49 EstimatorNet 0.871 ± 0.124 ...
- **p. 5 / III. EXPERIMENTS - extractive body cue:** The robot's trajectory was measured using a real-time kinematic (RTK) GPS [39] with a frequency of 10 Hz, mounted on top of the robot.
- **p. 3 / II. DREAMWAQ - extractive body cue:** Reward Equation (ri) Weight (wi) Lin. velocity tracking exp  -4(vcmd xy -vxy)2 1.0 Ang. velocity tracking exp  -4(ωcmd yaw -ωyaw)2 0.5 Linear velocity ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | DreamWaQ's limitation lies in its adaptation mechanism, where it must first hit the obstacles with its legs. | p. 6 (IV. CONCLUSION) |
| body limitation/failure cue | In severe cases, inaccurate estimation can lead to catastrophic failure. | p. 5 (III. EXPERIMENTS) |
| body limitation/failure cue | (a) Foot stumble Foot slip Normal walk Normal walk Normal walk Climb upstairs Go downstairs Irregular foothold Adaptation Recovery (a) (b) Normal walk Fig. | p. 6 (III. EXPERIMENTS) |
| body limitation/failure cue | 6 shows the robot's foot reflex when faced with foot stumbling and slipping. | p. 5 (III. EXPERIMENTS) |
| body limitation/failure cue | Finally, Section IV concludes this work and briefly discusses directions for future work. | p. 2 (3) A robustness and durability evaluation of the learned) |
| body limitation/failure cue | Fig. 2: The architecture of CENet consists of a body velocity estimation model and an auto-encoder model that shares a unified encoder. The shared ... | p. 3 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Each controller was run five times with different random seeds to verify repeatability. | p. 4 (III. EXPERIMENTS) |
| The networks were optimized using the Adam optimizer [37] with a learning rate of 10-3. | p. 4 (III. EXPERIMENTS) |
| Meanwhile, the robot adapts its gait for going upstairs by significantly increasing its footsteps. | p. 5 (III. EXPERIMENTS) |
| We hypothesize that this is made possible by two factors: 1) the forward-backward dynamics learning provides more accurate estimation in all terrains, and 2) ... | p. 5 (III. EXPERIMENTS) |
| The proposed framework was validated in real-world outdoor environments with varying conditions within a single run for a long distance. | p. 1 (Abstract) |
| In recent years, quadrupedal robots have played an important role in various applications, such as industrial inspection and exploration [1]-[6]. | p. 1 (I. INTRODUCTION) |
| 1) Policy Network: The policy, πφ(at/ot, vt, zt) is a neural network parameterized by φ that infers an action at, given a proprioceptive observation ... | p. 2 (II. DREAMWAQ) |
| The encoder network encodes oH t into vt and zt. | p. 3 (II. DREAMWAQ) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / IV. CONCLUSION - extractive body cue:** DreamWaQ's limitation lies in its adaptation mechanism, where it must first hit the obstacles with its legs.
- **p. 5 / III. EXPERIMENTS - extractive body cue:** In severe cases, inaccurate estimation can lead to catastrophic failure.
- **p. 6 / III. EXPERIMENTS - extractive body cue:** (a) Foot stumble Foot slip Normal walk Normal walk Normal walk Climb upstairs Go downstairs Irregular foothold Adaptation Recovery (a) (b) Normal walk Fig.
- **p. 5 / III. EXPERIMENTS - extractive body cue:** 6 shows the robot's foot reflex when faced with foot stumbling and slipping.
- **p. 2 / 3) A robustness and durability evaluation of the learned - extractive body cue:** Finally, Section IV concludes this work and briefly discusses directions for future work.
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: The architecture of CENet consists of a body velocity estimation model and an auto-encoder model that shares a unified encoder. The shared encoder ...

- **Evidence anchors reviewed:** datasets p. 4 (III. EXPERIMENTS), p. 5 (III. EXPERIMENTS), p. 5 (III. EXPERIMENTS), p. 2 (3) A robustness and durability evaluation of the learned), p. 4 (III. EXPERIMENTS), p. 2 (3) A robustness and durability evaluation of the learned), metrics p. 4 (Figure/Table caption), p. 4 (III. EXPERIMENTS), p. 5 (III. EXPERIMENTS), p. 5 (III. EXPERIMENTS), p. 2 (3) A robustness and durability evaluation of the learned), p. 6 (Figure/Table caption), baselines p. 4 (III. EXPERIMENTS), p. 5 (III. EXPERIMENTS), p. 4 (III. EXPERIMENTS), p. 2 (3) A robustness and durability evaluation of the learned), p. 5 (III. EXPERIMENTS), results p. 5 (Figure/Table caption), p. 5 (III. EXPERIMENTS), p. 2 (3) A robustness and durability evaluation of the learned), p. 4 (III. EXPERIMENTS), p. 4 (III. EXPERIMENTS), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
