# Method - ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Liu_ReasonGrounder_LVLM-Guided_Hierarchical_Feature_Splatting_for_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_ReasonGrounder_LVLM-Guided_Hierarchical_Feature_Splatting_for_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (Method), p. 6 (Method)): To extract language features from each image, we use the OpenCLIP ViT-B/16 model.

## Method Body Digest

- **p. 6 / Method - extractive body cue:** To extract language features from each image, we use the OpenCLIP ViT-B/16 model.
- **p. 6 / Method - extractive body cue:** We then train the hierarchical feature Gaussian field by fixing all other parameters of the 3D Gaussians.
- **p. 2 / 1. Introduction - extractive body cue:** LVLM aids in interpreting complex instructions and locating objects even when partially or fully occluded. • (4) Dataset Contributions: A new ReasoningGD dataset offers over ...
- **p. 1 / 1. Introduction - extractive body cue:** For instance, simple commands like apple can be directly interpreted, while more complex instructions, such as Can you localize the red, round, sweet fruit on ...
- **p. 2 / 1. Introduction - extractive body cue:** To achieve open-vocabulary 3D visual grounding and reasoning, this paper proposes ReasonGrounder, a novel LVLM-Guided Hierarchical Feature Splatting method that enables implicit instruction comprehension and ...
- **p. 6 / Method - extractive body cue:** Our ReasonGrounder employs the same explicit queries as previous state-of-the-art approaches. is deemed successful if the pixel with the highest relevance falls within the labeled ...
- **p. 1 / 1. Introduction - extractive body cue:** As shown in Figure 1, these instructions involve locating the target object, interpreting the intent of the description, and accounting for occlusion.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we introduce a novel ReasoningGD dataset containing over 10K complex scenes and 263 object types, with a total of approximately 2 million annotations.
- **p. 2 / 1. Introduction - extractive body cue:** To achieve open-vocabulary 3D visual grounding and reasoning, this paper proposes ReasonGrounder, a novel LVLM-Guided Hierarchical Feature Splatting method that enables implicit instruction comprehension and ...

## Source Evidence Cues

- **p. 6 / Method - extractive body cue:** To extract language features from each image, we use the OpenCLIP ViT-B/16 model.
- **p. 6 / Method - extractive body cue:** We then train the hierarchical feature Gaussian field by fixing all other parameters of the 3D Gaussians.
- **Detected method headings:** Method (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To extract language features from each image, we use the OpenCLIP ViT-B/16 model. | p. 6 (Method), p. 6 (Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | We then train the hierarchical feature Gaussian field by fixing all other parameters of the 3D Gaussians. | p. 6 (Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | To extract language features from each image, we use the OpenCLIP ViT-B/16 model. | p. 6 (Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | LVLM, aids, interpreting, complex, instructions, locating, objects, even, when, partially, fully, occluded, Dataset, Contributions | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | LVLM, aids, interpreting, complex, instructions, locating, objects, even, when, partially | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Furthermore, introduce, novel, ReasoningGD, dataset, containing, over, complex, scenes, object | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | not recovered | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** LVLM aids in interpreting complex instructions and locating objects even when partially or fully occluded. • (4) Dataset Contributions: A new ReasoningGD dataset offers over ...
- **p. 1 / 1. Introduction - extractive body cue:** For instance, simple commands like apple can be directly interpreted, while more complex instructions, such as Can you localize the red, round, sweet fruit on ...
- **p. 2 / 1. Introduction - extractive body cue:** To achieve open-vocabulary 3D visual grounding and reasoning, this paper proposes ReasonGrounder, a novel LVLM-Guided Hierarchical Feature Splatting method that enables implicit instruction comprehension and ...
- **p. 6 / Method - extractive body cue:** Our ReasonGrounder employs the same explicit queries as previous state-of-the-art approaches. is deemed successful if the pixel with the highest relevance falls within the labeled ...
- **p. 6 / Method - extractive body cue:** To extract language features from each image, we use the OpenCLIP ViT-B/16 model.
- **p. 1 / 1. Introduction - extractive body cue:** As shown in Figure 1, these instructions involve locating the target object, interpreting the intent of the description, and accounting for occlusion.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | In this work, we propose ReasonGrounder, an LVLM-guided framework that uses hierarchical 3D feature Gaussian fields for adaptive grouping based on physical ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Formally, we propose the ReasonGrounder framework as illustrated in Fig. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | The compressed features { ˆϕi} remain sufficient for scene representation, and the memory overhead is significantly reduced. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / Method - extractive body cue:** We then train the hierarchical feature Gaussian field by fixing all other parameters of the 3D Gaussians.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** extract, language, features, image, OpenCLIP, ViT-B/16, model, then, train, hierarchical, feature, Gaussian, field, fixing, other, parameters, Gaussians, LVLM, aids, interpreting.
- **Relevant PDF headings:** Method (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | This paper introduces a novel dataset, ReasoningGD, which includes over 10K scenes of varying complexity and more than 263 types of common ... | p. 5 (4. Experiments), p. 7 (4.2. Evaluation on 3D Reasoning) |
| Semantic / temporal fusion | Our ReasonGrounder demonstrates superior accuracy in open-vocabulary 3D localization compared to other state-of-the-art methods. | p. 7 (4.2. Evaluation on 3D Reasoning), p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding) |
| Robot query / planning handoff | Our results show that ReasonGrounder outperforms 2D-based methods like ODISE [35] and OV-Seg [25], and significantly surpasses 3D-based methods, including Method bed ... | p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding), p. 8 (4.2. Evaluation on 3D Reasoning) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Table 7. Ablation studies. The results are presented for two dif- ferent scenes: the Figurines scene from the LERF dataset and the 001 scene from ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Mean IoU (%) on LERF for open-vocabulary 3D vi- sual grounding. Our ReasonGrounder employs the same explicit queries as previous state-of-the-art approaches. is ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Examples of open-vocabulary 3D visual grounding and reasoning. In a given scene, the user observes from a per- spective with occlusions and asks ...
- **p. 5 / 4. Experiments - extractive body cue:** The dataset features multiple object instances with varying levels of occlusion, making it ideal for evaluating the ability in open-vocabulary 3D reasoning, grounding, and amodal ...
- **p. 7 / 4.2. Evaluation on 3D Reasoning - extractive body cue:** Existing openvocabulary 3D visual grounding methods struggle with localizing complete objects in novel views with occlusion, limiting their real-world applicability.
- **p. 7 / 4.2. Evaluation on 3D Reasoning - extractive body cue:** To test robustness, we selected five challenging scenes with small proportions, including multi-hierarchical structures and similar objects, along with ten text queries per scene from ...
- **p. 8 / 4.2. Evaluation on 3D Reasoning - extractive body cue:** This highlights the robustness of our ReasonGrounder in complex situations.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (Method), p. 6 (Method), objective 본문 anchor 없음, temporal p. 1 (Abstract), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Scale-Hierarchical Feature Gaussian Field), p. 4 (3.1. Scale-Hierarchical Feature Gaussian Field).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
