# Evaluation - Attention Is All You Need

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1706.03762; PDF retrieval source: https://arxiv.org/pdf/1706.03762. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (6 Results), p. 8 (6 Results), p. 9 (6 Results), p. 9 (6 Results), p. 10 (Figure/Table caption)): On the WMT 2014 English-to-French translation task, our big model achieves a BLEU score of 41.0, outperforming all of the previously published single models, at less than 1/4 the training ...

## Evaluation Body Digest

- **p. 8 / 6 Results - extractive body cue:** On the WMT 2014 English-to-French translation task, our big model achieves a BLEU score of 41.0, outperforming all of the previously published single models, at ...
- **p. 8 / 6 Results - extractive body cue:** 6.1 Machine Translation On the WMT 2014 English-to-German translation task, the big transformer model (Transformer (big) in Table 2) outperforms the best previously reported models ...
- **p. 9 / 6 Results - extractive body cue:** This task presents specific challenges: the output is subject to strong structural constraints and is significantly longer than the input.
- **p. 9 / 6 Results - extractive body cue:** 6.3 English Constituency Parsing To evaluate if the Transformer can generalize to other tasks we performed experiments on English constituency parsing.
- **p. 9 / 6 Results - extractive body cue:** While single-head attention is 0.9 BLEU worse than the best setting, quality also drops off with too many heads.
- **p. 9 / 6 Results - extractive body cue:** We also trained it in a semi-supervised setting, using the larger high-confidence and BerkleyParser corpora from with approximately 17M sentences [37].
- **p. 10 / Figure/Table caption - extractive body cue:** Table 4: The Transformer generalizes well to English constituency parsing (Results are on Section 23 of WSJ) Parser Training WSJ 23 F1 Vinyals & Kaiser ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 3: An example of the attention mechanism following long-distance dependencies in the encoder self-attention in layer 5 of 6. Many of the attention heads ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 논문이 정의한 robot/embodied environment.
- **Input boundary:** 논문이 명시한 observation과 task input.
- **Output/decision under evaluation:** paper-specific output/action.
- **Primary target:** primary task objective와 closed-loop behavior.
- **Detected evaluation headings:** 6 Results (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 6 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | On the WMT 2014 English-to-French translation task, our big model achieves a BLEU score of 41.0, outperforming all of the previously published single models, ... | p. 8 (6 Results) |
| 6 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | 6.1 Machine Translation On the WMT 2014 English-to-German translation task, the big transformer model (Transformer (big) in Table 2) outperforms the best previously reported ... | p. 8 (6 Results) |
| 6 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | We present these results in Table 3. | p. 9 (6 Results) |
| 6 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Furthermore, RNN sequence-to-sequence models have not been able to attain state-of-the-art results in small-data regimes [37]. | p. 9 (6 Results) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 4: The Transformer generalizes well to English constituency parsing (Results are on Section 23 of WSJ) Parser Training WSJ 23 F1 Vinyals & ... | p. 10 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / 6 Results - extractive body cue:** On the WMT 2014 English-to-French translation task, our big model achieves a BLEU score of 41.0, outperforming all of the previously published single models, at ...
- **p. 8 / 6 Results - extractive body cue:** 6.1 Machine Translation On the WMT 2014 English-to-German translation task, the big transformer model (Transformer (big) in Table 2) outperforms the best previously reported models ...
- **p. 9 / 6 Results - extractive body cue:** This task presents specific challenges: the output is subject to strong structural constraints and is significantly longer than the input.
- **p. 9 / 6 Results - extractive body cue:** 6.3 English Constituency Parsing To evaluate if the Transformer can generalize to other tasks we performed experiments on English constituency parsing.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1: The Transformer - model architecture. The Transformer follows this overall architecture using stacked self-attention and point-wise, fully connected layers for both the encoder ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: (left) Scaled Dot-Product Attention. (right) Multi-Head Attention consists of several attention layers running in parallel. of the values, where the weight assigned to ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Maximum path lengths, per-layer complexity and minimum number of sequential operations for different layer types. n is the sequence length, d is the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: The Transformer achieves better BLEU scores than previous state-of-the-art models on the English-to-German and English-to-French newstest2014 tests at a fraction of the training ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Variations on the Transformer architecture. Unlisted values are identical to those of the base model. All metrics are on the English-to-German translation development ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 4: The Transformer generalizes well to English constituency parsing (Results are on Section 23 of WSJ) Parser Training WSJ 23 F1 Vinyals & Kaiser ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 3: An example of the attention mechanism following long-distance dependencies in the encoder self-attention in layer 5 of 6. Many of the attention heads ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 4: Two attention heads, also in layer 5 of 6, apparently involved in anaphora resolution. Top: Full attentions for head 5. Bottom: Isolated attentions ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | On the WMT 2014 English-to-French translation task, our big model achieves a BLEU score of 41.0, outperforming all of the previously published single models, ... | embodiment, simulator version and control stack | p. 8 (6 Results), p. 8 (6 Results) |
| Task/environment | 6.1 Machine Translation On the WMT 2014 English-to-German translation task, the big transformer model (Transformer (big) in Table 2) outperforms the best previously reported ... | reset, timeout, object/scene variation | p. 8 (6 Results), p. 9 (6 Results) |
| Observation/sensor | 논문이 명시한 observation과 task input | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 2 (2 Background) |
| Output/decision | paper-specific output/action | action frame, controller and termination | p. 6 (2 Background), p. 1 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| On the WMT 2014 English-to-French translation task, our big model achieves a BLEU score of 41.0, outperforming all of the previously published single models, ... | definition/direction/unit from same section | p. 8 (6 Results) |
| 6.1 Machine Translation On the WMT 2014 English-to-German translation task, the big transformer model (Transformer (big) in Table 2) outperforms the best previously reported ... | definition/direction/unit from same section | p. 8 (6 Results) |
| While single-head attention is 0.9 BLEU worse than the best setting, quality also drops off with too many heads. | definition/direction/unit from same section | p. 9 (6 Results) |
| We also trained it in a semi-supervised setting, using the larger high-confidence and BerkleyParser corpora from with approximately 17M sentences [37]. | definition/direction/unit from same section | p. 9 (6 Results) |
| Table 4: The Transformer generalizes well to English constituency parsing (Results are on Section 23 of WSJ) Parser Training WSJ 23 F1 Vinyals & ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| Figure 3: An example of the attention mechanism following long-distance dependencies in the encoder self-attention in layer 5 of 6. Many of the attention ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| On the WMT 2014 English-to-French translation task, our big model achieves a BLEU score of 41.0, outperforming all of the previously published single models, ... | comparison identity and matched condition | p. 8 (6 Results) |
| 6.1 Machine Translation On the WMT 2014 English-to-German translation task, the big transformer model (Transformer (big) in Table 2) outperforms the best previously reported ... | comparison identity and matched condition | p. 8 (6 Results) |
| Furthermore, RNN sequence-to-sequence models have not been able to attain state-of-the-art results in small-data regimes [37]. | comparison identity and matched condition | p. 9 (6 Results) |
| Listed perplexities are per-wordpiece, according to our byte-pair encoding, and should not be compared to per-word perplexities. | comparison identity and matched condition | p. 9 (6 Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 6.2 Model Variations To evaluate the importance of different components of the Transformer, we varied our base model in different ways, measuring the change ... | component/input/data sensitivity | p. 8 (6 Results) |
| In row (E) we replace our sinusoidal positional encoding with learned positional embeddings [9], and observe nearly identical results to the base model. | component/input/data sensitivity | p. 9 (6 Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work we propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies ... | On the WMT 2014 English-to-French translation task, our big model achieves a BLEU score of 41.0, outperforming all of the previously published single models, ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (6 Results), p. 8 (6 Results), p. 9 (6 Results), p. 9 (6 Results), p. 10 (Figure/Table caption) |
| Primary metric/result | 6.1 Machine Translation On the WMT 2014 English-to-German translation task, the big transformer model (Transformer (big) in Table 2) outperforms the best previously reported ... | numeric claim only at cited anchor | p. 8 (6 Results) |

- Numeric sentences retained from the body:
- **p. 3 / 2 Background - extractive body cue:** 3.1 Encoder and Decoder Stacks Encoder: The encoder is composed of a stack of N = 6 identical layers.
- **p. 3 / 2 Background - extractive body cue:** Decoder: The decoder is also composed of a stack of N = 6 identical layers.
- **p. 7 / 2 Background - extractive body cue:** Sentences were encoded using byte-pair encoding [3], which has a shared sourcetarget vocabulary of about 37000 tokens.
- **p. 7 / 2 Background - extractive body cue:** We trained the base models for a total of 100,000 steps or 12 hours.
- **p. 7 / 2 Background - extractive body cue:** The big models were trained for 300,000 steps (3.5 days).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We plan to investigate this approach further in future work. | p. 7 (2 Background) |
| body limitation/failure cue | A single convolutional layer with kernel width k < n does not connect all pairs of input and output positions. | p. 7 (2 Background) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We varied the learning rate over the course of training, according to the formula: lrate = d-0.5 model · min(step_num-0.5, step_num · warmup_steps-1.5) (3) ... | p. 7 (2 Background) |
| We estimate the number of floating point operations used to train a model by multiplying the training time, the number of GPUs used, and ... | p. 8 (6 Results) |
| We performed only a small number of experiments to select the dropout, both attention and residual (section 5.4), learning rates and beam size on ... | p. 9 (6 Results) |
| The best performing models also connect the encoder and decoder through an attention mechanism. | p. 1 (Abstract) |
| Niki designed, implemented, tuned and evaluated countless model variants in our original codebase and tensor2tensor. | p. 1 (Abstract) |
| Given z, the decoder then generates an output sequence (y1, ..., ym) of symbols one element at a time. | p. 2 (2 Background) |
| 3 Model Architecture Most competitive neural sequence transduction models have an encoder-decoder structure [5, 2, 35]. | p. 2 (2 Background) |
| The output is computed as a weighted sum 3 | p. 3 (2 Background) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 2 Background - extractive body cue:** We plan to investigate this approach further in future work.
- **p. 7 / 2 Background - extractive body cue:** A single convolutional layer with kernel width k < n does not connect all pairs of input and output positions.

- **Evidence anchors reviewed:** datasets p. 8 (6 Results), p. 8 (6 Results), p. 9 (6 Results), p. 9 (6 Results), metrics p. 8 (6 Results), p. 8 (6 Results), p. 9 (6 Results), p. 9 (6 Results), p. 10 (Figure/Table caption), p. 13 (Figure/Table caption), baselines p. 8 (6 Results), p. 8 (6 Results), p. 9 (6 Results), p. 9 (6 Results), results p. 8 (6 Results), p. 8 (6 Results), p. 9 (6 Results), p. 9 (6 Results), p. 10 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
