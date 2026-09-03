# Method - ScanNet: Richly-annotated 3D Reconstructions of Indoor Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1702.04405; PDF retrieval source: https://arxiv.org/pdf/1702.04405. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. Surface Reconstruction), p. 4 (3.2. Surface Reconstruction)): BundleFusion produces accurate pose alignments which we then use to perform volumetric integration through VoxelHashing [62] and extract a high resolution surface mesh using the Marching Cubes algorithm on the ...

## Method Body Digest

- **p. 4 / 3.2. Surface Reconstruction - extractive body cue:** BundleFusion produces accurate pose alignments which we then use to perform volumetric integration through VoxelHashing [62] and extract a high resolution surface mesh using the ...
- **p. 4 / 3.2. Surface Reconstruction - extractive body cue:** There is a large variety of algorithms targeting this scenario [59, 88, 7, 62, 37, 89, 42, 9, 90, 38, 12].
- **p. 4 / 3.2. Surface Reconstruction - extractive body cue:** This annotation is in progress at ≈35%, with gray regions indicating unannotated surfaces.
- **p. 4 / 3.2. Surface Reconstruction - extractive body cue:** For each input scan, we first run BundleFusion [12] at a voxel resolution of 1 cm3.
- **p. 4 / 3.2. Surface Reconstruction - extractive body cue:** We chose the BundleFusion system [12] as it was designed and evaluated for similar sensor setups as ours, and provides real-time speed while being reasonably ...
- **p. 1 / 1. Introduction - extractive body cue:** Thus, existing work on 3D datasets often fall back to polygon or bounding box annotations on 2.5D RGB-D images [74, 92, 77], rather than directly ...
- **p. 1 / 1. Introduction - extractive body cue:** While much effort has been made on 2D datasets [17, 44, 47], where images can be downloaded from the web and directly annotated, the situation ...

## Design Rationale

- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we introduce ScanNet, a dataset of richlyannotated RGB-D scans of real-world environments containing 2.5M RGB-D images in 1513 scans acquired in 707 ...
- **p. 1 / 1. Introduction - extractive body cue:** In the collection of this dataset, we have considered two main research questions: 1) how can we design a framework that allows many people to ...
- **p. 4 / 3.2. Surface Reconstruction - extractive body cue:** This allows us to select the floor plane based on the scan bounding box and the normal most similar to the IMU up vector direction.

## Source Evidence Cues

