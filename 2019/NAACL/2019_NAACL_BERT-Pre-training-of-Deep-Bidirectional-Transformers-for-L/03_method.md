# Method - BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1810.04805; PDF retrieval source: https://arxiv.org/pdf/1810.04805. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (C T1), p. 1 (1 Introduction), p. 3 (C T1)): We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers.

## Method Body Digest

- **p. 1 / Abstract - extractive body cue:** We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers.
- **p. 2 / 1 Introduction - extractive body cue:** BERT is the first finetuning based representation model that achieves state-of-the-art performance on a large suite of sentence-level and token-level tasks, outperforming many task-specific architectures. ...
- **p. 2 / 1 Introduction - extractive body cue:** Unlike left-toright language model pre-training, the MLM objective enables the representation to fuse the left and the right context, which allows us to pretrain a ...
- **p. 5 / C T1 - extractive body cue:** 3.2 Fine-tuning BERT Fine-tuning is straightforward since the selfattention mechanism in the Transformer allows BERT to model many downstream taskswhether they involve single text or ...
- **p. 1 / 1 Introduction - extractive body cue:** The two approaches share the same objective function during pre-training, where they use unidirectional language models to learn general language representations.
- **p. 3 / C T1 - extractive body cue:** Model Architecture BERT's model architecture is a multi-layer bidirectional Transformer encoder based on the original implementation described in Vaswani et al.
- **p. 3 / C T1 - extractive body cue:** [CLS] is a special symbol added in front of every input example, and [SEP] is a special separator token (e.g. separating questions/answers). ing and auto-encoder ...
- **p. 1 / 1 Introduction - extractive body cue:** BERT alleviates the previously mentioned unidirectionality constraint by using a "masked language model" (MLM) pre-training objective, inspired by the Cloze task (Taylor, 1953).

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** Unlike left-toright language model pre-training, the MLM objective enables the representation to fuse the left and the right context, which allows us to pretrain a ...
- **p. 2 / 1 Introduction - extractive body cue:** The contributions of our paper are as follows: • We demonstrate the importance of bidirectional pre-training for language representations.
- **p. 1 / Abstract - extractive body cue:** We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers.

## Source Evidence Cues

