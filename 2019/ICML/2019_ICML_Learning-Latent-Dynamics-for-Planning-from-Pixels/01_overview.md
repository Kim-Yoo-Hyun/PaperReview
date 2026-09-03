# Learning Latent Dynamics for Planning from Pixels

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1811.04551.
> PDF retrieval source: https://arxiv.org/pdf/1811.04551. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2019 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, world model, Planning, latent dynamics
- Official paper: https://arxiv.org/abs/1811.04551
- Full-text retrieval: https://arxiv.org/pdf/1811.04551
- Code/Project: https://planetrl.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 Key difficulties include model inaccuracies, accumulating errors of multi-step predictions, failure to capture multiple possible futures, and overconfident predictions outside of the training distribution.를 문제로 두고, In this paper, we propose the Deep Planning Network (PlaNet), a model-based agent that learns the environment dynamics from pixels and chooses actions through online planning in a compact latent space.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Planning has been very successful for control tasks with known environment dynamics.
- **p. 1 / Abstract - extractive body cue:** To leverage planning in unknown environments, the agent needs to learn the dynamics from interactions with the world.
- **p. 1 / Abstract - extractive body cue:** However, learning dynamics models that are accurate enough for planning has been a long-standing challenge, especially in image-based domains.
- **p. 1 / Abstract - extractive body cue:** We propose the Deep Planning Network (PlaNet), a purely model-based agent that learns the environment dynamics from images and chooses actions through fast online planning ...
- **p. 1 / Abstract - extractive body cue:** To achieve high performance, the dynamics model must accurately predict the rewards ahead for multiple time steps.
- **p. 1 / 1. Introduction - extractive body cue:** Key difficulties include model inaccuracies, accumulating errors of multi-step predictions, failure to capture multiple possible futures, and overconfident predictions outside of the training distribution.
- **p. 1 / 1. Introduction - extractive body cue:** PlaNet solves continuous control tasks from pixels that are more difficult than those previously solved by planning with learned models.

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we propose the Deep Planning Network (PlaNet), a model-based agent that learns the environment dynamics from pixels and chooses actions through online ...
- **p. 1 / 1. Introduction - extractive body cue:** Key contributions of this work are summarized as follows: • Planning in latent spaces We solve a variety of tasks from the DeepMind control suite, ...
- **p. 2 / 2. Latent Space Planning - extractive body cue:** In this section, we introduce notation for the environment and describe the general implementation of our model-based agent.
- **p. 3 / 2 Initialize model parameters θ randomly - extractive body cue:** Because the reward is modeled as a function of the latent state, the planner can operate purely in latent space without generating images, which allows ...
- **p. 2 / 2. Latent Space Planning - extractive body cue:** We define a discrete time step t, hidden states st, image observations ot, continuous action vectors at, and scalar rewards rt, that follow the stochastic ...
- **p. 3 / 3. Recurrent State Space Model - extractive body cue:** Instead, we use an encoder q(s1:T / o1:T , a1:T ) = QT t=1 q(st / st-1, at-1, ot) to infer approximate state posteriors from ...
- **p. 4 / 3. Recurrent State Space Model - extractive body cue:** We use such a model, shown in Figure 2c, that we name recurrent state-space model (RSSM), Deterministic state model: ht = f(ht-1, st-1, at-1) Stochastic ...
- **p. 3 / 3. Recurrent State Space Model - extractive body cue:** In this section, we remind the reader of latent state-space models and then describe our dynamics model.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We define a discrete time step t, hidden states st, image observations ot, continuous action vectors at, and scalar rewards rt, that follow the stochastic dynamics Transition function: st ∼p(st / st-1, ... | observation, uncertainty/risk estimate와 task command | p. 2 (2. Latent Space Planning), p. 3 (3. Recurrent State Space Model) |
| State/latent | define, discrete, time, step, hidden, states, image, observations, continuous, action, vectors, scalar | safe set, recovery state 또는 constraint margin | p. 2 (2. Latent Space Planning), p. 3 (3. Recurrent State Space Model), p. 2 (2. Latent Space Planning) |
| Output/action | Instead, we use an encoder q(s1:T / o1:T , a1:T ) = QT t=1 q(st / st-1, at-1, ot) to infer approximate state posteriors from past observations and actions, where q(st / ... | shielded, recovery 또는 safe action | p. 3 (3. Recurrent State Space Model), p. 2 (2. Latent Space Planning), p. 3 (2 Initialize model parameters θ randomly) |
| Objective/outcome | CEM is a populationbased optimization algorithm that infers a distribution over action sequences that maximize the objective. | task return과 violation/failure probability | p. 3 (2 Initialize model parameters θ randomly), p. 4 (3. Recurrent State Space Model), p. 2 (2 Initialize model parameters θ randomly) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we propose the Deep Planning Network (PlaNet), a model-based agent that learns the environment dynamics from pixels and chooses actions through online ...
- **p. 1 / 1. Introduction - extractive body cue:** Key contributions of this work are summarized as follows: • Planning in latent spaces We solve a variety of tasks from the DeepMind control suite, ...
- **p. 2 / 2. Latent Space Planning - extractive body cue:** In this section, we introduce notation for the environment and describe the general implementation of our model-based agent.
- **p. 3 / 2 Initialize model parameters θ randomly - extractive body cue:** Because the reward is modeled as a function of the latent state, the planner can operate purely in latent space without generating images, which allows ...
- **p. 6 / 5. Experiments - extractive body cue:** Within less than one hundredth the episodes, PlaNet outperforms A3C (Mnih et al., 2016) and achieves similar performance to the top model-free algorithm D4PG (Barth-Maron ...
- **p. 6 / 5. Experiments - extractive body cue:** Iterative search for action sequences using CEM improves performance on all tasks.
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 12: Planning performance on the cheetah running task with the true simulator using different planner settings. Performance ranges from 132 (blue) to 837 (yellow). ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Comparison of PlaNet to the model-free algorithms A3C and D4PG reported by Tassa et al. (2018). The training curves for these are shown ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 6 (5. Experiments), p. 6 (5. Experiments) |
| Embodiment/environment | The cartpole swingup task requires a long planning horizon and to memorize the cart when it is out of view, reacher has a sparse reward given when the hand and goal area ... | hardware/simulator version and reset protocol | p. 6 (5. Experiments), p. 6 (5. Experiments) |
| Dataset/benchmark | The cartpole swingup task requires a long planning horizon and to memorize the cart when it is out of view, reacher has a sparse reward given when the hand and goal area ... | role, split, size and leakage | p. 6 (5. Experiments), p. 6 (5. Experiments) |
| Metric | The cartpole swingup task requires a long planning horizon and to memorize the cart when it is out of view, reacher has a sparse reward given when the hand and goal area ... | definition, denominator, direction and uncertainty | p. 6 (5. Experiments), p. 7 (Figure/Table caption), p. 19 (Figure/Table caption) |
| Baseline/ablation | The agent solves all tasks while learning slower compared to individually trained agents. | fair input/data/compute/action matching | p. 6 (5. Experiments), p. 6 (5. Experiments), p. 2 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 7. Discussion - extractive body cue:** Directions for future work include learning temporal abstraction instead of using a fixed action repeat, possibly through hierarchical models.
- **p. 6 / 5. Experiments - extractive body cue:** The cartpole swingup task requires a long planning horizon and to memorize the cart when it is out of view, reacher has a sparse reward ...
- **p. 6 / 5. Experiments - extractive body cue:** The noise might also add a safety margin to the planning objective that results in more robust action sequences.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Comparison of PlaNet to model-free algorithms and other model designs. Plots show test performance over the number of collected episodes. We compare PlaNet ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Latent dynamics model designs. In this example, the model observes the first two time steps and predicts the third. Circles represent stochastic variables ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 9: Comparison of hard ReLU (Nair & Hinton, 2010) and smooth ELU (Clevert et al., 2015) activation functions. We find that smooth activations help ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 10: Open-loop video predictions for test episodes. The columns 1-5 show reconstructed context frames and the remaining images are generated open-loop. Our RSSM achieves ...

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 Key difficulties include model inaccuracies, accumulating errors of multi-step predictions, failure to capture multiple possible futures, and overconfident predictions outside of the training distribution.를 문제로 두고, In this paper, we propose the Deep Planning Network (PlaNet), a model-based agent that learns the environment dynamics from pixels and chooses actions through online planning in a compact latent space.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 2 (2. Latent Space Planning), p. 3 (3. Recurrent State Space Model) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** PlaNet solves continuous control tasks from pixels that are more difficult than those previously solved by planning with learned models. (p. 1, 1. Introduction).
- **Actual contribution:** Key contributions of this work are summarized as follows: • Planning in latent spaces We solve a variety of tasks from the DeepMind control suite, shown in Figure 1, by ... (p. 1, 1. Introduction).
- **Evaluation boundary:** Figure 12: Planning performance on the cheetah running task with the true simulator using different planner settings. Performance ranges from 132 (blue) to 837 (yellow). Evaluating more action sequences, optimizing ... (p. 20, Figure/Table caption).
- **Explicit failure boundary:** Key difficulties include model inaccuracies, accumulating errors of multi-step predictions, failure to capture multiple possible futures, and overconfident predictions outside of the training distribution. (p. 1, 1. Introduction).
