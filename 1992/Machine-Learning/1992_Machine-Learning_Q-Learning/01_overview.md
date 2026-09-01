# Q-Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://doi.org/10.1007/BF00992698.
> PDF retrieval source: https://doi.org/10.1007/BF00992698. Reading tracker status/evidence was not changed.

- Year/Venue: 1992 / Machine Learning
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: Robotics, Reinforcement Learning, Q-learning, Value Learning
- Official paper: https://doi.org/10.1007/BF00992698
- Full-text retrieval: https://doi.org/10.1007/BF00992698
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 rl 문제를 이해하기 위해 읽는다. 본문은 Section 2 describes the problem, the method, and the notation, section 3 gives an overview of the proof, and section 4 discusses two extensions.를 문제로 두고, In O~-learning, the agent's experience consists of a sequence of distinct stages or episodes.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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
- **p. 7 / 3.2. The theorem - extractive body cue:** Then, for n > h, by B.4, compare the value _~ARp(IX, n), a t ..... as) of taking actions at, ..., as at state x ...
- **p. 2 / 2. The task for ~-learning - extractive body cue:** Under a policy 7r, the value of state x is W(x) = ~A~(x)) + ~ ~]/%[~(x)]V~(y Y because the agent expects to receive 6~x(Tr(x)) immediately ...
- **p. 3 / 2. The task for ~-learning - extractive body cue:** It is straightforward to show that V*(x) = max a O~*(x, a) and that if a* is an action at which the maximum is attained, ...
- **p. 4 / 3. The convergence proof - extractive body cue:** Cards are then removed one at a time from top of this deck and examined until one is found whose starting state and action match ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Y In other words, the ~ value is the expected discounted reward for executing action a at state x and following policy 7r thereafter. | state 또는 observation, action, reward와 transition history | p. 2 (2. The task for ~-learning), p. 2 (2. The task for ~-learning) |
| State/latent | other, words, value, expected, discounted, reward, executing, action, state, following, policy, thereafter | policy/value state와 action-selection variable | p. 2 (2. The task for ~-learning), p. 2 (2. The task for ~-learning), p. 3 (2. The task for ~-learning) |
| Output/action | Under a policy 7r, the value of state x is W(x) = ~A~(x)) + ~ ~]/%[~(x)]V~(y Y because the agent expects to receive 6~x(Tr(x)) immediately for performing the action 7r recommends, and ... | action policy와 induced trajectory | p. 2 (2. The task for ~-learning), p. 3 (2. The task for ~-learning), p. 1 (1. Introduction) |
| Objective/outcome | The task facing the agent is that of determining an optimal policy, one that maximizes total discounted expected reward. | expected return, task success, stability와 sample efficiency | p. 2 (2. The task for ~-learning), p. 3 (2. The task for ~-learning), p. 7 (3.2. The theorem) |

## Main Claims and Actual Contribution

- **p. 3 / 2. The task for ~-learning - extractive body cue:** In O~-learning, the agent's experience consists of a sequence of distinct stages or episodes.
- **p. 4 / 3. The convergence proof - extractive body cue:** A state of the AFI~, (x, n), consists of a card number (or level) n, together with a state x from the real process.
- **p. 4 / 3. The convergence proof - extractive body cue:** Replaying the episode on card t consists of emitting the reward, rt, written on the card, and then moving to the next state (Yt, t ...
- **p. 1 / 1. Introduction - extractive body cue:** Examples of its use include Barto and Singh (1990), Sutton (1990), Chapman and Kaelbling (1991), Mahadevan and Connell (1991), and Lin (1992), who developed it ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

RL, IL, offline learning, and robot data의 rl 문제를 이해하기 위해 읽는다. 본문은 Section 2 describes the problem, the method, and the notation, section 3 gives an overview of the proof, and section 4 discusses two extensions.를 문제로 두고, In O~-learning, the agent's experience consists of a sequence of distinct stages or episodes.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 7 (3.2. The theorem), p. 2 (2. The task for ~-learning), p. 4 (3. The convergence proof), p. 3 (2. The task for ~-learning), p. 4 (3. The convergence proof) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
