# Evaluation - Matterport3D: Learning from RGB-D Data in Indoor Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1709.06158; PDF retrieval source: https://arxiv.org/pdf/1709.06158. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (Figure/Table caption), p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 4 (3.3. Properties of the Dataset), p. 7 (Figure/Table caption)): Table 5: Region-type classification results. Each entry lists the prediction accuracy (percentage correct). By comparing the accuracy between [single] and [pano] we can see an improvement from increased image field ...

## Evaluation Body Digest

- **p. 2 / 3. The Matterport3D Dataset - extractive PDF cue:** This paper introduces a new RGB-D dataset of buildingscale scenes, and describes a set of scene understanding tasks that can be trained and tested from ...
- **p. 4 / 3.3. Properties of the Dataset - extractive PDF cue:** Our dataset contains high dynamic range (HDR) images acquired in static scenes from stationary cameras mounted on a tripod, and thus has no motion blur.
- **p. 4 / 3.3. Properties of the Dataset - extractive PDF cue:** This comprehensive sampling of viewpoint space provides new opportunities for learning about scenes as seen from arbitrary viewpoints that may be encountered by robots or ...
- **p. 2 / 3.1. Data Acquisition Process - extractive PDF cue:** For each environment in the dataset, an operator captures a set of panoramas uniformly spaced at approximately 2.5m throughout the entire walkable floor plan of ...
- **p. 3 / 3.3. Properties of the Dataset - extractive PDF cue:** Although we do not have ground-truth camera poses for the dataset and so cannot measure errors objectively, we subjectively estimate that the average registration error ...
- **p. 5 / 3.3. Properties of the Dataset - extractive PDF cue:** Data of this type is difficult to capture and distribute due to privacy concerns, and thus it is very valuable for learning about the types ...
- **p. 3 / 3.3. Properties of the Dataset - extractive PDF cue:** Previous RGB-D datasets have provided limited data about global alignment of camera poses.
- **p. 5 / 3.3. Properties of the Dataset - extractive PDF cue:** We believe that Matterport3D is the largest RGBD dataset available.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 3. The Matterport3D Dataset (p. 2); 3.3. Properties of the Dataset (p. 3).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | BENCHMARK / DATASET | Table 5: Region-type classification results. Each entry lists the prediction accuracy (percentage correct). By comparing the accuracy between [single] and [pano] we can see ... | p. 9 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Table 1: Keypoint matching results. Error (%) at 95% re- call on ground truth correspondences from the SUN3D test- ing scenes. We see an ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Table 2: View overlap prediction results. Results on SUN3D and Matterport3D dataset measured by normalized discounted cumulative gain. From the comparison we can clearly ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Figure 11: Examples of surface normal estimation. We show results of images from NYUv2 testing set. The results from the model fine-tuned on Matterport3D ... | p. 7 (Figure/Table caption) |
| 3.3. Properties of the Dataset | BENCHMARK / DATASET | Most have expressly attempted to cover each surface patch once, either to improve the efficiency of scene reconstruction or to reduce bias in scene ... | p. 4 (3.3. Properties of the Dataset) |

## Dataset / Benchmark Role

