# Method - Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2004.02857; PDF retrieval source: https://arxiv.org/pdf/2004.02857. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 1 (3 Facebook AI Research), p. 1 (3 Facebook AI Research), p. 2 (1 Introduction)): Specifically, we develop a simple sequence-to-sequence baseline architecture as well as a cross-modal attentionbased model.

## Method Body Digest

- **p. 3 / 1 Introduction - extractive PDF cue:** Specifically, we develop a simple sequence-to-sequence baseline architecture as well as a cross-modal attentionbased model.
- **p. 3 / 1 Introduction - extractive PDF cue:** In this work, we develop a continuous setting that enables these types of studies and take a first step towards integrating VLN agents with control ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Our VLN-CE setting (b) lifts these assumptions by instantiating the task in continuous environments with low-level actions - providing a more realistic testbed for robot ...
- **p. 1 / 3 Facebook AI Research - extractive PDF cue:** To contextualize this new task, we develop models that mirror many of the advances made in prior settings as well as single-modality baselines.
- **p. 1 / 3 Facebook AI Research - extractive PDF cue:** We develop a language-guided navigation task set in a continuous 3D environment where agents must execute low-level actions to follow natural language navigation directions.
- **p. 2 / 1 Introduction - extractive PDF cue:** This is in contrast to the continuous stream of observations a real agent would encounter while moving. - Perfect localization.
- **p. 4 / 1 Introduction - extractive PDF cue:** To summarize our contributions, we: - Lift the VLN task to continuous 3D environments - removing many unrealistic assumptions imposed by the nav-graph-based representation.
- **p. 2 / 1 Introduction - extractive PDF cue:** How an actual agent might acquire and update such a topology in new environments is an open question. - Oracle navigation.

## Design Rationale

- **p. 3 / 1 Introduction - extractive PDF cue:** In this work, we develop a continuous setting that enables these types of studies and take a first step towards integrating VLN agents with control ...
- **p. 1 / 1 Introduction - extractive PDF cue:** This paradigm enables efficient data collection and high visual fidelity compared to 3D scanning or creating synthetic environments; however, scenes are only observed from a ...
- **p. 4 / 1 Introduction - extractive PDF cue:** To summarize our contributions, we: - Lift the VLN task to continuous 3D environments - removing many unrealistic assumptions imposed by the nav-graph-based representation.

## Source Evidence Cues

