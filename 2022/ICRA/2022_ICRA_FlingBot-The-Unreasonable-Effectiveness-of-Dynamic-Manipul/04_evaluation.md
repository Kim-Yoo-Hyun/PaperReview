# Evaluation - FlingBot: The Unreasonable Effectiveness of Dynamic Manipulation for Cloth Unfolding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2105.03655; PDF retrieval source: https://arxiv.org/pdf/2105.03655. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4 Evaluation), p. 9 (4.4 Results), p. 8 (Figure/Table caption), p. 8 (4.4 Results), p. 9 (4.4 Results), p. 1 (Figure/Table caption)): While the pick & place baseline discovered a similar strategy, its performance is inherently limited by quasi-static actions, requiring significantly more steps to achieve a final coverage lower than FlingBot's.

## Evaluation Body Digest

- **p. 9 / 4.4 Results - extractive PDF cue:** The performance is reported averaged over 10 test episodes, where real-world grasp errors are filtered out (see "Real World Failure Cases" below).
- **p. 7 / 4 Evaluation - extractive PDF cue:** In real, the simulation policy is deployed to collect real world experience on 150 Normal Rect episodes (257 steps), optimized on both simulation and real ...
- **p. 6 / 4 Evaluation - extractive PDF cue:** 4.2 Task Dataset Generation Each task is specified by a cloth mesh, mass, stiffness, and initial configuration.
- **p. 6 / 4 Evaluation - extractive PDF cue:** To evaluate our policy, we load a task from the testing task datasets then run the policy for 10 steps or until the policy predicts ...
- **p. 7 / 4 Evaluation - extractive PDF cue:** In simulation, the policy is trained on 2000 rectangular cloths sampled evenly between Normal Rect and Large Rect, and evaluated on 600 novel tasks split ...
- **p. 9 / 4.4 Results - extractive PDF cue:** Task generation is automated using the robot arms by randomly grasping the cloth at height 0.50m then dropping it back on the workspace.
- **p. 8 / 4.4 Results - extractive PDF cue:** In this experiment, we investigate these approaches' performance on cloths which have dimensions larger than the robot arm's reach range.
- **p. 8 / 4 Evaluation - extractive PDF cue:** This demonstrates the difficulty of unfolding from highly crumpled initial configurations and dynamic action's superior efficiency. spite the cloth physical parameter variations in the training ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** 4 Evaluation (p. 6); 4.4 Results (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | While the pick & place baseline discovered a similar strategy, its performance is inherently limited by quasi-static actions, requiring significantly more steps to achieve ... | p. 7 (4 Evaluation) |
| 4.4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | 2, we report that our policy achieves over 80% on all cloth types, which outperforms the quasi-static pick & place baseline by over 40%. | p. 9 (4.4 Results) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5: Coverage v.s. Steps. With 95% confidence interval shaded. FlingBot can achieve high coverage within a few interaction steps, while the quasi-static baselines ... | p. 8 (Figure/Table caption) |
| 4.4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | 5, [FlingBot] achieves over 80% within 3 interactions (simulation normal cloth), while the quasi-static baselines never reach such a high coverage even with significantly ... | p. 8 (4.4 Results) |
| 4.4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Additionally, we report that the pre-finetune performance of FlingBot on Normal Cloths is 69.8%, justifying our decision to finetune to get a 12.1% improvement. | p. 9 (4.4 Results) |

## Dataset / Benchmark Role

