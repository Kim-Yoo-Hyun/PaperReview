# Evaluation - RoboPanoptes: The All-Seeing Robot with Whole-body Dexterity

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p042.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p042.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (B. Sweeping Task), p. 9 (C. Stowing Task), p. 6 (21 Whole), p. 10 (IX. LIMITATIONS AND FUTURE WORK), p. 8 (B. Sweeping Task), p. 8 (B. Sweeping Task)): RoboPanoptes achieves a 96.6% success rate, outperforming all baselines.

## Evaluation Body Digest

- **p. 7 / A. Unboxing Task - extractive body cue:** Performance: ‘The training dataset contains 147 demonstration episodes, with each demonstration averaging 15s.
- **p. 8 / B. Sweeping Task - extractive body cue:** ‘Task: The robot needs to sweep all objects (small or large, randomly placed on a table or under a shelf) into a target region around ...
- **p. 4 / V. DATA COLLECTION INTERFACE - extractive body cue:** During the demonstration, images from all cameras and robot joint positions are recorded at 10 Hz
- **p. 4 / V. DATA COLLECTION INTERFACE - extractive body cue:** During teleoperation, torque is disabled for the leader robot while being enabled for the follower. ‘To demonstrate task, « human operator uses both hands to ...
- **p. 5 / 21 Whole - extractive body cue:** The robot's motions continuously change the ‘camera poses and, thereby, the region of the environment each ‘camera is observing.
- **p. 5 / 21 Whole - extractive body cue:** To this end, we exploit pretrained vision foundation models such as CLIP [28] or DINO [3] that enable advanced semantic understanding [4] and visually-complex robot ...
- **p. 6 / VII. PRACTICAL Cons - extractive body cue:** In the following, we study RoboPanoptes' ability to perform a wide range of real-world manipulation tasks that require whole-body dexterity.
- **p. 6 / VII. PRACTICAL Cons - extractive body cue:** It offers a compact design (8 x 25x 4.5 mm) that fits well within the spatial constraints of the robot while providing a reasonable FOV ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mobile base와 one/two-arm manipulation environment.
- **Input boundary:** egocentric RGB-D, language/task goal, base-arm proprioception.
- **Output/decision under evaluation:** base motion plus arm/gripper action.
- **Primary target:** long-horizon task success, reachability, collision과 recovery.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| B. Sweeping Task | EMPIRICAL / REAL-ROBOT OR HARDWARE | RoboPanoptes achieves a 96.6% success rate, outperforming all baselines. | p. 9 (B. Sweeping Task) |
| C. Stowing Task | EMPIRICAL / REAL-ROBOT OR HARDWARE | RoboPanoptes achieves an overall success rate of 83.3%, compared to 27.8% for the w/o Camexa Pose policy and 0% for the Top-down Camera policy ... | p. 9 (C. Stowing Task) |
| 21 Whole | EMPIRICAL / REAL-ROBOT OR HARDWARE | Consistent with observations in previous work [34], this simple strategy significantly improves the robustness of the policy, enabling it to succeed even when some ... | p. 6 (21 Whole) |
| IX. LIMITATIONS AND FUTURE WORK | EMPIRICAL / REAL-ROBOT OR HARDWARE | Using stronger and more precise motors could improve system performance. | p. 10 (IX. LIMITATIONS AND FUTURE WORK) |
| B. Sweeping Task | EMPIRICAL / REAL-ROBOT OR HARDWARE | The task success rate for sweeping multiple small objects is measured by the ratio of objects inside the target zone. | p. 8 (B. Sweeping Task) |

## Dataset / Benchmark Role

