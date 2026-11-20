# Method - Mastering diverse control tasks through world models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (40 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2301.04104; PDF retrieval source: https://arxiv.org/pdf/2301.04104. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 3 (Abstract), p. 4 (Abstract), p. 3 (Abstract), p. 6 (Abstract), p. 6 (Abstract), p. 4 (Abstract)): The algorithm consists of three neural networks: the world model predicts the outcomes of potential actions, the critic judges the value of each outcome, and the actor chooses actions to ...

## Method Body Digest

- **p. 3 / Abstract - extractive body cue:** The algorithm consists of three neural networks: the world model predicts the outcomes of potential actions, the critic judges the value of each outcome, and ...
- **p. 4 / Abstract - extractive body cue:** The world model learns an understanding of the underlying structure of each environment. ht and zt forms the model state from which we predict rewards ...
- **p. 3 / Abstract - extractive body cue:** Then, a sequence model with recurrent state ht predicts the sequence of these representations given past actions at-1.
- **p. 6 / Abstract - extractive body cue:** The critic replay loss uses the imagination returns Rλ t at the start states of the imagination rollouts as on-policy value annotations for the replay ...
- **원문 대조:** 이산·연속 action 모두 REINFORCE 추정량을 사용한다. Actor 목적에는 return-minus-value를 max(1,S)로 나눈 stop-gradient 가중 log-policy 항과 entropy 항이 포함된다. ([PDF p. 6](https://arxiv.org/pdf/2301.04104#page=6), Actor learning, Eq. (6)).
- **p. 4 / Abstract - extractive body cue:** Given a sequence batch of inputs x1:T, actions a1:T, rewards r1:T, and continuation flags c1:T, the world model parameters ϕ are optimized end-to-end to minimize ...
- **p. 5 / Abstract - extractive body cue:** To consider rewards beyond the prediction horizon T = 16, the critic learns to approximate the distribution of returns28 for each state under the current ...
- **p. 7 / Abstract - extractive body cue:** Note that the loss only depends on the probabilities assigned to the bins but not on the continuous values associated with the bin locations, decoupling ...

## Design Rationale

- **p. 1 / Abstract - extractive body cue:** We present DreamerV3, a general algorithm that outperforms specialized methods across over 150 diverse tasks, with a single configuration.
- **p. 2 / Abstract - extractive body cue:** We present Dreamer, a general algorithm that outperforms specialized expert algorithms across a wide range of domains while using fixed hyperparameters, making reinforcement learning readily ...
- **p. 3 / Abstract - extractive body cue:** Learning algorithm We present the third generation of the Dreamer algorithm21,22.

## Source Evidence Cues

- **p. 3 / Abstract - extractive body cue:** The algorithm consists of three neural networks: the world model predicts the outcomes of potential actions, the critic judges the value of each outcome, and ...
- **p. 4 / Abstract - extractive body cue:** The world model learns an understanding of the underlying structure of each environment. ht and zt forms the model state from which we predict rewards ...
- **p. 3 / Abstract - extractive body cue:** Then, a sequence model with recurrent state ht predicts the sequence of these representations given past actions at-1.
- **p. 6 / Abstract - extractive body cue:** The critic replay loss uses the imagination returns Rλ t at the start states of the imagination rollouts as on-policy value annotations for the replay ...
- **원문 대조:** 이산·연속 action 모두 REINFORCE 추정량을 사용한다. Actor 목적에는 return-minus-value를 max(1,S)로 나눈 stop-gradient 가중 log-policy 항과 entropy 항이 포함된다. ([PDF p. 6](https://arxiv.org/pdf/2301.04104#page=6), Actor learning, Eq. (6)).
- **p. 4 / Abstract - extractive body cue:** Given a sequence batch of inputs x1:T, actions a1:T, rewards r1:T, and continuation flags c1:T, the world model parameters ϕ are optimized end-to-end to minimize ...
- **p. 5 / Abstract - extractive body cue:** To consider rewards beyond the prediction horizon T = 16, the critic learns to approximate the distribution of returns28 for each state under the current ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | The algorithm consists of three neural networks: the world model predicts the outcomes of potential actions, the critic judges the value of ... | p. 3 (Abstract), p. 4 (Abstract) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | The world model learns an understanding of the underlying structure of each environment. ht and zt forms the model state from which ... | p. 4 (Abstract), p. 3 (Abstract) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | Then, a sequence model with recurrent state ht predicts the sequence of these representations given past actions at-1. | p. 3 (Abstract), p. 6 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / Abstract - extractive body cue:** Given a sequence batch of inputs x1:T, actions a1:T, rewards r1:T, and continuation flags c1:T, the world model parameters ϕ are optimized end-to-end to minimize ...
- **p. 7 / Abstract - extractive body cue:** Note that the loss only depends on the probabilities assigned to the bins but not on the continuous values associated with the bin locations, decoupling ...
- **p. 6 / Abstract - extractive body cue:** To be robust to these outliers, we compute the range from the 5th to the 95th return percentile over the return batch and smooth out ...
- **p. 7 / Abstract - extractive body cue:** The network is then trained to minimize the categorical cross entropy loss for classification with soft targets.
- **p. 6 / Abstract - extractive body cue:** The critic replay loss uses the imagination returns Rλ t at the start states of the imagination rollouts as on-policy value annotations for the replay ...
- **p. 4 / Abstract - extractive body cue:** The two losses differ in the stop-gradient operator sg(·) and their loss scale.
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 4 (Abstract), p. 5 (Abstract), p. 7 (Abstract), p. 5 (Abstract), p. 6 (Abstract), p. 3 (Abstract).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | world, model, encodes, sensory, inputs, discrete, representations, predicted, sequence, recurrent, state, given, actions, consider | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | world, model, encodes, sensory, inputs, discrete, representations, predicted, sequence, recurrent | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | present, DreamerV3, general, algorithm, outperforms, specialized, methods, across, over, diverse | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | Given, sequence, batch, inputs, actions, rewards, continuation, flags, world, model | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / Abstract - extractive body cue:** The world model encodes sensory inputs into discrete representations zt that are predicted by a sequence model with recurrent state ht given actions at.
- **p. 5 / Abstract - extractive body cue:** To consider rewards beyond the prediction horizon T = 16, the critic learns to approximate the distribution of returns28 for each state under the current ...
- **p. 2 / Abstract - extractive body cue:** These specialized algorithms target the unique challenges posed by different application domains, such as continuous control6, discrete actions7,8, sparse rewards9, image inputs10, spatial environments11, and ...
- **p. 3 / Abstract - extractive body cue:** World model learning The world model learns compact representations of sensory inputs through autoencoding23 and enables planning by predicting future representations and rewards for potential ...
- **p. 4 / Abstract - extractive body cue:** The world model learns an understanding of the underlying structure of each environment. ht and zt forms the model state from which we predict rewards ...
- **p. 4 / Abstract - extractive body cue:** Given a sequence batch of inputs x1:T, actions a1:T, rewards r1:T, and continuation flags c1:T, the world model parameters ϕ are optimized end-to-end to minimize ...
- **p. 5 / Abstract - extractive body cue:** Moreover, we transform vector observations using the symlog function described later, to prevent large inputs and large reconstruction gradients, further stabilizing the trade-off with the ...
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | Episodes last until the player dies or up to 36000 steps equaling 30 minutes, during which the player needs to discover a ... | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | Given 5 context images and the full action sequence, the model predicts 45 frames into the future without access to intermediate images. | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | Episodes last until the player dies or up to 36000 steps equaling 30 minutes, during which the player needs to discover a ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / Abstract - extractive body cue:** The critic replay loss uses the imagination returns Rλ t at the start states of the imagination rollouts as on-policy value annotations for the replay ...
- **p. 10 / Abstract - extractive body cue:** Because of the training time in this complex domain, extensive tuning would be difficult for Minecraft.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** algorithm, consists, three, neural, networks, world, model, predicts, outcomes, potential, actions, critic, judges, value, outcome, actor, chooses, reach, most, valuable.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | Dreamer sets a new state-of-the-art on this benchmark, outperforming D4PG, DMPO, and MPO33. • Visual Control This benchmark consists of 20 continuous ... | p. 9 (Abstract), p. 9 (Abstract) |
| Filtering / recovery | Dreamer establishes a new state-of-the-art on this benchmark, outperforming DrQ-v2 and CURL47, which are specialized to visual environments and leverage data augmentation. | p. 9 (Abstract), p. 9 (Abstract) |
| Monitoring / re-entry | Figure 9: Item success rates as a percentage of episodes. Dreamer obtains items at substantially higher rates than the baselines and continues ... | p. 24 (Figure/Table caption), p. 2 (Abstract) |

## Failure and Ablation Link

- **p. 9 / Abstract - extractive body cue:** 0 50 100 Env steps (%) 0 50 100 Return (%) 14 task mean Dreamer No obs symlog No retnorm (advnorm) No symexp twohot (Huber) ...
- **p. 10 / Abstract - extractive body cue:** This finding could allow for future algorithm variants that leverage pretraining on unsupervised data.
- **p. 10 / Abstract - extractive body cue:** To investigate the effect of the world model, we ablate the learning signals of Dreamer by stopping either the task-specific reward and value prediction gradients ...
- **p. 1 / Abstract - extractive body cue:** Applied out of the box, Dreamer is the first algorithm to collect diamonds in Minecraft from scratch without human data or curricula.
- **p. 1 / Abstract - extractive body cue:** Our work allows solving challenging control problems without extensive experimentation, making reinforcement learning broadly applicable.
- **p. 2 / Abstract - extractive body cue:** Creating a general algorithm that learns to master new domains without having to be reconfigured has been a central challenge in artificial intelligence and would ...
- **p. 3 / Abstract - extractive body cue:** The actor and critic predict actions at and values vt and learn from trajectories of abstract representations predicted by the world model. problem without human ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (Abstract), p. 4 (Abstract), p. 3 (Abstract), p. 6 (Abstract), p. 6 (Abstract), p. 4 (Abstract), objective p. 4 (Abstract), p. 7 (Abstract), p. 6 (Abstract), p. 7 (Abstract), p. 6 (Abstract), p. 4 (Abstract), temporal p. 10 (Abstract), p. 4 (Abstract), p. 4 (Abstract), p. 8 (Abstract), p. 1 (Abstract), p. 2 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (40 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** The world model learns an understanding of the underlying structure of each environment. ht and zt forms the model state from which we predict rewards rt and episode continuation flags ... (p. 4, Abstract).
- **Objective/update evidence:** Given a sequence batch of inputs x1:T, actions a1:T, rewards r1:T, and continuation flags c1:T, the world model parameters ϕ are optimized end-to-end to minimize the prediction loss Lpred, the ... (p. 4, Abstract).
- **Temporal/runtime evidence:** Episodes last until the player dies or up to 36000 steps equaling 30 minutes, during which the player needs to discover a sequence of 12 items from sparse rewards by ... (p. 10, Abstract).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
