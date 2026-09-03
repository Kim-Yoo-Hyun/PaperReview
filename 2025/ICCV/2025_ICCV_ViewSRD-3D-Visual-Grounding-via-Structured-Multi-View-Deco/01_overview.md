# ViewSRD: 3D Visual Grounding via Structured Multi-View Decomposition

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Huang_ViewSRD_3D_Visual_Grounding_via_Structured_Multi-View_Decomposition_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_ViewSRD_3D_Visual_Grounding_via_Structured_Multi-View_Decomposition_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Huang_ViewSRD_3D_Visual_Grounding_via_Structured_Multi-View_Decomposition_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_ViewSRD_3D_Visual_Grounding_via_Structured_Multi-View_Decomposition_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Large language models (LLMs) often have difficulty interpreting such descriptions [17, 51], yet resolving these ambiguities is crucial for improving grounding accuracy [20].를 문제로 두고, In summary, our contributions are fourfold: • We propose ViewSRD, a framework that formulates 3D visual grounding as a structured multi-view decomposition process, effectively handling complex multi-anchor queries and mitigating text-vi ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D visual grounding aims to identify and localize objects in a 3D space based on textual descriptions.
- **p. 1 / Abstract - extractive body cue:** However, existing methods struggle with disentangling targets from anchors in complex multi-anchor queries and resolving inconsistencies in spatial descriptions caused by perspective variations.
- **p. 1 / Abstract - extractive body cue:** To tackle these challenges, we propose ViewSRD, a framework that formulates 3D visual grounding as a structured multi-view decomposition process.
- **p. 1 / Abstract - extractive body cue:** First, the Simple Relation Decoupling (SRD) module restructures complex multianchor queries into a set of targeted single-anchor statements, generating a structured set of perspective-aware descriptions ...
- **p. 1 / Abstract - extractive body cue:** These decomposed representations serve as the foundation for the Multi-view Textual-Scene Interaction (Multi-TSI) module, which integrates textual and scene features across multiple viewpoints using shared, ...
- **p. 1 / 2. The nightstand is closest to the wall - extractive body cue:** Large language models (LLMs) often have difficulty interpreting such descriptions [17, 51], yet resolving these ambiguities is crucial for improving grounding accuracy [20].
- **p. 2 / 2. The nightstand is closest to the wall - extractive body cue:** Ultimately, both the inherent complexity of multi-anchor queries and the challenges introduced by perspective shifts hinder the accurate interpretation of positional relationships in 3DVG, limiting ...

## Core Idea

- **p. 2 / 2. The nightstand is closest to the wall - extractive body cue:** In summary, our contributions are fourfold: • We propose ViewSRD, a framework that formulates 3D visual grounding as a structured multi-view decomposition process, effectively handling ...
- **p. 2 / 2. The nightstand is closest to the wall - extractive body cue:** This structured decomposition enables the model to extract more effective textual features for grounding. • We develop the Multi-view Textual-Scene Interaction (Multi-TSI) module to explicitly ...
- **p. 3 / 3. ViewSRD - extractive body cue:** The overall framework of our method is illustrated in Fig.
- **p. 4 / 3.2. Textual Aggregation - extractive body cue:** To enable the model to effectively learn from diverse sentence representations, we introduce a textual feature aggregation strategy.
- **p. 5 / 3.3. Multi-view Textual-Scene Interaction Module - extractive body cue:** At the final Transformer layer, the output consists of both [object] tokens and [view] tokens.
- **p. 5 / 3.3. Multi-view Textual-Scene Interaction Module - extractive body cue:** To effectively integrate sentence features from text encoders with viewpoint features extracted from CCVTs, we introduce the Multi-view Textual Module, which employs a cross-attention mechanism ...
- **p. 5 / 3.3. Multi-view Textual-Scene Interaction Module - extractive body cue:** To effectively capture object features across diverse scenes, we introduce a Multi-View Scene Module that extracts and refines scene representations from multiple viewpoints.
- **p. 6 / 3.5. Overall Loss Functions - extractive body cue:** For details of these losses, please refer to supplementary materials.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | These decomposed representations serve as the foundation for the Multi-view Textual-Scene Interaction (Multi-TSI) module, which integrates textual and scene features across multiple viewpoints using shared, Cross-modal Consistent View T ... | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (Abstract), p. 2 (2. The nightstand is closest to the wall) |
| State/latent | decomposed, representations, serve, foundation, Multi-view, Textual-Scene, Interaction, Multi-TSI, module, integrates, textual, scene | geometry, map, object/relationship state | p. 1 (Abstract), p. 2 (2. The nightstand is closest to the wall), p. 2 (2. The nightstand is closest to the wall) |
| Output/action | 1(b), ViewSRD first applies the SRD module to decompose complex multi-anchor queries into a set of simpler single-anchor queries, isolating interactions between the target and its anchors. | point map, pose, scene graph, affordance 또는 query result | p. 2 (2. The nightstand is closest to the wall), p. 2 (2. The nightstand is closest to the wall), p. 3 (3. ViewSRD) |
| Objective/outcome | For details of these losses, please refer to supplementary materials. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (3.5. Overall Loss Functions), p. 6 (3.5. Overall Loss Functions), p. 5 (3.3. Multi-view Textual-Scene Interaction Module) |

