# Method - Geometry-Aware Cross-Modal Graph Alignment for Referring Segmentation in 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Tao_Geometry-Aware_Cross-Modal_Graph_Alignment_for_Referring_Segmentation_in_3D_Gaussian_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Tao_Geometry-Aware_Cross-Modal_Graph_Alignment_for_Referring_Segmentation_in_3D_Gaussian_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (5.3. 3D Scene Graph Construction (3DSGC)), p. 5 (5.3. 3D Scene Graph Construction (3DSGC))): We use the pretrained model [18] to obtain the object-level representations and construct an object-level 3D scene graph Gsg = (V, E), where each node vi represents an object with ...

## Method Body Digest

- **p. 5 / 5.3. 3D Scene Graph Construction (3DSGC) - extractive body cue:** We use the pretrained model [18] to obtain the object-level representations and construct an object-level 3D scene graph Gsg = (V, E), where each node ...
- **p. 5 / 5.3. 3D Scene Graph Construction (3DSGC) - extractive body cue:** Relying solely on primitive-level reasoning forces the model to infer object structure implicitly from fragmentary cues, leading to ambiguous alignment under viewpoint changes.
- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are: • We introduce a geometry-aware perspective for language grounding that embeds explicit spatial structure into linguistic features, enabling more accurate reasoning. • ...
- **p. 2 / 1. Introduction - extractive body cue:** Instead of treating text as a purely semantic signal, we expand the input description with position-aware prompts to derive a semantic-spatial graph that captures relational ...
- **p. 5 / 5.3. 3D Scene Graph Construction (3DSGC) - extractive body cue:** Therefore, a principled geometric abstraction is required to elevate Gaussian primitives into an object-level relational representation that supports explicit spatial reasoning.
- **p. 3 / 3. Problem Statement and Notations - extractive body cue:** Language-Guided 3D Referring Segmentation.
- **p. 3 / 3. Problem Statement and Notations - extractive body cue:** While this framework enables basic language-to-geometry grounding, its spatial reasoning capability remains limited, as analyzed in Sec.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are: • We introduce a geometry-aware perspective for language grounding that embeds explicit spatial structure into linguistic features, enabling more accurate reasoning. • ...
- **p. 2 / 1. Introduction - extractive body cue:** Guided by these findings, we propose GeoCGA (see Fig.
- **p. 3 / 3. Problem Statement and Notations - extractive body cue:** Spatial awareness deficiency leads to incorrect localization in ReferSplat [13], while our method correctly grounds the target despite challenging spatial cues. ri for each Gaussian ...

## Source Evidence Cues

- **p. 5 / 5.3. 3D Scene Graph Construction (3DSGC) - extractive body cue:** We use the pretrained model [18] to obtain the object-level representations and construct an object-level 3D scene graph Gsg = (V, E), where each node ...
- **p. 5 / 5.3. 3D Scene Graph Construction (3DSGC) - extractive body cue:** Relying solely on primitive-level reasoning forces the model to infer object structure implicitly from fragmentary cues, leading to ambiguous alignment under viewpoint changes.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | We use the pretrained model [18] to obtain the object-level representations and construct an object-level 3D scene graph Gsg = (V, E), ... | p. 5 (5.3. 3D Scene Graph Construction (3DSGC)), p. 5 (5.3. 3D Scene Graph Construction (3DSGC)) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Relying solely on primitive-level reasoning forces the model to infer object structure implicitly from fragmentary cues, leading to ambiguous alignment under viewpoint ... | p. 5 (5.3. 3D Scene Graph Construction (3DSGC)) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | We use the pretrained model [18] to obtain the object-level representations and construct an object-level 3D scene graph Gsg = (V, E), ... | p. 5 (5.3. 3D Scene Graph Construction (3DSGC)) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | contributions, introduce, geometry-aware, perspective, language, grounding, embeds, explicit, spatial, structure, linguistic, features, enabling, more | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | contributions, introduce, geometry-aware, perspective, language, grounding, embeds, explicit, spatial, structure | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, introduce, geometry-aware, perspective, language, grounding, embeds, explicit, spatial, structure | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | not recovered | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are: • We introduce a geometry-aware perspective for language grounding that embeds explicit spatial structure into linguistic features, enabling more accurate reasoning. • ...
- **p. 2 / 1. Introduction - extractive body cue:** Instead of treating text as a purely semantic signal, we expand the input description with position-aware prompts to derive a semantic-spatial graph that captures relational ...
- **p. 5 / 5.3. 3D Scene Graph Construction (3DSGC) - extractive body cue:** Therefore, a principled geometric abstraction is required to elevate Gaussian primitives into an object-level relational representation that supports explicit spatial reasoning.
- **p. 3 / 3. Problem Statement and Notations - extractive body cue:** Language-Guided 3D Referring Segmentation.
- **p. 3 / 3. Problem Statement and Notations - extractive body cue:** While this framework enables basic language-to-geometry grounding, its spatial reasoning capability remains limited, as analyzed in Sec.
- **p. 5 / 5.3. 3D Scene Graph Construction (3DSGC) - extractive body cue:** Relying solely on primitive-level reasoning forces the model to infer object structure implicitly from fragmentary cues, leading to ambiguous alignment under viewpoint changes.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | LERF-OVS extends the 3D Gaussian Splatting framework to open-vocabulary segmentation across multiple scenes. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | 2(b)), a Geometry-aware Cross-modal Graph Alignment framework that explicitly integrates spatial reasoning into 3D language segmentation. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We train GeoCGA for 4 epochs per scene with AdamW (learning rate 1 × 10-4, weight decay 1 × 10-2). | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 5.3. 3D Scene Graph Construction (3DSGC) - extractive body cue:** We use the pretrained model [18] to obtain the object-level representations and construct an object-level 3D scene graph Gsg = (V, E), where each node ...
- **p. 7 / 6.1. Experimental Setting - extractive body cue:** We train GeoCGA for 4 epochs per scene with AdamW (learning rate 1 × 10-4, weight decay 1 × 10-2).

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** pretrained, model, obtain, object-level, representations, construct, scene, graph, Gsg, where, node, represents, object, aggregated, descriptors, including, spatial, appearance, information, Relying.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | 3), where scenes are relatively clean and objects are easier to localize, GeoCGA still achieves the best performance across all categories and ... | p. 7 (6.2. Comparisons with State-of-the-Arts), p. 8 (6.3. Ablation Study) |
| Semantic / temporal fusion | Superscripts indicate absolute improvements over the baseline. | p. 7 (6.2. Comparisons with State-of-the-Arts), p. 7 (6.2. Comparisons with State-of-the-Arts) |
| Robot query / planning handoff | 3), where scenes are relatively clean and objects are easier to localize, GeoCGA still achieves the best performance across all categories and ... | p. 7 (6.2. Comparisons with State-of-the-Arts), p. 7 (6.2. Comparisons with State-of-the-Arts) |

