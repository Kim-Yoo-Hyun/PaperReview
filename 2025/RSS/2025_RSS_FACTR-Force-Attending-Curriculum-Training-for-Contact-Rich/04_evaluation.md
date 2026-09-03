# Evaluation - FACTR: Force-Attending Curriculum Training for Contact-Rich Policy Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p079.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p079.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (C. Policy Evaluation), p. 8 (C. Policy Evaluation), p. 7 (C. Policy Evaluation), p. 7 (B. Teleoperation Evaluation), p. 6 (A. Experimental Setup), p. 9 (C. Policy Evaluation)): For the test objects, the vision-only policy achieves a success rate of 21.3% on average, which is significantly worse than policies incorporating force.

## Evaluation Body Digest

- **p. 7 / B. Teleoperation Evaluation - extractive body cue:** These asks are challenging as they require the robot to perceive and respond to the force feedback as it manipulates objects with unseen visual appearances ...
- **p. 8 / C. Policy Evaluation - extractive body cue:** We hypothesize that the force information provides important signals for mode switehing at moments such as when the robots get into contact withthe box in ...
- **p. 7 / B. Teleoperation Evaluation - extractive body cue:** We observe that for tasks that require continuous contact between the arm and an object, such as non-prehensile pivoting and bimanual box lifting, the un-actuated ...
- **p. 6 / A. Experimental Setup - extractive body cue:** «+ Fruit Pick and Place: The robot grasps a soft and delicate fruit and places it in a bowl, using the wrist camera and the ...
- **p. 6 / A. Experimental Setup - extractive body cue:** + Rolling Dough: The robot continuously rolls the dough to shape it into a eylinder for at least 8 seconds, using the front camera and ...
- **p. 8 / C. Policy Evaluation - extractive body cue:** Another notable observation is that FACTR also facilitates recovery behay Specifically, we evaluate the box-lifting task with five trials per object.
- **p. 9 / C. Policy Evaluation - extractive body cue:** [Right] FACTR leams to aitend to force more to complete the task.
- **p. 9 / C. Policy Evaluation - extractive body cue:** We choose the task of pivoting, one of the hardest tasks from our task suite, for the ablations.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** contact-rich manipulation scene.
- **Input boundary:** tactile image/force, vision과 proprioceptive history.
- **Output/decision under evaluation:** grasp/contact action, force command 또는 object motion.
- **Primary target:** slip/contact success, force/pose error와 robustness.
- **Detected evaluation headings:** V. EVALUATION (p. 6); A. Experimental Setup (p. 6); B. Teleoperation Evaluation (p. 6); C. Policy Evaluation (p. 7); XI. ADDITIONAL EXPERIMENTS (p. 14); XII. DETAILED QUANTITATIVE RESULTS (p. 14).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| C. Policy Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | For the test objects, the vision-only policy achieves a success rate of 21.3% on average, which is significantly worse than policies incorporating force. | p. 8 (C. Policy Evaluation) |
| C. Policy Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | Without a curriculum, policies naively incorporating force achieve a success rate of 61.2%, ‘hile FACTR achieves a success rate of 87.5%, which shows that ... | p. 8 (C. Policy Evaluation) |
| C. Policy Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | We present the average success rate for truining and testing objects, respectively. | p. 7 (C. Policy Evaluation) |
| B. Teleoperation Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our experiments show that our system allows users to ‘complete tasks with 64.7% higher task completion rate, 37.4% reduced completion time, and 83.3% improvement ... | p. 7 (B. Teleoperation Evaluation) |
| A. Experimental Setup | EMPIRICAL / SOURCE-REPORTED EVALUATION | We describe the tasks details and the success erteria below | p. 6 (A. Experimental Setup) |

## Dataset / Benchmark Role

