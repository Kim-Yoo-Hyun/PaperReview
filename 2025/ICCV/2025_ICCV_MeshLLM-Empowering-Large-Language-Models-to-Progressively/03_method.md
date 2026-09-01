# Method - MeshLLM: Empowering Large Language Models to Progressively Understand and Generate 3D Mesh

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Fang_MeshLLM_Empowering_Large_Language_Models_to_Progressively_Understand_and_Generate_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Fang_MeshLLM_Empowering_Large_Language_Models_to_Progressively_Understand_and_Generate_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. Primitive-Mesh), p. 4 (3.3. Training Task Design), p. 5 (3.4. SFT Data Curation), p. 3 (3. Method), p. 3 (3.2. Primitive-Mesh), p. 5 (3.4. SFT Data Curation)): Example of the constructed SFT data for training LLM. then apply farthest point sampling (FPS) and KNN to identify central points and point clusters, thereby partitioning the mesh into multiple ...

## Method Body Digest

- **p. 4 / 3.2. Primitive-Mesh - extractive PDF cue:** Example of the constructed SFT data for training LLM. then apply farthest point sampling (FPS) and KNN to identify central points and point clusters, thereby ...
- **p. 4 / 3.3. Training Task Design - extractive PDF cue:** Given a set of vertex coordinates V and its corresponding faces F, the LLM is optimized according to the following objective: max θ P(F / ...
- **p. 5 / 3.4. SFT Data Curation - extractive PDF cue:** It employs high-quality input-output data pairs with standard language modeling objectives to fine-tune LLMs, thereby better adapting LLM to 3D tasks.
- **p. 3 / 3. Method - extractive PDF cue:** Similar to LLaMA-Mesh [64], we adopt the OBJ-format as the fundamental representation for a mesh.
- **p. 3 / 3.2. Primitive-Mesh - extractive PDF cue:** This design is motivated by the observation that LLMs benefit from truncated local text in natural language tasks.
- **p. 5 / 3.4. SFT Data Curation - extractive PDF cue:** 5, we construct various forms of SFT data encompassing the aforementioned four training tasks.
- **p. 4 / 3.3. Training Task Design - extractive PDF cue:** (4) This task captures the geometric relationships between local Primitive-Mesh units, mitigating the loss of 3D spatial information inherent in textual serialization, thereby improving the ...
- **p. 5 / 3.3. Training Task Design - extractive PDF cue:** Given a mesh M and its textual description T , the following learning objective is constructed: max θ P(T / M, θ).

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** The main contributions of our work are as follows: • We introduce a mesh decomposition strategy to create 1500k+ Primitive-Meshes, expanding the scale of the ...
- **p. 3 / 3. Method - extractive PDF cue:** Next, we introduce the concept of Primitive-Mesh.
- **p. 3 / 3. Method - extractive PDF cue:** The set of faces F = {fj}Nf j=1 consists of Nf triangular face elements defined by three vertex indices.

## Source Evidence Cues

- **p. 4 / 3.2. Primitive-Mesh - extractive PDF cue:** Example of the constructed SFT data for training LLM. then apply farthest point sampling (FPS) and KNN to identify central points and point clusters, thereby ...
- **p. 4 / 3.3. Training Task Design - extractive PDF cue:** Given a set of vertex coordinates V and its corresponding faces F, the LLM is optimized according to the following objective: max θ P(F / ...
- **p. 5 / 3.4. SFT Data Curation - extractive PDF cue:** It employs high-quality input-output data pairs with standard language modeling objectives to fine-tune LLMs, thereby better adapting LLM to 3D tasks.
- **p. 3 / 3. Method - extractive PDF cue:** Similar to LLaMA-Mesh [64], we adopt the OBJ-format as the fundamental representation for a mesh.
- **p. 3 / 3.2. Primitive-Mesh - extractive PDF cue:** This design is motivated by the observation that LLMs benefit from truncated local text in natural language tasks.
- **p. 5 / 3.4. SFT Data Curation - extractive PDF cue:** 5, we construct various forms of SFT data encompassing the aforementioned four training tasks.
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Example of the constructed SFT data for training LLM. then apply farthest point sampling (FPS) and KNN to identify central points and ... | p. 4 (3.2. Primitive-Mesh), p. 4 (3.3. Training Task Design) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Given a set of vertex coordinates V and its corresponding faces F, the LLM is optimized according to the following objective: max ... | p. 4 (3.3. Training Task Design), p. 5 (3.4. SFT Data Curation) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | It employs high-quality input-output data pairs with standard language modeling objectives to fine-tune LLMs, thereby better adapting LLM to 3D tasks. | p. 5 (3.4. SFT Data Curation), p. 3 (3. Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.3. Training Task Design - extractive PDF cue:** Given a set of vertex coordinates V and its corresponding faces F, the LLM is optimized according to the following objective: max θ P(F / ...
- **p. 4 / 3.3. Training Task Design - extractive PDF cue:** (4) This task captures the geometric relationships between local Primitive-Mesh units, mitigating the loss of 3D spatial information inherent in textual serialization, thereby improving the ...
- **p. 5 / 3.3. Training Task Design - extractive PDF cue:** Given a mesh M and its textual description T , the following learning objective is constructed: max θ P(T / M, θ).
- **p. 5 / 3.4. SFT Data Curation - extractive PDF cue:** It employs high-quality input-output data pairs with standard language modeling objectives to fine-tune LLMs, thereby better adapting LLM to 3D tasks.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3.3. Training Task Design), p. 5 (3.3. Training Task Design), p. 4 (3.3. Training Task Design), p. 5 (3.4. SFT Data Curation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Large, Language, Model, output, input, mesh, understanding, generation, pretrain, clustered, primitive-mesh, semantic, muscular, humanoid | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Large, Language, Model, output, input, mesh, understanding, generation, pretrain, clustered | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | main, contributions, follows, introduce, mesh, decomposition, strategy, create, Primitive-Meshes, expanding | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Given, vertex, coordinates, corresponding, faces, LLM, optimized, according, following, objective | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. Primitive-Mesh - extractive PDF cue:** Large Language Model output input mesh understanding mesh generation (1) pretrain on clustered primitive-mesh (2) pretrain on semantic primitive-mesh a muscular humanoid character with armored ...
- **p. 5 / 3.4. SFT Data Curation - extractive PDF cue:** It employs high-quality input-output data pairs with standard language modeling objectives to fine-tune LLMs, thereby better adapting LLM to 3D tasks.
- **p. 3 / 3.2. Primitive-Mesh - extractive PDF cue:** This design is motivated by the observation that LLMs benefit from truncated local text in natural language tasks.
- **p. 1 / 1. Introduction - extractive PDF cue:** These methods typically rely on pretrained 3D encoders to map 3D structures into discrete token sequences before inputting them into LLMs for reasoning and questionanswering ...
- **p. 1 / 1. Introduction - extractive PDF cue:** With the rapid development of virtual reality and robotic interaction, equipping LLMs with 3D perception and spatial reasoning capabilities has become a pressing challenge.
- **p. 2 / 1. Introduction - extractive PDF cue:** This approach is based on two key observations.
- **p. 3 / 3.2. Primitive-Mesh - extractive PDF cue:** 3, we construct Primitive-Mesh using two strategies: 1) KNN-Based: Given a mesh M, we begin by densely sampling point clouds from the mesh and 14063
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We first describe the process of converting 3D mesh data into a textual sequence compatible with LLMs. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | 2) Sorting: Employing a sorting strategy akin to PolyGen [49], we assign a unique sequence to each mesh. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We train for 2 epochs on the KNN-based Primitive-Mesh dataset, 3 epochs on the se14065 | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.2. Primitive-Mesh - extractive PDF cue:** Example of the constructed SFT data for training LLM. then apply farthest point sampling (FPS) and KNN to identify central points and point clusters, thereby ...
- **p. 5 / 3.4. SFT Data Curation - extractive PDF cue:** It employs high-quality input-output data pairs with standard language modeling objectives to fine-tune LLMs, thereby better adapting LLM to 3D tasks.
- **p. 5 / 3.4. SFT Data Curation - extractive PDF cue:** 5, we construct various forms of SFT data encompassing the aforementioned four training tasks.
- **p. 5 / 4.1. Implementation Details - extractive PDF cue:** We train for 2 epochs on the KNN-based Primitive-Mesh dataset, 3 epochs on the se14065
- **p. 6 / 4.2. Dialogue Ability - extractive PDF cue:** In particular, the constructed data sets and training pipeline are fully compatible with any existing LLM without necessitating additional complex encoder-decoder designs.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Example, constructed, SFT, data, training, LLM, then, apply, farthest, point, sampling, FPS, KNN, identify, central, points, clusters, thereby, partitioning, mesh.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We follow dataset split configurations from previous works [8, 49], extracting 10% of the 4 subsets (chair, table, bench, lamp) from ShapeNet ... | p. 5 (4.1. Implementation Details), p. 5 (4.1. Implementation Details) |
| Semantic / temporal fusion | We further compare it with state-of-the-art methods in Fig. | p. 6 (4.3. Performance Evaluation), p. 6 (4.1. Implementation Details) |
| Robot query / planning handoff | 1, reveal that our method surpasses LLaMA-Mesh on multiple metrics and achieves a performance comparable to that of MeshXL, thereby validating the ... | p. 7 (4.3. Performance Evaluation), p. 7 (4.3. Performance Evaluation) |

## Failure and Ablation Link

- **p. 6 / 4.2. Dialogue Ability - extractive PDF cue:** In particular, the constructed data sets and training pipeline are fully compatible with any existing LLM without necessitating additional complex encoder-decoder designs.
- **p. 8 / 4.3. Performance Evaluation - extractive PDF cue:** Ablation studies of MeshLLM. "PM" denotes PrimitiveMesh.
- **p. 8 / 4.4. Ablation Studies - extractive PDF cue:** We conduct a series of ablation experiments, the results of which are summarized in Tab.
- **p. 8 / 5. Limitation and Future Work - extractive PDF cue:** While MeshLLM shows the potential of LLMs for 3D mesh understanding and generation, certain limitations remain, highlighting future research areas: 1) The scale of available ...
- **p. 8 / 6. Conclusions - extractive PDF cue:** In this paper, we propose MeshLLM, a novel approach that rethinks the paradigm of generating text-serialized meshes using Large Language Models, which addresses two key ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.2. Primitive-Mesh), p. 4 (3.3. Training Task Design), p. 5 (3.4. SFT Data Curation), p. 3 (3. Method), p. 3 (3.2. Primitive-Mesh), p. 5 (3.4. SFT Data Curation), objective p. 4 (3.3. Training Task Design), p. 4 (3.3. Training Task Design), p. 5 (3.3. Training Task Design), p. 5 (3.4. SFT Data Curation), temporal p. 3 (3. Method), p. 3 (3. Method), p. 4 (3.2. Primitive-Mesh), p. 4 (3.2. Primitive-Mesh), p. 8 (4.4. Ablation Studies), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
