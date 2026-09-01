# Method - Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://roboticsconference.org/program/papers/10/; PDF retrieval source: https://roboticsconference.org/program/papers/10/. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (III. HALO), p. 4 (III. HALO), p. 3 (III. HALO), p. 1 (Abstract), p. 3 (III. HALO), p. 1 (I. INTRODUCTION)): For VQA supervision, the policy backbone is conditioned on the encoded history Mt, the current observation embedding xt, and the question u, and the answer is predicted via a VQA ...

## Method Body Digest

- **p. 4 / III. HALO - extractive body cue:** For VQA supervision, the policy backbone is conditioned on the encoded history Mt, the current observation embedding xt, and the question u, and the answer ...
- **p. 4 / III. HALO - extractive body cue:** Motor Action Reducing Model Drift via Sparsification Text Instruction OR Task Instruction Robot Trajectory Text Query Text Answer Put all breads in microwave How many ...
- **p. 3 / III. HALO - extractive body cue:** First, because attention aggregates information from all stored history Mt, the policy may attend to task-irrelevant details and incorporate them into decision-making, leading to spurious ...
- **p. 1 / Abstract - extractive body cue:** However, directly incorporating longcontext transformer architecture into imitation learning from offline data introduces two key challenges: (1) the policy may learn spurious correlations between the ...
- **p. 3 / III. HALO - extractive body cue:** We parameterize the visuomotor policy πθ(at / τt, l) with three main components: (i) modality-specific encoders consisting of an observation encoder gobs θ and an ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** First, policies may exploit spurious correlations between past observations and current actions, i.e., attending to information that correlates with expert behavior in the training data ...
- **p. 5 / III. HALO - extractive body cue:** To improve data quality, we use an additional language model to rate each pair on correctness with respect to the trajectory description and relevance to ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The VQA objective biases memory retrieval towards task-relevant information, whereas the action prediction objective may still access information needed for low-level control.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** To address these challenges, we propose HALO: HistoryAware visuomotor policy for LOng-horizon robotic imitation learning.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Across these settings, we show that VQA-induced task priors provide a general solution, improving absolute task success by 7% on average across diverse tasks and ...
- **p. 1 / Abstract - extractive body cue:** To address both challenges, we introduce HALO, a visuomotor policy with an attention-based memory retrieval mechanism for long-horizon control.

## Source Evidence Cues

