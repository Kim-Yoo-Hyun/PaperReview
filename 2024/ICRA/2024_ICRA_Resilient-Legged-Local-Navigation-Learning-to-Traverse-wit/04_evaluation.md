# Evaluation - Resilient Legged Local Navigation: Learning to Traverse with Compromised Perception End-to-End

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2310.03581; PDF retrieval source: https://arxiv.org/pdf/2310.03581. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (V. RESULTS AND ANALYSES), p. 5 (V. RESULTS AND ANALYSES), p. 4 (IV. EXPERIMENTAL SETUP)): According to the results, all of the policies perform well when the visibility is 100 %, and the Planner achieves a perfect 100 % success rate.

## Evaluation Body Digest

- **p. 4 / IV. EXPERIMENTAL SETUP - extractive PDF cue:** Environments We verify our methodology on the quadruped ANYmal robot both in simulation and in the real world.
- **p. 4 / IV. EXPERIMENTAL SETUP - extractive PDF cue:** Training Settings For training, we consider the following settings: 1) Ours: As is presented in Sec.
- **p. 5 / V. RESULTS AND ANALYSES - extractive PDF cue:** Ours outperforms others in the metrics. commands directing away from the pit until the robot regains stability.
- **p. 5 / V. RESULTS AND ANALYSES - extractive PDF cue:** When the robot missteps into an invisible pit, the policy generates velocity Obstacles 100% Obstacles 50% Obstacles 0% Pits 100% Pits 50% Pits 0% 60 ...
- **p. 5 / V. RESULTS AND ANALYSES - extractive PDF cue:** According to the results, all of the policies perform well when the visibility is 100 %, and the Planner achieves a perfect 100 % success ...
- **p. 5 / V. RESULTS AND ANALYSES - extractive PDF cue:** Ours can have > 80% success rates even when the perception is fully corrupted, and generalize well to 0 % and 100 % visibility despite ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 4. We employ a terrain curriculum to facilitate learning. The terrains from top to bottom are obstacles on hilly, obstacles on boxes, pits on ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 2. Besides reaching the target in time, the robot should also reduce base collisions and avoid falls. An overview of our system is in ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** legged robot, terrain과 contact dynamics.
- **Input boundary:** proprioception, terrain/perception observation과 velocity command.
- **Output/decision under evaluation:** joint target, torque, footstep 또는 locomotion action.
- **Primary target:** velocity/progress, stability, energy와 terrain generalization.
- **Detected evaluation headings:** 3) Experimental validation of our method both in simula (p. 2); IV. EXPERIMENTAL SETUP (p. 4); V. RESULTS AND ANALYSES (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| V. RESULTS AND ANALYSES | EMPIRICAL / SIMULATION | According to the results, all of the policies perform well when the visibility is 100 %, and the Planner achieves a perfect 100 % ... | p. 5 (V. RESULTS AND ANALYSES) |
| V. RESULTS AND ANALYSES | EMPIRICAL / SIMULATION | However, as the visibility decreases, i.e., when perception failures increase, Ours drop performance much slower than the other two, and significantly outperform them. | p. 5 (V. RESULTS AND ANALYSES) |
| IV. EXPERIMENTAL SETUP | EMPIRICAL / SIMULATION | Each setting is run 3 times with different random seeds for statistics, which supports the significance of our performance by P Values. | p. 4 (IV. EXPERIMENTAL SETUP) |

## Dataset / Benchmark Role

- **p. 4 / IV. EXPERIMENTAL SETUP - extractive PDF cue:** Environments We verify our methodology on the quadruped ANYmal robot both in simulation and in the real world.
- **p. 4 / IV. EXPERIMENTAL SETUP - extractive PDF cue:** Training Settings For training, we consider the following settings: 1) Ours: As is presented in Sec.
- **p. 5 / V. RESULTS AND ANALYSES - extractive PDF cue:** Ours outperforms others in the metrics. commands directing away from the pit until the robot regains stability.
- **p. 5 / V. RESULTS AND ANALYSES - extractive PDF cue:** When the robot missteps into an invisible pit, the policy generates velocity Obstacles 100% Obstacles 50% Obstacles 0% Pits 100% Pits 50% Pits 0% 60 ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1. An illustration of what happens under perception failures, exem- plified by an invisible obstacle case. (A) Without perception failures, both classical planners and ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 2. An illustration of the privileged map and the corrupted map. The map (visualized by colored dots) provides the terrain traversability around the robot. ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 2. Besides reaching the target in time, the robot should also reduce base collisions and avoid falls. An overview of our system is in ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 3. An overview of our learning system. Left The actor-critic design of the navigation policy. Right: Our high-level navigation policy generates velocity commands tracked ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 4. We employ a terrain curriculum to facilitate learning. The terrains from top to bottom are obstacles on hilly, obstacles on boxes, pits on ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 5. Test terrains in simulation. The red boxes are the targets. 100 robots are tested together.
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 6. Emergent behaviors of obstacle avoidance after a collision in simulation. The policy can react to the collision and make a sidestep. A A ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 7. Emergent behaviors of recovery from an invisible pit in simulation. The policy can react to the missed step and drag the robot out ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Environments We verify our methodology on the quadruped ANYmal robot both in simulation and in the real world. | embodiment, simulator version and control stack | p. 4 (IV. EXPERIMENTAL SETUP), p. 4 (IV. EXPERIMENTAL SETUP) |
| Task/environment | Training Settings For training, we consider the following settings: 1) Ours: As is presented in Sec. | reset, timeout, object/scene variation | p. 4 (IV. EXPERIMENTAL SETUP), p. 5 (V. RESULTS AND ANALYSES) |
| Observation/sensor | proprioception, terrain/perception observation과 velocity command | calibration, preprocessing, privileged input | p. 3 (III. METHOD), p. 2 (I. INTRODUCTION) |
| Output/decision | joint target, torque, footstep 또는 locomotion action | action frame, controller and termination | p. 2 (III. METHOD), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| According to the results, all of the policies perform well when the visibility is 100 %, and the Planner achieves a perfect 100 % ... | definition/direction/unit from same section | p. 5 (V. RESULTS AND ANALYSES) |
| Ours can have > 80% success rates even when the perception is fully corrupted, and generalize well to 0 % and 100 % visibility ... | definition/direction/unit from same section | p. 5 (V. RESULTS AND ANALYSES) |
| Fig. 4. We employ a terrain curriculum to facilitate learning. The terrains from top to bottom are obstacles on hilly, obstacles on boxes, pits ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Fig. 2. Besides reaching the target in time, the robot should also reduce base collisions and avoid falls. An overview of our system is ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Each setting is run 3 times with different random seeds for statistics, which supports the significance of our performance by P Values. | definition/direction/unit from same section | p. 4 (IV. EXPERIMENTAL SETUP) |
| Fig. 3. An overview of our learning system. Left The actor-critic design of the navigation policy. Right: Our high-level navigation policy generates velocity commands ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Fig. 9. (A) Our proposed policy can reach the target when the robot is blind. It can react to collisions on the thighs, the ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Fig. 2. An illustration of the privileged map and the corrupted map. The map (visualized by colored dots) provides the terrain traversability around the ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Comparison Results We compare the proposed Ours with the baselines Oracle and Planner in simulation. | comparison identity and matched condition | p. 5 (V. RESULTS AND ANALYSES) |
| 2) Oracle: This setting is the same as Ours except that 100 % of the obstacles and pits are visible during training. | comparison identity and matched condition | p. 4 (IV. EXPERIMENTAL SETUP) |
| Besides these trained policies, we also use a heuristic-based local planner in [3], a representative for classicial local planners, as a baseline (abbreviated as ... | comparison identity and matched condition | p. 4 (IV. EXPERIMENTAL SETUP) |
| Ours outperforms others in the metrics. commands directing away from the pit until the robot regains stability. | comparison identity and matched condition | p. 5 (V. RESULTS AND ANALYSES) |
| Time Cost (s) Oracle Ours P Value Planner Oracle Ours P Value Planner Oracle Ours P Value Planner Obstacles-100 % 93.3±1.5 93.7±5.5 0.538 100 ... | comparison identity and matched condition | p. 6 (V. RESULTS AND ANALYSES) |
| Fig. 1. An illustration of what happens under perception failures, exem- plified by an invisible obstacle case. (A) Without perception failures, both classical planners ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 1. An illustration of what happens under perception failures, exem- plified by an invisible obstacle case. (A) Without perception failures, both classical planners ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Ablation Studies We evaluate different settings for ablation studies in simulation. | component/input/data sensitivity | p. 5 (V. RESULTS AND ANALYSES) |
| Fig. 8. Results of ablation studies. Ours outperforms others in the metrics. commands directing away from the pit until the robot regains stability. | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| 5) No LSTM Memory (NoMem): This setting differs from Ours in that we replace the LSTM layer in the actor network with an MLP ... | component/input/data sensitivity | p. 4 (IV. EXPERIMENTAL SETUP) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, we propose to incorporate locomotion-level observations into navigation, contrasting existing methods that typically decouple navigation from locomotion. | According to the results, all of the policies perform well when the visibility is 100 %, and the Planner achieves a perfect 100 % ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (V. RESULTS AND ANALYSES), p. 5 (V. RESULTS AND ANALYSES), p. 4 (IV. EXPERIMENTAL SETUP) |
| Primary metric/result | However, as the visibility decreases, i.e., when perception failures increase, Ours drop performance much slower than the other two, and significantly outperform them. | numeric claim only at cited anchor | p. 5 (V. RESULTS AND ANALYSES) |

