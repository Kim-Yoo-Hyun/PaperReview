# Evaluation - Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p045.html; PDF retrieval source: https://arxiv.org/pdf/2402.10329. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (V. CAPABILITY EXPERIMENTS), p. 7 (V. CAPABILITY EXPERIMENTS), p. 8 (V. CAPABILITY EXPERIMENTS), p. 8 (V. CAPABILITY EXPERIMENTS), p. 11 (Figure/Table caption), p. 9 (V. CAPABILITY EXPERIMENTS)): This baseline only achieves 11/20 = 55% success rate.

## Evaluation Body Digest

- **p. 6 / IV. EVALUATIONS - extractive body cue:** To access capability and generalization, we evaluate UMI on 4 real-world robotic tasks across both narrow domain and in-the-wild environments, shown in Fig.
- **p. 6 / V. CAPABILITY EXPERIMENTS - extractive body cue:** For capability experiments, all tasks are evaluated in the same environment as data collection but with randomized robot and object initial states.
- **p. 7 / V. CAPABILITY EXPERIMENTS - extractive body cue:** This task is evaluated in both narrow-domain and unseen environments as well as two robot embodiments.
- **p. 8 / V. CAPABILITY EXPERIMENTS - extractive body cue:** Performance: We collected 280 demonstration episodes for this task, with mixed multi and single-object picking and tossing.
- **p. 7 / V. CAPABILITY EXPERIMENTS - extractive body cue:** Performance The training dataset contains 305 episodes collected by 2 demonstrators, evaluation includes 20 test cases, with the testing initial state distribution shown in Fig.
- **p. 8 / V. CAPABILITY EXPERIMENTS - extractive body cue:** Dynamic Tossing Task The robot is tasked to sort 6 objects from the YCB object set [5] randomly placed on a table by tossing them ...
- **p. 10 / V. CAPABILITY EXPERIMENTS - extractive body cue:** We test the policy robustness with different inference time perturbations such as moving robot base, novel objects, different lighting conditions, and adding different and more ...
- **p. 9 / V. CAPABILITY EXPERIMENTS - extractive body cue:** In addition, the misalignment between the gripper and robot action (due to their different execution latency) leads to suboptimal object release during tossing.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** IV. EVALUATIONS (p. 6); V. CAPABILITY EXPERIMENTS (p. 6); VI. IN-THE-WILD GENERALIZATION EXPERIMENTS (p. 10).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. CAPABILITY EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | This baseline only achieves 11/20 = 55% success rate. | p. 7 (V. CAPABILITY EXPERIMENTS) |
| V. CAPABILITY EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | This experiment achieves 18/20 = 90% success rate, with the 2 failure cases being joint limit violations, which could have been avoided if we ... | p. 7 (V. CAPABILITY EXPERIMENTS) |
| V. CAPABILITY EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The delta action baseline achieves 16/20 = 80% success rate. | p. 8 (V. CAPABILITY EXPERIMENTS) |
| V. CAPABILITY EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our policy (with inference time latency matching) achieves 105/120 = 87.5% success rate, counted by the number of objects successfully tossed to their corresponding ... | p. 8 (V. CAPABILITY EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 12: SLAM Accuracy. We evaluate the SLAM accuracy with a MoCap benchmark including 7 single-gripper tasks and 7 bimanual tasks. Overall, we can ... | p. 11 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / IV. EVALUATIONS - extractive body cue:** To access capability and generalization, we evaluate UMI on 4 real-world robotic tasks across both narrow domain and in-the-wild environments, shown in Fig.
- **p. 6 / V. CAPABILITY EXPERIMENTS - extractive body cue:** For capability experiments, all tasks are evaluated in the same environment as data collection but with randomized robot and object initial states.
- **p. 7 / V. CAPABILITY EXPERIMENTS - extractive body cue:** This task is evaluated in both narrow-domain and unseen environments as well as two robot embodiments.
- **p. 8 / V. CAPABILITY EXPERIMENTS - extractive body cue:** Performance: We collected 280 demonstration episodes for this task, with mixed multi and single-object picking and tossing.
- **p. 7 / V. CAPABILITY EXPERIMENTS - extractive body cue:** Performance The training dataset contains 305 episodes collected by 2 demonstrators, evaluation includes 20 test cases, with the testing initial state distribution shown in Fig.
- **p. 8 / V. CAPABILITY EXPERIMENTS - extractive body cue:** Dynamic Tossing Task The robot is tasked to sort 6 objects from the YCB object set [5] randomly placed on a table by tossing them ...
- **p. 10 / V. CAPABILITY EXPERIMENTS - extractive body cue:** We test the policy robustness with different inference time perturbations such as moving robot base, novel objects, different lighting conditions, and adding different and more ...
- **p. 9 / V. CAPABILITY EXPERIMENTS - extractive body cue:** In addition, the misalignment between the gripper and robot action (due to their different execution latency) leads to suboptimal object release during tossing.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Universal Manipulation Interface (UMI) is a portable, intuitive, low-cost data collection and policy learning framework. This framework allows us to transfer diverse human ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: UMI Demonstration Interface Design. Left: Hand-held grippers for data collection, with a GoPro as the only sensor and recording device. Middle: Image from ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: Fisheye vs Rectilinear (a) UMI policies use raw Fisheye image as observation. (b) Rectifying a large 155° FoV image to the pin-hole model ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: UMI Side Mirrors. The ultra-wide-angle camera coupled with strategically positioned mirrors, facilitates implicit stereo depth estimation. (a): The view through each mirror effectively ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5: UMI Policy Interface Design. (b) UMI policy takes in a sequence of synchronized observations (RGB image, relative EE pose, and gripper width) and ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6: Relative Trajectory as Action Representation. Relative trajectory, used by UMI, is a sequence of end-effector (EE) poses relative to the same current EE ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Policy Rollouts. We test UMI on a variety of challenging real-world tasks. Cup arrangement tests UMI's ability to learn both prehensile and non-prehensile ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: Narrow-domain Evaluation Results. (a) Initial states for all evaluation episodes overlayed together. For each task, all methods start with the same set of ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To access capability and generalization, we evaluate UMI on 4 real-world robotic tasks across both narrow domain and in-the-wild environments, shown in Fig. | embodiment, simulator version and control stack | p. 6 (IV. EVALUATIONS), p. 6 (V. CAPABILITY EXPERIMENTS) |
| Task/environment | For capability experiments, all tasks are evaluated in the same environment as data collection but with randomized robot and object initial states. | reset, timeout, object/scene variation | p. 6 (V. CAPABILITY EXPERIMENTS), p. 7 (V. CAPABILITY EXPERIMENTS) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 3 (III. METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| (c) Success rate over 20 evaluation episodes, best performance for each column are bolded. | definition/direction/unit from same section | p. 8 (V. CAPABILITY EXPERIMENTS) |
| Fig. 12: SLAM Accuracy. We evaluate the SLAM accuracy with a MoCap benchmark including 7 single-gripper tasks and 7 bimanual tasks. Overall, we can ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |
| This baseline only achieves 11/20 = 55% success rate. | definition/direction/unit from same section | p. 7 (V. CAPABILITY EXPERIMENTS) |
| This experiment achieves 18/20 = 90% success rate, with the 2 failure cases being joint limit violations, which could have been avoided if we ... | definition/direction/unit from same section | p. 7 (V. CAPABILITY EXPERIMENTS) |
| The delta action baseline achieves 16/20 = 80% success rate. | definition/direction/unit from same section | p. 8 (V. CAPABILITY EXPERIMENTS) |
| As a result, the final success rate decreased to 69/120 = 57.5%. | definition/direction/unit from same section | p. 9 (V. CAPABILITY EXPERIMENTS) |
| Cafe Table Water Fountain Success Rate CLIP ViT finetune with narrow-domain Data 0 / 10 0 / 10 0.0 In-the-wild Data Training Cup 16 ... | definition/direction/unit from same section | p. 9 (V. CAPABILITY EXPERIMENTS) |
| What's the accuracy of the SLAM system? | definition/direction/unit from same section | p. 6 (IV. EVALUATIONS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| (b) Typical failure mode of the baseline/ablation policy. | comparison identity and matched condition | p. 8 (V. CAPABILITY EXPERIMENTS) |
| This baseline only achieves 11/20 = 55% success rate. | comparison identity and matched condition | p. 7 (V. CAPABILITY EXPERIMENTS) |
| Beyond the expected failure mode where the cup is outside of camera view, we found this baseline policy to perform surprisingly poor even if ... | comparison identity and matched condition | p. 7 (V. CAPABILITY EXPERIMENTS) |
| The delta action baseline achieves 16/20 = 80% success rate. | comparison identity and matched condition | p. 8 (V. CAPABILITY EXPERIMENTS) |
| The most salient failure case is when the two arms lift the bottom hem of the shirt, where the baseline policy often misses one ... | comparison identity and matched condition | p. 9 (V. CAPABILITY EXPERIMENTS) |
| 9(b), the robot with the baseline policy doesn't even move toward the cup. | comparison identity and matched condition | p. 10 (VI. IN-THE-WILD GENERALIZATION EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Effect of side mirrors [HD3]: To our surprise, directly providing mirror images decreases the performance from 18/20 = 90% (no mirror) to 17/20 = ... | component/input/data sensitivity | p. 8 (V. CAPABILITY EXPERIMENTS) |
| The next paragraphs will discuss our ablation studies around our key design decisions. | component/input/data sensitivity | p. 7 (V. CAPABILITY EXPERIMENTS) |
| … Toss lego to rectangle bin Grasp lego block Toss orange to round bin Init Init Reorient handle to the right Grasp espresso cup ... | component/input/data sensitivity | p. 7 (V. CAPABILITY EXPERIMENTS) |
| (b) Typical failure mode of the baseline/ablation policy. | component/input/data sensitivity | p. 8 (V. CAPABILITY EXPERIMENTS) |
| No relative inter-gripper proprioception [PD2.3]: Without inter-gripper proprioception information (during both training and eval), the coordination between the two arms becomes significantly worse. | component/input/data sensitivity | p. 9 (V. CAPABILITY EXPERIMENTS) |
| Dish Washing Task The robot needs to execute 7 steps of sequentially dependent actions (turn on faucet, grasp plate, pick up sponge, wash and ... | component/input/data sensitivity | p. 9 (V. CAPABILITY EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| 2), we show that UMI is capable of achieving a wide range of manipulation tasks that involve dynamic, bimanual, precise and long-horizon actions by ... | This baseline only achieves 11/20 = 55% success rate. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (V. CAPABILITY EXPERIMENTS), p. 7 (V. CAPABILITY EXPERIMENTS), p. 8 (V. CAPABILITY EXPERIMENTS), p. 8 (V. CAPABILITY EXPERIMENTS), p. 11 (Figure/Table caption), p. 9 (V. CAPABILITY EXPERIMENTS) |
| Primary metric/result | This experiment achieves 18/20 = 90% success rate, with the 2 failure cases being joint limit violations, which could have been avoided if we ... | numeric claim only at cited anchor | p. 7 (V. CAPABILITY EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / V. CAPABILITY EXPERIMENTS - extractive body cue:** … Toss lego to rectangle bin Grasp lego block Toss orange to round bin Init Init Reorient handle to the right Grasp espresso cup Final: ...
- **p. 7 / V. CAPABILITY EXPERIMENTS - extractive body cue:** Performance The training dataset contains 305 episodes collected by 2 demonstrators, evaluation includes 20 test cases, with the testing initial state distribution shown in Fig.
- **p. 8 / V. CAPABILITY EXPERIMENTS - extractive body cue:** Dynamic Tossing Task The robot is tasked to sort 6 objects from the YCB object set [5] randomly placed on a table by tossing them ...
- **p. 9 / V. CAPABILITY EXPERIMENTS - extractive body cue:** Bimanual Cloth Folding Task Two robot arms need to coordinate and fold the sweater's sleeves inward, fold up the bottom hem, rotate 90 degrees, and ...
- **p. 9 / V. CAPABILITY EXPERIMENTS - extractive body cue:** Dish Washing Task The robot needs to execute 7 steps of sequentially dependent actions (turn on faucet, grasp plate, pick up sponge, wash and wipe ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | While UMI demonstrates policy efficacy across a wide range of tasks and scenarios, a few limitations remain. | p. 11 (VIII. LIMITATIONS AND FUTURE WORKS) |
| body limitation/failure cue | Beyond the expected failure mode where the cup is outside of camera view, we found this baseline policy to perform surprisingly poor even if ... | p. 7 (V. CAPABILITY EXPERIMENTS) |
| body limitation/failure cue | This experiment achieves 18/20 = 90% success rate, with the 2 failure cases being joint limit violations, which could have been avoided if we ... | p. 7 (V. CAPABILITY EXPERIMENTS) |
| body limitation/failure cue | (b) Typical failure mode of the baseline/ablation policy. | p. 8 (V. CAPABILITY EXPERIMENTS) |
| body limitation/failure cue | The red arrow indicates failure behavior, green arrow indicates desired behavior. | p. 8 (V. CAPABILITY EXPERIMENTS) |
| body limitation/failure cue | The most salient failure case is when the two arms lift the bottom hem of the shirt, where the baseline policy often misses one ... | p. 9 (V. CAPABILITY EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Our policy (with inference time latency matching) achieves 105/120 = 87.5% success rate, counted by the number of objects successfully tossed to their corresponding ... | p. 8 (V. CAPABILITY EXPERIMENTS) |
| We test the policy robustness with different inference time perturbations such as moving robot base, novel objects, different lighting conditions, and adding different and ... | p. 10 (V. CAPABILITY EXPERIMENTS) |
| Cross-robot generalization: To demonstrate UMI's crossembodiment generality, we also deployed the same policy checkpoint on a Franka Emika FR2 robot, shown in Fig. | p. 7 (V. CAPABILITY EXPERIMENTS) |
| To compute absolute actions in the robot base frame, we calibrate both SLAM coordinates and the robot with respect to the same fiducial markers ... | p. 8 (V. CAPABILITY EXPERIMENTS) |
| No CLIP-pretrained ViT vision encoder. | p. 9 (V. CAPABILITY EXPERIMENTS) |
| Dish Washing Task The robot needs to execute 7 steps of sequentially dependent actions (turn on faucet, grasp plate, pick up sponge, wash and ... | p. 9 (V. CAPABILITY EXPERIMENTS) |
| The following sections describe how we enable the above goals through our hardware and policy interface design. | p. 3 (III. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 11 / VIII. LIMITATIONS AND FUTURE WORKS - extractive body cue:** While UMI demonstrates policy efficacy across a wide range of tasks and scenarios, a few limitations remain.
- **p. 7 / V. CAPABILITY EXPERIMENTS - extractive body cue:** Beyond the expected failure mode where the cup is outside of camera view, we found this baseline policy to perform surprisingly poor even if the ...
- **p. 7 / V. CAPABILITY EXPERIMENTS - extractive body cue:** This experiment achieves 18/20 = 90% success rate, with the 2 failure cases being joint limit violations, which could have been avoided if we had ...
- **p. 8 / V. CAPABILITY EXPERIMENTS - extractive body cue:** (b) Typical failure mode of the baseline/ablation policy.
- **p. 8 / V. CAPABILITY EXPERIMENTS - extractive body cue:** The red arrow indicates failure behavior, green arrow indicates desired behavior.
- **p. 9 / V. CAPABILITY EXPERIMENTS - extractive body cue:** The most salient failure case is when the two arms lift the bottom hem of the shirt, where the baseline policy often misses one of ...

- **Evidence anchors reviewed:** datasets p. 6 (IV. EVALUATIONS), p. 6 (V. CAPABILITY EXPERIMENTS), p. 7 (V. CAPABILITY EXPERIMENTS), p. 8 (V. CAPABILITY EXPERIMENTS), p. 7 (V. CAPABILITY EXPERIMENTS), p. 8 (V. CAPABILITY EXPERIMENTS), metrics p. 8 (V. CAPABILITY EXPERIMENTS), p. 11 (Figure/Table caption), p. 7 (V. CAPABILITY EXPERIMENTS), p. 7 (V. CAPABILITY EXPERIMENTS), p. 8 (V. CAPABILITY EXPERIMENTS), p. 9 (V. CAPABILITY EXPERIMENTS), baselines p. 8 (V. CAPABILITY EXPERIMENTS), p. 7 (V. CAPABILITY EXPERIMENTS), p. 7 (V. CAPABILITY EXPERIMENTS), p. 8 (V. CAPABILITY EXPERIMENTS), p. 9 (V. CAPABILITY EXPERIMENTS), p. 10 (VI. IN-THE-WILD GENERALIZATION EXPERIMENTS), results p. 7 (V. CAPABILITY EXPERIMENTS), p. 7 (V. CAPABILITY EXPERIMENTS), p. 8 (V. CAPABILITY EXPERIMENTS), p. 8 (V. CAPABILITY EXPERIMENTS), p. 11 (Figure/Table caption), p. 9 (V. CAPABILITY EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Fig. 8: Narrow-domain Evaluation Results. (a) Initial states for all evaluation episodes overlayed together. For each task, all methods start with the same set of initial states, matched manually with ... (p. 8, Figure/Table caption).
- **Metric evidence:** This baseline only achieves 11/20 = 55% success rate. (p. 7, V. CAPABILITY EXPERIMENTS).
- **Baseline/ablation evidence:** (b) Typical failure mode of the baseline/ablation policy. (p. 8, V. CAPABILITY EXPERIMENTS).
- **Failure/negative evidence:** This experiment achieves 18/20 = 90% success rate, with the 2 failure cases being joint limit violations, which could have been avoided if we had mounted the FR2 robot at ... (p. 7, V. CAPABILITY EXPERIMENTS).
