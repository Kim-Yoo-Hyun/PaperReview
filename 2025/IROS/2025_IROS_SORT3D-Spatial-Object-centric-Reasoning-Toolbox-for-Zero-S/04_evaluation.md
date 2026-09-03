# Evaluation - SORT3D: Spatial Object-centric Reasoning Toolbox for Zero-Shot 3D Grounding Using Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2504.18684; PDF retrieval source: https://arxiv.org/pdf/2504.18684. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (V. RESULTS AND DISCUSSION), p. 5 (V. RESULTS AND DISCUSSION), p. 5 (V. RESULTS AND DISCUSSION), p. 6 (V. RESULTS AND DISCUSSION), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption)): On Sr3D, SORT3D surpasses SOTA supervised training methods and achieves close overall performance to Transcrib3D while surpassing it in view-dependent accuracy.

## Evaluation Body Digest

- **p. 5 / IV. EXPERIMENTAL SETUP - extractive body cue:** Referential Grounding on Benchmark Datasets We test our model on both ReferIt3D subsets and the subset of IRef-VLA using ScanNet scenes and compare to SOTA ...
- **p. 6 / V. RESULTS AND DISCUSSION - extractive body cue:** Supervised Methods NS3D* [7] 62.7 62.0 - ViL3DRel* [20] 64.4 62.0 64.5 3D-VisTA* [5] 64.2 61.5 65.1 SceneVerse-GPS* [19] 64.9 56.9 67.9 Zero-Shot Methods ZSVG3D* ...
- **p. 5 / IV. EXPERIMENTAL SETUP - extractive body cue:** Both datasets consist of utterances describing a target object in a ScanNet [13] scene using spatial relations.
- **p. 6 / V. RESULTS AND DISCUSSION - extractive body cue:** toolbox, which does not have to be from a particular dataset, and we employed no dataset-specific training or fine-tuning.
- **p. 5 / IV. EXPERIMENTAL SETUP - extractive body cue:** For our methods, we conduct multiple trials on each data split to measure variance in LLMs, reported with standard deviation values on the grounding accuracy, ...
- **p. 5 / V. RESULTS AND DISCUSSION - extractive body cue:** We also note that the use of LLMs introduces variance between trials, affecting grounding accuracy up to 6%.
- **p. 6 / V. RESULTS AND DISCUSSION - extractive body cue:** Ablation of Captioning Module We evaluate the effect on grounding accuracy of adding open-vocabulary captions generated from 2D images of objects in the scene.
- **p. 6 / V. RESULTS AND DISCUSSION - extractive body cue:** On Sr3D, SORT3D surpasses SOTA supervised training methods and achieves close overall performance to Transcrib3D while surpassing it in view-dependent accuracy.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** IV. EXPERIMENTAL SETUP (p. 5); V. RESULTS AND DISCUSSION (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. RESULTS AND DISCUSSION | EMPIRICAL / SOURCE-REPORTED EVALUATION | On Sr3D, SORT3D surpasses SOTA supervised training methods and achieves close overall performance to Transcrib3D while surpassing it in view-dependent accuracy. | p. 6 (V. RESULTS AND DISCUSSION) |
| V. RESULTS AND DISCUSSION | EMPIRICAL / SOURCE-REPORTED EVALUATION | Similarly, while Transcrib3D reports higher accuracies, it relies on guiding principles [6] that are tailored to the language used in Nr3D and Sr3D, which ... | p. 5 (V. RESULTS AND DISCUSSION) |
| V. RESULTS AND DISCUSSION | EMPIRICAL / SOURCE-REPORTED EVALUATION | We see that our method achieves higher accuracy with GPT4o as the LLM backend and is on par with SOTA methods on View-Dependent statements ... | p. 5 (V. RESULTS AND DISCUSSION) |
| V. RESULTS AND DISCUSSION | EMPIRICAL / SOURCE-REPORTED EVALUATION | Despite this, by leveraging foundation models to obtain object semantic attributes and mapping spatial reasoning into sequential reasoning, our spatial reasoning toolbox approach achieves ... | p. 6 (V. RESULTS AND DISCUSSION) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 5: Navigation on the mecanum robot in the university corridor given the statement "Go to the table next to the bookshelf, then to ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / IV. EXPERIMENTAL SETUP - extractive body cue:** Referential Grounding on Benchmark Datasets We test our model on both ReferIt3D subsets and the subset of IRef-VLA using ScanNet scenes and compare to SOTA ...
- **p. 6 / V. RESULTS AND DISCUSSION - extractive body cue:** Supervised Methods NS3D* [7] 62.7 62.0 - ViL3DRel* [20] 64.4 62.0 64.5 3D-VisTA* [5] 64.2 61.5 65.1 SceneVerse-GPS* [19] 64.9 56.9 67.9 Zero-Shot Methods ZSVG3D* ...
- **p. 5 / IV. EXPERIMENTAL SETUP - extractive body cue:** Both datasets consist of utterances describing a target object in a ScanNet [13] scene using spatial relations.
- **p. 6 / V. RESULTS AND DISCUSSION - extractive body cue:** toolbox, which does not have to be from a particular dataset, and we employed no dataset-specific training or fine-tuning.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: An example of our system's workflow for using referential object grounding for downstream object-goal navigation. The agent uses the 2D image for fine-grained ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: The full system diagram for the SORT3D framework the characteristics of a query object in an image. Describe the <object> in this image, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Generated image crops and corresponding caption
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Correct (a) and incorrect (b) grounding examples. Top left and bottom left respectively show correctly grounded view-independent and view-dependent statements. Top right and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Navigation on the mecanum robot in the university corridor given the statement "Go to the table next to the bookshelf, then to the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Navigation on the mecanum robot in the student lounge given the statement "I want to play a board game, fetch me one from ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Referential Grounding on Benchmark Datasets We test our model on both ReferIt3D subsets and the subset of IRef-VLA using ScanNet scenes and compare to ... | embodiment, simulator version and control stack | p. 5 (IV. EXPERIMENTAL SETUP), p. 6 (V. RESULTS AND DISCUSSION) |
| Task/environment | Supervised Methods NS3D* [7] 62.7 62.0 - ViL3DRel* [20] 64.4 62.0 64.5 3D-VisTA* [5] 64.2 61.5 65.1 SceneVerse-GPS* [19] 64.9 56.9 67.9 Zero-Shot Methods ... | reset, timeout, object/scene variation | p. 6 (V. RESULTS AND DISCUSSION), p. 5 (IV. EXPERIMENTAL SETUP) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For our methods, we conduct multiple trials on each data split to measure variance in LLMs, reported with standard deviation values on the grounding ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTAL SETUP) |
| We also note that the use of LLMs introduces variance between trials, affecting grounding accuracy up to 6%. | definition/direction/unit from same section | p. 5 (V. RESULTS AND DISCUSSION) |
| Ablation of Captioning Module We evaluate the effect on grounding accuracy of adding open-vocabulary captions generated from 2D images of objects in the scene. | definition/direction/unit from same section | p. 6 (V. RESULTS AND DISCUSSION) |
| On Sr3D, SORT3D surpasses SOTA supervised training methods and achieves close overall performance to Transcrib3D while surpassing it in view-dependent accuracy. | definition/direction/unit from same section | p. 6 (V. RESULTS AND DISCUSSION) |
| Fig. 3: Generated image crops and corresponding caption | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Fig. 5: Navigation on the mecanum robot in the university corridor given the statement "Go to the table next to the bookshelf, then to ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Fig. 6: Navigation on the mecanum robot in the student lounge given the statement "I want to play a board game, fetch me one ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Referential Grounding on Benchmark Datasets We test our model on both ReferIt3D subsets and the subset of IRef-VLA using ScanNet scenes and compare to ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENTAL SETUP) |
| While supervised baselines such as ViL3DRel [20], 3DVisTA [5], and SceneVerse [19] report slightly higher overall grounding accuracies, these methods are explicitly trained on ... | comparison identity and matched condition | p. 5 (V. RESULTS AND DISCUSSION) |
| We augment the Transcrib3D [6] baseline model with our captions for each object as additional information passed into the LLM reasoner. | comparison identity and matched condition | p. 6 (V. RESULTS AND DISCUSSION) |
| Ablation of Captioning Module We evaluate the effect on grounding accuracy of adding open-vocabulary captions generated from 2D images of objects in the scene. | comparison identity and matched condition | p. 6 (V. RESULTS AND DISCUSSION) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation of Captioning Module We evaluate the effect on grounding accuracy of adding open-vocabulary captions generated from 2D images of objects in the scene. | component/input/data sensitivity | p. 6 (V. RESULTS AND DISCUSSION) |
| toolbox, which does not have to be from a particular dataset, and we employed no dataset-specific training or fine-tuning. | component/input/data sensitivity | p. 6 (V. RESULTS AND DISCUSSION) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To this end, we propose SORT3D, a Spatial Object-centric Reasoning Toolbox for 3D Grounding Using LLMs, shown | On Sr3D, SORT3D surpasses SOTA supervised training methods and achieves close overall performance to Transcrib3D while surpassing it in view-dependent accuracy. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (V. RESULTS AND DISCUSSION), p. 5 (V. RESULTS AND DISCUSSION), p. 5 (V. RESULTS AND DISCUSSION), p. 6 (V. RESULTS AND DISCUSSION), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Primary metric/result | Similarly, while Transcrib3D reports higher accuracies, it relies on guiding principles [6] that are tailored to the language used in Nr3D and Sr3D, which ... | numeric claim only at cited anchor | p. 5 (V. RESULTS AND DISCUSSION) |