- Numeric sentences retained from the body:
- **p. 6 / V. RESULTS AND ANALYSES - extractive PDF cue:** Time Cost (s) Oracle Ours P Value Planner Oracle Ours P Value Planner Oracle Ours P Value Planner Obstacles-100 % 93.3±1.5 93.7±5.5 0.538 100 1.4±2.1 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Despite our policy's generalization to different collision geometries, we find it cannot handle out-of-distribution mapping noises. | p. 6 (VI. LIMITATIONS AND FUTURE WORKS) |
| body limitation/failure cue | These results indicate that the navigation policy cannot learn to react to perception failures without being exposed to them, and the locomotion policy cannot ... | p. 5 (V. RESULTS AND ANALYSES) |
| body limitation/failure cue | Fig. 2. Besides reaching the target in time, the robot should also reduce base collisions and avoid falls. An overview of our system is ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Hence, it is of great interest if we can train a policy to actively explore these areas and explicitly revise the map allowing it ... | p. 6 (VI. LIMITATIONS AND FUTURE WORKS) |
| body limitation/failure cue | We draw the following conclusions based on the ablation results: 1) The proprioception as part of the observations is generally beneficial to the robustness ... | p. 5 (V. RESULTS AND ANALYSES) |
| body limitation/failure cue | Fig. 1. An illustration of what happens under perception failures, exem- plified by an invisible obstacle case. (A) Without perception failures, both classical planners ... | p. 1 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Each setting is run 3 times with different random seeds for statistics, which supports the significance of our performance by P Values. | p. 4 (IV. EXPERIMENTAL SETUP) |
| Actor Critic Low-Level Exteroception Proprioception Previous Action Position Command Heading Command Corrupted Map Navigation Action Latent Features Feature Mixing LSTM Memory Values Observations with ... | p. 3 (III. METHOD) |
| When the robot missteps into an invisible pit, the policy generates velocity Obstacles 100% Obstacles 50% Obstacles 0% Pits 100% Pits 50% Pits 0% ... | p. 5 (V. RESULTS AND ANALYSES) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / VI. LIMITATIONS AND FUTURE WORKS - extractive PDF cue:** Despite our policy's generalization to different collision geometries, we find it cannot handle out-of-distribution mapping noises.
- **p. 5 / V. RESULTS AND ANALYSES - extractive PDF cue:** These results indicate that the navigation policy cannot learn to react to perception failures without being exposed to them, and the locomotion policy cannot overcome ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 2. Besides reaching the target in time, the robot should also reduce base collisions and avoid falls. An overview of our system is in ...
- **p. 6 / VI. LIMITATIONS AND FUTURE WORKS - extractive PDF cue:** Hence, it is of great interest if we can train a policy to actively explore these areas and explicitly revise the map allowing it to ...
- **p. 5 / V. RESULTS AND ANALYSES - extractive PDF cue:** We draw the following conclusions based on the ablation results: 1) The proprioception as part of the observations is generally beneficial to the robustness against ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1. An illustration of what happens under perception failures, exem- plified by an invisible obstacle case. (A) Without perception failures, both classical planners and ...

- **PDF anchors reviewed:** datasets p. 4 (IV. EXPERIMENTAL SETUP), p. 4 (IV. EXPERIMENTAL SETUP), p. 5 (V. RESULTS AND ANALYSES), p. 5 (V. RESULTS AND ANALYSES), metrics p. 5 (V. RESULTS AND ANALYSES), p. 5 (V. RESULTS AND ANALYSES), p. 4 (Figure/Table caption), p. 2 (Figure/Table caption), p. 4 (IV. EXPERIMENTAL SETUP), p. 3 (Figure/Table caption), baselines p. 5 (V. RESULTS AND ANALYSES), p. 4 (IV. EXPERIMENTAL SETUP), p. 4 (IV. EXPERIMENTAL SETUP), p. 5 (V. RESULTS AND ANALYSES), p. 6 (V. RESULTS AND ANALYSES), p. 1 (Figure/Table caption), results p. 5 (V. RESULTS AND ANALYSES), p. 5 (V. RESULTS AND ANALYSES), p. 4 (IV. EXPERIMENTAL SETUP).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
