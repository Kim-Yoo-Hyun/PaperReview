# Evaluation - HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p070.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p070.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (A. Humanoid Whole-body Control), p. 10 (C. Teleoperation System), p. 7 (C. Hardware System Design), p. 7 (A. Humanoid Whole-body Control), p. 8 (A. Humanoid Whole-body Control), p. 9 (B. Teleoperation Hardware Performance)): In summary, symmetry data augmentation significantly improves training efficiency, while the use of symmetry loss effectively prevents the policy from sacrificing symmetry to complete tasks and also benefits the task ...

## Evaluation Body Digest

- **p. 10 / 20 Bet - extractive body cue:** This migration enables the use of HOMIE to control robots within a variety of simulated environments By leveraging these simulated scenes, the robots can perform ...
- **p. 10 / 20 Bet - extractive body cue:** We capture RGB images, robot states q, the upper body commands quypers and the locomotion commands Cy at 10Hz, and collect 50 episodes per task.
- **p. 8 / A. Humanoid Whole-body Control - extractive body cue:** Compared to the training setting of Unitree Gl. we only ‘change the range of height tracking and some robot-specific distance values, without any other changes ...
- **p. 8 / A. Humanoid Whole-body Control - extractive body cue:** This indirectly supports the idea that a symmetric policy benefits the robot's locomotion tasks [50].
- **p. 9 / C. Teleoperation System - extractive body cue:** 11: Comparison of completion time to perform desktop tasks between our hardware system and Open'Television [7]
- **p. 9 / C. Teleoperation System - extractive body cue:** 1 (b) highlights the extensibility of our system, enabling two operators to control separate robots and collaboratively perform tasks, such as transferring. apples.
- **p. 7 / C. Hardware System Design - extractive body cue:** In our system, we control the humanoid robot's locomotion through linear velocity, yaw velocity, and height adjustment. ‘These ‘commands allow the robot to fully demonstrate ...
- **p. 7 / A. Humanoid Whole-body Control - extractive body cue:** III-B, For each setting, we use three random seeds to train policies for Unitree G1 and ‘evaluate them in 1000 environments over a 20-second evaluation ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| A. Humanoid Whole-body Control | EMPIRICAL / REAL-ROBOT OR HARDWARE | In summary, symmetry data augmentation significantly improves training efficiency, while the use of symmetry loss effectively prevents the policy from sacrificing symmetry to complete ... | p. 8 (A. Humanoid Whole-body Control) |
| C. Teleoperation System | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results, shown in Fig. /, indicate that our system achieves task completion times nearly half of those of the VRbased method. | p. 10 (C. Teleoperation System) |
| C. Hardware System Design | EMPIRICAL / REAL-ROBOT OR HARDWARE | To achieve this, we use three small pedals to control these commands. | p. 7 (C. Hardware System Design) |
| A. Humanoid Whole-body Control | EMPIRICAL / REAL-ROBOT OR HARDWARE | All three configurations achieve similar final living times, but ours and w/o cur converge more quickly. | p. 7 (A. Humanoid Whole-body Control) |
| A. Humanoid Whole-body Control | EMPIRICAL / REAL-ROBOT OR HARDWARE | Both nsym and none show a tendency for improvement, but their training speed is much slower. | p. 8 (A. Humanoid Whole-body Control) |

## Dataset / Benchmark Role

