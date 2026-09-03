# Evaluation - Robot Data Curation with Mutual Information Estimators

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p023.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p023.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup), p. 7 (A. Experimental Setup), p. 15 (Figure/Table caption), p. 15 (Figure/Table caption), p. 16 (Figure/Table caption)): Following Gandhi et al, [25], we use a measure of demonstration "compatibility" to score data.

## Evaluation Body Digest

- **p. 6 / A. Experimental Setup - extractive body cue:** The multi-human datasets from the RoboMimic benchmark [50] include 100 demonstrations from each of three robot operators for three tasks in increasing difficulty: "Lift" where ...
- **p. 6 / A. Experimental Setup - extractive body cue:** 1) Datasets: ‘To assess the performance of different robot demonstration curation techniques, we perform experiments ‘on a broad set of datasets spanning simulated, real singlearm, ...
- **p. 7 / A. Experimental Setup - extractive body cue:** 4 Average qulity of demonstrations remaining in datasets after filtering with diferent choices of $ onthe Lift Can, and stasis fom the Robomimichenchak wih ts ...
- **p. 7 / A. Experimental Setup - extractive body cue:** We compare to InfoNCE as CLIP is ‘commonly used to curate datasets in vision and language [6+] MINE (MI.
- **p. 19 / C. Implementation Derails - extractive body cue:** Method Parameter ___RoboMimic State _Robotimic Image Franka ReboCrowd
- **p. 6 / A. Experimental Setup - extractive body cue:** Following Gandhi et al, [25], we use a measure of demonstration "compatibility" to score data.
- **p. 6 / A. Experimental Setup - extractive body cue:** We use VIP to estimate data quality by considering the total predicted reward over a demonstration.
- **p. 7 / A. Experimental Setup - extractive body cue:** For all experiments we use the Adam optimizer with leaming rate 0.0001 and a bateh size of 256.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** A. Experimental Setup (p. 6); C. Implementation Derails (p. 18).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| A. Experimental Setup | EMPIRICAL / SIMULATION | Following Gandhi et al, [25], we use a measure of demonstration "compatibility" to score data. | p. 6 (A. Experimental Setup) |
| A. Experimental Setup | EMPIRICAL / SIMULATION | We measure the performance of different data curation methods from both state, in which ground truth object information is provided, as well as third-person ... | p. 6 (A. Experimental Setup) |
| A. Experimental Setup | EMPIRICAL / SIMULATION | Results are shown as an average of 3 secs. | p. 7 (A. Experimental Setup) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Fig. 13. RoboMimic Policy learing performance from sate | p. 15 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Fig. 12. The performance of different mutual information estimators on the Franks Datasets, cut from the main text du to space | p. 15 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / A. Experimental Setup - extractive body cue:** The multi-human datasets from the RoboMimic benchmark [50] include 100 demonstrations from each of three robot operators for three tasks in increasing difficulty: "Lift" where ...
- **p. 6 / A. Experimental Setup - extractive body cue:** 1) Datasets: ‘To assess the performance of different robot demonstration curation techniques, we perform experiments ‘on a broad set of datasets spanning simulated, real singlearm, ...
- **p. 7 / A. Experimental Setup - extractive body cue:** 4 Average qulity of demonstrations remaining in datasets after filtering with diferent choices of $ onthe Lift Can, and stasis fom the Robomimichenchak wih ts ...
- **p. 7 / A. Experimental Setup - extractive body cue:** We compare to InfoNCE as CLIP is ‘commonly used to curate datasets in vision and language [6+] MINE (MI.
- **p. 19 / C. Implementation Derails - extractive body cue:** Method Parameter ___RoboMimic State _Robotimic Image Franka ReboCrowd

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3. Visualization of the tasks represented in the datasets we use inthis work, including the Can MH, Lift MH, and Square MH datasets from ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5. Average quality of demonstrations remaining
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6. Average quality of demonstrations remaining in datasets after itering vith diferent choices of S on the Franka Datasets. Average of 3 sds
- **p. 15 / Figure/Table caption - extractive body cue:** Fig. 12. The performance of different mutual information estimators on the Franks Datasets, cut from the main text du to space
- **p. 15 / Figure/Table caption - extractive body cue:** Fig. 13. RoboMimic Policy learing performance from sate
- **p. 15 / Figure/Table caption - extractive body cue:** Fig. 14. ‘The elect of diferent values of k 0a RoboCrowd
- **p. 16 / Figure/Table caption - extractive body cue:** Fig. 16. The effect of diferent lateat dimension sizes for 5 and =, 0a RoboMimic Image. we fad that performance is relatively sobust to this ...
- **p. 16 / Figure/Table caption - extractive body cue:** Fig. 17. The effect of difereat values of VAE on RoboMimic Image. We find that performance is relatively robust to this parameter for RoboMimic.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The multi-human datasets from the RoboMimic benchmark [50] include 100 demonstrations from each of three robot operators for three tasks in increasing difficulty: "Lift" ... | embodiment, simulator version and control stack | p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup) |
| Task/environment | 1) Datasets: ‘To assess the performance of different robot demonstration curation techniques, we perform experiments ‘on a broad set of datasets spanning simulated, real ... | reset, timeout, object/scene variation | p. 6 (A. Experimental Setup), p. 7 (A. Experimental Setup) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 1 (1. Iyrropucrion), p. 2 (A. Imitation Learning) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 3 (B. Demonstration Curation), p. 4 (B. Maximizing Marginal Action Entropy) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Following Gandhi et al, [25], we use a measure of demonstration "compatibility" to score data. | definition/direction/unit from same section | p. 6 (A. Experimental Setup) |
| We use VIP to estimate data quality by considering the total predicted reward over a demonstration. | definition/direction/unit from same section | p. 6 (A. Experimental Setup) |
| For all experiments we use the Adam optimizer with leaming rate 0.0001 and a bateh size of 256. | definition/direction/unit from same section | p. 7 (A. Experimental Setup) |
| We compare to InfoNCE as CLIP is ‘commonly used to curate datasets in vision and language [6+] MINE (MI. | definition/direction/unit from same section | p. 7 (A. Experimental Setup) |
| Fig. 13. RoboMimic Policy learing performance from sate | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| Fig. 12. The performance of different mutual information estimators on the Franks Datasets, cut from the main text du to space | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| Fig. 17. The effect of difereat values of VAE on RoboMimic Image. We find that performance is relatively robust to this parameter for RoboMimic. | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| Fig. 16. The effect of diferent lateat dimension sizes for 5 and =, 0a RoboMimic Image. we fad that performance is relatively sobust to ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 2) Baselines: We compare against a number of different data quality estimators from prior work in addition to a number of alternative mutual information ... | comparison identity and matched condition | p. 6 (A. Experimental Setup) |
| For each dataset we use the same architecture forall methods, where the latent = dimension is set to be consistent across both Demlnf and ... | comparison identity and matched condition | p. 7 (A. Experimental Setup) |
| Following prior works in active learning for imitation learning [18,31], we select data based on the uncertainty of an ensemble of 5 policies. | comparison identity and matched condition | p. 6 (A. Experimental Setup) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We additionally evaluate on versions of these datasets ("HiChew", "TootsieRoll, "HersheyKiss") where the unstructured play data has been removed, but where demonstrations still contain ... | component/input/data sensitivity | p. 6 (A. Experimental Setup) |
| Fig. 17. The effect of difereat values of VAE on RoboMimic Image. We find that performance is relatively robust to this parameter for RoboMimic. | component/input/data sensitivity | p. 16 (Figure/Table caption) |
| Fig. 16. The effect of diferent lateat dimension sizes for 5 and =, 0a RoboMimic Image. we fad that performance is relatively sobust to ... | component/input/data sensitivity | p. 16 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| come this challenge we propose Demonstration Information Estimation, which uses k-nearest-neighbor (k-NN) estimates of mutual information, Our method involves three steps - representation learning, ... | Following Gandhi et al, [25], we use a measure of demonstration "compatibility" to score data. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup), p. 7 (A. Experimental Setup), p. 15 (Figure/Table caption), p. 15 (Figure/Table caption), p. 16 (Figure/Table caption) |
| Primary metric/result | We measure the performance of different data curation methods from both state, in which ground truth object information is provided, as well as third-person ... | numeric claim only at cited anchor | p. 6 (A. Experimental Setup) |

