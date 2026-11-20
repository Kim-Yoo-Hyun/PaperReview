# Evaluation - BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2202.02005; PDF retrieval source: https://arxiv.org/pdf/2202.02005. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 19 (Figure/Table caption), p. 14 (Figure/Table caption), p. 3 (Figure/Table caption)): Table 2: Success rates for zero-shot (language) and few-shot (video) generalization to tasks not in the training dataset. The first 4 tasks only use objects from the 79-task family. The ...

## Evaluation Body Digest

- **p. 8 / 7 Discussion - extractive body cue:** Our evaluation covered 29 unseen vision-based manipulation tasks with a variety of objects and scenes.
- **p. 8 / 7 Discussion - extractive body cue:** However, even for tasks that are less successful, the robot often exhibits behavior suggesting that it understands at least part of the task, reaching for ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Success rates for zero-shot (language) and few-shot (video) generalization to tasks not in the training dataset. The first 4 tasks only use objects ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Mean number of interventions vs. task success rate. Each point represents a pol- icy evaluated during HG-DAgger data collection. There is a clear ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 7: Within each manipulation sub-task (e.g. "place the bottle in the ceramic bowl") the policy must generalize not only to variations in object positions, ...
- **p. 17 / Figure/Table caption - extractive body cue:** Table 6: Ablations of video encoder batch composition. In the ablations below, we control for the same architecture, dataset, hyperparameters, and training time, changing only ...
- **p. 8 / 7 Discussion - extractive body cue:** Another limitation is the lower performance of the video-conditioned policy, which encourages future research on improving the generalization of video-based task representations and enhancing the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Single-task bin and door performance, aver- age and standard deviation across runs. Bin-Emptying Picks / Minute # Runs Human Expert 6.3 (2.1) 2759

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2: Success rates for zero-shot (language) and few-shot (video) generalization to tasks not in the training dataset. The first 4 tasks only use ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5: Mean number of interventions vs. task success rate. Each point represents a pol- icy evaluated during HG-DAgger data collection. There is a ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 4: Ablation Studies. Left: Multi-task vs. single task models on the ‘place the bottle in the ceramic bowl' task. Training across tasks and ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 11: Bin Emptying and Door Opening tasks are used to validate that BC-Z can achieve a high level of task success and generalize ... | p. 19 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 7: Within each manipulation sub-task (e.g. "place the bottle in the ceramic bowl") the policy must generalize not only to variations in object ... | p. 14 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / 7 Discussion - extractive body cue:** Our evaluation covered 29 unseen vision-based manipulation tasks with a variety of objects and scenes.
- **p. 8 / 7 Discussion - extractive body cue:** However, even for tasks that are less successful, the robot often exhibits behavior suggesting that it understands at least part of the task, reaching for ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Overview of BC-Z. We collect a large-scale dataset (25,877 episodes) of 100 diverse manipulation tasks, and train a 7-DoF multi-task policy that conditions ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: A subset of training tasks (top row), and a subset of held-out tasks (bottom two rows) used for evaluating zero shot task generalization. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. The policy is a mapping from images and commands to actions, and can be written as µ : S × W →A, where ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: BC-Z network architecture. A monocular RGB image from the head-mounted camera is passed through a ResNet18 encoder, then through a two-layer MLP to ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Qualitative examples of BC-Z successfully performing held-out tasks. push open a door while avoiding collisions. Both tasks use the architecture in Figure 3, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Single-task bin and door performance, aver- age and standard deviation across runs. Bin-Emptying Picks / Minute # Runs Human Expert 6.3 (2.1) 2759
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Success rates for zero-shot (language) and few-shot (video) generalization to tasks not in the training dataset. The first 4 tasks only use objects ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Training vs. generalization per- formance, averaged across 21 of the train- ing tasks and all 28 held-out tasks. Setting Task Conditioning Success Train ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Our evaluation covered 29 unseen vision-based manipulation tasks with a variety of objects and scenes. | embodiment, simulator version and control stack | p. 8 (7 Discussion), p. 8 (7 Discussion) |
| Task/environment | However, even for tasks that are less successful, the robot often exhibits behavior suggesting that it understands at least part of the task, reaching ... | reset, timeout, object/scene variation | p. 8 (7 Discussion) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 8 (7 Discussion), p. 1 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 2: Success rates for zero-shot (language) and few-shot (video) generalization to tasks not in the training dataset. The first 4 tasks only use ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 5: Mean number of interventions vs. task success rate. Each point represents a pol- icy evaluated during HG-DAgger data collection. There is a ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 7: Within each manipulation sub-task (e.g. "place the bottle in the ceramic bowl") the policy must generalize not only to variations in object ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| Table 6: Ablations of video encoder batch composition. In the ablations below, we control for the same architecture, dataset, hyperparameters, and training time, changing ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| Another limitation is the lower performance of the video-conditioned policy, which encourages future research on improving the generalization of video-based task representations and enhancing ... | definition/direction/unit from same section | p. 8 (7 Discussion) |
| Table 1: Single-task bin and door performance, aver- age and standard deviation across runs. Bin-Emptying Picks / Minute # Runs Human Expert 6.3 (2.1) ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 7: Performance comparsion one-hot, language, or video conditioning over 21 training tasks. Video policies are conditioned on held-out videos of the training tasks. ... | definition/direction/unit from same section | p. 21 (Figure/Table caption) |
| Table 9: Performance comparison between different video embeddings on selected tasks. All tasks are held-out unless otherwise indicated. Numbers in (parentheses) are 1 unit ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 6: Ablations of video encoder batch composition. In the ablations below, we control for the same architecture, dataset, hyperparameters, and training time, changing ... | comparison identity and matched condition | p. 17 (Figure/Table caption) |
| Figure 9: Visualizations of different video encoders. Each row and column indicates a different task, with the entry at (i, j) indicating the cosine ... | comparison identity and matched condition | p. 18 (Figure/Table caption) |
| Table 4: Ablation Studies. Left: Multi-task vs. single task models on the ‘place the bottle in the ceramic bowl' task. Training across tasks and ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Through the experiments, we also learn that 100 training tasks is sufficient for enabling generalization to new tasks, that HG-DAgger is important for good ... | comparison identity and matched condition | p. 8 (7 Discussion) |
| Figure 13: An example of adapting a sim image (left) to look real (right) using RetinaGAN [51]. environment (including the door). Further, any collision ... | comparison identity and matched condition | p. 20 (Figure/Table caption) |
| Table 7: Performance comparsion one-hot, language, or video conditioning over 21 training tasks. Video policies are conditioned on held-out videos of the training tasks. ... | comparison identity and matched condition | p. 21 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 6: Ablations of video encoder batch composition. In the ablations below, we control for the same architecture, dataset, hyperparameters, and training time, changing ... | component/input/data sensitivity | p. 17 (Figure/Table caption) |
| Through the experiments, we also learn that 100 training tasks is sufficient for enabling generalization to new tasks, that HG-DAgger is important for good ... | component/input/data sensitivity | p. 8 (7 Discussion) |
| Table 4: Ablation Studies. Left: Multi-task vs. single task models on the ‘place the bottle in the ceramic bowl' task. Training across tasks and ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 13: An example of adapting a sim image (left) to look real (right) using RetinaGAN [51]. environment (including the door). Further, any collision ... | component/input/data sensitivity | p. 20 (Figure/Table caption) |
| Table 7: Performance comparsion one-hot, language, or video conditioning over 21 training tasks. Video policies are conditioned on held-out videos of the training tasks. ... | component/input/data sensitivity | p. 21 (Figure/Table caption) |
| Figure 2: A subset of training tasks (top row), and a subset of held-out tasks (bottom two rows) used for evaluating zero shot task ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contribution is an empirical study of a large-scale interactive imitation learning system that solves a breadth of tasks, including zero-shot and few-shot ... | Table 2: Success rates for zero-shot (language) and few-shot (video) generalization to tasks not in the training dataset. The first 4 tasks only use ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 19 (Figure/Table caption), p. 14 (Figure/Table caption), p. 3 (Figure/Table caption) |
| Primary metric/result | Figure 5: Mean number of interventions vs. task success rate. Each point represents a pol- icy evaluated during HG-DAgger data collection. There is a ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 2 / 1 Introduction - extractive body cue:** We collect a large-scale dataset (25,877 episodes) of 100 diverse manipulation tasks, and train a 7-DoF multi-task policy that conditions on task language strings or ...
- **p. 2 / 1 Introduction - extractive body cue:** Across 12 robots, 7 different operators collected 25,877 robot demonstrations that totaled 125 hours of robot time, as well as 18,726 human videos of the ...
- **p. 2 / 1 Introduction - extractive body cue:** These closedloop visuomotor policies perform asynchronous inference and control at 10Hz, amounting to well over 100 decisions per episode.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 13: An example of adapting a sim image (left) to look real (right) using RetinaGAN [51]. environment (including the door). Further, any collision ... | p. 20 (Figure/Table caption) |
| body limitation/failure cue | Our system does have a number of limitations. | p. 8 (7 Discussion) |
| body limitation/failure cue | A direction to address this limitation is to relabel the dataset with a variety of human-provided annotations [24], which could enable the system to ... | p. 8 (7 Discussion) |
| body limitation/failure cue | Table 5: Teleoperation buttons and controls. Control Function Right Controller (Arm) A Start recording, or mark demo as success if already recording B Stops ... | p. 13 (Figure/Table caption) |
| body limitation/failure cue | Figure 4: Qualitative examples of BC-Z successfully performing held-out tasks. push open a door while avoiding collisions. Both tasks use the architecture in Figure ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | Figure 8: Human demonstrations of the task (left) are augmented with random distortions and reflec- tions (right), then trained to match language features for ... | p. 15 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| With sufficient real-world data, these methods should in principle enable robots to generalize across new tasks, objects, and scenes without requiring hand-coded, task-specific representations. | p. 1 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 20 / Figure/Table caption - extractive body cue:** Figure 13: An example of adapting a sim image (left) to look real (right) using RetinaGAN [51]. environment (including the door). Further, any collision of ...
- **p. 8 / 7 Discussion - extractive body cue:** Our system does have a number of limitations.
- **p. 8 / 7 Discussion - extractive body cue:** A direction to address this limitation is to relabel the dataset with a variety of human-provided annotations [24], which could enable the system to handle ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 5: Teleoperation buttons and controls. Control Function Right Controller (Arm) A Start recording, or mark demo as success if already recording B Stops current ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Qualitative examples of BC-Z successfully performing held-out tasks. push open a door while avoiding collisions. Both tasks use the architecture in Figure 3, ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 8: Human demonstrations of the task (left) are augmented with random distortions and reflec- tions (right), then trained to match language features for the ...

