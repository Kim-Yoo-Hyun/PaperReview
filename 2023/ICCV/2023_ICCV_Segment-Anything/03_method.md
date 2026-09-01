# Method - Segment Anything

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (30 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2304.02643; PDF retrieval source: https://arxiv.org/pdf/2304.02643. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (3. What data can power this task and model?), p. 5 (3. Segment Anything Model), p. 2 (3. What data can power this task and model?), p. 5 (3. Segment Anything Model)): We use the promptable segmentation task as both a pre-training objective and to solve general downstream segmentation tasks via prompt engineering.

## Method Body Digest

- **p. 2 / 3. What data can power this task and model? - extractive PDF cue:** We use the promptable segmentation task as both a pre-training objective and to solve general downstream segmentation tasks via prompt engineering.
- **p. 5 / 3. Segment Anything Model - extractive PDF cue:** Motivated by scalability and powerful pretraining methods, we use an MAE [47] pre-trained Vision Transformer (ViT) [33] minimally adapted to process high resolution inputs [62].
- **p. 2 / 3. What data can power this task and model? - extractive PDF cue:** Surprisingly, we find that a simple design satisfies all three constraints: a powerful image encoder computes an image embedding, a prompt encoder embeds prompts, and ...
- **p. 5 / 3. Segment Anything Model - extractive PDF cue:** 4: an image encoder, a flexible prompt encoder, and a fast mask decoder.
- **p. 2 / 3. What data can power this task and model? - extractive PDF cue:** The promptable segmentation task and the goal of real-world use impose constraints on the model architecture.
- **p. 5 / 3. Segment Anything Model - extractive PDF cue:** During training, we backprop only the minimum loss [15, 45, 64] over masks.
- **p. 5 / 3. Segment Anything Model - extractive PDF cue:** We supervise mask prediction with the linear combination of focal loss [65] and dice loss [73] used in [14].
- **p. 5 / 3. Segment Anything Model - extractive PDF cue:** The mask decoder efficiently maps the image embedding, prompt embeddings, and an output token to a mask.

## Design Rationale

- **p. 2 / 3. What data can power this task and model? - extractive PDF cue:** We introduce each interconnected component next, followed by the dataset we created and the experiments that demonstrate the effectiveness of our approach.
- **p. 1 / 1. Introduction - extractive PDF cue:** That is, we seek to develop a promptable model and pre-train it on a broad dataset using a task that enables powerful generalization.
- **p. 2 / 3. What data can power this task and model? - extractive PDF cue:** Inspired by this line of work, we propose the promptable segmentation task, where the goal is to return a valid segmentation mask given any segmentation ...

## Source Evidence Cues

- **p. 2 / 3. What data can power this task and model? - extractive PDF cue:** We use the promptable segmentation task as both a pre-training objective and to solve general downstream segmentation tasks via prompt engineering.
- **p. 5 / 3. Segment Anything Model - extractive PDF cue:** Motivated by scalability and powerful pretraining methods, we use an MAE [47] pre-trained Vision Transformer (ViT) [33] minimally adapted to process high resolution inputs [62].
- **p. 2 / 3. What data can power this task and model? - extractive PDF cue:** Surprisingly, we find that a simple design satisfies all three constraints: a powerful image encoder computes an image embedding, a prompt encoder embeds prompts, and ...
- **p. 5 / 3. Segment Anything Model - extractive PDF cue:** 4: an image encoder, a flexible prompt encoder, and a fast mask decoder.
- **Detected method headings:** 2. What is the corresponding model architecture? (p. 1); 3. What data can power this task and model? (p. 1); 3. Segment Anything Model (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Input representation | source-defined input을 learnable representation으로 바꾼다 | paper-specific image/text/sequence input | encoder, tokenization, normalization 또는 feature extraction을 수행 | latent feature/state | We use the promptable segmentation task as both a pre-training objective and to solve general downstream segmentation tasks via prompt engineering. | p. 2 (3. What data can power this task and model?), p. 5 (3. Segment Anything Model) |
| Core objective / transformation | source task의 prediction·generation 목표를 최적화한다 | representation, target/condition | paper-specific model, loss, decoder 또는 generative process를 적용 | prediction/embedding/sample | Motivated by scalability and powerful pretraining methods, we use an MAE [47] pre-trained Vision Transformer (ViT) [33] minimally adapted to process high ... | p. 5 (3. Segment Anything Model), p. 2 (3. What data can power this task and model?) |
| Downstream transfer boundary | 결과를 후속 task 또는 embodied system에 전달한다 | output와 query/task context | task head, retrieval, grounding 또는 adapter를 적용 | task cue/representation | Surprisingly, we find that a simple design satisfies all three constraints: a powerful image encoder computes an image embedding, a prompt encoder ... | p. 2 (3. What data can power this task and model?), p. 5 (3. Segment Anything Model) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 3. What data can power this task and model? - extractive PDF cue:** The promptable segmentation task and the goal of real-world use impose constraints on the model architecture.
- **p. 2 / 3. What data can power this task and model? - extractive PDF cue:** We use the promptable segmentation task as both a pre-training objective and to solve general downstream segmentation tasks via prompt engineering.
- **p. 5 / 3. Segment Anything Model - extractive PDF cue:** During training, we backprop only the minimum loss [15, 45, 64] over masks.
- **p. 5 / 3. Segment Anything Model - extractive PDF cue:** We supervise mask prediction with the linear combination of focal loss [65] and dice loss [73] used in [14].
- **Formal bridge:** source-defined input o -> prediction/embedding/sample ŷ -> paper-specific objective -> source task metric; robot link not established.
- **Equation/algorithm anchors:** p. 2 (3. What data can power this task and model?), p. 2 (3. What data can power this task and model?), p. 5 (3. Segment Anything Model), p. 5 (3. Segment Anything Model).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | mask, decoder, efficiently, maps, image, embedding, prompt, embeddings, output, token, After, running, blocks, upsample | 논문이 명시한 observation과 task input | body cue; exact tensor/frame verify |
| State/latent | mask, decoder, efficiently, maps, image, embedding, prompt, embeddings, output, token | task state 또는 decision variable | body cue; notation verify |
| Action/output | introduce, interconnected, component, next, followed, dataset, created, experiments, demonstrate, effectiveness | paper-specific output/action | body cue; unit/decoder verify |
| Objective/constraint | promptable, segmentation, task, goal, real-world, impose, constraints, model, architecture, pre-training | paper-specific objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3. Segment Anything Model - extractive PDF cue:** The mask decoder efficiently maps the image embedding, prompt embeddings, and an output token to a mask.
- **p. 5 / 3. Segment Anything Model - extractive PDF cue:** After running two blocks, we upsample the image embedding and an MLP maps the output token to a dynamic linear classifier, which then computes the ...
- **p. 2 / 3. What data can power this task and model? - extractive PDF cue:** This task requires a model that supports flexible prompting and can output segmentation masks in realtime when prompted to allow for interactive use.
- **p. 2 / 3. What data can power this task and model? - extractive PDF cue:** The requirement of a valid output mask means that even when a prompt is ambiguous and could refer to multiple objects (for example, a point ...
- **p. 1 / 1. Introduction - extractive PDF cue:** In this work, our goal is to build a foundation model for image segmentation.
- **p. 1 / 1. Introduction - extractive PDF cue:** Such encoders also compose effectively with other modules to enable downstream tasks, such as image generation (e.g., DALL·E [83]).
- **p. 3 / 3. What data can power this task and model? - extractive PDF cue:** We group images by number of masks per image for visualization (there are ∼100 masks per image on average).
- **Normalized interface:** observation=논문이 명시한 observation과 task input; state=task state 또는 decision variable; output/action=paper-specific output/action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | Next, we present a sequence of experiments that traverse low, mid, and highlevel image understanding and roughly parallel the historical development of ... | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | SAM is applied zero-shot, i.e. it was not trained for object proposal generation nor did it access LVIS images or annotations. intermediate ... | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | not recovered | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | Given a precomputed image embedding, the prompt encoder and mask decoder run in a web browser, on CPU, in ∼50ms. | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 3. What data can power this task and model? - extractive PDF cue:** We use the promptable segmentation task as both a pre-training objective and to solve general downstream segmentation tasks via prompt engineering.
- **p. 5 / 3. Segment Anything Model - extractive PDF cue:** Motivated by scalability and powerful pretraining methods, we use an MAE [47] pre-trained Vision Transformer (ViT) [33] minimally adapted to process high resolution inputs [62].
- **p. 2 / 3. What data can power this task and model? - extractive PDF cue:** Surprisingly, we find that a simple design satisfies all three constraints: a powerful image encoder computes an image embedding, a prompt encoder embeds prompts, and ...
- **p. 11 / 7.5. Zero-Shot Text-to-Mask - extractive PDF cue:** That is, at inference time we run text through CLIP's text encoder and then give the resulting text embedding as a prompt to SAM (see ...
- **p. 2 / 3. What data can power this task and model? - extractive PDF cue:** Surprisingly, we find that a simple design satisfies all three constraints: a powerful image encoder computes an image embedding, a prompt encoder embeds prompts, and ...
- **p. 8 / 7. Zero-Shot Transfer Experiments - extractive PDF cue:** For all other model and training details, such as hyperparameters, refer to §A.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** promptable, segmentation, task, pre-training, objective, solve, general, downstream, tasks, prompt, engineering, Motivated, scalability, powerful, pretraining, methods, MAE, pre-trained, Vision, Transformer.
- **Relevant PDF headings:** 2. What is the corresponding model architecture? (p. 1); 3. What data can power this task and model? (p. 1); 3. Segment Anything Model (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Input representation | 5 we plot the spatial distribution of object centers in SA-1B compared to the largest existing segmentation datasets. | p. 7 (5. Segment Anything Dataset), p. 8 (7. Zero-Shot Transfer Experiments) |
| Core objective / transformation | We compare mainly to RITM [92], a strong interactive segmenter that performs best on our benchmark compared to other strong baselines [67, ... | p. 8 (7.1. Zero-Shot Single Point Valid Mask Evaluation), p. 9 (7.1. Zero-Shot Single Point Valid Mask Evaluation) |
| Downstream transfer boundary | SAM significantly outperforms prior interactive segmenters with 1 point and is on par with more points. | p. 9 (7.1. Zero-Shot Single Point Valid Mask Evaluation), p. 9 (7.1. Zero-Shot Single Point Valid Mask Evaluation) |

## Failure and Ablation Link

- **p. 8 / 7. Zero-Shot Transfer Experiments - extractive PDF cue:** Our experiments conclude with an ablation study.
- **p. 10 / 7.2. Zero-Shot Edge Detection - extractive PDF cue:** Redundant masks are removed by NMS.
- **p. 11 / 7.6. Ablations - extractive PDF cue:** We perform several ablations on our 23 dataset suite with the single center point prompt protocol.
- **p. 11 / 7.6. Ablations - extractive PDF cue:** The full SA-1B contains 11M images, which we uniformly subsample to 1M and 0.1M for this ablation.
- **p. 12 / 7.6. Ablations - extractive PDF cue:** manual + semi automatic + automatic automatic only Training data stages 50 60 70 mIoU (23 datasets) 1 point (oracle) 1 point 0.1M 1M 11M ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Figure 13: Ablation studies of our data engine stages, image encoder scaling, and training data scaling. (Left) Each data engine stage leads to improvements on ...
- **p. 8 / 6. Segment Anything RAI Analysis - extractive PDF cue:** We believe our findings stem from the nature of the task, and acknowledge biases may arise when SAM is used as a component in larger ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (3. What data can power this task and model?), p. 5 (3. Segment Anything Model), p. 2 (3. What data can power this task and model?), p. 5 (3. Segment Anything Model), objective p. 2 (3. What data can power this task and model?), p. 2 (3. What data can power this task and model?), p. 5 (3. Segment Anything Model), p. 5 (3. Segment Anything Model), temporal p. 8 (7. Zero-Shot Transfer Experiments), p. 10 (7.3. Zero-Shot Object Proposals), p. 2 (3. What data can power this task and model?), p. 2 (3. What data can power this task and model?), p. 4 (2. Segment Anything Task), p. 5 (3. Segment Anything Model).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