- **p. 3 / 1 Introduction - extractive PDF cue:** Specifically, we develop a simple sequence-to-sequence baseline architecture as well as a cross-modal attentionbased model.
- **p. 3 / 1 Introduction - extractive PDF cue:** In this work, we develop a continuous setting that enables these types of studies and take a first step towards integrating VLN agents with control ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Our VLN-CE setting (b) lifts these assumptions by instantiating the task in continuous environments with low-level actions - providing a more realistic testbed for robot ...
- **p. 1 / 3 Facebook AI Research - extractive PDF cue:** To contextualize this new task, we develop models that mirror many of the advances made in prior settings as well as single-modality baselines.
- **p. 1 / 3 Facebook AI Research - extractive PDF cue:** We develop a language-guided navigation task set in a continuous 3D environment where agents must execute low-level actions to follow natural language navigation directions.
- **p. 2 / 1 Introduction - extractive PDF cue:** This is in contrast to the continuous stream of observations a real agent would encounter while moving. - Perfect localization.
- **p. 4 / 1 Introduction - extractive PDF cue:** To summarize our contributions, we: - Lift the VLN task to continuous 3D environments - removing many unrealistic assumptions imposed by the nav-graph-based representation.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | Specifically, we develop a simple sequence-to-sequence baseline architecture as well as a cross-modal attentionbased model. | p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | In this work, we develop a continuous setting that enables these types of studies and take a first step towards integrating VLN ... | p. 3 (1 Introduction), p. 2 (1 Introduction) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | Our VLN-CE setting (b) lifts these assumptions by instantiating the task in continuous environments with low-level actions - providing a more realistic ... | p. 2 (1 Introduction), p. 1 (3 Facebook AI Research) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 Introduction - extractive PDF cue:** How an actual agent might acquire and update such a topology in new environments is an open question. - Oracle navigation.
- **p. 4 / 1 Introduction - extractive PDF cue:** This suggests prior results in VLN may be overly optimistic in terms of progress towards instruction-following robots functioning in the wild.
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 2 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | VLN-CE, setting, lifts, assumptions, instantiating, task, continuous, environments, low-level, actions, providing, more, realistic, testbed | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | VLN-CE, setting, lifts, assumptions, instantiating, task, continuous, environments, low-level, actions | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | develop, continuous, setting, enables, types, studies, take, first, step, towards | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | How, actual, agent, might, acquire, update, topology, environments, open, question | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive PDF cue:** Our VLN-CE setting (b) lifts these assumptions by instantiating the task in continuous environments with low-level actions - providing a more realistic testbed for robot ...
- **p. 3 / 1 Introduction - extractive PDF cue:** We perform a number of input-modality ablations to assess the biases and baselines in this new setting (including models without perception or instructions as suggested ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Taking a small step towards this goal, recent work has begun developing artificial agents that follow natural language navigation instructions in perceptually-rich, simulated environments [4,6].
- **p. 1 / 1 Introduction - extractive PDF cue:** Springing forth from the pages of science fiction and capturing the daydreams of weary chore-doers everywhere, the promise and potential of general-purpose robotic assistants that ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Moreover, the views the agent receives along the way are not well-posed by careful human operators as in the panoramas, but rather a consequence of ...
- **p. 2 / 1 Introduction - extractive PDF cue:** This is in contrast to the continuous stream of observations a real agent would encounter while moving. - Perfect localization.
- **p. 4 / 1 Introduction - extractive PDF cue:** Ours is the only to provide unconstrained navigation in real environments for crowdsourced instructions.
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | This model consists of a recurrent policy that takes a representation of the visual observation (depth and RGB) and instructions at each ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | Concretely, we can write the agent for time step t as ¯vt = mean-pool (Vt) , ¯dt = [d1, . . . ... | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | We train on all ground-truth paths until convergence on val-unseen (at most 30 epochs). | hardware, batch and throughput |

## Training vs Inference

- **p. 11 / 5 Experiments - extractive PDF cue:** We train on all ground-truth paths until convergence on val-unseen (at most 30 epochs).

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Specifically, develop, simple, sequence-to-sequence, baseline, architecture, well, cross-modal, attentionbased, model, continuous, setting, enables, types, studies, take, first, step, towards, integrating.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | This Cross-Modal Attention PM+DA*+Aug model achieves an SPL of 0.35 on val-seen and 0.30 on val-unseen - succeeding on 32% of episodes ... | p. 13 (5 Experiments), p. 11 (5 Experiments) |
| Baseline harness | Our baseline Seq2Seq model significantly outperforms the random and hand-crafted baselines, successfully reaching the goal in 20% of val-unseen episodes. | p. 12 (5 Experiments), p. 13 (5 Experiments) |
| Metric / failure reporting | Despite having no learned components nor processing any input, both these agents achieve approximately 3% success rates in val-unseen. | p. 12 (5 Experiments), p. 12 (5 Experiments) |

## Failure and Ablation Link

- **p. 12 / 5 Experiments - extractive PDF cue:** We believe that depth enable agents to quickly begin traversing environments effectively (e.g. without collisions) and without this it is very difficult to bootstrap to ...
- **p. 12 / 5 Experiments - extractive PDF cue:** Seq2Seq and Single-Modality Ablations.
- **p. 13 / 5 Experiments - extractive PDF cue:** We find that without data augmentation, the progress monitor over-fits considerably more (validation loss of 0.67 vs.
- **p. 13 / 5 Experiments - extractive PDF cue:** Specifically, we pretrain with imitation learning, data augmentation, and the progress monitoring loss, then finetune using DAgger (with β=0.75n+1) on the original data.
- **p. 9 / Figure/Table caption - extractive PDF cue:** Fig. 4. We develop a simple baseline agent (a) as well as an attentional agent (b) comparable to that in [29]. Both receive RGB and ...
- **p. 14 / 5 Experiments - extractive PDF cue:** The second example shows a failure of the agent - it navigates towards the wrong windows and fails to first "pass the kitchen" - stopping ...
- **p. 14 / 5 Experiments - extractive PDF cue:** We also observe failures when the agent never sees the object(s) referred to by the instruction in the scene - with a limited egocentric field-of-view, ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 1 (3 Facebook AI Research), p. 1 (3 Facebook AI Research), p. 2 (1 Introduction), objective p. 2 (1 Introduction), p. 4 (1 Introduction), temporal p. 9 (2 Related Work), p. 9 (2 Related Work), p. 11 (2 Related Work), p. 11 (5 Experiments), p. 12 (5 Experiments), p. 12 (5 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
