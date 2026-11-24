# Generative Adversarial Imitation Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1606.03476.
> PDF retrieval source: https://arxiv.org/pdf/1606.03476. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2016 / NeurIPS
- Authors: Jonathan Ho, Stefano Ermon
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Robotics, Imitation Learning, Reinforcement Learning
- Official paper: https://arxiv.org/abs/1606.03476
- Full-text retrieval: https://arxiv.org/pdf/1606.03476
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 6. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../work/sources/pdf_note_review_followup_2026-10-23.json).

## Why This Paper Is Here

GAIL은 전문가 시연과 현재 정책의 상호작용을 판별하는 모형을 이용해 명시적인 보상 없이 모방 정책을 학습한다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2016/file/cc7e2b878868cbae992d1fb743995d8f-Paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Consider learning a policy from example expert behavior, without interaction with the expert or access to reinforcement signal.
- **p. 1 / Abstract - extractive body cue:** One approach is to recover the expert's cost function with inverse reinforcement learning, then extract a policy from that cost function with reinforcement learning.
- **p. 1 / Abstract - extractive body cue:** This approach is indirect and can be slow.
- **p. 1 / Abstract - extractive body cue:** We propose a new general framework for directly extracting a policy from data, as if it were obtained by reinforcement learning following inverse reinforcement learning.
- **p. 1 / Abstract - extractive body cue:** We show that a certain instantiation of our framework draws an analogy between imitation learning and generative adversarial networks, from which we derive a model-free ...
- **p. 1 / 1 Introduction - extractive body cue:** Given that learner's true goal often is to take actions imitating the expert-indeed, many IRL algorithms are evaluated on the quality of the optimal actions ...
- **p. 4 / 2 Background - extractive body cue:** In reality, the expert trajectory distribution will be provided only as a finite set of samples, so in large environments, most of the expert's occupancy ...

## Core Idea

