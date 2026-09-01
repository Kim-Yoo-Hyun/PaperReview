# Method - Attention Is All You Need

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1706.03762; PDF retrieval source: https://arxiv.org/pdf/1706.03762. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (2 Background), p. 3 (2 Background), p. 5 (2 Background), p. 1 (Abstract)): We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.

## Method Body Digest

- **p. 1 / Abstract - extractive PDF cue:** We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.
- **p. 2 / 1 Introduction - extractive PDF cue:** In this work we propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between ...
- **p. 2 / 2 Background - extractive PDF cue:** To the best of our knowledge, however, the Transformer is the first transduction model relying entirely on self-attention to compute representations of its input and ...
- **p. 3 / 2 Background - extractive PDF cue:** The Transformer follows this overall architecture using stacked self-attention and point-wise, fully connected layers for both the encoder and decoder, shown in the left and ...
- **p. 5 / 2 Background - extractive PDF cue:** 3.2.3 Applications of Attention in our Model The Transformer uses multi-head attention in three different ways: • In "encoder-decoder attention" layers, the queries come from ...
- **p. 1 / Abstract - extractive PDF cue:** The best performing models also connect the encoder and decoder through an attention mechanism.
- **p. 3 / 2 Background - extractive PDF cue:** 3.1 Encoder and Decoder Stacks Encoder: The encoder is composed of a stack of N = 6 identical layers.
- **p. 1 / Abstract - extractive PDF cue:** On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** In this work we propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between ...
- **p. 1 / Abstract - extractive PDF cue:** We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data. ...
- **p. 1 / Abstract - extractive PDF cue:** We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.

## Source Evidence Cues

