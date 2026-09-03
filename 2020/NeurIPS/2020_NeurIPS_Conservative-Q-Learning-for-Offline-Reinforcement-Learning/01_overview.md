# Conservative Q-Learning for Offline Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html.
> PDF retrieval source: https://arxiv.org/pdf/2006.04779. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, offline reinforcement learning, conservative learning, Q-learning
- Official paper: https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html
- Full-text retrieval: https://arxiv.org/pdf/2006.04779
- Code/Project: https://github.com/aviralkumar2907/CQL
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 offline_rl 문제를 이해하기 위해 읽는다. 본문은 However, applying RL to real-world problems consistently poses practical challenges: in contrast to the kinds of data-driven methods that have been successful in supervised learning [24, 11], RL is classically regarded as ...를 문제로 두고, We propose a novel method for learning such conservative Qfunctions via a simple modification to standard value-based RL algorithms.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Effectively leveraging large, previously collected datasets in reinforcement learning (RL) is a key challenge for large-scale real-world applications.
- **p. 1 / Abstract - extractive body cue:** Offline RL algorithms promise to learn effective policies from previously-collected, static datasets without further interaction.
- **p. 1 / Abstract - extractive body cue:** However, in practice, offline RL presents a major challenge, and standard off-policy RL methods can fail due to overestimation of values induced by the distributional ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose conservative Q-learning (CQL), which aims to address these limitations by learning a conservative Q-function such that the expected value of ...
- **p. 1 / Abstract - extractive body cue:** We theoretically show that CQL produces a lower bound on the value of the current policy and that it can be incorporated into a policy ...
- **p. 1 / 1 Introduction - extractive body cue:** However, applying RL to real-world problems consistently poses practical challenges: in contrast to the kinds of data-driven methods that have been successful in supervised learning ...
- **p. 1 / 1 Introduction - extractive body cue:** This in principle can make it possible to leverage large datasets, but in practice fully offline RL methods pose major technical difficulties, stemming from the ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** We propose a novel method for learning such conservative Qfunctions via a simple modification to standard value-based RL algorithms.
- **p. 2 / 1 Introduction - extractive body cue:** The key idea behind our method is to minimize values under an appropriately chosen distribution over state-action tuples, and then further tighten this bound by ...
- **p. 5 / 2 Preliminaries - extractive body cue:** 3.3 Safe Policy Improvement Guarantees In Section 3.1 we proposed novel objectives for Q-function training such that the expected value of a policy under the ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose conservative Q-learning (CQL), which aims to address these limitations by learning a conservative Q-function such that the expected value of ...
- **p. 4 / 2 Preliminaries - extractive body cue:** Due to space constraints, we present these results in Theorem D.1 and Theorem D.2 in Appendix D.1.
- **p. 6 / 2 Preliminaries - extractive body cue:** (6) The expression of ζ in Theorem 3.6 consists of two terms: the first term captures the decrease in policy performance in M, that occurs ...
- **p. 2 / 2 Preliminaries - extractive body cue:** S, A represent state and action spaces, T(s′/s, a) and r(s, a) represent the dynamics and reward function, and γ ∈(0, 1) represents the discount ...
- **p. 2 / 2 Preliminaries - extractive body cue:** Given a dataset D = {(s, a, rs′)} of tuples from trajectories collected under a behavior policy πβ: ˆQk+1 ←arg min Q Es,a,s′∼D  (r(s, ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | S, A represent state and action spaces, T(s′/s, a) and r(s, a) represent the dynamics and reward function, and γ ∈(0, 1) represents the discount factor. πβ(a/s) represents the behavior policy, D ... | dataset state/observation, action, reward와 return-to-go | p. 2 (2 Preliminaries), p. 2 (2 Preliminaries) |
| State/latent | represent, state, action, spaces, dynamics, reward, function, represents, discount, factor, behavior, policy | Q/value 또는 sequence-policy state | p. 2 (2 Preliminaries), p. 2 (2 Preliminaries), p. 3 (2 Preliminaries) |
| Output/action | However, the policy may suffer from state distribution shift at test time. | dataset-supported action sequence | p. 2 (2 Preliminaries), p. 3 (2 Preliminaries), p. 3 (2 Preliminaries) |
| Objective/outcome | 2: for step t in {1, . . . , N} do 3: Train the Q-function using GQ gradient steps on objective from Equation 4 θt := θt-1 -ηQ∇θCQL(R)(θ) (Use B∗for Q-learning, ... | offline policy value, OOD safety와 closed-loop success | p. 6 (2 Preliminaries), p. 3 (2 Preliminaries), p. 5 (2 Preliminaries) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** We propose a novel method for learning such conservative Qfunctions via a simple modification to standard value-based RL algorithms.
- **p. 2 / 1 Introduction - extractive body cue:** The key idea behind our method is to minimize values under an appropriately chosen distribution over state-action tuples, and then further tighten this bound by ...
- **p. 5 / 2 Preliminaries - extractive body cue:** 3.3 Safe Policy Improvement Guarantees In Section 3.1 we proposed novel objectives for Q-function training such that the expected value of a policy under the ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose conservative Q-learning (CQL), which aims to address these limitations by learning a conservative Q-function such that the expected value of ...
- **p. 4 / 2 Preliminaries - extractive body cue:** Due to space constraints, we present these results in Theorem D.1 and Theorem D.2 in Appendix D.1.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Normalized scores of all methods on AntMaze, Adroit, and kitchen domains from D4RL, averaged across 4 seeds. On the harder mazes, CQL is ...
- **p. 31 / Figure/Table caption - extractive body cue:** Table 6: Average return obtained by CQL(H) and CQL(H) without the dataset average Q-value maximization term. The latter formulation corresponds to Equation 1, which is ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Performance of CQL(H) and prior methods on gym domains from D4RL, on the normalized return metric, averaged over 4 seeds. Note that CQL ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 31 (Figure/Table caption) |
| Embodiment/environment | CQL outperforms prior methods by as much as 2-5x on many benchmark tasks, and is the only method that can outperform simple behavioral cloning on a number of realistic datasets collected from ... | hardware/simulator version and reset protocol | p. 2 (1 Introduction), p. 1 (Abstract) |
| Dataset/benchmark | However, applying RL to real-world problems consistently poses practical challenges: in contrast to the kinds of data-driven methods that have been successful in supervised learning [24, 11], RL is classically regarded as ... | role, split, size and leakage | p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (1 Introduction), p. 3 (2 Preliminaries) |
| Metric | We also empirically demonstrate the robustness of our approach to Q-function estimation error. | definition, denominator, direction and uncertainty | p. 2 (1 Introduction), p. 8 (Figure/Table caption), p. 5 (2 Preliminaries) |
| Baseline/ablation | Table 5: Average return obtained by CQL(H), and CQL(ρ) on three D4RL MuJoCo environments. Observe that on these environments, CQL(H) generally outperforms CQL(ρ). Next, we evaluate the answer to question (2). On ... | fair input/data/compute/action matching | p. 30 (Figure/Table caption), p. 31 (Figure/Table caption), p. 1 (Abstract) |

## Explicit Limitations and Failure Boundary

- **p. 1 / 1 Introduction - extractive body cue:** This has made current results fall short of the full promise of such methods.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose conservative Q-learning (CQL), which aims to address these limitations by learning a conservative Q-function such that the expected value of ...
- **p. 2 / 2 Preliminaries - extractive body cue:** Note that Q-function training in offline RL does not suffer from state distribution shift, as the Bellman backup never queries the Q-function on out-of-distribution states.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 1: Performance of CQL, QR-DQN and REM as a function of training steps (x-axis) in setting (1) when provided with only the first 20% ...
- **p. 2 / 2 Preliminaries - extractive body cue:** Since D typically does not contain all possible transitions (s, a, s′), the policy evaluation step actually uses an empirical Bellman operator that only backs ...
- **p. 3 / 2 Preliminaries - extractive body cue:** Since standard Q-function training does not query the Q-function value at unobserved states, but queries the Q-function at unseen actions, we restrict µ to match ...
- **p. 4 / 2 Preliminaries - extractive body cue:** We also show that Equation 2 does not lower-bound the Q-value estimates pointwise.

## Why Read It

RL, IL, offline learning, and robot data의 offline_rl 문제를 이해하기 위해 읽는다. 본문은 However, applying RL to real-world problems consistently poses practical challenges: in contrast to the kinds of data-driven methods that have been successful in supervised learning [24, 11], RL is classically regarded as ...를 문제로 두고, We propose a novel method for learning such conservative Qfunctions via a simple modification to standard value-based RL algorithms.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 5 (2 Preliminaries), p. 5 (2 Preliminaries), p. 6 (2 Preliminaries), p. 5 (2 Preliminaries) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (31 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, applying RL to real-world problems consistently poses practical challenges: in contrast to the kinds of data-driven methods that have been successful in supervised learning [24, 11], RL is classically ... (p. 1, 1 Introduction).
- **Actual contribution:** We propose a novel method for learning such conservative Qfunctions via a simple modification to standard value-based RL algorithms. (p. 2, 1 Introduction).
- **Evaluation boundary:** Table 6: Average return obtained by CQL(H) and CQL(H) without the dataset average Q-value maximization term. The latter formulation corresponds to Equation 1, which is void of the dataset Q-value ... (p. 31, Figure/Table caption).
- **Explicit failure boundary:** Of course, policy constraints should prevent the policy from choosing OOD actions, however, as we will show that in certain cases, policy constraint methods might also fail to prevent the ... (p. 15, B Discussion of Gap-Expanding Behavior of CQL Backups).