- **p. 9 / 4.4 Results - extractive PDF cue:** The performance is reported averaged over 10 test episodes, where real-world grasp errors are filtered out (see "Real World Failure Cases" below).
- **p. 7 / 4 Evaluation - extractive PDF cue:** In real, the simulation policy is deployed to collect real world experience on 150 Normal Rect episodes (257 steps), optimized on both simulation and real ...
- **p. 6 / 4 Evaluation - extractive PDF cue:** 4.2 Task Dataset Generation Each task is specified by a cloth mesh, mass, stiffness, and initial configuration.
- **p. 6 / 4 Evaluation - extractive PDF cue:** To evaluate our policy, we load a task from the testing task datasets then run the policy for 10 steps or until the policy predicts ...
- **p. 7 / 4 Evaluation - extractive PDF cue:** In simulation, the policy is trained on 2000 rectangular cloths sampled evenly between Normal Rect and Large Rect, and evaluated on 600 novel tasks split ...
- **p. 9 / 4.4 Results - extractive PDF cue:** Task generation is automated using the robot arms by randomly grasping the cloth at height 0.50m then dropping it back on the workspace.
- **p. 8 / 4.4 Results - extractive PDF cue:** In this experiment, we investigate these approaches' performance on cloths which have dimensions larger than the robot arm's reach range.
- **p. 8 / 4 Evaluation - extractive PDF cue:** This demonstrates the difficulty of unfolding from highly crumpled initial configurations and dynamic action's superior efficiency. spite the cloth physical parameter variations in the training ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Cloth unfolding with dynamic inter- actions. Given a severely crumpled cloth, Fling- Bot uses a high-speed fling to unfurl the cloth with as ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Action Primitives. The dynamic Fling primitive starts with a two-arm grasp at the left L and right R grasp locations with center point ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Method Overview. From a top-down RGB image a), our policy evaluates a batch of different action rotations and scales by transforming the observation ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4: Qualitative Results in Real World. Cloth coverages are labeled on the top right corner. Red and green circles represent grasps by left and ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5: Coverage v.s. Steps. With 95% confidence interval shaded. FlingBot can achieve high coverage within a few interaction steps, while the quasi-static baselines never ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 1: Simulation Experiments (Final / Delta Coverage). Increased Reach Range. In this experiment, we investigate these approaches' performance on cloths which have dimensions larger ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 2: Real World Experiment (Final / Delta Coverage). Evaluating Real-World Unfolding. Finally, we fine- tune and evaluate our simulation models from Tab. 1 with ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Figure 6: Qualitative Results in Simulation Experiments. 6.2 Failure cases 1.0 1.2 1.4 1.6 Fling speed

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The performance is reported averaged over 10 test episodes, where real-world grasp errors are filtered out (see "Real World Failure Cases" below). | embodiment, simulator version and control stack | p. 9 (4.4 Results), p. 7 (4 Evaluation) |
| Task/environment | In real, the simulation policy is deployed to collect real world experience on 150 Normal Rect episodes (257 steps), optimized on both simulation and ... | reset, timeout, object/scene variation | p. 7 (4 Evaluation), p. 6 (4 Evaluation) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 5 (3 Method), p. 2 (1 Introduction) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 3 (3 Method), p. 5 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The average grasp success rate is 78.0%, 45.0%, and 75.8% for normal rectangular, large rectangular, and shirts respectively. | definition/direction/unit from same section | p. 9 (4.4 Results) |
| This fling speed module is trained using Deep Deterministic Policy Gradients (DDPG) [24] on the delta-coverage rewards to maximize single-step returns (discount factor γ ... | definition/direction/unit from same section | p. 7 (4 Evaluation) |
| The performance is reported averaged over 10 test episodes, where real-world grasp errors are filtered out (see "Real World Failure Cases" below). | definition/direction/unit from same section | p. 9 (4.4 Results) |
| Figure 4: Qualitative Results in Real World. Cloth coverages are labeled on the top right corner. Red and green circles represent grasps by left ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 9: To minimize collisions, arms should grasp points closer to their side (a) and be a reasonable distance away from each other (b). ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| Figure 5: Coverage v.s. Steps. With 95% confidence interval shaded. FlingBot can achieve high coverage within a few interaction steps, while the quasi-static baselines ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Finally, we evaluate the algorithm's performance on the real-world setup. | definition/direction/unit from same section | p. 6 (4 Evaluation) |
| While this choice also makes it possible for the normalized coverage to be greater than 1, it will still preserve performance rankings. | definition/direction/unit from same section | p. 6 (4 Evaluation) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to the quasi-static baselines, [FlingBot] increases the coverage by +52.0%, which is roughly twice that of the quasi-static baselines ( +27.1%, +24.8%, +23.1%). | comparison identity and matched condition | p. 8 (4.4 Results) |
| 2, we report that our policy achieves over 80% on all cloth types, which outperforms the quasi-static pick & place baseline by over 40%. | comparison identity and matched condition | p. 9 (4.4 Results) |
| Thus, we prefer the simpler [FlingBot] approach for comparisons with baselines. • Dynamic manipulation with fling parameter regression: [Fling-Reg] is identical to [FlingBot], but ... | comparison identity and matched condition | p. 8 (4 Evaluation) |
| 2b) and "pick and drag" (similar to Seita et al., with no lift step compared to pick and place) primitive respectively. | comparison identity and matched condition | p. 7 (4 Evaluation) |
| While the pick & place baseline discovered a similar strategy, its performance is inherently limited by quasi-static actions, requiring significantly more steps to achieve ... | comparison identity and matched condition | p. 7 (4 Evaluation) |
| Meanwhile, all quasi-static baselines exhibited worse cloth unfolding efficiency. | comparison identity and matched condition | p. 9 (4.4 Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 2: Action Primitives. The dynamic Fling primitive starts with a two-arm grasp at the left L and right R grasp locations with center ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary: • Our main contribution is in demonstrating the effectiveness of dynamic manipulation for cloth unfolding through our self-supervised learning framework, FlingBot. • ... | While the pick & place baseline discovered a similar strategy, its performance is inherently limited by quasi-static actions, requiring significantly more steps to achieve ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4 Evaluation), p. 9 (4.4 Results), p. 8 (Figure/Table caption), p. 8 (4.4 Results), p. 9 (4.4 Results), p. 1 (Figure/Table caption) |
| Primary metric/result | 2, we report that our policy achieves over 80% on all cloth types, which outperforms the quasi-static pick & place baseline by over 40%. | numeric claim only at cited anchor | p. 9 (4.4 Results) |

