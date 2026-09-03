# Evaluation - 3DS-VLA: A 3D Spatial-Aware Vision Language Action Model for Robust Multi-Task Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v305/li25g.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/li25g/li25g.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4 Experiment), p. 8 (4 Experiment), p. 6 (4 Experiment), p. 7 (4 Experiment), p. 6 (4 Experiment), p. 8 (4 Experiment)): Both Ours and Ours-s achieve the same average success rate of 0.66 on single-arm tasks, demonstrating that our model can effectively handle different embodiments within a unified training pipeline, without ...

## Evaluation Body Digest

- **p. 8 / 4 Experiment - extractive body cue:** Since we establish associations between the robot and its environment through structured text input, our model learns to focus on task-relevant objects while disregarding irrelevant ...
- **p. 6 / 4 Experiment - extractive body cue:** We train and test our methods using the same dataset as the baselines, with 100 demonstrations per task for training and 25 demonstrations for testing.
- **p. 7 / 4 Experiment - extractive body cue:** Our method is evaluated across 10 tasks on the Franka Research 3 (FR3) robot with a 3Dprinted UMI gripper [75].
- **p. 7 / 4 Experiment - extractive body cue:** 3, we use a model with the same architecture as ours but only take the image, robot state, and task description as input, directly outputting ...
- **p. 8 / 4 Experiment - extractive body cue:** 4, thanks to the spatial constraints that encode the relationship between the robot and its environment, our model is capable of adapting to such variations ...
- **p. 5 / 4 Experiment - extractive body cue:** The input RGB-D images, with a resolution of 336 × 336, are captured by a single camera mounted at the front of the robot.
- **p. 6 / 4 Experiment - extractive body cue:** In contrast, our approach improves the robot's spatial understanding by enhancing 3D observation and incorporating 3D spatial constraints.
- **p. 5 / 4 Experiment - extractive body cue:** We simultaneously train on demonstrations from the single-arm simulator RLBench [37, 72] and the dual-arm simulator RLBench2 [38].

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 Experiment (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | Both Ours and Ours-s achieve the same average success rate of 0.66 on single-arm tasks, demonstrating that our model can effectively handle different embodiments ... | p. 7 (4 Experiment) |
| 4 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | Remarkably, the model achieves similar accuracy as it does in clean background settings. | p. 8 (4 Experiment) |
| 4 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | 1, in the single-arm setting, our method surpasses all baselines by at least 4% average success rate. | p. 6 (4 Experiment) |
| 4 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | The success rate is used as the evaluation metric. | p. 7 (4 Experiment) |
| 4 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | 2, in the dual-arm setting, our method outperforms all baselines by a significant margin. | p. 6 (4 Experiment) |

## Dataset / Benchmark Role

- **p. 8 / 4 Experiment - extractive body cue:** Since we establish associations between the robot and its environment through structured text input, our model learns to focus on task-relevant objects while disregarding irrelevant ...
- **p. 6 / 4 Experiment - extractive body cue:** We train and test our methods using the same dataset as the baselines, with 100 demonstrations per task for training and 25 demonstrations for testing.
- **p. 7 / 4 Experiment - extractive body cue:** Our method is evaluated across 10 tasks on the Franka Research 3 (FR3) robot with a 3Dprinted UMI gripper [75].
- **p. 7 / 4 Experiment - extractive body cue:** 3, we use a model with the same architecture as ours but only take the image, robot state, and task description as input, directly outputting ...
- **p. 8 / 4 Experiment - extractive body cue:** 4, thanks to the spatial constraints that encode the relationship between the robot and its environment, our model is capable of adapting to such variations ...
- **p. 5 / 4 Experiment - extractive body cue:** The input RGB-D images, with a resolution of 336 × 336, are captured by a single camera mounted at the front of the robot.
- **p. 6 / 4 Experiment - extractive body cue:** In contrast, our approach improves the robot's spatial understanding by enhancing 3D observation and incorporating 3D spatial constraints.
- **p. 5 / 4 Experiment - extractive body cue:** We simultaneously train on demonstrations from the single-arm simulator RLBench [37, 72] and the dual-arm simulator RLBench2 [38].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: 3DS-VLA achieves comprehensive 3D spatial awareness by encoding 3D spatial observations with a pretrained 2D vision-language model and establishing 3D spatial constraints to ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Model Architecture. Given the current observation, task instruction, and keypoint con- straints, 3DS-VLA predicts the next-frame pose. It incorporates 3D spatial observations and ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Single-Arm Multi-Task Performance on RLBench of 21 tasks. Stack Open USB out Rubbish Close Toilet Beat
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2: Dual-Arm Multi-Task Performance on RL- Bench2 of 5 tasks Bimanual Task RVT-LF Peract-LF Peract2 Ours Lift ball 0.17 0.40 0.50
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3: The effectiveness of each pro- posed component. Row 3D Spatial 3D Aligned AVG. ID Constraint Tokens PEs
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Demonstrations of execution process and four types of generalization settings. 7
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: We compare 3DS-VLA with baselines on 10 real-world tasks and evaluate its robustness across test settings that vary from the training dataset domain. ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 4: Question-Answer Pair. We encode the current robot pose and target keypoint constraints as 3D spatio-temporal constraints in the model's language input. Both single-arm ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Since we establish associations between the robot and its environment through structured text input, our model learns to focus on task-relevant objects while disregarding ... | embodiment, simulator version and control stack | p. 8 (4 Experiment), p. 6 (4 Experiment) |
| Task/environment | We train and test our methods using the same dataset as the baselines, with 100 demonstrations per task for training and 25 demonstrations for ... | reset, timeout, object/scene variation | p. 6 (4 Experiment), p. 7 (4 Experiment) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (3 Method), p. 3 (3 Method) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 5 (3 Method), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 1, in the single-arm setting, our method surpasses all baselines by at least 4% average success rate. | definition/direction/unit from same section | p. 6 (4 Experiment) |
| The success rate is used as the evaluation metric. | definition/direction/unit from same section | p. 7 (4 Experiment) |
| Additionally, we perform an extra experiment where we first fine-tune the pretrained VLM on the OXE dataset [74], which only takes 2D images as ... | definition/direction/unit from same section | p. 7 (4 Experiment) |
| ID Constraint Tokens PEs Score 1 ✗ ✗ ✗ 0.41 2 ✓ ✗ ✗ 0.62 3 ✓ ✓ ✗ 0.60 4 ✓ ✓ ✓ ... | definition/direction/unit from same section | p. 6 (4 Experiment) |
| Remarkably, the model achieves similar accuracy as it does in clean background settings. | definition/direction/unit from same section | p. 8 (4 Experiment) |
| This makes the pipeline prone to failure if the underlying models are inaccurate-for example, if GroundingDINO [71] misses critical keypoints on the cup handle ... | definition/direction/unit from same section | p. 8 (4 Experiment) |
| Figure 1: 3DS-VLA achieves comprehensive 3D spatial awareness by encoding 3D spatial observations with a pretrained 2D vision-language model and establishing 3D spatial constraints ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 5: Visualization of simulation tasks. We conduct on both single-arm and dual-arm simula- tion tasks. 4. Bottle at rack: The robot needs to ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 2, in the dual-arm setting, our method outperforms all baselines by a significant margin. | comparison identity and matched condition | p. 6 (4 Experiment) |
| As shown in Table 4, our method outperforms all baselines, demonstrating superior interaction in 3D environments. | comparison identity and matched condition | p. 8 (4 Experiment) |
| The fine-tuning stage trains on 2,400 demonstrations and runs for 10 epochs, taking approximately 8 hours on an NVIDIA RTX A100 GPU, achieving a ... | comparison identity and matched condition | p. 5 (4 Experiment) |
| 1, in the single-arm setting, our method surpasses all baselines by at least 4% average success rate. | comparison identity and matched condition | p. 6 (4 Experiment) |
| 4: 1) Instance variation: We evaluate across a diverse set of unseen instances that differ in color, size, and appearance compared to the training ... | comparison identity and matched condition | p. 8 (4 Experiment) |
| Figure 5: Visualization of simulation tasks. We conduct on both single-arm and dual-arm simula- tion tasks. 4. Bottle at rack: The robot needs to ... | comparison identity and matched condition | p. 15 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Both Ours and Ours-s achieve the same average success rate of 0.66 on single-arm tasks, demonstrating that our model can effectively handle different embodiments ... | component/input/data sensitivity | p. 7 (4 Experiment) |
| 4.3 Ablation Study Does each component work? | component/input/data sensitivity | p. 7 (4 Experiment) |
| 0.18 0.29 0.22 0.46 ±0.30 Table 3: The effectiveness of each proposed component. | component/input/data sensitivity | p. 6 (4 Experiment) |
| This stems from their reliance on single-view 2D images without explicit 3D geometric understanding, which is essential for precise action prediction. | component/input/data sensitivity | p. 6 (4 Experiment) |
| To illustrate this, we test the "slide box" and "unplug charger" tasks with randomly set backgrounds, without additional training. | component/input/data sensitivity | p. 8 (4 Experiment) |
| Stack Pour Pick Stack Water Bottle at Slide Unplug Wipe Open Models Success ↑ Cup Water Place* Block* Plants Rack Box Charger Table Drawer ... | component/input/data sensitivity | p. 8 (4 Experiment) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are as follows: 1) We propose 3DS-VLA, equipping pretrained 2D VLMs with comprehensive 3D awareness for robust end-effector pose prediction. | Both Ours and Ours-s achieve the same average success rate of 0.66 on single-arm tasks, demonstrating that our model can effectively handle different embodiments ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4 Experiment), p. 8 (4 Experiment), p. 6 (4 Experiment), p. 7 (4 Experiment), p. 6 (4 Experiment), p. 8 (4 Experiment) |
| Primary metric/result | Remarkably, the model achieves similar accuracy as it does in clean background settings. | numeric claim only at cited anchor | p. 8 (4 Experiment) |

