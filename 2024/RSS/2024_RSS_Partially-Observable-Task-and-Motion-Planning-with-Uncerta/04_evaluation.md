# Evaluation - Partially Observable Task and Motion Planning with Uncertainty and Risk Awareness

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p118.html; PDF retrieval source: https://arxiv.org/pdf/2403.10454.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 9 (VII. REAL-WORLD IMPLEMENTATION)): Fig. 4: Comparisons of model-learning strategies on a simplified grid-world environment in which an agent must navigate from the blue cell to the green cell. Red intensity corresponds to p, ...

## Evaluation Body Digest

- **p. 9 / VII. REAL-WORLD IMPLEMENTATION - extractive body cue:** Searching for Objects in Clutter This task is the real-world counterpart to the PARTIAL OBSERVABILITY simulated experiment.
- **p. 9 / VII. REAL-WORLD IMPLEMENTATION - extractive body cue:** In this task, the robot is equipped with a single RGBD camera mounted to the gripper, and must find and pick up a small cube ...
- **p. 7 / VI. SIMULATED EXPERIMENTS & ANALYSIS - extractive body cue:** We applied TAMPURA to five simulated and two realworld robotics problems, illustrated in Figure 2 and Figure 1,
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4: Comparisons of model-learning strategies on a simplified grid-world environment in which an agent must navigate from the blue cell to the green cell. ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: This figure illustrates five long-horizon planning tasks that TAMPURA is capable of solving. Each of them contains a unique type of uncertainty including ...
- **p. 9 / VII. REAL-WORLD IMPLEMENTATION - extractive body cue:** See the supplementary material for videos of successful completions under various initializations of these tasks.
- **p. 9 / VII. REAL-WORLD IMPLEMENTATION - extractive body cue:** Given the current probabilistic occupancy grid, generated from point cloud data from RGB-Depth cameras, we approximate a motion planning path with gripper interpolation and calculate ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 6: TAMPURA searching a workspace to find and pick up a cube, looking around and moving objects to find it. Top: images of robot ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** robot mechanism의 state와 task-space dynamics.
- **Input boundary:** joint/task state, reference와 sensor feedback.
- **Output/decision under evaluation:** torque, force, velocity 또는 position command.
- **Primary target:** tracking, stability, constraint satisfaction과 contact behavior.
- **Detected evaluation headings:** VI. SIMULATED EXPERIMENTS & ANALYSIS (p. 7); VII. REAL-WORLD IMPLEMENTATION (p. 9).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 4: Comparisons of model-learning strategies on a simplified grid-world environment in which an agent must navigate from the blue cell to the green ... | p. 7 (Figure/Table caption) |
| VII. REAL-WORLD IMPLEMENTATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | See the supplementary material for videos of successful completions under various initializations of these tasks. | p. 9 (VII. REAL-WORLD IMPLEMENTATION) |

## Dataset / Benchmark Role

