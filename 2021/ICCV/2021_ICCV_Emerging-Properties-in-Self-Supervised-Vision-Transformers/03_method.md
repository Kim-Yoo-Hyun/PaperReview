# Method - Emerging Properties in Self-Supervised Vision Transformers

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2104.14294; PDF retrieval source: https://arxiv.org/pdf/2104.14294. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.1. SSL with Knowledge Distillation), p. 4 (3.1. SSL with Knowledge Distillation), p. 3 (3.1. SSL with Knowledge Distillation), p. 3 (3.1. SSL with Knowledge Distillation)): The neural network g is composed of a backbone f (ViT [19] or ResNet [34]), and of a projection head h: g = h ◦f.

## Method Body Digest

- **p. 4 / 3.1. SSL with Knowledge Distillation - extractive PDF cue:** The neural network g is composed of a backbone f (ViT [19] or ResNet [34]), and of a projection head h: g = h ◦f.
- **p. 4 / 3.1. SSL with Knowledge Distillation - extractive PDF cue:** While our framework can be stabilized with multiple normalizations [10], it can also work with only a centering and sharpening of the momentum teacher outputs ...
- **p. 3 / 3.1. SSL with Knowledge Distillation - extractive PDF cue:** Both networks share the same architecture g with different sets of parameters θs and θt.
- **p. 3 / 3.1. SSL with Knowledge Distillation - extractive PDF cue:** Given a fixed teacher network gθt, we learn to match these distributions by minimizing the cross-entropy loss w.r.t. the parameters of the student network θs: ...
- **p. 3 / 3.1. SSL with Knowledge Distillation - extractive PDF cue:** We minimize the loss: min θs X x∈{xg 1,xg 2} X x′∈V x′̸= x H(Pt(x), Ps(x′)).
- **p. 4 / 3.1. SSL with Knowledge Distillation - extractive PDF cue:** Several self-supervised methods differ by the operation used to avoid collapse, either through contrastive loss [73], clustering constraints [8, 10], predictor [30] or batch normalizations ...
- **p. 4 / 3.1. SSL with Knowledge Distillation - extractive PDF cue:** The update rule is θt ←λθt + (1 -λ)θs, with λ following a cosine schedule from 0.996 to 1 during training [30].
- **p. 3 / 3.1. SSL with Knowledge Distillation - extractive PDF cue:** Given an input image x, both networks output probability distributions over K dimensions denoted by Ps and Pt.

## Design Rationale

- **p. 3 / 3.1. SSL with Knowledge Distillation - extractive PDF cue:** However, our method shares also similarities with knowledge distillation [35] and we present it under this angle.
- **p. 2 / 1. Introduction - extractive PDF cue:** Of particular importance, our framework is flexible and works on both convnets and ViTs without the need to modify the architecture, nor adapt internal normalizations ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Interestingly, our method can work with only a centering and sharpening of the teacher output to avoid collapse, while other popular components such as predictor ...

## Source Evidence Cues

