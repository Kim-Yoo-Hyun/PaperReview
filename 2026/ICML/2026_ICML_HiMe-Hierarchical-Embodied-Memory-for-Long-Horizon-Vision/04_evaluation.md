# Evaluation - HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=vVVbGj9cMC; PDF retrieval source: https://openreview.net/pdf/1158a6b1525482f72ae519b3be5d06e0abef1732.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments)): HiMe significantly outperforms all baselines, achieving a 90% average success rate.

## Evaluation Body Digest

- **p. 7 / 4 Experiments - extractive PDF cue:** After a temporal interval, the robot is tasked with restoring the items to the environment.
- **p. 7 / 4 Experiments - extractive PDF cue:** We design a Domestic Maintenance task to evaluate the robot's capability to integrate inspection, sorting, and preference recall.
- **p. 8 / 4 Experiments - extractive PDF cue:** Without the Sentry, the Planner operates on a frame-by-frame style, and this high-frequency re-evaluation makes the robot hypersensitive to transient visual noise, leading to frequent, ...
- **p. 9 / 4 Experiments - extractive PDF cue:** 5 Further Analysis 5.1 Q1: What Type of Memory Representation is Most Effective for Robotic Tasks?
- **p. 9 / 4 Experiments - extractive PDF cue:** 1) Spatial and Recognition Demands in Robotics: Our study results show that robotics tasks impose strong spatial localization and fine-grained recognition demands that caption only ...
- **p. 8 / 4 Experiments - extractive PDF cue:** This represents the current paradigm of hierarchical robot foundation models, such as Hi-robot [8].
- **p. 10 / 4 Experiments - extractive PDF cue:** Thus, storing more data is insufficient; effective robots must maintain a concise, consistent memory.
- **p. 10 / 4 Experiments - extractive PDF cue:** Object Search Counting Rearrangement Average 50 60 70 80 90 100 Task Progress (%) 86 78 76 80 74 91 84 83 92 92 87 ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 Experiments (p. 7); C Additional Experiments (p. 19); C.2 Open-Source Planner Evaluation (p. 20).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | HiMe significantly outperforms all baselines, achieving a 90% average success rate. | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Although it stores history, it achieves a significantly lower task progress (65%) compared to HiMe (90%). | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 2) The Value of Consistency: While No Management achieves decent performance by retaining all history, it is still inferior to our full method (86% ... | p. 10 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 3) Superiority of Interleaved Memory: Our cross-modal approach achieves the best performance (Average 90%) by combining the spatial/recognitional fidelity of images with the semantic ... | p. 10 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 4, we observe a substantial improvement (14% vs. | p. 8 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 7 / 4 Experiments - extractive PDF cue:** After a temporal interval, the robot is tasked with restoring the items to the environment.
- **p. 7 / 4 Experiments - extractive PDF cue:** We design a Domestic Maintenance task to evaluate the robot's capability to integrate inspection, sorting, and preference recall.
- **p. 8 / 4 Experiments - extractive PDF cue:** Without the Sentry, the Planner operates on a frame-by-frame style, and this high-frequency re-evaluation makes the robot hypersensitive to transient visual noise, leading to frequent, ...
- **p. 9 / 4 Experiments - extractive PDF cue:** 5 Further Analysis 5.1 Q1: What Type of Memory Representation is Most Effective for Robotic Tasks?
- **p. 9 / 4 Experiments - extractive PDF cue:** 1) Spatial and Recognition Demands in Robotics: Our study results show that robotics tasks impose strong spatial localization and fine-grained recognition demands that caption only ...
- **p. 8 / 4 Experiments - extractive PDF cue:** This represents the current paradigm of hierarchical robot foundation models, such as Hi-robot [8].
- **p. 10 / 4 Experiments - extractive PDF cue:** Thus, storing more data is insufficient; effective robots must maintain a concise, consistent memory.
- **p. 10 / 4 Experiments - extractive PDF cue:** Object Search Counting Rearrangement Average 50 60 70 80 90 100 Task Progress (%) 86 78 76 80 74 91 84 83 92 92 87 ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- figure/table caption cue 없음

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | After a temporal interval, the robot is tasked with restoring the items to the environment. | embodiment, simulator version and control stack | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Task/environment | We design a Domestic Maintenance task to evaluate the robot's capability to integrate inspection, sorting, and preference recall. | reset, timeout, object/scene variation | p. 7 (4 Experiments), p. 8 (4 Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (Abstract), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| HiMe significantly outperforms all baselines, achieving a 90% average success rate. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Text is a lossy compression: if perception initially misses an object or its spatial context, discarding raw visuals prevents visual re-grounding to recover details ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| We report API calls, memory hit, and average scores across three tasks. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| We design a Domestic Maintenance task to evaluate the robot's capability to integrate inspection, sorting, and preference recall. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| 7 presents the Precision and Recall, where Subtask "Done" is treated as the positive class. | definition/direction/unit from same section | p. 11 (4 Experiments) |
| 2) The "Conservative" Nature of Sentry: The significant gap between high Precision and low Recall reveals 11 | definition/direction/unit from same section | p. 11 (4 Experiments) |
| While this minimizes premature stops (high Precision), the low Recall creates a "missing signal" problem where the agent might overshoot its target or enter ... | definition/direction/unit from same section | p. 12 (4 Experiments) |
| These tasks are specifically curated to evaluate diverse capabilities, including user interaction, preference memory, updating memory and planning with exploration. | definition/direction/unit from same section | p. 7 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| HiMe significantly outperforms all baselines, achieving a 90% average success rate. | comparison identity and matched condition | p. 9 (4 Experiments) |
| HiMe consistently outperforms both text-only and image-only baselines across all three tasks, verifying the robustness of our cross-modal memory mechanism. | comparison identity and matched condition | p. 10 (4 Experiments) |
| The comparisons are designed as follows: Transient Memory: A standard hierarchical VLA baseline where a memory-less Planner is invoked at fixed intervals (𝑛𝑚) and ... | comparison identity and matched condition | p. 8 (4 Experiments) |
| To assess the need for dynamic memory management, we run an ablation against two baselines: (1) No Management, which only supports Add/Retrieve and keeps ... | comparison identity and matched condition | p. 10 (4 Experiments) |
| Human High-level: A human oracle provides the correct subtask description at each step. | comparison identity and matched condition | p. 8 (4 Experiments) |
| We compare HiMe against Transient, Sentry, and Flat Memory baselines across three longhorizon tasks. | comparison identity and matched condition | p. 9 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| HiMe w/o Sentry: We utilize our complete Planner's memory design but remove the sentry module. | component/input/data sensitivity | p. 8 (4 Experiments) |
| Transient Memory w/ Sentry: This variant introduces our Sentry module to trigger the Planner based on task progress. | component/input/data sensitivity | p. 8 (4 Experiments) |
| In Counting, even with Sentry stabilization (Transient Memory w/ Sentry), the robot still fails (23%) due to the lack of persistence: without an explicit ... | component/input/data sensitivity | p. 9 (4 Experiments) |
| Object Search Counting Rearrangement Average 50 60 70 80 90 100 Task Progress (%) 86 78 76 80 74 91 84 83 92 92 ... | component/input/data sensitivity | p. 10 (4 Experiments) |
| Without Update/Delete, memory stores obsolete states (e.g., prior object locations) alongside current ones, introducing noise during Query and potentially confusing the Planner. | component/input/data sensitivity | p. 10 (4 Experiments) |
| In contrast, HiMe maintains an infinite structured memory, avoiding this forgetting and enabling immediate retrieval without physical re-exploration. | component/input/data sensitivity | p. 11 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our core contributions are summarized as follows: • We propose a Hierarchical Memory Management framework that decouples robotic control into transient (Executor), working (Sentry), ... | HiMe significantly outperforms all baselines, achieving a 90% average success rate. | PDF body cue; verify exact table/figure and matched conditions | p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Primary metric/result | Although it stores history, it achieves a significantly lower task progress (65%) compared to HiMe (90%). | numeric claim only at cited anchor | p. 9 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Experiments - extractive PDF cue:** 4.1 Task Setting To demonstrate the critical role of hierarchical memory in long-horizon tasks, we designed three distinct tabletop manipulation scenarios, as illustrated in Fig.
- **p. 8 / 4 Experiments - extractive PDF cue:** We use a WidowX-250s arm with a parallel gripper and dual-camera visual input (thirdperson and wrist view).
- **p. 8 / 4 Experiments - extractive PDF cue:** The Executor 𝜋𝑒runs at 2 Hz, predicting an action chunk 𝐴𝑡of 10 actions (10 Hz), of which 5 are executed open-loop.
- **p. 9 / 4 Experiments - extractive PDF cue:** Object Search Counting Rearrangement Average 0 20 40 60 80 100 Task Progress (%) 0 18 23 14 0 23 56 26 64 58 73 ...
- **p. 10 / 4 Experiments - extractive PDF cue:** Object Search Counting Rearrangement Average 50 60 70 80 90 100 Task Progress (%) 86 78 76 80 74 91 84 83 92 92 87 ...
- **p. 11 / 4 Experiments - extractive PDF cue:** Object Search Counting Rearrangement Average 50 60 70 80 90 100 Task Progress (%) 67 73 64 68 90 89 80 86 92 92 87 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The fundamental limitation of such contextual memory is the lack of consolidation: a simple FIFO queue cannot distinguish between truly critical frames and redundant ... | p. 9 (4 Experiments) |
| body limitation/failure cue | In Counting, even with Sentry stabilization (Transient Memory w/ Sentry), the robot still fails (23%) due to the lack of persistence: without an explicit ... | p. 9 (4 Experiments) |
| body limitation/failure cue | It ensures that execution loops are eventually broken even when the Sentry fails to trigger. | p. 12 (4 Experiments) |
| body limitation/failure cue | Since the Sentry is prone to False Negatives (missing the "Done" event), we design a fixed-interval Planner fallback. | p. 12 (4 Experiments) |
| body limitation/failure cue | Without the Sentry, the Planner operates on a frame-by-frame style, and this high-frequency re-evaluation makes the robot hypersensitive to transient visual noise, leading to ... | p. 8 (4 Experiments) |
| body limitation/failure cue | HiMe consistently outperforms both text-only and image-only baselines across all three tasks, verifying the robustness of our cross-modal memory mechanism. | p. 10 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| To monitor the subtask progress, the Sentry 𝜋𝑠is queried after every 10 execution steps of 𝜋𝑒. | p. 8 (4 Experiments) |
| This ablation validates the sentry's role in reducing computational redundancy and aligning planning steps with the dynamics of environments. | p. 8 (4 Experiments) |
| To assess the need for dynamic memory management, we run an ablation against two baselines: (1) No Management, which only supports Add/Retrieve and keeps ... | p. 10 (4 Experiments) |
| However, these training-based methods are often constrained by limited context windows and the inherent difficulty of optimizing long-range causal dependencies over hundreds of steps. | p. 2 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 4 Experiments - extractive PDF cue:** The fundamental limitation of such contextual memory is the lack of consolidation: a simple FIFO queue cannot distinguish between truly critical frames and redundant observations.
- **p. 9 / 4 Experiments - extractive PDF cue:** In Counting, even with Sentry stabilization (Transient Memory w/ Sentry), the robot still fails (23%) due to the lack of persistence: without an explicit memory ...
- **p. 12 / 4 Experiments - extractive PDF cue:** It ensures that execution loops are eventually broken even when the Sentry fails to trigger.
- **p. 12 / 4 Experiments - extractive PDF cue:** Since the Sentry is prone to False Negatives (missing the "Done" event), we design a fixed-interval Planner fallback.
- **p. 8 / 4 Experiments - extractive PDF cue:** Without the Sentry, the Planner operates on a frame-by-frame style, and this high-frequency re-evaluation makes the robot hypersensitive to transient visual noise, leading to frequent, ...
- **p. 10 / 4 Experiments - extractive PDF cue:** HiMe consistently outperforms both text-only and image-only baselines across all three tasks, verifying the robustness of our cross-modal memory mechanism.

- **PDF anchors reviewed:** datasets p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments), metrics p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 7 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), baselines p. 9 (4 Experiments), p. 10 (4 Experiments), p. 8 (4 Experiments), p. 10 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), results p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
