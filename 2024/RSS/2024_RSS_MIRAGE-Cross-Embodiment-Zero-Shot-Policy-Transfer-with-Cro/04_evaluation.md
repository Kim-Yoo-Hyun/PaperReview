# Evaluation - MIRAGE: Cross-Embodiment Zero-Shot Policy Transfer with Cross-Painting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p069.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p069.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 9 (Figure/Table caption), p. 2 (3) Physical experiments with Franka and UR5 demonstrating), p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS)): Study Results Table I shows that when the target robots have the same gripper as the source robot, most unseen target robots achieve very high task success rates.

## Evaluation Body Digest

- **p. 6 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** For simulation experiments, we take into account potential occlusions between the robot and objects by comparing the pixel-wise depth values between the camera observation of ...
- **p. 4 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** To motivate the study, imagine there is a source robot ("oracle") teaching a target robot to perform a task side by side in a duplicate ...
- **p. 4 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** At each timestep, the source robot sees the world state (pr, po) of the target environment, where pr and po are the poses of the ...
- **p. 5 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** Study Results Table I shows that when the target robots have the same gripper as the source robot, most unseen target robots achieve very high ...
- **p. 5 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** Results suggest that most unseen target robots can successfully perform the tasks using the source robot as its guide for where to move its gripper. ...
- **p. 2 / 3) Physical experiments with Franka and UR5 demonstrating - extractive body cue:** that Mirage successfully transfers between robots and grippers on 4 manipulation tasks, suffering only minimal performance degradation from the source policy and significantly outperforming a ...
- **p. 6 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** We use the source robot trajectory data D to fit a forward dynamics model f on the transitions: f(pS r,t, aS t ) = pS ...
- **p. 4 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** For all tasks, we train the source state-based policy on the Franka robot and evaluate the success rates on different target robots using the test-time ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 3) Physical experiments with Franka and UR5 demonstrating (p. 2); IV. STATE-BASED TRANSFER EXPERIMENTS (p. 4); VI. VISION-BASED POLICY TRANSFER EXPERIMENTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. STATE-BASED TRANSFER EXPERIMENTS | EMPIRICAL / SIMULATION | Study Results Table I shows that when the target robots have the same gripper as the source robot, most unseen target robots achieve very ... | p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Fig. 5: Mirage applied to first-person wrist camera images and third- person front camera images. For each view, the top row shows the actual ... | p. 9 (Figure/Table caption) |
| 3) Physical experiments with Franka and UR5 demonstrating | EMPIRICAL / SIMULATION | that Mirage successfully transfers between robots and grippers on 4 manipulation tasks, suffering only minimal performance degradation from the source policy and significantly outperforming ... | p. 2 (3) Physical experiments with Franka and UR5 demonstrating) |
| IV. STATE-BASED TRANSFER EXPERIMENTS | EMPIRICAL / SIMULATION | In comparison, with a 3-jaw gripper, Jaco's success rates are significantly lower than the others', especially on more challenging tasks, where the grasp configuration ... | p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS) |
| IV. STATE-BASED TRANSFER EXPERIMENTS | EMPIRICAL / SIMULATION | For all tasks, we train the source state-based policy on the Franka robot and evaluate the success rates on different target robots using the ... | p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** For simulation experiments, we take into account potential occlusions between the robot and objects by comparing the pixel-wise depth values between the camera observation of ...
- **p. 4 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** To motivate the study, imagine there is a source robot ("oracle") teaching a target robot to perform a task side by side in a duplicate ...
- **p. 4 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** At each timestep, the source robot sees the world state (pr, po) of the target environment, where pr and po are the poses of the ...
- **p. 5 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** Study Results Table I shows that when the target robots have the same gripper as the source robot, most unseen target robots achieve very high ...
- **p. 5 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** Results suggest that most unseen target robots can successfully perform the tasks using the source robot as its guide for where to move its gripper. ...
- **p. 2 / 3) Physical experiments with Franka and UR5 demonstrating - extractive body cue:** that Mirage successfully transfers between robots and grippers on 4 manipulation tasks, suffering only minimal performance degradation from the source policy and significantly outperforming a ...
- **p. 6 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** We use the source robot trajectory data D to fit a forward dynamics model f on the transitions: f(pS r,t, aS t ) = pS ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Overview of Mirage. We study zero-shot policy transfer across embodiments. Assume there is a policy trained on a source robot (left). At test ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Simulation Tasks and Robots. The simulation evaluation utilizes the Robosuite simulator with Lift, Stack, Can Pick-and-Place, Two Piece Assembly, and Square Peg Insertion ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: Illustration of Mirage's pipeline. We reproject the camera from the target frame to the source frame if there is a non-negligible camera angle ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4: Trajectory Rollouts of Simulated (Left) and Real (Right) Tasks. For each task, the top row shows the actual observations of the target robot ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 5: Mirage applied to first-person wrist camera images and third- person front camera images. For each view, the top row shows the actual observations ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 6: (a) An example of camera calibration error resulting in failure to mask all of the target robot out; (b) An example of the ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For simulation experiments, we take into account potential occlusions between the robot and objects by comparing the pixel-wise depth values between the camera observation ... | embodiment, simulator version and control stack | p. 6 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS) |
| Task/environment | To motivate the study, imagine there is a source robot ("oracle") teaching a target robot to perform a task side by side in a ... | reset, timeout, object/scene variation | p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (4) We assume that the background and lighting conditions), p. 4 (4) We assume that the background and lighting conditions) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 3 (III. PROBLEM STATEMENT), p. 7 (2) Can Mirage successfully zero-shot transfer trained vision) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For all tasks, we train the source state-based policy on the Franka robot and evaluate the success rates on different target robots using the ... | definition/direction/unit from same section | p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS) |
| Study Results Table I shows that when the target robots have the same gripper as the source robot, most unseen target robots achieve very ... | definition/direction/unit from same section | p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS) |
| In comparison, with a 3-jaw gripper, Jaco's success rates are significantly lower than the others', especially on more challenging tasks, where the grasp configuration ... | definition/direction/unit from same section | p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS) |
| The source policy predicts delta Cartesian actions and we use the operation space controller [49] on the target robot to servo to the pose ... | definition/direction/unit from same section | p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS) |
| that Mirage successfully transfers between robots and grippers on 4 manipulation tasks, suffering only minimal performance degradation from the source policy and significantly outperforming ... | definition/direction/unit from same section | p. 2 (3) Physical experiments with Franka and UR5 demonstrating) |
| Fig. 6: (a) An example of camera calibration error resulting in failure to mask all of the target robot out; (b) An example of ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| For real experiments, however, we do not use depth due to noise and imprecision in the camera observations. | definition/direction/unit from same section | p. 6 (IV. STATE-BASED TRANSFER EXPERIMENTS) |
| Fig. 5: Mirage applied to first-person wrist camera images and third- person front camera images. For each view, the top row shows the actual ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| that Mirage successfully transfers between robots and grippers on 4 manipulation tasks, suffering only minimal performance degradation from the source policy and significantly outperforming ... | comparison identity and matched condition | p. 2 (3) Physical experiments with Franka and UR5 demonstrating) |
| Fig. 5: Mirage applied to first-person wrist camera images and third- person front camera images. For each view, the top row shows the actual ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| To motivate the study, imagine there is a source robot ("oracle") teaching a target robot to perform a task side by side in a ... | comparison identity and matched condition | p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS) |
| MIRAGE: A CROSS-EMBODIMENT TRANSFER STRATEGY FOR VISION-BASED POLICIES Motivated by the observation that target robots can successfully perform tasks to a large extent simply ... | comparison identity and matched condition | p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS) |
| Note that Jaco has a 3-jaw gripper, but we include it for comparison. | comparison identity and matched condition | p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS) |
| In comparison, with a 3-jaw gripper, Jaco's success rates are significantly lower than the others', especially on more challenging tasks, where the grasp configuration ... | comparison identity and matched condition | p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Bridging the Visual Gap To replace the robots, we leverage the knowledge of the robot URDFs and camera poses to perform cross-painting at test ... | component/input/data sensitivity | p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To summarize, our key contributions are: | Study Results Table I shows that when the target robots have the same gripper as the source robot, most unseen target robots achieve very ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 9 (Figure/Table caption), p. 2 (3) Physical experiments with Franka and UR5 demonstrating), p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS) |
| Primary metric/result | Fig. 5: Mirage applied to first-person wrist camera images and third- person front camera images. For each view, the top row shows the actual ... | numeric claim only at cited anchor | p. 9 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 4 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** To answer this question, we consider 8 tasks across 3 simulators (Robosuite [119], ORBIT [69], and RLBench [43]) (Fig.
- **p. 4 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** Implementation Details For Robosuite, we choose 5 tasks: Lift, Stack, Can, Two Piece Assembly, and Square.
- **p. 5 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** We study 2 tasks: take the lid off a saucepan ("Unlid Pan") and turn on a lamp ("Lamp On"), and evaluate on the UR5 and ...
- **p. 4 / 1) We assume knowledge of the two robots' coordinate - extractive body cue:** Additionally, to study other policy classes, we evaluate policy transfers in ORBIT with a block lifting task, and in RLBench with 2 tasks: Lifting a ...
- **p. 6 / 2) Can Mirage successfully zero-shot transfer trained vision - extractive body cue:** The policies utilize 84x84 images, and Mirage operates at approximately 40 Hz to cross-paint the images.
- **p. 8 / 2) Can Mirage successfully zero-shot transfer trained vision - extractive body cue:** We evaluate Mirage on 4 tasks in 2 settings: Target (Different) Gripper ("T Grip"): Transferring policies between the Franka gripper and the Robotiq 2F-85 gripper ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Less robust source policies leave little room for error, while more robust ones tend to retry even if the target robot fails to grasp ... | p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS) |
| body limitation/failure cue | On the other hand, the failure modes we observe on the different robots or grippers are all very similar to those from the source ... | p. 9 (2) Can Mirage successfully zero-shot transfer trained vision) |
| body limitation/failure cue | Fig. 6: (a) An example of camera calibration error resulting in failure to mask all of the target robot out; (b) An example of ... | p. 10 (Figure/Table caption) |
| body limitation/failure cue | We see that there is a significant drop in performance, indicating that the difference in the forward dynamics between robots cannot be ignored when ... | p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS) |
| body limitation/failure cue | This is not surprising as the policy is trained with matching proprioceptive values and image observations, and large offsets in the proprioceptive values correspond ... | p. 9 (2) Can Mirage successfully zero-shot transfer trained vision) |
| body limitation/failure cue | that Mirage successfully transfers between robots and grippers on 4 manipulation tasks, suffering only minimal performance degradation from the source policy and significantly outperforming ... | p. 2 (3) Physical experiments with Franka and UR5 demonstrating) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Implementation Details For Robosuite, we choose 5 tasks: Lift, Stack, Can, Two Piece Assembly, and Square. | p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS) |
| Robosuite and ORBIT policies use closed-loop control (a trajectory consists of >50 timesteps), while for RLBench, the policies use open-loop control (a trajectory consists ... | p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS) |
| For the gripper, we similarly compute and set the joints of the source robot gripper in the renderer so that its width would roughly ... | p. 6 (IV. STATE-BASED TRANSFER EXPERIMENTS) |
| The target robot then uses a forward dynamics model to obtain the desired end effector pose in the target robot frame and executes the ... | p. 1 (2 Google DeepMind) |
| IV, we first train the source robot policies with behavior cloning (BC-RNN) on the provided demonstration data for each task (200 demos for Lift ... | p. 6 (2) Can Mirage successfully zero-shot transfer trained vision) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** Less robust source policies leave little room for error, while more robust ones tend to retry even if the target robot fails to grasp the ...
- **p. 9 / 2) Can Mirage successfully zero-shot transfer trained vision - extractive body cue:** On the other hand, the failure modes we observe on the different robots or grippers are all very similar to those from the source policy ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 6: (a) An example of camera calibration error resulting in failure to mask all of the target robot out; (b) An example of the ...
- **p. 5 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** We see that there is a significant drop in performance, indicating that the difference in the forward dynamics between robots cannot be ignored when transferring ...
- **p. 9 / 2) Can Mirage successfully zero-shot transfer trained vision - extractive body cue:** This is not surprising as the policy is trained with matching proprioceptive values and image observations, and large offsets in the proprioceptive values correspond to ...
- **p. 2 / 3) Physical experiments with Franka and UR5 demonstrating - extractive body cue:** that Mirage successfully transfers between robots and grippers on 4 manipulation tasks, suffering only minimal performance degradation from the source policy and significantly outperforming a ...

