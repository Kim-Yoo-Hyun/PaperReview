# Evaluation - CLIP-Fields: Weakly Supervised Semantic Fields for Robotic Memory

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2210.05663; PDF retrieval source: https://arxiv.org/pdf/2210.05663. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (V. EXPERIMENTAL EVALUATION), p. 7 (V. EXPERIMENTAL EVALUATION), p. 6 (V. EXPERIMENTAL EVALUATION), p. 7 (V. EXPERIMENTAL EVALUATION), p. 8 (V. EXPERIMENTAL EVALUATION), p. 8 (V. EXPERIMENTAL EVALUATION)): In Figure 5, we see once again that CLIP-Fields outperforms the RGB-based models significantly, to the point where even with three labelled views, CLIP-Fields has a higher AP than any ...

## Evaluation Body Digest

- **p. 5 / V. EXPERIMENTAL EVALUATION - extractive body cue:** Our visual segmentation experiments are performed on a subset of Habitat-Matterport 3D Semantic (HM3D semantics) [35] dataset, while our robot experiments were performed on a ...
- **p. 7 / V. EXPERIMENTAL EVALUATION - extractive body cue:** 9: Scenes for our real-world semantic navigation experiments.
- **p. 7 / V. EXPERIMENTAL EVALUATION - extractive body cue:** 2) Data collection and training: We ran our robot experiment in two different scenes, one in the lab kitchen, and another in the lab library ...
- **p. 8 / V. EXPERIMENTAL EVALUATION - extractive body cue:** 10: Examples of the robot's semantic navigation in two different testing environments, looking at objects given different queries.
- **p. 8 / V. EXPERIMENTAL EVALUATION - extractive body cue:** We consider the navigation task successful if the robot can navigate to and point the camera at an object that satisfies the query.
- **p. 5 / V. EXPERIMENTAL EVALUATION - extractive body cue:** We fine-tune the final layers of these pretrained models on each of our limited datasets, and then evaluate them on the held-out set.
- **p. 6 / V. EXPERIMENTAL EVALUATION - extractive body cue:** 7: Mean average accuracy on the semantic segmentation task on the HM3D Semantic dataset with label noise simulating errors in base labelling models.
- **p. 6 / V. EXPERIMENTAL EVALUATION - extractive body cue:** 5: Mean average precision in semantic segmentation on the Habitat-Matterport 3D (HM3D) Semantic dataset.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** V. EXPERIMENTAL EVALUATION (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTAL EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | In Figure 5, we see once again that CLIP-Fields outperforms the RGB-based models significantly, to the point where even with three labelled views, CLIP-Fields ... | p. 6 (V. EXPERIMENTAL EVALUATION) |
| V. EXPERIMENTAL EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | As the base models naturally improve over time with continuous efforts in the computer vision and natural language processing fields, we expect CLIP-Fields's performance ... | p. 7 (V. EXPERIMENTAL EVALUATION) |
| V. EXPERIMENTAL EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | As we can see in Figure 4, the average precision of the predictions retrieved from CLIP-Fields largely outperforms the RGB-models. | p. 6 (V. EXPERIMENTAL EVALUATION) |
| V. EXPERIMENTAL EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | By doing so, we simulate labelling our training data by a model whose mean accuracy is 1 -p. | p. 7 (V. EXPERIMENTAL EVALUATION) |
| V. EXPERIMENTAL EVALUATION | EMPIRICAL / REAL-ROBOT OR HARDWARE | We consider the navigation task successful if the robot can navigate to and point the camera at an object that satisfies the query. | p. 8 (V. EXPERIMENTAL EVALUATION) |

## Dataset / Benchmark Role

- **p. 5 / V. EXPERIMENTAL EVALUATION - extractive body cue:** Our visual segmentation experiments are performed on a subset of Habitat-Matterport 3D Semantic (HM3D semantics) [35] dataset, while our robot experiments were performed on a ...
- **p. 7 / V. EXPERIMENTAL EVALUATION - extractive body cue:** 9: Scenes for our real-world semantic navigation experiments.
- **p. 7 / V. EXPERIMENTAL EVALUATION - extractive body cue:** 2) Data collection and training: We ran our robot experiment in two different scenes, one in the lab kitchen, and another in the lab library ...
- **p. 8 / V. EXPERIMENTAL EVALUATION - extractive body cue:** 10: Examples of the robot's semantic navigation in two different testing environments, looking at objects given different queries.
- **p. 8 / V. EXPERIMENTAL EVALUATION - extractive body cue:** We consider the navigation task successful if the robot can navigate to and point the camera at an object that satisfies the query.
- **p. 5 / V. EXPERIMENTAL EVALUATION - extractive body cue:** We fine-tune the final layers of these pretrained models on each of our limited datasets, and then evaluate them on the held-out set.
- **p. 6 / V. EXPERIMENTAL EVALUATION - extractive body cue:** 7: Mean average accuracy on the semantic segmentation task on the HM3D Semantic dataset with label noise simulating errors in base labelling models.
- **p. 6 / V. EXPERIMENTAL EVALUATION - extractive body cue:** 5: Mean average precision in semantic segmentation on the Habitat-Matterport 3D (HM3D) Semantic dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Our approach, CLIP-Fields, integrates multiple views of a scene and can capture 3D semantics from relatively few examples. This results in a scalable ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Dataset creation process for CLIP-Fields by processing each frame of a collected RGB-D video. Models highlighted by dashed lines are off-the-shelf pre-trained models, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Model architecture for CLIP-Fields. We use a Multi-resolution Hash Encoder [20] to learn a low level spatial representation mapping R3 →Rd, which is ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Mean average precision in instance segmentation on the Habitat-Matterport 3D (HM3D) Semantic dataset, (top) calculated over only seen instances, and (bottom) calculated over ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Mean average precision in semantic segmentation on the Habitat-Matterport 3D (HM3D) Semantic dataset. Here, the average precision numbers are averaged over all semantic ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6: Mean average precision in zero-shot semantic segmentation on the Habitat-Matterport 3D (HM3D) Semantic dataset. 0.5 0.6 0.7 0.8 0.9 1.0
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 7: Mean average accuracy on the semantic segmentation task on the HM3D Semantic dataset with label noise simulating errors in base labelling models. Different ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 8: View localization using a trained CLIP-Fields. We encode the query image on the bottom left to its CLIP representation, and visualize the locations ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Our visual segmentation experiments are performed on a subset of Habitat-Matterport 3D Semantic (HM3D semantics) [35] dataset, while our robot experiments were performed on ... | embodiment, simulator version and control stack | p. 5 (V. EXPERIMENTAL EVALUATION), p. 7 (V. EXPERIMENTAL EVALUATION) |
| Task/environment | 9: Scenes for our real-world semantic navigation experiments. | reset, timeout, object/scene variation | p. 7 (V. EXPERIMENTAL EVALUATION), p. 7 (V. EXPERIMENTAL EVALUATION) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 1 (I. INTRODUCTION), p. 3 (IV. APPROACH) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 4 (IV. APPROACH), p. 4 (IV. APPROACH) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 7: Mean average accuracy on the semantic segmentation task on the HM3D Semantic dataset with label noise simulating errors in base labelling models. | definition/direction/unit from same section | p. 6 (V. EXPERIMENTAL EVALUATION) |
| Fig. 8: View localization using a trained CLIP-Fields. We encode the query image on the bottom left to its CLIP representation, and visualize the ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| For the RN50 FPN model, we report the mAP at [0.5-0.95] IoU range. | definition/direction/unit from same section | p. 5 (V. EXPERIMENTAL EVALUATION) |
| 4) CLIP-Fields's robustness to label errors: In real-world applications, CLIP-Fields relies on labels given by large | definition/direction/unit from same section | p. 6 (V. EXPERIMENTAL EVALUATION) |
| Thus, we can see that CLIP-Fields maintain reasonable accuracy as long as the base models are also reasonably accurate, which is the case for ... | definition/direction/unit from same section | p. 7 (V. EXPERIMENTAL EVALUATION) |
| Fig. 2: Dataset creation process for CLIP-Fields by processing each frame of a collected RGB-D video. Models highlighted by dashed lines are off-the-shelf pre-trained ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| These representations can once again be projected back into the camera frame to reconstruct the segmentation map predicted by CLIP-Fields. | definition/direction/unit from same section | p. 5 (V. EXPERIMENTAL EVALUATION) |
| We consider the navigation task successful if the robot can navigate to and point the camera at an object that satisfies the query. | definition/direction/unit from same section | p. 8 (V. EXPERIMENTAL EVALUATION) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In Figure 5, we see once again that CLIP-Fields outperforms the RGB-based models significantly, to the point where even with three labelled views, CLIP-Fields ... | comparison identity and matched condition | p. 6 (V. EXPERIMENTAL EVALUATION) |
| All baseline models were pre-trained on ImageNet-1K and then the COCO dataset. | comparison identity and matched condition | p. 5 (V. EXPERIMENTAL EVALUATION) |
| Baselines: In our semantic and instance segmentation tasks, we use 2D RGB based segmentation models as our baselines. | comparison identity and matched condition | p. 5 (V. EXPERIMENTAL EVALUATION) |
| Both CLIP-Fields and the baseline had access to the list of semantic labels in each scene with no extra annotations. | comparison identity and matched condition | p. 6 (V. EXPERIMENTAL EVALUATION) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We fine-tune the final layers of these pretrained models on each of our limited datasets, and then evaluate them on the held-out set. | component/input/data sensitivity | p. 5 (V. EXPERIMENTAL EVALUATION) |
| On this setting, we train CLIP-Fields with the provided instance segmented RGB-D images and the associated odometry data, and compare with the baseline pretrained ... | component/input/data sensitivity | p. 6 (V. EXPERIMENTAL EVALUATION) |
| Detic is absent from the first two evaluations since it is a detection model and thus cannot be fine-tuned on segmentation labels. | component/input/data sensitivity | p. 5 (V. EXPERIMENTAL EVALUATION) |
| Semantic Navigation on Robot with CLIP-Fields as Semantic-Spatial Memory Training a CLIP-Fields with available data, whether they are labeled by humans or pretrained models, ... | component/input/data sensitivity | p. 7 (V. EXPERIMENTAL EVALUATION) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| As a solution, we propose CLIP-Fields, which builds an implicit spatial semantic memory using webscale pretrained models as weak supervision. | In Figure 5, we see once again that CLIP-Fields outperforms the RGB-based models significantly, to the point where even with three labelled views, CLIP-Fields ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (V. EXPERIMENTAL EVALUATION), p. 7 (V. EXPERIMENTAL EVALUATION), p. 6 (V. EXPERIMENTAL EVALUATION), p. 7 (V. EXPERIMENTAL EVALUATION), p. 8 (V. EXPERIMENTAL EVALUATION), p. 8 (V. EXPERIMENTAL EVALUATION) |
| Primary metric/result | As the base models naturally improve over time with continuous efforts in the computer vision and natural language processing fields, we expect CLIP-Fields's performance ... | numeric claim only at cited anchor | p. 7 (V. EXPERIMENTAL EVALUATION) |

