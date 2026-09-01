# Decision Transformer: Reinforcement Learning via Sequence Modeling

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2106.01345.
> PDF retrieval source: https://arxiv.org/pdf/2106.01345. Reading tracker status/evidence was not changed.

- Year/Venue: 2021 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: Reinforcement Learning, Transformer, policy
- Official paper: https://arxiv.org/abs/2106.01345
- Full-text retrieval: https://arxiv.org/pdf/2106.01345
- Code/Project: https://github.com/kzl/decision-transformer
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-02 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 rl 문제를 이해하기 위해 읽는다. 본문은 To get an intuition for our proposal, consider the task of finding the shortest path on a directed graph, which can be posed as an RL problem.를 문제로 두고, Training dataset consists of random walk trajectories and their per-node returns-to-go (middle).를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce a framework that abstracts Reinforcement Learning (RL) as a sequence modeling problem.
- **p. 1 / Abstract - extractive body cue:** This allows us to draw upon the simplicity and scalability of the Transformer architecture, and associated advances in language modeling such as GPT-x and BERT.
- **p. 1 / Abstract - extractive body cue:** In particular, we present Decision Transformer, an architecture that casts the problem of RL as conditional sequence modeling.
- **p. 1 / Abstract - extractive body cue:** Unlike prior approaches to RL that fit value functions or compute policy gradients, Decision Transformer simply outputs the optimal actions by leveraging a causally masked ...
- **p. 1 / Abstract - extractive body cue:** By conditioning an autoregressive model on the desired return (reward), past states, and actions, our Decision Transformer model can generate future actions that achieve the ...
- **p. 3 / 1 Introduction - extractive body cue:** To get an intuition for our proposal, consider the task of finding the shortest path on a directed graph, which can be posed as an ...
- **p. 3 / 1 Introduction - extractive body cue:** Finally, empirical evidence suggest that a transformer modeling approach can model a wide distribution of behaviors, enabling better generalization and transfer [3].

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** Training dataset consists of random walk trajectories and their per-node returns-to-go (middle).
- **p. 4 / 1 Introduction - extractive body cue:** Motivated by this observation, we propose Decision Transformer, where we use the GPT architecture to autoregressively model trajectories (shown in Figure 1).
- **p. 4 / 3 Method - extractive body cue:** In this section, we present Decision Transformer, which models trajectories autoregressively with minimal modification to the transformer architecture, as summarized in Figure 1 and Algorithm ...
- **p. 5 / 3 Method - extractive body cue:** We did not find predicting the states or returns-to-go to improve performance, although it is easily permissible within our framework (as shown in Section 5.4) ...
- **p. 6 / 3 Method - extractive body cue:** We evaluate our method on 1% of all samples in the DQN-replay dataset as per Agarwal et al.
- **p. 4 / 3 Method - extractive body cue:** The key desiderata in our choice of trajectory representation are that it should enable transformers to learn meaningful patterns and we should be able to ...
- **p. 6 / 3 Method - extractive body cue:** In particular, our primary points of comparison are modelfree offline RL algorithms based on TD-learning, since our Decision Transformer architecture is fundamentally model-free in nature ...
- **p. 6 / 3 Method - extractive body cue:** In addition, we also compare against other prior model-free RL algorithms like BEAR [18] and BRAC [19]. • Imitation learning: this regime similarly uses supervised ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | By training an autoregressive model on sequences of states, actions, and returns, we reduce policy sampling to autoregressive generative modeling. | state 또는 observation, action, reward와 transition history | p. 3 (1 Introduction), p. 4 (2 Preliminaries) |
| State/latent | training, autoregressive, model, sequences, states, actions, returns, reduce, policy, sampling, generative, modeling | policy/value state와 action-selection variable | p. 3 (1 Introduction), p. 4 (2 Preliminaries), p. 4 (2 Preliminaries) |
| Output/action | We use st, at, and rt = R(st, at) to denote the state, action, and reward at timestep t, respectively. | action policy와 induced trajectory | p. 4 (2 Preliminaries), p. 4 (2 Preliminaries), p. 5 (3 Method) |
| Objective/outcome | As a result, instead of feeding the rewards directly, we feed the model with the returns-to-go bRt = PT t′=t rt′. | expected return, task success, stability와 sample efficiency | p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** Training dataset consists of random walk trajectories and their per-node returns-to-go (middle).
- **p. 4 / 1 Introduction - extractive body cue:** Motivated by this observation, we propose Decision Transformer, where we use the GPT architecture to autoregressively model trajectories (shown in Figure 1).
- **p. 4 / 3 Method - extractive body cue:** In this section, we present Decision Transformer, which models trajectories autoregressively with minimal modification to the transformer architecture, as summarized in Figure 1 and Algorithm ...
- **p. 5 / 3 Method - extractive body cue:** We did not find predicting the states or returns-to-go to improve performance, although it is easily permissible within our framework (as shown in Section 5.4) ...
- **p. 6 / 3 Method - extractive body cue:** We evaluate our method on 1% of all samples in the DQN-replay dataset as per Agarwal et al.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Comparison between Decision Transformer (DT) and Percentile Behavior Cloning (%BC). In contrast, when we study low data regimes - such as Atari, where ...
- **p. 21 / Figure/Table caption - extractive body cue:** Table 12: Raw scores for the 1% DQN-replay Atari dataset. We report the mean and variance across 3 seeds. Best mean scores are highlighted in ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Results for D4RL datasets3. We report the mean and variance for three seeds. Decision Transformer (DT) outperforms conventional RL algorithms on almost all ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 21 (Figure/Table caption) |
| Embodiment/environment | To evaluate this, we consider a delayed return version of the D4RL benchmarks where the agent does not receive any rewards along the trajectory, and instead receives the cumulative reward of the ... | hardware/simulator version and reset protocol | p. 10 (Dataset), p. 10 (Dataset) |
| Dataset/benchmark | Offline RL and the ability to model behaviors has the potential to enable sample-efficient online RL for downstream tasks. | role, split, size and leakage | p. 10 (Dataset), p. 10 (Dataset), p. 11 (Dataset), p. 11 (Dataset) |
| Metric | Table 6: Success rate for Key-to-Door environment. Methods using hindsight (Decision Transformer, %BC) can learn successful policies, while TD learning struggles to perform credit assignment. 5.5 Can transformers be accurate critics in ... | definition, denominator, direction and uncertainty | p. 10 (Figure/Table caption), p. 10 (Dataset), p. 21 (Figure/Table caption) |
| Baseline/ablation | Table 2: Results for D4RL datasets3. We report the mean and variance for three seeds. Decision Transformer (DT) outperforms conventional RL algorithms on almost all tasks. 3Given that CQL is generally the ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 5 Discussion - extractive body cue:** TD learning (CQL) cannot effectively propagate Q-values over the long horizons involved and gets poor performance.
- **p. 11 / Dataset - extractive body cue:** This act of optimizing a learned function can exacerbate and exploit any inaccuracies in the value function approximation, causing failures in policy improvement.
- **p. 12 / 7 Conclusion - extractive body cue:** Transformer models can also be used to model the state evolution of trajectory, potentially serving as an alternative to model-based RL, and we hope to ...
- **p. 10 / Dataset - extractive body cue:** Decision Transformer (DT) and imitation learning are minimally affected by the removal of dense rewards, while CQL fails.
- **p. 10 / Dataset - extractive body cue:** To evaluate this, we consider a delayed return version of the D4RL benchmarks where the agent does not receive any rewards along the trajectory, and ...
- **p. 11 / Dataset - extractive body cue:** Since Decision Transformer does not require explicit optimization using learned functions as objectives, it avoids the need for regularization or conservatism.

## Why Read It

RL, IL, offline learning, and robot data의 rl 문제를 이해하기 위해 읽는다. 본문은 To get an intuition for our proposal, consider the task of finding the shortest path on a directed graph, which can be posed as an RL problem.를 문제로 두고, Training dataset consists of random walk trajectories and their per-node returns-to-go (middle).를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (3 Method), p. 4 (3 Method), p. 6 (3 Method), p. 6 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
