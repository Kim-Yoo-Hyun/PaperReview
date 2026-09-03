# Method - Matterport3D: Learning from RGB-D Data in Indoor Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1709.06158; PDF retrieval source: https://arxiv.org/pdf/1709.06158. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (4.3. Surface Normal Estimation), p. 8 (4.5. Semantic Voxel Labeling), p. 7 (4.3. Surface Normal Estimation), p. 7 (4.3. Surface Normal Estimation), p. 5 (4.1. Keypoint Matching), p. 6 (4.3. Surface Normal Estimation)): The model is a fully convolutional neural network consisting of an encoder, which shares the same architecture as VGG-16 from the beginning till the first fully connected layer, and a ...

## Method Body Digest

- **p. 6 / 4.3. Surface Normal Estimation - extractive body cue:** The model is a fully convolutional neural network consisting of an encoder, which shares the same architecture as VGG-16 from the beginning till the first ...
- **p. 8 / 4.5. Semantic Voxel Labeling - extractive body cue:** We use 20 object class labels, and a network following the architecture of ScanNet [7], and training with 52,355 subvolume samples (418,840 augmented samples).
- **p. 7 / 4.3. Surface Normal Estimation - extractive body cue:** We train models by first pretraining on synthetic data and then finetuning on each dataset; i.e., NYUv2 and Matterport3D, respectively.
- **p. 7 / 4.3. Surface Normal Estimation - extractive body cue:** We use Matterport3D data as a large-scale real dataset with high-quality surface normal maps for pretraining, and train the model with a variety of training ...
- **p. 5 / 4.1. Keypoint Matching - extractive body cue:** With the recent success of neural networks, several works have begun to explore the use of deep learning techniques for training state-of-the-art keypoint descriptors that ...
- **p. 6 / 4.3. Surface Normal Estimation - extractive body cue:** For our study, we use the model proposed in Zhang et al.
- **p. 8 / 4.4. Region-Type Classification - extractive body cue:** We then train a convolutional neural network (ResNet-50 [18]) to classify each input image to predict the region type.
- **p. 3 / 3.3. Properties of the Dataset - extractive body cue:** Although we do not have ground-truth camera poses for the dataset and so cannot measure errors objectively, we subjectively estimate that the average registration error ...

## Design Rationale

- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce Matterport3D, a large-scale RGB-D dataset containing 10,800 panoramic views from 194,400 RGB-D images of 90 building-scale scenes.
- **p. 4 / 3.3. Properties of the Dataset - extractive body cue:** Providing scans of homes in their entirety enables opportunities for learning about long-range context, which is critical for holistic scene understanding and autonomous navigation.
- **p. 4 / 3.3. Properties of the Dataset - extractive body cue:** This multiplicity and diversity of views enables opportunities for learning to predict view-dependent surface properties, such as material reflectance [4, 26], and for learning to ...

## Source Evidence Cues

