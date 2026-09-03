# Evaluation - π0.5: a Vision-Language-Action Model with Open-World Generalization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v305/black25a.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/black25a/black25a.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 20 (Figure/Table caption), p. 24 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption)): Figure 10: Comparing π0.5 with other models. Our full model significantly outperforms both π0 and π0-FAST+Flow in the mock home test environments. We compare π0.5 to π0 as well as ...

## Evaluation Body Digest

- **p. 1 / Abstract - extractive body cue:** We describe π0.5, a new model based on π0 that uses co-training on heterogeneous tasks to enable broad generalization. π0.5 uses data from multiple robots, ...
- **p. 2 / 1 Introduction - extractive body cue:** We leverage this observation to design a co-training framework for VLAs that can utilize heterogeneous and diverse knowledge sources to enable broad generalization, creating the ...
- **p. 1 / Abstract - extractive body cue:** A: Chocolate Deploy in new homes out-of-the-box Fold laundry Figure 1: The π0.5 model transfers knowledge from a heterogeneous range of data sources, including other ...
- **p. 2 / 1 Introduction - extractive body cue:** Given general tasks (close the cabinets, put the items in the drawer, wipe the spill, and put the dishes in the sink), the model predicts ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7: Evaluating language following with dif- ferent numbers of training locations. We evalu- ate language following rate and success rate for pick- ing up ...
- **p. 24 / Figure/Table caption - extractive body cue:** Figure 18: Per-task performance breakdown for high-level inference methods. We evaluate the full π0.5 model and various high-level inference baselines across four representative household tasks. ...
- **p. 1 / Abstract - extractive body cue:** While vision-language-action (VLA) models have demonstrated impressive results for end-to-end robot control, it remains an open question how far such models can generalize in the ...
- **p. 1 / Abstract - extractive body cue:** Our experiments show that this kind of knowledge transfer is essential for effective generalization, and we demonstrate for the first time that an end-to-end learning-enabled ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** C Task evaluation rubric (p. 19).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 10: Comparing π0.5 with other models. Our full model significantly outperforms both π0 and π0-FAST+Flow in the mock home test environments. We compare ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 6: Evaluating performance with different numbers of locations. Performance over the four test tasks - "dishes in sink", "items in drawer", "laundry basket", ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 13: Robot system overview. We use two mobile manipulator platforms - each has four cameras (for- ward, backward, and both wrists), two 6 ... | p. 20 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 18: Per-task performance breakdown for high-level inference methods. We evaluate the full π0.5 model and various high-level inference baselines across four representative household ... | p. 24 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 7: Evaluating language following with dif- ferent numbers of training locations. We evalu- ate language following rate and success rate for pick- ing ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 1 / Abstract - extractive body cue:** We describe π0.5, a new model based on π0 that uses co-training on heterogeneous tasks to enable broad generalization. π0.5 uses data from multiple robots, ...
- **p. 2 / 1 Introduction - extractive body cue:** We leverage this observation to design a co-training framework for VLAs that can utilize heterogeneous and diverse knowledge sources to enable broad generalization, creating the ...
- **p. 1 / Abstract - extractive body cue:** A: Chocolate Deploy in new homes out-of-the-box Fold laundry Figure 1: The π0.5 model transfers knowledge from a heterogeneous range of data sources, including other ...
- **p. 2 / 1 Introduction - extractive body cue:** Given general tasks (close the cabinets, put the items in the drawer, wipe the spill, and put the dishes in the sink), the model predicts ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: The π0.5 model transfers knowledge from a heterogeneous range of data sources, including other robots, high-level subtask prediction, verbal instructions, and data from ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: π0.5 cleaning a new kitchen. The robot is tasked with cleaning a kitchen in a home that was not in the training data. ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Model overview. π0.5 is trained in two stages. First, a pre-training stage combines all of the different data sources to produce an initial ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Evaluation environments. We evaluate π0.5 in entirely new kitchens and bedrooms that were not seen during training, with novel objects, backgrounds, and layouts. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Evaluation in real homes. We evaluated π0.5 in three kitchens and three bedrooms in real homes that were not seen during training. We ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6: Evaluating performance with different numbers of locations. Performance over the four test tasks - "dishes in sink", "items in drawer", "laundry basket", "make ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7: Evaluating language following with dif- ferent numbers of training locations. We evalu- ate language following rate and success rate for pick- ing up ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 8: Training recipe ablations. We ablate parts of the training mixture on four test tasks (10 trials per task). Including cross-embodiment data, both in ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We describe π0.5, a new model based on π0 that uses co-training on heterogeneous tasks to enable broad generalization. π0.5 uses data from multiple ... | embodiment, simulator version and control stack | p. 1 (Abstract), p. 2 (1 Introduction) |
| Task/environment | We leverage this observation to design a co-training framework for VLAs that can utilize heterogeneous and diverse knowledge sources to enable broad generalization, creating ... | reset, timeout, object/scene variation | p. 2 (1 Introduction), p. 1 (Abstract) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 1 (Abstract) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (1 Introduction), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 7: Evaluating language following with dif- ferent numbers of training locations. We evalu- ate language following rate and success rate for pick- ing ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 18: Per-task performance breakdown for high-level inference methods. We evaluate the full π0.5 model and various high-level inference baselines across four representative household ... | definition/direction/unit from same section | p. 24 (Figure/Table caption) |
| While vision-language-action (VLA) models have demonstrated impressive results for end-to-end robot control, it remains an open question how far such models can generalize in ... | definition/direction/unit from same section | p. 1 (Abstract) |
| Our experiments show that this kind of knowledge transfer is essential for effective generalization, and we demonstrate for the first time that an end-to-end ... | definition/direction/unit from same section | p. 1 (Abstract) |
| Figure 5: Evaluation in real homes. We evaluated π0.5 in three kitchens and three bedrooms in real homes that were not seen during training. ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 9: Training recipe ablations. We evaluate language following with in-distribution (ID) and out- of-distribution (OOD) objects. Including web data (WD) is important for ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 8: Training recipe ablations. We ablate parts of the training mixture on four test tasks (10 trials per task). Including cross-embodiment data, both ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 16: Evaluation of the high-level inference process. While the full π0.5 model with high-level and low-level inference attains the best results, using only ... | definition/direction/unit from same section | p. 22 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 6: Evaluating performance with different numbers of locations. Performance over the four test tasks - "dishes in sink", "items in drawer", "laundry basket", ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 18: Per-task performance breakdown for high-level inference methods. We evaluate the full π0.5 model and various high-level inference baselines across four representative household ... | comparison identity and matched condition | p. 24 (Figure/Table caption) |
| Figure 15: Comparing π0.5 with other models on language following. We evaluate language following capabilities of π0.5 , π0, and π0-FAST+Flow, finding π0.5 outperforms ... | comparison identity and matched condition | p. 22 (Figure/Table caption) |
| Figure 10: Comparing π0.5 with other models. Our full model significantly outperforms both π0 and π0-FAST+Flow in the mock home test environments. We compare ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Our experiments and comparisons further show that this is enabled by transferring knowledge from other robots, high-level semantic prediction, verbal language instruction from human ... | comparison identity and matched condition | p. 2 (1 Introduction) |
| Figure 4: Evaluation environments. We evaluate π0.5 in entirely new kitchens and bedrooms that were not seen during training, with novel objects, backgrounds, and ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 18: Per-task performance breakdown for high-level inference methods. We evaluate the full π0.5 model and various high-level inference baselines across four representative household ... | component/input/data sensitivity | p. 24 (Figure/Table caption) |
| Figure 17: Per-task performance breakdown for training recipe ablations. We evaluate each training mix- ture variant on four representative household tasks: Items in Drawer, ... | component/input/data sensitivity | p. 23 (Figure/Table caption) |
| Figure 6: Evaluating performance with different numbers of locations. Performance over the four test tasks - "dishes in sink", "items in drawer", "laundry basket", ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Figure 9: Training recipe ablations. We evaluate language following with in-distribution (ID) and out- of-distribution (OOD) objects. Including web data (WD) is important for ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 8: Training recipe ablations. We ablate parts of the training mixture on four test tasks (10 trials per task). Including cross-embodiment data, both ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Our central contribution is a system for training a highly generalizable VLA, π0.5, together with a proof of concept that generalization can emerge from ... | component/input/data sensitivity | p. 2 (1 Introduction) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our central contribution is a system for training a highly generalizable VLA, π0.5, together with a proof of concept that generalization can emerge from ... | Figure 10: Comparing π0.5 with other models. Our full model significantly outperforms both π0 and π0-FAST+Flow in the mock home test environments. We compare ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 20 (Figure/Table caption), p. 24 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Primary metric/result | Figure 6: Evaluating performance with different numbers of locations. Performance over the four test tasks - "dishes in sink", "items in drawer", "laundry basket", ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 2 / 1 Introduction - extractive body cue:** We leverage this observation to design a co-training framework for VLAs that can utilize heterogeneous and diverse knowledge sources to enable broad generalization, creating the ...
- **p. 2 / 1 Introduction - extractive body cue:** We leverage this observation to design a co-training framework for VLAs that can utilize heterogeneous and diverse knowledge sources to enable broad generalization, creating the ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Web data (WD) does not make a significant difference, but we will see in Figures 9, 16 that it impacts object generalization and high-level ... | p. 8 (2 Related Work) |
| body limitation/failure cue | As expected, the performance on indistribution objects improves more quickly than that of out-of-distribution objects. | p. 7 (2 Related Work) |
| body limitation/failure cue | Performance increases steadily as we increase the number of training locations. standard rubric in Appendix C and (2) a more fine-grained evaluation of each ... | p. 7 (2 Related Work) |
| body limitation/failure cue | For both experiments we see in the results that excluding either of the two cross-embodiment data sources significantly degrades performance, indicating that π0.5 benefits ... | p. 8 (2 Related Work) |
| body limitation/failure cue | Figure 17: Per-task performance breakdown for training recipe ablations. We evaluate each training mix- ture variant on four representative household tasks: Items in Drawer, ... | p. 23 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Open-world generalization represents one of the biggest open problems in physical intelligence, and scalable learning systems offer a path to enable such generalization, as ... | p. 1 (1 Introduction) |
| The heterogeneity of these different sources of data present a major obstacle, but recent advances in vision-language-action (VLA) models provide us with a toolkit ... | p. 2 (1 Introduction) |
| Our central contribution is a system for training a highly generalizable VLA, π0.5, together with a proof of concept that generalization can emerge from ... | p. 2 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 2 Related Work - extractive body cue:** Web data (WD) does not make a significant difference, but we will see in Figures 9, 16 that it impacts object generalization and high-level performance.
- **p. 7 / 2 Related Work - extractive body cue:** As expected, the performance on indistribution objects improves more quickly than that of out-of-distribution objects.
- **p. 7 / 2 Related Work - extractive body cue:** Performance increases steadily as we increase the number of training locations. standard rubric in Appendix C and (2) a more fine-grained evaluation of each model's ...
- **p. 8 / 2 Related Work - extractive body cue:** For both experiments we see in the results that excluding either of the two cross-embodiment data sources significantly degrades performance, indicating that π0.5 benefits considerably ...
- **p. 23 / Figure/Table caption - extractive body cue:** Figure 17: Per-task performance breakdown for training recipe ablations. We evaluate each training mix- ture variant on four representative household tasks: Items in Drawer, Dishes ...

