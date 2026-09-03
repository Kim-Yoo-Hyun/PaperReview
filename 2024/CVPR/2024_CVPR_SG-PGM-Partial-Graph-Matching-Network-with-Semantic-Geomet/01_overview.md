# SG-PGM: Partial Graph Matching Network with Semantic Geometric Fusion for 3D Scene Graph Alignment and Its Downstream Tasks

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Xie_SG-PGM_Partial_Graph_Matching_Network_with_Semantic_Geometric_Fusion_for_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Xie_SG-PGM_Partial_Graph_Matching_Network_with_Semantic_Geometric_Fusion_for_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: sensor fusion, LiDAR, semantic, alignment, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Xie_SG-PGM_Partial_Graph_Matching_Network_with_Semantic_Geometric_Fusion_for_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Xie_SG-PGM_Partial_Graph_Matching_Network_with_Semantic_Geometric_Fusion_for_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 SGAligner [34] is the first work specifically focusing on this problem.를 문제로 두고, It consists of a finite set of object nodes V = {v1, v2, ..., vM}, an adjacency matrix A ∈{0, 1}M×M, a node feature matrix X ∈RM×· and a edge feature matrix ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Scene graphs have been recently introduced into 3D spatial understanding as a comprehensive representation of the scene.
- **p. 1 / Abstract - extractive body cue:** The alignment between 3D scene graphs is the first step of many downstream tasks such as scene graph aided point cloud registration, mosaicking, overlap checking, ...
- **p. 1 / Abstract - extractive body cue:** In this work, we treat 3D scene graph alignment as a partial graph-matching problem and propose to solve it with a graph neural network.
- **p. 1 / Abstract - extractive body cue:** We reuse the geometric features learned by a point cloud registration method and associate the clustered point-level geometric features with the node-level semantic feature via ...
- **p. 1 / Abstract - extractive body cue:** Partial matching is enabled by using a learnable method to select the top-k similar node pairs.
- **p. 1 / 1. Introduction - extractive body cue:** SGAligner [34] is the first work specifically focusing on this problem.
- **p. 1 / 1. Introduction - extractive body cue:** One of the main problems of the aforementioned applications is searching for the partial alignment of two or more 3D scene graphs.

## Core Idea

- **p. 3 / 3.1. Scene Graph Matching Network - extractive body cue:** It consists of a finite set of object nodes V = {v1, v2, ..., vM}, an adjacency matrix A ∈{0, 1}M×M, a node feature matrix ...
- **p. 4 / 3.2. Point to Scene Graph Feature Fusion - extractive body cue:** In that case, the subgraph that only consists of these nodes is automorphism.
- **p. 4 / 3.3. Super-point Matching Rescoring - extractive body cue:** We propose the Super-point Matching Rescoring method that uses the semantic similarity learned by our scene graph 28404
- **p. 5 / 3.3. Super-point Matching Rescoring - extractive body cue:** Therefore, our method can be easily adapted to most feature-based registration methods, bot point-level matching [13] and super-point matching [16, 31, 50].
- **p. 5 / 3.3. Super-point Matching Rescoring - extractive body cue:** Because our rescoring method does not introduce any learnable parameters, we do not need to train our method with the point cloud registration method jointly.
- **p. 4 / 3.1. Scene Graph Matching Network - extractive body cue:** To explicitly enable partial matching, we employ the pipeline introduced in [44]: the Soft-topK algorithm first flattens ˜S and selects the K most likely matched ...
- **p. 3 / 3.1. Scene Graph Matching Network - extractive body cue:** As illustrated in 2a, our matching network first projects the semantic node features X and semantic edge features E of the source and reference graphs ...
- **p. 4 / 3.3. Super-point Matching Rescoring - extractive body cue:** Feature-based point cloud registration methods like GeoTransformer [31] first compare the similarity of points or super-points, to determine the potential point-wise correspondence.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In this work, Sarkar et al. proposed a neural network that learns a joint multi-modal embedding encoded with semantic, geometric, and structural information for each node entity in the graph, which is ... | camera/depth stream, pose, map와 language goal | p. 1 (1. Introduction), p. 3 (3.1. Scene Graph Matching Network) |
| State/latent | Sarkar, neural, network, learns, joint, multi-modal, embedding, encoded, semantic, geometric, structural, information | robot pose, free-space/semantic map와 local goal | p. 1 (1. Introduction), p. 3 (3.1. Scene Graph Matching Network), p. 4 (3.1. Scene Graph Matching Network) |
| Output/action | The 3D scene graph may contain noise due to the imperfect output of graph estimation method [41, 46, 47, 54] and the dynamical scene changes in long-term [40]. | collision-free trajectory 또는 velocity command | p. 3 (3.1. Scene Graph Matching Network), p. 4 (3.1. Scene Graph Matching Network), p. 3 (3.1. Scene Graph Matching Network) |
| Objective/outcome | We follow [11, 18, 22] to further relax the constraint from the Quadratic Assignment Problem to the Linear Assignment Problem, and define the objective function f (·) as the negative cross entropy ... | goal reach, safety, localization error와 replanning latency | p. 3 (3.1. Scene Graph Matching Network), p. 3 (3.1. Scene Graph Matching Network), p. 5 (3.4. Loss Functions) |