- **p. 6 / 4.3. Surface Normal Estimation - extractive body cue:** The model is a fully convolutional neural network consisting of an encoder, which shares the same architecture as VGG-16 from the beginning till the first ...
- **p. 8 / 4.5. Semantic Voxel Labeling - extractive body cue:** We use 20 object class labels, and a network following the architecture of ScanNet [7], and training with 52,355 subvolume samples (418,840 augmented samples).
- **p. 7 / 4.3. Surface Normal Estimation - extractive body cue:** We train models by first pretraining on synthetic data and then finetuning on each dataset; i.e., NYUv2 and Matterport3D, respectively.
- **p. 7 / 4.3. Surface Normal Estimation - extractive body cue:** We use Matterport3D data as a large-scale real dataset with high-quality surface normal maps for pretraining, and train the model with a variety of training ...
- **p. 5 / 4.1. Keypoint Matching - extractive body cue:** With the recent success of neural networks, several works have begun to explore the use of deep learning techniques for training state-of-the-art keypoint descriptors that ...
- **p. 6 / 4.3. Surface Normal Estimation - extractive body cue:** For our study, we use the model proposed in Zhang et al.
- **p. 8 / 4.4. Region-Type Classification - extractive body cue:** We then train a convolutional neural network (ResNet-50 [18]) to classify each input image to predict the region type.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | The model is a fully convolutional neural network consisting of an encoder, which shares the same architecture as VGG-16 from the beginning ... | p. 6 (4.3. Surface Normal Estimation), p. 8 (4.5. Semantic Voxel Labeling) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | We use 20 object class labels, and a network following the architecture of ScanNet [7], and training with 52,355 subvolume samples (418,840 ... | p. 8 (4.5. Semantic Voxel Labeling), p. 7 (4.3. Surface Normal Estimation) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | We train models by first pretraining on synthetic data and then finetuning on each dataset; i.e., NYUv2 and Matterport3D, respectively. | p. 7 (4.3. Surface Normal Estimation), p. 7 (4.3. Surface Normal Estimation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.3. Properties of the Dataset - extractive body cue:** Although we do not have ground-truth camera poses for the dataset and so cannot measure errors objectively, we subjectively estimate that the average registration error ...
- **p. 5 / 4.1. Keypoint Matching - extractive body cue:** To supervise the triplet model, we train with an L2 hinge embedding loss.
- **p. 6 / 4.2. View Overlap Prediction - extractive body cue:** Similar to keypoint matching, we train this model in a triplet Siamese fashion, using the distance ratio loss from [19].
- **p. 6 / 4.2. View Overlap Prediction - extractive body cue:** From the comparison we can clearly see the performance improvement from training data with Matterport3D and from adding the extra overlap regression loss.
- **p. 1 / 1. Introduction - extractive body cue:** Although there has been impressive research progress on this topic, a significant limitation is the availability suitable RGB-D datasets from which models can be trained.
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 3 (3.3. Properties of the Dataset), p. 5 (4.1. Keypoint Matching), p. 6 (4.2. View Overlap Prediction), p. 6 (4.2. View Overlap Prediction), p. 7 (4.3. Surface Normal Estimation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | More, specifically, train, convolutional, neural, network, ResNet-50, input, image, patch, dimensional, descriptor, Most, RGB-D | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | More, specifically, train, convolutional, neural, network, ResNet-50, input, image, patch | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | introduce, Matterport3D, large-scale, RGB-D, dataset, containing, panoramic, views, images, building-scale | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | Although, have, ground-truth, camera, poses, dataset, cannot, measure, errors, objectively | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 4.1. Keypoint Matching - extractive body cue:** More specifically, we train a convolutional neural network (ResNet-50 [18]) to map an input image patch to a 512 dimensional descriptor.
- **p. 4 / 3.3. Properties of the Dataset - extractive body cue:** Most RGB-D image datasets have been captured mostly with hand-held video cameras and thus suffer from motion blur and other artifacts typical of real-time scanning; ...
- **p. 5 / 4.1. Keypoint Matching - extractive body cue:** Similar to state of the art by [19], we train the ConvNet in a triplet Siamese fashion, where each training example contains two matching image ...
- **p. 8 / 4.4. Region-Type Classification - extractive body cue:** We then train a convolutional neural network (ResNet-50 [18]) to classify each input image to predict the region type.
- **p. 6 / 4.2. View Overlap Prediction - extractive body cue:** Given a query image, the goal is to find other images with "as much overlap in surface visibility as possible." We quantify that notion as ...
- **p. 2 / 1. Introduction - extractive body cue:** The precise global alignment over building scale allows training for state-of-the-art keypoint descriptors that can robustly match keypoints from drastically varying camera views.
- **p. 2 / 1. Introduction - extractive body cue:** For each of these tasks, we provide baseline results using variants of existing state-of-the-art algorithms demonstrating the benefits of the Matterport3D data; we hope that ...
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | The Matterport data acquisition process uses a tripodmounted camera rig with three color and three depth cameras pointing slightly up, horizontal, and ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | The second step is to label 3D surfaces on objects in each region. | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / 4.5. Semantic Voxel Labeling - extractive body cue:** We use 20 object class labels, and a network following the architecture of ScanNet [7], and training with 52,355 subvolume samples (418,840 augmented samples).
- **p. 7 / 4.3. Surface Normal Estimation - extractive body cue:** We train models by first pretraining on synthetic data and then finetuning on each dataset; i.e., NYUv2 and Matterport3D, respectively.
- **p. 7 / 4.3. Surface Normal Estimation - extractive body cue:** We use Matterport3D data as a large-scale real dataset with high-quality surface normal maps for pretraining, and train the model with a variety of training ...
- **p. 5 / 4.1. Keypoint Matching - extractive body cue:** With the recent success of neural networks, several works have begun to explore the use of deep learning techniques for training state-of-the-art keypoint descriptors that ...
- **p. 8 / 4.4. Region-Type Classification - extractive body cue:** We then train a convolutional neural network (ResNet-50 [18]) to classify each input image to predict the region type.
- **p. 1 / 1. Introduction - extractive body cue:** As with other computer vision tasks, the performance of data-driven models exceeds that of hand-tuned models and depends directly on the quantity and quality of ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** model, fully, convolutional, neural, network, consisting, encoder, shares, same, architecture, VGG-16, beginning, till, first, connected, layer, purely, symmetric, decoder, object.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | This paper introduces a new RGB-D dataset of buildingscale scenes, and describes a set of scene understanding tasks that can be trained ... | p. 2 (3. The Matterport3D Dataset), p. 4 (3.3. Properties of the Dataset) |
| Baseline harness | Figure 9: Example training correspondences (left) and im- age patches (right) extracted from Matterport3D. Triplets of matching patches (first and second columns) ... | p. 5 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Metric / failure reporting | Table 5: Region-type classification results. Each entry lists the prediction accuracy (percentage correct). By comparing the accuracy between [single] and [pano] we ... | p. 9 (Figure/Table caption), p. 6 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 4 / 3.3. Properties of the Dataset - extractive body cue:** Please note the accuracy of the global alignment (no ghosting) and the relatively low noise in surface normals, even without advanced depth-fusion techniques.
- **p. 3 / 3.2. Semantic Annotation - extractive body cue:** The first step of our semantic annotation process is to break down each building into region components by specifying the 3D spatial extent and semantic ...
- **p. 4 / 3.3. Properties of the Dataset - extractive body cue:** Category wall objects door chair window ceiling picture floor misc lighting cushion table cabinet curtain plant shelving sink mirror chest towel stairs railing column counter ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 9: Example training correspondences (left) and im- age patches (right) extracted from Matterport3D. Triplets of matching patches (first and second columns) and non- matching ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Keypoint matching results. Error (%) at 95% re- call on ground truth correspondences from the SUN3D test- ing scenes. We see an improvement ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 11: Examples of surface normal estimation. We show results of images from NYUv2 testing set. The results from the model fine-tuned on Matterport3D (SUNCG-MP) ...
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 21: Surface Normal Estimation: Comparison of multiple training schema. We compare the model pretrained with different datasets on the NYUv2 testing set. The 1st ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (4.3. Surface Normal Estimation), p. 8 (4.5. Semantic Voxel Labeling), p. 7 (4.3. Surface Normal Estimation), p. 7 (4.3. Surface Normal Estimation), p. 5 (4.1. Keypoint Matching), p. 6 (4.3. Surface Normal Estimation), objective p. 3 (3.3. Properties of the Dataset), p. 5 (4.1. Keypoint Matching), p. 6 (4.2. View Overlap Prediction), p. 6 (4.2. View Overlap Prediction), p. 1 (1. Introduction), temporal p. 2 (3.1. Data Acquisition Process), p. 3 (3.2. Semantic Annotation), p. 3 (3.3. Properties of the Dataset), p. 4 (3.3. Properties of the Dataset), p. 5 (4.2. View Overlap Prediction), p. 5 (4.2. View Overlap Prediction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
