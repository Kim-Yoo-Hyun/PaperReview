# Method - Offline Reinforcement Learning with Implicit Q-Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=68n2s9ZJWF8; PDF retrieval source: https://arxiv.org/pdf/2110.06169. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 1 (ABSTRACT), p. 3 (3 PRELIMINARIES), p. 7 (3 PRELIMINARIES), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 7 (3 PRELIMINARIES)): The main insight in our work is that, instead of evaluating unseen actions from the latest policy, we can approximate the policy improvement step implicitly by treating the state value ...

## Method Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** The main insight in our work is that, instead of evaluating unseen actions from the latest policy, we can approximate the policy improvement step implicitly ...
- **p. 3 / 3 PRELIMINARIES - extractive body cue:** Off-policy RL methods based on approximate dynamic programming typically utilize a state-action value function (Q-function), referred to as Q(s, a), which corresponds to the discounted ...
- **p. 7 / 3 PRELIMINARIES - extractive body cue:** We will then compare IQL with state-of-theart single-step and multi-step algorithms on the D4RL (Fu et al., 2020) benchmark tasks, studying the degree to which ...
- **p. 1 / ABSTRACT - extractive body cue:** We propose a new offline RL method that never needs to evaluate actions outside of the dataset, but still enables the learned policy to improve ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This approach does not require explicit constraints or explicit regularization of out-ofdistribution actions during value function training, though our policy extraction step does implicitly enforce ...
- **p. 7 / 3 PRELIMINARIES - extractive body cue:** The dataset consists of 1 optimal trajectory and 99 trajectories with uniform random actions.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** (4) Our algorithm, implicit Q-Learning (IQL), aims to estimate this objective while evaluating the Qfunction only on the state-action pairs in the dataset.
- **p. 3 / 3 PRELIMINARIES - extractive body cue:** Like many recent offline RL methods, our work builds on approximate dynamic programming methods that minimize temporal difference error, according to the following loss: LT ...

## Design Rationale

- **p. 1 / ABSTRACT - extractive body cue:** We propose a new offline RL method that never needs to evaluate actions outside of the dataset, but still enables the learned policy to improve ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our method is easy to implement by making a small change to the loss function in a simple SARSA-like TD update and is computationally very ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The key idea in our method is to approximate an upper expectile of the distribution over values with respect to the distribution of dataset actions ...

## Source Evidence Cues