- **p. 2 / 3. The Matterport3D Dataset - extractive PDF cue:** This paper introduces a new RGB-D dataset of buildingscale scenes, and describes a set of scene understanding tasks that can be trained and tested from ...
- **p. 4 / 3.3. Properties of the Dataset - extractive PDF cue:** Our dataset contains high dynamic range (HDR) images acquired in static scenes from stationary cameras mounted on a tripod, and thus has no motion blur.
- **p. 4 / 3.3. Properties of the Dataset - extractive PDF cue:** This comprehensive sampling of viewpoint space provides new opportunities for learning about scenes as seen from arbitrary viewpoints that may be encountered by robots or ...
- **p. 2 / 3.1. Data Acquisition Process - extractive PDF cue:** For each environment in the dataset, an operator captures a set of panoramas uniformly spaced at approximately 2.5m throughout the entire walkable floor plan of ...
- **p. 3 / 3.3. Properties of the Dataset - extractive PDF cue:** Although we do not have ground-truth camera poses for the dataset and so cannot measure errors objectively, we subjectively estimate that the average registration error ...
- **p. 5 / 3.3. Properties of the Dataset - extractive PDF cue:** Data of this type is difficult to capture and distribute due to privacy concerns, and thus it is very valuable for learning about the types ...
- **p. 3 / 3.3. Properties of the Dataset - extractive PDF cue:** Previous RGB-D datasets have provided limited data about global alignment of camera poses.
- **p. 5 / 3.3. Properties of the Dataset - extractive PDF cue:** We believe that Matterport3D is the largest RGBD dataset available.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: The Matterport3D dataset provides visual data covering 90 buildings, including HDR color images, depth images, panoramic skyboxes, textured meshes, region lay- outs and ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2: Panoramas are captured from viewpoints (green spheres) on average 2.25m apart. which they generate a point cloud - we additionally pro- vide the ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3: Annotator-specified floor plans. Floor plans are used to define regions for object-level semantic annotation. Left: floor plan with textured mesh. Right: floor plan ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 4: Instance-level semantic annotations. Example rooms annotated with semantic categories for all object in- stances. Left: 3D room mesh. Middle: object instance la- bels. ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 5: Semantic annotation statistics. Total number of semantic annotations for the top object categories.
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 6: Visualizations of point clouds (left-to-right: color, diffuse shading, and normals). These images show pixels from all RGB-D images back-projected into world space according ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 7: Visualization of the set of images visible to a se- lected surface point (shown as red visibility lines). (Please note that the mesh ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 8: Histogram showing how many images observe each surface vertex. The mode is 7 and the average is 11. tribute them for academic research). ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This paper introduces a new RGB-D dataset of buildingscale scenes, and describes a set of scene understanding tasks that can be trained and tested ... | embodiment, simulator version and control stack | p. 2 (3. The Matterport3D Dataset), p. 4 (3.3. Properties of the Dataset) |
| Task/environment | Our dataset contains high dynamic range (HDR) images acquired in static scenes from stationary cameras mounted on a tripod, and thus has no motion ... | reset, timeout, object/scene variation | p. 4 (3.3. Properties of the Dataset), p. 4 (3.3. Properties of the Dataset) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 5 (4.1. Keypoint Matching), p. 4 (3.3. Properties of the Dataset) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 5 (4.1. Keypoint Matching), p. 8 (4.4. Region-Type Classification) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 1: Keypoint matching results. Error (%) at 95% re- call on ground truth correspondences from the SUN3D test- ing scenes. We see an ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 3: Surface normal estimation results. Impact of training with Matterport3D (MP) on performance in the NYUv2 dataset. The columns show the mean and ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 5: Region-type classification results. Each entry lists the prediction accuracy (percentage correct). By comparing the accuracy between [single] and [pano] we can see ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Although we do not have ground-truth camera poses for the dataset and so cannot measure errors objectively, we subjectively estimate that the average registration ... | definition/direction/unit from same section | p. 3 (3.3. Properties of the Dataset) |
| Please note the accuracy of the global alignment (no ghosting) and the relatively low noise in surface normals, even without advanced depth-fusion techniques. | definition/direction/unit from same section | p. 4 (3.3. Properties of the Dataset) |
| Most RGB-D image datasets have been captured mostly with hand-held video cameras and thus suffer from motion blur and other artifacts typical of real-time ... | definition/direction/unit from same section | p. 4 (3.3. Properties of the Dataset) |
| Table 6: Semantic voxel label prediction accuracy on our Matterport3D test scenes. | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Table 2: View overlap prediction results. Results on SUN3D and Matterport3D dataset measured by normalized discounted cumulative gain. From the comparison we can clearly ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 9: Example training correspondences (left) and im- age patches (right) extracted from Matterport3D. Triplets of matching patches (first and second columns) and non- ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Figure 10: Example overlap views from SUN3D and Mat- terport3D ranked by their overlap ratio. In contrast to RGB-D video datasets captured with hand-held ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| We describe the data in this section, along with a discussion of how it differs from prior work. | comparison identity and matched condition | p. 2 (3. The Matterport3D Dataset) |
| In comparison to previous datasets, Matterport3D has unique properties that open up new research opportunities: RGB-D Panoramas. | comparison identity and matched condition | p. 3 (3.3. Properties of the Dataset) |
| Please note the accuracy of the global alignment (no ghosting) and the relatively low noise in surface normals, even without advanced depth-fusion techniques. | comparison identity and matched condition | p. 4 (3.3. Properties of the Dataset) |
| Table 2: View overlap prediction results. Results on SUN3D and Matterport3D dataset measured by normalized discounted cumulative gain. From the comparison we can clearly ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Please note the accuracy of the global alignment (no ghosting) and the relatively low noise in surface normals, even without advanced depth-fusion techniques. | component/input/data sensitivity | p. 4 (3.3. Properties of the Dataset) |
| The first step of our semantic annotation process is to break down each building into region components by specifying the 3D spatial extent and ... | component/input/data sensitivity | p. 3 (3.2. Semantic Annotation) |
| Category wall objects door chair window ceiling picture floor misc lighting cushion table cabinet curtain plant shelving sink mirror chest towel stairs railing column ... | component/input/data sensitivity | p. 4 (3.3. Properties of the Dataset) |
| Figure 9: Example training correspondences (left) and im- age patches (right) extracted from Matterport3D. Triplets of matching patches (first and second columns) and non- ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Table 1: Keypoint matching results. Error (%) at 95% re- call on ground truth correspondences from the SUN3D test- ing scenes. We see an ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Figure 11: Examples of surface normal estimation. We show results of images from NYUv2 testing set. The results from the model fine-tuned on Matterport3D ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we introduce Matterport3D, a large-scale RGB-D dataset containing 10,800 panoramic views from 194,400 RGB-D images of 90 building-scale scenes. | Table 5: Region-type classification results. Each entry lists the prediction accuracy (percentage correct). By comparing the accuracy between [single] and [pano] we can see ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (Figure/Table caption), p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 4 (3.3. Properties of the Dataset), p. 7 (Figure/Table caption) |
| Primary metric/result | Table 1: Keypoint matching results. Error (%) at 95% re- call on ground truth correspondences from the SUN3D test- ing scenes. We see an ... | numeric claim only at cited anchor | p. 6 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 3 / 3.2. Semantic Annotation - extractive PDF cue:** The 3D segmentations contain a total of 50,811 object instance annotations.
- **p. 3 / 3.2. Semantic Annotation - extractive PDF cue:** Since AMT workers are allowed to provide freeform text labels, there were 1,659 unique text labels, which we then post-processed to establish a canonical set ...
- **p. 3 / 3.2. Semantic Annotation - extractive PDF cue:** The 3D segmentations contain a total of 50,811 object instance annotations.
- **p. 3 / 3.2. Semantic Annotation - extractive PDF cue:** Since AMT workers are allowed to provide freeform text labels, there were 1,659 unique text labels, which we then post-processed to establish a canonical set ...
- **p. 5 / 4. Learning from the Data - extractive PDF cue:** For all experiments, we have split the dataset into 61 scenes for training, 11 for validation, and 18 for testing (see the supplemental materials for ...
- **p. 8 / 4.5. Semantic Voxel Labeling - extractive PDF cue:** We use 20 object class labels, and a network following the architecture of ScanNet [7], and training with 52,355 subvolume samples (418,840 augmented samples).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Although we do not have ground-truth camera poses for the dataset and so cannot measure errors objectively, we subjectively estimate that the average registration ... | p. 3 (3.3. Properties of the Dataset) |
| body limitation/failure cue | Please note the accuracy of the global alignment (no ghosting) and the relatively low noise in surface normals, even without advanced depth-fusion techniques. | p. 4 (3.3. Properties of the Dataset) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Though the curation of the dataset is interesting in its own, the most compelling part of the project is the computer vision tasks enabled ... | p. 1 (1. Introduction) |
| As with other computer vision tasks, the performance of data-driven models exceeds that of hand-tuned models and depends directly on the quantity and quality ... | p. 1 (1. Introduction) |
| The network also contains shortcut link to copy the high resolution feature from the encoder | p. 6 (4.3. Surface Normal Estimation) |
| The model is a fully convolutional neural network consisting of an encoder, which shares the same architecture as VGG-16 from the beginning till the ... | p. 6 (4.3. Surface Normal Estimation) |
| Notice how the Matterport3D dataset is able to perform well on NYUv2, while the converse is not true. to the decoder to bring in ... | p. 7 (4.3. Surface Normal Estimation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / 3.3. Properties of the Dataset - extractive PDF cue:** Although we do not have ground-truth camera poses for the dataset and so cannot measure errors objectively, we subjectively estimate that the average registration error ...
- **p. 4 / 3.3. Properties of the Dataset - extractive PDF cue:** Please note the accuracy of the global alignment (no ghosting) and the relatively low noise in surface normals, even without advanced depth-fusion techniques.

- **PDF anchors reviewed:** datasets p. 2 (3. The Matterport3D Dataset), p. 4 (3.3. Properties of the Dataset), p. 4 (3.3. Properties of the Dataset), p. 2 (3.1. Data Acquisition Process), p. 3 (3.3. Properties of the Dataset), p. 5 (3.3. Properties of the Dataset), metrics p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 9 (Figure/Table caption), p. 3 (3.3. Properties of the Dataset), p. 4 (3.3. Properties of the Dataset), p. 4 (3.3. Properties of the Dataset), baselines p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), p. 2 (3. The Matterport3D Dataset), p. 3 (3.3. Properties of the Dataset), p. 4 (3.3. Properties of the Dataset), p. 6 (Figure/Table caption), results p. 9 (Figure/Table caption), p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 4 (3.3. Properties of the Dataset), p. 7 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
