# Evaluation - Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Peng_Counterfactual_VLA_Self-Reflective_Vision-Language-Action_Model_with_Adaptive_Reasoning_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Peng_Counterfactual_VLA_Self-Reflective_Vision-Language-Action_Model_with_Adaptive_Reasoning_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 1 (Figure/Table caption), p. 6 (4.2. Main Experiments), p. 6 (4.2. Main Experiments), p. 7 (4.2. Main Experiments), p. 8 (4.4. Qualitative Results), p. 4 (Figure/Table caption)): Figure 1. Counterfactual Vision-Language-Action (CF-VLA) Model. Top: CF-VLA conducts reasoning adaptively. The model engages in reasoning more frequently and achieves more signifi- cant task performance gains in complex scenarios that ...

## Evaluation Body Digest

- **p. 5 / 4.1. Experimental Setup - extractive body cue:** The counterfactual reasoning dataset DCF comes from the training set of Dmeta.
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** The entire data corpus forms the trajectory-only dataset Dtraj, which contains raw sensor data paired with ego-vehicle future trajectories.
- **p. 6 / 4.2. Main Experiments - extractive body cue:** Importantly, the secondround models trained on 3 datasets reduce the think rate by almost half and shorten the average output length.
- **p. 6 / 4.2. Main Experiments - extractive body cue:** After the second CF training round, CF-VLA (w/ route, round2, 3 datasets) further reduces the think rate by roughly 40-45% while maintaining or improving average ...
- **p. 7 / 4.2. Main Experiments - extractive body cue:** Ablations on meta-trajectory alignment and adaptive counterfactual reasoning.
- **p. 7 / 4.2. Main Experiments - extractive body cue:** Model MinADE↓ AvgADE↓ MinFDE↓ AvgFDE↓ MinIOU↑ (init →edited) Corner Dist.↓ Output Length Think Rate CF-VLA (filtered ds) 0.6712 1.4574 1.7988 3.9466 0.9207→0.9231 0.6010 125.67 0.2190 ...
- **p. 8 / 4.4. Qualitative Results - extractive body cue:** CF-VLA consistently identifies when its initial intent is misaligned with the scene and corrects it before trajectory generation.
- **p. 8 / 4.4. Qualitative Results - extractive body cue:** These cases show that CF-VLA's self-reflection produces targeted, scene-grounded corrections that improve safety, traffic efficiency, and semantic consistency.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** 3.4. Implementation Details (p. 5); 4. Experiments (p. 5); 4.1. Experimental Setup (p. 5); 4.2. Main Experiments (p. 6); 4.4. Qualitative Results (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 1. Counterfactual Vision-Language-Action (CF-VLA) Model. Top: CF-VLA conducts reasoning adaptively. The model engages in reasoning more frequently and achieves more signifi- cant task ... | p. 1 (Figure/Table caption) |
| 4.2. Main Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | We evaluate whether counterfactual reasoning improves trajectory accuracy, safety characteristics, and reasoning quality. | p. 6 (4.2. Main Experiments) |
| 4.2. Main Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Compared with lang-meta-act, which reasons for every sample, CF-VLA (w/ route, round1) already achieves better performance with a think rate below 0.25. | p. 6 (4.2. Main Experiments) |
| 4.2. Main Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | CF-VLA achieves better error reduction when the scenarios are harder, suggesting that CF-VLA not only reasons adaptively but learns when reasoning is most beneficial. | p. 7 (4.2. Main Experiments) |
| 4.4. Qualitative Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | These cases show that CF-VLA's self-reflection produces targeted, scene-grounded corrections that improve safety, traffic efficiency, and semantic consistency. | p. 8 (4.4. Qualitative Results) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Experimental Setup - extractive body cue:** The counterfactual reasoning dataset DCF comes from the training set of Dmeta.
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** The entire data corpus forms the trajectory-only dataset Dtraj, which contains raw sensor data paired with ego-vehicle future trajectories.
- **p. 6 / 4.2. Main Experiments - extractive body cue:** Importantly, the secondround models trained on 3 datasets reduce the think rate by almost half and shorten the average output length.
- **p. 6 / 4.2. Main Experiments - extractive body cue:** After the second CF training round, CF-VLA (w/ route, round2, 3 datasets) further reduces the think rate by roughly 40-45% while maintaining or improving average ...
- **p. 7 / 4.2. Main Experiments - extractive body cue:** Ablations on meta-trajectory alignment and adaptive counterfactual reasoning.
- **p. 7 / 4.2. Main Experiments - extractive body cue:** Model MinADE↓ AvgADE↓ MinFDE↓ AvgFDE↓ MinIOU↑ (init →edited) Corner Dist.↓ Output Length Think Rate CF-VLA (filtered ds) 0.6712 1.4574 1.7988 3.9466 0.9207→0.9231 0.6010 125.67 0.2190 ...
- **p. 8 / 4.4. Qualitative Results - extractive body cue:** CF-VLA consistently identifies when its initial intent is misaligned with the scene and corrects it before trajectory generation.
- **p. 8 / 4.4. Qualitative Results - extractive body cue:** These cases show that CF-VLA's self-reflection produces targeted, scene-grounded corrections that improve safety, traffic efficiency, and semantic consistency.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Counterfactual Vision-Language-Action (CF-VLA) Model. Top: CF-VLA conducts reasoning adaptively. The model engages in reasoning more frequently and achieves more signifi- cant task performance ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. The framework of CF-VLA. A base VLA is fine- tuned on a counterfactual reasoning dataset generated by a roll- out-filter-label pipeline. The resulting ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. (A) Adaptive Reasoning can be achieved by training models on a mixture of data with the unified instruction prompt. (B) Data generation process. ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. The dataset composition. We use a subset of the meta- action-labeled dataset Dmeta as the validation set Dval. samples form the counterfactual reasoning ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Evaluation results. CF-VLA improves trajectory accuracy (ADE, FDE), behavioral safety (Corner Distance, Collision, Off-road), and reasoning quality (IOU). ↓lower is better, ↑higher is ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Ablations on meta-trajectory alignment and adaptive counterfactual reasoning. We train models without route information.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Effect of our proposed data filtering pipeline. Models are fine-tuned with route information from meta-act (w/ route).
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Qualitative results of CF-VLA. For three representative and safety-critical scenarios, each row shows the model's initial meta- actions (left), the reasoning trace (middle), ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The counterfactual reasoning dataset DCF comes from the training set of Dmeta. | embodiment, simulator version and control stack | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup) |
| Task/environment | The entire data corpus forms the trajectory-only dataset Dtraj, which contains raw sensor data paired with ego-vehicle future trajectories. | reset, timeout, object/scene variation | p. 5 (4.1. Experimental Setup), p. 6 (4.2. Main Experiments) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 3 (3. Method), p. 1 (1. Introduction) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 4 (3.3. Rollout-Filter-Label Counterfactual Pipeline), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We evaluate models along three dimensions: 1) Trajectory Accuracy: We report MinADE/AvgADE and MinFDE/AvgFDE as mean/endpoint displacement errors over 6 predicted modes (lower is ... | definition/direction/unit from same section | p. 5 (4.1. Experimental Setup) |
| CF-VLA improves trajectory accuracy (ADE, FDE), behavioral safety (Corner Distance, Collision, Off-road), and reasoning quality (IOU). ↓lower is better, ↑higher is better. | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |
| With route information, CF-VLA (w/ route, round2, 3 ds) slightly trades minimum error for better average ADE/FDE and higher IOU, and further improves collision ... | definition/direction/unit from same section | p. 6 (4.2. Main Experiments) |
| Model MinADE↓ AvgADE↓ MinFDE↓ AvgFDE↓ MinIOU↑ (init →edited) Corner Dist.↓ Output Length Think Rate CF-VLA (filtered ds) 0.6712 1.4574 1.7988 3.9466 0.9207→0.9231 0.6010 125.67 ... | definition/direction/unit from same section | p. 7 (4.2. Main Experiments) |
| Figure 1. Counterfactual Vision-Language-Action (CF-VLA) Model. Top: CF-VLA conducts reasoning adaptively. The model engages in reasoning more frequently and achieves more signifi- cant task ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| For CFVLA, we report IOU after self-reflection, i.e., for the updated meta-actions. | definition/direction/unit from same section | p. 5 (4.1. Experimental Setup) |
| CF-VLA achieves better error reduction when the scenarios are harder, suggesting that CF-VLA not only reasons adaptively but learns when reasoning is most beneficial. | definition/direction/unit from same section | p. 7 (4.2. Main Experiments) |
| Figure 3. (A) Adaptive Reasoning can be achieved by training models on a mixture of data with the unified instruction prompt. (B) Data generation ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| With route information, meta-act (w/ route) provides an even stronger baseline. | comparison identity and matched condition | p. 6 (4.2. Main Experiments) |
| Compared to their non-reasoning counterparts, CF-VLA variants consistently improve both trajectory error and meta-action alignment. | comparison identity and matched condition | p. 6 (4.2. Main Experiments) |
| Model MinADE↓ AvgADE↓ MinFDE↓ AvgFDE↓ MinIOU↑ (init →edited) Corner Dist.↓ Output Length Think Rate meta-act (baseline) 0.8411 1.6216 2.3647 4.6616 0.9169 0.7720 85.32 - ... | comparison identity and matched condition | p. 7 (4.2. Main Experiments) |
| We train models without route information. | comparison identity and matched condition | p. 7 (4.2. Main Experiments) |
| Figure 2. The framework of CF-VLA. A base VLA is fine- tuned on a counterfactual reasoning dataset generated by a roll- out-filter-label pipeline. The ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Within each setting (with / without route), CF-VLA variants consistently achieve the lowest or near-lowest collision and off-road rates, indicating that counterfactual self-reflection translates ... | component/input/data sensitivity | p. 6 (4.2. Main Experiments) |
| We prepare two variants of the models to train with or without route information, which contain 20 waypoints spanning the future 80m with equal ... | component/input/data sensitivity | p. 6 (4.1. Experimental Setup) |
| Table 2. Ablations on meta-trajectory alignment and adaptive counterfactual reasoning. We train models without route information. | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Effect of our proposed data filtering pipeline. | component/input/data sensitivity | p. 7 (4.2. Main Experiments) |
| Figure 2. The framework of CF-VLA. A base VLA is fine- tuned on a counterfactual reasoning dataset generated by a roll- out-filter-label pipeline. The ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| We unfreeze all parameters during training. | component/input/data sensitivity | p. 5 (3.4. Implementation Details) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Second, standard training pipelines rarely teach models to answer counterfactual questions such as: "Given the plan I just proposed, what will happen, and how ... | Figure 1. Counterfactual Vision-Language-Action (CF-VLA) Model. Top: CF-VLA conducts reasoning adaptively. The model engages in reasoning more frequently and achieves more signifi- cant task ... | PDF body cue; verify exact table/figure and matched conditions | p. 1 (Figure/Table caption), p. 6 (4.2. Main Experiments), p. 6 (4.2. Main Experiments), p. 7 (4.2. Main Experiments), p. 8 (4.4. Qualitative Results), p. 4 (Figure/Table caption) |
| Primary metric/result | We evaluate whether counterfactual reasoning improves trajectory accuracy, safety characteristics, and reasoning quality. | numeric claim only at cited anchor | p. 6 (4.2. Main Experiments) |

- Numeric sentences retained from the body:
- **p. 5 / 3.4. Implementation Details - extractive body cue:** A wide (120°) and a telephoto (30°) cameras provide 2 videos at 2 Hz over the past 2 s.
- **p. 5 / 3.4. Implementation Details - extractive body cue:** The past 1.6 s of ego motion is embedded into a single trajectory-history token by an MLP-based trajectory history encoder.
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** We train and evaluate models on a large proprietary dataset consisting of 80,000 hours of human driving data from 25 countries, covering a variety of ...
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** Within Dtraj, we auto-labeled 3,000 hours of data and constructed the meta-action-labeled subset Dmeta.
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** We label meta-actions at 10Hz over the balanced dataset curated based on Operational Design Domains (ODDs).
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** The training set of Dmeta includes 433K 20s clips and 801K 8.4s samples.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | A rollout-filter-label counterfactual pipeline allows CF-VLA to mine its own failure cases and improve over multiple training rounds. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Experiments on large-scale driving datasets show consistent gains in trajectory accuracy, safety, and reasoning quality, demonstrating up to 17.6% lower trajectory error and 20.5% ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | 2) Safety Characteristics: Collision Rate measures the proportion of predicted trajectories that collide with other road users' trajectories within 5s, while Out-of-road Rate quantifies ... | p. 5 (4.1. Experimental Setup) |
| body limitation/failure cue | Model ADE↓ Min (Avg) FDE↓ Min (Avg) Corner Dist.↓ Collision↓ Off-road↓ IOU↑ init→edited Output Len. | p. 6 (4.1. Experimental Setup) |
| body limitation/failure cue | Relative to traj-only, the best CF models reduce collision rate by roughly 25-30% and off-road violations by about 15-20%, while also lowering corner distance ... | p. 6 (4.2. Main Experiments) |
| body limitation/failure cue | These complement distance-based metrics by revealing whether small deviations lead to unsafe outcomes. | p. 5 (4.1. Experimental Setup) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The past 1.6 s of ego motion is embedded into a single trajectory-history token by an MLP-based trajectory history encoder. | p. 5 (3.4. Implementation Details) |
| We also record Output Length (# tokens) and Think Rate, the fraction of responses containing counterfactual reasoning, to quantify the test-time compute and adaptive ... | p. 5 (4.1. Experimental Setup) |
| Reasoning inevitably increases sequence length compared to non-reasoning models, but CF-VLA uses test-time compute much more efficiently than models that always think. | p. 6 (4.2. Main Experiments) |
| This mechanism is essential because most scenarios are straightforward, and explicit reasoning on them increases hallucination risks and wastes test-time compute. | p. 3 (3.1. Self-Reflective Counterfactual Reasoning) |
| 2) Pre-filled metaactions xpf: the model is conditioned on the ground-truth meta-actions and only decodes the trajectory. | p. 4 (3.3. Rollout-Filter-Label Counterfactual Pipeline) |
| For each scene, two sets of trajectories are generated: 1) Free generation xfree: the model first predicts meta-actions and then decodes the trajectory conditioned ... | p. 4 (3.3. Rollout-Filter-Label Counterfactual Pipeline) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive body cue:** A rollout-filter-label counterfactual pipeline allows CF-VLA to mine its own failure cases and improve over multiple training rounds.
- **p. 8 / 5. Conclusion - extractive body cue:** Experiments on large-scale driving datasets show consistent gains in trajectory accuracy, safety, and reasoning quality, demonstrating up to 17.6% lower trajectory error and 20.5% lower ...
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** 2) Safety Characteristics: Collision Rate measures the proportion of predicted trajectories that collide with other road users' trajectories within 5s, while Out-of-road Rate quantifies whether ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** Model ADE↓ Min (Avg) FDE↓ Min (Avg) Corner Dist.↓ Collision↓ Off-road↓ IOU↑ init→edited Output Len.
- **p. 6 / 4.2. Main Experiments - extractive body cue:** Relative to traj-only, the best CF models reduce collision rate by roughly 25-30% and off-road violations by about 15-20%, while also lowering corner distance by ...
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** These complement distance-based metrics by revealing whether small deviations lead to unsafe outcomes.

- **PDF anchors reviewed:** datasets p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup), p. 6 (4.2. Main Experiments), p. 6 (4.2. Main Experiments), p. 7 (4.2. Main Experiments), p. 7 (4.2. Main Experiments), metrics p. 5 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 6 (4.2. Main Experiments), p. 7 (4.2. Main Experiments), p. 1 (Figure/Table caption), p. 5 (4.1. Experimental Setup), baselines p. 6 (4.2. Main Experiments), p. 6 (4.2. Main Experiments), p. 7 (4.2. Main Experiments), p. 7 (4.2. Main Experiments), p. 3 (Figure/Table caption), results p. 1 (Figure/Table caption), p. 6 (4.2. Main Experiments), p. 6 (4.2. Main Experiments), p. 7 (4.2. Main Experiments), p. 8 (4.4. Qualitative Results), p. 4 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
