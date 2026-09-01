# Method - OpenGS-Fusion: Open-Vocabulary Dense Mapping with Hybrid 3D Gaussian Splatting for Refined Object-Level Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2508.01150; PDF retrieval source: https://arxiv.org/pdf/2508.01150. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (2) Limited 3D Object-Level Understanding. Most exist), p. 4 (III. OPENGS-FUSION), p. 1 (1) Rigid Offline Pipeline. These methods rely on essen), p. 1 (1) Rigid Offline Pipeline. These methods rely on essen), p. 4 (III. OPENGS-FUSION), p. 3 (III. OPENGS-FUSION)): In summary, our contributions are as follows. • We introduce OpenGS-Fusion, an innovative openvocabulary dense mapping framework that leverages a hybrid scene representation to concurrently construct the appearance, geometry, and ...

## Method Body Digest

- **p. 2 / 2) Limited 3D Object-Level Understanding. Most exist - extractive PDF cue:** In summary, our contributions are as follows. • We introduce OpenGS-Fusion, an innovative openvocabulary dense mapping framework that leverages a hybrid scene representation to concurrently ...
- **p. 4 / III. OPENGS-FUSION - extractive PDF cue:** We first input Q into the CLIP model to extract text features, which are then compared with semantic features F of all global voxels V ...
- **p. 1 / 1) Rigid Offline Pipeline. These methods rely on essen - extractive PDF cue:** tial preprocessing steps, such as pretraining 3D Gaussian representation or offline compression of high-dimensional semantic features.
- **p. 1 / 1) Rigid Offline Pipeline. These methods rely on essen - extractive PDF cue:** However, in real-world applications, for example, robotic exploration and embodied interaction, models must support online perception.
- **p. 4 / III. OPENGS-FUSION - extractive PDF cue:** Therefore, we propose an adaptive threshold adjustment strategy assisted by MLLM, where MLLM refers to large vision language models that support both image and text ...
- **p. 3 / III. OPENGS-FUSION - extractive PDF cue:** Receiving RGB-D input with 2D language embeddings extracted from 2D foundation models, we simultaneously update the appearance, geometry and semantic features of our hybrid 3D ...
- **p. 2 / III. OPENGS-FUSION - extractive PDF cue:** We first extract 2D semantic features St following the methodology described in Sec.III-A.
- **p. 4 / III. OPENGS-FUSION - extractive PDF cue:** 3) Scene Optimization Strategy: To supervise the learning of our Gaussian representation, we apply the same loss function as described in [24].

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Our method enables versatile task-oriented interactions, such as 3D object extraction and editing in an interactive manner.
- **p. 2 / 2) Limited 3D Object-Level Understanding. Most exist - extractive PDF cue:** In summary, our contributions are as follows. • We introduce OpenGS-Fusion, an innovative openvocabulary dense mapping framework that leverages a hybrid scene representation to concurrently ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Compared to 3DGS-featurefield-based methods [12]-[15], our approach enables online modeling of scene appearance, geometry, and semantics while supporting 3D objectlevel queries.

## Source Evidence Cues

