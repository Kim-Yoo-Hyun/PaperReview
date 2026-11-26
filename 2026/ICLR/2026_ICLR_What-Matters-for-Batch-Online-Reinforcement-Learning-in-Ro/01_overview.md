# What Matters for Batch Online Reinforcement Learning in Robotics?

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://iclr.cc/virtual/2026/poster/10006859.
> PDF retrieval source: https://arxiv.org/pdf/2505.08078. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: Perry Dong, Suvir Mirchandani, Dorsa Sadigh, Chelsea Finn
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Robotics, Reinforcement Learning, batch online RL, real robot, value guidance
- Official paper: https://iclr.cc/virtual/2026/poster/10006859
- Full-text retrieval: https://arxiv.org/pdf/2505.08078
- Code/Project: https://pd-perry.github.io/batch-online-rl/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

이 연구는 로봇이 자율적으로 수집한 행동 자료를 배치마다 추가할 때 어떤 학습·행동 선택 방식이 정책 개선에 유리한지 비교한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/b650f2838de7e1e817b5408b48a19a63-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The ability to learn from large batches of autonomously collected data for policy improvement-a paradigm we refer to as batch online reinforcement learning-holds the promise ...
- **p. 1 / Abstract - extractive body cue:** Yet, despite the promise of this paradigm, it remains challenging to achieve due to algorithms not being able to learn effectively from the autonomous data.
- **p. 1 / Abstract - extractive body cue:** For example, prior works have applied imitation learning and filtered imitation learning methods to the batch online RL problem, but these algorithms often fail to ...
- **p. 1 / Abstract - extractive body cue:** This raises the question of what matters for effective batch online reinforcement learning in robotics.
- **p. 1 / Abstract - extractive body cue:** Motivated by this question, we perform a systematic empirical study of three axes-(i) algorithm class, (ii) policy extraction methods, and (iii) policy expressivity-and analyze how ...
- **p. 2 / 1 Introduction - extractive body cue:** Learning from autonomously collected data for policy improvement, however, remains a significant challenge in robot learning as current algorithms struggle to fully leverage this autonomous ...
- **p. 1 / 1 Introduction - extractive body cue:** Although recent works have focused on mitigating this gap by proposing large robotic datasets [1, 2], robot learning continues to operate under a substantially smaller ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** On top of the recipe, we propose a simple practical addition to induce even more diversity and achieve better sample efficiency: applying a small amount ...
- **p. 2 / 1 Introduction - extractive body cue:** Based on these observations, we propose a general recipe for effective batch online RL: train an expressive IL policy as the actor, train a Q-function ...
- **p. 5 / 3 Preliminaries - extractive body cue:** In Figure 3, we present the average normalized returns over iterations of batch online RL for each algorithm class on our six tasks.
- **p. 5 / 3 Preliminaries - extractive body cue:** Based on our results, in Section 5 we present a recipe for batch online RL, and demonstrate the practicality of the recipe on a challenging ...
- **p. 6 / 3 Preliminaries - extractive body cue:** We present the results of data scaling in Figure 5.
- **p. 8 / 3 Preliminaries - extractive body cue:** This is in contrast to batch online RL, where to leverage diversity of the online data, the initial model needs to have captured enough of ...
- **p. 5 / 3 Preliminaries - extractive body cue:** For all of the algorithm classes, we use a diffusion-based policy as the default.
- **p. 7 / 3 Preliminaries - extractive body cue:** For the expressive policy class, we use implicit policy extraction as analyzed in Section 4.2.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Based on these observations, we propose a general recipe for effective batch online RL: train an expressive IL policy as the actor, train a Q-function on the autonomous data, and perform implicit ... | multi-view observation, language/task label과 action trajectory | p. 2 (1 Introduction), p. 6 (3 Preliminaries) |
| State/latent | observations, general, recipe, effective, batch, online, train, expressive, policy, actor, Q-function, autonomous | shared representation, embodiment/task identity와 data distribution | p. 2 (1 Introduction), p. 6 (3 Preliminaries), p. 8 (3 Preliminaries) |
| Output/action | Intuitively, this makes sense because value-based RL methods can use the Q-function to determine which states and actions are desirable even in failure trajectories, thus allowing the policy to learn from a ... | dataset sample 또는 learned policy action | p. 6 (3 Preliminaries), p. 8 (3 Preliminaries), p. 3 (3 Preliminaries) |
| Objective/outcome | As in traditional RL, the objective is to find a policy π that maximizes the expected sum of discounted rewards Eτ∼pπ(τ)[P t γtr(st, at)] where pπ(τ) gives the likelihood of a trajectory ... | coverage, cross-embodiment transfer, data efficiency와 task success | p. 3 (3 Preliminaries), p. 4 (3 Preliminaries), p. 6 (3 Preliminaries) |

