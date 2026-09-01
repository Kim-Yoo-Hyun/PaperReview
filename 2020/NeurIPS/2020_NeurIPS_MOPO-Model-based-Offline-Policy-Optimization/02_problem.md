# Problem - MOPO: Model-based Offline Policy Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2005.13239; PDF retrieval source: https://arxiv.org/pdf/2005.13239. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Preliminaries), p. 7 (3 Preliminaries)): Our results suggest that MOPO substantially outperforms these prior methods on the offline RL benchmark D4RL [18] as well as on offline RL problems where the agent must generalize to ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Offline reinforcement learning (RL) refers to the problem of learning policies entirely from a large batch of previously collected data.
- **p. 1 / Abstract - extractive body cue:** This problem setting offers the promise of utilizing such datasets to acquire policies without any costly or dangerous active exploration.
- **p. 1 / Abstract - extractive body cue:** However, it is also challenging, due to the distributional shift between the offline training data and those states visited by the learned policy.
- **p. 1 / Abstract - extractive body cue:** Despite significant recent progress, the most successful prior methods are model-free and constrain the policy to the support of data, precluding generalization to unseen states.
- **p. 1 / Abstract - extractive body cue:** In this paper, we first observe that an existing model-based RL algorithm already produces significant gains in the offline setting compared to model-free approaches.
- **p. 2 / 1 Introduction - extractive body cue:** Our results suggest that MOPO substantially outperforms these prior methods on the offline RL benchmark D4RL [18] as well as on offline RL problems where ...
- **p. 1 / 1 Introduction - extractive body cue:** These failures are generally caused by large extrapolation error when the Q-function is evaluated on out-of-distribution actions [19, 36], which can lead to unstable learning ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Our results suggest that MOPO substantially outperforms these prior methods on the offline RL benchmark D4RL [18] as well as on offline ... | offline robot transition/trajectory dataset과 deployment MDP | body wording is the source claim |
| Observation / input | 4 MOPO: Model-Based Offline Policy Optimization Unlike model-free methods, our goal is to design an offline model-based reinforcement learning algorithm that can ... | dataset state/observation, action, reward와 return-to-go | exact sensor/frame/preprocessing from PDF |
| State / latent | MOPO, Model-Based, Offline, Policy, Optimization, Unlike, model-free, methods, goal, design | Q/value 또는 sequence-policy state | notation and tensor shape require body check |
| Output / action | Let, denote, probability, being, state, time, step, actions | dataset-supported action sequence | exact unit/frame/decoder require body check |
| Target outcome | offline return and deployment safety | offline policy value, OOD safety와 closed-loop success | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | dataset transition (s,a,r,s′); body terms: MOPO, Model-Based, Offline, Policy, Optimization, Unlike, model-free, methods, goal, design | p. 4 (3 Preliminaries), p. 2 (1 Introduction), p. 3 (3 Preliminaries) |
| Decision / output variable | dataset-supported policy action; body terms: Specifically, methods, estimate, error, respect, out-of-distribution, actions, only | p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract) |
| Objective / loss / cost | offline value with OOD control; cue terms: Moreover, equation, suggests, policy, obtains, high, reward, estimated | p. 2 (1 Introduction), p. 4 (3 Preliminaries), p. 4 (3 Preliminaries), p. 5 (3 Preliminaries), p. 5 (3 Preliminaries), p. 6 (3 Preliminaries) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3 Preliminaries), p. 1 (Abstract), p. 2 (1 Introduction) |
| Success / guarantee | offline return and deployment safety | p. 7 (5 Experiments), p. 8 (Figure/Table caption), p. 8 (5 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** These failures are generally caused by large extrapolation error when the Q-function is evaluated on out-of-distribution actions [19, 36], which can lead to unstable learning ...
- **p. 2 / 1 Introduction - extractive body cue:** In particular, because offline model-based algorithms cannot improve the dynamics model using additional experience, we expect that such algorithms require careful use of the model ...
- **p. 3 / 3 Preliminaries - extractive body cue:** In the offline RL problem, the algorithm only has access to a static dataset Denv = {(s, a, r, s′)} collected by one or a ...
- **p. 7 / 3 Preliminaries - extractive body cue:** While this estimator lacks theoretical guarantees, we find that it is sufficiently accurate to achieve good performance in practice.4 Hence the practical uncertainty-penalized reward of ...

## What the Paper Changes

PDF contribution framing (p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 5 (3 Preliminaries), p. 2 (1 Introduction)): Specifically, these methods estimate error with respect to out-of-distribution actions, but only consider states that lie within the offline dataset and do not ∗equal contribution. † equal advising.

- **p. 2 / 1 Introduction - extractive body cue:** The primary contribution of this work is an offline model-based RL algorithm that optimizes a policy in an uncertainty-penalized MDP, where the reward function is ...
- **p. 1 / Abstract - extractive body cue:** Instead, we propose to modify the existing model-based RL methods by applying them with rewards artificially penalized by the uncertainty of the dynamics.
- **p. 5 / 3 Preliminaries - extractive body cue:** We will analyze our framework under the assumption that we have access to an oracle uncertainty quantification module that provides an upper bound on the ...
- **p. 2 / 1 Introduction - extractive body cue:** Although neither method is designed for the batch setting, we find that the model-based method and its variant without ensembles show surprisingly large gains.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | However, uncertainty estimation does not explain the entire difference nor does it explain why model-free methods cannot also ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Our work opens up a number of questions and directions for future work. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | In particular, model-free offline RL cannot outperform the best trajectory in the batch dataset, whereas MOPO exceeds the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | BRACv uses this penalty both when updating the critic and when updating the actor, while BRAC-p uses this ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

offline_rl writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3 Preliminaries), p. 2 (1 Introduction), p. 3 (3 Preliminaries), p. 3 (3 Preliminaries). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Preliminaries), p. 7 (3 Preliminaries), interface p. 4 (3 Preliminaries), p. 2 (1 Introduction), p. 3 (3 Preliminaries), p. 3 (3 Preliminaries), objective p. 2 (1 Introduction), p. 4 (3 Preliminaries), p. 4 (3 Preliminaries), p. 5 (3 Preliminaries), p. 5 (3 Preliminaries), p. 6 (3 Preliminaries).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