## Main Claims and Actual Contribution

- **p. 3 / 3.1. Scene Graph Matching Network - extractive body cue:** It consists of a finite set of object nodes V = {v1, v2, ..., vM}, an adjacency matrix A ∈{0, 1}M×M, a node feature matrix ...
- **p. 4 / 3.2. Point to Scene Graph Feature Fusion - extractive body cue:** In that case, the subgraph that only consists of these nodes is automorphism.
- **p. 4 / 3.3. Super-point Matching Rescoring - extractive body cue:** We propose the Super-point Matching Rescoring method that uses the semantic similarity learned by our scene graph 28404
- **p. 5 / 3.3. Super-point Matching Rescoring - extractive body cue:** Therefore, our method can be easily adapted to most feature-based registration methods, bot point-level matching [13] and super-point matching [16, 31, 50].
- **p. 5 / 3.3. Super-point Matching Rescoring - extractive body cue:** Because our rescoring method does not introduce any learnable parameters, we do not need to train our method with the point cloud registration method jointly.
- **p. 6 / 4.1. Scene Graph Alignment and Overlap Checking - extractive body cue:** As shown in Table 1, adding the proposed P2SG Fusion to the baseline significantly improves the node alignment accuracy and is already higher than SGAligner.
- **p. 7 / 4.2. Point Cloud Registration and Mosaicking - extractive body cue:** It explains the accuracy improvement from the B+P variant to the B+P+K variant of our method.
- **p. 6 / 4.1. Scene Graph Alignment and Overlap Checking - extractive body cue:** Even though retrained with augmentation, SGAligner still shows a significant accuracy drop compared to results in Table 1, while the overall performance of our method ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 6 (4.1. Scene Graph Alignment and Overlap Checking), p. 7 (4.2. Point Cloud Registration and Mosaicking) |
| Embodiment/environment | For alignment and registration tasks, we follow the data prepossessing method in [34] and generate 15,277 training samples and 1,882 validation samples from the 3RScan dataset [40, 41]. | hardware/simulator version and reset protocol | p. 6 (4. Experiments), p. 7 (4.3. Aligning 3D Scenes with Changes) |
| Dataset/benchmark | Registration Strategy We build up an experiment to evaluate the registration performance on the same validation split used in 4.2 using the ground truth scene graph alignment and run registration with all-to-all ... | role, split, size and leakage | p. 6 (4. Experiments), p. 7 (4.3. Aligning 3D Scenes with Changes), p. 8 (4.4. Ablation Study), p. 6 (4.1. Scene Graph Alignment and Overlap Checking) |
| Metric | We use the same metrics as in [34] to evaluate the results: accuracy and completeness of the resulting reconstruction (the-lower-the-better), precision, recall, and F1-score of registered point clouds (the-higher-the-better). | definition, denominator, direction and uncertainty | p. 7 (4.2. Point Cloud Registration and Mosaicking), p. 7 (4.2. Point Cloud Registration and Mosaicking), p. 6 (4.1. Scene Graph Alignment and Overlap Checking) |
| Baseline/ablation | For ablation study, we incrementally add our proposed modules to our baseline B graph matching network: (1) B+P as adding P2SG Fusion, (2) B+P+K as adding Soft-topK and AFA-U, (3) SG-PGM (B+P+K+S) ... | fair input/data/compute/action matching | p. 6 (4. Experiments), p. 7 (4.2. Point Cloud Registration and Mosaicking), p. 7 (4.2. Point Cloud Registration and Mosaicking) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** Moreover, our scene graph alignment method remains decoupled from registration and robust to scene dynamics and noises.
- **p. 8 / 5. Conclusion - extractive body cue:** For future work, we would like to explore the approach for using semantic priors from scene graph alignment to design efficient sparse transformers for geometric ...
- **p. 6 / 4.1. Scene Graph Alignment and Overlap Checking - extractive body cue:** We trained SGAligner with random T and Gaussian noise as augmentation (SGA*).
- **p. 6 / 4.1. Scene Graph Alignment and Overlap Checking - extractive body cue:** This demonstrates that fusing graphs and geometric features with our method is robust against rotation.
- **p. 7 / 4.2. Point Cloud Registration and Mosaicking - extractive body cue:** As shown in Table 3, our method outperforms SGAligner in 4 out of 5 metrics even without a robust estimator (Ours+R).

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 SGAligner [34] is the first work specifically focusing on this problem.를 문제로 두고, It consists of a finite set of object nodes V = {v1, v2, ..., vM}, an adjacency matrix A ∈{0, 1}M×M, a node feature matrix X ∈RM×· and a edge feature matrix ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Scene Graph Matching Network), p. 3 (3.1. Scene Graph Matching Network) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
