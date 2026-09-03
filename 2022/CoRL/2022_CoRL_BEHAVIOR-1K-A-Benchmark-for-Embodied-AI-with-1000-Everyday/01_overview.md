# BEHAVIOR-1K: A Benchmark for Embodied AI with 1,000 Everyday Activities and Realistic Simulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (43 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v205/li23s.html.
> PDF retrieval source: https://arxiv.org/pdf/2403.09227. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Robotics, Benchmark, Embodied AI, long-horizon tasks, simulation, household robotics
- Official paper: https://proceedings.mlr.press/v205/li23s.html
- Full-text retrieval: https://arxiv.org/pdf/2403.09227
- Code/Project: https://behavior.stanford.edu/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (43 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Concretely, the difficulties derive in part from the length of BEHAVIOR-1K's activities and the complexity of the physical manipulation required.를 문제로 두고, In this work, we present BEHAVIOR-1K, a Benchmark of 1,000 Everyday Household Activities in Virtual, Interactive, and Ecological Environments-the next generation of BEHAVIOR-100 [27].를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present BEHAVIOR-1K, a comprehensive simulation benchmark for human-centered robotics.
- **p. 1 / Abstract - extractive body cue:** BEHAVIOR-1K includes two components, guided and motivated by the results of an extensive survey on ‘what do you want robots to do for you?'.
- **p. 1 / Abstract - extractive body cue:** The first is the definition of 1,000 everyday activities, grounded in 50 scenes (houses, gardens, restaurants, offices, etc.) with more than 9,000 objects annotated with ...
- **p. 1 / Abstract - extractive body cue:** The second is OMNIGIBSON, a novel simulation environment that supports these activities via realistic physics simulation and rendering of rigid bodies, deformable bodies, and liquids.
- **p. 1 / Abstract - extractive body cue:** Our experiments indicate that the activities in BEHAVIOR-1K are long-horizon and dependent on complex manipulation skills, both of which remain a challenge for even state-of-the-art ...
- **p. 2 / 1 Introduction - extractive body cue:** Concretely, the difficulties derive in part from the length of BEHAVIOR-1K's activities and the complexity of the physical manipulation required.
- **p. 2 / 1 Introduction - extractive body cue:** To calibrate the simulation-to-real gap of BEHAVIOR-1K, we provide an initial study on transferring solutions learned with a mobile manipulator in a simulated apartment to ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** In this work, we present BEHAVIOR-1K, a Benchmark of 1,000 Everyday Household Activities in Virtual, Interactive, and Ecological Environments-the next generation of BEHAVIOR-100 [27].
- **p. 8 / Method - extractive body cue:** We also evaluate to what extent the simplifications we introduce in physics and actuation (grasping, motion execution) during training impact the performance of RL-Prim. during ...
- **p. 2 / 1 Introduction - extractive body cue:** We hope that the BEHAVIOR-1K benchmark, our survey, and our analysis will serve to support and guide the development of future embodied AI agents and ...
- **p. 7 / Method - extractive body cue:** We evaluate three different baselines based on state-of-the-art reinforcement learning algorithms (RL) [60]: • RL-VMC, a visuomotor control (from image to low-level joint commands) RL ...
- **p. 7 / Method - extractive body cue:** The policy outputs a discrete selection of a primitive applied on an object; • RL-Prim.Hist., a variant of RL-Prim. that takes in the history observations ...
- **p. 8 / Method - extractive body cue:** 6.1), policy failures (i.e., selecting the wrong action primitive) dominate.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The policy outputs a discrete selection of a primitive applied on an object; • RL-Prim.Hist., a variant of RL-Prim. that takes in the history observations (3 steps) as additional inputs to help ... | standardized observation, action, task state와 evaluation split | p. 7 (Method), p. 7 (Method) |
| State/latent | policy, outputs, discrete, selection, primitive, applied, object, RL-Prim, Hist, variant, takes, history | benchmark state/goal와 method decision | p. 7 (Method), p. 7 (Method), p. 8 (Method) |
| Output/action | We evaluate three different baselines based on state-of-the-art reinforcement learning algorithms (RL) [60]: • RL-VMC, a visuomotor control (from image to low-level joint commands) RL solution based on Soft Actor-Critic (SAC) [48]; ... | policy/controller trajectory 또는 measured result | p. 7 (Method), p. 8 (Method), p. 2 (1 Introduction) |
| Objective/outcome | All agents are trained with a sparse task success reward without any reward engineering. | success metric, robustness, generalization과 reproducibility | p. 7 (Method), p. 7 (Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** In this work, we present BEHAVIOR-1K, a Benchmark of 1,000 Everyday Household Activities in Virtual, Interactive, and Ecological Environments-the next generation of BEHAVIOR-100 [27].
- **p. 8 / Method - extractive body cue:** We also evaluate to what extent the simplifications we introduce in physics and actuation (grasping, motion execution) during training impact the performance of RL-Prim. during ...
- **p. 2 / 1 Introduction - extractive body cue:** We hope that the BEHAVIOR-1K benchmark, our survey, and our analysis will serve to support and guide the development of future embodied AI agents and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Task success rates across three baseline methods. RL-VMC with end-to-end visuomotor control completely fails to solve any of the activities, whereas RL-Prim. and ...
- **p. 8 / Method - extractive body cue:** We achieve different success rates in simulation (50 runs, ∼40% success) and in the real world with optimal (27 runs, ∼22%) and trained policies (26 ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Efficiency metrics across three base- line methods. RL-VMC has low spatial and temporal efficiency because it fails to learn, whereas history information helps ...
- **p. 7 / Method - extractive body cue:** Following the metrics proposed in BEHAVIOR-100 [27], we report the success rate and efficiency metrics (distance traveled, time invested, and disarrangement caused) in Table 2 ...
- **p. 4 / C C - extractive body cue:** The realism achieved in rendering by OMNIGIBSON for BEHAVIOR-1K is also significantly higher than what was possible in BEHAVIOR-100 and other benchmarks (see Fig.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 8 (Method) |
| Embodiment/environment | The survey reveals systematicity in what activities people want robots to do, but more importantly, highlights two key factors that we should prioritize when designing robotic benchmarks: diversity in the type of ... | hardware/simulator version and reset protocol | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Dataset/benchmark | We present BEHAVIOR-1K, a comprehensive simulation benchmark for human-centered robotics. | role, split, size and leakage | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 3 (6. Clean a shower) |
| Metric | Following the metrics proposed in BEHAVIOR-100 [27], we report the success rate and efficiency metrics (distance traveled, time invested, and disarrangement caused) in Table 2 and 3, and the success score Q ... | definition, denominator, direction and uncertainty | p. 7 (Method), p. 7 (Figure/Table caption), p. 8 (Method) |
| Baseline/ablation | We evaluate three different baselines based on state-of-the-art reinforcement learning algorithms (RL) [60]: • RL-VMC, a visuomotor control (from image to low-level joint commands) RL solution based on Soft Actor-Critic (SAC) [48]; ... | fair input/data/compute/action matching | p. 7 (Method), p. 1 (Abstract), p. 2 (1 Introduction) |

## Explicit Limitations and Failure Boundary

- **p. 8 / Method - extractive body cue:** The failure cases are depicted in Fig.
- **p. 8 / Method - extractive body cue:** 6.1), policy failures (i.e., selecting the wrong action primitive) dominate.
- **p. 7 / Method - extractive body cue:** RL-VMC with end-to-end visuomotor control completely fails to solve any of the activities, whereas RL-Prim. and RL-Prim.Hist. with action primitives are able achieve decent performance.
- **p. 7 / Method - extractive body cue:** Furthermore, to accelerate training, the action primitives check only the feasibility (e.g., reachability, collisions) of the final configuration, e.g. the grasping pose for pick or ...

## Why Read It

RL, IL, offline learning, and robot data의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Concretely, the difficulties derive in part from the length of BEHAVIOR-1K's activities and the complexity of the physical manipulation required.를 문제로 두고, In this work, we present BEHAVIOR-1K, a Benchmark of 1,000 Everyday Household Activities in Virtual, Interactive, and Ecological Environments-the next generation of BEHAVIOR-100 [27].를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 7 (Method), p. 7 (Method), p. 8 (Method), p. 8 (Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
