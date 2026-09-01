# Method - Apprenticeship Learning via Inverse Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ai.stanford.edu/~pabbeel/irl/; PDF retrieval source: https://ai.stanford.edu/~ang/papers/icml04-apprentice.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3. Algorithm), p. 3 (3. Algorithm), p. 4 (3.1. A simpler algorithm), p. 4 (3. Algorithm)): (Whether the algorithm terminates is discussed in Section 4.) Then directly from Eq.

## Method Body Digest

- **p. 3 / 3. Algorithm - extractive PDF cue:** (Whether the algorithm terminates is discussed in Section 4.) Then directly from Eq.
- **p. 3 / 3. Algorithm - extractive PDF cue:** (The SVM problem is a quadratic programming problem (QP), so we can also use any generic QP solver.) In Figure 1 we show an example ...
- **p. 4 / 3.1. A simpler algorithm - extractive PDF cue:** Briefly, the projection method replaces step 2 of the algorithm with the following: - Set ¯µ(i-1) = ¯µ(i-2)+ (µ(i-1)-¯µ(i-2))T (µE-¯µ(i-2)) (µ(i-1)-¯µ(i-2))T (µ(i-1)-¯µ(i-2))(µ(i-1)-¯µ(i-2)) (This computes the ...
- **p. 4 / 3. Algorithm - extractive PDF cue:** The performance guarantees of our algorithm only depend on (approximately) matching the feature expectations, not on recovering the true underlying reward function.
- **p. 3 / 3. Algorithm - extractive PDF cue:** Three iterations for max-margin algorithm. the reward function being optimized by the expert.
- **p. 3 / 3. Algorithm - extractive PDF cue:** This step is similar to one used in (Ng & Russell, 2000), but unlike the algorithms given there, because of the 2-norm constraint on w ...
- **p. 4 / 3. Algorithm - extractive PDF cue:** 6-9), this policy attains performance near that of the expert's on the unknown reward function.6 Note that although we called one step of our algorithm ...
- **p. 2 / 2. Preliminaries - extractive PDF cue:** A policy π is a mapping from states to probability distributions over actions.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** In this paper, we assume that the expert is trying (without necessarily succeeding) to optimize an unknown reward function that can be expressed as a ...
- **p. 3 / 3. Algorithm - extractive PDF cue:** (The SVM problem is a quadratic programming problem (QP), so we can also use any generic QP solver.) In Figure 1 we show an example ...

## Source Evidence Cues

