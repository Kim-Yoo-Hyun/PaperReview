# Evaluation - Habitat 2.0: Training Home Assistants to Rearrange their Habitat

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.neurips.cc/paper_files/paper/2021/hash/021bbc7ee20b71134d53e20206bd6feb-Abstract.html; PDF retrieval source: https://proceedings.neurips.cc/paper_files/paper/2021/file/021bbc7ee20b71134d53e20206bd6feb-Paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (8 GPUs), p. 10 (8 GPUs), p. 7 (8 GPUs)): Figure 5: Success rates for Home Assistant Benchmark tasks. Due to the difficulty of full HAB tasks, we analyze performance as completing a part of the overall task. For the ...

## Evaluation Body Digest

- **p. 6 / 8 GPUs - extractive body cue:** 242 ±2 177 ±3 224 ±3 2223 ±3 814 ±2 941 ±2 7192 ±55 3965 ±30 4829 ±50 Table 2: Benchmarking H2.0 performance: simulation steps ...
- **p. 6 / 8 GPUs - extractive body cue:** However, we note the comparison between the two benchmarks is not exact since the robot type, number of objects, and 6
- **p. 8 / 8 GPUs - extractive body cue:** 6 Home Assistant Benchmark (HAB) We now describe our benchmark of common household assistive robotic tasks.
- **p. 7 / 8 GPUs - extractive body cue:** Note: the episodes in Pick are constructed such that the robot does not need to move its base.
- **p. 10 / 8 GPUs - extractive body cue:** We presented the ReplicaCAD dataset, the Habitat 2.0 platform and a home assistant benchmark.
- **p. 7 / 8 GPUs - extractive body cue:** 5 The Pick Task: a Base Case of Rearrangement We first carry out systematic analyses on a relatively simple robotic manipulation task: picking up one ...
- **p. 8 / 8 GPUs - extractive body cue:** Method Seen Unseen Layouts Objects Receptacles MonolithicRL 91.7 ±1.1 86.3 ±1.4 74.7 ±1.8 52.7 ±2.0 SPA 70.2 ±1.9 72.7 ±1.8 72.7 ±1.8 60.3 ±2.0 SPA-Priv ...
- **p. 10 / 8 GPUs - extractive body cue:** Results are on unseen layouts with mean and standard error computed for 100 episodes. navigation is often executed between successive skills, we include versions of ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | BENCHMARK / DATASET | Figure 5: Success rates for Home Assistant Benchmark tasks. Due to the difficulty of full HAB tasks, we analyze performance as completing a part ... | p. 10 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Table 2: Benchmarking H2.0 performance: simulation steps per second (higher better) over 10 runs and a 95% confidence-interval In Idle, the agent is executing ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Table 3: Pick generalization analysis: success rates with mean and standard error on 600 episodes (and across 3 seeds for MonolithicRL). Systematic Generalization. With ... | p. 8 (Figure/Table caption) |
| 8 GPUs | BENCHMARK / DATASET | 86.3%), significantly outperforming SPA (72.7%) and even SPA-Priv (80.0%). | p. 8 (8 GPUs) |
| 8 GPUs | BENCHMARK / DATASET | Coupled with the ReplicaCAD data these improvements allow us to investigate the performance of RL policies against classical MP approaches for the suite of ... | p. 10 (8 GPUs) |

## Dataset / Benchmark Role

