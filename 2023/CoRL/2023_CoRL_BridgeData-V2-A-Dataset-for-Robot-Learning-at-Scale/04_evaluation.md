# Evaluation - BridgeData V2: A Dataset for Robot Learning at Scale

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2308.12952; PDF retrieval source: https://arxiv.org/pdf/2308.12952. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 6 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments)): ResNet-18 ResNet-34 ResNet-50 Image Encoder 0.0 0.2 0.4 0.6 0.8 1.0 Average Success Rate 0.25 0.50 0.75 1.00 Proportion of Dataset 0.0 0.2 0.4 0.6 0.8 1.0 Average Success Rate ...

## Evaluation Body Digest

- **p. 3 / Dataset - extractive body cue:** Assembling a large real-world dataset is time-consuming and expensive, so there has also been significant work on developing simulated environments and datasets for robotic manipulation ...
- **p. 3 / Dataset - extractive body cue:** A real-world dataset provides a research testbed that is truer to downstream robotics applications.
- **p. 4 / Dataset - extractive body cue:** Annotators were asked to describe the task being performed by the robot in each trajectory, with particular emphasis on the final location of any moved ...
- **p. 7 / 5 Experiments - extractive body cue:** However, the language-conditioned methods particularly struggled on tasks involving unseen objects since these object names are not grounded in the dataset.
- **p. 7 / 5 Experiments - extractive body cue:** The tasks and environments in this evaluation matched tasks seen in the training data; however, there were differences in robot setup, camera placement, lighting conditions, ...
- **p. 15 / B.4 Contrastive RL - extractive body cue:** Task BridgeData V1 + PTR BridgeData V2 Put marker in bowl† 0.05 0.65 Put mushroom in pot‡ 0.10 0.70 Average 0.08 0.70 † Unseen objects, ...
- **p. 4 / Dataset - extractive body cue:** 3 BridgeData V2 Our goal is to design a dataset that facilitates research in large-scale robot learning.
- **p. 8 / 5 Experiments - extractive body cue:** 6 Discussion, Limitations, and Future Work We presented BridgeData V2, a dataset with 60,096 trajectories of robotic manipulation behaviors designed to enable research on scalable ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** Dataset (p. 3); 5 Experiments (p. 6); B Learning Method Implementation Details (p. 13).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5 Experiments | BENCHMARK / DATASET | ResNet-18 ResNet-34 ResNet-50 Image Encoder 0.0 0.2 0.4 0.6 0.8 1.0 Average Success Rate 0.25 0.50 0.75 1.00 Proportion of Dataset 0.0 0.2 0.4 ... | p. 8 (5 Experiments) |
| 5 Experiments | BENCHMARK / DATASET | Note that these evaluations were performed zero-shot, without any new data collected in Lab 2, and we expect fine-tuning on a small amount of ... | p. 7 (5 Experiments) |
| 5 Experiments | BENCHMARK / DATASET | We found that performance on an unseen pickand place task was significantly improved by training on data with greater skill diversity. | p. 8 (5 Experiments) |
| 5 Experiments | BENCHMARK / DATASET | The goal-conditioned methods are comparable to each other in success rate. | p. 6 (5 Experiments) |
| 5 Experiments | BENCHMARK / DATASET | To obtain success rates for each method, we collected 10 trials for each task, varying the positions of objects and distractors between trials. | p. 6 (5 Experiments) |

## Dataset / Benchmark Role