- **p. 4 / 3.2. Surface Reconstruction - extractive body cue:** BundleFusion produces accurate pose alignments which we then use to perform volumetric integration through VoxelHashing [62] and extract a high resolution surface mesh using the ...
- **p. 4 / 3.2. Surface Reconstruction - extractive body cue:** There is a large variety of algorithms targeting this scenario [59, 88, 7, 62, 37, 89, 42, 9, 90, 38, 12].
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | BundleFusion produces accurate pose alignments which we then use to perform volumetric integration through VoxelHashing [62] and extract a high resolution surface ... | p. 4 (3.2. Surface Reconstruction), p. 4 (3.2. Surface Reconstruction) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | There is a large variety of algorithms targeting this scenario [59, 88, 7, 62, 37, 89, 42, 9, 90, 38, 12]. | p. 4 (3.2. Surface Reconstruction) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | BundleFusion produces accurate pose alignments which we then use to perform volumetric integration through VoxelHashing [62] and extract a high resolution surface ... | p. 4 (3.2. Surface Reconstruction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.2. Surface Reconstruction - extractive body cue:** This annotation is in progress at ≈35%, with gray regions indicating unannotated surfaces.
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | input, scan, first, BundleFusion, voxel, resolution, chose, system, designed, evaluated, similar, sensor, setups, ours | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | input, scan, first, BundleFusion, voxel, resolution, chose, system, designed, evaluated | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | introduce, ScanNet, dataset, richlyannotated, RGB-D, scans, real-world, environments, containing, images | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | annotation, progress, gray, regions, indicating, unannotated, surfaces | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. Surface Reconstruction - extractive body cue:** For each input scan, we first run BundleFusion [12] at a voxel resolution of 1 cm3.
- **p. 4 / 3.2. Surface Reconstruction - extractive body cue:** We chose the BundleFusion system [12] as it was designed and evaluated for similar sensor setups as ours, and provides real-time speed while being reasonably ...
- **p. 1 / 1. Introduction - extractive body cue:** Thus, existing work on 3D datasets often fall back to polygon or bounding box annotations on 2.5D RGB-D images [74, 92, 77], rather than directly ...
- **p. 1 / 1. Introduction - extractive body cue:** While much effort has been made on 2D datasets [17, 44, 47], where images can be downloaded from the web and directly annotated, the situation ...
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | It is composed of 464 short RGB-D sequences, from which 1449 frames have been annotated with 2D polygons denoting semantic segmentations, as ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | The iPad RGB camera data is temporally synchronized with the depth sensor via hardware, providing synchronized depth and color capture at 30 ... | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | It is composed of 464 short RGB-D sequences, from which 1449 frames have been annotated with 2D polygons denoting semantic segmentations, as ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 5.1. 3D Object Classification - extractive body cue:** [66], we use an SGD solver with learning rate 0.01 and momentum 0.9, decaying the learning rate by half every 20 epochs, and training the ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** BundleFusion, produces, accurate, pose, alignments, then, perform, volumetric, integration, through, VoxelHashing, extract, high, resolution, surface, mesh, Marching, Cubes, algorithm, implicit.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | Our main goal driving the design of our framework was to allow untrained users to capture semantically labeled surfaces of indoor scenes ... | p. 3 (3. Dataset Acquisition Framework), p. 5 (4. ScanNet Dataset) |
| Baseline harness | Summary statistics for ScanNet compared to the most similar existing dataset (SceneNN [32]). | p. 5 (3.3. Semantic Annotation), p. 6 (5.1. 3D Object Classification) |
| Metric / failure reporting | On the other hand, training on ScanNet translates well to testing on SceneNN; as a result, the test results on SceneNN are ... | p. 7 (5.1. 3D Object Classification), p. 20 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 5 / 3.3. Semantic Annotation - extractive body cue:** Without the turntable rotation animation, many workers only annotated from the initial view and never used camera controls despite the provided instructions.
- **p. 5 / 3.3. Semantic Annotation - extractive body cue:** Earlier experiments without this constraint resulted in two undesirable behaviors: cheating by painting many surfaces with a few labels, and labeling of multiple object instances ...
- **p. 6 / 5.1. 3D Object Classification - extractive body cue:** For object classification, we follow the network architecture of the 3D Network-in-Network of [66], without the multi-orientation pooling step.
- **p. 12 / Figure/Table caption - extractive body cue:** Table 8. Total counts of annotated object instances of the 50 largest categories in ScanNet (left), and in SceneNN [32] (right), the most similar annotated ...
- **p. 8 / 5.2. Semantic Voxel Labeling - extractive body cue:** SceneNet trains on a large synthetic dataset and fine-tunes on NYU2.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Example reconstructed spaces in ScanNet annotated with instance-level object category labels through our crowdsourced annotation framework. ciently providing (dense) annotations in 3D is ...
- **p. 8 / 6. Conclusion - extractive body cue:** We demonstrated that the richlyannotated scan data collected so far in ScanNet is useful in achieving state-of-the-art performance on several 3D scene understanding tasks; we ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.2. Surface Reconstruction), p. 4 (3.2. Surface Reconstruction), objective p. 4 (3.2. Surface Reconstruction), temporal p. 2 (2. Previous Work), p. 3 (3.1. RGB-D Scanning), p. 3 (3.1. RGB-D Scanning), p. 4 (3.2. Surface Reconstruction), p. 4 (3.2. Surface Reconstruction), p. 6 (4. ScanNet Dataset).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
