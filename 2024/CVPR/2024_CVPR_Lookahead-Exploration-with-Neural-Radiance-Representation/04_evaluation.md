# Evaluation - Lookahead Exploration with Neural Radiance Representation for Continuous Vision-Language Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Wang_Lookahead_Exploration_with_Neural_Radiance_Representation_for_Continuous_Vision-Language_Navigation_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Wang_Lookahead_Exploration_with_Neural_Radiance_Representation_for_Continuous_Vision-Language_Navigation_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. Comparison to State-of-the-Art Methods), p. 6 (4.2. Comparison to State-of-the-Art Methods), p. 8 (4.3. Ablation Study), p. 7 (4.3. Ablation Study), p. 8 (4.3. Ablation Study), p. 7 (4.3. Ablation Study)): Compared with DREAMWALKER [39] in Table 1, which adopts a similar idea of lookahead exploration, our HNR model achieves performance improvement of about 10% on SR for all splits.

## Evaluation Body Digest

- **p. 6 / 4.2. Comparison to State-of-the-Art Methods - extractive body cue:** As illustrated in Table 1, for the val unseen split of the R2R-CE dataset, our model outperforms our baseline method ETPNav [9] by 4% on ...
- **p. 7 / 4.3. Ablation Study - extractive body cue:** Comparison among different candidate location representation methods on the val unseen split of the R2R-CE dataset.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** The effect of different numbers of nearest features in the HNR model on the val unseen split of the R2R-CE dataset.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Average cosine similarity between predicted future views and ground truth at different distances between candidate locations and agent, on the val unseen split of the ...
- **p. 6 / 4.1. Datasets and Evaluation Metrics - extractive body cue:** We evaluate our model on the R2R-CE [22] and RxRCE [23] datasets in continuous environments.
- **p. 7 / 4.3. Ablation Study - extractive body cue:** Evaluation on the RxR-CE dataset. # Representation Methods NE↓OSR↑SR↑SPL↑ 1 Single View 4.71 64.71 57.21 49.15 2 NeRF Rendering 4.79 65.14 56.55 48.61 3 Image ...
- **p. 6 / 4.1. Datasets and Evaluation Metrics - extractive body cue:** There are several standard metrics [5] in VLN for evaluating the agent's performance, including Trajectory Length (TL), Navigation Error (NE), Success Rate (SR), SR given ...
- **p. 7 / 4.3. Ablation Study - extractive body cue:** NeRF-based RGB rendering method [24] has a low image reconstruction accuracy in unseen environments due to the visual occlusions and high information redundancy of RGB ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Experiment (p. 6); 4.1. Datasets and Evaluation Metrics (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Comparison to State-of-the-Art Methods | SYSTEM / EVALUATION SCOPE UNRESOLVED | Compared with DREAMWALKER [39] in Table 1, which adopts a similar idea of lookahead exploration, our HNR model achieves performance improvement of about 10% ... | p. 6 (4.2. Comparison to State-of-the-Art Methods) |
| 4.2. Comparison to State-of-the-Art Methods | SYSTEM / EVALUATION SCOPE UNRESOLVED | Meanwhile, as illustrated in Table 2, the proposed method also achieves the improvement of 2% in the majority of metrics on the RxR-CE dataset. | p. 6 (4.2. Comparison to State-of-the-Art Methods) |
| 4.3. Ablation Study | SYSTEM / EVALUATION SCOPE UNRESOLVED | Row 2 doesn't use the lookahead node scores to evaluate the future paths and gain marginal performance improvement, confirming the necessity of the lookahead ... | p. 8 (4.3. Ablation Study) |
| 4.3. Ablation Study | SYSTEM / EVALUATION SCOPE UNRESOLVED | NeRF-based RGB rendering method [24] has a low image reconstruction accuracy in unseen environments due to the visual occlusions and high information redundancy of ... | p. 7 (4.3. Ablation Study) |
| 4.3. Ablation Study | SYSTEM / EVALUATION SCOPE UNRESOLVED | The lookahead node closest to the destination (i.e., Hard target) is not sure of the highest semantic match score with the instruction due to ... | p. 8 (4.3. Ablation Study) |

## Dataset / Benchmark Role

- **p. 6 / 4.2. Comparison to State-of-the-Art Methods - extractive body cue:** As illustrated in Table 1, for the val unseen split of the R2R-CE dataset, our model outperforms our baseline method ETPNav [9] by 4% on ...
- **p. 7 / 4.3. Ablation Study - extractive body cue:** Comparison among different candidate location representation methods on the val unseen split of the R2R-CE dataset.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** The effect of different numbers of nearest features in the HNR model on the val unseen split of the R2R-CE dataset.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Average cosine similarity between predicted future views and ground truth at different distances between candidate locations and agent, on the val unseen split of the ...
- **p. 6 / 4.1. Datasets and Evaluation Metrics - extractive body cue:** We evaluate our model on the R2R-CE [22] and RxRCE [23] datasets in continuous environments.
- **p. 7 / 4.3. Ablation Study - extractive body cue:** Evaluation on the RxR-CE dataset. # Representation Methods NE↓OSR↑SR↑SPL↑ 1 Single View 4.71 64.71 57.21 49.15 2 NeRF Rendering 4.79 65.14 56.55 48.61 3 Image ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Illustration of different methods to represent the naviga- ble candidate locations. (a) uses the single-view observation (yel- low sector area). (b) uses the ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. The framework of the hierarchical neural radiance representation model (HNR). The HNR model encodes the observed environ- ments (yellow area) into the feature ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Illustration of the volume rendering method and hierar- chical encoding. information are stored into the feature cloud M: Mt = Mt-1 ∪{[gt,j, Pt,j, ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. The framework of the lookahead VLN model. In addi- tion to the stop embedding (black), three types of nodes are used to structure ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Evaluation on the R2R-CE dataset. Methods Val Seen Val Unseen Test Unseen NE↓SR↑SPL↑NDTW↑SDTW↑NE↓SR↑SPL↑NDTW↑SDTW↑NE↓ SR↑SPL↑NDTW↑SDTW↑ CWP-CMA [16]
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Evaluation on the RxR-CE dataset. # Representation Methods NE↓OSR↑SR↑SPL↑ 1 Single View 4.71 64.71 57.21 49.15 2
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Comparison among different candidate location represen- tation methods on the val unseen split of the R2R-CE dataset. Comparisons among different representation methods. For ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Average cosine similarity between predicted future views and ground truth at different distances between candidate locations and agent, on the val unseen split ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | As illustrated in Table 1, for the val unseen split of the R2R-CE dataset, our model outperforms our baseline method ETPNav [9] by 4% ... | embodiment, simulator version and control stack | p. 6 (4.2. Comparison to State-of-the-Art Methods), p. 7 (4.3. Ablation Study) |
| Task/environment | Comparison among different candidate location representation methods on the val unseen split of the R2R-CE dataset. | reset, timeout, object/scene variation | p. 7 (4.3. Ablation Study), p. 8 (4.3. Ablation Study) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 5 (3.2. Hierarchical Neural Radiance Representation), p. 6 (3.3. Architecture of the Lookahead VLN model) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 3 (3.2. Hierarchical Neural Radiance Representation), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| There are several standard metrics [5] in VLN for evaluating the agent's performance, including Trajectory Length (TL), Navigation Error (NE), Success Rate (SR), SR ... | definition/direction/unit from same section | p. 6 (4.1. Datasets and Evaluation Metrics) |
| As illustrated in Table 1, for the val unseen split of the R2R-CE dataset, our model outperforms our baseline method ETPNav [9] by 4% ... | definition/direction/unit from same section | p. 6 (4.2. Comparison to State-of-the-Art Methods) |
| NeRF-based RGB rendering method [24] has a low image reconstruction accuracy in unseen environments due to the visual occlusions and high information redundancy of ... | definition/direction/unit from same section | p. 7 (4.3. Ablation Study) |
| Row 2 doesn't use the lookahead node scores to evaluate the future paths and gain marginal performance improvement, confirming the necessity of the lookahead ... | definition/direction/unit from same section | p. 8 (4.3. Ablation Study) |
| The lookahead node closest to the destination (i.e., Hard target) is not sure of the highest semantic match score with the instruction due to ... | definition/direction/unit from same section | p. 8 (4.3. Ablation Study) |
| Evaluation on the RxR-CE dataset. # Representation Methods NE↓OSR↑SR↑SPL↑ 1 Single View 4.71 64.71 57.21 49.15 2 NeRF Rendering 4.79 65.14 56.55 48.61 3 ... | definition/direction/unit from same section | p. 7 (4.3. Ablation Study) |
| Figure 1. Illustration of different methods to represent the naviga- ble candidate locations. (a) uses the single-view observation (yel- low sector area). (b) uses ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 4. The framework of the lookahead VLN model. In addi- tion to the stop embedding (black), three types of nodes are used to ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As illustrated in Table 1, for the val unseen split of the R2R-CE dataset, our model outperforms our baseline method ETPNav [9] by 4% ... | comparison identity and matched condition | p. 6 (4.2. Comparison to State-of-the-Art Methods) |
| For the test unseen split, the proposed method outperforms ETPNav by 3% on SR and 2% on SPL. | comparison identity and matched condition | p. 6 (4.2. Comparison to State-of-the-Art Methods) |
| Figure 1. Illustration of different methods to represent the naviga- ble candidate locations. (a) uses the single-view observation (yel- low sector area). (b) uses ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Comparisons among different representation methods. | comparison identity and matched condition | p. 7 (4.3. Ablation Study) |
| As shown in Table 3, without the training objective Lregion of region-level semantic alignment (row 6) in Section 3.2.3, the performance of the HNR ... | comparison identity and matched condition | p. 7 (4.3. Ablation Study) |
| Ablation study of the lookahead VLN model. | comparison identity and matched condition | p. 8 (23.1 Hz (42.3 ms)) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The effect of different numbers of nearest features in the HNR model on the val unseen split of the R2R-CE dataset. | component/input/data sensitivity | p. 8 (4.3. Ablation Study) |
| As shown in Table 3, without the training objective Lregion of region-level semantic alignment (row 6) in Section 3.2.3, the performance of the HNR ... | component/input/data sensitivity | p. 7 (4.3. Ablation Study) |
| Ablation study of the lookahead VLN model. | component/input/data sensitivity | p. 8 (23.1 Hz (42.3 ms)) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, our main contributions include: • We propose a hierarchical neural radiance representation model to produce multi-level semantic representations for future environments ... | Compared with DREAMWALKER [39] in Table 1, which adopts a similar idea of lookahead exploration, our HNR model achieves performance improvement of about 10% ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. Comparison to State-of-the-Art Methods), p. 6 (4.2. Comparison to State-of-the-Art Methods), p. 8 (4.3. Ablation Study), p. 7 (4.3. Ablation Study), p. 8 (4.3. Ablation Study), p. 7 (4.3. Ablation Study) |
| Primary metric/result | Meanwhile, as illustrated in Table 2, the proposed method also achieves the improvement of 2% in the majority of metrics on the RxR-CE dataset. | numeric claim only at cited anchor | p. 6 (4.2. Comparison to State-of-the-Art Methods) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Datasets and Evaluation Metrics - extractive body cue:** It includes trajectories that are diverse in terms of length (average is 15 meters), which is more challenging in the continuous environments.
- **p. 7 / 4.3. Ablation Study - extractive body cue:** Using regionlevel alignment, our HNR method has the best representation quality and its cosine similarity is above 0.8 overall, supporting the lookahead exploration well within ...
- **p. 8 / 23.1 Hz (42.3 ms) - extractive body cue:** Runtime analysis measured on one RTX 3090 GPU. # Slookahead Scandidate Soft Hard NE↓OSR↑SR↑SPL↑ 1 4.71 64.71 57.21 49.15 2 ✓ ✓ 4.71 66.43 57.75 ...
- **p. 3 / 3.1. Navigation Setups - extractive body cue:** At time step t, the agent observes panoramic RGB images Rt = {rt,i}12 i=1 and the depth images Dt = {dt,i}12 i=1 surrounding its current ...
- **p. 4 / 3.2. Hierarchical Neural Radiance Representation - extractive body cue:** Specifically, for each region-level representation, the HNR model uniformly samples N points {Pn/n = 1, ..., N} along the ray from the camera position P1 ...
- **p. 4 / 3.2. Hierarchical Neural Radiance Representation - extractive body cue:** With all latent vectors {r}N n=1 of N sampled points, we use the volume rendering method [28] to produce a region feature Rh,w for future ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Without the position and orientation of the k-nearest features relative to the sampled point (row 7) in Table 3, MLPfeature network cannot accurately estimate ... | p. 8 (4.3. Ablation Study) |
| body limitation/failure cue | The lookahead node closest to the destination (i.e., Hard target) is not sure of the highest semantic match score with the instruction due to ... | p. 8 (4.3. Ablation Study) |
| body limitation/failure cue | Figure 1. Illustration of different methods to represent the naviga- ble candidate locations. (a) uses the single-view observation (yel- low sector area). (b) uses ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Hierarchical encoding and multi-level semantic alignment help HNR integrate surrounding contexts and predict features of empty regions caused by visual occlusions. | p. 7 (4.3. Ablation Study) |
| body limitation/failure cue | As shown in Table 3, without the training objective Lregion of region-level semantic alignment (row 6) in Section 3.2.3, the performance of the HNR ... | p. 7 (4.3. Ablation Study) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Runtime analysis measured on one RTX 3090 GPU. # Slookahead Scandidate Soft Hard NE↓OSR↑SR↑SPL↑ 1 4.71 64.71 57.21 49.15 2 ✓ ✓ 4.71 66.43 ... | p. 8 (23.1 Hz (42.3 ms)) |
| Since the k-nearest features search has a heavy computational cost in our HNR model, we use the CUDA implementation of KD-Tree algorithm [14] to ... | p. 8 (4.3. Ablation Study) |
| During navigation, the agent's visual observations are encoded and stored into the feature cloud. | p. 3 (3.1. Navigation Setups) |
| Secondly, region-level embeddings within the same future view are fed into the view encoder and obtain the entire future view representation. | p. 3 (3.1. Navigation Setups) |
| The positional embedding is encoded as: qk = LN(W1[P rel k , θrel k , sk]) (6) where LN denotes layer normalization and W1 ... | p. 4 (3.2. Hierarchical Neural Radiance Representation) |
| View Encoder Panorama level Encoding 𝐌𝐋𝐏௙௘௔௧௨௥௘ … K-nearest features search Latent vector Prediction Panorama Encoder … … View level Encoding Region level Encoding Candidate ... | p. 4 (3.2. Hierarchical Neural Radiance Representation) |
| The view encoder consists of four-layer transformers. | p. 5 (3.2. Hierarchical Neural Radiance Representation) |
| The maximum number of action steps per episode is set to 15. | p. 5 (3.2. Hierarchical Neural Radiance Representation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4.3. Ablation Study - extractive body cue:** Without the position and orientation of the k-nearest features relative to the sampled point (row 7) in Table 3, MLPfeature network cannot accurately estimate the ...
- **p. 8 / 4.3. Ablation Study - extractive body cue:** The lookahead node closest to the destination (i.e., Hard target) is not sure of the highest semantic match score with the instruction due to visual ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Illustration of different methods to represent the naviga- ble candidate locations. (a) uses the single-view observation (yel- low sector area). (b) uses the ...
- **p. 7 / 4.3. Ablation Study - extractive body cue:** Hierarchical encoding and multi-level semantic alignment help HNR integrate surrounding contexts and predict features of empty regions caused by visual occlusions.
- **p. 7 / 4.3. Ablation Study - extractive body cue:** As shown in Table 3, without the training objective Lregion of region-level semantic alignment (row 6) in Section 3.2.3, the performance of the HNR model ...

- **Evidence anchors reviewed:** datasets p. 6 (4.2. Comparison to State-of-the-Art Methods), p. 7 (4.3. Ablation Study), p. 8 (4.3. Ablation Study), p. 8 (4.3. Ablation Study), p. 6 (4.1. Datasets and Evaluation Metrics), p. 7 (4.3. Ablation Study), metrics p. 6 (4.1. Datasets and Evaluation Metrics), p. 6 (4.2. Comparison to State-of-the-Art Methods), p. 7 (4.3. Ablation Study), p. 8 (4.3. Ablation Study), p. 8 (4.3. Ablation Study), p. 7 (4.3. Ablation Study), baselines p. 6 (4.2. Comparison to State-of-the-Art Methods), p. 6 (4.2. Comparison to State-of-the-Art Methods), p. 1 (Figure/Table caption), p. 7 (4.3. Ablation Study), p. 7 (4.3. Ablation Study), p. 8 (23.1 Hz (42.3 ms)), results p. 6 (4.2. Comparison to State-of-the-Art Methods), p. 6 (4.2. Comparison to State-of-the-Art Methods), p. 8 (4.3. Ablation Study), p. 7 (4.3. Ablation Study), p. 8 (4.3. Ablation Study), p. 7 (4.3. Ablation Study).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (10 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** As illustrated in Table 1, for the val unseen split of the R2R-CE dataset, our model outperforms our baseline method ETPNav [9] by 4% on SR and 2% on SPL. (p. 6, 4.2. Comparison to State-of-the-Art Methods).
- **Metric evidence:** There are several standard metrics [5] in VLN for evaluating the agent's performance, including Trajectory Length (TL), Navigation Error (NE), Success Rate (SR), SR given the Oracle stop policy (OSR), ... (p. 6, 4.1. Datasets and Evaluation Metrics).
- **Baseline/ablation evidence:** As illustrated in Table 1, for the val unseen split of the R2R-CE dataset, our model outperforms our baseline method ETPNav [9] by 4% on SR and 2% on SPL. (p. 6, 4.2. Comparison to State-of-the-Art Methods).
- **Failure/negative evidence:** Without the position and orientation of the k-nearest features relative to the sampled point (row 7) in Table 3, MLPfeature network cannot accurately estimate the volume density and fails to ... (p. 8, 4.3. Ablation Study).
