# Method - SG-PGM: Partial Graph Matching Network with Semantic Geometric Fusion for 3D Scene Graph Alignment and Its Downstream Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Xie_SG-PGM_Partial_Graph_Matching_Network_with_Semantic_Geometric_Fusion_for_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Xie_SG-PGM_Partial_Graph_Matching_Network_with_Semantic_Geometric_Fusion_for_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.1. Scene Graph Matching Network), p. 3 (3.1. Scene Graph Matching Network), p. 4 (3.3. Super-point Matching Rescoring), p. 3 (3.1. Scene Graph Matching Network), p. 5 (3.5. Revisiting the Downstream Tasks), p. 5 (3.4. Loss Functions)): To explicitly enable partial matching, we employ the pipeline introduced in [44]: the Soft-topK algorithm first flattens ˜S and selects the K most likely matched candidates, where K is learned ...

## Method Body Digest

- **p. 4 / 3.1. Scene Graph Matching Network - extractive PDF cue:** To explicitly enable partial matching, we employ the pipeline introduced in [44]: the Soft-topK algorithm first flattens ˜S and selects the K most likely matched ...
- **p. 3 / 3.1. Scene Graph Matching Network - extractive PDF cue:** As illustrated in 2a, our matching network first projects the semantic node features X and semantic edge features E of the source and reference graphs ...
- **p. 4 / 3.3. Super-point Matching Rescoring - extractive PDF cue:** Feature-based point cloud registration methods like GeoTransformer [31] first compare the similarity of points or super-points, to determine the potential point-wise correspondence.
- **p. 3 / 3.1. Scene Graph Matching Network - extractive PDF cue:** It consists of a finite set of object nodes V = {v1, v2, ..., vM}, an adjacency matrix A ∈{0, 1}M×M, a node feature matrix ...
- **p. 5 / 3.5. Revisiting the Downstream Tasks - extractive PDF cue:** Then feature-based point cloud registration is used to search point-wise correspondence traverse through all matched object pairs.
- **p. 5 / 3.4. Loss Functions - extractive PDF cue:** (5) We compute the ground truth graph similarity k with k = ∥S∥/ min(/Mref/ , /Msrc/) and use Mean Square Error (MSE) loss to supervise ...
- **p. 3 / 3.1. Scene Graph Matching Network - extractive PDF cue:** We follow [11, 18, 22] to further relax the constraint from the Quadratic Assignment Problem to the Linear Assignment Problem, and define the objective function ...
- **p. 3 / 3.1. Scene Graph Matching Network - extractive PDF cue:** Instead of posing the problem as a graph isomorphism search, we formulate the inexact graph matching as optimizing the following objective function: arg max S ...

## Design Rationale

- **p. 3 / 3.1. Scene Graph Matching Network - extractive PDF cue:** It consists of a finite set of object nodes V = {v1, v2, ..., vM}, an adjacency matrix A ∈{0, 1}M×M, a node feature matrix ...
- **p. 4 / 3.2. Point to Scene Graph Feature Fusion - extractive PDF cue:** In that case, the subgraph that only consists of these nodes is automorphism.
- **p. 4 / 3.3. Super-point Matching Rescoring - extractive PDF cue:** We propose the Super-point Matching Rescoring method that uses the semantic similarity learned by our scene graph 28404

## Source Evidence Cues

