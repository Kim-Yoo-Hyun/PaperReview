# Evaluation - Learning to Be Uncertain: Pre-training World Models with Horizon-Calibrated Uncertainty

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10007319; PDF retrieval source: https://openreview.net/pdf?id=pZuZWRuPyi. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 18 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 21 (Figure/Table caption)): In the imitation learning setting, HAUWM achieves stateof-the-art performance, outperforming baselines in several tasks and performing competitively in Drawer Close.

## Evaluation Body Digest

- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** 5.1 EXPERIMENTAL SETUP Benchmark Environments.
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** These include several locomotion tasks from the DeepMind Control Suite (DMC) (Tassa et al., 2018), a set of distinct robotic manipulation tasks from MetaWorld (Yu ...
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** Therefore, we fine-tune our pre-trained model using established algorithms for imitation learning (IL) and offline RL on several benchmark tasks, with standard VMAIL (Rafailov et ...
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** 3, our method, HAUWM, achieves state-of-the-art sample efficiency and final performance on the majority of the tested benchmarks.
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** This led to significant performance degradation, particularly on the DMC benchmark, confirming that explicitly modeling structured temporal uncertainty is critical for learning robust dynamics representations.
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** Furthermore, HAUWM shows strong performance in the offline RL, where learning from a fixed dataset without online interaction is required.
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 2: Performance of HAUWM and baselines on diverse downstream learning paradigms, includ- ing imitation and offline RL. All scores are normalized returns, reported as ...
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** First, to verify the necessity of our core contribution, we trained a variant without the Horizon-Calibrated Uncertainty loss (w/o HCU).

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** 5 EXPERIMENTS (p. 7); A ENVIROMENTS AND DATASETS (p. 14).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | In the imitation learning setting, HAUWM achieves stateof-the-art performance, outperforming baselines in several tasks and performing competitively in Drawer Close. | p. 9 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Performance (RQ1): Does HAUWM lead to improved sample efficiency and final performance on downstream RL tasks compared to state-of-the-art methods? | p. 7 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | 3, our method, HAUWM, achieves state-of-the-art sample efficiency and final performance on the majority of the tested benchmarks. | p. 8 (5 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 3: Core hyperparameters for HAUWM pre-training and fine-tuning. action inputs during fine-tuning. This approach significantly improves sample efficiency in down- stream tasks by ... | p. 18 (Figure/Table caption) |
| 5 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Conversely, on the Push Green task, HAUWM is outperformed by ContextWM. | p. 8 (5 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** 5.1 EXPERIMENTAL SETUP Benchmark Environments.
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** These include several locomotion tasks from the DeepMind Control Suite (DMC) (Tassa et al., 2018), a set of distinct robotic manipulation tasks from MetaWorld (Yu ...
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** Therefore, we fine-tune our pre-trained model using established algorithms for imitation learning (IL) and offline RL on several benchmark tasks, with standard VMAIL (Rafailov et ...
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** 3, our method, HAUWM, achieves state-of-the-art sample efficiency and final performance on the majority of the tested benchmarks.
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** This led to significant performance degradation, particularly on the DMC benchmark, confirming that explicitly modeling structured temporal uncertainty is critical for learning robust dynamics representations.
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** Furthermore, HAUWM shows strong performance in the offline RL, where learning from a fixed dataset without online interaction is required.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: (a) Prevailing pre-training methods erroneously compel a world model to predict a single deterministic outcome from action-free video, ignoring the multiple futures that ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Our pre-training framework (left) uses a dynamics ensemble to predict states at variable horizons, conditioned by a temporal embedding, learning a structured representation ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3: Performance comparison of HAUWM against state-of-the-art baselines on a suite of down- stream manipulation and locomotion tasks. Solid curves represent the mean evaluation ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: Ablation results on Kmax. We conduct a series of ablation studies to dissect the contributions of HAUWM's key components and validate our design ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 5: Imagined future rollouts from three randomly selected dynamics heads during action- free pre-training (a) and action-conditioned fine-tuning (b). The model produces diverse, high- ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 2: Performance of HAUWM and baselines on diverse downstream learning paradigms, includ- ing imitation and offline RL. All scores are normalized returns, reported as ...
- **p. 15 / Figure/Table caption - extractive PDF cue:** Figure 6: The observation example of each task in the environments: Meta-World (top left), DMC (bottom left), and RoboDesk (right). while open slide demands precise ...
- **p. 18 / Figure/Table caption - extractive PDF cue:** Table 3: Core hyperparameters for HAUWM pre-training and fine-tuning. action inputs during fine-tuning. This approach significantly improves sample efficiency in down- stream tasks by transferring ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 5.1 EXPERIMENTAL SETUP Benchmark Environments. | embodiment, simulator version and control stack | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Task/environment | These include several locomotion tasks from the DeepMind Control Suite (DMC) (Tassa et al., 2018), a set of distinct robotic manipulation tasks from MetaWorld ... | reset, timeout, object/scene variation | p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 5 (4 METHODOLOGY), p. 4 (3 PRELIMINARIES) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 5 (4 METHODOLOGY), p. 1 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 2: Performance of HAUWM and baselines on diverse downstream learning paradigms, includ- ing imitation and offline RL. All scores are normalized returns, reported ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| First, to verify the necessity of our core contribution, we trained a variant without the Horizon-Calibrated Uncertainty loss (w/o HCU). | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| The somewhat larger performance variance of HAUWM on tasks like Dial Turn is an expected trade-off of our ensemble-based architecture, which, while enabling superior ... | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| 4, a moderate value of Kmax = 5 yields the best performance. | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| Figure 3: Performance comparison of HAUWM against state-of-the-art baselines on a suite of down- stream manipulation and locomotion tasks. Solid curves represent the mean ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Analysis (RQ3): Does HAUWM successfully estimate the uncertainty in different training stage? | definition/direction/unit from same section | p. 7 (5 EXPERIMENTS) |
| The results, presented in table 2, demonstrate the broad applicability of our approach. | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| Table 6: Ablation on ensemble size M. Performance peaks at M = 7, confirming that moderate ensemble diversity yields the best downstream control performance. ... | definition/direction/unit from same section | p. 21 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Performance (RQ1): Does HAUWM lead to improved sample efficiency and final performance on downstream RL tasks compared to state-of-the-art methods? | comparison identity and matched condition | p. 7 (5 EXPERIMENTS) |
| In the imitation learning setting, HAUWM achieves stateof-the-art performance, outperforming baselines in several tasks and performing competitively in Drawer Close. | comparison identity and matched condition | p. 9 (5 EXPERIMENTS) |
| Figure 3: Performance comparison of HAUWM against state-of-the-art baselines on a suite of down- stream manipulation and locomotion tasks. Solid curves represent the mean ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| We compare our method, which we denote as HAUWM, against several strong baselines to provide a comprehensive evaluation: • APV (Seo et al., 2022): ... | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |
| Conversely, on the Push Green task, HAUWM is outperformed by ContextWM. | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |
| It significantly surpasses the baselines on almost all 9 | comparison identity and matched condition | p. 9 (5 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| First, to verify the necessity of our core contribution, we trained a variant without the Horizon-Calibrated Uncertainty loss (w/o HCU). | component/input/data sensitivity | p. 8 (5 EXPERIMENTS) |
| Ablation (RQ2): What are the relative contributions of the core components of HAUWM? | component/input/data sensitivity | p. 7 (5 EXPERIMENTS) |
| We conduct a series of ablation studies to dissect the contributions of HAUWM's key components and validate our design choices, and record results in ... | component/input/data sensitivity | p. 8 (5 EXPERIMENTS) |
| Furthermore, HAUWM shows strong performance in the offline RL, where learning from a fixed dataset without online interaction is required. | component/input/data sensitivity | p. 9 (5 EXPERIMENTS) |
| For additional ablation studies examining the scaling function k and the number of ensemble dynamics heads M, refer to the appendix E.4 and appendix ... | component/input/data sensitivity | p. 9 (5 EXPERIMENTS) |
| Table 6: Ablation on ensemble size M. Performance peaks at M = 7, confirming that moderate ensemble diversity yields the best downstream control performance. ... | component/input/data sensitivity | p. 21 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We propose a novel framework using variable-horizon prediction and introduce the Horizon-Calibrated Uncertainty (HCU) loss to learn the relationship between time and predictive uncertainty ... | In the imitation learning setting, HAUWM achieves stateof-the-art performance, outperforming baselines in several tasks and performing competitively in Drawer Close. | PDF body cue; verify exact table/figure and matched conditions | p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 18 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 21 (Figure/Table caption) |
| Primary metric/result | Performance (RQ1): Does HAUWM lead to improved sample efficiency and final performance on downstream RL tasks compared to state-of-the-art methods? | numeric claim only at cited anchor | p. 7 (5 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** All observations are rendered as 64×64×3 images.
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** Method DMC MetaWorld RoboDesk λ = 10.0 0.67±0.13 0.77±0.05 0.61 ± 0.09 λ = 10-1 0.69±0.06 0.80±0.10 0.60 ± 0.05 λ = 10-2 0.70±0.04 0.76±0.07 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | To maintain compatibility with this stream's original design, we condition it on relative temporal embeddings ∆te k=1 (as defined in Section 4.2), injecting a ... | p. 6 (4 METHODOLOGY) |
| body limitation/failure cue | This led to significant performance degradation, particularly on the DMC benchmark, confirming that explicitly modeling structured temporal uncertainty is critical for learning robust dynamics ... | p. 8 (5 EXPERIMENTS) |
| body limitation/failure cue | Robustness (RQ4): Can our pre-training world model generalize to diverse downstream learning paradigms? | p. 7 (5 EXPERIMENTS) |
| body limitation/failure cue | We attribute this strong performance to our core contribution: by pre-training a model that explicitly represents temporal uncertainty, the agent builds a more robust ... | p. 8 (5 EXPERIMENTS) |
| body limitation/failure cue | This suggests that the structured uncertainty learned during pre-training provides a robust foundation for mimicking experts, where understanding plausible future states is crucial. | p. 9 (5 EXPERIMENTS) |
| body limitation/failure cue | Therefore, we fine-tune our pre-trained model using established algorithms for imitation learning (IL) and offline RL on several benchmark tasks, with standard VMAIL (Rafailov ... | p. 9 (5 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The advantage is particularly pronounced in dynamically complex locomotion tasks such as Walker Run, and Hopper Hop. | p. 8 (5 EXPERIMENTS) |
| The somewhat larger performance variance of HAUWM on tasks like Dial Turn is an expected trade-off of our ensemble-based architecture, which, while enabling superior ... | p. 8 (5 EXPERIMENTS) |
| For image reconstruction, we compute the ensemble mean ¯µt+k = 1 M PM i=1 µθi(st, ∆te k) as st+k and decode it as ˆot+k ... | p. 5 (4 METHODOLOGY) |
| Minimizing LHCU explicitly encodes the inductive bias that uncertainty should increase with prediction horizon. | p. 5 (4 METHODOLOGY) |
| Implementation details are provided in appendix C.2. | p. 6 (4 METHODOLOGY) |
| Specifically, we initialize the visual encoder and ensemble dynamics heads from pretraining, freezing their parameters to retain general visual and temporal representations, while introducing ... | p. 6 (4 METHODOLOGY) |
| Solid curves represent the mean evaluation return across four random seeds, and shaded regions denote the 95% confidence interval. exploiting task-specific action knowledge from ... | p. 7 (4 METHODOLOGY) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4 METHODOLOGY - extractive PDF cue:** To maintain compatibility with this stream's original design, we condition it on relative temporal embeddings ∆te k=1 (as defined in Section 4.2), injecting a Gaussian ...
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** This led to significant performance degradation, particularly on the DMC benchmark, confirming that explicitly modeling structured temporal uncertainty is critical for learning robust dynamics representations.
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** Robustness (RQ4): Can our pre-training world model generalize to diverse downstream learning paradigms?
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** We attribute this strong performance to our core contribution: by pre-training a model that explicitly represents temporal uncertainty, the agent builds a more robust and ...
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** This suggests that the structured uncertainty learned during pre-training provides a robust foundation for mimicking experts, where understanding plausible future states is crucial.
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** Therefore, we fine-tune our pre-trained model using established algorithms for imitation learning (IL) and offline RL on several benchmark tasks, with standard VMAIL (Rafailov et ...

- **PDF anchors reviewed:** datasets p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), metrics p. 10 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 7 (Figure/Table caption), p. 7 (5 EXPERIMENTS), baselines p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 7 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), results p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 18 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 21 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
