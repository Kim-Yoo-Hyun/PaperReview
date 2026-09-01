# Method - Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (43 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2201.11903; PDF retrieval source: https://arxiv.org/pdf/2201.11903. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 3 (1 Introduction), p. 8 (6 Discussion)): The first is GPT-3 (Brown et al., 2020), for which we use text-ada-001, text-babbage-001, text-curie-001, and text-davinci-002, which presumably correspond to InstructGPT models of 350M, 1.3B, 6.7B, and 175B parameters ...

## Method Body Digest

- **p. 4 / 1 Introduction - extractive PDF cue:** The first is GPT-3 (Brown et al., 2020), for which we use text-ada-001, text-babbage-001, text-curie-001, and text-davinci-002, which presumably correspond to InstructGPT models of 350M, ...
- **p. 2 / 1 Introduction - extractive PDF cue:** This work underscores how large language models can learn via a few examples with natural language data about the task (c.f. automatically learning the patterns ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Specifically, we explore the ability of language models to perform few-shot prompting for reasoning tasks, given a prompt that consists of triples: ⟨input, chain of ...
- **p. 4 / 1 Introduction - extractive PDF cue:** For AQuA, we used four exemplars and solutions from the training set, as given in Appendix Table 21.
- **p. 3 / 1 Introduction - extractive PDF cue:** First, chain of thought, in principle, allows models to decompose multi-step problems into intermediate steps, which means that additional computation can be allocated to problems ...
- **p. 8 / 6 Discussion - extractive PDF cue:** We first saw that chain-of-thought prompting improves performance by a large margin on arithmetic reasoning, yielding improvements that are much stronger than ablations and robust ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Strikingly, chainof-thought prompting when used with the 540B parameter language model performs comparably with task-specific finetuned models on several tasks, even achieving new state of ...
- **p. 2 / 1 Introduction - extractive PDF cue:** A prompting only approach is important because it does not require a large training dataset and because a single model checkpoint can perform many tasks ...

## Design Rationale

- **p. 8 / 3.2 Results - extractive PDF cue:** We show that chain-ofthought prompting not only enables language models to perform symbolic reasoning tasks that are challenging in the standard prompting setting, but also ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Specifically, we explore the ability of language models to perform few-shot prompting for reasoning tasks, given a prompt that consists of triples: ⟨input, chain of ...
- **p. 2 / 1 Introduction - extractive PDF cue:** We present empirical evaluations on arithmetic, commonsense, and symbolic reasoning benchmarks, showing that chain-of-thought prompting outperforms standard prompting, sometimes to a striking degree.

## Source Evidence Cues

- **p. 4 / 1 Introduction - extractive PDF cue:** The first is GPT-3 (Brown et al., 2020), for which we use text-ada-001, text-babbage-001, text-curie-001, and text-davinci-002, which presumably correspond to InstructGPT models of 350M, ...
- **p. 2 / 1 Introduction - extractive PDF cue:** This work underscores how large language models can learn via a few examples with natural language data about the task (c.f. automatically learning the patterns ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Specifically, we explore the ability of language models to perform few-shot prompting for reasoning tasks, given a prompt that consists of triples: ⟨input, chain of ...
- **p. 4 / 1 Introduction - extractive PDF cue:** For AQuA, we used four exemplars and solutions from the training set, as given in Appendix Table 21.
- **p. 3 / 1 Introduction - extractive PDF cue:** First, chain of thought, in principle, allows models to decompose multi-step problems into intermediate steps, which means that additional computation can be allocated to problems ...
- **p. 8 / 6 Discussion - extractive PDF cue:** We first saw that chain-of-thought prompting improves performance by a large margin on arithmetic reasoning, yielding improvements that are much stronger than ablations and robust ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Strikingly, chainof-thought prompting when used with the 540B parameter language model performs comparably with task-specific finetuned models on several tasks, even achieving new state of ...
- **Detected method headings:** A.1 Why does increasing model scale improve chain-of-thought prompting? (p. 16)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Input representation | source-defined input을 learnable representation으로 바꾼다 | paper-specific image/text/sequence input | encoder, tokenization, normalization 또는 feature extraction을 수행 | latent feature/state | The first is GPT-3 (Brown et al., 2020), for which we use text-ada-001, text-babbage-001, text-curie-001, and text-davinci-002, which presumably correspond to InstructGPT ... | p. 4 (1 Introduction), p. 2 (1 Introduction) |
| Core objective / transformation | source task의 prediction·generation 목표를 최적화한다 | representation, target/condition | paper-specific model, loss, decoder 또는 generative process를 적용 | prediction/embedding/sample | This work underscores how large language models can learn via a few examples with natural language data about the task (c.f. automatically ... | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Downstream transfer boundary | 결과를 후속 task 또는 embodied system에 전달한다 | output와 query/task context | task head, retrieval, grounding 또는 adapter를 적용 | task cue/representation | Specifically, we explore the ability of language models to perform few-shot prompting for reasoning tasks, given a prompt that consists of triples: ... | p. 2 (1 Introduction), p. 4 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 Introduction - extractive PDF cue:** A prompting only approach is important because it does not require a large training dataset and because a single model checkpoint can perform many tasks ...
- **p. 2 / 1 Introduction - extractive PDF cue:** For rationale-augmented training and finetuning methods, it is costly to create a large set of high quality rationales, which is much more complicated than simple ...
- **Formal bridge:** source-defined input o -> prediction/embedding/sample ŷ -> paper-specific objective -> source task metric; robot link not established.
- **Equation/algorithm anchors:** p. 2 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Model, Input, Output, Figure, Chain-of-thought, prompting, enables, large, language, models, tackle, complex, arithmetic, commonsense | 논문이 명시한 observation과 task input | body cue; exact tensor/frame verify |
| State/latent | Model, Input, Output, Figure, Chain-of-thought, prompting, enables, large, language, models | task state 또는 decision variable | body cue; notation verify |
| Action/output | chain-ofthought, prompting, only, enables, language, models, perform, symbolic, reasoning, tasks | paper-specific output/action | body cue; unit/decoder verify |
| Objective/constraint | prompting, only, important, because, does, require, large, training, dataset, single | paper-specific objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Abstract - extractive PDF cue:** Model Input Model Output Model Output Model Input Figure 1: Chain-of-thought prompting enables large language models to tackle complex arithmetic, commonsense, and symbolic reasoning tasks.
- **p. 2 / 1 Introduction - extractive PDF cue:** That is, instead of finetuning a separate language model checkpoint for each new task, one can simply "prompt" the model with a few input-output exemplars ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Specifically, we explore the ability of language models to perform few-shot prompting for reasoning tasks, given a prompt that consists of triples: ⟨input, chain of ...
- **p. 3 / 1 Introduction - extractive PDF cue:** (2020), in which a language model is given in-context exemplars of input-output pairs before outputting a prediction for a test-time example.
- **p. 3 / 1 Introduction - extractive PDF cue:** Strikingly, chainof-thought prompting when used with the 540B parameter language model performs comparably with task-specific finetuned models on several tasks, even achieving new state of ...
- **p. 1 / Abstract - extractive PDF cue:** For instance, prompting a PaLM 540B with just eight chain-of-thought exemplars achieves state-of-the-art accuracy on the GSM8K benchmark of math word problems, surpassing even finetuned ...
- **p. 4 / 1 Introduction - extractive PDF cue:** Math Word Problems (free response) Math Word Problems (multiple choice) CSQA (commonsense) StrategyQA Date Understanding Sports Understanding Last Letter Concatenation Coin Flip (state tracking) Q: ...
- **Normalized interface:** observation=논문이 명시한 observation과 task input; state=task state 또는 decision variable; output/action=paper-specific output/action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | We explore how generating a chain of thought-a series of intermediate reasoning steps-significantly improves the ability of large language models to perform ... | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | 2 Chain-of-Thought Prompting Consider one's own thought process when solving a complicated reasoning task such as a multi-step math word problem. | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | not recovered | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 Introduction - extractive PDF cue:** This work underscores how large language models can learn via a few examples with natural language data about the task (c.f. automatically learning the patterns ...
- **p. 4 / 1 Introduction - extractive PDF cue:** For AQuA, we used four exemplars and solutions from the training set, as given in Appendix Table 21.
- **p. 6 / 3.2 Results - extractive PDF cue:** To confirm that successful chain-of-thought prompting works for other sets of exemplars, we also run experiments with three sets of eight exemplars randomly sampled from ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** first, GPT-3, Brown, text-ada-001, text-babbage-001, text-curie-001, text-davinci-002, presumably, correspond, InstructGPT, models, parameters, Ouyang, second, LaMDA, Thoppilan, underscores, large, language, learn.
- **Relevant PDF headings:** A.1 Why does increasing model scale improve chain-of-thought prompting? (p. 16).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Input representation | Finally, the SayCan dataset (Ahn et al., 2022) involves mapping a natural language instruction to a sequence of robot actions from a ... | p. 7 (3.2 Results), p. 5 (3.2 Results) |
| Core objective / transformation | Although there is variance among different chain of thought annotations, as would be expected when using exemplar-based prompting (Le Scao and Rush, ... | p. 6 (3.2 Results), p. 7 (3.2 Results) |
| Downstream transfer boundary | With chain-of-thought prompting, PaLM 540B achieved strong performance relative to baselines, outperforming the prior state of the art on StrategyQA (75.6% vs ... | p. 7 (3.2 Results), p. 7 (3.2 Results) |

## Failure and Ablation Link

- **p. 6 / 3.2 Results - extractive PDF cue:** To isolate the effect of variable computation from chain-of-thought reasoning, we test a configuration where the model is prompted to output a only sequence of ...
- **p. 5 / 3.2 Results - extractive PDF cue:** 3.3 Ablation Study The observed benefits of using chain-of-thought prompting raises the natural question of whether the same performance improvements can be conferred via other ...
- **p. 6 / 3.2 Results - extractive PDF cue:** (2021).1 Figure 6 shows these results for LaMDA 137B on GSM8K and MAWPS (ablation results for other datasets are given in Appendix Table 6 / ...
- **p. 17 / Figure/Table caption - extractive PDF cue:** Figure 10: Examples of semantic understanding and one-step missing errors that were fixed by scaling PaLM from 62B to 540B. A.2 What is the role ...
- **p. 23 / Figure/Table caption - extractive PDF cue:** Table 7: Ablation and robustness results for four datasets in commonsense and symbolic reasoning. Chain of thought generally outperforms ablations by a large amount. Chain ...
- **p. 9 / 6 Discussion - extractive PDF cue:** As for limitations, we first qualify that although chain of thought emulates the thought processes of human reasoners, this does not answer whether the neural ...
- **p. 9 / 6 Discussion - extractive PDF cue:** Third, there is no guarantee of correct reasoning paths, which can lead to both correct and incorrect answers; improving factual generations of language models is ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 3 (1 Introduction), p. 8 (6 Discussion), objective p. 2 (1 Introduction), p. 2 (1 Introduction), temporal p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
