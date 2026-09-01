# Method - Learning Transferable Visual Models From Natural Language Supervision

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (48 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2103.00020; PDF retrieval source: https://arxiv.org/pdf/2103.00020. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (2.4. Choosing and Scaling a Model), p. 4 (2.4. Choosing and Scaling a Model), p. 4 (2.3. Selecting an Efficient Pre-Training Method), p. 5 (2.4. Choosing and Scaling a Model), p. 3 (2.1. Natural Language Supervision), p. 3 (2.1. Natural Language Supervision)): Learning Transferable Visual Models From Natural Language Supervision 5 # image_encoder - ResNet or Vision Transformer # text_encoder - CBOW or Text Transformer # I[n, h, w, c] - minibatch ...

## Method Body Digest

- **p. 5 / 2.4. Choosing and Scaling a Model - extractive body cue:** Learning Transferable Visual Models From Natural Language Supervision 5 # image_encoder - ResNet or Vision Transformer # text_encoder - CBOW or Text Transformer # I[n, ...
- **p. 4 / 2.4. Choosing and Scaling a Model - extractive body cue:** For the first, we use ResNet-50 (He et al., 2016a) as the base architecture for the image encoder due to its widespread adoption and proven ...
- **p. 4 / 2.3. Selecting an Efficient Pre-Training Method - extractive body cue:** To our knowledge this batch construction technique and objective was first introduced in the area of deep metric learning as the multi-class N-pair loss Sohn ...
- **p. 5 / 2.4. Choosing and Scaling a Model - extractive body cue:** The text sequence is bracketed with [SOS] and [EOS] tokens and the activations of the highest layer of the transformer at the [EOS] token are ...
- **p. 3 / 2.1. Natural Language Supervision - extractive body cue:** Although early work wrestled with the complexity of natural language when using topic model and n-gram representations, improvements in deep contextual representation learning suggest we ...
- **p. 3 / 2.1. Natural Language Supervision - extractive body cue:** Learning from natural language has several potential strengths over other training methods.
- **p. 4 / 2.3. Selecting an Efficient Pre-Training Method - extractive body cue:** Finally all WordNet synsets not already in the query list are added. multi-modal embedding space by jointly training an image encoder and text encoder to ...
- **p. 5 / 2.5. Training - extractive body cue:** Hyper-parameters were then adapted heuristically for larger models due to computational constraints.

## Design Rationale

- **p. 1 / 1. Introduction and Motivating Work - extractive body cue:** Pre-training methods which learn directly from raw text have revolutionized NLP over the last few years (Dai & Le, 2015; Peters et al., 2018; Howard ...
- **p. 3 / 2.1. Natural Language Supervision - extractive body cue:** Learning from natural language also has an important advantage over most unsupervised or self-supervised learning approaches in that it doesn't "just" learn a representation but ...
- **p. 3 / 2.1. Natural Language Supervision - extractive body cue:** At the core of our approach is the idea of learning perception from supervision contained in natural language.

## Source Evidence Cues

- **p. 5 / 2.4. Choosing and Scaling a Model - extractive body cue:** Learning Transferable Visual Models From Natural Language Supervision 5 # image_encoder - ResNet or Vision Transformer # text_encoder - CBOW or Text Transformer # I[n, ...
- **p. 4 / 2.4. Choosing and Scaling a Model - extractive body cue:** For the first, we use ResNet-50 (He et al., 2016a) as the base architecture for the image encoder due to its widespread adoption and proven ...
- **p. 4 / 2.3. Selecting an Efficient Pre-Training Method - extractive body cue:** To our knowledge this batch construction technique and objective was first introduced in the area of deep metric learning as the multi-class N-pair loss Sohn ...
- **p. 5 / 2.4. Choosing and Scaling a Model - extractive body cue:** The text sequence is bracketed with [SOS] and [EOS] tokens and the activations of the highest layer of the transformer at the [EOS] token are ...
- **p. 3 / 2.1. Natural Language Supervision - extractive body cue:** Although early work wrestled with the complexity of natural language when using topic model and n-gram representations, improvements in deep contextual representation learning suggest we ...
- **p. 3 / 2.1. Natural Language Supervision - extractive body cue:** Learning from natural language has several potential strengths over other training methods.
- **Detected method headings:** 2. Approach (p. 3); 2.3. Selecting an Efficient Pre-Training Method (p. 4); 2.4. Choosing and Scaling a Model (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Input representation | source-defined input을 learnable representation으로 바꾼다 | paper-specific image/text/sequence input | encoder, tokenization, normalization 또는 feature extraction을 수행 | latent feature/state | Learning Transferable Visual Models From Natural Language Supervision 5 # image_encoder - ResNet or Vision Transformer # text_encoder - CBOW or Text ... | p. 5 (2.4. Choosing and Scaling a Model), p. 4 (2.4. Choosing and Scaling a Model) |
| Core objective / transformation | source task의 prediction·generation 목표를 최적화한다 | representation, target/condition | paper-specific model, loss, decoder 또는 generative process를 적용 | prediction/embedding/sample | For the first, we use ResNet-50 (He et al., 2016a) as the base architecture for the image encoder due to its widespread ... | p. 4 (2.4. Choosing and Scaling a Model), p. 4 (2.3. Selecting an Efficient Pre-Training Method) |
| Downstream transfer boundary | 결과를 후속 task 또는 embodied system에 전달한다 | output와 query/task context | task head, retrieval, grounding 또는 adapter를 적용 | task cue/representation | To our knowledge this batch construction technique and objective was first introduced in the area of deep metric learning as the multi-class ... | p. 4 (2.3. Selecting an Efficient Pre-Training Method), p. 5 (2.4. Choosing and Scaling a Model) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 2.3. Selecting an Efficient Pre-Training Method - extractive body cue:** To our knowledge this batch construction technique and objective was first introduced in the area of deep metric learning as the multi-class N-pair loss Sohn ...
- **p. 4 / 2.3. Selecting an Efficient Pre-Training Method - extractive body cue:** Finally all WordNet synsets not already in the query list are added. multi-modal embedding space by jointly training an image encoder and text encoder to ...
- **p. 5 / 2.5. Training - extractive body cue:** Hyper-parameters were then adapted heuristically for larger models due to computational constraints.
- **p. 5 / 2.5. Training - extractive body cue:** To save additional memory, gradient checkpointing (Griewank & Walther, 2000; Chen et al., 2016), half-precision Adam statistics (Dhariwal et al., 2020), and half-precision stochastically rounded ...
- **p. 3 / 2.1. Natural Language Supervision - extractive body cue:** Learning from natural language also has an important advantage over most unsupervised or self-supervised learning approaches in that it doesn't "just" learn a representation but ...
- **Formal bridge:** source-defined input o -> prediction/embedding/sample ŷ -> paper-specific objective -> source task metric; robot link not established.
- **Equation/algorithm anchors:** p. 4 (2.3. Selecting an Efficient Pre-Training Method), p. 4 (2.3. Selecting an Efficient Pre-Training Method), p. 5 (2.5. Training), p. 5 (2.4. Choosing and Scaling a Model).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | development, text-to-text, standardized, input-output, interface, McCann, Radford, Raffel, enabled, taskagnostic, architectures, zero-shot, transfer, downstream | 논문이 명시한 observation과 task input | body cue; exact tensor/frame verify |
| State/latent | development, text-to-text, standardized, input-output, interface, McCann, Radford, Raffel, enabled, taskagnostic | task state 또는 decision variable | body cue; notation verify |
| Action/output | Pre-training, methods, learn, directly, text, have, revolutionized, NLP, over, last | paper-specific output/action | body cue; unit/decoder verify |
| Objective/constraint | knowledge, batch, construction, technique, objective, first, introduced, area, deep, metric | paper-specific objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1. Introduction and Motivating Work - extractive body cue:** The development of "text-to-text" as a standardized input-output interface (McCann et al., 2018; Radford et al., 2019; Raffel et al., 2019) has enabled taskagnostic architectures ...
- **p. 2 / 1. Introduction and Motivating Work - extractive body cue:** When fine-tuned to ImageNet these pre-trained models increased accuracy by over 5% and improved the overall state of the art at the time.
- **p. 3 / 2.1. Natural Language Supervision - extractive body cue:** As discussed in the introduction, this is not at all a new idea, however terminology used to describe work in this space is varied, even ...
- **p. 4 / 2.3. Selecting an Efficient Pre-Training Method - extractive body cue:** State-of-the-art computer vision systems use very large amounts of compute.
- **p. 3 / 2.2. Creating a Sufficiently Large Dataset - extractive body cue:** After filtering to keep only images with natural language titles and/or descriptions in English, the dataset shrunk by a factor of 6 to only 15 ...
- **p. 4 / 2.2. Creating a Sufficiently Large Dataset - extractive body cue:** Learning Transferable Visual Models From Natural Language Supervision 4 balance the results by including up to 20,000 (image, text) pairs per query.
- **p. 5 / 2.4. Choosing and Scaling a Model - extractive body cue:** While previous computer vision research has often scaled models by increasing the width (Mahajan et al., 2018) or depth (He et al., 2016a) in isolation, ...
- **Normalized interface:** observation=논문이 명시한 observation과 task input; state=task state 또는 decision variable; output/action=paper-specific output/action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | Continuing with this interpretation, every step of CLIP pre-training can be viewed as optimizing the performance of a randomly created proxy to ... | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | CLIP is a significant step towards flexible and practical zero-shot computer vision classifiers. | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | Mixed-precision (Micikevicius et al., 2017) was used to accelerate training and save memory. | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 2.1. Natural Language Supervision - extractive body cue:** Learning from natural language has several potential strengths over other training methods.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Learning, Transferable, Visual, Models, Natural, Language, Supervision, image_encoder, ResNet, Vision, Transformer, text_encoder, CBOW, Text, minibatch, aligned, images, texts, W_i, learned.
- **Relevant PDF headings:** 2. Approach (p. 3); 2.3. Selecting an Efficient Pre-Training Method (p. 4); 2.4. Choosing and Scaling a Model (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Input representation | The 20 datasets with at least 16 examples per class were used in this analysis. we see that zero-shot CLIP is quite ... | p. 9 (3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE), p. 6 (3.1.1. MOTIVATION) |
| Core objective / transformation | Compared to the baseline of using contextless class names, prompt engineering and ensembling boost zero-shot classification performance by almost 5 points on ... | p. 7 (3.1.4. PROMPT ENGINEERING AND ENSEMBLING), p. 8 (3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE) |
| Downstream transfer boundary | Learning Transferable Visual Models From Natural Language Supervision 8 Similar to the "prompt engineering" discussion around GPT3 (Brown et al., 2020; Gao ... | p. 8 (3.1.4. PROMPT ENGINEERING AND ENSEMBLING), p. 6 (3.1.3. INITIAL COMPARISON TO VISUAL N-GRAMS) |

## Failure and Ablation Link

- **p. 6 / 3.1.1. MOTIVATION - extractive body cue:** While GPT-1 (Radford et al., 2018) focused on pretraining as a transfer learning method to improve supervised fine-tuning, it also included an ablation study demonstrating ...
- **p. 8 / 3.1.4. PROMPT ENGINEERING AND ENSEMBLING - extractive body cue:** Finally, we found that on satellite image classification datasets it helped to specify that the images were of this form and we use variants of ...
- **p. 15 / 3.3. Robustness to Natural Distribution Shift - extractive body cue:** As a step towards understanding whether pre-trained zero-shot models consistently have higher effective robustness than fine-tuned models, we encourage the authors of Mahajan et al.
- **p. 17 / 5. Data Overlap Analysis - extractive body cue:** One option to prevent this is to identify and remove all duplicates before training a model.
- **p. 46 / Figure/Table caption - extractive body cue:** Table 13. CLIP improves zero-shot retrieval and is competitive with the best fine-tuned result on Flickr30k text retrieval. Bold indicates best overall performance while an ...
- **p. 11 / 3.2. Representation Learning - extractive body cue:** An alternative is measuring the performance of end-to-end fine-tuning of the model.
- **p. 11 / 3.2. Representation Learning - extractive body cue:** Our best overall model is a ViT-L/14 that is fine-tuned at a higher resolution of 336 pixels on our dataset for 1 additional epoch.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (2.4. Choosing and Scaling a Model), p. 4 (2.4. Choosing and Scaling a Model), p. 4 (2.3. Selecting an Efficient Pre-Training Method), p. 5 (2.4. Choosing and Scaling a Model), p. 3 (2.1. Natural Language Supervision), p. 3 (2.1. Natural Language Supervision), objective p. 4 (2.3. Selecting an Efficient Pre-Training Method), p. 4 (2.3. Selecting an Efficient Pre-Training Method), p. 5 (2.5. Training), p. 5 (2.5. Training), p. 3 (2.1. Natural Language Supervision), temporal p. 6 (3.1.2. USING CLIP FOR ZERO-SHOT TRANSFER), p. 7 (3.1.3. INITIAL COMPARISON TO VISUAL N-GRAMS), p. 15 (3.3. Robustness to Natural Distribution Shift), p. 5 (2.4. Choosing and Scaling a Model), p. 5 (2.5. Training), p. 17 (4. Comparison to Human Performance).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