- **Evidence anchors reviewed:** datasets p. 8 (7 Discussion), p. 8 (7 Discussion), metrics p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 14 (Figure/Table caption), p. 17 (Figure/Table caption), p. 8 (7 Discussion), p. 6 (Figure/Table caption), baselines p. 17 (Figure/Table caption), p. 18 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (7 Discussion), p. 20 (Figure/Table caption), p. 21 (Figure/Table caption), results p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 19 (Figure/Table caption), p. 14 (Figure/Table caption), p. 3 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (23 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Table 6: Ablations of video encoder batch composition. In the ablations below, we control for the same architecture, dataset, hyperparameters, and training time, changing only the sampling strategy for each ... (p. 17, Figure/Table caption).
- **Metric evidence:** Another limitation is the lower performance of the video-conditioned policy, which encourages future research on improving the generalization of video-based task representations and enhancing the performance of imitation learning algori ... (p. 8, 7 Discussion).
- **Baseline/ablation evidence:** Table 4: Ablation Studies. Left: Multi-task vs. single task models on the ‘place the bottle in the ceramic bowl' task. Training across tasks and with adaptive state-diffs is important for ... (p. 8, Figure/Table caption).
- **Failure/negative evidence:** Further, any collision of the robot base and arm (not including the gripper) with the environment counted as the task failure by the operator. (p. 20, C Featurization Details).