- **p. 1 / Abstract - extractive PDF cue:** We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.
- **p. 2 / 1 Introduction - extractive PDF cue:** In this work we propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between ...
- **p. 2 / 2 Background - extractive PDF cue:** To the best of our knowledge, however, the Transformer is the first transduction model relying entirely on self-attention to compute representations of its input and ...
- **p. 3 / 2 Background - extractive PDF cue:** The Transformer follows this overall architecture using stacked self-attention and point-wise, fully connected layers for both the encoder and decoder, shown in the left and ...
- **p. 5 / 2 Background - extractive PDF cue:** 3.2.3 Applications of Attention in our Model The Transformer uses multi-head attention in three different ways: • In "encoder-decoder attention" layers, the queries come from ...
- **p. 1 / Abstract - extractive PDF cue:** The best performing models also connect the encoder and decoder through an attention mechanism.
- **p. 3 / 2 Background - extractive PDF cue:** 3.1 Encoder and Decoder Stacks Encoder: The encoder is composed of a stack of N = 6 identical layers.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Input representation | source-defined input을 learnable representation으로 바꾼다 | paper-specific image/text/sequence input | encoder, tokenization, normalization 또는 feature extraction을 수행 | latent feature/state | We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. | p. 1 (Abstract), p. 2 (1 Introduction) |
| Core objective / transformation | source task의 prediction·generation 목표를 최적화한다 | representation, target/condition | paper-specific model, loss, decoder 또는 generative process를 적용 | prediction/embedding/sample | In this work we propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw ... | p. 2 (1 Introduction), p. 2 (2 Background) |
| Downstream transfer boundary | 결과를 후속 task 또는 embodied system에 전달한다 | output와 query/task context | task head, retrieval, grounding 또는 adapter를 적용 | task cue/representation | To the best of our knowledge, however, the Transformer is the first transduction model relying entirely on self-attention to compute representations of ... | p. 2 (2 Background), p. 3 (2 Background) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / Abstract - extractive PDF cue:** On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight ...
- **p. 2 / 1 Introduction - extractive PDF cue:** The fundamental constraint of sequential computation, however, remains.
- **p. 2 / 1 Introduction - extractive PDF cue:** This inherently sequential nature precludes parallelization within training examples, which becomes critical at longer sequence lengths, as memory constraints limit batching across examples.
- **p. 4 / 2 Background - extractive PDF cue:** We suspect that for large values of dk, the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely ...
- **p. 5 / 2 Background - extractive PDF cue:** Due to the reduced dimension of each head, the total computational cost is similar to that of single-head attention with full dimensionality.
- **p. 8 / 2 Background - extractive PDF cue:** Model BLEU Training Cost (FLOPs) EN-DE EN-FR EN-DE EN-FR ByteNet [18] 23.75 Deep-Att + PosUnk [39] 39.2 1.0 · 1020 GNMT + RL [38] 24.6 ...
- **Formal bridge:** source-defined input o -> prediction/embedding/sample ŷ -> paper-specific objective -> source task metric; robot link not established.
- **Equation/algorithm anchors:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (2 Background), p. 5 (2 Background), p. 7 (2 Background).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Transformer, model, architecture, eschewing, recurrence, instead, relying, entirely, attention, mechanism, draw, global, dependencies, between | 논문이 명시한 observation과 task input | body cue; exact tensor/frame verify |
| State/latent | Transformer, model, architecture, eschewing, recurrence, instead, relying, entirely, attention, mechanism | task state 또는 decision variable | body cue; notation verify |
| Action/output | Transformer, model, architecture, eschewing, recurrence, instead, relying, entirely, attention, mechanism | paper-specific output/action | body cue; unit/decoder verify |
| Objective/constraint | WMT, English-to-French, translation, task, model, establishes, single-model, state-of-the-art, BLEU, score | paper-specific objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive PDF cue:** In this work we propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between ...
- **p. 2 / 2 Background - extractive PDF cue:** The goal of reducing sequential computation also forms the foundation of the Extended Neural GPU [16], ByteNet [18] and ConvS2S [9], all of which use ...
- **p. 6 / 2 Background - extractive PDF cue:** Hence we also compare the maximum path length between any two input and output positions in networks composed of the different layer types.
- **p. 1 / Abstract - extractive PDF cue:** On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight ...
- **p. 5 / 2 Background - extractive PDF cue:** The dimensionality of input and output is dmodel = 512, and the inner-layer has dimensionality dff = 2048.
- **p. 5 / 2 Background - extractive PDF cue:** 3.4 Embeddings and Softmax Similarly to other sequence transduction models, we use learned embeddings to convert the input tokens and output tokens to vectors of ...
- **p. 6 / 2 Background - extractive PDF cue:** The shorter these paths between any combination of positions in the input and output sequences, the easier it is to learn long-range dependencies [12].
- **Normalized interface:** observation=논문이 명시한 observation과 task input; state=task state 또는 decision variable; output/action=paper-specific output/action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | Aligning the positions to steps in computation time, they generate a sequence of hidden states ht, as a function of the previous ... | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | This inherently sequential nature precludes parallelization within training examples, which becomes critical at longer sequence lengths, as memory constraints limit batching across ... | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | This inherently sequential nature precludes parallelization within training examples, which becomes critical at longer sequence lengths, as memory constraints limit batching across ... | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 2 Background - extractive PDF cue:** We varied the learning rate over the course of training, according to the formula: lrate = d-0.5 model · min(step_num-0.5, step_num · warmup_steps-1.5) (3) This ...
- **p. 8 / 6 Results - extractive PDF cue:** We estimate the number of floating point operations used to train a model by multiplying the training time, the number of GPUs used, and an ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** simple, network, architecture, Transformer, solely, attention, mechanisms, dispensing, recurrence, convolutions, entirely, model, eschewing, instead, relying, mechanism, draw, global, dependencies, between.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Input representation | On the WMT 2014 English-to-French translation task, our big model achieves a BLEU score of 41.0, outperforming all of the previously published ... | p. 8 (6 Results), p. 8 (6 Results) |
| Core objective / transformation | On the WMT 2014 English-to-French translation task, our big model achieves a BLEU score of 41.0, outperforming all of the previously published ... | p. 8 (6 Results), p. 8 (6 Results) |
| Downstream transfer boundary | On the WMT 2014 English-to-French translation task, our big model achieves a BLEU score of 41.0, outperforming all of the previously published ... | p. 8 (6 Results), p. 8 (6 Results) |

## Failure and Ablation Link

- **p. 8 / 6 Results - extractive PDF cue:** 6.2 Model Variations To evaluate the importance of different components of the Transformer, we varied our base model in different ways, measuring the change in ...
- **p. 9 / 6 Results - extractive PDF cue:** In row (E) we replace our sinusoidal positional encoding with learned positional embeddings [9], and observe nearly identical results to the base model.
- **p. 7 / 2 Background - extractive PDF cue:** We plan to investigate this approach further in future work.
- **p. 7 / 2 Background - extractive PDF cue:** A single convolutional layer with kernel width k < n does not connect all pairs of input and output positions.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (2 Background), p. 3 (2 Background), p. 5 (2 Background), p. 1 (Abstract), objective p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (2 Background), p. 5 (2 Background), p. 8 (2 Background), temporal p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 5 (2 Background), p. 5 (2 Background), p. 6 (2 Background).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
