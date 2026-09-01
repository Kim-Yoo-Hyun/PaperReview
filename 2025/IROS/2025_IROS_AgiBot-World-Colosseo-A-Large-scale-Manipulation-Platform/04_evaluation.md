# Evaluation - AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://opendrivelab.com/AgiBot-World/; PDF retrieval source: https://arxiv.org/pdf/2503.06669. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (2) Implementation Details), p. 6 (1) Evaluation Tasks), p. 3 (Dataset), p. 4 (Dataset)): Fig. 7: Further analysis on: a) how model performance scales with data size, and b) the impact of filtering undesir- able data through manual review on policy learning. World alpha ...

## Evaluation Body Digest

- **p. 3 / Dataset - extractive body cue:** Based on the hardware platform developed by us, AgiBot G1, we construct AgiBot Worldan open-source robot manipulation dataset collected by more than 100 homogeneous robots, ...
- **p. 5 / Dataset - extractive body cue:** 3: Dataset Statistics. a) AgiBot World dataset covers the vast majority of robotic application scenarios, as well as a wide range of interactive objects. b) ...
- **p. 3 / Dataset - extractive body cue:** Prior datasets above generally face limitations in data scale, task practicality, and scenario naturalness, compounded by inadequate quality assurance and hardware restrictions, which impedes generalist ...
- **p. 4 / Dataset - extractive body cue:** Our dataset also features over 3,000 distinct objects, systematically categorized across various scenes.
- **p. 4 / Dataset - extractive body cue:** The dataset covers a wide range of scenarios and scene setups, ensuring both scale and diversity in the pursuit of generalizable robot policy.
- **p. 5 / Dataset - extractive body cue:** Latent Action Model Despite considerable advancements in gathering diverse robot demonstrations, the volume of action-labeled robot data remains limited relative to web-scale datasets.
- **p. 6 / V. EXPERIMENT AND ANALYSIS - extractive body cue:** We evaluate the real-world performance of policies pretrained on different data sources including the AgiBot World dataset, demonstrating the effectiveness credited from the GO-1 model ...
- **p. 6 / 1) Evaluation Tasks - extractive body cue:** Here we choose a comprehensive set of tasks that span various dimensions of policy capabilities from AgiBot World for evaluation, including tool-usage (Wipe Table), deformable ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** Dataset (p. 3); V. EXPERIMENT AND ANALYSIS (p. 6); 1) Evaluation Tasks (p. 6); 2) Implementation Details (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | BENCHMARK / DATASET | Fig. 7: Further analysis on: a) how model performance scales with data size, and b) the impact of filtering undesir- able data through manual ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Fig. 5: Is GO-1 a more powerful robot generalist policy? We evaluate GO-1 against previous generalist policy RDT-1B and our baseline without the latent ... | p. 7 (Figure/Table caption) |
| 2) Implementation Details | BENCHMARK / DATASET | 7(b), being larger in quantity does not necessarily translate to improved performance, while a smaller set of human-verified data yields a 0.18 boost in ... | p. 8 (2) Implementation Details) |
| 1) Evaluation Tasks | BENCHMARK / DATASET | Each episode scores 1.0 for full success, with fractional scores for partial success, enabling a nuanced performance assessment. | p. 6 (1) Evaluation Tasks) |
| Dataset | BENCHMARK / DATASET | The deployment results are adopted as feedback to improve the collection protocol. suffers from significant variability in embodiments, observation perspectives, and inconsistent data quality, ... | p. 3 (Dataset) |

## Dataset / Benchmark Role