- Numeric sentences retained from the body:
- **p. 5 / 4 Experiment - extractive body cue:** The fine-tuning stage trains on 2,400 demonstrations and runs for 10 epochs, taking approximately 8 hours on an NVIDIA RTX A100 GPU, achieving a 5Hz ...
- **p. 5 / 4 Experiment - extractive body cue:** We adopt 21 tasks from single-arm RLBench [37, 72] and 5 tasks of the same coordinate type from dual-arm RLBench [38], featuring variations such as ...
- **p. 6 / 4 Experiment - extractive body cue:** 0.18 0.29 0.22 0.46 ±0.30 Table 3: The effectiveness of each proposed component.
- **p. 7 / 4 Experiment - extractive body cue:** Our method is evaluated across 10 tasks on the Franka Research 3 (FR3) robot with a 3Dprinted UMI gripper [75].
- **p. 7 / 4 Experiment - extractive body cue:** We fine-tune the model with 10 epochs using pretrained weights obtained from simulation training.
- **p. 7 / 4 Experiment - extractive body cue:** For each task, we train an agent and evaluate it over 10 trials with diverse object poses.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This makes the pipeline prone to failure if the underlying models are inaccurate-for example, if GroundingDINO [71] misses critical keypoints on the cup handle ... | p. 8 (4 Experiment) |
| body limitation/failure cue | Compared with 2D VLA methods, we observe frequent failures during the critical final stage of 3D contact. | p. 6 (4 Experiment) |
| body limitation/failure cue | Please refer to Appendix for more details: Section 7.2 for visualization of tasks in RLBench and real world and Section 7.3 for discussion of ... | p. 8 (4 Experiment) |
| body limitation/failure cue | Figure 6: Visualization of real-world tasks. The tasks are shown in key-frame flow. The primary failure mode is the imprecise prediction of end-effector poses. ... | p. 16 (Figure/Table caption) |
| body limitation/failure cue | Figure 5: Visualization of simulation tasks. We conduct on both single-arm and dual-arm simula- tion tasks. 4. Bottle at rack: The robot needs to ... | p. 15 (Figure/Table caption) |
| body limitation/failure cue | The robustness of 3DS-VLA when handling noise. | p. 7 (4 Experiment) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The fine-tuning stage trains on 2,400 demonstrations and runs for 10 epochs, taking approximately 8 hours on an NVIDIA RTX A100 GPU, achieving a ... | p. 5 (4 Experiment) |
| The keyframes represent important or bottleneck steps of the gripper during task execution, such as a pre-pick, grasp, or place pose. | p. 5 (4 Experiment) |
| The first category includes: 1) RVT2 (RSS 2024) [26]: A transformer-based model on RLBench that encodes virtually projected images for 3D object manipulation. | p. 6 (4 Experiment) |
| Following the leader-follower architecture implementation [38], the output of one network serves as input to the other, with both actions executed sequentially. | p. 6 (4 Experiment) |
| For each task, we train an agent and evaluate it over 10 trials with diverse object poses. | p. 7 (4 Experiment) |
| We fine-tune the model with 10 epochs using pretrained weights obtained from simulation training. | p. 7 (4 Experiment) |
| Since Rekep's open-source implementation is not well-suited for RLBench, we compare it with only in real-world experiments. | p. 8 (4 Experiment) |
| 4, thanks to the spatial constraints that encode the relationship between the robot and its environment, our model is capable of adapting to such ... | p. 8 (4 Experiment) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4 Experiment - extractive body cue:** This makes the pipeline prone to failure if the underlying models are inaccurate-for example, if GroundingDINO [71] misses critical keypoints on the cup handle that ...
- **p. 6 / 4 Experiment - extractive body cue:** Compared with 2D VLA methods, we observe frequent failures during the critical final stage of 3D contact.
- **p. 8 / 4 Experiment - extractive body cue:** Please refer to Appendix for more details: Section 7.2 for visualization of tasks in RLBench and real world and Section 7.3 for discussion of failure ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 6: Visualization of real-world tasks. The tasks are shown in key-frame flow. The primary failure mode is the imprecise prediction of end-effector poses. This ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 5: Visualization of simulation tasks. We conduct on both single-arm and dual-arm simula- tion tasks. 4. Bottle at rack: The robot needs to grasp ...
- **p. 7 / 4 Experiment - extractive body cue:** The robustness of 3DS-VLA when handling noise.