- Numeric sentences retained from the body:
- **p. 7 / A. Experimental Setup - extractive body cue:** Images resized to $4 x 84 for RoboMimie and 128 x 128 otherwise.
- **p. 7 / A. Experimental Setup - extractive body cue:** State-based models are trained for 50,000 steps and image based models are trained for 100,000 steps using VMs provided by a Google TPU Research Cloud ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | variance across seeds, while the parametric estimators were more unstable and had one or two runs that performed far worse than the others. | p. 8 (C. Mutual Information Estimators) |
| body limitation/failure cue | Note that while this metric makes sense for active learning, it does not necessarily make sense in the offline setting, and in some ways ... | p. 6 (A. Experimental Setup) |
| body limitation/failure cue | This is particularly problematic for downstream data curation, as one often does not have ground truth labels to check the quality of the scoring ... | p. 8 (C. Mutual Information Estimators) |
| body limitation/failure cue | DemInf's performance is generally robust to this parameter, with no substantial change in performance in both HersheyKiss and Square MH. | p. 9 (C. Mutual Information Estimators) |
| body limitation/failure cue | Fig. 17. The effect of difereat values of VAE on RoboMimic Image. We find that performance is relatively robust to this parameter for RoboMimic. | p. 16 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We run three seeds for all methods, More details and hyperparameters can be found in Appendix . | p. 7 (A. Experimental Setup) |
| ‘Opuimizer ‘Adar Leaning Rate o0e01 1 Batch Size 256, A Training Steps 50,000 100,000 tion Chunk n 1 4 0 Image Resolution oss. | p. 19 (C. Implementation Derails) |
| When training VAEs from images we use matching ResNet-18 Decoder networks for ‘each view. | p. 7 (A. Experimental Setup) |
| For VAEs we use a symmetric decoder. | p. 18 (C. Implementation Derails) |
| For all methods using a state encoder, we use this architecture. | p. 18 (C. Implementation Derails) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / C. Mutual Information Estimators - extractive body cue:** variance across seeds, while the parametric estimators were more unstable and had one or two runs that performed far worse than the others.
- **p. 6 / A. Experimental Setup - extractive body cue:** Note that while this metric makes sense for active learning, it does not necessarily make sense in the offline setting, and in some ways may ...
- **p. 8 / C. Mutual Information Estimators - extractive body cue:** This is particularly problematic for downstream data curation, as one often does not have ground truth labels to check the quality of the scoring function,
- **p. 9 / C. Mutual Information Estimators - extractive body cue:** DemInf's performance is generally robust to this parameter, with no substantial change in performance in both HersheyKiss and Square MH.
- **p. 16 / Figure/Table caption - extractive body cue:** Fig. 17. The effect of difereat values of VAE on RoboMimic Image. We find that performance is relatively robust to this parameter for RoboMimic.

- **Evidence anchors reviewed:** datasets p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup), p. 7 (A. Experimental Setup), p. 7 (A. Experimental Setup), p. 19 (C. Implementation Derails), metrics p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup), p. 7 (A. Experimental Setup), p. 7 (A. Experimental Setup), p. 15 (Figure/Table caption), p. 15 (Figure/Table caption), baselines p. 6 (A. Experimental Setup), p. 7 (A. Experimental Setup), p. 6 (A. Experimental Setup), results p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup), p. 7 (A. Experimental Setup), p. 15 (Figure/Table caption), p. 15 (Figure/Table caption), p. 16 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