- Numeric sentences retained from the body:
- **p. 4 / IV. APPROACH - extractive body cue:** In this paper we used Sentence-BERT for these language features with n = 768.
- **p. 5 / IV. APPROACH - extractive body cue:** In this paper's experiments, we use the CLIP ViT-B/32 model embeddings, giving the visual features 512 dimensions.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In future work, we hope to explore models that share parameters across scenes, and can handle dynamic scenes and objects. | p. 8 (VI. CONCLUSIONS AND FUTURE WORK) |
| body limitation/failure cue | Detic is absent from the first two evaluations since it is a detection model and thus cannot be fine-tuned on segmentation labels. | p. 5 (V. EXPERIMENTAL EVALUATION) |
| body limitation/failure cue | However, if an object was misidentified during data preparation, CLIP-Fields fails to correctly identify it as well. | p. 8 (V. EXPERIMENTAL EVALUATION) |
| body limitation/failure cue | 4) CLIP-Fields's robustness to label errors: In real-world applications, CLIP-Fields relies on labels given by large | p. 6 (V. EXPERIMENTAL EVALUATION) |
| body limitation/failure cue | 7: Mean average accuracy on the semantic segmentation task on the HM3D Semantic dataset with label noise simulating errors in base labelling models. | p. 6 (V. EXPERIMENTAL EVALUATION) |
| body limitation/failure cue | In this section, we examine the robustness of CLIP-Fields to such label errors. | p. 7 (V. EXPERIMENTAL EVALUATION) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We use a batch size of 12, 544 everywhere since that is the maximum batch size we could fit in our VRAM of an ... | p. 5 (IV. APPROACH) |
| As the base models naturally improve over time with continuous efforts in the computer vision and natural language processing fields, we expect CLIP-Fields's performance ... | p. 7 (V. EXPERIMENTAL EVALUATION) |
| We encode the query image on the bottom left to its CLIP representation, and visualize the locations whose CLIP-Fields representations have the highest (more ... | p. 7 (V. EXPERIMENTAL EVALUATION) |
| We run twenty queries in the kitchen and fifteen queries in the library environment. | p. 8 (V. EXPERIMENTAL EVALUATION) |
| The images show the robot's POV given the associated query, with color coded borders showing approximate correctness. | p. 8 (V. EXPERIMENTAL EVALUATION) |
| Similar to CLIP [22], we also note that a larger batch size helps reduce the variance in the contrastive loss function. | p. 5 (IV. APPROACH) |
| We use a Multi-resolution Hash Encoder [20] to learn a low level spatial representation mapping R3 →Rd, which is then mapped to higher dimensions ... | p. 4 (IV. APPROACH) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / VI. CONCLUSIONS AND FUTURE WORK - extractive body cue:** In future work, we hope to explore models that share parameters across scenes, and can handle dynamic scenes and objects.
- **p. 5 / V. EXPERIMENTAL EVALUATION - extractive body cue:** Detic is absent from the first two evaluations since it is a detection model and thus cannot be fine-tuned on segmentation labels.
- **p. 8 / V. EXPERIMENTAL EVALUATION - extractive body cue:** However, if an object was misidentified during data preparation, CLIP-Fields fails to correctly identify it as well.
- **p. 6 / V. EXPERIMENTAL EVALUATION - extractive body cue:** 4) CLIP-Fields's robustness to label errors: In real-world applications, CLIP-Fields relies on labels given by large
- **p. 6 / V. EXPERIMENTAL EVALUATION - extractive body cue:** 7: Mean average accuracy on the semantic segmentation task on the HM3D Semantic dataset with label noise simulating errors in base labelling models.
- **p. 7 / V. EXPERIMENTAL EVALUATION - extractive body cue:** In this section, we examine the robustness of CLIP-Fields to such label errors.

