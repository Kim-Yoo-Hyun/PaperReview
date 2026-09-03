# Evaluation - Rapidly-Exploring Random Trees: A New Tool for Path Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (4 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://lavalle.pl/rrtpubs.html; PDF retrieval source: https://lavalle.pl/papers/Lav98c.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 2 (2. Rapidly-Exploring Random Trees), p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (3. Nice Properties of RRTs), p. 3 (3. Nice Properties of RRTs)): For holonomie planning, one can define (ru) = and /lull <1, which implies that any bounded velocity can be achieved.

## Evaluation Body Digest

- **p. 1 / 1 Introduction - extractive body cue:** Using state-space representations, this class of problems includes kinodynamic planning [3], which is an extremely general and important area in robotics, virtual prototyping, and many ...
- **p. 1 / 1 Introduction - extractive body cue:** The probabilistic roadmap technique might require the connections of thousands of configurations or states to find a soluti and if each connection is akin toa ...
- **p. 2 / 2. Rapidly-Exploring Random Trees - extractive body cue:** States in Xj» could correspond to ver locity bounds, configurations at which a robot is in collision with an obstacle in the world, or several ...
- **p. 3 / 3. Nice Properties of RRTs - extractive body cue:** Although the construction method is simple, it is no easy task to find a method that yields such desirable behavior.
- **p. 3 / 3. Nice Properties of RRTs - extractive body cue:** Based on simulation experiments, such as the one shown above, we have concluded that the generated paths are not far from optimal and that the ...
- **p. 2 / 3. Nice Properties of RRTs - extractive body cue:** The key advantages of RRTs are: 1) the expansion of an RRT is heavily biased. toward unexplored portions of the state space; 2) the dis ...
- **p. 3 / 3. Nice Properties of RRTs - extractive body cue:** A. probabilistic roadmap often suffers in performance because many extra edges are generated in attempts to form a connected roadmap.
- **p. 1 / Abstract - extractive body cue:** To date, we have successfully applied RRTs to holonomic, nonholonomic, and kinodynamic planning problems of up to twelve degrees of freedom.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** graph, configuration space 또는 task-and-motion planning domain.
- **Input boundary:** start/goal, map, dynamics와 successor/operator description.
- **Output/decision under evaluation:** feasible action sequence 또는 minimum-cost plan.
- **Primary target:** path cost, goal reachability, feasibility와 computation.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 2. Rapidly-Exploring Random Trees | EMPIRICAL / SIMULATION | For holonomie planning, one can define (ru) = and /lull <1, which implies that any bounded velocity can be achieved. | p. 2 (2. Rapidly-Exploring Random Trees) |
| Abstract | EMPIRICAL / SIMULATION | To date, we have successfully applied RRTs to holonomic, nonholonomic, and kinodynamic planning problems of up to twelve degrees of freedom. | p. 1 (Abstract) |
| 1 Introduction | EMPIRICAL / SIMULATION | Given these successes, and the fact that there is little hope of ever obtaining an efficient, general path planning algorithm, it is natural to ... | p. 1 (1 Introduction) |
| 1 Introduction | EMPIRICAL / SIMULATION | parameters as possible, This tends to lead to better performance analysis and consistency of behavior. | p. 2 (1 Introduction) |
| 3. Nice Properties of RRTs | EMPIRICAL / SIMULATION | A. probabilistic roadmap often suffers in performance because many extra edges are generated in attempts to form a connected roadmap. | p. 3 (3. Nice Properties of RRTs) |

## Dataset / Benchmark Role