- **p. 1 / Abstract - extractive body cue:** We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers.
- **p. 2 / 1 Introduction - extractive body cue:** BERT is the first finetuning based representation model that achieves state-of-the-art performance on a large suite of sentence-level and token-level tasks, outperforming many task-specific architectures. ...
- **p. 2 / 1 Introduction - extractive body cue:** Unlike left-toright language model pre-training, the MLM objective enables the representation to fuse the left and the right context, which allows us to pretrain a ...
- **p. 5 / C T1 - extractive body cue:** 3.2 Fine-tuning BERT Fine-tuning is straightforward since the selfattention mechanism in the Transformer allows BERT to model many downstream taskswhether they involve single text or ...
- **p. 1 / 1 Introduction - extractive body cue:** The two approaches share the same objective function during pre-training, where they use unidirectional language models to learn general language representations.
- **p. 3 / C T1 - extractive body cue:** Model Architecture BERT's model architecture is a multi-layer bidirectional Transformer encoder based on the original implementation described in Vaswani et al.
- **p. 3 / C T1 - extractive body cue:** [CLS] is a special symbol added in front of every input example, and [SEP] is a special separator token (e.g. separating questions/answers). ing and auto-encoder ...
- **Detected method headings:** 0.3 F1 behind fine-tuning the entire model. This (p. 9)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Input representation | source-defined input을 learnable representation으로 바꾼다 | paper-specific image/text/sequence input | encoder, tokenization, normalization 또는 feature extraction을 수행 | latent feature/state | We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers. | p. 1 (Abstract), p. 2 (1 Introduction) |
| Core objective / transformation | source task의 prediction·generation 목표를 최적화한다 | representation, target/condition | paper-specific model, loss, decoder 또는 generative process를 적용 | prediction/embedding/sample | BERT is the first finetuning based representation model that achieves state-of-the-art performance on a large suite of sentence-level and token-level tasks, outperforming ... | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Downstream transfer boundary | 결과를 후속 task 또는 embodied system에 전달한다 | output와 query/task context | task head, retrieval, grounding 또는 adapter를 적용 | task cue/representation | Unlike left-toright language model pre-training, the MLM objective enables the representation to fuse the left and the right context, which allows us ... | p. 2 (1 Introduction), p. 5 (C T1) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / 1 Introduction - extractive body cue:** BERT alleviates the previously mentioned unidirectionality constraint by using a "masked language model" (MLM) pre-training objective, inspired by the Cloze task (Taylor, 1953).
- **p. 4 / C T1 - extractive body cue:** Then, Ti will be used to predict the original token with cross entropy loss.
- **p. 1 / 1 Introduction - extractive body cue:** The two approaches share the same objective function during pre-training, where they use unidirectional language models to learn general language representations.
- **p. 2 / 1 Introduction - extractive body cue:** Unlike left-toright language model pre-training, the MLM objective enables the representation to fuse the left and the right context, which allows us to pretrain a ...
- **p. 3 / C T1 - extractive body cue:** [CLS] is a special symbol added in front of every input example, and [SEP] is a special separator token (e.g. separating questions/answers). ing and auto-encoder ...
- **p. 5 / C T1 - extractive body cue:** The NSP task is closely related to representationlearning objectives used in Jernite et al.
- **Formal bridge:** source-defined input o -> prediction/embedding/sample ŷ -> paper-specific objective -> source task metric; robot link not established.
- **Equation/algorithm anchors:** p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (C T1), p. 4 (C T1), p. 5 (C T1).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | result, pre-trained, BERT, model, finetuned, just, additional, output, layer, create, state-of-the-art, models, wide, range | 논문이 명시한 observation과 task input | body cue; exact tensor/frame verify |
| State/latent | result, pre-trained, BERT, model, finetuned, just, additional, output, layer, create | task state 또는 decision variable | body cue; notation verify |
| Action/output | Unlike, left-toright, language, model, pre-training, MLM, objective, enables, representation, fuse | paper-specific output/action | body cue; unit/decoder verify |
| Objective/constraint | BERT, alleviates, previously, mentioned, unidirectionality, constraint, masked, language, model, MLM | paper-specific objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Abstract - extractive body cue:** As a result, the pre-trained BERT model can be finetuned with just one additional output layer to create state-of-the-art models for a wide range of ...
- **p. 4 / C T1 - extractive body cue:** Input/Output Representations To make BERT handle a variety of down-stream tasks, our input representation is able to unambiguously represent both a single sentence and a ...
- **p. 5 / C T1 - extractive body cue:** For each task, we simply plug in the taskspecific inputs and outputs into BERT and finetune all the parameters end-to-end.
- **p. 5 / C T1 - extractive body cue:** 3.2 Fine-tuning BERT Fine-tuning is straightforward since the selfattention mechanism in the Transformer allows BERT to model many downstream taskswhether they involve single text or ...
- **p. 1 / 1 Introduction - extractive body cue:** The masked language model randomly masks some of the tokens from the input, and the objective is to predict the original vocabulary id of the ...
- **p. 2 / 1 Introduction - extractive body cue:** BERT is the first finetuning based representation model that achieves state-of-the-art performance on a large suite of sentence-level and token-level tasks, outperforming many task-specific architectures. ...
- **p. 3 / C T1 - extractive body cue:** Apart from output layers, the same architectures are used in both pre-training and fine-tuning.
- **Normalized interface:** observation=논문이 명시한 observation과 task input; state=task state 또는 decision variable; output/action=paper-specific output/action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | To fine-tune on GLUE, we represent the input sequence (for single sentence or sentence pairs) as described in Section 3, and use ... | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | As shown in Figure 1, in the question answering task, we represent the input question and passage as a single packed sequence, ... | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | There is a long history of pre-training general language representations, and we briefly review the most widely-used approaches in this section. | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | We fine-tune for 3 epochs with a learning rate of 5e-5 and a batch size of 32. | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 Introduction - extractive body cue:** Unlike left-toright language model pre-training, the MLM objective enables the representation to fuse the left and the right context, which allows us to pretrain a ...
- **p. 5 / C T1 - extractive body cue:** 3.2 Fine-tuning BERT Fine-tuning is straightforward since the selfattention mechanism in the Transformer allows BERT to model many downstream taskswhether they involve single text or ...
- **p. 1 / 1 Introduction - extractive body cue:** The two approaches share the same objective function during pre-training, where they use unidirectional language models to learn general language representations.
- **p. 3 / C T1 - extractive body cue:** [CLS] is a special symbol added in front of every input example, and [SEP] is a special separator token (e.g. separating questions/answers). ing and auto-encoder ...
- **p. 6 / 4 Experiments - extractive body cue:** We fine-tune for 3 epochs with a learning rate of 5e-5 and a batch size of 32.
- **p. 6 / 4 Experiments - extractive body cue:** We use a batch size of 32 and fine-tune for 3 epochs over the data for all GLUE tasks.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** introduce, language, representation, model, called, BERT, stands, Bidirectional, Encoder, Representations, Transformers, first, finetuning, achieves, state-of-the-art, performance, large, suite, sentence-level, token-level.
- **Relevant PDF headings:** 0.3 F1 behind fine-tuning the entire model. This (p. 9).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Input representation | 4.1 GLUE The General Language Understanding Evaluation (GLUE) benchmark (Wang et al., 2018a) is a collection of diverse natural language understanding tasks. | p. 5 (4 Experiments), p. 8 (4 Experiments) |
| Core objective / transformation | BERTLARGE outperforms the authors' baseline ESIM+ELMo system by +27.1% and OpenAI GPT by 8.3%. | p. 7 (4 Experiments), p. 6 (4 Experiments) |
| Downstream transfer boundary | Both BERTBASE and BERTLARGE outperform all systems on all tasks by a substantial margin, obtaining 4.5% and 7.0% respective average accuracy improvement ... | p. 6 (4 Experiments), p. 8 (4 Experiments) |

