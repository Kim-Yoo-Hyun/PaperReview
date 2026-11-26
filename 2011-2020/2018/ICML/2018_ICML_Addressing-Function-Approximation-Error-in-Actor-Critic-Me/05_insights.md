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

- **Paper-specific interface:** We propose that fitting the value of a small area around the target action y = r + Eϵ [Qθ′(s′, πφ′(s′) + ϵ)] , (13) would have the benefit of ... (p. 6, 5.3. Target Policy Smoothing Regularization).
- **Paper-specific mechanism:** Finally, we introduce a novel regularization strategy, where a SARSA-style update bootstraps similar action estimates to further reduce variance. (p. 1, 1. Introduction).
- **Evidence boundary:** the reported outcome is While a larger d would result in a larger benefit with respect to accumulating errors, for fair comparison, the critics are only trained once per time step, and training the ... (p. 7, 6.1. Evaluation); the relevant task/metric cue is We present the Twin Delayed Deep Deterministic policy gradient algorithm (TD3), which builds on the Deep Deterministic Policy Gradient algorithm (DDPG) (Lillicrap et al., 2015) by applying the modifications described ... (p. 6, 6. Experiments). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** For transitions where the episode terminates by reaching some failure state, and not due to the episode running until the max horizon, the value of Q(s, ·) is set to ... (p. 14, 4. Q values are stored in a lookup table).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Reinforcement Learning, continuous control, actor-critic`.
- **Reading predecessor in the generated track queue:** Continuous Control with Deep Reinforcement Learning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Hindsight Experience Replay (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Due to the connection between noise and overestimation, we examine the accumulation of errors from temporal difference learning.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: We propose that fitting the value of a small area around the target action y = r + Eϵ [Qθ′(s′, πφ′(s′) + ϵ)] , (13) would have the benefit of ... (p. 6, 5.3. Target Policy Smoothing Regularization); preserve the objective/update rule: To ensure the TD-error remains small, we update the (p. 5, 5.2. Target Networks and Delayed Policy Updates).
2. Use the paper-reported task/data/environment cue: (2016) with no modifications to the environment or reward. (p. 7, 6.1. Evaluation).
3. Compare against the reported or matched baseline: A full comparison between our re-tuned version and the baselines DDPG is provided in the supplementary material. (p. 8, 6.1. Evaluation).
4. Report the body metric with its denominator and aggregation: We present the Twin Delayed Deep Deterministic policy gradient algorithm (TD3), which builds on the Deep Deterministic Policy Gradient algorithm (DDPG) (Lillicrap et al., 2015) by applying the modifications described ... (p. 6, 6. Experiments).
5. Re-run the reported ablation or stress/failure condition: To remove the dependency on the initial parameters of the policy we use a purely exploratory policy for the first 10000 time steps of stable length environments (HalfCheetah-v1 and Ant-v1) ... (p. 7, 6.1. Evaluation); if none is reported, design one around: For transitions where the episode terminates by reaching some failure state, and not due to the episode running until the max horizon, the value of Q(s, ·) is set to ... (p. 14, 4. Q values are stored in a lookup table).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (1. Introduction), p. 1 (1. Introduction), match the reported outcome at p. 7 (6.1. Evaluation), p. 8 (6.2. Ablation Studies), p. 6 (6. Experiments), and measure the boundary at p. 14 (4. Q values are stored in a lookup table), p. 6 (5.3. Target Policy Smoothing Regularization).

## Falsifiable research question

Under the paper's stated interface (We propose that fitting the value of a small area around the target action y = r + Eϵ [Qθ′(s′, πφ′(s′) + ...), does the paper-specific mechanism (Finally, we introduce a novel regularization strategy, where a SARSA-style update bootstraps similar action estimates to further reduce variance.) retain the reported evaluation outcome (We present the Twin Delayed Deep Deterministic policy gradient algorithm (TD3), which builds on the Deep Deterministic Policy ...) when tested against the paper's strongest explicit boundary (For transitions where the episode terminates by reaching some failure state, and not due to the episode running ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (We present the Twin Delayed Deep Deterministic policy gradient algorithm (TD3), which builds on the Deep Deterministic Policy ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Finally, we introduce a novel regularization strategy, where a SARSA-style update bootstraps similar action estimates to further reduce variance. (p. 1, 1. Introduction).
- **Paper-supported outcome:** While a larger d would result in a larger benefit with respect to accumulating errors, for fair comparison, the critics are only trained once per time step, and training the ... (p. 7, 6.1. Evaluation).
- **Strongest explicit boundary:** For transitions where the episode terminates by reaching some failure state, and not due to the episode running until the max horizon, the value of Q(s, ·) is set to ... (p. 14, 4. Q values are stored in a lookup table).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
