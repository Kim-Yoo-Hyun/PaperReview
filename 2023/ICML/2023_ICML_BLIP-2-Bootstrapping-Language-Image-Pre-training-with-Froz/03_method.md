# Method - BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2301.12597; PDF retrieval source: https://arxiv.org/pdf/2301.12597. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3.1. Model Architecture), p. 3 (3.2. Bootstrap Vision-Language Representation), p. 2 (3.1. Model Architecture), p. 2 (3. Method), p. 4 (3.3. Bootstrap Vision-to-Language Generative Learning), p. 4 (3.3. Bootstrap Vision-to-Language Generative Learning)): (Right) The self-attention masking strategy for each objective to control query-text interaction. for visual feature extraction, (2) a text transformer that can function as both a text encoder and a ...

## Method Body Digest

- **p. 3 / 3.1. Model Architecture - extractive body cue:** (Right) The self-attention masking strategy for each objective to control query-text interaction. for visual feature extraction, (2) a text transformer that can function as both ...
- **p. 3 / 3.2. Bootstrap Vision-Language Representation - extractive body cue:** Since the architecture of Q-Former does not allow direct interactions between the frozen image encoder and the text tokens, the information required for generating the ...
- **p. 2 / 3.1. Model Architecture - extractive body cue:** As shown in Figure 2, Q-Former consists of two transformer submodules that share the same self-attention layers: (1) an image transformer that interacts with the ...
- **p. 2 / 3. Method - extractive body cue:** This section first introduces the model architecture of Q-Former, and then delineates the two-stage pre-training procedures.
- **p. 4 / 3.3. Bootstrap Vision-to-Language Generative Learning - extractive body cue:** For encoder-decoder-based LLMs, we pre-train with the prefix language modeling loss, where we split a text into two parts.
- **p. 4 / 3.3. Bootstrap Vision-to-Language Generative Learning - extractive body cue:** For decoderbased LLMs, we pre-train with the language modeling loss, where the frozen LLM is tasked to generate the text conditioned on the visual representation ...
- **p. 5 / 3.4. Model Pre-training - extractive body cue:** BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models The audi e-tron quattro concept is a plug-in hybrid electric sports car that ...
- **p. 3 / 3.2. Bootstrap Vision-Language Representation - extractive body cue:** Inspired by BLIP (Li et al., 2022), we jointly optimize three pre-training objectives that share the same input format and model parameters.

## Design Rationale

- **p. 1 / 1. Introduction - extractive body cue:** To achieve effective vision-language alignment with frozen unimodal models, we propose a Querying Transformer (QFormer) pre-trained with a new two-stage pre-training strategy.
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we propose a generic and Querying Transformer Q-Former Large Language Model (LLM) Queries Text Image Encoder Bootstrapping Pre-trained Image Models Bootstrapping Pre-trained ...
- **p. 2 / 3.1. Model Architecture - extractive body cue:** We propose Q-Former as the trainable module to bridge the gap between a frozen image encoder and a frozen LLM.

## Source Evidence Cues

