# Method - Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1007/BF00992696; PDF retrieval source: https://doi.org/10.1007/BF00992696. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 9 (5. Episodic REINFORCE algorithms), p. 8 (5. Episodic REINFORCE algorithms), p. 8 (4. REINFORCE algorithms), p. 9 (5. Episodic REINFORCE algorithms), p. 7 (4. REINFORCE algorithms), p. 7 (4. REINFORCE algorithms)): For example, if the network consists of Bernoulli-logistic units an episodic REINFORCE algorithm would prescribe weight changes according to the rule k Awij = c~ij(r - bij) Z [Yi(t) -pi(t)] ...

## Method Body Digest

- **p. 9 / 5. Episodic REINFORCE algorithms - extractive body cue:** For example, if the network consists of Bernoulli-logistic units an episodic REINFORCE algorithm would prescribe weight changes according to the rule k Awij = c~ij(r ...
- **p. 8 / 5. Episodic REINFORCE algorithms - extractive body cue:** In particular, assume a net N is trained on an episode-by-episode basis, where each episode consists of k time steps, during which the units may ...
- **p. 8 / 4. REINFORCE algorithms - extractive body cue:** As a particular example, for a network of Bernoulli-logistic units one may use the learning rule Awij = a(r - ?)(Yi - Pi) xj, (9) ...
- **p. 9 / 5. Episodic REINFORCE algorithms - extractive body cue:** One way to create a statistical gradient-following algorithm for this case is to simply replace r in (11) by E~= 1 r(t), but it is ...
- **p. 7 / 4. REINFORCE algorithms - extractive body cue:** Thus AR-b when applied to a network of Bernoulli-logistic units, is a REINFORCE algorithm.
- **p. 7 / 4. REINFORCE algorithms - extractive body cue:** The special case of this algorithm when the reinforcement signal is limited to 0 and 1 coincides with the 2-action version of the linear reward-inaction ...
- **p. 6 / 4. REINFORCE algorithms - extractive body cue:** Consider first a Bernoulli unit having no (nonreinforcement) input and suppose that the parameter to be adapted is Pi = Pr {Yi =-- 1}.
- **p. 7 / 4. REINFORCE algorithms - extractive body cue:** If k = 0, this is called the associative reward-inaction (AR_I) algorithm, and we see that the learning rule reduces to equation (8) in this ...

## Design Rationale

- **p. 1 / 1. Introduction - extractive body cue:** In this article we present analytical results concerning certain algorithms for tasks that are associative, meaning that the learner is required to perform an input-output ...
- **p. 2 / 1. Introduction - extractive body cue:** The results to be presented apply in general to any learner whose inputoutput mappings consists of a parameterized input-controlled distribution function from which outputs are ...
- **p. 8 / 5. Episodic REINFORCE algorithms - extractive body cue:** In particular, assume a net N is trained on an episode-by-episode basis, where each episode consists of k time steps, during which the units may ...

## Source Evidence Cues

- **p. 9 / 5. Episodic REINFORCE algorithms - extractive body cue:** For example, if the network consists of Bernoulli-logistic units an episodic REINFORCE algorithm would prescribe weight changes according to the rule k Awij = c~ij(r ...
- **p. 8 / 5. Episodic REINFORCE algorithms - extractive body cue:** In particular, assume a net N is trained on an episode-by-episode basis, where each episode consists of k time steps, during which the units may ...
- **p. 8 / 4. REINFORCE algorithms - extractive body cue:** As a particular example, for a network of Bernoulli-logistic units one may use the learning rule Awij = a(r - ?)(Yi - Pi) xj, (9) ...
- **p. 9 / 5. Episodic REINFORCE algorithms - extractive body cue:** One way to create a statistical gradient-following algorithm for this case is to simply replace r in (11) by E~= 1 r(t), but it is ...
- **p. 7 / 4. REINFORCE algorithms - extractive body cue:** Thus AR-b when applied to a network of Bernoulli-logistic units, is a REINFORCE algorithm.
- **p. 7 / 4. REINFORCE algorithms - extractive body cue:** The special case of this algorithm when the reinforcement signal is limited to 0 and 1 coincides with the 2-action version of the linear reward-inaction ...
- **p. 6 / 4. REINFORCE algorithms - extractive body cue:** Consider first a Bernoulli unit having no (nonreinforcement) input and suppose that the parameter to be adapted is Pi = Pr {Yi =-- 1}.
- **Detected method headings:** 4. REINFORCE algorithms (p. 5); 5. Episodic REINFORCE algorithms (p. 8); 8. Algorithm performance and other issues (p. 15)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Policy / value representation | state에서 action과 return estimate를 표현한다 | state/observation과 task context | actor, critic, value, Q 또는 sequence policy를 계산 | policy/value estimate | For example, if the network consists of Bernoulli-logistic units an episodic REINFORCE algorithm would prescribe weight changes according to the rule k ... | p. 9 (5. Episodic REINFORCE algorithms), p. 8 (5. Episodic REINFORCE algorithms) |
| Rollout / target construction | interaction에서 update target을 만든다 | state, action, reward, next state | return, advantage, TD target 또는 trajectory statistics를 구성 | training target | In particular, assume a net N is trained on an episode-by-episode basis, where each episode consists of k time steps, during which ... | p. 8 (5. Episodic REINFORCE algorithms), p. 8 (4. REINFORCE algorithms) |
| Policy / value update | 목표를 최적화해 다음 policy를 만든다 | target, replay/data와 parameters | gradient, trust region, entropy, replay 또는 constraint update를 수행 | updated policy/controller | As a particular example, for a network of Bernoulli-logistic units one may use the learning rule Awij = a(r - ?)(Yi - ... | p. 8 (4. REINFORCE algorithms), p. 9 (5. Episodic REINFORCE algorithms) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / 4. REINFORCE algorithms - extractive body cue:** If k = 0, this is called the associative reward-inaction (AR_I) algorithm, and we see that the learning rule reduces to equation (8) in this ...
- **p. 6 / 4. REINFORCE algorithms - extractive body cue:** This results relates VwE{r I W}, the gradient in weight space of the performance measure E {r ] W}, to E {AW] W}, the average ...
- **p. 9 / 5. Episodic REINFORCE algorithms - extractive body cue:** One way to create a statistical gradient-following algorithm for this case is to simply replace r in (11) by E~= 1 r(t), but it is ...
- **p. 6 / 4. REINFORCE algorithms - extractive body cue:** The name is an acronym for "REward Increment = Nonnegative Factor x Offset Reinforcement x Characteristic Eligibility," which describes the form of the algorithm.
- **p. 7 / 4. REINFORCE algorithms - extractive body cue:** Differentiating the equations (1) and (2) yields dpi/dsi = f'(si) and Osi/Owi j = xj.
- **p. 9 / 5. Episodic REINFORCE algorithms - extractive body cue:** GRADIENT ALGORITHMS 237 k Awij = °~ij(r - bij) ~a eij(t) t=l (~) where all notation is the same as that defined earlier, with eij(t ...
- **Formal bridge:** s_t/o_t -> a_t sampled or selected by πθ -> expected return / constrained return -> task return, success and safe execution.
- **Equation/algorithm anchors:** p. 6 (4. REINFORCE algorithms), p. 7 (4. REINFORCE algorithms), p. 7 (4. REINFORCE algorithms), p. 9 (5. Episodic REINFORCE algorithms), p. 9 (5. Episodic REINFORCE algorithms), p. 6 (4. REINFORCE algorithms).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | presented, apply, general, learner, whose, inputoutput, mappings, consists, parameterized, input-controlled, distribution, function, outputs, randomly | state 또는 observation, action, reward와 transition history | body cue; exact tensor/frame verify |
| State/latent | presented, apply, general, learner, whose, inputoutput, mappings, consists, parameterized, input-controlled | policy/value state와 action-selection variable | body cue; notation verify |
| Action/output | article, present, analytical, concerning, certain, algorithms, tasks, associative, meaning, learner | action policy와 induced trajectory | body cue; unit/decoder verify |
| Objective/constraint | called, associative, reward-inaction, AR_I, algorithm, learning, rule, reduces, equation, case | expected return / constrained return | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** The results to be presented apply in general to any learner whose inputoutput mappings consists of a parameterized input-controlled distribution function from which outputs are ...
- **p. 1 / 1. Introduction - extractive body cue:** In this article we present analytical results concerning certain algorithms for tasks that are associative, meaning that the learner is required to perform an input-output ...
- **p. 2 / 1. Introduction - extractive body cue:** WILLIAMS A further assumption we make here is that the learner's search behavior, always a necessary component of any form of reinforcement learning algorithm, is ...
- **p. 8 / 5. Episodic REINFORCE algorithms - extractive body cue:** In particular, assume a net N is trained on an episode-by-episode basis, where each episode consists of k time steps, during which the units may ...
- **p. 9 / 5. Episodic REINFORCE algorithms - extractive body cue:** One way to create a statistical gradient-following algorithm for this case is to simply replace r in (11) by E~= 1 r(t), but it is ...
- **p. 6 / 4. REINFORCE algorithms - extractive body cue:** Consider first a Bernoulli unit having no (nonreinforcement) input and suppose that the parameter to be adapted is Pi = Pr {Yi =-- 1}.
- **p. 7 / 4. REINFORCE algorithms - extractive body cue:** The special case of this algorithm when the reinforcement signal is limited to 0 and 1 coincides with the 2-action version of the linear reward-inaction ...
- **Normalized interface:** observation=state 또는 observation, action, reward와 transition history; state=policy/value state와 action-selection variable; output/action=action policy와 induced trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | rollout/return horizon과 episode termination; exact n-step/discount는 exact value was not selected from the PDF body. | In the absence of such assumptions, the expected value of r for any given time step may be a function of time ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 environment step이 분리되며 deployment control rate는 별도 contract다. | In particular, assume a net N is trained on an episode-by-episode basis, where each episode consists of k time steps, during which ... | Hz/fps, inference time and control rate |
| Memory | replay/rollout buffer와 actor/critic parameters; recurrent history 여부 확인 필요. | In the absence of such assumptions, the expected value of r for any given time step may be a function of time ... | window and reset |
| Compute | environment interaction, value/policy update와 batch size가 비용을 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / 5. Episodic REINFORCE algorithms - extractive body cue:** In particular, assume a net N is trained on an episode-by-episode basis, where each episode consists of k time steps, during which the units may ...
- **p. 8 / 5. Episodic REINFORCE algorithms - extractive body cue:** In particular, assume a net N is trained on an episode-by-episode basis, where each episode consists of k time steps, during which the units may ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** example, network, consists, Bernoulli-logistic, units, episodic, REINFORCE, algorithm, would, prescribe, weight, changes, according, rule, Awij, following, result, proved, Appendix, Theorem.
- **Relevant PDF headings:** 4. REINFORCE algorithms (p. 5); 5. Episodic REINFORCE algorithms (p. 8); 8. Algorithm performance and other issues (p. 15).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Policy / value representation | A more general formulation of such an episodic learning task is also possible, where reinforcement is delivered to the network at each ... | p. 9 (5. Episodic REINFORCE algorithms), p. 15 (8. Algorithm performance and other issues) |
| Rollout / target construction | In these studies, REINFORCE with reinforcement comparison was found to outperform all other algorithms investigated. | p. 15 (8. Algorithm performance and other issues), p. 17 (8. Algorithm performance and other issues) |
| Policy / value update | In those situations when it is known that unsatisfactory performance is being achieved it is reasonable to broaden this scale in order ... | p. 17 (8. Algorithm performance and other issues), p. 15 (8. Algorithm performance and other issues) |

## Failure and Ablation Link

- **p. 12 / 7. Compatibility with backpropagation - extractive body cue:** WILLIAMS effect of connectivity between units is ignored; each unit in the network tries to determine the effect of changes of its output on changes ...
- **p. 15 / 8. Algorithm performance and other issues - extractive body cue:** Some of the variants examined incorporated modifications designed to help defeat this often undesirable behavior.
- **p. 15 / 8. Algorithm performance and other issues - extractive body cue:** Williams and Peng (1991) have also investigated a number of variants of REINFORCE in nonassociative function-optimization tasks, using networks of Bernoulli units.
- **p. 18 / 8. Algorithm performance and other issues - extractive body cue:** A straightforward way to obtain a number of variants of REINFORCE is to vary the form of either of these factors.
- **p. 18 / 8. Algorithm performance and other issues - extractive body cue:** Furthermore, the corresponding strategy can be used to generate variants of REINFORCE in a number of other cases.
- **p. 19 / 8.5. Use of other local gradient estimates - extractive body cue:** But perhaps most significant of all is the fact that, in the sense given by Theorems 1 and 2, they climb an appropriate gradient without ...
- **p. 23 / 1 Og i - extractive body cue:** For any REINFORCE algorithm, E{zXwej I W} = ~j OE{r I W} Owij Proof E{Awij I W} = ~ E{Awijl W, X i = X} ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 9 (5. Episodic REINFORCE algorithms), p. 8 (5. Episodic REINFORCE algorithms), p. 8 (4. REINFORCE algorithms), p. 9 (5. Episodic REINFORCE algorithms), p. 7 (4. REINFORCE algorithms), p. 7 (4. REINFORCE algorithms), objective p. 7 (4. REINFORCE algorithms), p. 6 (4. REINFORCE algorithms), p. 9 (5. Episodic REINFORCE algorithms), p. 6 (4. REINFORCE algorithms), p. 7 (4. REINFORCE algorithms), p. 9 (5. Episodic REINFORCE algorithms), temporal p. 5 (3. The expected reinforcement performance criterion), p. 8 (5. Episodic REINFORCE algorithms), p. 9 (5. Episodic REINFORCE algorithms), p. 3 (2. Reinforcement-learning connectionist networks), p. 3 (2. Reinforcement-learning connectionist networks), p. 8 (5. Episodic REINFORCE algorithms).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (28 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** The special case of this algorithm when the reinforcement signal is limited to 0 and 1 coincides with the 2-action version of the linear reward-inaction (LR_I) stochastic learning automaton (Narendra ... (p. 7, 4. REINFORCE algorithms).
- **Objective/update evidence:** This results relates VwE{r I W}, the gradient in weight space of the performance measure E {r ] W}, to E {AW] W}, the average update vector in weight space, ... (p. 6, 4. REINFORCE algorithms).
- **Temporal/runtime evidence:** In the absence of such assumptions, the expected value of r for any given time step may be a function of time as well as of the history of the ... (p. 5, 3. The expected reinforcement performance criterion).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