- **p. 2 / 2) Limited 3D Object-Level Understanding. Most exist - extractive PDF cue:** In summary, our contributions are as follows. • We introduce OpenGS-Fusion, an innovative openvocabulary dense mapping framework that leverages a hybrid scene representation to concurrently ...
- **p. 4 / III. OPENGS-FUSION - extractive PDF cue:** We first input Q into the CLIP model to extract text features, which are then compared with semantic features F of all global voxels V ...
- **p. 1 / 1) Rigid Offline Pipeline. These methods rely on essen - extractive PDF cue:** tial preprocessing steps, such as pretraining 3D Gaussian representation or offline compression of high-dimensional semantic features.
- **p. 1 / 1) Rigid Offline Pipeline. These methods rely on essen - extractive PDF cue:** However, in real-world applications, for example, robotic exploration and embodied interaction, models must support online perception.
- **p. 4 / III. OPENGS-FUSION - extractive PDF cue:** Therefore, we propose an adaptive threshold adjustment strategy assisted by MLLM, where MLLM refers to large vision language models that support both image and text ...
- **p. 3 / III. OPENGS-FUSION - extractive PDF cue:** Receiving RGB-D input with 2D language embeddings extracted from 2D foundation models, we simultaneously update the appearance, geometry and semantic features of our hybrid 3D ...
- **p. 2 / III. OPENGS-FUSION - extractive PDF cue:** We first extract 2D semantic features St following the methodology described in Sec.III-A.
- **Detected method headings:** 1) Rigid Offline Pipeline. These methods rely on essen (p. 1)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | In summary, our contributions are as follows. • We introduce OpenGS-Fusion, an innovative openvocabulary dense mapping framework that leverages a hybrid scene ... | p. 2 (2) Limited 3D Object-Level Understanding. Most exist), p. 4 (III. OPENGS-FUSION) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | We first input Q into the CLIP model to extract text features, which are then compared with semantic features F of all ... | p. 4 (III. OPENGS-FUSION), p. 1 (1) Rigid Offline Pipeline. These methods rely on essen) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | tial preprocessing steps, such as pretraining 3D Gaussian representation or offline compression of high-dimensional semantic features. | p. 1 (1) Rigid Offline Pipeline. These methods rely on essen), p. 1 (1) Rigid Offline Pipeline. These methods rely on essen) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / III. OPENGS-FUSION - extractive PDF cue:** 3) Scene Optimization Strategy: To supervise the learning of our Gaussian representation, we apply the same loss function as described in [24].
- **p. 4 / III. OPENGS-FUSION - extractive PDF cue:** This approach allows our method to obtain a relatively accurate geometric representation at the initialization stage, reducing the optimization cost.
- **p. 1 / 2) Limited 3D Object-Level Understanding. Most exist - extractive PDF cue:** The TSDF's voxel-based structure facilitates lossless fusion of semantic arXiv:2508.01150v1 [cs.CV] 2 Aug 2025
- **p. 1 / Abstract - extractive PDF cue:** OpenGSFusion combines 3D Gaussian representation with a Truncated Signed Distance Field to facilitate lossless fusion of semantic features on-the-fly.
- **p. 2 / 2) Limited 3D Object-Level Understanding. Most exist - extractive PDF cue:** features and guides 3D Gaussian initialization, ensuring full semantic preservation while significantly improving scene update efficiency.
- **p. 2 / III. OPENGS-FUSION - extractive PDF cue:** Subsequently, the tuple {Ct, Dt, St, Pt} is used to update our hybrid scene representation M (Sec.III-B), following the approach in Sec.IIIC.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 1 (2) Limited 3D Object-Level Understanding. Most exist), p. 1 (Abstract), p. 4 (III. OPENGS-FUSION), p. 4 (III. OPENGS-FUSION), p. 2 (2) Limited 3D Object-Level Understanding. Most exist), p. 2 (III. OPENGS-FUSION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Therefore, adaptive, threshold, adjustment, strategy, assisted, MLLM, where, refers, large, vision, language, models, support | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Therefore, adaptive, threshold, adjustment, strategy, assisted, MLLM, where, refers, large | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | enables, versatile, task-oriented, interactions, object, extraction, editing, interactive, manner, summary | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Scene, Optimization, Strategy, supervise, learning, Gaussian, representation, apply, same, loss | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / III. OPENGS-FUSION - extractive PDF cue:** Therefore, we propose an adaptive threshold adjustment strategy assisted by MLLM, where MLLM refers to large vision language models that support both image and text ...
- **p. 1 / 1) Rigid Offline Pipeline. These methods rely on essen - extractive PDF cue:** However, in real-world applications, for example, robotic exploration and embodied interaction, models must support online perception.
- **p. 1 / Abstract - extractive PDF cue:** Extensive experiments demonstrate that our method outperforms existing methods in 3D object understanding and scene reconstruction quality, as well as showcasing its effectiveness in language-guided ...
- **p. 2 / III. OPENGS-FUSION - extractive PDF cue:** By inputting these proposals into the CLIP model, we can extract region-level semantic features, where all pixels within region Ri share a unified language embeddings ...
- **p. 2 / 2) Limited 3D Object-Level Understanding. Most exist - extractive PDF cue:** In summary, our contributions are as follows. • We introduce OpenGS-Fusion, an innovative openvocabulary dense mapping framework that leverages a hybrid scene representation to concurrently ...
- **p. 3 / III. OPENGS-FUSION - extractive PDF cue:** Open-Vocabulary Dense Scene Mapping Given input {Ct, Dt, St, Pt}, we update the global map M in three stages.
- **p. 3 / III. OPENGS-FUSION - extractive PDF cue:** Receiving RGB-D input with 2D language embeddings extracted from 2D foundation models, we simultaneously update the appearance, geometry and semantic features of our hybrid 3D ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Replica ScanNet Methods mAcc↑ mIoU↑ FPS↑ mAcc↑ mIoU↑ FPS↑ ConceptFusion* 28.02 11.49 0.49 21.22 10.64 0.52 ConceptGraphs 38.21 18.16 - 44.28 23.94 ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | We also evaluated geometric reconstruction accuracy with depth L1 loss and system efficiency with mapping frame rate (FPS). | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | To improve efficiency, MobileSAMv2 [42] was used as the 2D segmentation model in our 2D Embedding Extractor model, enabling real-time image segmentation ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 2) Limited 3D Object-Level Understanding. Most exist - extractive PDF cue:** In summary, our contributions are as follows. • We introduce OpenGS-Fusion, an innovative openvocabulary dense mapping framework that leverages a hybrid scene representation to concurrently ...
- **p. 1 / 1) Rigid Offline Pipeline. These methods rely on essen - extractive PDF cue:** tial preprocessing steps, such as pretraining 3D Gaussian representation or offline compression of high-dimensional semantic features.
- **p. 1 / 1) Rigid Offline Pipeline. These methods rely on essen - extractive PDF cue:** However, in real-world applications, for example, robotic exploration and embodied interaction, models must support online perception.
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** Additionally, compared to our code-based approach GSICPTABLE III QUANTITATIVE TRAIN VIEW RENDERING PERFORMANCE ON REPLICA.
- **p. 1 / 1) Rigid Offline Pipeline. These methods rely on essen - extractive PDF cue:** tial preprocessing steps, such as pretraining 3D Gaussian representation or offline compression of high-dimensional semantic features.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** summary, contributions, follows, introduce, OpenGS-Fusion, innovative, openvocabulary, dense, mapping, framework, leverages, hybrid, scene, representation, concurrently, construct, appearance, geometry, semantic, features.
- **Relevant PDF headings:** 1) Rigid Offline Pipeline. These methods rely on essen (p. 1).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Replica ScanNet Methods mAcc↑ mIoU↑ FPS↑ mAcc↑ mIoU↑ FPS↑ ConceptFusion* 28.02 11.49 0.49 21.22 10.64 0.52 ConceptGraphs 38.21 18.16 - 44.28 23.94 ... | p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT) |
| Global / local decision | Specifically, our method outperforms the state-of-the-art 3DGS-based approach, OpenGaussian, with improvements of 9.5% (Replica) and 12.2% (ScanNet) in terms of mIoU performance, ... | p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT) |
| Motion execution / recovery | Specifically, our method outperforms the state-of-the-art 3DGS-based approach, OpenGaussian, with improvements of 9.5% (Replica) and 12.2% (ScanNet) in terms of mIoU performance, ... | p. 5 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT) |