- **p. 10 / 20 Bet - extractive body cue:** This migration enables the use of HOMIE to control robots within a variety of simulated environments By leveraging these simulated scenes, the robots can perform ...
- **p. 10 / 20 Bet - extractive body cue:** We capture RGB images, robot states q, the upper body commands quypers and the locomotion commands Cy at 10Hz, and collect 50 episodes per task.
- **p. 8 / A. Humanoid Whole-body Control - extractive body cue:** Compared to the training setting of Unitree Gl. we only ‘change the range of height tracking and some robot-specific distance values, without any other changes ...
- **p. 8 / A. Humanoid Whole-body Control - extractive body cue:** This indirectly supports the idea that a symmetric policy benefits the robot's locomotion tasks [50].
- **p. 9 / C. Teleoperation System - extractive body cue:** 11: Comparison of completion time to perform desktop tasks between our hardware system and Open'Television [7]
- **p. 9 / C. Teleoperation System - extractive body cue:** 1 (b) highlights the extensibility of our system, enabling two operators to control separate robots and collaboratively perform tasks, such as transferring. apples.
- **p. 7 / C. Hardware System Design - extractive body cue:** In our system, we control the humanoid robot's locomotion through linear velocity, yaw velocity, and height adjustment. ‘These ‘commands allow the robot to fully demonstrate ...
- **p. 7 / A. Humanoid Whole-body Control - extractive body cue:** III-B, For each setting, we use three random seeds to train policies for Unitree G1 and ‘evaluate them in 1000 environments over a 20-second evaluation ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: HOMIE empowers the humanoid robot to execute various loco-manipulation tasks in the real world. (2): Squatting to grasp a tape and placing it ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: System Overview. (2): how an operator uses the exoskeleton-based hardware system to control humanoid robots in the
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: RL training framework of HOMIE,
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Different robots are trained to walk and squat with continuous changing upper-body poses in Isaac Gym.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Upper-body Exoskeleton. (a): The model architecture and physi
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6: Pedal command control. The three small pedals re- spectively control (0, tWmazls Hminy Hmar} and (0, -EVinaz} The left-side switching button is used ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Ablation experiments of our RL training framework. Each row from top to bottom represents the ablation study for upper-body curriculum, height tracking reward, ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: Key parameters of Unitree Gi (left) and Fourier GR-I (right). Hand weight ratio = total weight / hands weight.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This migration enables the use of HOMIE to control robots within a variety of simulated environments By leveraging these simulated scenes, the robots can ... | embodiment, simulator version and control stack | p. 10 (20 Bet), p. 10 (20 Bet) |
| Task/environment | We capture RGB images, robot states q, the upper body commands quypers and the locomotion commands Cy at 10Hz, and collect 50 episodes per ... | reset, timeout, object/scene variation | p. 10 (20 Bet), p. 8 (A. Humanoid Whole-body Control) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 4 (B. Humanoid Whole-body Control), p. 4 (B. Humanoid Whole-body Control) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 2 (Abstract), p. 5 (C. Hardware System Design) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| These results indicate that just scaling up the height tracking reward in hei may initially lead to faster reduction in height tracking error, but ... | definition/direction/unit from same section | p. 8 (A. Humanoid Whole-body Control) |
| Except for symmetry loss, the performance of ours and w/ aug is similar, However, when considering overall tracking accuracy, ours performs slightly better. | definition/direction/unit from same section | p. 8 (A. Humanoid Whole-body Control) |
| Metries for evaluation are tracking linear velocity error, tracking angular velocity error, tracking height error, symmetry loss and living time. | definition/direction/unit from same section | p. 7 (A. Humanoid Whole-body Control) |
| Each row from top to bottom represents the ablation study for upper-body curriculum, height tracking reward, and symmetry utilization, respectively. | definition/direction/unit from same section | p. 7 (C. Hardware System Design) |
| ‘To demonstrate the efficiency of our teleoperation system, ‘we compare the task completion time between our hardware system and a VR-based method, Open'Television [7], ... | definition/direction/unit from same section | p. 9 (C. Teleoperation System) |
| These results demonstrate that ‘our exoskeleton system enables operators to teleoperate robots more smoothly and efficiently, particularly in tasks requiring high precision and dexterity. | definition/direction/unit from same section | p. 10 (C. Teleoperation System) |
| The elapsed time from initiation to successful transfer completion is recorded as the "completion time," serving as the primary metric for evaluating operator proficiency ... | definition/direction/unit from same section | p. 10 (20 Bet) |
| Fig. 1: HOMIE empowers the humanoid robot to execute various loco-manipulation tasks in the real world. (2): Squatting to grasp a tape and placing ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to the training setting of Unitree Gl. we only ‘change the range of height tracking and some robot-specific distance values, without any other ... | comparison identity and matched condition | p. 8 (A. Humanoid Whole-body Control) |
| Thus, our curriculum approach leads to better performance compared to rand, Although w/o cur does not use a curriculum, allowing a; to continuously sample ... | comparison identity and matched condition | p. 7 (A. Humanoid Whole-body Control) |
| 7, reveal that ours outperforms both w/o eur and rand in linear velocity tracking, angular velocity tracking, and height error, with faster convergence and ... | comparison identity and matched condition | p. 7 (A. Humanoid Whole-body Control) |
| However, due to slower training, none exhibits less symmetry breaking compared to w/ aug. | comparison identity and matched condition | p. 8 (A. Humanoid Whole-body Control) |
| 11: Comparison of completion time to perform desktop tasks between our hardware system and Open'Television [7] | comparison identity and matched condition | p. 9 (C. Teleoperation System) |
| 10: Desktop tasks for comparison of completion time. «: Pick & Place; b: Scan Barcode; c: Hand Over; d: Open Oven. | comparison identity and matched condition | p. 9 (C. Teleoperation System) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| environments, where components unrelated to the ablation are kept unchanged, and only relevant parts are modified for training, Detailed parameters used in training and ... | component/input/data sensitivity | p. 7 (A. Humanoid Whole-body Control) |
| 7: Ablation experiments of our RL training framework. | component/input/data sensitivity | p. 7 (C. Hardware System Design) |
| Compared to the training setting of Unitree Gl. we only ‘change the range of height tracking and some robot-specific distance values, without any other ... | component/input/data sensitivity | p. 8 (A. Humanoid Whole-body Control) |
| Symmetry Utilization, We introduce three algorithmic variants for comparison with ours in terms of symmetry ut tion: w/ aug, which uses only symmetrical data ... | component/input/data sensitivity | p. 8 (A. Humanoid Whole-body Control) |
| Therefore, our approach achieves a very high output frequency without requiring GPU and System on Chip (SoC) intensive hardware. | component/input/data sensitivity | p. 9 (B. Teleoperation Hardware Performance) |
| In all these tasks, each robot is controlled by a single operator, and the communication between the robot and operator is facilitated via Wi-Fi, ... | component/input/data sensitivity | p. 9 (C. Teleoperation System) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce the training settings and three key techniques of our framework in this section | In summary, symmetry data augmentation significantly improves training efficiency, while the use of symmetry loss effectively prevents the policy from sacrificing symmetry to complete ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (A. Humanoid Whole-body Control), p. 10 (C. Teleoperation System), p. 7 (C. Hardware System Design), p. 7 (A. Humanoid Whole-body Control), p. 8 (A. Humanoid Whole-body Control), p. 9 (B. Teleoperation Hardware Performance) |
| Primary metric/result | The results, shown in Fig. /, indicate that our system achieves task completion times nearly half of those of the VRbased method. | numeric claim only at cited anchor | p. 10 (C. Teleoperation System) |