- Numeric sentences retained from the body:
- **p. 6 / V. RESULTS AND DISCUSSION - extractive body cue:** Supervised Methods NS3D* [7] 62.7 62.0 - ViL3DRel* [20] 64.4 62.0 64.5 3D-VisTA* [5] 64.2 61.5 65.1 SceneVerse-GPS* [19] 64.9 56.9 67.9 Zero-Shot Methods ZSVG3D* ...
- **p. 6 / V. RESULTS AND DISCUSSION - extractive body cue:** Supervised Methods ViL3DRel* [20] 72.8 63.8 73.2 3D-VisTA* [5] 76.4 58.9 77.3 SceneVerse-GPS* [19] 77.5 62.8 78.2 Zero-Shot Methods Transcrib3D* [6] (GPT-4) 98.4 98.2 98.4 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We see that SORT3D is able to explainably resolve complex view-dependent relations with multiple anchors and complex semantic descriptions (Figure 4-a), while also providing ... | p. 6 (V. RESULTS AND DISCUSSION) |
| body limitation/failure cue | In the bottom right, the model fails at pragmatics, picking out the rightmost pillow, instead of recognizing that the sentence implies choosing a pillow ... | p. 6 (V. RESULTS AND DISCUSSION) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For a fair comparison, we run Transcrib3D with the same two LLMs we use on the same test splits4. | p. 5 (IV. EXPERIMENTAL SETUP) |
| For our methods, we conduct multiple trials on each data split to measure variance in LLMs, reported with standard deviation values on the grounding ... | p. 5 (IV. EXPERIMENTAL SETUP) |
| Our mobile robot perception setup for real-world experiments consists of a 360 camera and a 3D LiDAR (section V-C contains further hardware details). | p. 3 (III. METHODOLOGY) |
| As the robot moves and produces new observations, we associate per-frame object instance pointclouds using a 2D tracking module and 3D proximity priors, followed ... | p. 3 (III. METHODOLOGY) |
| We release all object crops and captions as a supplement to the ScanNet [13] dataset along with our code. | p. 4 (III. METHODOLOGY) |
| We use Mistral Large 2 [28] for these steps, filtering objects based on their text descriptions, to best leverage the ability of LLMs to ... | p. 4 (III. METHODOLOGY) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / V. RESULTS AND DISCUSSION - extractive body cue:** We see that SORT3D is able to explainably resolve complex view-dependent relations with multiple anchors and complex semantic descriptions (Figure 4-a), while also providing explainable ...
- **p. 6 / V. RESULTS AND DISCUSSION - extractive body cue:** In the bottom right, the model fails at pragmatics, picking out the rightmost pillow, instead of recognizing that the sentence implies choosing a pillow on ...

- **Evidence anchors reviewed:** datasets p. 5 (IV. EXPERIMENTAL SETUP), p. 6 (V. RESULTS AND DISCUSSION), p. 5 (IV. EXPERIMENTAL SETUP), p. 6 (V. RESULTS AND DISCUSSION), metrics p. 5 (IV. EXPERIMENTAL SETUP), p. 5 (V. RESULTS AND DISCUSSION), p. 6 (V. RESULTS AND DISCUSSION), p. 6 (V. RESULTS AND DISCUSSION), p. 4 (Figure/Table caption), p. 7 (Figure/Table caption), baselines p. 5 (IV. EXPERIMENTAL SETUP), p. 5 (V. RESULTS AND DISCUSSION), p. 6 (V. RESULTS AND DISCUSSION), p. 6 (V. RESULTS AND DISCUSSION), results p. 6 (V. RESULTS AND DISCUSSION), p. 5 (V. RESULTS AND DISCUSSION), p. 5 (V. RESULTS AND DISCUSSION), p. 6 (V. RESULTS AND DISCUSSION), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
