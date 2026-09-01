# Evaluation - Tree Skeletonization from 3D Point Clouds by Denoising Diffusion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Marks_Tree_Skeletonization_from_3D_Point_Clouds_by_Denoising_Diffusion_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Marks_Tree_Skeletonization_from_3D_Point_Clouds_by_Denoising_Diffusion_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.2. Performance on multi-variety synthetic dataset), p. 7 (4.2. Performance on multi-variety synthetic dataset), p. 6 (4.1. Experimental setup), p. 6 (4.1. Experimental setup), p. 8 (4.4. Performance on BReTS dataset), p. 8 (4.4. Performance on BReTS dataset)): In fact, our approach still outperforms all baselines in the F1-Score, which gives a more complete picture than precision or recall individually.

## Evaluation Body Digest

- **p. 6 / 4.1. Experimental setup - extractive PDF cue:** To test the performance on real-world data, we evaluated our method on our apple orchard dataset presented in Sec.
- **p. 6 / 4.1. Experimental setup - extractive PDF cue:** We also defined the train, validation and test splits by randomly splitting the dataset in a 80%, 10%, and 10% for each tree species, as ...
- **p. 7 / 4.1. Experimental setup - extractive PDF cue:** The batch size and the learning rate were tuned on the validation set of the different datasets.
- **p. 7 / 4.2. Performance on multi-variety synthetic dataset - extractive PDF cue:** In the first experiment, we evaluate the performance of our skeletonization approach on the TreeNet3D dataset.
- **p. 8 / 4.4. Performance on BReTS dataset - extractive PDF cue:** Qualitative results on the BReTS dataset.
- **p. 8 / 4.4. Performance on BReTS dataset - extractive PDF cue:** Notice that our predictions are topological tree structures, however this is not always visible due to perfect overlap with the reference. the scan are leaves, ...
- **p. 6 / 4.1. Experimental setup - extractive PDF cue:** To evaluate the tree skeletonization performance, we use commonly used metrics: the Chamfer distance, precision, recall, and F1-score.
- **p. 6 / 4.1. Experimental setup - extractive PDF cue:** Approach Chamfer Precision Recall F1-Score distance [cm] ↓ [%] ↑ [%] ↑ [%] ↑ AdTree [15] 0.91 73.64 93.72 79.30 LBC [6] 2.55 72.79 50.12 ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4. Experiments and Discussions (p. 6); 4.1. Experimental setup (p. 6); 4.2. Performance on multi-variety synthetic dataset (p. 7); 4.3. Performance on synthetic apple tree dataset (p. 7); 4.4. Performance on BReTS dataset (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Performance on multi-variety synthetic dataset | EMPIRICAL / REAL-ROBOT OR HARDWARE | In fact, our approach still outperforms all baselines in the F1-Score, which gives a more complete picture than precision or recall individually. | p. 7 (4.2. Performance on multi-variety synthetic dataset) |
| 4.2. Performance on multi-variety synthetic dataset | EMPIRICAL / REAL-ROBOT OR HARDWARE | 1, we outperform all baselines in the Chamfer distance and F1-Score, showing that our predicted skeletons are closer to the reference and more accurate. | p. 7 (4.2. Performance on multi-variety synthetic dataset) |
| 4.1. Experimental setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | To evaluate the tree skeletonization performance, we use commonly used metrics: the Chamfer distance, precision, recall, and F1-score. | p. 6 (4.1. Experimental setup) |
| 4.1. Experimental setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | Skeletonization performance on TreeNet3D dataset (normalized by variety). | p. 6 (4.1. Experimental setup) |
| 4.4. Performance on BReTS dataset | EMPIRICAL / REAL-ROBOT OR HARDWARE | Qualitative results on the BReTS dataset. | p. 8 (4.4. Performance on BReTS dataset) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experimental setup - extractive PDF cue:** To test the performance on real-world data, we evaluated our method on our apple orchard dataset presented in Sec.
- **p. 6 / 4.1. Experimental setup - extractive PDF cue:** We also defined the train, validation and test splits by randomly splitting the dataset in a 80%, 10%, and 10% for each tree species, as ...
- **p. 7 / 4.1. Experimental setup - extractive PDF cue:** The batch size and the learning rate were tuned on the validation set of the different datasets.
- **p. 7 / 4.2. Performance on multi-variety synthetic dataset - extractive PDF cue:** In the first experiment, we evaluate the performance of our skeletonization approach on the TreeNet3D dataset.
- **p. 8 / 4.4. Performance on BReTS dataset - extractive PDF cue:** Qualitative results on the BReTS dataset.
- **p. 8 / 4.4. Performance on BReTS dataset - extractive PDF cue:** Notice that our predictions are topological tree structures, however this is not always visible due to perfect overlap with the reference. the scan are leaves, ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Our approach generates tree skeletons (right) of real orchard trees (left) from colorized point clouds (middle). We leverage a denoising diffusion probabilistic model ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of our tree skeletonization approach. Given a tree and its point cloud scan S, we define the initial set of nodes MT ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 2. In the following, we first describe the DDPM formu- lation and then we present our formulation to adapt it to the tree skeletonization ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Tree skeleton graph. We define the tree skeleton G as a graph with nodes V (in red) and edges E (in black). This ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Skeletonization performance on TreeNet3D dataset (normalized by variety). Best performance with respect to a par- ticular metric is bold and the second best ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Skeletonization performance on Smart-Tree apple data branches. Best performance with respect to a particular met- ric is bold and the second best is ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Skeletonization performance on our Orchard dataset. Best performance with respect to a particular metric is bold and the second best is underlined.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative results on the BReTS dataset. From the comparison it can be seen that the predictions of our method follow more closely the ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To test the performance on real-world data, we evaluated our method on our apple orchard dataset presented in Sec. | embodiment, simulator version and control stack | p. 6 (4.1. Experimental setup), p. 6 (4.1. Experimental setup) |
| Task/environment | We also defined the train, validation and test splits by randomly splitting the dataset in a 80%, 10%, and 10% for each tree species, ... | reset, timeout, object/scene variation | p. 6 (4.1. Experimental setup), p. 7 (4.1. Experimental setup) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 3 (3. Our Approach), p. 2 (1. Introduction) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 2 (1. Introduction), p. 4 (3. Our Approach) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| To evaluate the tree skeletonization performance, we use commonly used metrics: the Chamfer distance, precision, recall, and F1-score. | definition/direction/unit from same section | p. 6 (4.1. Experimental setup) |
| Approach Chamfer Precision Recall F1-Score distance [cm] ↓ [%] ↑ [%] ↑ [%] ↑ AdTree [15] 0.91 73.64 93.72 79.30 LBC [6] 2.55 72.79 ... | definition/direction/unit from same section | p. 6 (4.1. Experimental setup) |
| Still, it is able to outperform the baselines on the Chamfer distance metric and is a close second on the F1-Score metric, which combines ... | definition/direction/unit from same section | p. 7 (4.3. Performance on synthetic apple tree dataset) |
| Approach Chamfer Precision Recall F1-Score distance [cm] ↓ [%] ↑ [%] ↑ [%] ↑ AdTree [15] 4.55 29.48 49.31 36.06 LBC [6] 8.10 23.70 ... | definition/direction/unit from same section | p. 7 (4.1. Experimental setup) |
| For completeness we also tested the standard deviation of the predictions of our approach with different random initializations which is 0.047 cm on the ... | definition/direction/unit from same section | p. 8 (4.4. Performance on BReTS dataset) |
| Smart-Tree [13] still has significantly more false positives than our approach, which can also be seen in the precision and Chamfer distance metrics reported ... | definition/direction/unit from same section | p. 8 (4.4. Performance on BReTS dataset) |
| Figure 1. Our approach generates tree skeletons (right) of real orchard trees (left) from colorized point clouds (middle). We leverage a denoising diffusion probabilistic ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 3. Tree skeleton graph. We define the tree skeleton G as a graph with nodes V (in red) and edges E (in black). ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As baselines, we use state-of-the-art methods for tree skeletonization. | comparison identity and matched condition | p. 6 (4.1. Experimental setup) |
| 2 show that our method with a value of 7.66 cm achieves the best Chamfer distance compared to the baselines. | comparison identity and matched condition | p. 7 (4.3. Performance on synthetic apple tree dataset) |
| In fact, our approach still outperforms all baselines in the F1-Score, which gives a more complete picture than precision or recall individually. | comparison identity and matched condition | p. 7 (4.2. Performance on multi-variety synthetic dataset) |
| From the comparison it can be seen that the predictions of our method follow more closely the structure of the reference, and has less ... | comparison identity and matched condition | p. 8 (4.4. Performance on BReTS dataset) |
| Notice that our predictions are topological tree structures, however this is not always visible due to perfect overlap with the reference. the scan are ... | comparison identity and matched condition | p. 8 (4.4. Performance on BReTS dataset) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Notice that our predictions are topological tree structures, however this is not always visible due to perfect overlap with the reference. the scan are ... | component/input/data sensitivity | p. 8 (4.4. Performance on BReTS dataset) |
| AdTree [15] creates an initial skeleton by building the minimum spanning tree of the point cloud and then prunes the initial tree skeleton by ... | component/input/data sensitivity | p. 7 (4.1. Experimental setup) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our key contributions are: • A tree skeletonization approach using 3D point clouds as input that employs a novel diffusion-based formulation for ... | In fact, our approach still outperforms all baselines in the F1-Score, which gives a more complete picture than precision or recall individually. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.2. Performance on multi-variety synthetic dataset), p. 7 (4.2. Performance on multi-variety synthetic dataset), p. 6 (4.1. Experimental setup), p. 6 (4.1. Experimental setup), p. 8 (4.4. Performance on BReTS dataset), p. 8 (4.4. Performance on BReTS dataset) |
| Primary metric/result | 1, we outperform all baselines in the Chamfer distance and F1-Score, showing that our predicted skeletons are closer to the reference and more accurate. | numeric claim only at cited anchor | p. 7 (4.2. Performance on multi-variety synthetic dataset) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Experimental setup - extractive PDF cue:** Approach Chamfer Precision Recall F1-Score distance [cm] ↓ [%] ↑ [%] ↑ [%] ↑ AdTree [15] 0.91 73.64 93.72 79.30 LBC [6] 2.55 72.79 50.12 ...
- **p. 7 / 4.1. Experimental setup - extractive PDF cue:** Approach Chamfer Precision Recall F1-Score distance [cm] ↓ [%] ↑ [%] ↑ [%] ↑ AdTree [15] 4.55 29.48 49.31 36.06 LBC [6] 8.10 23.70 7.43 ...
- **p. 7 / 4.1. Experimental setup - extractive PDF cue:** As diffusion parameters, we used T = 1, 000 steps and tuned the noise factors β1 and βT for each dataset, as different tree sizes ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Those are way less than the nodes predicted by AdTree, which is a potential limitation. | p. 7 (4.2. Performance on multi-variety synthetic dataset) |
| body limitation/failure cue | This experiment, therefore, tests the realworld applicability of the compared methods, which cannot be shown on synthetic data alone. | p. 7 (4.4. Performance on BReTS dataset) |
| body limitation/failure cue | As the synthetic dataset TreeNet3D does not contain apple trees, we performed additional experiments on the simulated apple tree data provided by Dobbs et ... | p. 6 (4.1. Experimental setup) |
| body limitation/failure cue | We also defined the train, validation and test splits by randomly splitting the dataset in a 80%, 10%, and 10% for each tree species, ... | p. 6 (4.1. Experimental setup) |
| body limitation/failure cue | Due to the extreme amount of occlusions, the learned distribution of tree shapes is very effective. | p. 8 (5. Conclusion) |
| body limitation/failure cue | We showed that our method is robust to different tree species, scales, and appearances and compared its performance to state-of-the-art methods both on synthetic ... | p. 8 (5. Conclusion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The batch size and the learning rate were tuned on the validation set of the different datasets. | p. 7 (4.1. Experimental setup) |
| We trained our approach with a learning rate of 10-4 using the Adam optimizer [41]. | p. 7 (4.1. Experimental setup) |
| (13) In the tables we report the average of the metrics computed at different thresholds δ. | p. 6 (4.1. Experimental setup) |
| We then compute the metrics at 10 thresholds δ in the interval [δstart, δend] and approximate the area under curve. | p. 6 (4.1. Experimental setup) |
| In our case, we use the classifier-free guidance since it does not require a pre-trained encoder. | p. 4 (3.1. Denoising diffusion probabilistic models) |
| This can be simplified to sample xt from x0, without computing the intermediary steps x1, . . . , xt-1. | p. 4 (3.1. Denoising diffusion probabilistic models) |
| (4) to compute xT -1, . . . , x0, where x0 is a newly generated sample conditioned on c. | p. 5 (3.1. Denoising diffusion probabilistic models) |
| The trees were scanned 10 times over the whole growing season of one year with a terrestrial laser scanner (TLS). | p. 5 (3.3. Bonn Real-world Tree Skeletonization (BReTS)) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.2. Performance on multi-variety synthetic dataset - extractive PDF cue:** Those are way less than the nodes predicted by AdTree, which is a potential limitation.
- **p. 7 / 4.4. Performance on BReTS dataset - extractive PDF cue:** This experiment, therefore, tests the realworld applicability of the compared methods, which cannot be shown on synthetic data alone.
- **p. 6 / 4.1. Experimental setup - extractive PDF cue:** As the synthetic dataset TreeNet3D does not contain apple trees, we performed additional experiments on the simulated apple tree data provided by Dobbs et al.
- **p. 6 / 4.1. Experimental setup - extractive PDF cue:** We also defined the train, validation and test splits by randomly splitting the dataset in a 80%, 10%, and 10% for each tree species, as ...
- **p. 8 / 5. Conclusion - extractive PDF cue:** Due to the extreme amount of occlusions, the learned distribution of tree shapes is very effective.
- **p. 8 / 5. Conclusion - extractive PDF cue:** We showed that our method is robust to different tree species, scales, and appearances and compared its performance to state-of-the-art methods both on synthetic and ...

- **PDF anchors reviewed:** datasets p. 6 (4.1. Experimental setup), p. 6 (4.1. Experimental setup), p. 7 (4.1. Experimental setup), p. 7 (4.2. Performance on multi-variety synthetic dataset), p. 8 (4.4. Performance on BReTS dataset), p. 8 (4.4. Performance on BReTS dataset), metrics p. 6 (4.1. Experimental setup), p. 6 (4.1. Experimental setup), p. 7 (4.3. Performance on synthetic apple tree dataset), p. 7 (4.1. Experimental setup), p. 8 (4.4. Performance on BReTS dataset), p. 8 (4.4. Performance on BReTS dataset), baselines p. 6 (4.1. Experimental setup), p. 7 (4.3. Performance on synthetic apple tree dataset), p. 7 (4.2. Performance on multi-variety synthetic dataset), p. 8 (4.4. Performance on BReTS dataset), p. 8 (4.4. Performance on BReTS dataset), results p. 7 (4.2. Performance on multi-variety synthetic dataset), p. 7 (4.2. Performance on multi-variety synthetic dataset), p. 6 (4.1. Experimental setup), p. 6 (4.1. Experimental setup), p. 8 (4.4. Performance on BReTS dataset), p. 8 (4.4. Performance on BReTS dataset).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
