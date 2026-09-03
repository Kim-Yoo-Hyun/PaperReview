# Method - Conservative Q-Learning for Offline Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html; PDF retrieval source: https://arxiv.org/pdf/2006.04779. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (2 Preliminaries), p. 6 (2 Preliminaries), p. 2 (2 Preliminaries), p. 2 (2 Preliminaries), p. 4 (2 Preliminaries), p. 6 (2 Preliminaries)): 3.3 Safe Policy Improvement Guarantees In Section 3.1 we proposed novel objectives for Q-function training such that the expected value of a policy under the resulting Q-function lower bounds the ...

## Method Body Digest

- **p. 5 / 2 Preliminaries - extractive body cue:** 3.3 Safe Policy Improvement Guarantees In Section 3.1 we proposed novel objectives for Q-function training such that the expected value of a policy under the ...
- **p. 6 / 2 Preliminaries - extractive body cue:** (6) The expression of ζ in Theorem 3.6 consists of two terms: the first term captures the decrease in policy performance in M, that occurs ...
- **p. 2 / 2 Preliminaries - extractive body cue:** S, A represent state and action spaces, T(s′/s, a) and r(s, a) represent the dynamics and reward function, and γ ∈(0, 1) represents the discount ...
- **p. 2 / 2 Preliminaries - extractive body cue:** Given a dataset D = {(s, a, rs′)} of tuples from trajectories collected under a behavior policy πβ: ˆQk+1 ←arg min Q Es,a,s′∼D  (r(s, ...
- **p. 4 / 2 Preliminaries - extractive body cue:** Frist, if ρ = Unif(a), then the first term in Equation 3 corresponds to a soft-maximum of the Q-values at any state s and gives ...
- **p. 6 / 2 Preliminaries - extractive body cue:** Our algorithm uses the CQL(H) (or CQL(R) in general) objective from the CQL framework for training the Q-function Qθ, which is parameterized by a neural ...
- **p. 4 / 2 Preliminaries - extractive body cue:** (4) Second, if ρ(a/s) is chosen to be the previous policy ˆπk-1, the first term in Equation 4 is replaced by an exponential weighted average ...
- **p. 6 / 2 Preliminaries - extractive body cue:** 2: for step t in {1, . . . , N} do 3: Train the Q-function using GQ gradient steps on objective from Equation 4 ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** We propose a novel method for learning such conservative Qfunctions via a simple modification to standard value-based RL algorithms.
- **p. 2 / 1 Introduction - extractive body cue:** The key idea behind our method is to minimize values under an appropriately chosen distribution over state-action tuples, and then further tighten this bound by ...
- **p. 5 / 2 Preliminaries - extractive body cue:** 3.3 Safe Policy Improvement Guarantees In Section 3.1 we proposed novel objectives for Q-function training such that the expected value of a policy under the ...

## Source Evidence Cues

- **p. 5 / 2 Preliminaries - extractive body cue:** 3.3 Safe Policy Improvement Guarantees In Section 3.1 we proposed novel objectives for Q-function training such that the expected value of a policy under the ...
- **p. 6 / 2 Preliminaries - extractive body cue:** (6) The expression of ζ in Theorem 3.6 consists of two terms: the first term captures the decrease in policy performance in M, that occurs ...
- **p. 2 / 2 Preliminaries - extractive body cue:** S, A represent state and action spaces, T(s′/s, a) and r(s, a) represent the dynamics and reward function, and γ ∈(0, 1) represents the discount ...
- **p. 2 / 2 Preliminaries - extractive body cue:** Given a dataset D = {(s, a, rs′)} of tuples from trajectories collected under a behavior policy πβ: ˆQk+1 ←arg min Q Es,a,s′∼D  (r(s, ...
- **p. 4 / 2 Preliminaries - extractive body cue:** Frist, if ρ = Unif(a), then the first term in Equation 3 corresponds to a soft-maximum of the Q-values at any state s and gives ...
- **p. 6 / 2 Preliminaries - extractive body cue:** Our algorithm uses the CQL(H) (or CQL(R) in general) objective from the CQL framework for training the Q-function Qθ, which is parameterized by a neural ...
- **p. 4 / 2 Preliminaries - extractive body cue:** (4) Second, if ρ(a/s) is chosen to be the previous policy ˆπk-1, the first term in Equation 4 is replaced by an exponential weighted average ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Fixed-data support | 온라인 탐색 없이 transition/action 분포를 정의한다 | offline trajectories와 metadata | dataset support, behavior distribution과 task return을 정리 | training batch/support | 3.3 Safe Policy Improvement Guarantees In Section 3.1 we proposed novel objectives for Q-function training such that the expected value of a ... | p. 5 (2 Preliminaries), p. 6 (2 Preliminaries) |
| Value / uncertainty update | dataset 밖 action의 과대추정을 억제한다 | batch transition과 value parameters | conservative, implicit, uncertainty 또는 behavior-regularized update를 수행 | Q/V/uncertainty estimate | (6) The expression of ζ in Theorem 3.6 consists of two terms: the first term captures the decrease in policy performance in ... | p. 6 (2 Preliminaries), p. 2 (2 Preliminaries) |
| Policy extraction / deployment | 학습된 value를 실행 action으로 변환한다 | value와 behavior support | argmax, advantage weighting, sequence decoding 또는 constraint filtering을 적용 | dataset-supported action | S, A represent state and action spaces, T(s′/s, a) and r(s, a) represent the dynamics and reward function, and γ ∈(0, 1) ... | p. 2 (2 Preliminaries), p. 2 (2 Preliminaries) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 2 Preliminaries - extractive body cue:** 2: for step t in {1, . . . , N} do 3: Train the Q-function using GQ gradient steps on objective from Equation 4 ...
- **p. 3 / 2 Preliminaries - extractive body cue:** If we only require that the expected value of the ˆQπ under π(a/s) lower-bound V π, we can improve the bound by introducing an additional ...
- **p. 5 / 2 Preliminaries - extractive body cue:** In Theorem 3.5, we first show that CQL (Equation 2) optimizes a well-defined penalized RL empirical objective.
- **p. 2 / 2 Preliminaries - extractive body cue:** The goal in reinforcement learning is to learn a policy that maximizes the expected cumulative discounted reward in a Markov decision process (MDP), which is ...
- **p. 2 / 1 Introduction - extractive body cue:** The key idea behind our method is to minimize values under an appropriately chosen distribution over state-action tuples, and then further tighten this bound by ...
- **p. 3 / 2 Preliminaries - extractive body cue:** Intuitively, since Equation 2 maximizes Q-values under the behavior policy ˆπβ, Q-values for actions that are likely under ˆπβ might be overestimated, and hence ˆQπ ...
- **Formal bridge:** dataset transition (s,a,r,s′) -> dataset-supported policy action -> offline value with OOD control -> offline return and deployment safety.
- **Equation/algorithm anchors:** p. 6 (2 Preliminaries), p. 5 (2 Preliminaries), p. 3 (2 Preliminaries), p. 4 (2 Preliminaries), p. 6 (2 Preliminaries), p. 1 (Abstract).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | represent, state, action, spaces, dynamics, reward, function, represents, discount, factor, behavior, policy, dataset, discounted | dataset state/observation, action, reward와 return-to-go | body cue; exact tensor/frame verify |
| State/latent | represent, state, action, spaces, dynamics, reward, function, represents, discount, factor | Q/value 또는 sequence-policy state | body cue; notation verify |
| Action/output | novel, learning, conservative, Qfunctions, simple, modification, standard, value-based, algorithms, idea | dataset-supported action sequence | body cue; unit/decoder verify |
| Objective/constraint | step, Train, Q-function, gradient, steps, objective, Equation, CQL, Use, Q-learning | offline value with OOD control | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 2 Preliminaries - extractive body cue:** S, A represent state and action spaces, T(s′/s, a) and r(s, a) represent the dynamics and reward function, and γ ∈(0, 1) represents the discount ...
- **p. 2 / 2 Preliminaries - extractive body cue:** However, the policy may suffer from state distribution shift at test time.
- **p. 3 / 2 Preliminaries - extractive body cue:** Our choice of penalty is to minimize the expected Qvalue under a particular distribution of state-action pairs, µ(s, a).
- **p. 3 / 2 Preliminaries - extractive body cue:** Intuitively, since Equation 2 maximizes Q-values under the behavior policy ˆπβ, Q-values for actions that are likely under ˆπβ might be overestimated, and hence ˆQπ ...
- **p. 4 / 2 Preliminaries - extractive body cue:** (4) Second, if ρ(a/s) is chosen to be the previous policy ˆπk-1, the first term in Equation 4 is replaced by an exponential weighted average ...
- **p. 5 / 2 Preliminaries - extractive body cue:** When function approximation or sampling error makes OOD actions have higher learned Q-values, CQL backups are expected to be more robust, in that the policy ...
- **p. 5 / 2 Preliminaries - extractive body cue:** Theorem 3.3 shows that any variant of the CQL family learns Q-value estimates that lower-bound the actual Q-function under the action-distribution defined by the policy, ...
- **Normalized interface:** observation=dataset state/observation, action, reward와 return-to-go; state=Q/value 또는 sequence-policy state; output/action=dataset-supported action sequence.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | offline trajectory/discounted return horizon; deployment horizon과 분리한다. | 0 20 40 60 80 100 Training Iterations 20 15 10 5 0 5 10 15 Return Pong QR-DQN REM CQL 0 ... | episode/sequence/action-chunk boundary |
| Rate / latency | training은 batch update, inference는 environment control tick; exact values 확인 필요. | Interaction with the real world can be costly and dangerous, and the quantities of data that can be gathered online are substantially ... | Hz/fps, inference time and control rate |
| Memory | fixed dataset, value/policy parameters와 optional context/history. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | dataset size, conservative/value update와 sequence/action decoding이 비용을 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 2 Preliminaries - extractive body cue:** 3.3 Safe Policy Improvement Guarantees In Section 3.1 we proposed novel objectives for Q-function training such that the expected value of a policy under the ...
- **p. 2 / 2 Preliminaries - extractive body cue:** Given a dataset D = {(s, a, rs′)} of tuples from trajectories collected under a behavior policy πβ: ˆQk+1 ←arg min Q Es,a,s′∼D  (r(s, ...
- **p. 6 / 2 Preliminaries - extractive body cue:** Our algorithm uses the CQL(H) (or CQL(R) in general) objective from the CQL framework for training the Q-function Qθ, which is parameterized by a neural ...
- **p. 1 / 1 Introduction - extractive body cue:** However, applying RL to real-world problems consistently poses practical challenges: in contrast to the kinds of data-driven methods that have been successful in supervised learning ...
- **p. 2 / 1 Introduction - extractive body cue:** CQL can be implemented with less than 20 lines of code on top of a number of standard, online RL algorithms [21, 9], simply by ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Safe, Policy, Improvement, Guarantees, Section, novel, objectives, Q-function, training, expected, value, under, resulting, lower, bounds, actual, performance, expression, Theorem, consists.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Fixed-data support | CQL outperforms prior methods by as much as 2-5x on many benchmark tasks, and is the only method that can outperform simple ... | p. 2 (1 Introduction), p. 1 (Abstract) |
| Value / uncertainty update | Table 5: Average return obtained by CQL(H), and CQL(ρ) on three D4RL MuJoCo environments. Observe that on these environments, CQL(H) generally outperforms ... | p. 30 (Figure/Table caption), p. 31 (Figure/Table caption) |
| Policy extraction / deployment | Table 2: Normalized scores of all methods on AntMaze, Adroit, and kitchen domains from D4RL, averaged across 4 seeds. On the harder ... | p. 8 (Figure/Table caption), p. 31 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: Difference between policy values predicted by each algorithm and the true policy value for CQL, a variant of CQL that uses Equation 1, ...
- **p. 1 / Abstract - extractive body cue:** Offline RL algorithms promise to learn effective policies from previously-collected, static datasets without further interaction.
- **p. 4 / 2 Preliminaries - extractive body cue:** Frist, if ρ = Unif(a), then the first term in Equation 3 corresponds to a soft-maximum of the Q-values at any state s and gives ...
- **p. 5 / 2 Preliminaries - extractive body cue:** In Appendix A, we discuss an additional variant of CQL, drawing connections to distributionally robust optimization [45].
- **p. 5 / 2 Preliminaries - extractive body cue:** find that this variant can be more stable with high-dimensional action spaces (e.g., Table 2) where it is challenging to estimate log P a exp ...
- **p. 6 / 2 Preliminaries - extractive body cue:** 4 Practical Algorithm and Implementation Details Algorithm 1 Conservative Q-Learning (both variants) 1: Initialize Q-function, Qθ, and optionally a policy, πφ.
- **p. 6 / 2 Preliminaries - extractive body cue:** 2: for step t in {1, . . . , N} do 3: Train the Q-function using GQ gradient steps on objective from Equation 4 ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (2 Preliminaries), p. 6 (2 Preliminaries), p. 2 (2 Preliminaries), p. 2 (2 Preliminaries), p. 4 (2 Preliminaries), p. 6 (2 Preliminaries), objective p. 6 (2 Preliminaries), p. 3 (2 Preliminaries), p. 5 (2 Preliminaries), p. 2 (2 Preliminaries), p. 2 (1 Introduction), p. 3 (2 Preliminaries), temporal p. 9 (5 Related Work), p. 1 (1 Introduction), p. 2 (2 Preliminaries), p. 2 (1 Introduction), p. 3 (2 Preliminaries), p. 3 (2 Preliminaries).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (31 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** S, A represent state and action spaces, T(s′/s, a) and r(s, a) represent the dynamics and reward function, and γ ∈(0, 1) represents the discount factor. πβ(a/s) represents the behavior ... (p. 2, 2 Preliminaries).
- **Objective/update evidence:** In Theorem 3.5, we first show that CQL (Equation 2) optimizes a well-defined penalized RL empirical objective. (p. 5, 2 Preliminaries).
- **Temporal/runtime evidence:** Since D typically does not contain all possible transitions (s, a, s′), the policy evaluation step actually uses an empirical Bellman operator that only backs up a single sample. (p. 2, 2 Preliminaries).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
