# Problem - ViewSRD: 3D Visual Grounding via Structured Multi-View Decomposition

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Huang_ViewSRD_3D_Visual_Grounding_via_Structured_Multi-View_Decomposition_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_ViewSRD_3D_Visual_Grounding_via_Structured_Multi-View_Decomposition_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (2. The nightstand is closest to the wall), p. 2 (2. The nightstand is closest to the wall), p. 1 (2. The nightstand is closest to the wall), p. 2 (2. The nightstand is closest to the wall), p. 3 (3. ViewSRD)): Large language models (LLMs) often have difficulty interpreting such descriptions [17, 51], yet resolving these ambiguities is crucial for improving grounding accuracy [20].

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** 3D visual grounding aims to identify and localize objects in a 3D space based on textual descriptions.
- **p. 1 / Abstract - extractive body cue:** However, existing methods struggle with disentangling targets from anchors in complex multi-anchor queries and resolving inconsistencies in spatial descriptions caused by perspective variations.
- **p. 1 / Abstract - extractive body cue:** To tackle these challenges, we propose ViewSRD, a framework that formulates 3D visual grounding as a structured multi-view decomposition process.
- **p. 1 / Abstract - extractive body cue:** First, the Simple Relation Decoupling (SRD) module restructures complex multianchor queries into a set of targeted single-anchor statements, generating a structured set of perspective-aware descriptions ...
- **p. 1 / Abstract - extractive body cue:** These decomposed representations serve as the foundation for the Multi-view Textual-Scene Interaction (Multi-TSI) module, which integrates textual and scene features across multiple viewpoints using shared, ...
- **p. 1 / 2. The nightstand is closest to the wall - extractive body cue:** Large language models (LLMs) often have difficulty interpreting such descriptions [17, 51], yet resolving these ambiguities is crucial for improving grounding accuracy [20].
- **p. 2 / 2. The nightstand is closest to the wall - extractive body cue:** Ultimately, both the inherent complexity of multi-anchor queries and the challenges introduced by perspective shifts hinder the accurate interpretation of positional relationships in 3DVG, limiting ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Large language models (LLMs) often have difficulty interpreting such descriptions [17, 51], yet resolving these ambiguities is crucial for improving grounding accuracy ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | These decomposed representations serve as the foundation for the Multi-view Textual-Scene Interaction (Multi-TSI) module, which integrates textual and scene features across multiple ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | decomposed, representations, serve, foundation, Multi-view, Textual-Scene, Interaction, Multi-TSI, module, integrates | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | summary, contributions, fourfold, ViewSRD, framework, formulates, visual, grounding | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: decomposed, representations, serve, foundation, Multi-view, Textual-Scene, Interaction, Multi-TSI, module, integrates | p. 1 (Abstract), p. 2 (2. The nightstand is closest to the wall), p. 2 (2. The nightstand is closest to the wall) |
| Decision / output variable | geometry/map/query r; body terms: summary, contributions, fourfold, ViewSRD, framework, formulates, visual, grounding | p. 2 (2. The nightstand is closest to the wall), p. 2 (2. The nightstand is closest to the wall), p. 3 (3. ViewSRD) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: details, losses, please, refer, supplementary, materials, total, loss | p. 6 (3.5. Overall Loss Functions), p. 6 (3.5. Overall Loss Functions) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (3.5. Overall Loss Functions), p. 5 (3.3. Multi-view Textual-Scene Interaction Module), p. 5 (3.3. Multi-view Textual-Scene Interaction Module) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 8 (4.5. Ablation Study), p. 7 (4.3. Analysis of Anchors), p. 7 (4.3. Analysis of Anchors) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 2. The nightstand is closest to the wall - extractive body cue:** Ultimately, both the inherent complexity of multi-anchor queries and the challenges introduced by perspective shifts hinder the accurate interpretation of positional relationships in 3DVG, limiting ...
- **p. 1 / 2. The nightstand is closest to the wall - extractive body cue:** Compounding this challenge, inconsistenThis ICCV paper is the Open Access version, provided by the Computer Vision Foundation.
- **p. 2 / 2. The nightstand is closest to the wall - extractive body cue:** To tackle these challenges, we propose ViewSRD, a framework that formulates 3D visual grounding as a structured multi-view decomposition process.
- **p. 3 / 3. ViewSRD - extractive body cue:** This multi-view setup introduces significant challenges for 3D visual grounding: (1) language-grounded spatial relations must remain consistent across view-dependent variations, and (2) object referents may ...

## What the Paper Changes

PDF body contribution framing (p. 2 (2. The nightstand is closest to the wall), p. 2 (2. The nightstand is closest to the wall), p. 3 (3. ViewSRD), p. 4 (3.2. Textual Aggregation), p. 5 (3.3. Multi-view Textual-Scene Interaction Module)): In summary, our contributions are fourfold: • We propose ViewSRD, a framework that formulates 3D visual grounding as a structured multi-view decomposition process, effectively handling complex multi-anchor queries and mitigating ...

- **p. 2 / 2. The nightstand is closest to the wall - extractive body cue:** This structured decomposition enables the model to extract more effective textual features for grounding. • We develop the Multi-view Textual-Scene Interaction (Multi-TSI) module to explicitly ...
- **p. 3 / 3. ViewSRD - extractive body cue:** The overall framework of our method is illustrated in Fig.
- **p. 4 / 3.2. Textual Aggregation - extractive body cue:** To enable the model to effectively learn from diverse sentence representations, we introduce a textual feature aggregation strategy.
- **p. 5 / 3.3. Multi-view Textual-Scene Interaction Module - extractive body cue:** At the final Transformer layer, the output consists of both [object] tokens and [view] tokens.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | A limitation of ViewSRD is its assumption that complex queries can be fully decomposed without overlapping relationships. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | While the decomposition into overlapping relations does not degrade performance, it diminishes the intended benefits of simplification. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | These results confirm the robustness and generalizability of our approach across diverse scenario. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | In contrast, ViewSRD correctly grounds targets by decomposing complex queries and leveraging robust spatial relationships between targetanchor pairs. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (Abstract), p. 2 (2. The nightstand is closest to the wall), p. 2 (2. The nightstand is closest to the wall), p. 3 (3. ViewSRD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (2. The nightstand is closest to the wall), p. 2 (2. The nightstand is closest to the wall), p. 1 (2. The nightstand is closest to the wall), p. 2 (2. The nightstand is closest to the wall), p. 3 (3. ViewSRD), interface p. 1 (Abstract), p. 2 (2. The nightstand is closest to the wall), p. 2 (2. The nightstand is closest to the wall), p. 3 (3. ViewSRD), objective p. 6 (3.5. Overall Loss Functions), p. 6 (3.5. Overall Loss Functions).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
