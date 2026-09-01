# Evaluation - 3D Scene Graph: A Structure for Unified Semantics, 3D Space, and Camera

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1910.02527; PDF retrieval source: https://arxiv.org/pdf/1910.02527. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.2. Evaluation of Automated Pipeline), p. 6 (5.2. Evaluation of Automated Pipeline), p. 6 (5.2. Evaluation of Automated Pipeline), p. 7 (5.3. 2D Scene Graph Prediction), p. 8 (5.3. 2D Scene Graph Prediction), p. 8 (5.3. 2D Scene Graph Prediction)): Similar improvements can be seen in the case of 3D (Figure 7).

## Evaluation Body Digest

- **p. 6 / 5.1. Dataset Statistics - extractive PDF cue:** The semantic categories used come from the COCO dataset [33] for objects, MINC [8] for materials, and DTD [12] for textures.
- **p. 6 / 5.2. Evaluation of Automated Pipeline - extractive PDF cue:** We use the best offthe-shelf Mask R-CNN model trained on the COCO dataset.
- **p. 7 / 5.2. Evaluation of Automated Pipeline - extractive PDF cue:** To this end, we perform another set of experiments using BlitzNet [15], a network with faster inference but worse reported performance on the COCO dataset ...
- **p. 8 / 5.3. 2D Scene Graph Prediction - extractive PDF cue:** We compare the performance of two detectors with 7.4 AP difference in the COCO dataset.
- **p. 8 / 5.3. 2D Scene Graph Prediction - extractive PDF cue:** There are 3 standard evaluation setups for 2D scene graphs [35]: (a) Scene Graph Detection: Input is an image and output is bounding boxes, object ...
- **p. 7 / 5.3. 2D Scene Graph Prediction - extractive PDF cue:** We use this output for experiments on 2D scene graph prediction.
- **p. 7 / 5.2. Evaluation of Automated Pipeline - extractive PDF cue:** This suggests that the robustification mechanisms can provide similar value in increasing the performance of standard detectors and correct errors, regardless of initial predictions.
- **p. 8 / 5.3. 2D Scene Graph Prediction - extractive PDF cue:** We report f1-score and intersection-over-union as a per-pixel 8

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 5. Experiments (p. 6); 5.1. Dataset Statistics (p. 6); 5.2. Evaluation of Automated Pipeline (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Evaluation of Automated Pipeline | EMPIRICAL / SOURCE-REPORTED EVALUATION | Similar improvements can be seen in the case of 3D (Figure 7). | p. 7 (5.2. Evaluation of Automated Pipeline) |
| 5.2. Evaluation of Automated Pipeline | EMPIRICAL / SOURCE-REPORTED EVALUATION | The panorama results are obtained after applying both robustification mechanisms. | p. 6 (5.2. Evaluation of Automated Pipeline) |
| 5.2. Evaluation of Automated Pipeline | EMPIRICAL / SOURCE-REPORTED EVALUATION | And these in 3D: • Mask R-CNN [18] and Pano Projection: The panorama results of Mask R-CNN are projected on the 3D mesh surfaces ... | p. 6 (5.2. Evaluation of Automated Pipeline) |
| 5.3. 2D Scene Graph Prediction | EMPIRICAL / SOURCE-REPORTED EVALUATION | So far we focused on the automated detection results. | p. 7 (5.3. 2D Scene Graph Prediction) |
| 5.3. 2D Scene Graph Prediction | EMPIRICAL / SOURCE-REPORTED EVALUATION | AP performance of using different detectors. | p. 8 (5.3. 2D Scene Graph Prediction) |

## Dataset / Benchmark Role

- **p. 6 / 5.1. Dataset Statistics - extractive PDF cue:** The semantic categories used come from the COCO dataset [33] for objects, MINC [8] for materials, and DTD [12] for textures.
- **p. 6 / 5.2. Evaluation of Automated Pipeline - extractive PDF cue:** We use the best offthe-shelf Mask R-CNN model trained on the COCO dataset.
- **p. 7 / 5.2. Evaluation of Automated Pipeline - extractive PDF cue:** To this end, we perform another set of experiments using BlitzNet [15], a network with faster inference but worse reported performance on the COCO dataset ...
- **p. 8 / 5.3. 2D Scene Graph Prediction - extractive PDF cue:** We compare the performance of two detectors with 7.4 AP difference in the COCO dataset.
- **p. 8 / 5.3. 2D Scene Graph Prediction - extractive PDF cue:** There are 3 standard evaluation setups for 2D scene graphs [35]: (a) Scene Graph Detection: Input is an image and output is bounding boxes, object ...
- **p. 7 / 5.3. 2D Scene Graph Prediction - extractive PDF cue:** We use this output for experiments on 2D scene graph prediction.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. 3D Scene Graph: It consists of 4 layers, that represent semantics, 3D space and camera. Elements are nodes in the graph and have ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Constructing the 3D Scene Graph. (a) Input to the method is a 3D mesh model with registered panoramic images. (b) Each panorama is ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Framing: Examples of sampled rectilinear images using the framing robustification mechanism are shown in the dashed colored boxes. Detections (b) on individual frames ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Table 1. 3D Scene Graph Attributes and Relationships. For a detailed description see supplementary material [5]. Elements Attributes Relationships Object (O) Action Affordance, Class, Floor ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. It utilizes two heuristics: (a) placing the object at the center of the image and (b) having the image prop- erly zoomed-in around ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Multi-view consistency: Semantic labels from different panoramas are combined on the final mesh via multi-view consis- tency. Even though the individual projections carry ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 5. Semantic statistics for bed: (a) Number of object instances in buildings. (b) Distribution of its surface coverage. (c) Nearest object instance in 3D ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Evaluation of the automated pipeline on 2D panoramas and 3D mesh. We compute Average Precision (AP) and Average Recall (AR) for both modalities ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The semantic categories used come from the COCO dataset [33] for objects, MINC [8] for materials, and DTD [12] for textures. | embodiment, simulator version and control stack | p. 6 (5.1. Dataset Statistics), p. 6 (5.2. Evaluation of Automated Pipeline) |
| Task/environment | We use the best offthe-shelf Mask R-CNN model trained on the COCO dataset. | reset, timeout, object/scene variation | p. 6 (5.2. Evaluation of Automated Pipeline), p. 7 (5.2. Evaluation of Automated Pipeline) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 4 (3. 3D Scene Graph Structure), p. 5 (4. Constructing the 3D Scene Graph) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 2 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| This suggests that the robustification mechanisms can provide similar value in increasing the performance of standard detectors and correct errors, regardless of initial predictions. | definition/direction/unit from same section | p. 7 (5.2. Evaluation of Automated Pipeline) |
| We report f1-score and intersection-over-union as a per-pixel 8 | definition/direction/unit from same section | p. 8 (5.3. 2D Scene Graph Prediction) |
| As shown in Table 2, each mechanism in our approach contributes an additional boost in the final accuracy. | definition/direction/unit from same section | p. 7 (5.2. Evaluation of Automated Pipeline) |
| Table 6. Amodal mask segmentation quantitative results. f1-score empty occluded visible avg Avg. Amodal Mask 0.934 | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| We follow the COCO evaluation protocol [33] and report the average precision (AP) and recall (AR) for both modalities. | definition/direction/unit from same section | p. 6 (5.2. Evaluation of Automated Pipeline) |
| Figure 3. Framing: Examples of sampled rectilinear images using the framing robustification mechanism are shown in the dashed colored boxes. Detections (b) on individual ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 4. Multi-view consistency: Semantic labels from different panoramas are combined on the final mesh via multi-view consis- tency. Even though the individual projections ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| AP performance of using different detectors. | definition/direction/unit from same section | p. 8 (5.3. 2D Scene Graph Prediction) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Baselines: We compare the following approaches in 2D: • Mask R-CNN [18]: We run Mask R-CNN on 6 rectilinear images sampled on the panorama ... | comparison identity and matched condition | p. 6 (5.2. Evaluation of Automated Pipeline) |
| Values in parenthesis represent the absolute difference of the AP of each step with respect to the baseline. | comparison identity and matched condition | p. 7 (5.2. Evaluation of Automated Pipeline) |
| We notice that the results for both detectors provide a similar relative increase in AP among the different baselines (Table 4). | comparison identity and matched condition | p. 7 (5.2. Evaluation of Automated Pipeline) |
| The baseline is Statistically Informed Guess extracted from the training data. | comparison identity and matched condition | p. 8 (5.3. 2D Scene Graph Prediction) |
| As baselines, we take an average of amodal masks (a) over the training data (Avg. | comparison identity and matched condition | p. 8 (5.3. 2D Scene Graph Prediction) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Mask R-CNN with framing (c) was able to remove the tree detections and recuperate a missed toilet that is highly occluded. | component/input/data sensitivity | p. 7 (5.2. Evaluation of Automated Pipeline) |
| Mask R-CNN with framing and multi-view consistency (d) further removed the painted vase and bed reflection, achieving results very close to the ground truth. | component/input/data sensitivity | p. 7 (5.2. Evaluation of Automated Pipeline) |
| Since our semantic information resides in 3D space, we can infer the full extents of object occlusions without additional annotations and in a fully ... | component/input/data sensitivity | p. 8 (5.3. 2D Scene Graph Prediction) |
| Figure 1. 3D Scene Graph: It consists of 4 layers, that represent semantics, 3D space and camera. Elements are nodes in the graph and ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Figure 2. Constructing the 3D Scene Graph. (a) Input to the method is a 3D mesh model with registered panoramic images. (b) Each panorama ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| It is pre-trained on ImageNet-5K and fine-tuned on COCO. | component/input/data sensitivity | p. 6 (5.2. Evaluation of Automated Pipeline) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The input to our method is the typical output of 3D scanners and consists of 3D mesh models, registered RGB panoramas and the corresponding ... | Similar improvements can be seen in the case of 3D (Figure 7). | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.2. Evaluation of Automated Pipeline), p. 6 (5.2. Evaluation of Automated Pipeline), p. 6 (5.2. Evaluation of Automated Pipeline), p. 7 (5.3. 2D Scene Graph Prediction), p. 8 (5.3. 2D Scene Graph Prediction), p. 8 (5.3. 2D Scene Graph Prediction) |
| Primary metric/result | The panorama results are obtained after applying both robustification mechanisms. | numeric claim only at cited anchor | p. 6 (5.2. Evaluation of Automated Pipeline) |

- Numeric sentences retained from the body:
- **p. 7 / 5.2. Evaluation of Automated Pipeline - extractive PDF cue:** Note that the hours reported for the fully manual 3D annotation [7] are computed for 12 object classes (versus 62 in ours) and for an ...
- **p. 1 / 1. Introduction - extractive PDF cue:** 3D Scene Graph: It consists of 4 layers, that represent semantics, 3D space and camera.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 5. Semantic statistics for bed: (a) Number of object instances in buildings. (b) Distribution of its surface coverage. (c) Nearest object instance in ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | Figure 1. 3D Scene Graph: It consists of 4 layers, that represent semantics, 3D space and camera. Elements are nodes in the graph and ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Figure 3. Framing: Examples of sampled rectilinear images using the framing robustification mechanism are shown in the dashed colored boxes. Detections (b) on individual ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | The panorama results are obtained after applying both robustification mechanisms. | p. 6 (5.2. Evaluation of Automated Pipeline) |
| body limitation/failure cue | We want to further understand the behavior of the two robustification mechanisms when using a less accurate detector. | p. 7 (5.2. Evaluation of Automated Pipeline) |
| body limitation/failure cue | This suggests that the robustification mechanisms can provide similar value in increasing the performance of standard detectors and correct errors, regardless of initial predictions. | p. 7 (5.2. Evaluation of Automated Pipeline) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For more details on implementation and training/testing we refer the reader to Mask R-CNN [18] and Detectron [1]. | p. 6 (5.2. Evaluation of Automated Pipeline) |
| Baselines: We compare the following approaches in 2D: • Mask R-CNN [18]: We run Mask R-CNN on 6 rectilinear images sampled on the panorama ... | p. 6 (5.2. Evaluation of Automated Pipeline) |
| We compute Average Precision (AP) and Average Recall (AR) for both modalities based on COCO evaluation [33]. | p. 7 (5.2. Evaluation of Automated Pipeline) |
| These will next go through an automated step to generate the final 3D Scene Graph and compute attributes and relationships. | p. 7 (5.3. 2D Scene Graph Prediction) |
| This is a fundamental question for a content that preoccupies a number of domains, such as Computer Vision and Robotics. | p. 1 (1. Introduction) |
| Another interesting example is that of Visual Memex [36] that leverages a graph structure to encode contextual and visual similarities between objects without the ... | p. 3 (C S1) |
| Given these weights, we compute the highest scoring class per pixel. | p. 5 (4. Constructing the 3D Scene Graph) |
| The pipeline consists of two main steps (all operations are performed on rectilinear images). | p. 5 (4.1. User-in-the-loop verification) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 5. Semantic statistics for bed: (a) Number of object instances in buildings. (b) Distribution of its surface coverage. (c) Nearest object instance in 3D ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. 3D Scene Graph: It consists of 4 layers, that represent semantics, 3D space and camera. Elements are nodes in the graph and have ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Framing: Examples of sampled rectilinear images using the framing robustification mechanism are shown in the dashed colored boxes. Detections (b) on individual frames ...
- **p. 6 / 5.2. Evaluation of Automated Pipeline - extractive PDF cue:** The panorama results are obtained after applying both robustification mechanisms.
- **p. 7 / 5.2. Evaluation of Automated Pipeline - extractive PDF cue:** We want to further understand the behavior of the two robustification mechanisms when using a less accurate detector.
- **p. 7 / 5.2. Evaluation of Automated Pipeline - extractive PDF cue:** This suggests that the robustification mechanisms can provide similar value in increasing the performance of standard detectors and correct errors, regardless of initial predictions.

- **PDF anchors reviewed:** datasets p. 6 (5.1. Dataset Statistics), p. 6 (5.2. Evaluation of Automated Pipeline), p. 7 (5.2. Evaluation of Automated Pipeline), p. 8 (5.3. 2D Scene Graph Prediction), p. 8 (5.3. 2D Scene Graph Prediction), p. 7 (5.3. 2D Scene Graph Prediction), metrics p. 7 (5.2. Evaluation of Automated Pipeline), p. 8 (5.3. 2D Scene Graph Prediction), p. 7 (5.2. Evaluation of Automated Pipeline), p. 9 (Figure/Table caption), p. 6 (5.2. Evaluation of Automated Pipeline), p. 4 (Figure/Table caption), baselines p. 6 (5.2. Evaluation of Automated Pipeline), p. 7 (5.2. Evaluation of Automated Pipeline), p. 7 (5.2. Evaluation of Automated Pipeline), p. 8 (5.3. 2D Scene Graph Prediction), p. 8 (5.3. 2D Scene Graph Prediction), results p. 7 (5.2. Evaluation of Automated Pipeline), p. 6 (5.2. Evaluation of Automated Pipeline), p. 6 (5.2. Evaluation of Automated Pipeline), p. 7 (5.3. 2D Scene Graph Prediction), p. 8 (5.3. 2D Scene Graph Prediction), p. 8 (5.3. 2D Scene Graph Prediction).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