- Numeric sentences retained from the body:
- **p. 8 / A. Humanoid Whole-body Control - extractive body cue:** For height error, our method ‘converges faster than both w/o knee and hei, even though hei initially performs better (at 400 steps).
- **p. 9 / C. Teleoperation System - extractive body cue:** Since our system requires only 128 bytes(32-bit floats) per data packet, the measured communication latency under normal network conditions is 16 ms - a result ...
- **p. 10 / 20 Bet - extractive body cue:** We capture RGB images, robot states q, the upper body commands quypers and the locomotion commands Cy at 10Hz, and collect 50 episodes per task.
- **p. 2 / Abstract - extractive body cue:** This allows us to directly set the upper-body joint positions based on the exoskeleton readings, bypassing the need for IK and resulting in faster and ...
- **p. 8 / A. Humanoid Whole-body Control - extractive body cue:** For height error, our method ‘converges faster than both w/o knee and hei, even though hei initially performs better (at 400 steps).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Thus, our curriculum approach leads to better performance compared to rand, Although w/o cur does not use a curriculum, allowing a; to continuously sample ... | p. 7 (A. Humanoid Whole-body Control) |
| body limitation/failure cue | We design two additional algorithms w/o knee, which does not USE rinee described in Eq. | p. 8 (A. Humanoid Whole-body Control) |
| body limitation/failure cue | Infact, het ultimately does not achieve faster ‘convergence in height tracking compared to ours. | p. 8 (A. Humanoid Whole-body Control) |
| body limitation/failure cue | Fig. 1: HOMIE empowers the humanoid robot to execute various loco-manipulation tasks in the real world. (2): Squatting to grasp a tape and placing ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | These tasks showcase the robustness of our loco-manipulation policy and HOMIE 's ability 10 teleopeate humanoids perform a wide range of complex tasks in ... | p. 9 (C. Teleoperation System) |
| body limitation/failure cue | I (<), the robot is controlled to push a 60 kg person sitting in a chair, who weighs roughly twice as much as the ... | p. 9 (C. Teleoperation System) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The acquisition frequency represents the update signal frequency measured between the hardware components of the teleoperation system and the host computer via a wired ... | p. 8 (B. Teleoperation Hardware Performance) |
| Therefore, our approach achieves a very high output frequency without requiring GPU and System on Chip (SoC) intensive hardware. | p. 9 (B. Teleoperation Hardware Performance) |
| The system is fully system that combines a reinforcement learning poliey for body open-source, demos and code can be found in our websit control ... | p. 1 (Abstract) |
| to different robots, ‘The total cost of the hardware system is just $0.5k, significantly more affordable than motion capture (MoCap) devices [13] | p. 2 (Abstract) |
| 2) ‘The first successful implementation of teleoperationcompatible humanoid loco-manipulation, including dynamic squatting, without relying on motion prior data, | p. 2 (1) A novel humanoid teleoperation cockpit that combines) |
| Some research calculates the endeffector pose of the exoskeleton using Forward Kinematics (FK) and then apply IK to determine the robot's joint positions, while ... | p. 3 (A. Teleoperation Systems) |
| After the neural network computes ay based on Ort, We Use | p. 4 (B. Humanoid Whole-body Control) |
| 2, HOMIE consists of low-level policy Toco and an exoskeleton-based hardware system. | p. 4 (A. System Overview) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / A. Humanoid Whole-body Control - extractive body cue:** Thus, our curriculum approach leads to better performance compared to rand, Although w/o cur does not use a curriculum, allowing a; to continuously sample from
- **p. 8 / A. Humanoid Whole-body Control - extractive body cue:** We design two additional algorithms w/o knee, which does not USE rinee described in Eq.
- **p. 8 / A. Humanoid Whole-body Control - extractive body cue:** Infact, het ultimately does not achieve faster ‘convergence in height tracking compared to ours.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: HOMIE empowers the humanoid robot to execute various loco-manipulation tasks in the real world. (2): Squatting to grasp a tape and placing it ...
- **p. 9 / C. Teleoperation System - extractive body cue:** These tasks showcase the robustness of our loco-manipulation policy and HOMIE 's ability 10 teleopeate humanoids perform a wide range of complex tasks in various ...
- **p. 9 / C. Teleoperation System - extractive body cue:** I (<), the robot is controlled to push a 60 kg person sitting in a chair, who weighs roughly twice as much as the robot, ...