- **p. 3 / 3. Algorithm - extractive PDF cue:** (Whether the algorithm terminates is discussed in Section 4.) Then directly from Eq.
- **p. 3 / 3. Algorithm - extractive PDF cue:** (The SVM problem is a quadratic programming problem (QP), so we can also use any generic QP solver.) In Figure 1 we show an example ...
- **p. 4 / 3.1. A simpler algorithm - extractive PDF cue:** Briefly, the projection method replaces step 2 of the algorithm with the following: - Set ¯µ(i-1) = ¯µ(i-2)+ (µ(i-1)-¯µ(i-2))T (µE-¯µ(i-2)) (µ(i-1)-¯µ(i-2))T (µ(i-1)-¯µ(i-2))(µ(i-1)-¯µ(i-2)) (This computes the ...
- **p. 4 / 3. Algorithm - extractive PDF cue:** The performance guarantees of our algorithm only depend on (approximately) matching the feature expectations, not on recovering the true underlying reward function.
- **Detected method headings:** 3. Algorithm (p. 3); 3.1. A simpler algorithm (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Demonstration representation | expert trajectory를 training pair/context로 정렬한다 | observation history, goal, expert action | temporal alignment, relabeling 또는 latent context construction을 수행 | training sample/context | (Whether the algorithm terminates is discussed in Section 4.) Then directly from Eq. | p. 3 (3. Algorithm), p. 3 (3. Algorithm) |
| Policy fitting | expert action distribution을 학습한다 | context와 action target | behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화 | policy/action distribution | (The SVM problem is a quadratic programming problem (QP), so we can also use any generic QP solver.) In Figure 1 we ... | p. 3 (3. Algorithm), p. 4 (3.1. A simpler algorithm) |
| Closed-loop rollout | distribution shift와 recovery를 확인한다 | current observation/history | action/chunk을 실행하고 feedback으로 다음 prediction을 갱신 | trajectory/failure signal | Briefly, the projection method replaces step 2 of the algorithm with the following: - Set ¯µ(i-1) = ¯µ(i-2)+ (µ(i-1)-¯µ(i-2))T (µE-¯µ(i-2)) (µ(i-1)-¯µ(i-2))T (µ(i-1)-¯µ(i-2))(µ(i-1)-¯µ(i-2)) ... | p. 4 (3.1. A simpler algorithm), p. 4 (3. Algorithm) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3. Algorithm - extractive PDF cue:** Three iterations for max-margin algorithm. the reward function being optimized by the expert.
- **p. 3 / 3. Algorithm - extractive PDF cue:** This step is similar to one used in (Ng & Russell, 2000), but unlike the algorithms given there, because of the 2-norm constraint on w ...
- **p. 4 / 3. Algorithm - extractive PDF cue:** The performance guarantees of our algorithm only depend on (approximately) matching the feature expectations, not on recovering the true underlying reward function.
- **p. 4 / 3. Algorithm - extractive PDF cue:** 6-9), this policy attains performance near that of the expert's on the unknown reward function.6 Note that although we called one step of our algorithm ...
- **Formal bridge:** observation history o_{t−H:t} -> expert-like action/chunk a_{t:t+H} -> imitation or action-distribution loss -> closed-loop task success and robustness.
- **Equation/algorithm anchors:** p. 3 (3. Algorithm), p. 3 (3. Algorithm), p. 4 (3. Algorithm), p. 4 (3.1. A simpler algorithm).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | policy, mapping, states, probability, distributions, over, actions, value, Es0, Here, expectation, taken, respect, random | observation history와 expert trajectory/action | body cue; exact tensor/frame verify |
| State/latent | policy, mapping, states, probability, distributions, over, actions, value, Es0, Here | behavior policy와 temporal action context | body cue; notation verify |
| Action/output | assume, expert, trying, without, necessarily, succeeding, optimize, unknown, reward, function | predicted action 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Three, iterations, max-margin, algorithm, reward, function, being, optimized, expert, step | imitation or action-distribution loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 2. Preliminaries - extractive PDF cue:** A policy π is a mapping from states to probability distributions over actions.
- **p. 2 / 2. Preliminaries - extractive PDF cue:** The value of a policy π is Es0∼D[V π(s0)] = E[P∞ t=0 γtR(st)/π] (1) = E[P∞ t=0 γtw · φ(st)/π] (2) = w · E[P∞ ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Given a reward function and the MDPs state transition probabilities, the value function and optimal policy are exactly determined.
- **p. 1 / 1. Introduction - extractive PDF cue:** Most of these methods try to directly mimic the demonstrator by applying a supervised learning algorithm to learn a direct mapping from the states to ...
- **p. 3 / 2. Preliminaries - extractive PDF cue:** For simplicity of exposition, we will assume that the RL algorithm returns the optimal policy.
- **p. 3 / 3. Algorithm - extractive PDF cue:** To accomplish this, we will find a policy ˜π such that ∥µ(˜π) -µE∥2 ≤ϵ.
- **p. 4 / 3. Algorithm - extractive PDF cue:** Further, by "mixing" together the policies π(i) according to the mixture weights λi as discussed previously, we obtain a policy whose feature expectations are given ...
- **Normalized interface:** observation=observation history와 expert trajectory/action; state=behavior policy와 temporal action context; output/action=predicted action 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single-step 또는 action chunk/trajectory horizon; exact chunk length는 exact value not recovered from the selected body cues. | The "parameterized policy stochastic" uses a stochastic policy, with the probability of each action constant over each macrocell and set to the ... | episode/sequence/action-chunk boundary |
| Rate / latency | training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인. | We ran the algorithm once using all 64 features, and once using only the features that truly correspond to non-zero rewards.8 We ... | Hz/fps, inference time and control rate |
| Memory | current observation, temporal history 또는 recurrent/sequence context. | not recovered | window and reset |
| Compute | backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Whether, algorithm, terminates, discussed, Section, Then, directly, SVM, problem, quadratic, programming, generic, solver, Figure, example, what, first, three, iterations, could.
- **Relevant PDF headings:** 3. Algorithm (p. 3); 3.1. A simpler algorithm (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Demonstration representation | The simulation runs at 10Hz, and in the experiments that follow, the expert's features were estimated from a single trajectory of 1200 ... | p. 6 (5.2. Car driving simulation), p. 6 (5.2. Car driving simulation) |
| Policy fitting | Screenshot of driving simulator. learning a compact representation of the reward function, our algorithm significantly outperforms the other methods. | p. 6 (5.1. Gridworld), p. 5 (5.1. Gridworld) |
| Closed-loop rollout | Screenshot of driving simulator. learning a compact representation of the reward function, our algorithm significantly outperforms the other methods. | p. 6 (5.1. Gridworld), p. 4 (4. Theoretical results) |

## Failure and Ablation Link

- **p. 5 / 5.1. Gridworld - extractive PDF cue:** The agent has four actions to try to move in each of the four compass directions, but with 30% chance an action fails and results ...
- **p. 6 / 5.2. Car driving simulation - extractive PDF cue:** Nice: The highest priority is to avoid collisions than the "mimic the expert" algorithm initially.
- **p. 6 / 5.2. Car driving simulation - extractive PDF cue:** Since no "true" reward was ever specified or used in the experiments, we cannot report on the results of the algorithm according to R∗.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Feature expectations of teacher ˆµE and of selected/learned policy µ(˜π) (as estimated by Monte Carlo). and weights w corresponding to the reward function ...
- **p. 4 / 4. Theoretical results - extractive PDF cue:** In the case where the true reward function R∗does not lie exactly in the span of the basis functions φ, the algorithm still enjoys a ...
- **p. 4 / 4. Theoretical results - extractive PDF cue:** If the algorithm sometimes does not terminate, or if it sometimes takes a very (perhaps exponentially) large number of iterations to terminate, then it would ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3. Algorithm), p. 3 (3. Algorithm), p. 4 (3.1. A simpler algorithm), p. 4 (3. Algorithm), objective p. 3 (3. Algorithm), p. 3 (3. Algorithm), p. 4 (3. Algorithm), p. 4 (3. Algorithm), temporal p. 5 (5.1. Gridworld), p. 5 (5.1. Gridworld), p. 6 (5.2. Car driving simulation), p. 2 (2. Preliminaries), p. 2 (2. Preliminaries), p. 3 (3. Algorithm).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
