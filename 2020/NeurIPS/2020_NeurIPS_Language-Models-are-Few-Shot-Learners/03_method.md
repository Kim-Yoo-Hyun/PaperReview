# Method - Language Models are Few-Shot Learners

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (75 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2005.14165; PDF retrieval source: https://arxiv.org/pdf/2005.14165. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 8 (2 Approach), p. 9 (2 Approach), p. 6 (2 Approach), p. 43 (B Details of Model Training), p. 43 (B Details of Model Training), p. 8 (2 Approach)): 2.1 Model and Architectures We use the same model and architecture as GPT-2 [RWC+19], including the modified initialization, pre-normalization, and reversible tokenization described therein, with the exception that we use ...

## Method Body Digest

- **p. 8 / 2 Approach - extractive PDF cue:** 2.1 Model and Architectures We use the same model and architecture as GPT-2 [RWC+19], including the modified initialization, pre-normalization, and reversible tokenization described therein, with ...
- **p. 9 / 2 Approach - extractive PDF cue:** To train the larger models without running out of memory, we use a mixture of model parallelism within each matrix multiply and model parallelism across ...
- **p. 6 / 2 Approach - extractive PDF cue:** As indicated by the name, few-shot learning as described here for language models is related to few-shot learning as used in other contexts in ML ...
- **p. 43 / B Details of Model Training - extractive PDF cue:** We also gradually increase the batch size linearly from a small value (32k tokens) to the full value over the first 4-12 billion tokens of ...
- **p. 43 / B Details of Model Training - extractive PDF cue:** To train all versions of GPT-3, we use Adam with β1 = 0.9, β2 = 0.95, and ϵ = 10-8, we clip the global norm ...
- **p. 8 / 2 Approach - extractive PDF cue:** Previous work [KMH+20] suggests that with enough training data, scaling of validation loss should be approximately a smooth power law as a function of size; ...
- **p. 6 / 2 Approach - extractive PDF cue:** As shown in Figure 2.1, for a typical dataset an example has a context and a desired completion (for example an English sentence and the ...
- **p. 43 / B Details of Model Training - extractive PDF cue:** Data are sampled without replacement during training (until an epoch boundary is reached) to minimize overfitting.

## Design Rationale

- **p. 7 / 2 Approach - extractive PDF cue:** The panels above show four methods for performing a task with a language model - fine-tuning is the traditional method, whereas zero-, one-, and few-shot, ...
- **p. 5 / 1 Introduction - extractive PDF cue:** Specifically, we evaluate GPT-3 on over two dozen NLP datasets, as well as several novel tasks designed to test rapid adaptation to tasks unlikely to ...
- **p. 5 / 1 Introduction - extractive PDF cue:** GPT-3 also displays one-shot and few-shot proficiency at tasks designed to test rapid adaption or on-the-fly reasoning, which include unscrambling words, performing arithmetic, and using ...

## Source Evidence Cues

- **p. 8 / 2 Approach - extractive PDF cue:** 2.1 Model and Architectures We use the same model and architecture as GPT-2 [RWC+19], including the modified initialization, pre-normalization, and reversible tokenization described therein, with ...
- **p. 9 / 2 Approach - extractive PDF cue:** To train the larger models without running out of memory, we use a mixture of model parallelism within each matrix multiply and model parallelism across ...
- **p. 6 / 2 Approach - extractive PDF cue:** As indicated by the name, few-shot learning as described here for language models is related to few-shot learning as used in other contexts in ML ...
- **p. 43 / B Details of Model Training - extractive PDF cue:** We also gradually increase the batch size linearly from a small value (32k tokens) to the full value over the first 4-12 billion tokens of ...
- **p. 43 / B Details of Model Training - extractive PDF cue:** To train all versions of GPT-3, we use Adam with β1 = 0.9, β2 = 0.95, and ϵ = 10-8, we clip the global norm ...
- **p. 8 / 2 Approach - extractive PDF cue:** Previous work [KMH+20] suggests that with enough training data, scaling of validation loss should be approximately a smooth power law as a function of size; ...
- **p. 6 / 2 Approach - extractive PDF cue:** As shown in Figure 2.1, for a typical dataset an example has a context and a desired completion (for example an English sentence and the ...
- **Detected method headings:** 2 Approach (p. 2); B Details of Model Training (p. 2); 2 Approach (p. 6); B Details of Model Training (p. 43); Model (p. 47); Model (p. 48)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Input representation | source-defined input을 learnable representation으로 바꾼다 | paper-specific image/text/sequence input | encoder, tokenization, normalization 또는 feature extraction을 수행 | latent feature/state | 2.1 Model and Architectures We use the same model and architecture as GPT-2 [RWC+19], including the modified initialization, pre-normalization, and reversible tokenization ... | p. 8 (2 Approach), p. 9 (2 Approach) |
| Core objective / transformation | source task의 prediction·generation 목표를 최적화한다 | representation, target/condition | paper-specific model, loss, decoder 또는 generative process를 적용 | prediction/embedding/sample | To train the larger models without running out of memory, we use a mixture of model parallelism within each matrix multiply and ... | p. 9 (2 Approach), p. 6 (2 Approach) |
| Downstream transfer boundary | 결과를 후속 task 또는 embodied system에 전달한다 | output와 query/task context | task head, retrieval, grounding 또는 adapter를 적용 | task cue/representation | As indicated by the name, few-shot learning as described here for language models is related to few-shot learning as used in other ... | p. 6 (2 Approach), p. 43 (B Details of Model Training) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 43 / B Details of Model Training - extractive PDF cue:** Data are sampled without replacement during training (until an epoch boundary is reached) to minimize overfitting.
- **p. 43 / B Details of Model Training - extractive PDF cue:** To train all versions of GPT-3, we use Adam with β1 = 0.9, β2 = 0.95, and ϵ = 10-8, we clip the global norm ...
- **p. 8 / 2 Approach - extractive PDF cue:** We partition the model across GPUs along both the depth and width dimension in order to minimize data-transfer between nodes.
- **p. 8 / 2 Approach - extractive PDF cue:** Previous work [KMH+20] suggests that validation loss is not strongly sensitive to these parameters within a reasonably broad range.
- **p. 9 / 2 Approach - extractive PDF cue:** We measure the gradient noise scale during training and use it to guide our choice of batch size [MKAT18].
- **p. 9 / 2 Approach - extractive PDF cue:** Unfortunately, a bug in the filtering caused us to ignore some overlaps, and due to the cost of training it was not feasible to retrain ...
- **Formal bridge:** source-defined input o -> prediction/embedding/sample ŷ -> paper-specific objective -> source task metric; robot link not established.
- **Equation/algorithm anchors:** p. 8 (2 Approach), p. 8 (2 Approach), p. 9 (2 Approach), p. 43 (B Details of Model Training), p. 57 (Model), p. 58 (Model).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Recent, RWC, attempts, what, call, in-context, learning, text, input, pretrained, language, model, form, task | 논문이 명시한 observation과 task input | body cue; exact tensor/frame verify |
| State/latent | Recent, RWC, attempts, what, call, in-context, learning, text, input, pretrained | task state 또는 decision variable | body cue; notation verify |
| Action/output | panels, above, four, methods, performing, task, language, model, fine-tuning, traditional | paper-specific output/action | body cue; unit/decoder verify |
| Objective/constraint | Data, sampled, without, replacement, during, training, until, epoch, boundary, reached | paper-specific objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 1 Introduction - extractive PDF cue:** Recent work [RWC+19] attempts to do this via what we call "in-context learning", using the text input of a pretrained language model as a form ...
- **p. 7 / 2 Approach - extractive PDF cue:** Exact phrasings for all task descriptions, examples and prompts can be found in Appendix G. • Zero-Shot (0S) is the same as one-shot except that ...
- **p. 6 / 2 Approach - extractive PDF cue:** The main disadvantage is that results from this method have so far been much worse than state-of-the-art fine-tuned models.
- **p. 7 / 2 Approach - extractive PDF cue:** We especially highlight the few-shot results as many of them are only slightly behind state-of-the-art fine-tuned models.
- **p. 9 / 2 Approach - extractive PDF cue:** Dataset Quantity (tokens) Weight in training mix Epochs elapsed when training for 300B tokens Common Crawl (filtered) 410 billion 60% 0.44 WebText2 19 billion 22% ...
- **p. 3 / 1 Introduction - extractive PDF cue:** First, single-layer representations were learned using word vectors [MCCD13, PSM14] and fed to task-specific architectures, then RNNs with multiple layers of representations and contextual state ...
- **p. 5 / 1 Introduction - extractive PDF cue:** For each task, we evaluate GPT-3 under 3 conditions: (a) "few-shot learning", or in-context learning where we allow as many demonstrations as will fit into ...
- **Normalized interface:** observation=논문이 명시한 observation과 task input; state=task state 또는 decision variable; output/action=paper-specific output/action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | On tasks that involve binary classification, we give the options more semantically meaningful names (e.g. "True" or "False" rather than 0 or ... | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | To help with this, we can think in terms of traditional security risk assessment frameworks, which outline key steps such as identifying ... | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | These architectures and techniques are potentially complementary to our work, and could be applied to decrease latency and memory footprint of giant ... | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 9 / 2 Approach - extractive PDF cue:** To train the larger models without running out of memory, we use a mixture of model parallelism within each matrix multiply and model parallelism across ...
- **p. 6 / 2 Approach - extractive PDF cue:** As indicated by the name, few-shot learning as described here for language models is related to few-shot learning as used in other contexts in ML ...
- **p. 43 / B Details of Model Training - extractive PDF cue:** We also gradually increase the batch size linearly from a small value (32k tokens) to the full value over the first 4-12 billion tokens of ...
- **p. 43 / B Details of Model Training - extractive PDF cue:** To train all versions of GPT-3, we use Adam with β1 = 0.9, β2 = 0.95, and ϵ = 10-8, we clip the global norm ...
- **p. 8 / 2 Approach - extractive PDF cue:** Previous work [KMH+20] suggests that with enough training data, scaling of validation loss should be approximately a smooth power law as a function of size; ...
- **p. 8 / 2 Approach - extractive PDF cue:** Model Name nparams nlayers dmodel nheads dhead Batch Size Learning Rate GPT-3 Small 125M 12 768 12 64 0.5M 6.0 × 10-4 GPT-3 Medium 350M ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Model, Architectures, same, architecture, GPT-2, RWC, including, modified, initialization, pre-normalization, reversible, tokenization, described, therein, exception, alternating, dense, locally, banded, sparse.
- **Relevant PDF headings:** 2 Approach (p. 2); B Details of Model Training (p. 2); 2 Approach (p. 6); B Details of Model Training (p. 43); Model (p. 47); Model (p. 48).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Input representation | We omit the 4 Wikipedia-related tasks in that work because they are entirely contained in our training data, and we also omit ... | p. 11 (3 Results), p. 29 (3 Results) |
| Core objective / transformation | On DROP [DWD+19], a dataset testing discrete reasoning and numeracy in the context of reading comprehension, GPT-3 in a few-shot setting outperforms ... | p. 18 (3 Results), p. 19 (3 Results) |
| Downstream transfer boundary | GPT-3 significantly improves SOTA on LAMBADA while achieving respectable performance on two difficult completion prediction datasets. a[Tur20] b[RWC+19] c[LDL19] d[LCH+20] Figure 3.2: ... | p. 12 (3 Results), p. 16 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 1.2: Larger models make increasingly efficient use of in-context information. We show in-context learning performance on a simple task requiring the model to remove ...
- **p. 33 / 3 Results - extractive PDF cue:** Overall, we have made a best effort to measure and document the effects of data contamination, and to note or outright remove problematic results, depending ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 1.2 illustrates the conditions we study, and shows few-shot learning of a simple task requiring the model to remove extraneous symbols from a word. ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 2.2: Datasets used to train GPT-3. "Weight in training mix" refers to the fraction of examples during training that are drawn from a given ...
- **p. 29 / 3 Results - extractive PDF cue:** While it is common practice to train large models without investigating contamination, given the increasing scale of pretraining datasets, we believe this issue is becoming ...
- **p. 31 / 3 Results - extractive PDF cue:** For each benchmark, we produce a ‘clean' version which removes all potentially leaked examples, defined roughly as examples that have a 13-gram overlap with anything ...
- **p. 13 / 3 Results - extractive PDF cue:** [RRS20] recently demonstrated that a large language model can perform surprisingly well directly answering the questions without conditioning on auxilliary information.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 8 (2 Approach), p. 9 (2 Approach), p. 6 (2 Approach), p. 43 (B Details of Model Training), p. 43 (B Details of Model Training), p. 8 (2 Approach), objective p. 43 (B Details of Model Training), p. 43 (B Details of Model Training), p. 8 (2 Approach), p. 8 (2 Approach), p. 9 (2 Approach), p. 9 (2 Approach), temporal p. 10 (2.4 Evaluation), p. 35 (3 Results), p. 40 (7 Related Work), p. 40 (7 Related Work), p. 3 (1 Introduction), p. 3 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
