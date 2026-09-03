# Problem - Continuous Control with Deep Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1509.02971; PDF retrieval source: https://arxiv.org/pdf/1509.02971. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND)): However, this has many limitations, most notably the curse of dimensionality: the number of actions increases exponentially with the number of degrees of freedom.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** We adapt the ideas underlying the success of Deep Q-Learning to the continuous action domain.
- **p. 1 / ABSTRACT - extractive body cue:** We present an actor-critic, model-free algorithm based on the deterministic policy gradient that can operate over continuous action spaces.
- **p. 1 / ABSTRACT - extractive body cue:** Using the same learning algorithm, network architecture and hyper-parameters, our algorithm robustly solves more than 20 simulated physics tasks, including classic problems such as cartpole ...
- **p. 1 / ABSTRACT - extractive body cue:** Our algorithm is able to find policies whose performance is competitive with those found by a planning algorithm with full access to the dynamics of ...
- **p. 1 / ABSTRACT - extractive body cue:** We further demonstrate that for many of the tasks the algorithm can learn policies "end-to-end": directly from raw pixel inputs.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, this has many limitations, most notably the curse of dimensionality: the number of actions increases exponentially with the number of degrees of freedom.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Such large action spaces are difficult to explore efficiently, and thus successfully training DQN-like networks in this context is likely intractable.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, this has many limitations, most notably the curse of dimensionality: the number of actions increases exponentially with the number of degrees ... | robot/environment의 sequential decision process | body wording is the source claim |
| Observation / input | A long-standing challenge of robotic control is to learn an action policy directly from raw sensory input such as video. | state 또는 observation, action, reward와 transition history | exact sensor/frame/preprocessing from PDF body |
| State / latent | long-standing, challenge, robotic, control, learn, action, policy, directly, sensory, input | policy/value state와 action-selection variable | notation and tensor shape require body check |
| Output / action | DPG, algorithm, maintains, parameterized, actor, function, specifies, current | action policy와 induced trajectory | exact unit/frame/decoder require body check |
| Target outcome | task return, success and safe execution | expected return, task success, stability와 sample efficiency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s_t/o_t; body terms: long-standing, challenge, robotic, control, learn, action, policy, directly, sensory, input | p. 2 (1 INTRODUCTION), p. 2 (2 BACKGROUND), p. 3 (2 BACKGROUND) |
| Decision / output variable | a_t sampled or selected by πθ; body terms: present, model-free, off-policy, actor-critic, algorithm, deep, function, approximators | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT) |
| Objective / loss / cost | expected return / constrained return; cue terms: consider, function, approximators, parameterized, optimize, minimizing, loss, Est | p. 4 (2 BACKGROUND), p. 1 (ABSTRACT), p. 3 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (2 BACKGROUND), p. 4 (2 BACKGROUND), p. 3 (2 BACKGROUND) |
| Success / guarantee | task return, success and safe execution | p. 7 (Figure/Table caption), p. 6 (4 RESULTS), p. 5 (4 RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive body cue:** Such large action spaces are difficult to explore efficiently, and thus successfully training DQN-like networks in this context is likely intractable.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Prior to DQN, it was generally believed that learning value functions using large, non-linear function approximators was difficult and unstable.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** A key feature of the approach is its simplicity: it requires only a straightforward actor-critic architecture and learning algorithm with very few "moving parts", making ...
- **p. 3 / 2 BACKGROUND - extractive body cue:** However, such approximators appear essential in order to learn and generalize on large state spaces.

## What the Paper Changes

PDF body contribution framing (p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND)): In this work we present a model-free, off-policy actor-critic algorithm using deep function approximators that can learn policies in high-dimensional, continuous action spaces.

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In order to evaluate our method we constructed a variety of challenging physical control problems that involve complex multi-joint movements, unstable and rich contact dynamics, ...
- **p. 1 / ABSTRACT - extractive body cue:** We present an actor-critic, model-free algorithm based on the deterministic policy gradient that can operate over continuous action spaces.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, as we show below, a naive application of this actor-critic method with neural function approximators is unstable for challenging problems.
- **p. 3 / 2 BACKGROUND - extractive body cue:** Our contribution here is to provide modifications to DPG, inspired by the success of DQN, which allow it to use neural network function approximators to ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 12 | Table 2: Dimensionality of the MuJoCo tasks: the dimensionality of the underlying physics model dim(s), number of action ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | The work combines insights from recent advances in deep learning and reinforcement learning, resulting in an algorithm that ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | We evaluated the policy periodically during training by testing it without exploration noise. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | We used an identical network architecture and learning algorithm hyper-parameters to the physics tasks but altered the noise ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

rl writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1 INTRODUCTION), p. 2 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND), interface p. 2 (1 INTRODUCTION), p. 2 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND), objective p. 4 (2 BACKGROUND), p. 1 (ABSTRACT), p. 3 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, this has many limitations, most notably the curse of dimensionality: the number of actions increases exponentially with the number of degrees of freedom. (p. 1, 1 INTRODUCTION).
- **Formulation-changing contribution:** In this work we present a model-free, off-policy actor-critic algorithm using deep function approximators that can learn policies in high-dimensional, continuous action spaces. (p. 1, 1 INTRODUCTION).
- **Assumption/failure evidence:** On both low-dimensional and from pixels, some replicas were able to learn reasonable policies that are able to complete a circuit around the track though other replicas failed to learn ... (p. 6, 4 RESULTS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
