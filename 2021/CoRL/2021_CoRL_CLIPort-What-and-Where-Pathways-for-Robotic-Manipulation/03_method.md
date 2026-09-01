# Method - CLIPort: What and Where Pathways for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2109.12098; PDF retrieval source: https://arxiv.org/pdf/2109.12098. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction)): The key insight of the approach is formulating tabletop manipulation as a series of pick-and-place affordance predictions, where the objective is to detect actions rather than detect objects and then ...

## Method Body Digest

- **p. 2 / 1 Introduction - extractive body cue:** The key insight of the approach is formulating tabletop manipulation as a series of pick-and-place affordance predictions, where the objective is to detect actions rather ...
- **p. 1 / Abstract - extractive body cue:** To this end, we propose a framework that combines the best of both worlds: a two-stream architecture with semantic and spatial pathways for vision-based manipulation.
- **p. 2 / 1 Introduction - extractive body cue:** We introduce a two-stream architecture for manipulation with semantic and spatial pathways broadly inspired by (or vaguely analogous to) the two-stream hypothesis in cognitive psychology ...
- **p. 1 / 1 Introduction - extractive body cue:** In parallel, there has been great progress in learning models for visual representations [11, 12] and aligning representations of vision and language [13, 14, 15] ...
- **p. 3 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • An extended benchmark of language-grounding tasks for manipulation in Ravens [2]. • Two-stream architecture for using internet ...
- **p. 3 / 1 Introduction - extractive body cue:** The benchmark, code, and pre-trained models are available at: cliport.github.io.
- **p. 1 / 1 Introduction - extractive body cue:** In realistic human-robot interaction settings, collecting additional demonstrations or providing goal-images is often infeasible and unscalable.
- **p. 1 / Abstract - extractive body cue:** Our end-to-end framework is capable of solving a variety of language-specified tabletop tasks from packing unseen objects to folding cloths, all without any explicit representations ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** We propose 10 language-conditioned tasks with 1000s of unique instances per task that require both semantic and spatial reasoning (see Figure 1 a-j).
- **p. 2 / 1 Introduction - extractive body cue:** Specifically, we present CLIPORT, a languageconditioned imitation-learning agent that integrates the semantic understanding (what) of CLIP [1] with the spatial precision (where) of Transporter [2].
- **p. 3 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • An extended benchmark of language-grounding tasks for manipulation in Ravens [2]. • Two-stream architecture for using internet ...

## Source Evidence Cues

