# FurnitureBench: Reproducible Real-World Benchmark for Long-Horizon Complex Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2305.12821.
> PDF retrieval source: https://arxiv.org/pdf/2305.12821. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, Benchmark, assembly, long-horizon manipulation, real-world evaluation, reproducibility
- Official paper: https://arxiv.org/abs/2305.12821
- Full-text retrieval: https://arxiv.org/pdf/2305.12821
- Code/Project: https://clvrai.github.io/furniture-bench/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Furniture assembly is a proper task suite to benchmark a difficult, long-horizon manipulation task through which many challenges in robotic manipulation must be addressed to solve.를 문제로 두고, The main contributions of this paper are as follows: • We introduce FurnitureBench, a real-world furniture assembly benchmark, which allows robotics researchers to investigate RL, IL, and TAMP algorithms on a realistic ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Reinforcement learning (RL), imitation learning (IL), and task and motion planning (TAMP) have demonstrated impressive performance across various robotic manipulation tasks.
- **p. 1 / Abstract - extractive body cue:** However, these approaches have been limited to learning simple behaviors in current real-world manipulation benchmarks, such as pushing or pick-and-place.
- **p. 1 / Abstract - extractive body cue:** To enable more complex, long-horizon behaviors of an autonomous robot, we propose to focus on real-world furniture assembly, a complex, longhorizon robot manipulation task that ...
- **p. 1 / Abstract - extractive body cue:** We present FurnitureBench, a reproducible real-world furniture assembly benchmark aimed at providing a low barrier for entry and being easily reproducible, so that researchers across ...
- **p. 1 / Abstract - extractive body cue:** For ease of use, we provide 200+ hours of precollected data (5000+ demonstrations), 3D printable furniture models, a robotic environment setup guide, and systematic task ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Furniture assembly is a proper task suite to benchmark a difficult, long-horizon manipulation task through which many challenges in robotic manipulation must be addressed to ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Due to the limitations imposed by using a single robotic arm, we modify some furniture pieces feasible to be assembled with one hand. strations that ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** The main contributions of this paper are as follows: • We introduce FurnitureBench, a real-world furniture assembly benchmark, which allows robotics researchers to investigate RL, ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To this end, we propose to focus on furniture assembly as the next milestone for complex, long-horizon robotic manipulation, and present FurnitureBench, a reproducible real-world ...
- **p. 1 / Abstract - extractive body cue:** To enable more complex, long-horizon behaviors of an autonomous robot, we propose to focus on real-world furniture assembly, a complex, longhorizon robot manipulation task that ...
- **p. 1 / Abstract - extractive body cue:** We present FurnitureBench, a reproducible real-world furniture assembly benchmark aimed at providing a low barrier for entry and being easily reproducible, so that researchers across ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Due to the limitations imposed by using a single robotic arm, we modify some furniture pieces feasible to be assembled with one hand. strations that ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** (Right) A suite of 8 furniture models in our benchmark.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** (Left) A decorated room in the real world with furniture models our robot assembled.
- **p. 7 / 2) The furniture parts are rearranged using our provided - extractive body cue:** 3) A policy controls the robot until it completes the task, stops motions for 5 sec, shows unsafe movements, exceeds 350 steps per skill, or ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our reproducible robot system (a) and visual observations from the front-view camera (b) and wrist camera (c). of long-horizon complex robotic manipulation tasks. | standardized observation, action, task state와 evaluation split | p. 2 (I. INTRODUCTION), p. 7 (2) The furniture parts are rearranged using our provided) |
| State/latent | reproducible, robot, system, visual, observations, front-view, camera, wrist, long-horizon, complex, robotic, manipulation | benchmark state/goal와 method decision | p. 2 (I. INTRODUCTION), p. 7 (2) The furniture parts are rearranged using our provided), p. 1 (Body text (section boundary not confidently recovered)) |
| Output/action | 3) A policy controls the robot until it completes the task, stops motions for 5 sec, shows unsafe movements, exceeds 350 steps per skill, or exceeds 3000 steps in total. | policy/controller trajectory 또는 measured result | p. 7 (2) The furniture parts are rearranged using our provided), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Abstract) |
| Objective/outcome | success metric, robustness, generalization과 reproducibility | success metric, robustness, generalization과 reproducibility | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** The main contributions of this paper are as follows: • We introduce FurnitureBench, a real-world furniture assembly benchmark, which allows robotics researchers to investigate RL, ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To this end, we propose to focus on furniture assembly as the next milestone for complex, long-horizon robotic manipulation, and present FurnitureBench, a reproducible real-world ...
- **p. 1 / Abstract - extractive body cue:** To enable more complex, long-horizon behaviors of an autonomous robot, we propose to focus on real-world furniture assembly, a complex, longhorizon robot manipulation task that ...
- **p. 1 / Abstract - extractive body cue:** We present FurnitureBench, a reproducible real-world furniture assembly benchmark aimed at providing a low barrier for entry and being easily reproducible, so that researchers across ...
- **p. 7 / VI. BENCHMARKING RESULTS - extractive body cue:** The "pushing" skill in drawer achieves 30% success rate, which is slightly worse than that of the "grasping" skill (60%), with BC.
- **p. 7 / VI. BENCHMARKING RESULTS - extractive body cue:** However, in lamp and round_table, where the round-shaped parts need to be screwed, IQL struggles and achieves only 10% and 0% success rates, respectively.
- **p. 8 / VI. BENCHMARKING RESULTS - extractive body cue:** Figures 8 and 10 show that IQL-R3M achieves 4 phases on average and 40% success rate on the low randomness level.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 8: Correlation between FurnitureBench and Furni- tureSim. We compare the performance of IL and offline RL methods with respect to the dataset size between ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 7 (VI. BENCHMARKING RESULTS), p. 7 (VI. BENCHMARKING RESULTS) |
| Embodiment/environment | But, this benchmark environment and tasks can be also used for research in TAMP. | hardware/simulator version and reset protocol | p. 7 (VI. BENCHMARKING RESULTS), p. 7 (VI. BENCHMARKING RESULTS) |
| Dataset/benchmark | A trained model is evaluated for 10 episodes, where their initial states are set following the provided task initialization guide tool. | role, split, size and leakage | p. 7 (VI. BENCHMARKING RESULTS), p. 7 (VI. BENCHMARKING RESULTS), p. 6 (V. EXPERIMENTAL SETUP), p. 8 (VI. BENCHMARKING RESULTS) |
| Metric | Fig. 10: Full-assembly benchmark results. We report the number of completed phases averaged over 10 episodes and the error bars indicating the minimum and maximum completed phases. The background color indicates each ... | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 7 (VI. BENCHMARKING RESULTS), p. 7 (VI. BENCHMARKING RESULTS) |
| Baseline/ablation | We evaluate our benchmark with imitation learning (BC) and the state-of-the-art offline RL (IQL) methods. | fair input/data/compute/action matching | p. 6 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP), p. 7 (VI. BENCHMARKING RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 18 / Figure/Table caption - extractive body cue:** Fig. 17: Furniture 3D models. IKEA model furniture (left), 3D furniture model (middle), and 3D printed furniture model (right). Each furniture model introduces unique interactions ...
- **p. 7 / VI. BENCHMARKING RESULTS - extractive body cue:** The failure of these algorithms to even attach a pair of furniture parts despite the high-quality demonstration dataset highlights the need for further algorithmic improvements ...
- **p. 7 / VI. BENCHMARKING RESULTS - extractive body cue:** On the other hand, both algorithms struggle at "inserting" skill, which shows from 0% to 20% success rates. "Inserting" requires precise control to correctly align ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 3: 3D printed furniture models. Each furniture is designed inspired by IKEA furniture. Due to the limitations imposed by using a single robotic arm, ...
- **p. 8 / VI. BENCHMARKING RESULTS - extractive body cue:** It always achieves the phase 3 (grasping the leg) but fails at inserting 60% of the time.
- **p. 8 / VI. BENCHMARKING RESULTS - extractive body cue:** This result reassures that "inserting" is the most challenging skill as it involves stochastic and frequent collisions.
- **p. 34 / Figure/Table caption - extractive body cue:** Fig. 36: Affix obstacle. The red circles represent where to attach the double-sided rubber tape. Make sure the obstacle does not move when pushed. Important ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Furniture assembly is a proper task suite to benchmark a difficult, long-horizon manipulation task through which many challenges in robotic manipulation must be addressed to solve.를 문제로 두고, The main contributions of this paper are as follows: • We introduce FurnitureBench, a real-world furniture assembly benchmark, which allows robotics researchers to investigate RL, IL, and TAMP algorithms on a realistic ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (35 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Furniture assembly is a proper task suite to benchmark a difficult, long-horizon manipulation task through which many challenges in robotic manipulation must be addressed to solve. (p. 2, I. INTRODUCTION).
- **Actual contribution:** The main contributions of this paper are as follows: • We introduce FurnitureBench, a real-world furniture assembly benchmark, which allows robotics researchers to investigate RL, IL, and TAMP algorithms on ... (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** Fig. 10: Full-assembly benchmark results. We report the number of completed phases averaged over 10 episodes and the error bars indicating the minimum and maximum completed phases. The background color ... (p. 8, Figure/Table caption).
- **Explicit failure boundary:** On the other hand, both algorithms struggle at "inserting" skill, which shows from 0% to 20% success rates. "Inserting" requires precise control to correctly align a screw and a hole, ... (p. 7, VI. BENCHMARKING RESULTS).
