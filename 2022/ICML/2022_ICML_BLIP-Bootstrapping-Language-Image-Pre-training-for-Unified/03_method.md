# Method - BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2201.12086; PDF retrieval source: https://arxiv.org/pdf/2201.12086. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3. Method), p. 3 (3.1. Model Architecture), p. 4 (3.3. CapFilt), p. 4 (3.3. CapFilt)): This section first introduces our new model architecture MED and its pre-training objectives, and then delineates CapFilt for dataset bootstrapping.

## Method Body Digest

- **p. 3 / 3. Method - extractive body cue:** This section first introduces our new model architecture MED and its pre-training objectives, and then delineates CapFilt for dataset bootstrapping.
- **p. 3 / 3.1. Model Architecture - extractive body cue:** In order to pre-train a unified model with both understanding and generation capabilities, we propose multimodal mixture of encoder-decoder (MED), a multi-task model which can ...
- **p. 4 / 3.3. CapFilt - extractive body cue:** Finally, we combine the filtered image-text pairs with the human-annotated pairs to form a new dataset, which we use to pre-train a new model.
- **p. 4 / 3.3. CapFilt - extractive body cue:** The filter is an image-grounded text encoder.
- **p. 3 / 3.2. Pre-training Objectives - extractive body cue:** It optimizes a cross entropy loss which trains the model to maximize the likelihood of the text in an autoregressive manner.
- **p. 3 / 3.2. Pre-training Objectives - extractive body cue:** We jointly optimize three objectives during pre-training, with two understanding-based objectives and one generationbased objective.
- **p. 4 / 3.3. CapFilt - extractive body cue:** It is finetuned with the LM objective to decode texts given images.
- **p. 4 / 3.3. CapFilt - extractive body cue:** It is finetuned with the ITC and ITM objectives to learn whether a text matches an image.

## Design Rationale

- **p. 1 / 1. Introduction - extractive body cue:** To this end, we propose BLIP: Bootstrapping LanguageImage Pre-training for unified vision-language understanding and generation.
- **p. 2 / 1. Introduction - extractive body cue:** We propose multimodal mixture of encoder-decoder, a unified vision-language model which can operate in one of the three functionalities: (1) Unimodal encoder is trained with ...
- **p. 3 / 3. Method - extractive body cue:** We propose BLIP, a unified VLP framework to learn from noisy image-text pairs.

## Source Evidence Cues

