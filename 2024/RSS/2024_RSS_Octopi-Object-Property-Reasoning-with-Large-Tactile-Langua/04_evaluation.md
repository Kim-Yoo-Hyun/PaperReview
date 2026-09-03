# Evaluation - Octopi: Object Property Reasoning with Large Tactile-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2405.02794; PDF retrieval source: https://arxiv.org/pdf/2405.02794. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (VI. EXPERIMENTAL RESULTS), p. 8 (VI. EXPERIMENTAL RESULTS), p. 6 (VI. EXPERIMENTAL RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS), p. 8 (VI. EXPERIMENTAL RESULTS)): For both OCTOPI7b and OCTOPI-13b, including the object property significantly improves performance, which supports our overall hypothesis that leveraging these properties is helpful for these tasks.

## Evaluation Body Digest

- **p. 6 / VI. EXPERIMENTAL RESULTS - extractive body cue:** To address the above questions, we evaluated OCTOPI using (i) accuracy on the physical understanding tasks in PHYSICLEAR's test set, (ii) accuracy on scenario reasoning ...
- **p. 7 / VI. EXPERIMENTAL RESULTS - extractive body cue:** Avocado Ripeness Classification To evaluate OCTOPI's usefulness as a tactile-grounded physical reasoning system for real world tasks, we integrated two GelSight sensors on a 7-DoF ...
- **p. 8 / VI. EXPERIMENTAL RESULTS - extractive body cue:** PG-InstructBLIP was trained to infer a predetermined set of physical properties from visual images of real objects in the EgoObjects dataset [65].
- **p. 7 / VI. EXPERIMENTAL RESULTS - extractive body cue:** At test time, the Franka robot grasped each avocado once to collect the tactile readings, before passing it to the model.
- **p. 8 / VI. EXPERIMENTAL RESULTS - extractive body cue:** Unlike the PHYSICLEAR dataset, these tactile videos are collected with only pressing and without any rotation.
- **p. 8 / VI. EXPERIMENTAL RESULTS - extractive body cue:** OCTOPI-13b has a higher combined accuracy (i.e. all three physical properties are correctly predicted for a given object) when compared to OCTOPI-7b, suggesting there are ...
- **p. 8 / VI. EXPERIMENTAL RESULTS - extractive body cue:** OCTOPI-13b obtains a ripeness prediction accuracy of 63.00%.
- **p. 7 / VI. EXPERIMENTAL RESULTS - extractive body cue:** For both OCTOPI7b and OCTOPI-13b, including the object property significantly improves performance, which supports our overall hypothesis that leveraging these properties is helpful for these ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** contact-rich manipulation scene.
- **Input boundary:** tactile image/force, vision과 proprioceptive history.
- **Output/decision under evaluation:** grasp/contact action, force command 또는 object motion.
- **Primary target:** slip/contact success, force/pose error와 robustness.
- **Detected evaluation headings:** V. EXPERIMENTAL SETUP (p. 6); VI. EXPERIMENTAL RESULTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| VI. EXPERIMENTAL RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | For both OCTOPI7b and OCTOPI-13b, including the object property significantly improves performance, which supports our overall hypothesis that leveraging these properties is helpful for ... | p. 7 (VI. EXPERIMENTAL RESULTS) |
| VI. EXPERIMENTAL RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | For avocado property prediction, OCTOPI-13b achieves an accuracy of 35.50%, which is significantly higher than that of the random baseline (3.70%). | p. 8 (VI. EXPERIMENTAL RESULTS) |
| VI. EXPERIMENTAL RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | To address the above questions, we evaluated OCTOPI using (i) accuracy on the physical understanding tasks in PHYSICLEAR's test set, (ii) accuracy on scenario ... | p. 6 (VI. EXPERIMENTAL RESULTS) |
| VI. EXPERIMENTAL RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | This suggests that OCTOPI's physical understanding improves significantly with LLM size. | p. 7 (VI. EXPERIMENTAL RESULTS) |
| VI. EXPERIMENTAL RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Using the CLIP fine-tuned on property prediction improves OCTOPI's performance in property prediction. | p. 8 (VI. EXPERIMENTAL RESULTS) |

## Dataset / Benchmark Role

