# Method - DINOv2: Learning Robust Visual Features without Supervision

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (32 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2304.07193; PDF retrieval source: https://arxiv.org/pdf/2304.07193. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 31 (B.1 Unsupervised pre-training), p. 31 (B.2 High-Resolution adaptation), p. 29 (B.1 Unsupervised pre-training), p. 29 (B.1 Unsupervised pre-training), p. 30 (B.1 Unsupervised pre-training), p. 30 (B.1 Unsupervised pre-training)): We use MLP feed-forward networks for distilled models, and SwiGLU (Shazeer, 2020) when training from scratch.

## Method Body Digest

- **p. 31 / B.1 Unsupervised pre-training - extractive PDF cue:** We use MLP feed-forward networks for distilled models, and SwiGLU (Shazeer, 2020) when training from scratch.
- **p. 31 / B.2 High-Resolution adaptation - extractive PDF cue:** We initialise the model with the pretrained weights then train it for 10k iterations with the same procedure as the original pretraining.
- **p. 29 / B.1 Unsupervised pre-training - extractive PDF cue:** We use hyperparameters shown in Table 16, ViT architectures described in Table 17.
- **p. 29 / B.1 Unsupervised pre-training - extractive PDF cue:** For unsupervised pre-training we build on the DINO and iBOT codebases.
- **p. 30 / B.1 Unsupervised pre-training - extractive PDF cue:** We kept a few datasets aside in order to evaluate performance outside of the pretraining domain.
- **p. 30 / B.1 Unsupervised pre-training - extractive PDF cue:** We chose to include as many datasets as possible in the pretraining data in order to cover as many domains as possible.
- **p. 31 / B.1 Unsupervised pre-training - extractive PDF cue:** All models run for 625k iterations with optimizer AdamW, an initial LayerScale value of 1e-5, a weight decay cosine schedule from 0.04 to 0.2, a ...
- **p. 29 / B.1 Unsupervised pre-training - extractive PDF cue:** We apply the KoLeo regularizer with a weight of 0.1 between the class tokens of the first global crop, for all samples within a GPU ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** Most of our technical contributions are tailored toward stabilizing and accelerating discriminative self-supervised learning when scaling in model and data sizes.
- **p. 2 / 1 Introduction - extractive PDF cue:** We gathered a small but diverse corpus of 142M images to validate our approach.
- **p. 3 / 1 Introduction - extractive PDF cue:** We show performance on eight types of vision tasks, as presented in Sec.

## Source Evidence Cues

- **p. 31 / B.1 Unsupervised pre-training - extractive PDF cue:** We use MLP feed-forward networks for distilled models, and SwiGLU (Shazeer, 2020) when training from scratch.
- **p. 31 / B.2 High-Resolution adaptation - extractive PDF cue:** We initialise the model with the pretrained weights then train it for 10k iterations with the same procedure as the original pretraining.
- **p. 29 / B.1 Unsupervised pre-training - extractive PDF cue:** We use hyperparameters shown in Table 16, ViT architectures described in Table 17.
- **p. 29 / B.1 Unsupervised pre-training - extractive PDF cue:** For unsupervised pre-training we build on the DINO and iBOT codebases.
- **p. 30 / B.1 Unsupervised pre-training - extractive PDF cue:** We kept a few datasets aside in order to evaluate performance outside of the pretraining domain.
- **p. 30 / B.1 Unsupervised pre-training - extractive PDF cue:** We chose to include as many datasets as possible in the pretraining data in order to cover as many domains as possible.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Input representation | source-defined input을 learnable representation으로 바꾼다 | paper-specific image/text/sequence input | encoder, tokenization, normalization 또는 feature extraction을 수행 | latent feature/state | We use MLP feed-forward networks for distilled models, and SwiGLU (Shazeer, 2020) when training from scratch. | p. 31 (B.1 Unsupervised pre-training), p. 31 (B.2 High-Resolution adaptation) |
| Core objective / transformation | source task의 prediction·generation 목표를 최적화한다 | representation, target/condition | paper-specific model, loss, decoder 또는 generative process를 적용 | prediction/embedding/sample | We initialise the model with the pretrained weights then train it for 10k iterations with the same procedure as the original pretraining. | p. 31 (B.2 High-Resolution adaptation), p. 29 (B.1 Unsupervised pre-training) |
| Downstream transfer boundary | 결과를 후속 task 또는 embodied system에 전달한다 | output와 query/task context | task head, retrieval, grounding 또는 adapter를 적용 | task cue/representation | We use hyperparameters shown in Table 16, ViT architectures described in Table 17. | p. 29 (B.1 Unsupervised pre-training), p. 29 (B.1 Unsupervised pre-training) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 31 / B.1 Unsupervised pre-training - extractive PDF cue:** All models run for 625k iterations with optimizer AdamW, an initial LayerScale value of 1e-5, a weight decay cosine schedule from 0.04 to 0.2, a ...
- **p. 29 / B.1 Unsupervised pre-training - extractive PDF cue:** We apply the KoLeo regularizer with a weight of 0.1 between the class tokens of the first global crop, for all samples within a GPU ...
- **p. 31 / B.1 Unsupervised pre-training - extractive PDF cue:** It is updated at the end of every training step.
- **Formal bridge:** source-defined input o -> prediction/embedding/sample ŷ -> paper-specific objective -> source task metric; robot link not established.
- **Equation/algorithm anchors:** p. 31 (B.1 Unsupervised pre-training), p. 31 (B.1 Unsupervised pre-training).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Published, Transactions, Machine, Learning, Research, flops, Accuracy, Inet-1k, mIoU, Segmentation, R-MSE, Monocular, Depth, Classification | 논문이 명시한 observation과 task input | body cue; exact tensor/frame verify |
| State/latent | Published, Transactions, Machine, Learning, Research, flops, Accuracy, Inet-1k, mIoU, Segmentation | task state 또는 decision variable | body cue; notation verify |
| Action/output | Most, technical, contributions, tailored, toward, stabilizing, accelerating, discriminative, self-supervised, learning | paper-specific output/action | body cue; unit/decoder verify |
| Objective/constraint | models, iterations, optimizer, AdamW, initial, LayerScale, value, weight, decay, cosine | paper-specific objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 1 Introduction - extractive PDF cue:** Published in Transactions on Machine Learning Research (01/2024) 1010 1011 1012 flops 75 78 81 84 87 Accuracy Inet-1k 1010 1011 1012 flops 40 48 ...
- **p. 30 / B.1 Unsupervised pre-training - extractive PDF cue:** Published in Transactions on Machine Learning Research (01/2024) Task Dataset / Split Images Retrieval Retrieved Final classification ImageNet-22k / - 14,197,086 as is - 14,197,086 ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Published in Transactions on Machine Learning Research (01/2024) Figure 1: Visualization of the first PCA components.
- **p. 2 / 1 Introduction - extractive PDF cue:** Additionally, the features output by self-supervised models have been shown to exhibit various useful properties, and have enabled enabled a wide variety of applications (Amir ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Our family of models drastically improves over the previous state of the art in self-supervised learning and reaches performance comparable with weaklysupervised features.
- **p. 31 / B.1 Unsupervised pre-training - extractive PDF cue:** The teacher is initialized with the same state as the student, and is an exponential moving average of the student network, with a momentum value ...
- **p. 1 / 1 Introduction - extractive PDF cue:** These models should generate visual features that work out of the box on any task, both at the image level, e.g., image classification, and pixel ...
- **Normalized interface:** observation=논문이 명시한 observation과 task input; state=task state 또는 decision variable; output/action=paper-specific output/action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | We apply the KoLeo regularizer with a weight of 0.1 between the class tokens of the first global crop, for all samples ... | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | It is updated at the end of every training step. | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | These improvements make our approach around 2× faster and require 3× less memory than similar discriminative self-supervised methods, allowing us to leverage ... | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 31 / B.1 Unsupervised pre-training - extractive PDF cue:** We use MLP feed-forward networks for distilled models, and SwiGLU (Shazeer, 2020) when training from scratch.
- **p. 31 / B.2 High-Resolution adaptation - extractive PDF cue:** We initialise the model with the pretrained weights then train it for 10k iterations with the same procedure as the original pretraining.
- **p. 29 / B.1 Unsupervised pre-training - extractive PDF cue:** For unsupervised pre-training we build on the DINO and iBOT codebases.
- **p. 30 / B.1 Unsupervised pre-training - extractive PDF cue:** We kept a few datasets aside in order to evaluate performance outside of the pretraining domain.
- **p. 30 / B.1 Unsupervised pre-training - extractive PDF cue:** We chose to include as many datasets as possible in the pretraining data in order to cover as many domains as possible.
- **p. 31 / B.2 High-Resolution adaptation - extractive PDF cue:** All the hyperparameters are kept the same as in the first pretraining, except the base learning rate which is reduced.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** MLP, feed-forward, networks, distilled, models, SwiGLU, Shazeer, when, training, scratch, initialise, model, pretrained, weights, then, train, iterations, same, procedure, original.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Input representation | This benchmark covers scenes, objects (food, cars, planes), and textures. | p. 13 (7 Results), p. 13 (7 Results) |
| Core objective / transformation | When comparing with state-of-the-art SSL methods, our models shows drastically better robustness (+29.6% on A (Hendrycks et al., 2021b), +22.1% on R ... | p. 12 (7 Results), p. 14 (7 Results) |
| Downstream transfer boundary | Figure 6: Role of resolution. Performance of ViT-L/16 trained on ImageNet-1k at fixed resolution ("224" and "416") or trained at 224 then ... | p. 10 (Figure/Table caption), p. 13 (7 Results) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Ablation of the source of pretraining data. We compare the INet-22k dataset that was used in iBOT to our dataset, LVD-142M. Each model ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 3: (a) Effect of the KoLeo loss term. (b) Effect of the iBOT Masked Image Modeling (MIM) loss term. Evaluation performed on ImageNet-{1k,A} (classification ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Visualization of the first PCA components. We compute a PCA between the patches of the images from the same column (a, b, c ...
- **p. 18 / 7 Results - extractive PDF cue:** Background is removed by removing patches with a negative score of the first PCA component.
- **p. 12 / Figure/Table caption - extractive PDF cue:** Table 4: Linear evaluation on ImageNet-1k of frozen pretrained features. We report Top-1 accuracy on the validation set for publicly available models trained on public ...
- **p. 30 / Figure/Table caption - extractive PDF cue:** Table 15: Composition of our LVD-142M dataset. We report the list of datasets and associated splits used to build the dataset, how they were included ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 1: Ablation study of the training differences between iBOT and DINOv2. We optimize for k-NN performance, as in our experience, the linear probe performance ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 31 (B.1 Unsupervised pre-training), p. 31 (B.2 High-Resolution adaptation), p. 29 (B.1 Unsupervised pre-training), p. 29 (B.1 Unsupervised pre-training), p. 30 (B.1 Unsupervised pre-training), p. 30 (B.1 Unsupervised pre-training), objective p. 31 (B.1 Unsupervised pre-training), p. 29 (B.1 Unsupervised pre-training), p. 31 (B.1 Unsupervised pre-training), temporal p. 29 (B.1 Unsupervised pre-training), p. 31 (B.1 Unsupervised pre-training), p. 10 (2 Related Work), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (2 Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