- **p. 7 / A. Unboxing Task - extractive body cue:** Performance: ‘The training dataset contains 147 demonstration episodes, with each demonstration averaging 15s.
- **p. 8 / B. Sweeping Task - extractive body cue:** ‘Task: The robot needs to sweep all objects (small or large, randomly placed on a table or under a shelf) into a target region around ...
- **p. 4 / V. DATA COLLECTION INTERFACE - extractive body cue:** During the demonstration, images from all cameras and robot joint positions are recorded at 10 Hz
- **p. 4 / V. DATA COLLECTION INTERFACE - extractive body cue:** During teleoperation, torque is disabled for the leader robot while being enabled for the follower. ‘To demonstrate task, « human operator uses both hands to ...
- **p. 5 / 21 Whole - extractive body cue:** The robot's motions continuously change the ‘camera poses and, thereby, the region of the environment each ‘camera is observing.
- **p. 5 / 21 Whole - extractive body cue:** To this end, we exploit pretrained vision foundation models such as CLIP [28] or DINO [3] that enable advanced semantic understanding [4] and visually-complex robot ...
- **p. 6 / VII. PRACTICAL Cons - extractive body cue:** In the following, we study RoboPanoptes' ability to perform a wide range of real-world manipulation tasks that require whole-body dexterity.
- **p. 6 / VII. PRACTICAL Cons - extractive body cue:** It offers a compact design (8 x 25x 4.5 mm) that fits well within the spatial constraints of the robot while providing a reasonable FOV ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Modular Hardware Design including a) a body module consisting of an actuator, two cameras, and wire fixtures, as well sb) a head module ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Data Collection Interface. The operator uses both hands to control the leader robot, whose joint angles are sent to the follower robot in ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Whole-body Visuomotor Policy leverages whole-body vision for whole-body dextri
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Sweeping Task. a) Different test scenarios. b) RoboPanoptes policy rollouts, highlighting the body contacts with objects. c) Typical failure cases of baselines. The ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 8: Stowing Task. a) Different test scenarios. b) RoboPanoptes policy rollouts, demonstrating the ability of precise long-horizon

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Performance: ‘The training dataset contains 147 demonstration episodes, with each demonstration averaging 15s. | embodiment, simulator version and control stack | p. 7 (A. Unboxing Task), p. 8 (B. Sweeping Task) |
| Task/environment | ‘Task: The robot needs to sweep all objects (small or large, randomly placed on a table or under a shelf) into a target region ... | reset, timeout, object/scene variation | p. 8 (B. Sweeping Task), p. 4 (V. DATA COLLECTION INTERFACE) |
| Observation/sensor | egocentric RGB-D, language/task goal, base-arm proprioception | calibration, preprocessing, privileged input | p. 2 (1. Ivrropuction), p. 2 (1. Ivrropuction) |
| Output/decision | base motion plus arm/gripper action | action frame, controller and termination | p. 4 (V. DATA COLLECTION INTERFACE), p. 4 (VI. WHOLE-Bopy VisUoMOTOR POLICY) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| overall 94.4% success rate, outperforming all baselines. | definition/direction/unit from same section | p. 8 (A. Unboxing Task) |
| The task success rate for sweeping multiple small objects is measured by the ratio of objects inside the target zone. | definition/direction/unit from same section | p. 8 (B. Sweeping Task) |
| We compare the methods' success rate and time per block in Fig. | definition/direction/unit from same section | p. 9 (B. Sweeping Task) |
| The take success rate is measured by whether both shoes are inside the drawer and the drawer is fully closed in the end. | definition/direction/unit from same section | p. 9 (C. Stowing Task) |
| Consistent with observations in previous work [34], this simple strategy significantly improves the robustness of the policy, enabling it to succeed even when some ... | definition/direction/unit from same section | p. 6 (21 Whole) |
| The leader's joint positions are sent to the follower in real time, allowing it to mirror the leader using PID position control at a ... | definition/direction/unit from same section | p. 4 (V. DATA COLLECTION INTERFACE) |
| During teleoperation, torque is disabled for the leader robot while being enabled for the follower. ‘To demonstrate task, « human operator uses both hands ... | definition/direction/unit from same section | p. 4 (V. DATA COLLECTION INTERFACE) |
| To coordinate the moving ‘cameras and make policy learning more efficient, we employ a view-dependent positional encoding strategy. | definition/direction/unit from same section | p. 5 (21 Whole) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| overall 94.4% success rate, outperforming all baselines. | comparison identity and matched condition | p. 8 (A. Unboxing Task) |
| Compared to a common manipulation system, RoboPanoptes needs to handle significantly more complex observation spaces due to the following factors: | comparison identity and matched condition | p. 4 (VI. WHOLE-Bopy VisUoMOTOR POLICY) |
| We compare RoboPanoptes/ with several baselines, including using a) only the head camera, b) the four neck cameras, and ¢) a top-down camera. | comparison identity and matched condition | p. 6 (VII. PRACTICAL Cons) |
| ) Typical failure cases of the baselines. | comparison identity and matched condition | p. 7 (VII. PRACTICAL Cons) |
| RoboPanoptes achieves an overall success rate of 83.3%, compared to 27.8% for the w/o Camexa Pose policy and 0% for the Top-down Camera policy ... | comparison identity and matched condition | p. 9 (C. Stowing Task) |
| With wholebody sweeping. the robot manipulates object piles much more efficiently, leveraging multiple contacts (2 s/block for teleoperation and 3.2s/block for our rollouts). as ... | comparison identity and matched condition | p. 9 (B. Sweeping Task) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Variants using all of RoboPanoptes' cameras but without view-dependent pesitional encoding or without blink traning serve as ablations of our design. | component/input/data sensitivity | p. 6 (VII. PRACTICAL Cons) |
| In contrast, USB cameras provide a reliable and standardized interface and, through UVC, are compatible across a wide range of devices without the need ... | component/input/data sensitivity | p. 6 (VII. PRACTICAL Cons) |
| + w/o Blink Training: A whole-body visuomotor policy trained without randomized camera dropouts. | component/input/data sensitivity | p. 7 (A. Unboxing Task) |
| + w/o Camera Pose: A whole-body visuomotor policy trained without view-dependent positional encoding. | component/input/data sensitivity | p. 7 (A. Unboxing Task) |
| For sweeping a large object, the task success rate is measured by whether the object is dragged into the target zone without being knocked ... | component/input/data sensitivity | p. 8 (B. Sweeping Task) |
| before, one using only a top-down camera and one without | component/input/data sensitivity | p. 9 (C. Stowing Task) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our primary contribution is the RoboPanoptes system, demonstrating novel whole-body dexterity capabilities through whole-body vision. | RoboPanoptes achieves a 96.6% success rate, outperforming all baselines. | PDF body cue; verify exact table/figure and matched conditions | p. 9 (B. Sweeping Task), p. 9 (C. Stowing Task), p. 6 (21 Whole), p. 10 (IX. LIMITATIONS AND FUTURE WORK), p. 8 (B. Sweeping Task), p. 8 (B. Sweeping Task) |
| Primary metric/result | RoboPanoptes achieves an overall success rate of 83.3%, compared to 27.8% for the w/o Camexa Pose policy and 0% for the Top-down Camera policy ... | numeric claim only at cited anchor | p. 9 (C. Stowing Task) |

