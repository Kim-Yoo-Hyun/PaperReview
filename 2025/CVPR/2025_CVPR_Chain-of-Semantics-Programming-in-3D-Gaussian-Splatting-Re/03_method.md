# Method - Chain of Semantics Programming in 3D Gaussian Splatting Representation for 3D Vision Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Shi_Chain_of_Semantics_Programming_in_3D_Gaussian_Splatting_Representation_for_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Shi_Chain_of_Semantics_Programming_in_3D_Gaussian_Splatting_Representation_for_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. Dynamic Interaction in 3DGS Representation), p. 4 (3.3. Chain of Semantics Programming), p. 3 (3. Methodology), p. 5 (3.4. Grounded-aware Self-Check Mechanism), p. 3 (3.1. Utterance Semantics Parsing)): Then, based on the given utterance and the 3D scene, use the LLM to explore the 3DGS representation, identify a suitable viewpoint for observation, and render the corresponding 2D image ...

## Method Body Digest

- **p. 4 / 3.2. Dynamic Interaction in 3DGS Representation - extractive PDF cue:** Then, based on the given utterance and the 3D scene, use the LLM to explore the 3DGS representation, identify a suitable viewpoint for observation, and ...
- **p. 4 / 3.3. Chain of Semantics Programming - extractive PDF cue:** We use the chain of semantics to guide the process of programming: \ mathcal {L }_p=\ text {programmer} \xleftarrow {\text {guide}} \mathcal {C}(\mathcal {U}) (11) ...
- **p. 3 / 3. Methodology - extractive PDF cue:** We then reconstruct the 3D scene using the 3DGS representation to enable exploration in 3D worlds and render free-viewing 2D images, as shown in Figure ...
- **p. 5 / 3.4. Grounded-aware Self-Check Mechanism - extractive PDF cue:** To address this, we assess and validate the execution results by re-evaluating the grounding outputs. \m a thcal {I}^{\text {err}} = \text {aware}(target) (14) here, ...
- **p. 3 / 3.1. Utterance Semantics Parsing - extractive PDF cue:** The function utterance parser(·) is a LLM module.
- **p. 5 / 3.4. Grounded-aware Self-Check Mechanism - extractive PDF cue:** For instance, if the user intends to locate a single object but two are returned, or if the execution yields no results (e.g., no object ...
- **p. 2 / 1. Introduction - extractive PDF cue:** This method constructs a relationship graph and facilitates a chain of semantics programming, enabling multi-step object grounding. • We first use 3DGS to reconstruct the ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Furthermore, the quality of 2D images derived from point clouds is frequently low or incomplete, hindering the extraction of clean, fine-grained semantics in diverse scenes ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Our contributions are summarized as follows: • We propose a chain of semantics programming method with the grounded-aware self-check mechanism for enhanced grounded reasoning in ...
- **p. 2 / 1. Introduction - extractive PDF cue:** This method constructs a relationship graph and facilitates a chain of semantics programming, enabling multi-step object grounding. • We first use 3DGS to reconstruct the ...
- **p. 3 / 3. Methodology - extractive PDF cue:** In this section, we introduce our proposed zero-shot neurosymbolic framework that employs a LLM as a neurosymbolic function for object grounding.

## Source Evidence Cues

- **p. 4 / 3.2. Dynamic Interaction in 3DGS Representation - extractive PDF cue:** Then, based on the given utterance and the 3D scene, use the LLM to explore the 3DGS representation, identify a suitable viewpoint for observation, and ...
- **p. 4 / 3.3. Chain of Semantics Programming - extractive PDF cue:** We use the chain of semantics to guide the process of programming: \ mathcal {L }_p=\ text {programmer} \xleftarrow {\text {guide}} \mathcal {C}(\mathcal {U}) (11) ...
- **p. 3 / 3. Methodology - extractive PDF cue:** We then reconstruct the 3D scene using the 3DGS representation to enable exploration in 3D worlds and render free-viewing 2D images, as shown in Figure ...
- **p. 5 / 3.4. Grounded-aware Self-Check Mechanism - extractive PDF cue:** To address this, we assess and validate the execution results by re-evaluating the grounding outputs. \m a thcal {I}^{\text {err}} = \text {aware}(target) (14) here, ...
- **p. 3 / 3.1. Utterance Semantics Parsing - extractive PDF cue:** The function utterance parser(·) is a LLM module.
- **Detected method headings:** 3. Methodology (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Then, based on the given utterance and the 3D scene, use the LLM to explore the 3DGS representation, identify a suitable viewpoint ... | p. 4 (3.2. Dynamic Interaction in 3DGS Representation), p. 4 (3.3. Chain of Semantics Programming) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | We use the chain of semantics to guide the process of programming: \ mathcal {L }_p=\ text {programmer} \xleftarrow {\text {guide}} \mathcal ... | p. 4 (3.3. Chain of Semantics Programming), p. 3 (3. Methodology) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | We then reconstruct the 3D scene using the 3DGS representation to enable exploration in 3D worlds and render free-viewing 2D images, as ... | p. 3 (3. Methodology), p. 5 (3.4. Grounded-aware Self-Check Mechanism) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.4. Grounded-aware Self-Check Mechanism - extractive PDF cue:** For instance, if the user intends to locate a single object but two are returned, or if the execution yields no results (e.g., no object ...
- **p. 5 / 3.4. Grounded-aware Self-Check Mechanism - extractive PDF cue:** To address this, we assess and validate the execution results by re-evaluating the grounding outputs. \m a thcal {I}^{\text {err}} = \text {aware}(target) (14) here, ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3.2. Dynamic Interaction in 3DGS Representation), p. 4 (3.2. Dynamic Interaction in 3DGS Representation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | constructs, relationship, graph, facilitates, chain, semantics, programming, enabling, multi-step, object, grounding, first, DGS, reconstruct | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | constructs, relationship, graph, facilitates, chain, semantics, programming, enabling, multi-step, object | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, summarized, follows, chain, semantics, programming, grounded-aware, self-check, mechanism, enhanced | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | instance, user, intends, locate, single, object, returned, execution, yields, located | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive PDF cue:** This method constructs a relationship graph and facilitates a chain of semantics programming, enabling multi-step object grounding. • We first use 3DGS to reconstruct the ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Furthermore, the quality of 2D images derived from point clouds is frequently low or incomplete, hindering the extraction of clean, fine-grained semantics in diverse scenes ...
- **p. 4 / 3.2. Dynamic Interaction in 3DGS Representation - extractive PDF cue:** Then, based on the given utterance and the 3D scene, use the LLM to explore the 3DGS representation, identify a suitable viewpoint for observation, and ...
- **p. 3 / 3.2. Dynamic Interaction in 3DGS Representation - extractive PDF cue:** For given 3D point cloud Opc, 2D image frame Oimg i , and the pose of each 2D image frame Opose i = (Ri/Ti).
- **p. 1 / 1. Introduction - extractive PDF cue:** Our proposed zero-shot framework enables interaction and retrieval within a 3D Gaussian Splatting representation to obtain fine-grained semantics and supports multi-step spatial reasoning.
- **p. 5 / 3.4. Grounded-aware Self-Check Mechanism - extractive PDF cue:** To address this, we assess and validate the execution results by re-evaluating the grounding outputs. \m a thcal {I}^{\text {err}} = \text {aware}(target) (14) here, ...
- **p. 4 / 3.2. Dynamic Interaction in 3DGS Representation - extractive PDF cue:** Target ID Executor Self-Check Interact & Retrieval (c) Chain of Semantics Programming w. grounded-aware self-check (b) 3D Scene Reconstruction Camera Poses 2D Frames Densify & ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Through the chain of semantics programming, our framework can explicitly account for the conditionality of relationships and connections among multiple relationships, utilizing ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Our proposed zero-shot framework enables interaction and retrieval within a 3D Gaussian Splatting representation to obtain fine-grained semantics and supports multi-step spatial ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Then, given, utterance, scene, LLM, explore, DGS, representation, identify, suitable, viewpoint, observation, render, corresponding, image, additional, semantic, information, chain, semantics.
- **Relevant PDF headings:** 3. Methodology (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Sr3D comprises 83.5K template-based utterances that leverage spatial relationships among fine-grained object classes to localize a referred object in a scene, and ... | p. 5 (4.1. Datasets), p. 7 (4.4. Ablation study) |
| Semantic / temporal fusion | With limited train data for the supervised models, our zero-shot method outperforms all compared models in both two datasets, as shown in ... | p. 5 (4.3. Comparison to Prior Works), p. 5 (4.3. Comparison to Prior Works) |
| Robot query / planning handoff | This mechanism achieves improvements of 4.5% on Nr3D and 1.8% on Sr3D. | p. 7 (4.4. Ablation study), p. 5 (4.3. Comparison to Prior Works) |

## Failure and Ablation Link

- **p. 6 / 4.4. Ablation study - extractive PDF cue:** The object grounding accuracy results from the ablation study of Nr3D and Sr3D are shown in Table 6 and Table 7, respectively.
- **p. 6 / 4.4. Ablation study - extractive PDF cue:** In this section, we conduct an ablation study on both two datasets to analyze the influence of our proposed method, containing Chain of semantics (CoS.), ...
- **p. 7 / 4.4. Ablation study - extractive PDF cue:** Without this mechanism, when errors occur during code execution, the only option is to reattempt reasoning, failing to learn from previous mistakes.
- **p. 7 / 4.4. Ablation study - extractive PDF cue:** However, in Sr3D, the view-dependent grounding accuracy decreases by 12.8% (without Chain of Semantics) and 15.6% (with Chain of Semantics) compared to dialogue.
- **p. 8 / 4.5. Qualitative results - extractive PDF cue:** We used only 3D point clouds, images, and corresponding camera parameters for the reconstruction, without utilizing depth information or 3D meshes.
- **p. 8 / 5. Conclusion - extractive PDF cue:** We show that chain of semantics programming enhances the understanding of complex spatial relationships, and the 3D Gaussian Splatting representation provides fine-grained 2D semantics, overcoming ...
- **p. 8 / 4.5. Qualitative results - extractive PDF cue:** The fifth image illustrates a failure case where dense object grounding becomes more prone to confusion, increasing the difficulty of grounding to the correct object.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.2. Dynamic Interaction in 3DGS Representation), p. 4 (3.3. Chain of Semantics Programming), p. 3 (3. Methodology), p. 5 (3.4. Grounded-aware Self-Check Mechanism), p. 3 (3.1. Utterance Semantics Parsing), objective p. 5 (3.4. Grounded-aware Self-Check Mechanism), p. 5 (3.4. Grounded-aware Self-Check Mechanism), temporal p. 5 (3.3. Chain of Semantics Programming), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Dynamic Interaction in 3DGS Representation), p. 3 (3. Methodology), p. 4 (3.3. Chain of Semantics Programming).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