- **p. 3 / Dataset - extractive body cue:** Based on the hardware platform developed by us, AgiBot G1, we construct AgiBot Worldan open-source robot manipulation dataset collected by more than 100 homogeneous robots, ...
- **p. 5 / Dataset - extractive body cue:** 3: Dataset Statistics. a) AgiBot World dataset covers the vast majority of robotic application scenarios, as well as a wide range of interactive objects. b) ...
- **p. 3 / Dataset - extractive body cue:** Prior datasets above generally face limitations in data scale, task practicality, and scenario naturalness, compounded by inadequate quality assurance and hardware restrictions, which impedes generalist ...
- **p. 4 / Dataset - extractive body cue:** Our dataset also features over 3,000 distinct objects, systematically categorized across various scenes.
- **p. 4 / Dataset - extractive body cue:** The dataset covers a wide range of scenarios and scene setups, ensuring both scale and diversity in the pursuit of generalizable robot policy.
- **p. 5 / Dataset - extractive body cue:** Latent Action Model Despite considerable advancements in gathering diverse robot demonstrations, the volume of action-labeled robot data remains limited relative to web-scale datasets.
- **p. 6 / V. EXPERIMENT AND ANALYSIS - extractive body cue:** We evaluate the real-world performance of policies pretrained on different data sources including the AgiBot World dataset, demonstrating the effectiveness credited from the GO-1 model ...
- **p. 6 / 1) Evaluation Tasks - extractive body cue:** Here we choose a comprehensive set of tasks that span various dimensions of policy capabilities from AgiBot World for evaluation, including tool-usage (Wipe Table), deformable ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Introducing AgiBot World Colosseo, an open-sourced large-scale manipulation platform comprising data, models, benchmarks and ecosystem. AgiBot World stands out for its unparalleled scale ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Data collection pipeline. We embrace a human-in- the-loop framework to ensure high quality, enriched with detailed annotations and error recovery behaviors. Human feedback ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Dataset Statistics. a) AgiBot World dataset covers the vast majority of robotic application scenarios, as well as a wide range of interactive objects. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: We propose GO-1, a generalist policy featuring general reasoning and long-horizon planning capabilities. The latent action model (LAM) learns universal action representations from ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Is GO-1 a more powerful robot generalist policy? We evaluate GO-1 against previous generalist policy RDT-1B and our baseline without the latent planner, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Does AgiBot World dataset improve policy per- formance and generalizability? Policies pre-trained on our dataset outperform those trained on OXE in both seen ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Further analysis on: a) how model performance scales with data size, and b) the impact of filtering undesir- able data through manual review ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Based on the hardware platform developed by us, AgiBot G1, we construct AgiBot Worldan open-source robot manipulation dataset collected by more than 100 homogeneous ... | embodiment, simulator version and control stack | p. 3 (Dataset), p. 5 (Dataset) |
| Task/environment | 3: Dataset Statistics. a) AgiBot World dataset covers the vast majority of robotic application scenarios, as well as a wide range of interactive objects. ... | reset, timeout, object/scene variation | p. 5 (Dataset), p. 3 (Dataset) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 7 (2) Implementation Details) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 7: Further analysis on: a) how model performance scales with data size, and b) the impact of filtering undesir- able data through manual ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Each episode scores 1.0 for full success, with fractional scores for partial success, enabling a nuanced performance assessment. | definition/direction/unit from same section | p. 6 (1) Evaluation Tasks) |
| Notably, the AgiBot 0.41 0.59 0.00 0.20 0.40 0.60 0.80 Num of Training Trajectories Performance Completion Score (a) Data Scalability (b) Data Quality All ... | definition/direction/unit from same section | p. 7 (2) Implementation Details) |
| 7(b), being larger in quantity does not necessarily translate to improved performance, while a smaller set of human-verified data yields a 0.18 boost in ... | definition/direction/unit from same section | p. 8 (2) Implementation Details) |
| The evaluation metric employs a normalized score, computed as the average across 10 rollouts per task, scenario, and method. | definition/direction/unit from same section | p. 6 (1) Evaluation Tasks) |
| However, they are often able to recover from these errors and successfully complete the task without requiring a full reconfiguration of the setup. | definition/direction/unit from same section | p. 4 (Dataset) |
| Notably, to expand data applicability and potential, we include imperfect data (i.e., failure recovery data with annotated error states) and tasks with dexterous hands. | definition/direction/unit from same section | p. 3 (Dataset) |
| We embrace a human-inthe-loop framework to ensure high quality, enriched with detailed annotations and error recovery behaviors. | definition/direction/unit from same section | p. 4 (Dataset) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Across all tasks and comparisons, GO-1 outperforms baselines by a large margin. | comparison identity and matched condition | p. 7 (1) Evaluation Tasks) |
| We evaluate GO-1 against previous generalist policy RDT-1B and our baseline without the latent planner, with all policies pre-trained on AgiBot World beta. | comparison identity and matched condition | p. 7 (1) Evaluation Tasks) |
| Fig. 1: Introducing AgiBot World Colosseo, an open-sourced large-scale manipulation platform comprising data, models, benchmarks and ecosystem. AgiBot World stands out for its unparalleled ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Compared to Vision-Language-Action (VLA) model where action is vision-language conditioned, the ViLLA model predicts latent action tokens, conditioned on the generation of subsequent robot ... | comparison identity and matched condition | p. 5 (Dataset) |
| Hand Failure Recovery Human-inthe-loop Collection RoboNet [11] 162k n/a 10 ✗ ✗ Single ✗ ✗ ✗ scripted BridgeData [12] 7.2k 4 12 ✗ ✗ ... | comparison identity and matched condition | p. 3 (Dataset) |
| However, they are often able to recover from these errors and successfully complete the task without requiring a full reconfiguration of the setup. | comparison identity and matched condition | p. 4 (Dataset) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We evaluate the real-world performance of policies pretrained on different data sources including the AgiBot World dataset, demonstrating the effectiveness credited from the GO-1 ... | component/input/data sensitivity | p. 6 (V. EXPERIMENT AND ANALYSIS) |
| We evaluate GO-1 against previous generalist policy RDT-1B and our baseline without the latent planner, with all policies pre-trained on AgiBot World beta. | component/input/data sensitivity | p. 7 (1) Evaluation Tasks) |
| Specifically, we provide an ablation study by fine-tuning an RDT model using both verified (528 trajectories) and unverified (482 trajectories) data from the "Wipe ... | component/input/data sensitivity | p. 8 (2) Implementation Details) |
| However, they are often able to recover from these errors and successfully complete the task without requiring a full reconfiguration of the setup. | component/input/data sensitivity | p. 4 (Dataset) |
| For instance, RDT [10] employs Diffusion Transformers, initially pre-trained on heterogeneous multirobot datasets and fine-tuned on over 6k dual-arm trajectories, showcasing the benefits of ... | component/input/data sensitivity | p. 3 (Dataset) |
| For GO1, fine-tuning is conducted with a learning rate of 2e-5, a batch size of 768, and 30,000 optimization steps. | component/input/data sensitivity | p. 7 (2) Implementation Details) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Following our dataset, to address the limitations of previous robot foundation models that heavily rely on indomain robot datasets, we present Genie Operator-1 (GO1), ... | Fig. 7: Further analysis on: a) how model performance scales with data size, and b) the impact of filtering undesir- able data through manual ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (2) Implementation Details), p. 6 (1) Evaluation Tasks), p. 3 (Dataset), p. 4 (Dataset) |
| Primary metric/result | Fig. 5: Is GO-1 a more powerful robot generalist policy? We evaluate GO-1 against previous generalist policy RDT-1B and our baseline without the latent ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 3 / Dataset - extractive body cue:** The latest version contains 1,001,552 trajectories, with a total duration of 2976.4 hours, covering 217 specific tasks, 87 skills, and 106 scenes.
- **p. 4 / Dataset - extractive body cue:** Image observations and proprioceptive states, including joint and end-effector positions, are recorded at a control frequency of 30 Hz.
- **p. 5 / Dataset - extractive body cue:** (c) Extensive Skill Set Trajectories (a) Diverse Scenarios and Objects Open X-Embodiment v1.0 DROID AgiBot World DROID OXE Line of 100 Trajectories (b) Long-Horizon Tasks ...
- **p. 5 / Dataset - extractive body cue:** 3: Dataset Statistics. a) AgiBot World dataset covers the vast majority of robotic application scenarios, as well as a wide range of interactive objects. b) ...
- **p. 5 / Dataset - extractive body cue:** In contrast, widely used datasets, such as DROID, primarily consist of trajectories ranging from 5s to 20s, while OXE v1.0 predominantly contains trajectories within 5s. ...
- **p. 6 / 1) Evaluation Tasks - extractive body cue:** The evaluation metric employs a normalized score, computed as the average across 10 rollouts per task, scenario, and method.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Notably, to expand data applicability and potential, we include imperfect data (i.e., failure recovery data with annotated error states) and tasks with dexterous hands. | p. 3 (Dataset) |
| body limitation/failure cue | Hand Failure Recovery Human-inthe-loop Collection RoboNet [11] 162k n/a 10 ✗ ✗ Single ✗ ✗ ✗ scripted BridgeData [12] 7.2k 4 12 ✗ ✗ ... | p. 3 (Dataset) |
| body limitation/failure cue | These trajectories, referred to as failure recovery data, constitute approximately one percent of the dataset. | p. 4 (Dataset) |
| body limitation/failure cue | Teleoperator Training Data Collection Data Upload Data Processing Quality Check Failure Recovery Annotation Data Delivery Data Discard No: Discard Edge-side Cloud-side Task Succeed Failed ... | p. 4 (Dataset) |
| body limitation/failure cue | 7(b), being larger in quantity does not necessarily translate to improved performance, while a smaller set of human-verified data yields a 0.18 boost in ... | p. 8 (2) Implementation Details) |
| body limitation/failure cue | This ensures that our dataset adequately represents a broad spectrum of skills, providing sufficient data for each to support robust policy learning. | p. 5 (Dataset) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For GO1, fine-tuning is conducted with a learning rate of 2e-5, a batch size of 768, and 30,000 optimization steps. | p. 7 (2) Implementation Details) |
| The evaluation metric employs a normalized score, computed as the average across 10 rollouts per task, scenario, and method. | p. 6 (1) Evaluation Tasks) |
| 5, are averaged over 30 trials per task, with 10 trials conducted in a seen setup and 20 trials under variations or distractions. | p. 7 (2) Implementation Details) |
| The dataset is available under the CC BY-NC-SA 4.0 license, along with the model checkpoints and code. | p. 3 (Dataset) |
| The action expert decodes low-level action chunks, denoted by At = [at,at+1,...,at+H] with H = 30, using proprioceptive state pt over an interval of ... | p. 6 (Dataset) |
| We replicate real-world environment at a 1:1 scale for the industrial and retail scenarios, which are barely present before. | p. 3 (Dataset) |
| AgiBot World provides extensive coverage across five key domains: domestic, retail, industrial, restaurant, and office environments. | p. 4 (Dataset) |
| The latent action tokens are quantized using a VQ-VAE objective [32], with a codebook of size /C/. | p. 5 (Dataset) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / Dataset - extractive body cue:** Notably, to expand data applicability and potential, we include imperfect data (i.e., failure recovery data with annotated error states) and tasks with dexterous hands.
- **p. 3 / Dataset - extractive body cue:** Hand Failure Recovery Human-inthe-loop Collection RoboNet [11] 162k n/a 10 ✗ ✗ Single ✗ ✗ ✗ scripted BridgeData [12] 7.2k 4 12 ✗ ✗ Single ...
- **p. 4 / Dataset - extractive body cue:** These trajectories, referred to as failure recovery data, constitute approximately one percent of the dataset.
- **p. 4 / Dataset - extractive body cue:** Teleoperator Training Data Collection Data Upload Data Processing Quality Check Failure Recovery Annotation Data Delivery Data Discard No: Discard Edge-side Cloud-side Task Succeed Failed No ...
- **p. 8 / 2) Implementation Details - extractive body cue:** 7(b), being larger in quantity does not necessarily translate to improved performance, while a smaller set of human-verified data yields a 0.18 boost in the ...
- **p. 5 / Dataset - extractive body cue:** This ensures that our dataset adequately represents a broad spectrum of skills, providing sufficient data for each to support robust policy learning.

- **PDF anchors reviewed:** datasets p. 3 (Dataset), p. 5 (Dataset), p. 3 (Dataset), p. 4 (Dataset), p. 4 (Dataset), p. 5 (Dataset), metrics p. 7 (Figure/Table caption), p. 6 (1) Evaluation Tasks), p. 7 (2) Implementation Details), p. 8 (2) Implementation Details), p. 6 (1) Evaluation Tasks), p. 4 (Dataset), baselines p. 7 (1) Evaluation Tasks), p. 7 (1) Evaluation Tasks), p. 1 (Figure/Table caption), p. 5 (Dataset), p. 3 (Dataset), p. 4 (Dataset), results p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (2) Implementation Details), p. 6 (1) Evaluation Tasks), p. 3 (Dataset), p. 4 (Dataset).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