- **p. 6 / VI. EXPERIMENTAL RESULTS - extractive body cue:** To address the above questions, we evaluated OCTOPI using (i) accuracy on the physical understanding tasks in PHYSICLEAR's test set, (ii) accuracy on scenario reasoning ...
- **p. 7 / VI. EXPERIMENTAL RESULTS - extractive body cue:** Avocado Ripeness Classification To evaluate OCTOPI's usefulness as a tactile-grounded physical reasoning system for real world tasks, we integrated two GelSight sensors on a 7-DoF ...
- **p. 8 / VI. EXPERIMENTAL RESULTS - extractive body cue:** PG-InstructBLIP was trained to infer a predetermined set of physical properties from visual images of real objects in the EgoObjects dataset [65].
- **p. 7 / VI. EXPERIMENTAL RESULTS - extractive body cue:** At test time, the Franka robot grasped each avocado once to collect the tactile readings, before passing it to the model.
- **p. 8 / VI. EXPERIMENTAL RESULTS - extractive body cue:** Unlike the PHYSICLEAR dataset, these tactile videos are collected with only pressing and without any rotation.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Avocado ripeness selection by combining tactile information with commonsense knowledge. Using inputs from its tactile sensor, OCTOPI identifies the left avocado as softer. ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2. PHYSICLEAR and OCTOPI (with key contributions starred). We collect tactile videos for everyday household objects by hand with two exploratory procedures: pressing and ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. OCTOPI Framework. Our framework consists of CLIP's vi- sual encoder, a projection module with two linear layers, and Vicuna v1.5 as the LLM. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4. Rice (Cooked v.s. Uncooked) Reasoning. OCTOPI-13b is prompted to reason about whether a scoop of rice is more likely to be cooked or ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5. Toothbrush Part Reasoning. Given a tactile video of a toothbrush's handle and the same toothbrush's bristles, OCTOPI-13b is prompted to reason which tactile ...
- **p. 17 / Figure/Table caption - extractive body cue:** Fig. 6. Confusion Matrices for the CLIP Classifier's Physical Property Predictions. We visualize the confusion matrices for the fine-tuned CLIP classifier's physical property predictions on ...
- **p. 17 / Figure/Table caption - extractive body cue:** Fig. 7. Visualizations of CLIP Visual Encoder's Embeddings. We visualize the fine-tuned CLIP visual encoder's output embeddings for each tactile video sample for each physical ...
- **p. 17 / Figure/Table caption - extractive body cue:** Fig. 8. Cropped Avocado Image for Vision-only Property Prediction. PG-InstructBLIP is not trained on our three physical prop- erties and we find that it never ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To address the above questions, we evaluated OCTOPI using (i) accuracy on the physical understanding tasks in PHYSICLEAR's test set, (ii) accuracy on scenario ... | embodiment, simulator version and control stack | p. 6 (VI. EXPERIMENTAL RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS) |
| Task/environment | Avocado Ripeness Classification To evaluate OCTOPI's usefulness as a tactile-grounded physical reasoning system for real world tasks, we integrated two GelSight sensors on a ... | reset, timeout, object/scene variation | p. 7 (VI. EXPERIMENTAL RESULTS), p. 8 (VI. EXPERIMENTAL RESULTS) |
| Observation/sensor | tactile image/force, vision과 proprioceptive history | calibration, preprocessing, privileged input | p. 4 (III. PHYSICLEAR - TACTILE AND PHYSICAL), p. 1 (I. INTRODUCTION) |
| Output/decision | grasp/contact action, force command 또는 object motion | action frame, controller and termination | p. 1 (Abstract), p. 3 (III. PHYSICLEAR - TACTILE AND PHYSICAL) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| To address the above questions, we evaluated OCTOPI using (i) accuracy on the physical understanding tasks in PHYSICLEAR's test set, (ii) accuracy on scenario ... | definition/direction/unit from same section | p. 6 (VI. EXPERIMENTAL RESULTS) |
| OCTOPI-13b has a higher combined accuracy (i.e. all three physical properties are correctly predicted for a given object) when compared to OCTOPI-7b, suggesting there ... | definition/direction/unit from same section | p. 8 (VI. EXPERIMENTAL RESULTS) |
| OCTOPI-13b obtains a ripeness prediction accuracy of 63.00%. | definition/direction/unit from same section | p. 8 (VI. EXPERIMENTAL RESULTS) |
| For both OCTOPI7b and OCTOPI-13b, including the object property significantly improves performance, which supports our overall hypothesis that leveraging these properties is helpful for ... | definition/direction/unit from same section | p. 7 (VI. EXPERIMENTAL RESULTS) |
| Avocado Ripeness Classification To evaluate OCTOPI's usefulness as a tactile-grounded physical reasoning system for real world tasks, we integrated two GelSight sensors on a ... | definition/direction/unit from same section | p. 7 (VI. EXPERIMENTAL RESULTS) |
| Fig. 8. Cropped Avocado Image for Vision-only Property Prediction. PG-InstructBLIP is not trained on our three physical prop- erties and we find that it ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| OCTOPI13b outperforms OCTOPI-7b by 6.96% on PC, 9.33% on PSS and 16.04% on POM. | comparison identity and matched condition | p. 7 (VI. EXPERIMENTAL RESULTS) |
| Interestingly, we observed that the 7b model marginally outperformed the 13b model. | comparison identity and matched condition | p. 7 (VI. EXPERIMENTAL RESULTS) |
| OCTOPI-7b and OCTOPI-13b perform above the random baseline for object property predictions and have similar performance to the finetuned CLIP. | comparison identity and matched condition | p. 8 (VI. EXPERIMENTAL RESULTS) |
| For avocado property prediction, OCTOPI-13b achieves an accuracy of 35.50%, which is significantly higher than that of the random baseline (3.70%). | comparison identity and matched condition | p. 8 (VI. EXPERIMENTAL RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Further, we explored the effect of using physical property descriptions by fine-tuning both OCTOPI-7b and OCTOPI13b on the physical understanding tasks without intermediate physical ... | component/input/data sensitivity | p. 7 (VI. EXPERIMENTAL RESULTS) |
| CLIP Fine-tuning Ablation Results on Object Property Prediction. | component/input/data sensitivity | p. 8 (VI. EXPERIMENTAL RESULTS) |
| It reasons about the rice state correctly without being trained to do so. | component/input/data sensitivity | p. 7 (VI. EXPERIMENTAL RESULTS) |
| Unlike the PHYSICLEAR dataset, these tactile videos are collected with only pressing and without any rotation. | component/input/data sensitivity | p. 8 (VI. EXPERIMENTAL RESULTS) |
| Fig. 2. PHYSICLEAR and OCTOPI (with key contributions starred). We collect tactile videos for everyday household objects by hand with two exploratory procedures: pressing ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| Fig. 6. Confusion Matrices for the CLIP Classifier's Physical Property Predictions. We visualize the confusion matrices for the fine-tuned CLIP classifier's physical property predictions ... | component/input/data sensitivity | p. 17 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| PHYSICLEAR and OCTOPI (with key contributions starred). | For both OCTOPI7b and OCTOPI-13b, including the object property significantly improves performance, which supports our overall hypothesis that leveraging these properties is helpful for ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (VI. EXPERIMENTAL RESULTS), p. 8 (VI. EXPERIMENTAL RESULTS), p. 6 (VI. EXPERIMENTAL RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS), p. 8 (VI. EXPERIMENTAL RESULTS) |
| Primary metric/result | For avocado property prediction, OCTOPI-13b achieves an accuracy of 35.50%, which is significantly higher than that of the random baseline (3.70%). | numeric claim only at cited anchor | p. 8 (VI. EXPERIMENTAL RESULTS) |

- Numeric sentences retained from the body:
- **p. 4 / III. PHYSICLEAR - TACTILE AND PHYSICAL - extractive body cue:** This division resulted in 60 objects for training and 7 objects each for validation and testing.
- **p. 6 / IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED - extractive body cue:** Specifically, we attach 8 task-specific learnable prompts and a shared linear layer to the input sequence of each Transformer [51] layer in the visual encoder ...
- **p. 6 / 3) Can OCTOPI's understanding of the physical properties - extractive body cue:** We randomly sampled 5 frames from these salient frames during training and selected 5 frames at uniform intervals from the first salient frame during evaluation.
- **p. 6 / 3) Can OCTOPI's understanding of the physical properties - extractive body cue:** Training Hyperparameters Encoder fine-tuning was performed for 30 epochs using the AdamW optimizer [35] with no weight decay, a learning rate of 10-3, batch size ...
- **p. 6 / 3) Can OCTOPI's understanding of the physical properties - extractive body cue:** During tactile feature alignment, the projection module is trained using 8k PHYSICLEAR samples using the AdamW optimizer [35] with no weight decay, a learning rate ...
- **p. 6 / 3) Can OCTOPI's understanding of the physical properties - extractive body cue:** Training Requirements Encoder fine-tuning took 6 hours and required less than 5GB of GPU VRAM.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This suggests that OCTOPI-13b's physical property prediction capability is robust to differences in tactile exploratory procedures. | p. 8 (VI. EXPERIMENTAL RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Training Hyperparameters Encoder fine-tuning was performed for 30 epochs using the AdamW optimizer [35] with no weight decay, a learning rate of 10-3, batch ... | p. 6 (3) Can OCTOPI's understanding of the physical properties) |
| During tactile feature alignment, the projection module is trained using 8k PHYSICLEAR samples using the AdamW optimizer [35] with no weight decay, a learning ... | p. 6 (3) Can OCTOPI's understanding of the physical properties) |
| FT CLIP is the combination of the fine-tuned CLIP visual encoder and the three separate trained classification layers. | p. 8 (VI. EXPERIMENTAL RESULTS) |
| OCTOPI is a LLaMA-based [49, 50] LVLM (Vicuna [11]) equipped with a CLIP-based [39] tactile encoder, whose representations have been aligned via projection. | p. 1 (I. INTRODUCTION) |
| Our framework consists of CLIP's visual encoder, a projection module with two linear layers, and Vicuna v1.5 as the LLM. | p. 4 (III. PHYSICLEAR - TACTILE AND PHYSICAL) |
| The encoder's output is then mapped to the LLM's word embedding space using a projection module, typically consisting of one or two trainable layers. | p. 4 (IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED) |
| In the following, we describe each of these steps in greater detail. | p. 5 (IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED) |
| Encoder Fine-tuning Existing LVLM models take natural videos as input and can use CLIP's visual encoder without modification. | p. 5 (IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / VI. EXPERIMENTAL RESULTS - extractive body cue:** This suggests that OCTOPI-13b's physical property prediction capability is robust to differences in tactile exploratory procedures.

- **Evidence anchors reviewed:** datasets p. 6 (VI. EXPERIMENTAL RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS), p. 8 (VI. EXPERIMENTAL RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS), p. 8 (VI. EXPERIMENTAL RESULTS), metrics p. 6 (VI. EXPERIMENTAL RESULTS), p. 8 (VI. EXPERIMENTAL RESULTS), p. 8 (VI. EXPERIMENTAL RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS), p. 17 (Figure/Table caption), baselines p. 7 (VI. EXPERIMENTAL RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS), p. 8 (VI. EXPERIMENTAL RESULTS), p. 8 (VI. EXPERIMENTAL RESULTS), results p. 7 (VI. EXPERIMENTAL RESULTS), p. 8 (VI. EXPERIMENTAL RESULTS), p. 6 (VI. EXPERIMENTAL RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS), p. 8 (VI. EXPERIMENTAL RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** To address the above questions, we evaluated OCTOPI using (i) accuracy on the physical understanding tasks in PHYSICLEAR's test set, (ii) accuracy on scenario reasoning tasks, (iii) task success rate ... (p. 6, VI. EXPERIMENTAL RESULTS).
- **Metric evidence:** To address the above questions, we evaluated OCTOPI using (i) accuracy on the physical understanding tasks in PHYSICLEAR's test set, (ii) accuracy on scenario reasoning tasks, (iii) task success rate ... (p. 6, VI. EXPERIMENTAL RESULTS).
- **Baseline/ablation evidence:** It reasons about the rice state correctly without being trained to do so. (p. 7, VI. EXPERIMENTAL RESULTS).
- **Failure/negative evidence:** The choice of these specific properties was also informed by the data collection methodology [27], tailored to the limitations and strengths of the GelSight sensor, including considerations for its sensitivity ... (p. 3, III. PHYSICLEAR - TACTILE AND PHYSICAL).
