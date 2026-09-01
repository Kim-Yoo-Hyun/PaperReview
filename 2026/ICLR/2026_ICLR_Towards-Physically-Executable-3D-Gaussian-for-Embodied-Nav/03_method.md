# Method - Towards Physically Executable 3D Gaussian for Embodied Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=HB6KvsqcAn; PDF retrieval source: https://openreview.net/pdf/5cdfb5b83429401e057b422d807ffd76daa429d7.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 15 (A IMPLEMENTATION DETAILS), p. 15 (A IMPLEMENTATION DETAILS)): The training data did not include any VLN-CE R2R or RxR samples.

## Method Body Digest

- **p. 15 / A IMPLEMENTATION DETAILS - extractive PDF cue:** The training data did not include any VLN-CE R2R or RxR samples.
- **p. 15 / A IMPLEMENTATION DETAILS - extractive PDF cue:** We selected 500k "trajectory-instruction" pairs from SAGE-Bench, with no overlap with the test set.
- **p. 15 / A IMPLEMENTATION DETAILS - extractive PDF cue:** We run A*-based shortest-path search to generate trajectories with a cost function that integrates free-space distance, narrow-passage penalties, and area preferences to ensure both obstacle ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Vision-and-Language Navigation (VLN) is a core capability for Vision-Language Action (VLA) models, enabling them to follow natural language instructions and navigate complex indoor spaces (Wei ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** For data, we provide a hierarchical instruction scheme that combines high-level semantic goals (especially task-causal ones like "I'm thirsty, get water from the table") with ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Additionally, we design a 2D semantic top-down map derived from 3DGS to support instruction generation and path planning.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** Published as a conference paper at ICLR 2026 Object-Level Semantic Grounding 1 Semantically and Physically Aligned Gaussian Environments for 3D Nav Physics-Aware Execution Jointing 2 ...
- **p. 15 / A IMPLEMENTATION DETAILS - extractive PDF cue:** To diversify the dataset, start-end pairs are sampled across different rooms, functional areas, and object instances, and a minimum safety distance is enforced to avoid ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** We introduce a 3DGS-Mesh Hybrid Representation: starting from our mesh scene data, we extract collision bodies for each object as the physics layer, while using ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** In this work, we present SAGE-3D (Semantically and Physically Aligned Gaussian Environments for 3D Navigation), a paradigm that upgrades 3DGS from a purely perceptual scene ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** Published as a conference paper at ICLR 2026 Object-Level Semantic Grounding 1 Semantically and Physically Aligned Gaussian Environments for 3D Nav Physics-Aware Execution Jointing 2 ...

## Source Evidence Cues

- **p. 15 / A IMPLEMENTATION DETAILS - extractive PDF cue:** The training data did not include any VLN-CE R2R or RxR samples.
- **p. 15 / A IMPLEMENTATION DETAILS - extractive PDF cue:** We selected 500k "trajectory-instruction" pairs from SAGE-Bench, with no overlap with the test set.
- **Detected method headings:** B DETAILED SAMPLING METHOD OF INTERIORGS (p. 15)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | The training data did not include any VLN-CE R2R or RxR samples. | p. 15 (A IMPLEMENTATION DETAILS), p. 15 (A IMPLEMENTATION DETAILS) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | We selected 500k "trajectory-instruction" pairs from SAGE-Bench, with no overlap with the test set. | p. 15 (A IMPLEMENTATION DETAILS) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | The training data did not include any VLN-CE R2R or RxR samples. | p. 15 (A IMPLEMENTATION DETAILS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 15 / A IMPLEMENTATION DETAILS - extractive PDF cue:** We run A*-based shortest-path search to generate trajectories with a cost function that integrates free-space distance, narrow-passage penalties, and area preferences to ensure both obstacle ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Vision-and-Language, Navigation, VLN, core, capability, Vision-Language, Action, VLA, models, enabling, them, follow, natural, language | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Vision-and-Language, Navigation, VLN, core, capability, Vision-Language, Action, VLA, models, enabling | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | introduce, DGS-Mesh, Hybrid, Representation, starting, mesh, scene, data, extract, collision | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | shortest-path, search, generate, trajectories, cost, function, integrates, free-space, distance, narrow-passage | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Vision-and-Language Navigation (VLN) is a core capability for Vision-Language Action (VLA) models, enabling them to follow natural language instructions and navigate complex indoor spaces (Wei ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** For data, we provide a hierarchical instruction scheme that combines high-level semantic goals (especially task-causal ones like "I'm thirsty, get water from the table") with ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Additionally, we design a 2D semantic top-down map derived from 3DGS to support instruction generation and path planning.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** Published as a conference paper at ICLR 2026 Object-Level Semantic Grounding 1 Semantically and Physically Aligned Gaussian Environments for 3D Nav Physics-Aware Execution Jointing 2 ...
- **p. 15 / A IMPLEMENTATION DETAILS - extractive PDF cue:** We selected 500k "trajectory-instruction" pairs from SAGE-Bench, with no overlap with the test set.
- **p. 15 / A IMPLEMENTATION DETAILS - extractive PDF cue:** To diversify the dataset, start-end pairs are sampled across different rooms, functional areas, and object instances, and a minimum safety distance is enforced to avoid ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | The results show that 3DGS scene data achieves a perframe rendering time of 6.2 ms and an average memory usage of 220 ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | PS is computed from the variance of consecutive heading changes: PS = 1 - 1 T -1 T X t=2 min /∆θt/ ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | The results show that 3DGS scene data achieves a perframe rendering time of 6.2 ms and an average memory usage of 220 ... | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | The results show that 3DGS scene data achieves a perframe rendering time of 6.2 ms and an average memory usage of 220 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 15 / A IMPLEMENTATION DETAILS - extractive PDF cue:** The training data did not include any VLN-CE R2R or RxR samples.
- **p. 15 / A IMPLEMENTATION DETAILS - extractive PDF cue:** Training was carried out on 8 NVIDIA Tesla H20 GPUs with a batch size of 256 and a learning rate of 2 × 10-5.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** We randomly selected 10k training samples and 1k validation samples from both traditional scanned mesh data and our 3DGS data, and conducted experiments with the ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** training, data, include, VLN-CE, R2R, RxR, samples, selected, trajectory-instruction, pairs, SAGE-Bench, overlap, test, shortest-path, search, generate, trajectories, cost, function, integrates.
- **Relevant PDF headings:** B DETAILED SAMPLING METHOD OF INTERIORGS (p. 15).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Data in # Train SAGE-Bench VLN #Scenes #Samples SR ↑ OSR ↑ SPL ↑ CSR ↑ ICP ↓ PS ↑ 800 240k ... | p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |
| Global / local decision | 4, models trained entirely on SAGE-Bench data (without any VLN-CE data) achieved clear performance improvements over their respective baselines. | p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Motion execution / recovery | Even the recent SOTA model NaVILA achieves only a 0.39 success rate on high-level instructions, significantly lower than its 0.56 success rate ... | p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** 4, models trained entirely on SAGE-Bench data (without any VLN-CE data) achieved clear performance improvements over their respective baselines.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** We trained two models on this subset: one based on NaVILA's pre-trained model navila-siglip-llama3-8b-v1.5-pretrain (denoted as NaVILA-base), producing NaVILA-SAGE; and the other based on Navid's ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of SAGE-3D, which consists of two key components: (1) Object-Level Semantic Grounding, 3DGS data is annotated by expect at the object level, ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Overview of SAGE-Bench. SAGE-Bench includes a hierarchical instruction generation scheme, two major task types, two episode complexity categories, and three newly designed natural ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** 4 corroborate this finding: the NaVILA model (blue trajectory) exhibits unsmooth movement and persistent collisions that conventional metrics fail to reveal.
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Traditional 3DGS vs. Our work. Compared with traditional 3DGS, our InteriorGS pro- vides object-level 3DGS annotations across diverse indoor and outdoor scenes, including ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of SAGE-3D, which consists of two key components: (1) Object-Level Semantic Grounding, 3DGS data is annotated by expect at the object level, ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 15 (A IMPLEMENTATION DETAILS), p. 15 (A IMPLEMENTATION DETAILS), objective p. 15 (A IMPLEMENTATION DETAILS), temporal p. 8 (4 EXPERIMENTS), p. 7 (3) Path Smoothness), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