- **p. 2 / 1 Introduction - extractive body cue:** The key insight of the approach is formulating tabletop manipulation as a series of pick-and-place affordance predictions, where the objective is to detect actions rather ...
- **p. 1 / Abstract - extractive body cue:** To this end, we propose a framework that combines the best of both worlds: a two-stream architecture with semantic and spatial pathways for vision-based manipulation.
- **p. 2 / 1 Introduction - extractive body cue:** We introduce a two-stream architecture for manipulation with semantic and spatial pathways broadly inspired by (or vaguely analogous to) the two-stream hypothesis in cognitive psychology ...
- **p. 1 / 1 Introduction - extractive body cue:** In parallel, there has been great progress in learning models for visual representations [11, 12] and aligning representations of vision and language [13, 14, 15] ...
- **p. 3 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • An extended benchmark of language-grounding tasks for manipulation in Ravens [2]. • Two-stream architecture for using internet ...
- **p. 3 / 1 Introduction - extractive body cue:** The benchmark, code, and pre-trained models are available at: cliport.github.io.
- **Detected method headings:** C Two Stream Architecture Details (p. 20)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | The key insight of the approach is formulating tabletop manipulation as a series of pick-and-place affordance predictions, where the objective is to ... | p. 2 (1 Introduction), p. 1 (Abstract) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | To this end, we propose a framework that combines the best of both worlds: a two-stream architecture with semantic and spatial pathways ... | p. 1 (Abstract), p. 2 (1 Introduction) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | We introduce a two-stream architecture for manipulation with semantic and spatial pathways broadly inspired by (or vaguely analogous to) the two-stream hypothesis ... | p. 2 (1 Introduction), p. 1 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 Introduction - extractive body cue:** The key insight of the approach is formulating tabletop manipulation as a series of pick-and-place affordance predictions, where the objective is to detect actions rather ...
- **p. 1 / 1 Introduction - extractive body cue:** In parallel, there has been great progress in learning models for visual representations [11, 12] and aligning representations of vision and language [13, 14, 15] ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 2 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | insight, formulating, tabletop, manipulation, series, pick-and-place, affordance, predictions, where, objective, detect, actions, rather, objects | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | insight, formulating, tabletop, manipulation, series, pick-and-place, affordance, predictions, where, objective | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | language-conditioned, tasks, unique, instances, task, require, semantic, spatial, reasoning, Figure | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | insight, formulating, tabletop, manipulation, series, pick-and-place, affordance, predictions, where, objective | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive body cue:** The key insight of the approach is formulating tabletop manipulation as a series of pick-and-place affordance predictions, where the objective is to detect actions rather ...
- **p. 1 / 1 Introduction - extractive body cue:** In realistic human-robot interaction settings, collecting additional demonstrations or providing goal-images is often infeasible and unscalable.
- **p. 1 / Abstract - extractive body cue:** Our end-to-end framework is capable of solving a variety of language-specified tabletop tasks from packing unseen objects to folding cloths, all without any explicit representations ...
- **p. 2 / 1 Introduction - extractive body cue:** We also demonstrate our approach on a Franka Panda manipulator with one multi-task model for 9 real-world tasks trained with just 179 image-action pairs (see ...
- **p. 3 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • An extended benchmark of language-grounding tasks for manipulation in Ravens [2]. • Two-stream architecture for using internet ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | As in Transporter [2, 6], our framework can be extended to handle any motion primitive like pushing, sliding, etc. that can be ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Our end-to-end framework is capable of solving a variety of language-specified tabletop tasks from packing unseen objects to folding cloths, all without ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | Our end-to-end framework is capable of solving a variety of language-specified tabletop tasks from packing unseen objects to folding cloths, all without ... | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / 1 Introduction - extractive body cue:** In parallel, there has been great progress in learning models for visual representations [11, 12] and aligning representations of vision and language [13, 14, 15] ...
- **p. 3 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • An extended benchmark of language-grounding tasks for manipulation in Ravens [2]. • Two-stream architecture for using internet ...
- **p. 3 / 1 Introduction - extractive body cue:** The benchmark, code, and pre-trained models are available at: cliport.github.io.
- **p. 3 / 1 Introduction - extractive body cue:** The benchmark, code, and pre-trained models are available at: cliport.github.io.
- **p. 7 / 4 Results - extractive body cue:** Although pre-trained CLIP has been exposed to the attribute ‘pink', it could correspond to different concepts in the physical setting depending on factors like lighting ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** insight, formulating, tabletop, manipulation, series, pick-and-place, affordance, predictions, where, objective, detect, actions, rather, objects, then, learn, policy, framework, combines, best.
- **Relevant PDF headings:** C Two Stream Architecture Details (p. 20).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | For packing objects, we use 56 tabletop objects from the Google Scanned Objects dataset [61] and split them into 37 seen and ... | p. 6 (4 Results), p. 8 (4 Results) |
| Action / skill decoding | We perform experiments both in simulation and hardware aimed at answering the following questions: 1) How effective is the language-conditioned two-stream architecture ... | p. 6 (4 Results), p. 6 (4 Results) |
| Receding execution / feedback | Table 1. Language-Conditioned Test Results. Task success scores (mean %) from 100 evaluation instances vs. # of training demonstrations (1, 10, 100, ... | p. 7 (Figure/Table caption), p. 22 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 21 / Figure/Table caption - extractive body cue:** Table 5. Ablations and Baselines. Evaluation scores (mean %) for stack-block-pyramid-seq and packing-google-objects-seq tasks from 100 evaluation runs. Stacking block pyramids involves both semantic and ...
- **p. 6 / 4 Results - extractive body cue:** CLIP-only shows what can be achieved by fine-tuning a pre-trained semantic model for manipulation without spatial information, particularly depth.
- **p. 6 / 4 Results - extractive body cue:** In addition to these baselines, we present various ablations and alternative one-stream and twostream models in Appendix F.
- **p. 7 / 4 Results - extractive body cue:** This supports our premise that language is a strong conditioning mechanism for reusing concepts from other tasks without learning them from scratch.
- **p. 7 / 4 Results - extractive body cue:** As evidenced in towers-of-hanoi-seq-unseen-colors task in Table 1, Transporter-only suffers from a performance drop because of rings with unseen colors despite the fact that Tower ...
- **p. 14 / Figure/Table caption - extractive body cue:** Table 3. Language-conditioned tasks in Ravens [2] with their associated challenges. We extend the Ravens benchmark [2] to 10 language-conditioned. 8 out of 10 tasks ...
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 9. Data Augmentation: SE(2) transform applied to RGB-D input. The left image shows the original input, and the right image shows the transformed input ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), objective p. 2 (1 Introduction), p. 1 (1 Introduction), temporal p. 5 (2 Related Work), p. 1 (Abstract), p. 4 (2 Related Work), p. 4 (2 Related Work), p. 1 (1 Introduction), p. 2 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
