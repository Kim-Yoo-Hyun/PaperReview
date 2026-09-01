# Method - ViewSRD: 3D Visual Grounding via Structured Multi-View Decomposition

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Huang_ViewSRD_3D_Visual_Grounding_via_Structured_Multi-View_Decomposition_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_ViewSRD_3D_Visual_Grounding_via_Structured_Multi-View_Decomposition_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3.3. Multi-view Textual-Scene Interaction Module), p. 5 (3.3. Multi-view Textual-Scene Interaction Module), p. 6 (3.5. Overall Loss Functions), p. 6 (3.5. Overall Loss Functions)): To effectively integrate sentence features from text encoders with viewpoint features extracted from CCVTs, we introduce the Multi-view Textual Module, which employs a cross-attention mechanism [39] to seamlessly encode viewpoint ...

## Method Body Digest

- **p. 5 / 3.3. Multi-view Textual-Scene Interaction Module - extractive PDF cue:** To effectively integrate sentence features from text encoders with viewpoint features extracted from CCVTs, we introduce the Multi-view Textual Module, which employs a cross-attention mechanism ...
- **p. 5 / 3.3. Multi-view Textual-Scene Interaction Module - extractive PDF cue:** To effectively capture object features across diverse scenes, we introduce a Multi-View Scene Module that extracts and refines scene representations from multiple viewpoints.
- **p. 6 / 3.5. Overall Loss Functions - extractive PDF cue:** For details of these losses, please refer to supplementary materials.
- **p. 6 / 3.5. Overall Loss Functions - extractive PDF cue:** The total loss function is defined as: L = 𝜆𝑂𝑏𝑗L𝑂𝑏𝑗𝑒𝑐𝑡+ 𝜆𝑅𝑒𝑓L𝑃 𝑅𝑒𝑓+ 𝜆𝑆𝑒𝑛𝑡L𝑆𝑒𝑛𝑡.
- **p. 5 / 3.3. Multi-view Textual-Scene Interaction Module - extractive PDF cue:** The CCVTs are jointly optimized with our proposed textual and scene modules.
- **p. 5 / 3.3. Multi-view Textual-Scene Interaction Module - extractive PDF cue:** We take the average of these dot products across different sentences and compute a corresponding probability distribution using the softmax function.
- **p. 1 / Abstract - extractive PDF cue:** These decomposed representations serve as the foundation for the Multi-view Textual-Scene Interaction (Multi-TSI) module, which integrates textual and scene features across multiple viewpoints using shared, ...
- **p. 2 / 2. The nightstand is closest to the wall - extractive PDF cue:** 1(b), ViewSRD first applies the SRD module to decompose complex multi-anchor queries into a set of simpler single-anchor queries, isolating interactions between the target and ...

## Design Rationale

- **p. 2 / 2. The nightstand is closest to the wall - extractive PDF cue:** In summary, our contributions are fourfold: • We propose ViewSRD, a framework that formulates 3D visual grounding as a structured multi-view decomposition process, effectively handling ...
- **p. 2 / 2. The nightstand is closest to the wall - extractive PDF cue:** This structured decomposition enables the model to extract more effective textual features for grounding. • We develop the Multi-view Textual-Scene Interaction (Multi-TSI) module to explicitly ...
- **p. 3 / 3. ViewSRD - extractive PDF cue:** The overall framework of our method is illustrated in Fig.

## Source Evidence Cues

