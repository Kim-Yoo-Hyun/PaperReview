# Evaluation - RoboNet: Large-Scale Multi-Robot Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v100/dasari20a.html; PDF retrieval source: https://proceedings.mlr.press/v100/dasari20a.html. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 13 (C Database Implementation Details), p. 13 (C Database Implementation Details)): Table 5: Evaluation results for adaptation to an unseen Baxter robot. The model pre-trained on RoboNet's Sawyer data, achieves the best performance when fine- tuned with 300 trajectories from the

## Evaluation Body Digest

- **p. 13 / C Database Implementation Details - extractive PDF cue:** However, these results do demonstrate that visual foresight models can adapt to moderate morphological changes using a modest amount of data. t = 0 t ...
- **p. 13 / C Database Implementation Details - extractive PDF cue:** Held out viewpoint Training viewpoints Franka Panda KUKA Sawyer Figure 7: Experimental setups for benchmarking tasks on the Kuka, Franka, and Sawyer robots.
- **p. 12 / C Database Implementation Details - extractive PDF cue:** D Description of Benchmarking Tasks For all control benchmarks we used object relocation tasks from a set of fixed initial positions towards a set of ...
- **p. 12 / C Database Implementation Details - extractive PDF cue:** The experimental setups for each robot are depicted in Figure 7.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2: Evaluation of viewpoint generalization, showing the average distance to the goal after ex- ecuting the action sequence and standard error. A model trained ...
- **p. 13 / C Database Implementation Details - extractive PDF cue:** executing the action sequences computed by the algorithm the remaining distance to the goal is measured using a tape, and success is determined by human ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 5: Evaluation results for adaptation to an unseen Baxter robot. The model pre-trained on RoboNet's Sawyer data, achieves the best performance when fine- tuned ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 6: Inverse model results on 5 reaching tasks. The model is success- ful across multiple robot platforms and generalizes to a new viewpoint. To ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** C Database Implementation Details (p. 12).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | BENCHMARK / DATASET | Table 5: Evaluation results for adaptation to an unseen Baxter robot. The model pre-trained on RoboNet's Sawyer data, achieves the best performance when fine- ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Figure 4: Example task of grasping and moving a thin plastic cup with the Franka robot, using visual foresight pre-trained on RoboNet w/o Franka ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Table 6: Inverse model results on 5 reaching tasks. The model is success- ful across multiple robot platforms and generalizes to a new viewpoint. ... | p. 7 (Figure/Table caption) |
| C Database Implementation Details | BENCHMARK / DATASET | The results qualitative results of this evaluation are shown in Figure 8 and the quantitative results are in Table 7, averaging over 10 trajectories ... | p. 13 (C Database Implementation Details) |
| C Database Implementation Details | BENCHMARK / DATASET | executing the action sequences computed by the algorithm the remaining distance to the goal is measured using a tape, and success is determined by ... | p. 13 (C Database Implementation Details) |

## Dataset / Benchmark Role

