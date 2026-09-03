# Extreme Parkour with Legged Robots

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2309.14341.
> PDF retrieval source: https://arxiv.org/pdf/2309.14341. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, quadruped locomotion, parkour, Reinforcement Learning
- Official paper: https://arxiv.org/abs/2309.14341
- Full-text retrieval: https://arxiv.org/pdf/2309.14341
- Code/Project: https://extreme-parkour.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 However, low cost poses a new challenge for parkour which is not as prominent in prior walking works.를 문제로 두고, To allow the robot to adjust itself as per the obstacle type at deployment, we propose a novel dual distillation method.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Humans can perform parkour by traversing obstacles in a highly dynamic fashion requiring precise eye-muscle coordination and movement.
- **p. 1 / Abstract - extractive body cue:** Getting robots to do the same task requires overcoming similar challenges.
- **p. 1 / Abstract - extractive body cue:** Classically, this is done by independently engineering perception, actuation, and control systems to very low tolerances.
- **p. 1 / Abstract - extractive body cue:** This restricts them to tightly controlled settings such as a predetermined obstacle course in labs.
- **p. 1 / Abstract - extractive body cue:** In contrast, humans are able to learn parkour through practice without significantly changing their underlying biology.
- **p. 3 / 1 Introduction - extractive body cue:** However, low cost poses a new challenge for parkour which is not as prominent in prior walking works.
- **p. 3 / 1 Introduction - extractive body cue:** All these challenges are not feasible with such an approach.

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** To allow the robot to adjust itself as per the obstacle type at deployment, we propose a novel dual distillation method.
- **p. 3 / 1 Introduction - extractive body cue:** Below, we summarize the main contributions: • A novel dual distillation method for distilling both agile motor commands and rapidly fluctuating heading directions from depth ...
- **p. 5 / 3 Method - extractive body cue:** We present a simple, unified reward formulation from which diverse behaviors emerge automatically and are perfectly adapted to the terrain geometry.
- **p. 6 / 3 Method - extractive body cue:** To overcome this issue, we propose to use a mixture of teacher and student (MTS).
- **p. 6 / 3 Method - extractive body cue:** To explore this diversity, we introduce a term to track a desired forward vector using the same inner product design principle, which can be controlled ...
- **p. 6 / 3 Method - extractive body cue:** 3.2 Reinforcement Learning from Scandots (Phase 1) We use the above rewards to learn a policy using model-free RL [33] in simulation.
- **p. 5 / 3 Method - extractive body cue:** We use Regularized Online Adaptation (ROA)[9] to train an estimator to recover environmental information from the history of observations.
- **p. 5 / 3 Method - extractive body cue:** In this paper, we use ROA for adaptation and two-phase training for the vision backbone but introduce key modifications for the challenging task of extreme ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | As a result at deployment, the policy not only outputs agile motor commands but also rapidly adjusts heading directions all from input depth image. | proprioception, terrain/perception observation과 velocity command | p. 3 (1 Introduction), p. 6 (3 Method) |
| State/latent | result, deployment, policy, only, outputs, agile, motor, commands, rapidly, adjusts, heading, directions | body/contact state, foothold 또는 behavior mode | p. 3 (1 Introduction), p. 6 (3 Method), p. 6 (3 Method) |
| Output/action | This policy takes as input, the proprioception x, scandots m, target heading ˆd, walking flag W and commanded speed vcmd. | joint target, torque, footstep 또는 locomotion action | p. 6 (3 Method), p. 6 (3 Method), p. 5 (3 Method) |
| Objective/outcome | While the above reward is sufficient for diverse parkour behavior, for challenging obstacles the robot tends to step close to the edge to minimize energy usage. | velocity/progress, stability, energy와 terrain generalization | p. 5 (3 Method), p. 2 (3 Method), p. 5 (3 Method) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** To allow the robot to adjust itself as per the obstacle type at deployment, we propose a novel dual distillation method.
- **p. 3 / 1 Introduction - extractive body cue:** Below, we summarize the main contributions: • A novel dual distillation method for distilling both agile motor commands and rapidly fluctuating heading directions from depth ...
- **p. 5 / 3 Method - extractive body cue:** We present a simple, unified reward formulation from which diverse behaviors emerge automatically and are perfectly adapted to the terrain geometry.
- **p. 6 / 3 Method - extractive body cue:** To overcome this issue, we propose to use a mixture of teacher and student (MTS).
- **p. 6 / 3 Method - extractive body cue:** To explore this diversity, we introduce a term to track a desired forward vector using the same inner product design principle, which can be controlled ...
- **p. 8 / 4 Results - extractive body cue:** In addition, its feet clearance also helps it to achieve some performance with noisy measurements.
- **p. 8 / 4 Results - extractive body cue:** NoClear achieves slightly higher performance but it places feet close to the obstacle edges which is unstable in the real world.
- **p. 9 / 4 Results - extractive body cue:** We find that ours has much higher success rate in all environments.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4 Results), p. 8 (4 Results) |
| Embodiment/environment | Starred is recent concurrent work [47]. baseline comparison in simulation since it is infeasible to provide human joystick commands and provide real-world comparisons instead. | hardware/simulator version and reset protocol | p. 9 (4 Results), p. 7 (4 Results) |
| Dataset/benchmark | 4.2.1 High jump Our robot is able to jump on a gym box 0.5m high (Fig. | role, split, size and leakage | p. 9 (4 Results), p. 7 (4 Results), p. 7 (4 Results), p. 8 (4 Results) |
| Metric | We find that ours has much higher success rate in all environments. | definition, denominator, direction and uncertainty | p. 9 (4 Results), p. 9 (4 Results), p. 8 (4 Results) |
| Baseline/ablation | We find that our method outperforms the baselines in terms of both metrics. | fair input/data/compute/action matching | p. 8 (4 Results), p. 9 (4 Results), p. 9 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 9 / Figure/Table caption - extractive body cue:** Figure 7: For each terrain, we run 5 trials and record the number of successes. We find that ours has 20-80% higher success rate on ...
- **p. 8 / 4 Results - extractive body cue:** Noisy is able to get some performance but has very large variance since it can rely on collisions with its legs to sense terrain geometry ...
- **p. 9 / 4 Results - extractive body cue:** These sudden adjustments are out-ofdistribution for the policy and it cannot adapt fast enough, causing it to fail.
- **p. 8 / 4 Results - extractive body cue:** NoClear achieves slightly higher performance but it places feet close to the obstacle edges which is unstable in the real world.

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 However, low cost poses a new challenge for parkour which is not as prominent in prior walking works.를 문제로 두고, To allow the robot to adjust itself as per the obstacle type at deployment, we propose a novel dual distillation method.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (1 Introduction), p. 3 (1 Introduction), p. 6 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, low cost poses a new challenge for parkour which is not as prominent in prior walking works. (p. 3, 1 Introduction).
- **Actual contribution:** Below, we summarize the main contributions: • A novel dual distillation method for distilling both agile motor commands and rapidly fluctuating heading directions from depth images. • A simple yet ... (p. 3, 1 Introduction).
- **Evaluation boundary:** Figure 7: For each terrain, we run 5 trials and record the number of successes. We find that ours has 20-80% higher success rate on the most difficult instance of ... (p. 9, Figure/Table caption).
- **Explicit failure boundary:** It sometimes succeeds on hurdles and gaps but fails when the human has to provide sudden direction changes which are out-of-distribution. (p. 9, 4 Results).
