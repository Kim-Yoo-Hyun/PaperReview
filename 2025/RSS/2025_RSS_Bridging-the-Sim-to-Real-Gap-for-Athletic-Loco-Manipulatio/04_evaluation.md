# Evaluation - Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p125.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p125.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (Figure/Table caption), p. 5 (A. Comparing System Identification Approaches), p. 6 (B. Finetuning Foundational WBC), p. 6 (B. Finetuning Foundational WBC), p. 7 (A. Whole-Body Control), p. 8 (B. Overcoming the sim-to-real gap)): Fig. 4: UAN improves simulator accuracy and real throwing performance. UAN (Ours) achieves lower sim-to-real difference in throw distance as compared to standard baselines, resulting in a better real throw ...

## Evaluation Body Digest

- **p. 6 / B. Finetuning Foundational WBC - extractive PDF cue:** On hardware, the ball was thrown approximately 20m, with the real robot throwing slightly further than in simulation - possibly due to inaccuracies in the ...
- **p. 3 / A. Unsupervised Actuator Net - extractive PDF cue:** 4) Task Design: For each environment at each timestep, wwe uniformly sample a real-world transition, (8,74, $¢1)4. and set the state of the simulator to ...
- **p. 3 / A. Unsupervised Actuator Net - extractive PDF cue:** 2) Data collection: We collect data on real hardware to construct a dataset of transitions {(s1.74,S+.1),}\g fom each actuator.
- **p. 4 / B. Whole-body Controller Pre-training - extractive PDF cue:** We also randomize the PD gains and stall torques for each actuator in the robot's legs, and the policy lag length to learn robustness to ...
- **p. 7 / B. Finetuning Foundational WBC - extractive PDF cue:** Since the robot's arm is much weaker than the legs, the policy learns to pitch its base backwards to swing the weight upwards into the ...
- **p. 8 / B. Overcoming the sim-to-real gap - extractive PDF cue:** Their approach, however, relies on torque sensing, which is uncommon in consumer robotic hardware, [41] avoided reliance on an output torque sensor when training an ...
- **p. 6 / A. Comparing System Identification Approaches - extractive PDF cue:** ‘To further assess these system identification methods in a task context, we trained arm-only throwing policies in simulation augmented with each approach and deployed them ...
- **p. 7 / B. Finetuning Foundational WBC - extractive PDF cue:** Our fine-tuning approach requires a task reference trajectory, which may not be available for all robot morphologies or tasks.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** legged robot, terrain과 contact dynamics.
- **Input boundary:** proprioception, terrain/perception observation과 velocity command.
- **Output/decision under evaluation:** joint target, torque, footstep 또는 locomotion action.
- **Primary target:** velocity/progress, stability, energy와 terrain generalization.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 4: UAN improves simulator accuracy and real throwing performance. UAN (Ours) achieves lower sim-to-real difference in throw distance as compared to standard baselines, ... | p. 5 (Figure/Table caption) |
| A. Comparing System Identification Approaches | EMPIRICAL / REAL-ROBOT OR HARDWARE | We first evaluate the modeling accuracy of these approaches by reporting the mean-square joint position error on both the training data and on an ... | p. 5 (A. Comparing System Identification Approaches) |
| B. Finetuning Foundational WBC | EMPIRICAL / REAL-ROBOT OR HARDWARE | We found that No-Pre-Training achieved similar throwing performance to No-E2E, despite hitting a larger peak power ouput | p. 6 (B. Finetuning Foundational WBC) |
| B. Finetuning Foundational WBC | EMPIRICAL / REAL-ROBOT OR HARDWARE | However, the strong performance of No-E2E shows that the WBC' performance can be improved by providing a better reference trajectory. | p. 6 (B. Finetuning Foundational WBC) |
| A. Whole-Body Control | EMPIRICAL / REAL-ROBOT OR HARDWARE | WBC approaches based on offline trajectory optimization or online ‘optimization with reduced-order models have achieved considerable success in dynamic walking and manipulation (1, 3, ... | p. 7 (A. Whole-Body Control) |

## Dataset / Benchmark Role

- **p. 6 / B. Finetuning Foundational WBC - extractive PDF cue:** On hardware, the ball was thrown approximately 20m, with the real robot throwing slightly further than in simulation - possibly due to inaccuracies in the ...
- **p. 3 / A. Unsupervised Actuator Net - extractive PDF cue:** 4) Task Design: For each environment at each timestep, wwe uniformly sample a real-world transition, (8,74, $¢1)4. and set the state of the simulator to ...
- **p. 3 / A. Unsupervised Actuator Net - extractive PDF cue:** 2) Data collection: We collect data on real hardware to construct a dataset of transitions {(s1.74,S+.1),}\g fom each actuator.
- **p. 4 / B. Whole-body Controller Pre-training - extractive PDF cue:** We also randomize the PD gains and stall torques for each actuator in the robot's legs, and the policy lag length to learn robustness to ...
- **p. 7 / B. Finetuning Foundational WBC - extractive PDF cue:** Since the robot's arm is much weaker than the legs, the policy learns to pitch its base backwards to swing the weight upwards into the ...
- **p. 8 / B. Overcoming the sim-to-real gap - extractive PDF cue:** Their approach, however, relies on torque sensing, which is uncommon in consumer robotic hardware, [41] avoided reliance on an output torque sensor when training an ...
- **p. 6 / A. Comparing System Identification Approaches - extractive PDF cue:** ‘To further assess these system identification methods in a task context, we trained arm-only throwing policies in simulation augmented with each approach and deployed them ...
- **p. 7 / B. Finetuning Foundational WBC - extractive PDF cue:** Our fine-tuning approach requires a task reference trajectory, which may not be available for all robot morphologies or tasks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2: Unsupervised Actuator Network (UAN) approach for real-to-sim-to-real. Our training pipeline involves three steps: 1) Train a UAN to close the sim-to-real gap for ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 3: Unitree Z1 Pro arm. ‘This arm's harmonic actuators behave substantially differently from the quasi-direct-drive motors common in small legged robots. This image also ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 4: UAN improves simulator accuracy and real throwing performance. UAN (Ours) achieves lower sim-to-real difference in throw distance as compared to standard baselines, resulting ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Fig. 6: UAN achieves the tightest real-to-sim fit to the training data, as well as a throw trajectory unseen during training, We rolled out three ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | On hardware, the ball was thrown approximately 20m, with the real robot throwing slightly further than in simulation - possibly due to inaccuracies in ... | embodiment, simulator version and control stack | p. 6 (B. Finetuning Foundational WBC), p. 3 (A. Unsupervised Actuator Net) |
| Task/environment | 4) Task Design: For each environment at each timestep, wwe uniformly sample a real-world transition, (8,74, $¢1)4. and set the state of the simulator ... | reset, timeout, object/scene variation | p. 3 (A. Unsupervised Actuator Net), p. 3 (A. Unsupervised Actuator Net) |
| Observation/sensor | proprioception, terrain/perception observation과 velocity command | calibration, preprocessing, privileged input | p. 3 (B. Whole-body Controller Pre-training), p. 3 (B. Whole-body Controller Pre-training) |
| Output/decision | joint target, torque, footstep 또는 locomotion action | action frame, controller and termination | p. 2 (1. Iyrropucrion), p. 4 (B. Whole-body Controller Pre-training) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We first evaluate the modeling accuracy of these approaches by reporting the mean-square joint position error on both the training data and on an ... | definition/direction/unit from same section | p. 5 (A. Comparing System Identification Approaches) |
| Fig. 4: UAN improves simulator accuracy and real throwing performance. UAN (Ours) achieves lower sim-to-real difference in throw distance as compared to standard baselines, ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| The EE tracking term rewards ‘minimizing the distance between four key points, where one key point is positioned at the frame's origin, and the ... | definition/direction/unit from same section | p. 4 (B. Whole-body Controller Pre-training) |
| While [48] also guide training with reference trajectories, they rely on tracking rewards, whereas we crucially rely exclusively on task-oriented rewards, enabling athletic performance ... | definition/direction/unit from same section | p. 7 (A. Whole-Body Control) |
| In the field of dynamic legged robots, common parameters to randomize include the proportional and derivative gains of each joint, the stall torques. the ... | definition/direction/unit from same section | p. 7 (B. Overcoming the sim-to-real gap) |
| We found that Actuator-Net error remains bounded on the 5s throw trajectory but diverges when rolling out the 5 nin training trajectories, while the ... | definition/direction/unit from same section | p. 8 (B. Overcoming the sim-to-real gap) |
| task reward with the UAN in loop, and 3) Deploy. | definition/direction/unit from same section | p. 3 (A. Unsupervised Actuator Net) |
| For a complete list of reward terms, please refer to Appendix A | definition/direction/unit from same section | p. 3 (A. Unsupervised Actuator Net) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 4: UAN improves simulator accuracy and real throwing performance. UAN (Ours) achieves lower sim-to-real difference in throw distance as compared to standard baselines, ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| 1) Default: The baseline simulator with no addtional modifications | comparison identity and matched condition | p. 5 (A. Comparing System Identification Approaches) |
| peak leg power as compared to a throwing policy trained from scratch (No-P re. frozen WBC (No-#28). ‘The WBC before finetuning (No-Pine | comparison identity and matched condition | p. 6 (A. Comparing System Identification Approaches) |
| arm to match the lower joint velocities seen on hardware) Actuator Net can improve over the baseline by capturing lag effects, but it diverged ... | comparison identity and matched condition | p. 6 (A. Comparing System Identification Approaches) |
| Prior work proposed simulated athletic tasks as a benchmark for learned whole-body control [44, 26], though they left simto-real transfer as future work. | comparison identity and matched condition | p. 7 (B. Overcoming the sim-to-real gap) |
| Some policy architectures (i.e., CNNs [22] and transformers [35]) have been shown to achieve in-context adaptation without relying on a teacher-student distillation. | comparison identity and matched condition | p. 8 (B. Overcoming the sim-to-real gap) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In this section, we report ablations that identify the contribution of key system components and present results for the athletic tasks. | component/input/data sensitivity | p. 5 (A. Arm Modifications) |
| Following our UAN training (Section II-A), we pre-trained a WBC (Section II-B) and then fine-tuned policies for each task (Section II-C), Ablations comparing our ... | component/input/data sensitivity | p. 5 (C. Task-Specific Finetuning) |
| Some policy architectures (i.e., CNNs [22] and transformers [35]) have been shown to achieve in-context adaptation without relying on a teacher-student distillation. | component/input/data sensitivity | p. 8 (B. Overcoming the sim-to-real gap) |
| In contrast, our approach, UAN, employs an actuator net without relying on torque data, Instead, we train the network to predict corrective torques for ... | component/input/data sensitivity | p. 8 (B. Overcoming the sim-to-real gap) |
| Train UAN 2.Pre-train / Fine-tune WBC 3. | component/input/data sensitivity | p. 3 (A. Unsupervised Actuator Net) |
| and EE pose), then and fine-tune it on an athlet | component/input/data sensitivity | p. 3 (A. Unsupervised Actuator Net) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Rather than enforcing strict adherence to a reference trajectory, we propose treating it as a hint to guide exploration, In our approach, « WBC ... | Fig. 4: UAN improves simulator accuracy and real throwing performance. UAN (Ours) achieves lower sim-to-real difference in throw distance as compared to standard baselines, ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (Figure/Table caption), p. 5 (A. Comparing System Identification Approaches), p. 6 (B. Finetuning Foundational WBC), p. 6 (B. Finetuning Foundational WBC), p. 7 (A. Whole-Body Control), p. 8 (B. Overcoming the sim-to-real gap) |
| Primary metric/result | We first evaluate the modeling accuracy of these approaches by reporting the mean-square joint position error on both the training data and on an ... | numeric claim only at cited anchor | p. 5 (A. Comparing System Identification Approaches) |

