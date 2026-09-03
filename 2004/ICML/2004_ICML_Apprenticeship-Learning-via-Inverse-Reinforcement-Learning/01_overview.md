# Apprenticeship Learning via Inverse Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://ai.stanford.edu/~pabbeel/irl/.
> PDF retrieval source: https://ai.stanford.edu/~ang/papers/icml04-apprentice.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2004 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Robotics, Imitation Learning, inverse reinforcement learning, apprenticeship learning
- Official paper: https://ai.stanford.edu/~pabbeel/irl/
- Full-text retrieval: https://ai.stanford.edu/~ang/papers/icml04-apprentice.pdf
- Code/Project: https://ai.stanford.edu/~pabbeel/irl/
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 From conversations with engineers in industry and our own experience in applying reinforcement learning algorithms to several robots, we believe that, for many problems, the difficulty of manually specifying a reward function ...를 문제로 두고, In this paper, we assume that the expert is trying (without necessarily succeeding) to optimize an unknown reward function that can be expressed as a linear combination of known "features." Even though ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We consider learning in a Markov decision process where we are not explicitly given a reward function, but where instead we can observe an expert ...
- **p. 1 / Abstract - extractive body cue:** This setting is useful in applications (such as the task of driving) where it may be difficult to write down an explicit reward function specifying ...
- **p. 1 / Abstract - extractive body cue:** We think of the expert as trying to maximize a reward function that is expressible as a linear combination of known features, and give an ...
- **p. 1 / Abstract - extractive body cue:** Our algorithm is based on using "inverse reinforcement learning" to try to recover the unknown reward function.
- **p. 1 / Abstract - extractive body cue:** We show that our algorithm terminates in a small number of iterations, and that even though we may never recover the expert's reward function, the ...
- **p. 1 / 1. Introduction - extractive body cue:** From conversations with engineers in industry and our own experience in applying reinforcement learning algorithms to several robots, we believe that, for many problems, the ...
- **p. 1 / 1. Introduction - extractive body cue:** However, we believe that even the reward function is frequently difficult to specify manually.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we assume that the expert is trying (without necessarily succeeding) to optimize an unknown reward function that can be expressed as a ...
- **p. 3 / 3. Algorithm - extractive body cue:** (The SVM problem is a quadratic programming problem (QP), so we can also use any generic QP solver.) In Figure 1 we show an example ...
- **p. 3 / 3. Algorithm - extractive body cue:** (Whether the algorithm terminates is discussed in Section 4.) Then directly from Eq.
- **p. 4 / 3.1. A simpler algorithm - extractive body cue:** Briefly, the projection method replaces step 2 of the algorithm with the following: - Set ¯µ(i-1) = ¯µ(i-2)+ (µ(i-1)-¯µ(i-2))T (µE-¯µ(i-2)) (µ(i-1)-¯µ(i-2))T (µ(i-1)-¯µ(i-2))(µ(i-1)-¯µ(i-2)) (This computes the ...
- **p. 4 / 3. Algorithm - extractive body cue:** The performance guarantees of our algorithm only depend on (approximately) matching the feature expectations, not on recovering the true underlying reward function.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | A policy π is a mapping from states to probability distributions over actions. | observation history와 expert trajectory/action | p. 2 (2. Preliminaries), p. 2 (2. Preliminaries) |
| State/latent | policy, mapping, states, probability, distributions, over, actions, value, Es0, Here, expectation, taken | behavior policy와 temporal action context | p. 2 (2. Preliminaries), p. 2 (2. Preliminaries), p. 1 (1. Introduction) |
| Output/action | The value of a policy π is Es0∼D[V π(s0)] = E[P∞ t=0 γtR(st)/π] (1) = E[P∞ t=0 γtw · φ(st)/π] (2) = w · E[P∞ t=0 γtφ(st)/π] (3) Here, the expectation is ... | predicted action 또는 action chunk | p. 2 (2. Preliminaries), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Objective/outcome | Three iterations for max-margin algorithm. the reward function being optimized by the expert. | imitation error, task success, robustness와 compounding error | p. 3 (3. Algorithm), p. 3 (3. Algorithm), p. 4 (3. Algorithm) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we assume that the expert is trying (without necessarily succeeding) to optimize an unknown reward function that can be expressed as a ...
- **p. 3 / 3. Algorithm - extractive body cue:** (The SVM problem is a quadratic programming problem (QP), so we can also use any generic QP solver.) In Figure 1 we show an example ...
- **p. 6 / 5.1. Gridworld - extractive body cue:** Screenshot of driving simulator. learning a compact representation of the reward function, our algorithm significantly outperforms the other methods.
- **p. 4 / 4. Theoretical results - extractive body cue:** Most of the results in the previous section were predicated on the assumption that the algorithm terminates with t ≤ϵ.
- **p. 4 / 4. Theoretical results - extractive body cue:** In the case where the true reward function R∗does not lie exactly in the span of the basis functions φ, the algorithm still enjoys a ...
- **p. 5 / 5.1. Gridworld - extractive body cue:** Plot of performance vs. number of sampled trajectories from the expert.
- **p. 5 / 5.1. Gridworld - extractive body cue:** The performance measure is the value of the best policy in the set output by the algorithm.
- **p. 6 / 5.2. Car driving simulation - extractive body cue:** Since no "true" reward was ever specified or used in the experiments, we cannot report on the results of the algorithm according to R∗.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 6 (5.1. Gridworld), p. 4 (4. Theoretical results) |
| Embodiment/environment | The simulation runs at 10Hz, and in the experiments that follow, the expert's features were estimated from a single trajectory of 1200 samples (corresponding to 2 minutes of driving time). | hardware/simulator version and reset protocol | p. 6 (5.2. Car driving simulation), p. 6 (5.2. Car driving simulation) |
| Dataset/benchmark | In particular, we do not rely on the expert's demonstrations to learn the state transition probabilities. | role, split, size and leakage | p. 6 (5.2. Car driving simulation), p. 6 (5.2. Car driving simulation), p. 5 (5.1. Gridworld), p. 5 (5.1. Gridworld) |
| Metric | In the case where the true reward function R∗does not lie exactly in the span of the basis functions φ, the algorithm still enjoys a graceful degradation of performance. | definition, denominator, direction and uncertainty | p. 4 (4. Theoretical results), p. 5 (4. Theoretical results), p. 5 (5.1. Gridworld) |
| Baseline/ablation | Screenshot of driving simulator. learning a compact representation of the reward function, our algorithm significantly outperforms the other methods. | fair input/data/compute/action matching | p. 6 (5.1. Gridworld), p. 5 (5.1. Gridworld) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 5.1. Gridworld - extractive body cue:** The agent has four actions to try to move in each of the four compass directions, but with 30% chance an action fails and results ...
- **p. 6 / 5.2. Car driving simulation - extractive body cue:** Nice: The highest priority is to avoid collisions than the "mimic the expert" algorithm initially.
- **p. 6 / 5.2. Car driving simulation - extractive body cue:** Since no "true" reward was ever specified or used in the experiments, we cannot report on the results of the algorithm according to R∗.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Feature expectations of teacher ˆµE and of selected/learned policy µ(˜π) (as estimated by Monte Carlo). and weights w corresponding to the reward function ...
- **p. 4 / 4. Theoretical results - extractive body cue:** In the case where the true reward function R∗does not lie exactly in the span of the basis functions φ, the algorithm still enjoys a ...
- **p. 4 / 4. Theoretical results - extractive body cue:** If the algorithm sometimes does not terminate, or if it sometimes takes a very (perhaps exponentially) large number of iterations to terminate, then it would ...

## Why Read It

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 From conversations with engineers in industry and our own experience in applying reinforcement learning algorithms to several robots, we believe that, for many problems, the difficulty of manually specifying a reward function ...를 문제로 두고, In this paper, we assume that the expert is trying (without necessarily succeeding) to optimize an unknown reward function that can be expressed as a linear combination of known "features." Even though ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (2. Preliminaries), p. 3 (3. Algorithm) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
