# Method - An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2010.11929; PDF retrieval source: https://arxiv.org/pdf/2010.11929. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3 METHOD), p. 3 (3 METHOD), p. 4 (3 METHOD), p. 4 (3 METHOD)): The Transformer encoder (Vaswani et al., 2017) consists of alternating layers of multiheaded selfattention (MSA, see Appendix A) and MLP blocks (Eq.

## Method Body Digest

- **p. 3 / 3 METHOD - extractive body cue:** The Transformer encoder (Vaswani et al., 2017) consists of alternating layers of multiheaded selfattention (MSA, see Appendix A) and MLP blocks (Eq.
- **p. 3 / 3 METHOD - extractive body cue:** Similar to BERT's [class] token, we prepend a learnable embedding to the sequence of embedded patches (z0 0 = xclass), whose state at the output ...
- **p. 4 / 3 METHOD - extractive body cue:** Note that this resolution adjustment and patch extraction are the only points at which an inductive bias about the 2D structure of the images is ...
- **p. 4 / 3 METHOD - extractive body cue:** As a special case, the patches can have spatial size 1x1, which means that the input sequence is obtained by simply flattening the spatial dimensions ...
- **p. 4 / 3 METHOD - extractive body cue:** The Vision Transformer can handle arbitrary sequence lengths (up to memory constraints), however, the pre-trained position embeddings may no longer be meaningful.
- **p. 3 / 3 METHOD - extractive body cue:** An advantage of this intentionally simple setup is that scalable NLP Transformer architectures - and their efficient implementations - can be used almost out of ...
- **p. 3 / 3 METHOD - extractive body cue:** To handle 2D images, we reshape the image x ∈RH×W ×C into a sequence of flattened 2D patches xp ∈RN×(P 2·C), where (H, W) is ...
- **p. 4 / 3 METHOD - extractive body cue:** As an alternative to raw image patches, the input sequence can be formed from feature maps of a CNN (LeCun et al., 1989).

## Design Rationale

- **p. 3 / 3 METHOD - extractive body cue:** The Transformer encoder (Vaswani et al., 2017) consists of alternating layers of multiheaded selfattention (MSA, see Appendix A) and MLP blocks (Eq.

## Source Evidence Cues

- **p. 3 / 3 METHOD - extractive body cue:** The Transformer encoder (Vaswani et al., 2017) consists of alternating layers of multiheaded selfattention (MSA, see Appendix A) and MLP blocks (Eq.
- **p. 3 / 3 METHOD - extractive body cue:** Similar to BERT's [class] token, we prepend a learnable embedding to the sequence of embedded patches (z0 0 = xclass), whose state at the output ...
- **p. 4 / 3 METHOD - extractive body cue:** Note that this resolution adjustment and patch extraction are the only points at which an inductive bias about the 2D structure of the images is ...
- **p. 4 / 3 METHOD - extractive body cue:** As a special case, the patches can have spatial size 1x1, which means that the input sequence is obtained by simply flattening the spatial dimensions ...
- **Detected method headings:** 3 METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Input representation | source-defined input을 learnable representation으로 바꾼다 | paper-specific image/text/sequence input | encoder, tokenization, normalization 또는 feature extraction을 수행 | latent feature/state | The Transformer encoder (Vaswani et al., 2017) consists of alternating layers of multiheaded selfattention (MSA, see Appendix A) and MLP blocks (Eq. | p. 3 (3 METHOD), p. 3 (3 METHOD) |
| Core objective / transformation | source task의 prediction·generation 목표를 최적화한다 | representation, target/condition | paper-specific model, loss, decoder 또는 generative process를 적용 | prediction/embedding/sample | Similar to BERT's [class] token, we prepend a learnable embedding to the sequence of embedded patches (z0 0 = xclass), whose state ... | p. 3 (3 METHOD), p. 4 (3 METHOD) |
| Downstream transfer boundary | 결과를 후속 task 또는 embodied system에 전달한다 | output와 query/task context | task head, retrieval, grounding 또는 adapter를 적용 | task cue/representation | Note that this resolution adjustment and patch extraction are the only points at which an inductive bias about the 2D structure of ... | p. 4 (3 METHOD), p. 4 (3 METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3 METHOD - extractive body cue:** The Vision Transformer can handle arbitrary sequence lengths (up to memory constraints), however, the pre-trained position embeddings may no longer be meaningful.
- **p. 3 / 3 METHOD - extractive body cue:** An advantage of this intentionally simple setup is that scalable NLP Transformer architectures - and their efficient implementations - can be used almost out of ...
- **Formal bridge:** source-defined input o -> prediction/embedding/sample ŷ -> paper-specific objective -> source task metric; robot link not established.
- **Equation/algorithm anchors:** p. 4 (3 METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Similar, BERT, class, token, prepend, learnable, embedding, sequence, embedded, patches, xclass, whose, state, output | 논문이 명시한 observation과 task input | body cue; exact tensor/frame verify |
| State/latent | Similar, BERT, class, token, prepend, learnable, embedding, sequence, embedded, patches | task state 또는 decision variable | body cue; notation verify |
| Action/output | Transformer, encoder, Vaswani, consists, alternating, layers, multiheaded, selfattention, MSA, Appendix | paper-specific output/action | body cue; unit/decoder verify |
| Objective/constraint | Vision, Transformer, handle, arbitrary, sequence, lengths, memory, constraints, however, pre-trained | paper-specific objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3 METHOD - extractive body cue:** Similar to BERT's [class] token, we prepend a learnable embedding to the sequence of embedded patches (z0 0 = xclass), whose state at the output ...
- **p. 3 / 3 METHOD - extractive body cue:** To handle 2D images, we reshape the image x ∈RH×W ×C into a sequence of flattened 2D patches xp ∈RN×(P 2·C), where (H, W) is ...
- **p. 4 / 3 METHOD - extractive body cue:** As an alternative to raw image patches, the input sequence can be formed from feature maps of a CNN (LeCun et al., 1989).
- **p. 4 / 3 METHOD - extractive body cue:** Note that this resolution adjustment and patch extraction are the only points at which an inductive bias about the 2D structure of the images is ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** To do so, we split an image into patches and provide the sequence of linear embeddings of these patches as an input to a Transformer.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Therefore, in large-scale image recognition, classic ResNetlike architectures are still state of the art (Mahajan et al., 2018; Xie et al., 2020; Kolesnikov et al., ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** When pre-trained on the public ImageNet-21k dataset or the in-house JFT-300M dataset, ViT approaches or beats state of the art on multiple image recognition benchmarks.
- **Normalized interface:** observation=논문이 명시한 observation과 task input; state=task state 또는 decision variable; output/action=paper-specific output/action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | The Vision Transformer can handle arbitrary sequence lengths (up to memory constraints), however, the pre-trained position embeddings may no longer be meaningful. | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | The resulting sequence of embedding vectors serves as input to the encoder. | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | The Vision Transformer can handle arbitrary sequence lengths (up to memory constraints), however, the pre-trained position embeddings may no longer be meaningful. | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | Option (ii) results in a 4x longer sequence length, and a more expensive ViT model. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4 EXPERIMENTS - extractive body cue:** All models were trained on TPUv3 hardware, and we report the number of TPUv3-core-days taken to pre-train each of them, that is, the number of ...
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** VTAB (19 tasks) 65 70 75 80 Accuracy [%] Natural (7 tasks) 70 80 90 Specialized (4 tasks) 80 82 85 88 90 Structured (8 ...
- **p. 3 / 3 METHOD - extractive body cue:** The classification head is implemented by a MLP with one hidden layer at pre-training time and by a single linear layer at fine-tuning time.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Transformer, encoder, Vaswani, consists, alternating, layers, multiheaded, selfattention, MSA, Appendix, MLP, blocks, Similar, BERT, class, token, prepend, learnable, embedding, sequence.
- **Relevant PDF headings:** 3 METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Input representation | We transfer the models trained on these dataset to several benchmark tasks: ImageNet on the original validation labels and the cleaned-up ReaL ... | p. 4 (4 EXPERIMENTS), p. 4 (4 EXPERIMENTS) |
| Core objective / transformation | Vision Transformer models pre-trained on the JFT-300M dataset outperform ResNet-based baselines on all datasets, while taking substantially less computational resources to pre-train. | p. 6 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS) |
| Downstream transfer boundary | Figure 5: Performance versus pre-training compute for different architectures: Vision Transformers, ResNets, and hybrids. Vision Transformers generally outperform ResNets with the same ... | p. 7 (Figure/Table caption), p. 6 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 5 / 4 EXPERIMENTS - extractive body cue:** The second is Noisy Student (Xie et al., 2020), which is a large EfficientNet trained using semi-supervised learning on ImageNet and JFT300M with the labels ...
- **p. 5 / 4 EXPERIMENTS - extractive body cue:** In what follows we use brief notation to indicate the model size and the input patch size: for instance, ViT-L/16 means the "Large" variant with ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Similarly, larger ViT variants overtake smaller ones as the dataset grows.
- **p. 14 / Figure/Table caption - extractive body cue:** Table 4: Hyperparameters for fine-tuning. All models are fine-tuned with cosine learning rate decay, a batch size of 512, no weight decay, and grad clipping ...
- **p. 15 / Figure/Table caption - extractive body cue:** Table 5: Top1 accuracy (in %) of Vision Transformer on various datasets when pre-trained on Im- ageNet, ImageNet-21k or JFT300M. These values correspond to Figure ...
- **p. 17 / Figure/Table caption - extractive body cue:** Table 8: Results of the ablation study on positional embeddings with ViT-B/16 model evaluated on ImageNet 5-shot linear. the difference in performance is fully explained ...
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 9. D.4 POSITIONAL EMBEDDING We ran ablations on different ways of encoding spatial information using positional embedding. We tried the following cases: • Providing ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3 METHOD), p. 3 (3 METHOD), p. 4 (3 METHOD), p. 4 (3 METHOD), objective p. 4 (3 METHOD), p. 3 (3 METHOD), temporal p. 4 (3 METHOD), p. 3 (3 METHOD), p. 3 (3 METHOD), p. 4 (3 METHOD), p. 5 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
