# Evaluation - Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2501.10100; PDF retrieval source: https://arxiv.org/pdf/2501.10100. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 8 (Figure/Table caption), p. 7 (4 Experiments), p. 9 (4 Experiments)): A.4.1 reveals that, while extending both M and N improves accuracy, practical considerations of computational cost necessitate careful tuning of these hyperparameters to achieve optimal performance.

## Evaluation Body Digest

- **p. 6 / 4 Experiments - extractive body cue:** The experiments are designed to assess the accuracy and robustness of RWM, evaluate its architectural and training design choices, and demonstrate its effectiveness across diverse ...
- **p. 9 / 4 Experiments - extractive body cue:** Current training in simulation avoids potential hardware damage, but incorporating safety constraints and robust uncertainty estimates will be critical for deploying RWM and MBPO-PPO in ...
- **p. 9 / 4 Experiments - extractive body cue:** These results underline the effectiveness of RWM and MBPO-PPO in enabling robust and scalable policy deployment for real-world robotic systems.
- **p. 6 / 4 Experiments - extractive body cue:** We then compare various network architectures and the error induced across diverse robotic environments and tasks to demonstrate the generality of RWM.
- **p. 8 / 4 Experiments - extractive body cue:** Reach-UR10 Reach-Franka Lift-Cube-Franka Open-Drawer-Franka Repose-Cube-Allegro Velocity-Unitree-A1 Velocity-Unitree-Go1 Velocity-Unitree-Go2 Velocity-Anymal-B Velocity-Anymal-C Velocity-Anymal-D Velocity-Spot Velocity-Cassie Velocity-H ...
- **p. 7 / 4 Experiments - extractive body cue:** The performance gap between RWM-AR and the baselines is especially pronounced in complex and dynamic tasks, such as velocity tracking for legged robots, where accurate ...
- **p. 7 / 4 Experiments - extractive body cue:** 4.3 Generality across Robotic Environments To assess the generality and robustness of RWM across a diverse range of robotic environments, we compare its performance with ...
- **p. 8 / 4 Experiments - extractive body cue:** These results demonstrate that RWM, when combined with autoregressive training, achieves robust and generalizable performance across diverse robotic tasks.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** physics simulation의 robot/environment model.
- **Input boundary:** simulated state, geometry, contact와 control input.
- **Output/decision under evaluation:** simulation step, trajectory 또는 environment query.
- **Primary target:** physical plausibility, speed, reproducibility와 task utility.
- **Detected evaluation headings:** 4 Experiments (p. 6); A.4 Additional Experiments and Discussions (p. 18).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | A.4.1 reveals that, while extending both M and N improves accuracy, practical considerations of computational cost necessitate careful tuning of these hyperparameters to achieve ... | p. 6 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | These results demonstrate that RWM, when combined with autoregressive training, achieves robust and generalizable performance across diverse robotic tasks. | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The comparison also reveals that RWM-AR significantly outperforms its teacherforcing counterpart (RWM-TF), underscoring the importance of autoregressive training in mitigating compounding prediction errors over ... | p. 7 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4: Autoregressive trajectory prediction errors across diverse robotic environments and network architectures. RWM trained with autoregressive training (RWM-AR) consistently outperforms baseline methods, including ... | p. 8 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 3.2 by including both RWM trained with teacher-forcing (RWM-TF) and autoregressive training (RWM-AR), demonstrating the significant performance gains achieved by the latter. | p. 7 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 6 / 4 Experiments - extractive body cue:** The experiments are designed to assess the accuracy and robustness of RWM, evaluate its architectural and training design choices, and demonstrate its effectiveness across diverse ...
- **p. 9 / 4 Experiments - extractive body cue:** Current training in simulation avoids potential hardware damage, but incorporating safety constraints and robust uncertainty estimates will be critical for deploying RWM and MBPO-PPO in ...
- **p. 9 / 4 Experiments - extractive body cue:** These results underline the effectiveness of RWM and MBPO-PPO in enabling robust and scalable policy deployment for real-world robotic systems.
- **p. 6 / 4 Experiments - extractive body cue:** We then compare various network architectures and the error induced across diverse robotic environments and tasks to demonstrate the generality of RWM.
- **p. 8 / 4 Experiments - extractive body cue:** Reach-UR10 Reach-Franka Lift-Cube-Franka Open-Drawer-Franka Repose-Cube-Allegro Velocity-Unitree-A1 Velocity-Unitree-Go1 Velocity-Unitree-Go2 Velocity-Anymal-B Velocity-Anymal-C Velocity-Anymal-D Velocity-Spot Velocity-Cassie Velocity-H ...
- **p. 7 / 4 Experiments - extractive body cue:** The performance gap between RWM-AR and the baselines is especially pronounced in complex and dynamic tasks, such as velocity tracking for legged robots, where accurate ...
- **p. 7 / 4 Experiments - extractive body cue:** 4.3 Generality across Robotic Environments To assess the generality and robustness of RWM across a diverse range of robotic environments, we compare its performance with ...
- **p. 8 / 4 Experiments - extractive body cue:** These results demonstrate that RWM, when combined with autoregressive training, achieves robust and generalizable performance across diverse robotic tasks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Autoregressive imagination, ground-truth simulation, and real-world deployment of RWM. For each environment, the top row showcases the RWM autoregressively predicting future trajectories in ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: Comparison of training paradigms for world models with an example of a history horizon H = 3. (a) Autoregressive training operates with an ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: (Left) Solid lines represent ground truth trajectories, while dashed lines denote predicted state evolution. Predictions commence at t = 32 using historical observations, ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Autoregressive trajectory prediction errors across diverse robotic environments and network architectures. RWM trained with autoregressive training (RWM-AR) consistently outperforms baseline methods, including MLP, ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Model error and policy mean reward for the ANYmal D (left) and Unitree G1 (right) velocity tracking task with MBPO-PPO. The policy is ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 1: Comparison with model-free method

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The experiments are designed to assess the accuracy and robustness of RWM, evaluate its architectural and training design choices, and demonstrate its effectiveness across ... | embodiment, simulator version and control stack | p. 6 (4 Experiments), p. 9 (4 Experiments) |
| Task/environment | Current training in simulation avoids potential hardware damage, but incorporating safety constraints and robust uncertainty estimates will be critical for deploying RWM and MBPO-PPO ... | reset, timeout, object/scene variation | p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Observation/sensor | simulated state, geometry, contact와 control input | calibration, preprocessing, privileged input | p. 4 (3 Approach), p. 4 (3 Approach) |
| Output/decision | simulation step, trajectory 또는 environment query | action frame, controller and termination | p. 5 (3 Approach), p. 6 (3 Approach) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 0 1000 2000 Training Iterations 0 10 20 30 40 50 e SHAC Dreamer MBPO-PPO 0 1000 2000 Training Iterations 30 20 10 0 ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Figure 5: Model error and policy mean reward for the ANYmal D (left) and Unitree G1 (right) velocity tracking task with MBPO-PPO. The policy ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| The experiments are designed to assess the accuracy and robustness of RWM, evaluate its architectural and training design choices, and demonstrate its effectiveness across ... | definition/direction/unit from same section | p. 6 (4 Experiments) |
| We then compare various network architectures and the error induced across diverse robotic environments and tasks to demonstrate the generality of RWM. | definition/direction/unit from same section | p. 6 (4 Experiments) |
| In contrast, RWM demonstrates superior stability, maintaining lower prediction errors even under high noise levels. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Grey curves represent the MLP baseline, which exhibits significantly higher error accumulation and reduced robustness to noise. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Dreamer demonstrates partial convergence, achieving higher rewards compared to SHAC but significantly lagging behind MBPO-PPO. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| As a result, Dreamer encounters moderate compounding errors during policy learning, which hinder its convergence to optimal behaviors. | definition/direction/unit from same section | p. 9 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 4: Autoregressive trajectory prediction errors across diverse robotic environments and network architectures. RWM trained with autoregressive training (RWM-AR) consistently outperforms baseline methods, including ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| The comparison also reveals that RWM-AR significantly outperforms its teacherforcing counterpart (RWM-TF), underscoring the importance of autoregressive training in mitigating compounding prediction errors over ... | comparison identity and matched condition | p. 7 (4 Experiments) |
| The results indicate a clear advantage of RWM over the MLP baseline across all noise levels. | comparison identity and matched condition | p. 7 (4 Experiments) |
| Note that the baselines are trained using teacher forcing as they are traditionally implemented. | comparison identity and matched condition | p. 8 (4 Experiments) |
| Dreamer demonstrates partial convergence, achieving higher rewards compared to SHAC but significantly lagging behind MBPO-PPO. | comparison identity and matched condition | p. 9 (4 Experiments) |
| A comparison of state evolution between the RWM prediction and the ground truth simulation is illustrated in Fig. | comparison identity and matched condition | p. 6 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In addition, the need for additional interaction with the environment to fine-tune the world model highlights areas for further refinement. | component/input/data sensitivity | p. 9 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are summarized as follows: (i) We introduce a novel network architecture and training framework that enables the learning of reliable world models ... | A.4.1 reveals that, while extending both M and N improves accuracy, practical considerations of computational cost necessitate careful tuning of these hyperparameters to achieve ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 8 (Figure/Table caption), p. 7 (4 Experiments), p. 9 (4 Experiments) |
| Primary metric/result | These results demonstrate that RWM, when combined with autoregressive training, achieves robust and generalizable performance across diverse robotic tasks. | numeric claim only at cited anchor | p. 8 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 6 / 4 Experiments - extractive body cue:** The control frequency of the robot is at 50 Hz.
- **p. 6 / 4 Experiments - extractive body cue:** The model is trained with history horizon M = 32 and forecast horizon N = 8.
- **p. 5 / 3 Approach - extractive body cue:** (a) Autoregressive training operates with an example of a forecast horizon N = 2, leveraging historical data and its own predictions for long-horizon robustness.
- **p. 5 / 3 Approach - extractive body cue:** (b) Teacher-forcing training can be viewed as a special case of autoregressive training with a forecast horizon N = 1, using ground truth observations for ...
- **p. 5 / 3 Approach - extractive body cue:** Specifically, teacher-forcing can be viewed as a special case of autoregressive training with forecast horizon N = 1, which boosts training with higher parallelization.
- **p. 17 / A.3 Training Parameters - extractive body cue:** The learning networks and algorithm are implemented in PyTorch 2.4.0 with CUDA 12.6 and trained on an NVIDIA RTX 4090 GPU.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In contrast, SHAC fails to converge, producing unstable behaviors that degrade both policy and model quality. | p. 9 (4 Experiments) |
| body limitation/failure cue | 5 Limitations The policy learned with RWM and MBPO-PPO surpasses existing MBRL methods in both robustness and generalization. | p. 9 (4 Experiments) |
| body limitation/failure cue | In this work, we present RWM, a robust and scalable framework for learning world models tailored to complex robotic tasks. | p. 10 (6 Conclusion) |
| body limitation/failure cue | The results highlight RWM 's potential to enable adaptive, robust, and high-performing robotic systems, setting a foundation for broader adoption of model-based approaches in ... | p. 10 (6 Conclusion) |
| body limitation/failure cue | Grey curves represent the MLP baseline, which exhibits significantly higher error accumulation and reduced robustness to noise. | p. 7 (4 Experiments) |
| body limitation/failure cue | To assess the robustness of RWM, we analyze its performance under Gaussian noise perturbations applied to both observations and actions. | p. 7 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Training the world model entirely from scratch on such data would lead to severe overfitting and long training times. | p. 19 (A.4.3 Collision Handling and Model Pretraining) |
| To evaluate this aspect, we analyze the autoregressive prediction performance of RWM using trajectories collected from ANYmal D hardware. | p. 6 (4 Experiments) |
| And finally, we learn a policy in RWM with the proposed MBPO-PPO and demonstrate the applicability and robustness of the method on ANYmal D ... | p. 6 (4 Experiments) |
| As forecast steps increase, the relative prediction error of the MLP model grows significantly, diverging more rapidly than RWM. | p. 7 (4 Experiments) |
| (Right) Yellow curves denote RWM at varying noise levels, demonstrating consistent robustness and lower error accumulation across forecast steps. | p. 7 (4 Experiments) |
| The policy is trained using estimated rewards computed from predicted observations by RWM. | p. 8 (4 Experiments) |
| 4.4 Policy Learning and Hardware Transfer Using MBPO-PPO, we train a goal-conditioned velocity tracking policy for ANYmal D and Unitree G1 leveraging RWM. | p. 8 (4 Experiments) |
| Nevertheless, enabling safe and effective online learning directly on hardware remains challenging (see Sec. | p. 9 (4 Experiments) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 4 Experiments - extractive body cue:** In contrast, SHAC fails to converge, producing unstable behaviors that degrade both policy and model quality.
- **p. 9 / 4 Experiments - extractive body cue:** 5 Limitations The policy learned with RWM and MBPO-PPO surpasses existing MBRL methods in both robustness and generalization.
- **p. 10 / 6 Conclusion - extractive body cue:** In this work, we present RWM, a robust and scalable framework for learning world models tailored to complex robotic tasks.
- **p. 10 / 6 Conclusion - extractive body cue:** The results highlight RWM 's potential to enable adaptive, robust, and high-performing robotic systems, setting a foundation for broader adoption of model-based approaches in real-world ...
- **p. 7 / 4 Experiments - extractive body cue:** Grey curves represent the MLP baseline, which exhibits significantly higher error accumulation and reduced robustness to noise.
- **p. 7 / 4 Experiments - extractive body cue:** To assess the robustness of RWM, we analyze its performance under Gaussian noise perturbations applied to both observations and actions.

- **Evidence anchors reviewed:** datasets p. 6 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 6 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), metrics p. 8 (4 Experiments), p. 8 (Figure/Table caption), p. 6 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), baselines p. 8 (Figure/Table caption), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 6 (4 Experiments), results p. 6 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 8 (Figure/Table caption), p. 7 (4 Experiments), p. 9 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
