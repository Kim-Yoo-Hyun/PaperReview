# Method - Policy Gradient Methods for Reinforcement Learning with Function Approximation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html; PDF retrieval source: https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (Abstract), p. 1 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 3 (Abstract)): For example, the policy might be represented by a neural network whose input is a representation of the state, whose output is action selection probabilities, and whose weights are the ...

## Method Body Digest

- **p. 2 / Abstract - extractive body cue:** For example, the policy might be represented by a neural network whose input is a representation of the state, whose output is action selection probabilities, ...
- **p. 1 / Abstract - extractive body cue:** First, it is oriented toward finding deterministic policies, whereas the optimal policy is often stochastic, selecting different actions with specific probabilities (e.g., see Singh, Jaakkola, ...
- **p. 1 / Abstract - extractive body cue:** The dominant approach for the last decade has been the value-function approach, in which all function approximation effort goes into estimating a value function, with ...
- **p. 2 / Abstract - extractive body cue:** Our result also suggests a way of proving the convergence of a wide variety of algorithms based on "actor-critic" or policy-iteration architectures (e.g., Barto, Sutton, ...
- **p. 3 / Abstract - extractive body cue:** This leads to Williams's episodic REINFORCE algorithm, t::..Ot oc a1r~~,at2 Rt (1 ) (the ~a 7r St,at 7r\St,Ut) corrects for the oversampling of actions preferred ...
- **p. 3 / Abstract - extractive body cue:** In the average reward formulation, the value of a state-action pair given a policy is defined as 00 Q1r(s,a) = LE {rt - p(1I") I ...
- **p. 4 / Abstract - extractive body cue:** If fw satisfies (3) and is compatible with the policy parameterization in the sense thatl 8fw(s, a) 81r(s, a) 1 = 8w 80 1r(s, a) ...
- **p. 1 / Abstract - extractive body cue:** In this paper we explore an alternative approach in which the policy is explicitly represented by its own function approximator, independent of the value function, ...

## Design Rationale

- **p. 2 / Abstract - extractive body cue:** Konda and Tsitsiklis (in prep.) independently developed a very simialr result to ours.

## Source Evidence Cues

- **p. 2 / Abstract - extractive body cue:** For example, the policy might be represented by a neural network whose input is a representation of the state, whose output is action selection probabilities, ...
- **p. 1 / Abstract - extractive body cue:** First, it is oriented toward finding deterministic policies, whereas the optimal policy is often stochastic, selecting different actions with specific probabilities (e.g., see Singh, Jaakkola, ...
- **p. 1 / Abstract - extractive body cue:** The dominant approach for the last decade has been the value-function approach, in which all function approximation effort goes into estimating a value function, with ...
- **p. 2 / Abstract - extractive body cue:** Our result also suggests a way of proving the convergence of a wide variety of algorithms based on "actor-critic" or policy-iteration architectures (e.g., Barto, Sutton, ...
- **p. 3 / Abstract - extractive body cue:** This leads to Williams's episodic REINFORCE algorithm, t::..Ot oc a1r~~,at2 Rt (1 ) (the ~a 7r St,at 7r\St,Ut) corrects for the oversampling of actions preferred ...
- **p. 3 / Abstract - extractive body cue:** In the average reward formulation, the value of a state-action pair given a policy is defined as 00 Q1r(s,a) = LE {rt - p(1I") I ...
- **p. 4 / Abstract - extractive body cue:** If fw satisfies (3) and is compatible with the policy parameterization in the sense thatl 8fw(s, a) 81r(s, a) 1 = 8w 80 1r(s, a) ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Policy / value representation | state에서 action과 return estimate를 표현한다 | state/observation과 task context | actor, critic, value, Q 또는 sequence policy를 계산 | policy/value estimate | For example, the policy might be represented by a neural network whose input is a representation of the state, whose output is ... | p. 2 (Abstract), p. 1 (Abstract) |
| Rollout / target construction | interaction에서 update target을 만든다 | state, action, reward, next state | return, advantage, TD target 또는 trajectory statistics를 구성 | training target | First, it is oriented toward finding deterministic policies, whereas the optimal policy is often stochastic, selecting different actions with specific probabilities (e.g., ... | p. 1 (Abstract), p. 1 (Abstract) |
| Policy / value update | 목표를 최적화해 다음 policy를 만든다 | target, replay/data와 parameters | gradient, trust region, entropy, replay 또는 constraint update를 수행 | updated policy/controller | The dominant approach for the last decade has been the value-function approach, in which all function approximation effort goes into estimating a ... | p. 1 (Abstract), p. 2 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / Abstract - extractive body cue:** In this paper we explore an alternative approach in which the policy is explicitly represented by its own function approximator, independent of the value function, ...
- **p. 3 / Abstract - extractive body cue:** (2) This way of expressing the gradient was first rtiscussed for the average-reward formulation by Marbach and Tsitsiklis (1998), based on a related expression in ...
- **p. 2 / Abstract - extractive body cue:** However, VAPS methods do not climb the gradient of performance (expected long-term reward), but of a measure combining performance and valuefunction accuracy.
- **p. 2 / Abstract - extractive body cue:** Like policy-gradient methods, VAPS includes separately parameterized policy and value functions updated by gradient methods.
- **p. 3 / Abstract - extractive body cue:** Policy Gradient Methods for RL with Function Approximation 1059 With function approximation, two ways of formulating the agent's objective are useful.
- **p. 1 / Abstract - extractive body cue:** Our main new result is to show that the gradient can be written in a form suitable for estimation from experience aided by an approximate ...
- **Formal bridge:** s_t/o_t -> a_t sampled or selected by πθ -> expected return / constrained return -> task return, success and safe execution.
- **Equation/algorithm anchors:** p. 3 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 2 (Abstract), p. 1 (Body text (section boundary not confidently recovered)), p. 3 (Abstract).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | example, policy, might, represented, neural, network, whose, input, representation, state, output, action, selection, probabilities | state 또는 observation, action, reward와 transition history | body cue; exact tensor/frame verify |
| State/latent | example, policy, might, represented, neural, network, whose, input, representation, state | policy/value state와 action-selection variable | body cue; notation verify |
| Action/output | Konda, Tsitsiklis, prep, independently, developed, very, simialr, result, ours, example | action policy와 induced trajectory | body cue; unit/decoder verify |
| Objective/constraint | explore, alternative, policy, explicitly, represented, function, approximator, independent, value, updated | expected return / constrained return | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / Abstract - extractive body cue:** For example, the policy might be represented by a neural network whose input is a representation of the state, whose output is action selection probabilities, ...
- **p. 1 / Abstract - extractive body cue:** The dominant approach for the last decade has been the value-function approach, in which all function approximation effort goes into estimating a value function, with ...
- **p. 3 / Abstract - extractive body cue:** In the average reward formulation, the value of a state-action pair given a policy is defined as 00 Q1r(s,a) = LE {rt - p(1I") I ...
- **p. 1 / Abstract - extractive body cue:** First, it is oriented toward finding deterministic policies, whereas the optimal policy is often stochastic, selecting different actions with specific probabilities (e.g., see Singh, Jaakkola, ...
- **p. 2 / Abstract - extractive body cue:** The state, action, and reward at each time t E {O, 1, 2, . . . } are denoted St E S, at E A, ...
- **p. 3 / Abstract - extractive body cue:** In any event, the key aspect of both expressions for the gradient is that their are no terms of the form adiJII): the effect of ...
- **p. 4 / Abstract - extractive body cue:** (3) /I a Theorem 2 (Policy Gradient with Function Approximation).
- **Normalized interface:** observation=state 또는 observation, action, reward와 transition history; state=policy/value state와 action-selection variable; output/action=action policy와 induced trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | rollout/return horizon과 episode termination; exact n-step/discount는 exact value was not selected from the PDF body. | This can occur even if the best approximation is found at each step before changing the policy, and whether the notion of ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 environment step이 분리되며 deployment control rate는 별도 contract다. | Let {Ok}~o be any step-size sequence such that limk-+oo Ok = 0 and l:k Ok = 00. | Hz/fps, inference time and control rate |
| Memory | replay/rollout buffer와 actor/critic parameters; recurrent history 여부 확인 필요. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | environment interaction, value/policy update와 batch size가 비용을 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- training/inference separation PDF body cue not selected; no claim inferred

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** example, policy, might, represented, neural, network, whose, input, representation, state, output, action, selection, probabilities, weights, parameters, First, oriented, toward, finding.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Policy / value representation | The environment's dynamics are characterized by state transition probabilities, P:SI = Pr { St+ 1 = Sf I St = s, at ... | p. 2 (Abstract), p. 3 (Abstract) |
| Rollout / target construction | The issues here are entirely analogous to those in the use of reinforcement baselines in earlier work (e.g., Williams, 1992; Dayan, 1991; ... | p. 5 (Abstract), p. 2 (Abstract) |
| Policy / value update | If the above can be achieved, then 0 can usually be assured to converge to a locally optimal policy in the performance ... | p. 2 (Abstract), p. 4 (Abstract) |

## Failure and Ablation Link

- **p. 3 / Abstract - extractive body cue:** In any event, the key aspect of both expressions for the gradient is that their are no terms of the form adiJII): the effect of ...
- **p. 2 / Abstract - extractive body cue:** Williams's (1988, 1992) REINFORCE algorithm also finds an unbiased estimate of the gradient, but without the assistance of a learned value function.
- **p. 5 / Abstract - extractive body cue:** Our results establish that that approximation process can proceed without affecting the expected evolution of fw and 1r.
- **p. 2 / Abstract - extractive body cue:** Similarly, Gordon's (1995) fitted value iteration is also convergent and value-based, but does not find a locally optimal policy.
- **p. 2 / Abstract - extractive body cue:** As a result, VAPS does not converge to a locally optimal policy, except in the case that no weight is put upon value-function accuracy, in ...
- **p. 3 / Abstract - extractive body cue:** In any event, the key aspect of both expressions for the gradient is that their are no terms of the form adiJII): the effect of ...
- **p. 5 / Abstract - extractive body cue:** (This follows immediately because l:a 87r~~a) = 0, Vs E S.) The choice of v does not affect any of our theorems, but can substantially ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (Abstract), p. 1 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 3 (Abstract), objective p. 1 (Abstract), p. 3 (Abstract), p. 2 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 1 (Abstract), temporal p. 1 (Abstract), p. 5 (Abstract), p. 2 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 5 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** For example, the policy might be represented by a neural network whose input is a representation of the state, whose output is action selection probabilities, and whose weights are the ... (p. 2, Abstract).
- **Objective/update evidence:** In this paper we explore an alternative approach in which the policy is explicitly represented by its own function approximator, independent of the value function, and is updated according to ... (p. 1, Abstract).
- **Temporal/runtime evidence:** Let {Ok}~o be any step-size sequence such that limk-+oo Ok = 0 and l:k Ok = 00. (p. 5, Abstract).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
