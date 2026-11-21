# MOPO: Model-based Offline Policy Optimization

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2005.13239.
> PDF retrieval source: https://arxiv.org/pdf/2005.13239. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / NeurIPS
- Authors: Tianhe Yu, Garrett Thomas, Lantao Yu, Stefano Ermon, James Zou, Sergey Levine, Chelsea Finn, Tengyu Ma
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, offline reinforcement learning, model-based RL, distribution shift
- Official paper: https://arxiv.org/abs/2005.13239
- Full-text retrieval: https://arxiv.org/pdf/2005.13239
- Code/Project: https://github.com/tianheyu927/mopo
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

MOPO는 오프라인 데이터로 학습한 동역학에서 정책을 개선할 때 예측이 불확실한 구간의 보상을 낮춘다. [PDF 1쪽](https://arxiv.org/pdf/2005.13239#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Offline reinforcement learning (RL) refers to the problem of learning policies entirely from a large batch of previously collected data.
- **p. 1 / Abstract - extractive body cue:** This problem setting offers the promise of utilizing such datasets to acquire policies without any costly or dangerous active exploration.
- **p. 1 / Abstract - extractive body cue:** However, it is also challenging, due to the distributional shift between the offline training data and those states visited by the learned policy.
- **p. 1 / Abstract - extractive body cue:** Despite significant recent progress, the most successful prior methods are model-free and constrain the policy to the support of data, precluding generalization to unseen states.
- **p. 1 / Abstract - extractive body cue:** In this paper, we first observe that an existing model-based RL algorithm already produces significant gains in the offline setting compared to model-free approaches.
- **p. 2 / 1 Introduction - extractive body cue:** Our results suggest that MOPO substantially outperforms these prior methods on the offline RL benchmark D4RL [18] as well as on offline RL problems where ...
- **p. 1 / 1 Introduction - extractive body cue:** These failures are generally caused by large extrapolation error when the Q-function is evaluated on out-of-distribution actions [19, 36], which can lead to unstable learning ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** The primary contribution of this work is an offline model-based RL algorithm that optimizes a policy in an uncertainty-penalized MDP, where the reward function is ...
- **p. 1 / Abstract - extractive body cue:** Instead, we propose to modify the existing model-based RL methods by applying them with rewards artificially penalized by the uncertainty of the dynamics.
- **p. 5 / 3 Preliminaries - extractive body cue:** We will analyze our framework under the assumption that we have access to an oracle uncertainty quantification module that provides an upper bound on the ...
- **p. 2 / 1 Introduction - extractive body cue:** Although neither method is designed for the batch setting, we find that the model-based method and its variant without ensembles show surprisingly large gains.
- **p. 1 / Abstract - extractive body cue:** However, standard model-based RL methods, designed for the online setting, do not provide an explicit mechanism to avoid the offline setting's distributional shift issue.
- **p. 4 / 3 Preliminaries - extractive body cue:** 4 MOPO: Model-Based Offline Policy Optimization Unlike model-free methods, our goal is to design an offline model-based reinforcement learning algorithm that can take actions that ...
- **p. 4 / 3 Preliminaries - extractive body cue:** Then we maximize the conservative estimation of the return by an off-the-shelf reinforcement learning algorithm, which gives MOPO, a generic model-based off-policy algorithm (Section 4.2).
- **p. 7 / 3 Preliminaries - extractive body cue:** Following MBPO, we model the dynamics using a neural network that outputs a Gaussian distribution over the next state and reward3: bTθ,φ(st+1, r/st, at) = ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 4 MOPO: Model-Based Offline Policy Optimization Unlike model-free methods, our goal is to design an offline model-based reinforcement learning algorithm that can take actions that are not strictly within the support of ... | dataset state/observation, action, reward와 return-to-go | p. 4 (3 Preliminaries), p. 2 (1 Introduction) |
| State/latent | MOPO, Model-Based, Offline, Policy, Optimization, Unlike, model-free, methods, goal, design, reinforcement, learning | Q/value 또는 sequence-policy state | p. 4 (3 Preliminaries), p. 2 (1 Introduction), p. 3 (3 Preliminaries) |
| Output/action | We argue that it is important for an offline RL algorithm to be equipped with the ability to leave the data support to learn a better policy for two reasons: (1) the ... | dataset-supported action sequence | p. 2 (1 Introduction), p. 3 (3 Preliminaries), p. 3 (3 Preliminaries) |
| Objective/outcome | Moreover, equation (2) suggests that a policy that obtains high reward in the estimated MDP while also minimizing Gπ c M will obtain high reward in the real MDP. | offline policy value, OOD safety와 closed-loop success | p. 4 (3 Preliminaries), p. 6 (3 Preliminaries), p. 3 (3 Preliminaries) |

## Main Claims and Actual Contribution

- 모델 오차에서 오는 위험을 보상 벌점으로 표현하고 논문이 정한 오차 가정 아래 실제 정책 수익의 하한과 연결한다. [PDF 4쪽](https://arxiv.org/pdf/2005.13239#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2005.13239#page=5)
- 오프라인 연속 제어에서 모델로 생성한 전이와 벌점을 사용한 정책을 기존 오프라인 학습 방식과 비교했다. [PDF 6쪽](https://arxiv.org/pdf/2005.13239#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2005.13239#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 9 (Figure/Table caption), p. 18 (Figure/Table caption) |
| Embodiment/environment | 5.1 Evaluation on the D4RL benchmark To answer question (1), we evaluate our method on a large subset of datasets in the D4RL benchmark [18] based on the MuJoCo simulator [69], including ... | hardware/simulator version and reset protocol | p. 7 (5 Experiments), p. 8 (5 Experiments) |
| Dataset/benchmark | In particular, model-free offline RL cannot outperform the best trajectory in the batch dataset, whereas MOPO exceeds the batch max by a significant margin. | role, split, size and leakage | p. 7 (5 Experiments), p. 8 (5 Experiments), p. 8 (5 Experiments), p. 7 (5 Experiments) |
| Metric | To extend the theory to an unknown reward function, we can consider the reward as being concatenated onto the state, so that the admissible error estimator bounds the error on (s′, r), ... | definition, denominator, direction and uncertainty | p. 7 (5 Experiments), p. 8 (Figure/Table caption), p. 8 (5 Experiments) |
| Baseline/ablation | We compare against several baselines, including the current state-of-the-art model-free offline RL algorithms. | fair input/data/compute/action matching | p. 7 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 6 Conclusion - extractive body cue:** However, uncertainty estimation does not explain the entire difference nor does it explain why model-free methods cannot also enjoy the benefits of uncertainty estimation.
- **p. 9 / 6 Conclusion - extractive body cue:** Our work opens up a number of questions and directions for future work.
- **p. 8 / 5 Experiments - extractive body cue:** In particular, model-free offline RL cannot outperform the best trajectory in the batch dataset, whereas MOPO exceeds the batch max by a significant margin.
- **p. 7 / 5 Experiments - extractive body cue:** BRACv uses this penalty both when updating the critic and when updating the actor, while BRAC-p uses this penalty only when updating the actor and ...
- **p. 8 / 5 Experiments - extractive body cue:** Numbers for model-free methods taken from [18], which does not report standard deviation.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Comparison between vanilla model-based RL (MBPO [29]) with or without model ensembles and vanilla model-free RL (SAC [27]) on two offline RL tasks: ...
- **p. 7 / 5 Experiments - extractive body cue:** (2) Can MOPO solve tasks that require generalization to out-of-distribution behaviors?

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 1 (1 Introduction), p. 3 (3 Preliminaries), p. 7 (3 Preliminaries), p. 4 (3 Preliminaries)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (19 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** In particular, because offline model-based algorithms cannot improve the dynamics model using additional experience, we expect that such algorithms require careful use of the model in regions outside of the ... (p. 2, 1 Introduction).
- **Actual contribution:** Although neither method is designed for the batch setting, we find that the model-based method and its variant without ensembles show surprisingly large gains. (p. 2, 1 Introduction).
- **Evaluation boundary:** Table 1: Results for D4RL datasets. Each number is the normalized score proposed in [18] of the policy at the last iteration of training, averaged over 6 random seeds, ± ... (p. 8, Figure/Table caption).
- **Explicit failure boundary:** These failures are generally caused by large extrapolation error when the Q-function is evaluated on out-of-distribution actions [19, 36], which can lead to unstable learning and divergence. (p. 1, 1 Introduction).