- **p. 4 / III. HALO - extractive body cue:** For VQA supervision, the policy backbone is conditioned on the encoded history Mt, the current observation embedding xt, and the question u, and the answer ...
- **p. 4 / III. HALO - extractive body cue:** Motor Action Reducing Model Drift via Sparsification Text Instruction OR Task Instruction Robot Trajectory Text Query Text Answer Put all breads in microwave How many ...
- **p. 3 / III. HALO - extractive body cue:** First, because attention aggregates information from all stored history Mt, the policy may attend to task-irrelevant details and incorporate them into decision-making, leading to spurious ...
- **p. 1 / Abstract - extractive body cue:** However, directly incorporating longcontext transformer architecture into imitation learning from offline data introduces two key challenges: (1) the policy may learn spurious correlations between the ...
- **p. 3 / III. HALO - extractive body cue:** We parameterize the visuomotor policy πθ(at / τt, l) with three main components: (i) modality-specific encoders consisting of an observation encoder gobs θ and an ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** First, policies may exploit spurious correlations between past observations and current actions, i.e., attending to information that correlates with expert behavior in the training data ...
- **p. 5 / III. HALO - extractive body cue:** To improve data quality, we use an additional language model to rate each pair on correctness with respect to the trajectory description and relevance to ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | For VQA supervision, the policy backbone is conditioned on the encoded history Mt, the current observation embedding xt, and the question u, ... | p. 4 (III. HALO), p. 4 (III. HALO) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | Motor Action Reducing Model Drift via Sparsification Text Instruction OR Task Instruction Robot Trajectory Text Query Text Answer Put all breads in ... | p. 4 (III. HALO), p. 3 (III. HALO) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | First, because attention aggregates information from all stored history Mt, the policy may attend to task-irrelevant details and incorporate them into decision-making, ... | p. 3 (III. HALO), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / I. INTRODUCTION - extractive body cue:** The VQA objective biases memory retrieval towards task-relevant information, whereas the action prediction objective may still access information needed for low-level control.
- **p. 4 / III. HALO - extractive body cue:** In standard end-to-end imitation learning, the retrieval mechanism is trained solely through the action prediction objective.
- **p. 4 / III. HALO - extractive body cue:** For VQA supervision, the policy backbone is conditioned on the encoded history Mt, the current observation embedding xt, and the question u, and the answer ...
- **p. 5 / III. HALO - extractive body cue:** If the retrieved information improves action prediction or VQA accuracy, gradients flowing through the attention output increase the corresponding query-key similarities, reinforcing the selection of ...
- **p. 1 / Abstract - extractive body cue:** Concretely, it generates task-relevant, memory-dependent question-answer pairs from demonstration trajectories and trains the policy jointly with a video questionanswering objective, transferring VLM priors to the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Together, these results highlight the importance of learning to retrieve task-relevant information from memory and grounding retrieval in action prediction for long-horizon control.
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 1 (Abstract), p. 2 (I. INTRODUCTION), p. 4 (III. HALO), p. 4 (III. HALO), p. 5 (III. HALO), p. 5 (III. HALO).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | parameterize, visuomotor, policy, three, main, components, modality-specific, encoders, consisting, observation, encoder, gobs, action, gact | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | parameterize, visuomotor, policy, three, main, components, modality-specific, encoders, consisting, observation | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | address, challenges, HALO, HistoryAware, visuomotor, policy, LOng-horizon, robotic, imitation, learning | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | VQA, objective, biases, memory, retrieval, towards, task-relevant, information, whereas, action | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. HALO - extractive body cue:** We parameterize the visuomotor policy πθ(at / τt, l) with three main components: (i) modality-specific encoders consisting of an observation encoder gobs θ and an ...
- **p. 3 / III. HALO - extractive body cue:** Given Mt, the current embedding xt, and the task instruction l, the policy backbone fθ produces a latent state zt = fθ(Mt, xt, l), This ...
- **p. 4 / III. HALO - extractive body cue:** HALO learns a visuomotor policy that retrieves information from the past observations and actions to predict low-level robot actions (middle), guided by priors from vision-language ...
- **p. 4 / III. HALO - extractive body cue:** Motor Action Reducing Model Drift via Sparsification Text Instruction OR Task Instruction Robot Trajectory Text Query Text Answer Put all breads in microwave How many ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Under partial observability, the policy must retrieve relevant information from past observations stored in memory to predict correct low-level actions.
- **p. 2 / I. INTRODUCTION - extractive body cue:** The policy is co-trained to both imitate expert actions and answer questions about past observations.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Rather than attending to the full history, the policy retrieves the top-k most informative observations or actions via learned query-key matching and conditions exclusively in ...
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | Token Merging [40] compresses the history by merging tokens with similar embeddings that are temporally adjacent to maintain a fixed budget of ... | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | At each time step t, a query vector is computed from the current context, qt = fq(xt, l), while each memory element ... | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | Token Merging [40] compresses the history by merging tokens with similar embeddings that are temporally adjacent to maintain a fixed budget of ... | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | Standard Transformer 0.40 0.30 0.20 0.40 0.50 0.36 HALO 0.55 0.40 0.55 0.60 0.65 0.55 Scene Memory Transformer (SMT) [24] compresses the ... | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / I. INTRODUCTION - extractive body cue:** First, policies may exploit spurious correlations between past observations and current actions, i.e., attending to information that correlates with expert behavior in the training data ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** VQA, supervision, policy, backbone, conditioned, encoded, history, current, observation, embedding, question, answer, predicted, head, where, consists, shared, gobs, action, encoder.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | In addition, we measure manipulation and memory failures in real-world evaluations, finding that HALO reduces them by 8% and 25% absolute over ... | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Filtering / recovery | (Table II) We observe a similar trend in real-world settings, where HALO consistently outperforms the standard Transformer baseline by 19%. | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Monitoring / re-entry | Cotraining VQA and action prediction achieves 64% success, outperforming pretrain-then-finetune (44%) and no-VQA training (42%) by 20 and 22 points, respectively. | p. 8 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 8 / IV. EXPERIMENTS - extractive body cue:** We compare HALO against a variant trained without VQA supervision.
- **p. 8 / IV. EXPERIMENTS - extractive body cue:** The minimal gain from separate pretrain-then-finetune compared to no-VQA suggests that VQA knowledge is lost during fine-tuning, whereas co-training effectively shapes retrieval toward task-relevant information.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** However, HALO remains competitive without task-specific assumptions or hand-designed rules, making it versatile with less engineering effort across information types.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** This suggests that learning what to retrieve directly from data using HALO not only removes manually designed task-specific priors but also improves performance, possibly by ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2. HALO learns to retrieve diverse forms of task-relevant information from history, guided by priors distilled from vision-language foundation models. observations can amplify this ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** These results support our hypothesis that HALO reduces model drift (fewer manipulation failures)
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** In addition, we measure manipulation and memory failures in real-world evaluations, finding that HALO reduces them by 8% and 25% absolute over full attention in ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (III. HALO), p. 4 (III. HALO), p. 3 (III. HALO), p. 1 (Abstract), p. 3 (III. HALO), p. 1 (I. INTRODUCTION), objective p. 2 (I. INTRODUCTION), p. 4 (III. HALO), p. 4 (III. HALO), p. 5 (III. HALO), p. 1 (Abstract), p. 2 (I. INTRODUCTION), temporal p. 7 (IV. EXPERIMENTS), p. 3 (III. HALO), p. 4 (III. HALO), p. 5 (III. HALO), p. 7 (IV. EXPERIMENTS), p. 3 (III. HALO).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
