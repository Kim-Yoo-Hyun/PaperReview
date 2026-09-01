# Evaluation - SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2011.07215; PDF retrieval source: https://arxiv.org/pdf/2011.07215. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (6 Experiments), p. 7 (6 Experiments), p. 8 (6 Experiments), p. 16 (Figure/Table caption), p. 17 (Figure/Table caption), p. 6 (6 Experiments)): While it outperforms the rest of the baselines due to the use of the segmentation map and a better action space for exploration, the result shows that there still exists ...

## Evaluation Body Digest

- **p. 7 / 6 Experiments - extractive body cue:** Thus, this evaluation points to a clear need for new methods development for image-based robot manipulation of deformable objects.
- **p. 8 / 6 Experiments - extractive body cue:** We perform a series of pick and place actions both in simulation and on the real robot.
- **p. 8 / 6 Experiments - extractive body cue:** We set up a real world cloth manipulation environment with a Sawyer robot with a Weiss gripper, as shown in Figure 4.
- **p. 6 / 6 Experiments - extractive body cue:** In this section, we perform experiments with an aim to answer the following questions: • Are SoftGym tasks challenging for current reinforcement learning algorithms? • ...
- **p. 7 / 6 Experiments - extractive body cue:** 6.2 Benchmarking results on SoftGym-Medium A summary of the final normalized performance of all baselines on the evaluation set is shown in Figure 2.
- **p. 6 / 6 Experiments - extractive body cue:** 6.1 Experimental Setup For each task, we compute a lower bound and upper bound on performance so that we can more easily analyze the performance ...
- **p. 16 / Figure/Table caption - extractive body cue:** Table 3: Task specific planning horizon for CEM B.2 SAC and CURL-SAC We use the CURL-SAC implementation from the released code3. Both Q-value network and ...
- **p. 16 / Figure/Table caption - extractive body cue:** Table 5: SAC task dependent hyper-parameters. If learning rate decay is applied, the actor learning rate is halved every 75K steps and the critic learning ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 6 Experiments (p. 6); A.4 Training and Evaluation (p. 15).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 6 Experiments | BENCHMARK / DATASET | While it outperforms the rest of the baselines due to the use of the segmentation map and a better action space for exploration, the ... | p. 7 (6 Experiments) |
| 6 Experiments | BENCHMARK / DATASET | This is especially true for StraightenRope, SpreadCloth, and FoldCloth, and the learning curves for these tasks seem to imply that even with more training ... | p. 7 (6 Experiments) |
| 6 Experiments | BENCHMARK / DATASET | This demonstration suggests that the simulation environment can reflect the complex dynamics in the real world and that algorithmic improvements of methods developed in ... | p. 8 (6 Experiments) |
| Figure/Table caption | BENCHMARK / DATASET | Table 3: Task specific planning horizon for CEM B.2 SAC and CURL-SAC We use the CURL-SAC implementation from the released code3. Both Q-value network ... | p. 16 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Table 7: Architecture of the deconvolutional neural network (VAE decoder) in PlaNet. We use a GRU [56] with 200 hidden nodes as the deterministic ... | p. 17 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 6 Experiments - extractive body cue:** Thus, this evaluation points to a clear need for new methods development for image-based robot manipulation of deformable objects.
- **p. 8 / 6 Experiments - extractive body cue:** We perform a series of pick and place actions both in simulation and on the real robot.
- **p. 8 / 6 Experiments - extractive body cue:** We set up a real world cloth manipulation environment with a Sawyer robot with a Weiss gripper, as shown in Figure 4.
- **p. 6 / 6 Experiments - extractive body cue:** In this section, we perform experiments with an aim to answer the following questions: • Are SoftGym tasks challenging for current reinforcement learning algorithms? • ...
- **p. 7 / 6 Experiments - extractive body cue:** 6.2 Benchmarking results on SoftGym-Medium A summary of the final normalized performance of all baselines on the evaluation set is shown in Figure 2.
- **p. 6 / 6 Experiments - extractive body cue:** 6.1 Experimental Setup For each task, we compute a lower bound and upper bound on performance so that we can more easily analyze the performance ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1: Visualizations of all tasks in SoftGym. These tasks can be used to evaluate how well an algorithm works on a variety of deformable ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2: Normalized performance at the last time step of the episode of all the algorithms on the evaluation set. The x-axis shows the number ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 2. As expected, the Dynamics Oracle performs the best and is able to solve most of the tasks. As the dynamics and ground-truth position ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3: Bottom row: Open-loop prediction of PlaNet. Given an initial set of five frames, PlaNet predicts the following 30 frames. Here we show the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Two pick-and-place rollouts both in simulation and in the real world for a cloth manipulation task. For each rollout, the left column shows ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 1: Different task variations in all tasks. Refer to the appendix for more details of the ranges of the variations and how they are ...
- **p. 15 / Figure/Table caption - extractive body cue:** Table 2: Action repetition and task horizon. B.1 CEM with Dynamics Oracle For CEM, we use 10 optimization iteration. Model predictive control is used. Different ...
- **p. 16 / Figure/Table caption - extractive body cue:** Table 3: Task specific planning horizon for CEM B.2 SAC and CURL-SAC We use the CURL-SAC implementation from the released code3. Both Q-value network and ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Thus, this evaluation points to a clear need for new methods development for image-based robot manipulation of deformable objects. | embodiment, simulator version and control stack | p. 7 (6 Experiments), p. 8 (6 Experiments) |
| Task/environment | We perform a series of pick and place actions both in simulation and on the real robot. | reset, timeout, object/scene variation | p. 8 (6 Experiments), p. 8 (6 Experiments) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 5 (1 Introduction) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 5 (1 Introduction), p. 6 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 3: Task specific planning horizon for CEM B.2 SAC and CURL-SAC We use the CURL-SAC implementation from the released code3. Both Q-value network ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| Table 5: SAC task dependent hyper-parameters. If learning rate decay is applied, the actor learning rate is halved every 75K steps and the critic ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| 6.1 Experimental Setup For each task, we compute a lower bound and upper bound on performance so that we can more easily analyze the ... | definition/direction/unit from same section | p. 6 (6 Experiments) |
| We run each algorithm for 5 random seeds and plot the median of the normalized performance. | definition/direction/unit from same section | p. 7 (6 Experiments) |
| In Figure 2, we show the final performance of this method with 20 pick-and-place steps for each episode. | definition/direction/unit from same section | p. 7 (6 Experiments) |
| Figure 2: Normalized performance at the last time step of the episode of all the algorithms on the evaluation set. The x-axis shows the ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 1: Different task variations in all tasks. Refer to the appendix for more details of the ranges of the variations and how they ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| Figure 6. We see that the performance of CEM is sensitive to the planning horizon in TransportWater, FoldCloth and DropCloth, whereas the performance is ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| While it outperforms the rest of the baselines due to the use of the segmentation map and a better action space for exploration, the ... | comparison identity and matched condition | p. 7 (6 Experiments) |
| Compared to the reduced state oracle, image based methods have much worse performance in certain tasks such as FoldCloth or StraightenRope, indicating that there ... | comparison identity and matched condition | p. 7 (6 Experiments) |
| Table 2: Action repetition and task horizon. B.1 CEM with Dynamics Oracle For CEM, we use 10 optimization iteration. Model predictive control is used. ... | comparison identity and matched condition | p. 15 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| no ablation sentence selected | not reported; proposed stress test only | verify ablation section |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we present SoftGym, a set of open-source simulated benchmarks for manipulating deformable objects, with a standard OpenAI Gym API and Python ... | While it outperforms the rest of the baselines due to the use of the segmentation map and a better action space for exploration, the ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (6 Experiments), p. 7 (6 Experiments), p. 8 (6 Experiments), p. 16 (Figure/Table caption), p. 17 (Figure/Table caption), p. 6 (6 Experiments) |
| Primary metric/result | This is especially true for StraightenRope, SpreadCloth, and FoldCloth, and the learning curves for these tasks seem to imply that even with more training ... | numeric claim only at cited anchor | p. 7 (6 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 6 Experiments - extractive body cue:** For CEM, no parameters are trained, so we modify this procedure: instead, we randomly sample 10 task variations from the evaluation set and compute the ...
- **p. 8 / 6 Experiments - extractive body cue:** Given an initial set of five frames, PlaNet predicts the following 30 frames.
- **p. 4 / 1 Introduction - extractive body cue:** 4.2 Tasks SoftGym-Medium includes six tasks (see Appendix for more details): TransportWater Move a cup of water to a target position as fast as possible ...
- **p. 4 / 1 Introduction - extractive body cue:** On a Nvidia 2080Ti GPU, all SoftGym tasks run about 4x faster than real time, with rendering.
- **p. 4 / 1 Introduction - extractive body cue:** One million simulation steps takes 6 hours (wall-clock time) and corresponds to at least 35 hours for a real robot to collect.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | from a policy that always does nothing. | p. 7 (6 Experiments) |
| body limitation/failure cue | On the other hand, this method does not perform very well on the FoldCloth task. | p. 7 (6 Experiments) |
| body limitation/failure cue | Table 7: Architecture of the deconvolutional neural network (VAE decoder) in PlaNet. We use a GRU [56] with 200 hidden nodes as the deterministic ... | p. 17 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Most of the experiments are run on an Nvidia 2080Ti GPU, with 4 virtual CPUs and 40G RAM. | p. 7 (6 Experiments) |
| We run each algorithm for 5 random seeds and plot the median of the normalized performance. | p. 7 (6 Experiments) |
| The x-axis shows the number of training time steps. | p. 6 (1 Introduction) |
| 6.1 Experimental Setup For each task, we compute a lower bound and upper bound on performance so that we can more easily analyze the ... | p. 6 (6 Experiments) |
| On a Nvidia 2080Ti GPU, all SoftGym tasks run about 4x faster than real time, with rendering. | p. 4 (1 Introduction) |
| Code and videos of the learned policies can be found on our project website.1 Keywords: Benchmark, Reinforcement Learning, Deformable Object Manipulation | p. 1 (Abstract) |
| Robotic manipulation of deformable objects has wide application both in our daily lives, such as folding laundry and making food, and in industrial applications, ... | p. 1 (1 Introduction) |
| Given the current particle positions pi and velocities vi, FleX first computes a predicted position ˆpi = pi +∆tvi 2 | p. 2 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 6 Experiments - extractive body cue:** from a policy that always does nothing.
- **p. 7 / 6 Experiments - extractive body cue:** On the other hand, this method does not perform very well on the FoldCloth task.
- **p. 17 / Figure/Table caption - extractive body cue:** Table 7: Architecture of the deconvolutional neural network (VAE decoder) in PlaNet. We use a GRU [56] with 200 hidden nodes as the deterministic path ...

- **PDF anchors reviewed:** datasets p. 7 (6 Experiments), p. 8 (6 Experiments), p. 8 (6 Experiments), p. 6 (6 Experiments), p. 7 (6 Experiments), p. 6 (6 Experiments), metrics p. 16 (Figure/Table caption), p. 16 (Figure/Table caption), p. 6 (6 Experiments), p. 7 (6 Experiments), p. 7 (6 Experiments), p. 6 (Figure/Table caption), baselines p. 7 (6 Experiments), p. 7 (6 Experiments), p. 15 (Figure/Table caption), results p. 7 (6 Experiments), p. 7 (6 Experiments), p. 8 (6 Experiments), p. 16 (Figure/Table caption), p. 17 (Figure/Table caption), p. 6 (6 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
