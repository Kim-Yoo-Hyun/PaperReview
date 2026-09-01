# Problem - DayDreamer: World Models for Physical Robot Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v205/wu23c.html; PDF retrieval source: https://arxiv.org/pdf/2206.14176. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction)): Despite the promises of world models, learning accurate world models for the real world is a big open challenge.

## PDF Body Digest

- **p. 2 / 1 Introduction - extractive body cue:** Replay Buffer Real World Actor Critic World Model Figure 2: Dreamer follows a simple pipeline for online learning on robot hardware without simulators.
- **p. 2 / 1 Introduction - extractive body cue:** The current learned policy collects experience on the robot.
- **p. 2 / 1 Introduction - extractive body cue:** This experience is added to the replay buffer.
- **p. 2 / 1 Introduction - extractive body cue:** The world model is trained on replayed off-policy sequences through supervised learning.
- **p. 2 / 1 Introduction - extractive body cue:** An actor critic algorithm optimizes a neural network policy from imagined rollouts in the latent space of the world model.
- **p. 2 / 1 Introduction - extractive body cue:** Despite the promises of world models, learning accurate world models for the real world is a big open challenge.
- **p. 2 / 1 Introduction - extractive body cue:** However, current algorithms require too much interaction with the environment to learn successful behaviors, making them impractical for many real world tasks.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Despite the promises of world models, learning accurate world models for the real world is a big open challenge. | uncertain robot state와 safe/unsafe operating region | body wording is the source claim |
| Observation / input | The world model is based on the Recurrent State-Space Model (RSSM; Hafner et al., 2018), which consists of four components: Encoder Network: ... | observation, uncertainty/risk estimate와 task command | exact sensor/frame/preprocessing from PDF |
| State / latent | world, model, Recurrent, State-Space, RSSM, Hafner, consists, four, components, Encoder | safe set, recovery state 또는 constraint margin | notation and tensor shape require body check |
| Output / action | actor, critic, algorithm, consists, neural, networks, Network, role | shielded, recovery 또는 safe action | exact unit/frame/decoder require body check |
| Target outcome | low violation/failure probability with useful intervention | task return과 violation/failure probability | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | state/history and risk h(s); body terms: world, model, Recurrent, State-Space, RSSM, Hafner, consists, four, components, Encoder | p. 3 (2 Approach), p. 3 (1 Introduction), p. 4 (2 Approach) |
| Decision / output variable | filtered/recovery action u_safe; body terms: Dreamer, consists, neural, network, components, world, model, Recurrent | p. 3 (1 Introduction), p. 3 (2 Approach), p. 4 (2 Approach) |
| Objective / loss / cost | task utility subject to safety constraint; cue terms: actor, critic, algorithm, consists, neural, networks, Network, role | p. 4 (2 Approach), p. 4 (2 Approach), p. 3 (2 Approach) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (2 Approach), p. 3 (2 Approach), p. 3 (2 Approach) |
| Success / guarantee | low violation/failure probability with useful intervention | p. 6 (3 Experiments), p. 6 (3 Experiments), p. 7 (3 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** However, current algorithms require too much interaction with the environment to learn successful behaviors, making them impractical for many real world tasks.
- **p. 3 / 1 Introduction - extractive body cue:** A recurrent state-space model (RSSM) is trained to predict future codes given actions, without observing intermediate inputs.

## What the Paper Changes

PDF contribution framing (p. 3 (1 Introduction), p. 3 (2 Approach), p. 4 (2 Approach), p. 2 (1 Introduction), p. 2 (1 Introduction)): Dreamer consists of two neural network components.

- **p. 3 / 2 Approach - extractive body cue:** The world model is based on the Recurrent State-Space Model (RSSM; Hafner et al., 2018), which consists of four components: Encoder Network: encθ(st / st-1, ...
- **p. 4 / 2 Approach - extractive body cue:** The actor critic algorithm consists of two neural networks: Actor Network: π(at / st) Critic Network: v(st) (2) The role of the actor network is ...
- **p. 2 / 1 Introduction - extractive body cue:** Deep reinforcement learning (RL) offers a popular approach to robot learning that enables robots to improve their behavior over time through trial and error.
- **p. 2 / 1 Introduction - extractive body cue:** The key contributions of this paper are summarized as follows: • Dreamer on Robots We apply Dreamer to 4 robots, demonstrating successful learning directly in ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Limitations While Dreamer shows promising results, learning on hardware over many hours creates wear on robots that may ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | In comparison, SAC quickly learns to roll off its back but fails to stand up or walk given ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Prior work in quadruped locomotion requires either extensive training in simulation under domain randomization, using recovery controllers to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | The filled circles indicate times where the robot fell on its back, requiring the learning of a robust ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

safety writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (2 Approach), p. 3 (1 Introduction), p. 4 (2 Approach), p. 4 (2 Approach). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), interface p. 3 (2 Approach), p. 3 (1 Introduction), p. 4 (2 Approach), p. 4 (2 Approach), objective p. 4 (2 Approach), p. 4 (2 Approach), p. 3 (2 Approach).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