- **Evidence anchors reviewed:** datasets p. 10 (20 Bet), p. 10 (20 Bet), p. 8 (A. Humanoid Whole-body Control), p. 8 (A. Humanoid Whole-body Control), p. 9 (C. Teleoperation System), p. 9 (C. Teleoperation System), metrics p. 8 (A. Humanoid Whole-body Control), p. 8 (A. Humanoid Whole-body Control), p. 7 (A. Humanoid Whole-body Control), p. 7 (C. Hardware System Design), p. 9 (C. Teleoperation System), p. 10 (C. Teleoperation System), baselines p. 8 (A. Humanoid Whole-body Control), p. 7 (A. Humanoid Whole-body Control), p. 7 (A. Humanoid Whole-body Control), p. 8 (A. Humanoid Whole-body Control), p. 9 (C. Teleoperation System), p. 9 (C. Teleoperation System), results p. 8 (A. Humanoid Whole-body Control), p. 10 (C. Teleoperation System), p. 7 (C. Hardware System Design), p. 7 (A. Humanoid Whole-body Control), p. 8 (A. Humanoid Whole-body Control), p. 9 (B. Teleoperation Hardware Performance).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (21 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** These results indicate that just scaling up the height tracking reward in hei may initially lead to faster reduction in height tracking error, but it negatively affects the feedback from ... (p. 8, A. Humanoid Whole-body Control).
- **Metric evidence:** Except for symmetry loss, the performance of ours and w/ aug is similar, However, when considering overall tracking accuracy, ours performs slightly better. (p. 8, A. Humanoid Whole-body Control).
- **Baseline/ablation evidence:** Compared to the training setting of Unitree Gl. we only ‘change the range of height tracking and some robot-specific distance values, without any other changes in reward scales or training ... (p. 8, A. Humanoid Whole-body Control).
- **Failure/negative evidence:** However, due to limitations in the accuracy, inference speed, and difficulty in handling occlusions of pose estimation, such approaches cannot guarantee rapid and accurate pose acquisition. (p. 2, A. Teleoperation Systems).
