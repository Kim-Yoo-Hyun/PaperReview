# Evaluation - ElasticFusion: Dense SLAM Without A Pose Graph

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss11/p01.html; PDF retrieval source: https://www.roboticsproceedings.org/rss11/p01.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (VII. EVALUATION), p. 7 (VII. EVALUATION), p. 8 (VII. EVALUATION), p. 8 (VII. EVALUATION)): Interestingly our frame-to-model only results are also comparable in performance, whereas a uniform increase in accuracy is achieved when active to inactive model deformations are used, proving their efficacy in ...

## Evaluation Body Digest

- **p. 8 / VII. EVALUATION - extractive body cue:** The Lab dataset contains a very loopy trajectory around a large office environment with many global and local loop closures.
- **p. 7 / VII. EVALUATION - extractive body cue:** We also include trajectory estimation results for each dataset.
- **p. 7 / VII. EVALUATION - extractive body cue:** Trajectory Estimation To evaluate the trajectory estimation performance of our approach we test our system on the RGB-D benchmark of Sturm et al.
- **p. 8 / VII. EVALUATION - extractive body cue:** Name (Fig.) Copy (5i) Lab (5ii) Hotel (5iii) Office (1) Frames 5490 6533 7725 5000 Surfels 4.4×106 3.5×106 4.1×106 4.8×106 Graph nodes 351 282 328 ...
- **p. 7 / VII. EVALUATION - extractive body cue:** We evaluate the performance of our system both quantitatively and qualitatively in terms of trajectory estimation, surface reconstruction accuracy and computational performance.
- **p. 7 / VII. EVALUATION - extractive body cue:** Interestingly our frame-to-model only results are also comparable in performance, whereas a uniform increase in accuracy is achieved when active to inactive model deformations are ...
- **p. 8 / VII. EVALUATION - extractive body cue:** On surface reconstruction, local loops only scores 0.099m and global loops only scores 0.103m.
- **p. 8 / VII. EVALUATION - extractive body cue:** These results show that again our trajectory estimation performance is on par with or better than existing approaches.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** VII. EVALUATION (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| VII. EVALUATION | EMPIRICAL / SOURCE-REPORTED EVALUATION | Interestingly our frame-to-model only results are also comparable in performance, whereas a uniform increase in accuracy is achieved when active to inactive model deformations ... | p. 7 (VII. EVALUATION) |
| VII. EVALUATION | EMPIRICAL / SOURCE-REPORTED EVALUATION | These results show that our trajectory estimation performance is on par with or better than existing state-of-the-art systems that Fig. | p. 7 (VII. EVALUATION) |
| VII. EVALUATION | EMPIRICAL / SOURCE-REPORTED EVALUATION | It is also shown that our surface reconstruction results are superior to all other systems. | p. 8 (VII. EVALUATION) |
| VII. EVALUATION | EMPIRICAL / SOURCE-REPORTED EVALUATION | On surface reconstruction, local loops only scores 0.099m and global loops only scores 0.103m. | p. 8 (VII. EVALUATION) |

## Dataset / Benchmark Role

- **p. 8 / VII. EVALUATION - extractive body cue:** The Lab dataset contains a very loopy trajectory around a large office environment with many global and local loop closures.
- **p. 7 / VII. EVALUATION - extractive body cue:** We also include trajectory estimation results for each dataset.
- **p. 7 / VII. EVALUATION - extractive body cue:** Trajectory Estimation To evaluate the trajectory estimation performance of our approach we test our system on the RGB-D benchmark of Sturm et al.
- **p. 8 / VII. EVALUATION - extractive body cue:** Name (Fig.) Copy (5i) Lab (5ii) Hotel (5iii) Office (1) Frames 5490 6533 7725 5000 Surfels 4.4×106 3.5×106 4.1×106 4.8×106 Graph nodes 351 282 328 ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Comprehensive scan of an office containing over 4.5 million surfels captured in real-time. have relied on alternation and effectively per-surface-element- independent filtering [15, ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: Example SLAM sequence with active model coloured by surface normal overlaid on the inactive model in greyscale; (i) Initially all data is in ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Temporal deformation graph connectivity before loop closure. The top half shows a mapping sequence where the camera first maps left to right over ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4: Orthogonal frontal view heat maps showing reconstruc- tion error on the kt0 dataset. Points more than 0.1m from ground truth have been removed ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 5: Qualitative datasets; (i) A comprehensive scan of a copy room; (ii) A loopy large scan of a computer lab; (iii) A comprehensive scan ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Frame time vs. number of surfels on the Hotel dataset. understand the capabilities of our approach2.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The Lab dataset contains a very loopy trajectory around a large office environment with many global and local loop closures. | embodiment, simulator version and control stack | p. 8 (VII. EVALUATION), p. 7 (VII. EVALUATION) |
| Task/environment | We also include trajectory estimation results for each dataset. | reset, timeout, object/scene variation | p. 7 (VII. EVALUATION), p. 7 (VII. EVALUATION) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 2 (I. INTRODUCTION), p. 2 (II. APPROACH OVERVIEW) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We evaluate the performance of our system both quantitatively and qualitatively in terms of trajectory estimation, surface reconstruction accuracy and computational performance. | definition/direction/unit from same section | p. 7 (VII. EVALUATION) |
| Interestingly our frame-to-model only results are also comparable in performance, whereas a uniform increase in accuracy is achieved when active to inactive model deformations ... | definition/direction/unit from same section | p. 7 (VII. EVALUATION) |
| On surface reconstruction, local loops only scores 0.099m and global loops only scores 0.103m. | definition/direction/unit from same section | p. 8 (VII. EVALUATION) |
| These results show that again our trajectory estimation performance is on par with or better than existing approaches. | definition/direction/unit from same section | p. 8 (VII. EVALUATION) |
| Fig. 2: Example SLAM sequence with active model coloured by surface normal overlaid on the inactive model in greyscale; (i) Initially all data is ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Fig. 3: Temporal deformation graph connectivity before loop closure. The top half shows a mapping sequence where the camera first maps left to right ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| These results show that our trajectory estimation performance is on par with or better than existing state-of-the-art systems that Fig. | comparison identity and matched condition | p. 7 (VII. EVALUATION) |
| In Table I we compare our system to four other state-of-the-art RGB-D based SLAM systems; DVO SLAM [10], RGB-D SLAM [5], MRSMap [21] and ... | comparison identity and matched condition | p. 7 (VII. EVALUATION) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Points more than 0.1m from ground truth have been removed for visualisation purposes. | component/input/data sensitivity | p. 7 (VII. EVALUATION) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In the following, we summarise the key elements of our method. | Interestingly our frame-to-model only results are also comparable in performance, whereas a uniform increase in accuracy is achieved when active to inactive model deformations ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (VII. EVALUATION), p. 7 (VII. EVALUATION), p. 8 (VII. EVALUATION), p. 8 (VII. EVALUATION) |
| Primary metric/result | These results show that our trajectory estimation performance is on par with or better than existing state-of-the-art systems that Fig. | numeric claim only at cited anchor | p. 7 (VII. EVALUATION) |

- Numeric sentences retained from the body:
- **p. 8 / VII. EVALUATION - extractive body cue:** Name (Fig.) Copy (5i) Lab (5ii) Hotel (5iii) Office (1) Frames 5490 6533 7725 5000 Surfels 4.4×106 3.5×106 4.1×106 4.8×106 Graph nodes 351 282 328 ...
- **p. 8 / VII. EVALUATION - extractive body cue:** We recommend viewing of our accompanying videos to more clearly visualise and Milliseconds 15 20 25 30 35 40 45 50 Millions of Surfels 0 ...
- **p. 8 / VII. EVALUATION - extractive body cue:** As shown in Figure 6 the execution time of the system increases with the number of surfels in the map, with an overall average of ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In future work we wish to address the problem of map scalability beyond whole rooms and also investigate the problem of dense globally consistent ... | p. 8 (VIII. CONCLUSION) |
| body limitation/failure cue | We evaluate our approach on all four trajectories in the living room scene (including synthetic noise) providing surface reconstruction accuracy results in comparison to ... | p. 7 (VII. EVALUATION) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The test platform was a desktop PC with an Intel Core i7-4930K CPU at 3.4GHz, 32GB of RAM and an nVidia GeForce GTX 780 ... | p. 8 (VII. EVALUATION) |
| 5: Qualitative datasets; (i) A comprehensive scan of a copy room; (ii) A loopy large scan of a computer lab; (iii) A comprehensive scan ... | p. 8 (VII. EVALUATION) |
| Like many dense SLAM systems ours makes significant use of GPU programming. | p. 2 (II. APPROACH OVERVIEW) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / VIII. CONCLUSION - extractive body cue:** In future work we wish to address the problem of map scalability beyond whole rooms and also investigate the problem of dense globally consistent SLAM ...
- **p. 7 / VII. EVALUATION - extractive body cue:** We evaluate our approach on all four trajectories in the living room scene (including synthetic noise) providing surface reconstruction accuracy results in comparison to the ...

- **Evidence anchors reviewed:** datasets p. 8 (VII. EVALUATION), p. 7 (VII. EVALUATION), p. 7 (VII. EVALUATION), p. 8 (VII. EVALUATION), metrics p. 7 (VII. EVALUATION), p. 7 (VII. EVALUATION), p. 8 (VII. EVALUATION), p. 8 (VII. EVALUATION), p. 2 (Figure/Table caption), p. 4 (Figure/Table caption), baselines p. 7 (VII. EVALUATION), p. 7 (VII. EVALUATION), results p. 7 (VII. EVALUATION), p. 7 (VII. EVALUATION), p. 8 (VII. EVALUATION), p. 8 (VII. EVALUATION).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
