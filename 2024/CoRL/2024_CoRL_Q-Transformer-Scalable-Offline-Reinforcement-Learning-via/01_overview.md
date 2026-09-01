# Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2309.10150.
> PDF retrieval source: https://arxiv.org/pdf/2309.10150. Reading tracker status/evidence was not changed.

- Year/Venue: 2024 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: Robotics, offline reinforcement learning, Transformer, robot manipulation
- Official paper: https://arxiv.org/abs/2309.10150
- Full-text retrieval: https://arxiv.org/pdf/2309.10150
- Code/Project: https://qtransformer.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 offline_rl 문제를 이해하기 위해 읽는다. 본문은 training high-capacity models such as Transformers using RL algorithms has proven more difficult to instantiate effectively at large scale.를 문제로 두고, We propose a specific regularizer that minimizes values of every action that was not taken in the dataset and show that our method can learn from both narrow demonstration-like data and broader ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In this work, we present a scalable reinforcement learning method for training multi-task policies from large offline datasets that can leverage both human demonstrations and ...
- **p. 1 / Abstract - extractive body cue:** Our method uses a Transformer to provide a scalable representation for Q-functions trained via offline temporal difference backups.
- **p. 1 / Abstract - extractive body cue:** We therefore refer to the method as Q-Transformer.
- **p. 1 / Abstract - extractive body cue:** By discretizing each action dimension and representing the Q-value of each action dimension as separate tokens, we can apply effective high-capacity sequence modeling techniques for ...
- **p. 1 / Abstract - extractive body cue:** We present several design decisions that enable good performance with offline RL training, and show that Q-Transformer outperforms prior offline RL algorithms and imitation learning ...
- **p. 2 / 1 Introduction - extractive body cue:** training high-capacity models such as Transformers using RL algorithms has proven more difficult to instantiate effectively at large scale.
- **p. 4 / 3 Background - extractive body cue:** In this work, we consider tasks with sparse rewards, where a binary reward R ∈{0, 1} (indicating success or failure) is assigned at the last ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** We propose a specific regularizer that minimizes values of every action that was not taken in the dataset and show that our method can learn ...
- **p. 4 / 3 Background - extractive body cue:** Next, we introduce a particular conservative Q-function regularizer that enables learning from offline datasets.
- **p. 1 / 1 Introduction - extractive body cue:** Human demonstrations Autonomous data Conservative regularization Autoregressive Q-learning Monte-Carlo returns Mixed quality data environment step action dimension … … Q-values per action dimension Q-Transformer Figure ...
- **p. 2 / 1 Introduction - extractive body cue:** In summary, our main contribution is the Q-Transformer, a Transformer-based architecture for robotic offline reinforcement learning that makes use of per-dimension tokenization of Q-values and ...
- **p. 1 / Abstract - extractive body cue:** Our method uses a Transformer to provide a scalable representation for Q-functions trained via offline temporal difference backups.
- **p. 4 / 3 Background - extractive body cue:** FiLM EfficientNet + Transformer Positional encoding Universal Sentence Encoder Self-Attention Layers (8x) Camera images Language instruction Pick sponge… Q-values for each action bin One-hot action ...
- **p. 4 / 3 Background - extractive body cue:** 4 Q-Transformer In this section, we introduce Q-Transformer, an architecture for offline Q-learning with Transformer models, which is based on three main ingredients.
- **p. 2 / 1 Introduction - extractive body cue:** training high-capacity models such as Transformers using RL algorithms has proven more difficult to instantiate effectively at large scale.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The language instruction is encoded with Universal Sentence Encoder [68] and then fed to FiLM EfficientNet [69, 70] network together with the robot camera images. for real-world robotic learning, where on-policy data ... | dataset state/observation, action, reward와 return-to-go | p. 4 (3 Background), p. 4 (3 Background) |
| State/latent | language, instruction, encoded, Universal, Sentence, Encoder, then, FiLM, EfficientNet, network, together, robot | Q/value 또는 sequence-policy state | p. 4 (3 Background), p. 4 (3 Background), p. 6 (3 Background) |
| Output/action | FiLM EfficientNet + Transformer Positional encoding Universal Sentence Encoder Self-Attention Layers (8x) Camera images Language instruction Pick sponge… Q-values for each action bin One-hot action Feed previously predicted action dimen ... | dataset-supported action sequence | p. 4 (3 Background), p. 6 (3 Background), p. 3 (3 Background) |
| Objective/outcome | The key insight behind our design is that, rather than minimizing the Q-values on actions not in the data, we can instead regularize these Q-values to be close to the minimal attainable ... | offline policy value, OOD safety와 closed-loop success | p. 5 (3 Background), p. 5 (3 Background), p. 3 (3 Background) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** We propose a specific regularizer that minimizes values of every action that was not taken in the dataset and show that our method can learn ...
- **p. 4 / 3 Background - extractive body cue:** Next, we introduce a particular conservative Q-function regularizer that enables learning from offline datasets.
- **p. 1 / 1 Introduction - extractive body cue:** Human demonstrations Autonomous data Conservative regularization Autoregressive Q-learning Monte-Carlo returns Mixed quality data environment step action dimension … … Q-values per action dimension Q-Transformer Figure ...
- **p. 2 / 1 Introduction - extractive body cue:** In summary, our main contribution is the Q-Transformer, a Transformer-based architecture for robotic offline reinforcement learning that makes use of per-dimension tokenization of Q-values and ...
- **p. 1 / Abstract - extractive body cue:** Our method uses a Transformer to provide a scalable representation for Q-functions trained via offline temporal difference backups.
- **p. 7 / 5 Experiments - extractive body cue:** Q-Transformer has the highest success rate and outperforms both the behavior cloning baseline (RT-1) and offline RL baselines (Decision Transformer, IQL), exceeding the average performance ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Left: Ablations: changing to softmax conservatism decreases performance. Removing MC returns or conservatism completely collapse performance. Top Right: The n-step return ver- sion ...
- **p. 7 / 5 Experiments - extractive body cue:** 5.2 Benchmarking in simulation Training steps Success rate QT-Opt CQL AW-Opt IQL Q-Transformer (ours) Decision Transformer RT-1 BC Figure 5: Performance comparison on a simulated ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (5 Experiments), p. 8 (Figure/Table caption) |
| Embodiment/environment | To evaluate how well Q-Transformer can perform when learning from real-world offline datasets while effectively incorporating autonomously collected failed episodes, we evaluate Q-Transformer on 72 unique manipulation tasks, and a varie ... | hardware/simulator version and reset protocol | p. 6 (5 Experiments), p. 8 (5 Experiments) |
| Dataset/benchmark | 5.1 Real-world language-conditioned manipulation evaluation Training dataset. | role, split, size and leakage | p. 6 (5 Experiments), p. 8 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments) |
| Metric | 5.2 Benchmarking in simulation Training steps Success rate QT-Opt CQL AW-Opt IQL Q-Transformer (ours) Decision Transformer RT-1 BC Figure 5: Performance comparison on a simulated picking task. | definition, denominator, direction and uncertainty | p. 7 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments) |
| Baseline/ablation | Q-Transformer has the highest success rate and outperforms both the behavior cloning baseline (RT-1) and offline RL baselines (Decision Transformer, IQL), exceeding the average performance of the best-performing prior method by about ... | fair input/data/compute/action matching | p. 7 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5 Experiments - extractive body cue:** First, we focus on sparse binary reward tasks corresponding to success or failure for each trial.
- **p. 8 / 5 Experiments - extractive body cue:** Our framework does have several limitations.
- **p. 6 / 3 Background - extractive body cue:** Although this does not change convergence, including this maximization speeds up learning (see Section 5.3).
- **p. 6 / 5 Experiments - extractive body cue:** To ensure a fair comparison between Q-Transformer and imitation learning methods, we discard all successful episodes in the autonomously collected data when we train our ...
- **p. 7 / 5 Experiments - extractive body cue:** Decision Transformer is trained on both demonstrations and sub-optimal data, but is not able to leverage the noisy data for policy improvement and does not ...
- **p. 7 / 5 Experiments - extractive body cue:** The demonstrations are replayed with noise to generate more trajectories (∼92% of the data).

## Why Read It

RL, IL, offline learning, and robot data의 offline_rl 문제를 이해하기 위해 읽는다. 본문은 training high-capacity models such as Transformers using RL algorithms has proven more difficult to instantiate effectively at large scale.를 문제로 두고, We propose a specific regularizer that minimizes values of every action that was not taken in the dataset and show that our method can learn from both narrow demonstration-like data and broader ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 4 (3 Background), p. 4 (3 Background), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 4 (3 Background) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
