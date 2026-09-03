# Evaluation - R3M: A Universal Visual Representation for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v205/nair23a.html; PDF retrieval source: https://proceedings.mlr.press/v205/nair23a.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 17 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 18 (Figure/Table caption)): Figure 8: Performance over different views/dataset sizes. We report the success rate of R3M and baseline across each view (left) and dataset size (right). We see that the performance improvement ...

## Evaluation Body Digest

- **p. 5 / 4 Experiments - extractive body cue:** In our experiments, we aim to study how the pre-trained R3M representation can be re-used for multiple downstream robot learning tasks.
- **p. 5 / 4 Experiments - extractive body cue:** First, we study if R3M enables more data efficient imitation learning on unseen environments and tasks compared to existing visual representations and learning from scratch.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Data Efficient Imitation Learning in Unseen Environments/Tasks. We report the success rates of downstream imitation learning with standard error bars. We observe that ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Ablating Components of R3M. We see report success rate of downstream imitation learning on variants of R3M. We observe that on average, removing ...
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 8: Performance over different views/dataset sizes. We report the success rate of R3M and baseline across each view (left) and dataset size (right). We ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Real World Success Rates. R3M outperforms CLIP on the challenging real world manipulation tasks. In Table 3, we report the success rates comparing ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Real World Robot Learning with R3M. With R3M we are able to learn challenging tasks like putting lettuce in the pan, pushing the ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 9: Per task Success Rate. We observe that R3M is the highest performing method on 11/12 tasks. 18

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** 4 Experiments (p. 5); A.3 Additional Implementation Details (p. 14); B Evaluation Details (p. 14); C Additional Results (p. 17).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 8: Performance over different views/dataset sizes. We report the success rate of R3M and baseline across each view (left) and dataset size (right). ... | p. 17 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4: Data Efficient Imitation Learning in Unseen Environments/Tasks. We report the success rates of downstream imitation learning with standard error bars. We observe ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 3: Real World Success Rates. R3M outperforms CLIP on the challenging real world manipulation tasks. In Table 3, we report the success rates ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5: Real World Robot Learning with R3M. With R3M we are able to learn challenging tasks like putting lettuce in the pan, pushing ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1: Ablating Components of R3M. We see report success rate of downstream imitation learning on variants of R3M. We observe that on average, ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / 4 Experiments - extractive body cue:** In our experiments, we aim to study how the pre-trained R3M representation can be re-used for multiple downstream robot learning tasks.
- **p. 5 / 4 Experiments - extractive body cue:** First, we study if R3M enables more data efficient imitation learning on unseen environments and tasks compared to existing visual representations and learning from scratch.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Pre-Training Reusable Representations for Robot Manipulation (R3M): We pre-train a visual representation using diverse human video datasets like Ego4D [16], and study its ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Ego4D [16] Video and Language (left). Sample frames and associated language from Grauman et al. [16] used for training R3M. R3M Training (right). ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Simulated Evaluation Environments. We consider a comprehensive set of manipulation tasks in simulation (left), including 5 tasks with a Sawyer from MetaWorld [22], ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Data Efficient Imitation Learning in Unseen Environments/Tasks. We report the success rates of downstream imitation learning with standard error bars. We observe that ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Ablating Components of R3M. We see report success rate of downstream imitation learning on variants of R3M. We observe that on average, removing ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Importance of Data vs. Algo- rithm. We find that the MoCo-Ego4D and MVP models, which leverage the same or more data and compute ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Real World Robot Learning with R3M. With R3M we are able to learn challenging tasks like putting lettuce in the pan, pushing the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Real World Success Rates. R3M outperforms CLIP on the challenging real world manipulation tasks. In Table 3, we report the success rates comparing ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In our experiments, we aim to study how the pre-trained R3M representation can be re-used for multiple downstream robot learning tasks. | embodiment, simulator version and control stack | p. 5 (4 Experiments), p. 5 (4 Experiments) |
| Task/environment | First, we study if R3M enables more data efficient imitation learning on unseen environments and tasks compared to existing visual representations and learning from ... | reset, timeout, object/scene variation | p. 5 (4 Experiments) |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 1 (1 Introduction), p. 1 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 4: Data Efficient Imitation Learning in Unseen Environments/Tasks. We report the success rates of downstream imitation learning with standard error bars. We observe ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 1: Ablating Components of R3M. We see report success rate of downstream imitation learning on variants of R3M. We observe that on average, ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 8: Performance over different views/dataset sizes. We report the success rate of R3M and baseline across each view (left) and dataset size (right). ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| Table 3: Real World Success Rates. R3M outperforms CLIP on the challenging real world manipulation tasks. In Table 3, we report the success rates ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 5: Real World Robot Learning with R3M. With R3M we are able to learn challenging tasks like putting lettuce in the pan, pushing ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 9: Per task Success Rate. We observe that R3M is the highest performing method on 11/12 tasks. 18 | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| The policy, π, is trained with a standard behavior cloning loss //at -π([zt, pt])//2 | definition/direction/unit from same section | p. 5 (4 Experiments) |
| Finally, in the appendix, we take a deeper look at task performance of R3M and prior methods with different amounts of data, different camera ... | definition/direction/unit from same section | p. 5 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 4: Data Efficient Imitation Learning in Unseen Environments/Tasks. We report the success rates of downstream imitation learning with standard error bars. We observe ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 3: Real World Success Rates. R3M outperforms CLIP on the challenging real world manipulation tasks. In Table 3, we report the success rates ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| First, we study if R3M enables more data efficient imitation learning on unseen environments and tasks compared to existing visual representations and learning from ... | comparison identity and matched condition | p. 5 (4 Experiments) |
| Figure 5: Real World Robot Learning with R3M. With R3M we are able to learn challenging tasks like putting lettuce in the pan, pushing ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Figure 8: Performance over different views/dataset sizes. We report the success rate of R3M and baseline across each view (left) and dataset size (right). ... | comparison identity and matched condition | p. 17 (Figure/Table caption) |
| Table 2: Importance of Data vs. Algo- rithm. We find that the MoCo-Ego4D and MVP models, which leverage the same or more data and ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 1: Ablating Components of R3M. We see report success rate of downstream imitation learning on variants of R3M. We observe that on average, ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Figure 1: Pre-Training Reusable Representations for Robot Manipulation (R3M): We pre-train a visual representation using diverse human video datasets like Ego4D [16], and study ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| Figure 4: Data Efficient Imitation Learning in Unseen Environments/Tasks. We report the success rates of downstream imitation learning with standard error bars. We observe ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Second, again in the data efficient imitation learning setting, we ablate the different components of the R3M training objective and observe that all components ... | component/input/data sensitivity | p. 5 (4 Experiments) |
| Given a pretrained visual representation Fϕ, we form the state representation as a concatenation of the visual embedding zt = Fϕ(It) and the robot ... | component/input/data sensitivity | p. 5 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We hypothesize that a good representation for vision-based robotic manipulation consists of three components. | Figure 8: Performance over different views/dataset sizes. We report the success rate of R3M and baseline across each view (left) and dataset size (right). ... | PDF body cue; verify exact table/figure and matched conditions | p. 17 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 18 (Figure/Table caption) |
| Primary metric/result | Figure 4: Data Efficient Imitation Learning in Unseen Environments/Tasks. We report the success rates of downstream imitation learning with standard error bars. We observe ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 5 Limitations and Future Work In this work, we set out to study if pre-training visual representations on diverse human videos can enable efficient ... | p. 8 (2. We) |
| body limitation/failure cue | While we were excited by strong results on a wide set of simulated and real robotic tasks, a number of important limitations remain. | p. 8 (2. We) |
| body limitation/failure cue | Specifically, we compare the full R3M with R3M(-Aug), which does not use crop augmentations, R3M(-L1), which does not include L1 regularization, and R3M(-Lang), which ... | p. 7 (2. We) |
| body limitation/failure cue | For a robust evaluation, we consider multiple views for each environment (See Figure 3), and 3 dataset sizes: [5, 10, 25] in MetaWorld and ... | p. 6 (2. We) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| no implementation/reproducibility sentence selected | verify appendix and code/project |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 2. We - extractive body cue:** 5 Limitations and Future Work In this work, we set out to study if pre-training visual representations on diverse human videos can enable efficient learning ...
- **p. 8 / 2. We - extractive body cue:** While we were excited by strong results on a wide set of simulated and real robotic tasks, a number of important limitations remain.
- **p. 7 / 2. We - extractive body cue:** Specifically, we compare the full R3M with R3M(-Aug), which does not use crop augmentations, R3M(-L1), which does not include L1 regularization, and R3M(-Lang), which does ...
- **p. 6 / 2. We - extractive body cue:** For a robust evaluation, we consider multiple views for each environment (See Figure 3), and 3 dataset sizes: [5, 10, 25] in MetaWorld and Franka ...

- **Evidence anchors reviewed:** datasets p. 5 (4 Experiments), p. 5 (4 Experiments), metrics p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 17 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 18 (Figure/Table caption), baselines p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 5 (4 Experiments), p. 8 (Figure/Table caption), p. 17 (Figure/Table caption), p. 7 (Figure/Table caption), results p. 17 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 18 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 8: Performance over different views/dataset sizes. We report the success rate of R3M and baseline across each view (left) and dataset size (right). We see that the performance improvement ... (p. 17, Figure/Table caption).
- **Metric evidence:** Finally, in the appendix, we take a deeper look at task performance of R3M and prior methods with different amounts of data, different camera viewpoints, and different tasks. (p. 5, 4 Experiments).
- **Baseline/ablation evidence:** First, we study if R3M enables more data efficient imitation learning on unseen environments and tasks compared to existing visual representations and learning from scratch. (p. 5, 4 Experiments).
- **Failure/negative evidence:** While we were excited by strong results on a wide set of simulated and real robotic tasks, a number of important limitations remain. (p. 8, 2. We).
