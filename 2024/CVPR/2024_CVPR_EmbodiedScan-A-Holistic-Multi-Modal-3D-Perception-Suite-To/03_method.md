# Method - EmbodiedScan: A Holistic Multi-Modal 3D Perception Suite Towards Embodied AI

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Wang_EmbodiedScan_A_Holistic_Multi-Modal_3D_Perception_Suite_Towards_Embodied_AI_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Wang_EmbodiedScan_A_Holistic_Multi-Modal_3D_Perception_Suite_Towards_Embodied_AI_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (4.1. Multi-Modal 3D Encoder), p. 5 (4.1. Multi-Modal 3D Encoder), p. 6 (4.2. Sparse & Dense Decoder), p. 1 (Abstract), p. 4 (3.2. Annotation), p. 5 (4.1. Multi-Modal 3D Encoder)): Given the multi-level sparse visual features F S k and text features from the text encoder, we use a multi-modal fusion transformer model [20, 61] for vision-language information interactions.

## Method Body Digest

- **p. 6 / 4.1. Multi-Modal 3D Encoder - extractive body cue:** Given the multi-level sparse visual features F S k and text features from the text encoder, we use a multi-modal fusion transformer model [20, 61] ...
- **p. 5 / 4.1. Multi-Modal 3D Encoder - extractive body cue:** Next, we first present how we aggregate multi-view inputs and then introduce different fusion approaches for dense and sparse feature extraction.
- **p. 6 / 4.2. Sparse & Dense Decoder - extractive body cue:** We use cross-entropy loss and sceneclass affinity loss [55] for training.
- **p. 1 / Abstract - extractive body cue:** This necessitates the ability to fully understand 3D scenes given their first-person observations and contextualize them into language for interaction.
- **p. 4 / 3.2. Annotation - extractive body cue:** We used the Segment Anything Model (SAM) [22] and a customized annotation tool based on [24] (Fig.
- **p. 5 / 4.1. Multi-Modal 3D Encoder - extractive body cue:** For the sparse case, we use multi-level features as seeds instead of a single dense feature map to predict 3D objects.
- **p. 3 / 3.1. Data Collection & Processing - extractive body cue:** We first unified the format into a general multi-view case to fit Matterport3D by adding randomness when loading images but maintaining sequential continuity for ScanNet ...
- **p. 6 / 4.2. Sparse & Dense Decoder - extractive body cue:** Training objectives include the original classification loss, centerness loss, and a disentangled Chamfer Distance (CD) loss for eight corners [3, 44].

## Design Rationale

- **p. 1 / Abstract - extractive body cue:** Building upon this database, we introduce a baseline framework named Embodied Perceptron.
- **p. 1 / Abstract - extractive body cue:** To address the gap, we introduce EmbodiedScan, a multi-modal, ego-centric 3D perception dataset and benchmark for holistic 3D scene understanding.

## Source Evidence Cues

- **p. 6 / 4.1. Multi-Modal 3D Encoder - extractive body cue:** Given the multi-level sparse visual features F S k and text features from the text encoder, we use a multi-modal fusion transformer model [20, 61] ...
- **p. 5 / 4.1. Multi-Modal 3D Encoder - extractive body cue:** Next, we first present how we aggregate multi-view inputs and then introduce different fusion approaches for dense and sparse feature extraction.
- **p. 6 / 4.2. Sparse & Dense Decoder - extractive body cue:** We use cross-entropy loss and sceneclass affinity loss [55] for training.
- **p. 1 / Abstract - extractive body cue:** This necessitates the ability to fully understand 3D scenes given their first-person observations and contextualize them into language for interaction.
- **p. 4 / 3.2. Annotation - extractive body cue:** We used the Segment Anything Model (SAM) [22] and a customized annotation tool based on [24] (Fig.
- **p. 5 / 4.1. Multi-Modal 3D Encoder - extractive body cue:** For the sparse case, we use multi-level features as seeds instead of a single dense feature map to predict 3D objects.
- **p. 3 / 3.1. Data Collection & Processing - extractive body cue:** We first unified the format into a general multi-view case to fit Matterport3D by adding randomness when loading images but maintaining sequential continuity for ScanNet ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | Given the multi-level sparse visual features F S k and text features from the text encoder, we use a multi-modal fusion transformer ... | p. 6 (4.1. Multi-Modal 3D Encoder), p. 5 (4.1. Multi-Modal 3D Encoder) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | Next, we first present how we aggregate multi-view inputs and then introduce different fusion approaches for dense and sparse feature extraction. | p. 5 (4.1. Multi-Modal 3D Encoder), p. 6 (4.2. Sparse & Dense Decoder) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | We use cross-entropy loss and sceneclass affinity loss [55] for training. | p. 6 (4.2. Sparse & Dense Decoder), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 4.2. Sparse & Dense Decoder - extractive body cue:** Training objectives include the original classification loss, centerness loss, and a disentangled Chamfer Distance (CD) loss for eight corners [3, 44].
- **p. 6 / 4.2. Sparse & Dense Decoder - extractive body cue:** We use cross-entropy loss and sceneclass affinity loss [55] for training.
- **p. 5 / 4. Embodied Perceptron - extractive body cue:** In addition, we customize the output's parameterization and training objectives to fit the formulation of oriented 3D bounding boxes in the sparse decoder.
- **p. 5 / 4.1. Multi-Modal 3D Encoder - extractive body cue:** The initial attempt of still query features from Fup or raw images I for these seeds is unstable due to inconsistent features for fusion and ...
- **p. 4 / 3.2. Annotation - extractive body cue:** Given updated 3D bounding boxes annotated with orientations, we derive the language prompts that describe the spatial relationships among objects following SR3D [1].
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 6 (4.2. Sparse & Dense Decoder), p. 5 (4. Embodied Perceptron), p. 5 (4.1. Multi-Modal 3D Encoder), p. 6 (4.2. Sparse & Dense Decoder), p. 4 (3.2. Annotation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, dataset, take, multi-modality, input, including, RGB, images, point, clouds, derived, depth, maps, well | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | Given, dataset, take, multi-modality, input, including, RGB, images, point, clouds | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | Building, upon, database, introduce, baseline, framework, named, Embodied, Perceptron, address | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | Training, objectives, include, original, classification, loss, centerness, disentangled, Chamfer, Distance | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 4. Embodied Perceptron - extractive body cue:** Given this dataset, we can take multi-modality input, including RGB images, point clouds derived from depth maps as well as language prompts, to extract multi-modal ...
- **p. 1 / 1. Introduction - extractive body cue:** Most previous studies have primarily revolved around scene-level input and output problems from a global view [13, 34, 40], i.e., taking reconstructed 3D point clouds ...
- **p. 1 / Abstract - extractive body cue:** This necessitates the ability to fully understand 3D scenes given their first-person observations and contextualize them into language for interaction.
- **p. 4 / 3.1. Data Collection & Processing - extractive body cue:** A global coordinate system is necessary to aggregate multi-view observations and serve as a reference for outputs.
- **p. 5 / 4.1. Multi-Modal 3D Encoder - extractive body cue:** Next, we first present how we aggregate multi-view inputs and then introduce different fusion approaches for dense and sparse feature extraction.
- **p. 2 / Dataset - extractive body cue:** We establish two series of benchmarks on EmbodiedScan: 1) fundamental 3D perception benchmarks focusing on traditional tasks, including 3D detection and semantic occupancy prediction under ...
- **p. 5 / 4.1. Multi-Modal 3D Encoder - extractive body cue:** Formally, the input aggregated points P ∈RNp×3 (first voxelized) and Ni images as I ∈RNi×H×W are processed via a Minkowski ResNet and a shared 2D ...
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | Building upon this database, we introduce a baseline framework named Embodied Perceptron. | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | Built upon this dataset, we devise a baseline framework for ego-centric 3D perception, Embodied Perceptron. | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | As for different sampling rates of images in ScanNet and 3RScan videos, we sample one keyframe per 10 frames for ScanNet and ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 4.2. Sparse & Dense Decoder - extractive body cue:** We use cross-entropy loss and sceneclass affinity loss [55] for training.
- **p. 3 / 3.1. Data Collection & Processing - extractive body cue:** We first unified the format into a general multi-view case to fit Matterport3D by adding randomness when loading images but maintaining sequential continuity for ScanNet ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Given, multi-level, sparse, visual, features, text, encoder, multi-modal, fusion, transformer, model, vision-language, information, interactions, Next, first, present, aggregate, multi-view, inputs.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | To bridge this divide, we introduce a multi-modal, egocentric 3D perception dataset and benchmark for holistic 3D scene understanding, termed EmbodiedScan, aimed ... | p. 2 (Dataset), p. 2 (Dataset) |
| Baseline harness | Our baseline outperforms all due to the strong multi-modal encoder. | p. 8 (5.2. Language-Grounded Benchmark), p. 8 (5.1. Fundamental 3D Perception Benchmarks) |
| Metric / failure reporting | Substituting this with our decoder design markedly improves performance. | p. 7 (5.1. Fundamental 3D Perception Benchmarks), p. 3 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 4 / 3.3. Statistics - extractive body cue:** We remove four categories, {wall, ceiling, floor, object} in our 3D detection benchmark and divide the remaining 284 categories into three splits, {head, common, tail} ...
- **p. 4 / 3.2. Annotation - extractive body cue:** Semantic occupancy necessitates accurate boundaries across semantic regions without considering object pose or recalling all the objects, so the original point cloud segmentation annotations were ...
- **p. 7 / 5.1. Fundamental 3D Perception Benchmarks - extractive body cue:** If a category lacks instances, it is removed when calculating mAP and mIoU.
- **p. 7 / 5.1. Fundamental 3D Perception Benchmarks - extractive body cue:** Variants of our baselines exhibit a performance trend akin to embodied benchmarks.
- **p. 8 / 5.1. Fundamental 3D Perception Benchmarks - extractive body cue:** Ablation with conventional settings.
- **p. 8 / 5.2. Language-Grounded Benchmark - extractive body cue:** As an initial step, this setup takes multi-view RGB-D images as input without considering differing prompt timestamps.
- **p. 2 / Dataset - extractive body cue:** On the other hand, since we cannot trivially obtain the reconstruction of a new environment, models trained with scene-level input are not directly applicable in ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (4.1. Multi-Modal 3D Encoder), p. 5 (4.1. Multi-Modal 3D Encoder), p. 6 (4.2. Sparse & Dense Decoder), p. 1 (Abstract), p. 4 (3.2. Annotation), p. 5 (4.1. Multi-Modal 3D Encoder), objective p. 6 (4.2. Sparse & Dense Decoder), p. 6 (4.2. Sparse & Dense Decoder), p. 5 (4. Embodied Perceptron), p. 5 (4.1. Multi-Modal 3D Encoder), p. 4 (3.2. Annotation), temporal p. 1 (Abstract), p. 2 (Dataset), p. 2 (Dataset), p. 3 (3.1. Data Collection & Processing), p. 3 (2. Related Work), p. 4 (3.1. Data Collection & Processing).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
