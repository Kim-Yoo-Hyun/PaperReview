# Evaluation - Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2004.02857; PDF retrieval source: https://arxiv.org/pdf/2004.02857. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 12 (5 Experiments), p. 12 (5 Experiments), p. 11 (5 Experiments), p. 15 (5 Experiments), p. 13 (5 Experiments), p. 13 (5 Experiments)): Despite having no learned components nor processing any input, both these agents achieve approximately 3% success rates in val-unseen.

## Evaluation Body Digest

- **p. 13 / 5 Experiments - extractive body cue:** This Cross-Modal Attention PM+DA*+Aug model achieves an SPL of 0.35 on val-seen and 0.30 on val-unseen - succeeding on 32% of episodes in new environments.
- **p. 11 / 5 Experiments - extractive body cue:** Once again, we train to convergence on val-unseen (6 to 10 dataset collections, depending on the model).
- **p. 12 / 5 Experiments - extractive body cue:** Our baseline Seq2Seq model significantly outperforms the random and hand-crafted baselines, successfully reaching the goal in 20% of val-unseen episodes.
- **p. 14 / 5 Experiments - extractive body cue:** Qualitative examples of our Cross Modal Attention model taken in unseen validation environments.
- **p. 14 / 5 Experiments - extractive body cue:** Despite having similar cross-modal attention architectures, RCM [29] achieves an SPL of 0.38 in test environments while our model yields 5 Note that the VLN ...
- **p. 15 / 5 Experiments - extractive body cue:** Comparison on the VLN validation and test sets with existing models.
- **p. 11 / 5 Experiments - extractive body cue:** We report standard metrics for visual navigation tasks defined in [2,4,18] - trajectory length in meters (TL), navigation error in meters from goal at termination ...
- **p. 15 / 5 Experiments - extractive body cue:** Val-Seen (VLN) Val-Unseen (VLN) Test (VLN) Model TL ↓ NE ↓ OS ↑ SR ↑ SPL ↑ TL ↓ NE ↓ OS ↑ SR ↑ ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 5 Experiments (p. 11).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5 Experiments | BENCHMARK / DATASET | Despite having no learned components nor processing any input, both these agents achieve approximately 3% success rates in val-unseen. | p. 12 (5 Experiments) |
| 5 Experiments | BENCHMARK / DATASET | We find that depth is a very strong signal for learning, with models lacking it (No Depth and No Vision) failing to outperform chance ... | p. 12 (5 Experiments) |
| 5 Experiments | BENCHMARK / DATASET | For our discussion, we will examine success rate and SPL as the primary metrics for performance and use NDTW to describe how paths differ ... | p. 11 (5 Experiments) |
| 5 Experiments | BENCHMARK / DATASET | Even compensating for this possible underestimation, nav-graph-based approaches still outperform our continuous models significantly. | p. 15 (5 Experiments) |
| 5 Experiments | BENCHMARK / DATASET | We examine the validation performance of PM+Aug (row 11) and find it to outperform Aug or PM alone (by 0.02-0.03 SPL). | p. 13 (5 Experiments) |

## Dataset / Benchmark Role

