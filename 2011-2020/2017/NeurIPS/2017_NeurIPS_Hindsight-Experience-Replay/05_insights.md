# Insights — Hindsight Experience Replay

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1707.01495; PDF retrieval source: https://arxiv.org/pdf/1707.01495. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** In this paper we introduce a technique called Hindsight Experience Replay (HER) which allows the algorithm to perform exactly this kind of reasoning and can ...
- **p. 1 / Abstract - extractive body cue:** We present a novel technique called Hindsight Experience Replay which allows sample-efficient learning from rewards which are sparse and binary and therefore avoid the need ...
- **p. 4 / 2 Background - extractive body cue:** In order to solve this problem we introduce the technique of Hindsight Experience Replay which is the crux of our approach.
- **p. 2 / 2 Background - extractive body cue:** In this section we introduce reinforcement learning formalism used in the paper as well as RL algorithms we use in our experiments.
- **p. 3 / 2 Background - extractive body cue:** Instead of shaping the reward we propose a different solution which does not require any domain knowledge.
- **p. 4 / 2 Background - extractive body cue:** Notice that the goal being pursued influences the agent's actions but not the environment dynamics and therefore we can replay each trajectory with an arbitrary ...
- **p. 3 / 2 Background - extractive body cue:** 2.3 Deep Deterministic Policy Gradients (DDPG) Deep Deterministic Policy Gradients (DDPG) (Lillicrap et al., 2015) is a model-free RL algorithm for continuous action spaces.
- **Contribution anchor:** p. 2 (1 Introduction), p. 1 (Abstract), p. 4 (2 Background), p. 2 (2 Background), p. 3 (2 Background), p. 4 (2 Background)

### Strongest assumption and failure boundary

- **p. 5 / 2 Background - extractive body cue:** These results are indicative of the practical challenges with reward shaping, and that shaped rewards would often constitute a compromise on the metric we truly ...
- **p. 1 / 1 Introduction - extractive body cue:** However, a common challenge, especially for robotics, is the need to engineer a reward function that not only reflects the task at hand but is ...
- **p. 3 / 2 Background - extractive body cue:** While using a shaped reward solves the problem in our toy environment, it may be difficult to apply to more complicated problems.
- **p. 3 / 2 Background - extractive body cue:** VIME (Houthooft et al., 2016), count-based exploration (Ostrovski et al., 2017) or bootstrapped DQN (Osband et al., 2016)) does not help here because the real ...
- **p. 1 / 1 Introduction - extractive body cue:** Reinforcement learning (RL) combined with neural networks has recently led to a wide range of successes in learning policies for sequential decision-making problems.
- **p. 6 / 4 Experiments - extractive body cue:** In this task a puck is placed on a long slippery table and the target position is outside of the robot's reach so that it ...
- **p. 10 / 5 Related work - extractive body cue:** It does not have to be robust to noisy observations because it is not used during the deployment on the physical robot.
- **Boundary to test:** In this task a puck is placed on a long slippery table and the target position is outside of the robot's reach so that it has to hit the puck with such ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this paper we introduce a technique called Hindsight Experience Replay (HER) which allows the algorithm to perform exactly this kind of reasoning and can be combined with any off-policy RL algorithm. | p. 2 (1 Introduction), p. 1 (Abstract) |
| Reported outcome | 4.3 we check if HER improves performance in the single-goal setup. | p. 5 (4 Experiments), p. 7 (4 Experiments) |
| Failure/limitation | In this task a puck is placed on a long slippery table and the target position is outside of the robot's reach so that it has to hit the puck with such ... | p. 6 (4 Experiments), p. 10 (5 Related work) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** A deterministic policy is a mapping from states to actions: π : S →A. (p. 2, 2 Background).
- **Paper-specific mechanism:** In this paper we introduce a technique called Hindsight Experience Replay (HER) which allows the algorithm to perform exactly this kind of reasoning and can be combined with any off-policy ... (p. 2, 1 Introduction).
- **Evidence boundary:** the reported outcome is 4.6 we show the results of the experiments on the physical robot. (p. 5, 4 Experiments); the relevant task/metric cue is 0 50 100 150 200 0% 20% 40% 60% 80% 100% success rate pushing DDPG DDPG+HER 0 50 100 150 200 epoch number (every epoch = 800 episodes = 800x50 ... (p. 9, 4 Experiments). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** These results are indicative of the practical challenges with reward shaping, and that shaped rewards would often constitute a compromise on the metric we truly care about (such as binary ... (p. 5, 2 Background).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Reinforcement Learning, goal-conditioned RL, sparse rewards`.
- **Reading predecessor in the generated track queue:** Addressing Function Approximation Error in Actor-Critic Methods (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Constrained Policy Optimization (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In this task a puck is placed on a long slippery table and the target position is outside of the robot's reach so that it has to hit the puck with such ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: A deterministic policy is a mapping from states to actions: π : S →A. (p. 2, 2 Background); preserve the objective/update rule: The network is trained using mini-batch gradient descent on the loss L which encourages the approximated Q-function to satisfy the Bellman equation: L = E (Q(st, at) -yt)2, where yt ... (p. 2, 2 Background).
2. Use the paper-reported task/data/environment cue: We decided to use manipulation environments based on an existing hardware robot to ensure that the challenges we face correspond as closely as possible to the real world. (p. 5, 4 Experiments).
3. Compare against the reported or matched baseline: 4.2 we compare the performance of DDPG with and without HER. (p. 5, 4 Experiments).
4. Report the body metric with its denominator and aggregation: 0 50 100 150 200 0% 20% 40% 60% 80% 100% success rate pushing DDPG DDPG+HER 0 50 100 150 200 epoch number (every epoch = 800 episodes = 800x50 ... (p. 9, 4 Experiments).
5. Re-run the reported ablation or stress/failure condition: In this section we check how the performance of DDPG with and without HER changes if we replace this reward with one which is shaped. (p. 8, 4 Experiments); if none is reported, design one around: These results are indicative of the practical challenges with reward shaping, and that shaped rewards would often constitute a compromise on the metric we truly care about (such as binary ... (p. 5, 2 Background).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1 Introduction), p. 1 (Abstract), match the reported outcome at p. 5 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), and measure the boundary at p. 5 (2 Background), p. 6 (4 Experiments).

## Falsifiable research question

Under the paper's stated interface (A deterministic policy is a mapping from states to actions: π : S →A.), does the paper-specific mechanism (In this paper we introduce a technique called Hindsight Experience Replay (HER) which allows the algorithm to perform exactly this kind of ...) retain the reported evaluation outcome (0 50 100 150 200 0% 20% 40% 60% 80% 100% success rate pushing DDPG DDPG+HER 0 50 ...) when tested against the paper's strongest explicit boundary (These results are indicative of the practical challenges with reward shaping, and that shaped rewards would often constitute ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (0 50 100 150 200 0% 20% 40% 60% 80% 100% success rate pushing DDPG DDPG+HER 0 50 ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In this paper we introduce a technique called Hindsight Experience Replay (HER) which allows the algorithm to perform exactly this kind of reasoning and can be combined with any off-policy ... (p. 2, 1 Introduction).
- **Paper-supported outcome:** 4.6 we show the results of the experiments on the physical robot. (p. 5, 4 Experiments).
- **Strongest explicit boundary:** These results are indicative of the practical challenges with reward shaping, and that shaped rewards would often constitute a compromise on the metric we truly care about (such as binary ... (p. 5, 2 Background).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