- **p. 3 / 3.1. Model Architecture - extractive body cue:** (Right) The self-attention masking strategy for each objective to control query-text interaction. for visual feature extraction, (2) a text transformer that can function as both ...
- **p. 3 / 3.2. Bootstrap Vision-Language Representation - extractive body cue:** Since the architecture of Q-Former does not allow direct interactions between the frozen image encoder and the text tokens, the information required for generating the ...
- **p. 2 / 3.1. Model Architecture - extractive body cue:** As shown in Figure 2, Q-Former consists of two transformer submodules that share the same self-attention layers: (1) an image transformer that interacts with the ...
- **p. 2 / 3. Method - extractive body cue:** This section first introduces the model architecture of Q-Former, and then delineates the two-stage pre-training procedures.
- **p. 4 / 3.3. Bootstrap Vision-to-Language Generative Learning - extractive body cue:** For encoder-decoder-based LLMs, we pre-train with the prefix language modeling loss, where we split a text into two parts.
- **p. 4 / 3.3. Bootstrap Vision-to-Language Generative Learning - extractive body cue:** For decoderbased LLMs, we pre-train with the language modeling loss, where the frozen LLM is tasked to generate the text conditioned on the visual representation ...
- **p. 5 / 3.4. Model Pre-training - extractive body cue:** BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models The audi e-tron quattro concept is a plug-in hybrid electric sports car that ...
- **Detected method headings:** 3. Method (p. 2); 3.1. Model Architecture (p. 2); 3.4. Model Pre-training (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Input representation | source-defined input을 learnable representation으로 바꾼다 | paper-specific image/text/sequence input | encoder, tokenization, normalization 또는 feature extraction을 수행 | latent feature/state | (Right) The self-attention masking strategy for each objective to control query-text interaction. for visual feature extraction, (2) a text transformer that can ... | p. 3 (3.1. Model Architecture), p. 3 (3.2. Bootstrap Vision-Language Representation) |
| Core objective / transformation | source task의 prediction·generation 목표를 최적화한다 | representation, target/condition | paper-specific model, loss, decoder 또는 generative process를 적용 | prediction/embedding/sample | Since the architecture of Q-Former does not allow direct interactions between the frozen image encoder and the text tokens, the information required ... | p. 3 (3.2. Bootstrap Vision-Language Representation), p. 2 (3.1. Model Architecture) |
| Downstream transfer boundary | 결과를 후속 task 또는 embodied system에 전달한다 | output와 query/task context | task head, retrieval, grounding 또는 adapter를 적용 | task cue/representation | As shown in Figure 2, Q-Former consists of two transformer submodules that share the same self-attention layers: (1) an image transformer that ... | p. 2 (3.1. Model Architecture), p. 2 (3. Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.2. Bootstrap Vision-Language Representation - extractive body cue:** Inspired by BLIP (Li et al., 2022), we jointly optimize three pre-training objectives that share the same input format and model parameters.
- **p. 3 / 3.1. Model Architecture - extractive body cue:** We jointly optimize three objectives which enforce the queries (a set of learnable embeddings) to extract visual representation most relevant to the text.
- **p. 4 / 3.3. Bootstrap Vision-to-Language Generative Learning - extractive body cue:** For encoder-decoder-based LLMs, we pre-train with the prefix language modeling loss, where we split a text into two parts.
- **p. 4 / 3.3. Bootstrap Vision-to-Language Generative Learning - extractive body cue:** For decoderbased LLMs, we pre-train with the language modeling loss, where the frozen LLM is tasked to generate the text conditioned on the visual representation ...
- **p. 5 / 3.4. Model Pre-training - extractive body cue:** Explain the advantages of this product.
- **Formal bridge:** source-defined input o -> prediction/embedding/sample ŷ -> paper-specific objective -> source task metric; robot link not established.
- **Equation/algorithm anchors:** p. 3 (3.1. Model Architecture), p. 3 (3.2. Bootstrap Vision-Language Representation), p. 4 (3.3. Bootstrap Vision-to-Language Generative Learning), p. 4 (3.3. Bootstrap Vision-to-Language Generative Learning).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | extracts, fixed, number, output, features, image, encoder, independent, input, resolution, fully-connected, layer, adapts, dimension | 논문이 명시한 observation과 task input | body cue; exact tensor/frame verify |
| State/latent | extracts, fixed, number, output, features, image, encoder, independent, input, resolution | task state 또는 decision variable | body cue; notation verify |
| Action/output | achieve, effective, vision-language, alignment, frozen, unimodal, models, Querying, Transformer, QFormer | paper-specific output/action | body cue; unit/decoder verify |
| Objective/constraint | Inspired, BLIP, jointly, optimize, three, pre-training, objectives, share, same, input | paper-specific objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 3.1. Model Architecture - extractive body cue:** It extracts a fixed number of output features from the image encoder, independent of input image resolution.
- **p. 4 / 3.2. Bootstrap Vision-Language Representation - extractive body cue:** The fully-connected layer adapts from the output dimension of the Q-Former to the input dimension of the chosen LLM.
- **p. 4 / 3.2. Bootstrap Vision-Language Representation - extractive body cue:** OPT) Image Encoder Input Image Learned Queries a cat Suffix Text … Q-Former … Fully Connected … LLM Encoder Bootstrapping from an Encoder-Decoder-based Large Language ...
- **p. 2 / 1. Introduction - extractive body cue:** BLIP-2 achieves state-of-the-art performance on various vision-language tasks including visual question answering, image captioning, and image-text retrieval. • Powered by LLMs (e.g.
- **p. 3 / 3.1. Model Architecture - extractive body cue:** We create a set number of learnable query embeddings as input to the image transformer.
- **p. 3 / 3.2. Bootstrap Vision-Language Representation - extractive body cue:** Image-grounded Text Generation (ITG) loss trains the Q-Former to generate texts, given input images as the condition.
- **p. 1 / 1. Introduction - extractive body cue:** However, most state-of-the-art vision-language models incur a high computation cost during pre-training, due to end-to-end training using large-scale models and datasets.
- **Normalized interface:** observation=논문이 명시한 observation과 task input; state=task state 또는 decision variable; output/action=paper-specific output/action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | We pre-train for 250k steps in the first stage and 80k steps in the second stage. | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | We use images of size 224×224, augmented with random resized cropping and horizontal flipping. | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | Tell me something about the history of this place. | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | We use images of size 224×224, augmented with random resized cropping and horizontal flipping. | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 3. Method - extractive body cue:** This section first introduces the model architecture of Q-Former, and then delineates the two-stage pre-training procedures.
- **p. 4 / 3.3. Bootstrap Vision-to-Language Generative Learning - extractive body cue:** For encoder-decoder-based LLMs, we pre-train with the prefix language modeling loss, where we split a text into two parts.
- **p. 4 / 3.3. Bootstrap Vision-to-Language Generative Learning - extractive body cue:** For decoderbased LLMs, we pre-train with the language modeling loss, where the frozen LLM is tasked to generate the text conditioned on the visual representation ...
- **p. 5 / 3.4. Model Pre-training - extractive body cue:** BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models The audi e-tron quattro concept is a plug-in hybrid electric sports car that ...
- **p. 5 / 3.4. Model Pre-training - extractive body cue:** BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models The audi e-tron quattro concept is a plug-in hybrid electric sports car that ...
- **p. 7 / 4.1. Instructed Zero-shot Image-to-Text Generation - extractive body cue:** BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models Models #Trainable Params NoCaps Zero-shot (validation set) COCO Fine-tuned in-domain near-domain out-domain overall ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Right, self-attention, masking, strategy, objective, control, query-text, interaction, visual, feature, extraction, text, transformer, function, encoder, decoder, Since, architecture, Q-Former, does.
- **Relevant PDF headings:** 3. Method (p. 2); 3.1. Model Architecture (p. 2); 3.4. Model Pre-training (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Input representation | On the OK-VQA (Marino et al., 2019) dataset, BLIP-2 comes secondary to Flamingo80B. | p. 6 (4.1. Instructed Zero-shot Image-to-Text Generation), p. 6 (4.1. Instructed Zero-shot Image-to-Text Generation) |
| Core objective / transformation | Compared to previous state-of-the-art models, BLIP-2 achieves improved performance while requiring substantially fewer number of trainable parameters during vision-language pre-training. | p. 6 (4. Experiment), p. 6 (4.1. Instructed Zero-shot Image-to-Text Generation) |
| Downstream transfer boundary | Compared to previous state-of-the-art models, BLIP-2 achieves improved performance while requiring substantially fewer number of trainable parameters during vision-language pre-training. | p. 6 (4. Experiment), p. 6 (4.1. Instructed Zero-shot Image-to-Text Generation) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Effect of vision-language representation learning on vision-to-language generative learning. Without representation learning, the Q-Former fails the bridge the modality gap, leading to significantly ...
- **p. 7 / 4.1. Instructed Zero-shot Image-to-Text Generation - extractive body cue:** BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models Models #Trainable Params NoCaps Zero-shot (validation set) COCO Fine-tuned in-domain near-domain out-domain overall ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 8. Hyperparameters for fine-tuning BLIP-2 with ViT-g on VQA. Image Encoder ViT-L/14 ViT-g/14 Fine-tuning epochs 5 Warmup steps 1000
- **p. 12 / Figure/Table caption - extractive body cue:** Table 9. Hyperparameters for fine-tuning BLIP-2 on COCO image-text retrieval. albert einstein - the world is a book, and those who do not travel read ...
- **p. 8 / 5. Limitation - extractive body cue:** The LLMs cannot learn from it the correlation among multiple image-text pairs in a single sequence.
- **p. 8 / 5. Limitation - extractive body cue:** We aim to create a similar dataset in future work.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Effect of vision-language representation learning on vision-to-language generative learning. Without representation learning, the Q-Former fails the bridge the modality gap, leading to significantly ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3.1. Model Architecture), p. 3 (3.2. Bootstrap Vision-Language Representation), p. 2 (3.1. Model Architecture), p. 2 (3. Method), p. 4 (3.3. Bootstrap Vision-to-Language Generative Learning), p. 4 (3.3. Bootstrap Vision-to-Language Generative Learning), objective p. 3 (3.2. Bootstrap Vision-Language Representation), p. 3 (3.1. Model Architecture), p. 4 (3.3. Bootstrap Vision-to-Language Generative Learning), p. 4 (3.3. Bootstrap Vision-to-Language Generative Learning), p. 5 (3.4. Model Pre-training), temporal p. 4 (3.4. Model Pre-training), p. 4 (3.4. Model Pre-training), p. 5 (3.4. Model Pre-training), p. 2 (1. Introduction), p. 8 (6. Conclusion), p. 8 (5. Limitation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