## Main Claims and Actual Contribution

- 자율 수집 자료에 대한 모방·가치 기반 학습과 정책 분포에서 높은 가치의 행동을 고르는 방법을 비교한다. [PDF 3쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/b650f2838de7e1e817b5408b48a19a63-Paper-Conference.pdf#page=3) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/b650f2838de7e1e817b5408b48a19a63-Paper-Conference.pdf#page=6)
- 정책 분포의 표현력과 시간적으로 상관된 탐색 잡음이 추가 수집 뒤의 성과에 미치는 영향을 실험한다. [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/b650f2838de7e1e817b5408b48a19a63-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/b650f2838de7e1e817b5408b48a19a63-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/b650f2838de7e1e817b5408b48a19a63-Paper-Conference.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Embodiment/environment | Based on our results, in Section 5 we present a recipe for batch online RL, and demonstrate the practicality of the recipe on a challenging real-world robotic task of hanging tape on ... | hardware/simulator version and reset protocol | p. 5 (3 Preliminaries), p. 8 (3 Preliminaries) |
| Dataset/benchmark | Though they are a less expressive class of policies, Gaussian policy are still worth examining because they are fast for inference, which is especially desirable in real-world tasks. | role, split, size and leakage | p. 5 (3 Preliminaries), p. 8 (3 Preliminaries), p. 7 (3 Preliminaries), p. 7 (3 Preliminaries) |
| Metric | However, directly adding noise may not be applicable in some deployment settings, though we find empirically that adding a small amount of noise only changes the success rate of the policy marginally. | definition, denominator, direction and uncertainty | p. 9 (6 Discussion), p. 15 (Figure/Table caption), p. 5 (Figure/Table caption) |
| Baseline/ablation | Figure 11: Normalized returns of value-based RL compared with IL, filtered-IL, and temporally- correlated noise at different data scales, shown for each task. From Figure 11, we see that value-based RL scales ... | fair input/data/compute/action matching | p. 13 (Figure/Table caption), p. 5 (3 Preliminaries), p. 5 (3 Preliminaries) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 6 Discussion - extractive body cue:** Our work presents a general recipe on batch online RL, though it does have a number of limitations.
- **p. 9 / 6 Discussion - extractive body cue:** 7 Limitations In this work, we empirically analyze the key axes that affect performance in batch online RL, demonstrating that the general recipe of value-based ...
- **p. 5 / 3 Preliminaries - extractive body cue:** Vanilla IL performs the worst on all tasks, which is perhaps not surprising as vanilla IL will fit the failure trajectories of the autonomous rollouts.
- **p. 6 / 3 Preliminaries - extractive body cue:** Intuitively, this makes sense because value-based RL methods can use the Q-function to determine which states and actions are desirable even in failure trajectories, thus ...
- **p. 6 / 3 Preliminaries - extractive body cue:** One takeaway from this section is that for batch online RL, we cannot get away with just doing IL or filtered-IL as many prior works ...
- **p. 7 / 3 Preliminaries - extractive body cue:** The policy extracted from explicit policy extraction cannot adjust to this shift as well as implicit policy extraction, resulting in subpar performance.
- **p. 8 / 3 Preliminaries - extractive body cue:** This suggests that temporally-correlated noise can be a valuable addition, though our recipe does not hinge on it.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 1 (1 Introduction), p. 3 (3 Preliminaries), p. 4 (3 Preliminaries)이다.