## Failure and Ablation Link

- **p. 5 / IV. EXPERIMENT - extractive PDF cue:** To ensure fairness, we adhere to [4] for training LangSplat, OpenGaussian, and our method, without optimizing the positional attributes of Gaussian primitives.
- **p. 5 / IV. EXPERIMENT - extractive PDF cue:** Specifically, our method outperforms the state-of-the-art 3DGS-based approach, OpenGaussian, with improvements of 9.5% (Replica) and 12.2% (ScanNet) in terms of mIoU performance, while operating in ...
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** Ablation Experiments To further validate our method, we conducted ablation studies focusing on the core parameters of our hybrid representation, specifically the voxel size of ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2. Overview of OpenGS-Fusion. Receiving RGB-D input with 2D language embeddings extracted from 2D foundation models, we simultaneously update the appearance, geometry and semantic ...
- **p. 7 / V. CONCLUSIONS - extractive PDF cue:** However, our method currently relies on accurate pose estimation and faces limitations in query efficiency.
- **p. 7 / V. CONCLUSIONS - extractive PDF cue:** Future work will explore how to leverage hybrid scene representation for pose estimation and investigate lightweight MLLMs specifically designed for image retrieval tasks to further ...
- **p. 5 / IV. EXPERIMENT - extractive PDF cue:** OpenGaussian fails to locate both instances as they are segmented into separate entities, and the model by default only retrieves the instance that best matches ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (2) Limited 3D Object-Level Understanding. Most exist), p. 4 (III. OPENGS-FUSION), p. 1 (1) Rigid Offline Pipeline. These methods rely on essen), p. 1 (1) Rigid Offline Pipeline. These methods rely on essen), p. 4 (III. OPENGS-FUSION), p. 3 (III. OPENGS-FUSION), objective p. 4 (III. OPENGS-FUSION), p. 4 (III. OPENGS-FUSION), p. 1 (2) Limited 3D Object-Level Understanding. Most exist), p. 1 (Abstract), p. 2 (2) Limited 3D Object-Level Understanding. Most exist), p. 2 (III. OPENGS-FUSION), temporal p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 1 (1) Rigid Offline Pipeline. These methods rely on essen), p. 1 (1) Rigid Offline Pipeline. These methods rely on essen), p. 2 (II. RELATED WORKS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
