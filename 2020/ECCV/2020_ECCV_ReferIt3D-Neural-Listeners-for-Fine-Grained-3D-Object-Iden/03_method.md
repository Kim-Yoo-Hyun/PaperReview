# Method - ReferIt3D: Neural Listeners for Fine-Grained 3D Object Identification in Real-World Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://referit3d.github.io/; PDF retrieval source: https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123460409.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (body section not recovered), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction)): We also show that architectures which promote object-to-object communication via graph neural networks outperform less context-aware alternatives, and that fine-grained object classification is a bottleneck for language-assisted 3D obje ...

## Method Body Digest

- **p. 1 / body section not recovered - extractive body cue:** We also show that architectures which promote object-to-object communication via graph neural networks outperform less context-aware alternatives, and that fine-grained object classification is a bottleneck ...
- **p. 1 / 1 Introduction - extractive body cue:** Even in embodied AI most works (e.g., embodied QA [21], or embodied visual recognition [69]), fine-grained 3D object identification is not explicitly modeled.
- **p. 2 / 1 Introduction - extractive body cue:** Despite this, developing datasets and methods with characteristics that enable machine learning models to perform well on this 3D reference task is far from straightforward; ...
- **p. 3 / 1 Introduction - extractive body cue:** We show that training with Sr3D in addition to natural language data (Nr3D or [18]) improves neural-based pipelines.
- **p. 3 / 1 Introduction - extractive body cue:** ReferIt3DNet: We explore the task of understanding object references grounded in real-world 3D data (including both language and scenes) by designing a novel visio-linguistic graph ...
- **p. 1 / 1 Introduction - extractive body cue:** The progress on connecting language and vision in the past decade has rekindled interest in tasks like visual question answering (e.g., [12,54]), image captioning (e.g., ...
- **p. 3 / 1 Introduction - extractive body cue:** As we show in our experiments, this step is critical for progress in 3D visual object identification from free-form language descriptions.
- **p. 2 / 1 Introduction - extractive body cue:** Solving such a reference problem directly in 3D space - i.e., without a camera view dependency - can benefit many downstream robotics applications, including embodied ...

## Design Rationale

- **p. 3 / 1 Introduction - extractive body cue:** For Sr3D we propose a simple but effective methodology for building template-based and spatially-oriented object referential language in 3D scenes.
- **p. 3 / 1 Introduction - extractive body cue:** Fine-Grained ReferIt3D task: We introduce the task of language-based identification of specific 3D object instances, where fine-grained object-centric and multi-object understanding is necessary for its ...
- **p. 2 / 1 Introduction - extractive body cue:** This flexibility enables us also to bypass camera view dependency (e.g., having access to parts of a scene occluded by a fixed camera) when we ...

## Source Evidence Cues

- **p. 1 / body section not recovered - extractive body cue:** We also show that architectures which promote object-to-object communication via graph neural networks outperform less context-aware alternatives, and that fine-grained object classification is a bottleneck ...
- **p. 1 / 1 Introduction - extractive body cue:** Even in embodied AI most works (e.g., embodied QA [21], or embodied visual recognition [69]), fine-grained 3D object identification is not explicitly modeled.
- **p. 2 / 1 Introduction - extractive body cue:** Despite this, developing datasets and methods with characteristics that enable machine learning models to perform well on this 3D reference task is far from straightforward; ...
- **p. 3 / 1 Introduction - extractive body cue:** We show that training with Sr3D in addition to natural language data (Nr3D or [18]) improves neural-based pipelines.
- **p. 3 / 1 Introduction - extractive body cue:** ReferIt3DNet: We explore the task of understanding object references grounded in real-world 3D data (including both language and scenes) by designing a novel visio-linguistic graph ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | We also show that architectures which promote object-to-object communication via graph neural networks outperform less context-aware alternatives, and that fine-grained object classification ... | p. 1 (body section not recovered), p. 1 (1 Introduction) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Even in embodied AI most works (e.g., embodied QA [21], or embodied visual recognition [69]), fine-grained 3D object identification is not explicitly ... | p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Despite this, developing datasets and methods with characteristics that enable machine learning models to perform well on this 3D reference task is ... | p. 2 (1 Introduction), p. 3 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / 1 Introduction - extractive body cue:** The progress on connecting language and vision in the past decade has rekindled interest in tasks like visual question answering (e.g., [12,54]), image captioning (e.g., ...
- **p. 3 / 1 Introduction - extractive body cue:** As we show in our experiments, this step is critical for progress in 3D visual object identification from free-form language descriptions.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Solving, reference, problem, directly, space, without, camera, view, dependency, benefit, many, downstream, robotics, applications | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Solving, reference, problem, directly, space, without, camera, view, dependency, benefit | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Sr3D, simple, effective, methodology, building, template-based, spatially-oriented, object, referential, language | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | progress, connecting, language, vision, past, decade, rekindled, interest, tasks, like | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive body cue:** Solving such a reference problem directly in 3D space - i.e., without a camera view dependency - can benefit many downstream robotics applications, including embodied ...
- **p. 1 / 1 Introduction - extractive body cue:** However, most of these works focus on developing better models that connect vision to language in images, which express after all only a 2D view ...
- **p. 1 / 1 Introduction - extractive body cue:** Recent works have enhanced the accessibility of visual content through language via grounding (e.g., [49,48]), showing strong results in locating linguistically described visual elements in ...
- **p. 3 / 1 Introduction - extractive body cue:** For Sr3D we propose a simple but effective methodology for building template-based and spatially-oriented object referential language in 3D scenes.
- **p. 2 / 1 Introduction - extractive body cue:** An alternative, yet more direct way to gain this understanding is by analyzing point cloud data of real-world scenes [3,52].
- **p. 3 / 1 Introduction - extractive body cue:** We show that training with Sr3D in addition to natural language data (Nr3D or [18]) improves neural-based pipelines.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | As we show in our experiments, this step is critical for progress in 3D visual object identification from free-form language descriptions. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | It applies to distance on the horizontal placement of the objects. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 1 Introduction - extractive body cue:** We show that training with Sr3D in addition to natural language data (Nr3D or [18]) improves neural-based pipelines.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** architectures, promote, object-to-object, communication, graph, neural, networks, outperform, less, context-aware, alternatives, fine-grained, object, classification, bottleneck, language-assisted, identification, Even, embodied, most.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | This demonstrates the contribution of adding a synthetically generated dataset to a human one. | p. 13 (VI SD), p. 13 (VI SD) |
| Semantic / temporal fusion | Decoupled approach: This is a baseline listener consisting of a text classifier and an (FG) object classifier that are trained separately. | p. 11 (VI SD), p. 11 (VI SD) |
| Robot query / planning handoff | Table 2. ReferIt3DNet performance on Nr3D with/out Sr3D. The first row contains the achieved accuracy on the Nr3D testing data for a ... | p. 12 (Figure/Table caption), p. 12 (VI SD) |

## Failure and Ablation Link

- **p. 12 / VI SD - extractive body cue:** The first row contains the achieved accuracy on the Nr3D testing data for a listener trained solely with the Nr3D training set; the other rows ...
- **p. 12 / VI SD - extractive body cue:** Vision + Language + Graph (structured) Context (ReferIt3DNet): This is our proposed listener and comes in three variants that differ w.r.t. where we fuse the ...
- **p. 14 / 6 Conclusion - extractive body cue:** Success cases are in the top four images and Failure in the bottom two.
- **p. 13 / VI SD - extractive body cue:** Finally, the last row shows two challenging failure cases of our model.
- **p. 13 / VI SD - extractive body cue:** This does not come as a surprise, since the network has naturally more work to do to comprehend nuances related to viewing the scene w.r.t. ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (body section not recovered), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), objective p. 1 (1 Introduction), p. 3 (1 Introduction), temporal p. 3 (1 Introduction), p. 6 (2 Related Work), p. 6 (2 Related Work), p. 7 (2 Related Work), p. 8 (2 Related Work), p. 9 (2 Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
