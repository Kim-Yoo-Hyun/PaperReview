# Method - Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (33 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2303.05499; PDF retrieval source: https://arxiv.org/pdf/2303.05499. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (1. Model Overall), p. 19 (A.1 Hyperparameters), p. 19 (A.2 Pseudo Code Language-Guided Query Selection)): Input Text Input Image Model Outputs Keys& Values Cross-Modality Queries Text Features Image Features Vanilla Text Features A Cross-Modality Decoder Layer Cross-Modality Query Self-Attention Image Cross-Attention Text Cross-Attention FF ...

## Method Body Digest

- **p. 5 / 1. Model Overall - extractive body cue:** Input Text Input Image Model Outputs Keys& Values Cross-Modality Queries Text Features Image Features Vanilla Text Features A Cross-Modality Decoder Layer Cross-Modality Query Self-Attention Image ...
- **p. 19 / A.1 Hyperparameters - extractive body cue:** Item Value optimizer AdamW lr 1e-4 lr of image backbone 1e-5 lr of text backbone 1e-5 weight decay 0.0001 clip max norm 0.1 number of ...
- **p. 19 / A.2 Pseudo Code Language-Guided Query Selection - extractive body cue:** We use bs and ndim for batch size and feature dimension in the pseudo-code. num_img_tokens and num_text_tokens are used for the number of image and ...
- **p. 2 / 1 Introduction - extractive body cue:** The key to achieving this goal is using contrastive loss between region outputs and language features at the neck and/or head outputs.
- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we aim to develop a strong system to detect arbitrary objects specified by human language inputs, a task commonly referred to as ...
- **p. 3 / 1 Introduction - extractive body cue:** For example, GLIP [25] performs early fusion in the neck module (phase A), and OV-DETR [55] uses language-aware queries as head inputs (phase B).
- **p. 3 / 1 Introduction - extractive body cue:** It removes the attention between unrelated categories during word feature extractions.
- **p. 4 / 1 Introduction - extractive body cue:** It also establishes a new state of the art on the ODinW [23] zero-shot benchmark with a 26.1 mean AP.

## Design Rationale

- **p. 3 / 1 Introduction - extractive body cue:** To mitigate this issue and improve model performance during grounded training, we introduce a technique that utilizes sub-sentence level text features.
- **p. 3 / 1 Introduction - extractive body cue:** The layer-by-layer design enables it to interact with language information easily.
- **p. 19 / A.2 Pseudo Code Language-Guided Query Selection - extractive body cue:** We present the pseudo-code of the Language-Guided Query Selection module in Algorithm 1.

## Source Evidence Cues

