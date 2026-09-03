# Insights — Human-level control through deep reinforcement learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1038/nature14236; PDF retrieval source: https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 2 6 F E B R U A R Y - extractive body cue:** Notably, our method was able to train large neural networks using a reinforcementlearningsignalandstochasticgradientdescentinastablemannerillustrated by the temporal evolution of two indices of learning (the agent's average ...
- **p. 2 / 2 6 F E B R U A R Y - extractive body cue:** The input to the neural network consists of an 843 843 4 image produced by the preprocessing map w, followed by three convolutional layers (note: ...
- **p. 3 / V O L - extractive body cue:** Furthermore, we also show that the representations learned by DQN are able to generalize to data generated from policies other than its own-in simulations where ...
- **p. 6 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** The final hidden layer is fully-connected and consists of 512 rectifier units.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Here we use recent advances in training deep neural networks9-11 to develop a novel artificial agent, termed a deep Q-network, that can learnsuccessfulpoliciesdirectlyfromhigh-dimensionalsensoryinputs using end-to-end ...
- **p. 6 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** The main advantageof this type of architecture is the ability tocompute Q-valuesforall possibleactionsinagivenstatewithonlyasingleforwardpassthroughthenetwork.
- **p. 6 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** We instead usean architecture in which there is a separate output unit for each possible action, and only the state representation is an input to ...
- **Contribution anchor:** p. 2 (2 6 F E B R U A R Y), p. 2 (2 6 F E B R U A R Y), p. 3 (V O L), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 1 (Body text (section not recovered)), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess)

### Strongest assumption and failure boundary

- **p. 4 / 2 6 F E B R U A R Y - extractive body cue:** Indeed, in certain games DQN is able to discover a relatively long-term strategy (for example, Breakout: the agent learns the optimal strategy, which is to ...
- **p. 2 / 2 6 F E B R U A R Y - extractive body cue:** difficult and engaging for human players.
- **p. 2 / 2 6 F E B R U A R Y - extractive body cue:** Our DQN method outperforms the best existing reinforcement learning methods on 43 of the games without incorporating any of the additional prior knowledge about Atari ...
- **p. 3 / V O L - extractive body cue:** Furthermore, we also show that the representations learned by DQN are able to generalize to data generated from policies other than its own-in simulations where ...
- **p. 4 / 2 6 F E B R U A R Y - extractive body cue:** In the future, it will be important to explore the potential use of biasing the content of experience replay towards salient events, a phenomenon that ...
- **p. 5 / 2 6 F E B R U A R Y - extractive body cue:** Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory.
- **p. 6 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** At the same time, it could affect the performance of our agent since it cannot differentiate between rewards of different magnitude.
- **Boundary to test:** Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Notably, our method was able to train large neural networks using a reinforcementlearningsignalandstochasticgradientdescentinastablemannerillustrated by the temporal evolution of two indices of learning (the agent's average score-per-ep ... | p. 2 (2 6 F E B R U A R Y), p. 2 (2 6 F E B R U A R Y) |
| Reported outcome | The human performanceis theaverage rewardachievedfromaround20episodesofeachgamelastingamaximumof5 min each, following around 2 h of practice playing each game. | p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| Failure/limitation | Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory. | p. 5 (2 6 F E B R U A R Y), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `joint/task state, reference와 sensor feedback → state estimate, task-space error와 control decision → torque, force, velocity 또는 position command`.
- 이 논문의 재사용 가능한 지점은 The outputs correspond to the predicted Q-values of the individual actions for the input state.를 We instead usean architecture in which there is a separate output unit for each possible action, and only the state representation is an input to the neural network.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 state estimate, task-space error와 control decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Notably, our method was able to train large neural networks using a reinforcementlearningsignalandstochasticgradientdescentinastablemannerillustrated by the temporal evolution of two indices of learning (the agent's average score-per-ep ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Planning and control`; tags: `Robotics, Reinforcement Learning, Deep Q-Network, Value Learning`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Reinforcement learning for robot soccer..
3. Compare against the body-reported baseline or a matched simpler baseline: The random agent served as a baseline comparison and chose a random action at 10 Hz which is every sixth frame, repeating its last action on intervening frames..
4. Report the body metric and its denominator/aggregation: Clipping the rewards in this manner limits the scale of the error derivatives and makesiteasierto use thesamelearningrateacrossmultiplegames..
5. Re-run the body-reported ablation/failure condition: Because running the emulator forward for one step requires much less computationthan having the agent select an action, this technique allows the agent to play roughly k times more games without significantly ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 7 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess); the primary result is directionally consistent at p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 7 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Notably, able, train mechanism이 The random agent served as a baseline comparison and chose a random action at 10 Hz ... 대비 Clipping the rewards in this manner limits the scale of the error derivatives and makesiteasierto use thesamelearningrateacrossmultiplegames.을 개선하고, Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
