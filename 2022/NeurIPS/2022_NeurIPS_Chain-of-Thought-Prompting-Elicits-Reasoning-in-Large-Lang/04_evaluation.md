# Evaluation - Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (43 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2201.11903; PDF retrieval source: https://arxiv.org/pdf/2201.11903. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (3.2 Results), p. 7 (3.2 Results), p. 5 (3.2 Results), p. 5 (3.2 Results), p. 8 (3.2 Results), p. 2 (Figure/Table caption)): With chain-of-thought prompting, PaLM 540B achieved strong performance relative to baselines, outperforming the prior state of the art on StrategyQA (75.6% vs 69.4%) and outperforming an unaided sports enthusiast on ...

## Evaluation Body Digest

- **p. 7 / 3.2 Results - extractive PDF cue:** Finally, the SayCan dataset (Ahn et al., 2022) involves mapping a natural language instruction to a sequence of robot actions from a discrete set.
- **p. 5 / 3.2 Results - extractive PDF cue:** Third, chain-of-thought prompting via GPT-3 175B and PaLM 540B compares favorably to prior state of the art, which typically finetunes a task-specific model on a ...
- **p. 4 / 3.2 Results - extractive PDF cue:** The strongest results of chain-of-thought prompting are summarized in Figure 4, with all experimental outputs for each model collection, model size, and benchmark shown in ...
- **p. 5 / 3.2 Results - extractive PDF cue:** On the other two datasets, AQuA and ASDiv, PaLM with chain-of-thought prompting reaches within 2% of the state of the art (Appendix Table 2).
- **p. 6 / 3.2 Results - extractive PDF cue:** Results for other datasets are given in Appendix Table 6 and Table 7.
- **p. 7 / 3.2 Results - extractive PDF cue:** We consider five datasets covering a diverse range of commonsense reasoning types.
- **p. 8 / 3.2 Results - extractive PDF cue:** As the construction of these symbolic reasoning tasks is well-defined, for each task we consider an in-domain test set for which examples had the same ...
- **p. 8 / 3.2 Results - extractive PDF cue:** And yet, small models still fail-the ability to perform abstract manipulations on unseen symbols for these three tasks only arises at the scale of 100B ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 논문이 정의한 robot/embodied environment.
- **Input boundary:** 논문이 명시한 observation과 task input.
- **Output/decision under evaluation:** paper-specific output/action.
- **Primary target:** primary task objective와 closed-loop behavior.
- **Detected evaluation headings:** 3.2 Results (p. 4); B All Experimental Results (p. 20).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 3.2 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | With chain-of-thought prompting, PaLM 540B achieved strong performance relative to baselines, outperforming the prior state of the art on StrategyQA (75.6% vs 69.4%) and ... | p. 7 (3.2 Results) |
| 3.2 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | These results demonstrate that chain-of-thought prompting can also improve performance on tasks requiring a range of commonsense reasoning abilities (though note that gain was ... | p. 7 (3.2 Results) |
| 3.2 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | On the other hand, for SingleOp, the easiest subset of MAWPS which only requires a single step to solve, performance improvements were either negative ... | p. 5 (3.2 Results) |
| 3.2 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | 3.3 Ablation Study The observed benefits of using chain-of-thought prompting raises the natural question of whether the same performance improvements can be conferred via ... | p. 5 (3.2 Results) |
| 3.2 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | With chain-of-thought prompting, language models achieve upward scaling curves (though performance is lower than in the in-domain setting). | p. 8 (3.2 Results) |

## Dataset / Benchmark Role

- **p. 7 / 3.2 Results - extractive PDF cue:** Finally, the SayCan dataset (Ahn et al., 2022) involves mapping a natural language instruction to a sequence of robot actions from a discrete set.
- **p. 5 / 3.2 Results - extractive PDF cue:** Third, chain-of-thought prompting via GPT-3 175B and PaLM 540B compares favorably to prior state of the art, which typically finetunes a task-specific model on a ...
- **p. 4 / 3.2 Results - extractive PDF cue:** The strongest results of chain-of-thought prompting are summarized in Figure 4, with all experimental outputs for each model collection, model size, and benchmark shown in ...
- **p. 5 / 3.2 Results - extractive PDF cue:** On the other two datasets, AQuA and ASDiv, PaLM with chain-of-thought prompting reaches within 2% of the state of the art (Appendix Table 2).
- **p. 6 / 3.2 Results - extractive PDF cue:** Results for other datasets are given in Appendix Table 6 and Table 7.
- **p. 7 / 3.2 Results - extractive PDF cue:** We consider five datasets covering a diverse range of commonsense reasoning types.
- **p. 8 / 3.2 Results - extractive PDF cue:** As the construction of these symbolic reasoning tasks is well-defined, for each task we consider an in-domain test set for which examples had the same ...
- **p. 8 / 3.2 Results - extractive PDF cue:** And yet, small models still fail-the ability to perform abstract manipulations on unseen symbols for these three tasks only arises at the scale of 100B ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Chain-of-thought prompting enables large language models to tackle complex arithmetic, commonsense, and symbolic reasoning tasks. Chain-of-thought reasoning processes are highlighted. 36th Conference on ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2: PaLM 540B uses chain-of- thought prompting to achieve new state- of-the-art performance on the GSM8K benchmark of math word problems. Finetuned GPT-3 and ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3: Examples of ⟨input, chain of thought, output⟩triples for arithmetic, commonsense, and symbolic reasoning benchmarks. Chains of thought are highlighted. Full prompts in Appendix ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4: Chain-of-thought prompting enables large language models to solve challenging math problems. Notably, chain-of-thought reasoning is an emergent ability of increasing model scale. Prior ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 5: Ablation study for dif- ferent variations of prompting us- ing LaMDA 137B and PaLM 540B. Results for other datasets are given in Appendix ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 6: Chain-of-thought prompting has variance for different prompt exam- ples (as expected) but outperforms stan- dard prompting for various annotators as well as for ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 7: Chain-of-thought prompting also improves the commonsense reasoning abilities of language models. The language model shown here is PaLM. Prior best numbers are from ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 8: Using chain-of-thought prompting facilitates generalization to longer sequences in two symbolic rea- soning tasks. Our final experimental evaluation considers symbolic rea- soning, which ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Finally, the SayCan dataset (Ahn et al., 2022) involves mapping a natural language instruction to a sequence of robot actions from a discrete set. | embodiment, simulator version and control stack | p. 7 (3.2 Results), p. 5 (3.2 Results) |
| Task/environment | Third, chain-of-thought prompting via GPT-3 175B and PaLM 540B compares favorably to prior state of the art, which typically finetunes a task-specific model on ... | reset, timeout, object/scene variation | p. 5 (3.2 Results), p. 4 (3.2 Results) |
| Observation/sensor | 논문이 명시한 observation과 task input | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 2 (1 Introduction) |
| Output/decision | paper-specific output/action | action frame, controller and termination | p. 2 (1 Introduction), p. 3 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 3.4 Robustness of Chain of Thought GSM8K 0 5 10 15 20 Solve rate (%) Standard prompting Chain-of-thought prompting · different annotator (B) · ... | definition/direction/unit from same section | p. 6 (3.2 Results) |
| The summary is that scaling PaLM to 540B fixes a large portion of one-step missing and semantic understanding errors in the 62B model (see ... | definition/direction/unit from same section | p. 5 (3.2 Results) |
| To provide a small insight into why scaling improves chain-of-thought reasoning ability, we performed a similar analysis of errors made by PaLM 62B and ... | definition/direction/unit from same section | p. 5 (3.2 Results) |
| Sensitivity to exemplars is a key consideration of prompting approaches-for instance, varying the permutation of few-shot exemplars can cause the accuracy of GPT-3 on ... | definition/direction/unit from same section | p. 6 (3.2 Results) |
| Figure 9: Error analysis of 45 problems that PaLM 62B got incorrect. These errors were categorized that semantic understanding, one step missing, and other. ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| Table 7: Ablation and robustness results for four datasets in commonsense and symbolic reasoning. Chain of thought generally outperforms ablations by a large amount. ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |
| These results demonstrate that chain-of-thought prompting can also improve performance on tasks requiring a range of commonsense reasoning abilities (though note that gain was ... | definition/direction/unit from same section | p. 7 (3.2 Results) |
| With chain-of-thought prompting, PaLM 540B achieved strong performance relative to baselines, outperforming the prior state of the art on StrategyQA (75.6% vs 69.4%) and ... | definition/direction/unit from same section | p. 7 (3.2 Results) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Although there is variance among different chain of thought annotations, as would be expected when using exemplar-based prompting (Le Scao and Rush, 2021; Reynolds ... | comparison identity and matched condition | p. 6 (3.2 Results) |
| With chain-of-thought prompting, PaLM 540B achieved strong performance relative to baselines, outperforming the prior state of the art on StrategyQA (75.6% vs 69.4%) and ... | comparison identity and matched condition | p. 7 (3.2 Results) |
| For instance, for GSM8K (the dataset with the lowest baseline performance), performance more than doubled for the largest GPT and PaLM models. | comparison identity and matched condition | p. 5 (3.2 Results) |
| This variant performs about the same as the baseline, which suggests that the sequential reasoning embodied in the chain of thought is useful for ... | comparison identity and matched condition | p. 6 (3.2 Results) |
| source (examples in this dataset already included reasoning steps like a chain of thought).2 Figure 6 shows that these prompts performed comparably with our ... | comparison identity and matched condition | p. 7 (3.2 Results) |
| Table 7: Ablation and robustness results for four datasets in commonsense and symbolic reasoning. Chain of thought generally outperforms ablations by a large amount. ... | comparison identity and matched condition | p. 23 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To isolate the effect of variable computation from chain-of-thought reasoning, we test a configuration where the model is prompted to output a only sequence ... | component/input/data sensitivity | p. 6 (3.2 Results) |
| 3.3 Ablation Study The observed benefits of using chain-of-thought prompting raises the natural question of whether the same performance improvements can be conferred via ... | component/input/data sensitivity | p. 5 (3.2 Results) |
| (2021).1 Figure 6 shows these results for LaMDA 137B on GSM8K and MAWPS (ablation results for other datasets are given in Appendix Table 6 ... | component/input/data sensitivity | p. 6 (3.2 Results) |
| Figure 10: Examples of semantic understanding and one-step missing errors that were fixed by scaling PaLM from 62B to 540B. A.2 What is the ... | component/input/data sensitivity | p. 17 (Figure/Table caption) |
| Table 7: Ablation and robustness results for four datasets in commonsense and symbolic reasoning. Chain of thought generally outperforms ablations by a large amount. ... | component/input/data sensitivity | p. 23 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We show that chain-ofthought prompting not only enables language models to perform symbolic reasoning tasks that are challenging in the standard prompting setting, but ... | With chain-of-thought prompting, PaLM 540B achieved strong performance relative to baselines, outperforming the prior state of the art on StrategyQA (75.6% vs 69.4%) and ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (3.2 Results), p. 7 (3.2 Results), p. 5 (3.2 Results), p. 5 (3.2 Results), p. 8 (3.2 Results), p. 2 (Figure/Table caption) |
| Primary metric/result | These results demonstrate that chain-of-thought prompting can also improve performance on tasks requiring a range of commonsense reasoning abilities (though note that gain was ... | numeric claim only at cited anchor | p. 7 (3.2 Results) |

- Numeric sentences retained from the body:
- **p. 7 / 3.2 Results - extractive PDF cue:** 2We sample examples ≤60 tokens to fit into our input context window, and also limit the examples to ≤2 steps to solve for a fair ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | As for limitations, we first qualify that although chain of thought emulates the thought processes of human reasoners, this does not answer whether the ... | p. 9 (6 Discussion) |
| body limitation/failure cue | Third, there is no guarantee of correct reasoning paths, which can lead to both correct and incorrect answers; improving factual generations of language models ... | p. 9 (6 Discussion) |
| body limitation/failure cue | As for the OOD evaluations, standard prompting fails for both tasks. | p. 8 (3.2 Results) |
| body limitation/failure cue | Table 6: Ablation and robustness results for arithmetic reasoning datasets. Chain of thought generally outperforms ablations by a large amount. "Equation only" performs in ... | p. 23 (Figure/Table caption) |
| body limitation/failure cue | We first saw that chain-of-thought prompting improves performance by a large margin on arithmetic reasoning, yielding improvements that are much stronger than ablations and ... | p. 8 (6 Discussion) |
| body limitation/failure cue | That is, chain-of-thought prompting does not positively impact performance for small models, and only yields performance gains when used with models of ∼100B parameters. | p. 4 (3.2 Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| As LaMDA experiments did not show large variance among different seeds, to save compute we report results for a single exemplar order for all ... | p. 4 (1 Introduction) |
| To confirm that successful chain-of-thought prompting works for other sets of exemplars, we also run experiments with three sets of eight exemplars randomly sampled ... | p. 6 (3.2 Results) |
| We explore how generating a chain of thought-a series of intermediate reasoning steps-significantly improves the ability of large language models to perform complex reasoning. | p. 1 (Abstract) |
| A chain of thought is a series of intermediate natural language reasoning steps that lead to the final output, and we refer to this ... | p. 2 (1 Introduction) |
| That is, instead of finetuning a separate language model checkpoint for each new task, one can simply "prompt" the model with a few input-output ... | p. 2 (1 Introduction) |
| First, chain of thought, in principle, allows models to decompose multi-step problems into intermediate steps, which means that additional computation can be allocated to ... | p. 3 (1 Introduction) |
| The fourth is UL2 20B (Tay et al., 2022), and the fifth is Codex (Chen et al., 2021, code-davinci-002 in the OpenAI API). | p. 4 (1 Introduction) |
| For each of 4 days, 5 more computers were added. | p. 6 (3.2 Results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 6 Discussion - extractive PDF cue:** As for limitations, we first qualify that although chain of thought emulates the thought processes of human reasoners, this does not answer whether the neural ...
- **p. 9 / 6 Discussion - extractive PDF cue:** Third, there is no guarantee of correct reasoning paths, which can lead to both correct and incorrect answers; improving factual generations of language models is ...
- **p. 8 / 3.2 Results - extractive PDF cue:** As for the OOD evaluations, standard prompting fails for both tasks.
- **p. 23 / Figure/Table caption - extractive PDF cue:** Table 6: Ablation and robustness results for arithmetic reasoning datasets. Chain of thought generally outperforms ablations by a large amount. "Equation only" performs in between ...
- **p. 8 / 6 Discussion - extractive PDF cue:** We first saw that chain-of-thought prompting improves performance by a large margin on arithmetic reasoning, yielding improvements that are much stronger than ablations and robust ...
- **p. 4 / 3.2 Results - extractive PDF cue:** That is, chain-of-thought prompting does not positively impact performance for small models, and only yields performance gains when used with models of ∼100B parameters.

- **PDF anchors reviewed:** datasets p. 7 (3.2 Results), p. 5 (3.2 Results), p. 4 (3.2 Results), p. 5 (3.2 Results), p. 6 (3.2 Results), p. 7 (3.2 Results), metrics p. 6 (3.2 Results), p. 5 (3.2 Results), p. 5 (3.2 Results), p. 6 (3.2 Results), p. 16 (Figure/Table caption), p. 23 (Figure/Table caption), baselines p. 6 (3.2 Results), p. 7 (3.2 Results), p. 5 (3.2 Results), p. 6 (3.2 Results), p. 7 (3.2 Results), p. 23 (Figure/Table caption), results p. 7 (3.2 Results), p. 7 (3.2 Results), p. 5 (3.2 Results), p. 5 (3.2 Results), p. 8 (3.2 Results), p. 2 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