## Failure and Ablation Link

- **p. 7 / 6.2. Comparisons with State-of-the-Arts - extractive body cue:** Comparative ablation results on Ramen and Kitchen.
- **p. 7 / 6.2. Comparisons with State-of-the-Arts - extractive body cue:** Ablation study on Semantic Graph and Geometry Graph.
- **p. 8 / 6.3. Ablation Study - extractive body cue:** Overall, all components contribute positively, indicating that structured graph reasoning and explicit relation modeling jointly enhance the robustness of GeoCGA.
- **p. 8 / 6.3. Ablation Study - extractive body cue:** The bottom row illustrates typical failure modes where spatial ambiguity or relational confusion leads to incorrect (ReferSplat [13]) or incomplete (Ours) segmentation. mentary perspectives.
- **p. 8 / 7. Conclusion and Discussion - extractive body cue:** Future work may explore end-to-end differentiable object discovery to reduce reliance on pretrained representations, as well as richer geometric priors and more scalable graph matching ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. Spatial reasoning deficiency leads to coarse segmenta- tion in ReferSplat [13], while our method produces precise masks. consistent segmentation under complex spatial cues. ...
- **p. 6 / 6.1. Experimental Setting - extractive body cue:** Ref-LERF emphasizes fine-grained referring understanding within individual scenes that involve intricate spatial layouts and strong occlusions.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (5.3. 3D Scene Graph Construction (3DSGC)), p. 5 (5.3. 3D Scene Graph Construction (3DSGC)), objective 본문 anchor 없음, temporal p. 6 (6.1. Experimental Setting), p. 2 (1. Introduction), p. 2 (2. Related Work), p. 3 (3. Problem Statement and Notations), p. 3 (2. Related Work), p. 5 (5.2. Geometry-Aware Prompt Expansion (GAPE)).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
