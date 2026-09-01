# Method - Addressing Function Approximation Error in Actor-Critic Methods

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1802.09477; PDF retrieval source: https://arxiv.org/pdf/1802.09477. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 6 (5.3. Target Policy Smoothing Regularization), p. 5 (5.2. Target Networks and Delayed Policy Updates), p. 6 (5.3. Target Policy Smoothing Regularization), p. 5 (5.2. Target Networks and Delayed Policy Updates)): Algorithm 1 TD3 Initialize critic networks Qθ1, Qθ2, and actor network πφ with random parameters θ1, θ2, φ Initialize target networks θ′ 1 ←θ1, θ′ 2 ←θ2, φ′ ←φ Initialize ...

## Method Body Digest

- **p. 6 / 5.3. Target Policy Smoothing Regularization - extractive body cue:** Algorithm 1 TD3 Initialize critic networks Qθ1, Qθ2, and actor network πφ with random parameters θ1, θ2, φ Initialize target networks θ′ 1 ←θ1, θ′ ...
- **p. 5 / 5.2. Target Networks and Delayed Policy Updates - extractive body cue:** If target networks can be used to reduce the error over multiple updates, and policy updates on high-error states cause divergent behavior, then the policy ...
- **p. 6 / 5.3. Target Policy Smoothing Regularization - extractive body cue:** We propose that fitting the value of a small area around the target action y = r + Eϵ [Qθ′(s′, πφ′(s′) + ϵ)] , (13) ...
- **p. 5 / 5.2. Target Networks and Delayed Policy Updates - extractive body cue:** Average estimated value of a randomly selected state on Hopper-v1 without target networks, (τ = 1), and with slowupdating target networks, (τ = 0.1, 0.01), ...
- **p. 5 / 5.2. Target Networks and Delayed Policy Updates - extractive body cue:** As deep function approximators require multiple gradient updates to converge, target networks provide a stable objective in the learning 0.0 0.2 0.4 0.6 0.8 1.0 ...
- **p. 6 / 5.2. Target Networks and Delayed Policy Updates - extractive body cue:** By sufficiently delaying the policy updates we limit the likelihood of repeating updates with respect to an unchanged critic.
- **p. 2 / 3. Background - extractive body cue:** At each discrete time step t, with a given state s ∈S, the agent selects actions a ∈A with respect to its policy π : ...
- **p. 1 / 1. Introduction - extractive body cue:** This favors underestimations, which do not tend to be propagated during learning, as actions with low value estimates are avoided by the policy.

## Design Rationale

- **p. 1 / 1. Introduction - extractive body cue:** Finally, we introduce a novel regularization strategy, where a SARSA-style update bootstraps similar action estimates to further reduce variance.
- **p. 1 / 1. Introduction - extractive body cue:** Second, to address the coupling of value and policy, we propose delaying policy updates until the value estimate has converged.
- **p. 5 / 5.2. Target Networks and Delayed Policy Updates - extractive body cue:** We propose delaying policy updates until the value error is as small as possible.

## Source Evidence Cues

