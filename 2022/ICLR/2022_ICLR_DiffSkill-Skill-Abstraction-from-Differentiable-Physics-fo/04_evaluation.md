# Evaluation - DiffSkill: Skill Abstraction from Differentiable Physics for Deformable Object Manipulations with Tools

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2203.17275; PDF retrieval source: https://arxiv.org/pdf/2203.17275. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS)): Each entry shows the normalized improvement / success rate.

## Evaluation Body Digest

- **p. 5 / 3 EXPERIMENTS - extractive body cue:** We build our simulation environments on top of PlasticineLab (Huang et al., 2021), a differentiable physics benchmark using the DiffTaichi system (Hu et al., 2019a) ...
- **p. 6 / 3 EXPERIMENTS - extractive body cue:** We then train our VAE, policy, feasibility and score predictors over this demonstration video dataset.
- **p. 6 / 3 EXPERIMENTS - extractive body cue:** We found behavior cloning to be sufficient for learning short-horizon skills from the demonstration dataset.
- **p. 5 / 3 EXPERIMENTS - extractive body cue:** 3.1 EXPERIMENTAL SETUP Tasks and environments We experiment with a set of sequential deformable object manipulation tasks with dough.
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** Note that this method requires full state of the simulation and multiple forward and backward passes through the simulator during evaluation time.
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** Remarkably, DiffSkill even outperforms the trajectory optimizer that controls both tools at the same time, which uses the full simulation state during evaluation time.
- **p. 8 / 3 EXPERIMENTS - extractive body cue:** Since we do not have the intermediate goals anymore, we try two different ways of choosing the skills to execute at each stage: Randomly pick ...
- **p. 8 / 3 EXPERIMENTS - extractive body cue:** Method Task LiftSpread GatherTransport CutRearrange No Discrete Planning 0.758 / 20% 0.312 / 0% 0.118 / 0% Direct Execution (Random) 0.593 / 15% 0.369 / ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** 3 EXPERIMENTS (p. 5); A IMPLEMENTATION DETAILS (p. 14).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 3 EXPERIMENTS | EMPIRICAL / SIMULATION | Each entry shows the normalized improvement / success rate. | p. 7 (3 EXPERIMENTS) |
| 3 EXPERIMENTS | EMPIRICAL / SIMULATION | Method Task (H) LiftSpread (2) GatherTransport (2) CutRearrange (3) Tool A only Trajectory Opt (Oracle) 0.755 / 0% 0.386 / 0% 0.033 / 0% ... | p. 7 (3 EXPERIMENTS) |
| 3 EXPERIMENTS | EMPIRICAL / SIMULATION | Method Task LiftSpread GatherTransport CutRearrange No Discrete Planning 0.758 / 20% 0.312 / 0% 0.118 / 0% Direct Execution (Random) 0.593 / 15% 0.369 ... | p. 8 (3 EXPERIMENTS) |
| 3 EXPERIMENTS | EMPIRICAL / SIMULATION | The numbers on the bottom right shows the achieved normalized improvement metric at that time. | p. 8 (3 EXPERIMENTS) |
| 3 EXPERIMENTS | EMPIRICAL / SIMULATION | We report both the normalized performance metric and the success rate for comparisons. | p. 6 (3 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 5 / 3 EXPERIMENTS - extractive body cue:** We build our simulation environments on top of PlasticineLab (Huang et al., 2021), a differentiable physics benchmark using the DiffTaichi system (Hu et al., 2019a) ...
- **p. 6 / 3 EXPERIMENTS - extractive body cue:** We then train our VAE, policy, feasibility and score predictors over this demonstration video dataset.
- **p. 6 / 3 EXPERIMENTS - extractive body cue:** We found behavior cloning to be sufficient for learning short-horizon skills from the demonstration dataset.
- **p. 5 / 3 EXPERIMENTS - extractive body cue:** 3.1 EXPERIMENTAL SETUP Tasks and environments We experiment with a set of sequential deformable object manipulation tasks with dough.
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** Note that this method requires full state of the simulation and multiple forward and backward passes through the simulator during evaluation time.
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** Remarkably, DiffSkill even outperforms the trajectory optimizer that controls both tools at the same time, which uses the full simulation state during evaluation time.
- **p. 8 / 3 EXPERIMENTS - extractive body cue:** Since we do not have the intermediate goals anymore, we try two different ways of choosing the skills to execute at each stage: Randomly pick ...
- **p. 8 / 3 EXPERIMENTS - extractive body cue:** Method Task LiftSpread GatherTransport CutRearrange No Discrete Planning 0.758 / 20% 0.312 / 0% 0.118 / 0% Direct Execution (Random) 0.593 / 15% 0.369 / ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Humans use various tools to manipulate deformable objects much more effectively than state-of-the-art robotic systems. This work aims to narrow the gap and ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: (a) Collecting demonstration trajectories by running a gradient-based trajectory optimizer in a differentiable simulator. (b) Neural abstraction by imitating the expert demonstration, which ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Normalized improvement of all methods and the success rate on different tasks. Each entry shows the normalized improvement / success rate. The top ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3: Visualization of the generated plan and the corresponding execution. The plan generated by DiffSkill is shown in the left, where the first and ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Normalized improvement and success rate of ablation methods. 4
- **p. 14 / Figure/Table caption - extractive body cue:** Table 3: Summary of all hyper-parameters. B COMPARISON WITH MODEL-FREE RL ON SINGLE-TOOL TASKS In this work, we focus on solving long-horizon multi-tool tasks. But ...
- **p. 14 / Figure/Table caption - extractive body cue:** Table 4: Normalized improvement of all methods and the success rate on single-tool tasks. Each entry shows the normalized improvement / success rate. 14

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We build our simulation environments on top of PlasticineLab (Huang et al., 2021), a differentiable physics benchmark using the DiffTaichi system (Hu et al., ... | embodiment, simulator version and control stack | p. 5 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS) |
| Task/environment | We then train our VAE, policy, feasibility and score predictors over this demonstration video dataset. | reset, timeout, object/scene variation | p. 6 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 4 (2 METHOD), p. 2 (1 INTRODUCTION) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 2 (2 METHOD), p. 4 (2 METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| After training, we find the feasibility and score predictor to perform well on the held out trajectories, achieving a L2 error of less than ... | definition/direction/unit from same section | p. 6 (3 EXPERIMENTS) |
| Table 1: Normalized improvement of all methods and the success rate on different tasks. Each entry shows the normalized improvement / success rate. The ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| We report both the normalized performance metric and the success rate for comparisons. | definition/direction/unit from same section | p. 6 (3 EXPERIMENTS) |
| Method Task (H) LiftSpread (2) GatherTransport (2) CutRearrange (3) Tool A only Trajectory Opt (Oracle) 0.755 / 0% 0.386 / 0% 0.033 / 0% ... | definition/direction/unit from same section | p. 7 (3 EXPERIMENTS) |
| Method Task LiftSpread GatherTransport CutRearrange No Discrete Planning 0.758 / 20% 0.312 / 0% 0.118 / 0% Direct Execution (Random) 0.593 / 15% 0.369 ... | definition/direction/unit from same section | p. 8 (3 EXPERIMENTS) |
| Model parameter Value dimension of latent space 8 MLP hidden node number 1024 Training parameters Value learning rate 0.001 batch size 128 optimizer Adam ... | definition/direction/unit from same section | p. 14 (A IMPLEMENTATION DETAILS) |
| Figure 2: (a) Collecting demonstration trajectories by running a gradient-based trajectory optimizer in a differentiable simulator. (b) Neural abstraction by imitating the expert demonstration, ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| In this case, we can see that using random skills at each stage results in poor performance. | definition/direction/unit from same section | p. 8 (3 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 3.3 BASELINES We compare with three strong baselines: Model-free Reinforcement Learning (RL) We compare with two model-free RL methods: TD3 (Fujimoto et al., 2018) ... | comparison identity and matched condition | p. 6 (3 EXPERIMENTS) |
| Method Task LiftSpread GatherTransport CutRearrange No Discrete Planning 0.758 / 20% 0.312 / 0% 0.118 / 0% Direct Execution (Random) 0.593 / 15% 0.369 ... | comparison identity and matched condition | p. 8 (3 EXPERIMENTS) |
| Figure 1: Humans use various tools to manipulate deformable objects much more effectively than state-of-the-art robotic systems. This work aims to narrow the gap ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| Behavior Cloning We compare with another baseline that directly trains a goal-conditioned policy with Behavior Cloning (BC) and hindsight relabeling using all tools. | comparison identity and matched condition | p. 6 (3 EXPERIMENTS) |
| Second, with multiple tools, we can see that DiffSkill significantly outperforms the single-skill policy. | comparison identity and matched condition | p. 7 (3 EXPERIMENTS) |
| Still, DiffSkill is able to achieve higher success, even though the trajectory optimizer oracle achieves a higher average score. | comparison identity and matched condition | p. 7 (3 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 3: Visualization of the generated plan and the corresponding execution. The plan generated by DiffSkill is shown in the left, where the first ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 1: Humans use various tools to manipulate deformable objects much more effectively than state-of-the-art robotic systems. This work aims to narrow the gap ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| 3.5 ABLATION ANALYSIS We perform two ablations on DiffSkill. | component/input/data sensitivity | p. 7 (3 EXPERIMENTS) |
| This is because it requires three stages of manipulation; further, it is non-trivial to transport the dough without deforming it too much. | component/input/data sensitivity | p. 7 (3 EXPERIMENTS) |
| Without discrete planning, the policy performs poorly. | component/input/data sensitivity | p. 8 (3 EXPERIMENTS) |
| Table 3: Summary of all hyper-parameters. B COMPARISON WITH MODEL-FREE RL ON SINGLE-TOOL TASKS In this work, we focus on solving long-horizon multi-tool tasks. ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our method consists of three components, (1) a trajectory optimizer that acts as an expert that applies gradient-based optimization on the differentiable simulator to ... | Each entry shows the normalized improvement / success rate. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS) |
| Primary metric/result | Method Task (H) LiftSpread (2) GatherTransport (2) CutRearrange (3) Tool A only Trajectory Opt (Oracle) 0.755 / 0% 0.386 / 0% 0.033 / 0% ... | numeric claim only at cited anchor | p. 7 (3 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / 3 EXPERIMENTS - extractive body cue:** These modules share the same encoder architecture: 4 convolutional layers with a kernel size of 4 and a stride of 2 and a channel size ...
- **p. 14 / A IMPLEMENTATION DETAILS - extractive body cue:** Model parameter Value dimension of latent space 8 MLP hidden node number 1024 Training parameters Value learning rate 0.001 batch size 128 optimizer Adam beta1 ...
- **p. 14 / A IMPLEMENTATION DETAILS - extractive body cue:** Model parameter Value dimension of latent space 8 MLP hidden node number 1024 Training parameters Value learning rate 0.001 batch size 128 optimizer Adam beta1 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In Table 3, we can see that the learned skills (labeled as Behavior Cloning) approach the normalized performance of the trajectory optimization (Trajectory Opt) ... | p. 6 (3 EXPERIMENTS) |
| body limitation/failure cue | 3.4 RESULT ANALYSIS We show that DiffSkill is able to solve the challenging long-horizon, tool-use tasks from the sensory observation (RGB-D) while the baselines ... | p. 7 (3 EXPERIMENTS) |
| body limitation/failure cue | On the other hand, if we do not optimize for the intermediate goals, we also cannot determine which tools to use at evaluation time, ... | p. 8 (3 EXPERIMENTS) |
| body limitation/failure cue | In this way, a normalized performance of 0 representing a policy that does nothing and a normalized performance of 1 representing an upper bound ... | p. 6 (3 EXPERIMENTS) |
| body limitation/failure cue | This is because the trajectory optimizer is more reliable at finding partial solutions that transport part of the dough to the target locations but ... | p. 7 (3 EXPERIMENTS) |
| body limitation/failure cue | There are a few interesting directions for future work. | p. 9 (4 RELATED WORK) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Model parameter Value dimension of latent space 8 MLP hidden node number 1024 Training parameters Value learning rate 0.001 batch size 128 optimizer Adam ... | p. 14 (A IMPLEMENTATION DETAILS) |
| In this section, we will discuss our experimental setup, implementation details and comparison results. | p. 5 (3 EXPERIMENTS) |
| The VAE, feasibility and the score predictor also share the same weights for the encoder. | p. 6 (3 EXPERIMENTS) |
| For each configuration, we run the optimizer for each tool separately to generate trajectories of length 50. | p. 6 (3 EXPERIMENTS) |
| A list of the hyperparameters used can be found in Table 3. | p. 14 (A IMPLEMENTATION DETAILS) |
| 2 to obtain cost C(k, z) ; Choose k, z that minimizes C(k, z); for i ←0 to H do Reset tools to initial ... | p. 5 (2 METHOD) |
| Additionally, the trajectory optimizer takes minutes to run, which is too slow during evaluation for real-time applications. | p. 4 (2 METHOD) |
| Variational Auto-Encoder: As will be explained in Section 2.4, we will plan to compose skills in a latent space instead of optimizing directly in ... | p. 4 (2 METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 3 EXPERIMENTS - extractive body cue:** In Table 3, we can see that the learned skills (labeled as Behavior Cloning) approach the normalized performance of the trajectory optimization (Trajectory Opt) on ...
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** 3.4 RESULT ANALYSIS We show that DiffSkill is able to solve the challenging long-horizon, tool-use tasks from the sensory observation (RGB-D) while the baselines cannot.
- **p. 8 / 3 EXPERIMENTS - extractive body cue:** On the other hand, if we do not optimize for the intermediate goals, we also cannot determine which tools to use at evaluation time, since ...
- **p. 6 / 3 EXPERIMENTS - extractive body cue:** In this way, a normalized performance of 0 representing a policy that does nothing and a normalized performance of 1 representing an upper bound of ...
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** This is because the trajectory optimizer is more reliable at finding partial solutions that transport part of the dough to the target locations but does ...
- **p. 9 / 4 RELATED WORK - extractive body cue:** There are a few interesting directions for future work.

- **Evidence anchors reviewed:** datasets p. 5 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS), p. 5 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS), metrics p. 6 (3 EXPERIMENTS), p. 7 (Figure/Table caption), p. 6 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS), p. 14 (A IMPLEMENTATION DETAILS), baselines p. 6 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS), p. 2 (Figure/Table caption), p. 6 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS), results p. 7 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Method Task LiftSpread GatherTransport CutRearrange No Discrete Planning 0.758 / 20% 0.312 / 0% 0.118 / 0% Direct Execution (Random) 0.593 / 15% 0.369 / 0% 0.018 / 2.5% Direct ... (p. 8, 3 EXPERIMENTS).
- **Metric evidence:** After training, we find the feasibility and score predictor to perform well on the held out trajectories, achieving a L2 error of less than 0.05 for the score predictor and ... (p. 6, 3 EXPERIMENTS).
- **Baseline/ablation evidence:** Method Task LiftSpread GatherTransport CutRearrange No Discrete Planning 0.758 / 20% 0.312 / 0% 0.118 / 0% Direct Execution (Random) 0.593 / 15% 0.369 / 0% 0.018 / 2.5% Direct ... (p. 8, 3 EXPERIMENTS).
- **Failure/negative evidence:** This threshold is manually picked by observing the performance gap between successful and failed trajectories. (p. 6, 3 EXPERIMENTS).