- Numeric sentences retained from the body:
- **p. 3 / A. Unsupervised Actuator Net - extractive PDF cue:** Each training episode consists of a 20s rollout executing the torque sequence from the hardware data from 3, t0 8744.20 Through taining on rollouts, the ...
- **p. 3 / B. Whole-body Controller Pre-training - extractive PDF cue:** 1) Policy Architecture: "The WBC is a control policy, a, = ro(Or-yc4)e Where the action at time f, ay, is a vector of position targets ...
- **p. 3 / B. Whole-body Controller Pre-training - extractive PDF cue:** 2) Observation Space: ‘The policy's observation space consists of proprioceptive readings from the robot's onboard sen= sors including the gravity vector projected in the robot's ...
- **p. 4 / C. Task-Specific Finetuning - extractive PDF cue:** To avoid policy collapse, we set a low initial learning rate (1 x 10~®) for the actor and retain the standard deviation from pre-training.
- **p. 7 / B. Finetuning Foundational WBC - extractive PDF cue:** In both experiments, the robot lifted the weight above its base and maintained it there stably for more than 5s.
- **p. 8 / B. Overcoming the sim-to-real gap - extractive PDF cue:** We found that Actuator-Net error remains bounded on the 5s throw trajectory but diverges when rolling out the 5 nin training trajectories, while the UAN ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | During development, the Unitree ZI Pro arm experienced structural failures at inks 2 and 4, with minor deformations at Tink 5. | p. 5 (A. Arm Modifications) |
| body limitation/failure cue | Meanwhile, the Default, DR, and ROA policies produced unstable behaviors-the Default policy, for instance, strayed excessively and failed to throw the bull at all. | p. 6 (A. Comparing System Identification Approaches) |
| body limitation/failure cue | ‘To avoid the reliance on high-quality pre-training, another possibility is to discard the explicit notion of reference trajectories altogether and directly train end-to-end policies ... | p. 7 (A. Whole-Body Control) |
| body limitation/failure cue | For this comparison, wwe train and test policies with a fixed-base arm, to avoid the risk of the legged base falling during performance-critical ablations, | p. 5 (C. Task-Specific Finetuning) |
| body limitation/failure cue | Since the robot's arm is much weaker than the legs, the policy learns to pitch its base backwards to swing the weight upwards into ... | p. 7 (B. Finetuning Foundational WBC) |
| body limitation/failure cue | As shown by Figure 6, UAN can even accurately capture the arm's response to Gaussian noise control input, which is commonly used for exploration ... | p. 6 (A. Comparing System Identification Approaches) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| ining scheme buikls upon the method proposed in {7] by incorporating a strategy for learning to track an EE orientation command, As in Section ... | p. 3 (B. Whole-body Controller Pre-training) |
| 1) Policy Architecture: "The WBC is a control policy, a, = ro(Or-yc4)e Where the action at time f, ay, is a vector of position ... | p. 3 (B. Whole-body Controller Pre-training) |
| We also randomize the PD gains and stall torques for each actuator in the robot's legs, and the policy lag length to learn robustness ... | p. 4 (B. Whole-body Controller Pre-training) |
| To avoid policy collapse, we set a low initial learning rate (1 x 10~®) for the actor and retain the standard deviation from pre-training. | p. 4 (C. Task-Specific Finetuning) |
| 5) CEM: A method in which friction, frictional damping, ‘and armature parameters are optimized using the crossentropy method to minimize the mean-square joint position ... | p. 5 (A. Comparing System Identification Approaches) |
| Still, the No-E2E policy does not perform to the maximum capability of the hardware. | p. 6 (B. Finetuning Foundational WBC) |
| In contrast, the UAN policy achieved the farthest throws on hardware with the smallest sim-to-real gap. | p. 6 (A. Comparing System Identification Approaches) |
| Since the robot's arm is much weaker than the legs, the policy learns to pitch its base backwards to swing the weight upwards into ... | p. 7 (B. Finetuning Foundational WBC) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / A. Arm Modifications - extractive PDF cue:** During development, the Unitree ZI Pro arm experienced structural failures at inks 2 and 4, with minor deformations at Tink 5.
- **p. 6 / A. Comparing System Identification Approaches - extractive PDF cue:** Meanwhile, the Default, DR, and ROA policies produced unstable behaviors-the Default policy, for instance, strayed excessively and failed to throw the bull at all.
- **p. 7 / A. Whole-Body Control - extractive PDF cue:** ‘To avoid the reliance on high-quality pre-training, another possibility is to discard the explicit notion of reference trajectories altogether and directly train end-to-end policies for ...
- **p. 5 / C. Task-Specific Finetuning - extractive PDF cue:** For this comparison, wwe train and test policies with a fixed-base arm, to avoid the risk of the legged base falling during performance-critical ablations,
- **p. 7 / B. Finetuning Foundational WBC - extractive PDF cue:** Since the robot's arm is much weaker than the legs, the policy learns to pitch its base backwards to swing the weight upwards into the ...
- **p. 6 / A. Comparing System Identification Approaches - extractive PDF cue:** As shown by Figure 6, UAN can even accurately capture the arm's response to Gaussian noise control input, which is commonly used for exploration in ...

