# Human-level control through deep reinforcement learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://doi.org/10.1038/nature14236.
> PDF retrieval source: https://doi.org/10.1038/nature14236. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2015 / Nature
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: Robotics, Reinforcement Learning, Deep Q-Network, Value Learning
- Official paper: https://doi.org/10.1038/nature14236
- Full-text retrieval: https://doi.org/10.1038/nature14236
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 control 문제를 이해하기 위해 읽는다. 본문은 Indeed, in certain games DQN is able to discover a relatively long-term strategy (for example, Breakout: the agent learns the optimal strategy, which is to first dig a tunnel around the side ...를 문제로 두고, Notably, our method was able to train large neural networks using a reinforcementlearningsignalandstochasticgradientdescentinastablemannerillustrated by the temporal evolution of two indices of learning (the agent's average score-per-ep ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Body text (section not recovered) - extractive body cue:** LETTER doi:10.1038/nature14236 Human-level control through deep reinforcement learning Volodymyr Mnih1*, Koray Kavukcuoglu1*, David Silver1*, Andrei A.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Bellemare1, Alex Graves1, Martin Riedmiller1, Andreas K.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Here we use recent advances in training deep neural networks9-11 to develop a novel artificial agent, termed a deep Q-network, that can learnsuccessfulpoliciesdirectlyfromhigh-dimensionalsensoryinputs using end-to-end ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** We tested this agent on the challenging domain of classic Atari 2600 games12.
- **p. 1 / Body text (section not recovered) - extractive body cue:** We demonstrate that the deep Q-network agent, receiving only the pixels and the game score as inputs, was able to surpass the performance of all ...
- **p. 4 / 2 6 F E B R U A R Y - extractive body cue:** Indeed, in certain games DQN is able to discover a relatively long-term strategy (for example, Breakout: the agent learns the optimal strategy, which is to ...
- **p. 2 / 2 6 F E B R U A R Y - extractive body cue:** difficult and engaging for human players.

## Core Idea

- **p. 2 / 2 6 F E B R U A R Y - extractive body cue:** Notably, our method was able to train large neural networks using a reinforcementlearningsignalandstochasticgradientdescentinastablemannerillustrated by the temporal evolution of two indices of learning (the agent's average ...
- **p. 2 / 2 6 F E B R U A R Y - extractive body cue:** The input to the neural network consists of an 843 843 4 image produced by the preprocessing map w, followed by three convolutional layers (note: ...
- **p. 3 / V O L - extractive body cue:** Furthermore, we also show that the representations learned by DQN are able to generalize to data generated from policies other than its own-in simulations where ...
- **p. 6 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** The final hidden layer is fully-connected and consists of 512 rectifier units.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Here we use recent advances in training deep neural networks9-11 to develop a novel artificial agent, termed a deep Q-network, that can learnsuccessfulpoliciesdirectlyfromhigh-dimensionalsensoryinputs using end-to-end ...
- **p. 6 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** The main advantageof this type of architecture is the ability tocompute Q-valuesforall possibleactionsinagivenstatewithonlyasingleforwardpassthroughthenetwork.
- **p. 6 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** We instead usean architecture in which there is a separate output unit for each possible action, and only the state representation is an input to ...
- **p. 7 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** First, we use a technique known as experience replay23 in which we store the agent's experiences at each time-step, et5(st,at, rt,st 1 1), in a ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The outputs correspond to the predicted Q-values of the individual actions for the input state. | joint/task state, reference와 sensor feedback | p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| State/latent | outputs, correspond, predicted, Q-values, individual, actions, input, state, instead, usean, architecture, there | state estimate, task-space error와 control decision | p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 2 (2 6 F E B R U A R Y) |
| Output/action | We instead usean architecture in which there is a separate output unit for each possible action, and only the state representation is an input to the neural network. | torque, force, velocity 또는 position command | p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 2 (2 6 F E B R U A R Y), p. 2 (2 6 F E B R U A R Y) |
| Objective/outcome | This is based on the following intuition: if the optimal value Q s0,a0 ð Þ of the sequence s9 at the next time-step was known for all possible actions a9, thentheoptimalstrategy istoselecttheactiona9 ... | tracking, stability, constraint satisfaction과 contact behavior | p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 7 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |

## Main Claims and Actual Contribution

- **p. 2 / 2 6 F E B R U A R Y - extractive body cue:** Notably, our method was able to train large neural networks using a reinforcementlearningsignalandstochasticgradientdescentinastablemannerillustrated by the temporal evolution of two indices of learning (the agent's average ...
- **p. 2 / 2 6 F E B R U A R Y - extractive body cue:** The input to the neural network consists of an 843 843 4 image produced by the preprocessing map w, followed by three convolutional layers (note: ...
- **p. 3 / V O L - extractive body cue:** Furthermore, we also show that the representations learned by DQN are able to generalize to data generated from policies other than its own-in simulations where ...
- **p. 6 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** The final hidden layer is fully-connected and consists of 512 rectifier units.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Here we use recent advances in training deep neural networks9-11 to develop a novel artificial agent, termed a deep Q-network, that can learnsuccessfulpoliciesdirectlyfromhigh-dimensionalsensoryinputs using end-to-end ...
- **p. 6 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** The human performanceis theaverage rewardachievedfromaround20episodesofeachgamelastingamaximumof5 min each, following around 2 h of practice playing each game.
- **p. 6 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** This had a minimal effect: changing the normalized DQN performance by more than 5% in only six games (Boxing, Breakout, Crazy Climber, Demon Attack, Krull ...
- **p. 7 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** Rectified linear units improve restricted Boltzmann machines.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| Embodiment/environment | Reinforcement learning for robot soccer. | hardware/simulator version and reset protocol | p. 5 (2 6 F E B R U A R Y), p. 5 (2 6 F E B R U A R Y) |
| Dataset/benchmark | The human performanceis theaverage rewardachievedfromaround20episodesofeachgamelastingamaximumof5 min each, following around 2 h of practice playing each game. | role, split, size and leakage | p. 5 (2 6 F E B R U A R Y), p. 5 (2 6 F E B R U A R Y), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| Metric | Clipping the rewards in this manner limits the scale of the error derivatives and makesiteasierto use thesamelearningrateacrossmultiplegames. | definition, denominator, direction and uncertainty | p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 4 (2 6 F E B R U A R Y) |
| Baseline/ablation | The random agent served as a baseline comparison and chose a random action at 10 Hz which is every sixth frame, repeating its last action on intervening frames. | fair input/data/compute/action matching | p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 13 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 4 (2 6 F E B R U A R Y) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 2 6 F E B R U A R Y - extractive body cue:** Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory.
- **p. 6 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** At the same time, it could affect the performance of our agent since it cannot differentiate between rewards of different magnitude.
- **p. 6 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** Thevaluesofallthehyperparametersandoptimizationparameterswereselected by performing an informal search on the games Pong, Breakout, Seaquest, Space Invaders and Beam Rider.
- **p. 9 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** At time point 2, the agent starts moving the paddle towards the ball and the value of the ‘up' action stays high while the value ...
- **p. 7 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** The final term is the variance of the targets, which does not depend on the parameters hi that we are currently optimizing, and may therefore ...
- **p. 7 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** This approach is in some respects limited because the memory buffer does not differentiate important transitions and always overwrites with recent transitions owing to the ...

## Why Read It

Planning and control의 control 문제를 이해하기 위해 읽는다. 본문은 Indeed, in certain games DQN is able to discover a relatively long-term strategy (for example, Breakout: the agent learns the optimal strategy, which is to first dig a tunnel around the side ...를 문제로 두고, Notably, our method was able to train large neural networks using a reinforcementlearningsignalandstochasticgradientdescentinastablemannerillustrated by the temporal evolution of two indices of learning (the agent's average score-per-ep ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 4 (2 6 F E B R U A R Y), p. 2 (2 6 F E B R U A R Y), p. 2 (2 6 F E B R U A R Y), p. 3 (V O L), p. 4 (2 6 F E B R U A R Y), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
