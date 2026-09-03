# Method - ALIGN: Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2102.05918; PDF retrieval source: https://arxiv.org/pdf/2102.05918. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (4.1. Pre-training on Noisy Image-Text Pairs), p. 3 (4.1. Pre-training on Noisy Image-Text Pairs), p. 4 (4.3. Transferring to Visual Classification), p. 9 (8. Multilingual ALIGN Model), p. 4 (4.3. Transferring to Visual Classification), p. 9 (8. Multilingual ALIGN Model)): The model consists of a pair of image and text encoders with a cosine-similarity combination function at the top.

## Method Body Digest

- **p. 3 / 4.1. Pre-training on Noisy Image-Text Pairs - extractive body cue:** The model consists of a pair of image and text encoders with a cosine-similarity combination function at the top.
- **p. 3 / 4.1. Pre-training on Noisy Image-Text Pairs - extractive body cue:** We use EfficientNet with global pooling (without training the 1x1 conv layer in the classification head) as the image encoder and BERT with [CLS] token ...
- **p. 4 / 4.3. Transferring to Visual Classification - extractive body cue:** (2020), we also evaluate the robustness of our model on Visual Task Adaptation Benchmark (VTAB) (Zhai et al., 2019) which consists of 19 diverse (covering ...
- **p. 9 / 8. Multilingual ALIGN Model - extractive body cue:** Model training follows the exact English configuration.
- **p. 4 / 4.3. Transferring to Visual Classification - extractive body cue:** We first apply zero-shot transfer of ALIGN to visual classification tasks on ImageNet ILSVRC-2012 benchmark (Deng et al., 2009) and its variants including ImageNet-R(endition) (Hendrycks ...
- **p. 9 / 8. Multilingual ALIGN Model - extractive body cue:** A multilingual model ALIGNmling is trained using this data.
- **p. 3 / 4.1. Pre-training on Noisy Image-Text Pairs - extractive body cue:** We minimize the sum of two losses: one for image-to-text classification Li2t = -1 N N X i log exp(x⊤ i yi/σ) PN j=1 exp(x⊤ ...
- **p. 3 / 4.1. Pre-training on Noisy Image-Text Pairs - extractive body cue:** The image and text encoders are optimized via normalized softmax loss (Zhai & Wu, 2019).

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Moreover, such cross-modality matching naturally enables zero-shot image classification when feeding the classnames into the text encoder, achieving 76.4% top-1 accuracy in ImageNet without using ...
- **p. 3 / 4.1. Pre-training on Noisy Image-Text Pairs - extractive body cue:** The model consists of a pair of image and text encoders with a cosine-similarity combination function at the top.
- **p. 4 / 4.3. Transferring to Visual Classification - extractive body cue:** (2020), we also evaluate the robustness of our model on Visual Task Adaptation Benchmark (VTAB) (Zhai et al., 2019) which consists of 19 diverse (covering ...

## Source Evidence Cues

- **p. 3 / 4.1. Pre-training on Noisy Image-Text Pairs - extractive body cue:** The model consists of a pair of image and text encoders with a cosine-similarity combination function at the top.
- **p. 3 / 4.1. Pre-training on Noisy Image-Text Pairs - extractive body cue:** We use EfficientNet with global pooling (without training the 1x1 conv layer in the classification head) as the image encoder and BERT with [CLS] token ...
- **p. 4 / 4.3. Transferring to Visual Classification - extractive body cue:** (2020), we also evaluate the robustness of our model on Visual Task Adaptation Benchmark (VTAB) (Zhai et al., 2019) which consists of 19 diverse (covering ...
- **p. 9 / 8. Multilingual ALIGN Model - extractive body cue:** Model training follows the exact English configuration.
- **p. 4 / 4.3. Transferring to Visual Classification - extractive body cue:** We first apply zero-shot transfer of ALIGN to visual classification tasks on ImageNet ILSVRC-2012 benchmark (Deng et al., 2009) and its variants including ImageNet-R(endition) (Hendrycks ...
- **p. 9 / 8. Multilingual ALIGN Model - extractive body cue:** A multilingual model ALIGNmling is trained using this data.
- **Detected method headings:** 6.1. Model Architectures (p. 7); 8. Multilingual ALIGN Model (p. 9)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Input representation | source-defined input을 learnable representation으로 바꾼다 | paper-specific image/text/sequence input | encoder, tokenization, normalization 또는 feature extraction을 수행 | latent feature/state | The model consists of a pair of image and text encoders with a cosine-similarity combination function at the top. | p. 3 (4.1. Pre-training on Noisy Image-Text Pairs), p. 3 (4.1. Pre-training on Noisy Image-Text Pairs) |
| Core objective / transformation | source task의 prediction·generation 목표를 최적화한다 | representation, target/condition | paper-specific model, loss, decoder 또는 generative process를 적용 | prediction/embedding/sample | We use EfficientNet with global pooling (without training the 1x1 conv layer in the classification head) as the image encoder and BERT ... | p. 3 (4.1. Pre-training on Noisy Image-Text Pairs), p. 4 (4.3. Transferring to Visual Classification) |
| Downstream transfer boundary | 결과를 후속 task 또는 embodied system에 전달한다 | output와 query/task context | task head, retrieval, grounding 또는 adapter를 적용 | task cue/representation | (2020), we also evaluate the robustness of our model on Visual Task Adaptation Benchmark (VTAB) (Zhai et al., 2019) which consists of ... | p. 4 (4.3. Transferring to Visual Classification), p. 9 (8. Multilingual ALIGN Model) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 4.1. Pre-training on Noisy Image-Text Pairs - extractive body cue:** We minimize the sum of two losses: one for image-to-text classification Li2t = -1 N N X i log exp(x⊤ i yi/σ) PN j=1 exp(x⊤ ...
- **p. 3 / 4.1. Pre-training on Noisy Image-Text Pairs - extractive body cue:** The image and text encoders are optimized via normalized softmax loss (Zhai & Wu, 2019).
- **p. 9 / 8. Multilingual ALIGN Model - extractive body cue:** Given that, we further lift the language constraint of the conceptual caption data processing pipeline to extend the dataset to multilingual (covering 100+ languages) and ...
- **p. 9 / 8. Multilingual ALIGN Model - extractive body cue:** One advantage of ALIGN is that the model is trained on noisy web image text data with very simple filters, and none of the filters ...
- **Formal bridge:** source-defined input o -> prediction/embedding/sample ŷ -> paper-specific objective -> source task metric; robot link not established.
- **Equation/algorithm anchors:** p. 3 (4.1. Pre-training on Noisy Image-Text Pairs), p. 3 (4.1. Pre-training on Noisy Image-Text Pairs), p. 9 (8. Multilingual ALIGN Model).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | aligned, image, text, representations, naturally, suited, cross-modality, matching/retrieval, tasks, achieve, state-of-the-art, SOTA, corresponding, benchmarks | 논문이 명시한 observation과 task input | body cue; exact tensor/frame verify |
| State/latent | aligned, image, text, representations, naturally, suited, cross-modality, matching/retrieval, tasks, achieve | task state 또는 decision variable | body cue; notation verify |
| Action/output | Moreover, cross-modality, matching, naturally, enables, zero-shot, image, classification, when, feeding | paper-specific output/action | body cue; unit/decoder verify |
| Objective/constraint | minimize, losses, image-to-text, classification, Li2t, other, text-to-image, Lt2i, Here, normalized | paper-specific objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** The aligned image and text representations are naturally suited for cross-modality matching/retrieval tasks and achieve state-of-the-art (SOTA) results in corresponding benchmarks.
- **p. 1 / 1. Introduction - extractive body cue:** In this work, we leverage a dataset of over one billion noisy image alt-text pairs to scale visual and vision-language representation learning.
- **p. 1 / 1. Introduction - extractive body cue:** However, vision-language pre-training datasets such as Conceptual Captions (Sharma et al., 2018), Visual Genome Dense Captions (Krishna et al., 2016), and ImageBERT (Qi et al., ...
- **p. 2 / 1. Introduction - extractive body cue:** Visual and language representations are jointly learned from noisy image alt-text data.
- **p. 4 / 4.3. Transferring to Visual Classification - extractive body cue:** For this purpose, we use the ImageNet as well as a handful of smaller fine-grained classification datasets such as Oxford Flowers-102 (Nilsback & Zisserman, 2008), ...
- **p. 9 / 8. Multilingual ALIGN Model - extractive body cue:** One advantage of ALIGN is that the model is trained on noisy web image text data with very simple filters, and none of the filters ...
- **p. 9 / 8. Multilingual ALIGN Model - extractive body cue:** Given that, we further lift the language constraint of the conceptual caption data processing pipeline to extend the dataset to multilingual (covering 100+ languages) and ...
- **Normalized interface:** observation=논문이 명시한 observation과 task input; state=task state 또는 decision variable; output/action=paper-specific output/action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | But instead of applying the complex filtering and post-processing steps as proposed by (Sharma et al., 2018) to clean the dataset, we ... | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | For BERT we use wordpiece sequence of maximum 64 tokens since the input texts are no longer than 20 unigrams. | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | not recovered | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | For BERT we use wordpiece sequence of maximum 64 tokens since the input texts are no longer than 20 unigrams. | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 4.1. Pre-training on Noisy Image-Text Pairs - extractive body cue:** We use EfficientNet with global pooling (without training the 1x1 conv layer in the classification head) as the image encoder and BERT with [CLS] token ...
- **p. 4 / 4.3. Transferring to Visual Classification - extractive body cue:** (2020), we also evaluate the robustness of our model on Visual Task Adaptation Benchmark (VTAB) (Zhai et al., 2019) which consists of 19 diverse (covering ...
- **p. 9 / 8. Multilingual ALIGN Model - extractive body cue:** Model training follows the exact English configuration.
- **p. 9 / 8. Multilingual ALIGN Model - extractive body cue:** A multilingual model ALIGNmling is trained using this data.
- **p. 6 / 5.2. Zero-shot Visual Classification - extractive body cue:** In both stages of training, we use a global batch size of 1024, SGD optimizer with momentum 0.9, and learning rate decayed every 30 epochs ...
- **p. 4 / 5.1. Image-Text Matching & Retrieval - extractive body cue:** We also reduce the initial learning rate to 1e-5 and train for 3K and 6K steps (with linear decay) respectively on Flickr30K and MSCOCO.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** model, consists, pair, image, text, encoders, cosine-similarity, combination, function, EfficientNet, global, pooling, without, training, conv, layer, classification, head, encoder, BERT.
- **Relevant PDF headings:** 6.1. Model Architectures (p. 7); 8. Multilingual ALIGN Model (p. 9).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Input representation | After the sweep, the selected hyperparameters are used to train on the combined training and validation splits of 1000 images for each ... | p. 6 (5.2. Zero-shot Visual Classification), p. 6 (5.2. Zero-shot Visual Classification) |
| Core objective / transformation | So we list the baseline results in (Foret et al., 2021) without using SAM optimization for a fairer comparison. | p. 6 (5.2. Zero-shot Visual Classification), p. 4 (5.1. Image-Text Matching & Retrieval) |
| Downstream transfer boundary | With frozen features, ALIGN slightly outperforms CLIP and achieves SOTA result of 85.5% top-1 accuracy. | p. 6 (5.2. Zero-shot Visual Classification), p. 5 (5.2. Zero-shot Visual Classification) |

## Failure and Ablation Link

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. A summary of our method, ALIGN. Visual and language representations are jointly learned from noisy image alt-text data. The representations can be used ...
- **p. 4 / 5. Experiments and Results - extractive body cue:** The image encoder is trained at resolution of 289 × 289 pixels no matter what EfficientNet variant is used.
- **p. 4 / 5. Experiments and Results - extractive body cue:** Unless in the ablation study, we use the results of ALIGN where the image encoder is EfficientNet-L2 and the text encoder is BERT-Large.
- **p. 5 / 5.2. Zero-shot Visual Classification - extractive body cue:** Top-1 Accuracy of zero-shot transfer of ALIGN to image classification on ImageNet and its variants.
- **p. 6 / 5.2. Zero-shot Visual Classification - extractive body cue:** So we list the baseline results in (Foret et al., 2021) without using SAM optimization for a fairer comparison.
- **p. 6 / 5.2. Zero-shot Visual Classification - extractive body cue:** Our result (average of three runs) is comparable to the SOTA results without tweaking on optimization algorithms.
- **p. 7 / 6.2. Pre-training Datasets - extractive body cue:** Ablation study of different training datasets.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (4.1. Pre-training on Noisy Image-Text Pairs), p. 3 (4.1. Pre-training on Noisy Image-Text Pairs), p. 4 (4.3. Transferring to Visual Classification), p. 9 (8. Multilingual ALIGN Model), p. 4 (4.3. Transferring to Visual Classification), p. 9 (8. Multilingual ALIGN Model), objective p. 3 (4.1. Pre-training on Noisy Image-Text Pairs), p. 3 (4.1. Pre-training on Noisy Image-Text Pairs), p. 9 (8. Multilingual ALIGN Model), p. 9 (8. Multilingual ALIGN Model), temporal p. 1 (1. Introduction), p. 4 (5. Experiments and Results), p. 4 (5. Experiments and Results), p. 6 (5.2. Zero-shot Visual Classification), p. 1 (Abstract), p. 3 (3. A Large-Scale Noisy Image-Text Dataset).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