- **p. 7 / B. Teleoperation Evaluation - extractive body cue:** These asks are challenging as they require the robot to perceive and respond to the force feedback as it manipulates objects with unseen visual appearances ...
- **p. 8 / C. Policy Evaluation - extractive body cue:** We hypothesize that the force information provides important signals for mode switehing at moments such as when the robots get into contact withthe box in ...
- **p. 7 / B. Teleoperation Evaluation - extractive body cue:** We observe that for tasks that require continuous contact between the arm and an object, such as non-prehensile pivoting and bimanual box lifting, the un-actuated ...
- **p. 6 / A. Experimental Setup - extractive body cue:** «+ Fruit Pick and Place: The robot grasps a soft and delicate fruit and places it in a bowl, using the wrist camera and the ...
- **p. 6 / A. Experimental Setup - extractive body cue:** + Rolling Dough: The robot continuously rolls the dough to shape it into a eylinder for at least 8 seconds, using the front camera and ...
- **p. 8 / C. Policy Evaluation - extractive body cue:** Another notable observation is that FACTR also facilitates recovery behay Specifically, we evaluate the box-lifting task with five trials per object.
- **p. 9 / C. Policy Evaluation - extractive body cue:** [Right] FACTR leams to aitend to force more to complete the task.
- **p. 9 / C. Policy Evaluation - extractive body cue:** We choose the task of pivoting, one of the hardest tasks from our task suite, for the ablations.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: Our low-cost bimanual teleoperation system with force- feedback. The system features wo actuated leader arms, two follower arms with external joint torque sensors ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: FACTR allows our policy to beter integrate force information without overfittng to visual information, resulting in better generalization
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Tasks. We evaluate our leader follower teleoperation system and autonomous policies trained with FACTR on four contact-rich tasks. These asks are challenging as ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: FACTR leads to better object generalization,
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: User study. FACTR teleoperation system allows users to complete tasks
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 9: Policies trained with FACTR learns to identify mode switching. We visualize the average cross attention of the aeton tokens to

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | These asks are challenging as they require the robot to perceive and respond to the force feedback as it manipulates objects with unseen visual ... | embodiment, simulator version and control stack | p. 7 (B. Teleoperation Evaluation), p. 8 (C. Policy Evaluation) |
| Task/environment | We hypothesize that the force information provides important signals for mode switehing at moments such as when the robots get into contact withthe box ... | reset, timeout, object/scene variation | p. 8 (C. Policy Evaluation), p. 7 (B. Teleoperation Evaluation) |
| Observation/sensor | tactile image/force, vision과 proprioceptive history | calibration, preprocessing, privileged input | p. 4 (A. Problem Statement and Base Model), p. 5 (A. Problem Statement and Base Model) |
| Output/decision | grasp/contact action, force command 또는 object motion | action frame, controller and termination | p. 5 (A. Problem Statement and Base Model), p. 4 (A. Problem Statement and Base Model) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We present the average success rate for truining and testing objects, respectively. | definition/direction/unit from same section | p. 7 (C. Policy Evaluation) |
| th significantly higher success rate, using less time, and. | definition/direction/unit from same section | p. 8 (C. Policy Evaluation) |
| In contrast, force-attending policies maintain similar success rates across both attempts. | definition/direction/unit from same section | p. 8 (C. Policy Evaluation) |
| When contact is lst, the resulting large joint-space error causes the PID controller to generate large torques, causing abrupt movements that exceed the velocity ... | definition/direction/unit from same section | p. 7 (B. Teleoperation Evaluation) |
| We describe the tasks details and the success erteria below | definition/direction/unit from same section | p. 6 (A. Experimental Setup) |
| We setup four contact-rich tasks, which are illustrated in Fig. | definition/direction/unit from same section | p. 6 (A. Experimental Setup) |
| We found that performance with a curriculum of decaying smoothing performs better than a fixed curriculum across all tasks. | definition/direction/unit from same section | p. 9 (C. Policy Evaluation) |
| We hypothesize that to enable better performance, the final policy needs to take in the fully unblurred vision information. | definition/direction/unit from same section | p. 9 (C. Policy Evaluation) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| ‘+ How does FACTR perform compared to baseline approaches that do not use force feedback and ones that use force feedback without FACTR? | comparison identity and matched condition | p. 7 (C. Policy Evaluation) |
| follower baseline system with mechanical joint regulation, similar to [29]. | comparison identity and matched condition | p. 7 (B. Teleoperation Evaluation) |
| While without the curriculum, the policy does not pay enough attention 10 force, and either fails to lift or balance the novel boxes. | comparison identity and matched condition | p. 8 (C. Policy Evaluation) |
| Without a curriculum, policies naively incorporating force achieve a success rate of 61.2%, ‘hile FACTR achieves a success rate of 87.5%, which shows that ... | comparison identity and matched condition | p. 8 (C. Policy Evaluation) |
| ‘Comparisons with other scheduler parameters. | comparison identity and matched condition | p. 9 (C. Policy Evaluation) |
| We choose the task of pivoting, one of the hardest tasks from our task suite, for the ablations. | comparison identity and matched condition | p. 9 (C. Policy Evaluation) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We discuss more detailed ablations ‘on the curriculum in See. | component/input/data sensitivity | p. 7 (C. Policy Evaluation) |
| ‘+ How does FACTR perform compared to baseline approaches that do not use force feedback and ones that use force feedback without FACTR? | component/input/data sensitivity | p. 7 (C. Policy Evaluation) |
| While without the curriculum, the policy does not pay enough attention 10 force, and either fails to lift or balance the novel boxes. | component/input/data sensitivity | p. 8 (C. Policy Evaluation) |
| Without a curriculum, policies naively incorporating force achieve a success rate of 61.2%, ‘hile FACTR achieves a success rate of 87.5%, which shows that ... | component/input/data sensitivity | p. 8 (C. Policy Evaluation) |
| We choose the task of pivoting, one of the hardest tasks from our task suite, for the ablations. | component/input/data sensitivity | p. 9 (C. Policy Evaluation) |
| Fig. 4: FACTR allows our policy to beter integrate force information without overfittng to visual information, resulting in better generalization | component/input/data sensitivity | p. 5 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| For the decoder, we introduce & action tokens, A ¢ R**¢. | For the test objects, the vision-only policy achieves a success rate of 21.3% on average, which is significantly worse than policies incorporating force. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (C. Policy Evaluation), p. 8 (C. Policy Evaluation), p. 7 (C. Policy Evaluation), p. 7 (B. Teleoperation Evaluation), p. 6 (A. Experimental Setup), p. 9 (C. Policy Evaluation) |
| Primary metric/result | Without a curriculum, policies naively incorporating force achieve a success rate of 61.2%, ‘hile FACTR achieves a success rate of 87.5%, which shows that ... | numeric claim only at cited anchor | p. 8 (C. Policy Evaluation) |