- **p. 1 / ABSTRACT - extractive body cue:** The main insight in our work is that, instead of evaluating unseen actions from the latest policy, we can approximate the policy improvement step implicitly ...
- **p. 3 / 3 PRELIMINARIES - extractive body cue:** Off-policy RL methods based on approximate dynamic programming typically utilize a state-action value function (Q-function), referred to as Q(s, a), which corresponds to the discounted ...
- **p. 7 / 3 PRELIMINARIES - extractive body cue:** We will then compare IQL with state-of-theart single-step and multi-step algorithms on the D4RL (Fu et al., 2020) benchmark tasks, studying the degree to which ...
- **p. 1 / ABSTRACT - extractive body cue:** We propose a new offline RL method that never needs to evaluate actions outside of the dataset, but still enables the learned policy to improve ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This approach does not require explicit constraints or explicit regularization of out-ofdistribution actions during value function training, though our policy extraction step does implicitly enforce ...
- **p. 7 / 3 PRELIMINARIES - extractive body cue:** The dataset consists of 1 optimal trajectory and 99 trajectories with uniform random actions.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** (4) Our algorithm, implicit Q-Learning (IQL), aims to estimate this objective while evaluating the Qfunction only on the state-action pairs in the dataset.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Fixed-data support | 온라인 탐색 없이 transition/action 분포를 정의한다 | offline trajectories와 metadata | dataset support, behavior distribution과 task return을 정리 | training batch/support | The main insight in our work is that, instead of evaluating unseen actions from the latest policy, we can approximate the policy ... | p. 1 (ABSTRACT), p. 3 (3 PRELIMINARIES) |
| Value / uncertainty update | dataset 밖 action의 과대추정을 억제한다 | batch transition과 value parameters | conservative, implicit, uncertainty 또는 behavior-regularized update를 수행 | Q/V/uncertainty estimate | Off-policy RL methods based on approximate dynamic programming typically utilize a state-action value function (Q-function), referred to as Q(s, a), which corresponds ... | p. 3 (3 PRELIMINARIES), p. 7 (3 PRELIMINARIES) |
| Policy extraction / deployment | 학습된 value를 실행 action으로 변환한다 | value와 behavior support | argmax, advantage weighting, sequence decoding 또는 constraint filtering을 적용 | dataset-supported action | We will then compare IQL with state-of-theart single-step and multi-step algorithms on the D4RL (Fu et al., 2020) benchmark tasks, studying the ... | p. 7 (3 PRELIMINARIES), p. 1 (ABSTRACT) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3 PRELIMINARIES - extractive body cue:** Like many recent offline RL methods, our work builds on approximate dynamic programming methods that minimize temporal difference error, according to the following loss: LT ...
- **p. 5 / 3 PRELIMINARIES - extractive body cue:** As shown in prior work, this objective learns a policy that maximizes the Q-values subject to a distribution constraint (Peters & Schaal, 2007; Peng et ...
- **p. 3 / 3 PRELIMINARIES - extractive body cue:** Most recent offline RL methods modify either the value function loss (above) to regularize the value function in a way that keeps the resulting policy ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This approach does not require explicit constraints or explicit regularization of out-ofdistribution actions during value function training, though our policy extraction step does implicitly enforce ...
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** Note that we can optimize this objective with stochastic gradient descent.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** Prior work (Brandfonbrener et al., 2021; Peng et al., 2019) has proposed directly using this objective to learn Qπβ, and then train the policy πψ ...
- **Formal bridge:** dataset transition (s,a,r,s′) -> dataset-supported policy action -> offline value with OOD control -> offline return and deployment safety.
- **Equation/algorithm anchors:** p. 4 (3 PRELIMINARIES), p. 5 (3 PRELIMINARIES), p. 5 (3 PRELIMINARIES), p. 3 (3 PRELIMINARIES), p. 2 (1 INTRODUCTION), p. 3 (3 PRELIMINARIES).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Off-policy, methods, approximate, dynamic, programming, typically, utilize, state-action, value, function, Q-function, referred, corresponds, discounted | dataset state/observation, action, reward와 return-to-go | body cue; exact tensor/frame verify |
| State/latent | Off-policy, methods, approximate, dynamic, programming, typically, utilize, state-action, value, function | Q/value 또는 sequence-policy state | body cue; notation verify |
| Action/output | offline, never, needs, evaluate, actions, outside, dataset, still, enables, learned | dataset-supported action sequence | body cue; unit/decoder verify |
| Objective/constraint | Like, many, recent, offline, methods, builds, approximate, dynamic, programming, minimize | offline value with OOD control | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3 PRELIMINARIES - extractive body cue:** Off-policy RL methods based on approximate dynamic programming typically utilize a state-action value function (Q-function), referred to as Q(s, a), which corresponds to the discounted ...
- **p. 7 / 3 PRELIMINARIES - extractive body cue:** When the static dataset is heavily corrupted by suboptimal actions, one-step policy evaluation results in a value function that degrades to zero far from the ...
- **p. 1 / ABSTRACT - extractive body cue:** The main insight in our work is that, instead of evaluating unseen actions from the latest policy, we can approximate the policy improvement step implicitly ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this work, we start from an observation that in-distribution constraints widely used in prior work might not be sufficient to avoid value function extrapolation, ...
- **p. 1 / ABSTRACT - extractive body cue:** We propose a new offline RL method that never needs to evaluate actions outside of the dataset, but still enables the learned policy to improve ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This approach does not require explicit constraints or explicit regularization of out-ofdistribution actions during value function training, though our policy extraction step does implicitly enforce ...
- **p. 3 / 3 PRELIMINARIES - extractive body cue:** This is important because out-of-distribution actions a′ can produce erroneous values for Qˆθ(s′, a′) in the above objective, often leading to overestimation as the policy ...
- **Normalized interface:** observation=dataset state/observation, action, reward와 return-to-go; state=Q/value 또는 sequence-policy state; output/action=dataset-supported action sequence.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | offline trajectory/discounted return horizon; deployment horizon과 분리한다. | 0.00 0.25 0.50 0.75 1.00 Gradient Steps (×106) 0 50 100 Episode Return antmaze-medium-play-v0 0.00 0.25 0.50 0.75 1.00 Gradient Steps (×106) ... | episode/sequence/action-chunk boundary |
| Rate / latency | training은 batch update, inference는 environment control tick; exact values 확인 필요. | To evaluate the finetuning capability of various RL algorithms, we first run offline RL on each dataset, then run 1M steps of ... | Hz/fps, inference time and control rate |
| Memory | fixed dataset, value/policy parameters와 optional context/history. | not recovered | window and reset |
| Compute | dataset size, conservative/value update와 sequence/action decoding이 비용을 결정한다. | 0.00 0.25 0.50 0.75 1.00 Gradient Steps (×106) 0 50 100 Episode Return antmaze-medium-play-v0 0.00 0.25 0.50 0.75 1.00 Gradient Steps (×106) ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 INTRODUCTION - extractive body cue:** This approach does not require explicit constraints or explicit regularization of out-ofdistribution actions during value function training, though our policy extraction step does implicitly enforce ...
- **p. 9 / 3 PRELIMINARIES - extractive body cue:** To evaluate the finetuning capability of various RL algorithms, we first run offline RL on each dataset, then run 1M steps of online RL, and ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We alternate between fitting this value function with expectile regression, and then using it to compute Bellman backups for training the Q-function.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** main, insight, instead, evaluating, unseen, actions, latest, policy, approximate, improvement, step, implicitly, treating, state, value, function, random, variable, randomness, determined.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Fixed-data support | We will then compare IQL with state-of-theart single-step and multi-step algorithms on the D4RL (Fu et al., 2020) benchmark tasks, studying the ... | p. 7 (3 PRELIMINARIES), p. 7 (3 PRELIMINARIES) |
| Value / uncertainty update | Figure 3: Estimating a larger expectile τ is crucial for antmaze tasks that require dynamical program- ming ('stitching'). Comparisons and baselines. We ... | p. 8 (Figure/Table caption), p. 8 (3 PRELIMINARIES) |
| Policy extraction / deployment | Table 2: Online finetuning results showing the initial perfor- mance after offline RL, and performance after 1M steps of on- line RL. ... | p. 9 (Figure/Table caption), p. 9 (3 PRELIMINARIES) |

## Failure and Ablation Link

- **p. 4 / 3 PRELIMINARIES - extractive body cue:** Crucially, we will show that it is possible to do this without ever querying the learned Q-function on out-of-sample actions by utilizing expectile regression.
- **p. 9 / 3 PRELIMINARIES - extractive body cue:** IQL is well-suited for online fine-tuning for two reasons.
- **p. 9 / 3 PRELIMINARIES - extractive body cue:** 5.3 ONLINE FINE-TUNING AFTER OFFLINE RL Dataset AWAC CQL IQL (Ours) antmaze-umaze-v0 56.7 →59.0 70.1 →99.4 86.7 →96.0 antmaze-umaze-diverse-v0 49.3 →49.0 31.1 →99.4 75.0 →84.0 ...
- **p. 5 / 3 PRELIMINARIES - extractive body cue:** TD learning (IQL): for each gradient step do ψ ←ψ -λV ∇ψLV (ψ) θ ←θ -λQ∇θLQ(θ) ˆθ ←(1 -α)ˆθ + αθ end for Policy extraction ...
- **p. 6 / 3 PRELIMINARIES - extractive body cue:** Note that the policy does not influence the value function in any way, and therefore extraction could be performed either concurrently or after TD learning.
- **p. 7 / 3 PRELIMINARIES - extractive body cue:** Since IQL (d) performs iterative dynamic programming, it correctly propagates the signal, and the values are no longer dominated by noise.
- **p. 7 / 3 PRELIMINARIES - extractive body cue:** When the static dataset is heavily corrupted by suboptimal actions, one-step policy evaluation results in a value function that degrades to zero far from the ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 1 (ABSTRACT), p. 3 (3 PRELIMINARIES), p. 7 (3 PRELIMINARIES), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 7 (3 PRELIMINARIES), objective p. 3 (3 PRELIMINARIES), p. 5 (3 PRELIMINARIES), p. 3 (3 PRELIMINARIES), p. 2 (1 INTRODUCTION), p. 4 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES), temporal p. 8 (3 PRELIMINARIES), p. 9 (3 PRELIMINARIES), p. 9 (3 PRELIMINARIES), p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION), p. 2 (2 RELATED WORK).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