## Main Claims and Actual Contribution

- **p. 2 / 2. The nightstand is closest to the wall - extractive body cue:** In summary, our contributions are fourfold: • We propose ViewSRD, a framework that formulates 3D visual grounding as a structured multi-view decomposition process, effectively handling ...
- **p. 2 / 2. The nightstand is closest to the wall - extractive body cue:** This structured decomposition enables the model to extract more effective textual features for grounding. • We develop the Multi-view Textual-Scene Interaction (Multi-TSI) module to explicitly ...
- **p. 3 / 3. ViewSRD - extractive body cue:** The overall framework of our method is illustrated in Fig.
- **p. 4 / 3.2. Textual Aggregation - extractive body cue:** To enable the model to effectively learn from diverse sentence representations, we introduce a textual feature aggregation strategy.
- **p. 5 / 3.3. Multi-view Textual-Scene Interaction Module - extractive body cue:** At the final Transformer layer, the output consists of both [object] tokens and [view] tokens.
- **p. 7 / 4.2. 3D Visual Grounding Results - extractive body cue:** Quantitative results on Nr3D (Table 1) show that ViewSRD achieves a 5.2% accuracy gain over the best prior method, CoT3DRef, under identical settings.
- **p. 7 / 4.3. Analysis of Anchors - extractive body cue:** Notably, our approach achieves higher accuracy in multianchor queries than in single-anchor ones, demonstrating that when properly processed, multi-anchor information enhances 3DVG performance rather than ...
- **p. 8 / 4.5. Ablation Study - extractive body cue:** These results indicate that as an LLM's ability to disentangle complex sentence structures improves, it becomes more effective at isolating and extracting relevant information, ultimately ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4.2. 3D Visual Grounding Results), p. 7 (4.3. Analysis of Anchors) |
| Embodiment/environment | Nr3D [1] contains 45,503 human utterances referencing 707 indoor scenes from ScanNet [10], covering 76 object categories with multiple same-class distractors. | hardware/simulator version and reset protocol | p. 6 (4.1. Experiment Settings), p. 6 (4.1. Experiment Settings) |
| Dataset/benchmark | Performance (%) of SRD module improves MVT [18], BUTD-DETR [21] and EDA [42] on ScanRefer [6] dataset. | role, split, size and leakage | p. 6 (4.1. Experiment Settings), p. 6 (4.1. Experiment Settings), p. 7 (4.3. Analysis of Anchors), p. 8 (4.5. Ablation Study) |
| Metric | LLM decoupler Accuracy OpenChat [40] 69.6% DeepSeek-R1 [28] 69.9% Qwen-Plus [46] 70.5% Qwen-Turbo [46] 70.7% views, performance improves from 64.4% (1 view) to 67.7% (2 views), but plateaus at 68.4% with 8 ... | definition, denominator, direction and uncertainty | p. 8 (4.5. Ablation Study), p. 7 (4.3. Analysis of Anchors), p. 7 (4.3. Analysis of Anchors) |
| Baseline/ablation | We compare ViewSRD with recent state-of-the-art approaches to evaluate its effectiveness on 3DVG. | fair input/data/compute/action matching | p. 6 (4.2. 3D Visual Grounding Results), p. 7 (4.2. 3D Visual Grounding Results), p. 7 (4.3. Analysis of Anchors) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** A limitation of ViewSRD is its assumption that complex queries can be fully decomposed without overlapping relationships.
- **p. 8 / 5. Conclusion - extractive body cue:** While the decomposition into overlapping relations does not degrade performance, it diminishes the intended benefits of simplification.
- **p. 7 / 4.2. 3D Visual Grounding Results - extractive body cue:** These results confirm the robustness and generalizability of our approach across diverse scenario.
- **p. 7 / 4.2. 3D Visual Grounding Results - extractive body cue:** In contrast, ViewSRD correctly grounds targets by decomposing complex queries and leveraging robust spatial relationships between targetanchor pairs.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Large language models (LLMs) often have difficulty interpreting such descriptions [17, 51], yet resolving these ambiguities is crucial for improving grounding accuracy [20].를 문제로 두고, In summary, our contributions are fourfold: • We propose ViewSRD, a framework that formulates 3D visual grounding as a structured multi-view decomposition process, effectively handling complex multi-anchor queries and mitigating text-vi ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (2. The nightstand is closest to the wall), p. 2 (2. The nightstand is closest to the wall), p. 1 (2. The nightstand is closest to the wall), p. 2 (2. The nightstand is closest to the wall), p. 3 (3. ViewSRD), p. 5 (3.3. Multi-view Textual-Scene Interaction Module) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
