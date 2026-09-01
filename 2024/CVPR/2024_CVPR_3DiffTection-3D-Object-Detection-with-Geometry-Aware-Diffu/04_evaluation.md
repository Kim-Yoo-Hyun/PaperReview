# Evaluation - 3DiffTection: 3D Object Detection with Geometry-Aware Diffusion Features

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Xu_3DiffTection_3D_Object_Detection_with_Geometry-Aware_Diffusion_Features_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Xu_3DiffTection_3D_Object_Detection_with_Geometry-Aware_Diffusion_Features_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4. Experiments), p. 6 (4.1. 3D Object Detection on Omni3D-ARKitscenes), p. 4 (Figure/Table caption), p. 7 (4.2. Cross-dataset Generalization), p. 7 (4.3. Label Efficiency), p. 8 (4.4. Analysis and Ablation)): 3DiffTection significantly outperforms baselines, including CubeRCNN-DLA-Aug, which is trained with 6x more supervision data. a novel-view synthesis task, we only take two views, one as the source view and another ...

## Evaluation Body Digest

- **p. 5 / 4. Experiments - extractive PDF cue:** For training 3D object detection, we use Omni3D-ARkitscenes as our primary in-domain experiment dataset, and Omni3DSUNRGBD for our cross-dataset experiments.
- **p. 6 / 4.1. 3D Object Detection on Omni3D-ARKitscenes - extractive PDF cue:** Notably, 3DiffTection significantly outperforms CubeRCNNDLA [5], a prior art in single-view 3D detection on the Omni3D-ARKitScenes dataset, achieving a margin of 7.4% at a resolution ...
- **p. 6 / 4.2. Cross-dataset Generalization - extractive PDF cue:** We evaluate it with two settings: (1) finetune the parameters on the Omni3D-SUNRBGD dataset and test the performance on Omni3D-SUNRGBD dataset, and (2) train the ...
- **p. 7 / 4.2. Cross-dataset Generalization - extractive PDF cue:** The results are reported for overlapped 14 classes between Omni3DSUNRGBD and Omni3D-ARKiSscenes dataset.
- **p. 7 / 4.2. Cross-dataset Generalization - extractive PDF cue:** For all zero-shot experiments, the methods are first trained on Omni3D-ARKitscenes for 3D detection and then directly tested on Omni3D-SUNRGBD dataset. "2D GT" means we ...
- **p. 5 / 4. Experiments - extractive PDF cue:** Datasets and implementation details For all our experiments, we train the geometric ControlNet on the official ARKitscene datasets [3], which provide around 450K posed low-resolution ...
- **p. 8 / 4.4. Analysis and Ablation - extractive PDF cue:** All results are reported using the Omni3D-ARKitscenes in Tab.
- **p. 8 / 4.4. Analysis and Ablation - extractive PDF cue:** Analysis of 3DiffTection Modules on Omni3D-ARKitScenes testing set.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.2. Cross-dataset Generalization (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 3DiffTection significantly outperforms baselines, including CubeRCNN-DLA-Aug, which is trained with 6x more supervision data. a novel-view synthesis task, we only take two views, one ... | p. 6 (4. Experiments) |
| 4.1. 3D Object Detection on Omni3D-ARKitscenes | EMPIRICAL / SOURCE-REPORTED EVALUATION | Notably, 3DiffTection significantly outperforms CubeRCNNDLA [5], a prior art in single-view 3D detection on the Omni3D-ARKitScenes dataset, achieving a margin of 7.4% at a ... | p. 6 (4.1. 3D Object Detection on Omni3D-ARKitscenes) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 3. Architecture of Geometric ControlNet. Left: Original Stable Diffusion UNet encoder block. Right: We train novel view image synthesis by adding a geometric ... | p. 4 (Figure/Table caption) |
| 4.2. Cross-dataset Generalization | EMPIRICAL / SOURCE-REPORTED EVALUATION | We observe that if we have ground truth 2D bounding boxes, 3DiffTection with semantic-ControlNet can even achieve the best performance. | p. 7 (4.2. Cross-dataset Generalization) |
| 4.3. Label Efficiency | EMPIRICAL / SOURCE-REPORTED EVALUATION | Notably, even with 50% of the labels, our proposed 3DiffTection achieves | p. 7 (4.3. Label Efficiency) |

## Dataset / Benchmark Role

- **p. 5 / 4. Experiments - extractive PDF cue:** For training 3D object detection, we use Omni3D-ARkitscenes as our primary in-domain experiment dataset, and Omni3DSUNRGBD for our cross-dataset experiments.
- **p. 6 / 4.1. 3D Object Detection on Omni3D-ARKitscenes - extractive PDF cue:** Notably, 3DiffTection significantly outperforms CubeRCNNDLA [5], a prior art in single-view 3D detection on the Omni3D-ARKitScenes dataset, achieving a margin of 7.4% at a resolution ...
- **p. 6 / 4.2. Cross-dataset Generalization - extractive PDF cue:** We evaluate it with two settings: (1) finetune the parameters on the Omni3D-SUNRBGD dataset and test the performance on Omni3D-SUNRGBD dataset, and (2) train the ...
- **p. 7 / 4.2. Cross-dataset Generalization - extractive PDF cue:** The results are reported for overlapped 14 classes between Omni3DSUNRGBD and Omni3D-ARKiSscenes dataset.
- **p. 7 / 4.2. Cross-dataset Generalization - extractive PDF cue:** For all zero-shot experiments, the methods are first trained on Omni3D-ARKitscenes for 3D detection and then directly tested on Omni3D-SUNRGBD dataset. "2D GT" means we ...
- **p. 5 / 4. Experiments - extractive PDF cue:** Datasets and implementation details For all our experiments, we train the geometric ControlNet on the official ARKitscene datasets [3], which provide around 450K posed low-resolution ...
- **p. 8 / 4.4. Analysis and Ablation - extractive PDF cue:** All results are reported using the Omni3D-ARKitscenes in Tab.
- **p. 8 / 4.4. Analysis and Ablation - extractive PDF cue:** Analysis of 3DiffTection Modules on Omni3D-ARKitScenes testing set.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. (1) We enhance pre-trained diffusion features with 3D awareness by training a geometric ControlNet (Sec. 3.2). (2) We employ a semantic ControlNet (Sec. ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Visualization of semantic correspondence prediction using different features Given a Red Source Point in the left most reference image, we predict the corresponding ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Architecture of Geometric ControlNet. Left: Original Stable Diffusion UNet encoder block. Right: We train novel view image synthesis by adding a geometric ControlNet ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. 3D Object Detection Results on Omni3D-ARKitScenes testing set. 3DiffTection significantly outperforms baselines, including CubeRCNN-DLA-Aug, which is trained with 6x more supervision data. a ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative results on Omni3D-ARKitScene 3D Detection. In contrast to Cube-RCNN (bottom), our approach (top) accurately predicts both the box class and 3D locations. ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Cross-domain experiment on the Omni3D-SUNRGBD dataset. The "Pre-trained on ARKit" denotes we pre-train the backbone on Omni3D-ARkitscenes. For CubeCNN, we pre-train it with ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3. Analysis of 3DiffTection Modules on Omni3D-ARKitScenes testing set. We first compare different backbones by freezing the backbone and only training the 3D detection ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5. Novel-view synthesis visualization on Omni3D-ARKitScenes testing set. Our model with Geometry-ControlNet synthesizes realistic novel views from a single input image. metric consistency of ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For training 3D object detection, we use Omni3D-ARkitscenes as our primary in-domain experiment dataset, and Omni3DSUNRGBD for our cross-dataset experiments. | embodiment, simulator version and control stack | p. 5 (4. Experiments), p. 6 (4.1. 3D Object Detection on Omni3D-ARKitscenes) |
| Task/environment | Notably, 3DiffTection significantly outperforms CubeRCNNDLA [5], a prior art in single-view 3D detection on the Omni3D-ARKitScenes dataset, achieving a margin of 7.4% at a ... | reset, timeout, object/scene variation | p. 6 (4.1. 3D Object Detection on Omni3D-ARKitscenes), p. 6 (4.2. Cross-dataset Generalization) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 3 (3.1. Diffusion Model as a Feature Extractor), p. 3 (3.1. Diffusion Model as a Feature Extractor) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 1 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Finally, in Section 4.4, we confirm 3DiffTection's enhanced 3D awareness by measuring its feature correspondence accuracy. | definition/direction/unit from same section | p. 5 (4. Experiments) |
| Subsequently, we demonstrate its ability to maintain strong performance with limited labels (Section 4.3). | definition/direction/unit from same section | p. 5 (4. Experiments) |
| The bird's-eye-view visualization further demonstrates that our predictions surpass the baseline performance of Cube-RCNN. | definition/direction/unit from same section | p. 7 (4.2. Cross-dataset Generalization) |
| In low-data regime (for both 50% and 10% label setting), 3DiffTection demonstrates significantly better performance, and more modest degradation than baselines. | definition/direction/unit from same section | p. 7 (4.3. Label Efficiency) |
| While enhancing performance is an interesting future work, here we utilize NVS as an auxiliary task which is demonstrated to effectively enhance our model's ... | definition/direction/unit from same section | p. 8 (4.4. Analysis and Ablation) |
| Figure 1. (1) We enhance pre-trained diffusion features with 3D awareness by training a geometric ControlNet (Sec. 3.2). (2) We employ a semantic ControlNet ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| This yield a performance boost of 5.09%. | definition/direction/unit from same section | p. 6 (4.2. Cross-dataset Generalization) |
| Then, we reintegrate the semantic ControlNet and jointly train it with the 3D head. | definition/direction/unit from same section | p. 6 (4.2. Cross-dataset Generalization) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 1, we analyze the 3D object detection performance of 3DiffTection compared to several baseline methods. | comparison identity and matched condition | p. 6 (4.1. 3D Object Detection on Omni3D-ARKitscenes) |
| 3DiffTection significantly outperforms baselines, including CubeRCNN-DLA-Aug, which is trained with 6x more supervision data. a novel-view synthesis task, we only take two views, one ... | comparison identity and matched condition | p. 6 (4. Experiments) |
| Without ground truth 2D bounding boxes, 3DiffTection is also able to outperform DIFT-SD and CubeRCNN by 5.90% and 5.83%, respectively. | comparison identity and matched condition | p. 7 (4.2. Cross-dataset Generalization) |
| The bird's-eye-view visualization further demonstrates that our predictions surpass the baseline performance of Cube-RCNN. | comparison identity and matched condition | p. 7 (4.2. Cross-dataset Generalization) |
| This indicate a 2.81% decrease in AP3D compared to the standard Stable Diffusion, affirming our hypothesis. | comparison identity and matched condition | p. 8 (4.4. Analysis and Ablation) |
| The results demonstrate that our proposed epipolar warp operator is effective in synthesizing the scene with accurate geometry and layout compared to the ground ... | comparison identity and matched condition | p. 8 (4.4. Analysis and Ablation) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Without any training of the geometric ControlNet on the OmniSUNRGBD, 3DiffTection (w/o Semantic-ControlNet) with only tuned a 3D head surpasses the fully fine-tuned CubeRCNN-DLA ... | component/input/data sensitivity | p. 6 (4.2. Cross-dataset Generalization) |
| We then validate its capacity for generalization to new datasets, both with and without tuning of the detection head (Section 4.2). | component/input/data sensitivity | p. 5 (4. Experiments) |
| These results indicate that even without training the geometric ControlNet in the target domain, the semantic ControlNet adeptly adapts features for perception tasks. | component/input/data sensitivity | p. 6 (4.2. Cross-dataset Generalization) |
| Without ground truth 2D bounding boxes, 3DiffTection is also able to outperform DIFT-SD and CubeRCNN by 5.90% and 5.83%, respectively. | component/input/data sensitivity | p. 7 (4.2. Cross-dataset Generalization) |
| To further demonstrate the transferrability of 3DiffTection, we train the models for 3D detection on Omni3DARkitscenes and directly test it on Omni3D-SUNRGBD datset without ... | component/input/data sensitivity | p. 7 (4.2. Cross-dataset Generalization) |
| Note that in the following experiments, the pretrained geometric ControlNet is kept frozen. | component/input/data sensitivity | p. 5 (4. Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our primary contributions are as follows: (1) We introduce a scalable technique for enhancing pretrained 2D diffusion models with 3D awareness through a novel ... | 3DiffTection significantly outperforms baselines, including CubeRCNN-DLA-Aug, which is trained with 6x more supervision data. a novel-view synthesis task, we only take two views, one ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4. Experiments), p. 6 (4.1. 3D Object Detection on Omni3D-ARKitscenes), p. 4 (Figure/Table caption), p. 7 (4.2. Cross-dataset Generalization), p. 7 (4.3. Label Efficiency), p. 8 (4.4. Analysis and Ablation) |
| Primary metric/result | Notably, 3DiffTection significantly outperforms CubeRCNNDLA [5], a prior art in single-view 3D detection on the Omni3D-ARKitScenes dataset, achieving a margin of 7.4% at a ... | numeric claim only at cited anchor | p. 6 (4.1. 3D Object Detection on Omni3D-ARKitscenes) |

- Numeric sentences retained from the body:
- **p. 6 / 4. Experiments - extractive PDF cue:** 3DiffTection significantly outperforms baselines, including CubeRCNN-DLA-Aug, which is trained with 6x more supervision data. a novel-view synthesis task, we only take two views, one as ...
- **p. 6 / 4.1. 3D Object Detection on Omni3D-ARKitscenes - extractive PDF cue:** Notably, 3DiffTection significantly outperforms CubeRCNNDLA [5], a prior art in single-view 3D detection on the Omni3D-ARKitScenes dataset, achieving a margin of 7.4% at a resolution ...
- **p. 6 / 4.1. 3D Object Detection on Omni3D-ARKitscenes - extractive PDF cue:** 3DiffTection exceeds DreamTeacher by 6.02% and 7.61% at resolutions of 256×256 and 512×512, respectively.
- **p. 6 / 4.1. 3D Object Detection on Omni3D-ARKitscenes - extractive PDF cue:** Remarkably, our model outperforms CubeRCNN-DLA-Aug by 2.03% on AP3D while using nearly 6x less data, demonstrating its data efficiency.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 3DiffTection has limitations, including the need for image pairs with accurate camera poses and challenges in handling dynamic objects from in-the-wild videos. | p. 8 (5. Conclusion and Limitations) |
| body limitation/failure cue | In contrast, 3DiffTection which does not rely on multi-view images for training the detection network and uses only view-pairs for geometric network training, surpasses ... | p. 6 (4.1. 3D Object Detection on Omni3D-ARKitscenes) |
| body limitation/failure cue | While enhancing performance is an interesting future work, here we utilize NVS as an auxiliary task which is demonstrated to effectively enhance our model's ... | p. 8 (4.4. Analysis and Ablation) |
| body limitation/failure cue | As seen in the middle column, our model can even handle severe occlusion cases, i.e., the sofa in the middle image and the sink ... | p. 6 (4.1. 3D Object Detection on Omni3D-ARKitscenes) |
| body limitation/failure cue | In low-data regime (for both 50% and 10% label setting), 3DiffTection demonstrates significantly better performance, and more modest degradation than baselines. | p. 7 (4.3. Label Efficiency) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| To evaluate the performance, we compute a mean AP3D across all categories in Omni3D-ARkitscenes and over a range of IoU3D thresholds in [0.05, 0.10, ... | p. 5 (4. Experiments) |
| Datasets and implementation details For all our experiments, we train the geometric ControlNet on the official ARKitscene datasets [3], which provide around 450K posed ... | p. 5 (4. Experiments) |
| Formally, given an image x, we sample a noise image xt at time t, and obtain the diffusion features f = F(xt; Θ), xt ... | p. 3 (3.1. Diffusion Model as a Feature Extractor) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion and Limitations - extractive PDF cue:** 3DiffTection has limitations, including the need for image pairs with accurate camera poses and challenges in handling dynamic objects from in-the-wild videos.
- **p. 6 / 4.1. 3D Object Detection on Omni3D-ARKitscenes - extractive PDF cue:** In contrast, 3DiffTection which does not rely on multi-view images for training the detection network and uses only view-pairs for geometric network training, surpasses these ...
- **p. 8 / 4.4. Analysis and Ablation - extractive PDF cue:** While enhancing performance is an interesting future work, here we utilize NVS as an auxiliary task which is demonstrated to effectively enhance our model's 3D ...
- **p. 6 / 4.1. 3D Object Detection on Omni3D-ARKitscenes - extractive PDF cue:** As seen in the middle column, our model can even handle severe occlusion cases, i.e., the sofa in the middle image and the sink in ...
- **p. 7 / 4.3. Label Efficiency - extractive PDF cue:** In low-data regime (for both 50% and 10% label setting), 3DiffTection demonstrates significantly better performance, and more modest degradation than baselines.

- **PDF anchors reviewed:** datasets p. 5 (4. Experiments), p. 6 (4.1. 3D Object Detection on Omni3D-ARKitscenes), p. 6 (4.2. Cross-dataset Generalization), p. 7 (4.2. Cross-dataset Generalization), p. 7 (4.2. Cross-dataset Generalization), p. 5 (4. Experiments), metrics p. 5 (4. Experiments), p. 5 (4. Experiments), p. 7 (4.2. Cross-dataset Generalization), p. 7 (4.3. Label Efficiency), p. 8 (4.4. Analysis and Ablation), p. 1 (Figure/Table caption), baselines p. 6 (4.1. 3D Object Detection on Omni3D-ARKitscenes), p. 6 (4. Experiments), p. 7 (4.2. Cross-dataset Generalization), p. 7 (4.2. Cross-dataset Generalization), p. 8 (4.4. Analysis and Ablation), p. 8 (4.4. Analysis and Ablation), results p. 6 (4. Experiments), p. 6 (4.1. 3D Object Detection on Omni3D-ARKitscenes), p. 4 (Figure/Table caption), p. 7 (4.2. Cross-dataset Generalization), p. 7 (4.3. Label Efficiency), p. 8 (4.4. Analysis and Ablation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
