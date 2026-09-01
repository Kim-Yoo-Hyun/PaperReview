# Evaluation - KPConv: Flexible and Deformable Convolution for Point Clouds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1904.08889; PDF retrieval source: https://arxiv.org/pdf/1904.08889. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. 3D Scene Segmentation), p. 8 (4.4. Learned Features and Effective Receptive Field), p. 5 (4.1. 3D Shape Classification and Segmentation), p. 6 (4.1. 3D Shape Classification and Segmentation), p. 7 (4.4. Learned Features and Effective Receptive Field), p. 7 (4.2. 3D Scene Segmentation)): Among these 4 datasets, KPConv deformable kernels improved the results on Paris-Lille-3D and S3DIS while the rigid version was better on Scannet and Semantic3D.

## Evaluation Body Digest

- **p. 6 / 4.2. 3D Scene Segmentation - extractive PDF cue:** The 3D scenes in these datasets are too big to be segmented as a whole.
- **p. 6 / 4.2. 3D Scene Segmentation - extractive PDF cue:** Semantic3D is an online benchmark comprising several fixed lidar scans of different outdoor scenes.
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** We use Scannet dataset (same parameters as before) and use the official validation set, because the test set cannot be used for such evaluations.
- **p. 8 / 4.4. Learned Features and Effective Receptive Field - extractive PDF cue:** This adaptive behavior shows that deformable KPConv improves the network ability to adapt to the geometry of the scene objects, and explains the better performances ...
- **p. 5 / 4.1. 3D Shape Classification and Segmentation - extractive PDF cue:** For benchmarking purpose, we use data provided by [27].
- **p. 5 / 4.1. 3D Shape Classification and Segmentation - extractive PDF cue:** First, we evaluate our networks on two common model datasets.
- **p. 7 / 4.2. 3D Scene Segmentation - extractive PDF cue:** An illustration of segmented scenes on Semantic3D and S3DIS is shown in Figure 4.
- **p. 8 / 4.4. Learned Features and Effective Receptive Field - extractive PDF cue:** ERF values are merged with scene colors as red intensity.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. 3D Scene Segmentation | SYSTEM / EVALUATION SCOPE UNRESOLVED | Among these 4 datasets, KPConv deformable kernels improved the results on Paris-Lille-3D and S3DIS while the rigid version was better on Scannet and Semantic3D. | p. 6 (4.2. 3D Scene Segmentation) |
| 4.4. Learned Features and Effective Receptive Field | SYSTEM / EVALUATION SCOPE UNRESOLVED | This adaptive behavior shows that deformable KPConv improves the network ability to adapt to the geometry of the scene objects, and explains the better ... | p. 8 (4.4. Learned Features and Effective Receptive Field) |
| 4.1. 3D Shape Classification and Segmentation | SYSTEM / EVALUATION SCOPE UNRESOLVED | As shown on Table 1, our networks outperform other state-of-the-art methods using only points (we do not take into account methods using normals as ... | p. 5 (4.1. 3D Shape Classification and Segmentation) |
| 4.1. 3D Shape Classification and Segmentation | SYSTEM / EVALUATION SCOPE UNRESOLVED | KP-FCNN outperforms all other algorithms, including those using additional inputs like images or normals. | p. 6 (4.1. 3D Shape Classification and Segmentation) |
| 4.4. Learned Features and Effective Receptive Field | SYSTEM / EVALUATION SCOPE UNRESOLVED | To achieve a deeper understanding of KPConv, we offer two insights of the learning mechanisms. | p. 7 (4.4. Learned Features and Effective Receptive Field) |

## Dataset / Benchmark Role

- **p. 6 / 4.2. 3D Scene Segmentation - extractive PDF cue:** The 3D scenes in these datasets are too big to be segmented as a whole.
- **p. 6 / 4.2. 3D Scene Segmentation - extractive PDF cue:** Semantic3D is an online benchmark comprising several fixed lidar scans of different outdoor scenes.
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** We use Scannet dataset (same parameters as before) and use the official validation set, because the test set cannot be used for such evaluations.
- **p. 8 / 4.4. Learned Features and Effective Receptive Field - extractive PDF cue:** This adaptive behavior shows that deformable KPConv improves the network ability to adapt to the geometry of the scene objects, and explains the better performances ...
- **p. 5 / 4.1. 3D Shape Classification and Segmentation - extractive PDF cue:** For benchmarking purpose, we use data provided by [27].
- **p. 5 / 4.1. 3D Shape Classification and Segmentation - extractive PDF cue:** First, we evaluate our networks on two common model datasets.
- **p. 7 / 4.2. 3D Scene Segmentation - extractive PDF cue:** An illustration of segmented scenes on Semantic3D and S3DIS is shown in Figure 4.
- **p. 8 / 4.4. Learned Features and Effective Receptive Field - extractive PDF cue:** ERF values are merged with scene colors as red intensity.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. KPConv illustrated on 2D points. Input points with a constant scalar feature (in grey) are convolved through a KPConv that is defined by ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Comparison between an image convolution (left) and a KPConv (right) on 2D points for a simpler illustration. In the image, each pixel feature ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Deformable KPConv illustrated on 2D points. gdeform(yi, ∆(x)) = X k<K h (yi, exk + ∆k(x)) Wk (5) We define the offsets ∆k(x) ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. 3D Shape Classification and Segmentation results. For generalizability to real data, we only consider scores obtained without shape normals on ModelNet40 dataset. The ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. 3D scene segmentation scores (mIoU). Scannet, Se- mantic3D and Paris-Lille-3D (PL3D) scores are taken from their respective online benchmarks (reduced-8 challenge for Seman- ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Outdoor and Indoor scenes, respectively from Seman- tic3D and S3DIS, classified by KP-FCNN with deformable ker- nels. KPConv performs better than rigid KPConv ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5. Ablation study on Scannet validation set. Evolution of the mIoU when reducing the number of kernel points.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6. Low and high level features learned in KP-CNN. Each feature is displayed on 2 input point clouds taken from Model- Net40. High activations ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The 3D scenes in these datasets are too big to be segmented as a whole. | embodiment, simulator version and control stack | p. 6 (4.2. 3D Scene Segmentation), p. 6 (4.2. 3D Scene Segmentation) |
| Task/environment | Semantic3D is an online benchmark comprising several fixed lidar scans of different outdoor scenes. | reset, timeout, object/scene variation | p. 6 (4.2. 3D Scene Segmentation), p. 7 (4.3. Ablation Study) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 6. Semantic segmentation IoU scores on S3DIS Area-5. Additionally, we give the mean class recall, a measure that some previous works call mean ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| Table 1. 3D Shape Classification and Segmentation results. For generalizability to real data, we only consider scores obtained without shape normals on ModelNet40 dataset. ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Compared to other point convolution architectures [2, 20, 41], KPConv performances exceed previous scores by 19 mIoU points on Scannet and 9 mIoU points ... | definition/direction/unit from same section | p. 6 (4.2. 3D Scene Segmentation) |
| S3DIS scores are given for Area-5 (see supplementary material for k-fold). studies are not reflected by the test scores on this benchmark. | definition/direction/unit from same section | p. 7 (4.2. 3D Scene Segmentation) |
| Scannet, Semantic3D and Paris-Lille-3D (PL3D) scores are taken from their respective online benchmarks (reduced-8 challenge for Semantic3D). | definition/direction/unit from same section | p. 7 (4.2. 3D Scene Segmentation) |
| We also notice that rigid KPConv performances are slightly better. | definition/direction/unit from same section | p. 5 (4.1. 3D Shape Classification and Segmentation) |
| Because of our subsampling strategy, the input point clouds do not all have the same number of points, which is not a problem as ... | definition/direction/unit from same section | p. 5 (4.1. 3D Shape Classification and Segmentation) |
| Indeed, it covers the whole bed, and concentrates more on the chair that on the surrounding ground. | definition/direction/unit from same section | p. 8 (4.4. Learned Features and Effective Receptive Field) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As shown on Table 1, our networks outperform other state-of-the-art methods using only points (we do not take into account methods using normals as ... | comparison identity and matched condition | p. 5 (4.1. 3D Shape Classification and Segmentation) |
| KP-FCNN outperforms all other algorithms, including those using additional inputs like images or normals. | comparison identity and matched condition | p. 6 (4.1. 3D Shape Classification and Segmentation) |
| As shown in Table 2, our architecture ranks second on Scannet and outperforms all other segmentation architectures on the other datasets. | comparison identity and matched condition | p. 6 (4.2. 3D Scene Segmentation) |
| We found that the deformable KPConv outperformed its rigid counterpart on several different validation sets (see Section 4.3). | comparison identity and matched condition | p. 7 (4.2. 3D Scene Segmentation) |
| We believe KPConv could thrive on larger datasets because its kernel combines a strong descriptive power (compared to other simpler representations, like the linear ... | comparison identity and matched condition | p. 7 (4.2. 3D Scene Segmentation) |
| Figure 2. Comparison between an image convolution (left) and a KPConv (right) on 2D points for a simpler illustration. In the image, each pixel ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| For generalizability to real data, we only consider scores obtained without shape normals on ModelNet40 dataset. | component/input/data sensitivity | p. 6 (4.1. 3D Shape Classification and Segmentation) |
| SubSparseCNN score on Scannet was not reported in their original paper [9], so it is hard to compare without knowing their experimental setup. | component/input/data sensitivity | p. 6 (4.2. 3D Scene Segmentation) |
| Ablation study on Scannet validation set. | component/input/data sensitivity | p. 7 (4.4. Learned Features and Effective Receptive Field) |
| We conduct an ablation study to support our claim that deformable KPConv has a stronger descriptive power than rigid KPConv. | component/input/data sensitivity | p. 7 (4.3. Ablation Study) |
| Figure 11. Illustration of the deformations learned by a KPConv network with or without regularization. | component/input/data sensitivity | p. 13 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Furthermore, we propose a deformable version of our convolution [7], which consists of learning local shifts applied to the kernel points (see Figure 3). | Among these 4 datasets, KPConv deformable kernels improved the results on Paris-Lille-3D and S3DIS while the rigid version was better on Scannet and Semantic3D. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. 3D Scene Segmentation), p. 8 (4.4. Learned Features and Effective Receptive Field), p. 5 (4.1. 3D Shape Classification and Segmentation), p. 6 (4.1. 3D Shape Classification and Segmentation), p. 7 (4.4. Learned Features and Effective Receptive Field), p. 7 (4.2. 3D Scene Segmentation) |
| Primary metric/result | This adaptive behavior shows that deformable KPConv improves the network ability to adapt to the geometry of the scene objects, and explains the better ... | numeric claim only at cited anchor | p. 8 (4.4. Learned Features and Effective Receptive Field) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. 3D Shape Classification and Segmentation - extractive PDF cue:** ShapenetPart is a collection of 16,681 point clouds from 16 categories, each with 2-6 part labels.
- **p. 5 / 4.1. 3D Shape Classification and Segmentation - extractive PDF cue:** On average, a ModelNet40 object point cloud comprises 6,800 points in our framework.
- **p. 6 / 4.1. 3D Shape Classification and Segmentation - extractive PDF cue:** The clouds are smaller (2,300 points on average), and we can process 4.1 batches of 16 shapes per second.
- **p. 6 / 4.2. 3D Scene Segmentation - extractive PDF cue:** Indeed, despite comprising 15 scenes and 4 billion points, it contains a majority of ground, building and vegetation points and a few real objects like ...
- **p. 6 / 4.2. 3D Scene Segmentation - extractive PDF cue:** Although this is not the case of Scannet, which comprises more than 1,500 scenes with various objects and shapes, our validation
- **p. 5 / 3.4. Kernel Point Network Architectures - extractive PDF cue:** Those features are concatenated to the upsampled ones and processed by a unary convolution, which is the equivalent of a 1×1 convolution in image or ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We use Scannet dataset (same parameters as before) and use the official validation set, because the test set cannot be used for such evaluations. | p. 7 (4.3. Ablation Study) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| This constant feature encodes the geometry of the input points. | p. 5 (4.1. 3D Shape Classification and Segmentation) |
| It is computed as the gradient of KPConv responses at this particular location with respect to the input point features. | p. 8 (4.4. Learned Features and Effective Receptive Field) |
| To apprehend the differences between the representations learned by rigid and deformable KPConv, we can compute its Effective Receptive Field (ERF) [22] at different ... | p. 8 (4.4. Learned Features and Effective Receptive Field) |
| Skip links are used to pass the features between intermediate layers of the encoder and the decoder. | p. 5 (3.4. Kernel Point Network Architectures) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** We use Scannet dataset (same parameters as before) and use the official validation set, because the test set cannot be used for such evaluations.

- **PDF anchors reviewed:** datasets p. 6 (4.2. 3D Scene Segmentation), p. 6 (4.2. 3D Scene Segmentation), p. 7 (4.3. Ablation Study), p. 8 (4.4. Learned Features and Effective Receptive Field), p. 5 (4.1. 3D Shape Classification and Segmentation), p. 5 (4.1. 3D Shape Classification and Segmentation), metrics p. 14 (Figure/Table caption), p. 6 (Figure/Table caption), p. 6 (4.2. 3D Scene Segmentation), p. 7 (4.2. 3D Scene Segmentation), p. 7 (4.2. 3D Scene Segmentation), p. 5 (4.1. 3D Shape Classification and Segmentation), baselines p. 5 (4.1. 3D Shape Classification and Segmentation), p. 6 (4.1. 3D Shape Classification and Segmentation), p. 6 (4.2. 3D Scene Segmentation), p. 7 (4.2. 3D Scene Segmentation), p. 7 (4.2. 3D Scene Segmentation), p. 3 (Figure/Table caption), results p. 6 (4.2. 3D Scene Segmentation), p. 8 (4.4. Learned Features and Effective Receptive Field), p. 5 (4.1. 3D Shape Classification and Segmentation), p. 6 (4.1. 3D Shape Classification and Segmentation), p. 7 (4.4. Learned Features and Effective Receptive Field), p. 7 (4.2. 3D Scene Segmentation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
