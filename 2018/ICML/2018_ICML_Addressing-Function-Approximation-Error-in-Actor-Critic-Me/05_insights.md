# Insights — Addressing Function Approximation Error in Actor-Critic Methods

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1802.09477; PDF retrieval source: https://arxiv.org/pdf/1802.09477. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1. Introduction - extractive body cue:** Finally, we introduce a novel regularization strategy, where a SARSA-style update bootstraps similar action estimates to further reduce variance.
- **p. 1 / 1. Introduction - extractive body cue:** Second, to address the coupling of value and policy, we propose delaying policy updates until the value estimate has converged.
- **p. 5 / 5.2. Target Networks and Delayed Policy Updates - extractive body cue:** We propose delaying policy updates until the value error is as small as possible.
- **p. 6 / 5.3. Target Policy Smoothing Regularization - extractive body cue:** We introduce a regularization strategy for deep value learning, target policy smoothing, which mimics the learning update from SARSA (Sutton & Barto, 1998).
- **p. 6 / 5.3. Target Policy Smoothing Regularization - extractive body cue:** We propose that fitting the value of a small area around the target action y = r + Eϵ [Qθ′(s′, πφ′(s′) + ϵ)] , (13) ...
- **p. 6 / 5.3. Target Policy Smoothing Regularization - extractive body cue:** Algorithm 1 TD3 Initialize critic networks Qθ1, Qθ2, and actor network πφ with random parameters θ1, θ2, φ Initialize target networks θ′ 1 ←θ1, θ′ ...
- **p. 5 / 5.2. Target Networks and Delayed Policy Updates - extractive body cue:** If target networks can be used to reduce the error over multiple updates, and policy updates on high-error states cause divergent behavior, then the policy ...
- **Contribution anchor:** p. 1 (1. Introduction), p. 1 (1. Introduction), p. 5 (5.2. Target Networks and Delayed Policy Updates), p. 6 (5.3. Target Policy Smoothing Regularization), p. 6 (5.3. Target Policy Smoothing Regularization), p. 6 (5.3. Target Policy Smoothing Regularization)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** Our proposed method addresses these issues, and greatly outperforms the current state of the art.
- **p. 1 / 1. Introduction - extractive body cue:** In reinforcement learning problems with discrete action spaces, the issue of value overestimation as a result of function approximation errors is well-studied.
- **p. 2 / 3. Background - extractive body cue:** The return is defined as the discounted sum of rewards Rt = PT i=t γi-tr(si, ai), where γ is a discount factor determining the priority ...
- **p. 3 / 3. Background - extractive body cue:** The weights of a target network are either updated periodically to exactly match the weights of the current network, or by some proportion τ at ...
- **p. 8 / 7. Conclusion - extractive body cue:** Due to the connection between noise and overestimation, we examine the accumulation of errors from temporal difference learning.
- **p. 7 / 6.1. Evaluation - extractive body cue:** Afterwards, we use an off-policy exploration strategy, adding Gaussian noise N(0, 0.1) to each action.
- **p. 7 / 6.1. Evaluation - extractive body cue:** Unlike the original implementation of DDPG, we used uncorrelated noise for exploration as we found noise drawn from the Ornstein-Uhlenbeck (Uhlenbeck & Ornstein, 1930) process ...
- **Boundary to test:** Due to the connection between noise and overestimation, we examine the accumulation of errors from temporal difference learning.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Finally, we introduce a novel regularization strategy, where a SARSA-style update bootstraps similar action estimates to further reduce variance. | p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Reported outcome | Method HCheetah Hopper Walker2d Ant TD3 9532.99 3304.75 4565.24 4185.06 DDPG 3162.50 1731.94 1520.90 816.35 AHE 8401.02 1061.77 2362.13 564.07 AHE + DP 7588.64 1465.11 2459.53 896.13 AHE + TPS 9023.40 907.56 ... | p. 8 (6.2. Ablation Studies), p. 8 (6.1. Evaluation) |
| Failure/limitation | Due to the connection between noise and overestimation, we examine the accumulation of errors from temporal difference learning. | p. 8 (7. Conclusion), p. 7 (6.1. Evaluation) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `state 또는 observation, action, reward와 transition history → policy/value state와 action-selection variable → action policy와 induced trajectory`.
- 이 논문의 재사용 가능한 지점은 At each discrete time step t, with a given state s ∈S, the agent selects actions a ∈A with respect to its policy π : S →A, receiving a reward r and ...를 Algorithm 1 TD3 Initialize critic networks Qθ1, Qθ2, and actor network πφ with random parameters θ1, θ2, φ Initialize target networks θ′ 1 ←θ1, θ′ 2 ←θ2, φ′ ←φ Initialize replay buffer ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 policy/value state와 action-selection variable가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Due to the connection between noise and overestimation, we examine the accumulation of errors from temporal difference learning.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Finally, we introduce a novel regularization strategy, where a SARSA-style update bootstraps similar action estimates to further reduce variance.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Reinforcement Learning, continuous control, actor-critic`.
- **Reading predecessor in the generated track queue:** Continuous Control with Deep Reinforcement Learning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Hindsight Experience Replay (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Due to the connection between noise and overestimation, we examine the accumulation of errors from temporal difference learning.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Addressing Function Approximation Error in Actor-Critic Methods average reward over 10 episodes with no exploration noise..
3. Compare against the body-reported baseline or a matched simpler baseline: A full comparison between our re-tuned version and the baselines DDPG is provided in the supplementary material..
4. Report the body metric and its denominator/aggregation: Addressing Function Approximation Error in Actor-Critic Methods average reward over 10 episodes with no exploration noise..
5. Re-run the body-reported ablation/failure condition: We additionally compare the effectiveness of the actor-critic variants of Double Q-learning (Van Hasselt, 2010) and Double DQN (Van Hasselt et al., 2016), denoted DQ-AC and DDQN-AC respectively, in Table 2..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 6 (5.3. Target Policy Smoothing Regularization), p. 5 (5.2. Target Networks and Delayed Policy Updates), p. 6 (5.3. Target Policy Smoothing Regularization); the primary result is directionally consistent at p. 8 (6.2. Ablation Studies), p. 8 (6.1. Evaluation), p. 6 (6. Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Finally, introduce, novel mechanism이 A full comparison between our re-tuned version and the baselines DDPG is provided in the supplementary ... 대비 Addressing Function Approximation Error in Actor-Critic Methods average reward over 10 episodes with no exploration noise.을 개선하고, Due to the connection between noise and overestimation, we examine the accumulation of errors from temporal ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
