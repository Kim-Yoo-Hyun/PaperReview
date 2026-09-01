# Evaluation - Flamingo: a Visual Language Model for Few-Shot Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (54 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2204.14198; PDF retrieval source: https://arxiv.org/pdf/2204.14198. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 3 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (3 Experiments), p. 5 (Figure/Table caption), p. 35 (Figure/Table caption)): Figure 2: Flamingo results overview. Left: Our largest model, dubbed Flamingo, outperforms state-of-the-art fine-tuned models on 6 of the 16 tasks we consider with no fine-tuning. For the 9 tasks ...

## Evaluation Body Digest

- **p. 7 / 3 Experiments - extractive PDF cue:** For the DEV benchmarks that are used both to validate design decisions and hyperparameters, as well as to report final performance, we therefore use four ...
- **p. 7 / 3 Experiments - extractive PDF cue:** To account for this, we report performance on an additional set of 11 benchmarks, spanning captioning, video question-answering, as well as some less commonly explored ...
- **p. 31 / Figure/Table caption - extractive PDF cue:** Table 6: Summary of the evaluation benchmarks. DEV benchmarks were used to validate general design decision of the Flamingo models. Gen. stands for generative task ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: Comparison to the state of the art. A single Flamingo model reaches the state of the art on a wide array of image ...
- **p. 7 / 3 Experiments - extractive PDF cue:** Performance estimates on the DEV benchmarks may be biased, as a result of model selection.
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2: Flamingo results overview. Left: Our largest model, dubbed Flamingo, outperforms state-of-the-art fine-tuned models on 6 of the 16 tasks we consider with no ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4: GATED XATTN-DENSE layers. To condition the LM on visual inputs, we insert new cross-attention layers between existing pretrained and frozen LM layers. The ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3: Ablation studies. Each row should be compared to the baseline Flamingo run (top row). Step time measures the time spent to perform gradient ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 논문이 정의한 robot/embodied environment.
- **Input boundary:** 논문이 명시한 observation과 task input.
- **Output/decision under evaluation:** paper-specific output/action.
- **Primary target:** primary task objective와 closed-loop behavior.
- **Detected evaluation headings:** 3 Experiments (p. 7); A.2 In-context few-shot evaluation details (p. 25); A.3 Training dataset details (p. 26); A.3.4 Dataset deduplication against evaluation tasks (p. 28); B Experiments (p. 28); B.1 Training and evaluation details (p. 28); B.1.4 Evaluation benchmarks (p. 30); Dataset (p. 31); B.1.5 Few-shot learning evaluation hyperparameters (p. 32); B.2 Additional performance results (p. 33); B.3.2 Dataset mixing strategies for the contrastive pretraining (p. 36); Dataset (p. 37).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 2: Flamingo results overview. Left: Our largest model, dubbed Flamingo, outperforms state-of-the-art fine-tuned models on 6 of the 16 tasks we consider with ... | p. 3 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 1: Comparison to the state of the art. A single Flamingo model reaches the state of the art on a wide array of ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 3: Ablation studies. Each row should be compared to the baseline Flamingo run (top row). Step time measures the time spent to perform ... | p. 8 (Figure/Table caption) |
| 3 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Flamingo outperforms by a large margin all previous zero-shot or few-shot methods on the 16 benchmarks considered. | p. 7 (3 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 4: GATED XATTN-DENSE layers. To condition the LM on visual inputs, we insert new cross-attention layers between existing pretrained and frozen LM layers. ... | p. 5 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 3 Experiments - extractive PDF cue:** For the DEV benchmarks that are used both to validate design decisions and hyperparameters, as well as to report final performance, we therefore use four ...
- **p. 7 / 3 Experiments - extractive PDF cue:** To account for this, we report performance on an additional set of 11 benchmarks, spanning captioning, video question-answering, as well as some less commonly explored ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Selected examples of inputs and outputs obtained from Flamingo-80B. Flamingo can rapidly adapt to various image/video understanding tasks with few-shot prompting (top). Out ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2: Flamingo results overview. Left: Our largest model, dubbed Flamingo, outperforms state-of-the-art fine-tuned models on 6 of the 16 tasks we consider with no ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3: Flamingo architecture overview. Flamingo is a family of visual language models (VLMs) that take as input visual data interleaved with text and produce ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4: GATED XATTN-DENSE layers. To condition the LM on visual inputs, we insert new cross-attention layers between existing pretrained and frozen LM layers. The ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: Comparison to the state of the art. A single Flamingo model reaches the state of the art on a wide array of image ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Comparison to SotA when fine-tuning Flamingo. We fine-tune Flamingo on all nine tasks where Flamingo does not achieve SotA with few-shot learning. Flamingo ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3: Ablation studies. Each row should be compared to the baseline Flamingo run (top row). Step time measures the time spent to perform gradient ...
- **p. 23 / Figure/Table caption - extractive PDF cue:** Figure 5: The Perceiver Resampler module maps a variable size grid of spatio-temporal visual features output by the Vision Encoder to a fixed number of ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For the DEV benchmarks that are used both to validate design decisions and hyperparameters, as well as to report final performance, we therefore use ... | embodiment, simulator version and control stack | p. 7 (3 Experiments), p. 7 (3 Experiments) |
| Task/environment | To account for this, we report performance on an additional set of 11 benchmarks, spanning captioning, video question-answering, as well as some less commonly ... | reset, timeout, object/scene variation | p. 7 (3 Experiments) |
| Observation/sensor | 논문이 명시한 observation과 task input | calibration, preprocessing, privileged input | p. 4 (2 Approach), p. 3 (1 Introduction) |
| Output/decision | paper-specific output/action | action frame, controller and termination | p. 5 (2 Approach), p. 5 (2 Approach) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 6: Summary of the evaluation benchmarks. DEV benchmarks were used to validate general design decision of the Flamingo models. Gen. stands for generative ... | definition/direction/unit from same section | p. 31 (Figure/Table caption) |
| Table 1: Comparison to the state of the art. A single Flamingo model reaches the state of the art on a wide array of ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Performance estimates on the DEV benchmarks may be biased, as a result of model selection. | definition/direction/unit from same section | p. 7 (3 Experiments) |
| Figure 2: Flamingo results overview. Left: Our largest model, dubbed Flamingo, outperforms state-of-the-art fine-tuned models on 6 of the 16 tasks we consider with ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 4: GATED XATTN-DENSE layers. To condition the LM on visual inputs, we insert new cross-attention layers between existing pretrained and frozen LM layers. ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Table 3: Ablation studies. Each row should be compared to the baseline Flamingo run (top row). Step time measures the time spent to perform ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 7: Interleaved visual data and text support. Given text interleaved with images/videos, e.g. coming from a webpage, we first process the text by ... | definition/direction/unit from same section | p. 24 (Figure/Table caption) |
| Figure 9: Training datasets. Mixture of training datasets of different formats. 𝑁corresponds to the number of visual inputs for a single example. For paired ... | definition/direction/unit from same section | p. 26 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 3: Ablation studies. Each row should be compared to the baseline Flamingo run (top row). Step time measures the time spent to perform ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Table 10: Additional ablation studies. Each row in this ablation study table should be compared to the baseline Flamingo run reported at the top ... | comparison identity and matched condition | p. 35 (Figure/Table caption) |
| Figure 2: Flamingo results overview. Left: Our largest model, dubbed Flamingo, outperforms state-of-the-art fine-tuned models on 6 of the 16 tasks we consider with ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| Table 9: Zero-shot contrastive pretraining evaluation. Zero-shot image-text retrieval evaluation of our pretrained contrastive model compared to the state-of-the-art dual encoder contrastive models. Ablated ... | comparison identity and matched condition | p. 35 (Figure/Table caption) |
| On six tasks, Flamingo even outperforms the fine-tuned SotA despite using a single set of model weights and only 32 task-specific examples. | comparison identity and matched condition | p. 7 (3 Experiments) |
| Flamingo outperforms by a large margin all previous zero-shot or few-shot methods on the 16 benchmarks considered. | comparison identity and matched condition | p. 7 (3 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 11: Effect of contrastive pretraining datasets and combination strategies. The first two rows show the effect of training a small model on LTIP ... | component/input/data sensitivity | p. 37 (Figure/Table caption) |
| An ablation study is given in Section 3.3. | component/input/data sensitivity | p. 7 (3 Experiments) |
| Table 1: Comparison to the state of the art. A single Flamingo model reaches the state of the art on a wide array of ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Table 10. We ablate the size of our Resampler with three options: Small, Medium (default value for all Flamingo models), and Large. We see ... | component/input/data sensitivity | p. 35 (Figure/Table caption) |
| Figure 3: Flamingo architecture overview. Flamingo is a family of visual language models (VLMs) that take as input visual data interleaved with text and ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Table 3: Ablation studies. Each row should be compared to the baseline Flamingo run (top row). Step time measures the time spent to perform ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are the following: (i) We introduce the Flamingo family of VLMs which can perform various multimodal tasks (such as captioning, ... | Figure 2: Flamingo results overview. Left: Our largest model, dubbed Flamingo, outperforms state-of-the-art fine-tuned models on 6 of the 16 tasks we consider with ... | PDF body cue; verify exact table/figure and matched conditions | p. 3 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (3 Experiments), p. 5 (Figure/Table caption), p. 35 (Figure/Table caption) |
| Primary metric/result | Table 1: Comparison to the state of the art. A single Flamingo model reaches the state of the art on a wide array of ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 7 / 3 Experiments - extractive PDF cue:** On six tasks, Flamingo even outperforms the fine-tuned SotA despite using a single set of model weights and only 32 task-specific examples.
- **p. 5 / 2 Approach - extractive PDF cue:** For video inputs, frames are sampled at 1 FPS and encoded independently to obtain a 3D spatio-temporal grid of features to which learned temporal embeddings ...
- **p. 6 / 2 Approach - extractive PDF cue:** From each document, we sample a random subsequence of 𝐿= 256 tokens and take up to the first 𝑁= 5 images included in the sampled ...
- **p. 6 / 2 Approach - extractive PDF cue:** 2.5 Task adaptation with few-shot in-context learning Once Flamingo is trained, we use it to tackle a visual task by conditioning it on a multimodal ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 13: Hallucinations and ungrounded guesses in open-ended visual question answering. Left: The model occasionally hallucinates by producing answers that seem likely given the ... | p. 42 (Figure/Table caption) |
| body limitation/failure cue | We discuss the limitations of our work in more depth in Appendix D.1. | p. 10 (5 Discussion) |
| body limitation/failure cue | Figure 9: Training datasets. Mixture of training datasets of different formats. 𝑁corresponds to the number of visual inputs for a single example. For paired ... | p. 26 (Figure/Table caption) |
| body limitation/failure cue | Table 10. We ablate the size of our Resampler with three options: Small, Medium (default value for all Flamingo models), and Large. We see ... | p. 35 (Figure/Table caption) |
| body limitation/failure cue | Table 2: Comparison to SotA when fine-tuning Flamingo. We fine-tune Flamingo on all nine tasks where Flamingo does not achieve SotA with few-shot learning. ... | p. 8 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We keep all evaluation hyperparameters fixed across all benchmarks. | p. 7 (3 Experiments) |
| For the DEV benchmarks that are used both to validate design decisions and hyperparameters, as well as to report final performance, we therefore use ... | p. 7 (3 Experiments) |
| Note that we use smaller batch sizes and a shorter training schedule compared to the final models. | p. 8 (Method) |
| In short, we do so by fine-tuning the model on a short schedule with a small learning rate by additionally unfreezing the vision backbone ... | p. 8 (Method) |
| First, the Perceiver Resampler (Section 2.1) receives spatio-temporal features from the Vision Encoder (obtained from either an image or a video) and outputs a ... | p. 4 (2 Approach) |
| This module connects the vision encoder to the frozen language model as shown in Figure 3. | p. 5 (2 Approach) |
| We provide an illustration, more architectural details, and pseudo-code in Appendix A.1.1. | p. 5 (2 Approach) |
| Further images are discarded in order to save compute. | p. 6 (2 Approach) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 42 / Figure/Table caption - extractive PDF cue:** Figure 13: Hallucinations and ungrounded guesses in open-ended visual question answering. Left: The model occasionally hallucinates by producing answers that seem likely given the text ...
- **p. 10 / 5 Discussion - extractive PDF cue:** We discuss the limitations of our work in more depth in Appendix D.1.
- **p. 26 / Figure/Table caption - extractive PDF cue:** Figure 9: Training datasets. Mixture of training datasets of different formats. 𝑁corresponds to the number of visual inputs for a single example. For paired image ...
- **p. 35 / Figure/Table caption - extractive PDF cue:** Table 10. We ablate the size of our Resampler with three options: Small, Medium (default value for all Flamingo models), and Large. We see that ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Comparison to SotA when fine-tuning Flamingo. We fine-tune Flamingo on all nine tasks where Flamingo does not achieve SotA with few-shot learning. Flamingo ...

- **PDF anchors reviewed:** datasets p. 7 (3 Experiments), p. 7 (3 Experiments), metrics p. 31 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (3 Experiments), p. 3 (Figure/Table caption), p. 5 (Figure/Table caption), p. 8 (Figure/Table caption), baselines p. 8 (Figure/Table caption), p. 35 (Figure/Table caption), p. 3 (Figure/Table caption), p. 35 (Figure/Table caption), p. 7 (3 Experiments), p. 7 (3 Experiments), results p. 3 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (3 Experiments), p. 5 (Figure/Table caption), p. 35 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