- Numeric sentences retained from the body:
- **p. 6 / 4 Evaluation - extractive PDF cue:** To evaluate our policy, we load a task from the testing task datasets then run the policy for 10 steps or until the policy predicts ...
- **p. 6 / 4 Evaluation - extractive PDF cue:** 4.2 Task Dataset Generation Each task is specified by a cloth mesh, mass, stiffness, and initial configuration.
- **p. 7 / 4 Evaluation - extractive PDF cue:** Fling Init Normal Rect (Real) P & P Fling Large Rect (Real) P & P Fling Shirt (Real) P & P Step 1 Step 2 ...
- **p. 7 / 4 Evaluation - extractive PDF cue:** In real, the simulation policy is deployed to collect real world experience on 150 Normal Rect episodes (257 steps), optimized on both simulation and real ...
- **p. 8 / 4 Evaluation - extractive PDF cue:** 0 2 4 6 8 10 Episode Step 0.2 0.4 0.6 0.8 1.0 Coverage (%) Sim Normal Rectangular Cloths 0 2 4 6 8 10 ...
- **p. 9 / 4.4 Results - extractive PDF cue:** 5 shows that our flinging policies take only 3 actions to reach their maximum coverages, while the quasi-static baselines take upwards of 8 steps to ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 8: Failure Cases in Simulation Experiments. 6.3 Real world fling parameter robustness In designing our motion primitive, we optimized fling parameters (waypoints, velocities, ... | p. 13 (Figure/Table caption) |
| body limitation/failure cue | We discuss more of real world grasp failures in Sec. | p. 9 (4.4 Results) |
| body limitation/failure cue | The performance is reported averaged over 10 test episodes, where real-world grasp errors are filtered out (see "Real World Failure Cases" below). | p. 9 (4.4 Results) |
| body limitation/failure cue | Figure 6: Qualitative Results in Simulation Experiments. 6.2 Failure cases 1.0 1.2 1.4 1.6 Fling speed | p. 12 (Figure/Table caption) |
| body limitation/failure cue | 1, [Fling-Reg] completely fails to perform the task, demonstrating the advantage of encoding inductive biases which leverage equivariances in the problem structure. | p. 8 (4 Evaluation) |
| body limitation/failure cue | Figure 9: To minimize collisions, arms should grasp points closer to their side (a) and be a reasonable distance away from each other (b). ... | p. 15 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| To evaluate our policy, we load a task from the testing task datasets then run the policy for 10 steps or until the policy ... | p. 6 (4 Evaluation) |
| All our coverage statistics are normalized (i.e., divided by the maximum possible coverage of the cloth in a flattened configuration) and can be easily ... | p. 6 (4 Evaluation) |
| FlingBot discovered through trial-and-error a two-arm corner and edge grasp when corners and edges are visible. | p. 7 (4 Evaluation) |
| While the pick & place baseline discovered a similar strategy, its performance is inherently limited by quasi-static actions, requiring significantly more steps to achieve ... | p. 7 (4 Evaluation) |
| FlingBot can achieve high coverage within a few interaction steps, while the quasi-static baselines never reach high coverages even with significantly more interaction steps. | p. 8 (4 Evaluation) |
| The system collected 257 experience steps over 150 cloth tasks for finetuning in total. | p. 9 (4.4 Results) |
| While the pick & place primitive only takes a median time of 8.8s, it is unable to reach the high coverages even with many ... | p. 9 (4.4 Results) |
| The network is trained using the Adam optimizer with a learning rate of 1e-3 and a weight decay of 1e-6. | p. 5 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 13 / Figure/Table caption - extractive PDF cue:** Figure 8: Failure Cases in Simulation Experiments. 6.3 Real world fling parameter robustness In designing our motion primitive, we optimized fling parameters (waypoints, velocities, accelera- ...
- **p. 9 / 4.4 Results - extractive PDF cue:** We discuss more of real world grasp failures in Sec.
- **p. 9 / 4.4 Results - extractive PDF cue:** The performance is reported averaged over 10 test episodes, where real-world grasp errors are filtered out (see "Real World Failure Cases" below).
- **p. 12 / Figure/Table caption - extractive PDF cue:** Figure 6: Qualitative Results in Simulation Experiments. 6.2 Failure cases 1.0 1.2 1.4 1.6 Fling speed
- **p. 8 / 4 Evaluation - extractive PDF cue:** 1, [Fling-Reg] completely fails to perform the task, demonstrating the advantage of encoding inductive biases which leverage equivariances in the problem structure.
- **p. 15 / Figure/Table caption - extractive PDF cue:** Figure 9: To minimize collisions, arms should grasp points closer to their side (a) and be a reasonable distance away from each other (b). 6.6 ...

- **PDF anchors reviewed:** datasets p. 9 (4.4 Results), p. 7 (4 Evaluation), p. 6 (4 Evaluation), p. 6 (4 Evaluation), p. 7 (4 Evaluation), p. 9 (4.4 Results), metrics p. 9 (4.4 Results), p. 7 (4 Evaluation), p. 9 (4.4 Results), p. 7 (Figure/Table caption), p. 15 (Figure/Table caption), p. 8 (Figure/Table caption), baselines p. 8 (4.4 Results), p. 9 (4.4 Results), p. 8 (4 Evaluation), p. 7 (4 Evaluation), p. 7 (4 Evaluation), p. 9 (4.4 Results), results p. 7 (4 Evaluation), p. 9 (4.4 Results), p. 8 (Figure/Table caption), p. 8 (4.4 Results), p. 9 (4.4 Results), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