- **p. 9 / VII. REAL-WORLD IMPLEMENTATION - extractive body cue:** Searching for Objects in Clutter This task is the real-world counterpart to the PARTIAL OBSERVABILITY simulated experiment.
- **p. 9 / VII. REAL-WORLD IMPLEMENTATION - extractive body cue:** In this task, the robot is equipped with a single RGBD camera mounted to the gripper, and must find and pick up a small cube ...
- **p. 7 / VI. SIMULATED EXPERIMENTS & ANALYSIS - extractive body cue:** We applied TAMPURA to five simulated and two realworld robotics problems, illustrated in Figure 2 and Figure 1,

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Top: Robot with wrist mounted camera looking for a banana. The robot plans to take information gathering actions based on a posterior estimate ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: This figure illustrates five long-horizon planning tasks that TAMPURA is capable of solving. Each of them contains a unique type of uncertainty including ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: Uncertainty and Risk Aware Task and Motion Planning. (a) The robot's continuous space of probabilistic beliefs about world state is partitioned into a ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4: Comparisons of model-learning strategies on a simplified grid-world environment in which an agent must navigate from the blue cell to the green cell. ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 5: TAMPURA moving cubes into a bowl without hitting a human in the workspace. Top row: images of robot execution. Bottom row: the robot's ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 6: TAMPURA searching a workspace to find and pick up a cube, looking around and moving objects to find it. Top: images of robot ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Searching for Objects in Clutter This task is the real-world counterpart to the PARTIAL OBSERVABILITY simulated experiment. | embodiment, simulator version and control stack | p. 9 (VII. REAL-WORLD IMPLEMENTATION), p. 9 (VII. REAL-WORLD IMPLEMENTATION) |
| Task/environment | In this task, the robot is equipped with a single RGBD camera mounted to the gripper, and must find and pick up a small ... | reset, timeout, object/scene variation | p. 9 (VII. REAL-WORLD IMPLEMENTATION), p. 7 (VI. SIMULATED EXPERIMENTS & ANALYSIS) |
| Observation/sensor | joint/task state, reference와 sensor feedback | calibration, preprocessing, privileged input | p. 3 (III. BACKGROUND), p. 3 (III. BACKGROUND) |
| Output/decision | torque, force, velocity 또는 position command | action frame, controller and termination | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 4: Comparisons of model-learning strategies on a simplified grid-world environment in which an agent must navigate from the blue cell to the green ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Fig. 2: This figure illustrates five long-horizon planning tasks that TAMPURA is capable of solving. Each of them contains a unique type of uncertainty ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| We applied TAMPURA to five simulated and two realworld robotics problems, illustrated in Figure 2 and Figure 1, | definition/direction/unit from same section | p. 7 (VI. SIMULATED EXPERIMENTS & ANALYSIS) |
| See the supplementary material for videos of successful completions under various initializations of these tasks. | definition/direction/unit from same section | p. 9 (VII. REAL-WORLD IMPLEMENTATION) |
| Given the current probabilistic occupancy grid, generated from point cloud data from RGB-Depth cameras, we approximate a motion planning path with gripper interpolation and ... | definition/direction/unit from same section | p. 9 (VII. REAL-WORLD IMPLEMENTATION) |
| Fig. 6: TAMPURA searching a workspace to find and pick up a cube, looking around and moving objects to find it. Top: images of ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 4: Comparisons of model-learning strategies on a simplified grid-world environment in which an agent must navigate from the blue cell to the green ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| The robot's task is to move these cubes into the bowl without colliding with a human's hand moving around in the workspace. | comparison identity and matched condition | p. 9 (VII. REAL-WORLD IMPLEMENTATION) |
| Fig. 5: TAMPURA moving cubes into a bowl without hitting a human in the workspace. Top row: images of robot execution. Bottom row: the ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The robot's task is to move these cubes into the bowl without colliding with a human's hand moving around in the workspace. | component/input/data sensitivity | p. 9 (VII. REAL-WORLD IMPLEMENTATION) |
| Fig. 5: TAMPURA moving cubes into a bowl without hitting a human in the workspace. Top row: images of robot execution. Bottom row: the ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To mitigate this, we introduce the concept of a belief-space controller, which takes the current belief as input and executes in closedloop fashion over ... | Fig. 4: Comparisons of model-learning strategies on a simplified grid-world environment in which an agent must navigate from the blue cell to the green ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 9 (VII. REAL-WORLD IMPLEMENTATION) |
| Primary metric/result | See the supplementary material for videos of successful completions under various initializations of these tasks. | numeric claim only at cited anchor | p. 9 (VII. REAL-WORLD IMPLEMENTATION) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Despite these novelties, TAMPURA, and TAMP in general, have several limitations. | p. 9 (VIII. DISCUSSION) |
| body limitation/failure cue | The primary failure modes were (1) failure in perception (due, we believe, to improperly calibrated hard-coded camera poses), and (2) issues with tension in ... | p. 9 (VII. REAL-WORLD IMPLEMENTATION) |
| body limitation/failure cue | Fig. 3: Uncertainty and Risk Aware Task and Motion Planning. (a) The robot's continuous space of probabilistic beliefs about world state is partitioned into ... | p. 3 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The primary failure modes were (1) failure in perception (due, we believe, to improperly calibrated hard-coded camera poses), and (2) issues with tension in ... | p. 9 (VII. REAL-WORLD IMPLEMENTATION) |
| The reduction from Mc to Ms is performed in several steps. | p. 4 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP) |
| Here, Pre ⊆ΨB is the set of belief propositions that must hold for a controller c ∈C to be executed, Eff ⊆ΨB is the ... | p. 4 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP) |
| Operator schemata In our implementation, the set of operators and the set of controllers are generated from a set of operator schemata. | p. 5 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / VIII. DISCUSSION - extractive body cue:** Despite these novelties, TAMPURA, and TAMP in general, have several limitations.
- **p. 9 / VII. REAL-WORLD IMPLEMENTATION - extractive body cue:** The primary failure modes were (1) failure in perception (due, we believe, to improperly calibrated hard-coded camera poses), and (2) issues with tension in the ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: Uncertainty and Risk Aware Task and Motion Planning. (a) The robot's continuous space of probabilistic beliefs about world state is partitioned into a ...

- **Evidence anchors reviewed:** datasets p. 9 (VII. REAL-WORLD IMPLEMENTATION), p. 9 (VII. REAL-WORLD IMPLEMENTATION), p. 7 (VI. SIMULATED EXPERIMENTS & ANALYSIS), metrics p. 7 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (VI. SIMULATED EXPERIMENTS & ANALYSIS), p. 9 (VII. REAL-WORLD IMPLEMENTATION), p. 9 (VII. REAL-WORLD IMPLEMENTATION), p. 10 (Figure/Table caption), baselines p. 7 (Figure/Table caption), p. 9 (VII. REAL-WORLD IMPLEMENTATION), p. 9 (Figure/Table caption), results p. 7 (Figure/Table caption), p. 9 (VII. REAL-WORLD IMPLEMENTATION).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
