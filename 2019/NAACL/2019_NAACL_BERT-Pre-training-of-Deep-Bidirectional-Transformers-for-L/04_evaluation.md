# Evaluation - BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1810.04805; PDF retrieval source: https://arxiv.org/pdf/1810.04805. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 6 (4 Experiments), p. 5 (4 Experiments), p. 7 (4 Experiments)): Both BERTBASE and BERTLARGE outperform all systems on all tasks by a substantial margin, obtaining 4.5% and 7.0% respective average accuracy improvement over the prior state of the art.

## Evaluation Body Digest

- **p. 5 / 4 Experiments - extractive PDF cue:** 4.1 GLUE The General Language Understanding Evaluation (GLUE) benchmark (Wang et al., 2018a) is a collection of diverse natural language understanding tasks.
- **p. 8 / 4 Experiments - extractive PDF cue:** We can see that larger models lead to a strict accuracy improvement across all four datasets, even for MRPC which only has 3,600 labeled training ...
- **p. 5 / 4 Experiments - extractive PDF cue:** Detailed descriptions of GLUE datasets are included in Appendix B.1.
- **p. 6 / 4 Experiments - extractive PDF cue:** 4.2 SQuAD v1.1 The Stanford Question Answering Dataset (SQuAD v1.1) is a collection of 100k crowdsourced question/answer pairs (Rajpurkar et al., 2016).
- **p. 6 / 4 Experiments - extractive PDF cue:** Additionally, for BERTLARGE we found that finetuning was sometimes unstable on small datasets, so we ran several random restarts and selected the best model on ...
- **p. 7 / 4 Experiments - extractive PDF cue:** When fine-tuning on the SWAG dataset, we construct four input sequences, each containing the concatenation of the given sentence (sentence A) and a possible continuation ...
- **p. 7 / 4 Experiments - extractive PDF cue:** 4.4 SWAG The Situations With Adversarial Generations (SWAG) dataset contains 113k sentence-pair completion examples that evaluate grounded commonsense inference (Zellers et al., 2018).
- **p. 8 / 4 Experiments - extractive PDF cue:** This is directly comparable to OpenAI GPT, but using our larger training dataset, our input representation, and our fine-tuning scheme.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 논문이 정의한 robot/embodied environment.
- **Input boundary:** 논문이 명시한 observation과 task input.
- **Output/decision under evaluation:** paper-specific output/action.
- **Primary target:** primary task objective와 closed-loop behavior.
- **Detected evaluation headings:** 4 Experiments (p. 5); B Detailed Experimental Setup (p. 14).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Both BERTBASE and BERTLARGE outperform all systems on all tasks by a substantial margin, obtaining 4.5% and 7.0% respective average accuracy improvement over the ... | p. 6 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | This does significantly improve results on SQuAD, but the results are still far worse than those of the pretrained bidirectional models. | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | It is also perhaps surprising that we are able to achieve such significant improvements on top of models which are already quite large relative ... | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | We find that BERTLARGE significantly outperforms BERTBASE across all tasks, especially those with very little training data. | p. 6 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 7For example, the BERT SQuAD model can be trained in around 30 minutes on a single Cloud TPU to achieve a Dev F1 score ... | p. 5 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 5 / 4 Experiments - extractive PDF cue:** 4.1 GLUE The General Language Understanding Evaluation (GLUE) benchmark (Wang et al., 2018a) is a collection of diverse natural language understanding tasks.
- **p. 8 / 4 Experiments - extractive PDF cue:** We can see that larger models lead to a strict accuracy improvement across all four datasets, even for MRPC which only has 3,600 labeled training ...
- **p. 5 / 4 Experiments - extractive PDF cue:** Detailed descriptions of GLUE datasets are included in Appendix B.1.
- **p. 6 / 4 Experiments - extractive PDF cue:** 4.2 SQuAD v1.1 The Stanford Question Answering Dataset (SQuAD v1.1) is a collection of 100k crowdsourced question/answer pairs (Rajpurkar et al., 2016).
- **p. 6 / 4 Experiments - extractive PDF cue:** Additionally, for BERTLARGE we found that finetuning was sometimes unstable on small datasets, so we ran several random restarts and selected the best model on ...
- **p. 7 / 4 Experiments - extractive PDF cue:** When fine-tuning on the SWAG dataset, we construct four input sequences, each containing the concatenation of the given sentence (sentence A) and a possible continuation ...
- **p. 7 / 4 Experiments - extractive PDF cue:** 4.4 SWAG The Situations With Adversarial Generations (SWAG) dataset contains 113k sentence-pair completion examples that evaluate grounded commonsense inference (Zellers et al., 2018).
- **p. 8 / 4 Experiments - extractive PDF cue:** This is directly comparable to OpenAI GPT, but using our larger training dataset, our input representation, and our fine-tuning scheme.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 1: Overall pre-training and fine-tuning procedures for BERT. Apart from output layers, the same architec- tures are used in both pre-training and fine-tuning. The ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 2: BERT input representation. The input embeddings are the sum of the token embeddings, the segmenta- tion embeddings and the position embeddings. The NSP ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1: GLUE Test results, scored by the evaluation server (https://gluebenchmark.com/leaderboard). The number below each task denotes the number of training examples. The "Average" column ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2: SQuAD 1.1 results. The BERT ensemble is 7x systems which use different pre-training check- points and fine-tuning seeds. System Dev Test EM
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3: SQuAD 2.0 results. We exclude entries that use BERT as one of their components. tuning data, we only lose 0.1-0.4 F1, still outper- ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4: SWAG Dev and Test accuracies. †Human per- formance is measured with 100 samples, as reported in the SWAG paper. ˆ si,j = maxj≥iS·Ti ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 5: Ablation over the pre-training tasks using the BERTBASE architecture. "No NSP" is trained without the next sentence prediction task. "LTR & No NSP" ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 6. In this table, we report the average Dev Set accuracy from 5 random restarts of fine-tuning. We can see that larger models lead ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 4.1 GLUE The General Language Understanding Evaluation (GLUE) benchmark (Wang et al., 2018a) is a collection of diverse natural language understanding tasks. | embodiment, simulator version and control stack | p. 5 (4 Experiments), p. 8 (4 Experiments) |
| Task/environment | We can see that larger models lead to a strict accuracy improvement across all four datasets, even for MRPC which only has 3,600 labeled ... | reset, timeout, object/scene variation | p. 8 (4 Experiments), p. 5 (4 Experiments) |
| Observation/sensor | 논문이 명시한 observation과 task input | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 4 (C T1) |
| Output/decision | paper-specific output/action | action frame, controller and termination | p. 5 (C T1), p. 5 (C T1) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| F1 scores are reported for QQP and MRPC, Spearman correlations are reported for STS-B, and accuracy scores are reported for the other tasks. | definition/direction/unit from same section | p. 6 (4 Experiments) |
| 7For example, the BERT SQuAD model can be trained in around 30 minutes on a single Cloud TPU to achieve a Dev F1 score ... | definition/direction/unit from same section | p. 5 (4 Experiments) |
| In fact, our single BERT model outperforms the top ensemble system in terms of F1 score. | definition/direction/unit from same section | p. 6 (4 Experiments) |
| The only task-specific parameters introduced is a vector whose dot product with the [CLS] token representation C denotes a score for each choice which ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| For prediction, we compare the score of the no-answer span: snull = S·C + E·C to the score of the best non-null span 12The ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| In this table, we report the average Dev Set accuracy from 5 random restarts of fine-tuning. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| 5.2 Effect of Model Size In this section, we explore the effect of model size on fine-tuning task accuracy. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| The reported Dev and Test scores are averaged over 5 random restarts using those hyperparameters. layer in the output. | definition/direction/unit from same section | p. 9 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| BERTLARGE outperforms the authors' baseline ESIM+ELMo system by +27.1% and OpenAI GPT by 8.3%. | comparison identity and matched condition | p. 7 (4 Experiments) |
| In fact, our single BERT model outperforms the top ensemble system in terms of F1 score. | comparison identity and matched condition | p. 6 (4 Experiments) |
| Our best performing system outperforms the top leaderboard system by +1.5 F1 in ensembling and +1.3 F1 as a single system. | comparison identity and matched condition | p. 6 (4 Experiments) |
| The results compared to prior leaderboard entries and top published work (Sun et al., 2018; Wang et al., 2018b) are shown in Table 3, ... | comparison identity and matched condition | p. 7 (4 Experiments) |
| BERTLARGE performs competitively with state-of-the-art methods. | comparison identity and matched condition | p. 9 (4 Experiments) |
| Dev Set Tasks MNLI-m QNLI MRPC SST-2 SQuAD (Acc) (Acc) (Acc) (Acc) (F1) BERTBASE 84.4 88.4 86.7 92.7 88.5 No NSP 83.9 84.9 86.5 ... | comparison identity and matched condition | p. 8 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 5.1 Effect of Pre-training Tasks We demonstrate the importance of the deep bidirectionality of BERT by evaluating two pretraining objectives using exactly the same ... | component/input/data sensitivity | p. 8 (4 Experiments) |
| Dev Set Tasks MNLI-m QNLI MRPC SST-2 SQuAD (Acc) (Acc) (Acc) (Acc) (F1) BERTBASE 84.4 88.4 86.7 92.7 88.5 No NSP 83.9 84.9 86.5 ... | component/input/data sensitivity | p. 8 (4 Experiments) |
| To ablate the fine-tuning approach, we apply the feature-based approach by extracting the activations from one or more layers without fine-tuning any parameters of ... | component/input/data sensitivity | p. 9 (4 Experiments) |
| The effect of model size is explored more thoroughly in Section 5.2. | component/input/data sensitivity | p. 6 (4 Experiments) |
| Without TriviaQA fine11QANet is described in Yu et al. | component/input/data sensitivity | p. 6 (4 Experiments) |
| 5 Ablation Studies In this section, we perform ablation experiments over a number of facets of BERT in order to better understand their relative ... | component/input/data sensitivity | p. 7 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Unlike left-toright language model pre-training, the MLM objective enables the representation to fuse the left and the right context, which allows us to pretrain ... | Both BERTBASE and BERTLARGE outperform all systems on all tasks by a substantial margin, obtaining 4.5% and 7.0% respective average accuracy improvement over the ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 6 (4 Experiments), p. 5 (4 Experiments), p. 7 (4 Experiments) |
| Primary metric/result | This does significantly improve results on SQuAD, but the results are still far worse than those of the pretrained bidirectional models. | numeric claim only at cited anchor | p. 8 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 6 / 4 Experiments - extractive PDF cue:** We use a batch size of 32 and fine-tune for 3 epochs over the data for all GLUE tasks.
- **p. 6 / 4 Experiments - extractive PDF cue:** We fine-tune for 3 epochs with a learning rate of 5e-5 and a batch size of 32.
- **p. 7 / 4 Experiments - extractive PDF cue:** The BERT ensemble is 7x systems which use different pre-training checkpoints and fine-tuning seeds.
- **p. 7 / 4 Experiments - extractive PDF cue:** We exclude entries that use BERT as one of their components. tuning data, we only lose 0.1-0.4 F1, still outperforming all existing systems by a ...
- **p. 7 / 4 Experiments - extractive PDF cue:** For prediction, we compare the score of the no-answer span: snull = S·C + E·C to the score of the best non-null span 12The TriviaQA ...
- **p. 7 / 4 Experiments - extractive PDF cue:** System Dev Test ESIM+GloVe 51.9 52.7 ESIM+ELMo 59.1 59.2 OpenAI GPT - 78.0 BERTBASE 81.6 - BERTLARGE 86.6 86.3 Human (expert)† - 85.0 Human (5 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Additionally, for BERTLARGE we found that finetuning was sometimes unstable on small datasets, so we ran several random restarts and selected the best model ... | p. 6 (4 Experiments) |
| body limitation/failure cue | Given a question and a passage from 9The GLUE data set distribution does not include the Test labels, and we only made a single ... | p. 6 (4 Experiments) |
| body limitation/failure cue | The left-only constraint was also applied at fine-tuning, because removing it introduced a pre-train/fine-tune mismatch that degraded downstream performance. | p. 8 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We fine-tune for 3 epochs with a learning rate of 5e-5 and a batch size of 32. | p. 6 (4 Experiments) |
| We use a batch size of 32 and fine-tune for 3 epochs over the data for all GLUE tasks. | p. 6 (4 Experiments) |
| The BERT ensemble is 7x systems which use different pre-training checkpoints and fine-tuning seeds. | p. 7 (4 Experiments) |
| Second, there are major computational benefits to pre-compute an expensive representation of the training data once and then run many experiments with cheaper models ... | p. 9 (4 Experiments) |
| We compute a standard classification loss with C and W, i.e., log(softmax(CW T )). | p. 5 (4 Experiments) |
| (2017) is (L=6, H=1024, A=16) with 100M parameters for the encoder, and the largest Transformer we have found in the literature is (L=64, H=512, ... | p. 8 (4 Experiments) |
| We trained a number of BERT models with a differing number of layers, hidden units, and attention heads, while otherwise using the same hyperparameters ... | p. 8 (4 Experiments) |
| Hyperparameters were selected using the Dev set. | p. 9 (4 Experiments) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4 Experiments - extractive PDF cue:** Additionally, for BERTLARGE we found that finetuning was sometimes unstable on small datasets, so we ran several random restarts and selected the best model on ...
- **p. 6 / 4 Experiments - extractive PDF cue:** Given a question and a passage from 9The GLUE data set distribution does not include the Test labels, and we only made a single GLUE ...
- **p. 8 / 4 Experiments - extractive PDF cue:** The left-only constraint was also applied at fine-tuning, because removing it introduced a pre-train/fine-tune mismatch that degraded downstream performance.

- **PDF anchors reviewed:** datasets p. 5 (4 Experiments), p. 8 (4 Experiments), p. 5 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), metrics p. 6 (4 Experiments), p. 5 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), baselines p. 7 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments), results p. 6 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 6 (4 Experiments), p. 5 (4 Experiments), p. 7 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
