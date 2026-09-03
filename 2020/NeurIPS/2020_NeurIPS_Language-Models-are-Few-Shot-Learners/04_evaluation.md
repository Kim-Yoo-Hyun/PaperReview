# Evaluation - Language Models are Few-Shot Learners

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (75 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2005.14165; PDF retrieval source: https://arxiv.org/pdf/2005.14165. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 12 (3 Results), p. 16 (Figure/Table caption), p. 11 (3 Results), p. 13 (3 Results), p. 17 (3 Results), p. 5 (Figure/Table caption)): GPT-3 significantly improves SOTA on LAMBADA while achieving respectable performance on two difficult completion prediction datasets. a[Tur20] b[RWC+19] c[LDL19] d[LCH+20] Figure 3.2: On LAMBADA, the few-shot capability of language mode ...

## Evaluation Body Digest

- **p. 11 / 3 Results - extractive body cue:** We omit the 4 Wikipedia-related tasks in that work because they are entirely contained in our training data, and we also omit the one-billion word ...
- **p. 29 / 3 Results - extractive body cue:** 4 Measuring and Preventing Memorization Of Benchmarks Since our training dataset is sourced from the internet, it is possible that our model was trained on ...
- **p. 18 / 3 Results - extractive body cue:** 3.7 SuperGLUE In order to better aggregate results on NLP tasks and compare to popular models such as BERT and RoBERTa in a more systematic ...
- **p. 33 / 3 Results - extractive body cue:** • Language modeling: We found the 4 Wikipedia language modeling benchmarks measured in GPT-2, plus the Children's Book Test dataset, to be almost entirely contained ...
- **p. 10 / 2.4 Evaluation - extractive body cue:** For most tasks we compare the per-token likelihood (to normalize for length), however on a small number of datasets (ARC, OpenBookQA, and RACE) we gain ...
- **p. 13 / 3 Results - extractive body cue:** We evaluate GPT-3 on the 3 datasets in [RRS20]: Natural Questions [KPR+19], WebQuestions [BCFL13], and TriviaQA [JCWZ17], using the same splits.
- **p. 10 / 2.4 Evaluation - extractive body cue:** For LAMBADA and Storycloze there is no supervised training set available so we draw conditioning examples from the development set and evaluate on the test ...
- **p. 13 / 3 Results - extractive body cue:** One note of caution is that an analysis of test set contamination identified that a significant minority of the LAMBADA dataset appears to be present ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 논문이 정의한 robot/embodied environment.
- **Input boundary:** 논문이 명시한 observation과 task input.
- **Output/decision under evaluation:** paper-specific output/action.
- **Primary target:** primary task objective와 closed-loop behavior.
- **Detected evaluation headings:** 2.4 Evaluation (p. 2); 3 Results (p. 2); 2.4 Evaluation (p. 10); 3 Results (p. 10).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 3 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | GPT-3 significantly improves SOTA on LAMBADA while achieving respectable performance on two difficult completion prediction datasets. a[Tur20] b[RWC+19] c[LDL19] d[LCH+20] Figure 3.2: On LAMBADA, ... | p. 12 (3 Results) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 3.5: Zero-, one-, and few-shot performance on the adversarial Winogrande dataset as model capacity scales. Scaling is relatively smooth with the gains to ... | p. 16 (Figure/Table caption) |
| 3 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | [BHT+20] reflect on the small 1.5% improvement achieved by a doubling of model size between two recent state of the art results ([SPP+19] 11 | p. 11 (3 Results) |
| 3 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | GPT-3 achieves 78.1% accuracy in the one-shot setting and 79.3% accuracy in the few-shot setting, outperforming the 75.4% accuracy of a fine-tuned 1.5B parameter ... | p. 13 (3 Results) |
| 3 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | The largest model achieves a score on the development set in all three conditions that exceeds the best recorded score on the task. such ... | p. 17 (3 Results) |

## Dataset / Benchmark Role

- **p. 11 / 3 Results - extractive body cue:** We omit the 4 Wikipedia-related tasks in that work because they are entirely contained in our training data, and we also omit the one-billion word ...
- **p. 29 / 3 Results - extractive body cue:** 4 Measuring and Preventing Memorization Of Benchmarks Since our training dataset is sourced from the internet, it is possible that our model was trained on ...
- **p. 18 / 3 Results - extractive body cue:** 3.7 SuperGLUE In order to better aggregate results on NLP tasks and compare to popular models such as BERT and RoBERTa in a more systematic ...
- **p. 33 / 3 Results - extractive body cue:** • Language modeling: We found the 4 Wikipedia language modeling benchmarks measured in GPT-2, plus the Children's Book Test dataset, to be almost entirely contained ...
- **p. 10 / 2.4 Evaluation - extractive body cue:** For most tasks we compare the per-token likelihood (to normalize for length), however on a small number of datasets (ARC, OpenBookQA, and RACE) we gain ...
- **p. 13 / 3 Results - extractive body cue:** We evaluate GPT-3 on the 3 datasets in [RRS20]: Natural Questions [KPR+19], WebQuestions [BCFL13], and TriviaQA [JCWZ17], using the same splits.
- **p. 10 / 2.4 Evaluation - extractive body cue:** For LAMBADA and Storycloze there is no supervised training set available so we draw conditioning examples from the development set and evaluate on the test ...
- **p. 13 / 3 Results - extractive body cue:** One note of caution is that an analysis of test set contamination identified that a significant minority of the LAMBADA dataset appears to be present ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1.1: Language model meta-learning. During unsupervised pre-training, a language model develops a broad set of skills and pattern recognition abilities. It then uses these ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1.2: Larger models make increasingly efficient use of in-context information. We show in-context learning performance on a simple task requiring the model to remove ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 1.3: Aggregate performance for all 42 accuracy-denominated benchmarks While zero-shot performance improves steadily with model size, few-shot performance increases more rapidly, demonstrating that larger ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 1.2 illustrates the conditions we study, and shows few-shot learning of a simple task requiring the model to remove extraneous symbols from a word. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 2.1: Zero-shot, one-shot and few-shot, contrasted with traditional fine-tuning. The panels above show four methods for performing a task with a language model - ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 2.1 shows the four methods using the example of translating English to French. In this paper we focus on zero-shot, one-shot and few-shot, with ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2.1: Sizes, architectures, and learning hyper-parameters (batch size in tokens and learning rate) of the models which we trained. All models were trained for ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2.1 shows the sizes and architectures of our 8 models. Here nparams is the total number of trainable parameters, nlayers is the total number ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We omit the 4 Wikipedia-related tasks in that work because they are entirely contained in our training data, and we also omit the one-billion ... | embodiment, simulator version and control stack | p. 11 (3 Results), p. 29 (3 Results) |
| Task/environment | 4 Measuring and Preventing Memorization Of Benchmarks Since our training dataset is sourced from the internet, it is possible that our model was trained ... | reset, timeout, object/scene variation | p. 29 (3 Results), p. 18 (3 Results) |
| Observation/sensor | 논문이 명시한 observation과 task input | calibration, preprocessing, privileged input | p. 4 (1 Introduction), p. 7 (2 Approach) |
| Output/decision | paper-specific output/action | action frame, controller and termination | p. 6 (2 Approach), p. 7 (2 Approach) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| All scores are F1 except results for RACE which report accuracy. a[JZC+19] b[JN20] c[AI19] d[QIA20] e[SPP+19] fine-tuned RoBERTa. | definition/direction/unit from same section | p. 18 (3 Results) |
| We score the model using F1 similarity score, BLEU, or exact match, depending on what is standard for the dataset at hand. | definition/direction/unit from same section | p. 10 (2.4 Evaluation) |
| GPT-3 significantly improves SOTA on LAMBADA while achieving respectable performance on two difficult completion prediction datasets. a[Tur20] b[RWC+19] c[LDL19] d[LCH+20] Figure 3.2: On LAMBADA, ... | definition/direction/unit from same section | p. 12 (3 Results) |
| SuperGLUE BoolQ CB CB COPA RTE Average Accuracy Accuracy F1 Accuracy Accuracy Fine-tuned SOTA 89.0 91.0 96.9 93.9 94.8 92.5 Fine-tuned BERT-Large 69.0 77.4 ... | definition/direction/unit from same section | p. 19 (3 Results) |
| Mean human accuracy (the ratio of correct assignments to non-neutral assignments per participant) at detecting that the intentionally bad articles were model generated was ... | definition/direction/unit from same section | p. 26 (3 Results) |
| Mean accuracy 95% Confidence Interval (low, hi) t compared to control (p-value) "I don't know" assignments Control (deliberately bad model) 86% 83%-90% - 3.6 ... | definition/direction/unit from same section | p. 26 (3 Results) |
| Mean accuracy 95% Confidence Interval (low, hi) t compared to control (p-value) "I don't know" assignments Control 88% 84%-91% - 2.7% GPT-3 175B 52% ... | definition/direction/unit from same section | p. 27 (3 Results) |
| While this setting decreases the performance of the smallest model by almost 20%, for GPT-3 it improves accuracy by 10%. | definition/direction/unit from same section | p. 12 (3 Results) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| On DROP [DWD+19], a dataset testing discrete reasoning and numeracy in the context of reading comprehension, GPT-3 in a few-shot setting outperforms the fine-tuned ... | comparison identity and matched condition | p. 18 (3 Results) |
| SuperGLUE BoolQ CB CB COPA RTE Average Accuracy Accuracy F1 Accuracy Accuracy Fine-tuned SOTA 89.0 91.0 96.9 93.9 94.8 92.5 Fine-tuned BERT-Large 69.0 77.4 ... | comparison identity and matched condition | p. 19 (3 Results) |
| PIQA shows relatively shallow scaling with model size and is still over 10% worse than human performance, but GPT-3's few-shot and even zero-shot result ... | comparison identity and matched condition | p. 18 (3 Results) |
| Despite these weaknesses, GPT-3 still outperforms a fine-tuned BERT-large on four of eight tasks and on two tasks GPT-3 is close to the state-of-the-art ... | comparison identity and matched condition | p. 20 (3 Results) |
| Table 3.8: Performance of GPT-3 on SuperGLUE compared to fine-tuned baselines and SOTA. All results are reported on the test set. GPT-3 few-shot is ... | comparison identity and matched condition | p. 19 (Figure/Table caption) |
| GPT-3 2.7B outperforms the SOTA 17B parameter Turing-NLG [Tur20] in this setting, and GPT-3 175B advances the state of the art by 18%. | comparison identity and matched condition | p. 12 (3 Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 1.2: Larger models make increasingly efficient use of in-context information. We show in-context learning performance on a simple task requiring the model to ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Overall, we have made a best effort to measure and document the effects of data contamination, and to note or outright remove problematic results, ... | component/input/data sensitivity | p. 33 (3 Results) |
| Figure 1.2 illustrates the conditions we study, and shows few-shot learning of a simple task requiring the model to remove extraneous symbols from a ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Table 2.2: Datasets used to train GPT-3. "Weight in training mix" refers to the fraction of examples during training that are drawn from a ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| While it is common practice to train large models without investigating contamination, given the increasing scale of pretraining datasets, we believe this issue is ... | component/input/data sensitivity | p. 29 (3 Results) |
| For each benchmark, we produce a ‘clean' version which removes all potentially leaked examples, defined roughly as examples that have a 13-gram overlap with ... | component/input/data sensitivity | p. 31 (3 Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The panels above show four methods for performing a task with a language model - fine-tuning is the traditional method, whereas zero-, one-, and ... | GPT-3 significantly improves SOTA on LAMBADA while achieving respectable performance on two difficult completion prediction datasets. a[Tur20] b[RWC+19] c[LDL19] d[LCH+20] Figure 3.2: On LAMBADA, ... | PDF body cue; verify exact table/figure and matched conditions | p. 12 (3 Results), p. 16 (Figure/Table caption), p. 11 (3 Results), p. 13 (3 Results), p. 17 (3 Results), p. 5 (Figure/Table caption) |
| Primary metric/result | Figure 3.5: Zero-, one-, and few-shot performance on the adversarial Winogrande dataset as model capacity scales. Scaling is relatively smooth with the gains to ... | numeric claim only at cited anchor | p. 16 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 10 / 3 Results - extractive body cue:** For this graph we also include 6 additional extra-small models with as few as 100,000 parameters.
- **p. 11 / 3 Results - extractive body cue:** Our largest model sets a new SOTA on PTB by a substantial margin of 15 points, achieving a perplexity of 20.50.
- **p. 18 / 3 Results - extractive body cue:** On OpenBookQA [MCKS18], GPT-3 improves significantly from zero to few shot settings but is still over 20 points short of the overall SOTA.
- **p. 18 / 3 Results - extractive body cue:** GPT-3 performs best (within 3 points of the human baseline) on CoQA [RCM19] a free-form conversational dataset and performs worst (13 F1 below an ELMo ...
- **p. 20 / 3 Results - extractive body cue:** A value of K = 32 means that our model was shown 32 examples per task, for 256 examples total divided across the 8 tasks ...
- **p. 22 / 3 Results - extractive body cue:** In all 10 tasks the model must generate the correct answer exactly.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | An important limitation of our contamination analysis is that we cannot be sure that the clean subset is drawn from the same distribution as ... | p. 33 (3 Results) |
| body limitation/failure cue | Despite many limitations and weaknesses, these results suggest that very large language models may be an important ingredient in the development of adaptable, general ... | p. 41 (8 Conclusion) |
| body limitation/failure cue | 21 4 Measuring and Preventing Memorization Of Benchmarks 29 5 Limitations 33 6 Broader Impacts 34 6.1 Misuse of Language Models . . . ... | p. 2 (3 Results) |
| body limitation/failure cue | Figure 1.2: Larger models make increasingly efficient use of in-context information. We show in-context learning performance on a simple task requiring the model to ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | On COPA and ReCoRD GPT-3 achieves near-SOTA performance in the one-shot and few-shot settings, with COPA falling only a couple points short and achieving ... | p. 20 (3 Results) |
| body limitation/failure cue | This suggests that the model really does appear to learn these tasks at test time, as the model cannot perform them zero-shot and their ... | p. 24 (3 Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Model Name nparams nlayers dmodel nheads dhead Batch Size Learning Rate GPT-3 Small 125M 12 768 12 64 0.5M 6.0 × 10-4 GPT-3 Medium ... | p. 8 (2 Approach) |
| 2.3 Training Process As found in [KMH+20, MKAT18], larger models can typically use a larger batch size, but require a smaller learning rate. | p. 9 (2 Approach) |
| We also gradually increase the batch size linearly from a small value (32k tokens) to the full value over the first 4-12 billion tokens ... | p. 43 (B Details of Model Training) |
| To train all versions of GPT-3, we use Adam with β1 = 0.9, β2 = 0.95, and ϵ = 10-8, we clip the global ... | p. 43 (B Details of Model Training) |
| 43 C Details of Test Set Contamination Studies 43 D Total Compute Used to Train Language Models 46 E Human Quality Assessment of Synthetic ... | p. 2 (B Details of Model Training) |
| Larger values of K are usually but not always better, so when a separate development and test set are available, we experiment with a ... | p. 10 (2.4 Evaluation) |
| In this work we do not fine-tune GPT-3 because our focus is on task-agnostic performance, but GPT-3 can be fine-tuned in principle and this ... | p. 6 (2 Approach) |
| We measure the gradient noise scale during training and use it to guide our choice of batch size [MKAT18]. | p. 9 (2 Approach) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 33 / 3 Results - extractive body cue:** An important limitation of our contamination analysis is that we cannot be sure that the clean subset is drawn from the same distribution as the ...
- **p. 41 / 8 Conclusion - extractive body cue:** Despite many limitations and weaknesses, these results suggest that very large language models may be an important ingredient in the development of adaptable, general language ...
- **p. 2 / 3 Results - extractive body cue:** 21 4 Measuring and Preventing Memorization Of Benchmarks 29 5 Limitations 33 6 Broader Impacts 34 6.1 Misuse of Language Models . . . . ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1.2: Larger models make increasingly efficient use of in-context information. We show in-context learning performance on a simple task requiring the model to remove ...
- **p. 20 / 3 Results - extractive body cue:** On COPA and ReCoRD GPT-3 achieves near-SOTA performance in the one-shot and few-shot settings, with COPA falling only a couple points short and achieving second ...
- **p. 24 / 3 Results - extractive body cue:** This suggests that the model really does appear to learn these tasks at test time, as the model cannot perform them zero-shot and their artificial ...

- **Evidence anchors reviewed:** datasets p. 11 (3 Results), p. 29 (3 Results), p. 18 (3 Results), p. 33 (3 Results), p. 10 (2.4 Evaluation), p. 13 (3 Results), metrics p. 18 (3 Results), p. 10 (2.4 Evaluation), p. 12 (3 Results), p. 19 (3 Results), p. 26 (3 Results), p. 26 (3 Results), baselines p. 18 (3 Results), p. 19 (3 Results), p. 18 (3 Results), p. 20 (3 Results), p. 19 (Figure/Table caption), p. 12 (3 Results), results p. 12 (3 Results), p. 16 (Figure/Table caption), p. 11 (3 Results), p. 13 (3 Results), p. 17 (3 Results), p. 5 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
