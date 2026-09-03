# Evaluation - ULIP: Learning a Unified Representation of Language, Images, and Point Clouds for 3D Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2212.05171; PDF retrieval source: https://arxiv.org/pdf/2212.05171. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), p. 4 (4.1. 3D Backbone Networks), p. 8 (Figure/Table caption)): Table 2. Standard 3D classification results on ModelNet40. ULIP significantly improves our baselines. Our best number achieves new SOTA. * means a voting technique is applied to the method to ...

## Evaluation Body Digest

- **p. 4 / 4.2. Downstream Datasets - extractive body cue:** ModelNet40 is a synthetic dataset of 3D CAD models.
- **p. 4 / 4.2. Downstream Datasets - extractive body cue:** We use the following two datasets for both standard and zero-shot 3D classification.
- **p. 5 / 4.3. Implementation Details - extractive body cue:** On ScanObjectNN, we use the learning rate of 0.03 and finetune for 350 epochs with batch size 32 for PointMLP.
- **p. 5 / 4.3. Implementation Details - extractive body cue:** We keep using the same prompt strategy as it is during pre-training when constructing text features for each category candidate in this task.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 5. Zero-shot 3D classification on ScanObjectNN. ULIP- based methods outperform the previous SOTA (PointCLIP) by a very large margin (at least 29.2% on top-1 ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Data efficiency comparison. The X axis indicates the percentage of samples used for training and Y axis denotes the overall accuracy. Both PointMLP ...
- **p. 4 / 4. Experiments - extractive body cue:** To demonstrate the benefits of pre-training 3D backbone networks using ULIP, we conduct experiments on two 3D tasks: a standard 3D classification task that involves ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Illustration of our method. The inputs of multimodal pre-training (Left) are a batch of objects represented as triplets (image, text, point cloud). Image ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 4); 4.2. Downstream Datasets (p. 4); 4.3. Implementation Details (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 2. Standard 3D classification results on ModelNet40. ULIP significantly improves our baselines. Our best number achieves new SOTA. * means a voting technique ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 5. Zero-shot 3D classification on ScanObjectNN. ULIP- based methods outperform the previous SOTA (PointCLIP) by a very large margin (at least 29.2% on ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 1. 3D classification results on ScanObjectNN. ULIP signifi- cantly improves our baselines. Our best result outperforms SOTA largely by around 3% on Overall ... | p. 5 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 3. Data efficiency comparison. The X axis indicates the percentage of samples used for training and Y axis denotes the overall accuracy. Both ... | p. 6 (Figure/Table caption) |
| 4.1. 3D Backbone Networks | EMPIRICAL / SOURCE-REPORTED EVALUATION | It improves its recognition ability by conducting self-supervised pre-training on ShapeNet55. | p. 4 (4.1. 3D Backbone Networks) |

## Dataset / Benchmark Role

- **p. 4 / 4.2. Downstream Datasets - extractive body cue:** ModelNet40 is a synthetic dataset of 3D CAD models.
- **p. 4 / 4.2. Downstream Datasets - extractive body cue:** We use the following two datasets for both standard and zero-shot 3D classification.
- **p. 5 / 4.3. Implementation Details - extractive body cue:** On ScanObjectNN, we use the learning rate of 0.03 and finetune for 350 epochs with batch size 32 for PointMLP.
- **p. 5 / 4.3. Implementation Details - extractive body cue:** We keep using the same prompt strategy as it is during pre-training when constructing text features for each category candidate in this task.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Illustration of ULIP. ULIP improves 3D understand- ing by aligning features from images, texts, and point clouds in the same space. To reduce ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Illustration of our method. The inputs of multimodal pre-training (Left) are a batch of objects represented as triplets (image, text, point cloud). Image ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. 3D classification results on ScanObjectNN. ULIP signifi- cantly improves our baselines. Our best result outperforms SOTA largely by around 3% on Overall Acc. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Standard 3D classification results on ModelNet40. ULIP significantly improves our baselines. Our best number achieves new SOTA. * means a voting technique is ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Data efficiency comparison. The X axis indicates the percentage of samples used for training and Y axis denotes the overall accuracy. Both PointMLP ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Analysis of aligning three vs. two modalities on zero-shot 3D classification on ModelNet40. Results show that aligning represen- tations of three modalities always ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Zero-shot 3D classification on ModelNet40. ULIP-based methods outperform the previous SOTA (PointCLIP) by a very large margin in different evaluation sets.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 5. Zero-shot 3D classification on ScanObjectNN. ULIP- based methods outperform the previous SOTA (PointCLIP) by a very large margin (at least 29.2% on top-1 ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | ModelNet40 is a synthetic dataset of 3D CAD models. | embodiment, simulator version and control stack | p. 4 (4.2. Downstream Datasets), p. 4 (4.2. Downstream Datasets) |
| Task/environment | We use the following two datasets for both standard and zero-shot 3D classification. | reset, timeout, object/scene variation | p. 4 (4.2. Downstream Datasets), p. 5 (4.3. Implementation Details) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3.1. Creating Training Triplets for ULIP), p. 3 (3.1. Creating Training Triplets for ULIP) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 6 (Model) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 5. Zero-shot 3D classification on ScanObjectNN. ULIP- based methods outperform the previous SOTA (PointCLIP) by a very large margin (at least 29.2% on ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 3. Data efficiency comparison. The X axis indicates the percentage of samples used for training and Y axis denotes the overall accuracy. Both ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| To demonstrate the benefits of pre-training 3D backbone networks using ULIP, we conduct experiments on two 3D tasks: a standard 3D classification task that ... | definition/direction/unit from same section | p. 4 (4. Experiments) |
| Figure 2. Illustration of our method. The inputs of multimodal pre-training (Left) are a batch of objects represented as triplets (image, text, point cloud). ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| The inputs of image and text modalities are generated as described in Section 3.1. | definition/direction/unit from same section | p. 5 (4.3. Implementation Details) |
| We use 64 as the batch size, 10-3 as the learning rate, and AdamW as the optimizer. | definition/direction/unit from same section | p. 5 (4.3. Implementation Details) |
| Table 2. Standard 3D classification results on ModelNet40. ULIP significantly improves our baselines. Our best number achieves new SOTA. * means a voting technique ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Figure 4. Qualitative results of real image to point cloud retrieval. Query images are from Caltech101, and point clouds are from Model- Net40. We ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 1. 3D classification results on ScanObjectNN. ULIP signifi- cantly improves our baselines. Our best result outperforms SOTA largely by around 3% on Overall ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Table 5. Zero-shot 3D classification on ScanObjectNN. ULIP- based methods outperform the previous SOTA (PointCLIP) by a very large margin (at least 29.2% on ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 2. Standard 3D classification results on ModelNet40. ULIP significantly improves our baselines. Our best number achieves new SOTA. * means a voting technique ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Figure 4. Qualitative results of real image to point cloud retrieval. Query images are from Caltech101, and point clouds are from Model- Net40. We ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| PointMLP [29] is the SOTA method on standard 3D classification task. | comparison identity and matched condition | p. 4 (4.1. 3D Backbone Networks) |
| Figure 3. Data efficiency comparison. The X axis indicates the percentage of samples used for training and Y axis denotes the overall accuracy. Both ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 3We used the variants provided by [58] in our experiments. | component/input/data sensitivity | p. 5 (4.3. Implementation Details) |
| Table 1. 3D classification results on ScanObjectNN. ULIP signifi- cantly improves our baselines. Our best result outperforms SOTA largely by around 3% on Overall ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Table 9. ModelNet40 Medium Set. Hard Set: We remove both extract category names and their synonyms in our pre-training dataset. The final Hard Set ... | component/input/data sensitivity | p. 12 (Figure/Table caption) |
| Table 8. ModelNet40 All Set. Medium Set: We remove categories whose exact category names exist in our pre-training dataset. The resulting cate- gories in ... | component/input/data sensitivity | p. 12 (Figure/Table caption) |
| Figure 2. Illustration of our method. The inputs of multimodal pre-training (Left) are a batch of objects represented as triplets (image, text, point cloud). ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Table 6. Analysis of aligning three vs. two modalities on zero-shot 3D classification on ScanObjectNN. Results show that aligning representations of three modalities always ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present the standard 3D classification performances of our baselines and our methods on ScanObjectNN in Table 7. | Table 2. Standard 3D classification results on ModelNet40. ULIP significantly improves our baselines. Our best number achieves new SOTA. * means a voting technique ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), p. 4 (4.1. 3D Backbone Networks), p. 8 (Figure/Table caption) |
| Primary metric/result | Table 5. Zero-shot 3D classification on ScanObjectNN. ULIP- based methods outperform the previous SOTA (PointCLIP) by a very large margin (at least 29.2% on ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 4.3. Implementation Details - extractive body cue:** For the 3D input, we uniformly sample Np = 1024, 2048, or 8192 points for accommodating the requirements of different backbones.
- **p. 5 / 4.3. Implementation Details - extractive body cue:** On ModelNet40, we use the learning rate as 0.00015 and fine-tune our model for 200 epochs, with the batch size as 24 for PointNet++.
- **p. 5 / 4.3. Implementation Details - extractive body cue:** For PointMLP, we set the learning rate as 0.1 and fine-tune the model for 300 epochs, with the batch size as 32.
- **p. 5 / 4.3. Implementation Details - extractive body cue:** On ScanObjectNN, we use the learning rate of 0.03 and finetune for 350 epochs with batch size 32 for PointMLP.
- **p. 5 / 4.3. Implementation Details - extractive body cue:** For PointBERT, we use the learning rate of 0.0002 and finetune for 300 epochs with batch size 32.
- **p. 3 / 3.1. Creating Training Triplets for ULIP - extractive body cue:** To obtain images that semantically align well with each CAD model, we synthesize multiview images of each CAD model by placing virtual cameras around each ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | During pre-training, we utilize an advanced version of CLIP, namely SLIP [32], that shows superior performance as our image-text encoders. | p. 5 (4.3. Implementation Details) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For PointBERT, we use the learning rate of 0.0002 and finetune for 300 epochs with batch size 32. | p. 5 (4.3. Implementation Details) |
| For PointMLP, we set the learning rate as 0.1 and fine-tune the model for 300 epochs, with the batch size as 32. | p. 5 (4.3. Implementation Details) |
| Then we input Si into our text encoder fS(·) and get a set of representations, respectively. | p. 3 (3.1. Creating Training Triplets for ULIP) |
| Then a 3D encoder takes the augmented point cloud Pi as input and outputs its 3D representation hP i via | p. 3 (3.1. Creating Training Triplets for ULIP) |
| In this section, we first present experimental settings, including our experimenting 3D backbones, downstream datasets, and implementation details. | p. 4 (4. Experiments) |
| It conducts zero-shot 3D classification by first converting a 3D point cloud into 6 orthogonal depth maps, then using CLIP's image encoder to get ... | p. 6 (Model) |
| We use our pre-trained ULIP with PointBERT as the 3D encoder directly. | p. 8 (4.7. Cross-Modal Retrieval) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 4.3. Implementation Details - extractive body cue:** During pre-training, we utilize an advanced version of CLIP, namely SLIP [32], that shows superior performance as our image-text encoders.

- **Evidence anchors reviewed:** datasets p. 4 (4.2. Downstream Datasets), p. 4 (4.2. Downstream Datasets), p. 5 (4.3. Implementation Details), p. 5 (4.3. Implementation Details), metrics p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 4 (4. Experiments), p. 4 (Figure/Table caption), p. 5 (4.3. Implementation Details), p. 5 (4.3. Implementation Details), baselines p. 5 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption), p. 4 (4.1. 3D Backbone Networks), p. 6 (Figure/Table caption), results p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), p. 4 (4.1. 3D Backbone Networks), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
