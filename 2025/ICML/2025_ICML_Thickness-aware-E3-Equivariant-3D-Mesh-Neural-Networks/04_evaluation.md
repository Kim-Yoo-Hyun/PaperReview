# Evaluation - Thickness-aware E(3)-Equivariant 3D Mesh Neural Networks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=Ya2ksKuNMh; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/167333. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.4.1. MAIN RESULTS), p. 7 (5.4.1. MAIN RESULTS), p. 8 (5.4.2. IMPACT OF THICKNESS-AWARE FRAMEWORK), p. 14 (Figure/Table caption), p. 13 (Figure/Table caption), p. 8 (5.4.2. IMPACT OF THICKNESS-AWARE FRAMEWORK)): The results demonstrate that spatial information alone is sufficient to achieve strong performance in terms of R2 score, highlighting its importance in representing meaningful relationships and Figure 6.

## Evaluation Body Digest

- **p. 6 / 5.1. Dataset Description - extractive body cue:** We evaluate T-EMNN using a dataset from real-world injection molding applications.
- **p. 6 / 5.1. Dataset Description - extractive body cue:** This dataset is well-suited for evaluating T-EMNN as its geometries exhibit thickness across all surfaces, enabling thickness-related interaction modeling.
- **p. 7 / 5.3. Evaluation Settings - extractive body cue:** We assess the model performance using three metrics: 1) RMSE, which evaluates the effectiveness of handling outliers, 2) MAE, which measures the consistency and accuracy ...
- **p. 8 / 5.4.3. EVALUATION UNDER DYNAMIC SETTING - extractive body cue:** To evaluate the dynamic capabilities of our framework-particularly the thickness processor-we conduct next-timestep deformation prediction using the Deforming Plate dataset (Pfaff et al., 2020).
- **p. 7 / 5.4.1. MAIN RESULTS - extractive body cue:** Spatial information plays a critical role in capturing localized patterns, which are essential for accurate interpretation in downstream tasks.
- **p. 8 / 5.4.2. IMPACT OF THICKNESS-AWARE FRAMEWORK - extractive body cue:** This result validates the importance of the thickness in 3D objects, and its effective integration can improve the models' capability in static analysis.
- **p. 7 / 5.4.1. MAIN RESULTS - extractive body cue:** This underscores the critical role of E(3)-equivariance in ensuring the robustness of the coordinate system.
- **p. 7 / 5.4.1. MAIN RESULTS - extractive body cue:** The results demonstrate that spatial information alone is sufficient to achieve strong performance in terms of R2 score, highlighting its importance in representing meaningful relationships ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiment (p. 6); 5.1. Dataset Description (p. 6); 5.3. Evaluation Settings (p. 6); 5.4. Experiment Results (p. 7); 5.4.1. MAIN RESULTS (p. 7); 5.4.3. EVALUATION UNDER DYNAMIC SETTING (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.4.1. MAIN RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results demonstrate that spatial information alone is sufficient to achieve strong performance in terms of R2 score, highlighting its importance in representing meaningful ... | p. 7 (5.4.1. MAIN RESULTS) |
| 5.4.1. MAIN RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The enhanced alignment provided by our proposed data-driven coordinate system significantly improves the representation of spatial relationships, leading to superior performance in downstream tasks. | p. 7 (5.4.1. MAIN RESULTS) |
| 5.4.2. IMPACT OF THICKNESS-AWARE FRAMEWORK | EMPIRICAL / REAL-ROBOT OR HARDWARE | 8, all baseline models exhibit improved performance when incorporating thickness edges compared to their counterparts without them. | p. 8 (5.4.2. IMPACT OF THICKNESS-AWARE FRAMEWORK) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 13. R2 scores for all test data. In the shape IDs, ‘s' indicates seen shapes included in the training data, while ‘us' refers ... | p. 14 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 4. Comparison of training speed (iteration/sec) and GPU memory usage (MB) across different models. Our model is based on MGN, with an additional ... | p. 13 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 5.1. Dataset Description - extractive body cue:** We evaluate T-EMNN using a dataset from real-world injection molding applications.
- **p. 6 / 5.1. Dataset Description - extractive body cue:** This dataset is well-suited for evaluating T-EMNN as its geometries exhibit thickness across all surfaces, enabling thickness-related interaction modeling.
- **p. 7 / 5.3. Evaluation Settings - extractive body cue:** We assess the model performance using three metrics: 1) RMSE, which evaluates the effectiveness of handling outliers, 2) MAE, which measures the consistency and accuracy ...
- **p. 8 / 5.4.3. EVALUATION UNDER DYNAMIC SETTING - extractive body cue:** To evaluate the dynamic capabilities of our framework-particularly the thickness processor-we conduct next-timestep deformation prediction using the Deforming Plate dataset (Pfaff et al., 2020).
- **p. 7 / 5.4.1. MAIN RESULTS - extractive body cue:** Spatial information plays a critical role in capturing localized patterns, which are essential for accurate interpretation in downstream tasks.
- **p. 8 / 5.4.2. IMPACT OF THICKNESS-AWARE FRAMEWORK - extractive body cue:** This result validates the importance of the thickness in 3D objects, and its effective integration can improve the models' capability in static analysis.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. The left figures show a mesh, with two different target nodes (•), their thickness paired nodes (•), thickness distance (-), and nearby nodes ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of T-EMNN. 𝐛! 𝐛" 𝐛# 𝐱$$%& 𝐱'( 𝐛# 𝐯= 𝐱!" -𝐱##$%
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Our proposed data-driven coordinate system. system defined by the shape itself, independent of its orien- tation or alignment in the original coordinate system. ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. The concept of thickness (left) and width (right). Sec 3.3. In brief, thickness is characterized by the spatial separation between opposing surfaces, with ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Model Performance in In-Distribution and Out-of-Distribution Settings, averaged over 3 seeds with standard deviation (in parentheses). Bold indicates the best performance among the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Learning curve of the thickness threshold τ during train- ing across three seeds (left), and the distribution of thickness values t(vi) with the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6. Performance comparison of T-EMNN with a fixed thick- ness threshold. The value 5.68 corresponds to the learned thickness threshold in T-EMNN when using ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7. Visualization of error magnitude (RMSE). The ground truth shows deformation magnitude (a), while (b-f) illustrate prediction errors. Additional examples are in Fig. 15 ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate T-EMNN using a dataset from real-world injection molding applications. | embodiment, simulator version and control stack | p. 6 (5.1. Dataset Description), p. 6 (5.1. Dataset Description) |
| Task/environment | This dataset is well-suited for evaluating T-EMNN as its geometries exhibit thickness across all surfaces, enabling thickness-related interaction modeling. | reset, timeout, object/scene variation | p. 6 (5.1. Dataset Description), p. 7 (5.3. Evaluation Settings) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (4. Methodology), p. 4 (4.2.1. ENCODER) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3.1. Notations), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| This underscores the critical role of E(3)-equivariance in ensuring the robustness of the coordinate system. | definition/direction/unit from same section | p. 7 (5.4.1. MAIN RESULTS) |
| The results demonstrate that spatial information alone is sufficient to achieve strong performance in terms of R2 score, highlighting its importance in representing meaningful ... | definition/direction/unit from same section | p. 7 (5.4.1. MAIN RESULTS) |
| The ground truth shows deformation magnitude (a), while (b-f) illustrate prediction errors. | definition/direction/unit from same section | p. 8 (5.4.1. MAIN RESULTS) |
| Figure 13. R2 scores for all test data. In the shape IDs, ‘s' indicates seen shapes included in the training data, while ‘us' refers ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| Visualization of error magnitude (RMSE). | definition/direction/unit from same section | p. 8 (5.4.1. MAIN RESULTS) |
| Figure 11. Examples of Dataset Shapes. The experimental conditions consist of eight types for each shape: pack pressure, pack time, projected area, gate size, ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| MGN (Pfaff et al., 2020) models physical interactions using graph-based message passing but lacks E(3)- equivariance. | definition/direction/unit from same section | p. 6 (5.2. Baselines) |
| Building upon EGNN, EMNN (Trang et al., 2024) optimizes this framework for mesh data by generating E(3)-invariant messages that incorporate geometric information from mesh ... | definition/direction/unit from same section | p. 6 (5.2. Baselines) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 8, all baseline models exhibit improved performance when incorporating thickness edges compared to their counterparts without them. | comparison identity and matched condition | p. 8 (5.4.2. IMPACT OF THICKNESS-AWARE FRAMEWORK) |
| Comparison of baselines with xinv and their extension with our thickness edges. models that originally lacked it, such as (e) MGN. | comparison identity and matched condition | p. 8 (5.4.1. MAIN RESULTS) |
| As baselines, we include multiple graph-based neural network methods to evaluate T-EMNN against existing techniques. | comparison identity and matched condition | p. 6 (5.2. Baselines) |
| To address the missing spatial information in baseline methods, we incorporate an additional spatial encoder, as defined in Eq. | comparison identity and matched condition | p. 7 (5.4.1. MAIN RESULTS) |
| Moreover, for baselines that do not explicitly leverage latent spatial embeddings (e.g., (c) MGN, (f) EGNN, and (i) EMNN in Tab. | comparison identity and matched condition | p. 7 (5.4.1. MAIN RESULTS) |
| Table 4. Comparison of training speed (iteration/sec) and GPU memory usage (MB) across different models. Our model is based on MGN, with an additional ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Building upon EGNN, EMNN (Trang et al., 2024) optimizes this framework for mesh data by generating E(3)-invariant messages that incorporate geometric information from mesh ... | component/input/data sensitivity | p. 6 (5.2. Baselines) |
| Thickness-aware E(3)-Equivariant 3D Mesh Neural Networks Table 1. | component/input/data sensitivity | p. 7 (5.3. Evaluation Settings) |
| However, when the coordinate system lacks E(3)-equivariant properties, performance significantly deteriorates when testing data exhibits a different coordinate distribution (i.e., out-of-distribution results of (a) ... | component/input/data sensitivity | p. 7 (5.4.1. MAIN RESULTS) |
| Ablation Study of Thickness Edge Features. | component/input/data sensitivity | p. 8 (5.4.2. IMPACT OF THICKNESS-AWARE FRAMEWORK) |
| 8, all baseline models exhibit improved performance when incorporating thickness edges compared to their counterparts without them. | component/input/data sensitivity | p. 8 (5.4.2. IMPACT OF THICKNESS-AWARE FRAMEWORK) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The key contributions of this study are as follows: • Thickness-Aware Framework: We propose a Thicknessaware E(3)-Equivariant 3D Mesh Neural Networks (TEMNN) that accurately ... | The results demonstrate that spatial information alone is sufficient to achieve strong performance in terms of R2 score, highlighting its importance in representing meaningful ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.4.1. MAIN RESULTS), p. 7 (5.4.1. MAIN RESULTS), p. 8 (5.4.2. IMPACT OF THICKNESS-AWARE FRAMEWORK), p. 14 (Figure/Table caption), p. 13 (Figure/Table caption), p. 8 (5.4.2. IMPACT OF THICKNESS-AWARE FRAMEWORK) |
| Primary metric/result | The enhanced alignment provided by our proposed data-driven coordinate system significantly improves the representation of spatial relationships, leading to superior performance in downstream tasks. | numeric claim only at cited anchor | p. 7 (5.4.1. MAIN RESULTS) |

- Numeric sentences retained from the body:
- **p. 7 / 5.3. Evaluation Settings - extractive body cue:** Model Performance in In-Distribution and Out-of-Distribution Settings, averaged over 3 seeds with standard deviation (in parentheses).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 14. Comparisons between volume mesh and surface mesh. The methods used for comparison are based on the MGN framework with coordinate embeddings from ... | p. 14 (Figure/Table caption) |
| body limitation/failure cue | Figure 13. R2 scores for all test data. In the shape IDs, ‘s' indicates seen shapes included in the training data, while ‘us' refers ... | p. 14 (Figure/Table caption) |
| body limitation/failure cue | Table 4. Comparison of training speed (iteration/sec) and GPU memory usage (MB) across different models. Our model is based on MGN, with an additional ... | p. 13 (Figure/Table caption) |
| body limitation/failure cue | Note that the out-of-distribution scenario is designed to assess how well the methods adapt to objects 6 | p. 6 (5.3. Evaluation Settings) |
| body limitation/failure cue | This underscores the critical role of E(3)-equivariance in ensuring the robustness of the coordinate system. | p. 7 (5.4.1. MAIN RESULTS) |
| body limitation/failure cue | Model Performance in In-Distribution and Out-of-Distribution Settings, averaged over 3 seeds with standard deviation (in parentheses). | p. 7 (5.3. Evaluation Settings) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| To address the missing spatial information in baseline methods, we incorporate an additional spatial encoder, as defined in Eq. | p. 7 (5.4.1. MAIN RESULTS) |
| Model Performance in In-Distribution and Out-of-Distribution Settings, averaged over 3 seeds with standard deviation (in parentheses). | p. 7 (5.3. Evaluation Settings) |
| 5, τ converges to 5.68 across three seeds with low variance, filtering out 3.83% of thickness edges exceeding this threshold (Sec. | p. 8 (5.4.2. IMPACT OF THICKNESS-AWARE FRAMEWORK) |
| This is because the inherent locality of surface-mesh, where it requires GNN-based methods to take at least six propagation steps along the shortest path ... | p. 8 (5.4.2. IMPACT OF THICKNESS-AWARE FRAMEWORK) |
| T-EMNN consists of an encoder (Sec. | p. 3 (4. Methodology) |
| Our method, T-EMNN, extends the encode-process-decode framework of MGN (Pfaff et al., 2020), introducing key innovations for handling 3D shapes with thickness while incorporating ... | p. 3 (4. Methodology) |
| This transformation is achieved through the following steps: Step 1: Adjust Coordinates to Center of Mass. | p. 4 (4. Methodology) |
| For every node vi ∈V and edge eij ∈E within the surface mesh M = (V, E), we encode their features using respective MLP ... | p. 4 (4.2.1. ENCODER) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 14 / Figure/Table caption - extractive body cue:** Figure 14. Comparisons between volume mesh and surface mesh. The methods used for comparison are based on the MGN framework with coordinate embeddings from our ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 13. R2 scores for all test data. In the shape IDs, ‘s' indicates seen shapes included in the training data, while ‘us' refers to ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 4. Comparison of training speed (iteration/sec) and GPU memory usage (MB) across different models. Our model is based on MGN, with an additional thickness ...
- **p. 6 / 5.3. Evaluation Settings - extractive body cue:** Note that the out-of-distribution scenario is designed to assess how well the methods adapt to objects 6
- **p. 7 / 5.4.1. MAIN RESULTS - extractive body cue:** This underscores the critical role of E(3)-equivariance in ensuring the robustness of the coordinate system.
- **p. 7 / 5.3. Evaluation Settings - extractive body cue:** Model Performance in In-Distribution and Out-of-Distribution Settings, averaged over 3 seeds with standard deviation (in parentheses).

- **Evidence anchors reviewed:** datasets p. 6 (5.1. Dataset Description), p. 6 (5.1. Dataset Description), p. 7 (5.3. Evaluation Settings), p. 8 (5.4.3. EVALUATION UNDER DYNAMIC SETTING), p. 7 (5.4.1. MAIN RESULTS), p. 8 (5.4.2. IMPACT OF THICKNESS-AWARE FRAMEWORK), metrics p. 7 (5.4.1. MAIN RESULTS), p. 7 (5.4.1. MAIN RESULTS), p. 8 (5.4.1. MAIN RESULTS), p. 14 (Figure/Table caption), p. 8 (5.4.1. MAIN RESULTS), p. 12 (Figure/Table caption), baselines p. 8 (5.4.2. IMPACT OF THICKNESS-AWARE FRAMEWORK), p. 8 (5.4.1. MAIN RESULTS), p. 6 (5.2. Baselines), p. 7 (5.4.1. MAIN RESULTS), p. 7 (5.4.1. MAIN RESULTS), p. 13 (Figure/Table caption), results p. 7 (5.4.1. MAIN RESULTS), p. 7 (5.4.1. MAIN RESULTS), p. 8 (5.4.2. IMPACT OF THICKNESS-AWARE FRAMEWORK), p. 14 (Figure/Table caption), p. 13 (Figure/Table caption), p. 8 (5.4.2. IMPACT OF THICKNESS-AWARE FRAMEWORK).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
