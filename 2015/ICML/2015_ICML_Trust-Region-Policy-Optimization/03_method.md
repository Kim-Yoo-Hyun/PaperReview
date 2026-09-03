# Method - Trust Region Policy Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v37/schulman15.html; PDF retrieval source: https://arxiv.org/pdf/1502.05477. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization), p. 6 (3. Approximately solve this constrained optimization), p. 6 (3. Approximately solve this constrained optimization)): We use the conjugate gradient algorithm followed by a line search, which is altogether only slightly more expensive than computing the gradient itself.

## Method Body Digest

- **p. 5 / 3. Approximately solve this constrained optimization - extractive body cue:** We use the conjugate gradient algorithm followed by a line search, which is altogether only slightly more expensive than computing the gradient itself.
- **p. 5 / 3. Approximately solve this constrained optimization - extractive body cue:** Empirically, it is hard to robustly choose the penalty coefficient, so we use a hard constraint instead of a penalty, with parameter δ (the bound ...
- **p. 6 / 3. Approximately solve this constrained optimization - extractive body cue:** Relative entropy policy search (REPS) (Peters et al., 2010) constrains the state-action marginals p(s, a), while TRPO constrains the conditionals p(a/s).
- **p. 6 / 3. Approximately solve this constrained optimization - extractive body cue:** Levine and Abbeel (2014) also use a KL divergence constraint, but its purpose is to encourage the policy not to stray from regions where the ...
- **p. 6 / 3. Approximately solve this constrained optimization - extractive body cue:** The natural policy gradient (Kakade, 2002) can be obtained as a special case of the update in Equation (12) by using a linear approximation to ...
- **p. 6 / 3. Approximately solve this constrained optimization - extractive body cue:** We can also obtain the standard policy gradient update by using an ℓ2 constraint or penalty: maximize θ h ∇θLθold(θ)
- **p. 5 / 3. Approximately solve this constrained optimization - extractive body cue:** Let us briefly summarize the relationship between the theory from Section 3 and the practical algorithm we have described: • The theory justifies optimizing a ...
- **p. 2 / 2 Preliminaries - extractive body cue:** This implies the classic result that the update performed by exact policy iteration, which uses the deterministic policy ˜π(s) = arg maxa Aπ(s, a), improves ...

## Design Rationale

- **p. 2 / 2 Preliminaries - extractive body cue:** Instead, we introduce the following local approximation to η: Lπ(˜π) = η(π) + X s ρπ(s) X a ˜π(a/s)Aπ(s, a).
- **p. 3 / 2 Preliminaries - extractive body cue:** Trust region policy optimization, which we propose in the following section, is an approximation to Algorithm 1, which uses a constraint on the KL divergence ...
- **p. 5 / 2 Preliminaries - extractive body cue:** 6 Practical Algorithm Here we present two practical policy optimization algorithm based on the ideas above, which use either the single path or vine sampling ...

## Source Evidence Cues

- **p. 5 / 3. Approximately solve this constrained optimization - extractive body cue:** We use the conjugate gradient algorithm followed by a line search, which is altogether only slightly more expensive than computing the gradient itself.
- **p. 5 / 3. Approximately solve this constrained optimization - extractive body cue:** Empirically, it is hard to robustly choose the penalty coefficient, so we use a hard constraint instead of a penalty, with parameter δ (the bound ...
- **p. 6 / 3. Approximately solve this constrained optimization - extractive body cue:** Relative entropy policy search (REPS) (Peters et al., 2010) constrains the state-action marginals p(s, a), while TRPO constrains the conditionals p(a/s).
- **p. 6 / 3. Approximately solve this constrained optimization - extractive body cue:** Levine and Abbeel (2014) also use a KL divergence constraint, but its purpose is to encourage the policy not to stray from regions where the ...
- **Detected method headings:** A Proof of Policy Improvement Bound (p. 10); B Perturbation Theory Proof of Policy Improvement Bound (p. 12)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Policy / value representation | state에서 action과 return estimate를 표현한다 | state/observation과 task context | actor, critic, value, Q 또는 sequence policy를 계산 | policy/value estimate | We use the conjugate gradient algorithm followed by a line search, which is altogether only slightly more expensive than computing the gradient ... | p. 5 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization) |
| Rollout / target construction | interaction에서 update target을 만든다 | state, action, reward, next state | return, advantage, TD target 또는 trajectory statistics를 구성 | training target | Empirically, it is hard to robustly choose the penalty coefficient, so we use a hard constraint instead of a penalty, with parameter ... | p. 5 (3. Approximately solve this constrained optimization), p. 6 (3. Approximately solve this constrained optimization) |
| Policy / value update | 목표를 최적화해 다음 policy를 만든다 | target, replay/data와 parameters | gradient, trust region, entropy, replay 또는 constraint update를 수행 | updated policy/controller | Relative entropy policy search (REPS) (Peters et al., 2010) constrains the state-action marginals p(s, a), while TRPO constrains the conditionals p(a/s). | p. 6 (3. Approximately solve this constrained optimization), p. 6 (3. Approximately solve this constrained optimization) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3. Approximately solve this constrained optimization - extractive body cue:** The natural policy gradient (Kakade, 2002) can be obtained as a special case of the update in Equation (12) by using a linear approximation to ...
- **p. 6 / 3. Approximately solve this constrained optimization - extractive body cue:** We can also obtain the standard policy gradient update by using an ℓ2 constraint or penalty: maximize θ h ∇θLθold(θ)
- **p. 5 / 3. Approximately solve this constrained optimization - extractive body cue:** Empirically, it is hard to robustly choose the penalty coefficient, so we use a hard constraint instead of a penalty, with parameter δ (the bound ...
- **p. 5 / 3. Approximately solve this constrained optimization - extractive body cue:** Let us briefly summarize the relationship between the theory from Section 3 and the practical algorithm we have described: • The theory justifies optimizing a ...
- **Formal bridge:** s_t/o_t -> a_t sampled or selected by πθ -> expected return / constrained return -> task return, success and safe execution.
- **Equation/algorithm anchors:** p. 6 (3. Approximately solve this constrained optimization), p. 6 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | implies, classic, result, update, performed, exact, policy, iteration, uses, deterministic, maxa, improves, there, least | state 또는 observation, action, reward와 transition history | body cue; exact tensor/frame verify |
| State/latent | implies, classic, result, update, performed, exact, policy, iteration, uses, deterministic | policy/value state와 action-selection variable | body cue; notation verify |
| Action/output | Instead, introduce, following, local, approximation, Trust, region, policy, optimization, section | action policy와 induced trajectory | body cue; unit/decoder verify |
| Objective/constraint | natural, policy, gradient, Kakade, obtained, special, case, update, Equation, linear | expected return / constrained return | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 2 Preliminaries - extractive body cue:** This implies the classic result that the update performed by exact policy iteration, which uses the deterministic policy ˜π(s) = arg maxa Aπ(s, a), improves ...
- **p. 4 / 2 Preliminaries - extractive body cue:** Here, we generate a set of trajectories via simulation of the policy and incorporate all state-action pairs (sn, an) into the objective.
- **p. 5 / 2 Preliminaries - extractive body cue:** Trust Region Policy Optimization mate ˆQθi(sn, an,k) by performing a rollout (i.e., a short trajectory) starting with state sn and action an,k.
- **p. 6 / 3. Approximately solve this constrained optimization - extractive body cue:** Relative entropy policy search (REPS) (Peters et al., 2010) constrains the state-action marginals p(s, a), while TRPO constrains the conditionals p(a/s).
- **p. 4 / 2 Preliminaries - extractive body cue:** Trust Region Policy Optimization This problem imposes a constraint that the KL divergence is bounded at every point in the state space.
- **p. 1 / 2 Preliminaries - extractive body cue:** Consider an infinite-horizon discounted Markov decision process (MDP), defined by the tuple (S, A, P, r, ρ0, γ), where S is a finite set of ...
- **p. 2 / 2 Preliminaries - extractive body cue:** (3) Note that Lπ uses the visitation frequency ρπ rather than ρ˜π, ignoring changes in state visitation density due to changes in the policy.
- **Normalized interface:** observation=state 또는 observation, action, reward와 transition history; state=policy/value state와 action-selection variable; output/action=action policy와 induced trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | rollout/return horizon과 episode termination; exact n-step/discount는 exact value was not selected from the PDF body. | 5.1 Single Path In this estimation procedure, we collect a sequence of states by sampling s0 ∼ρ0 and then simulating the policy ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 environment step이 분리되며 deployment control rate는 별도 contract다. | We can rewrite Equation (1) with a sum over states instead of timesteps: η(˜π) = η(π) + ∞ X t=0 X s ... | Hz/fps, inference time and control rate |
| Memory | replay/rollout buffer와 actor/critic parameters; recurrent history 여부 확인 필요. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | environment interaction, value/policy update와 batch size가 비용을 결정한다. | We can rewrite Equation (1) with a sum over states instead of timesteps: η(˜π) = η(π) + ∞ X t=0 X s ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3. Approximately solve this constrained optimization - extractive body cue:** Empirically, it is hard to robustly choose the penalty coefficient, so we use a hard constraint instead of a penalty, with parameter δ (the bound ...
- **p. 6 / 3. Approximately solve this constrained optimization - extractive body cue:** Relative entropy policy search (REPS) (Peters et al., 2010) constrains the state-action marginals p(s, a), while TRPO constrains the conditionals p(a/s).
- **p. 6 / 3. Approximately solve this constrained optimization - extractive body cue:** Levine and Abbeel (2014) also use a KL divergence constraint, but its purpose is to encourage the policy not to stray from regions where the ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** conjugate, gradient, algorithm, followed, line, search, altogether, only, slightly, more, expensive, computing, itself, Empirically, hard, robustly, choose, penalty, coefficient, constraint.
- **Relevant PDF headings:** A Proof of Policy Improvement Bound (p. 10); B Perturbation Theory Proof of Policy Improvement Bound (p. 12).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Policy / value representation | 8.1 Simulated Robotic Locomotion We conducted the robotic locomotion experiments using the MuJoCo simulator (Todorov et al., 2012). | p. 6 (3. Can TRPO be used to solve challenging large-scale), p. 6 (1. What are the performance characteristics of the single) |
| Rollout / target construction | This self-normalized estimator removes the need to use a baseline for the Q-values (note that the gradient is unchanged by adding a ... | p. 5 (2 Preliminaries), p. 7 (3. Can TRPO be used to solve challenging large-scale) |
| Policy / value update | Though this difference might seem subtle, our experiments demonstrate that it significantly improves the algorithm's performance on larger problems. | p. 6 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization) |

## Failure and Ablation Link

- **p. 5 / 2 Preliminaries - extractive body cue:** This self-normalized estimator removes the need to use a baseline for the Q-values (note that the gradient is unchanged by adding a constant to the ...
- **p. 5 / 3. Approximately solve this constrained optimization - extractive body cue:** As described in Appendix C, this analytic estimator has computational benefits in the large-scale setting, since it removes the need to store a dense Hessian ...
- **p. 6 / 3. Can TRPO be used to solve challenging large-scale - extractive body cue:** To answer (1) and (2), we compare the performance of the single path and vine variants of TRPO, several ablated variants, and a number of ...
- **p. 7 / 3. Can TRPO be used to solve challenging large-scale - extractive body cue:** Note that for the hopper and walker, a score of -1 is achievable without any forward velocity, indicating a policy that simply learned balanced standing, ...
- **p. 5 / 3. Approximately solve this constrained optimization - extractive body cue:** The analytic estimator integrates over the action at each state sn, and does not depend on the action an that was sampled.
- **p. 6 / 3. Approximately solve this constrained optimization - extractive body cue:** Unlike REPS, our approach does not require a costly nonlinear optimization in the inner loop.
- **p. 5 / 2 Preliminaries - extractive body cue:** We can greatly reduce the variance of the Q-value differences between rollouts by using the same random number sequence for the noise in each of ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization), p. 6 (3. Approximately solve this constrained optimization), p. 6 (3. Approximately solve this constrained optimization), objective p. 6 (3. Approximately solve this constrained optimization), p. 6 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization), temporal p. 4 (2 Preliminaries), p. 2 (2 Preliminaries), p. 2 (2 Preliminaries), p. 5 (2 Preliminaries), p. 7 (3. Can TRPO be used to solve challenging large-scale), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Trust Region Policy Optimization mate ˆQθi(sn, an,k) by performing a rollout (i.e., a short trajectory) starting with state sn and action an,k. (p. 5, 2 Preliminaries).
- **Objective/update evidence:** The natural policy gradient (Kakade, 2002) can be obtained as a special case of the update in Equation (12) by using a linear approximation to L and a quadratic approximation ... (p. 6, 3. Approximately solve this constrained optimization).
- **Temporal/runtime evidence:** 5.1 Single Path In this estimation procedure, we collect a sequence of states by sampling s0 ∼ρ0 and then simulating the policy πθold for some number of timesteps to generate ... (p. 4, 2 Preliminaries).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