- **Evidence anchors reviewed:** datasets p. 5 (V. EXPERIMENTAL EVALUATION), p. 7 (V. EXPERIMENTAL EVALUATION), p. 7 (V. EXPERIMENTAL EVALUATION), p. 8 (V. EXPERIMENTAL EVALUATION), p. 8 (V. EXPERIMENTAL EVALUATION), p. 5 (V. EXPERIMENTAL EVALUATION), metrics p. 6 (V. EXPERIMENTAL EVALUATION), p. 7 (Figure/Table caption), p. 5 (V. EXPERIMENTAL EVALUATION), p. 6 (V. EXPERIMENTAL EVALUATION), p. 7 (V. EXPERIMENTAL EVALUATION), p. 4 (Figure/Table caption), baselines p. 6 (V. EXPERIMENTAL EVALUATION), p. 5 (V. EXPERIMENTAL EVALUATION), p. 5 (V. EXPERIMENTAL EVALUATION), p. 6 (V. EXPERIMENTAL EVALUATION), results p. 6 (V. EXPERIMENTAL EVALUATION), p. 7 (V. EXPERIMENTAL EVALUATION), p. 6 (V. EXPERIMENTAL EVALUATION), p. 7 (V. EXPERIMENTAL EVALUATION), p. 8 (V. EXPERIMENTAL EVALUATION), p. 8 (V. EXPERIMENTAL EVALUATION).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
