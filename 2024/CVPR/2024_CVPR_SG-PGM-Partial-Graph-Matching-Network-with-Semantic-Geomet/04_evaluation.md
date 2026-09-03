# Evaluation - SG-PGM: Partial Graph Matching Network with Semantic Geometric Fusion for 3D Scene Graph Alignment and Its Downstream Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Xie_SG-PGM_Partial_Graph_Matching_Network_with_Semantic_Geometric_Fusion_for_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Xie_SG-PGM_Partial_Graph_Matching_Network_with_Semantic_Geometric_Fusion_for_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.1. Scene Graph Alignment and Overlap Checking), p. 7 (4.2. Point Cloud Registration and Mosaicking), p. 6 (4.1. Scene Graph Alignment and Overlap Checking), p. 7 (4.2. Point Cloud Registration and Mosaicking), p. 8 (4.3. Aligning 3D Scenes with Changes), p. 8 (4.3. Aligning 3D Scenes with Changes)): As shown in Table 1, adding the proposed P2SG Fusion to the baseline significantly improves the node alignment accuracy and is already higher than SGAligner.

## Evaluation Body Digest

- **p. 6 / 4. Experiments - extractive body cue:** For alignment and registration tasks, we follow the data prepossessing method in [34] and generate 15,277 training samples and 1,882 validation samples from the 3RScan ...
- **p. 7 / 4.3. Aligning 3D Scenes with Changes - extractive body cue:** 3RScan dataset provides multiple rescans of one scene with changes such as moved, removed, and deformed objects.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Registration Strategy We build up an experiment to evaluate the registration performance on the same validation split used in 4.2 using the ground truth scene ...
- **p. 6 / 4.1. Scene Graph Alignment and Overlap Checking - extractive body cue:** We provide a more practical evaluation by augmenting random transformation between two scene fragments, different from the T = I4 benchmark in [34].
- **p. 7 / 4.2. Point Cloud Registration and Mosaicking - extractive body cue:** We select 143 scenes for testing point cloud mosaicking and the results are listed in Table 5.
- **p. 8 / 4.3. Aligning 3D Scenes with Changes - extractive body cue:** Following SGAligner [34], we investigate the alignment in the following scenarios: (i) aligning a sub-scene on the original scan that contains no changes; (ii) aligning ...
- **p. 5 / 4. Experiments - extractive body cue:** We evaluate our method for scene graph alignment and overlap-checking (Sec.
- **p. 7 / 4.2. Point Cloud Registration and Mosaicking - extractive body cue:** We use the same metrics as in [34] to evaluate the results: accuracy and completeness of the resulting reconstruction (the-lower-the-better), precision, recall, and F1-score of ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Scene Graph Alignment and Overlap Checking | SYSTEM / EVALUATION SCOPE UNRESOLVED | As shown in Table 1, adding the proposed P2SG Fusion to the baseline significantly improves the node alignment accuracy and is already higher than ... | p. 6 (4.1. Scene Graph Alignment and Overlap Checking) |
| 4.2. Point Cloud Registration and Mosaicking | SYSTEM / EVALUATION SCOPE UNRESOLVED | It explains the accuracy improvement from the B+P variant to the B+P+K variant of our method. | p. 7 (4.2. Point Cloud Registration and Mosaicking) |
| 4.1. Scene Graph Alignment and Overlap Checking | SYSTEM / EVALUATION SCOPE UNRESOLVED | Even though retrained with augmentation, SGAligner still shows a significant accuracy drop compared to results in Table 1, while the overall performance of our ... | p. 6 (4.1. Scene Graph Alignment and Overlap Checking) |
| 4.2. Point Cloud Registration and Mosaicking | SYSTEM / EVALUATION SCOPE UNRESOLVED | We use the same metrics as in [34] to evaluate the results: accuracy and completeness of the resulting reconstruction (the-lower-the-better), precision, recall, and F1-score ... | p. 7 (4.2. Point Cloud Registration and Mosaicking) |
| 4.3. Aligning 3D Scenes with Changes | SYSTEM / EVALUATION SCOPE UNRESOLVED | Our approach outperforms SGAligner in most metrics of all three scenarios, which indicates the strong robustness to scene changes. | p. 8 (4.3. Aligning 3D Scenes with Changes) |

## Dataset / Benchmark Role

- **p. 6 / 4. Experiments - extractive body cue:** For alignment and registration tasks, we follow the data prepossessing method in [34] and generate 15,277 training samples and 1,882 validation samples from the 3RScan ...
- **p. 7 / 4.3. Aligning 3D Scenes with Changes - extractive body cue:** 3RScan dataset provides multiple rescans of one scene with changes such as moved, removed, and deformed objects.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Registration Strategy We build up an experiment to evaluate the registration performance on the same validation split used in 4.2 using the ground truth scene ...
- **p. 6 / 4.1. Scene Graph Alignment and Overlap Checking - extractive body cue:** We provide a more practical evaluation by augmenting random transformation between two scene fragments, different from the T = I4 benchmark in [34].
- **p. 7 / 4.2. Point Cloud Registration and Mosaicking - extractive body cue:** We select 143 scenes for testing point cloud mosaicking and the results are listed in Table 5.
- **p. 8 / 4.3. Aligning 3D Scenes with Changes - extractive body cue:** Following SGAligner [34], we investigate the alignment in the following scenarios: (i) aligning a sub-scene on the original scan that contains no changes; (ii) aligning ...
- **p. 5 / 4. Experiments - extractive body cue:** We evaluate our method for scene graph alignment and overlap-checking (Sec.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. SG-PGM: partial graph matching for 3D scene graph alignment. Semantic and geometric features are fused for object-wise matching between fragments (a), and downstream ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. The network overview of the proposed system. (a) shows the feature extraction and our proposed Point to Scene Graph Feature Fusion of one ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Scene graph encoder with GATv2 layers and learnable skip connections. In the alignment and registration stage (shown in Figure 2b), fused embedding of ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. P2SG fusion module projects point-wise geometric features to node-wise geometric embedding and combines it with the semantic scene graph feature. As is illustrated ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. Long-range cross-object geometric feature is gathered in registration method [31] with transformer. Points in red circles are difficult to match without taking nearby ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Evaluation on node matching. We evaluate the scene graph node alignment of our method's different variants and compare it with SGAligner. All metrics ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6. Evaluation on node matching with transformation T̸ = I4. Results are distributed per overlap range. We provide a more practical evaluation by augmenting ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Overlap check for point cloud registration. T = I4 between fragments. All metrics are the-higher-the-better.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For alignment and registration tasks, we follow the data prepossessing method in [34] and generate 15,277 training samples and 1,882 validation samples from the ... | embodiment, simulator version and control stack | p. 6 (4. Experiments), p. 7 (4.3. Aligning 3D Scenes with Changes) |
| Task/environment | 3RScan dataset provides multiple rescans of one scene with changes such as moved, removed, and deformed objects. | reset, timeout, object/scene variation | p. 7 (4.3. Aligning 3D Scenes with Changes), p. 8 (4.4. Ablation Study) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 3 (3.1. Scene Graph Matching Network) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 4 (3.1. Scene Graph Matching Network), p. 3 (3.1. Scene Graph Matching Network) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We use the same metrics as in [34] to evaluate the results: accuracy and completeness of the resulting reconstruction (the-lower-the-better), precision, recall, and F1-score ... | definition/direction/unit from same section | p. 7 (4.2. Point Cloud Registration and Mosaicking) |
| We evaluate the registration accuracy with Chamfer Distance (CD), Relative Rotation and Translation Error (RRE and RTE), Feature Matching Recall (FMR) and Registration Recall ... | definition/direction/unit from same section | p. 7 (4.2. Point Cloud Registration and Mosaicking) |
| Therefore, we also assess our results using the F1-score (the harmonic mean of the precision and recall). | definition/direction/unit from same section | p. 6 (4.1. Scene Graph Alignment and Overlap Checking) |
| With the Soft-topK module, our method can also effectively surpass the false-positive matching pairs and therefore yield the highest F1 score. | definition/direction/unit from same section | p. 6 (4.1. Scene Graph Alignment and Overlap Checking) |
| Registration Strategy We build up an experiment to evaluate the registration performance on the same validation split used in 4.2 using the ground truth ... | definition/direction/unit from same section | p. 8 (4.4. Ablation Study) |
| Table 6. Alignment of a local 3D scene to a prior 3D map with differences in overlap and changes. We run SGAligner on our ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 4. P2SG fusion module projects point-wise geometric features to node-wise geometric embedding and combines it with the semantic scene graph feature. As is ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 5. Long-range cross-object geometric feature is gathered in registration method [31] with transformer. Points in red circles are difficult to match without taking ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For ablation study, we incrementally add our proposed modules to our baseline B graph matching network: (1) B+P as adding P2SG Fusion, (2) B+P+K ... | comparison identity and matched condition | p. 6 (4. Experiments) |
| Our method outperforms others even without using RANSAC. | comparison identity and matched condition | p. 7 (4.2. Point Cloud Registration and Mosaicking) |
| As shown in Table 3, our method outperforms SGAligner in 4 out of 5 metrics even without a robust estimator (Ours+R). | comparison identity and matched condition | p. 7 (4.2. Point Cloud Registration and Mosaicking) |
| This means that our method provides more false-positive matching in low-overlap cases compared to high-overlap cases, but still much better than [34]. | comparison identity and matched condition | p. 6 (4.1. Scene Graph Alignment and Overlap Checking) |
| Our approach outperforms SGAligner in most metrics of all three scenarios, which indicates the strong robustness to scene changes. | comparison identity and matched condition | p. 8 (4.3. Aligning 3D Scenes with Changes) |
| Super-point Matching Rescoring As shown in Table 4, with the help of the Super-point Matching Rescoring, our method shows obviously better performance in terms ... | comparison identity and matched condition | p. 8 (4.4. Ablation Study) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 4. 3D point cloud registration per overlap. Random transformation is augmented to the scene fragments. Comparison against GCNet [56] is in Appendix Table ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| In this section, we use the scene graph alignment result from SGAligner and our method's variants as priors, to support pretrained GeoTransformer [31] for ... | component/input/data sensitivity | p. 7 (4.2. Point Cloud Registration and Mosaicking) |
| Table 1. Evaluation on node matching. We evaluate the scene graph node alignment of our method's different variants and compare it with SGAligner. All ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| 4.2) and provide an ablation study (Sec. | component/input/data sensitivity | p. 6 (4. Experiments) |
| Ablation study on different registration strategies. | component/input/data sensitivity | p. 8 (4.4. Ablation Study) |
| Registration results with and without Superpoint Matching Rescoring of low overlapping scene fragments. | component/input/data sensitivity | p. 8 (4.3. Aligning 3D Scenes with Changes) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| It consists of a finite set of object nodes V = {v1, v2, ..., vM}, an adjacency matrix A ∈{0, 1}M×M, a node feature ... | As shown in Table 1, adding the proposed P2SG Fusion to the baseline significantly improves the node alignment accuracy and is already higher than ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.1. Scene Graph Alignment and Overlap Checking), p. 7 (4.2. Point Cloud Registration and Mosaicking), p. 6 (4.1. Scene Graph Alignment and Overlap Checking), p. 7 (4.2. Point Cloud Registration and Mosaicking), p. 8 (4.3. Aligning 3D Scenes with Changes), p. 8 (4.3. Aligning 3D Scenes with Changes) |
| Primary metric/result | It explains the accuracy improvement from the B+P variant to the B+P+K variant of our method. | numeric claim only at cited anchor | p. 7 (4.2. Point Cloud Registration and Mosaicking) |

- Numeric sentences retained from the body:
- **p. 7 / 4.2. Point Cloud Registration and Mosaicking - extractive body cue:** We select 143 scenes for testing point cloud mosaicking and the results are listed in Table 5.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Moreover, our scene graph alignment method remains decoupled from registration and robust to scene dynamics and noises. | p. 8 (5. Conclusion) |
| body limitation/failure cue | For future work, we would like to explore the approach for using semantic priors from scene graph alignment to design efficient sparse transformers for ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | We trained SGAligner with random T and Gaussian noise as augmentation (SGA*). | p. 6 (4.1. Scene Graph Alignment and Overlap Checking) |
| body limitation/failure cue | This demonstrates that fusing graphs and geometric features with our method is robust against rotation. | p. 6 (4.1. Scene Graph Alignment and Overlap Checking) |
| body limitation/failure cue | As shown in Table 3, our method outperforms SGAligner in 4 out of 5 metrics even without a robust estimator (Ours+R). | p. 7 (4.2. Point Cloud Registration and Mosaicking) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Sample numbers are different from the original data splits, due to the uncontrolled random seed in their implementation. | p. 6 (4. Experiments) |
| (5) We compute the ground truth graph similarity k with k = ∥S∥/ min(/Mref/ , /Msrc/) and use Mean Square Error (MSE) loss to ... | p. 5 (3.4. Loss Functions) |
| Implementation details and evaluation metrics definitions are in Appendix A and B. | p. 6 (4. Experiments) |
| We run SGAligner on our generated data samples and list the results together with ours in Table 6. | p. 8 (4.3. Aligning 3D Scenes with Changes) |
| Registration Strategy We build up an experiment to evaluate the registration performance on the same validation split used in 4.2 using the ground truth ... | p. 8 (4.4. Ablation Study) |
| We then combine the geometric embedding FP from the point cloud encoder to form the fused embedding FS+P . | p. 3 (3.1. Scene Graph Matching Network) |
| Scene graph encoder with GATv2 layers and learnable skip connections. | p. 4 (3.1. Scene Graph Matching Network) |
| Thus, the scene graph encoder outputs multi-layers node embedding FS ∈RM×ds with ds = d(n + 1), as shown in Figure 3. | p. 4 (3.1. Scene Graph Matching Network) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive body cue:** Moreover, our scene graph alignment method remains decoupled from registration and robust to scene dynamics and noises.
- **p. 8 / 5. Conclusion - extractive body cue:** For future work, we would like to explore the approach for using semantic priors from scene graph alignment to design efficient sparse transformers for geometric ...
- **p. 6 / 4.1. Scene Graph Alignment and Overlap Checking - extractive body cue:** We trained SGAligner with random T and Gaussian noise as augmentation (SGA*).
- **p. 6 / 4.1. Scene Graph Alignment and Overlap Checking - extractive body cue:** This demonstrates that fusing graphs and geometric features with our method is robust against rotation.
- **p. 7 / 4.2. Point Cloud Registration and Mosaicking - extractive body cue:** As shown in Table 3, our method outperforms SGAligner in 4 out of 5 metrics even without a robust estimator (Ours+R).

- **Evidence anchors reviewed:** datasets p. 6 (4. Experiments), p. 7 (4.3. Aligning 3D Scenes with Changes), p. 8 (4.4. Ablation Study), p. 6 (4.1. Scene Graph Alignment and Overlap Checking), p. 7 (4.2. Point Cloud Registration and Mosaicking), p. 8 (4.3. Aligning 3D Scenes with Changes), metrics p. 7 (4.2. Point Cloud Registration and Mosaicking), p. 7 (4.2. Point Cloud Registration and Mosaicking), p. 6 (4.1. Scene Graph Alignment and Overlap Checking), p. 6 (4.1. Scene Graph Alignment and Overlap Checking), p. 8 (4.4. Ablation Study), p. 8 (Figure/Table caption), baselines p. 6 (4. Experiments), p. 7 (4.2. Point Cloud Registration and Mosaicking), p. 7 (4.2. Point Cloud Registration and Mosaicking), p. 6 (4.1. Scene Graph Alignment and Overlap Checking), p. 8 (4.3. Aligning 3D Scenes with Changes), p. 8 (4.4. Ablation Study), results p. 6 (4.1. Scene Graph Alignment and Overlap Checking), p. 7 (4.2. Point Cloud Registration and Mosaicking), p. 6 (4.1. Scene Graph Alignment and Overlap Checking), p. 7 (4.2. Point Cloud Registration and Mosaicking), p. 8 (4.3. Aligning 3D Scenes with Changes), p. 8 (4.3. Aligning 3D Scenes with Changes).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