- **p. 3 / Dataset - extractive body cue:** Assembling a large real-world dataset is time-consuming and expensive, so there has also been significant work on developing simulated environments and datasets for robotic manipulation ...
- **p. 3 / Dataset - extractive body cue:** A real-world dataset provides a research testbed that is truer to downstream robotics applications.
- **p. 4 / Dataset - extractive body cue:** Annotators were asked to describe the task being performed by the robot in each trajectory, with particular emphasis on the final location of any moved ...
- **p. 7 / 5 Experiments - extractive body cue:** However, the language-conditioned methods particularly struggled on tasks involving unseen objects since these object names are not grounded in the dataset.
- **p. 7 / 5 Experiments - extractive body cue:** The tasks and environments in this evaluation matched tasks seen in the training data; however, there were differences in robot setup, camera placement, lighting conditions, ...
- **p. 15 / B.4 Contrastive RL - extractive body cue:** Task BridgeData V1 + PTR BridgeData V2 Put marker in bowl† 0.05 0.65 Put mushroom in pot‡ 0.10 0.70 Average 0.08 0.70 † Unseen objects, ...
- **p. 4 / Dataset - extractive body cue:** 3 BridgeData V2 Our goal is to design a dataset that facilitates research in large-scale robot learning.
- **p. 8 / 5 Experiments - extractive body cue:** 6 Discussion, Limitations, and Future Work We presented BridgeData V2, a dataset with 60,096 trajectories of robotic manipulation behaviors designed to enable research on scalable ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 13 / Figure/Table caption - extractive body cue:** Table 5. We provide a breakdown of which portions of the dataset include which sensors in Figure 6. B Learning Method Implementation Details Below we ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Assembling a large real-world dataset is time-consuming and expensive, so there has also been significant work on developing simulated environments and datasets for robotic ... | embodiment, simulator version and control stack | p. 3 (Dataset), p. 3 (Dataset) |
| Task/environment | A real-world dataset provides a research testbed that is truer to downstream robotics applications. | reset, timeout, object/scene variation | p. 3 (Dataset), p. 4 (Dataset) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 14 (B.4 Contrastive RL), p. 2 (1 Introduction) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 2 (1 Introduction), p. 14 (B.1 Goal-conditioned behavior cloning) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| ResNet-18 ResNet-34 ResNet-50 Image Encoder 0.0 0.2 0.4 0.6 0.8 1.0 Average Success Rate 0.25 0.50 0.75 1.00 Proportion of Dataset 0.0 0.2 0.4 ... | definition/direction/unit from same section | p. 8 (5 Experiments) |
| The goal-conditioned methods are comparable to each other in success rate. | definition/direction/unit from same section | p. 6 (5 Experiments) |
| To obtain success rates for each method, we collected 10 trials for each task, varying the positions of objects and distractors between trials. | definition/direction/unit from same section | p. 6 (5 Experiments) |
| Success rates are averaged over 10 trials. | definition/direction/unit from same section | p. 7 (5 Experiments) |
| As seen in Table 4, performance was somewhat worse in Lab 2, but all methods attained non-zero success. | definition/direction/unit from same section | p. 7 (5 Experiments) |
| We found that as dataset size increases, performance improves for both a seen and unseen task. | definition/direction/unit from same section | p. 8 (5 Experiments) |
| However, it is difficult to replicate the complexity of the real world (e.g., objects, environments, lighting, and physics) in a simulator well enough to ... | definition/direction/unit from same section | p. 3 (Dataset) |
| 4 Offline Learning Methods To demonstrate that BridgeData V2 is compatible with a variety of learning methods with different assumptions, we evaluated several state-of-the-art ... | definition/direction/unit from same section | p. 5 (Dataset) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Once again, RT-1 greatly outperformed the LCBC baseline. | comparison identity and matched condition | p. 7 (5 Experiments) |
| Most apparently, RT-1 is significantly better than our LCBC baseline, likely due to a combination of design decisions such as larger images, action discretization, ... | comparison identity and matched condition | p. 6 (5 Experiments) |
| (R) We compared the performance of GCBC trained on a dataset with only 3 skills and a dataset with all 13 skills, keeping the ... | comparison identity and matched condition | p. 8 (5 Experiments) |
| Note that these evaluations were performed zero-shot, without any new data collected in Lab 2, and we expect fine-tuning on a small amount of ... | comparison identity and matched condition | p. 7 (5 Experiments) |
| 4 Offline Learning Methods To demonstrate that BridgeData V2 is compatible with a variety of learning methods with different assumptions, we evaluated several state-of-the-art ... | comparison identity and matched condition | p. 5 (Dataset) |
| As a baseline, we evaluate a standard goal-conditioned behavior cloning method. | comparison identity and matched condition | p. 6 (Dataset) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Note that these evaluations were performed zero-shot, without any new data collected in Lab 2, and we expect fine-tuning on a small amount of ... | component/input/data sensitivity | p. 7 (5 Experiments) |
| Additionally, unlike many prior datasets [23, 5], our experiments isolate the effect of data diversity and show that greater diversity improves generalization, corroborating the ... | component/input/data sensitivity | p. 3 (Dataset) |
| Task BridgeData V1 + PTR BridgeData V2 Put marker in bowl† 0.05 0.65 Put mushroom in pot‡ 0.10 0.70 Average 0.08 0.70 † Unseen ... | component/input/data sensitivity | p. 15 (B.4 Contrastive RL) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we propose a new dataset, which we call BridgeData V2 (Figure 1) because it greatly expands on the previously released Bridge ... | ResNet-18 ResNet-34 ResNet-50 Image Encoder 0.0 0.2 0.4 0.6 0.8 1.0 Average Success Rate 0.25 0.50 0.75 1.00 Proportion of Dataset 0.0 0.2 0.4 ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 6 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments) |
| Primary metric/result | Note that these evaluations were performed zero-shot, without any new data collected in Lab 2, and we expect fine-tuning on a small amount of ... | numeric claim only at cited anchor | p. 7 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 4 / Dataset - extractive body cue:** 3.1 System setup Randomized Cameras Fixed Camera With Depth WidowX 250 Robot Arm Figure 2 (System setup) A picture of our robot setup showing the ...
- **p. 4 / Dataset - extractive body cue:** The images are saved at a 640x480 resolution and the control frequency is 5 Hz.
- **p. 4 / Dataset - extractive body cue:** Every 50 trajectories, the collector randomizes the poses of the cameras, switches out the objects in the scene, and randomizes the position of the workspace ...
- **p. 5 / Dataset - extractive body cue:** BridgeData V2 features 24 environments, including kitchens, sinks, and tabletops, as well as more than 100 objects.
- **p. 5 / Dataset - extractive body cue:** In total, BridgeData V2 contains 50,365 expert demonstrations and 9,731 trajectories from a scripted policy.
- **p. 6 / 5 Experiments - extractive body cue:** To obtain success rates for each method, we collected 10 trials for each task, varying the positions of objects and distractors between trials.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 6 Discussion, Limitations, and Future Work We presented BridgeData V2, a dataset with 60,096 trajectories of robotic manipulation behaviors designed to enable research on ... | p. 8 (5 Experiments) |
| body limitation/failure cue | While this policy fails frequently, we can run it autonomously to collect a large amount of pick-and-place data for a wide range of objects ... | p. 4 (Dataset) |
| body limitation/failure cue | Additionally, the "put eggplant in pot" is a very challenging task in both labs since the eggplant easily slips out of the gripper. | p. 7 (5 Experiments) |
| body limitation/failure cue | Training on a combination of the largest datasets released so far is an exciting and promising direction for future work. | p. 3 (Dataset) |
| body limitation/failure cue | However, it is difficult to replicate the complexity of the real world (e.g., objects, environments, lighting, and physics) in a simulator well enough to ... | p. 3 (Dataset) |
| body limitation/failure cue | Methods that benefit from suboptimal data, such as offline RL, can leverage this autonomous data to learn more robust behaviors. | p. 4 (Dataset) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We use the Adam optimizer [60] with a learning rate of 3e-4. | p. 14 (B.1 Goal-conditioned behavior cloning) |
| Third, we increase the GCBC regularization coefficient to 0.2 to avoid sampling out-ofdistribution actions and use the same batch size as other methods to ... | p. 14 (B.4 Contrastive RL) |
| To obtain success rates for each method, we collected 10 trials for each task, varying the positions of objects and distractors between trials. | p. 6 (5 Experiments) |
| Success rates are averaged over 10 trials. | p. 7 (5 Experiments) |
| We used 20 trials per policy in this experiment. | p. 8 (5 Experiments) |
| First, we tested GCBC with different sizes of image encoders on the task of moving a spoon. | p. 8 (5 Experiments) |
| Below we list relevant implementation details for each method. | p. 13 (B Learning Method Implementation Details) |
| During training, the goal associated with an observation is selected by uniformly sampling an observation from the future timesteps in the trajectory. | p. 13 (B Learning Method Implementation Details) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5 Experiments - extractive body cue:** 6 Discussion, Limitations, and Future Work We presented BridgeData V2, a dataset with 60,096 trajectories of robotic manipulation behaviors designed to enable research on scalable ...
- **p. 4 / Dataset - extractive body cue:** While this policy fails frequently, we can run it autonomously to collect a large amount of pick-and-place data for a wide range of objects more ...
- **p. 7 / 5 Experiments - extractive body cue:** Additionally, the "put eggplant in pot" is a very challenging task in both labs since the eggplant easily slips out of the gripper.
- **p. 3 / Dataset - extractive body cue:** Training on a combination of the largest datasets released so far is an exciting and promising direction for future work.
- **p. 3 / Dataset - extractive body cue:** However, it is difficult to replicate the complexity of the real world (e.g., objects, environments, lighting, and physics) in a simulator well enough to thoroughly ...
- **p. 4 / Dataset - extractive body cue:** Methods that benefit from suboptimal data, such as offline RL, can leverage this autonomous data to learn more robust behaviors.

- **Evidence anchors reviewed:** datasets p. 3 (Dataset), p. 3 (Dataset), p. 4 (Dataset), p. 7 (5 Experiments), p. 7 (5 Experiments), p. 15 (B.4 Contrastive RL), metrics p. 8 (5 Experiments), p. 6 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), baselines p. 7 (5 Experiments), p. 6 (5 Experiments), p. 8 (5 Experiments), p. 7 (5 Experiments), p. 5 (Dataset), p. 6 (Dataset), results p. 8 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 6 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
