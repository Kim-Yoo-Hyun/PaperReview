# Evaluation - Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=lNVHg9npif; PDF retrieval source: https://openreview.net/pdf/641fc522a201fc660b34e1224cbf7afa6ace2eee.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 9 (Figure/Table caption), p. 7 (5.2. Metrics and Evaluation Protocol), p. 8 (5.3. Core Results), p. 8 (5.3. Core Results), p. 9 (Figure/Table caption)): Figure 5: Comparisons to Prior Methods. Hi Robot outperforms GPT-4o and flat VLA on Table Bussing, Sandwich Making, and Grocery Shopping. Hi Robot averages over 40% higher instruction accuracy than ...

## Evaluation Body Digest

- **p. 8 / 5.2. Metrics and Evaluation Protocol - extractive PDF cue:** Task progress quantifies how closely the robot matches the intended goal and is computed by the proportion of objects that are successfully placed in their ...
- **p. 8 / 5.2. Metrics and Evaluation Protocol - extractive PDF cue:** chopstick HI ROBOT pick up one slice of cheddar cheese put Oreo into the basket respond: Done!
- **p. 5 / 5. Experiments - extractive PDF cue:** In our experimental evaluation, we study a range of problems that combine challenging physical interactions with complex user interaction, including multi-stage instructions, live user feedback ...
- **p. 7 / 5.2. Metrics and Evaluation Protocol - extractive PDF cue:** Each evaluation consists of 20 trials per task per method.
- **p. 7 / 5.2. Metrics and Evaluation Protocol - extractive PDF cue:** This score measures how well the high-level policy's predicted instruction aligns with human intent, requiring multi-modal understanding of the current environment and prompt.
- **p. 8 / 5.3. Core Results - extractive PDF cue:** (4) Expert human guidance reveals the low-level policy's strengths but underscores the need for high-level reasoning.
- **p. 8 / 5.2. Metrics and Evaluation Protocol - extractive PDF cue:** The Instruction Accuracy for a trial is then computed as the proportion of correct predictions out of the total number of predictions.
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 7: Ablation on synthetic data. Synthetic data is essential for handling open-ended instructions, as the model trained with- out it struggle with user-driven deviations, ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4.4. Model Architecture and Implementation (p. 5); 5. Experiments (p. 5); 5.2. Metrics and Evaluation Protocol (p. 7); 5.3. Core Results (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 5: Comparisons to Prior Methods. Hi Robot outperforms GPT-4o and flat VLA on Table Bussing, Sandwich Making, and Grocery Shopping. Hi Robot averages ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 8: Hierarchical policy vs. flat policy. The hierarchical approach outperforms the flat variant trained on the same data, as it effectively integrates user ... | p. 9 (Figure/Table caption) |
| 5.2. Metrics and Evaluation Protocol | EMPIRICAL / SOURCE-REPORTED EVALUATION | This score measures how well the high-level policy's predicted instruction aligns with human intent, requiring multi-modal understanding of the current environment and prompt. | p. 7 (5.2. Metrics and Evaluation Protocol) |
| 5.3. Core Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | We present results for our system and two key baselines: a GPT-4o policy and a flat VLA method. | p. 8 (5.3. Core Results) |
| 5.3. Core Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Quantitative and qualitative results are in Figure 5 and Figure 6, and we summarize our findings below. | p. 8 (5.3. Core Results) |

## Dataset / Benchmark Role

- **p. 8 / 5.2. Metrics and Evaluation Protocol - extractive PDF cue:** Task progress quantifies how closely the robot matches the intended goal and is computed by the proportion of objects that are successfully placed in their ...
- **p. 8 / 5.2. Metrics and Evaluation Protocol - extractive PDF cue:** chopstick HI ROBOT pick up one slice of cheddar cheese put Oreo into the basket respond: Done!
- **p. 5 / 5. Experiments - extractive PDF cue:** In our experimental evaluation, we study a range of problems that combine challenging physical interactions with complex user interaction, including multi-stage instructions, live user feedback ...
- **p. 7 / 5.2. Metrics and Evaluation Protocol - extractive PDF cue:** Each evaluation consists of 20 trials per task per method.
- **p. 7 / 5.2. Metrics and Evaluation Protocol - extractive PDF cue:** This score measures how well the high-level policy's predicted instruction aligns with human intent, requiring multi-modal understanding of the current environment and prompt.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Open-ended instruction following. Hi Robot enables robots to follow multi-stage instructions, adapt to real-time corrections and constraints, complete unseen long-horizon tasks, and respond ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of hierarchical VLA. The policy consists of a high-level and a low-level policy. The high-level policy pro- cesses open-ended instructions and images ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Data collection and generation for training the high- level policy. We first collect teleoperated robot demonstrations and segment them into short skills (e.g., ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4: Task domains used in our evaluation. Across three domains, we evaluate complex instructions, intermediate feedback, and user interruptions. For example, in Table Bussing, ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5: Comparisons to Prior Methods. Hi Robot outperforms GPT-4o and flat VLA on Table Bussing, Sandwich Making, and Grocery Shopping. Hi Robot averages over ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6: Qualitative Command Comparisons. GPT-4o often (a) misidentifies objects, (b) skips subtasks, or (c) ignores user intent. Hi Robot consistently produces commands aligned with ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 7: Ablation on synthetic data. Synthetic data is essential for handling open-ended instructions, as the model trained with- out it struggle with user-driven deviations, ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 8: Hierarchical policy vs. flat policy. The hierarchical approach outperforms the flat variant trained on the same data, as it effectively integrates user feedback ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Task progress quantifies how closely the robot matches the intended goal and is computed by the proportion of objects that are successfully placed in ... | embodiment, simulator version and control stack | p. 8 (5.2. Metrics and Evaluation Protocol), p. 8 (5.2. Metrics and Evaluation Protocol) |
| Task/environment | chopstick HI ROBOT pick up one slice of cheddar cheese put Oreo into the basket respond: Done! | reset, timeout, object/scene variation | p. 8 (5.2. Metrics and Evaluation Protocol), p. 5 (5. Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 4 (3. Preliminaries and Problem Statement) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 3 (3. Preliminaries and Problem Statement), p. 4 (3. Preliminaries and Problem Statement) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| This score measures how well the high-level policy's predicted instruction aligns with human intent, requiring multi-modal understanding of the current environment and prompt. | definition/direction/unit from same section | p. 7 (5.2. Metrics and Evaluation Protocol) |
| (4) Expert human guidance reveals the low-level policy's strengths but underscores the need for high-level reasoning. | definition/direction/unit from same section | p. 8 (5.3. Core Results) |
| The Instruction Accuracy for a trial is then computed as the proportion of correct predictions out of the total number of predictions. | definition/direction/unit from same section | p. 8 (5.2. Metrics and Evaluation Protocol) |
| Figure 7: Ablation on synthetic data. Synthetic data is essential for handling open-ended instructions, as the model trained with- out it struggle with user-driven ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Figure 8: Hierarchical policy vs. flat policy. The hierarchical approach outperforms the flat variant trained on the same data, as it effectively integrates user ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Figure 5: Comparisons to Prior Methods. Hi Robot outperforms GPT-4o and flat VLA on Table Bussing, Sandwich Making, and Grocery Shopping. Hi Robot averages ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 2: Overview of hierarchical VLA. The policy consists of a high-level and a low-level policy. The high-level policy pro- cesses open-ended instructions and ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 3: Data collection and generation for training the high- level policy. We first collect teleoperated robot demonstrations and segment them into short skills ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Across all tasks, Hi Robot exhibits substantially higher Instruction Accuracy and Task Progress, compared to GPT4o and the flat baseline. | comparison identity and matched condition | p. 8 (5.3. Core Results) |
| Figure 6: Qualitative Command Comparisons. GPT-4o often (a) misidentifies objects, (b) skips subtasks, or (c) ignores user intent. Hi Robot consistently produces commands aligned ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Figure 5: Comparisons to Prior Methods. Hi Robot outperforms GPT-4o and flat VLA on Table Bussing, Sandwich Making, and Grocery Shopping. Hi Robot averages ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 8: Hierarchical policy vs. flat policy. The hierarchical approach outperforms the flat variant trained on the same data, as it effectively integrates user ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| Figure 1: Open-ended instruction following. Hi Robot enables robots to follow multi-stage instructions, adapt to real-time corrections and constraints, complete unseen long-horizon tasks, and ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| Figure 7: Ablation on synthetic data. Synthetic data is essential for handling open-ended instructions, as the model trained with- out it struggle with user-driven ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 8: Hierarchical policy vs. flat policy. The hierarchical approach outperforms the flat variant trained on the same data, as it effectively integrates user ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Without synthetic data, the highlevel policy aligns well with image observations but ignores user constraints. as a correct prediction; otherwise, it is labeled as ... | component/input/data sensitivity | p. 8 (5.2. Metrics and Evaluation Protocol) |
| Figure 7: Ablation on synthetic data. Synthetic data is essential for handling open-ended instructions, as the model trained with- out it struggle with user-driven ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| The lowlevel policy is the π0 VLA (Black et al., 2024), which is trained by finetuning PaliGemma-3B with an additional flow matching "action expert" ... | component/input/data sensitivity | p. 5 (4.4. Model Architecture and Implementation) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We show that our framework enables a robot to process much more complex prompts than prior end-to-end instruction following systems and incorporate feedback during ... | Figure 5: Comparisons to Prior Methods. Hi Robot outperforms GPT-4o and flat VLA on Table Bussing, Sandwich Making, and Grocery Shopping. Hi Robot averages ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 9 (Figure/Table caption), p. 7 (5.2. Metrics and Evaluation Protocol), p. 8 (5.3. Core Results), p. 8 (5.3. Core Results), p. 9 (Figure/Table caption) |
| Primary metric/result | Figure 8: Hierarchical policy vs. flat policy. The hierarchical approach outperforms the flat variant trained on the same data, as it effectively integrates user ... | numeric claim only at cited anchor | p. 9 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 7 / 5.2. Metrics and Evaluation Protocol - extractive PDF cue:** Each evaluation consists of 20 trials per task per method.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Our system also has a number of limitations that could be studied in future work. | p. 9 (6. Discussion and Future Work) |
| body limitation/failure cue | With human high-level instructions, the lowlevel policy executes nearly flawlessly, showing that failures stem more from reasoning than actuation. | p. 8 (5.3. Core Results) |
| body limitation/failure cue | Coupling these two layers more directly, e.g. by allowing the high-level policy to be more aware of how successfully the low-level policy completes each ... | p. 9 (6. Discussion and Future Work) |
| body limitation/failure cue | GPT-4o, however, often fails to maintain a coherent internal state, leading to commands like picking up new objects when the gripper is still occupied ... | p. 8 (5.3. Core Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The Instruction Accuracy for a trial is then computed as the proportion of correct predictions out of the total number of predictions. | p. 8 (5.2. Metrics and Evaluation Protocol) |
| In our implementation, the low-level and high-level policies use the same base VLM as a starting point, namely the PaliGemma-3B VLM (Beyer et al., ... | p. 5 (4.4. Model Architecture and Implementation) |
| Each evaluation consists of 20 trials per task per method. | p. 7 (5.2. Metrics and Evaluation Protocol) |
| We report two complementary metrics, measured by a human evaluator who is blind to the method being run. | p. 7 (5.2. Metrics and Evaluation Protocol) |
| Task progress quantifies how closely the robot matches the intended goal and is computed by the proportion of objects that are successfully placed in ... | p. 8 (5.2. Metrics and Evaluation Protocol) |
| When the system receives a user intervention, the high-level inference is triggered immediately to recompute ˆℓt. | p. 4 (4.2. Incorporating User Interaction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 6. Discussion and Future Work - extractive PDF cue:** Our system also has a number of limitations that could be studied in future work.
- **p. 8 / 5.3. Core Results - extractive PDF cue:** With human high-level instructions, the lowlevel policy executes nearly flawlessly, showing that failures stem more from reasoning than actuation.
- **p. 9 / 6. Discussion and Future Work - extractive PDF cue:** Coupling these two layers more directly, e.g. by allowing the high-level policy to be more aware of how successfully the low-level policy completes each command, ...
- **p. 8 / 5.3. Core Results - extractive PDF cue:** GPT-4o, however, often fails to maintain a coherent internal state, leading to commands like picking up new objects when the gripper is still occupied or ...

- **PDF anchors reviewed:** datasets p. 8 (5.2. Metrics and Evaluation Protocol), p. 8 (5.2. Metrics and Evaluation Protocol), p. 5 (5. Experiments), p. 7 (5.2. Metrics and Evaluation Protocol), p. 7 (5.2. Metrics and Evaluation Protocol), metrics p. 7 (5.2. Metrics and Evaluation Protocol), p. 8 (5.3. Core Results), p. 8 (5.2. Metrics and Evaluation Protocol), p. 9 (Figure/Table caption), p. 9 (Figure/Table caption), p. 7 (Figure/Table caption), baselines p. 8 (5.3. Core Results), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 9 (Figure/Table caption), p. 2 (Figure/Table caption), p. 9 (Figure/Table caption), results p. 7 (Figure/Table caption), p. 9 (Figure/Table caption), p. 7 (5.2. Metrics and Evaluation Protocol), p. 8 (5.3. Core Results), p. 8 (5.3. Core Results), p. 9 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
