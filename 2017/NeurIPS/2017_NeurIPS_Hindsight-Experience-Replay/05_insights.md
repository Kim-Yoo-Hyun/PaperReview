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

- **Closed-loop position:** `state 또는 observation, action, reward와 transition history → policy/value state와 action-selection variable → action policy와 induced trajectory`.
- 이 논문의 재사용 가능한 지점은 A deterministic policy is a mapping from states to actions: π : S →A.를 (2015a) show that in this setup it is possible to train an approximator to the Q-function using direct bootstrapping from the Bellman equation (just like in case of DQN) and that a ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 policy/value state와 action-selection variable가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 In this task a puck is placed on a long slippery table and the target position is outside of the robot's reach so that it has to hit the puck with such ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this paper we introduce a technique called Hindsight Experience Replay (HER) which allows the algorithm to perform exactly this kind of reasoning and can be combined with any off-policy RL algorithm.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Reinforcement Learning, goal-conditioned RL, sparse rewards`.
- **Reading predecessor in the generated track queue:** Addressing Function Approximation Error in Actor-Critic Methods (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Constrained Policy Optimization (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In this task a puck is placed on a long slippery table and the target position is outside of the robot's reach so that it has to hit the puck with such ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We decided to use manipulation environments based on an existing hardware robot to ensure that the challenges we face correspond as closely as possible to the real world..
3. Compare against the body-reported baseline or a matched simpler baseline: 4.2 we compare the performance of DDPG with and without HER..
4. Report the body metric and its denominator/aggregation: 0 50 100 150 200 0% 20% 40% 60% 80% 100% success rate pushing DDPG DDPG+HER 0 50 100 150 200 epoch number (every epoch = 800 episodes = 800x50 timesteps) 0% ....
5. Re-run the body-reported ablation/failure condition: In this section we check how the performance of DDPG with and without HER changes if we replace this reward with one which is shaped..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (2 Background), p. 2 (2 Background), p. 2 (1 Introduction); the primary result is directionally consistent at p. 5 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 introduce, technique, called mechanism이 4.2 we compare the performance of DDPG with and without HER. 대비 0 50 100 150 200 0% 20% 40% 60% 80% 100% success rate pushing DDPG DDPG+HER 0 50 ...을 개선하고, In this task a puck is placed on a long slippery table and the target position ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
