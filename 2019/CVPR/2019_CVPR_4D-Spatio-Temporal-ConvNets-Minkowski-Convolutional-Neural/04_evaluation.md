# Evaluation - 4D Spatio-Temporal ConvNets: Minkowski Convolutional Neural Networks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1904.08755; PDF retrieval source: https://arxiv.org/pdf/1904.08755. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (7.4. Results and Analysis), p. 7 (7.4. Results and Analysis), p. 8 (7.4. Results and Analysis), p. 8 (7.4. Results and Analysis), p. 13 (Figure/Table caption), p. 14 (Figure/Table caption)): We trained the same network for 60k iterations with 2cm voxel and achieved 72.1% mIoU on ScanNet after the deadline.

## Evaluation Body Digest

- **p. 7 / 7.3. Datasets - extractive body cue:** In total, the train/val/test set contain 20k/815/1886 3D scenes respectively.
- **p. 7 / 7.3. Datasets - extractive body cue:** We use the Synthia dataset [27] to create 3D video sequences.
- **p. 8 / 7.4. Results and Analysis - extractive body cue:** We use the Synthia datasets with and without noise for 3D and 4D analysis and results are presented in Tab.
- **p. 8 / 7.4. Results and Analysis - extractive body cue:** Specifically, when we simulate noise in sensory inputs on the 4D Synthia dataset, we can observe that the 4D networks are more robust to noise.
- **p. 7 / 7.3. Datasets - extractive body cue:** Per class IoU in the supplementary material.
- **p. 7 / 7.2. Training and Evaluation - extractive body cue:** For evaluation, we use the standard mean Intersection over Union (mIoU) and mean Accuracy (mAcc) for metrics following the previous works.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Segmentation results on the noisy Synthia 4D dataset IoU Building Road Sidewalk Fence Vegetation Pole
- **p. 8 / 7.4. Results and Analysis - extractive body cue:** However, the results quickly saturate.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 7. Experiments (p. 7); 7.1. Implementation (p. 7); 7.2. Training and Evaluation (p. 7); 7.3. Datasets (p. 7); 7.4. Results and Analysis (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 7.4. Results and Analysis | EMPIRICAL / SIMULATION | We trained the same network for 60k iterations with 2cm voxel and achieved 72.1% mIoU on ScanNet after the deadline. | p. 7 (7.4. Results and Analysis) |
| 7.4. Results and Analysis | EMPIRICAL / SIMULATION | We were able to achieve +19% mIOU on ScanNet, and +7% on Stanford compared with the bestpublished works by the CVPR deadline. | p. 7 (7.4. Results and Analysis) |
| 7.4. Results and Analysis | EMPIRICAL / SIMULATION | 4D analysis The RueMongue dataset is a small dataset that ranges one section of a street, so with the smallest network, we were able ... | p. 8 (7.4. Results and Analysis) |
| 7.4. Results and Analysis | EMPIRICAL / SIMULATION | However, the results quickly saturate. | p. 8 (7.4. Results and Analysis) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Table 1: ScanNet [1] 3D Segmentation Benchmark Results Method bath bed bksf cab chair cntr curt desk door floor othr pic ref show sink ... | p. 13 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 7.3. Datasets - extractive body cue:** In total, the train/val/test set contain 20k/815/1886 3D scenes respectively.
- **p. 7 / 7.3. Datasets - extractive body cue:** We use the Synthia dataset [27] to create 3D video sequences.
- **p. 8 / 7.4. Results and Analysis - extractive body cue:** We use the Synthia datasets with and without noise for 3D and 4D analysis and results are presented in Tab.
- **p. 8 / 7.4. Results and Analysis - extractive body cue:** Specifically, when we simulate noise in sensory inputs on the 4D Synthia dataset, we can observe that the 4D networks are more robust to noise.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: An example of 3D video: 3D scenes at different time steps. Best viewed on display. 1D: Line 2D: Square 3D: Cube 4D: Tesseract
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 2: 2D projections of hypercubes in various dimen- sions more affordable and widely used for robotics applications, 3D-videos became readily-available sources of input for ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Various kernels in space-time. The red arrow indicates the temporal dimension and the other two axes are for spatial dimensions. The third spatial ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4: Architecture of ResNet18 (left) and MinkowskiNet18 (right). Note the structural similarity. × indicates a hypercubic kernel, + indicates a hypercross kernel. (best viewed ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Architecture of MinkowskiUNet32. × indicates a hypercubic kernel, + indicates a hypercross kernel. (best viewed on display) variations of the same architecture for ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: 3D Semantic Label Benchmark on ScanNet† [5] Method mIOU ScanNet [5] 30.6 SSC-UNet [10] 30.8 PointNet++ [23] 33.9
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Segmentation results on the 4D Synthia dataset
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Segmentation results on the noisy Synthia 4D dataset IoU Building Road Sidewalk Fence Vegetation Pole

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In total, the train/val/test set contain 20k/815/1886 3D scenes respectively. | embodiment, simulator version and control stack | p. 7 (7.3. Datasets), p. 7 (7.3. Datasets) |
| Task/environment | We use the Synthia dataset [27] to create 3D video sequences. | reset, timeout, object/scene variation | p. 7 (7.3. Datasets), p. 8 (7.4. Results and Analysis) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (4.3. Max Pooling), p. 4 (4.3. Max Pooling) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (Abstract), p. 3 (3.1. Generalized Sparse Convolution) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Per class IoU in the supplementary material. | definition/direction/unit from same section | p. 7 (7.3. Datasets) |
| For evaluation, we use the standard mean Intersection over Union (mIoU) and mean Accuracy (mAcc) for metrics following the previous works. | definition/direction/unit from same section | p. 7 (7.2. Training and Evaluation) |
| Table 3: Segmentation results on the noisy Synthia 4D dataset IoU Building Road Sidewalk Fence Vegetation Pole | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| However, the results quickly saturate. | definition/direction/unit from same section | p. 8 (7.4. Results and Analysis) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We were able to achieve +19% mIOU on ScanNet, and +7% on Stanford compared with the bestpublished works by the CVPR deadline. | comparison identity and matched condition | p. 7 (7.4. Results and Analysis) |
| It allows us to gauge the performance of the high-dimensional networks with the same architecture with other state-of-the-art methods. | comparison identity and matched condition | p. 7 (7. Experiments) |
| Note that the number of parameters added to the 4D network compared with the 3D network is less than 6.4 % and 6e-3 % ... | comparison identity and matched condition | p. 8 (7.4. Results and Analysis) |
| We use various 3D and 4D networks with and without TS-CRF. | comparison identity and matched condition | p. 8 (7.4. Results and Analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Next, we create multiple 4D datasets from 3D datasets that have temporal sequences and analyze each of the proposed components for ablation study. | component/input/data sensitivity | p. 7 (7. Experiments) |
| We feed an entire room to a MinkowskiNet fully convolutionally without cropping. | component/input/data sensitivity | p. 7 (7.3. Datasets) |
| We use various 3D and 4D networks with and without TS-CRF. | component/input/data sensitivity | p. 8 (7.4. Results and Analysis) |
| We use the Synthia datasets with and without noise for 3D and 4D analysis and results are presented in Tab. | component/input/data sensitivity | p. 8 (7.4. Results and Analysis) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To overcome this challenge, we propose custom kernels with non-(hyper)-cubic shapes using the generalized sparse convolution. | We trained the same network for 60k iterations with 2cm voxel and achieved 72.1% mIoU on ScanNet after the deadline. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (7.4. Results and Analysis), p. 7 (7.4. Results and Analysis), p. 8 (7.4. Results and Analysis), p. 8 (7.4. Results and Analysis), p. 13 (Figure/Table caption), p. 14 (Figure/Table caption) |
| Primary metric/result | We were able to achieve +19% mIOU on ScanNet, and +7% on Stanford compared with the bestpublished works by the CVPR deadline. | numeric claim only at cited anchor | p. 7 (7.4. Results and Analysis) |

- Numeric sentences retained from the body:
- **p. 2 / 1. Introduction - extractive body cue:** 3At the time of submission, our proposed method was the first very deep 3D convolutional neural networks with more than 20 layers.
- **p. 4 / 4.1. Sparse Tensor Quantization - extractive body cue:** Algorithm 1 GPU Sparse Tensor Quantization Inputs: coordinates Cp ∈RN×D, features Fp ∈RN×Nf , target labels l ∈ZN +, quantization step size vl C′ p ...
- **p. 4 / 4.3. Max Pooling - extractive body cue:** Algorithm 3 GPU Sparse Tensor MaxPooling Input: input feature F, output mapping O (I′, O′) ←SortByKey(I, key=O) S ←Sequence(length(O′)) S′, O" ←ReduceByKey(S, key=O′, fn=f) return ...
- **p. 5 / 4.5. Non-spatial Functions - extractive body cue:** Algorithm 4 GPU Sparse Tensor AvgPooling Input: mapping M = (I, O), features F, one vector 1 SM = coo2csr(row=O, col=I, val=1) F ′ = ...
- **p. 5 / 5.2. Residual Minkowski Networks - extractive body cue:** For the first layer, instead of a 7 × 7 2D convolution, we use a 5×5×5×1 generalized sparse convolution.
- **p. 5 / 5.2. Residual Minkowski Networks - extractive body cue:** We use multiple Sparse Conv 3×3×3+3, 256 Sparse Conv 3×3×3+3, 64 Sparse Conv 3×3×3+3, 64 Sparse Conv 3×3×3+3, 64 Sparse Conv 3×3×3+3, 64 Sparse Conv ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Specifically, when we simulate noise in sensory inputs on the 4D Synthia dataset, we can observe that the 4D networks are more robust to ... | p. 8 (7.4. Results and Analysis) |
| body limitation/failure cue | However, the loss does not enforce consistency as it does not have pair-wise terms. | p. 6 (6. Trilateral Stationary-CRF) |
| body limitation/failure cue | We used elastic distortion, Gaussian noise, and chromatic shift in the color for the noisy 4D Synthia experiments. | p. 7 (7.3. Datasets) |
| body limitation/failure cue | Since the dataset is purely synthetic, we added various noise to the input point clouds to simulate noisy observations. | p. 7 (7.3. Datasets) |
| body limitation/failure cue | As the input pointcloud coordinates are noisy, averaging along the temporal dimension introduces noise. | p. 8 (7.4. Results and Analysis) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We use Momentum SGD with the Poly scheduler to train networks from learning rate 1e-1 and apply data augmentation including random scaling, rotation around ... | p. 7 (7.2. Training and Evaluation) |
| It only computes outputs for predefined coordinates and saves them into a compact sparse tensor (Sec. | p. 2 (1. Introduction) |
| 1, we list the GPU function for this process. | p. 3 (4.1. Sparse Tensor Quantization) |
| Thus, this creates nontrivial implementation for a max/average pooling. | p. 4 (4.3. Max Pooling) |
| A CPU-version works similarly except that all reduction and sorting are processed serially. | p. 4 (4.1. Sparse Tensor Quantization) |
| Thus, we can create a high-dimensional network only with generalized sparse convolutions, making the implementation easier and generic. | p. 5 (5.2. Residual Minkowski Networks) |
| Algorithm 4 GPU Sparse Tensor AvgPooling Input: mapping M = (I, O), features F, one vector 1 SM = coo2csr(row=O, col=I, val=1) F ′ ... | p. 5 (4.5. Non-spatial Functions) |
| 4 is equivalent to a generalized sparse convolution in the 7D space since φp is stationary and each edge between xi, xj can be ... | p. 6 (6.3. Learning with 7D Sparse Convolution) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 7.4. Results and Analysis - extractive body cue:** Specifically, when we simulate noise in sensory inputs on the 4D Synthia dataset, we can observe that the 4D networks are more robust to noise.
- **p. 6 / 6. Trilateral Stationary-CRF - extractive body cue:** However, the loss does not enforce consistency as it does not have pair-wise terms.
- **p. 7 / 7.3. Datasets - extractive body cue:** We used elastic distortion, Gaussian noise, and chromatic shift in the color for the noisy 4D Synthia experiments.
- **p. 7 / 7.3. Datasets - extractive body cue:** Since the dataset is purely synthetic, we added various noise to the input point clouds to simulate noisy observations.
- **p. 8 / 7.4. Results and Analysis - extractive body cue:** As the input pointcloud coordinates are noisy, averaging along the temporal dimension introduces noise.

- **Evidence anchors reviewed:** datasets p. 7 (7.3. Datasets), p. 7 (7.3. Datasets), p. 8 (7.4. Results and Analysis), p. 8 (7.4. Results and Analysis), metrics p. 7 (7.3. Datasets), p. 7 (7.2. Training and Evaluation), p. 8 (Figure/Table caption), p. 8 (7.4. Results and Analysis), baselines p. 7 (7.4. Results and Analysis), p. 7 (7. Experiments), p. 8 (7.4. Results and Analysis), p. 8 (7.4. Results and Analysis), results p. 7 (7.4. Results and Analysis), p. 7 (7.4. Results and Analysis), p. 8 (7.4. Results and Analysis), p. 8 (7.4. Results and Analysis), p. 13 (Figure/Table caption), p. 14 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
