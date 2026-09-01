# Problem - Decision Transformer: Reinforcement Learning via Sequence Modeling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2106.01345; PDF retrieval source: https://arxiv.org/pdf/2106.01345. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 3 (1 Introduction), p. 3 (1 Introduction)): To get an intuition for our proposal, consider the task of finding the shortest path on a directed graph, which can be posed as an RL problem.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We introduce a framework that abstracts Reinforcement Learning (RL) as a sequence modeling problem.
- **p. 1 / Abstract - extractive body cue:** This allows us to draw upon the simplicity and scalability of the Transformer architecture, and associated advances in language modeling such as GPT-x and BERT.
- **p. 1 / Abstract - extractive body cue:** In particular, we present Decision Transformer, an architecture that casts the problem of RL as conditional sequence modeling.
- **p. 1 / Abstract - extractive body cue:** Unlike prior approaches to RL that fit value functions or compute policy gradients, Decision Transformer simply outputs the optimal actions by leveraging a causally masked ...
- **p. 1 / Abstract - extractive body cue:** By conditioning an autoregressive model on the desired return (reward), past states, and actions, our Decision Transformer model can generate future actions that achieve the ...
- **p. 3 / 1 Introduction - extractive body cue:** To get an intuition for our proposal, consider the task of finding the shortest path on a directed graph, which can be posed as an ...
- **p. 3 / 1 Introduction - extractive body cue:** Finally, empirical evidence suggest that a transformer modeling approach can model a wide distribution of behaviors, enabling better generalization and transfer [3].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | To get an intuition for our proposal, consider the task of finding the shortest path on a directed graph, which can be ... | robot/environment의 sequential decision process | body wording is the source claim |
| Observation / input | By training an autoregressive model on sequences of states, actions, and returns, we reduce policy sampling to autoregressive generative modeling. | state 또는 observation, action, reward와 transition history | exact sensor/frame/preprocessing from PDF |
| State / latent | training, autoregressive, model, sequences, states, actions, returns, reduce, policy, sampling | policy/value state와 action-selection variable | notation and tensor shape require body check |
| Output / action | MDP, tuple, consists, states, actions, transition, dynamics, reward | action policy와 induced trajectory | exact unit/frame/decoder require body check |
| Target outcome | task return, success and safe execution | expected return, task success, stability와 sample efficiency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s_t/o_t; body terms: training, autoregressive, model, sequences, states, actions, returns, reduce, policy, sampling | p. 3 (1 Introduction), p. 4 (2 Preliminaries), p. 4 (2 Preliminaries) |
| Decision / output variable | a_t sampled or selected by πθ; body terms: Training, dataset, consists, random, walk, trajectories, per-node, returns-to-go | p. 3 (1 Introduction), p. 4 (1 Introduction), p. 4 (3 Method) |
| Objective / loss / cost | expected return / constrained return; cue terms: result, instead, feeding, rewards, directly, feed, model, returns-to-go | p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method) |
| Success / guarantee | task return, success and safe execution | p. 10 (Figure/Table caption), p. 10 (Dataset), p. 21 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 3 / 1 Introduction - extractive body cue:** Finally, empirical evidence suggest that a transformer modeling approach can model a wide distribution of behaviors, enabling better generalization and transfer [3].

## What the Paper Changes

PDF contribution framing (p. 3 (1 Introduction), p. 4 (1 Introduction), p. 4 (3 Method), p. 5 (3 Method), p. 6 (3 Method)): Training dataset consists of random walk trajectories and their per-node returns-to-go (middle).

- **p. 4 / 1 Introduction - extractive body cue:** Motivated by this observation, we propose Decision Transformer, where we use the GPT architecture to autoregressively model trajectories (shown in Figure 1).
- **p. 4 / 3 Method - extractive body cue:** In this section, we present Decision Transformer, which models trajectories autoregressively with minimal modification to the transformer architecture, as summarized in Figure 1 and Algorithm ...
- **p. 5 / 3 Method - extractive body cue:** We did not find predicting the states or returns-to-go to improve performance, although it is easily permissible within our framework (as shown in Section 5.4) ...
- **p. 6 / 3 Method - extractive body cue:** We evaluate our method on 1% of all samples in the DQN-replay dataset as per Agarwal et al.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | TD learning (CQL) cannot effectively propagate Q-values over the long horizons involved and gets poor performance. | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | This act of optimizing a learned function can exacerbate and exploit any inaccuracies in the value function approximation, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | Transformer models can also be used to model the state evolution of trajectory, potentially serving as an alternative ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Decision Transformer (DT) and imitation learning are minimally affected by the removal of dense rewards, while CQL fails. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

rl writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (1 Introduction), p. 4 (2 Preliminaries), p. 4 (2 Preliminaries), p. 5 (3 Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 3 (1 Introduction), p. 3 (1 Introduction), interface p. 3 (1 Introduction), p. 4 (2 Preliminaries), p. 4 (2 Preliminaries), p. 5 (3 Method), objective p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
