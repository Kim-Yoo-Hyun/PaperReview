# Evaluation - DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2403.12945; PDF retrieval source: https://arxiv.org/pdf/2403.12945. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (Figure/Table caption), p. 7 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 1 (Figure/Table caption), p. 8 (V. EXPERIMENTS), p. 20 (Figure/Table caption)): Fig. 8: Does DROID Improve Policy Performance and Robustness? We find that across all our evaluation tasks, co-training with DROID significantly improves both in distribution and OOD performance over both ...

## Evaluation Body Digest

- **p. 5 / IV. DROID DATASET ANALYSIS - extractive body cue:** Overall, we find that DROID significantly increases diversity in tasks, objects, scenes, viewpoints and interaction locations over existing large scale robot manipulation datasets.
- **p. 3 / Dataset - extractive body cue:** Calibration Public Robot Collection MIME [50] 8.3k 20 1 ✗ ✗ ✓ human teleop RoboTurk [36] 2.1k 2 1 ✗ ✗ ✓ human teleop RoboNet ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** To test how DROID and existing datasets affect policy robustness, we evaluate each task and method in two settings: "in-distribution," which reflects the distribution of ...
- **p. 3 / Dataset - extractive body cue:** As a result, DROID contains data from 564 scenes across 52 buildings, a substantial increase compared to any existing robot manipulation dataset.
- **p. 6 / IV. DROID DATASET ANALYSIS - extractive body cue:** DROID contains 564 unique scenes, an order of magnitude more than existing large robot manipulation datasets.
- **p. 8 / V. EXPERIMENTS - extractive body cue:** OXE contains most of the existing large robot manipulation datasets we compared DROID to in Section IV, as well as a large number of other ...
- **p. 5 / IV. DROID DATASET ANALYSIS - extractive body cue:** A key reason is DROID's data collection protocol (see Section III-B): by collecting data with 50 data collectors in 52 buildings across three continents, switching ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** The analysis in the previous section highlighted the diversity of tasks, objects, scenes, and viewpoints in the DROID dataset.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** Dataset (p. 3); IV. DROID DATASET ANALYSIS (p. 5); V. EXPERIMENTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | BENCHMARK / DATASET | Fig. 8: Does DROID Improve Policy Performance and Robustness? We find that across all our evaluation tasks, co-training with DROID significantly improves both in ... | p. 9 (Figure/Table caption) |
| V. EXPERIMENTS | BENCHMARK / DATASET | Across the board, we find that DROID improves policy success rate while increasing robustness to scene changes like distractors or novel object instances. | p. 7 (V. EXPERIMENTS) |
| V. EXPERIMENTS | BENCHMARK / DATASET | Across all tasks, we find that DROID substantially improves policy performance compared to the diffusion policy trained on in-domain data only. | p. 8 (V. EXPERIMENTS) |
| Figure/Table caption | BENCHMARK / DATASET | Fig. 1: We introduce DROID (Distributed Robot Interaction Dataset), an "in-the-wild" robot manipulation dataset with 76k trajectories or 350 hours of interaction data, collected ... | p. 1 (Figure/Table caption) |
| V. EXPERIMENTS | BENCHMARK / DATASET | While we've seen the benefits of co-training with DROID, can we quantify how much of a role scene diversity plays in improved policy robustness? | p. 8 (V. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 5 / IV. DROID DATASET ANALYSIS - extractive body cue:** Overall, we find that DROID significantly increases diversity in tasks, objects, scenes, viewpoints and interaction locations over existing large scale robot manipulation datasets.
- **p. 3 / Dataset - extractive body cue:** Calibration Public Robot Collection MIME [50] 8.3k 20 1 ✗ ✗ ✓ human teleop RoboTurk [36] 2.1k 2 1 ✗ ✗ ✓ human teleop RoboNet ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** To test how DROID and existing datasets affect policy robustness, we evaluate each task and method in two settings: "in-distribution," which reflects the distribution of ...
- **p. 3 / Dataset - extractive body cue:** As a result, DROID contains data from 564 scenes across 52 buildings, a substantial increase compared to any existing robot manipulation dataset.
- **p. 6 / IV. DROID DATASET ANALYSIS - extractive body cue:** DROID contains 564 unique scenes, an order of magnitude more than existing large robot manipulation datasets.
- **p. 8 / V. EXPERIMENTS - extractive body cue:** OXE contains most of the existing large robot manipulation datasets we compared DROID to in Section IV, as well as a large number of other ...
- **p. 5 / IV. DROID DATASET ANALYSIS - extractive body cue:** A key reason is DROID's data collection protocol (see Section III-B): by collecting data with 50 data collectors in 52 buildings across three continents, switching ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** The analysis in the previous section highlighted the diversity of tasks, objects, scenes, and viewpoints in the DROID dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We introduce DROID (Distributed Robot Interaction Dataset), an "in-the-wild" robot manipulation dataset with 76k trajectories or 350 hours of interaction data, collected across ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: The DROID robot platform. We use the same hardware setup across all 13 institutions to streamline data collection while maximizing portability and flexibility. ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Distribution of verbs and objects in DROID. Top: Distribution of verbs after de-duplication with GPT-4. DROID has a long tail of diverse tasks ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Number of scenes per scene type. DROID has an order of magnitude more scenes than other large robot manipulation datasets, spanning a much ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Third-person camera viewpoints in DROID (subsampled). DROID episodes cover a total of 1417 camera viewpoints along with intrinsic and extrinsic stereo camera calibration. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Visualization of 3D interaction points relative to the robot base. We visualize the 3D location at which the gripper first closes in each ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Robot setups for policy evaluation. We cover a wide range of tasks and scenes, from lab evaluations to offices and real households, to ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 8: Does DROID Improve Policy Performance and Robustness? We find that across all our evaluation tasks, co-training with DROID significantly improves both in distribution ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Overall, we find that DROID significantly increases diversity in tasks, objects, scenes, viewpoints and interaction locations over existing large scale robot manipulation datasets. | embodiment, simulator version and control stack | p. 5 (IV. DROID DATASET ANALYSIS), p. 3 (Dataset) |
| Task/environment | Calibration Public Robot Collection MIME [50] 8.3k 20 1 ✗ ✗ ✓ human teleop RoboTurk [36] 2.1k 2 1 ✗ ✗ ✓ human teleop ... | reset, timeout, object/scene variation | p. 3 (Dataset), p. 8 (V. EXPERIMENTS) |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 4 (III. DROID DATA COLLECTION SETUP), p. 2 (I. INTRODUCTION) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 2 (I. INTRODUCTION), p. 3 (Dataset) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 8: Does DROID Improve Policy Performance and Robustness? We find that across all our evaluation tasks, co-training with DROID significantly improves both in ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Across the board, we find that DROID improves policy success rate while increasing robustness to scene changes like distractors or novel object instances. | definition/direction/unit from same section | p. 7 (V. EXPERIMENTS) |
| Fig. 17: Distribution of respective metrics i.e. IOU and mean reprojection errors after thresholding and filtering with the strategy outlined in Sec. G-A and ... | definition/direction/unit from same section | p. 22 (Figure/Table caption) |
| Fig. 1: We introduce DROID (Distributed Robot Interaction Dataset), an "in-the-wild" robot manipulation dataset with 76k trajectories or 350 hours of interaction data, collected ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| In this section, we investigate whether this diverse data resource can be used to boost policy performance and robustness across | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| To this end, we use diffusion policies [7, 16, 21, 38, 54], which leverage denoising diffusion models for action prediction and have recently demonstrated ... | definition/direction/unit from same section | p. 7 (V. EXPERIMENTS) |
| This difference is especially notable 3We use a curated split of OXE based on Octo Model Team et al. | definition/direction/unit from same section | p. 8 (V. EXPERIMENTS) |
| Across all tasks, we find that DROID substantially improves policy performance compared to the diffusion policy trained on in-domain data only. | definition/direction/unit from same section | p. 8 (V. EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| One of the unique benefits of DROID compared to existing robot datasets is its amount of scene diversity. | comparison identity and matched condition | p. 8 (V. EXPERIMENTS) |
| Across all tasks, we find that DROID substantially improves policy performance compared to the diffusion policy trained on in-domain data only. | comparison identity and matched condition | p. 8 (V. EXPERIMENTS) |
| We compare success rate averaged across all tasks with standard error, and find DROID outperforms the next best method by 22% absolute success rate ... | comparison identity and matched condition | p. 9 (V. EXPERIMENTS) |
| By comparing Figure 10's individual task performances with the corresponding tasks in Figure 8, we also see that the performance of co-training with the ... | comparison identity and matched condition | p. 9 (V. EXPERIMENTS) |
| In line with prior work [7], we train the diffusion policy to generate 16-step action sequences, and during rollouts, step 8 actions open loop ... | comparison identity and matched condition | p. 7 (V. EXPERIMENTS) |
| As such, we build on existing state-of-the-art 2Fang et al. | comparison identity and matched condition | p. 3 (Dataset) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We then use GPT4 to de-duplicate the verbs, i.e., remove synonyms and typos. | component/input/data sensitivity | p. 6 (IV. DROID DATASET ANALYSIS) |
| The out of distribution variant consists of toasting novel objects. | component/input/data sensitivity | p. 7 (V. EXPERIMENTS) |
| The out of distribution variant involves placing a distractor plate on the table. | component/input/data sensitivity | p. 7 (V. EXPERIMENTS) |
| Cook Lentils: The robot needs to remove the pan lid, pick up and pour lentils into the pan, and turn on the stove(add distractor ... | component/input/data sensitivity | p. 8 (V. EXPERIMENTS) |
| We remove the Language Table dataset [35], equivalent to 5% of the Octo training mix, due to its repetitive scene layouts and tasks, and ... | component/input/data sensitivity | p. 8 (V. EXPERIMENTS) |
| Fig. 11: DROID data collection GUI. Top left: Screen for entering feasible tasks for the current scene. Tasks can either be selected from a ... | component/input/data sensitivity | p. 16 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, we introduce DROID (Distributed Robot Interaction Dataset), a robot manipulation dataset of unprecedented diversity (see Fig. | Fig. 8: Does DROID Improve Policy Performance and Robustness? We find that across all our evaluation tasks, co-training with DROID significantly improves both in ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (Figure/Table caption), p. 7 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 1 (Figure/Table caption), p. 8 (V. EXPERIMENTS), p. 20 (Figure/Table caption) |
| Primary metric/result | Across the board, we find that DROID improves policy success rate while increasing robustness to scene changes like distractors or novel object instances. | numeric claim only at cited anchor | p. 7 (V. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 3 / Dataset - extractive body cue:** As a result, DROID contains data from 564 scenes across 52 buildings, a substantial increase compared to any existing robot manipulation dataset.
- **p. 6 / IV. DROID DATASET ANALYSIS - extractive body cue:** 2000 trajectories than whether it has 0 vs.
- **p. 6 / IV. DROID DATASET ANALYSIS - extractive body cue:** It shows that DROID not only contains diverse objects, but also a diverse range of interactions with most objects. c) Scene diversity: We define 10 ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** To this end, we train policies across 6 tasks in 4 different locations including lab, office, and household settings, to reflect the diversity of real ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** 7, we choose 6 tasks in 4 locations that span a representative range of real robot learning use cases: from simple pick-place tasks to multistage ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Concretely, we evaluate on the following 6 tasks, each with their own out-of-distribution variants: Closing Waffle Maker: A short horizon task in a lab setting ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | To test how DROID and existing datasets affect policy robustness, we evaluate each task and method in two settings: "in-distribution," which reflects the distribution ... | p. 8 (V. EXPERIMENTS) |
| body limitation/failure cue | Fig. 11: DROID data collection GUI. Top left: Screen for entering feasible tasks for the current scene. Tasks can either be selected from a ... | p. 16 (Figure/Table caption) |
| body limitation/failure cue | Fig. 8: Does DROID Improve Policy Performance and Robustness? We find that across all our evaluation tasks, co-training with DROID significantly improves both in ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | Fig. 12: Qualitative examples of scenes in DROID. We use GPT-4V to categorize scenes into 9 scene types. DROID contains robot manipulation demonstrations in ... | p. 17 (Figure/Table caption) |
| body limitation/failure cue | Our policy learning evaluations show that DROID is a valuable data resource for improving policy performance and robustness, even in comparison to existing large ... | p. 9 (VI. DISCUSSION) |
| body limitation/failure cue | Calibration Public Robot Collection MIME [50] 8.3k 20 1 ✗ ✗ ✓ human teleop RoboTurk [36] 2.1k 2 1 ✗ ✗ ✓ human teleop ... | p. 3 (Dataset) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| This includes the full dataset under CC-BY 4.0 license, an interactive dataset visualizer, code for training generalizable policies on DROID, pre-trained policy checkpoints, and ... | p. 3 (III. DROID DATA COLLECTION SETUP) |
| All experiments use the DROID hardware stack for policy evaluations. | p. 7 (V. EXPERIMENTS) |
| We first downsample the camera observations to a resolution of 128 × 128 and use a ResNet-50 visual encoder pre-trained on ImageNet [11] to ... | p. 7 (V. EXPERIMENTS) |
| Similarly, in the multi-step Cook Lentils task, baselines tend to fail after two or sometimes just one step, while co-training with DROID is the ... | p. 8 (V. EXPERIMENTS) |
| Additionally, collecting data at scale requires substantial investments in hardware and human labour for supervision, particularly for collecting demonstration data. | p. 2 (I. INTRODUCTION) |
| To streamline distributed data collection and ensure applicability of the final dataset to a wide range of research settings, all data is collected on ... | p. 2 (I. INTRODUCTION) |
| In this section, we introduce our hardware setup and the data collection protocol. | p. 3 (III. DROID DATA COLLECTION SETUP) |
| We provide a thoroughly tested guide to replicate the hardware and software of our setup. | p. 4 (III. DROID DATA COLLECTION SETUP) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / V. EXPERIMENTS - extractive body cue:** To test how DROID and existing datasets affect policy robustness, we evaluate each task and method in two settings: "in-distribution," which reflects the distribution of ...
- **p. 16 / Figure/Table caption - extractive body cue:** Fig. 11: DROID data collection GUI. Top left: Screen for entering feasible tasks for the current scene. Tasks can either be selected from a list ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 8: Does DROID Improve Policy Performance and Robustness? We find that across all our evaluation tasks, co-training with DROID significantly improves both in distribution ...
- **p. 17 / Figure/Table caption - extractive body cue:** Fig. 12: Qualitative examples of scenes in DROID. We use GPT-4V to categorize scenes into 9 scene types. DROID contains robot manipulation demonstrations in a ...
- **p. 9 / VI. DISCUSSION - extractive body cue:** Our policy learning evaluations show that DROID is a valuable data resource for improving policy performance and robustness, even in comparison to existing large robot ...
- **p. 3 / Dataset - extractive body cue:** Calibration Public Robot Collection MIME [50] 8.3k 20 1 ✗ ✗ ✓ human teleop RoboTurk [36] 2.1k 2 1 ✗ ✗ ✓ human teleop RoboNet ...

- **PDF anchors reviewed:** datasets p. 5 (IV. DROID DATASET ANALYSIS), p. 3 (Dataset), p. 8 (V. EXPERIMENTS), p. 3 (Dataset), p. 6 (IV. DROID DATASET ANALYSIS), p. 8 (V. EXPERIMENTS), metrics p. 9 (Figure/Table caption), p. 7 (V. EXPERIMENTS), p. 22 (Figure/Table caption), p. 1 (Figure/Table caption), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), baselines p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 3 (Dataset), results p. 9 (Figure/Table caption), p. 7 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 1 (Figure/Table caption), p. 8 (V. EXPERIMENTS), p. 20 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
