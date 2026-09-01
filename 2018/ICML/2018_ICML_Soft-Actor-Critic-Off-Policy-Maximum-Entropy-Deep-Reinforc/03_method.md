# Method - Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v80/haarnoja18b.html; PDF retrieval source: https://arxiv.org/pdf/1801.01290. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (4. From Soft Policy Iteration to Soft), p. 5 (4.2. Soft Actor-Critic), p. 6 (4.2. Soft Actor-Critic), p. 4 (4.2. Soft Actor-Critic), p. 5 (4.2. Soft Actor-Critic), p. 3 (4. From Soft Policy Iteration to Soft)): We will first present this derivation, verify that the corresponding algorithm converges to the optimal policy from its density class, and then present a practical deep reinforcement learning algorithm based ...

## Method Body Digest

- **p. 3 / 4. From Soft Policy Iteration to Soft - extractive body cue:** We will first present this derivation, verify that the corresponding algorithm converges to the optimal policy from its density class, and then present a practical ...
- **p. 5 / 4.2. Soft Actor-Critic - extractive body cue:** Soft Actor-Critic estimated from a single action sample from the current policy without introducing a bias, but in practice, including a separate function approximator for ...
- **p. 6 / 4.2. Soft Actor-Critic - extractive body cue:** The algorithm is agnostic to the parameterization of the policy, as long as it can be evaluated for any arbitrary state-action tuple.
- **p. 4 / 4.2. Soft Actor-Critic - extractive body cue:** For example, the value functions can be modeled as expressive neural networks, and the policy as a Gaussian with mean and covariance given by neural ...
- **p. 5 / 4.2. Soft Actor-Critic - extractive body cue:** To that end, we reparameterize the policy using a neural network transformation at = fφ(ϵt; st), (11) Algorithm 1 Soft Actor-Critic Initialize parameter vectors ψ, ...
- **p. 3 / 4. From Soft Policy Iteration to Soft - extractive body cue:** Actor-Critic Our off-policy soft actor-critic algorithm can be derived starting from a maximum entropy variant of the policy iteration method.
- **p. 4 / 4.2. Soft Actor-Critic - extractive body cue:** We will consider a parameterized state value function Vψ(st), soft Q-function Qθ(st, at), and a tractable policy πφ(at/st).
- **p. 4 / 4.1. Derivation of Soft Policy Iteration - extractive body cue:** Let πold ∈Π and let πnew be the optimizer of the minimization problem defined in Equation 4.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** We present empirical results that show that soft actor-critic attains a substantial improvement in both performance and sample efficiency over both off-policy and on-policy prior ...
- **p. 2 / 1. Introduction - extractive body cue:** We present a convergence proof for policy iteration in the maximum entropy framework, and then introduce a new algorithm based on an approximation to this ...
- **p. 3 / 3.2. Maximum Entropy Reinforcement Learning - extractive body cue:** Though such algorithms have previously been proposed for conventional reinforcement learning, our method is, to our knowledge, the first off-policy actor-critic method in the maximum ...

## Source Evidence Cues