- Numeric sentences retained from the body:
- **p. 7 / C. Policy Evaluation - extractive body cue:** For each object in each task, we evaluated 5-10 trials.
- **p. 9 / C. Policy Evaluation - extractive body cue:** Pixel Space Latent Space Blur Downsample Blur Downsample Constant 1625 1525 17RS---«6RS, Linear 19725 182519725 «18/25 Cosine 2025 «1972517259725, Exp 1925 2125202519125 Step 1925 1825202519725

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Developing. adaptive or self-tuning curriculum strategies could help mitigate this issue by dynamically adjusting hyperparameters based on task-specific requirements, Addressing these limitations could further ... | p. 9 (VI. CONCLUSION AND LIMITATIONS) |
| body limitation/failure cue | While without the curriculum, the policy does not pay enough attention 10 force, and either fails to lift or balance the novel boxes. | p. 8 (C. Policy Evaluation) |
| body limitation/failure cue | This limitation can particularly affect tasks that involve subtle force adjustments during finegrained manipulation since the torque readings can be too noisy to be ... | p. 9 (VI. CONCLUSION AND LIMITATIONS) |
| body limitation/failure cue | 6, All the policies perform similarly on the train objects for most tasks, except for the rolling dough task, where the vision-only policy smashes ... | p. 7 (C. Policy Evaluation) |
| body limitation/failure cue | FACTR leads to better recovery behavior. | p. 8 (C. Policy Evaluation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For each object in each task, we evaluated 5-10 trials. | p. 7 (C. Policy Evaluation) |
| We collected 50 demonstrations with our teleoperation system, We trained each method with the same hyperparameters, where details can be found in the Appendix ... | p. 7 (C. Policy Evaluation) |
| A trial begins when the policy successfully lifts the box for the first time; we then knock the box down and assess the second ... | p. 8 (C. Policy Evaluation) |
| Another notable observation is that FACTR also facilitates recovery behay Specifically, we evaluate the box-lifting task with five trials per object. | p. 8 (C. Policy Evaluation) |
| the force oF vision tokens of the first decoder layer during policy rollout. | p. 9 (C. Policy Evaluation) |
| We evaluate only on the five test objects for five trials each, since they are more indicative of policy performance than train objects. | p. 9 (C. Policy Evaluation) |
| We let dues be the predicted future joint position targets over the next k time steps. | p. 4 (A. Problem Statement and Base Model) |
| Vision Encoder 4 Extemal : . a Force ext | p. 5 (A. Problem Statement and Base Model) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / VI. CONCLUSION AND LIMITATIONS - extractive body cue:** Developing. adaptive or self-tuning curriculum strategies could help mitigate this issue by dynamically adjusting hyperparameters based on task-specific requirements, Addressing these limitations could further enhance ...
- **p. 8 / C. Policy Evaluation - extractive body cue:** While without the curriculum, the policy does not pay enough attention 10 force, and either fails to lift or balance the novel boxes.
- **p. 9 / VI. CONCLUSION AND LIMITATIONS - extractive body cue:** This limitation can particularly affect tasks that involve subtle force adjustments during finegrained manipulation since the torque readings can be too noisy to be used ...
- **p. 7 / C. Policy Evaluation - extractive body cue:** 6, All the policies perform similarly on the train objects for most tasks, except for the rolling dough task, where the vision-only policy smashes the ...
- **p. 8 / C. Policy Evaluation - extractive body cue:** FACTR leads to better recovery behavior.

- **Evidence anchors reviewed:** datasets p. 7 (B. Teleoperation Evaluation), p. 8 (C. Policy Evaluation), p. 7 (B. Teleoperation Evaluation), p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup), p. 8 (C. Policy Evaluation), metrics p. 7 (C. Policy Evaluation), p. 8 (C. Policy Evaluation), p. 8 (C. Policy Evaluation), p. 7 (B. Teleoperation Evaluation), p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup), baselines p. 7 (C. Policy Evaluation), p. 7 (B. Teleoperation Evaluation), p. 8 (C. Policy Evaluation), p. 8 (C. Policy Evaluation), p. 9 (C. Policy Evaluation), p. 9 (C. Policy Evaluation), results p. 8 (C. Policy Evaluation), p. 8 (C. Policy Evaluation), p. 7 (C. Policy Evaluation), p. 7 (B. Teleoperation Evaluation), p. 6 (A. Experimental Setup), p. 9 (C. Policy Evaluation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Our experiments show that our system allows users to ‘complete tasks with 64.7% higher task completion rate, 37.4% reduced completion time, and 83.3% improvement in the subjective ease of use ... (p. 7, B. Teleoperation Evaluation).
- **Metric evidence:** Our experiments show that our system allows users to ‘complete tasks with 64.7% higher task completion rate, 37.4% reduced completion time, and 83.3% improvement in the subjective ease of use ... (p. 7, B. Teleoperation Evaluation).
- **Baseline/ablation evidence:** ‘+ How does FACTR perform compared to baseline approaches that do not use force feedback and ones that use force feedback without FACTR? (p. 7, C. Policy Evaluation).
- **Failure/negative evidence:** While without the curriculum, the policy does not pay enough attention 10 force, and either fails to lift or balance the novel boxes. (p. 8, C. Policy Evaluation).
