# Q-Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://doi.org/10.1007/BF00992698.
> PDF retrieval source: https://doi.org/10.1007/BF00992698. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 1992 / Machine Learning
- Authors: Christopher J. C. H. Watkins, Peter Dayan
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Reinforcement Learning, Q-learning, Value Learning
- Official paper: https://doi.org/10.1007/BF00992698
- Full-text retrieval: https://www.gatsby.ucl.ac.uk/~dayan/papers/cjch.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://www.gatsby.ucl.ac.uk/~dayan/papers/cjch.pdf) 기준이다.

## Why This Paper Is Here

Watkins와 Dayan은 이산 상태·행동의 Q-learning이 주어진 표집과 학습률 조건에서 최적 행동가치로 수렴함을 증명했다. [PDF 1쪽](https://www.gatsby.ucl.ac.uk/~dayan/papers/cjch.pdf#page=1)

## Problem and Motivation

- **p. 1 / 1. Introduction - extractive body cue:** O~-learning (Watkins, 1989) is a form of model-free reinforcement learning.
- **p. 1 / 1. Introduction - extractive body cue:** It can also be viewed as a method of asynchronous dynamic programming (DP).
- **p. 1 / 1. Introduction - extractive body cue:** It provides agents with the capability of learning to act optimally in Markovian domains by experiencing the consequences of actions, without requiring them to build ...
- **p. 1 / 1. Introduction - extractive body cue:** Learning proceeds similarly to Sutton's (1984; 1988) method of temporal differences (TD): an agent tries an action at a particular state, and evaluates its consequences ...
- **p. 1 / 1. Introduction - extractive body cue:** By trying all actions in all states repeatedly, it learns which are best overall, judged by long-term discounted reward.
- **p. 1 / 1. Introduction - extractive body cue:** Section 2 describes the problem, the method, and the notation, section 3 gives an overview of the proof, and section 4 discusses two extensions.

## Core Idea

- **p. 3 / 2. The task for ~-learning - extractive body cue:** In O~-learning, the agent's experience consists of a sequence of distinct stages or episodes.
- **p. 4 / 3. The convergence proof - extractive body cue:** A state of the AFI~, (x, n), consists of a card number (or level) n, together with a state x from the real process.
- **p. 4 / 3. The convergence proof - extractive body cue:** Replaying the episode on card t consists of emitting the reward, rt, written on the card, and then moving to the next state (Yt, t ...
- **p. 1 / 1. Introduction - extractive body cue:** Examples of its use include Barto and Singh (1990), Sutton (1990), Chapman and Kaelbling (1991), Mahadevan and Connell (1991), and Lin (1992), who developed it ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** We show that 0~-learning converges to the optimum action-values with probability 1 so long as all actions are repeatedly sampled in all states and the ...
- **p. 7 / 3.2. The theorem - extractive body cue:** Then, for n > h, by B.4, compare the value _~ARp(IX, n), a t ..... as) of taking actions at, ..., as at state x ...
- **p. 2 / 2. The task for ~-learning - extractive body cue:** Under a policy 7r, the value of state x is W(x) = ~A~(x)) + ~ ~]/%[~(x)]V~(y Y because the agent expects to receive 6~x(Tr(x)) immediately ...
- **p. 3 / 2. The task for ~-learning - extractive body cue:** It is straightforward to show that V*(x) = max a O~*(x, a) and that if a* is an action at which the maximum is attained, ...

## Observation, State, and Output Interface

유한한 마르코프 의사결정 과정에서 보상과 다음 상태의 최대 Q값으로 상태·행동 표를 갱신한다. 모든 상태·행동 쌍의 반복 표집 등 가정 아래 최적 Q값으로의 수렴을 증명한다. [PDF 1쪽](https://www.gatsby.ucl.ac.uk/~dayan/papers/cjch.pdf#page=1) · [PDF 3쪽](https://www.gatsby.ucl.ac.uk/~dayan/papers/cjch.pdf#page=3)

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Y In other words, the ~ value is the expected discounted reward for executing action a at state x and following policy 7r thereafter. | 관측 상태·행동·즉시 보상·다음 상태 | p. 2 (2. The task for ~-learning), p. 2 (2. The task for ~-learning) |
| State/latent | other, words, value, expected, discounted, reward, executing, action, state, following, policy, thereafter | 상태·행동별 Q 추정치 | p. 2 (2. The task for ~-learning), p. 2 (2. The task for ~-learning), p. 3 (2. The task for ~-learning) |
| Output/action | Under a policy 7r, the value of state x is W(x) = ~A~(x)) + ~ ~]/%[~(x)]V~(y Y because the agent expects to receive 6~x(Tr(x)) immediately for performing the action 7r recommends, and ... | 갱신된 Q값과 유도되는 탐욕 정책 | p. 2 (2. The task for ~-learning), p. 3 (2. The task for ~-learning), p. 1 (Body text (section boundary not confidently recovered)) |
| Objective/outcome | The task facing the agent is that of determining an optimal policy, one that maximizes total discounted expected reward. | 반복 표집 등 가정에서의 최적 Q값 수렴 | p. 2 (2. The task for ~-learning), p. 3 (2. The task for ~-learning), p. 7 (3.2. The theorem) |

## Main Claims and Actual Contribution

- 관측한 보상과 다음 상태에서 가장 좋은 행동의 추정가치로 방문한 상태·행동의 값을 갱신한다. [PDF 2쪽](https://www.gatsby.ucl.ac.uk/~dayan/papers/cjch.pdf#page=2) · [PDF 3쪽](https://www.gatsby.ucl.ac.uk/~dayan/papers/cjch.pdf#page=3)
- 과거 행동을 재생하는 보조 마르코프 과정을 구성해 반복 표집 조건에서 확률 1 수렴을 보인다. [PDF 3쪽](https://www.gatsby.ucl.ac.uk/~dayan/papers/cjch.pdf#page=3) · [PDF 4쪽](https://www.gatsby.ucl.ac.uk/~dayan/papers/cjch.pdf#page=4) · [PDF 5쪽](https://www.gatsby.ucl.ac.uk/~dayan/papers/cjch.pdf#page=5) · [PDF 7쪽](https://www.gatsby.ucl.ac.uk/~dayan/papers/cjch.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 4 (3. The convergence proof), p. 5 (3.1. Lemmas) |
| Embodiment/environment | First, all the cards for episodes later than n are eliminated, leaving just a finite deck. | hardware/simulator version and reset protocol | p. 4 (3. The convergence proof), p. 5 (3.1. Lemmas) |
| Dataset/benchmark | The AFIP effectively estimates the mean rewards and transitions of the real process over all the episodes. | role, split, size and leakage | p. 4 (3. The convergence proof), p. 5 (3.1. Lemmas), p. 6 (3.1. Lemmas), p. 4 (3. The convergence proof) |
| Metric | DAYAN Theorem Given bounded rewards I rn [ -< (R, learning rates 0 < c~ n < 1, and ~ Otni(x,a ) : 0o, ~11 [~ni(x,a)] 2 < 0o, ~tX, a, i=1 ... | definition, denominator, direction and uncertainty | p. 4 (2. The task for ~-learning), p. 4 (3. The convergence proof), p. 5 (3.1. Lemmas) |
| Baseline/ablation | Assume, without loss of generality, that O~0(x, a) < 61/(1 - 3') and that 61 __. | fair input/data/compute/action matching | p. 6 (3.2. The theorem), p. 5 (3. The convergence proof), p. 7 (3.2. The theorem) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4. Discussions and conclusions - extractive body cue:** Unfortunately, the theorem does not extend trivially to this case, and alternative proof methods such as those in Kushner and Clark (1978) may be required.
- **p. 8 / 4. Discussions and conclusions - extractive body cue:** The theorem above only proves the convergence of a restricted version of Watkins' (1989) comprehensive Q-learning algorithm, since it does not permit updates based on ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 7 (3.2. The theorem), p. 2 (2. The task for ~-learning), p. 4 (3. The convergence proof), p. 3 (2. The task for ~-learning)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Section 2 describes the problem, the method, and the notation, section 3 gives an overview of the proof, and section 4 discusses two extensions. (p. 1, 1. Introduction).
- **Actual contribution:** O~-learning (Watkins, 1989) is a form of model-free reinforcement learning. (p. 1, 1. Introduction).
- **Evaluation boundary:** Imagine each episode (xt, at, Yt, rt, °~t) written on a card. (p. 4, 3. The convergence proof).
- **Explicit failure boundary:** Unfortunately, the theorem does not extend trivially to this case, and alternative proof methods such as those in Kushner and Clark (1978) may be required. (p. 8, 4. Discussions and conclusions).