- **Evidence anchors reviewed:** datasets p. 6 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 2 (3) Physical experiments with Franka and UR5 demonstrating), metrics p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 2 (3) Physical experiments with Franka and UR5 demonstrating), p. 10 (Figure/Table caption), baselines p. 2 (3) Physical experiments with Franka and UR5 demonstrating), p. 9 (Figure/Table caption), p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS), results p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 9 (Figure/Table caption), p. 2 (3) Physical experiments with Franka and UR5 demonstrating), p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Study Results Table I shows that when the target robots have the same gripper as the source robot, most unseen target robots achieve very high task success rates. (p. 5, IV. STATE-BASED TRANSFER EXPERIMENTS).
- **Metric evidence:** that Mirage successfully transfers between robots and grippers on 4 manipulation tasks, suffering only minimal performance degradation from the source policy and significantly outperforming a state-of-the-art generalist model. (p. 2, 3) Physical experiments with Franka and UR5 demonstrating).
- **Baseline/ablation evidence:** that Mirage successfully transfers between robots and grippers on 4 manipulation tasks, suffering only minimal performance degradation from the source policy and significantly outperforming a state-of-the-art generalist model. (p. 2, 3) Physical experiments with Franka and UR5 demonstrating).
- **Failure/negative evidence:** Less robust source policies leave little room for error, while more robust ones tend to retry even if the target robot fails to grasp the object the first time. (p. 5, IV. STATE-BASED TRANSFER EXPERIMENTS).
