# Evaluation - Room-Across-Room: Multilingual Vision-and-Language Navigation with Dense Spatiotemporal Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://aclanthology.org/2020.emnlp-main.356/; PDF retrieval source: https://aclanthology.org/2020.emnlp-main.356.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5 Experiments), p. 9 (5 Experiments), p. 8 (Figure/Table caption), p. 7 (5 Experiments), p. 7 (5 Experiments), p. 6 (Figure/Table caption)): Applying the same approach to textual attention did not improve performance.

## Evaluation Body Digest

- **p. 7 / 5 Experiments - extractive body cue:** Monolingual Results Table 5 provides results on the val-unseen split for several training settings, as well as human performance from Follower annotations.
- **p. 8 / 5 Experiments - extractive body cue:** As one of the first large-scale spatially-temporally aligned language datasets, RxR offers new opportunities to extend this work from images to environments.
- **p. 9 / 5 Experiments - extractive body cue:** Test Set RxR includes a heldout test set, which we divide into two splits: test-standard and testchallenge.
- **p. 7 / 5 Experiments - extractive body cue:** (2020), we pretrain the CNN in an image-text dual encoder setting using the Conceptual Captions dataset (Sharma et al., 2018).
- **p. 8 / 5 Experiments - extractive body cue:** 8) performs best on both datasets, but domain differences thwart simple transfer learning (i.e., train on X, evaluate on Y). instruction-path pair is treated as ...
- **p. 9 / 5 Experiments - extractive body cue:** Method Vision Language en hi te en hi te en hi te en hi te (4) Multi ✓ ✓ 11.0 10.9 11.0 22.2 23.0 23.1 ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 4: Simple baselines on val-unseen paths. RxR proves more difficult than R2R overall, and less amenable to agents that tend to go straight (baselines ...
- **p. 7 / 5 Experiments - extractive body cue:** (2019), the reward at each step is the incremental difference in NDTW, plus a linear function of navigation error after stopping.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 5 Experiments (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5 Experiments | BENCHMARK / DATASET | Applying the same approach to textual attention did not improve performance. | p. 8 (5 Experiments) |
| 5 Experiments | BENCHMARK / DATASET | The multimodal agent (4) outperforms both the languageonly agent (9) and the vision-only agent (10), indicating that both modalities contribute to performance. | p. 9 (5 Experiments) |
| Figure/Table caption | BENCHMARK / DATASET | Table 5: RxR val-unseen: Monolingual vs. multilingual results. Training with both Guide and Follower paths benefits all languages (exp. 3 vs. 1 and 2), ... | p. 8 (Figure/Table caption) |
| 5 Experiments | BENCHMARK / DATASET | In preliminary experiments, we found that pretraining the CNN in this way gave noticeable improvements over the same CNN pretrained for image classification on ... | p. 7 (5 Experiments) |
| 5 Experiments | BENCHMARK / DATASET | Monolingual Results Table 5 provides results on the val-unseen split for several training settings, as well as human performance from Follower annotations. | p. 7 (5 Experiments) |

## Dataset / Benchmark Role

- **p. 7 / 5 Experiments - extractive body cue:** Monolingual Results Table 5 provides results on the val-unseen split for several training settings, as well as human performance from Follower annotations.
- **p. 8 / 5 Experiments - extractive body cue:** As one of the first large-scale spatially-temporally aligned language datasets, RxR offers new opportunities to extend this work from images to environments.
- **p. 9 / 5 Experiments - extractive body cue:** Test Set RxR includes a heldout test set, which we divide into two splits: test-standard and testchallenge.
- **p. 7 / 5 Experiments - extractive body cue:** (2020), we pretrain the CNN in an image-text dual encoder setting using the Conceptual Captions dataset (Sharma et al., 2018).
- **p. 8 / 5 Experiments - extractive body cue:** 8) performs best on both datasets, but domain differences thwart simple transfer learning (i.e., train on X, evaluate on Y). instruction-path pair is treated as ...
- **p. 9 / 5 Experiments - extractive body cue:** Method Vision Language en hi te en hi te en hi te en hi te (4) Multi ✓ ✓ 11.0 10.9 11.0 22.2 23.0 23.1 ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: RxR's instructions are densely grounded to the visual scene by aligning the annotator's virtual pose to their spoken instructions for navigating a path. ...
- **p. 2 / Figure/Table caption - extractive body cue:** Table 1: VLN dataset comparison. RxR is larger, multi- lingual, and includes dense spatiotemporal groundings (Ground) and follower demonstrations (Demos). led to a focus on ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Given the panorama navigation graph P with room graph R in Figure 2a, we sample a simple room path (r0, r2, r3) inducing ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: RxR's paths are longer on average than R2R's, exhibiting far greater variation in length (mea- sured in both meters and edges) while achieving ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4: Example spatiotemporal alignment of textual instructions, visual percepts and actions for an en-US Guide and the corresponding Follower. The next se- lected action ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2: RxR summary statistics. Times in seconds (s). In contrast, RxR's Guides speak and the tool logs their entire virtual camera pose sequence. We ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3: Linguistic phenomena in a manually annotated random sample of 25 paths from RxR and R2R. p is the % of sentences that contain ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Top: Instruction and path progress alignment for Guides and Followers. Bottom: Equirectangular heatmap of Guide and Follower camera poses, centered on their initial ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Monolingual Results Table 5 provides results on the val-unseen split for several training settings, as well as human performance from Follower annotations. | embodiment, simulator version and control stack | p. 7 (5 Experiments), p. 8 (5 Experiments) |
| Task/environment | As one of the first large-scale spatially-temporally aligned language datasets, RxR offers new opportunities to extend this work from images to environments. | reset, timeout, object/scene variation | p. 8 (5 Experiments), p. 9 (5 Experiments) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 5 (1 Introduction) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 6 (29. US English instructions are the longest on av), p. 5 (29. US English instructions are the longest on av) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 4: Simple baselines on val-unseen paths. RxR proves more difficult than R2R overall, and less amenable to agents that tend to go straight ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| (2019), the reward at each step is the incremental difference in NDTW, plus a linear function of navigation error after stopping. | definition/direction/unit from same section | p. 7 (5 Experiments) |
| Each minibatch is constructed from 50% behavioural cloning roll-outs (following the gold paths while minimizing crossentropy loss), and 50% policy gradient rollouts with reward ... | definition/direction/unit from same section | p. 7 (5 Experiments) |
| Spatiotemporal Grounding Supervision Table 5 experiment (6) incorporates a loss for spatiotemporal grounding over visual attention which gives mixed results on val-unseen (better on ... | definition/direction/unit from same section | p. 8 (5 Experiments) |
| Train Data SR ↑ SPL ↑ SDTW ↑ NDTW ↑ Exp. | definition/direction/unit from same section | p. 8 (5 Experiments) |
| The language-only agent is much better than random, but both modalities are required for best performance. | definition/direction/unit from same section | p. 9 (5 Experiments) |
| While the learned agent is clearly much better than a random agent, there is a great deal of headroom to reach human performance. | definition/direction/unit from same section | p. 9 (5 Experiments) |
| Figure 2: Given the panorama navigation graph P with room graph R in Figure 2a, we sample a simple room path (r0, r2, r3) ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 1 and 2), monolingual outperforms multilingual (exp. | comparison identity and matched condition | p. 8 (5 Experiments) |
| Spatiotemporal Grounding Supervision Table 5 experiment (6) incorporates a loss for spatiotemporal grounding over visual attention which gives mixed results on val-unseen (better on ... | comparison identity and matched condition | p. 8 (5 Experiments) |
| The multimodal agent (4) outperforms both the languageonly agent (9) and the vision-only agent (10), indicating that both modalities contribute to performance. | comparison identity and matched condition | p. 9 (5 Experiments) |
| Table 4: Simple baselines on val-unseen paths. RxR proves more difficult than R2R overall, and less amenable to agents that tend to go straight ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| In contrast, the vision-only model has no access to the instructions, without which the paths are highly random. | comparison identity and matched condition | p. 9 (5 Experiments) |
| Table 1: VLN dataset comparison. RxR is larger, multi- lingual, and includes dense spatiotemporal groundings (Ground) and follower demonstrations (Demos). led to a focus ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 7) is trained without data augmentation from model-generated instructions (Fried et al., 2018; Tan et al., 2019) and with hyperparameters tuned for RxR. | component/input/data sensitivity | p. 8 (5 Experiments) |
| In contrast, the vision-only model has no access to the instructions, without which the paths are highly random. | component/input/data sensitivity | p. 9 (5 Experiments) |
| This is likely because even without vision, parts of the instructions such as ‘turn left‘ and ‘go upstairs‘ still have meaning in the context ... | component/input/data sensitivity | p. 9 (5 Experiments) |
| (2020), we pretrain the CNN in an image-text dual encoder setting using the Conceptual Captions dataset (Sharma et al., 2018). | component/input/data sensitivity | p. 7 (5 Experiments) |
| However, since RxR instructions are much longer than R2R, we replace the bidirectional LSTM instruction encoder with a more parallelizable CNN encoder. | component/input/data sensitivity | p. 7 (5 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce Room-across-Room (RxR), a VLN dataset that addresses gaps in existing ones by (1) ∗First two.
| Primary metric/result | The multimodal agent (4) outperforms both the languageonly agent (9) and the vision-only agent (10), indicating that both modalities contribute to performance. | numeric claim only at cited anchor | p. 9 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 5 / 1 Introduction - extractive body cue:** We use a 640 × 480 pixel viewing canvas and a camera vertical field of view of 75 degrees.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Although RxR and R2R share the same underlying environments, we note that RxR →R2R cannot exploit R2R's | p. 8 (5 Experiments) |
| body limitation/failure cue | This is consistent with results in multilingual machine translation (MT) and automatic speech recognition (ASR) where adding more languages can also lead to degradation ... | p. 8 (5 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All agents are trained with Adam (Kingma and Ba, 2014) to convergence (100K iterations with batch size of 32 and initial learning rate of ... | p. 7 (5 Experiments) |
| The LSTM decoder computes an updated hidden state ht by conditioning on the previous selected action in at-1 and attending over the panoptic encoding ... | p. 7 (5 Experiments) |
| 7) is trained without data augmentation from model-generated instructions (Fried et al., 2018; Tan et al., 2019) and with hyperparameters tuned for RxR. | p. 8 (5 Experiments) |
| The dataset is available.1 We plan to release a test evaluation server, our annotation tool, and code for all experiments. | p. 2 (1 Introduction) |
| This especially matters for VLN, as different languages encode spatial and temporal information in idiosyncratic ways-e.g., how contact/support relationships are expressed (Munnich et al., ... | p. 2 (1 Introduction) |
| Guide Alignment Follower Alignment Now you are standing in-front of a closed door, turn to your left, you can see two wooden steps, climb ... | p. 4 (1 Introduction) |
| On average, Guide task annotations (including both steps, performed back-to-back) take 458 seconds. | p. 5 (1 Introduction) |
| Each simple baseline requires a stopping criteria; we choose to stop after N steps where N is the average number of steps in the ... | p. 6 (3. Given correct first step then go straight) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5 Experiments - extractive body cue:** Although RxR and R2R share the same underlying environments, we note that RxR →R2R cannot exploit R2R's
- **p. 8 / 5 Experiments - extractive body cue:** This is consistent with results in multilingual machine translation (MT) and automatic speech recognition (ASR) where adding more languages can also lead to degradation for ...

- **Evidence anchors reviewed:** datasets p. 7 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), metrics p. 6 (Figure/Table caption), p. 7 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), baselines p. 8 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 6 (Figure/Table caption), p. 9 (5 Experiments), p. 2 (Figure/Table caption), results p. 8 (5 Experiments), p. 9 (5 Experiments), p. 8 (Figure/Table caption), p. 7 (5 Experiments), p. 7 (5 Experiments), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