- **p. 1 / 1 Introduction - extractive body cue:** Using state-space representations, this class of problems includes kinodynamic planning [3], which is an extremely general and important area in robotics, virtual prototyping, and many ...
- **p. 1 / 1 Introduction - extractive body cue:** The probabilistic roadmap technique might require the connections of thousands of configurations or states to find a soluti and if each connection is akin toa ...
- **p. 2 / 2. Rapidly-Exploring Random Trees - extractive body cue:** States in Xj» could correspond to ver locity bounds, configurations at which a robot is in collision with an obstacle in the world, or several ...
- **p. 3 / 3. Nice Properties of RRTs - extractive body cue:** Although the construction method is simple, it is no easy task to find a method that yields such desirable behavior.
- **p. 3 / 3. Nice Properties of RRTs - extractive body cue:** Based on simulation experiments, such as the one shown above, we have concluded that the generated paths are not far from optimal and that the ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- figure/table caption PDF body cue not selected; no claim inferred

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Using state-space representations, this class of problems includes kinodynamic planning [3], which is an extremely general and important area in robotics, virtual prototyping, and ... | embodiment, simulator version and control stack | p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Task/environment | The probabilistic roadmap technique might require the connections of thousands of configurations or states to find a soluti and if each connection is akin ... | reset, timeout, object/scene variation | p. 1 (1 Introduction), p. 2 (2. Rapidly-Exploring Random Trees) |
| Observation/sensor | start/goal, map, dynamics와 successor/operator description | calibration, preprocessing, privileged input | p. 2 (9 Return T), p. 2 (2. Rapidly-Exploring Random Trees) |
| Output/decision | feasible action sequence 또는 minimum-cost plan | action frame, controller and termination | p. 1 (Abstract), p. 1 (Body text (section boundary not confidently recovered)) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The key advantages of RRTs are: 1) the expansion of an RRT is heavily biased. toward unexplored portions of the state space; 2) the ... | definition/direction/unit from same section | p. 2 (3. Nice Properties of RRTs) |
| A. probabilistic roadmap often suffers in performance because many extra edges are generated in attempts to form a connected roadmap. | definition/direction/unit from same section | p. 3 (3. Nice Properties of RRTs) |
| To date, we have successfully applied RRTs to holonomic, nonholonomic, and kinodynamic planning problems of up to twelve degrees of freedom. | definition/direction/unit from same section | p. 1 (Abstract) |
| Given these successes, and the fact that there is little hope of ever obtaining an efficient, general path planning algorithm, it is natural to ... | definition/direction/unit from same section | p. 1 (1 Introduction) |
| GENERATERRT (ini: At) 1 Tinit(tinie); | definition/direction/unit from same section | p. 2 (2. Rapidly-Exploring Random Trees) |
| A crucial piece of analysis that remains open is the rate of convergence | definition/direction/unit from same section | p. 3 (3. Nice Properties of RRTs) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The key advantages of RRTs are: 1) the expansion of an RRT is heavily biased. toward unexplored portions of the state space; 2) the ... | comparison identity and matched condition | p. 2 (3. Nice Properties of RRTs) |
| Based on several experiments in 2D, convex spaces, the ‘optimal path to the root in comparison to the path in the RRT, differ on ... | comparison identity and matched condition | p. 3 (3. Nice Properties of RRTs) |
| For these reasons and out preliminary observations from. experimentation, it appears that an RRT-based planner may generally yield better performance than a probabilistic roadmap-based ... | comparison identity and matched condition | p. 3 (3. Nice Properties of RRTs) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The key advantages of RRTs are: 1) the expansion of an RRT is heavily biased. toward unexplored portions of the state space; 2) the ... | component/input/data sensitivity | p. 2 (3. Nice Properties of RRTs) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Tn this paper, we introduce a randomized data structure for path planning that is designed for problems that, have nonholonomic constraints. | For holonomie planning, one can define (ru) = and /lull <1, which implies that any bounded velocity can be achieved. | PDF body cue; verify exact table/figure and matched conditions | p. 2 (2. Rapidly-Exploring Random Trees), p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (3. Nice Properties of RRTs), p. 3 (3. Nice Properties of RRTs) |
| Primary metric/result | To date, we have successfully applied RRTs to holonomic, nonholonomic, and kinodynamic planning problems of up to twelve degrees of freedom. | numeric claim only at cited anchor | p. 1 (Abstract) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Collision detection can be performed by an incremental method such as Mirtich's V-Clip. | p. 2 (9 Return T) |
| body limitation/failure cue | States in Xj» could correspond to ver locity bounds, configurations at which a robot is in collision with an obstacle in the world, or ... | p. 2 (2. Rapidly-Exploring Random Trees) |
| body limitation/failure cue | In a related paper [7], we presented an RRT-based, planner that computes collision-free kinodynamic trajec~ tories that fire thrusters for hovercrafts and satellites in, ... | p. 3 (4 Examples) |
| body limitation/failure cue | Collision detection is a key bottleneck in path planning, and an RRT is completely suited for incremental collision detection, This allows the fastest-avaliable collision ... | p. 3 (3. Nice Properties of RRTs) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Several desir- ‘able properties and a basic implementation of RRTs are discussed. | p. 1 (Abstract) |
| For a kinodynamic planning problem, X =T(C), which is the tangent bundle of the configuration space [7] (a state encodes both configuration and velocity). | p. 2 (2. Rapidly-Exploring Random Trees) |
| The vector & denotes the derivative of state with respect to time, This controlstheoretic representation is powerful enough to encode virtually any kinematic and ... | p. 2 (2. Rapidly-Exploring Random Trees) |
| In a related paper [7], we presented an RRT-based, planner that computes collision-free kinodynamic trajec~ tories that fire thrusters for hovercrafts and satellites in, ... | p. 3 (4 Examples) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / 9 Return T - extractive body cue:** Collision detection can be performed by an incremental method such as Mirtich's V-Clip.
- **p. 2 / 2. Rapidly-Exploring Random Trees - extractive body cue:** States in Xj» could correspond to ver locity bounds, configurations at which a robot is in collision with an obstacle in the world, or several ...
- **p. 3 / 4 Examples - extractive body cue:** In a related paper [7], we presented an RRT-based, planner that computes collision-free kinodynamic trajec~ tories that fire thrusters for hovercrafts and satellites in, cluttered ...
- **p. 3 / 3. Nice Properties of RRTs - extractive body cue:** Collision detection is a key bottleneck in path planning, and an RRT is completely suited for incremental collision detection, This allows the fastest-avaliable collision detection ...

