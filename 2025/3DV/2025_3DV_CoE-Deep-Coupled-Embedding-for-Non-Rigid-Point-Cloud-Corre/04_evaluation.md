# Evaluation - CoE: Deep Coupled Embedding for Non-Rigid Point Cloud Correspondences

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=pIDl4wuZoG&name=pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5.7. Shape Segmentation), p. 7 (5.3. Non-isometric Shape Matching), p. 7 (5.4. Generalisation), p. 8 (5.5. Robustness), p. 6 (5. Experiments), p. 6 (5.1. Baselines)): Extensive experiments showcase that our proposed method achieves superior results in a number of non-rigid matching benchmarks and is promising in other shape analysis challenges, such as partial shape matching ...

## Evaluation Body Digest

- **p. 7 / 5.3. Non-isometric Shape Matching - extractive PDF cue:** Datasets We employ the recent non-isometric benchmark DT4D-M [27] as the testbed for this task.
- **p. 7 / 5.2. Near-isometric Shape Matching - extractive PDF cue:** The SHREC19 dataset includes 44 human shapes and is exclusively used as a test set.
- **p. 6 / 5.2. Near-isometric Shape Matching - extractive PDF cue:** Datasets We choose FAUST [6], SCAPE [1] and SHREC19 [29] as testbeds for the task of near-isometric shape matching, specifically the more recent remeshed version ...
- **p. 8 / 5.5. Robustness - extractive PDF cue:** Topology changes We employ models pre-trained on FAUST and SCAPE respectively and test on the TOPKIDS dataset [23], which contains 26 shapes of kids with ...
- **p. 8 / 5.5. Robustness - extractive PDF cue:** Generalisation from the training set SURREAL to the test set SHREC19.
- **p. 6 / 5.2. Near-isometric Shape Matching - extractive PDF cue:** The SCAPE dataset comprises 71 shapes of a single person in different poses.
- **p. 7 / 5.2. Near-isometric Shape Matching - extractive PDF cue:** Note that the mean geodesic error deteriorates in all cases, underlining the importance of smoothness of learned embeddings.
- **p. 7 / 5.2. Near-isometric Shape Matching - extractive PDF cue:** Ours produces the most accurate and smooth correspondences, despite highly nonisometric deformation (errors highlighted in red).

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.7. Shape Segmentation | EMPIRICAL / SOURCE-REPORTED EVALUATION | Extensive experiments showcase that our proposed method achieves superior results in a number of non-rigid matching benchmarks and is promising in other shape analysis ... | p. 8 (5.7. Shape Segmentation) |
| 5.3. Non-isometric Shape Matching | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method outperforms all learning based baselines. | p. 7 (5.3. Non-isometric Shape Matching) |
| 5.4. Generalisation | EMPIRICAL / SOURCE-REPORTED EVALUATION | Remarkably, ours outperforms all baselines including the multimodal meshdependent method SSMSM under this setting. | p. 7 (5.4. Generalisation) |
| 5.5. Robustness | EMPIRICAL / SOURCE-REPORTED EVALUATION | Note that all investigated methods suffer from the challenging topological changes, however ours outperforms by achieving the lowest mean geodesic error. | p. 8 (5.5. Robustness) |
| 5. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 5.1 before reporting experiment results on nearisometric and non-isometric matching in Sec. | p. 6 (5. Experiments) |

## Dataset / Benchmark Role

