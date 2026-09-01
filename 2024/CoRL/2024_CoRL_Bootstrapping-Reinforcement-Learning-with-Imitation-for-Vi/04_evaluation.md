# Evaluation - Bootstrapping Reinforcement Learning with Imitation for Vision-Based Agile Flight

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=bt0PX0e4rE; PDF retrieval source: https://arxiv.org/pdf/2403.12203. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 15 (A.8 Unobservable States Illustration), p. 13 (A.6 Performance w/ Diff. History Length), p. 7 (3 Methodology), p. 13 (A.6 Performance w/ Diff. History Length), p. 14 (Figure/Table caption), p. 15 (A.8 Unobservable States Illustration)): The quantitative results, shown in 6, clearly indicate that our approach greatly improves policy performance, achieving lap times within a difference of 0.05s to that in [9], where they outperformed ...

## Evaluation Body Digest

- **p. 8 / 3 Methodology - extractive PDF cue:** Realworld Experiments To demonstrate policy improvements, we validated our policy in real-world scenarios using Hardware-in-the-Loop (HIL) simulations, aided by a VICON motion capture system for ...
- **p. 8 / 3 Methodology - extractive PDF cue:** For future work, we aim to integrate a customized vision encoder that leverages data from diverse simulation settings, modalities, and extensive real-world environments.
- **p. 12 / A.2 Reward Formulations for RL Trainings - extractive PDF cue:** 4 in both simulation and real-world experiments, aiming to achieve optimal and smooth performance for the state-based policy.
- **p. 5 / 3 Methodology - extractive PDF cue:** Further details on training configurations and our hardware setup are available in the Appendix.
- **p. 5 / 3 Methodology - extractive PDF cue:** This approach involves augmenting the critic function inputs with privileged information, such as the robot state s.
- **p. 6 / 3 Methodology - extractive PDF cue:** Hence, to benchmark the learned policies' performance, we conduct a detailed analysis of our approach to the existing baselines using various time horizons for the ...
- **p. 6 / 3 Methodology - extractive PDF cue:** To simulate real-world scenarios, we include domain randomization such as gate scales, pixel position noise (10 pixels in both (u, v) in a 1280 × ...
- **p. 12 / A.2 Reward Formulations for RL Trainings - extractive PDF cue:** The reward components are formulated as follows: rprog t = λ1(dGate(t -1) -dGate(t)), rperc t = λ2 exp(λ3 · δ4 cam), ract t = -λ3∥at ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| A.8 Unobservable States Illustration | EMPIRICAL / REAL-ROBOT OR HARDWARE | The quantitative results, shown in 6, clearly indicate that our approach greatly improves policy performance, achieving lap times within a difference of 0.05s to ... | p. 15 (A.8 Unobservable States Illustration) |
| A.6 Performance w/ Diff. History Length | EMPIRICAL / REAL-ROBOT OR HARDWARE | More importantly, in all of these cases, our approach achieves both better performance and success rate. | p. 13 (A.6 Performance w/ Diff. History Length) |
| 3 Methodology | EMPIRICAL / REAL-ROBOT OR HARDWARE | Firstly, it is noteworthy that the direct RL from corners or pixels achieves a 0% success rate in all three tracks. | p. 7 (3 Methodology) |
| A.6 Performance w/ Diff. History Length | EMPIRICAL / REAL-ROBOT OR HARDWARE | It is evident that by incorporating more historical information, the student could achieve a higher success rate. | p. 13 (A.6 Performance w/ Diff. History Length) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 5: Ablation study on history length of the policy observations using raw pixels. We could clearly find out by using more history observations, ... | p. 14 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / 3 Methodology - extractive PDF cue:** Realworld Experiments To demonstrate policy improvements, we validated our policy in real-world scenarios using Hardware-in-the-Loop (HIL) simulations, aided by a VICON motion capture system for ...
- **p. 8 / 3 Methodology - extractive PDF cue:** For future work, we aim to integrate a customized vision encoder that leverages data from diverse simulation settings, modalities, and extensive real-world environments.
- **p. 12 / A.2 Reward Formulations for RL Trainings - extractive PDF cue:** 4 in both simulation and real-world experiments, aiming to achieve optimal and smooth performance for the state-based policy.
- **p. 5 / 3 Methodology - extractive PDF cue:** Further details on training configurations and our hardware setup are available in the Appendix.
- **p. 5 / 3 Methodology - extractive PDF cue:** This approach involves augmenting the critic function inputs with privileged information, such as the robot state s.
- **p. 6 / 3 Methodology - extractive PDF cue:** Hence, to benchmark the learned policies' performance, we conduct a detailed analysis of our approach to the existing baselines using various time horizons for the ...
- **p. 6 / 3 Methodology - extractive PDF cue:** To simulate real-world scenarios, we include domain randomization such as gate scales, pixel position noise (10 pixels in both (u, v) in a 1280 × ...
- **p. 12 / A.2 Reward Formulations for RL Trainings - extractive PDF cue:** The reward components are formulated as follows: rprog t = λ1(dGate(t -1) -dGate(t)), rperc t = λ2 exp(λ3 · δ4 cam), ract t = -λ3∥at ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Long exposure image of real-world flights shows a blue trajectory for our approach and a red one for the imitation policy. Training on ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 4. The drone perceives the environment solely through a single RGB camera, and the learned policy network utilizes egocentric vision input op to output ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2: We demonstrate visuomotor policy learning in three different stages. In stage I, we train a state-based teacher policy using RL. In stage II, ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3: Visualization of difference between the symmetric and asymmet- ric actor-critic learning setup. To acquire an imitation learning policy, the most common methods are ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4: Visualization of the drone racing tracks used for the experiments, each characterized by varying levels of complexity. All the tracks maintain a consistent ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1: Policy performance evaluation averaged by 6 different history lengths using both implicitly learned representations, specifically a common ResNet50 [42] for RGB images, and ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5: Left: Reward comparison between our approach and the other RL configurations. Ours is the only approach that is able to learn to perform ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2: Evalutation results on Perceptual and Po- sitional disturbance. Disturbance Prob. [%] SR% Error [m] IL Ours IL Ours

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Realworld Experiments To demonstrate policy improvements, we validated our policy in real-world scenarios using Hardware-in-the-Loop (HIL) simulations, aided by a VICON motion capture system ... | embodiment, simulator version and control stack | p. 8 (3 Methodology), p. 8 (3 Methodology) |
| Task/environment | For future work, we aim to integrate a customized vision encoder that leverages data from diverse simulation settings, modalities, and extensive real-world environments. | reset, timeout, object/scene variation | p. 8 (3 Methodology), p. 12 (A.2 Reward Formulations for RL Trainings) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 4 (3 Methodology), p. 3 (3 Methodology) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 8 (3 Methodology), p. 4 (3 Methodology) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We use three evaluation metrics: success rate (SR), mean-gate-passing-error (MGE), and lap time (LT). | definition/direction/unit from same section | p. 5 (3 Methodology) |
| More importantly, in all of these cases, our approach achieves both better performance and success rate. | definition/direction/unit from same section | p. 13 (A.6 Performance w/ Diff. History Length) |
| Firstly, it is noteworthy that the direct RL from corners or pixels achieves a 0% success rate in all three tracks. | definition/direction/unit from same section | p. 7 (3 Methodology) |
| It is evident that by incorporating more historical information, the student could achieve a higher success rate. | definition/direction/unit from same section | p. 13 (A.6 Performance w/ Diff. History Length) |
| [%] SR% Error [m] IL Ours IL Ours Perceptual 1 59 100 0.38 0.25 5 33 91 0.55 0.39 Positional 1 84 100 0.32 ... | definition/direction/unit from same section | p. 7 (3 Methodology) |
| 0 1000 2000 3000 4000 Steps (k) 0 100 200 300 400 Average reward Ours Champion Level Policy Figure 9: Return comparison between our ... | definition/direction/unit from same section | p. 15 (A.8 Unobservable States Illustration) |
| Once the policy achieves high-reward action sequences, the policy update rate also increases. | definition/direction/unit from same section | p. 5 (3 Methodology) |
| Our approach consistently achieved faster lap times and smaller gate errors in the real-world setting, confirming the effective real-world transfer of our vision-based quadrotor ... | definition/direction/unit from same section | p. 8 (3 Methodology) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 5: Ablation study on history length of the policy observations using raw pixels. We could clearly find out by using more history observations, ... | comparison identity and matched condition | p. 14 (Figure/Table caption) |
| Across all configurations and racing tracks, our approach consistently exhibits the best performance in all the metrics compared to all baselines, under the same ... | comparison identity and matched condition | p. 7 (3 Methodology) |
| 2, it is clear that our approach outperforms the baseline DAgger approach in terms of robustness to unknown disturbance. | comparison identity and matched condition | p. 8 (3 Methodology) |
| Despite demonstrating superior robustness compared to existing baselines, we believe the perception module in our framework is to improve to handle more out-of-distribution cases. | comparison identity and matched condition | p. 8 (3 Methodology) |
| Notably, our approach consistently outperforms baseline methods across all history lengths ger to imitate the slow policy, after which we apply our approach to ... | comparison identity and matched condition | p. 15 (A.8 Unobservable States Illustration) |
| Figure 5: Left: Reward comparison between our approach and the other RL configurations. Ours is the only approach that is able to learn to ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 5: Left: Reward comparison between our approach and the other RL configurations. Ours is the only approach that is able to learn to ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Table 6: Ablation study on history length of the policy observations using raw pixels. We could clearly find out by using more history observations, ... | component/input/data sensitivity | p. 15 (Figure/Table caption) |
| Figure 1: Long exposure image of real-world flights shows a blue trajectory for our approach and a red one for the imitation policy. Training ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| This limitation arises because the student policy is trained only on the explicit actions of the expert, without understanding the underlying context that the ... | component/input/data sensitivity | p. 6 (3 Methodology) |
| This once again underscores the difficulty of RL exploration in high-dimensional time series without bootstrapping. | component/input/data sensitivity | p. 7 (3 Methodology) |
| Approach Slow IL policy Our Finetuned Policy Champion-level Policy LT [s] SR [%] LT [s] SR [%] LT [s] SR [%] Nominal Simulation 9.53 ... | component/input/data sensitivity | p. 15 (A.8 Unobservable States Illustration) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Contributions By leveraging the complementary advantages of IL and RL, we propose a framework that trains a policy capable of navigating through a sequence ... | The quantitative results, shown in 6, clearly indicate that our approach greatly improves policy performance, achieving lap times within a difference of 0.05s to ... | PDF body cue; verify exact table/figure and matched conditions | p. 15 (A.8 Unobservable States Illustration), p. 13 (A.6 Performance w/ Diff. History Length), p. 7 (3 Methodology), p. 13 (A.6 Performance w/ Diff. History Length), p. 14 (Figure/Table caption), p. 15 (A.8 Unobservable States Illustration) |
| Primary metric/result | More importantly, in all of these cases, our approach achieves both better performance and success rate. | numeric claim only at cited anchor | p. 13 (A.6 Performance w/ Diff. History Length) |

- Numeric sentences retained from the body:
- **p. 6 / 3 Methodology - extractive PDF cue:** All the tracks maintain a consistent size scale, spanning widths from 8 meters to 16 meters.
- **p. 7 / 3 Methodology - extractive PDF cue:** 0 2000 4000 6000 8000 Steps (k) 0 20 40 60 Average reward Ours RL Vanilla Bootstrap 0 20 40 60 80 100 Percentage IL ...
- **p. 7 / 3 Methodology - extractive PDF cue:** [%] SR% Error [m] IL Ours IL Ours Perceptual 1 59 100 0.38 0.25 5 33 91 0.55 0.39 Positional 1 84 100 0.32 0.28 ...
- **p. 8 / 3 Methodology - extractive PDF cue:** 0 -5 5 10 x [m] y [m] v [m/s] -8 -6 -4 -2 0 2 4 6 8 0 2 4 6 8 10 ...
- **p. 12 / A.1 Quadrotor Dynamics for Policy Training - extractive PDF cue:** The quadrotor is assumed to be a 6 degree-of-freedom rigid body of mass m and diagonal moment of inertia matrix J = diag(Jx, Jy, Jz).
- **p. 13 / A.3 Training Configurations - extractive PDF cue:** For imitation learning, we employ a batch size of 512, and convergence typically occurs after collecting 5M data samples over approximately 100 epochs.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | To simulate real-world scenarios, we include domain randomization such as gate scales, pixel position noise (10 pixels in both (u, v) in a 1280 ... | p. 6 (3 Methodology) |
| body limitation/failure cue | To simulate realworld uncertainties, we conducted two experiments: i) random frame blackouts to mimic sensor failures like communication loss, and ii) random positional jumps ... | p. 8 (3 Methodology) |
| body limitation/failure cue | One limitation is that our current setup is tested in the controlled lab settings, it will likely fail in an in-the-wild setup. | p. 8 (3 Methodology) |
| body limitation/failure cue | 4.2 Experiment Results Performance comparison to baseline approaches One inherent limitation of the student-teacher IL framework is to infer reasonable actions from partial information. | p. 6 (3 Methodology) |
| body limitation/failure cue | Reward Name Symbol Value Progress reward λ1 0.5 Perception-aware reward λ2 0.025 Command smoothness reward λ3 2e-4 Body rate penalty λ4 5e-4 Gate passing ... | p. 13 (A.3 Training Configurations) |
| body limitation/failure cue | We believe this approach is easily generalizable to other platforms as it does not require task-specific information. | p. 5 (3 Methodology) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For imitation learning, we employ a batch size of 512, and convergence typically occurs after collecting 5M data samples over approximately 100 epochs. | p. 13 (A.3 Training Configurations) |
| We incorporate a linear decay in the learning rate, starting at 1e-3 and decreasing to 1e-5 at 50 epochs, remaining unchanged for the remainder ... | p. 13 (A.3 Training Configurations) |
| In imitation learning, a 3-layer Temporal Convolutional Network (TCN) is utilized to encode the 32 timestamps of perceptual inputs. | p. 12 (A.3 Training Configurations) |
| In our experiments, we employ identical hyperparameters for both state-based teacher training and vision-based RL fine-tuning to ensure a fair comparison. | p. 12 (A.2 Reward Formulations for RL Trainings) |
| In our approach, the exploration and learning rates should dynamically depend on the agents' performance rather than being solely determined by the number of ... | p. 5 (3 Methodology) |
| By linking the learning rates and the clip range to the policy rollout performance, we eliminate the need for heuristic tuning of learning rates ... | p. 5 (3 Methodology) |
| We use a Temporal Convolutional Network (TCN) [40] to encode the series of vision embeddings from I or corners C. | p. 4 (3 Methodology) |
| The vision-based student policy takes a sequence (history length H timesteps) of perceptual observations [ot-H+1, . . . , ot] as input. | p. 4 (3 Methodology) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 3 Methodology - extractive PDF cue:** To simulate real-world scenarios, we include domain randomization such as gate scales, pixel position noise (10 pixels in both (u, v) in a 1280 × ...
- **p. 8 / 3 Methodology - extractive PDF cue:** To simulate realworld uncertainties, we conducted two experiments: i) random frame blackouts to mimic sensor failures like communication loss, and ii) random positional jumps during ...
- **p. 8 / 3 Methodology - extractive PDF cue:** One limitation is that our current setup is tested in the controlled lab settings, it will likely fail in an in-the-wild setup.
- **p. 6 / 3 Methodology - extractive PDF cue:** 4.2 Experiment Results Performance comparison to baseline approaches One inherent limitation of the student-teacher IL framework is to infer reasonable actions from partial information.
- **p. 13 / A.3 Training Configurations - extractive PDF cue:** Reward Name Symbol Value Progress reward λ1 0.5 Perception-aware reward λ2 0.025 Command smoothness reward λ3 2e-4 Body rate penalty λ4 5e-4 Gate passing reward ...
- **p. 5 / 3 Methodology - extractive PDF cue:** We believe this approach is easily generalizable to other platforms as it does not require task-specific information.

- **PDF anchors reviewed:** datasets p. 8 (3 Methodology), p. 8 (3 Methodology), p. 12 (A.2 Reward Formulations for RL Trainings), p. 5 (3 Methodology), p. 5 (3 Methodology), p. 6 (3 Methodology), metrics p. 5 (3 Methodology), p. 13 (A.6 Performance w/ Diff. History Length), p. 7 (3 Methodology), p. 13 (A.6 Performance w/ Diff. History Length), p. 7 (3 Methodology), p. 15 (A.8 Unobservable States Illustration), baselines p. 14 (Figure/Table caption), p. 7 (3 Methodology), p. 8 (3 Methodology), p. 8 (3 Methodology), p. 15 (A.8 Unobservable States Illustration), p. 7 (Figure/Table caption), results p. 15 (A.8 Unobservable States Illustration), p. 13 (A.6 Performance w/ Diff. History Length), p. 7 (3 Methodology), p. 13 (A.6 Performance w/ Diff. History Length), p. 14 (Figure/Table caption), p. 15 (A.8 Unobservable States Illustration).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