- **PDF anchors reviewed:** datasets p. 6 (B. Finetuning Foundational WBC), p. 3 (A. Unsupervised Actuator Net), p. 3 (A. Unsupervised Actuator Net), p. 4 (B. Whole-body Controller Pre-training), p. 7 (B. Finetuning Foundational WBC), p. 8 (B. Overcoming the sim-to-real gap), metrics p. 5 (A. Comparing System Identification Approaches), p. 5 (Figure/Table caption), p. 4 (B. Whole-body Controller Pre-training), p. 7 (A. Whole-Body Control), p. 7 (B. Overcoming the sim-to-real gap), p. 8 (B. Overcoming the sim-to-real gap), baselines p. 5 (Figure/Table caption), p. 5 (A. Comparing System Identification Approaches), p. 6 (A. Comparing System Identification Approaches), p. 6 (A. Comparing System Identification Approaches), p. 7 (B. Overcoming the sim-to-real gap), p. 8 (B. Overcoming the sim-to-real gap), results p. 5 (Figure/Table caption), p. 5 (A. Comparing System Identification Approaches), p. 6 (B. Finetuning Foundational WBC), p. 6 (B. Finetuning Foundational WBC), p. 7 (A. Whole-Body Control), p. 8 (B. Overcoming the sim-to-real gap).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
