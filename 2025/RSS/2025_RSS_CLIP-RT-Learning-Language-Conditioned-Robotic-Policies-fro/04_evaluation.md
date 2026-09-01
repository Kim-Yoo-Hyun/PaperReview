# Evaluation - CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p016.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p016.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark), p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (C. Experiments on Common and Novel Tasks)): As shown in Table I, the recent state-of-the-art VLA model, OpenVLA-OFT [30], achieves the highest average success rate of 95.3%.

## Evaluation Body Digest

- **p. 5 / A. Tasks & Dataset - extractive body cue:** This set of tasks serves as a benchmark for evaluating the model's ability to acquire new skills using in-domain data, We first collect indomain data ...
- **p. 9 / B. Adapting CLIP-RT to the LIBERO Benchmark - extractive body cue:** This modification enables us to evaluate the core architectural strengths of CLIP-RT-language-based policy pretraining and lightweight design-on a widely used simulation benchmark (LIBERO), ‘The results ...
- **p. 5 / A. Tasks & Dataset - extractive body cue:** Leveraging stochastic trajectory augmentation (STA), we augment each demonstration with 3 additional trajectories across all tasks. ‘This augmentation increases the dataset size to approximately 11K ...
- **p. 9 / B. Adapting CLIP-RT to the LIBERO Benchmark - extractive body cue:** Surprisingly, CLIP-RT+ attains a near perfect success rate (99.2%) on the LIBERO-Object task suite, indicating strong generalization to unseen objects in simulation environments.
- **p. 8 / A. Tasks & Dataset - extractive body cue:** We evaluate on four task suites of the LIBERO benchmark: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-Long.
- **p. 8 / B. Adapting CLIP-RT to the LIBERO Benchmark - extractive body cue:** Before describing how we adapt CLIP-RT to the LIBERO simulation benchmark, we acknowledge the inherent dificulty of directly representing the fine-grained, continuous humanteleoperated actions in ...
- **p. 9 / B. Adapting CLIP-RT to the LIBERO Benchmark - extractive body cue:** As shown in Table I, the recent state-of-the-art VLA model, OpenVLA-OFT [30], achieves the highest average success rate of 95.3%.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Performance on varying numbers of human inter- ventions. Success rates of two challenging tasks under 0,

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** IV. EXPERIMENTS ON REAL-WORLD RoBoTiC (p. 5); A. Tasks & Dataset (p. 5); C. Experiments on Common and Novel Tasks (p. 5); A. Tasks & Dataset (p. 8); B. Adapting CLIP-RT to the LIBERO Benchmark (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| B. Adapting CLIP-RT to the LIBERO Benchmark | EMPIRICAL / SIMULATION | As shown in Table I, the recent state-of-the-art VLA model, OpenVLA-OFT [30], achieves the highest average success rate of 95.3%. | p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark) |
| B. Adapting CLIP-RT to the LIBERO Benchmark | EMPIRICAL / SIMULATION | [30], we measure the throughput and latency on an NVIDIA A100 GPU, As shown in Table I, CLIP-RT+ achieves 39% improved throughput (4.2Hz~>163.8H7) compared ... | p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Fig. 4: Suecess rates on 9 Common tasks (top) and 9 Novel tasks (bottom). We conduct experiments using all compared ‘methods on Common tasks ... | p. 5 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Fig. 6: Results on few-shot learning. We report the perfor- mance of CLIP-RT, CLIP-RT-Action, and OpenVLA with 1, 5, and 10 demonstrations (from left ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Fig. 7: Performance on varying numbers of human inter- ventions. Success rates of two challenging tasks under 0, | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / A. Tasks & Dataset - extractive body cue:** This set of tasks serves as a benchmark for evaluating the model's ability to acquire new skills using in-domain data, We first collect indomain data ...
- **p. 9 / B. Adapting CLIP-RT to the LIBERO Benchmark - extractive body cue:** This modification enables us to evaluate the core architectural strengths of CLIP-RT-language-based policy pretraining and lightweight design-on a widely used simulation benchmark (LIBERO), ‘The results ...
- **p. 5 / A. Tasks & Dataset - extractive body cue:** Leveraging stochastic trajectory augmentation (STA), we augment each demonstration with 3 additional trajectories across all tasks. ‘This augmentation increases the dataset size to approximately 11K ...
- **p. 9 / B. Adapting CLIP-RT to the LIBERO Benchmark - extractive body cue:** Surprisingly, CLIP-RT+ attains a near perfect success rate (99.2%) on the LIBERO-Object task suite, indicating strong generalization to unseen objects in simulation environments.
- **p. 8 / A. Tasks & Dataset - extractive body cue:** We evaluate on four task suites of the LIBERO benchmark: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-Long.
- **p. 8 / B. Adapting CLIP-RT to the LIBERO Benchmark - extractive body cue:** Before describing how we adapt CLIP-RT to the LIBERO simulation benchmark, we acknowledge the inherent dificulty of directly representing the fine-grained, continuous humanteleoperated actions in ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Overview of language-guided teleoperation,
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: A simplified 2D example of stochastic trajectory augmentation (STA). (a): a demonstration trajectory from the starts to the endpoint ¢, passing through a ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Suecess rates on 9 Common tasks (top) and 9 Novel tasks (bottom). We conduct experiments using all compared ‘methods on Common tasks and ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: A comparison of multi-task and single-task policies ‘on Novel tasks. The performance of each task is in Figure 12 ‘of Appendix.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6: Results on few-shot learning. We report the perfor- mance of CLIP-RT, CLIP-RT-Action, and OpenVLA with 1, 5, and 10 demonstrations (from left to ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Performance on varying numbers of human inter- ventions. Success rates of two challenging tasks under 0,
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 8: Ensembling CLIP-RT and GPT outputs. Given an image and language instruction (top), CLIP-RT produces initial scores for candidate actions (left). GPT then supplies ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 9: Example failure cases of CLIP-RT. (a) CLIP-RT

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This set of tasks serves as a benchmark for evaluating the model's ability to acquire new skills using in-domain data, We first collect indomain ... | embodiment, simulator version and control stack | p. 5 (A. Tasks & Dataset), p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark) |
| Task/environment | This modification enables us to evaluate the core architectural strengths of CLIP-RT-language-based policy pretraining and lightweight design-on a widely used simulation benchmark (LIBERO), ‘The ... | reset, timeout, object/scene variation | p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark), p. 5 (A. Tasks & Dataset) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (A. Preliminaries), p. 2 (A. Preliminaries) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 7 (256 33%), p. 3 (B. CLIP-Based Robotics Transformer (CLIP-RT)) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| As shown in Table I, the recent state-of-the-art VLA model, OpenVLA-OFT [30], achieves the highest average success rate of 95.3%. | definition/direction/unit from same section | p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark) |
| Surprisingly, CLIP-RT+ attains a near perfect success rate (99.2%) on the LIBERO-Object task suite, indicating strong generalization to unseen objects in simulation environments. | definition/direction/unit from same section | p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark) |
| Fig. 7: Performance on varying numbers of human inter- ventions. Success rates of two challenging tasks under 0, | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Fig. 4: Suecess rates on 9 Common tasks (top) and 9 Novel tasks (bottom). We conduct experiments using all compared ‘methods on Common tasks ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Fig. 6: Results on few-shot learning. We report the perfor- mance of CLIP-RT, CLIP-RT-Action, and OpenVLA with 1, 5, and 10 demonstrations (from left ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Fig. 8: Ensembling CLIP-RT and GPT outputs. Given an image and language instruction (top), CLIP-RT produces initial scores for candidate actions (left). GPT then ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Before describing how we adapt CLIP-RT to the LIBERO simulation benchmark, we acknowledge the inherent dificulty of directly representing the fine-grained, continuous humanteleoperated actions ... | definition/direction/unit from same section | p. 8 (B. Adapting CLIP-RT to the LIBERO Benchmark) |
| Fig. 3: A simplified 2D example of stochastic trajectory augmentation (STA). (a): a demonstration trajectory from the starts to the endpoint ¢, passing through ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We introduce baseline ‘models and then discuss the results in detail | comparison identity and matched condition | p. 5 (C. Experiments on Common and Novel Tasks) |
| We train and evaluate CLIP-RT on both Common and Novel tasks, comparing with diverse baselines. | comparison identity and matched condition | p. 5 (C. Experiments on Common and Novel Tasks) |
| As shown in Table I, the recent state-of-the-art VLA model, OpenVLA-OFT [30], achieves the highest average success rate of 95.3%. | comparison identity and matched condition | p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark) |
| When compared to OpenVLA-OFT using the same action chunk size of 8, CLIP-RT+ improves both throughput and latency by approximately 49%. | comparison identity and matched condition | p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark) |
| Fig. 5: A comparison of multi-task and single-task policies ‘on Novel tasks. The performance of each task is in Figure 12 ‘of Appendix. | comparison identity and matched condition | p. 6 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| «+ CLIP-RT-Zero is an ablated model trained solely on the ‘OXE dataset without accessing any in-domain data, | component/input/data sensitivity | p. 5 (C. Experiments on Common and Novel Tasks) |
| We also fine-tune OpenVLA, ‘on the same in-domain data as CLIP-RT by using lowlevel 7D end-effector actions as supervision. | component/input/data sensitivity | p. 5 (C. Experiments on Common and Novel Tasks) |
| This modification enables us to evaluate the core architectural strengths of CLIP-RT-language-based policy pretraining and lightweight design-on a widely used simulation benchmark (LIBERO), ‘The ... | component/input/data sensitivity | p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark) |
| All models, except Diffusion Policy (DP) [10], were fine-tuned. | component/input/data sensitivity | p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Sec- ‘ond, we propose a data collection framework that enables non-experts to collect robot data only through natural language and augment the human-collected demonstration ... | As shown in Table I, the recent state-of-the-art VLA model, OpenVLA-OFT [30], achieves the highest average success rate of 95.3%. | PDF body cue; verify exact table/figure and matched conditions | p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark), p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (C. Experiments on Common and Novel Tasks) |
| Primary metric/result | [30], we measure the throughput and latency on an NVIDIA A100 GPU, As shown in Table I, CLIP-RT+ achieves 39% improved throughput (4.2Hz~>163.8H7) compared ... | numeric claim only at cited anchor | p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark) |

