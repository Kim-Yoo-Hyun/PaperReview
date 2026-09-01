# Method - Maximum a Posteriori Policy Optimisation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=S1ANxQW0b; PDF retrieval source: https://openreview.net/forum?id=S1ANxQW0b. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): We introduce a new algorithm for reinforcement learning called Maximum aposteriori Policy Optimisation (MPO) based on coordinate ascent on a relativeentropy objective.

## Method Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** We introduce a new algorithm for reinforcement learning called Maximum aposteriori Policy Optimisation (MPO) based on coordinate ascent on a relativeentropy objective.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this paper we propose a novel off-policy algorithm that benefits from the best properties of both classes.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** And subsequently it updates the policy such that better actions in that state will have better probabilities to be chosen.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We leverage the fast convergence properties of EM-style coordinate ascent by alternating a nonparametric data-based E-step which re-weights state-action samples, with a supervised, parametric M-step ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In contrast to typical off-policy value-gradient algorithms, the new algorithm does not require gradient of the Q-function to update the policy.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** 2016), Stochastic Value Gradient (SVG, Heess et al.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** In contrast, off-policy value-gradient algorithms such as the Deep Deterministic Policy Gradient (DDPG, Silver et al.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Published as a conference paper at ICLR 2018 rewards, what are the actions most likely to have been taken?".

## Design Rationale

- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this paper we propose a novel off-policy algorithm that benefits from the best properties of both classes.
- **p. 1 / ABSTRACT - extractive body cue:** We introduce a new algorithm for reinforcement learning called Maximum aposteriori Policy Optimisation (MPO) based on coordinate ascent on a relativeentropy objective.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We show below that several algorithms, including TRPO, can be directly related to this perspective.

## Source Evidence Cues