- **p. 13 / 5 Experiments - extractive body cue:** This Cross-Modal Attention PM+DA*+Aug model achieves an SPL of 0.35 on val-seen and 0.30 on val-unseen - succeeding on 32% of episodes in new environments.
- **p. 11 / 5 Experiments - extractive body cue:** Once again, we train to convergence on val-unseen (6 to 10 dataset collections, depending on the model).
- **p. 12 / 5 Experiments - extractive body cue:** Our baseline Seq2Seq model significantly outperforms the random and hand-crafted baselines, successfully reaching the goal in 20% of val-unseen episodes.
- **p. 14 / 5 Experiments - extractive body cue:** Qualitative examples of our Cross Modal Attention model taken in unseen validation environments.
- **p. 14 / 5 Experiments - extractive body cue:** Despite having similar cross-modal attention architectures, RCM [29] achieves an SPL of 0.38 in test environments while our model yields 5 Note that the VLN ...
- **p. 15 / 5 Experiments - extractive body cue:** Comparison on the VLN validation and test sets with existing models.
- **p. 11 / 5 Experiments - extractive body cue:** We report standard metrics for visual navigation tasks defined in [2,4,18] - trajectory length in meters (TL), navigation error in meters from goal at termination ...
- **p. 15 / 5 Experiments - extractive body cue:** Val-Seen (VLN) Val-Unseen (VLN) Test (VLN) Model TL ↓ NE ↓ OS ↑ SR ↑ SPL ↑ TL ↓ NE ↓ OS ↑ SR ↑ ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1. The VLN setting (a) operates on a fixed topology of panoramic images (shown in blue) - assuming perfect navigation between nodes (often meters ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1. Comparison of language-guided visual navigation tasks. Ours is the only to provide unconstrained navigation in real environments for crowdsourced instructions. Task Instructions Environment ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 2. We transfer nav-graph trajectories over panoramas (blue dots) from the Room-to- Room (R2R) dataset to locations in reconstructed Matterport3D (MP3D) environments. Some map ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 3. We successfully transfer 77% of the R2R trajectories. (a) Most panorama nodes transfer directly, but 3% require horizontal adjustment - with an average ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 4. We develop a simple baseline agent (a) as well as an attentional agent (b) comparable to that in [29]. Both receive RGB and ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 2. No-learning baselines and input modality ablations for our baseline sequence- to-sequence model. Given the long trajectories involved, we find both random agents and ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 3. Performance in VLN-CE. We find that popular techniques in VLN have mixed benefit in VLN-CE; however, our best performing model combining all examined ...
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 5. Qualitative examples of our Cross Modal Attention model taken in unseen vali- dation environments. In the first example our agent successfully follows the ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This Cross-Modal Attention PM+DA*+Aug model achieves an SPL of 0.35 on val-seen and 0.30 on val-unseen - succeeding on 32% of episodes in new ... | embodiment, simulator version and control stack | p. 13 (5 Experiments), p. 11 (5 Experiments) |
| Task/environment | Once again, we train to convergence on val-unseen (6 to 10 dataset collections, depending on the model). | reset, timeout, object/scene variation | p. 11 (5 Experiments), p. 12 (5 Experiments) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 1 (1 Introduction), p. 1 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We report standard metrics for visual navigation tasks defined in [2,4,18] - trajectory length in meters (TL), navigation error in meters from goal at ... | definition/direction/unit from same section | p. 11 (5 Experiments) |
| For our discussion, we will examine success rate and SPL as the primary metrics for performance and use NDTW to describe how paths differ ... | definition/direction/unit from same section | p. 11 (5 Experiments) |
| In contrast, a similar hand-crafted random-heading-and-forward model in VLN yields a 16.3% success rate [4]. | definition/direction/unit from same section | p. 12 (5 Experiments) |
| Despite having no learned components nor processing any input, both these agents achieve approximately 3% success rates in val-unseen. | definition/direction/unit from same section | p. 12 (5 Experiments) |
| We examine the validation performance of PM+Aug (row 11) and find it to outperform Aug or PM alone (by 0.02-0.03 SPL). | definition/direction/unit from same section | p. 13 (5 Experiments) |
| Finally, we examine the performance of DA*+Aug (row 12) and find that this outperforms DA (by 0.01-0.02 SPL), but is unable to match pre-training ... | definition/direction/unit from same section | p. 13 (5 Experiments) |
| Despite having similar cross-modal attention architectures, RCM [29] achieves an SPL of 0.38 in test environments while our model yields 5 Note that the ... | definition/direction/unit from same section | p. 14 (5 Experiments) |
| 4 shows these effects account for a drop of approximately 10 SPL. | definition/direction/unit from same section | p. 15 (5 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our baseline Seq2Seq model significantly outperforms the random and hand-crafted baselines, successfully reaching the goal in 20% of val-unseen episodes. | comparison identity and matched condition | p. 12 (5 Experiments) |
| We find the cross-modal attention model outperforms the Seq2Seq baseline under all settings for new environments. | comparison identity and matched condition | p. 13 (5 Experiments) |
| As illustrated in [27], models examining only single modalities can be very strong baselines in embodied tasks. | comparison identity and matched condition | p. 12 (5 Experiments) |
| 5.3 Examining the Impact of the Nav-Graph in VLN To draw a direct comparison between the VLN and VLN-CE settings, we convert trajectories taken ... | comparison identity and matched condition | p. 14 (5 Experiments) |
| 5.1 Establishing Baseline Performance for VLN-CE No-Learning Baselines. | comparison identity and matched condition | p. 11 (5 Experiments) |
| For DAgger [24], we collect the nth set by taking the oracle action with probability β=0.75n and the current policy action otherwise. | comparison identity and matched condition | p. 11 (5 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We believe that depth enable agents to quickly begin traversing environments effectively (e.g. without collisions) and without this it is very difficult to bootstrap ... | component/input/data sensitivity | p. 12 (5 Experiments) |
| Seq2Seq and Single-Modality Ablations. | component/input/data sensitivity | p. 12 (5 Experiments) |
| We find that without data augmentation, the progress monitor over-fits considerably more (validation loss of 0.67 vs. | component/input/data sensitivity | p. 13 (5 Experiments) |
| Specifically, we pretrain with imitation learning, data augmentation, and the progress monitoring loss, then finetune using DAgger (with β=0.75n+1) on the original data. | component/input/data sensitivity | p. 13 (5 Experiments) |
| Fig. 4. We develop a simple baseline agent (a) as well as an attentional agent (b) comparable to that in [29]. Both receive RGB ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, we develop a continuous setting that enables these types of studies and take a first step towards integrating VLN agents with ... | Despite having no learned components nor processing any input, both these agents achieve approximately 3% success rates in val-unseen. | PDF body cue; verify exact table/figure and matched conditions | p. 12 (5 Experiments), p. 12 (5 Experiments), p. 11 (5 Experiments), p. 15 (5 Experiments), p. 13 (5 Experiments), p. 13 (5 Experiments) |
| Primary metric/result | We find that depth is a very strong signal for learning, with models lacking it (No Depth and No Vision) failing to outperform chance ... | numeric claim only at cited anchor | p. 12 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 11 / 5 Experiments - extractive body cue:** We train on all ground-truth paths until convergence on val-unseen (at most 30 epochs).
- **p. 11 / 5 Experiments - extractive body cue:** We collect 5, 000 trajectories at each stage and then perform 4 epochs of imitation learning (with inflection weighting) over all collected trajectories.
- **p. 15 / 5 Experiments - extractive body cue:** Further, state-of-the-art on the test set is near 0.47 SPL, over 2x what we report.
- **p. 3 / 1 Introduction - extractive body cue:** Agents in our task are free to navigate to any unobstructed point through a set of low-level actions (e.g. move forward 0.25m, turn-left 15 degrees) ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The second example shows a failure of the agent - it navigates towards the wrong windows and fails to first "pass the kitchen" - ... | p. 14 (5 Experiments) |
| body limitation/failure cue | We also observe failures when the agent never sees the object(s) referred to by the instruction in the scene - with a limited egocentric ... | p. 14 (5 Experiments) |
| body limitation/failure cue | In models presented here, we took an approach where observations were mapped directly to low-level control in an end-to-end manner; however, exploring modular approaches ... | p. 15 (6 Discussion) |
| body limitation/failure cue | We believe that depth enable agents to quickly begin traversing environments effectively (e.g. without collisions) and without this it is very difficult to bootstrap ... | p. 12 (5 Experiments) |
| body limitation/failure cue | By default, our models cannot succeed on these. | p. 15 (5 Experiments) |
| body limitation/failure cue | Fig. 2. We transfer nav-graph trajectories over panoramas (blue dots) from the Room-to- Room (R2R) dataset to locations in reconstructed Matterport3D (MP3D) environments. Some ... | p. 7 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We utilize the Adam optimizer [15] with a learning rate of 2.5 × 10-4 and a batch size of 5 full trajectories. | p. 11 (5 Experiments) |
| We train on all ground-truth paths until convergence on val-unseen (at most 30 epochs). | p. 11 (5 Experiments) |
| Most works use this data to encode precise geometry between nodes in the nav-graph as part of the decision making process, e.g. moving 30°W ... | p. 2 (1 Introduction) |
| In this work, we focus in on the Vision-and-Language Navigation (VLN) [4] task and lift these implicit assumptions by instantiating it in continuous 3D ... | p. 3 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 14 / 5 Experiments - extractive body cue:** The second example shows a failure of the agent - it navigates towards the wrong windows and fails to first "pass the kitchen" - stopping ...
- **p. 14 / 5 Experiments - extractive body cue:** We also observe failures when the agent never sees the object(s) referred to by the instruction in the scene - with a limited egocentric field-of-view, ...
- **p. 15 / 6 Discussion - extractive body cue:** In models presented here, we took an approach where observations were mapped directly to low-level control in an end-to-end manner; however, exploring modular approaches is ...
- **p. 12 / 5 Experiments - extractive body cue:** We believe that depth enable agents to quickly begin traversing environments effectively (e.g. without collisions) and without this it is very difficult to bootstrap to ...
- **p. 15 / 5 Experiments - extractive body cue:** By default, our models cannot succeed on these.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 2. We transfer nav-graph trajectories over panoramas (blue dots) from the Room-to- Room (R2R) dataset to locations in reconstructed Matterport3D (MP3D) environments. Some map ...

- **Evidence anchors reviewed:** datasets p. 13 (5 Experiments), p. 11 (5 Experiments), p. 12 (5 Experiments), p. 14 (5 Experiments), p. 14 (5 Experiments), p. 15 (5 Experiments), metrics p. 11 (5 Experiments), p. 11 (5 Experiments), p. 12 (5 Experiments), p. 12 (5 Experiments), p. 13 (5 Experiments), p. 13 (5 Experiments), baselines p. 12 (5 Experiments), p. 13 (5 Experiments), p. 12 (5 Experiments), p. 14 (5 Experiments), p. 11 (5 Experiments), p. 11 (5 Experiments), results p. 12 (5 Experiments), p. 12 (5 Experiments), p. 11 (5 Experiments), p. 15 (5 Experiments), p. 13 (5 Experiments), p. 13 (5 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