- **p. 6 / 5.3. Target Policy Smoothing Regularization - extractive body cue:** Algorithm 1 TD3 Initialize critic networks Qθ1, Qθ2, and actor network πφ with random parameters θ1, θ2, φ Initialize target networks θ′ 1 ←θ1, θ′ ...
- **p. 5 / 5.2. Target Networks and Delayed Policy Updates - extractive body cue:** If target networks can be used to reduce the error over multiple updates, and policy updates on high-error states cause divergent behavior, then the policy ...
- **p. 6 / 5.3. Target Policy Smoothing Regularization - extractive body cue:** We propose that fitting the value of a small area around the target action y = r + Eϵ [Qθ′(s′, πφ′(s′) + ϵ)] , (13) ...
- **p. 5 / 5.2. Target Networks and Delayed Policy Updates - extractive body cue:** Average estimated value of a randomly selected state on Hopper-v1 without target networks, (τ = 1), and with slowupdating target networks, (τ = 0.1, 0.01), ...
- **Detected method headings:** 5.2. Target Networks and Delayed Policy Updates (p. 5); 5.3. Target Policy Smoothing Regularization (p. 6); C. Convergence results for single-step on-policy (p. 10)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Policy / value representation | state에서 action과 return estimate를 표현한다 | state/observation과 task context | actor, critic, value, Q 또는 sequence policy를 계산 | policy/value estimate | Algorithm 1 TD3 Initialize critic networks Qθ1, Qθ2, and actor network πφ with random parameters θ1, θ2, φ Initialize target networks θ′ ... | p. 6 (5.3. Target Policy Smoothing Regularization), p. 5 (5.2. Target Networks and Delayed Policy Updates) |
| Rollout / target construction | interaction에서 update target을 만든다 | state, action, reward, next state | return, advantage, TD target 또는 trajectory statistics를 구성 | training target | If target networks can be used to reduce the error over multiple updates, and policy updates on high-error states cause divergent behavior, ... | p. 5 (5.2. Target Networks and Delayed Policy Updates), p. 6 (5.3. Target Policy Smoothing Regularization) |
| Policy / value update | 목표를 최적화해 다음 policy를 만든다 | target, replay/data와 parameters | gradient, trust region, entropy, replay 또는 constraint update를 수행 | updated policy/controller | We propose that fitting the value of a small area around the target action y = r + Eϵ [Qθ′(s′, πφ′(s′) + ... | p. 6 (5.3. Target Policy Smoothing Regularization), p. 5 (5.2. Target Networks and Delayed Policy Updates) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 5.2. Target Networks and Delayed Policy Updates - extractive body cue:** As deep function approximators require multiple gradient updates to converge, target networks provide a stable objective in the learning 0.0 0.2 0.4 0.6 0.8 1.0 ...
- **p. 6 / 5.3. Target Policy Smoothing Regularization - extractive body cue:** Algorithm 1 TD3 Initialize critic networks Qθ1, Qθ2, and actor network πφ with random parameters θ1, θ2, φ Initialize target networks θ′ 1 ←θ1, θ′ ...
- **p. 5 / 5.2. Target Networks and Delayed Policy Updates - extractive body cue:** If target networks can be used to reduce the error over multiple updates, and policy updates on high-error states cause divergent behavior, then the policy ...
- **p. 6 / 5.2. Target Networks and Delayed Policy Updates - extractive body cue:** By sufficiently delaying the policy updates we limit the likelihood of repeating updates with respect to an unchanged critic.
- **Formal bridge:** s_t/o_t -> a_t sampled or selected by πθ -> expected return / constrained return -> task return, success and safe execution.
- **Equation/algorithm anchors:** p. 5 (5.2. Target Networks and Delayed Policy Updates), p. 6 (5.3. Target Policy Smoothing Regularization), p. 5 (5.2. Target Networks and Delayed Policy Updates), p. 6 (5.3. Target Policy Smoothing Regularization).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | discrete, time, step, given, state, agent, selects, actions, respect, policy, receiving, reward, environment, Algorithm | state 또는 observation, action, reward와 transition history | body cue; exact tensor/frame verify |
| State/latent | discrete, time, step, given, state, agent, selects, actions, respect, policy | policy/value state와 action-selection variable | body cue; notation verify |
| Action/output | Finally, introduce, novel, regularization, strategy, where, SARSA-style, update, bootstraps, similar | action policy와 induced trajectory | body cue; unit/decoder verify |
| Objective/constraint | deep, function, approximators, require, multiple, gradient, updates, converge, target, networks | expected return / constrained return | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 3. Background - extractive body cue:** At each discrete time step t, with a given state s ∈S, the agent selects actions a ∈A with respect to its policy π : ...
- **p. 6 / 5.3. Target Policy Smoothing Regularization - extractive body cue:** Algorithm 1 TD3 Initialize critic networks Qθ1, Qθ2, and actor network πφ with random parameters θ1, θ2, φ Initialize target networks θ′ 1 ←θ1, θ′ ...
- **p. 6 / 5.3. Target Policy Smoothing Regularization - extractive body cue:** We propose that fitting the value of a small area around the target action y = r + Eϵ [Qθ′(s′, πφ′(s′) + ϵ)] , (13) ...
- **p. 1 / 1. Introduction - extractive body cue:** This favors underestimations, which do not tend to be propagated during learning, as actions with low value estimates are avoided by the policy.
- **p. 1 / 1. Introduction - extractive body cue:** During training, Double DQN estimates the value of the current policy with a separate target value function, allowing actions to be evaluated without maximization bias.
- **p. 2 / 3. Background - extractive body cue:** (1) Qπ(s, a) = Esi∼pπ,ai∼π [Rt/s, a], the expected return when performing action a in state s and following π after, is known as the ...
- **p. 5 / 5.2. Target Networks and Delayed Policy Updates - extractive body cue:** Average estimated value of a randomly selected state on Hopper-v1 without target networks, (τ = 1), and with slowupdating target networks, (τ = 0.1, 0.01), ...
- **Normalized interface:** observation=state 또는 observation, action, reward와 transition history; state=policy/value state와 action-selection variable; output/action=action policy와 induced trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | rollout/return horizon과 episode termination; exact n-step/discount는 exact value not recovered from the selected body cues. | After each time step, the networks are trained with a mini-batch of a 100 transitions, sampled uniformly from a replay buffer containing ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 environment step이 분리되며 deployment control rate는 별도 contract다. | Average return over the last 10 evaluations over 10 trials of 1 million time steps, comparing ablation over delayed policy updates (DP), ... | Hz/fps, inference time and control rate |
| Memory | replay/rollout buffer와 actor/critic parameters; recurrent history 여부 확인 필요. | After each time step, the networks are trained with a mini-batch of a 100 transitions, sampled uniformly from a replay buffer containing ... | window and reset |
| Compute | environment interaction, value/policy update와 batch size가 비용을 결정한다. | Average return over the last 10 evaluations over 10 trials of 1 million time steps, comparing ablation over delayed policy updates (DP), ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 5.2. Target Networks and Delayed Policy Updates - extractive body cue:** Average estimated value of a randomly selected state on Hopper-v1 without target networks, (τ = 1), and with slowupdating target networks, (τ = 0.1, 0.01), ...
- **p. 8 / 6.2. Ablation Studies - extractive body cue:** Although the actor is trained for only half the number of iterations, the inclusion of delayed policy update generally improves performance, while reducing training time.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Algorithm, TD3, Initialize, critic, networks, actor, network, random, parameters, target, replay, buffer, Select, action, exploration, noise, observe, reward, state, Store.
- **Relevant PDF headings:** 5.2. Target Networks and Delayed Policy Updates (p. 5); 5.3. Target Policy Smoothing Regularization (p. 6); C. Convergence results for single-step on-policy (p. 10).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Policy / value representation | Addressing Function Approximation Error in Actor-Critic Methods average reward over 10 episodes with no exploration noise. | p. 8 (6.1. Evaluation), p. 7 (6.1. Evaluation) |
| Rollout / target construction | A full comparison between our re-tuned version and the baselines DDPG is provided in the supplementary material. | p. 8 (6.1. Evaluation), p. 8 (6.2. Ablation Studies) |
| Policy / value update | Method HCheetah Hopper Walker2d Ant TD3 9532.99 3304.75 4565.24 4185.06 DDPG 3162.50 1731.94 1520.90 816.35 AHE 8401.02 1061.77 2362.13 564.07 AHE + ... | p. 8 (6.2. Ablation Studies), p. 8 (6.1. Evaluation) |

## Failure and Ablation Link

- **p. 8 / 6.2. Ablation Studies - extractive body cue:** We additionally compare the effectiveness of the actor-critic variants of Double Q-learning (Van Hasselt, 2010) and Double DQN (Van Hasselt et al., 2016), denoted DQ-AC ...
- **p. 8 / 6.2. Ablation Studies - extractive body cue:** We perform ablation studies to understand the contribution of each individual component: Clipped Double Q-learning (Section 4.2), delayed policy updates (Section 5.2) and target policy ...
- **p. 7 / 6.1. Evaluation - extractive body cue:** To remove the dependency on the initial parameters of the policy we use a purely exploratory policy for the first 10000 time steps of stable ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Measuring overestimation bias in the value estimates of actor critic variants of Double DQN (DDQN-AC) and Double Q- learning (DQ-AC) on MuJoCo environments ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Average estimated value of a randomly selected state on Hopper-v1 without target networks, (τ = 1), and with slow- updating target networks, (τ ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 8. Comparison of TD3 and the Double Q-learning (DQ-AC) and Double DQN (DDQN-AC) actor-critic variants, which also leverage delayed policy updates and target policy ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 7. Ablation over the varying modifications to our DDPG (AHE), comparing the addition of delayed policy updates (AHE + DP), target policy smoothing (AHE ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 6 (5.3. Target Policy Smoothing Regularization), p. 5 (5.2. Target Networks and Delayed Policy Updates), p. 6 (5.3. Target Policy Smoothing Regularization), p. 5 (5.2. Target Networks and Delayed Policy Updates), objective p. 5 (5.2. Target Networks and Delayed Policy Updates), p. 6 (5.3. Target Policy Smoothing Regularization), p. 5 (5.2. Target Networks and Delayed Policy Updates), p. 6 (5.2. Target Networks and Delayed Policy Updates), temporal p. 7 (6.1. Evaluation), p. 8 (6.2. Ablation Studies), p. 2 (2. Related Work), p. 6 (6. Experiments), p. 7 (6.1. Evaluation), p. 4 (4.1. Overestimation Bias in Actor-Critic).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