- **p. 6 / 8 GPUs - extractive body cue:** 242 ±2 177 ±3 224 ±3 2223 ±3 814 ±2 941 ±2 7192 ±55 3965 ±30 4829 ±50 Table 2: Benchmarking H2.0 performance: simulation steps ...
- **p. 6 / 8 GPUs - extractive body cue:** However, we note the comparison between the two benchmarks is not exact since the robot type, number of objects, and 6
- **p. 8 / 8 GPUs - extractive body cue:** 6 Home Assistant Benchmark (HAB) We now describe our benchmark of common household assistive robotic tasks.
- **p. 7 / 8 GPUs - extractive body cue:** Note: the episodes in Pick are constructed such that the robot does not need to move its base.
- **p. 10 / 8 GPUs - extractive body cue:** We presented the ReplicaCAD dataset, the Habitat 2.0 platform and a home assistant benchmark.
- **p. 7 / 8 GPUs - extractive body cue:** 5 The Pick Task: a Base Case of Rearrangement We first carry out systematic analyses on a relatively simple robotic manipulation task: picking up one ...
- **p. 8 / 8 GPUs - extractive body cue:** Method Seen Unseen Layouts Objects Receptacles MonolithicRL 91.7 ±1.1 86.3 ±1.4 74.7 ±1.8 52.7 ±2.0 SPA 70.2 ±1.9 72.7 ±1.8 72.7 ±1.8 60.3 ±2.0 SPA-Priv ...
- **p. 10 / 8 GPUs - extractive body cue:** Results are on unseen layouts with mean and standard error computed for 100 episodes. navigation is often executed between successive skills, we include versions of ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: A mobile manipulator (Fetch robot) simulated in Habitat 2.0 performing rearrangement tasks in a ReplicaCAD apartment - (left) opening a drawer before picking ...
- **p. 3 / Figure/Table caption - extractive body cue:** Table 1: High-level comparison of different simulators. Note: Speeds were taken directly from respective publications or obtained via direct personal correspondence with the authors when ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Left: The original Replica scene. Right: the artist recreated scene ReplicaCAD. All objects (furniture, mugs) including articulated ones (drawers, fridge) in ReplicaCAD are ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Interleaved physics and rendering. Top shows the normal sequential method of performing physics (st, at) ! st+1 then rendering st+1 ! ot+1. Bottom ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2: Benchmarking H2.0 performance: simulation steps per second (higher better) over 10 runs and a 95% confidence-interval In Idle, the agent is executing random ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Fetch with head and arm cameras picking up a bowl from the counter. It can sense its proprioceptive-state - arm joint angles (7- ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Pick generalization analysis: success rates with mean and standard error on 600 episodes (and across 3 seeds for MonolithicRL). Systematic Generalization. With H2.0 ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 5: Success rates for Home Assistant Benchmark tasks. Due to the difficulty of full HAB tasks, we analyze performance as completing a part of ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 242 ±2 177 ±3 224 ±3 2223 ±3 814 ±2 941 ±2 7192 ±55 3965 ±30 4829 ±50 Table 2: Benchmarking H2.0 performance: simulation ... | embodiment, simulator version and control stack | p. 6 (8 GPUs), p. 6 (8 GPUs) |
| Task/environment | However, we note the comparison between the two benchmarks is not exact since the robot type, number of objects, and 6 | reset, timeout, object/scene variation | p. 6 (8 GPUs), p. 8 (8 GPUs) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 7 (8 GPUs), p. 8 (8 GPUs) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 7 (8 GPUs), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 5: Success rates for Home Assistant Benchmark tasks. Due to the difficulty of full HAB tasks, we analyze performance as completing a part ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| Method Seen Unseen Layouts Objects Receptacles MonolithicRL 91.7 ±1.1 86.3 ±1.4 74.7 ±1.8 52.7 ±2.0 SPA 70.2 ±1.9 72.7 ±1.8 72.7 ±1.8 60.3 ±2.0 ... | definition/direction/unit from same section | p. 8 (8 GPUs) |
| (a) TidyHouse (b) PrepareGroceries (c) SetTable Figure 5: Success rates for Home Assistant Benchmark tasks. | definition/direction/unit from same section | p. 10 (8 GPUs) |
| 242 ±2 177 ±3 224 ±3 2223 ±3 814 ±2 941 ±2 7192 ±55 3965 ±30 4829 ±50 Table 2: Benchmarking H2.0 performance: simulation ... | definition/direction/unit from same section | p. 6 (8 GPUs) |
| An object is considered successfully picked if the arm returns to a known ‘resting position' with the target object grasped. | definition/direction/unit from same section | p. 7 (8 GPUs) |
| In the supplementary we also analyze different sensor input modalities (Appendix F.1), the surprising success of "blind" policies (Appendix F.2), the effect of different ... | definition/direction/unit from same section | p. 8 (8 GPUs) |
| Due to the difficulty of the full task, for analysis, the X-axis lists the sequence of agent-environment interactions (pick, place, open, close) required to ... | definition/direction/unit from same section | p. 9 (8 GPUs) |
| The ablations for H2.0 (denoted by ‘- render opts', ‘-physics opts', and ‘-all opts.') show that principles followed in our system design lead to ... | definition/direction/unit from same section | p. 6 (8 GPUs) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In the more complex task of PrepareGroceries (Figure 5b), TP+SRL outperforms TP+SPA both with and without oracle navigation due to the perception challenge of ... | comparison identity and matched condition | p. 10 (8 GPUs) |
| 86.3%), significantly outperforming SPA (72.7%) and even SPA-Priv (80.0%). | comparison identity and matched condition | p. 8 (8 GPUs) |
| The purpose of this baseline is to provide an upper-bound on the performance of SPA. | comparison identity and matched condition | p. 8 (8 GPUs) |
| In the easiest setting, Tidy House with oracle navigation (Figure 5a), TP+SPA performs better than TP+SRL. | comparison identity and matched condition | p. 10 (8 GPUs) |
| Table 1: High-level comparison of different simulators. Note: Speeds were taken directly from respective publications or obtained via direct personal correspondence with the authors ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| However, we note the comparison between the two benchmarks is not exact since the robot type, number of objects, and 6 | comparison identity and matched condition | p. 6 (8 GPUs) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In the supplementary we also analyze different sensor input modalities (Appendix F.1), the surprising success of "blind" policies (Appendix F.2), the effect of different ... | component/input/data sensitivity | p. 8 (8 GPUs) |
| The ablations for H2.0 (denoted by ‘- render opts', ‘-physics opts', and ‘-all opts.') show that principles followed in our system design lead to ... | component/input/data sensitivity | p. 6 (8 GPUs) |
| The task for the robot is to pick up a target object with center-of-mass coordinates s0 2 R3 (provided in robot's coordinate system) as ... | component/input/data sensitivity | p. 7 (8 GPUs) |
| PrepareGroceries: Remove 2 objects from the fridge to the counters and place one object back in the fridge (see Fig. | component/input/data sensitivity | p. 8 (8 GPUs) |
| Crafting an SPA pipeline for opening/closing unknown articulated containers is an open unsolved problem in robotics - involving detecting and tracking articulation [66, 67] ... | component/input/data sensitivity | p. 9 (8 GPUs) |
| Sense-plan-act variants scale poorly to increasing task complexity. | component/input/data sensitivity | p. 10 (8 GPUs) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To support this long-term research agenda, we present: • ReplicaCAD: an artist-authored fully-interactive recreation of ‘FRL-apartment' spaces from the Replica dataset [2] consisting of ... | Figure 5: Success rates for Home Assistant Benchmark tasks. Due to the difficulty of full HAB tasks, we analyze performance as completing a part ... | PDF body cue; verify exact table/figure and matched conditions | p. 10 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (8 GPUs), p. 10 (8 GPUs), p. 7 (8 GPUs) |
| Primary metric/result | Table 2: Benchmarking H2.0 performance: simulation steps per second (higher better) over 10 runs and a 95% confidence-interval In Idle, the agent is executing ... | numeric claim only at cited anchor | p. 6 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 8 GPUs - extractive body cue:** Idle Idle Interact Idle Idle Interact Idle Idle Interact 1⇥RGB 2⇥RGB-D 2⇥RGB-D 1⇥RGB 2⇥RGB-D 2⇥RGB-D 1⇥RGB 2⇥RGB-D 2⇥RGB-D H2.0 (Full) 1191 ±36 669 ±13 510 ...
- **p. 6 / 8 GPUs - extractive body cue:** 242 ±2 177 ±3 224 ±3 2223 ±3 814 ±2 941 ±2 7192 ±55 3965 ±30 4829 ±50 Table 2: Benchmarking H2.0 performance: simulation steps ...
- **p. 7 / 8 GPUs - extractive body cue:** Finally, H2.0 scales well - achieving 8,186 SPS (272⇥real-time) multi-process on a single GPU and 25,734 SPS (850⇥ real-time) on a single node with 8 ...
- **p. 7 / 8 GPUs - extractive body cue:** The agent performs end-effector control at 30Hz.
- **p. 8 / 8 GPUs - extractive body cue:** Method Seen Unseen Layouts Objects Receptacles MonolithicRL 91.7 ±1.1 86.3 ±1.4 74.7 ±1.8 52.7 ±2.0 SPA 70.2 ±1.9 72.7 ±1.8 72.7 ±1.8 60.3 ±2.0 SPA-Priv ...
- **p. 8 / 8 GPUs - extractive body cue:** In training the agent sees 9 objects from the YCB dataset kitchen and food categories (chef can, cracker box, sugar box, tomato soup can, tuna ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We make the following observations (See Appendix I for skill learning curves and SPA failure statistics): 1. | p. 10 (8 GPUs) |
| body limitation/failure cue | The agent fails if the accumulated contact force experienced by the arm/body exceeds a threshold of 5k Newtons. | p. 7 (8 GPUs) |
| body limitation/failure cue | If the scalar is negative and the gripper is currently holding an object, then the object currently held in the gripper is released and ... | p. 7 (8 GPUs) |
| body limitation/failure cue | We cannot make any such claims for SPA. | p. 8 (8 GPUs) |
| body limitation/failure cue | SensePlanAct (SPA) pipeline: Sensing consists of constructing an accumulative 3D point-cloud of the scene from depth sensors, which is then used for collision queries. | p. 8 (8 GPUs) |
| body limitation/failure cue | The agent is evaluated on unseen layouts and configurations of objects, and so cannot simply memorize. | p. 9 (8 GPUs) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Specifically, we present: (i) ReplicaCAD: an artist-authored, annotated, reconfigurable 3D dataset of apartments (matching real spaces) with articulated objects (e.g. cabinets and drawers that ... | p. 1 (Abstract) |
| 242 ±2 177 ±3 224 ±3 2223 ±3 814 ±2 941 ±2 7192 ±55 3965 ±30 4829 ±50 Table 2: Benchmarking H2.0 performance: simulation ... | p. 6 (8 GPUs) |
| Training and testing such robots in hardware directly is slow, expensive, and difficult to reproduce. | p. 2 (1 Introduction) |
| H2.0 also scales well - achieving 8,200 SPS (273⇥real-time) multi-process on a single GPU and over 25,000 SPS (850⇥real-time) on a single node with ... | p. 2 (1 Introduction) |
| Benchmarking was conducted by different teams on different hardware with different underlying 3D assets simulating different capabilities. | p. 3 (1 Introduction) |
| A direct comparison against other simulators is not feasible due to different capabilities, assets, hardware, and experimental settings. | p. 7 (8 GPUs) |
| The visual input is encoded using a CNN, concatenated with embeddings of proprioceptive-sensing and goal coordinates, and fed to a recurrent actor-critic network, trained ... | p. 7 (8 GPUs) |
| Million steps of experience (see Appendix C for details). | p. 8 (8 GPUs) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 8 GPUs - extractive body cue:** We make the following observations (See Appendix I for skill learning curves and SPA failure statistics): 1.
- **p. 7 / 8 GPUs - extractive body cue:** The agent fails if the accumulated contact force experienced by the arm/body exceeds a threshold of 5k Newtons.
- **p. 7 / 8 GPUs - extractive body cue:** If the scalar is negative and the gripper is currently holding an object, then the object currently held in the gripper is released and simulated ...
- **p. 8 / 8 GPUs - extractive body cue:** We cannot make any such claims for SPA.
- **p. 8 / 8 GPUs - extractive body cue:** SensePlanAct (SPA) pipeline: Sensing consists of constructing an accumulative 3D point-cloud of the scene from depth sensors, which is then used for collision queries.
- **p. 9 / 8 GPUs - extractive body cue:** The agent is evaluated on unseen layouts and configurations of objects, and so cannot simply memorize.

- **Evidence anchors reviewed:** datasets p. 6 (8 GPUs), p. 6 (8 GPUs), p. 8 (8 GPUs), p. 7 (8 GPUs), p. 10 (8 GPUs), p. 7 (8 GPUs), metrics p. 10 (Figure/Table caption), p. 8 (8 GPUs), p. 10 (8 GPUs), p. 6 (8 GPUs), p. 7 (8 GPUs), p. 8 (8 GPUs), baselines p. 10 (8 GPUs), p. 8 (8 GPUs), p. 8 (8 GPUs), p. 10 (8 GPUs), p. 3 (Figure/Table caption), p. 6 (8 GPUs), results p. 10 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (8 GPUs), p. 10 (8 GPUs), p. 7 (8 GPUs).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
