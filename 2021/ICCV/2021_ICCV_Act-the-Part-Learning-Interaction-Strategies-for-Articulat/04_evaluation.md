# Evaluation - Act the Part: Learning Interaction Strategies for Articulated Object Part Discovery

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2105.01047; PDF retrieval source: https://arxiv.org/pdf/2105.01047. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (4.2. Benchmark Results), p. 7 (4.2. Benchmark Results), p. 7 (4.2. Benchmark Results), p. 8 (4.3. Real World Results), p. 5 (4.2. Benchmark Results), p. 6 (4.2. Benchmark Results)): While other algorithms' performance saturate quickly with one or two interactions, [Ours-Touch] and [Ours-NoTouch] are able to improve with more interactions.

## Evaluation Body Digest

- **p. 5 / 4. Evaluation - extractive body cue:** Dataset, test initialization, and pre-trained models will be released for reproducibility and benchmarking.
- **p. 8 / 4.3. Real World Results - extractive body cue:** To validate performance independent of robot execution accuracy, a human is instructed to execute the actions.
- **p. 6 / 4.2. Benchmark Results - extractive body cue:** Our network learns a policy to interact with unseen objects and categories.
- **p. 7 / 4.2. Benchmark Results - extractive body cue:** Results on two unseen object categories show our methods (pink and brown) approach the oracle baseline over time.
- **p. 7 / 4.2. Benchmark Results - extractive body cue:** Our algorithm does not make category-level assumptions, therefore the same policy and perception model should work for unseen object categories with different kinematic structures.
- **p. 8 / 4.3. Real World Results - extractive body cue:** Since our algorithm does not need prior knowledge of objects or special sensory input during inference, we can directly test our learned model on real ...
- **p. 5 / 4. Evaluation - extractive body cue:** The multilink objects have three links in a chain similar to eyeglasses.
- **p. 6 / 4.2. Benchmark Results - extractive body cue:** While it is only trained on objects with two part, it also learns to reason about three part objects.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Evaluation (p. 5); 4.2. Benchmark Results (p. 5); 4.3. Real World Results (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Benchmark Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | While other algorithms' performance saturate quickly with one or two interactions, [Ours-Touch] and [Ours-NoTouch] are able to improve with more interactions. | p. 5 (4.2. Benchmark Results) |
| 4.2. Benchmark Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Furthermore, this result suggests more complex perceptual modules are necessary to get push-only policies to achieve competitive performance at this task. | p. 7 (4.2. Benchmark Results) |
| 4.2. Benchmark Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | 2, we see that [Ours-Touch] outperforms [Ours-NoTouch] in most categories. | p. 7 (4.2. Benchmark Results) |
| 4.3. Real World Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | To validate performance independent of robot execution accuracy, a human is instructed to execute the actions. | p. 8 (4.3. Real World Results) |
| 4.2. Benchmark Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | We also provide qualitative results in Fig. | p. 5 (4.2. Benchmark Results) |

## Dataset / Benchmark Role

- **p. 5 / 4. Evaluation - extractive body cue:** Dataset, test initialization, and pre-trained models will be released for reproducibility and benchmarking.
- **p. 8 / 4.3. Real World Results - extractive body cue:** To validate performance independent of robot execution accuracy, a human is instructed to execute the actions.
- **p. 6 / 4.2. Benchmark Results - extractive body cue:** Our network learns a policy to interact with unseen objects and categories.
- **p. 7 / 4.2. Benchmark Results - extractive body cue:** Results on two unseen object categories show our methods (pink and brown) approach the oracle baseline over time.
- **p. 7 / 4.2. Benchmark Results - extractive body cue:** Our algorithm does not make category-level assumptions, therefore the same policy and perception model should work for unseen object categories with different kinematic structures.
- **p. 8 / 4.3. Real World Results - extractive body cue:** Since our algorithm does not need prior knowledge of objects or special sensory input during inference, we can directly test our learned model on real ...
- **p. 5 / 4. Evaluation - extractive body cue:** The multilink objects have three links in a chain similar to eyeglasses.
- **p. 6 / 4.2. Benchmark Results - extractive body cue:** While it is only trained on objects with two part, it also learns to reason about three part objects.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Interaction for Part Discovery. Passive part segmenta- tion algorithms require detailed annotation and cannot generalize to new categories. While motion can help discover ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Model overview. (a) The interaction network computes hold and push from an image observation and current part mem- ory. The physics simulator gives ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Interaction network. Given an image and the current belief of part segmentation, our network predicts a hold and a push conditioned on the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. Part network. Given a pair of observations and the action that caused the change, this network predicts motion masks aligned to each observation. ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1. Reward Calculation. N/A indicates no backpropagation due to insufficient information. For more details refer to Appx. C. and a mask V c, relative ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. Qualitative Results. Our network learns a policy to interact with unseen objects and categories. While it is only trained on objects with two ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Perception performance. MAPE [frac] / dH95 [pixels] / mIoU [%]. Image resolution is 90 × 90. Numbers are evaluated after the fifth interaction. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6. IoU w.r.t. Interaction Steps. Results on two unseen object categories show our methods (pink and brown) approach the oracle baseline over time.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Dataset, test initialization, and pre-trained models will be released for reproducibility and benchmarking. | embodiment, simulator version and control stack | p. 5 (4. Evaluation), p. 8 (4.3. Real World Results) |
| Task/environment | To validate performance independent of robot execution accuracy, a human is instructed to execute the actions. | reset, timeout, object/scene variation | p. 8 (4.3. Real World Results), p. 6 (4.2. Benchmark Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3.2. Learning to Act to Discover Parts), p. 2 (3.1. Problem Formulation) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The metric penalizes both errors in mask prediction and failure to discover masks (e.g. if one of two parts is discovered, maximum IoU is ... | definition/direction/unit from same section | p. 5 (4.1. Metrics and Points of Comparison) |
| We conjecture this is due to the benefit of using touch signal to define more specific reward cases and to make reward more dense, ... | definition/direction/unit from same section | p. 7 (4.2. Benchmark Results) |
| IoU performance on the multilink category is better than on eyeglasses; however, MAPE is comparable, suggesting that eyeglasses are particularly challenging for reasons other ... | definition/direction/unit from same section | p. 7 (4.2. Benchmark Results) |
| To validate performance independent of robot execution accuracy, a human is instructed to execute the actions. | definition/direction/unit from same section | p. 8 (4.3. Real World Results) |
| In example (a), we pick various hold positions and analyze the "push right" reward prediction maps (recall: pushing is conditioned on holding). | definition/direction/unit from same section | p. 8 (4.3. Real World Results) |
| Part-aware Intersection over Union (IoU). | definition/direction/unit from same section | p. 5 (4.1. Metrics and Points of Comparison) |
| Our interaction network takes the current belief of the part segmentation as input and obtains reward for new part discovery. | definition/direction/unit from same section | p. 6 (4.2. Benchmark Results) |
| (compared to upper bounds using ground truth state), they are informative for discovering new parts of the object and self-correct errors over time. | definition/direction/unit from same section | p. 6 (4.2. Benchmark Results) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Results on two unseen object categories show our methods (pink and brown) approach the oracle baseline over time. | comparison identity and matched condition | p. 7 (4.2. Benchmark Results) |
| We also design two oracle algorithms using simulation state to provide performance upper bounds: • GT-Act: Optimal action based on ground truth state, but ... | comparison identity and matched condition | p. 5 (4.1. Metrics and Points of Comparison) |
| (compared to upper bounds using ground truth state), they are informative for discovering new parts of the object and self-correct errors over time. | comparison identity and matched condition | p. 6 (4.2. Benchmark Results) |
| 2, we see that [Ours-Touch] outperforms [Ours-NoTouch] in most categories. | comparison identity and matched condition | p. 7 (4.2. Benchmark Results) |
| We compare the AtP framework trained with and without touch reward, [Ours-Touch] and [Ours-NoTouch] respectively, with the following alternative approaches to study the efficacy ... | comparison identity and matched condition | p. 5 (4.1. Metrics and Points of Comparison) |
| Without any fine-tuning, the algorithm shows promising results on inferring interaction strategies and reasoning about the observed motion for part discovery. | comparison identity and matched condition | p. 8 (4.3. Real World Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Without any fine-tuning, the algorithm shows promising results on inferring interaction strategies and reasoning about the observed motion for part discovery. | component/input/data sensitivity | p. 8 (4.3. Real World Results) |
| In this experiment, we want to evaluate the effect of touch feedback. | component/input/data sensitivity | p. 7 (4.2. Benchmark Results) |
| To provide a better metric for these structures, we measure dH95, which is a part-aware variant of a common metric in medical image segmentation ... | component/input/data sensitivity | p. 5 (4.1. Metrics and Points of Comparison) |
| We compare the AtP framework trained with and without touch reward, [Ours-Touch] and [Ours-NoTouch] respectively, with the following alternative approaches to study the efficacy ... | component/input/data sensitivity | p. 5 (4.1. Metrics and Points of Comparison) |
| However, we are still able to learn helpful interaction strategies even without touch. | component/input/data sensitivity | p. 7 (4.2. Benchmark Results) |
| Figure 3. Interaction network. Given an image and the current belief of part segmentation, our network predicts a hold and a push conditioned on ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address these challenges, we introduce Act the Part | While other algorithms' performance saturate quickly with one or two interactions, [Ours-Touch] and [Ours-NoTouch] are able to improve with more interactions. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (4.2. Benchmark Results), p. 7 (4.2. Benchmark Results), p. 7 (4.2. Benchmark Results), p. 8 (4.3. Real World Results), p. 5 (4.2. Benchmark Results), p. 6 (4.2. Benchmark Results) |
| Primary metric/result | Furthermore, this result suggests more complex perceptual modules are necessary to get push-only policies to achieve competitive performance at this task. | numeric claim only at cited anchor | p. 7 (4.2. Benchmark Results) |

- Numeric sentences retained from the body:
- **p. 5 / 4.2. Benchmark Results - extractive body cue:** As expected, the upper bounds peaks at 2 and 3 steps for pliers and multilink, respectively.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The metric penalizes both errors in mask prediction and failure to discover masks (e.g. if one of two parts is discovered, maximum IoU is ... | p. 5 (4.1. Metrics and Points of Comparison) |
| body limitation/failure cue | G for more real world experiment results and failure case analysis. | p. 8 (4.3. Real World Results) |
| body limitation/failure cue | Figure 13. Failure Modes. (a) On three link objects our model sometimes struggles to split parts that have been grouped together in the part ... | p. 14 (Figure/Table caption) |
| body limitation/failure cue | Figure 1. Interaction for Part Discovery. Passive part segmenta- tion algorithms require detailed annotation and cannot generalize to new categories. While motion can help ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | We see broad scope for future work including extensions to 3D part segmentation and singular frameworks for rigid, articulated, and deformable object understanding. | p. 8 (5. Conclusion and Future Work) |
| body limitation/failure cue | Due to space limitation, only three interaction steps are shown in this figure. | p. 6 (4.2. Benchmark Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We compute the average of perceptual metrics for each category at every timestep over five models trained with different random seeds. | p. 5 (4.1. Metrics and Points of Comparison) |
| To evaluate, we plot the part mIoU w.r.t. interaction steps in Fig. | p. 5 (4.2. Benchmark Results) |
| Due to space limitation, only three interaction steps are shown in this figure. | p. 6 (4.2. Benchmark Results) |
| (a) The interaction network computes hold and push from an image observation and current part memory. | p. 3 (3.1. Problem Formulation) |
| 3, we use a shared ResNet18 [16] with two residual decoder heads wired with U-Net [39] skip connections. | p. 3 (3.2. Learning to Act to Discover Parts) |
| We compute the L2-norm of the flow field and normalize by the max value. | p. 4 (3.5. Reward) |
| The network is comprised of a shared encoder with two decoder heads to predict Mt and Mt+1. | p. 4 (3.3. Learning to Discover Parts from Action) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 4.1. Metrics and Points of Comparison - extractive body cue:** The metric penalizes both errors in mask prediction and failure to discover masks (e.g. if one of two parts is discovered, maximum IoU is 50%).
- **p. 8 / 4.3. Real World Results - extractive body cue:** G for more real world experiment results and failure case analysis.
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 13. Failure Modes. (a) On three link objects our model sometimes struggles to split parts that have been grouped together in the part memory. ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Interaction for Part Discovery. Passive part segmenta- tion algorithms require detailed annotation and cannot generalize to new categories. While motion can help discover ...
- **p. 8 / 5. Conclusion and Future Work - extractive body cue:** We see broad scope for future work including extensions to 3D part segmentation and singular frameworks for rigid, articulated, and deformable object understanding.
- **p. 6 / 4.2. Benchmark Results - extractive body cue:** Due to space limitation, only three interaction steps are shown in this figure.

- **Evidence anchors reviewed:** datasets p. 5 (4. Evaluation), p. 8 (4.3. Real World Results), p. 6 (4.2. Benchmark Results), p. 7 (4.2. Benchmark Results), p. 7 (4.2. Benchmark Results), p. 8 (4.3. Real World Results), metrics p. 5 (4.1. Metrics and Points of Comparison), p. 7 (4.2. Benchmark Results), p. 7 (4.2. Benchmark Results), p. 8 (4.3. Real World Results), p. 8 (4.3. Real World Results), p. 5 (4.1. Metrics and Points of Comparison), baselines p. 7 (4.2. Benchmark Results), p. 5 (4.1. Metrics and Points of Comparison), p. 6 (4.2. Benchmark Results), p. 7 (4.2. Benchmark Results), p. 5 (4.1. Metrics and Points of Comparison), p. 8 (4.3. Real World Results), results p. 5 (4.2. Benchmark Results), p. 7 (4.2. Benchmark Results), p. 7 (4.2. Benchmark Results), p. 8 (4.3. Real World Results), p. 5 (4.2. Benchmark Results), p. 6 (4.2. Benchmark Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Results on two unseen object categories show our methods (pink and brown) approach the oracle baseline over time. (p. 7, 4.2. Benchmark Results).
- **Metric evidence:** The metric penalizes both errors in mask prediction and failure to discover masks (e.g. if one of two parts is discovered, maximum IoU is 50%). (p. 5, 4.1. Metrics and Points of Comparison).
- **Baseline/ablation evidence:** Results on two unseen object categories show our methods (pink and brown) approach the oracle baseline over time. (p. 7, 4.2. Benchmark Results).
- **Failure/negative evidence:** The metric penalizes both errors in mask prediction and failure to discover masks (e.g. if one of two parts is discovered, maximum IoU is 50%). (p. 5, 4.1. Metrics and Points of Comparison).
