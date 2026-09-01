# Method - Visual Instruction Tuning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2304.08485; PDF retrieval source: https://arxiv.org/pdf/2304.08485. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 9 (Method), p. 9 (Method)): Visual features Before Last Best variant 90.92 89.96 (-0.96) Predict answer first - 89.77 (-1.15) Training from scratch 85.81 (-5.11) - 7B model size 89.84 (-1.08) - Table 8: Design ...

## Method Body Digest

- **p. 9 / Method - extractive PDF cue:** Visual features Before Last Best variant 90.92 89.96 (-0.96) Predict answer first - 89.77 (-1.15) Training from scratch 85.81 (-5.11) - 7B model size 89.84 ...
- **p. 9 / Method - extractive PDF cue:** To decide the order between the answer and reasoning process in the model prediction, we run both variants and observe that answer-first reports the best ...
- **p. 2 / 1 Introduction - extractive PDF cue:** In this paper, we present visual instruction-tuning, the first attempt to extend instruction-tuning to the language-image multimodal space, to pave the way towards building a ...
- **p. 1 / 1 Introduction - extractive PDF cue:** One of the core aspirations in artificial intelligence is to develop a general-purpose assistant that can effectively follow multi-modal vision-and-language instructions, aligned with human intent ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Large language models (LLM), on the other hand, have shown that language can play a wider role: a universal interface for a general-purpose assistant, where ...
- **p. 2 / 1 Introduction - extractive PDF cue:** One key challenge is the lack of vision-language instruction-following data.
- **p. 9 / Method - extractive PDF cue:** Question categories: NAT = natural science, SOC = social science, LAN = language science, TXT = text context, IMG = image context, NO = no ...
- **p. 9 / Method - extractive PDF cue:** We hypothesize that this is because CLIP's last layer features may focus more on global and abstract image properties compared to the layer before it, ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** We present LLaVA-Bench with two challenging benchmarks, with a diverse selection of paired images, instructions and detailed annotations. • Open-source.
- **p. 2 / 1 Introduction - extractive PDF cue:** We present a data reformation perspective and pipeline to convert image-text pairs into an appropriate instruction-following format, using ChatGPT/GPT-4. • Large multimodal models.
- **p. 1 / 1 Introduction - extractive PDF cue:** For example, the recent success of ChatGPT [35] and GPT-4 [36] have demonstrated the power of aligned LLMs in following human instructions, and have stimulated ...

## Source Evidence Cues