- **Evidence anchors reviewed:** datasets p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), metrics p. 7 (Figure/Table caption), p. 24 (Figure/Table caption), p. 1 (Abstract), p. 1 (Abstract), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), baselines p. 7 (Figure/Table caption), p. 24 (Figure/Table caption), p. 22 (Figure/Table caption), p. 8 (Figure/Table caption), p. 2 (1 Introduction), p. 6 (Figure/Table caption), results p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 20 (Figure/Table caption), p. 24 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (24 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 18: Per-task performance breakdown for high-level inference methods. We evaluate the full π0.5 model and various high-level inference baselines across four representative household tasks. For Items in Drawer and ... (p. 24, Figure/Table caption).
- **Metric evidence:** Figure 17: Per-task performance breakdown for training recipe ablations. We evaluate each training mix- ture variant on four representative household tasks: Items in Drawer, Dishes in Sink, Laundry Basket, and ... (p. 23, Figure/Table caption).
- **Baseline/ablation evidence:** Figure 6: Evaluating performance with different numbers of locations. Performance over the four test tasks - "dishes in sink", "items in drawer", "laundry basket", "make bed" - improves with more ... (p. 7, Figure/Table caption).
- **Failure/negative evidence:** Some evaluations include cancelled episodes due to robot failures, time limitations or other causes, which are removed. (p. 20, 3 DoF holonomic base).