- **Evidence anchors reviewed:** datasets p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (2. Rapidly-Exploring Random Trees), p. 3 (3. Nice Properties of RRTs), p. 3 (3. Nice Properties of RRTs), metrics p. 2 (3. Nice Properties of RRTs), p. 3 (3. Nice Properties of RRTs), p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (2. Rapidly-Exploring Random Trees), p. 3 (3. Nice Properties of RRTs), baselines p. 2 (3. Nice Properties of RRTs), p. 3 (3. Nice Properties of RRTs), p. 3 (3. Nice Properties of RRTs), results p. 2 (2. Rapidly-Exploring Random Trees), p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (3. Nice Properties of RRTs), p. 3 (3. Nice Properties of RRTs).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (4 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** For these reasons and out preliminary observations from. experimentation, it appears that an RRT-based planner may generally yield better performance than a probabilistic roadmap-based planner; however, itis difficult to make ... (p. 3, 3. Nice Properties of RRTs).
- **Metric evidence:** parameters as possible, This tends to lead to better performance analysis and consistency of behavior. (p. 2, 1 Introduction).
- **Baseline/ablation evidence:** The key advantages of RRTs are: 1) the expansion of an RRT is heavily biased. toward unexplored portions of the state space; 2) the dis tribution of vertices in an ... (p. 2, 3. Nice Properties of RRTs).
- **Failure/negative evidence:** The primary difficulty with existing techniques is that, although powerful for standard path planning, they do not naturally extend to general nonholonomic planning problems. (p. 1, 1 Introduction).
