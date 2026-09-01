# Method - HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=vVVbGj9cMC; PDF retrieval source: https://openreview.net/pdf/1158a6b1525482f72ae519b3be5d06e0abef1732.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (1 Introduction), p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction)): Our core contributions are summarized as follows: • We propose a Hierarchical Memory Management framework that decouples robotic control into transient (Executor), working (Sentry), and episodic (Planner) memory layers, resolving ...

## Method Body Digest

- **p. 3 / 1 Introduction - extractive PDF cue:** Our core contributions are summarized as follows: • We propose a Hierarchical Memory Management framework that decouples robotic control into transient (Executor), working (Sentry), and ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Most existing architectures rely on the Markov assumption, where the policy 𝑝(𝑎𝑡/𝑜𝑡, 𝑙) predicts the action 𝑎𝑡at time step 𝑡conditioned only on the transient observation ...
- **p. 1 / Abstract - extractive PDF cue:** To resolve this architectural misalignment, we propose HiMe, a Hierarchical Embodied Memory framework that decouples embodied intelligence into a high-frequency Executor for execution, a Sentry ...
- **p. 2 / 1 Introduction - extractive PDF cue:** To overcome these limitations, one intuitive approach is to imbue VLA models with native memory capabilities through specialized training or auxiliary losses [3, 4].
- **p. 2 / 1 Introduction - extractive PDF cue:** However, a static memory hierarchy alone is insufficient for the complexities of real-world human-robot interaction, which is characterized by: (1) multimodal richness, where human instructions ...
- **p. 3 / 1 Introduction - extractive PDF cue:** When the Sentry detects a significant state transition or a revision in user intent, the Planner proactively refines the knowledge base.
- **p. 2 / 1 Introduction - extractive PDF cue:** This scale constraint, in turn, limits the internal world knowledge and generalization capabilities of the VLM, weakening its zero-shot performance.
- **p. 1 / Abstract - extractive PDF cue:** We also introduce a dynamic knowledge system based on cross-modal semantic schemas and active management mechanisms, allowing robots to maintain memory plasticity through "Add, Update, ...

## Design Rationale

- **p. 3 / 1 Introduction - extractive PDF cue:** Our core contributions are summarized as follows: • We propose a Hierarchical Memory Management framework that decouples robotic control into transient (Executor), working (Sentry), and ...
- **p. 2 / 1 Introduction - extractive PDF cue:** 1, motivated by this temporal and scale mismatch, we introduce HiMe, a Hierarchical Embodied Memory framework that decouples embodied intelligence into three functional layers with ...
- **p. 3 / 1 Introduction - extractive PDF cue:** In contrast to passive storage, we introduce explicit Add, Update, and Delete operations to grant the robot knowledge plasticity.

## Source Evidence Cues

