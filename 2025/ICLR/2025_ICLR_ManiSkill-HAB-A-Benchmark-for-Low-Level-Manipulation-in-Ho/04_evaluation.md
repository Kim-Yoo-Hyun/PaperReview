# Evaluation - ManiSkill-HAB: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=6bKEWevgSd; PDF retrieval source: https://arxiv.org/pdf/2412.13211. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (6 RESULTS), p. 10 (6 RESULTS), p. 19 (Figure/Table caption), p. 9 (6 RESULTS), p. 8 (6 RESULTS), p. 10 (6 RESULTS)): Even with per-object RL policies, our low-level mobile manipulation subtasks are difficult to train on dense reward, and improving subtask success rate is the most direct way to improve overall ...

## Evaluation Body Digest

- **p. 9 / 6 RESULTS - extractive PDF cue:** This is not an issue with magical grasping (Gu et al., 2023a), indicating that low-level control may need more scene diversity. pick_0 place_0 pick_1 place_1 ...
- **p. 18 / A.4.1 DATASET SIZE - extractive PDF cue:** DEMOS SoR 1 0.00 ± 0.00 10 0.02 ± 0.03 100 0.27 ± 0.19 500 0.53 ± 0.13 1000 0.62 ± 0.09 To highlight the ...
- **p. 10 / 6 RESULTS - extractive PDF cue:** We generate 3 datasets with 500 demonstrations per object: 1) place in goal only, 2) drop in goal only, and 3) 50/50 split ("place", "drop", ...
- **p. 18 / A.4.1 DATASET SIZE - extractive PDF cue:** In Table 4, we run 1000 evaluation episodes per policy, and group results by demonstrations per object.
- **p. 22 / A.6.1 DATASET FILTERING AND GENERATION - extractive PDF cue:** We generate 1000 demonstrations per object/articulation for each subtask using per-object RL policies on the train split.
- **p. 9 / 6 RESULTS - extractive PDF cue:** Published as a conference paper at ICLR 2025 validation split, the Close Fridge policy completely fails on validation scenes because the fridge door opens into ...
- **p. 10 / 6 RESULTS - extractive PDF cue:** TASK SPLIT TYPE S-ONCE F-COL F-GRASP F-OTHER TidyHouse Train RL-All 29.46 34.52 28.17 7.85 RL-Per 71.63 17.26 2.48 8.63 Val RL-All 33.73 33.13 24.50 8.64 ...
- **p. 17 / A.3 RL SUBTASK EVALUATION CURVES - extractive PDF cue:** During training, we evaluate our policies every 10000 steps on 189 episodes.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 6 RESULTS (p. 8); A.3 RL SUBTASK EVALUATION CURVES (p. 17); A.4 ADDITIONAL EXPERIMENTS (p. 18); A.4.1 DATASET SIZE (p. 18); A.6 TRAJECTORY CATEGORIZATION AND DATASET FILTERING (p. 22); A.6.1 DATASET FILTERING AND GENERATION (p. 22).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 6 RESULTS | BENCHMARK / DATASET | Even with per-object RL policies, our low-level mobile manipulation subtasks are difficult to train on dense reward, and improving subtask success rate is the ... | p. 8 (6 RESULTS) |
| 6 RESULTS | BENCHMARK / DATASET | Does training per-object Pick and Place policies improve subtask success rate compared to allobject policies? | p. 10 (6 RESULTS) |
| Figure/Table caption | BENCHMARK / DATASET | Figure 8: SAC vs PPO subtask success once rate (%) curves on the train split. Lines are averaged across 3 seeds; since success rate ... | p. 19 (Figure/Table caption) |
| 6 RESULTS | BENCHMARK / DATASET | Futhermore, we provide an ‘upper bound' on performance based on the success rates of each subtask policy. | p. 9 (6 RESULTS) |
| 6 RESULTS | BENCHMARK / DATASET | First, our optimistic upper bound shows low expected success rate on the long-horizon tasks. | p. 8 (6 RESULTS) |

## Dataset / Benchmark Role

- **p. 9 / 6 RESULTS - extractive PDF cue:** This is not an issue with magical grasping (Gu et al., 2023a), indicating that low-level control may need more scene diversity. pick_0 place_0 pick_1 place_1 ...
- **p. 18 / A.4.1 DATASET SIZE - extractive PDF cue:** DEMOS SoR 1 0.00 ± 0.00 10 0.02 ± 0.03 100 0.27 ± 0.19 500 0.53 ± 0.13 1000 0.62 ± 0.09 To highlight the ...
- **p. 10 / 6 RESULTS - extractive PDF cue:** We generate 3 datasets with 500 demonstrations per object: 1) place in goal only, 2) drop in goal only, and 3) 50/50 split ("place", "drop", ...
- **p. 18 / A.4.1 DATASET SIZE - extractive PDF cue:** In Table 4, we run 1000 evaluation episodes per policy, and group results by demonstrations per object.
- **p. 22 / A.6.1 DATASET FILTERING AND GENERATION - extractive PDF cue:** We generate 1000 demonstrations per object/articulation for each subtask using per-object RL policies on the train split.
- **p. 9 / 6 RESULTS - extractive PDF cue:** Published as a conference paper at ICLR 2025 validation split, the Close Fridge policy completely fails on validation scenes because the fridge door opens into ...
- **p. 10 / 6 RESULTS - extractive PDF cue:** TASK SPLIT TYPE S-ONCE F-COL F-GRASP F-OTHER TidyHouse Train RL-All 29.46 34.52 28.17 7.85 RL-Per 71.63 17.26 2.48 8.63 Val RL-All 33.73 33.13 24.50 8.64 ...
- **p. 17 / A.3 RL SUBTASK EVALUATION CURVES - extractive PDF cue:** During training, we evaluate our policies every 10000 steps on 189 episodes.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Live-rendered frames taken from ManiSkill-HAB environments while running policy roll- outs with skill chaining. Ray-tracing enabled. Full videos available on website.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 2: Interact benchmark comparing MS-HAB (ours) with Habitat. Each data point is annotated with the number of parallel environments used. SPS and GPU memory ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3: Renders of low-level, whole-body control policies solving Pick, Place, Open, and Close subtasks. We render 1 512x512 image and 4 128x128 sensor images. ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 4: Long-horizon task progressive completion rates (%) on train and validation splits averaged over 1000 episodes. Futhermore, we provide an ‘upper bound' on performance ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 1: Subtask success once rates for RL and IL baselines. The RL-Per vs All column shows the difference in per-object RL policy performance and ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 2: Trajectory labeling on Pick Cracker Box with all and per-object RL policies. We group the trajectories into four categories: success once (S-Once), excessive ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Table 3: Success once rate (S-Once, %) and ratio of "place in goal" to "drop to goal" trajectories (Place : Drop). Note that some success ...
- **p. 17 / Figure/Table caption - extractive PDF cue:** Figure 5: Per-object vs all-object RL success once rate (%) evaluation curves for Pick and Place policies across tasks. We run 3 seeds for each ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This is not an issue with magical grasping (Gu et al., 2023a), indicating that low-level control may need more scene diversity. pick_0 place_0 pick_1 ... | embodiment, simulator version and control stack | p. 9 (6 RESULTS), p. 18 (A.4.1 DATASET SIZE) |
| Task/environment | DEMOS SoR 1 0.00 ± 0.00 10 0.02 ± 0.03 100 0.27 ± 0.19 500 0.53 ± 0.13 1000 0.62 ± 0.09 To highlight ... | reset, timeout, object/scene variation | p. 18 (A.4.1 DATASET SIZE), p. 10 (6 RESULTS) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 4 (3 PRELIMINARIES), p. 6 (5 METHODOLOGY) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 5 (3 PRELIMINARIES), p. 7 (5 METHODOLOGY) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Even with per-object RL policies, our low-level mobile manipulation subtasks are difficult to train on dense reward, and improving subtask success rate is the ... | definition/direction/unit from same section | p. 8 (6 RESULTS) |
| Futhermore, we provide an ‘upper bound' on performance based on the success rates of each subtask policy. | definition/direction/unit from same section | p. 9 (6 RESULTS) |
| First, our optimistic upper bound shows low expected success rate on the long-horizon tasks. | definition/direction/unit from same section | p. 8 (6 RESULTS) |
| Does training per-object Pick and Place policies improve subtask success rate compared to allobject policies? | definition/direction/unit from same section | p. 10 (6 RESULTS) |
| Furthermore there are large jumps in success rate as demonstrations per object increases from 10 to 100 to 500. | definition/direction/unit from same section | p. 18 (A.4.1 DATASET SIZE) |
| Figure 8: SAC vs PPO subtask success once rate (%) curves on the train split. Lines are averaged across 3 seeds; since success rate ... | definition/direction/unit from same section | p. 19 (Figure/Table caption) |
| Table 2: Trajectory labeling on Pick Cracker Box with all and per-object RL policies. We group the trajectories into four categories: success once (S-Once), ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| Figure 2: Interact benchmark comparing MS-HAB (ours) with Habitat. Each data point is annotated with the number of parallel environments used. SPS and GPU ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Second, TidyHouse and SetTable RL baselines have some gap between upper bound and real completion rate, indicating potential handoff issues or disturbance to prior ... | comparison identity and matched condition | p. 8 (6 RESULTS) |
| Meanwhile, the PrepareGroceries RL baseline has a large drop in completion rate during the second PickFr subtask, indicating that the first PickFr causes too ... | comparison identity and matched condition | p. 8 (6 RESULTS) |
| Does training per-object Pick and Place policies improve subtask success rate compared to allobject policies? | comparison identity and matched condition | p. 10 (6 RESULTS) |
| Table 1: Subtask success once rates for RL and IL baselines. The RL-Per vs All column shows the difference in per-object RL policy performance ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| To verify this, we run two ablations. | comparison identity and matched condition | p. 10 (6 RESULTS) |
| For Pick, we require "straightforward success" demonstrations, where the agent successfully picks the object without dropping it while remaining within the cumulative collision threshold. | comparison identity and matched condition | p. 22 (A.6.1 DATASET FILTERING AND GENERATION) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We remove all collision requirements, and allow placing on the full target receptacle surface. | component/input/data sensitivity | p. 18 (A.3 RL SUBTASK EVALUATION CURVES) |
| To verify this, we run two ablations. | component/input/data sensitivity | p. 10 (6 RESULTS) |
| Although MS-HAB does not simulate state transitions like breaking, placing objects without dropping is a desirable, safe robot behavior to avoid excessive damage. | component/input/data sensitivity | p. 10 (6 RESULTS) |
| For Pick, we require "straightforward success" demonstrations, where the agent successfully picks the object without dropping it while remaining within the cumulative collision threshold. | component/input/data sensitivity | p. 22 (A.6.1 DATASET FILTERING AND GENERATION) |
| For Open and Close, we require "open success" and "closed success" demonstrations, where the agent opens/closes the articulation without excessive collisions, and the articulation ... | component/input/data sensitivity | p. 22 (A.6.1 DATASET FILTERING AND GENERATION) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present MS-HAB1, a holistic, open-sourced, home-scale manipulation benchmark with four key features: (1) fast simulation with realistic physics and manipulation, including low-level control, ... | Even with per-object RL policies, our low-level mobile manipulation subtasks are difficult to train on dense reward, and improving subtask success rate is the ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (6 RESULTS), p. 10 (6 RESULTS), p. 19 (Figure/Table caption), p. 9 (6 RESULTS), p. 8 (6 RESULTS), p. 10 (6 RESULTS) |
| Primary metric/result | Does training per-object Pick and Place policies improve subtask success rate compared to allobject policies? | numeric claim only at cited anchor | p. 10 (6 RESULTS) |

- Numeric sentences retained from the body:
- **p. 9 / 6 RESULTS - extractive PDF cue:** This is not an issue with magical grasping (Gu et al., 2023a), indicating that low-level control may need more scene diversity. pick_0 place_0 pick_1 place_1 ...
- **p. 10 / 6 RESULTS - extractive PDF cue:** Per Table 1, per-object policies perform notably better in TidyHouse and Prepare Groceries Pick, which involve 9 objects, with more modest improvement in SetTable Pick, ...
- **p. 10 / 6 RESULTS - extractive PDF cue:** The all-object policy is 1.88-2.42x more likely to fail to excessive collisions and 1.8712.37x more likely to fail to grasp the object, indicating that overfitting ...
- **p. 17 / A.3 RL SUBTASK EVALUATION CURVES - extractive PDF cue:** During training, we evaluate our policies every 10000 steps on 189 episodes.
- **p. 18 / A.4.1 DATASET SIZE - extractive PDF cue:** DEMOS SoR 1 0.00 ± 0.00 10 0.02 ± 0.03 100 0.27 ± 0.19 500 0.53 ± 0.13 1000 0.62 ± 0.09 To highlight the ...
- **p. 7 / 5 METHODOLOGY - extractive PDF cue:** We train 3 seeds for each task/subtask/object combination, evaluating on 189 episodes every 100,000 train samples.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Table 2: Trajectory labeling on Pick Cracker Box with all and per-object RL policies. We group the trajectories into four categories: success once (S-Once), ... | p. 10 (Figure/Table caption) |
| body limitation/failure cue | Eplace = () ∧eexcessive collisions̸ ∈Eplace viii Didn't reach goal failure: Agent grasps x, but cannot manipulate x to within 15cm of gpos. /Eplace/ ... | p. 24 (A.6.2 DEFINITIONS) |
| body limitation/failure cue | Epick = (econtact, egrasped, . . . , esuccess) ∧/Epick/ > 3 ∧eexcessive collisions̸ ∈Epick iii Success then drop: Agent successfully picks x and ... | p. 23 (A.6.2 DEFINITIONS) |
| body limitation/failure cue | First, we define 1placed is latest sequence = (/Eplace/ ≤2 ∧dg x,0 ≤0.15) ∨(iplace,released at goal > iplace,released outside goal ∧iplace,released at goal > ... | p. 24 (A.6.2 DEFINITIONS) |
| body limitation/failure cue | Previous failure modes are not applicable, and iopen,slightly opened > iopen,opened ∧ iopen,slightly opened > iopen,closed ∧eexcessive collisions̸ ∈Eopen viii Too slow failure: Agent ... | p. 25 (A.6.2 DEFINITIONS) |
| body limitation/failure cue | Published as a conference paper at ICLR 2025 iv Excessive collision failure: Agent exceeds collision threshold. eexcessive collisions ∈Eclose v Can't reach articulation failure: ... | p. 26 (A.6.2 DEFINITIONS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| During training, we evaluate our policies every 10000 steps on 189 episodes. | p. 17 (A.3 RL SUBTASK EVALUATION CURVES) |
| 6 are caused primarily by the 10 000 N cumulative robot force limit we set, which is not used in the original implementation of ... | p. 17 (A.3 RL SUBTASK EVALUATION CURVES) |
| 5.1, and we train SAC with 20 million samples per run. | p. 19 (A.4.3 SAC VS PPO FOR RL TRAINING) |
| Lines are averaged across 3 seeds; since success rate can jump rapidly, shaded regions represent min/max values. | p. 19 (A.4.3 SAC VS PPO FOR RL TRAINING) |
| We train Pick with 50M timesteps and Place with 25M timesteps. | p. 7 (5 METHODOLOGY) |
| We select the checkpoint with highest evaluation success once rate as our final policy. | p. 7 (5 METHODOLOGY) |
| Visual observations are encoded by the 5-layer CNN from Bojarski et al. | p. 8 (5 METHODOLOGY) |
| As the dataset generation code is publicly available, users have the flexibility to create their own datasets with custom constraints tailored to their specific ... | p. 8 (5 METHODOLOGY) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 2: Trajectory labeling on Pick Cracker Box with all and per-object RL policies. We group the trajectories into four categories: success once (S-Once), excessive ...
- **p. 24 / A.6.2 DEFINITIONS - extractive PDF cue:** Eplace = () ∧eexcessive collisions̸ ∈Eplace viii Didn't reach goal failure: Agent grasps x, but cannot manipulate x to within 15cm of gpos. /Eplace/ > ...
- **p. 23 / A.6.2 DEFINITIONS - extractive PDF cue:** Epick = (econtact, egrasped, . . . , esuccess) ∧/Epick/ > 3 ∧eexcessive collisions̸ ∈Epick iii Success then drop: Agent successfully picks x and returns ...
- **p. 24 / A.6.2 DEFINITIONS - extractive PDF cue:** First, we define 1placed is latest sequence = (/Eplace/ ≤2 ∧dg x,0 ≤0.15) ∨(iplace,released at goal > iplace,released outside goal ∧iplace,released at goal > iplace,grasped) ...
- **p. 25 / A.6.2 DEFINITIONS - extractive PDF cue:** Previous failure modes are not applicable, and iopen,slightly opened > iopen,opened ∧ iopen,slightly opened > iopen,closed ∧eexcessive collisions̸ ∈Eopen viii Too slow failure: Agent is ...
- **p. 26 / A.6.2 DEFINITIONS - extractive PDF cue:** Published as a conference paper at ICLR 2025 iv Excessive collision failure: Agent exceeds collision threshold. eexcessive collisions ∈Eclose v Can't reach articulation failure: Agent ...

- **PDF anchors reviewed:** datasets p. 9 (6 RESULTS), p. 18 (A.4.1 DATASET SIZE), p. 10 (6 RESULTS), p. 18 (A.4.1 DATASET SIZE), p. 22 (A.6.1 DATASET FILTERING AND GENERATION), p. 9 (6 RESULTS), metrics p. 8 (6 RESULTS), p. 9 (6 RESULTS), p. 8 (6 RESULTS), p. 10 (6 RESULTS), p. 18 (A.4.1 DATASET SIZE), p. 19 (Figure/Table caption), baselines p. 8 (6 RESULTS), p. 8 (6 RESULTS), p. 10 (6 RESULTS), p. 9 (Figure/Table caption), p. 10 (6 RESULTS), p. 22 (A.6.1 DATASET FILTERING AND GENERATION), results p. 8 (6 RESULTS), p. 10 (6 RESULTS), p. 19 (Figure/Table caption), p. 9 (6 RESULTS), p. 8 (6 RESULTS), p. 10 (6 RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
