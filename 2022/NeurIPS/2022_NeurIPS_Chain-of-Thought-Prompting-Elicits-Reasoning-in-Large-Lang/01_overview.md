# Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (43 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2201.11903.
> PDF retrieval source: https://arxiv.org/pdf/2201.11903. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Foundations: Vision and Language Models
- Tier: REFERENCE
- Tags: LLM, reasoning, Chain-of-Thought
- Official paper: https://arxiv.org/abs/2201.11903
- Full-text retrieval: https://arxiv.org/pdf/2201.11903
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (43 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Foundations: Vision and Language Models의 upstream 문제를 이해하기 위해 읽는다. 본문은 Both of the above ideas, however, have key limitations.를 문제로 두고, We show that chain-ofthought prompting not only enables language models to perform symbolic reasoning tasks that are challenging in the standard prompting setting, but also facilitates length generalization to inference-time inputs long ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We explore how generating a chain of thought-a series of intermediate reasoning steps-significantly improves the ability of large language models to perform complex reasoning.
- **p. 1 / Abstract - extractive body cue:** In particular, we show how such reasoning abilities emerge naturally in sufficiently large language models via a simple method called chain-ofthought prompting, where a few ...
- **p. 1 / Abstract - extractive body cue:** Experiments on three large language models show that chain-of-thought prompting improves performance on a range of arithmetic, commonsense, and symbolic reasoning tasks.
- **p. 1 / Abstract - extractive body cue:** The empirical gains can be striking.
- **p. 1 / Abstract - extractive body cue:** For instance, prompting a PaLM 540B with just eight chain-of-thought exemplars achieves state-of-the-art accuracy on the GSM8K benchmark of math word problems, surpassing even finetuned ...
- **p. 2 / 1 Introduction - extractive body cue:** Both of the above ideas, however, have key limitations.
- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we combine the strengths of these two ideas in a way that avoids their limitations.

## Core Idea

- **p. 8 / 3.2 Results - extractive body cue:** We show that chain-ofthought prompting not only enables language models to perform symbolic reasoning tasks that are challenging in the standard prompting setting, but also ...
- **p. 2 / 1 Introduction - extractive body cue:** Specifically, we explore the ability of language models to perform few-shot prompting for reasoning tasks, given a prompt that consists of triples: ⟨input, chain of ...
- **p. 2 / 1 Introduction - extractive body cue:** We present empirical evaluations on arithmetic, commonsense, and symbolic reasoning benchmarks, showing that chain-of-thought prompting outperforms standard prompting, sometimes to a striking degree.
- **p. 5 / 3.2 Results - extractive body cue:** 0 20 40 60 GSM8K solve rate (%) LaMDA GPT PaLM Standard prompting Chain-of-thought prompting Prior supervised best 0 20 40 60 80 SVAMP solve ...
- **p. 1 / Abstract - extractive body cue:** Model Input Model Output Model Output Model Input Figure 1: Chain-of-thought prompting enables large language models to tackle complex arithmetic, commonsense, and symbolic reasoning tasks.
- **p. 4 / 1 Introduction - extractive body cue:** The first is GPT-3 (Brown et al., 2020), for which we use text-ada-001, text-babbage-001, text-curie-001, and text-davinci-002, which presumably correspond to InstructGPT models of 350M, ...
- **p. 2 / 1 Introduction - extractive body cue:** This work underscores how large language models can learn via a few examples with natural language data about the task (c.f. automatically learning the patterns ...
- **p. 4 / 1 Introduction - extractive body cue:** For AQuA, we used four exemplars and solutions from the training set, as given in Appendix Table 21.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Model Input Model Output Model Output Model Input Figure 1: Chain-of-thought prompting enables large language models to tackle complex arithmetic, commonsense, and symbolic reasoning tasks. | 논문이 명시한 observation과 task input | p. 1 (Abstract), p. 2 (1 Introduction) |
| State/latent | Model, Input, Output, Figure, Chain-of-thought, prompting, enables, large, language, models, tackle, complex | task state 또는 decision variable | p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Output/action | That is, instead of finetuning a separate language model checkpoint for each new task, one can simply "prompt" the model with a few input-output exemplars demonstrating the task. | paper-specific output/action | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Objective/outcome | A prompting only approach is important because it does not require a large training dataset and because a single model checkpoint can perform many tasks without loss of generality. | primary task objective와 closed-loop behavior | p. 2 (1 Introduction), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 8 / 3.2 Results - extractive body cue:** We show that chain-ofthought prompting not only enables language models to perform symbolic reasoning tasks that are challenging in the standard prompting setting, but also ...
- **p. 2 / 1 Introduction - extractive body cue:** Specifically, we explore the ability of language models to perform few-shot prompting for reasoning tasks, given a prompt that consists of triples: ⟨input, chain of ...
- **p. 2 / 1 Introduction - extractive body cue:** We present empirical evaluations on arithmetic, commonsense, and symbolic reasoning benchmarks, showing that chain-of-thought prompting outperforms standard prompting, sometimes to a striking degree.
- **p. 5 / 3.2 Results - extractive body cue:** 0 20 40 60 GSM8K solve rate (%) LaMDA GPT PaLM Standard prompting Chain-of-thought prompting Prior supervised best 0 20 40 60 80 SVAMP solve ...
- **p. 1 / Abstract - extractive body cue:** Model Input Model Output Model Output Model Input Figure 1: Chain-of-thought prompting enables large language models to tackle complex arithmetic, commonsense, and symbolic reasoning tasks.
- **p. 7 / 3.2 Results - extractive body cue:** With chain-of-thought prompting, PaLM 540B achieved strong performance relative to baselines, outperforming the prior state of the art on StrategyQA (75.6% vs 69.4%) and outperforming ...
- **p. 7 / 3.2 Results - extractive body cue:** These results demonstrate that chain-of-thought prompting can also improve performance on tasks requiring a range of commonsense reasoning abilities (though note that gain was minimal ...
- **p. 5 / 3.2 Results - extractive body cue:** On the other hand, for SingleOp, the easiest subset of MAWPS which only requires a single step to solve, performance improvements were either negative or ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (3.2 Results), p. 7 (3.2 Results) |
| Embodiment/environment | Finally, the SayCan dataset (Ahn et al., 2022) involves mapping a natural language instruction to a sequence of robot actions from a discrete set. | hardware/simulator version and reset protocol | p. 7 (3.2 Results), p. 5 (3.2 Results) |
| Dataset/benchmark | The strongest results of chain-of-thought prompting are summarized in Figure 4, with all experimental outputs for each model collection, model size, and benchmark shown in Table 2 in the Appendix. | role, split, size and leakage | p. 7 (3.2 Results), p. 5 (3.2 Results), p. 4 (3.2 Results), p. 5 (3.2 Results) |
| Metric | 3.4 Robustness of Chain of Thought GSM8K 0 5 10 15 20 Solve rate (%) Standard prompting Chain-of-thought prompting · different annotator (B) · different annotator (C) · intentionally concise style · ... | definition, denominator, direction and uncertainty | p. 6 (3.2 Results), p. 5 (3.2 Results), p. 5 (3.2 Results) |
| Baseline/ablation | Although there is variance among different chain of thought annotations, as would be expected when using exemplar-based prompting (Le Scao and Rush, 2021; Reynolds and McDonell, 2021; Zhao et al., 2021), all ... | fair input/data/compute/action matching | p. 6 (3.2 Results), p. 7 (3.2 Results), p. 5 (3.2 Results) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 6 Discussion - extractive body cue:** As for limitations, we first qualify that although chain of thought emulates the thought processes of human reasoners, this does not answer whether the neural ...
- **p. 9 / 6 Discussion - extractive body cue:** Third, there is no guarantee of correct reasoning paths, which can lead to both correct and incorrect answers; improving factual generations of language models is ...
- **p. 8 / 3.2 Results - extractive body cue:** As for the OOD evaluations, standard prompting fails for both tasks.
- **p. 23 / Figure/Table caption - extractive body cue:** Table 6: Ablation and robustness results for arithmetic reasoning datasets. Chain of thought generally outperforms ablations by a large amount. "Equation only" performs in between ...
- **p. 8 / 6 Discussion - extractive body cue:** We first saw that chain-of-thought prompting improves performance by a large margin on arithmetic reasoning, yielding improvements that are much stronger than ablations and robust ...
- **p. 4 / 3.2 Results - extractive body cue:** That is, chain-of-thought prompting does not positively impact performance for small models, and only yields performance gains when used with models of ∼100B parameters.
- **p. 6 / 3.2 Results - extractive body cue:** This result implies that successful use of chain of thought does not depend on a particular linguistic style.

## Why Read It

Foundations: Vision and Language Models의 upstream 문제를 이해하기 위해 읽는다. 본문은 Both of the above ideas, however, have key limitations.를 문제로 두고, We show that chain-ofthought prompting not only enables language models to perform symbolic reasoning tasks that are challenging in the standard prompting setting, but also facilitates length generalization to inference-time inputs long ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (3.2 Results), p. 8 (3.2 Results), p. 5 (3.2 Results), p. 4 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