- **p. 13 / C Database Implementation Details - extractive PDF cue:** However, these results do demonstrate that visual foresight models can adapt to moderate morphological changes using a modest amount of data. t = 0 t ...
- **p. 13 / C Database Implementation Details - extractive PDF cue:** Held out viewpoint Training viewpoints Franka Panda KUKA Sawyer Figure 7: Experimental setups for benchmarking tasks on the Kuka, Franka, and Sawyer robots.
- **p. 12 / C Database Implementation Details - extractive PDF cue:** D Description of Benchmarking Tasks For all control benchmarks we used object relocation tasks from a set of fixed initial positions towards a set of ...
- **p. 12 / C Database Implementation Details - extractive PDF cue:** The experimental setups for each robot are depicted in Figure 7.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: A glimpse of the RoboNet dataset, with example trajectories, robots, and viewpoints. We collected data with Sawyer, Franka, WidowX, Kuka, and Baxter robots, ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 2: Qualitative examples of the various attributes in the RoboNet dataset. Robot type (number of trajectories) Sawyer (68k), Baxter (18k), WidowX (5k), Franka (7.9k),
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1: Quantitative overview of the various attributes in the RoboNet dataset, including the 6 different robot arms and 6 different grippers. 5 Robot-Agnostic Visual ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3: Zero-shot generalization to new back- grounds with a model trained across multiple views. Avg. dist. (cm) seen view Avg. dist. (cm) held-out view ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2: Evaluation of viewpoint generalization, showing the average distance to the goal after ex- ecuting the action sequence and standard error. A model trained ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 3: Results for adaptation to an unseen Kuka robot. The model pre-trained on RoboNet without the Kuka, R3, and Fetch data, achieves the best ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 4: Results for adapta- tion to an unseen Franka robot. The model pre-trained on RoboNet without the Franka, R3, and Fetch data, achieves the ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 5: Evaluation results for adaptation to an unseen Baxter robot. The model pre-trained on RoboNet's Sawyer data, achieves the best performance when fine- tuned ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | However, these results do demonstrate that visual foresight models can adapt to moderate morphological changes using a modest amount of data. t = 0 ... | embodiment, simulator version and control stack | p. 13 (C Database Implementation Details), p. 13 (C Database Implementation Details) |
| Task/environment | Held out viewpoint Training viewpoints Franka Panda KUKA Sawyer Figure 7: Experimental setups for benchmarking tasks on the Kuka, Franka, and Sawyer robots. | reset, timeout, object/scene variation | p. 13 (C Database Implementation Details), p. 12 (C Database Implementation Details) |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 2 (1 Introduction), p. 13 (C Database Implementation Details) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 2: Evaluation of viewpoint generalization, showing the average distance to the goal after ex- ecuting the action sequence and standard error. A model ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| executing the action sequences computed by the algorithm the remaining distance to the goal is measured using a tape, and success is determined by ... | definition/direction/unit from same section | p. 13 (C Database Implementation Details) |
| Table 5: Evaluation results for adaptation to an unseen Baxter robot. The model pre-trained on RoboNet's Sawyer data, achieves the best performance when fine- ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 6: Inverse model results on 5 reaching tasks. The model is success- ful across multiple robot platforms and generalizes to a new viewpoint. ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| The database stores every trajectory as a separate entity with a set of attributes that can be filtered. | definition/direction/unit from same section | p. 12 (C Database Implementation Details) |
| Figure 8: Example task of pushing an object with an unseen gripper, in this case the Robotiq gripper. Avg. distance (cm) zero-shot 15.5 ± ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 4: Results for adapta- tion to an unseen Franka robot. The model pre-trained on RoboNet without the Franka, R3, and Fetch data, achieves ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Figure 8: Example task of pushing an object with an unseen gripper, in this case the Robotiq gripper. Avg. distance (cm) zero-shot 15.5 ± ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |
| Avg. distance (cm) zero-shot 15.5 ± 2.6 without pretraining 17 ± 1.8 pretraining on Sawyer-only 9.8 ± 2.1 pretraining on all of RoboNet 14.7 ... | comparison identity and matched condition | p. 13 (C Database Implementation Details) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 4: Results for adapta- tion to an unseen Franka robot. The model pre-trained on RoboNet without the Franka, R3, and Fetch data, achieves ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Figure 8: Example task of pushing an object with an unseen gripper, in this case the Robotiq gripper. Avg. distance (cm) zero-shot 15.5 ± ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |
| Avg. distance (cm) zero-shot 15.5 ± 2.6 without pretraining 17 ± 1.8 pretraining on Sawyer-only 9.8 ± 2.1 pretraining on all of RoboNet 14.7 ... | component/input/data sensitivity | p. 13 (C Database Implementation Details) |
| Figure 4: Example task of grasping and moving a thin plastic cup with the Franka robot, using visual foresight pre-trained on RoboNet w/o Franka ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions therefore consist of the RoboNet dataset, and an experimental evaluation that studies our framework for multi-robot, multi-domain model-based reinforcement learning based ... | Table 5: Evaluation results for adaptation to an unseen Baxter robot. The model pre-trained on RoboNet's Sawyer data, achieves the best performance when fine- ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 13 (C Database Implementation Details), p. 13 (C Database Implementation Details) |
| Primary metric/result | Figure 4: Example task of grasping and moving a thin plastic cup with the Franka robot, using visual foresight pre-trained on RoboNet w/o Franka ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 13 / C Database Implementation Details - extractive PDF cue:** The results qualitative results of this evaluation are shown in Figure 8 and the quantitative results are in Table 7, averaging over 10 trajectories each.
- **p. 13 / C Database Implementation Details - extractive PDF cue:** Avg. distance (cm) zero-shot 15.5 ± 2.6 without pretraining 17 ± 1.8 pretraining on Sawyer-only 9.8 ± 2.1 pretraining on all of RoboNet 14.7 ± ...
- **p. 13 / C Database Implementation Details - extractive PDF cue:** The model trained on only Sawyer data performs the best when fine-tuned on 300 trajectories with a Robotiq gripper.
- **p. 13 / C Database Implementation Details - extractive PDF cue:** The results qualitative results of this evaluation are shown in Figure 8 and the quantitative results are in Table 7, averaging over 10 trajectories each.
- **p. 13 / C Database Implementation Details - extractive PDF cue:** Avg. distance (cm) zero-shot 15.5 ± 2.6 without pretraining 17 ± 1.8 pretraining on Sawyer-only 9.8 ± 2.1 pretraining on all of RoboNet 14.7 ± ...
- **p. 13 / C Database Implementation Details - extractive PDF cue:** The model trained on only Sawyer data performs the best when fine-tuned on 300 trajectories with a Robotiq gripper.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Next, we discuss limitations of the dataset and evaluation, and additional directions for future work. | p. 8 (6 Discussion) |
| body limitation/failure cue | While our results demonstrated a large degree of generalization, a number of important limitations remain, which we aim to study in future work. | p. 8 (6 Discussion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Data is stored in the widely adopted hdf5-format, and videos are encoded via MP4 for efficiency reasons. | p. 12 (C Database Implementation Details) |
| We provide code infrastructure that allows a user to filter certain subsets of attributes for training and testing. | p. 12 (C Database Implementation Details) |
| executing the action sequences computed by the algorithm the remaining distance to the goal is measured using a tape, and success is determined by ... | p. 13 (C Database Implementation Details) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6 Discussion - extractive PDF cue:** Next, we discuss limitations of the dataset and evaluation, and additional directions for future work.
- **p. 8 / 6 Discussion - extractive PDF cue:** While our results demonstrated a large degree of generalization, a number of important limitations remain, which we aim to study in future work.

- **PDF anchors reviewed:** datasets p. 13 (C Database Implementation Details), p. 13 (C Database Implementation Details), p. 12 (C Database Implementation Details), p. 12 (C Database Implementation Details), metrics p. 6 (Figure/Table caption), p. 13 (C Database Implementation Details), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 12 (C Database Implementation Details), p. 13 (Figure/Table caption), baselines p. 6 (Figure/Table caption), p. 13 (Figure/Table caption), p. 13 (C Database Implementation Details), results p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 13 (C Database Implementation Details), p. 13 (C Database Implementation Details).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
