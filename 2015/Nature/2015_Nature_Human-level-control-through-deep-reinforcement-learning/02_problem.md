# Problem - Human-level control through deep reinforcement learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1038/nature14236; PDF retrieval source: https://doi.org/10.1038/nature14236. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 4 (2 6 F E B R U A R Y), p. 2 (2 6 F E B R U A R Y), p. 2 (2 6 F E B R U A R Y), p. 3 (V O L), p. 4 (2 6 F E B R U A R Y)): Indeed, in certain games DQN is able to discover a relatively long-term strategy (for example, Breakout: the agent learns the optimal strategy, which is to first dig a tunnel around ...

## PDF Body Digest

- **p. 1 / Front matter - extractive PDF cue:** LETTER doi:10.1038/nature14236 Human-level control through deep reinforcement learning Volodymyr Mnih1*, Koray Kavukcuoglu1*, David Silver1*, Andrei A.
- **p. 1 / Front matter - extractive PDF cue:** Bellemare1, Alex Graves1, Martin Riedmiller1, Andreas K.
- **p. 1 / Front matter - extractive PDF cue:** Here we use recent advances in training deep neural networks9-11 to develop a novel artificial agent, termed a deep Q-network, that can learnsuccessfulpoliciesdirectlyfromhigh-dimensionalsensoryinputs using end-to-end ...
- **p. 1 / Front matter - extractive PDF cue:** We tested this agent on the challenging domain of classic Atari 2600 games12.
- **p. 1 / Front matter - extractive PDF cue:** We demonstrate that the deep Q-network agent, receiving only the pixels and the game score as inputs, was able to surpass the performance of all ...
- **p. 4 / 2 6 F E B R U A R Y - extractive PDF cue:** Indeed, in certain games DQN is able to discover a relatively long-term strategy (for example, Breakout: the agent learns the optimal strategy, which is to ...
- **p. 2 / 2 6 F E B R U A R Y - extractive PDF cue:** difficult and engaging for human players.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Indeed, in certain games DQN is able to discover a relatively long-term strategy (for example, Breakout: the agent learns the optimal strategy, ... | robot mechanism의 state와 task-space dynamics | body wording is the source claim |
| Observation / input | The outputs correspond to the predicted Q-values of the individual actions for the input state. | joint/task state, reference와 sensor feedback | exact sensor/frame/preprocessing from PDF |
| State / latent | outputs, correspond, predicted, Q-values, individual, actions, input, state, instead, usean | state estimate, task-space error와 control decision | notation and tensor shape require body check |
| Output / action | input, neural, network, consists, image, produced, preprocessing, followed | torque, force, velocity 또는 position command | exact unit/frame/decoder require body check |
| Target outcome | stability, tracking and constraint satisfaction | tracking, stability, constraint satisfaction과 contact behavior | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | q, q̇, x, wrench; body terms: outputs, correspond, predicted, Q-values, individual, actions, input, state, instead, usean | p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 2 (2 6 F E B R U A R Y) |
| Decision / output variable | u/τ subject to dynamics and actuator/contact constraints; body terms: Notably, able, train, large, neural, networks, temporal, evolution | p. 2 (2 6 F E B R U A R Y), p. 2 (2 6 F E B R U A R Y), p. 3 (V O L) |
| Objective / loss / cost | tracking or interaction error; cue terms: following, intuition, optimal, value, sequence, next, time-step, known | p. 7 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 7 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 8 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 12 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 9 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 9 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| Success / guarantee | stability, tracking and constraint satisfaction | p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 4 (2 6 F E B R U A R Y) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 2 6 F E B R U A R Y - extractive PDF cue:** difficult and engaging for human players.
- **p. 2 / 2 6 F E B R U A R Y - extractive PDF cue:** Our DQN method outperforms the best existing reinforcement learning methods on 43 of the games without incorporating any of the additional prior knowledge about Atari ...
- **p. 3 / V O L - extractive PDF cue:** Furthermore, we also show that the representations learned by DQN are able to generalize to data generated from policies other than its own-in simulations where ...
- **p. 4 / 2 6 F E B R U A R Y - extractive PDF cue:** In the future, it will be important to explore the potential use of biasing the content of experience replay towards salient events, a phenomenon that ...

## What the Paper Changes

PDF contribution framing (p. 2 (2 6 F E B R U A R Y), p. 2 (2 6 F E B R U A R Y), p. 3 (V O L), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 1 (Front matter)): Notably, our method was able to train large neural networks using a reinforcementlearningsignalandstochasticgradientdescentinastablemannerillustrated by the temporal evolution of two indices of learning (the agent's average score-per-ep ...

- **p. 2 / 2 6 F E B R U A R Y - extractive PDF cue:** The input to the neural network consists of an 843 843 4 image produced by the preprocessing map w, followed by three convolutional layers (note: ...
- **p. 3 / V O L - extractive PDF cue:** Furthermore, we also show that the representations learned by DQN are able to generalize to data generated from policies other than its own-in simulations where ...
- **p. 6 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive PDF cue:** The final hidden layer is fully-connected and consists of 512 rectifier units.
- **p. 1 / Front matter - extractive PDF cue:** Here we use recent advances in training deep neural networks9-11 to develop a novel artificial agent, termed a deep Q-network, that can learnsuccessfulpoliciesdirectlyfromhigh-dimensionalsensoryinputs using end-to-end ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | At the same time, it could affect the performance of our agent since it cannot differentiate between rewards ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Thevaluesofallthehyperparametersandoptimizationparameterswereselected by performing an informal search on the games Pong, Breakout, Seaquest, Space Invaders and Beam Rider. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | At time point 2, the agent starts moving the paddle towards the ball and the value of the ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

control writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 2 (2 6 F E B R U A R Y), p. 2 (2 6 F E B R U A R Y). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 4 (2 6 F E B R U A R Y), p. 2 (2 6 F E B R U A R Y), p. 2 (2 6 F E B R U A R Y), p. 3 (V O L), p. 4 (2 6 F E B R U A R Y), interface p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 2 (2 6 F E B R U A R Y), p. 2 (2 6 F E B R U A R Y), objective p. 7 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 7 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 8 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 12 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