- **p. 9 / Method - extractive PDF cue:** Visual features Before Last Best variant 90.92 89.96 (-0.96) Predict answer first - 89.77 (-1.15) Training from scratch 85.81 (-5.11) - 7B model size 89.84 ...
- **p. 9 / Method - extractive PDF cue:** To decide the order between the answer and reasoning process in the model prediction, we run both variants and observe that answer-first reports the best ...
- **Detected method headings:** Method (p. 9)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Input representation | source-defined input을 learnable representation으로 바꾼다 | paper-specific image/text/sequence input | encoder, tokenization, normalization 또는 feature extraction을 수행 | latent feature/state | Visual features Before Last Best variant 90.92 89.96 (-0.96) Predict answer first - 89.77 (-1.15) Training from scratch 85.81 (-5.11) - 7B ... | p. 9 (Method), p. 9 (Method) |
| Core objective / transformation | source task의 prediction·generation 목표를 최적화한다 | representation, target/condition | paper-specific model, loss, decoder 또는 generative process를 적용 | prediction/embedding/sample | To decide the order between the answer and reasoning process in the model prediction, we run both variants and observe that answer-first ... | p. 9 (Method) |
| Downstream transfer boundary | 결과를 후속 task 또는 embodied system에 전달한다 | output와 query/task context | task head, retrieval, grounding 또는 adapter를 적용 | task cue/representation | Visual features Before Last Best variant 90.92 89.96 (-0.96) Predict answer first - 89.77 (-1.15) Training from scratch 85.81 (-5.11) - 7B ... | p. 9 (Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** source-defined input o -> prediction/embedding/sample ŷ -> paper-specific objective -> source task metric; robot link not established.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | present, visual, instruction-tuning, first, attempt, extend, language-image, multimodal, space, pave, towards, building, general-purpose, assistant | 논문이 명시한 observation과 task input | body cue; exact tensor/frame verify |
| State/latent | present, visual, instruction-tuning, first, attempt, extend, language-image, multimodal, space, pave | task state 또는 decision variable | body cue; notation verify |
| Action/output | present, LLaVA-Bench, challenging, benchmarks, diverse, selection, paired, images, instructions, detailed | paper-specific output/action | body cue; unit/decoder verify |
| Objective/constraint | not recovered | paper-specific objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive PDF cue:** In this paper, we present visual instruction-tuning, the first attempt to extend instruction-tuning to the language-image multimodal space, to pave the way towards building a ...
- **p. 1 / 1 Introduction - extractive PDF cue:** One of the core aspirations in artificial intelligence is to develop a general-purpose assistant that can effectively follow multi-modal vision-and-language instructions, aligned with human intent ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Large language models (LLM), on the other hand, have shown that language can play a wider role: a universal interface for a general-purpose assistant, where ...
- **p. 2 / 1 Introduction - extractive PDF cue:** One key challenge is the lack of vision-language instruction-following data.
- **p. 9 / Method - extractive PDF cue:** Question categories: NAT = natural science, SOC = social science, LAN = language science, TXT = text context, IMG = image context, NO = no ...
- **p. 9 / Method - extractive PDF cue:** We hypothesize that this is because CLIP's last layer features may focus more on global and abstract image properties compared to the layer before it, ...
- **Normalized interface:** observation=논문이 명시한 observation과 task input; state=task state 또는 decision variable; output/action=paper-specific output/action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | [Start a new conversation, and clear the history] User What's happening in the scene? | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | LLaVA performs significantly better than others. † For a given set of LLaVA decoding sequences, we evaluate by querying GPT-4 three times; ... | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | [Start a new conversation, and clear the history] User What's happening in the scene? | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | We pre-train our model on the filtered CC-595K subset for 1 epoch with a learning rate of 2e-3 and a batch size ... | hardware, batch and throughput |

## Training vs Inference

- **p. 9 / Method - extractive PDF cue:** Visual features Before Last Best variant 90.92 89.96 (-0.96) Predict answer first - 89.77 (-1.15) Training from scratch 85.81 (-5.11) - 7B model size 89.84 ...
- **p. 9 / Method - extractive PDF cue:** To decide the order between the answer and reasoning process in the model prediction, we run both variants and observe that answer-first reports the best ...
- **p. 5 / 5 Experiments - extractive PDF cue:** We pre-train our model on the filtered CC-595K subset for 1 epoch with a learning rate of 2e-3 and a batch size of 128, and ...
- **p. 5 / 5 Experiments - extractive PDF cue:** We train all models with 8× A100s, following Vicuna's hyperparameters [9].
- **p. 8 / 5 Experiments - extractive PDF cue:** For LLaVA, we use the visual features before the last layer, ask the model to first predict reasons and then the answer, and train it ...
- **p. 9 / Method - extractive PDF cue:** To decide the order between the answer and reasoning process in the model prediction, we run both variants and observe that answer-first reports the best ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Visual, features, Before, Last, Best, variant, Predict, answer, first, Training, scratch, model, size, Table, Design, choice, ablations, decide, order, between.
- **Relevant PDF headings:** Method (p. 9).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Input representation | The benchmark dataset is split into training, validation, and test splits with 12726, 4241, and 4241 examples, respectively. | p. 8 (5 Experiments), p. 7 (5 Experiments) |
| Core objective / transformation | Compared to BLIP-2 [28] and OpenFlamingo [5], LLaVA accurately follows the user's instructions, instead of simply describing the scene. | p. 6 (5 Experiments), p. 7 (5 Experiments) |
| Downstream transfer boundary | Surprisingly, this scheme is able to provide consistent improvement over all question classes, and achieves a new SoTA accuracy of 92.53%. | p. 8 (5 Experiments), p. 7 (5 Experiments) |

## Failure and Ablation Link

- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 8: Design choice ablations (%). The differ- ence with the best variant is reported in red text. Ablations. We ablate several design choices on ...
- **p. 7 / 5 Experiments - extractive PDF cue:** Conversation Detail description Complex reasoning All Full data 83.1 75.3 96.5 85.1 Detail + Complex 81.5 (-1.6) 73.3 (-2.0) 90.8 (-5.7) 81.9 (-3.2) Conv + ...
- **p. 8 / 5 Experiments - extractive PDF cue:** We consider two representative methods, including GPT-3.5 model (text-davinci-002) with and without chainof-thought (CoT), LLaMA-Adapter [59], as well as multimodal chain-of-thought (MM-CoT) [61], which is ...
- **p. 17 / Figure/Table caption - extractive PDF cue:** Figure 3: LLaVA is capable of recognizing the visual content following the user's intent, without directly prompting for visual recognition. It also provides a detailed ...
- **p. 5 / 5 Experiments - extractive PDF cue:** We pre-train our model on the filtered CC-595K subset for 1 epoch with a learning rate of 2e-3 and a batch size of 128, and ...
- **p. 18 / Figure/Table caption - extractive PDF cue:** Figure 4: LLaVA relates the movie scenes to the textual knowledge from the pretrained LLM. The painting depicts a dog in a humorous situation, where ...
- **p. 7 / 5 Experiments - extractive PDF cue:** We also observed an interesting failure of LLaVA, as it responds with yes when asked if strawberry-flavored yogurt is present, even though the fridge contains ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 9 (Method), p. 9 (Method), objective 본문 anchor 없음, temporal p. 6 (5 Experiments), p. 7 (5 Experiments), p. 2 (2 Related Work), p. 3 (2 Related Work), p. 4 (2 Related Work), p. 4 (2 Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
