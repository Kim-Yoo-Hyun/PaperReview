# Problem - FROSS: Faster-Than-Real-Time Online 3D Semantic Scene Graph Generation from RGB-D Images

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (5 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Hou_FROSS_Faster-Than-Real-Time_Online_3D_Semantic_Scene_Graph_Generation_from_RGB-D_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Hou_FROSS_Faster-Than-Real-Time_Online_3D_Semantic_Scene_Graph_Generation_from_RGB-D_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (Body text (section not recovered)), p. 1 (6. Detailed Evaluation Metric)): FROSS: Faster-than-Real-Time Online 3D Semantic Scene Graph Generation from RGB-D Images Supplementary Material

## PDF Body Digest

- **p. 1 / Body text (section not recovered) - extractive body cue:** FROSS: Faster-than-Real-Time Online 3D Semantic Scene Graph Generation from RGB-D Images Supplementary Material
- **p. 1 / 6. Detailed Evaluation Metric - extractive body cue:** The evaluation procedure in this paper follows closely with Wu [35] to ensure a fair comparison.
- **p. 1 / 6. Detailed Evaluation Metric - extractive body cue:** The only difference is the exclusion of the ‘none' relationship category, as FROSS does not predict it.
- **p. 1 / 6. Detailed Evaluation Metric - extractive body cue:** Wu [35] also provided results evaluated under this protocol in their publicly released code.
- **p. 1 / 6. Detailed Evaluation Metric - extractive body cue:** Specifically, for a detected triplet in which both the subject and object match ground truth objects, only the predicted class labels for the subject, object, ...
- **p. 2 / 7.3. 2D Scene Graph Generation Performance - extractive body cue:** In this section, we present the evaluation of two models: the original EGTR [12] 2D SG generation model and our modified version employed in FROSS, ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | FROSS: Faster-than-Real-Time Online 3D Semantic Scene Graph Generation from RGB-D Images Supplementary Material | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | FROSS: Faster-than-Real-Time Online 3D Semantic Scene Graph Generation from RGB-D Images Supplementary Material | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | FROSS, Faster-than-Real-Time, Online, Semantic, Scene, Graph, Generation, RGB-D, Images, Supplementary | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | section, present, evaluation, models, original, EGTR, generation, model | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: FROSS, Faster-than-Real-Time, Online, Semantic, Scene, Graph, Generation, RGB-D, Images, Supplementary | p. 1 (Body text (section not recovered)), p. 2 (8. Statistics of the ReplicaSSG Dataset) |
| Decision / output variable | path/waypoint/velocity; body terms: section, present, evaluation, models, original, EGTR, generation, model | p. 2 (7.3. 2D Scene Graph Generation Performance) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: relationship, metrics, evaluated, graph, constraints, described | p. 3 (8. Statistics of the ReplicaSSG Dataset) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (8. Statistics of the ReplicaSSG Dataset) |
| Success / guarantee | goal reach with collision-free execution | p. 1 (6. Detailed Evaluation Metric), p. 1 (7.1. Object and Predicate Performance per Class), p. 2 (7.2. Additional Qualitative Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 6. Detailed Evaluation Metric - extractive body cue:** The evaluation procedure in this paper follows closely with Wu [35] to ensure a fair comparison.

## What the Paper Changes

PDF body contribution framing (p. 2 (7.3. 2D Scene Graph Generation Performance)): In this section, we present the evaluation of two models: the original EGTR [12] 2D SG generation model and our modified version employed in FROSS, RT-DETR+EGTR.

- additional contribution cue 없음

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 1 | The only difference is the exclusion of the ‘none' relationship category, as FROSS does not predict it. | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | While addressing this issue could potentially enhance FROSS's performance, we leave it as future work, as class imbalance ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | These results further demonstrate FROSS's robustness in diverse scene conditions. | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Misclassified objects are likely caused by occlusions from certain viewpoints or unusual viewing angles. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (Body text (section not recovered)), p. 2 (8. Statistics of the ReplicaSSG Dataset). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (Body text (section not recovered)), p. 1 (6. Detailed Evaluation Metric), interface p. 1 (Body text (section not recovered)), p. 2 (8. Statistics of the ReplicaSSG Dataset), objective p. 3 (8. Statistics of the ReplicaSSG Dataset).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
