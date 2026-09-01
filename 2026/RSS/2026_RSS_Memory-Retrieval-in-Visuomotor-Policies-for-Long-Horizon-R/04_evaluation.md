# Evaluation - Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://roboticsconference.org/program/papers/10/; PDF retrieval source: https://roboticsconference.org/program/papers/10/. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS)): Cotraining VQA and action prediction achieves 64% success, outperforming pretrain-then-finetune (44%) and no-VQA training (42%) by 20 and 22 points, respectively.

## Evaluation Body Digest

- **p. 7 / IV. EXPERIMENTS - extractive body cue:** In addition, we measure manipulation and memory failures in real-world evaluations, finding that HALO reduces them by 8% and 25% absolute over full attention in ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Average (Spatial Info.) (Relational Info.) (Numerical Info.) (Event-time Info.) Standard Transformer 0.26 0.23 0.12 0.27 0.22 Scene Memory Transformer 0.53 0.25 0.17 0.40 0.34 SAM2Act++ ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Across episodes, the involved objects and their relations vary.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Store N objects (Spatial information, Human-robot collaboration).
- **p. 8 / IV. EXPERIMENTS - extractive body cue:** Adding VLMinduced priors improves average success by 10%, suggesting that VQA supervision helps the policy identify relevant history, particularly in tasks that require recalling past ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** We evaluate our approach on long-horizon manipulation tasks that require retrieving diverse information types-spatial,
- **p. 8 / IV. EXPERIMENTS - extractive body cue:** The sparsification methods relying on fixed access patterns may miss task-relevant events occurring at unpredictable times.
- **p. 8 / IV. EXPERIMENTS - extractive body cue:** A moderate value (k = 8) achieves the best performance (52% success).

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Cotraining VQA and action prediction achieves 64% success, outperforming pretrain-then-finetune (44%) and no-VQA training (42%) by 20 and 22 points, respectively. | p. 8 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Compared to hand-designed features, HALO achieves an absolute improvement of 12%. | p. 7 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | A moderate value (k = 8) achieves the best performance (52% success). | p. 8 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Compared to SAM2Act++, HALO improves average task success by 21% points. | p. 7 (IV. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 7 / IV. EXPERIMENTS - extractive body cue:** In addition, we measure manipulation and memory failures in real-world evaluations, finding that HALO reduces them by 8% and 25% absolute over full attention in ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Average (Spatial Info.) (Relational Info.) (Numerical Info.) (Event-time Info.) Standard Transformer 0.26 0.23 0.12 0.27 0.22 Scene Memory Transformer 0.53 0.25 0.17 0.40 0.34 SAM2Act++ ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Across episodes, the involved objects and their relations vary.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Store N objects (Spatial information, Human-robot collaboration).
- **p. 8 / IV. EXPERIMENTS - extractive body cue:** Adding VLMinduced priors improves average success by 10%, suggesting that VQA supervision helps the policy identify relevant history, particularly in tasks that require recalling past ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** We evaluate our approach on long-horizon manipulation tasks that require retrieving diverse information types-spatial,
- **p. 8 / IV. EXPERIMENTS - extractive body cue:** The sparsification methods relying on fixed access patterns may miss task-relevant events occurring at unpredictable times.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Memory retrieval in visuomotor policy learning. Long-horizon household tasks require robots to act on information no longer present in the current sensory input. ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2. HALO learns to retrieve diverse forms of task-relevant information from history, guided by priors distilled from vision-language foundation models. observations can amplify this ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. Overview. HALO learns a visuomotor policy that retrieves information from the past observations and actions to predict low-level robot actions (middle), guided by ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4. Overview of video question-answer generation for knowledge distillation. Images are first converted to text using a grounded vision model, and trajectories are summarized ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5. Visualization of real-world tasks. We evaluate HALO in four stationary and mobile manipulation tasks, including a human-robot collaborative task (rows) with strong partial ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In addition, we measure manipulation and memory failures in real-world evaluations, finding that HALO reduces them by 8% and 25% absolute over full attention ... | embodiment, simulator version and control stack | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Task/environment | Average (Spatial Info.) (Relational Info.) (Numerical Info.) (Event-time Info.) Standard Transformer 0.26 0.23 0.12 0.27 0.22 Scene Memory Transformer 0.53 0.25 0.17 0.40 0.34 ... | reset, timeout, object/scene variation | p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 3 (III. HALO), p. 3 (III. HALO) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 4 (III. HALO), p. 4 (III. HALO) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| A moderate value (k = 8) achieves the best performance (52% success). | definition/direction/unit from same section | p. 8 (IV. EXPERIMENTS) |
| Smaller k (e.g., k = 4, 40% success) omits useful context, while larger k incorporates irrelevant history (48% for k = 12, 33% for ... | definition/direction/unit from same section | p. 8 (IV. EXPERIMENTS) |
| Return to Same Container (Object relations). | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| ReMemBer [18] stores text summaries of past observations generated by a VLM. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| Compared to SAM2Act++, HALO improves average task success by 21% points. | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| Text summaries generated by VLM often capture coarse semantic information, but may omit details needed for control. | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| Fig. 1. Memory retrieval in visuomotor policy learning. Long-horizon household tasks require robots to act on information no longer present in the current sensory ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 3. Overview. HALO learns a visuomotor policy that retrieves information from the past observations and actions to predict low-level robot actions (middle), guided ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| (Table II) We observe a similar trend in real-world settings, where HALO consistently outperforms the standard Transformer baseline by 19%. | comparison identity and matched condition | p. 7 (IV. EXPERIMENTS) |
| HALO outperforms ReMemBer by 23% points on average. | comparison identity and matched condition | p. 7 (IV. EXPERIMENTS) |
| HALO outperforms the best alternative, gated attention, by 11%. | comparison identity and matched condition | p. 8 (IV. EXPERIMENTS) |
| We compare HALO's stage-wise pipeline against a single-prompt baseline that generates QA pairs directly from long videos. | comparison identity and matched condition | p. 8 (IV. EXPERIMENTS) |
| Hand-designed Features uses human-designed rules to select which task-relevant features to store or discard, similar to prior work MemER [23]. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| With the goal of reducing memory size or introducing inductive priors about what should be stored, prior work proposes several alternatives: SAM2Act++ [5] uses ... | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We compare HALO against a variant trained without VQA supervision. | component/input/data sensitivity | p. 8 (IV. EXPERIMENTS) |
| The minimal gain from separate pretrain-then-finetune compared to no-VQA suggests that VQA knowledge is lost during fine-tuning, whereas co-training effectively shapes retrieval toward task-relevant ... | component/input/data sensitivity | p. 8 (IV. EXPERIMENTS) |
| However, HALO remains competitive without task-specific assumptions or hand-designed rules, making it versatile with less engineering effort across information types. | component/input/data sensitivity | p. 7 (IV. EXPERIMENTS) |
| This suggests that learning what to retrieve directly from data using HALO not only removes manually designed task-specific priors but also improves performance, possibly ... | component/input/data sensitivity | p. 7 (IV. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address these challenges, we propose HALO: HistoryAware visuomotor policy for LOng-horizon robotic imitation learning. | Cotraining VQA and action prediction achieves 64% success, outperforming pretrain-then-finetune (44%) and no-VQA training (42%) by 20 and 22 points, respectively. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Primary metric/result | Compared to hand-designed features, HALO achieves an absolute improvement of 12%. | numeric claim only at cited anchor | p. 7 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Average (Spatial Info.) (Relational Info.) (Numerical Info.) (Event-time Info.) Standard Transformer 0.26 0.23 0.12 0.27 0.22 Scene Memory Transformer 0.53 0.25 0.17 0.40 0.34 SAM2Act++ ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Standard Transformer 0.40 0.30 0.20 0.40 0.50 0.36 HALO 0.55 0.40 0.55 0.60 0.65 0.55 Scene Memory Transformer (SMT) [24] compresses the entire history into ...
- **p. 8 / IV. EXPERIMENTS - extractive body cue:** Cotraining VQA and action prediction achieves 64% success, outperforming pretrain-then-finetune (44%) and no-VQA training (42%) by 20 and 22 points, respectively.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 2. HALO learns to retrieve diverse forms of task-relevant information from history, guided by priors distilled from vision-language foundation models. observations can amplify ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | These results support our hypothesis that HALO reduces model drift (fewer manipulation failures) | p. 7 (IV. EXPERIMENTS) |
| body limitation/failure cue | In addition, we measure manipulation and memory failures in real-world evaluations, finding that HALO reduces them by 8% and 25% absolute over full attention ... | p. 7 (IV. EXPERIMENTS) |
| body limitation/failure cue | Method Retrieve Object Return to Container LSTM 0.14 0.12 Mamba 0.20 0.18 TransformerXL 0.12 0.20 Window Attention 0.13 0.16 Strided Attention 0.20 0.28 Hierarchical ... | p. 8 (IV. EXPERIMENTS) |
| body limitation/failure cue | Developing adaptive strategies that retrieve only the necessary amount of information at each step is a promising direction for future work. | p. 8 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| It encodes human priors about what information is important while keeping memory compact. | p. 6 (IV. EXPERIMENTS) |
| To mitigate spurious correlations, we build on the observation that vision-language models (VLMs) encode rich priors about which information from past observations is relevant ... | p. 2 (I. INTRODUCTION) |
| We further find that while vision-language models encode informative priors about task-relevant information, policies using these priors alone reach only 18% absolute success, compared ... | p. 2 (I. INTRODUCTION) |
| The encoded history is Mt = {(x1, e1), . . . , (xt-1, et-1)}. | p. 3 (III. HALO) |
| At time step t, the current observation is encoded as xt = gobs θ (ot) and past actions as ei = gact θ (ai) ... | p. 3 (III. HALO) |
| Both objectives share the same modality-specific encoders gθ and a common backbone fθ that contains the memory retrieval mechanism, differing only in their prediction ... | p. 4 (III. HALO) |
| Distilling Vision-Language Model Priors via Video Question-Answering Vision-language models encode rich priors about scenes, objects, activities, and semantics to understand task instructions, making them ... | p. 4 (III. HALO) |
| Text Answers Text Instructions What activity occurred between timesteps t1 and t2 ? | p. 5 (III. HALO) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2. HALO learns to retrieve diverse forms of task-relevant information from history, guided by priors distilled from vision-language foundation models. observations can amplify this ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** These results support our hypothesis that HALO reduces model drift (fewer manipulation failures)
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** In addition, we measure manipulation and memory failures in real-world evaluations, finding that HALO reduces them by 8% and 25% absolute over full attention in ...
- **p. 8 / IV. EXPERIMENTS - extractive body cue:** Method Retrieve Object Return to Container LSTM 0.14 0.12 Mamba 0.20 0.18 TransformerXL 0.12 0.20 Window Attention 0.13 0.16 Strided Attention 0.20 0.28 Hierarchical Attention ...
- **p. 8 / IV. EXPERIMENTS - extractive body cue:** Developing adaptive strategies that retrieve only the necessary amount of information at each step is a promising direction for future work.

- **PDF anchors reviewed:** datasets p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), metrics p. 8 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), baselines p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), results p. 8 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