- **p. 5 / 1. Model Overall - extractive body cue:** Input Text Input Image Model Outputs Keys& Values Cross-Modality Queries Text Features Image Features Vanilla Text Features A Cross-Modality Decoder Layer Cross-Modality Query Self-Attention Image ...
- **p. 19 / A.1 Hyperparameters - extractive body cue:** Item Value optimizer AdamW lr 1e-4 lr of image backbone 1e-5 lr of text backbone 1e-5 weight decay 0.0001 clip max norm 0.1 number of ...
- **p. 19 / A.2 Pseudo Code Language-Guided Query Selection - extractive body cue:** We use bs and ndim for batch size and feature dimension in the pseudo-code. num_img_tokens and num_text_tokens are used for the number of image and ...
- **Detected method headings:** 1. Model Overall (p. 5); C.4 Model Efficiency (p. 22); 1. Model Overall (p. 23)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Input representation | source-defined input을 learnable representation으로 바꾼다 | paper-specific image/text/sequence input | encoder, tokenization, normalization 또는 feature extraction을 수행 | latent feature/state | Input Text Input Image Model Outputs Keys& Values Cross-Modality Queries Text Features Image Features Vanilla Text Features A Cross-Modality Decoder Layer Cross-Modality ... | p. 5 (1. Model Overall), p. 19 (A.1 Hyperparameters) |
| Core objective / transformation | source task의 prediction·generation 목표를 최적화한다 | representation, target/condition | paper-specific model, loss, decoder 또는 generative process를 적용 | prediction/embedding/sample | Item Value optimizer AdamW lr 1e-4 lr of image backbone 1e-5 lr of text backbone 1e-5 weight decay 0.0001 clip max norm ... | p. 19 (A.1 Hyperparameters), p. 19 (A.2 Pseudo Code Language-Guided Query Selection) |
| Downstream transfer boundary | 결과를 후속 task 또는 embodied system에 전달한다 | output와 query/task context | task head, retrieval, grounding 또는 adapter를 적용 | task cue/representation | We use bs and ndim for batch size and feature dimension in the pseudo-code. num_img_tokens and num_text_tokens are used for the number ... | p. 19 (A.2 Pseudo Code Language-Guided Query Selection) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 19 / A.1 Hyperparameters - extractive body cue:** Item Value optimizer AdamW lr 1e-4 lr of image backbone 1e-5 lr of text backbone 1e-5 weight decay 0.0001 clip max norm 0.1 number of ...
- **p. 5 / 1. Model Overall - extractive body cue:** Input Text Input Image Model Outputs Keys& Values Cross-Modality Queries Text Features Image Features Vanilla Text Features A Cross-Modality Decoder Layer Cross-Modality Query Self-Attention Image ...
- **Formal bridge:** source-defined input o -> prediction/embedding/sample ŷ -> paper-specific objective -> source task metric; robot link not established.
- **Equation/algorithm anchors:** p. 19 (A.1 Hyperparameters), p. 5 (1. Model Overall).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Input, Text, Image, Model, Outputs, Keys, Values, Cross-Modality, Queries, Features, Vanilla, Decoder, Layer, Query | 논문이 명시한 observation과 task input | body cue; exact tensor/frame verify |
| State/latent | Input, Text, Image, Model, Outputs, Keys, Values, Cross-Modality, Queries, Features | task state 또는 decision variable | body cue; notation verify |
| Action/output | mitigate, issue, improve, model, performance, during, grounded, training, introduce, technique | paper-specific output/action | body cue; unit/decoder verify |
| Objective/constraint | Item, Value, optimizer, AdamW, image, backbone, text, weight, decay, clip | paper-specific objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 1. Model Overall - extractive body cue:** Input Text Input Image Model Outputs Keys& Values Cross-Modality Queries Text Features Image Features Vanilla Text Features A Cross-Modality Decoder Layer Cross-Modality Query Self-Attention Image ...
- **p. 2 / 1 Introduction - extractive body cue:** The key to achieving this goal is using contrastive loss between region outputs and language features at the neck and/or head outputs.
- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we aim to develop a strong system to detect arbitrary objects specified by human language inputs, a task commonly referred to as ...
- **p. 3 / 1 Introduction - extractive body cue:** For example, GLIP [25] performs early fusion in the neck module (phase A), and OV-DETR [55] uses language-aware queries as head inputs (phase B).
- **p. 3 / 1 Introduction - extractive body cue:** It removes the attention between unrelated categories during word feature extractions.
- **p. 4 / 1 Introduction - extractive body cue:** It also establishes a new state of the art on the ODinW [23] zero-shot benchmark with a 26.1 mean AP.
- **p. 19 / A.2 Pseudo Code Language-Guided Query Selection - extractive body cue:** We present the pseudo-code of the Language-Guided Query Selection module in Algorithm 1.
- **Normalized interface:** observation=논문이 명시한 observation과 task input; state=task state 또는 decision variable; output/action=paper-specific output/action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | While some studies have examined open-set detection models under a "partial label" framework-training on a subset of data (e.g., base categories) and ... | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | OV-DETR [56] uses image and text embedding encoded by a CLIP model as queries to decode the category-specified boxes in the DETR ... | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | not recovered | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 19 / A.1 Hyperparameters - extractive body cue:** Item Value optimizer AdamW lr 1e-4 lr of image backbone 1e-5 lr of text backbone 1e-5 weight decay 0.0001 clip max norm 0.1 number of ...
- **p. 9 / 4 Experiments - extractive body cue:** The model is trained on 64 Nvidia A100 GPUs with a total batch size of 64.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Input, Text, Image, Model, Outputs, Keys, Values, Cross-Modality, Queries, Features, Vanilla, Decoder, Layer, Query, Self-Attention, Cross-Attention, FFN, Updated, Item, Value.
- **Relevant PDF headings:** 1. Model Overall (p. 5); C.4 Model Efficiency (p. 22); 1. Model Overall (p. 23).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Input representation | LVIS Benchmark LVIS [15] is a dataset for long-tail objects. | p. 10 (4 Experiments), p. 11 (4 Experiments) |
| Core objective / transformation | Table 2. We pre-train models on large-scale datasets and directly evaluate our model on the COCO benchmark. As the O365 dataset [43] ... | p. 9 (Figure/Table caption), p. 10 (4 Experiments) |
| Downstream transfer boundary | Table 9: Transfer pre-trained DINO to Grounding DINO. We freeze shared modules between DINO and Grounding DINO during grounded fine-tuning. All models ... | p. 21 (Figure/Table caption), p. 13 (4 Experiments) |

## Failure and Ablation Link

- **p. 13 / Figure/Table caption - extractive body cue:** Table 6: Impacts of RefC and COCO data for open-set settings. All models are trained with a Swin Transformer Tiny backbone. 4.5 Ablations We conduct ...
- **p. 14 / Figure/Table caption - extractive body cue:** Table 7: Ablations for our model. All models are trained on the O365 dataset with a Swin Transformer Tiny backbone. fusion approach. Moreover, we extend ...
- **p. 21 / Figure/Table caption - extractive body cue:** Table 10: Comparison between two Grounding DINO variants: Training from scratch and transfer from DINO-pretrained models. The models are trained on O365 and evaluated on ...
- **p. 8 / 4 Experiments - extractive body cue:** Ablations are then conducted to show the effectiveness of our model design (Sec.
- **p. 10 / 4 Experiments - extractive body cue:** To our knowledge, no existing DETR-like models effectively address the rarity challenge in LVIS without extra training data, which may be a characteristic limitation of ...
- **p. 9 / 4 Experiments - extractive body cue:** 4.1 Implementation Details We trained two model variants, Grounding DINO T with Swin-T [32], and Grounding DINO L with Swin-L [32] as an image backbone, ...
- **p. 10 / 4 Experiments - extractive body cue:** With stronger backbones and larger data, Grounding DINO sets a new record of 52.5 AP on the COCO object detection benchmark without seeing any COCO ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (1. Model Overall), p. 19 (A.1 Hyperparameters), p. 19 (A.2 Pseudo Code Language-Guided Query Selection), objective p. 19 (A.1 Hyperparameters), p. 5 (1. Model Overall), temporal p. 3 (1 Introduction), p. 4 (2 Related Work), p. 5 (2. A Feature Enhancer Layer), p. 5 (2. A Feature Enhancer Layer).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
