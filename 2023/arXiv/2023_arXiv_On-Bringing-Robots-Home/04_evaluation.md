# Evaluation - On Bringing Robots Home

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (32 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2311.16098; PDF retrieval source: https://arxiv.org/pdf/2311.16098. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 1 (Figure/Table caption), p. 22 (Figure/Table caption), p. 21 (3 Experiments), p. 21 (3 Experiments), p. 12 (3 Experiments), p. 12 (3 Experiments)): Figure 1: We present Dobb·E, a simple framework to train robots, which is then field tested in homes across New York City. In under 30 mins of training per task, ...

## Evaluation Body Digest

- **p. 3 / 3 Experiments - extractive body cue:** 25 4.4 Robustifying Robot Hardware . . . . . . . . . . . . . . . . . . . . ...
- **p. 20 / 3 Experiments - extractive body cue:** Robot hardware limitations Our robot platform, Hello Robot Stretch RE1, was robust enough that we were able to run all the home experiments on a ...
- **p. 17 / 3 Experiments - extractive body cue:** We found that 6D pick and place tasks generally fail because they generally require robot motion in a variety of axes: like translations and rotations ...
- **p. 18 / 3 Experiments - extractive body cue:** Demo Robot run: Without Shadows Robot run: With Shadows Frame Step 0 5 10 15 20 25 30 20 50 70 90 100 110 125 ...
- **p. 21 / 3 Experiments - extractive body cue:** The failure modes for tasks without depth are generally concentrated around cases where the robot end-effector (and thus the camera) is very close to some ...
- **p. 12 / 3 Experiments - extractive body cue:** On these 109 tasks, the robot gets an 81% success rate, and can complete 102 tasks with at least even odds.
- **p. 12 / 3 Experiments - extractive body cue:** Note that none of our experiments overlapped with the environments on which our HoNY dataset was collected to ensure that the experimental environments are novel.
- **p. 15 / 3 Experiments - extractive body cue:** Turning on light switch Figure 10: A small subset of 8 robot rollouts from the 109 tasks that we tried in homes.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mobile base와 one/two-arm manipulation environment.
- **Input boundary:** egocentric RGB-D, language/task goal, base-arm proprioception.
- **Output/decision under evaluation:** base motion plus arm/gripper action.
- **Primary target:** long-horizon task success, reachability, collision과 recovery.
- **Detected evaluation headings:** 3 Experiments (p. 2); 3 Experiments (p. 12).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1: We present Dobb·E, a simple framework to train robots, which is then field tested in homes across New York City. In under ... | p. 1 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 23: Barplot showing the distribution of task success rates in our two setups, one using depth and another not using depth. In most ... | p. 22 (Figure/Table caption) |
| 3 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | As we see in Figure 22, adding more demonstrations always improves the performance of our system. | p. 21 (3 Experiments) |
| 3 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | This shows us that on the average case, if our model can somewhat solve a task, we can improve the performance of the system ... | p. 21 (3 Experiments) |
| 3 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | On these 109 tasks, the robot gets an 81% success rate, and can complete 102 tasks with at least even odds. | p. 12 (3 Experiments) |

## Dataset / Benchmark Role

- **p. 3 / 3 Experiments - extractive body cue:** 25 4.4 Robustifying Robot Hardware . . . . . . . . . . . . . . . . . . . . ...
- **p. 20 / 3 Experiments - extractive body cue:** Robot hardware limitations Our robot platform, Hello Robot Stretch RE1, was robust enough that we were able to run all the home experiments on a ...
- **p. 17 / 3 Experiments - extractive body cue:** We found that 6D pick and place tasks generally fail because they generally require robot motion in a variety of axes: like translations and rotations ...
- **p. 18 / 3 Experiments - extractive body cue:** Demo Robot run: Without Shadows Robot run: With Shadows Frame Step 0 5 10 15 20 25 30 20 50 70 90 100 110 125 ...
- **p. 21 / 3 Experiments - extractive body cue:** The failure modes for tasks without depth are generally concentrated around cases where the robot end-effector (and thus the camera) is very close to some ...
- **p. 12 / 3 Experiments - extractive body cue:** On these 109 tasks, the robot gets an 81% success rate, and can complete 102 tasks with at least even odds.
- **p. 12 / 3 Experiments - extractive body cue:** Note that none of our experiments overlapped with the environments on which our HoNY dataset was collected to ensure that the experimental environments are novel.
- **p. 15 / 3 Experiments - extractive body cue:** Turning on light switch Figure 10: A small subset of 8 robot rollouts from the 109 tasks that we tried in homes.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: We present Dobb·E, a simple framework to train robots, which is then field tested in homes across New York City. In under 30 ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: (A) We design a new imitation learning framework, starting with a data collection tool. (B) Using this data collection tool, users can easily ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: We ran experiments in a total of 10 homes near the New York City area, and successfully completed 102 out of 109 tasks ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Photographs of our designed hardware, including the (A) Stick and the (B) identical iPhone mount for Hello Robot: Stretch wrist. From the iPhone's ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Subsample of 45 frames from Homes of New York dataset, collected using our Stick in 22 homes. Camera Mounts We create and use ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 6: Breakdown of Homes of New York dataset by task: on the left, the statistics is shown by number of demonstrations, and on the ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 7: Breakdown of our collected dataset by homes. On the left, the statistics are shown by number of demonstrations, and on the right, the ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 1: While previous datasets focused on the number of manipulation trajectories, we instead focus on diverse scenes and environments. As a result, we end ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 25 4.4 Robustifying Robot Hardware . . . . . . . . . . . . . . . . . . . ... | embodiment, simulator version and control stack | p. 3 (3 Experiments), p. 20 (3 Experiments) |
| Task/environment | Robot hardware limitations Our robot platform, Hello Robot Stretch RE1, was robust enough that we were able to run all the home experiments on ... | reset, timeout, object/scene variation | p. 20 (3 Experiments), p. 17 (3 Experiments) |
| Observation/sensor | egocentric RGB-D, language/task goal, base-arm proprioception | calibration, preprocessing, privileged input | p. 6 (C D), p. 6 (C D) |
| Output/decision | base motion plus arm/gripper action | action frame, controller and termination | p. 7 (C D), p. 7 (C D) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 0 20 40 60 80 100 Success rate (%) Air-fryer closing Cushion flipping Door closing Drawer closing Chair pulling Pulling from shelf Bag pickup ... | definition/direction/unit from same section | p. 16 (3 Experiments) |
| We see that Dobb·E can chain subtasks, although the errors can accumulate and make overall task success rate low. section, we show the difference ... | definition/direction/unit from same section | p. 23 (3 Experiments) |
| Figure 21: Comparison between different representation models at a set of tasks done in (a) our lab and (b) in a real home enviroment. ... | definition/direction/unit from same section | p. 21 (Figure/Table caption) |
| On these 109 tasks, the robot gets an 81% success rate, and can complete 102 tasks with at least even odds. | definition/direction/unit from same section | p. 12 (3 Experiments) |
| 3.1 List of Tasks in Homes In Table 2 we provide an overview of the 109 tasks that we attempted in the 10 homes, ... | definition/direction/unit from same section | p. 12 (3 Experiments) |
| 0 5 10 15 20 25 30 Count Rotation? = No Rotation? = Yaw 0 20 40 60 80 100 Success rate (%) 0 ... | definition/direction/unit from same section | p. 16 (3 Experiments) |
| We find that the type of movement affects the success rate of the tasks. | definition/direction/unit from same section | p. 17 (3 Experiments) |
| (b) Correlation analysis between time taken to demonstrate a task and the success rate of the associated robot policy. | definition/direction/unit from same section | p. 17 (3 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Alongside these household experiments, we also set up a "home" area in our lab, with a benchmark suite with 10 tasks that we use ... | comparison identity and matched condition | p. 12 (3 Experiments) |
| There are clear patterns in how easy or difficult different tasks may be, compared to each other. | comparison identity and matched condition | p. 17 (3 Experiments) |
| Moreover, the distribution of successes for tasks which require 6D motion is the flattest, which shows that tasks requiring full 6D motions are harder ... | comparison identity and matched condition | p. 17 (3 Experiments) |
| As we can see, while VC1 is closer in performance to our model compared to IN-1K, R3M and MVP, it under-performs our model in ... | comparison identity and matched condition | p. 21 (3 Experiments) |
| In most settings, using depth outperforms not using depth. | comparison identity and matched condition | p. 22 (3 Experiments) |
| Rollout With Shadows Demo Without Shadows Figure 15: First person view from the iPhone from the (top row) Stick during demonstration collection and (bottom ... | comparison identity and matched condition | p. 18 (3 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The failure modes for tasks without depth are generally concentrated around cases where the robot end-effector (and thus the camera) is very close to ... | component/input/data sensitivity | p. 21 (3 Experiments) |
| These ablation experiments evaluate different components of our system and how they contribute to our performance. | component/input/data sensitivity | p. 21 (3 Experiments) |
| Alongside these household experiments, we also set up a "home" area in our lab, with a benchmark suite with 10 tasks that we use ... | component/input/data sensitivity | p. 12 (3 Experiments) |
| Rollout With Shadows Demo Without Shadows Figure 15: First person view from the iPhone from the (top row) Stick during demonstration collection and (bottom ... | component/input/data sensitivity | p. 18 (3 Experiments) |
| Demo Robot run: Without Shadows Robot run: With Shadows Frame Step 0 5 10 15 20 25 30 20 50 70 90 100 110 ... | component/input/data sensitivity | p. 18 (3 Experiments) |
| Rollout With Depth Rollout Without Depth Depth Image Demo Figure 18: Opening an outward facing window blind (top row) both without depth (second row) ... | component/input/data sensitivity | p. 19 (3 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work we present Dobb·E, a framework for teaching robots in homes by embodying three core principles: efficiency, safety, and user comfort. | Figure 1: We present Dobb·E, a simple framework to train robots, which is then field tested in homes across New York City. In under ... | PDF body cue; verify exact table/figure and matched conditions | p. 1 (Figure/Table caption), p. 22 (Figure/Table caption), p. 21 (3 Experiments), p. 21 (3 Experiments), p. 12 (3 Experiments), p. 12 (3 Experiments) |
| Primary metric/result | Figure 23: Barplot showing the distribution of task success rates in our two setups, one using depth and another not using depth. In most ... | numeric claim only at cited anchor | p. 22 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 12 / 3 Experiments - extractive body cue:** We experimentally validated our setup by evaluating it across 10 households in the New York and New Jersey area on a total of 109 tasks.
- **p. 12 / 3 Experiments - extractive body cue:** On these 109 tasks, the robot gets an 81% success rate, and can complete 102 tasks with at least even odds.
- **p. 12 / 3 Experiments - extractive body cue:** Alongside these household experiments, we also set up a "home" area in our lab, with a benchmark suite with 10 tasks that we use to ...
- **p. 12 / 3 Experiments - extractive body cue:** 3.1 List of Tasks in Homes In Table 2 we provide an overview of the 109 tasks that we attempted in the 10 homes, as ...
- **p. 15 / 3 Experiments - extractive body cue:** Turning on light switch Figure 10: A small subset of 8 robot rollouts from the 109 tasks that we tried in homes.
- **p. 16 / 3 Experiments - extractive body cue:** The X-axis shows the number of successes out of 10 rollouts, and the Y-axis shows number of tasks with the corresponding number of success.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 20: First-person POV rollouts of Home 3 Pick and Place comparing (top) a policy trained on demos where the object is picked and ... | p. 20 (Figure/Table caption) |
| body limitation/failure cue | Figure 18: Opening an outward facing window blind (top row) both without depth (second row) and with depth (third row). The depth values (bottom ... | p. 19 (Figure/Table caption) |
| body limitation/failure cue | We discuss the failure cases further in Section 3.3. | p. 17 (3 Experiments) |
| body limitation/failure cue | Once we turned on an overhead light for even lighting, there were no more failures. | p. 17 (3 Experiments) |
| body limitation/failure cue | The failure modes for tasks without depth are generally concentrated around cases where the robot end-effector (and thus the camera) is very close to ... | p. 21 (3 Experiments) |
| body limitation/failure cue | This failure mode points to the need of better designed, less bare-boned robot grippers for household tasks. | p. 23 (3 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Robot hardware limitations Our robot platform, Hello Robot Stretch RE1, was robust enough that we were able to run all the home experiments on ... | p. 20 (3 Experiments) |
| 25 4.4 Robustifying Robot Hardware . . . . . . . . . . . . . . . . . . . ... | p. 3 (3 Experiments) |
| Alongside these household experiments, we also set up a "home" area in our lab, with a benchmark suite with 10 tasks that we use ... | p. 12 (3 Experiments) |
| Demo Robot run: Without Shadows Robot run: With Shadows Frame Step 0 5 10 15 20 25 30 20 50 70 90 100 110 ... | p. 18 (3 Experiments) |
| A secondary problem with reflective surfaces like mirrors is that we collect demonstrations using the Stick but run the trained policies on the robot. | p. 19 (3 Experiments) |
| However, there are certain hardware limitations that caused several of our tasks to fail. | p. 20 (3 Experiments) |
| 3.4 Ablations We created a benchmark set of tasks in our lab, with a setup that closely resembles a home, to be able to ... | p. 21 (3 Experiments) |
| The hardware odometry from the iPhone is much more robust, and thus the actions extracted from it are also reliable regardless of the camera ... | p. 23 (3 Experiments) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 20 / Figure/Table caption - extractive body cue:** Figure 20: First-person POV rollouts of Home 3 Pick and Place comparing (top) a policy trained on demos where the object is picked and placed ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 18: Opening an outward facing window blind (top row) both without depth (second row) and with depth (third row). The depth values (bottom row) ...
- **p. 17 / 3 Experiments - extractive body cue:** We discuss the failure cases further in Section 3.3.
- **p. 17 / 3 Experiments - extractive body cue:** Once we turned on an overhead light for even lighting, there were no more failures.
- **p. 21 / 3 Experiments - extractive body cue:** The failure modes for tasks without depth are generally concentrated around cases where the robot end-effector (and thus the camera) is very close to some ...
- **p. 23 / 3 Experiments - extractive body cue:** This failure mode points to the need of better designed, less bare-boned robot grippers for household tasks.

- **Evidence anchors reviewed:** datasets p. 3 (3 Experiments), p. 20 (3 Experiments), p. 17 (3 Experiments), p. 18 (3 Experiments), p. 21 (3 Experiments), p. 12 (3 Experiments), metrics p. 16 (3 Experiments), p. 23 (3 Experiments), p. 21 (Figure/Table caption), p. 12 (3 Experiments), p. 12 (3 Experiments), p. 16 (3 Experiments), baselines p. 12 (3 Experiments), p. 17 (3 Experiments), p. 17 (3 Experiments), p. 21 (3 Experiments), p. 22 (3 Experiments), p. 18 (3 Experiments), results p. 1 (Figure/Table caption), p. 22 (Figure/Table caption), p. 21 (3 Experiments), p. 21 (3 Experiments), p. 12 (3 Experiments), p. 12 (3 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