## Failure and Ablation Link

- **p. 8 / 4 Experiments - extractive body cue:** 5.1 Effect of Pre-training Tasks We demonstrate the importance of the deep bidirectionality of BERT by evaluating two pretraining objectives using exactly the same pretraining ...
- **p. 8 / 4 Experiments - extractive body cue:** Dev Set Tasks MNLI-m QNLI MRPC SST-2 SQuAD (Acc) (Acc) (Acc) (Acc) (F1) BERTBASE 84.4 88.4 86.7 92.7 88.5 No NSP 83.9 84.9 86.5 92.6 ...
- **p. 9 / 4 Experiments - extractive body cue:** To ablate the fine-tuning approach, we apply the feature-based approach by extracting the activations from one or more layers without fine-tuning any parameters of BERT.
- **p. 6 / 4 Experiments - extractive body cue:** The effect of model size is explored more thoroughly in Section 5.2.
- **p. 6 / 4 Experiments - extractive body cue:** Without TriviaQA fine11QANet is described in Yu et al.
- **p. 7 / 4 Experiments - extractive body cue:** 5 Ablation Studies In this section, we perform ablation experiments over a number of facets of BERT in order to better understand their relative importance.
- **p. 9 / 4 Experiments - extractive body cue:** Following standard practice, we formulate this as a tagging task but do not use a CRF Hyperparams Dev Set Accuracy #L #H #A LM (ppl) ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (C T1), p. 1 (1 Introduction), p. 3 (C T1), objective p. 1 (1 Introduction), p. 4 (C T1), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (C T1), p. 5 (C T1), temporal p. 5 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 3 (C T1), p. 2 (2 Related Work), p. 4 (C T1).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