- **p. 5 / 3.3. Multi-view Textual-Scene Interaction Module - extractive PDF cue:** To effectively integrate sentence features from text encoders with viewpoint features extracted from CCVTs, we introduce the Multi-view Textual Module, which employs a cross-attention mechanism ...
- **p. 5 / 3.3. Multi-view Textual-Scene Interaction Module - extractive PDF cue:** To effectively capture object features across diverse scenes, we introduce a Multi-View Scene Module that extracts and refines scene representations from multiple viewpoints.
- **p. 6 / 3.5. Overall Loss Functions - extractive PDF cue:** For details of these losses, please refer to supplementary materials.
- **p. 6 / 3.5. Overall Loss Functions - extractive PDF cue:** The total loss function is defined as: L = 𝜆𝑂𝑏𝑗L𝑂𝑏𝑗𝑒𝑐𝑡+ 𝜆𝑅𝑒𝑓L𝑃 𝑅𝑒𝑓+ 𝜆𝑆𝑒𝑛𝑡L𝑆𝑒𝑛𝑡.
- **Detected method headings:** 4.4. SRD Enhances Other 3DVG Methods (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To effectively integrate sentence features from text encoders with viewpoint features extracted from CCVTs, we introduce the Multi-view Textual Module, which employs ... | p. 5 (3.3. Multi-view Textual-Scene Interaction Module), p. 5 (3.3. Multi-view Textual-Scene Interaction Module) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To effectively capture object features across diverse scenes, we introduce a Multi-View Scene Module that extracts and refines scene representations from multiple ... | p. 5 (3.3. Multi-view Textual-Scene Interaction Module), p. 6 (3.5. Overall Loss Functions) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | For details of these losses, please refer to supplementary materials. | p. 6 (3.5. Overall Loss Functions), p. 6 (3.5. Overall Loss Functions) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3.5. Overall Loss Functions - extractive PDF cue:** For details of these losses, please refer to supplementary materials.
- **p. 6 / 3.5. Overall Loss Functions - extractive PDF cue:** The total loss function is defined as: L = 𝜆𝑂𝑏𝑗L𝑂𝑏𝑗𝑒𝑐𝑡+ 𝜆𝑅𝑒𝑓L𝑃 𝑅𝑒𝑓+ 𝜆𝑆𝑒𝑛𝑡L𝑆𝑒𝑛𝑡.
- **p. 5 / 3.3. Multi-view Textual-Scene Interaction Module - extractive PDF cue:** The CCVTs are jointly optimized with our proposed textual and scene modules.
- **p. 5 / 3.3. Multi-view Textual-Scene Interaction Module - extractive PDF cue:** We take the average of these dot products across different sentences and compute a corresponding probability distribution using the softmax function.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 6 (3.5. Overall Loss Functions), p. 6 (3.5. Overall Loss Functions).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | decomposed, representations, serve, foundation, Multi-view, Textual-Scene, Interaction, Multi-TSI, module, integrates, textual, scene, features, across | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | decomposed, representations, serve, foundation, Multi-view, Textual-Scene, Interaction, Multi-TSI, module, integrates | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, contributions, fourfold, ViewSRD, framework, formulates, visual, grounding, structured, multi-view | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | details, losses, please, refer, supplementary, materials, total, loss, function, defined | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Abstract - extractive PDF cue:** These decomposed representations serve as the foundation for the Multi-view Textual-Scene Interaction (Multi-TSI) module, which integrates textual and scene features across multiple viewpoints using shared, ...
- **p. 2 / 2. The nightstand is closest to the wall - extractive PDF cue:** 1(b), ViewSRD first applies the SRD module to decompose complex multi-anchor queries into a set of simpler single-anchor queries, isolating interactions between the target and ...
- **p. 2 / 2. The nightstand is closest to the wall - extractive PDF cue:** In summary, our contributions are fourfold: • We propose ViewSRD, a framework that formulates 3D visual grounding as a structured multi-view decomposition process, effectively handling ...
- **p. 3 / 3. ViewSRD - extractive PDF cue:** The second is the Multi-view Textual-Scene Interaction (Multi-TSI) module, which mitigates viewpoint dependency by integrating a shared, cross-modal consistent view token into both the language ...
- **p. 1 / Abstract - extractive PDF cue:** Experiments on 3D visual grounding datasets show that ViewSRD significantly outperforms state-of-the-art methods, particularly in complex queries requiring precise spatial differentiation.
- **p. 3 / 3. ViewSRD - extractive PDF cue:** This decomposition enables more precise inference of relative relationships between objects, improving the model's ability to capture spatial interactions.
- **p. 4 / 3.1. Simple Relation Decoupling Module - extractive PDF cue:** Given an input sentence, 𝐶𝑙𝑎𝑠first determines which word belongs to the target.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | This decoupling mechanism reduces ambiguity in multi-anchor descriptions, enhances target grounding, and serves as a model-independent preprocessing step, ensuring seamless compatibility with ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | To tackle these challenges, we propose ViewSRD, a framework that formulates 3D visual grounding as a structured multi-view decomposition process. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | All experiments are implemented in PyTorch and run on a single RTX 4090 GPU. | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** effectively, integrate, sentence, features, text, encoders, viewpoint, extracted, CCVTs, introduce, Multi-view, Textual, Module, employs, cross-attention, mechanism, seamlessly, encode, feature, space.
- **Relevant PDF headings:** 4.4. SRD Enhances Other 3DVG Methods (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Nr3D [1] contains 45,503 human utterances referencing 707 indoor scenes from ScanNet [10], covering 76 object categories with multiple same-class distractors. | p. 6 (4.1. Experiment Settings), p. 6 (4.1. Experiment Settings) |
| Semantic / temporal fusion | We compare ViewSRD with recent state-of-the-art approaches to evaluate its effectiveness on 3DVG. | p. 6 (4.2. 3D Visual Grounding Results), p. 7 (4.2. 3D Visual Grounding Results) |
| Robot query / planning handoff | Quantitative results on Nr3D (Table 1) show that ViewSRD achieves a 5.2% accuracy gain over the best prior method, CoT3DRef, under identical ... | p. 7 (4.2. 3D Visual Grounding Results), p. 7 (4.3. Analysis of Anchors) |

## Failure and Ablation Link

- **p. 8 / 4.5. Ablation Study - extractive PDF cue:** To assess the contribution of each component within ViewSRD, we conducted detailed ablation studies on the Nr3D dataset [1].
- **p. 8 / 4.5. Ablation Study - extractive PDF cue:** We evaluate the effect of varying view counts on 3DVG performance using the Nr3D dataset.
- **p. 7 / 4.2. 3D Visual Grounding Results - extractive PDF cue:** Moreover, under viewpoint shifts, CoT3DRef struggles to maintain alignment, whereas ViewSRD reliably grounds targets by capturing spatial relations invariant to viewpoint changes (e.g., "The trash ...
- **p. 7 / 4.4. SRD Enhances Other 3DVG Methods - extractive PDF cue:** This decoupling mechanism reduces ambiguity in multi-anchor descriptions, enhances target grounding, and serves as a model-independent preprocessing step, ensuring seamless compatibility with various 3DVG methods ...
- **p. 8 / 5. Conclusion - extractive PDF cue:** A limitation of ViewSRD is its assumption that complex queries can be fully decomposed without overlapping relationships.
- **p. 8 / 5. Conclusion - extractive PDF cue:** While the decomposition into overlapping relations does not degrade performance, it diminishes the intended benefits of simplification.
- **p. 7 / 4.2. 3D Visual Grounding Results - extractive PDF cue:** These results confirm the robustness and generalizability of our approach across diverse scenario.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3.3. Multi-view Textual-Scene Interaction Module), p. 5 (3.3. Multi-view Textual-Scene Interaction Module), p. 6 (3.5. Overall Loss Functions), p. 6 (3.5. Overall Loss Functions), objective p. 6 (3.5. Overall Loss Functions), p. 6 (3.5. Overall Loss Functions), p. 5 (3.3. Multi-view Textual-Scene Interaction Module), p. 5 (3.3. Multi-view Textual-Scene Interaction Module), temporal p. 7 (4.4. SRD Enhances Other 3DVG Methods), p. 1 (Abstract), p. 1 (2. The nightstand is closest to the wall), p. 3 (3. ViewSRD), p. 6 (3.4. Textual-Scene Reasoning Module), p. 8 (5. Conclusion).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
