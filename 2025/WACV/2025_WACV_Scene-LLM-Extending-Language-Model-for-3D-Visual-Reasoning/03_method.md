# Method - Scene-LLM: Extending Language Model for 3D Visual Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/WACV2025/html/Fu_Scene-LLM_Extending_Language_Model_for_3D_Visual_Reasoning_WACV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/WACV2025/papers/Fu_Scene-LLM_Extending_Language_Model_for_3D_Visual_Reasoning_WACV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (1. Introduction), p. 4 (4. Scene-LLM), p. 5 (4.1. 3D Visual Feature), p. 1 (Abstract), p. 4 (4.1. 3D Visual Feature), p. 5 (4.1. 3D Visual Feature)): In summary, our primary contributions are: • We introduce Scene-LLM, a 3D-VLM that connecting 3D visual information with LLM and sets new stateof-the-art on 3D-VQA and interactive planning benchmarks; • ...

## Method Body Digest

- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, our primary contributions are: • We introduce Scene-LLM, a 3D-VLM that connecting 3D visual information with LLM and sets new stateof-the-art on 3D-VQA ...
- **p. 4 / 4. Scene-LLM - extractive PDF cue:** This section outlines the 3D visual feature extraction process, model architecture, 3D visual information alignment, and the inference process.
- **p. 5 / 4.1. 3D Visual Feature - extractive PDF cue:** The scene semantic feature is then updated using: \l abe l {eq u a ti o n: u p da te} \t extbf {F}^{vox}_{t+1} = ...
- **p. 1 / Abstract - extractive PDF cue:** Notably, we use egocentric 3D frame features for feature alignment, an efficient technique that incorporates the model with fine-grained concepts.
- **p. 4 / 4.1. 3D Visual Feature - extractive PDF cue:** This involves first extracting pixel-wise CLIP features from each image and then aggregating these into a 3D point set, as inspired by ConceptFusion [27].
- **p. 5 / 4.1. 3D Visual Feature - extractive PDF cue:** To update scene features Fvox t at state t to state t + 1, we first render a 3D frame from the current camera view.
- **p. 2 / 1. Introduction - extractive PDF cue:** We used an image caption model [12] and a LLM [67] to generate conceptual and instructional following annotations.
- **p. 1 / Abstract - extractive PDF cue:** Scene-LLM adopts a unified 3D visual feature representation, that incorporates dense spatial information and supports scene state updates.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, our primary contributions are: • We introduce Scene-LLM, a 3D-VLM that connecting 3D visual information with LLM and sets new stateof-the-art on 3D-VQA ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To overcome this, we propose integrating both types of 3D visual information to an unified visual feature in Scene-LLM.
- **p. 1 / Abstract - extractive PDF cue:** Unique to our approach is the integration of both scene-level and egocentric 3D information with a compact hybrid representation.

## Source Evidence Cues

- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, our primary contributions are: • We introduce Scene-LLM, a 3D-VLM that connecting 3D visual information with LLM and sets new stateof-the-art on 3D-VQA ...
- **p. 4 / 4. Scene-LLM - extractive PDF cue:** This section outlines the 3D visual feature extraction process, model architecture, 3D visual information alignment, and the inference process.
- **p. 5 / 4.1. 3D Visual Feature - extractive PDF cue:** The scene semantic feature is then updated using: \l abe l {eq u a ti o n: u p da te} \t extbf {F}^{vox}_{t+1} = ...
- **p. 1 / Abstract - extractive PDF cue:** Notably, we use egocentric 3D frame features for feature alignment, an efficient technique that incorporates the model with fine-grained concepts.
- **p. 4 / 4.1. 3D Visual Feature - extractive PDF cue:** This involves first extracting pixel-wise CLIP features from each image and then aggregating these into a 3D point set, as inspired by ConceptFusion [27].
- **p. 5 / 4.1. 3D Visual Feature - extractive PDF cue:** To update scene features Fvox t at state t to state t + 1, we first render a 3D frame from the current camera view.
- **p. 2 / 1. Introduction - extractive PDF cue:** We used an image caption model [12] and a LLM [67] to generate conceptual and instructional following annotations.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | In summary, our primary contributions are: • We introduce Scene-LLM, a 3D-VLM that connecting 3D visual information with LLM and sets new ... | p. 2 (1. Introduction), p. 4 (4. Scene-LLM) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | This section outlines the 3D visual feature extraction process, model architecture, 3D visual information alignment, and the inference process. | p. 4 (4. Scene-LLM), p. 5 (4.1. 3D Visual Feature) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The scene semantic feature is then updated using: \l abe l {eq u a ti o n: u p da te} \t ... | p. 5 (4.1. 3D Visual Feature), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4.3. Inference - extractive PDF cue:** Then, the 3D scene feature is updated as per Equation 1.
- **p. 1 / Abstract - extractive PDF cue:** Scene-LLM adopts a unified 3D visual feature representation, that incorporates dense spatial information and supports scene state updates.
- **p. 2 / 1. Introduction - extractive PDF cue:** This method not only retains dense spatial information but also facilitates interactive updates.
- **p. 2 / 1. Introduction - extractive PDF cue:** Egocentric information is crucial for immediate updates during object interactions and for localizing the agent within the scene.
- **p. 4 / 4.1. 3D Visual Feature - extractive PDF cue:** To tokenize these 3D visual features for compatibility with LLM input, we adopt a hybrid point-voxel representation [40], balancing the need for dense 3D visual ...
- **p. 5 / 4.3. Inference - extractive PDF cue:** These updates are vital for observation collection, agent grounding, and replanning.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (4.3. Inference), p. 1 (Abstract), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (4.1. 3D Visual Feature), p. 5 (4.3. Inference).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | egocentric, step, frame, data, instruction, first, input, Scene-LLM, describe, current, state, updated, scene, feature | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | egocentric, step, frame, data, instruction, first, input, Scene-LLM, describe, current | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, primary, contributions, introduce, Scene-LLM, D-VLM, connecting, visual, information, LLM | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Then, scene, feature, updated, Equation, Scene-LLM, adopts, unified, visual, representation | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 4.3. Inference - extractive PDF cue:** At the egocentric step, 3D frame data and a egocentric instruction are first input to Scene-LLM to describe the current state.
- **p. 5 / 4.3. Inference - extractive PDF cue:** The updated scene feature, along with the state description and user instructions, are fed into Scene-LLM to yield the corresponding response.
- **p. 7 / C VoteNet+MCAN [78] - extractive PDF cue:** The notation "(s)" denotes textual inputs that include step-by-step instructions.
- **p. 4 / 3.1. Frame Data Generation - extractive PDF cue:** The data generation comprises two stages: a 3D frame-language generation stage, which uses image frames and a 2D VLM to generate frame descriptions, and a ...
- **p. 2 / 1. Introduction - extractive PDF cue:** We used an image caption model [12] and a LLM [67] to generate conceptual and instructional following annotations.
- **p. 2 / 1. Introduction - extractive PDF cue:** While previous studies have explored using patchy visual features [38] and query tokens [34] for downsampling visual features, 3D point sets pose a unique problem ...
- **p. 7 / C VoteNet+MCAN [78] - extractive PDF cue:** Scene-LLM performs the best among methods using goal instruction only.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | I saw… Knife (in the bowl on the side table) … I saw a small table … Apple … knife … bread ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Next-step: GotoLocation bowl I saw a sink … A medicine cabinet … Dishwasher … Next-step: PutObject knife, bowl I saw a flat, ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 4. Scene-LLM - extractive PDF cue:** This section outlines the 3D visual feature extraction process, model architecture, 3D visual information alignment, and the inference process.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** summary, primary, contributions, introduce, Scene-LLM, D-VLM, connecting, visual, information, LLM, sets, stateof-the-art, D-VQA, interactive, planning, benchmarks, egocentric, scene-level, represented, unified.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | This benchmark tests a model's ability to understand 3D scenes using questionanswering tasks using ScanNet dataset [14]. | p. 5 (5.1. Results and Benchmark Evaluation), p. 5 (5.1. Results and Benchmark Evaluation) |
| Semantic / temporal fusion | Our evaluation of Scene-LLM on 3D visual question answering (3D-VQA) benchmarks is summarized in Table 1 for ScanQA and Table 2 for ... | p. 6 (5.1. Results and Benchmark Evaluation), p. 8 (Figure/Table caption) |
| Robot query / planning handoff | Table 5. High-level planning accuracy(HLP) on Alfred dataset valid unseen/seen set with different inference strategy. Full model outperform strategies without egocentric and ... | p. 8 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 5 / 5. Experiments - extractive PDF cue:** We conducted ablation studies by replacing visual representation and extractor with those from other methods to demonstrate the effectiveness of our 3D visual representation, the ...
- **p. 6 / 5.1. Results and Benchmark Evaluation - extractive PDF cue:** We present results both with and without task-specific finetuning for a comprehensive anal2200
- **p. 6 / 5.1. Results and Benchmark Evaluation - extractive PDF cue:** Responses for the top 3 non-interactive scenes are generated without task-specific finetuning, and those for the bottom interactive scene are generated with finetuning.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 5. High-level planning accuracy(HLP) on Alfred dataset valid unseen/seen set with different inference strategy. Full model outperform strategies without egocentric and scene state updates. ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Ablation Studies comparing different input modalities, 3D representation, pertaining strategy, and data augmentation on ScanQA and SQA3D benchmarks. #Param reports the number of ...
- **p. 7 / 5.1. Results and Benchmark Evaluation - extractive PDF cue:** The ‘*' symbol indicates task-specific fine-tuning.
- **p. 8 / 6. Conclusion - extractive PDF cue:** Scene-LLM faces limitations such as LLM input token length, challenges in processing dynamic scenes without a state detector, lacking geometry feature, and language hallucinations.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (1. Introduction), p. 4 (4. Scene-LLM), p. 5 (4.1. 3D Visual Feature), p. 1 (Abstract), p. 4 (4.1. 3D Visual Feature), p. 5 (4.1. 3D Visual Feature), objective p. 5 (4.3. Inference), p. 1 (Abstract), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (4.1. 3D Visual Feature), p. 5 (4.3. Inference), temporal p. 6 (5.1. Results and Benchmark Evaluation), p. 6 (5.1. Results and Benchmark Evaluation), p. 5 (4.3. Inference), p. 5 (5. Experiments), p. 1 (Abstract), p. 1 (Front matter).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
