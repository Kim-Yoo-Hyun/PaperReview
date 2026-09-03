# Evaluation - Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2307.01928; PDF retrieval source: https://arxiv.org/pdf/2307.01928. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 Experiments), p. 2 (Figure/Table caption), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 6 (4 Experiments)): Nonetheless, KnowNo still achieves 1-ϵ target success rate, as the coverage guarantee from CP makes no assumption about the LLM confidences (e.g., calibrated or accurate) - KnowNo flexibly compensates for ...

## Evaluation Body Digest

- **p. 6 / 4 Experiments - extractive body cue:** In future deployment, we envision that a robot can interact with an end-user (e.g., in a home) to collect a dataset through interactions with the ...
- **p. 7 / 4 Experiments - extractive body cue:** 4.2 Hardware: Multi-Step Tabletop Rearrangement In this example, a UR5 robot arm is asked to sort a variety of toy food items on a table ...
- **p. 6 / 4 Experiments - extractive body cue:** A robot arm is asked to rearrange objects on a table in the PyBullet simulator [17] (Fig.
- **p. 8 / 4 Experiments - extractive body cue:** Method 1-ϵ Plan Succ Task Succ Set Size Help-Step Help-Trial KNOWNO 0.75 0.76 0.74 1.72 0.58 0.92 Simple Set 0.58 0.76 0.72 2.04 0.72 1.00 ...
- **p. 8 / 4 Experiments - extractive body cue:** 4.3 Hardware: Mobile Manipulator in a Kitchen Method Model 1-ϵ Plan Succ Task Succ Set Size Help KNOWNO PaLM-2L 0.85 0.87 0.76 2.22 0.67 Simple ...
- **p. 7 / 4 Experiments - extractive body cue:** Then we run 50 trials for both methods in hardware.
- **p. 7 / 4 Experiments - extractive body cue:** 4 we vary the target error rate ϵ and show the curves of task success rate vs. prediction set size and human help rate averaged ...
- **p. 8 / 4 Experiments - extractive body cue:** Nonetheless, KnowNo still achieves 1-ϵ target success rate, as the coverage guarantee from CP makes no assumption about the LLM confidences (e.g., calibrated or accurate) ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** 4 Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Nonetheless, KnowNo still achieves 1-ϵ target success rate, as the coverage guarantee from CP makes no assumption about the LLM confidences (e.g., calibrated or ... | p. 8 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1: KNOWNO uses Conformal Prediction (CP) to align the uncertainty of LLM planners. Given a language instruction, an LLM generates possible next steps ... | p. 2 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | KNOWNO achieves target task success rate consistently. | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | KNOWNO achieves high task success rate with lower human help as ϵ varies. | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | In Table 2, we compare KNOWNO to Simple Set again by first setting ϵ = 0.15 and also finding ϵ = 0.24 for Simple ... | p. 8 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 6 / 4 Experiments - extractive body cue:** In future deployment, we envision that a robot can interact with an end-user (e.g., in a home) to collect a dataset through interactions with the ...
- **p. 7 / 4 Experiments - extractive body cue:** 4.2 Hardware: Multi-Step Tabletop Rearrangement In this example, a UR5 robot arm is asked to sort a variety of toy food items on a table ...
- **p. 6 / 4 Experiments - extractive body cue:** A robot arm is asked to rearrange objects on a table in the PyBullet simulator [17] (Fig.
- **p. 8 / 4 Experiments - extractive body cue:** Method 1-ϵ Plan Succ Task Succ Set Size Help-Step Help-Trial KNOWNO 0.75 0.76 0.74 1.72 0.58 0.92 Simple Set 0.58 0.76 0.72 2.04 0.72 1.00 ...
- **p. 8 / 4 Experiments - extractive body cue:** 4.3 Hardware: Mobile Manipulator in a Kitchen Method Model 1-ϵ Plan Succ Task Succ Set Size Help KNOWNO PaLM-2L 0.85 0.87 0.76 2.22 0.67 Simple ...
- **p. 7 / 4 Experiments - extractive body cue:** Then we run 50 trials for both methods in hardware.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: KNOWNO uses Conformal Prediction (CP) to align the uncertainty of LLM planners. Given a language instruction, an LLM generates possible next steps and ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: KNOWNO formulates LLM planning as MCQA by first prompting an LLM to generate plausible options, and then asking it to predict the correct ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Deviation from specified task success level 1-ϵ=0.85 to the empirical success rate for the three settings in Simulation. 200 trials are run for ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Comparison of task success rate vs average prediction set size (Left) and vs. human help rate (Right) in Simulation averaged over the three ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: (Left) Multi-step CP is applied in Hardware Tabletop Rearrangement. (Right) CP models ambiguity in possible human locations and triggers clarification from the human ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Results for Hardware Multi-Step Tabletop Rearrangement. Plan success rate is fixed between KNOWNO and Simple Set for comparing the other metrics. Bimanual manipulation. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Results for Hardware Mobile Manipulation. Plan success rate is fixed between KNOWNO and Sim- ple Set to compare the other metrics. In this ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In future deployment, we envision that a robot can interact with an end-user (e.g., in a home) to collect a dataset through interactions with ... | embodiment, simulator version and control stack | p. 6 (4 Experiments), p. 7 (4 Experiments) |
| Task/environment | 4.2 Hardware: Multi-Step Tabletop Rearrangement In this example, a UR5 robot arm is asked to sort a variety of toy food items on a ... | reset, timeout, object/scene variation | p. 7 (4 Experiments), p. 6 (4 Experiments) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 3 (1 Introduction), p. 2 (1 Introduction) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 3 (1 Introduction), p. 1 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 4 we vary the target error rate ϵ and show the curves of task success rate vs. prediction set size and human help rate ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Nonetheless, KnowNo still achieves 1-ϵ target success rate, as the coverage guarantee from CP makes no assumption about the LLM confidences (e.g., calibrated or ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Note that the ϵ level is not used in Prompt Set or Binary, and so the user cannot explicitly control the task success rate. | definition/direction/unit from same section | p. 6 (4 Experiments) |
| 4.1 Simulation: Tabletop Rearrangement Deviation from … Figure 3: Deviation from specified task success level 1-ϵ=0.85 to the empirical success rate for the three ... | definition/direction/unit from same section | p. 6 (4 Experiments) |
| KNOWNO achieves target task success rate consistently. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Plan success rate is fixed between KNOWNO and Simple Set to compare the other metrics. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Figure 1: KNOWNO uses Conformal Prediction (CP) to align the uncertainty of LLM planners. Given a language instruction, an LLM generates possible next steps ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 2: KNOWNO formulates LLM planning as MCQA by first prompting an LLM to generate plausible options, and then asking it to predict the ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 1: KNOWNO uses Conformal Prediction (CP) to align the uncertainty of LLM planners. Given a language instruction, an LLM generates possible next steps ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| We also introduce two prompt-based baselines: Prompt Set prompts the LLM to directly output the prediction set (e.g., "Prediction set: [A, C]"); Binary prompts ... | comparison identity and matched condition | p. 6 (4 Experiments) |
| A straightforward way to construct prediction sets given a desired 1-ϵ coverage is to rank options according to confidence and construct a set such ... | comparison identity and matched condition | p. 6 (4 Experiments) |
| Second, it requires 20× inference time compared to other methods. | comparison identity and matched condition | p. 7 (4 Experiments) |
| Also, as the scenarios get increasingly ambiguous (least in Attribute and most in Spatial), the baselines show larger deviations. | comparison identity and matched condition | p. 7 (4 Experiments) |
| Compared to Simple Set which uses a much higher ϵ, KNOWNO achieves the specified trial-level task success rate precisely by leveraging the Multi-Step Uncertainty ... | comparison identity and matched condition | p. 8 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Lastly, we consider No Help where the option with the highest score is always executed without any human intervention. | component/input/data sensitivity | p. 6 (4 Experiments) |
| We also run KNOWNO with two other LLMs (without hardware evaluation). | component/input/data sensitivity | p. 8 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Here, we present a novel extension of CP to multi-step settings that tackles this challenge. | Nonetheless, KnowNo still achieves 1-ϵ target success rate, as the coverage guarantee from CP makes no assumption about the LLM confidences (e.g., calibrated or ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 Experiments), p. 2 (Figure/Table caption), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 6 (4 Experiments) |
| Primary metric/result | Figure 1: KNOWNO uses Conformal Prediction (CP) to align the uncertainty of LLM planners. Given a language instruction, an LLM generates possible next steps ... | numeric claim only at cited anchor | p. 2 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 4 Experiments - extractive body cue:** Labeling the calibration data takes about 4 hours (for 400 examples) in the multi-step setting and 1.5 hours in single-step settings.
- **p. 6 / 4 Experiments - extractive body cue:** A straightforward way to construct prediction sets given a desired 1-ϵ coverage is to rank options according to confidence and construct a set such that ...
- **p. 6 / 4 Experiments - extractive body cue:** 200 trials are run for each method/setting.
- **p. 7 / 4 Experiments - extractive body cue:** 200 trials are run for each method. ϵ is varied from 0.25 to 0.01 for KNOWNO, and from 0.6 to 0.01 for Simple Set and ...
- **p. 7 / 4 Experiments - extractive body cue:** Then we run 50 trials for both methods in hardware.
- **p. 2 / 1 Introduction - extractive body cue:** LLM Generates Question Conformal prediction threshold: 0.21 Steps with scores above threshold: 0.44 - Put plastic bowl in microwave.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Limitations and future work: The primary limitation of our work is that the task completion guarantee assumes environments (objects) are fully grounded in the ... | p. 9 (6 Discussion) |
| body limitation/failure cue | Another limitation is that, for the task guarantee to hold, the human needs to faithfully provide help when the robot needs it. | p. 9 (6 Discussion) |
| body limitation/failure cue | First, we investigate whether KNOWNO and the baselines achieve a given target task success rate consistently in the three settings - we set the ... | p. 7 (4 Experiments) |
| body limitation/failure cue | Note that the ϵ level is not used in Prompt Set or Binary, and so the user cannot explicitly control the task success rate. | p. 6 (4 Experiments) |
| body limitation/failure cue | Simple Set and Ensemble Set cannot achieve coverage consistently. | p. 7 (4 Experiments) |
| body limitation/failure cue | Target success guarantee from KnowNo is robust to varying LLM choice. | p. 8 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Then we run 50 trials for both methods in hardware. | p. 7 (4 Experiments) |
| 200 trials are run for each method/setting. | p. 6 (4 Experiments) |
| We also run KNOWNO with two other LLMs (without hardware evaluation). | p. 8 (4 Experiments) |
| Method 1-ϵ Plan Succ Task Succ Set Size Help-Step Help-Trial KNOWNO 0.75 0.76 0.74 1.72 0.58 0.92 Simple Set 0.58 0.76 0.72 2.04 0.72 ... | p. 8 (4 Experiments) |
| Second, it requires 20× inference time compared to other methods. | p. 7 (4 Experiments) |
| Instead of using cumulative thresholding, KNOWNO constructs prediction sets by including options with scores higher than a threshold computed using CP, which results in ... | p. 6 (4 Experiments) |
| 1), or robot code executed by an interpreter [5]. | p. 2 (1 Introduction) |
| Possible next steps: 0.44 - Put plastic bowl in microwave. | p. 2 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 6 Discussion - extractive body cue:** Limitations and future work: The primary limitation of our work is that the task completion guarantee assumes environments (objects) are fully grounded in the text ...
- **p. 9 / 6 Discussion - extractive body cue:** Another limitation is that, for the task guarantee to hold, the human needs to faithfully provide help when the robot needs it.
- **p. 7 / 4 Experiments - extractive body cue:** First, we investigate whether KNOWNO and the baselines achieve a given target task success rate consistently in the three settings - we set the failure ...
- **p. 6 / 4 Experiments - extractive body cue:** Note that the ϵ level is not used in Prompt Set or Binary, and so the user cannot explicitly control the task success rate.
- **p. 7 / 4 Experiments - extractive body cue:** Simple Set and Ensemble Set cannot achieve coverage consistently.
- **p. 8 / 4 Experiments - extractive body cue:** Target success guarantee from KnowNo is robust to varying LLM choice.

- **Evidence anchors reviewed:** datasets p. 6 (4 Experiments), p. 7 (4 Experiments), p. 6 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), metrics p. 7 (4 Experiments), p. 8 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), baselines p. 2 (Figure/Table caption), p. 6 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), results p. 8 (4 Experiments), p. 2 (Figure/Table caption), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 6 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