- Numeric sentences retained from the body:
- **p. 5 / A. Tasks & Dataset - extractive body cue:** This set of tasks serves as a benchmark for evaluating the model's ability to acquire new skills using in-domain data, We first collect indomain data ...
- **p. 8 / B. Adapting CLIP-RT to the LIBERO Benchmark - extractive body cue:** We train CLIP-RT+ using 8 NVIDIA H100 GPUs for 128 epochs with a batch size of 256.
- **p. 9 / B. Adapting CLIP-RT to the LIBERO Benchmark - extractive body cue:** However, CLIP-RT+ shows comparable performance across all task suites with an average score of 92.8%, while using 6x fewer parameters (1.3B) compared with OpenVLA-OFT (7.7B).
- **p. 9 / B. Adapting CLIP-RT to the LIBERO Benchmark - extractive body cue:** [30], we measure the throughput and latency on an NVIDIA A100 GPU, As shown in Table I, CLIP-RT+ achieves 39% improved throughput (4.2Hz~>163.8H7) compared with ...
- **p. 1 / Abstract - extractive body cue:** In realworld evaluations, CLIP-RT demonstrates strong capabilities in learning novel manipulation skills, outperforming OpenVLA (7B. parameters) by 24% in average success rates, while using 7x ...
- **p. 1 / Abstract - extractive body cue:** In simulated environments, CLIP-RP also yields strong performance, achieving a 92.8% average success rate on the LIBERO benchmark with an inference throughput of 163 Hz.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Inherent Limitations in Human Language Supervision. | p. 9 (B. Limitations and Future Work) |
| body limitation/failure cue | Without incorporating action history into the context, the model cannot make informed | p. 9 (B. Limitations and Future Work) |
| body limitation/failure cue | Fig. 9: Example failure cases of CLIP-RT. (a) CLIP-RT | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Fig. 3: A simplified 2D example of stochastic trajectory augmentation (STA). (a): a demonstration trajectory from the starts to the endpoint ¢, passing through ... | p. 4 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We train CLIP-RT+ using 8 NVIDIA H100 GPUs for 128 epochs with a batch size of 256. | p. 8 (B. Adapting CLIP-RT to the LIBERO Benchmark) |
| ‘+ OpenVLA [29] is a state-of-the-art, open-source visionlanguage-action (VLA) model. ‘This model leverages the 7B-parameter Llama2 language model [55] and a sual encoder that ... | p. 5 (C. Experiments on Common and Novel Tasks) |
| [30], we measure the throughput and latency on an NVIDIA A100 GPU, As shown in Table I, CLIP-RT+ achieves 39% improved throughput (4.2Hz~>163.8H7) compared ... | p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark) |
| It requires four 11100 GPUs for one day with a batch size of 128. | p. 4 (B. CLIP-Based Robotics Transformer (CLIP-RT)) |
| It consists of two steps: Ianguage-based teleoperation and stochastic trajectory augmentation (STA). | p. 1 (Abstract) |
| In simulated environments, CLIP-RP also yields strong performance, achieving a 92.8% average success rate on the LIBERO benchmark with an inference throughput of 163 ... | p. 1 (Abstract) |
| CLIP-RT achieves strong results, an average success rate of 92.8%, with an improved inference throughput of 163Hz. | p. 2 (Abstract) |
| Using the contrastive objective, CLIP trains an image encoder f(:) and a text encoder q(-) on 400M image-text pairs. | p. 3 (A. Preliminaries) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / B. Limitations and Future Work - extractive body cue:** Inherent Limitations in Human Language Supervision.
- **p. 9 / B. Limitations and Future Work - extractive body cue:** Without incorporating action history into the context, the model cannot make informed
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 9: Example failure cases of CLIP-RT. (a) CLIP-RT
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: A simplified 2D example of stochastic trajectory augmentation (STA). (a): a demonstration trajectory from the starts to the endpoint ¢, passing through a ...

- **PDF anchors reviewed:** datasets p. 5 (A. Tasks & Dataset), p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark), p. 5 (A. Tasks & Dataset), p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark), p. 8 (A. Tasks & Dataset), p. 8 (B. Adapting CLIP-RT to the LIBERO Benchmark), metrics p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark), p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark), p. 7 (Figure/Table caption), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), baselines p. 5 (C. Experiments on Common and Novel Tasks), p. 5 (C. Experiments on Common and Novel Tasks), p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark), p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark), p. 6 (Figure/Table caption), results p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark), p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (C. Experiments on Common and Novel Tasks).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