- **p. 4 / 3.1. SSL with Knowledge Distillation - extractive PDF cue:** The neural network g is composed of a backbone f (ViT [19] or ResNet [34]), and of a projection head h: g = h ◦f.
- **p. 4 / 3.1. SSL with Knowledge Distillation - extractive PDF cue:** While our framework can be stabilized with multiple normalizations [10], it can also work with only a centering and sharpening of the momentum teacher outputs ...
- **p. 3 / 3.1. SSL with Knowledge Distillation - extractive PDF cue:** Both networks share the same architecture g with different sets of parameters θs and θt.
- **p. 3 / 3.1. SSL with Knowledge Distillation - extractive PDF cue:** Given a fixed teacher network gθt, we learn to match these distributions by minimizing the cross-entropy loss w.r.t. the parameters of the student network θs: ...
- **Detected method headings:** 3. Approach (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Input representation | source-defined input을 learnable representation으로 바꾼다 | paper-specific image/text/sequence input | encoder, tokenization, normalization 또는 feature extraction을 수행 | latent feature/state | The neural network g is composed of a backbone f (ViT [19] or ResNet [34]), and of a projection head h: g ... | p. 4 (3.1. SSL with Knowledge Distillation), p. 4 (3.1. SSL with Knowledge Distillation) |
| Core objective / transformation | source task의 prediction·generation 목표를 최적화한다 | representation, target/condition | paper-specific model, loss, decoder 또는 generative process를 적용 | prediction/embedding/sample | While our framework can be stabilized with multiple normalizations [10], it can also work with only a centering and sharpening of the ... | p. 4 (3.1. SSL with Knowledge Distillation), p. 3 (3.1. SSL with Knowledge Distillation) |
| Downstream transfer boundary | 결과를 후속 task 또는 embodied system에 전달한다 | output와 query/task context | task head, retrieval, grounding 또는 adapter를 적용 | task cue/representation | Both networks share the same architecture g with different sets of parameters θs and θt. | p. 3 (3.1. SSL with Knowledge Distillation), p. 3 (3.1. SSL with Knowledge Distillation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.1. SSL with Knowledge Distillation - extractive PDF cue:** Given a fixed teacher network gθt, we learn to match these distributions by minimizing the cross-entropy loss w.r.t. the parameters of the student network θs: ...
- **p. 3 / 3.1. SSL with Knowledge Distillation - extractive PDF cue:** We minimize the loss: min θs X x∈{xg 1,xg 2} X x′∈V x′̸= x H(Pt(x), Ps(x′)).
- **p. 4 / 3.1. SSL with Knowledge Distillation - extractive PDF cue:** Several self-supervised methods differ by the operation used to avoid collapse, either through contrastive loss [73], clustering constraints [8, 10], predictor [30] or batch normalizations ...
- **p. 4 / 3.1. SSL with Knowledge Distillation - extractive PDF cue:** The update rule is θt ←λθt + (1 -λ)θs, with λ following a cosine schedule from 0.996 to 1 during training [30].
- **Formal bridge:** source-defined input o -> prediction/embedding/sample ŷ -> paper-specific objective -> source task metric; robot link not established.
- **Equation/algorithm anchors:** p. 4 (3.1. SSL with Knowledge Distillation), p. 3 (3.1. SSL with Knowledge Distillation), p. 3 (3.1. SSL with Knowledge Distillation), p. 4 (3.1. SSL with Knowledge Distillation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, input, image, networks, output, probability, distributions, over, dimensions, denoted, model, passes, different, random | 논문이 명시한 observation과 task input | body cue; exact tensor/frame verify |
| State/latent | Given, input, image, networks, output, probability, distributions, over, dimensions, denoted | task state 또는 decision variable | body cue; notation verify |
| Action/output | However, shares, similarities, knowledge, distillation, present, under, angle, particular, importance | paper-specific output/action | body cue; unit/decoder verify |
| Objective/constraint | Given, fixed, teacher, network, learn, match, distributions, minimizing, cross-entropy, loss | paper-specific objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. SSL with Knowledge Distillation - extractive PDF cue:** Given an input image x, both networks output probability distributions over K dimensions denoted by Ps and Pt.
- **p. 2 / 1. Introduction - extractive PDF cue:** The model passes two different random transformations of an input image to the student and teacher networks.
- **p. 3 / 3.1. SSL with Knowledge Distillation - extractive PDF cue:** The probability P is obtained by normalizing the output of the network g with a softmax function.
- **p. 4 / 3.1. SSL with Knowledge Distillation - extractive PDF cue:** The features used in downstream tasks are the backbone f output.
- **p. 4 / 3.1. SSL with Knowledge Distillation - extractive PDF cue:** While our framework can be stabilized with multiple normalizations [10], it can also work with only a centering and sharpening of the momentum teacher outputs ...
- **p. 2 / 1. Introduction - extractive PDF cue:** The output of the teacher network is centered with a mean computed over the batch.
- **p. 1 / 1. Introduction - extractive PDF cue:** Their adoption has been coupled with a training strategy inspired by natural language processing (NLP), that is, pretraining on large quantities of data and finetuning ...
- **Normalized interface:** observation=논문이 명시한 observation과 task input; state=task state 또는 decision variable; output/action=paper-specific output/action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | We add an extra learnable token to the sequence [18, 19]. | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | The role of this token is to aggregate information from the entire sequence and we attach the projection head h at its ... | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | In practice, this requires large batches [12] or memory banks [33, 73]. | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | The learning rate is linearly ramped up during the first 10 epochs to its base value determined with the following linear scaling ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.2. Implementation and evaluation protocols - extractive PDF cue:** In this section, we provide the implementation details to train with DINO and present the evaluation protocols used in our experiments.
- **p. 6 / 4.1. Comparing with SSL frameworks on ImageNet - extractive PDF cue:** Nonetheless, a base ViT with 8 × 8 patches trained with DINO achieves 80.1% top-1 in linear classification and 77.4% with a k-NN classifier with ...
- **p. 6 / 4.1. Comparing with SSL frameworks on ImageNet - extractive PDF cue:** ViT-S/16 ImNet 33.5 8.9 63.0 37.2 DINO ResNet-50 ImNet 35.4 11.1 55.9 27.5 DINO ViT-S/16 ImNet 41.8 13.7 63.1 34.4 DINO ViT-S/16 GLDv2 51.5 24.3 ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** neural, network, composed, backbone, ViT, ResNet, projection, head, While, framework, stabilized, multiple, normalizations, only, centering, sharpening, momentum, teacher, outputs, avoid.
- **Relevant PDF headings:** 3. Approach (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Input representation | 5 that even though our training objective nor our architecture are designed for dense tasks, the performance is competitive on this benchmark. | p. 7 (4.2. Properties of ViT trained with SSL), p. 5 (3.2. Implementation and evaluation protocols) |
| Core objective / transformation | We observe that DINO features outperform those trained on ImageNet with labels. | p. 6 (4.2. Properties of ViT trained with SSL), p. 6 (4.2. Properties of ViT trained with SSL) |
| Downstream transfer boundary | While training a larger ViT with DINO improves the performance, reducing the size of the patches ("/8" variants) has a bigger impact ... | p. 6 (4.1. Comparing with SSL frameworks on ImageNet), p. 7 (4.2. Properties of ViT trained with SSL) |

## Failure and Ablation Link

- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 9: Effect of batch sizes. Top-1 with k-NN for models trained for 100 epochs without multi-crop. In Tab. 9, we study the impact of ...
- **p. 5 / 3.2. Implementation and evaluation protocols - extractive PDF cue:** We pretrain the models on the ImageNet dataset [60] without labels.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 7: Important component for self-supervised ViT pre- training. Models are trained for 300 epochs with ViT-S/16. We study the different components that matter for ...
- **p. 5 / 3.2. Implementation and evaluation protocols - extractive PDF cue:** We freeze the pretrain model to compute and store the features of the training data of the downstream task.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5: Effect of Patch Size. k-NN eval- uation as a function of the throughputs for dif- ferent input patch sizes with ViT-B and ViT-S. ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Table 1: Networks configuration. "Blocks" is the number of Transformer blocks, "dim" is channel dimension and "heads" is the number of heads in multi-head attention. ...
- **p. 6 / 4.1. Comparing with SSL frameworks on ImageNet - extractive PDF cue:** We explore variants of ViT-S in Appendix D.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.1. SSL with Knowledge Distillation), p. 4 (3.1. SSL with Knowledge Distillation), p. 3 (3.1. SSL with Knowledge Distillation), p. 3 (3.1. SSL with Knowledge Distillation), objective p. 3 (3.1. SSL with Knowledge Distillation), p. 3 (3.1. SSL with Knowledge Distillation), p. 4 (3.1. SSL with Knowledge Distillation), p. 4 (3.1. SSL with Knowledge Distillation), temporal p. 4 (3.2. Implementation and evaluation protocols), p. 4 (3.2. Implementation and evaluation protocols), p. 5 (3.2. Implementation and evaluation protocols), p. 5 (3.2. Implementation and evaluation protocols), p. 2 (2. Related work), p. 2 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