- **p. 1 / Abstract - extractive body cue:** We show that a certain instantiation of our framework draws an analogy between imitation learning and generative adversarial networks, from which we derive a model-free ...
- **p. 1 / 1 Introduction - extractive body cue:** Then, we instantiate our framework in Sections 4 and 5 with a new model-free imitation learning algorithm.
- **p. 3 / 2 Background - extractive body cue:** We explore such algorithms in Sections 4 and 5, where we show that certain settings of ψ lead to both existing algorithms and a novel ...
- **p. 3 / 2 Background - extractive body cue:** The occupancy measure can be interpreted as the distribution of state-action pairs that an agent encounters when navigating the environment with policy π, and it ...
- **p. 4 / 2 Background - extractive body cue:** Keeping in mind that we wish to eventually develop an imitation learning algorithm suitable for large environments, we would like to relax Eq.
- **p. 2 / 1 Introduction - extractive body cue:** networks [9], a technique from the deep learning community that has led to recent successes in modeling distributions of natural images: our algorithm harnesses generative ...
- **p. 4 / 2 Background - extractive body cue:** For a class of cost functions C ⊂RS×A, an apprenticeship learning algorithm finds a policy that performs better than the expert across C, by optimizing ...
- **PDF p. 6, Eq. (13) (DOC-QA2 원문 대조):** ψ_GA(c)는 모든 위치에서 c<0일 때 expert occupancy에 대한 E[g(c(s,a))], 그 외에는 +∞다. g(x)=−x−log(1−exp(x)) for x<0, 그 외 +∞. 유한 cost 영역과 piecewise 조건을 보존한다.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | There are two main approaches suitable for this setting: behavioral cloning [20], which learns a policy as a supervised learning problem over state-action pairs from expert trajectories; and inverse reinforcement learning [25, ... | observation history와 expert trajectory/action | p. 1 (1 Introduction), p. 4 (2 Background) |
| State/latent | There, main, approaches, suitable, setting, behavioral, cloning, learns, policy, supervised, learning, problem | behavior policy와 temporal action context | p. 1 (1 Introduction), p. 4 (2 Background), p. 3 (2 Background) |
| Output/action | In reality, the expert trajectory distribution will be provided only as a finite set of samples, so in large environments, most of the expert's occupancy measure values will be exactly zero, and ... | predicted action 또는 action chunk | p. 4 (2 Background), p. 3 (2 Background), p. 4 (2 Background) |
| Objective/outcome | For a class of cost functions C ⊂RS×A, an apprenticeship learning algorithm finds a policy that performs better than the expert across C, by optimizing the objective minimize π max c∈C Eπ[c(s, ... | imitation error, task success, robustness와 compounding error | p. 4 (2 Background), p. 5 (2 Background), p. 2 (2 Background) |

## Main Claims and Actual Contribution

- 정규화된 역강화학습과 정책 최적화의 결합을 상태·행동 점유 분포 맞추기로 정식화한다. [PDF 3쪽](https://proceedings.neurips.cc/paper_files/paper/2016/file/cc7e2b878868cbae992d1fb743995d8f-Paper.pdf#page=3) · [PDF 4쪽](https://proceedings.neurips.cc/paper_files/paper/2016/file/cc7e2b878868cbae992d1fb743995d8f-Paper.pdf#page=4)
- 판별기 학습과 신뢰 영역 정책 갱신을 번갈아 수행하고 연속 제어 과제에서 시연 수에 따른 성능을 비교한다. [PDF 6쪽](https://proceedings.neurips.cc/paper_files/paper/2016/file/cc7e2b878868cbae992d1fb743995d8f-Paper.pdf#page=6) · [PDF 8쪽](https://proceedings.neurips.cc/paper_files/paper/2016/file/cc7e2b878868cbae992d1fb743995d8f-Paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (6 Experiments), p. 7 (6 Experiments) |
| Embodiment/environment | We found that on the classic control tasks (cartpole, acrobot, and mountain car), behavioral cloning suffered in expert data efficiency compared to FEM and GTAL, which for the most part were able ... | hardware/simulator version and reset protocol | p. 7 (6 Experiments), p. 7 (6 Experiments) |
| Dataset/benchmark | We found that on the classic control tasks (cartpole, acrobot, and mountain car), behavioral cloning suffered in expert data efficiency compared to FEM and GTAL, which for the most part were able ... | role, split, size and leakage | p. 7 (6 Experiments), p. 7 (6 Experiments) |
| Metric | The policy is trained with supervised learning, using Adam [12] with minibatches of 128 examples, until validation error stops decreasing. | definition, denominator, direction and uncertainty | p. 7 (6 Experiments), p. 7 (6 Experiments), p. 13 (Figure/Table caption) |
| Baseline/ablation | We tested Algorithm 1 against three baselines: 1. | fair input/data/compute/action matching | p. 7 (6 Experiments), p. 7 (6 Experiments), p. 8 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 2. Form a gradient estimate with Eq. (12) with c∗ - extractive body cue:** When D cannot distinguish data generated by G from the true data, then G has successfully matched the true data.
- **p. 6 / 2. Form a gradient estimate with Eq. (12) with c∗ - extractive body cue:** The indicator regularizers δC, used by the linear apprenticeship learning algorithms described in Section 4, are always fixed, and cannot adapt to data as ψGA ...
- **p. 5 / 2. Form a gradient estimate with Eq. (12) with c∗ - extractive body cue:** This carefully constructed step scheme ensures that divergence does not occur due to high noise in estimating the gradient (12).
- **p. 5 / 2 Background - extractive body cue:** If C does not include a cost function that explains expert behavior well, then attempting to recover a policy from such an encoding will not ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 Introduction), p. 4 (2 Background), p. 2 (2 Background), p. 3 (2 Background), p. 2 (1 Introduction)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Inverse reinforcement learning (IRL), on the other hand, learns a cost function that prioritizes entire trajectories over others, so compounding error, a problem for methods that fit single-timestep decisions, is ... (p. 1, 1 Introduction).
- **Actual contribution:** Then, we instantiate our framework in Sections 4 and 5 with a new model-free imitation learning algorithm. (p. 1, 1 Introduction).
- **Evaluation boundary:** We found that on the classic control tasks (cartpole, acrobot, and mountain car), behavioral cloning suffered in expert data efficiency compared to FEM and GTAL, which for the most part ... (p. 7, 6 Experiments).
- **Explicit failure boundary:** FEM and GTAL performed poorly for Ant, producing policies consistently worse than a policy that chooses actions uniformly at random. (p. 8, 6 Experiments).
