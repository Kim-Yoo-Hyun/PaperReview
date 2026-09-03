# Method - Q-Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1007/BF00992698; PDF retrieval source: https://doi.org/10.1007/BF00992698. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 7 (3.2. The theorem), p. 2 (2. The task for ~-learning), p. 4 (3. The convergence proof), p. 3 (2. The task for ~-learning), p. 4 (3. The convergence proof), p. 2 (2. The task for ~-learning)): Then, for n > h, by B.4, compare the value _~ARp(IX, n), a t ..... as) of taking actions at, ..., as at state x in the ARP, with Q(x, ...

## Method Body Digest

- **p. 7 / 3.2. The theorem - extractive body cue:** Then, for n > h, by B.4, compare the value _~ARp(IX, n), a t ..... as) of taking actions at, ..., as at state x ...
- **p. 2 / 2. The task for ~-learning - extractive body cue:** Under a policy 7r, the value of state x is W(x) = ~A~(x)) + ~ ~]/%[~(x)]V~(y Y because the agent expects to receive 6~x(Tr(x)) immediately ...
- **p. 4 / 3. The convergence proof - extractive body cue:** Replaying the episode on card t consists of emitting the reward, rt, written on the card, and then moving to the next state (Yt, t ...
- **p. 3 / 2. The task for ~-learning - extractive body cue:** It is straightforward to show that V*(x) = max a O~*(x, a) and that if a* is an action at which the maximum is attained, ...
- **p. 4 / 3. The convergence proof - extractive body cue:** Cards are then removed one at a time from top of this deck and examined until one is found whose starting state and action match ...
- **p. 2 / 2. The task for ~-learning - extractive body cue:** Y In other words, the ~ value is the expected discounted reward for executing action a at state x and following policy 7r thereafter.
- **p. 3 / 2. The task for ~-learning - extractive body cue:** This may be considered a strong condition on the way states and actions are selected--however, under the stochastic conditions of the theorem, no method could ...
- **p. 2 / 2. The task for ~-learning - extractive body cue:** The task facing the agent is that of determining an optimal policy, one that maximizes total discounted expected reward.

## Design Rationale

- **p. 3 / 2. The task for ~-learning - extractive body cue:** In O~-learning, the agent's experience consists of a sequence of distinct stages or episodes.
- **p. 4 / 3. The convergence proof - extractive body cue:** A state of the AFI~, (x, n), consists of a card number (or level) n, together with a state x from the real process.
- **p. 4 / 3. The convergence proof - extractive body cue:** Replaying the episode on card t consists of emitting the reward, rt, written on the card, and then moving to the next state (Yt, t ...

## Source Evidence Cues

- **p. 7 / 3.2. The theorem - extractive body cue:** Then, for n > h, by B.4, compare the value _~ARp(IX, n), a t ..... as) of taking actions at, ..., as at state x ...
- **p. 2 / 2. The task for ~-learning - extractive body cue:** Under a policy 7r, the value of state x is W(x) = ~A~(x)) + ~ ~]/%[~(x)]V~(y Y because the agent expects to receive 6~x(Tr(x)) immediately ...
- **p. 4 / 3. The convergence proof - extractive body cue:** Replaying the episode on card t consists of emitting the reward, rt, written on the card, and then moving to the next state (Yt, t ...
- **p. 3 / 2. The task for ~-learning - extractive body cue:** It is straightforward to show that V*(x) = max a O~*(x, a) and that if a* is an action at which the maximum is attained, ...
- **p. 4 / 3. The convergence proof - extractive body cue:** Cards are then removed one at a time from top of this deck and examined until one is found whose starting state and action match ...
- **p. 2 / 2. The task for ~-learning - extractive body cue:** Y In other words, the ~ value is the expected discounted reward for executing action a at state x and following policy 7r thereafter.
- **p. 3 / 2. The task for ~-learning - extractive body cue:** This may be considered a strong condition on the way states and actions are selected--however, under the stochastic conditions of the theorem, no method could ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Policy / value representation | state에서 action과 return estimate를 표현한다 | state/observation과 task context | actor, critic, value, Q 또는 sequence policy를 계산 | policy/value estimate | Then, for n > h, by B.4, compare the value _~ARp(IX, n), a t ..... as) of taking actions at, ..., as ... | p. 7 (3.2. The theorem), p. 2 (2. The task for ~-learning) |
| Rollout / target construction | interaction에서 update target을 만든다 | state, action, reward, next state | return, advantage, TD target 또는 trajectory statistics를 구성 | training target | Under a policy 7r, the value of state x is W(x) = ~A~(x)) + ~ ~]/%[~(x)]V~(y Y because the agent expects to ... | p. 2 (2. The task for ~-learning), p. 4 (3. The convergence proof) |
| Policy / value update | 목표를 최적화해 다음 policy를 만든다 | target, replay/data와 parameters | gradient, trust region, entropy, replay 또는 constraint update를 수행 | updated policy/controller | Replaying the episode on card t consists of emitting the reward, rt, written on the card, and then moving to the next ... | p. 4 (3. The convergence proof), p. 3 (2. The task for ~-learning) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 2. The task for ~-learning - extractive body cue:** The task facing the agent is that of determining an optimal policy, one that maximizes total discounted expected reward.
- **p. 3 / 2. The task for ~-learning - extractive body cue:** Of course, in the early stages of learning, the O~ values may not accurately reflect the policy they implicitly define (the maximizing actions in equation ...
- **p. 7 / 3.2. The theorem - extractive body cue:** The second term is the cost, from B.4, of the incorrect rewards and transition probabilities.
- **p. 7 / 3.2. The theorem - extractive body cue:** Then, for n > h, by B.4, compare the value _~ARp(IX, n), a t ..... as) of taking actions at, ..., as at state x ...
- **p. 4 / 3. The convergence proof - extractive body cue:** Define ~t(x,n),(y,m )DAFIp [a] and (Rx(n)(a) as the transition-probability matrices and expected rewards of the AFtP.
- **p. 6 / 3.1. Lemmas - extractive body cue:** DAYAN B.3 With probability 1, the probabilities P~[a] and expected rewards 61}n)(a) in the AFIP converge and tend to the transition matrices and expected rewards ...
- **Formal bridge:** s_t/o_t -> a_t sampled or selected by πθ -> expected return / constrained return -> task return, success and safe execution.
- **Equation/algorithm anchors:** p. 3 (2. The task for ~-learning), p. 6 (3.2. The theorem), p. 7 (3.2. The theorem), p. 7 (3.2. The theorem), p. 2 (2. The task for ~-learning), p. 3 (2. The task for ~-learning).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | other, words, value, expected, discounted, reward, executing, action, state, following, policy, thereafter, Under, because | state 또는 observation, action, reward와 transition history | body cue; exact tensor/frame verify |
| State/latent | other, words, value, expected, discounted, reward, executing, action, state, following | policy/value state와 action-selection variable | body cue; notation verify |
| Action/output | learning, agent, experience, consists, sequence, distinct, stages, episodes, state, AFI | action policy와 induced trajectory | body cue; unit/decoder verify |
| Objective/constraint | task, facing, agent, determining, optimal, policy, maximizes, total, discounted, expected | expected return / constrained return | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 2. The task for ~-learning - extractive body cue:** Y In other words, the ~ value is the expected discounted reward for executing action a at state x and following policy 7r thereafter.
- **p. 2 / 2. The task for ~-learning - extractive body cue:** Under a policy 7r, the value of state x is W(x) = ~A~(x)) + ~ ~]/%[~(x)]V~(y Y because the agent expects to receive 6~x(Tr(x)) immediately ...
- **p. 3 / 2. The task for ~-learning - extractive body cue:** This may be considered a strong condition on the way states and actions are selected--however, under the stochastic conditions of the theorem, no method could ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** It works by successively improving its evaluations of the quality of particular actions at particular states.
- **p. 1 / 1. Introduction - extractive body cue:** By trying all actions in all states repeatedly, it learns which are best overall, judged by long-term discounted reward.
- **p. 3 / 2. The task for ~-learning - extractive body cue:** The initial O~ values, O~o(X, a), for all states and actions are assumed given.
- **p. 4 / 3. The convergence proof - extractive body cue:** The next state of the AFII ~, given current state (x, n) and action a, is determined as follows.
- **Normalized interface:** observation=state 또는 observation, action, reward와 transition history; state=policy/value state와 action-selection variable; output/action=action policy와 induced trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | rollout/return horizon과 episode termination; exact n-step/discount는 exact value was not selected from the PDF body. | Consider a computational agent moving around some discrete, finite world, choosing one from a finite collection of actions at every time step. | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 environment step이 분리되며 deployment control rate는 별도 contract다. | Learning proceeds similarly to Sutton's (1984; 1988) method of temporal differences (TD): an agent tries an action at a particular state, and ... | Hz/fps, inference time and control rate |
| Memory | replay/rollout buffer와 actor/critic parameters; recurrent history 여부 확인 필요. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | environment interaction, value/policy update와 batch size가 비용을 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- training/inference separation PDF body cue not selected; no claim inferred

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Then, compare, value, ARp, taking, actions, state, them, real, process, Where, equation, first, term, counts, cost, conditions, holding, straying, below.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Policy / value representation | First, all the cards for episodes later than n are eliminated, leaving just a finite deck. | p. 4 (3. The convergence proof), p. 5 (3.1. Lemmas) |
| Rollout / target construction | Assume, without loss of generality, that O~0(x, a) < 61/(1 - 3') and that 61 __. | p. 6 (3.2. The theorem), p. 5 (3. The convergence proof) |
| Policy / value update | Unfortunately, the theorem does not extend trivially to this case, and alternative proof methods such as those in Kushner and Clark (1978) ... | p. 8 (4. Discussions and conclusions), p. 8 (4. Discussions and conclusions) |

## Failure and Ablation Link

- **p. 5 / 3. The convergence proof - extractive body cue:** 2 Note that during such a sequence, episode cards are only removed from the deck, and are never replaced.
- **p. 7 / 3.2. The theorem - extractive body cue:** However, by B.1, the effect of taking only s actions makes a difference of less than e/6 for both the ARP and the real process.
- **p. 4 / 3. The convergence proof - extractive body cue:** Cards are then removed one at a time from top of this deck and examined until one is found whose starting state and action match ...
- **p. 6 / 3.2. The theorem - extractive body cue:** Assume, without loss of generality, that O~0(x, a) < 61/(1 - 3') and that 61 __.
- **p. 8 / 4. Discussions and conclusions - extractive body cue:** Unfortunately, the theorem does not extend trivially to this case, and alternative proof methods such as those in Kushner and Clark (1978) may be required.
- **p. 8 / 4. Discussions and conclusions - extractive body cue:** The theorem above only proves the convergence of a restricted version of Watkins' (1989) comprehensive Q-learning algorithm, since it does not permit updates based on ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 7 (3.2. The theorem), p. 2 (2. The task for ~-learning), p. 4 (3. The convergence proof), p. 3 (2. The task for ~-learning), p. 4 (3. The convergence proof), p. 2 (2. The task for ~-learning), objective p. 2 (2. The task for ~-learning), p. 3 (2. The task for ~-learning), p. 7 (3.2. The theorem), p. 7 (3.2. The theorem), p. 4 (3. The convergence proof), p. 6 (3.1. Lemmas), temporal p. 2 (2. The task for ~-learning), p. 1 (1. Introduction), p. 3 (2. The task for ~-learning), p. 3 (2. The task for ~-learning), p. 4 (3. The convergence proof), p. 5 (3. The convergence proof).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Y In other words, the ~ value is the expected discounted reward for executing action a at state x and following policy 7r thereafter. (p. 2, 2. The task for ~-learning).
- **Objective/update evidence:** The second term is the cost, from B.4, of the incorrect rewards and transition probabilities. (p. 7, 3.2. The theorem).
- **Temporal/runtime evidence:** In O~-learning, the agent's experience consists of a sequence of distinct stages or episodes. (p. 3, 2. The task for ~-learning).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