- **p. 3 / 1 Introduction - extractive PDF cue:** Our core contributions are summarized as follows: • We propose a Hierarchical Memory Management framework that decouples robotic control into transient (Executor), working (Sentry), and ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Most existing architectures rely on the Markov assumption, where the policy 𝑝(𝑎𝑡/𝑜𝑡, 𝑙) predicts the action 𝑎𝑡at time step 𝑡conditioned only on the transient observation ...
- **p. 1 / Abstract - extractive PDF cue:** To resolve this architectural misalignment, we propose HiMe, a Hierarchical Embodied Memory framework that decouples embodied intelligence into a high-frequency Executor for execution, a Sentry ...
- **p. 2 / 1 Introduction - extractive PDF cue:** To overcome these limitations, one intuitive approach is to imbue VLA models with native memory capabilities through specialized training or auxiliary losses [3, 4].
- **p. 2 / 1 Introduction - extractive PDF cue:** However, a static memory hierarchy alone is insufficient for the complexities of real-world human-robot interaction, which is characterized by: (1) multimodal richness, where human instructions ...
- **p. 3 / 1 Introduction - extractive PDF cue:** When the Sentry detects a significant state transition or a revision in user intent, the Planner proactively refines the knowledge base.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Our core contributions are summarized as follows: • We propose a Hierarchical Memory Management framework that decouples robotic control into transient (Executor), ... | p. 3 (1 Introduction), p. 1 (1 Introduction) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Most existing architectures rely on the Markov assumption, where the policy 𝑝(𝑎𝑡/𝑜𝑡, 𝑙) predicts the action 𝑎𝑡at time step 𝑡conditioned only on ... | p. 1 (1 Introduction), p. 1 (Abstract) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | To resolve this architectural misalignment, we propose HiMe, a Hierarchical Embodied Memory framework that decouples embodied intelligence into a high-frequency Executor for ... | p. 1 (Abstract), p. 2 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 Introduction - extractive PDF cue:** This scale constraint, in turn, limits the internal world knowledge and generalization capabilities of the VLM, weakening its zero-shot performance.
- **p. 2 / 1 Introduction - extractive PDF cue:** To overcome these limitations, one intuitive approach is to imbue VLA models with native memory capabilities through specialized training or auxiliary losses [3, 4].
- **p. 1 / Abstract - extractive PDF cue:** We also introduce a dynamic knowledge system based on cross-modal semantic schemas and active management mechanisms, allowing robots to maintain memory plasticity through "Add, Update, ...
- **p. 3 / 1 Introduction - extractive PDF cue:** In contrast to passive storage, we introduce explicit Add, Update, and Delete operations to grant the robot knowledge plasticity.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 3 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Most, existing, architectures, rely, Markov, assumption, where, policy, predicts, action, time, step, conditioned, only | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Most, existing, architectures, rely, Markov, assumption, where, policy, predicts, action | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | core, contributions, summarized, follows, Hierarchical, Memory, Management, framework, decouples, robotic | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | scale, constraint, turn, limits, internal, world, knowledge, generalization, capabilities, VLM | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1 Introduction - extractive PDF cue:** Most existing architectures rely on the Markov assumption, where the policy 𝑝(𝑎𝑡/𝑜𝑡, 𝑙) predicts the action 𝑎𝑡at time step 𝑡conditioned only on the transient observation ...
- **p. 2 / 1 Introduction - extractive PDF cue:** However, a static memory hierarchy alone is insufficient for the complexities of real-world human-robot interaction, which is characterized by: (1) multimodal richness, where human instructions ...
- **p. 1 / Abstract - extractive PDF cue:** Current Vision-Language-Action (VLA) models excel at robotic manipulation but often struggle with non-Markovian tasks requiring long-term memory and reasoning due to their reliance on immediate ...
- **p. 2 / 1 Introduction - extractive PDF cue:** (2) The Sentry acts as the guardian of working memory (short-term memory); it asynchronously filters the continuous sensory stream to identify critical state transitions, effectively ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Our core contributions are summarized as follows: • We propose a Hierarchical Memory Management framework that decouples robotic control into transient (Executor), working (Sentry), and ...
- **p. 3 / 1 Introduction - extractive PDF cue:** When the Sentry detects a significant state transition or a revision in user intent, the Planner proactively refines the knowledge base.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | By observing a sequence of 8 frames (consistent with our sentry‘s working memory), the Sentry can leverage temporal cues to make more ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Flat Memory: The Planner operates at a fixed frequency and receives the 8 most recent observations, assisted by a FIFO queue of ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | By observing a sequence of 8 frames (consistent with our sentry‘s working memory), the Sentry can leverage temporal cues to make more ... | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | By observing a sequence of 8 frames (consistent with our sentry‘s working memory), the Sentry can leverage temporal cues to make more ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 Introduction - extractive PDF cue:** To overcome these limitations, one intuitive approach is to imbue VLA models with native memory capabilities through specialized training or auxiliary losses [3, 4].
- **p. 2 / 1 Introduction - extractive PDF cue:** However, a static memory hierarchy alone is insufficient for the complexities of real-world human-robot interaction, which is characterized by: (1) multimodal richness, where human instructions ...
- **p. 2 / 1 Introduction - extractive PDF cue:** However, these training-based methods are often constrained by limited context windows and the inherent difficulty of optimizing long-range causal dependencies over hundreds of steps.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** core, contributions, summarized, follows, Hierarchical, Memory, Management, framework, decouples, robotic, control, transient, Executor, working, Sentry, episodic, Planner, layers, resolving, granularity.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | After a temporal interval, the robot is tasked with restoring the items to the environment. | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Action / skill decoding | HiMe significantly outperforms all baselines, achieving a 90% average success rate. | p. 9 (4 Experiments), p. 10 (4 Experiments) |
| Receding execution / feedback | HiMe significantly outperforms all baselines, achieving a 90% average success rate. | p. 9 (4 Experiments), p. 9 (4 Experiments) |

## Failure and Ablation Link

- **p. 8 / 4 Experiments - extractive PDF cue:** HiMe w/o Sentry: We utilize our complete Planner's memory design but remove the sentry module.
- **p. 8 / 4 Experiments - extractive PDF cue:** Transient Memory w/ Sentry: This variant introduces our Sentry module to trigger the Planner based on task progress.
- **p. 9 / 4 Experiments - extractive PDF cue:** In Counting, even with Sentry stabilization (Transient Memory w/ Sentry), the robot still fails (23%) due to the lack of persistence: without an explicit memory ...
- **p. 10 / 4 Experiments - extractive PDF cue:** Object Search Counting Rearrangement Average 50 60 70 80 90 100 Task Progress (%) 86 78 76 80 74 91 84 83 92 92 87 ...
- **p. 10 / 4 Experiments - extractive PDF cue:** Without Update/Delete, memory stores obsolete states (e.g., prior object locations) alongside current ones, introducing noise during Query and potentially confusing the Planner.
- **p. 11 / 4 Experiments - extractive PDF cue:** In contrast, HiMe maintains an infinite structured memory, avoiding this forgetting and enabling immediate retrieval without physical re-exploration.
- **p. 9 / 4 Experiments - extractive PDF cue:** The fundamental limitation of such contextual memory is the lack of consolidation: a simple FIFO queue cannot distinguish between truly critical frames and redundant observations.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (1 Introduction), p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), objective p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 3 (1 Introduction), temporal p. 11 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 11 (4 Experiments), p. 12 (6 Conclusion), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