- **Evidence anchors reviewed:** datasets p. 8 (4 Experiment), p. 6 (4 Experiment), p. 7 (4 Experiment), p. 7 (4 Experiment), p. 8 (4 Experiment), p. 5 (4 Experiment), metrics p. 6 (4 Experiment), p. 7 (4 Experiment), p. 7 (4 Experiment), p. 6 (4 Experiment), p. 8 (4 Experiment), p. 8 (4 Experiment), baselines p. 6 (4 Experiment), p. 8 (4 Experiment), p. 5 (4 Experiment), p. 6 (4 Experiment), p. 8 (4 Experiment), p. 15 (Figure/Table caption), results p. 7 (4 Experiment), p. 8 (4 Experiment), p. 6 (4 Experiment), p. 7 (4 Experiment), p. 6 (4 Experiment), p. 8 (4 Experiment).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Additionally, we perform an extra experiment where we first fine-tune the pretrained VLM on the OXE dataset [74], which only takes 2D images as input, and then continue finetuning on ... (p. 7, 4 Experiment).
- **Metric evidence:** 1, in the single-arm setting, our method surpasses all baselines by at least 4% average success rate. (p. 6, 4 Experiment).
- **Baseline/ablation evidence:** 2, in the dual-arm setting, our method outperforms all baselines by a significant margin. (p. 6, 4 Experiment).
- **Failure/negative evidence:** This makes the pipeline prone to failure if the underlying models are inaccurate-for example, if GroundingDINO [71] misses critical keypoints on the cup handle that needs to be grasped, or ... (p. 8, 4 Experiment).
