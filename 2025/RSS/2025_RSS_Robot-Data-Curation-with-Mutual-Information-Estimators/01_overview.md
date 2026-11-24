# Robot Data Curation with Mutual Information Estimators

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p023.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p023.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: Joey Hejna, Suvir Mirchandani, Ashwin Balakrishna, Annie Xie, Ayzaan Wahid, Jonathan Tompson, Pannag R. Sanketi, Dhruv Shah, Coline Manon Devin, Dorsa Sadigh
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Robotics, Imitation Learning, data curation, demonstrations
- Official paper: https://www.roboticsproceedings.org/rss21/p023.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p023.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; tesseract OCR fallback; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

이 연구는 시연 뒤에 모방 정책이 배울 행동의 다양성과 예측 가능성을 함께 고려해 개별 로봇 시연의 상대 품질을 추정한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p023.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The performance of imitation learning policies often hhinges on the datasets with which they are trained.
- **p. 1 / Abstract - extractive body cue:** Consequently, investment in data collection for robotics has grown across both industrial and academic labs.
- **p. 1 / Abstract - extractive body cue:** However, despite the marked increase in the quantity of demonstrations collected, Title work has sought to assess the quality of said data despite mounting evidence ...
- **p. 1 / Abstract - extractive body cue:** In this work, we take a critical step towards addressing the data quality in roboties.
- **p. 1 / Abstract - extractive body cue:** Given a dataset f demonstrations, we aim to estimate the relative quality of individual demonstrations in terms of both action diversity and predictability.
- **p. 1 / 1. Iyrropucrion - extractive body cue:** In robotics, we often do not have access to data at a similar scale due to the difficulty and cost of collection Moreover. even if ...
- **p. 3 / B. Demonstration Curation - extractive body cue:** This is a more difficult problem than considered in prior work.

## Core Idea

- **p. 4 / V. MetHop - extractive body cue:** come this challenge we propose Demonstration Information Estimation, which uses k-nearest-neighbor (k-NN) estimates of mutual information, Our method involves three steps - representation learning, mutual ...
- **p. 4 / V. MetHop - extractive body cue:** In this section we propose the Demonstration Information Estimation (DemInf) method for computationally estimating mutual information for demonstration data, Though mutual information is usually considered ...
- **p. 1 / Abstract - extractive body cue:** Moreover, training polices based on data filtered bby our method leads to a §-10% improvement in RoboMimic and better performance on real ALOHA and Franka ...
- **p. 2 / 1. Iyrropucrion - extractive body cue:** To address this problem, we introduce Demonstration Information Estimation ‘or Deming for short.
- **p. 2 / 1. Iyrropucrion - extractive body cue:** For text data, this often consists of simple n-gram classifiers, or metadata filtering, which have been shown to have a large impact oon performance [72].
- **p. 18 / C. Implementation Derails - extractive body cue:** For action encoders and decoders, we use the same architecture as for state.
- **p. 18 / C. Implementation Derails - extractive body cue:** For all methods using a state encoder, we use this architecture.
- **p. 4 / B. Maximizing Marginal Action Entropy - extractive body cue:** Having a high marginal action entropy avoids this pitfall, forcing the learned policy to pay attention to the state when making predictions, which is desirable ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In contrast, we believe metrics for imitation learning should be able to measure the relative predictability of the state-action distribution directly, which affects how well a policy is able to fit the ... | observation history와 expert trajectory/action | p. 1 (1. Iyrropucrion), p. 2 (A. Imitation Learning) |
| State/latent | contrast, believe, metrics, imitation, learning, should, able, measure, relative, predictability, state-action, distribution | behavior policy와 temporal action context | p. 1 (1. Iyrropucrion), p. 2 (A. Imitation Learning), p. 3 (B. Demonstration Curation) |
| Output/action | Broadly, the objective of imitation learning is to learn a policy x» : S > A parameterized by 6 that is able to effectively reproduce the behavior of an expert x within ... | predicted action 또는 action chunk | p. 2 (A. Imitation Learning), p. 3 (B. Demonstration Curation), p. 4 (B. Maximizing Marginal Action Entropy) |
| Objective/outcome | [6], we can bound the di tribution matching objective from Eq. | imitation error, task success, robustness와 compounding error | p. 3 (A. Minimizing Conditional Action Entropy), p. 3 (A. Minimizing Conditional Action Entropy), p. 4 (B. Maximizing Marginal Action Entropy) |

## Main Claims and Actual Contribution

- 상태·행동의 잠재 표현에서 최근접 이웃을 이용해 각 궤적이 상호정보량에 기여하는 정도를 계산한다. [PDF 3쪽](https://www.roboticsproceedings.org/rss21/p023.pdf#page=3) · [PDF 4쪽](https://www.roboticsproceedings.org/rss21/p023.pdf#page=4)
- 예측한 순위를 사람의 품질 평가와 비교하고 선별한 시연으로 학습했을 때의 정책 성능을 측정한다. [PDF 7쪽](https://www.roboticsproceedings.org/rss21/p023.pdf#page=7) · [PDF 8쪽](https://www.roboticsproceedings.org/rss21/p023.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup) |
| Embodiment/environment | The multi-human datasets from the RoboMimic benchmark [50] include 100 demonstrations from each of three robot operators for three tasks in increasing difficulty: "Lift" where the robot simply lifts a cube, "Can" ... | hardware/simulator version and reset protocol | p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup) |
| Dataset/benchmark | 4 Average qulity of demonstrations remaining in datasets after filtering with diferent choices of $ onthe Lift Can, and stasis fom the Robomimichenchak wih ts (Lal) a iss (ah. | role, split, size and leakage | p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup), p. 7 (A. Experimental Setup), p. 7 (A. Experimental Setup) |
| Metric | Following Gandhi et al, [25], we use a measure of demonstration "compatibility" to score data. | definition, denominator, direction and uncertainty | p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup), p. 7 (A. Experimental Setup) |
| Baseline/ablation | 2) Baselines: We compare against a number of different data quality estimators from prior work in addition to a number of alternative mutual information estimators, which we label with "(MI)". | fair input/data/compute/action matching | p. 6 (A. Experimental Setup), p. 7 (A. Experimental Setup), p. 6 (A. Experimental Setup) |

## Explicit Limitations and Failure Boundary

- **p. 8 / C. Mutual Information Estimators - extractive body cue:** variance across seeds, while the parametric estimators were more unstable and had one or two runs that performed far worse than the others.
- **p. 6 / A. Experimental Setup - extractive body cue:** Note that while this metric makes sense for active learning, it does not necessarily make sense in the offline setting, and in some ways may ...
- **p. 8 / C. Mutual Information Estimators - extractive body cue:** This is particularly problematic for downstream data curation, as one often does not have ground truth labels to check the quality of the scoring function,
- **p. 9 / C. Mutual Information Estimators - extractive body cue:** DemInf's performance is generally robust to this parameter, with no substantial change in performance in both HersheyKiss and Square MH.
- **p. 16 / Figure/Table caption - extractive body cue:** Fig. 17. The effect of difereat values of VAE on RoboMimic Image. We find that performance is relatively robust to this parameter for RoboMimic.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Iyrropucrion), p. 3 (B. Demonstration Curation), p. 4 (V. MetHop), p. 4 (I N\), p. 18 (C. Implementation Derails)이다.
