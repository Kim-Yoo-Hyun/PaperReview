# Method - GeoProg3D: Compositional Visual Reasoning for City-Scale 3D Language Fields

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (4.1. Task Definition)): In summary, our contributions are threefold: • We propose GeoProg3D, a framework for compositional reasoning over city-scale 3D language fields, where visual programming can perform various 3D geographic vision tasks ...

## Method Body Digest

- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, our contributions are threefold: • We propose GeoProg3D, a framework for compositional reasoning over city-scale 3D language fields, where visual programming can perform ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To validate the effectiveness, we introduce novel tasks designed to assess urban-scale geographic visual reasoning capabilities and present GeoEval3D, a benchmark dataset specifically developed for ...
- **p. 6 / 4.1. Task Definition - extractive PDF cue:** The task set Qi = {(qk, ak)}Ki k=1 consists of pairs of queries qk and the corresponding ground truth answers ak.
- **p. 2 / 1. Introduction - extractive PDF cue:** However, intuitive and efficient interaction with these detailed 3D city models using natural language remains largely unexplored.
- **p. 6 / 4.3. Dataset construction and statistics - extractive PDF cue:** GeoEval3D is composed of unique 952 queries.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, our contributions are threefold: • We propose GeoProg3D, a framework for compositional reasoning over city-scale 3D language fields, where visual programming can perform ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To validate the effectiveness, we introduce novel tasks designed to assess urban-scale geographic visual reasoning capabilities and present GeoEval3D, a benchmark dataset specifically developed for ...
- **p. 6 / 4.1. Task Definition - extractive PDF cue:** The task set Qi = {(qk, ak)}Ki k=1 consists of pairs of queries qk and the corresponding ground truth answers ak.

## Source Evidence Cues

- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, our contributions are threefold: • We propose GeoProg3D, a framework for compositional reasoning over city-scale 3D language fields, where visual programming can perform ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To validate the effectiveness, we introduce novel tasks designed to assess urban-scale geographic visual reasoning capabilities and present GeoEval3D, a benchmark dataset specifically developed for ...
- **p. 6 / 4.1. Task Definition - extractive PDF cue:** The task set Qi = {(qk, ak)}Ki k=1 consists of pairs of queries qk and the corresponding ground truth answers ak.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | In summary, our contributions are threefold: • We propose GeoProg3D, a framework for compositional reasoning over city-scale 3D language fields, where visual ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To validate the effectiveness, we introduce novel tasks designed to assess urban-scale geographic visual reasoning capabilities and present GeoEval3D, a benchmark dataset ... | p. 2 (1. Introduction), p. 6 (4.1. Task Definition) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The task set Qi = {(qk, ak)}Ki k=1 consists of pairs of queries qk and the corresponding ground truth answers ak. | p. 6 (4.1. Task Definition) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | summary, contributions, threefold, GeoProg3D, framework, compositional, reasoning, over, city-scale, language, fields, where, visual, programming | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | summary, contributions, threefold, GeoProg3D, framework, compositional, reasoning, over, city-scale, language | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, contributions, threefold, GeoProg3D, framework, compositional, reasoning, over, city-scale, language | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | not recovered | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, our contributions are threefold: • We propose GeoProg3D, a framework for compositional reasoning over city-scale 3D language fields, where visual programming can perform ...
- **p. 2 / 1. Introduction - extractive PDF cue:** However, intuitive and efficient interaction with these detailed 3D city models using natural language remains largely unexplored.
- **p. 6 / 4.3. Dataset construction and statistics - extractive PDF cue:** GeoEval3D is composed of unique 952 queries.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Notably, our method excelled in the MESD (distance measurement) task, demonstrating precise horizontal spatial assessment capabilities. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | In addition, LangSplat caused a memory error with UrbanScene3D in our setting, which implies the efficiency of the tree structure for learning ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | In addition, LangSplat caused a memory error with UrbanScene3D in our setting, which implies the efficiency of the tree structure for learning ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** summary, contributions, threefold, GeoProg3D, framework, compositional, reasoning, over, city-scale, language, fields, where, visual, programming, perform, various, geographic, vision, tasks, image.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | The dataset B = {(Di, Qi)}S i=1 consists of pairs multi-view image sets Di and task sets Qi, where S is the ... | p. 6 (4. GeoEval3D Dataset), p. 6 (4. GeoEval3D Dataset) |
| Semantic / temporal fusion | We observed that GCLF outperforms baselines on GoogleEarth. | p. 7 (5.2. Experimental results), p. 7 (5.2. Experimental results) |
| Robot query / planning handoff | GeoProg3D further improved accuracy on both GoolgeEarth and UrbanScene3D. | p. 7 (5.2. Experimental results), p. 7 (5.2. Experimental results) |

## Failure and Ablation Link

- **p. 8 / 5.2. Experimental results - extractive PDF cue:** To assess the impact of each component of GeoProg3D, we conducted an ablation study to investigate the three tasks of GoogleEarth's GRD, SPR, and CMP.
- **p. 8 / 5.2. Experimental results - extractive PDF cue:** See appendix B for more ablation studies.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 7. Qualitative results and failure cases. The Ground Truth region for the GRD task is delineated by the yellow frame. localization that is independent ...
- **p. 8 / 5.2. Experimental results - extractive PDF cue:** Ablation study of different Geographical Vision APIs. itative examples and failure cases.
- **p. 7 / 5.1. Evaluation metrics - extractive PDF cue:** Note that MES-H and CMP are not evaluated in UrbanScene3D because Ground Truth for height cannot be obtained.
- **p. 7 / 5.2. Experimental results - extractive PDF cue:** These results demonstrate the limitations of localization using 3D language fields alone in 3D urban scenes and the effectiveness of GV-APIs and visual programming in ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (4.1. Task Definition), objective 본문 anchor 없음, temporal p. 7 (5.2. Experimental results), p. 7 (5.2. Experimental results), p. 8 (5.2. Experimental results), p. 3 (3.1. Overview of GeoProg3D), p. 1 (Abstract), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
