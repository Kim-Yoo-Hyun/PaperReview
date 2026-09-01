# Problem - Conservative Q-Learning for Offline Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html; PDF retrieval source: https://arxiv.org/pdf/2006.04779. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction), p. 5 (2 Preliminaries), p. 5 (2 Preliminaries), p. 6 (2 Preliminaries)): However, applying RL to real-world problems consistently poses practical challenges: in contrast to the kinds of data-driven methods that have been successful in supervised learning [24, 11], RL is classically ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Effectively leveraging large, previously collected datasets in reinforcement learning (RL) is a key challenge for large-scale real-world applications.
- **p. 1 / Abstract - extractive body cue:** Offline RL algorithms promise to learn effective policies from previously-collected, static datasets without further interaction.
- **p. 1 / Abstract - extractive body cue:** However, in practice, offline RL presents a major challenge, and standard off-policy RL methods can fail due to overestimation of values induced by the distributional ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose conservative Q-learning (CQL), which aims to address these limitations by learning a conservative Q-function such that the expected value of ...
- **p. 1 / Abstract - extractive body cue:** We theoretically show that CQL produces a lower bound on the value of the current policy and that it can be incorporated into a policy ...
- **p. 1 / 1 Introduction - extractive body cue:** However, applying RL to real-world problems consistently poses practical challenges: in contrast to the kinds of data-driven methods that have been successful in supervised learning ...
- **p. 1 / 1 Introduction - extractive body cue:** This in principle can make it possible to leverage large datasets, but in practice fully offline RL methods pose major technical difficulties, stemming from the ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, applying RL to real-world problems consistently poses practical challenges: in contrast to the kinds of data-driven methods that have been successful ... | offline robot transition/trajectory dataset과 deployment MDP | body wording is the source claim |
| Observation / input | S, A represent state and action spaces, T(s′/s, a) and r(s, a) represent the dynamics and reward function, and γ ∈(0, 1) ... | dataset state/observation, action, reward와 return-to-go | exact sensor/frame/preprocessing from PDF |
| State / latent | represent, state, action, spaces, dynamics, reward, function, represents, discount, factor | Q/value 또는 sequence-policy state | notation and tensor shape require body check |
| Output / action | choice, penalty, minimize, expected, Qvalue, under, particular, distribution | dataset-supported action sequence | exact unit/frame/decoder require body check |
| Target outcome | offline return and deployment safety | offline policy value, OOD safety와 closed-loop success | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | dataset transition (s,a,r,s′); body terms: represent, state, action, spaces, dynamics, reward, function, represents, discount, factor | p. 2 (2 Preliminaries), p. 2 (2 Preliminaries), p. 3 (2 Preliminaries) |
| Decision / output variable | dataset-supported policy action; body terms: novel, learning, conservative, Qfunctions, simple, modification, standard, value-based | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (2 Preliminaries) |
| Objective / loss / cost | offline value with OOD control; cue terms: step, Train, Q-function, gradient, steps, objective, Equation, CQL | p. 6 (2 Preliminaries), p. 5 (2 Preliminaries), p. 3 (2 Preliminaries), p. 4 (2 Preliminaries), p. 6 (2 Preliminaries), p. 1 (Abstract) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (2 Preliminaries), p. 2 (1 Introduction), p. 3 (2 Preliminaries) |
| Success / guarantee | offline return and deployment safety | p. 2 (1 Introduction), p. 8 (Figure/Table caption), p. 5 (2 Preliminaries) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** This in principle can make it possible to leverage large datasets, but in practice fully offline RL methods pose major technical difficulties, stemming from the ...
- **p. 5 / 2 Preliminaries - extractive body cue:** We also showed that the Q-function is gap-expanding, meaning that it should only ever over-estimate the gap between in-distribution and out-of-distribution actions, preventing OOD actions.
- **p. 5 / 2 Preliminaries - extractive body cue:** Our final result shows that CQL Q-function update is "gap-expanding", by which we mean that the difference in Q-values at in-distribution actions and over-optimistically erroneous ...
- **p. 6 / 2 Preliminaries - extractive body cue:** Note that this penalty is implicitly introduced by virtue by the gap-expanding (Theorem 3.4) behavior of CQL.

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (2 Preliminaries), p. 1 (Abstract), p. 4 (2 Preliminaries)): We propose a novel method for learning such conservative Qfunctions via a simple modification to standard value-based RL algorithms.

- **p. 2 / 1 Introduction - extractive body cue:** The key idea behind our method is to minimize values under an appropriately chosen distribution over state-action tuples, and then further tighten this bound by ...
- **p. 5 / 2 Preliminaries - extractive body cue:** 3.3 Safe Policy Improvement Guarantees In Section 3.1 we proposed novel objectives for Q-function training such that the expected value of a policy under the ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose conservative Q-learning (CQL), which aims to address these limitations by learning a conservative Q-function such that the expected value of ...
- **p. 4 / 2 Preliminaries - extractive body cue:** Due to space constraints, we present these results in Theorem D.1 and Theorem D.2 in Appendix D.1.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 1 | This has made current results fall short of the full promise of such methods. | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | In this paper, we propose conservative Q-learning (CQL), which aims to address these limitations by learning a conservative ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Note that Q-function training in offline RL does not suffer from state distribution shift, as the Bellman backup ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Figure 1: Performance of CQL, QR-DQN and REM as a function of training steps (x-axis) in setting (1) ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

offline_rl writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (2 Preliminaries), p. 2 (2 Preliminaries), p. 3 (2 Preliminaries), p. 3 (2 Preliminaries). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), p. 5 (2 Preliminaries), p. 5 (2 Preliminaries), p. 6 (2 Preliminaries), interface p. 2 (2 Preliminaries), p. 2 (2 Preliminaries), p. 3 (2 Preliminaries), p. 3 (2 Preliminaries), objective p. 6 (2 Preliminaries), p. 5 (2 Preliminaries), p. 3 (2 Preliminaries), p. 4 (2 Preliminaries), p. 6 (2 Preliminaries), p. 1 (Abstract).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