- **p. 1 / ABSTRACT - extractive body cue:** We introduce a new algorithm for reinforcement learning called Maximum aposteriori Policy Optimisation (MPO) based on coordinate ascent on a relativeentropy objective.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this paper we propose a novel off-policy algorithm that benefits from the best properties of both classes.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** And subsequently it updates the policy such that better actions in that state will have better probabilities to be chosen.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We leverage the fast convergence properties of EM-style coordinate ascent by alternating a nonparametric data-based E-step which re-weights state-action samples, with a supervised, parametric M-step ...
- **Detected method headings:** A.2 REGULARIZED JOINT POLICY GRADIENT (p. 16)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Policy / value representation | state에서 action과 return estimate를 표현한다 | state/observation과 task context | actor, critic, value, Q 또는 sequence policy를 계산 | policy/value estimate | We introduce a new algorithm for reinforcement learning called Maximum aposteriori Policy Optimisation (MPO) based on coordinate ascent on a relativeentropy objective. | p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION) |
| Rollout / target construction | interaction에서 update target을 만든다 | state, action, reward, next state | return, advantage, TD target 또는 trajectory statistics를 구성 | training target | In this paper we propose a novel off-policy algorithm that benefits from the best properties of both classes. | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Policy / value update | 목표를 최적화해 다음 policy를 만든다 | target, replay/data와 parameters | gradient, trust region, entropy, replay 또는 constraint update를 수행 | updated policy/controller | And subsequently it updates the policy such that better actions in that state will have better probabilities to be chosen. | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In contrast to typical off-policy value-gradient algorithms, the new algorithm does not require gradient of the Q-function to update the policy.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** 2016), Stochastic Value Gradient (SVG, Heess et al.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** In contrast, off-policy value-gradient algorithms such as the Deep Deterministic Policy Gradient (DDPG, Silver et al.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Published as a conference paper at ICLR 2018 rewards, what are the actions most likely to have been taken?".
- **Formal bridge:** s_t/o_t -> a_t sampled or selected by πθ -> expected return / constrained return -> task return, success and safe execution.
- **Equation/algorithm anchors:** p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | subsequently, updates, policy, better, actions, state, will, have, probabilities, chosen, develop, off-policy, algorithms, demonstrate | state 또는 observation, action, reward와 transition history | body cue; exact tensor/frame verify |
| State/latent | subsequently, updates, policy, better, actions, state, will, have, probabilities, chosen | policy/value state와 action-selection variable | body cue; notation verify |
| Action/output | novel, off-policy, algorithm, benefits, best, properties, classes, introduce, reinforcement, learning | action policy와 induced trajectory | body cue; unit/decoder verify |
| Objective/constraint | contrast, typical, off-policy, value-gradient, algorithms, algorithm, does, require, gradient, Q-function | expected return / constrained return | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 INTRODUCTION - extractive body cue:** And subsequently it updates the policy such that better actions in that state will have better probabilities to be chosen.
- **p. 1 / ABSTRACT - extractive body cue:** We develop two off-policy algorithms and demonstrate that they are competitive with the state-of-the-art in deep reinforcement learning.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Instead it uses samples from the Q-function to compare different actions in a given state.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this paper we propose a novel off-policy algorithm that benefits from the best properties of both classes.
- **Normalized interface:** observation=state 또는 observation, action, reward와 transition history; state=policy/value state와 action-selection variable; output/action=action policy와 induced trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | rollout/return horizon과 episode termination; exact n-step/discount는 exact value not recovered from the selected body cues. | 5.1.2 COMPLETE RESULTS ON THE CONTROL SUITE The results for MPO (non-parameteric) - and a comparison to an implementation of state-of-the-art algorithms ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 environment step이 분리되며 deployment control rate는 별도 contract다. | 0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 training_steps 1e7 0 200 400 600 800 1000 mean_return task_name=run, domain_name=humanoid agent=DDPG agent=EPG + ... | Hz/fps, inference time and control rate |
| Memory | replay/rollout buffer와 actor/critic parameters; recurrent history 여부 확인 필요. | Casting Reinforcement Learning (RL) as an inference problem has a long history dating back at least two decades (Dayan & Hinton, 1997). | window and reset |
| Compute | environment interaction, value/policy update와 batch size가 비용을 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 9 / 5 EXPERIMENTS - extractive body cue:** 0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 training_steps 1e7 0 200 400 600 800 1000 mean_return task_name=run, domain_name=humanoid agent=DDPG agent=EPG + retrace + entropy ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** introduce, algorithm, reinforcement, learning, called, Maximum, aposteriori, Policy, Optimisation, MPO, coordinate, ascent, relativeentropy, objective, novel, off-policy, benefits, best, properties, classes.
- **Relevant PDF headings:** A.2 REGULARIZED JOINT POLICY GRADIENT (p. 16).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Policy / value representation | For example, the classical cart-pole and acrobot dynamical systems, 2D and Humanoid walking as well as simple low-dimensional planar reaching and manipulation ... | p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Rollout / target construction | Figure 2: Ablation study of the MPO algorithm and comparison to common baselines from the liter- ature on three domains from the ... | p. 8 (Figure/Table caption), p. 8 (5 EXPERIMENTS) |
| Policy / value update | This difference is so extreme that in several instances the PPO baseline converges an order of magnitude slower than the off-policy algorithms ... | p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Finally using only a single sample to estimate the integral (and hence the likelihood ratio gradient) results in an actor-critic variant with Retrace that is ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** To make computation time bearable in these more complicated domains we utilize a parallel variant of our algorithm: in this implementation K learners are all ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** This difference is so extreme that in several instances the PPO baseline converges an order of magnitude slower than the off-policy algorithms and we thus ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 2: Ablation study of the MPO algorithm and comparison to common baselines from the liter- ature on three domains from the control suite. We ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** 0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 training_steps 1e7 0 200 400 600 800 1000 mean_return task_name=run, domain_name=humanoid agent=DDPG agent=EPG + retrace + entropy ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), objective p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), temporal p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 5 (2.1 RELATED WORK), p. 2 (1 INTRODUCTION), p. 2 (2.1 RELATED WORK), p. 3 (2.1 RELATED WORK).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