- **p. 7 / 5.3. Non-isometric Shape Matching - extractive PDF cue:** Datasets We employ the recent non-isometric benchmark DT4D-M [27] as the testbed for this task.
- **p. 7 / 5.2. Near-isometric Shape Matching - extractive PDF cue:** The SHREC19 dataset includes 44 human shapes and is exclusively used as a test set.
- **p. 6 / 5.2. Near-isometric Shape Matching - extractive PDF cue:** Datasets We choose FAUST [6], SCAPE [1] and SHREC19 [29] as testbeds for the task of near-isometric shape matching, specifically the more recent remeshed version ...
- **p. 8 / 5.5. Robustness - extractive PDF cue:** Topology changes We employ models pre-trained on FAUST and SCAPE respectively and test on the TOPKIDS dataset [23], which contains 26 shapes of kids with ...
- **p. 8 / 5.5. Robustness - extractive PDF cue:** Generalisation from the training set SURREAL to the test set SHREC19.
- **p. 6 / 5.2. Near-isometric Shape Matching - extractive PDF cue:** The SCAPE dataset comprises 71 shapes of a single person in different poses.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We propose a novel way to learn coupled embeddings of non-rigidly deformable shapes that are geometry-aware, robust and can be directly applied to ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Examples of LBO eigenbases and our learned coupled embeddings on a pair of non-rigidly deformed shapes. Ours are consistent while LBO eigenbases suffer ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Table 1. Summary of our notation used in the paper. is required for good performance [16, 22] (also see Sec. 5, Tab. 2), since the ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Pipeline overview. Given a pair of shapes S and T rep- resented in point clouds, Our embedding extractor - ASAP Diffu- sionNet with ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Quantitative results on FAUST, SCAPE, SHREC19, TOPKIDS and DT4D-M. The best results are highlighted, and the second best results are indicated in blue. ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative result on DT4D-M. Ours produces the most accurate and smooth correspondences, despite highly non- isometric deformation (errors highlighted in red). The SHREC19 ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Generalisation ability. The best results in each column are highlighted. Our method outperforms all learning based base- lines. Letters S,W in parentheses stand ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5. Generalisation from the training set SURREAL to the test set SHREC19. Our method generalises better compared to baselines (errors highlighted in red). Additive ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Datasets We employ the recent non-isometric benchmark DT4D-M [27] as the testbed for this task. | embodiment, simulator version and control stack | p. 7 (5.3. Non-isometric Shape Matching), p. 7 (5.2. Near-isometric Shape Matching) |
| Task/environment | The SHREC19 dataset includes 44 human shapes and is exclusively used as a test set. | reset, timeout, object/scene variation | p. 7 (5.2. Near-isometric Shape Matching), p. 6 (5.2. Near-isometric Shape Matching) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 6 (4.2. Unsupervised Loss), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Note that the mean geodesic error deteriorates in all cases, underlining the importance of smoothness of learned embeddings. | definition/direction/unit from same section | p. 7 (5.2. Near-isometric Shape Matching) |
| Ours produces the most accurate and smooth correspondences, despite highly nonisometric deformation (errors highlighted in red). | definition/direction/unit from same section | p. 7 (5.2. Near-isometric Shape Matching) |
| Our method generalises better compared to baselines (errors highlighted in red). | definition/direction/unit from same section | p. 8 (5.5. Robustness) |
| Ours is least sensitive to this noise among all competing methods (errors highlighted in red). | definition/direction/unit from same section | p. 8 (5.6. Partial Shape Matching) |
| Table 4. Ablation study of our loss and pipeline. Each loss term and network component contributes to reduce matching errors. Finally, the eigenvalues Λ ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |
| Figure 7. Visualisation of a challenging pair with crossed legs. We show our full design can successfully handle this challenge while all baseline methods ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| Figure 17. Robustness against additive noise. Ours produces stable correspondences under this noise compared to the baselines (errors highlighted in red). | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| Figure 10. Illustration of mean geodesic error under different spec- tral resolutions. Our method is robust for different choice of spec- tral resolution. We ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method outperforms all learning based baselines. | comparison identity and matched condition | p. 7 (5.3. Non-isometric Shape Matching) |
| Remarkably, ours outperforms all baselines including the multimodal meshdependent method SSMSM under this setting. | comparison identity and matched condition | p. 7 (5.4. Generalisation) |
| Our method generalises better compared to baselines (errors highlighted in red). | comparison identity and matched condition | p. 8 (5.5. Robustness) |
| Figure 17. Robustness against additive noise. Ours produces stable correspondences under this noise compared to the baselines (errors highlighted in red). | comparison identity and matched condition | p. 16 (Figure/Table caption) |
| We start this section by introducing the most relevant baselines in Sec. | comparison identity and matched condition | p. 6 (5. Experiments) |
| Compared to the noise-free case, we also have the least overall performance degradation. | comparison identity and matched condition | p. 8 (5.5. Robustness) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Please refer to the supplementary for qualitative results and additional ablation experiments. | component/input/data sensitivity | p. 7 (5.2. Near-isometric Shape Matching) |
| An interesting direction is to incorporate the advancement in SO(3)/SE(3) invariant architecture [12] to eliminate the necessity of pre-alignment. | component/input/data sensitivity | p. 8 (5.7. Shape Segmentation) |
| Table 4. Ablation study of our loss and pipeline. Each loss term and network component contributes to reduce matching errors. Finally, the eigenvalues Λ ... | component/input/data sensitivity | p. 11 (Figure/Table caption) |
| As an ablative study we disable the ASAP component hence employ the vanilla DiffusionNet as feature extractor and report its quantitative results in Tab. | component/input/data sensitivity | p. 7 (5.2. Near-isometric Shape Matching) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are: • We propose a novel unsupervised way to learn per-point embeddings directly from raw point clouds under various non-rigid ... | Extensive experiments showcase that our proposed method achieves superior results in a number of non-rigid matching benchmarks and is promising in other shape analysis ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5.7. Shape Segmentation), p. 7 (5.3. Non-isometric Shape Matching), p. 7 (5.4. Generalisation), p. 8 (5.5. Robustness), p. 6 (5. Experiments), p. 6 (5.1. Baselines) |
| Primary metric/result | Our method outperforms all learning based baselines. | numeric claim only at cited anchor | p. 7 (5.3. Non-isometric Shape Matching) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 16. Qualitative results on DT4D-M. More qualitative non-isometric matching results (top) . Failure cases mainly due to challenging topological noise (bottom) . | p. 15 (Figure/Table caption) |
| body limitation/failure cue | Limitations, Future Work and Conclusion In this paper, we proposed an unsupervised method to learn high-quality, well-generalised embeddings directly from raw point clouds. | p. 8 (5.7. Shape Segmentation) |
| body limitation/failure cue | Figure 13. Failure cases on FAUST. All three failure examples relate to the touching hands, where the points of two hands are locally mixed ... | p. 14 (Figure/Table caption) |
| body limitation/failure cue | Figure 7. Visualisation of a challenging pair with crossed legs. We show our full design can successfully handle this challenge while all baseline methods ... | p. 12 (Figure/Table caption) |
| body limitation/failure cue | Figure 10. Illustration of mean geodesic error under different spec- tral resolutions. Our method is robust for different choice of spec- tral resolution. We ... | p. 13 (Figure/Table caption) |
| body limitation/failure cue | We evaluate robustness from two perspectives: (1) random additive Gaussian noise to point clouds, (2) changes and inconsistency in shape topology. | p. 7 (5.5. Robustness) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Embedding Extractor Module computes per point intermediate embedding ˆΨ(·), which is a non-linear mapping: | p. 4 (4.1. Network Architecture) |
| It captures the local geometric information of different scales on the manifold by modelling a heat diffusion process with different timesteps and constrains the ... | p. 5 (4.1. Network Architecture) |
| The core concept of cross attention is that it computes a similarity matrix between the key and query (transformed version of ˆΨS, ˆΨT ), ... | p. 5 (4.1. Network Architecture) |
| Please see supplementary for implementation details. | p. 6 (4.2. Unsupervised Loss) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 15 / Figure/Table caption - extractive PDF cue:** Figure 16. Qualitative results on DT4D-M. More qualitative non-isometric matching results (top) . Failure cases mainly due to challenging topological noise (bottom) .
- **p. 8 / 5.7. Shape Segmentation - extractive PDF cue:** Limitations, Future Work and Conclusion In this paper, we proposed an unsupervised method to learn high-quality, well-generalised embeddings directly from raw point clouds.
- **p. 14 / Figure/Table caption - extractive PDF cue:** Figure 13. Failure cases on FAUST. All three failure examples relate to the touching hands, where the points of two hands are locally mixed and ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Figure 7. Visualisation of a challenging pair with crossed legs. We show our full design can successfully handle this challenge while all baseline methods fails ...
- **p. 13 / Figure/Table caption - extractive PDF cue:** Figure 10. Illustration of mean geodesic error under different spec- tral resolutions. Our method is robust for different choice of spec- tral resolution. We conduct ...
- **p. 7 / 5.5. Robustness - extractive PDF cue:** We evaluate robustness from two perspectives: (1) random additive Gaussian noise to point clouds, (2) changes and inconsistency in shape topology.

- **PDF anchors reviewed:** datasets p. 7 (5.3. Non-isometric Shape Matching), p. 7 (5.2. Near-isometric Shape Matching), p. 6 (5.2. Near-isometric Shape Matching), p. 8 (5.5. Robustness), p. 8 (5.5. Robustness), p. 6 (5.2. Near-isometric Shape Matching), metrics p. 7 (5.2. Near-isometric Shape Matching), p. 7 (5.2. Near-isometric Shape Matching), p. 8 (5.5. Robustness), p. 8 (5.6. Partial Shape Matching), p. 11 (Figure/Table caption), p. 12 (Figure/Table caption), baselines p. 7 (5.3. Non-isometric Shape Matching), p. 7 (5.4. Generalisation), p. 8 (5.5. Robustness), p. 16 (Figure/Table caption), p. 6 (5. Experiments), p. 8 (5.5. Robustness), results p. 8 (5.7. Shape Segmentation), p. 7 (5.3. Non-isometric Shape Matching), p. 7 (5.4. Generalisation), p. 8 (5.5. Robustness), p. 6 (5. Experiments), p. 6 (5.1. Baselines).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
