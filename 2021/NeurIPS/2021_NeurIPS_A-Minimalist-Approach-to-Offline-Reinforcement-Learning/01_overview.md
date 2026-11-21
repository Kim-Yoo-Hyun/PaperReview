# A Minimalist Approach to Offline Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2106.06860.
> PDF retrieval source: https://arxiv.org/pdf/2106.06860. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / NeurIPS
- Authors: Scott Fujimoto, Shixiang (Shane) Gu
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, offline reinforcement learning, behavior cloning, continuous control
- Official paper: https://arxiv.org/abs/2106.06860
- Full-text retrieval: https://arxiv.org/pdf/2106.06860
- Code/Project: https://github.com/sfujim/TD3_BC
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

TD3+BC는 고정된 데이터에서 TD3를 학습할 때 정책 갱신에 행동 복제 항을 더하는 오프라인 강화학습 기준선이다. [PDF 1쪽](https://arxiv.org/pdf/2106.06860#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Offline reinforcement learning (RL) defines the task of learning from a fixed batch of data.
- **p. 1 / Abstract - extractive body cue:** Due to errors in value estimation from out-of-distribution actions, most offline RL algorithms take the approach of constraining or regularizing the policy with the actions ...
- **p. 1 / Abstract - extractive body cue:** Built on pre-existing RL algorithms, modifications to make an RL algorithm work offline comes at the cost of additional complexity.
- **p. 1 / Abstract - extractive body cue:** Offline RL algorithms introduce new hyperparameters and often leverage secondary components such as generative models, while adjusting the underlying RL algorithm.
- **p. 1 / Abstract - extractive body cue:** In this paper we aim to make a deep RL algorithm work while making minimal changes.
- **p. 3 / 3 Background - extractive body cue:** One challenge for offline RL is the problem of extrapolation error [Fujimoto et al., 2019b], which is generalization error in the approximate value function, induced ...
- **p. 4 / 3 Background - extractive body cue:** However, in the offline setting, where we cannot interact with the environment, making additional adjustments to the underlying algorithm should be considered as more costly ...

## Core Idea

- **p. 1 / 1 Introduction - extractive body cue:** Consequently, offline RL enables the use of previously logged data or leveraging an expert, such as a human operator, without any of the risk associated ...
- **p. 2 / 1 Introduction - extractive body cue:** The surprising effectiveness of our minimalist approach suggests that in the context of offline RL, simpler approaches have been left underexplored in favor of more ...
- **p. 3 / 3 Background - extractive body cue:** We believe these challenges highlight the importance of minimalist approaches, where performance can be easily attributed to algorithmic contributions, rather than entangled with the specifics ...
- **p. 4 / 3 Background - extractive body cue:** If additional changes are necessary, then it suggests the algorithmic contributions alone are insufficient.
- **p. 6 / 3 Background - extractive body cue:** As discussed in Section 4 a minimalist approach has a variety of benefits, such as reducing the number of hyperparameters to tune, increasing scalability by ...
- **p. 4 / 3 Background - extractive body cue:** Most offline RL algorithms are built explicitly on top of an existing off-policy deep RL algorithm, such as TD3 [Fujimoto et al., 2018] or SAC ...
- **p. 4 / 3 Background - extractive body cue:** CQL Fisher-BRC TD3+BC [Kumar et al., 2020] [Kostrikov et al., 2021] (Ours) Algorithmic Adjustments Add regularizer to critic† Train a generative model†‡ Add a BC ...
- **p. 1 / Abstract - extractive body cue:** Due to errors in value estimation from out-of-distribution actions, most offline RL algorithms take the approach of constraining or regularizing the policy with the actions ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | While most off-policy RL algorithms are applicable in the offline setting, they tend to under-perform due to "extrapolation error": an error in policy evaluation, where agents tend to poorly estimate the value ... | dataset state/observation, action, reward와 return-to-go | p. 1 (1 Introduction), p. 3 (3 Background) |
| State/latent | While, most, off-policy, algorithms, applicable, offline, setting, they, tend, under-perform, extrapolation, error | Q/value 또는 sequence-policy state | p. 1 (1 Introduction), p. 3 (3 Background), p. 1 (1 Introduction) |
| Output/action | The behavior of an RL agent is determined by a policy π which maps states to actions (deterministic policy), or states to a probability distribution over actions (stochastic policy). | dataset-supported action sequence | p. 3 (3 Background), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Objective/outcome | The objective of an RL agent is to maximize the expected discounted return Eπ[P∞ t=0 γtrt+1], which is the expected cumulative sum of rewards when following the policy in the MDP, where ... | offline policy value, OOD safety와 closed-loop success | p. 3 (3 Background), p. 4 (3 Background), p. 6 (3 Background) |

## Main Claims and Actual Contribution

- 데이터 상태를 정규화하고 동작이 시연에서 지나치게 멀어지지 않도록 가치 최대화와 행동 모방을 결합한다. [PDF 2쪽](https://arxiv.org/pdf/2106.06860#page=2) · [PDF 3쪽](https://arxiv.org/pdf/2106.06860#page=3)
- 오프라인 연속 제어 데이터에서 더 복잡한 알고리즘과 정책 성능 및 학습 시간을 비교했다. [PDF 4쪽](https://arxiv.org/pdf/2106.06860#page=4) · [PDF 7쪽](https://arxiv.org/pdf/2106.06860#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Embodiment/environment | We evaluate our proposed approach on the D4RL benchmark of OpenAI gym MuJoCo tasks [Todorov et al., 2012, Brockman et al., 2016, Fu et al., 2020], which encompasses a variety of dataset ... | hardware/simulator version and reset protocol | p. 7 (6 Experiments), p. 7 (6 Experiments) |
| Dataset/benchmark | We evaluate our proposed approach on the D4RL benchmark of OpenAI gym MuJoCo tasks [Todorov et al., 2012, Brockman et al., 2016, Fu et al., 2020], which encompasses a variety of dataset ... | role, split, size and leakage | p. 7 (6 Experiments), p. 7 (6 Experiments) |
| Metric | Table 2: Average normalized score over the final 10 evaluations and 5 seeds. The highest performing scores are highlighted. CQL and Fisher-BRC are re-run using author-provided implementations to ensure an identical evaluation ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 17 (Figure/Table caption), p. 18 (Figure/Table caption) |
| Baseline/ablation | Our offline RL baselines include two state-of-the-art algorithms, CQL [Kumar et al., 2020] and Fisher-BRC [Kostrikov et al., 2021], as well as BRAC [Wu et al., 2019] and AWAC [Nair et al., ... | fair input/data/compute/action matching | p. 7 (6 Experiments), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 7 Conclusion - extractive body cue:** Finally, we believe the sheer simplicity of our approach highlights a possible overemphasis on algorithmic complexity made by the community, and we hope to inspire ...
- **p. 9 / 7 Conclusion - extractive body cue:** Additionally, we highlight existing open challenges in offline RL research, including not only the extra implementation, computation, and hyperparameter-tuning complexities that we successfully address in ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Run time comparison of training each offline RL algorithm (does not include evaluation costs). (Left) Breakdown of the cost of the added implementation ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 8: Benchmarking wall-clock training time of DT and TD3+BC over 1 million steps. Does not include evaluation costs. We remark that the DT was ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 3 (3 Background), p. 4 (3 Background), p. 5 (3 Background), p. 6 (3 Background)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (19 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** One challenge for offline RL is the problem of extrapolation error [Fujimoto et al., 2019b], which is generalization error in the approximate value function, induced by selecting actions not contained ... (p. 3, 3 Background).
- **Actual contribution:** Consequently, offline RL enables the use of previously logged data or leveraging an expert, such as a human operator, without any of the risk associated with an untrained RL agent. (p. 1, 1 Introduction).
- **Evaluation boundary:** Table 9: Average normalized score using the D4RL -v2 datasets. The highest performing scores are highlighted. ± captures the standard deviation over seeds. Total (DT) sums scores over the subset ... (p. 18, Figure/Table caption).
- **Explicit failure boundary:** We use the hyperparameters defined in the CQL paper rather than the default settings in the CQL GitHub as we found those settings performed poorly. † denotes hyperparameters which deviate ... (p. 15, B Experimental Details).
