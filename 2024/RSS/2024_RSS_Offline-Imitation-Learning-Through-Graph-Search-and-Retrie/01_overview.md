# Offline Imitation Learning Through Graph Search and Retrieval

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss20/p054.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss20/p054.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Robotics, Imitation Learning, offline learning, graph search, retrieval
- Official paper: https://www.roboticsproceedings.org/rss20/p054.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss20/p054.pdf
- Code/Project: https://www.roboticsproceedings.org/rss20/p054.html
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 offline_rl 문제를 이해하기 위해 읽는다. 본문은 Moreover, there usually exist suboptimal behaviors within a successful demonstration, such as retrying to grip the item if the first attempt fails.를 문제로 두고, As a direct approach that uses graph search rather than deep RL, our method enjoys high time efficiency.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Imitation learning is a powerful machine learning algorithm for a robot to acquire manipulation skills.
- **p. 1 / Abstract - extractive body cue:** Nevertheless, many real-world manipulation tasks involve precise and dexterous robot-object interactions, which make it difficult for humans to collect high-quality expert demonstrations.
- **p. 1 / Abstract - extractive body cue:** As a result, a robot has to learn skills from suboptimal demonstrations and unstructured interactions, which remains a key challenge.
- **p. 1 / Abstract - extractive body cue:** Existing works typically use offline deep reinforcement learning (RL) to solve this challenge, but in practice these algorithms are unstable and fragile due to the ...
- **p. 1 / Abstract - extractive body cue:** To overcome this problem, we propose GSR, a simple yet effective algorithm that learns from suboptimal demonstrations through Graph Search and Retrieval.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Moreover, there usually exist suboptimal behaviors within a successful demonstration, such as retrying to grip the item if the first attempt fails.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Despite numerous challenges in both perception and action, our method can consistently improve baselines' success rate by 10% to 30% and proficiency by over 30%.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** As a direct approach that uses graph search rather than deep RL, our method enjoys high time efficiency.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We also provide various quantitative and qualitative analyses to show that our method is capable of identifying good behaviors in the dataset.
- **p. 3 / IV. POLICY LEARNING - extractive body cue:** We introduce the implementation details in the remaining sections.
- **p. 4 / IV. POLICY LEARNING - extractive body cue:** To address the first problem, we propose to identify and connect similar states in the dataset to form a better distance estimate in section IV-B.
- **p. 5 / IV. POLICY LEARNING - extractive body cue:** The pseudo-code of our method is summarized in Algorithm 1.
- **p. 4 / IV. POLICY LEARNING - extractive body cue:** To identify similar states, we use the off-shelf pretrained vision models to compute features for similarity computation.
- **p. 4 / IV. POLICY LEARNING - extractive body cue:** Algorithm 1: GSR 1 [Optional] Finetune pretrained fθ on D; 2 Build graph G(V, E) using procedure in Section IV-B; 3 Set w[v] = 0 ...
- **p. 5 / IV. POLICY LEARNING - extractive body cue:** Implementation and Time Complexity We use R3M [33] as pretrained feature since it is pretrained with a contrastive objective, which we find can represent fine-grained ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | If we define w(o, a) = exp(A(o, a)) where A is the advantage of taking action a at observation o, this corresponds to the policy extraction objective used in Advantage-Weighted Regression (AWR) ... | dataset state/observation, action, reward와 return-to-go | p. 3 (III. PRELIMINARIES), p. 3 (III. PRELIMINARIES) |
| State/latent | define, where, advantage, taking, action, observation, corresponds, policy, extraction, objective, Advantage-Weighted, Regression | Q/value 또는 sequence-policy state | p. 3 (III. PRELIMINARIES), p. 3 (III. PRELIMINARIES), p. 2 (I. INTRODUCTION) |
| Output/action | Each trajectory τ is a sequence of observations o0:T and corresponding actions a0:T , i.e., τ = (o0, a0, o1, a1, ..., oT , aT ). | dataset-supported action sequence | p. 3 (III. PRELIMINARIES), p. 2 (I. INTRODUCTION), p. 4 (IV. POLICY LEARNING) |
| Objective/outcome | Algorithm 1: GSR 1 [Optional] Finetune pretrained fθ on D; 2 Build graph G(V, E) using procedure in Section IV-B; 3 Set w[v] = 0 for each v ∈V; 4 Compute feature ... | offline policy value, OOD safety와 closed-loop success | p. 4 (IV. POLICY LEARNING), p. 3 (IV. POLICY LEARNING), p. 3 (IV. POLICY LEARNING) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** As a direct approach that uses graph search rather than deep RL, our method enjoys high time efficiency.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We also provide various quantitative and qualitative analyses to show that our method is capable of identifying good behaviors in the dataset.
- **p. 3 / IV. POLICY LEARNING - extractive body cue:** We introduce the implementation details in the remaining sections.
- **p. 4 / IV. POLICY LEARNING - extractive body cue:** To address the first problem, we propose to identify and connect similar states in the dataset to form a better distance estimate in section IV-B.
- **p. 5 / IV. POLICY LEARNING - extractive body cue:** The pseudo-code of our method is summarized in Algorithm 1.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** We find that our method can achieve a success rate greater than 80% in the considered task and outperform all baselines in execution time.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** A good method is expected to achieve a high success rate with low execution time. • Normalized Proficiency (NP) is a metric we use for ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** The second finding is that our algorithm can also improve the success rate of state-of-the-art algorithms.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Embodiment/environment | Bottom: Our real-world tasks. and Worse-Better20 (the whole worse-human dataset with 20% data of the better-human dataset). • Nut Assembly In this task, the robot is required to pick up a square ... | hardware/simulator version and reset protocol | p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Dataset/benchmark | Specifically, we use three tasks that contain human demonstrations of diverse qualities (Worse, Okay, Better): • Can Pick-and-Place In this task, the robot is required to pick up a can on the ... | role, split, size and leakage | p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Metric | 3) Evaluation Metric: To evaluate the performance of a trained policy, we use the following metrics. • Success rate (SR) is defined as the number of task successes divided by the number ... | definition, denominator, direction and uncertainty | p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |
| Baseline/ablation | We first study how much performance gain our method can achieve compared to the state-of-the-art imitation learning baseline. | fair input/data/compute/action matching | p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 8 / V. EXPERIMENTS - extractive body cue:** However, in many cases, they will get stuck or go out of distribution, leading to a complete failure.
- **p. 8 / V. EXPERIMENTS - extractive body cue:** Interestingly, we have the following findings: (1) All the temporal segments that lead to the failures are weakened and have low weights.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** The robot is required to push a blue cylinder toward a green cube on the table. • Spoon Scooping In this task, the robot is ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** This task highlights the challenge of robust perception against partial occlusion and fine-grained manipulation. • Tweezer Manipulation In this task, the robot needs to first ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Then, through both quantitative and qualitative analysis, we show that our method identify and chain useful behaviors in the dataset to learn a robust policy.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** We observe that the baselines appear to repeat the failed human attempts during demo collection more frequently compared to our method.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** In some cases, they may eventually recover from failed behavior modes (by repeating subsequent retrying behavior demonstrated by a human) and complete the task.

## Why Read It

RL, IL, offline learning, and robot data의 offline_rl 문제를 이해하기 위해 읽는다. 본문은 Moreover, there usually exist suboptimal behaviors within a successful demonstration, such as retrying to grip the item if the first attempt fails.를 문제로 두고, As a direct approach that uses graph search rather than deep RL, our method enjoys high time efficiency.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. PRELIMINARIES), p. 4 (IV. POLICY LEARNING), p. 4 (IV. POLICY LEARNING) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
