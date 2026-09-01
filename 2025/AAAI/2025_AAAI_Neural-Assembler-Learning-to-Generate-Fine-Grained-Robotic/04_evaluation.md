# Evaluation - Neural Assembler: Learning to Generate Fine-Grained Robotic Assembly Instructions from Multi-View Images

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ojs.aaai.org/index.php/AAAI/article/view/33613; PDF retrieval source: https://ojs.aaai.org/index.php/AAAI/article/view/33613. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 6 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments)): As indicated in Table 3, the Neural Assembler achieves performance in real-world experiments close to the results obtained in simulated environments, demonstrating its robust applicability.

## Evaluation Body Digest

- **p. 8 / 4 Experiments - extractive body cue:** (2022b) 7.3 21.8 Ours 34.2 58.5 Real-World Dataset LSTM Graves and Graves (2012) 7.3 21.8 DETR3D Wang et al.
- **p. 8 / 4 Experiments - extractive body cue:** (2022b) 2.4 12.8 Ours 22.0 50.5 Table 3: The performance of the fine-tuned model on the novel simulated dataset and real-world dataset.
- **p. 9 / 4 Experiments - extractive body cue:** The left box displays 4 images captured using a Realsense camera, while the right delineates the detected type, position, rotation angle of each brick, and ...
- **p. 6 / 4 Experiments - extractive body cue:** Furthermore, for the object pose estimation component, our methodology is rigorously benchmarked against DETR3D Wang et al.
- **p. 6 / 4 Experiments - extractive body cue:** The two datasets, characterized by brick number, occlusion from variable visibility, and complex assembly graph, reflect the complexity of assembly tasks.
- **p. 7 / 4 Experiments - extractive body cue:** Per-scene quantitative results on the CLEVR-Assembly Dataset are summarized in Table 1.
- **p. 9 / 4 Experiments - extractive body cue:** As indicated in Table 3, the Neural Assembler achieves performance in real-world experiments close to the results obtained in simulated environments, demonstrating its robust applicability.
- **p. 7 / 4 Experiments - extractive body cue:** 5 further shows the generated assembly instructions for a brick model in the CLEVR-Assembly Dataset.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 4 Experiments (p. 6); A.1 Dataset Generation (p. 12); A.2 Implementation Details (p. 12); A.4 Real-World Robotic Experiment (p. 13).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | BENCHMARK / DATASET | As indicated in Table 3, the Neural Assembler achieves performance in real-world experiments close to the results obtained in simulated environments, demonstrating its robust ... | p. 9 (4 Experiments) |
| 4 Experiments | BENCHMARK / DATASET | As shown in Tables 1 and 2, the result shows that more perspectives as input can improve the performance. | p. 7 (4 Experiments) |
| 4 Experiments | BENCHMARK / DATASET | Neural Assembler outperforms baseline models in all metrics considered. | p. 7 (4 Experiments) |
| 4 Experiments | BENCHMARK / DATASET | This comparison is pivotal in underscoring the adaptability and accuracy of our model in 3D pose estimation, a crucial aspect in varied application domains. | p. 6 (4 Experiments) |
| 4 Experiments | BENCHMARK / DATASET | For instance, the more compact assembly of LEGO bricks results in increased occlusion. | p. 8 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 8 / 4 Experiments - extractive body cue:** (2022b) 7.3 21.8 Ours 34.2 58.5 Real-World Dataset LSTM Graves and Graves (2012) 7.3 21.8 DETR3D Wang et al.
- **p. 8 / 4 Experiments - extractive body cue:** (2022b) 2.4 12.8 Ours 22.0 50.5 Table 3: The performance of the fine-tuned model on the novel simulated dataset and real-world dataset.
- **p. 9 / 4 Experiments - extractive body cue:** The left box displays 4 images captured using a Realsense camera, while the right delineates the detected type, position, rotation angle of each brick, and ...
- **p. 6 / 4 Experiments - extractive body cue:** Furthermore, for the object pose estimation component, our methodology is rigorously benchmarked against DETR3D Wang et al.
- **p. 6 / 4 Experiments - extractive body cue:** The two datasets, characterized by brick number, occlusion from variable visibility, and complex assembly graph, reflect the complexity of assembly tasks.
- **p. 7 / 4 Experiments - extractive body cue:** Per-scene quantitative results on the CLEVR-Assembly Dataset are summarized in Table 1.
- **p. 9 / 4 Experiments - extractive body cue:** As indicated in Table 3, the Neural Assembler achieves performance in real-world experiments close to the results obtained in simulated environments, demonstrating its robust applicability.
- **p. 7 / 4 Experiments - extractive body cue:** 5 further shows the generated assembly instructions for a brick model in the CLEVR-Assembly Dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Schematic illustration of the proposed Neural Assembler. See Section 3 for more details. integrate information from images captured from multiple perspectives. Secondly, estimating ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: The proposed Neural Assembler architecture. An image encoder outputs the visual embeddings of multi-view images. The shape and texture library are provided as ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Illustration of 3D position prediction mod- ule. During inference, the pose of each object in 3D space is obtained by merging the poses ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Comparison of per-scene metrics.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: The probability distribution of CCA. The metric CCA proposed by Chen et al. (2019) is adopted here for the brick order evaluation. It ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Result from CLEVR-Assembly Dataset. Multi-view Images Brick Type 3D Pos Rotation (0, 0, 4) 0 Last Step
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Result from LEGO-Assembly Dataset.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Comparison of baselines on per-step metrics.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | (2022b) 7.3 21.8 Ours 34.2 58.5 Real-World Dataset LSTM Graves and Graves (2012) 7.3 21.8 DETR3D Wang et al. | embodiment, simulator version and control stack | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Task/environment | (2022b) 2.4 12.8 Ours 22.0 50.5 Table 3: The performance of the fine-tuned model on the novel simulated dataset and real-world dataset. | reset, timeout, object/scene variation | p. 8 (4 Experiments), p. 9 (4 Experiments) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 2 (1 Introduction), p. 1 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For per-step metrics, we evaluate the Pos Acc and Rot Acc (3D position accuracy and rotation accuracy), Shape Acc and Texture Acc (shape accuracy ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| (2022b) 16.8 4.5 89.5 35.3 Ours (w/o consensus) 28.6 6.6 92.1 45.5 Ours (2 views) 22.0 4.6 88.7 38.6 Ours (3 views) 25.7 9.3 ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| It is evident that Neural Assembler is adept at excluding perspectives where bricks are obscured by predicting confidence scores, thereby identifying optimal perspectives for ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| The shape, material, iou prediction heads are implemented using 3-layer MLP and ReLU activations. | definition/direction/unit from same section | p. 6 (4 Experiments) |
| This comparison is pivotal in underscoring the adaptability and accuracy of our model in 3D pose estimation, a crucial aspect in varied application domains. | definition/direction/unit from same section | p. 6 (4 Experiments) |
| Figure 3: Illustration of 3D position prediction mod- ule. During inference, the pose of each object in 3D space is obtained by merging the ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| For 3D pose estimation, we select the perspective with a confidence score greater than a threshold and extract its 12 | definition/direction/unit from same section | p. 12 (A.2 Implementation Details) |
| Fig.6 further shows the generated assembly instructions for a LEGO model. | definition/direction/unit from same section | p. 8 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Neural Assembler outperforms baseline models in all metrics considered. | comparison identity and matched condition | p. 7 (4 Experiments) |
| (2022b), a prominent baseline in the realm of object detection within autonomous driving scenarios. | comparison identity and matched condition | p. 6 (4 Experiments) |
| In addressing this novel task, for which no direct baseline exists, we have established a comparative framework against three distinct baseline methods to demonstrate ... | comparison identity and matched condition | p. 6 (4 Experiments) |
| Number of views Furthermore, we compared the results obtained by accepting different numbers of images as input. | comparison identity and matched condition | p. 7 (4 Experiments) |
| The results in Table 1 and Table 2 shows that Neural Assembler can yield more accurate results than other baselines. | comparison identity and matched condition | p. 8 (4 Experiments) |
| Table 2: Comparison of baselines on per-step metrics. | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Without scene consensus, it is difficult for the model to integrate information from multi-view images to obtain the overall information of each brick. | component/input/data sensitivity | p. 7 (4 Experiments) |
| Furthermore, for the object pose estimation component, our methodology is rigorously benchmarked against DETR3D Wang et al. | component/input/data sensitivity | p. 6 (4 Experiments) |
| (2022b) 2.4 12.8 Ours 22.0 50.5 Table 3: The performance of the fine-tuned model on the novel simulated dataset and real-world dataset. | component/input/data sensitivity | p. 8 (4 Experiments) |
| This data facilitated the creation of a synthetic dataset, used for fine-tuning the model initially trained on the CLEVR-Assembly dataset. | component/input/data sensitivity | p. 9 (4 Experiments) |
| The manipulation component involves a Robotiq 2F-85 two-finger gripper, providing adept grasping capabilities. | component/input/data sensitivity | p. 13 (A.4 Real-World Robotic Experiment) |
| Figure 1: Schematic illustration of the proposed Neural Assembler. See Section 3 for more details. integrate information from images captured from multiple perspectives. Secondly, ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| For this novel task, we propose an end-to-end neural network, dubbed as Neural Assembler. | As indicated in Table 3, the Neural Assembler achieves performance in real-world experiments close to the results obtained in simulated environments, demonstrating its robust ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 6 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Primary metric/result | As shown in Tables 1 and 2, the result shows that more perspectives as input can improve the performance. | numeric claim only at cited anchor | p. 7 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 6 / 4 Experiments - extractive body cue:** Training is conducted on an RTX 3090 GPU using AdamW, with an initial rate of 5e-4, decaying by 0.8 per epoch, a weight decay of ...
- **p. 12 / A.1 Dataset Generation - extractive body cue:** The rotation is sampled from (0, (90 · k ± 30)◦, (45 ± 15)◦) for camera k.
- **p. 12 / A.2 Implementation Details - extractive body cue:** All models are trained using AdamW, with an initial rate of 5e-4, decaying by 0.8 per epoch, a weight decay of 1e-3, and batch size ...
- **p. 13 / A.2 Implementation Details - extractive body cue:** Model Architecture A pre-trained Vision Transformer (ViT-B/16) processes an image of size 224×224, yielding image features of dimension 768×(196+1).
- **p. 12 / A.2 Implementation Details - extractive body cue:** All models are trained using AdamW, with an initial rate of 5e-4, decaying by 0.8 per epoch, a weight decay of 1e-3, and batch size ...
- **p. 13 / A.2 Implementation Details - extractive body cue:** Model Architecture A pre-trained Vision Transformer (ViT-B/16) processes an image of size 224×224, yielding image features of dimension 768×(196+1).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The operation is rolled back if the brick is unstable upon free fall. | p. 12 (A.1 Dataset Generation) |
| body limitation/failure cue | Figure 8: Failure case. The model confidently but incorrectly predicts the highlighted block in View 1, while in View 3, despite correct keypoint identification, ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | Prediction Ground Truth View 1 View 2 View 3 View 4 Figure 8: Failure case. | p. 9 (4 Experiments) |
| body limitation/failure cue | Lastly, in evaluating our multi-view image feature fusion process, we contrast our approach with a method that does not leverage scene consensus. | p. 6 (4 Experiments) |
| body limitation/failure cue | The two datasets, characterized by brick number, occlusion from variable visibility, and complex assembly graph, reflect the complexity of assembly tasks. | p. 6 (4 Experiments) |
| body limitation/failure cue | This is because each brick may not be seen from some perspectives due to the existence of occlusion. | p. 7 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Training is conducted on an RTX 3090 GPU using AdamW, with an initial rate of 5e-4, decaying by 0.8 per epoch, a weight decay ... | p. 6 (4 Experiments) |
| We use the pre-trained ViT-B/16 weights and fine-tune it with the learning rate setting to the same value as other modules. | p. 12 (A.2 Implementation Details) |
| (2017) point cloud encoder, and a ResNet-18He et al. | p. 6 (4 Experiments) |
| 1 2 3 4 5 6 7 8 9 Number of Steps 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 Probability (a) CLEVR-Assembly ... | p. 7 (4 Experiments) |
| Hyperparameters For training loss: L = α · Lcount + β · Lgraph + Lpose, (6) Lpose = Lkeypoint + Lmask + γ1Lrotation (7) ... | p. 12 (A.2 Implementation Details) |
| For the Transformer Decoder, the query is constituted by object queries of dimension (N1 + N2 + 16) × 256. | p. 13 (A.2 Implementation Details) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 12 / A.1 Dataset Generation - extractive body cue:** The operation is rolled back if the brick is unstable upon free fall.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 8: Failure case. The model confidently but incorrectly predicts the highlighted block in View 1, while in View 3, despite correct keypoint identification, occlusion ...
- **p. 9 / 4 Experiments - extractive body cue:** Prediction Ground Truth View 1 View 2 View 3 View 4 Figure 8: Failure case.
- **p. 6 / 4 Experiments - extractive body cue:** Lastly, in evaluating our multi-view image feature fusion process, we contrast our approach with a method that does not leverage scene consensus.
- **p. 6 / 4 Experiments - extractive body cue:** The two datasets, characterized by brick number, occlusion from variable visibility, and complex assembly graph, reflect the complexity of assembly tasks.
- **p. 7 / 4 Experiments - extractive body cue:** This is because each brick may not be seen from some perspectives due to the existence of occlusion.

- **PDF anchors reviewed:** datasets p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), metrics p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments), p. 5 (Figure/Table caption), baselines p. 7 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (Figure/Table caption), results p. 9 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 6 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
