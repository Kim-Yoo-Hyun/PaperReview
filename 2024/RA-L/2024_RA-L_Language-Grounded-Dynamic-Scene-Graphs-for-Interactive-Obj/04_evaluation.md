# Evaluation - Language-Grounded Dynamic Scene Graphs for Interactive Object Search with Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2403.08605; PDF retrieval source: https://arxiv.org/pdf/2403.08605. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS)): Similarly, while HIMOS achieves a high success rate, it is unable to explore efficiently.

## Evaluation Body Digest

- **p. 6 / V. EXPERIMENTS - extractive body cue:** Simulation Experiments We instantiate the task in the iGibson simulator [32] with a Fetch robot.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** We found that real-world scenes contained in iGibson regularly feature constant-diameter corridors and narrow passages due to furniture placements, which impede detecting rooms based on ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Evaluated across 10 episodes and all test scenes with 2D grid resolution of 0.05 m to account for thin walls.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** In this task, the robot does not receive a specific object class to find, but rather a fuzzy description, such as "I am hungry.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** For simplicity, we recompute the scene graph each time step.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Random: uniform random choice among all available actions (detected frontiers and closed objects).
- **p. 7 / V. EXPERIMENTS - extractive body cue:** In contrast, MoMa-LLM achieves similar success rates as HIMOS with a much higher search efficiency, both in terms of SPL and AUC-E.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Success rate (SR): the share of episodes in which the agent finds the target object.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mobile base와 one/two-arm manipulation environment.
- **Input boundary:** egocentric RGB-D, language/task goal, base-arm proprioception.
- **Output/decision under evaluation:** base motion plus arm/gripper action.
- **Primary target:** long-horizon task success, reachability, collision과 recovery.
- **Detected evaluation headings:** V. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Similarly, while HIMOS achieves a high success rate, it is unable to explore efficiently. | p. 7 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | In contrast, MoMa-LLM achieves similar success rates as HIMOS with a much higher search efficiency, both in terms of SPL and AUC-E. | p. 7 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | This results in an efficiency curve, in which the best policies are located in the top left corner, enabling the comparison of success rates ... | p. 6 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Success rate (SR): the share of episodes in which the agent finds the target object. | p. 6 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | ESC-Interactive: ESC is a recent approach for semantic object search [27] which scores frontiers based on object-object and object-room co-occurrences as well as their ... | p. 5 (V. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / V. EXPERIMENTS - extractive body cue:** Simulation Experiments We instantiate the task in the iGibson simulator [32] with a Fetch robot.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** We found that real-world scenes contained in iGibson regularly feature constant-diameter corridors and narrow passages due to furniture placements, which impede detecting rooms based on ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Evaluated across 10 episodes and all test scenes with 2D grid resolution of 0.05 m to account for thin walls.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** In this task, the robot does not receive a specific object class to find, but rather a fuzzy description, such as "I am hungry.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** For simplicity, we recompute the scene graph each time step.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Random: uniform random choice among all available actions (detected frontiers and closed objects).

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. MoMa-LLM performs long-horizon interactive object search in house- hold environments from language queries using dynamically built scene graphs. graphs from dense maps and ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. MoMa-LLM: From posed RGB-D images and semantics, we construct a semantic 3D map from which we extract a various occupancy maps in the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. Room Classification Prompt: based on the objects and room clusters of the scene graph, an LLM performs open-vocabulary classification. edges and nodes of ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4. High-level Reasoning Prompt: We encode the extracted scene representation to natural language, providing structured information to a language model. with semantic meaning. Firstly, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5. Interactive search efficiency curve in simulation. Each point depicts the success rate for a given maximum time budget (x-axis). training scenes for the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6. We construct a real-world apartment covering four rooms and 54 objects and transfer the model to a Toyota HSR robot. these objects would ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Simulation Experiments We instantiate the task in the iGibson simulator [32] with a Fetch robot. | embodiment, simulator version and control stack | p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Task/environment | We found that real-world scenes contained in iGibson regularly feature constant-diameter corridors and narrow passages due to furniture placements, which impede detecting rooms based ... | reset, timeout, object/scene variation | p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |
| Observation/sensor | egocentric RGB-D, language/task goal, base-arm proprioception | calibration, preprocessing, privileged input | p. 5 (IV. MOMA-LLM), p. 5 (IV. MOMA-LLM) |
| Output/decision | base motion plus arm/gripper action | action frame, controller and termination | p. 3 (IV. MOMA-LLM), p. 4 (IV. MOMA-LLM) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In contrast, MoMa-LLM achieves similar success rates as HIMOS with a much higher search efficiency, both in terms of SPL and AUC-E. | definition/direction/unit from same section | p. 7 (V. EXPERIMENTS) |
| Success rate (SR): the share of episodes in which the agent finds the target object. | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| This results in an efficiency curve, in which the best policies are located in the top left corner, enabling the comparison of success rates ... | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| Similarly, while HIMOS achieves a high success rate, it is unable to explore efficiently. | definition/direction/unit from same section | p. 7 (V. EXPERIMENTS) |
| ESC-Interactive: ESC is a recent approach for semantic object search [27] which scores frontiers based on object-object and object-room co-occurrences as well as their ... | definition/direction/unit from same section | p. 5 (V. EXPERIMENTS) |
| Fig. 6. We construct a real-world apartment covering four rooms and 54 objects and transfer the model to a Toyota HSR robot. these objects ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Fig. 2. MoMa-LLM: From posed RGB-D images and semantics, we construct a semantic 3D map from which we extract a various occupancy maps in ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Fig. 3. Room Classification Prompt: based on the objects and room clusters of the scene graph, an LLM performs open-vocabulary classification. edges and nodes ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Unstructured LLM: This baseline provides the scene graph in a JSON format without any additional structure to the language model. | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |
| Baselines: We compare our approach against heuristic-based, recent learning-based, and language-based methods. | comparison identity and matched condition | p. 5 (V. EXPERIMENTS) |
| We provide all baselines except Unstructured LLM with a ground truth done() decision when the object has been observed. | comparison identity and matched condition | p. 5 (V. EXPERIMENTS) |
| ESC in contrast, is able to exploit the co-occurrences to improve over the other baselines. | comparison identity and matched condition | p. 7 (V. EXPERIMENTS) |
| We evaluate both MoMa-LLM and the most efficient baseline, ESC, on identical start positions and targets. | comparison identity and matched condition | p. 7 (V. EXPERIMENTS) |
| This results in an efficiency curve, in which the best policies are located in the top left corner, enabling the comparison of success rates ... | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Unstructured LLM: This baseline provides the scene graph in a JSON format without any additional structure to the language model. | component/input/data sensitivity | p. 6 (V. EXPERIMENTS) |
| We then perform a number of ablations of the language encodings. | component/input/data sensitivity | p. 7 (V. EXPERIMENTS) |
| Removing the history also leads to a, although smaller, drop in performance. | component/input/data sensitivity | p. 7 (V. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our approach incorporates a scene understanding module that, given object detections, constructs open-vocabulary scene ∗Equal contribution. | Similarly, while HIMOS achieves a high success rate, it is unable to explore efficiently. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Primary metric/result | In contrast, MoMa-LLM achieves similar success rates as HIMOS with a much higher search efficiency, both in terms of SPL and AUC-E. | numeric claim only at cited anchor | p. 7 (V. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Evaluated across 10 episodes and all test scenes with 2D grid resolution of 0.05 m to account for thin walls.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Both methods succeeded in 8/10 episodes, demonstrating the successful transfer of the system to the real world.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Furthermore, the agent was able to react to the (unseen) subpolicy failures, such as re-trying to open a drawer when the gripper slipped off ... | p. 7 (V. EXPERIMENTS) |
| body limitation/failure cue | The two failures stemmed from irrecoverable failures of the subpolicies, in particular, collisions of the base during navigation or of the arm while opening ... | p. 7 (V. EXPERIMENTS) |
| body limitation/failure cue | Object interactions, distance travelled and infeasible actions averaged over all episodes, including early terminated failures. | p. 6 (V. EXPERIMENTS) |
| body limitation/failure cue | This metric does not take into account the costs of object interactions. | p. 6 (V. EXPERIMENTS) |
| body limitation/failure cue | Fig. 6. We construct a real-world apartment covering four rooms and 54 objects and transfer the model to a Toyota HSR robot. these objects ... | p. 8 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For simplicity, we recompute the scene graph each time step. | p. 5 (V. EXPERIMENTS) |
| More advanced implementations would reduce costs through incremental updates. | p. 5 (V. EXPERIMENTS) |
| We terminate an episode if the agent reaches 50 high-level steps, indicating being stuck. | p. 6 (V. EXPERIMENTS) |
| We calculate the integral up to 5,000 low-level steps, at which points almost all methods make no further progress. | p. 6 (V. EXPERIMENTS) |
| 1 Department of Computer Science, University of Freiburg, Germany. | p. 1 (I. INTRODUCTION) |
| Based on this, we compute a Generalized Voronoi Diagram (GVD) that holds a set of points V with the same clearance to the closest ... | p. 3 (IV. MOMA-LLM) |
| Grounded High-Level Planning We encode the accumulated knowledge of the scene graph into natural language by extracting the relevant components and embedding them in ... | p. 4 (IV. MOMA-LLM) |
| 1) Scene Structure: We encode the main room-object structure from the scene graph into a structured list of rooms and their containing objects and ... | p. 4 (IV. MOMA-LLM) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / V. EXPERIMENTS - extractive body cue:** Furthermore, the agent was able to react to the (unseen) subpolicy failures, such as re-trying to open a drawer when the gripper slipped off the ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** The two failures stemmed from irrecoverable failures of the subpolicies, in particular, collisions of the base during navigation or of the arm while opening the ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Object interactions, distance travelled and infeasible actions averaged over all episodes, including early terminated failures.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** This metric does not take into account the costs of object interactions.
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6. We construct a real-world apartment covering four rooms and 54 objects and transfer the model to a Toyota HSR robot. these objects would ...

- **PDF anchors reviewed:** datasets p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), metrics p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 8 (Figure/Table caption), baselines p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), results p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