- **p. 4 / 3.1. Scene Graph Matching Network - extractive PDF cue:** To explicitly enable partial matching, we employ the pipeline introduced in [44]: the Soft-topK algorithm first flattens ˜S and selects the K most likely matched ...
- **p. 3 / 3.1. Scene Graph Matching Network - extractive PDF cue:** As illustrated in 2a, our matching network first projects the semantic node features X and semantic edge features E of the source and reference graphs ...
- **p. 4 / 3.3. Super-point Matching Rescoring - extractive PDF cue:** Feature-based point cloud registration methods like GeoTransformer [31] first compare the similarity of points or super-points, to determine the potential point-wise correspondence.
- **p. 3 / 3.1. Scene Graph Matching Network - extractive PDF cue:** It consists of a finite set of object nodes V = {v1, v2, ..., vM}, an adjacency matrix A ∈{0, 1}M×M, a node feature matrix ...
- **p. 5 / 3.5. Revisiting the Downstream Tasks - extractive PDF cue:** Then feature-based point cloud registration is used to search point-wise correspondence traverse through all matched object pairs.
- **p. 5 / 3.4. Loss Functions - extractive PDF cue:** (5) We compute the ground truth graph similarity k with k = ∥S∥/ min(/Mref/ , /Msrc/) and use Mean Square Error (MSE) loss to supervise ...
- **Detected method headings:** 3. The Superpoint Matching Rescoring method for guiding (p. 2); 3. Approach (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | To explicitly enable partial matching, we employ the pipeline introduced in [44]: the Soft-topK algorithm first flattens ˜S and selects the K ... | p. 4 (3.1. Scene Graph Matching Network), p. 3 (3.1. Scene Graph Matching Network) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | As illustrated in 2a, our matching network first projects the semantic node features X and semantic edge features E of the source ... | p. 3 (3.1. Scene Graph Matching Network), p. 4 (3.3. Super-point Matching Rescoring) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | Feature-based point cloud registration methods like GeoTransformer [31] first compare the similarity of points or super-points, to determine the potential point-wise correspondence. | p. 4 (3.3. Super-point Matching Rescoring), p. 3 (3.1. Scene Graph Matching Network) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.1. Scene Graph Matching Network - extractive PDF cue:** We follow [11, 18, 22] to further relax the constraint from the Quadratic Assignment Problem to the Linear Assignment Problem, and define the objective function ...
- **p. 3 / 3.1. Scene Graph Matching Network - extractive PDF cue:** Instead of posing the problem as a graph isomorphism search, we formulate the inexact graph matching as optimizing the following objective function: arg max S ...
- **p. 5 / 3.4. Loss Functions - extractive PDF cue:** We utilize the Negative Cross-Entropy (NCE) loss in its sparse form to supervise the soft correspondence prediction of scene graph matching.
- **p. 5 / 3.4. Loss Functions - extractive PDF cue:** Having ∥S∥as the number of nonzero elements of S, the scene graph matching loss per sample Ls is defined as: Ls = 1 ∥S∥ {S(i,j)̸=0} ...
- **p. 4 / 3.1. Scene Graph Matching Network - extractive PDF cue:** In the alignment and registration stage (shown in Figure 2b), fused embedding of the source and reference graph is taken by the AIS [13] module ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 3 (3.1. Scene Graph Matching Network), p. 3 (3.1. Scene Graph Matching Network), p. 5 (3.4. Loss Functions), p. 5 (3.4. Loss Functions), p. 4 (3.2. Point to Scene Graph Feature Fusion), p. 4 (3.2. Point to Scene Graph Feature Fusion).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Sarkar, neural, network, learns, joint, multi-modal, embedding, encoded, semantic, geometric, structural, information, node, entity | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Sarkar, neural, network, learns, joint, multi-modal, embedding, encoded, semantic, geometric | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | consists, finite, object, nodes, adjacency, matrix, node, feature, edge, case | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | follow, further, relax, constraint, Quadratic, Assignment, Problem, Linear, define, objective | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1. Introduction - extractive PDF cue:** In this work, Sarkar et al. proposed a neural network that learns a joint multi-modal embedding encoded with semantic, geometric, and structural information for each ...
- **p. 3 / 3.1. Scene Graph Matching Network - extractive PDF cue:** The 3D scene graph may contain noise due to the imperfect output of graph estimation method [41, 46, 47, 54] and the dynamical scene changes ...
- **p. 4 / 3.1. Scene Graph Matching Network - extractive PDF cue:** Thus, the scene graph encoder outputs multi-layers node embedding FS ∈RM×ds with ds = d(n + 1), as shown in Figure 3.
- **p. 3 / 3.1. Scene Graph Matching Network - extractive PDF cue:** Additionally, each 3D points of the corresponded point cloud P =  pi ∈R3 / i = 1, ..., N
- **p. 4 / 3.3. Super-point Matching Rescoring - extractive PDF cue:** Feature-based point cloud registration methods like GeoTransformer [31] first compare the similarity of points or super-points, to determine the potential point-wise correspondence.
- **p. 5 / 3.5. Revisiting the Downstream Tasks - extractive PDF cue:** Recent point cloud registration methods [31, 51] successfully encode long-range geometric context with Transformer [39].
- **p. 5 / 3.5. Revisiting the Downstream Tasks - extractive PDF cue:** In SGAligner, the source and reference point clouds are divided into matched object pairs using the estimated graph alignment.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Acknowledgement: The research leading to these results has been partially funded by the German Ministry of Education and Research (BMBF) under Grant ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | The alignment between 3D scene graphs is the first step of many downstream tasks such as scene graph aided point cloud registration, ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** explicitly, enable, partial, matching, employ, pipeline, introduced, Soft-topK, algorithm, first, flattens, selects, most, likely, matched, candidates, where, learned, Attention-fused, Aggregation.
- **Relevant PDF headings:** 3. The Superpoint Matching Rescoring method for guiding (p. 2); 3. Approach (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | For alignment and registration tasks, we follow the data prepossessing method in [34] and generate 15,277 training samples and 1,882 validation samples ... | p. 6 (4. Experiments), p. 7 (4.3. Aligning 3D Scenes with Changes) |
| Global / local decision | For ablation study, we incrementally add our proposed modules to our baseline B graph matching network: (1) B+P as adding P2SG Fusion, ... | p. 6 (4. Experiments), p. 7 (4.2. Point Cloud Registration and Mosaicking) |
| Motion execution / recovery | As shown in Table 1, adding the proposed P2SG Fusion to the baseline significantly improves the node alignment accuracy and is already ... | p. 6 (4.1. Scene Graph Alignment and Overlap Checking), p. 7 (4.2. Point Cloud Registration and Mosaicking) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4. 3D point cloud registration per overlap. Random transformation is augmented to the scene fragments. Comparison against GCNet [56] is in Appendix Table 13. ...
- **p. 7 / 4.2. Point Cloud Registration and Mosaicking - extractive PDF cue:** In this section, we use the scene graph alignment result from SGAligner and our method's variants as priors, to support pretrained GeoTransformer [31] for point ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Evaluation on node matching. We evaluate the scene graph node alignment of our method's different variants and compare it with SGAligner. All metrics ...
- **p. 6 / 4. Experiments - extractive PDF cue:** 4.2) and provide an ablation study (Sec.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** Ablation study on different registration strategies.
- **p. 8 / 4.3. Aligning 3D Scenes with Changes - extractive PDF cue:** Registration results with and without Superpoint Matching Rescoring of low overlapping scene fragments.
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 5. Long-range cross-object geometric feature is gathered in registration method [31] with transformer. Points in red circles are difficult to match without taking nearby ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.1. Scene Graph Matching Network), p. 3 (3.1. Scene Graph Matching Network), p. 4 (3.3. Super-point Matching Rescoring), p. 3 (3.1. Scene Graph Matching Network), p. 5 (3.5. Revisiting the Downstream Tasks), p. 5 (3.4. Loss Functions), objective p. 3 (3.1. Scene Graph Matching Network), p. 3 (3.1. Scene Graph Matching Network), p. 5 (3.4. Loss Functions), p. 5 (3.4. Loss Functions), p. 4 (3.1. Scene Graph Matching Network), temporal p. 8 (5. Conclusion), p. 1 (Abstract), p. 2 (2. Related Work), p. 2 (2. Related Work), p. 5 (3.5. Revisiting the Downstream Tasks).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