- **p. 3 / 4. From Soft Policy Iteration to Soft - extractive body cue:** We will first present this derivation, verify that the corresponding algorithm converges to the optimal policy from its density class, and then present a practical ...
- **p. 5 / 4.2. Soft Actor-Critic - extractive body cue:** Soft Actor-Critic estimated from a single action sample from the current policy without introducing a bias, but in practice, including a separate function approximator for ...
- **p. 6 / 4.2. Soft Actor-Critic - extractive body cue:** The algorithm is agnostic to the parameterization of the policy, as long as it can be evaluated for any arbitrary state-action tuple.
- **p. 4 / 4.2. Soft Actor-Critic - extractive body cue:** For example, the value functions can be modeled as expressive neural networks, and the policy as a Gaussian with mean and covariance given by neural ...
- **p. 5 / 4.2. Soft Actor-Critic - extractive body cue:** To that end, we reparameterize the policy using a neural network transformation at = fφ(ϵt; st), (11) Algorithm 1 Soft Actor-Critic Initialize parameter vectors ψ, ...
- **p. 3 / 4. From Soft Policy Iteration to Soft - extractive body cue:** Actor-Critic Our off-policy soft actor-critic algorithm can be derived starting from a maximum entropy variant of the policy iteration method.
- **p. 4 / 4.2. Soft Actor-Critic - extractive body cue:** We will consider a parameterized state value function Vψ(st), soft Q-function Qθ(st, at), and a tractable policy πφ(at/st).
- **Detected method headings:** 4. From Soft Policy Iteration to Soft (p. 3); 4.1. Derivation of Soft Policy Iteration (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Policy / value representation | state에서 action과 return estimate를 표현한다 | state/observation과 task context | actor, critic, value, Q 또는 sequence policy를 계산 | policy/value estimate | We will first present this derivation, verify that the corresponding algorithm converges to the optimal policy from its density class, and then ... | p. 3 (4. From Soft Policy Iteration to Soft), p. 5 (4.2. Soft Actor-Critic) |
| Rollout / target construction | interaction에서 update target을 만든다 | state, action, reward, next state | return, advantage, TD target 또는 trajectory statistics를 구성 | training target | Soft Actor-Critic estimated from a single action sample from the current policy without introducing a bias, but in practice, including a separate ... | p. 5 (4.2. Soft Actor-Critic), p. 6 (4.2. Soft Actor-Critic) |
| Policy / value update | 목표를 최적화해 다음 policy를 만든다 | target, replay/data와 parameters | gradient, trust region, entropy, replay 또는 constraint update를 수행 | updated policy/controller | The algorithm is agnostic to the parameterization of the policy, as long as it can be evaluated for any arbitrary state-action tuple. | p. 6 (4.2. Soft Actor-Critic), p. 4 (4.2. Soft Actor-Critic) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 4.1. Derivation of Soft Policy Iteration - extractive body cue:** Let πold ∈Π and let πnew be the optimizer of the minimization problem defined in Equation 4.
- **p. 5 / 4.2. Soft Actor-Critic - extractive body cue:** The soft Q-function parameters can be trained to minimize the soft Bellman residual JQ(θ) = E(st,at)∼D 1 2  Qθ(st, at) -ˆQ(st, at) 2 , ...
- **p. 4 / 4.1. Derivation of Soft Policy Iteration - extractive body cue:** For this projection, we can show that the new, projected policy has a higher value than the old policy with respect to the objective in ...
- **p. 5 / 4.2. Soft Actor-Critic - extractive body cue:** Finally, the policy parameters can be learned by directly minimizing the expected KL-divergence in Equation 4: Jπ(φ) = Est∼D  DKL  πφ( · /st)
- **p. 6 / 4.2. Soft Actor-Critic - extractive body cue:** Soft Actor-Critic 0.0 0.2 0.4 0.6 0.8 1.0 million steps 0 1000 2000 3000 4000 average return (a) Hopper-v1 0.0 0.2 0.4 0.6 0.8 1.0 ...
- **Formal bridge:** s_t/o_t -> a_t sampled or selected by πθ -> expected return / constrained return -> task return, success and safe execution.
- **Equation/algorithm anchors:** p. 4 (4.1. Derivation of Soft Policy Iteration), p. 4 (4.1. Derivation of Soft Policy Iteration), p. 5 (4.2. Soft Actor-Critic), p. 5 (4.2. Soft Actor-Critic).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | will, denote, state, state-action, marginals, trajectory, distribution, induced, policy, at/st, algorithm, agnostic, parameterization, long | state 또는 observation, action, reward와 transition history | body cue; exact tensor/frame verify |
| State/latent | will, denote, state, state-action, marginals, trajectory, distribution, induced, policy, at/st | policy/value state와 action-selection variable | body cue; notation verify |
| Action/output | present, empirical, soft, actor-critic, attains, substantial, improvement, performance, sample, efficiency | action policy와 induced trajectory | body cue; unit/decoder verify |
| Objective/constraint | Let, optimizer, minimization, problem, defined, Equation, soft, Q-function, parameters, trained | expected return / constrained return | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Notation - extractive body cue:** We will use ρπ(st) and ρπ(st, at) to denote the state and state-action marginals of the trajectory distribution induced by a policy π(at/st).
- **p. 6 / 4.2. Soft Actor-Critic - extractive body cue:** The algorithm is agnostic to the parameterization of the policy, as long as it can be evaluated for any arbitrary state-action tuple.
- **p. 3 / 3.1. Notation - extractive body cue:** We address policy learning in continuous action spaces.
- **p. 1 / 1. Introduction - extractive body cue:** We explore how to design an efficient and stable modelfree deep RL algorithm for continuous state and action spaces.
- **p. 1 / 1. Introduction - extractive body cue:** This challenge is further exacerbated in continuous state and action spaces, where a separate actor network is often used to perform the maximization in Q-learning.
- **p. 2 / 1. Introduction - extractive body cue:** However, the on-policy variants suffer from poor sample complexity for the reasons discussed above, while the off-policy variants require complex approximate inference procedures in continuous ...
- **p. 2 / 1. Introduction - extractive body cue:** This algorithm extends readily to very complex, high-dimensional tasks, such as the Humanoid benchmark (Duan et al., 2016) with 21 action dimensions, where off-policy methods ...
- **Normalized interface:** observation=state 또는 observation, action, reward와 transition history; state=policy/value state와 action-selection variable; output/action=action policy와 induced trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | rollout/return horizon과 episode termination; exact n-step/discount는 exact value not recovered from the selected body cues. | We train five different instances of each algorithm with different random seeds, with each performing one evaluation rollout every 1000 environment steps. | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 environment step이 분리되며 deployment control rate는 별도 contract다. | The source code of our SAC implementation1 and videos2 are available online. | Hz/fps, inference time and control rate |
| Memory | replay/rollout buffer와 actor/critic parameters; recurrent history 여부 확인 필요. | not recovered | window and reset |
| Compute | environment interaction, value/policy update와 batch size가 비용을 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4.2. Soft Actor-Critic - extractive body cue:** Soft Actor-Critic estimated from a single action sample from the current policy without introducing a bias, but in practice, including a separate function approximator for ...
- **p. 6 / 5. Experiments - extractive body cue:** The source code of our SAC implementation1 and videos2 are available online.
- **p. 7 / 5.1. Comparative Evaluation - extractive body cue:** We train five different instances of each algorithm with different random seeds, with each performing one evaluation rollout every 1000 environment steps.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** will, first, present, derivation, verify, corresponding, algorithm, converges, optimal, policy, density, class, then, practical, deep, reinforcement, learning, theory, Soft, Actor-Critic.
- **Relevant PDF headings:** 4. From Soft Policy Iteration to Soft (p. 3); 4.1. Derivation of Soft Policy Iteration (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Policy / value representation | We compare our method to prior techniques on a range of challenging continuous control tasks from the OpenAI gym benchmark suite (Brockman ... | p. 6 (5. Experiments), p. 6 (5. Experiments) |
| Rollout / target construction | The results show that, overall, SAC performs comparably to the baseline methods on the easier tasks and outperforms them on the harder ... | p. 7 (5.1. Comparative Evaluation), p. 7 (5.2. Ablation Study) |
| Policy / value update | The stability of the algorithm also plays a large role in performance: easier tasks make it more practical to tune hyperparameters to ... | p. 6 (5. Experiments), p. 7 (5.1. Comparative Evaluation) |

## Failure and Ablation Link

- **p. 14 / Figure/Table caption - extractive body cue:** Figure 4. Training curves for additional baseline (Trust-PCL) and for two SAC variants. Soft actor-critic with hard target update (blue) differs from standard SAC in ...
- **p. 6 / 5. Experiments - extractive body cue:** We have included trust region path consistency learning (Trust-PCL) (Nachum et al., 2017b) and two other variants of SAC in Appendix E.
- **p. 7 / 5.2. Ablation Study - extractive body cue:** Comparison of SAC (blue) and a deterministic variant of SAC (red) in terms of the stability of individual random seeds on the Humanoid (rllab) benchmark.
- **p. 7 / 5.2. Ablation Study - extractive body cue:** Soft actor-critic performs much more consistently, while the deterministic variant exhibits very high variability across seeds, indicating substantially worse stability.
- **p. 8 / 5.2. Ablation Study - extractive body cue:** Sensitivity of soft actor-critic to selected hyperparameters on Ant-v1 task.
- **p. 8 / 5.2. Ablation Study - extractive body cue:** We found this variant to benefit from taking more than one gradient step between the environment steps, which can improve performance but also increases the ...
- **p. 8 / 6. Conclusion - extractive body cue:** Our results suggest that stochastic, entropy maximizing reinforcement learning algorithms can provide a promising avenue for improved robustness and stability, and further exploration of maximum ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (4. From Soft Policy Iteration to Soft), p. 5 (4.2. Soft Actor-Critic), p. 6 (4.2. Soft Actor-Critic), p. 4 (4.2. Soft Actor-Critic), p. 5 (4.2. Soft Actor-Critic), p. 3 (4. From Soft Policy Iteration to Soft), objective p. 4 (4.1. Derivation of Soft Policy Iteration), p. 5 (4.2. Soft Actor-Critic), p. 4 (4.1. Derivation of Soft Policy Iteration), p. 5 (4.2. Soft Actor-Critic), p. 6 (4.2. Soft Actor-Critic), temporal p. 7 (5.1. Comparative Evaluation), p. 6 (5. Experiments), p. 6 (5. Experiments), p. 7 (5.1. Comparative Evaluation), p. 8 (5.2. Ablation Study), p. 8 (5.2. Ablation Study).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
