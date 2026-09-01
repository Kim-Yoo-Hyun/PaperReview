# Evaluation - RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p028.html; PDF retrieval source: https://arxiv.org/pdf/2412.09858. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.2. RLDG vs. Conventional Fine-tuning), p. 7 (Figure/Table caption), p. 6 (4.2. RLDG vs. Conventional Fine-tuning), p. 6 (4.2. RLDG vs. Conventional Fine-tuning), p. 9 (5.1. Is RL data better because of better action), p. 2 (Figure/Table caption)): When evaluated on seen (VGA) and unseen (Type C) Connector Insertion tasks, RLDG shows superior sample efficiency, requiring significantly fewer demonstrations to achieve perfect success rate in both scenarios while ...

## Evaluation Body Digest

- **p. 6 / 4.1. Experimental Setup and Tasks - extractive body cue:** We also use the single object insertion task of FMB (Luo et al., 2024c), a common and reproducible benchmark for comparing robotic manipulation methods.
- **p. 5 / 4.1. Experimental Setup and Tasks - extractive body cue:** We also test our method on a pickand-place task, where the robot grasps an object from a randomized location and places it in a bowl.
- **p. 6 / 4.1. Experimental Setup and Tasks - extractive body cue:** (C) FMB Insertion involves inserting a pre-grasped object in a moving board while (D) FMB Assembly starts with the object on the table and involves ...
- **p. 8 / 4.3. Generalization of RLDG vs. Original RL - extractive body cue:** Generalist robot policies trained on RL-generated data using RLDG consistently achieve higher performance across all tasks compared to conventional fine-tuning methods using human demonstrations.
- **p. 8 / 4.3. Generalization of RLDG vs. Original RL - extractive body cue:** Additionally, the multi-task capabilities of OpenVLA and Octo allowed fine-tuning on multiple connector data in the Connector Insertion task, achieving 73/80 and 50/80, respectively, when ...
- **p. 5 / 4.1. Experimental Setup and Tasks - extractive body cue:** We evaluate RLDG on four real-world manipulation tasks that present distinct challenges.
- **p. 7 / 4.2. RLDG vs. Conventional Fine-tuning - extractive body cue:** For the VGA connector, OpenVLA with RLDG achieved a 100% success rate with just 45 RL episodes, compared to 300 required from human demonstrations to ...
- **p. 7 / 4.2. RLDG vs. Conventional Fine-tuning - extractive body cue:** RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning Figure 4: Success rate comparison of OpenVLA and Octo policies fine-tuned with RLDG versus conventional methods using ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** 4. Experiment and Results (p. 5); 4.1. Experimental Setup and Tasks (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. RLDG vs. Conventional Fine-tuning | EMPIRICAL / REAL-ROBOT OR HARDWARE | When evaluated on seen (VGA) and unseen (Type C) Connector Insertion tasks, RLDG shows superior sample efficiency, requiring significantly fewer demonstrations to achieve perfect ... | p. 7 (4.2. RLDG vs. Conventional Fine-tuning) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4: Success rate comparison of OpenVLA and Octo policies fine-tuned with RLDG versus conventional methods using human demonstrations. Both generalists trained with RLDG ... | p. 7 (Figure/Table caption) |
| 4.2. RLDG vs. Conventional Fine-tuning | EMPIRICAL / REAL-ROBOT OR HARDWARE | The benefit of RLDG is equally pronounced for Octo, where it improved the success rate by 10% and 6 | p. 6 (4.2. RLDG vs. Conventional Fine-tuning) |
| 4.2. RLDG vs. Conventional Fine-tuning | EMPIRICAL / REAL-ROBOT OR HARDWARE | On each task, both OpenVLA and Octo fine-tuned with RL-generated data consistently achieved higher success rates than their counterparts trained with human demonstrations, in ... | p. 6 (4.2. RLDG vs. Conventional Fine-tuning) |
| 5.1. Is RL data better because of better action | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Figure 7, mixing human states and RL actions yields a better fine-tuning success rate than using fully human data (more than ... | p. 9 (5.1. Is RL data better because of better action) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experimental Setup and Tasks - extractive body cue:** We also use the single object insertion task of FMB (Luo et al., 2024c), a common and reproducible benchmark for comparing robotic manipulation methods.
- **p. 5 / 4.1. Experimental Setup and Tasks - extractive body cue:** We also test our method on a pickand-place task, where the robot grasps an object from a randomized location and places it in a bowl.
- **p. 6 / 4.1. Experimental Setup and Tasks - extractive body cue:** (C) FMB Insertion involves inserting a pre-grasped object in a moving board while (D) FMB Assembly starts with the object on the table and involves ...
- **p. 8 / 4.3. Generalization of RLDG vs. Original RL - extractive body cue:** Generalist robot policies trained on RL-generated data using RLDG consistently achieve higher performance across all tasks compared to conventional fine-tuning methods using human demonstrations.
- **p. 8 / 4.3. Generalization of RLDG vs. Original RL - extractive body cue:** Additionally, the multi-task capabilities of OpenVLA and Octo allowed fine-tuning on multiple connector data in the Connector Insertion task, achieving 73/80 and 50/80, respectively, when ...
- **p. 5 / 4.1. Experimental Setup and Tasks - extractive body cue:** We evaluate RLDG on four real-world manipulation tasks that present distinct challenges.
- **p. 7 / 4.2. RLDG vs. Conventional Fine-tuning - extractive body cue:** For the VGA connector, OpenVLA with RLDG achieved a 100% success rate with just 45 RL episodes, compared to 300 required from human demonstrations to ...
- **p. 7 / 4.2. RLDG vs. Conventional Fine-tuning - extractive body cue:** RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning Figure 4: Success rate comparison of OpenVLA and Octo policies fine-tuned with RLDG versus conventional methods using ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: RLDG improves generalist robot policies like OpenVLA and Octo by training with specialist RL policies and using them to generate high-quality fine-tuning datasets. ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 2. The arm tracks end-effector commands with a 1kHz low-level impedance controller. Data col- lection, RL, and Octo policies command actions at 10Hz, while ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: We use a Franka Emika Panda arm with a par- allel jaw gripper teleoperated by a 3Dconnexion Space- Mouse device. There is a ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Illustrations of tasks used to evaluate RLDG. (A) Precise Connector Insertion includes three training objects and four unseen test objects for evaluating policy ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Success rate comparison of OpenVLA and Octo policies fine-tuned with RLDG versus conventional methods using human demonstrations. Both generalists trained with RLDG consistently ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Success rate of OpenVLA policies fine-tuned on different sizes of RL-generated and human-collected
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Cycle time comparison between policies trained with RL data versus human demonstrations. N/A for RL in FMB Assembly denotes policy not trained on ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7: Fine-tuning success rate on the FMB insertion task with different fine-tuning data sources and varied dataset sizes (from 25 trajectories to 300 trajectories). ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We also use the single object insertion task of FMB (Luo et al., 2024c), a common and reproducible benchmark for comparing robotic manipulation methods. | embodiment, simulator version and control stack | p. 6 (4.1. Experimental Setup and Tasks), p. 5 (4.1. Experimental Setup and Tasks) |
| Task/environment | We also test our method on a pickand-place task, where the robot grasps an object from a randomized location and places it in a ... | reset, timeout, object/scene variation | p. 5 (4.1. Experimental Setup and Tasks), p. 6 (4.1. Experimental Setup and Tasks) |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 4 (3.3. Generalist Policy Finetuning), p. 5 (3.3. Generalist Policy Finetuning) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 5 (3.3. Generalist Policy Finetuning), p. 4 (3.1. Online RL Training) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| When evaluated on seen (VGA) and unseen (Type C) Connector Insertion tasks, RLDG shows superior sample efficiency, requiring significantly fewer demonstrations to achieve perfect ... | definition/direction/unit from same section | p. 7 (4.2. RLDG vs. Conventional Fine-tuning) |
| We present the success rate of each policy and method in Fig. | definition/direction/unit from same section | p. 6 (4.2. RLDG vs. Conventional Fine-tuning) |
| The benefit of RLDG is equally pronounced for Octo, where it improved the success rate by 10% and 6 | definition/direction/unit from same section | p. 6 (4.2. RLDG vs. Conventional Fine-tuning) |
| 37%, respectively, although the overall success rate is lower than OpenVLA. | definition/direction/unit from same section | p. 7 (4.2. RLDG vs. Conventional Fine-tuning) |
| In contrast, OpenVLA and Octo with RLDG achieved 10/20 and 4/20 success rates respectively on the same task. | definition/direction/unit from same section | p. 8 (4.3. Generalization of RLDG vs. Original RL) |
| 4, the RL policy success rate quickly degraded from 20/20 for the training scenario to 1/20 for the unseen scenario of the Pick and ... | definition/direction/unit from same section | p. 8 (4.3. Generalization of RLDG vs. Original RL) |
| As shown in Figure 7, mixing human states and RL actions yields a better fine-tuning success rate than using fully human data (more than ... | definition/direction/unit from same section | p. 9 (5.1. Is RL data better because of better action) |
| Figure 1: RLDG improves generalist robot policies like OpenVLA and Octo by training with specialist RL policies and using them to generate high-quality fine-tuning ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| On the precise FMB Insertion and Connector Insertion tasks, where we anticipated the generalist to benefit the most from higher quality training data, OpenVLA ... | comparison identity and matched condition | p. 6 (4.2. RLDG vs. Conventional Fine-tuning) |
| For the VGA connector, OpenVLA with RLDG achieved a 100% success rate with just 45 RL episodes, compared to 300 required from human demonstrations ... | comparison identity and matched condition | p. 7 (4.2. RLDG vs. Conventional Fine-tuning) |
| Both generalists trained with RLDG consistently outperform their counterparts trained with the same number of successful expert human demonstrations in both training and unseen ... | comparison identity and matched condition | p. 7 (4.2. RLDG vs. Conventional Fine-tuning) |
| Compared to directly using the RL policies that generated the data, RLDG also demonstrated much greater generalization capabilities and robustness to unseen test scenarios. | comparison identity and matched condition | p. 8 (4.3. Generalization of RLDG vs. Original RL) |
| Generalist robot policies trained on RL-generated data using RLDG consistently achieve higher performance across all tasks compared to conventional fine-tuning methods using human demonstrations. | comparison identity and matched condition | p. 8 (4.3. Generalization of RLDG vs. Original RL) |
| We have shown that fine-tuning generalist policies with RL data yields superior performance compared to training on human data. | comparison identity and matched condition | p. 9 (4.3. Generalization of RLDG vs. Original RL) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To further investigate the effectiveness of RLDG, we conduct a scaling experiment studying the success rate of OpenVLA policies on a seen VGA connector ... | component/input/data sensitivity | p. 7 (4.2. RLDG vs. Conventional Fine-tuning) |
| Human demonstration policies often maintained contact pressure without necessary exploratory movements. | component/input/data sensitivity | p. 9 (5.1. Is RL data better because of better action) |
| For the generalist policies, we fine-tune only using the wrist camera image as input. | component/input/data sensitivity | p. 5 (4.1. Experimental Setup and Tasks) |
| For each task, we fine-tune OpenVLA and Octo on RL-generated data as described in Sec. | component/input/data sensitivity | p. 6 (4.2. RLDG vs. Conventional Fine-tuning) |
| In this section, we seek to answer Question 1 by comparing generalist policies fine-tuned using RLDG and standard generalist fine-tuning via imitation learning. | component/input/data sensitivity | p. 6 (4.2. RLDG vs. Conventional Fine-tuning) |
| These results strongly suggest that fine-tuning generalist policies using RLDG is more sample-efficient and leads to higher performance than human demonstrations for both in-distribution ... | component/input/data sensitivity | p. 7 (4.2. RLDG vs. Conventional Fine-tuning) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To tackle this challenge, we propose Reinforcement Learning Distilled Generalist (RLDG), a simple yet effective method that leverages reinforcement learning to generate high-quality training ... | When evaluated on seen (VGA) and unseen (Type C) Connector Insertion tasks, RLDG shows superior sample efficiency, requiring significantly fewer demonstrations to achieve perfect ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.2. RLDG vs. Conventional Fine-tuning), p. 7 (Figure/Table caption), p. 6 (4.2. RLDG vs. Conventional Fine-tuning), p. 6 (4.2. RLDG vs. Conventional Fine-tuning), p. 9 (5.1. Is RL data better because of better action), p. 2 (Figure/Table caption) |
| Primary metric/result | Figure 4: Success rate comparison of OpenVLA and Octo policies fine-tuned with RLDG versus conventional methods using human demonstrations. Both generalists trained with RLDG ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Experimental Setup and Tasks - extractive body cue:** Data collection, RL, and Octo policies command actions at 10Hz, while OpenVLA runs at 4Hz due to inference speed limitations.
- **p. 8 / 4.2. RLDG vs. Conventional Fine-tuning - extractive body cue:** For OpenVLA, we primarily attribute this deficiency to the control frequency gap between the RL policy's 10Hz and OpenVLA's 4Hz, changing the system dynamics and ...
- **p. 8 / 4.3. Generalization of RLDG vs. Original RL - extractive body cue:** Additionally, the multi-task capabilities of OpenVLA and Octo allowed fine-tuning on multiple connector data in the Connector Insertion task, achieving 73/80 and 50/80, respectively, when ...
- **p. 9 / 5.1. Is RL data better because of better action - extractive body cue:** As shown in Figure 7, mixing human states and RL actions yields a better fine-tuning success rate than using fully human data (more than 50% ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The second part focuses on dissecting the failure modes of the fine-tuned policies on each individual task. | p. 9 (4.3. Generalization of RLDG vs. Original RL) |
| body limitation/failure cue | However, an interesting RL-specific failure mode was observed: objects were sometimes dropped too early, bouncing out of the bowl. | p. 9 (5.1. Is RL data better because of better action) |
| body limitation/failure cue | Data collection, RL, and Octo policies command actions at 10Hz, while OpenVLA runs at 4Hz due to inference speed limitations. | p. 5 (4.1. Experimental Setup and Tasks) |
| body limitation/failure cue | (B) Pick and Place involves an unseen scenario that tests the policy's visual robustness to different backgrounds and objects. | p. 6 (4.1. Experimental Setup and Tasks) |
| body limitation/failure cue | 4, the RL policy success rate quickly degraded from 20/20 for the training scenario to 1/20 for the unseen scenario of the Pick and ... | p. 8 (4.3. Generalization of RLDG vs. Original RL) |
| body limitation/failure cue | Compared to directly using the RL policies that generated the data, RLDG also demonstrated much greater generalization capabilities and robustness to unseen test scenarios. | p. 8 (4.3. Generalization of RLDG vs. Original RL) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| no implementation/reproducibility sentence selected | verify appendix and code/project |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 4.3. Generalization of RLDG vs. Original RL - extractive body cue:** The second part focuses on dissecting the failure modes of the fine-tuned policies on each individual task.
- **p. 9 / 5.1. Is RL data better because of better action - extractive body cue:** However, an interesting RL-specific failure mode was observed: objects were sometimes dropped too early, bouncing out of the bowl.
- **p. 5 / 4.1. Experimental Setup and Tasks - extractive body cue:** Data collection, RL, and Octo policies command actions at 10Hz, while OpenVLA runs at 4Hz due to inference speed limitations.
- **p. 6 / 4.1. Experimental Setup and Tasks - extractive body cue:** (B) Pick and Place involves an unseen scenario that tests the policy's visual robustness to different backgrounds and objects.
- **p. 8 / 4.3. Generalization of RLDG vs. Original RL - extractive body cue:** 4, the RL policy success rate quickly degraded from 20/20 for the training scenario to 1/20 for the unseen scenario of the Pick and Place ...
- **p. 8 / 4.3. Generalization of RLDG vs. Original RL - extractive body cue:** Compared to directly using the RL policies that generated the data, RLDG also demonstrated much greater generalization capabilities and robustness to unseen test scenarios.

- **PDF anchors reviewed:** datasets p. 6 (4.1. Experimental Setup and Tasks), p. 5 (4.1. Experimental Setup and Tasks), p. 6 (4.1. Experimental Setup and Tasks), p. 8 (4.3. Generalization of RLDG vs. Original RL), p. 8 (4.3. Generalization of RLDG vs. Original RL), p. 5 (4.1. Experimental Setup and Tasks), metrics p. 7 (4.2. RLDG vs. Conventional Fine-tuning), p. 6 (4.2. RLDG vs. Conventional Fine-tuning), p. 6 (4.2. RLDG vs. Conventional Fine-tuning), p. 7 (4.2. RLDG vs. Conventional Fine-tuning), p. 8 (4.3. Generalization of RLDG vs. Original RL), p. 8 (4.3. Generalization of RLDG vs. Original RL), baselines p. 6 (4.2. RLDG vs. Conventional Fine-tuning), p. 7 (4.2. RLDG vs. Conventional Fine-tuning), p. 7 (4.2. RLDG vs. Conventional Fine-tuning), p. 8 (4.3. Generalization of RLDG vs. Original RL), p. 8 (4.3. Generalization of RLDG vs. Original RL), p. 9 (4.3. Generalization of RLDG vs. Original RL), results p. 7 (4.2. RLDG vs. Conventional Fine-tuning), p. 7 (Figure/Table caption), p. 6 (4.2. RLDG vs. Conventional Fine-tuning), p. 6 (4.2. RLDG vs. Conventional Fine-tuning), p. 9 (5.1. Is RL data better because of better action), p. 2 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
