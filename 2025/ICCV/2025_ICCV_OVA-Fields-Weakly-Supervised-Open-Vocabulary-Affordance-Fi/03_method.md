# Method - OVA-Fields: Weakly Supervised Open-Vocabulary Affordance Fields for Robot Operational Part Detection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Su_OVA-Fields_Weakly_Supervised_Open-Vocabulary_Affordance_Fields_for_Robot_Operational_Part_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Su_OVA-Fields_Weakly_Supervised_Open-Vocabulary_Affordance_Fields_for_Robot_Operational_Part_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3.2. Spatial Feature Extraction and Feature Fusion), p. 4 (3.2. Spatial Feature Extraction and Feature Fusion), p. 4 (3.2. Spatial Feature Extraction and Feature Fusion), p. 3 (3.1. Multi-Modal Affordance Perception), p. 5 (3.3. Query Mapping), p. 5 (3.2. Spatial Feature Extraction and Feature Fusion)): Through a series of processing steps, the OVA-Fields then produces a high-dimensional feature representation for each coordinate point, which incorporates both rich visual information and affordance information.

## Method Body Digest

- **p. 3 / 3.2. Spatial Feature Extraction and Feature Fusion - extractive PDF cue:** Through a series of processing steps, the OVA-Fields then produces a high-dimensional feature representation for each coordinate point, which incorporates both rich visual information and ...
- **p. 4 / 3.2. Spatial Feature Extraction and Feature Fusion - extractive PDF cue:** First, the Multi-modal Affordance Perception (MAP) module extracts visual and affordance features (Sec.
- **p. 4 / 3.2. Spatial Feature Extraction and Feature Fusion - extractive PDF cue:** These spatial and affordance embeddings are then combined through element-wise addition into a feature fc, which is processed by a multi-head attention mechanism.
- **p. 3 / 3.1. Multi-Modal Affordance Perception - extractive PDF cue:** We combine affordance detection with visual feature extraction to create the comprehensive object representations.
- **p. 5 / 3.3. Query Mapping - extractive PDF cue:** We compute the similarity between vq and the feature representations of each point to identify manipulative regions: s(p) = sim(vq, f(p)) = vq · f(p) ...
- **p. 5 / 3.2. Spatial Feature Extraction and Feature Fusion - extractive PDF cue:** (5) This balanced loss optimizes the OVA-Fields to generate embeddings that capture both affordance and visual features, supporting robust affordance detection and visual recognition in ...
- **p. 4 / 3.2. Spatial Feature Extraction and Feature Fusion - extractive PDF cue:** This loss maximizes the similarity between the correct affordance and point features while minimizing it for incorrect affordances.
- **p. 3 / 3.1. Multi-Modal Affordance Perception - extractive PDF cue:** To address this, we apply BSRGAN [46] for super-resolution, with the objectives of enhancing the resolution of small object bounding boxes and improving the detection ...

## Design Rationale

- **p. 3 / 3. Methods - extractive PDF cue:** Here, we introduce our framework, OVA-Fields, which enables accurate affordance detection in 3D scenes based on natural language queries.
- **p. 2 / 1. Introduction - extractive PDF cue:** Our main contributions are summarized as follows: • We propose OVA-Fields, a novel framework for affordance detection in 3D real-world scenes.
- **p. 1 / 1. Introduction - extractive PDF cue:** Our framework directly maps the user's open-vocabulary semantic queries to actionable affordance locations in the complex 3D scenes, allowing robots to identify and interact with ...

## Source Evidence Cues

- **p. 3 / 3.2. Spatial Feature Extraction and Feature Fusion - extractive PDF cue:** Through a series of processing steps, the OVA-Fields then produces a high-dimensional feature representation for each coordinate point, which incorporates both rich visual information and ...
- **p. 4 / 3.2. Spatial Feature Extraction and Feature Fusion - extractive PDF cue:** First, the Multi-modal Affordance Perception (MAP) module extracts visual and affordance features (Sec.
- **p. 4 / 3.2. Spatial Feature Extraction and Feature Fusion - extractive PDF cue:** These spatial and affordance embeddings are then combined through element-wise addition into a feature fc, which is processed by a multi-head attention mechanism.
- **p. 3 / 3.1. Multi-Modal Affordance Perception - extractive PDF cue:** We combine affordance detection with visual feature extraction to create the comprehensive object representations.
- **p. 5 / 3.3. Query Mapping - extractive PDF cue:** We compute the similarity between vq and the feature representations of each point to identify manipulative regions: s(p) = sim(vq, f(p)) = vq · f(p) ...
- **p. 5 / 3.2. Spatial Feature Extraction and Feature Fusion - extractive PDF cue:** (5) This balanced loss optimizes the OVA-Fields to generate embeddings that capture both affordance and visual features, supporting robust affordance detection and visual recognition in ...
- **Detected method headings:** 3. Methods (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Through a series of processing steps, the OVA-Fields then produces a high-dimensional feature representation for each coordinate point, which incorporates both rich ... | p. 3 (3.2. Spatial Feature Extraction and Feature Fusion), p. 4 (3.2. Spatial Feature Extraction and Feature Fusion) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | First, the Multi-modal Affordance Perception (MAP) module extracts visual and affordance features (Sec. | p. 4 (3.2. Spatial Feature Extraction and Feature Fusion), p. 4 (3.2. Spatial Feature Extraction and Feature Fusion) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | These spatial and affordance embeddings are then combined through element-wise addition into a feature fc, which is processed by a multi-head attention ... | p. 4 (3.2. Spatial Feature Extraction and Feature Fusion), p. 3 (3.1. Multi-Modal Affordance Perception) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.2. Spatial Feature Extraction and Feature Fusion - extractive PDF cue:** This loss maximizes the similarity between the correct affordance and point features while minimizing it for incorrect affordances.
- **p. 5 / 3.2. Spatial Feature Extraction and Feature Fusion - extractive PDF cue:** (5) This balanced loss optimizes the OVA-Fields to generate embeddings that capture both affordance and visual features, supporting robust affordance detection and visual recognition in ...
- **p. 3 / 3.1. Multi-Modal Affordance Perception - extractive PDF cue:** To address this, we apply BSRGAN [46] for super-resolution, with the objectives of enhancing the resolution of small object bounding boxes and improving the detection ...
- **p. 4 / 3.2. Spatial Feature Extraction and Feature Fusion - extractive PDF cue:** The total loss L combines these two terms by 6388
- **p. 3 / 3.1. Multi-Modal Affordance Perception - extractive PDF cue:** These heatmaps show the likelihood of specific affordances associated with the object, producing heatmaps Hi for each affordance type aj (e.g., "open" or "hold").
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 3 (3.1. Multi-Modal Affordance Perception), p. 4 (3.2. Spatial Feature Extraction and Feature Fusion), p. 4 (3.2. Spatial Feature Extraction and Feature Fusion), p. 5 (3.2. Spatial Feature Extraction and Feature Fusion).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | OVA-Fields, uses, sequence, RGB-D, images, along, pose, data, camera, intrinsics, input, build, point, cloud | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | OVA-Fields, uses, sequence, RGB-D, images, along, pose, data, camera, intrinsics | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | Here, introduce, framework, OVA-Fields, enables, accurate, affordance, detection, scenes, natural | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | loss, maximizes, similarity, between, correct, affordance, point, features, while, minimizing | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.2. Spatial Feature Extraction and Feature Fusion - extractive PDF cue:** In the OVA-Fields, our approach uses a sequence of RGB-D images, along with pose data and camera intrinsics, as input to build a point cloud ...
- **p. 2 / 1. Introduction - extractive PDF cue:** This module detects key parts like handles with low computational cost, supporting robust and scalable real robot manipulation. • We enable seamless integration between semantic ...
- **p. 4 / 3.2. Spatial Feature Extraction and Feature Fusion - extractive PDF cue:** A learnable temperature parameter further optimizes the OVA-Fields' ability to distinguish affordance types, allowing accurate detection of actionable regions in real 3D environments based on ...
- **p. 5 / 3.3. Query Mapping - extractive PDF cue:** In the final step, we map the user's complex natural language instructions to specific affordances in the 3D scene to identify the corresponding manipulative regions.
- **p. 2 / 1. Introduction - extractive PDF cue:** Such a model would allow robots to detect actionable areas and interact effectively with specific parts in complex and multi-object environments, guided by open-ended user ...
- **p. 3 / 3.1. Multi-Modal Affordance Perception - extractive PDF cue:** (1) These high-response regions indicate potential actionable areas on the image plane.
- **p. 4 / 3.2. Spatial Feature Extraction and Feature Fusion - extractive PDF cue:** Negative samples contain mismatched pairs, such as "handle" points with unrelated actions ("grab the cup") or visual contexts, like refrigerator handles paired with distant image ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Let I represent the input sequence of image frames, and OD(I) = b1, b2, . . . , bn denote the set ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Here, we introduce our framework, OVA-Fields, which enables accurate affordance detection in 3D scenes based on natural language queries. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | For example, "Open the refrigerator" (Level 1) achieves 100% success (10/10 trials), while context-dependent instructions like "Find a snack for my lunch" ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4.1. Experiment Settings - extractive PDF cue:** OpenScene and CLIPFO3D are adjusted with frozen encoders and retrained projections using our affordance labels.
- **p. 3 / 3.1. Multi-Modal Affordance Perception - extractive PDF cue:** The scaled values H are then passed through a sigmoid function to compute the final weight, ensuring balanced training responses across regions.
- **p. 3 / 3.1. Multi-Modal Affordance Perception - extractive PDF cue:** Using a pre-trained CLIP model [28], visual embeddings are computed for each bounding box, embedding both object and spatial information into the 3D scene.
- **p. 4 / 3.2. Spatial Feature Extraction and Feature Fusion - extractive PDF cue:** OVA-Fields integrates feature fusion and training in three key steps.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Through, series, processing, steps, OVA-Fields, then, produces, high-dimensional, feature, representation, coordinate, point, incorporates, rich, visual, information, affordance, First, Multi-modal, Perception.
- **Relevant PDF headings:** 3. Methods (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Our experimental dataset comprises multi-source RGB-D sequences captured using consumer-grade devices (Apple iPad Pro with LiDAR) and benchmark datasets to systematically evaluate ... | p. 5 (4.1. Experiment Settings), p. 5 (4.1. Experiment Settings) |
| Action / skill decoding | In the context of fine-grained affordance detection, our model consistently outperforms baseline approaches. | p. 5 (4.2. Numerical and Visual Comparisons), p. 6 (4.2. Numerical and Visual Comparisons) |
| Receding execution / feedback | The case of "grab the cup" reveals that although affordance detection reaches 90% spatial accuracy, the current pipeline achieves a 20% success ... | p. 8 (5. Real Robot Experiments), p. 6 (4.3. Ablation Study) |

## Failure and Ablation Link

- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** Comparison of the small object processing procedure in the ablation study. a systematic ablation study on the dynamic weight mechanism by comparing four variants (Tab.
- **p. 6 / 4.3. Ablation Study - extractive PDF cue:** To evaluate the effectiveness of our small object handling mechanism, we conduct a comparative experiment by studying the OVAFields' performance with and without the super-resolution ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 4. Effectiveness of dynamic feature arbitration. Our dy- namic weighting shows that static blending fails to handle feature conflicts in open-vocabulary settings. Notably, pure ...
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** All variants share identical training protocols on the Lab and Home dataset and are evaluated on two metrics: mIoU and instruction grounding accuracy (the success ...
- **p. 5 / 4.1. Experiment Settings - extractive PDF cue:** For ClosedSet Affordance Detection Model (3D AffordanceNet [5], Mask3D [31]), we adjust Mask3D's architectures while preserving its core mechanisms and replace Mask3D's output head with ...
- **p. 5 / 4.1. Experiment Settings - extractive PDF cue:** For Open-Vocabulary Affordance Detection Models (OpenAD [36], OpenMask3D [35], CLIP-Fields [32], OpenScene [26], CLIP-FO3D [45]), we maintain OpenMask3D's and CLIP-Fields's original architectures but unify text-conditional ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Method Overview. OVA-Fields integrates feature fusion and training in three key steps. First, the Multi-modal Affordance Perception (MAP) module extracts visual and affordance ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3.2. Spatial Feature Extraction and Feature Fusion), p. 4 (3.2. Spatial Feature Extraction and Feature Fusion), p. 4 (3.2. Spatial Feature Extraction and Feature Fusion), p. 3 (3.1. Multi-Modal Affordance Perception), p. 5 (3.3. Query Mapping), p. 5 (3.2. Spatial Feature Extraction and Feature Fusion), objective p. 4 (3.2. Spatial Feature Extraction and Feature Fusion), p. 5 (3.2. Spatial Feature Extraction and Feature Fusion), p. 3 (3.1. Multi-Modal Affordance Perception), p. 4 (3.2. Spatial Feature Extraction and Feature Fusion), p. 3 (3.1. Multi-Modal Affordance Perception), temporal p. 3 (3.1. Multi-Modal Affordance Perception), p. 3 (3. Methods), p. 4 (3.2. Spatial Feature Extraction and Feature Fusion), p. 5 (4. Experiments), p. 5 (3.3. Query Mapping), p. 8 (5. Real Robot Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