- Numeric sentences retained from the body:
- **p. 4 / IV. MODULAR HARDWARE DESIGN - extractive body cue:** We use the Adafruit Ultra Tiny USB Camera with a GC0307 image sensor, characterized by an extremely small dimension (8x 25x 4.5 mm) that easily ...
- **p. 4 / V. DATA COLLECTION INTERFACE - extractive body cue:** The leader's joint positions are sent to the follower in real time, allowing it to mirror the leader using PID position control at a control ...
- **p. 4 / V. DATA COLLECTION INTERFACE - extractive body cue:** During the demonstration, images from all cameras and robot joint positions are recorded at 10 Hz
- **p. 5 / 21 Whole - extractive body cue:** Specif ically, we first resize the images to 224 x 224 resolution and apply color jiter augmentation, We batch the 21 images and feed them ...
- **p. 6 / 21 Whole - extractive body cue:** On average, the dropout rate (Le., camera discount) observed for the used cameras is 4.4% and latency ranges from 1Sms to 100ms.
- **p. 6 / VII. PRACTICAL Cons - extractive body cue:** It offers a compact design (8 x 25x 4.5 mm) that fits well within the spatial constraints of the robot while providing a reasonable FOV ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The Top-down Camere policy fails to locate the hance. ‘odiing policy's actions ae less precise, leading to failures ike missing the shoe or misaligning ... | p. 10 (IX. LIMITATIONS AND FUTURE WORK) |
| body limitation/failure cue | Using a whole-body visuomotor policy, RoboPanoptes learns to infer complex whole-body actions from high-dimensional camera observations, while remaining robust to potential sensor failures. | p. 10 (X. CONCLUSION) |
| body limitation/failure cue | + Unreliable cameras: A system of many cameras is prone to unpredictable failures and delays, requiring the policy to be robust to such disturbances, | p. 4 (VI. WHOLE-Bopy VisUoMOTOR POLICY) |
| body limitation/failure cue | Since our demonstration data contains behaviors of recovering from a sub-goal failure (c.g. failed grasps), we observe that the learned policy is able to ... | p. 9 (C. Stowing Task) |
| body limitation/failure cue | To make the system robust to such camera failure at test time, we employ a "blink training" strategy that randomly drops out camera inputs ... | p. 6 (21 Whole) |
| body limitation/failure cue | This proves that our blink training strategy is critical to the robustness of the policy, especially during unexpected test-time sensor failures. | p. 8 (A. Unboxing Task) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| refully coded motion patterns (e.., sinusoid functions (21, 40, 2), which do not transfer to complex manipulation tasks While RL exploration offers an altematve, ... | p. 4 (V. DATA COLLECTION INTERFACE) |
| Specifically, we ‘compute the 6D camera poses in the base frame using the forward kinematics based on the current joint angles. | p. 5 (21 Whole) |
| It predicts T, actions A,, of which Ty < Tp are executed on the robot. {In our implementation, we set the observation horizon T, ... | p. 5 (21 Whole) |
| This section highlights critical implementation details for developing an effective RoboPanoptes system. | p. 6 (VII. PRACTICAL Cons) |
| In contrast, USB cameras provide a reliable and standardized interface and, through UVC, are compatible across a wide range of devices without the need ... | p. 6 (VII. PRACTICAL Cons) |
| + ResNet Encodes: A whole-body visuomotor policy with a ResNet-34 [15] vision encoder trained from seratch instead of using a pretrained vision encoder. | p. 9 (B. Sweeping Task) |
| Encoder policy often sweeps toward incorrect or empty regions, which we hypothesize is due to Inaccurate semantic understanding in the visual representation, | p. 9 (B. Sweeping Task) |
| In our current implementation, the robot's fixed base limits it to table-top manipulation tasks. | p. 10 (IX. LIMITATIONS AND FUTURE WORK) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / IX. LIMITATIONS AND FUTURE WORK - extractive body cue:** The Top-down Camere policy fails to locate the hance. ‘odiing policy's actions ae less precise, leading to failures ike missing the shoe or misaligning the ...
- **p. 10 / X. CONCLUSION - extractive body cue:** Using a whole-body visuomotor policy, RoboPanoptes learns to infer complex whole-body actions from high-dimensional camera observations, while remaining robust to potential sensor failures.
- **p. 4 / VI. WHOLE-Bopy VisUoMOTOR POLICY - extractive body cue:** + Unreliable cameras: A system of many cameras is prone to unpredictable failures and delays, requiring the policy to be robust to such disturbances,
- **p. 9 / C. Stowing Task - extractive body cue:** Since our demonstration data contains behaviors of recovering from a sub-goal failure (c.g. failed grasps), we observe that the learned policy is able to capture ...
- **p. 6 / 21 Whole - extractive body cue:** To make the system robust to such camera failure at test time, we employ a "blink training" strategy that randomly drops out camera inputs during ...
- **p. 8 / A. Unboxing Task - extractive body cue:** This proves that our blink training strategy is critical to the robustness of the policy, especially during unexpected test-time sensor failures.

- **Evidence anchors reviewed:** datasets p. 7 (A. Unboxing Task), p. 8 (B. Sweeping Task), p. 4 (V. DATA COLLECTION INTERFACE), p. 4 (V. DATA COLLECTION INTERFACE), p. 5 (21 Whole), p. 5 (21 Whole), metrics p. 8 (A. Unboxing Task), p. 8 (B. Sweeping Task), p. 9 (B. Sweeping Task), p. 9 (C. Stowing Task), p. 6 (21 Whole), p. 4 (V. DATA COLLECTION INTERFACE), baselines p. 8 (A. Unboxing Task), p. 4 (VI. WHOLE-Bopy VisUoMOTOR POLICY), p. 6 (VII. PRACTICAL Cons), p. 7 (VII. PRACTICAL Cons), p. 9 (C. Stowing Task), p. 9 (B. Sweeping Task), results p. 9 (B. Sweeping Task), p. 9 (C. Stowing Task), p. 6 (21 Whole), p. 10 (IX. LIMITATIONS AND FUTURE WORK), p. 8 (B. Sweeping Task), p. 8 (B. Sweeping Task).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** overall 94.4% success rate, outperforming all baselines. (p. 8, A. Unboxing Task).
- **Metric evidence:** Consistent with observations in previous work [34], this simple strategy significantly improves the robustness of the policy, enabling it to succeed even when some cameras are completely disabled during test ... (p. 6, 21 Whole).
- **Baseline/ablation evidence:** Variants using all of RoboPanoptes' cameras but without view-dependent pesitional encoding or without blink traning serve as ablations of our design. (p. 6, VII. PRACTICAL Cons).
- **Failure/negative evidence:** The Top-down Camere policy fails to locate the hance. ‘odiing policy's actions ae less precise, leading to failures ike missing the shoe or misaligning the drawer. (p. 10, IX. LIMITATIONS AND FUTURE WORK).