- **p. 3 / 3. Method - extractive body cue:** This section first introduces our new model architecture MED and its pre-training objectives, and then delineates CapFilt for dataset bootstrapping.
- **p. 3 / 3.1. Model Architecture - extractive body cue:** In order to pre-train a unified model with both understanding and generation capabilities, we propose multimodal mixture of encoder-decoder (MED), a multi-task model which can ...
- **p. 4 / 3.3. CapFilt - extractive body cue:** Finally, we combine the filtered image-text pairs with the human-annotated pairs to form a new dataset, which we use to pre-train a new model.
- **p. 4 / 3.3. CapFilt - extractive body cue:** The filter is an image-grounded text encoder.
- **Detected method headings:** 3. Method (p. 3); 3.1. Model Architecture (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Input representation | source-defined input을 learnable representation으로 바꾼다 | paper-specific image/text/sequence input | encoder, tokenization, normalization 또는 feature extraction을 수행 | latent feature/state | This section first introduces our new model architecture MED and its pre-training objectives, and then delineates CapFilt for dataset bootstrapping. | p. 3 (3. Method), p. 3 (3.1. Model Architecture) |
| Core objective / transformation | source task의 prediction·generation 목표를 최적화한다 | representation, target/condition | paper-specific model, loss, decoder 또는 generative process를 적용 | prediction/embedding/sample | In order to pre-train a unified model with both understanding and generation capabilities, we propose multimodal mixture of encoder-decoder (MED), a multi-task ... | p. 3 (3.1. Model Architecture), p. 4 (3.3. CapFilt) |
| Downstream transfer boundary | 결과를 후속 task 또는 embodied system에 전달한다 | output와 query/task context | task head, retrieval, grounding 또는 adapter를 적용 | task cue/representation | Finally, we combine the filtered image-text pairs with the human-annotated pairs to form a new dataset, which we use to pre-train a ... | p. 4 (3.3. CapFilt), p. 4 (3.3. CapFilt) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.2. Pre-training Objectives - extractive body cue:** It optimizes a cross entropy loss which trains the model to maximize the likelihood of the text in an autoregressive manner.
- **p. 3 / 3.2. Pre-training Objectives - extractive body cue:** We jointly optimize three objectives during pre-training, with two understanding-based objectives and one generationbased objective.
- **p. 4 / 3.3. CapFilt - extractive body cue:** It is finetuned with the LM objective to decode texts given images.
- **p. 4 / 3.3. CapFilt - extractive body cue:** It is finetuned with the ITC and ITM objectives to learn whether a text matches an image.
- **Formal bridge:** source-defined input o -> prediction/embedding/sample ŷ -> paper-specific objective -> source task metric; robot link not established.
- **Equation/algorithm anchors:** p. 3 (3.2. Pre-training Objectives), p. 3 (3.2. Pre-training Objectives), p. 4 (3.3. CapFilt), p. 4 (3.3. CapFilt).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | find, more, diverse, captions, yield, larger, gains, BLIP, achieves, state-of-the-art, performance, wide, range, vision-language | 논문이 명시한 observation과 task input | body cue; exact tensor/frame verify |
| State/latent | find, more, diverse, captions, yield, larger, gains, BLIP, achieves, state-of-the-art | task state 또는 decision variable | body cue; notation verify |
| Action/output | BLIP, Bootstrapping, LanguageImage, Pre-training, unified, vision-language, understanding, generation, multimodal, mixture | paper-specific output/action | body cue; unit/decoder verify |
| Objective/constraint | optimizes, cross, entropy, loss, trains, model, maximize, likelihood, text, autoregressive | paper-specific objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1. Introduction - extractive body cue:** We also find that more diverse captions yield larger gains. • BLIP achieves state-of-the-art performance on a wide range of vision-language tasks, including image-text.
- **p. 2 / 1. Introduction - extractive body cue:** We also achieve state-ofthe-art zero-shot performance when directly transferring our models to two video-language tasks: text-to-video retrieval and videoQA.
- **p. 2 / 1. Introduction - extractive body cue:** (2) Image-grounded text encoder uses additional cross-attention layers to model vision-language interactions, and is trained with a image-text matching (ITM) loss to distinguish between positive ...
- **p. 3 / 3.1. Model Architecture - extractive body cue:** A task-specific [Encode] token is appended to the text, and the output embedding of [Encode] is used as the multimodal representation of the image-text pair.
- **p. 3 / 3.1. Model Architecture - extractive body cue:** We employ a visual transformer (Dosovitskiy et al., 2021) as our image encoder, which divides an input image into patches and encodes them as a ...
- **p. 1 / 1. Introduction - extractive body cue:** (2) Data perspective: most state-of-the-art methods (e.g., CLIP (Radford et al., 2021), ALBEF (Li et al., 2021a), SimVLM (Wang et al., 2021)) pre-train on image-text ...
- **p. 4 / 3.3. CapFilt - extractive body cue:** Specifically, the captioner is an image-grounded text decoder.
- **Normalized interface:** observation=논문이 명시한 observation과 task input; state=task state 또는 decision variable; output/action=paper-specific output/action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | We propose BLIP, a unified VLP framework to learn from noisy image-text pairs. | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | A [Decode] token is used to signal the beginning of a sequence, and an end-of-sequence token is used to signal its end. | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | not recovered | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | To process video input, we uniformly sample n frames per video (n = 8 for retrieval and n = 16 for QA), ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3. Method - extractive body cue:** This section first introduces our new model architecture MED and its pre-training objectives, and then delineates CapFilt for dataset bootstrapping.
- **p. 3 / 3.1. Model Architecture - extractive body cue:** In order to pre-train a unified model with both understanding and generation capabilities, we propose multimodal mixture of encoder-decoder (MED), a multi-task model which can ...
- **p. 4 / 3.3. CapFilt - extractive body cue:** Finally, we combine the filtered image-text pairs with the human-annotated pairs to form a new dataset, which we use to pre-train a new model.
- **p. 4 / 4.1. Pre-training Details - extractive body cue:** We pre-train the model for 20 epochs using a batch size of 2880 (ViT-B) / 2400 (ViT-L).

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** section, first, introduces, model, architecture, MED, pre-training, objectives, then, delineates, CapFilt, dataset, bootstrapping, order, pre-train, unified, understanding, generation, capabilities, multimodal.
- **Relevant PDF headings:** 3. Method (p. 3); 3.1. Model Architecture (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Input representation | In Table 1, we compare models pre-trained on different datasets to demonstrate the efficacy of CapFilt on downstream tasks, including image-text retrieval ... | p. 4 (4.2. Effect of CapFilt), p. 4 (4.1. Pre-training Details) |
| Core objective / transformation | Table 11. Comparisons with state-of-the-art methods for video question answering. We report top-1 test accuracy on two datasets. Despite the domain difference ... | p. 8 (Figure/Table caption), p. 4 (4.2. Effect of CapFilt) |
| Downstream transfer boundary | Table 11. Comparisons with state-of-the-art methods for video question answering. We report top-1 test accuracy on two datasets. Despite the domain difference ... | p. 8 (Figure/Table caption), p. 4 (4.2. Effect of CapFilt) |

## Failure and Ablation Link

- **p. 5 / Figure/Table caption - extractive body cue:** Table 3. Comparison between different parameter sharing strategies for the text encoder and decoder during pre-training. In Figure 4, we show some example captions and ...
- **p. 4 / 4.1. Pre-training Details - extractive body cue:** We explore two variants of ViTs: ViT-B/16 and ViT-L/16.
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. Evaluation of the effect of the captioner (C) and filter (F) for dataset bootstrapping. Downstream tasks include image-text retrieval and image captioning with ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 4. Effect of sharing parameters between the captioner and filter. Models are pre-trained on 14M images.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We use a Captioner (Cap) to generate synthetic captions for web images, and a Filter (Filt) to remove noisy captions. collected from the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Learning framework of BLIP. We introduce a captioner to produce synthetic captions for web images, and a filter to remove noisy image-text pairs. ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Pre-training model architecture and objectives of BLIP (same parameters have the same color). We propose multimodal mixture of encoder-decoder, a unified vision-language model ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3. Method), p. 3 (3.1. Model Architecture), p. 4 (3.3. CapFilt), p. 4 (3.3. CapFilt), objective p. 3 (3.2. Pre-training Objectives), p. 3 (3.2. Pre-training Objectives), p. 4 (3.3. CapFilt), p. 4 (3.3. CapFilt), temporal p. 3 (3. Method), p. 3 (3.1. Model Architecture), p. 8 (5.6. Zero-shot Transfer to Video-Language Tasks), p. 1 (1. Introduction), p. 1 (Abstract), p. 2 (2.1. Vision-language Pre-training).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
