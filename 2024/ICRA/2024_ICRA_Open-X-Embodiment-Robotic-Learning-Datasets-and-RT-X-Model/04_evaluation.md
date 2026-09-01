# Evaluation - Open X-Embodiment: Robotic Learning Datasets and RT-X Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2310.08864; PDF retrieval source: https://arxiv.org/pdf/2310.08864. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 1 (Figure/Table caption)): Our results showed that the RT-1X policy has a 50% higher success rate than the original, state-of-the-art methods contributed by different collaborating institutions, while the bigger vision-language-modelbased version (RT-2-X) demonst ...

## Evaluation Body Digest

- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** Row Model Size History Length Dataset Co-Trained w/ Web Initial Checkpoint Emergent Skills Evaluation RT-2 Generalization Evaluation (1) RT-2 55B none Google Robot action Yes ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** These tasks involve objects and skills that are not present in the RT-2 dataset but occur in the Bridge dataset [95] for a different robot ...
- **p. 5 / V. EXPERIMENTAL RESULTS - extractive body cue:** Our experiments answer three questions about the effect of X-embodiment training: (1) Can policies trained on our X-embodiment dataset effectively enable positive transfer, such that ...
- **p. 5 / V. EXPERIMENTAL RESULTS - extractive body cue:** For small-scale dataset experiments, we use Kitchen Manipulation [128], Cable Routing [129], NYU Door Opening [130], AUTOLab UR5 [132], and Robot Play [134].
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** We also note that the 55B model has significantly higher success rate in the Emergent Skills compared to the 5B model (row (2) vs row ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** Our results showed that the RT-1X policy has a 50% higher success rate than the original, state-of-the-art methods contributed by different collaborating institutions, while the ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: RT-1-X mean success rate is 50% higher than that of either the Original Method or RT-1. RT-1 and RT-1-X have the same network ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We propose an open, large-scale dataset for robot learning curated from 21 institutions across the globe. The dataset represents diverse behaviors, robot embodiments ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** V. EXPERIMENTAL RESULTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTAL RESULTS | BENCHMARK / DATASET | Our results showed that the RT-1X policy has a 50% higher success rate than the original, state-of-the-art methods contributed by different collaborating institutions, while ... | p. 6 (V. EXPERIMENTAL RESULTS) |
| V. EXPERIMENTAL RESULTS | BENCHMARK / DATASET | However, the larger RT-2-X model outperforms both the Original Method and RT-1 suggesting that X-robot training can improve performance in the data-rich domains, but ... | p. 5 (V. EXPERIMENTAL RESULTS) |
| V. EXPERIMENTAL RESULTS | BENCHMARK / DATASET | 4), where we would expect transfer from larger datasets to significantly improve performance, and evaluation on domains that have large-scale datasets (Table I), where ... | p. 5 (V. EXPERIMENTAL RESULTS) |
| V. EXPERIMENTAL RESULTS | BENCHMARK / DATASET | We note that including a short history of images significantly improves generalization performance (row (4) vs row (5)). | p. 6 (V. EXPERIMENTAL RESULTS) |
| Figure/Table caption | BENCHMARK / DATASET | Fig. 1: We propose an open, large-scale dataset for robot learning curated from 21 institutions across the globe. The dataset represents diverse behaviors, robot ... | p. 1 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** Row Model Size History Length Dataset Co-Trained w/ Web Initial Checkpoint Emergent Skills Evaluation RT-2 Generalization Evaluation (1) RT-2 55B none Google Robot action Yes ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** These tasks involve objects and skills that are not present in the RT-2 dataset but occur in the Bridge dataset [95] for a different robot ...
- **p. 5 / V. EXPERIMENTAL RESULTS - extractive body cue:** Our experiments answer three questions about the effect of X-embodiment training: (1) Can policies trained on our X-embodiment dataset effectively enable positive transfer, such that ...
- **p. 5 / V. EXPERIMENTAL RESULTS - extractive body cue:** For small-scale dataset experiments, we use Kitchen Manipulation [128], Cable Routing [129], NYU Door Opening [130], AUTOLab UR5 [132], and Robot Play [134].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We propose an open, large-scale dataset for robot learning curated from 21 institutions across the globe. The dataset represents diverse behaviors, robot embodiments ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: The Open X-Embodiment Dataset. (a): the dataset consists of 60 individual datasets across 22 embodiments. (b): the Franka robot has the largest diversity ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: RT-1-X and RT-2-X both take images and a text instruction as input and output discretized end-effector actions. RT-1-X is an architecture designed for ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: RT-1-X mean success rate is 50% higher than that of either the Original Method or RT-1. RT-1 and RT-1-X have the same network ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: To assess transfer between embodiments, we evaluate the RT-2-X model on out-of-distribution skills. These skills are in the Bridge dataset, but not in ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Row Model Size History Length Dataset Co-Trained w/ Web Initial Checkpoint Emergent Skills Evaluation RT-2 Generalization Evaluation (1) RT-2 55B none Google Robot action ... | embodiment, simulator version and control stack | p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |
| Task/environment | These tasks involve objects and skills that are not present in the RT-2 dataset but occur in the Bridge dataset [95] for a different ... | reset, timeout, object/scene variation | p. 6 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (5 Hz), p. 4 (IV. RT-X DESIGN) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 3 (III. THE OPEN X-EMBODIMENT REPOSITORY), p. 1 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We also note that the 55B model has significantly higher success rate in the Emergent Skills compared to the 5B model (row (2) vs ... | definition/direction/unit from same section | p. 6 (V. EXPERIMENTAL RESULTS) |
| Our results showed that the RT-1X policy has a 50% higher success rate than the original, state-of-the-art methods contributed by different collaborating institutions, while ... | definition/direction/unit from same section | p. 6 (V. EXPERIMENTAL RESULTS) |
| Fig. 4: RT-1-X mean success rate is 50% higher than that of either the Original Method or RT-1. RT-1 and RT-1-X have the same ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Fig. 1: We propose an open, large-scale dataset for robot learning curated from 21 institutions across the globe. The dataset represents diverse behaviors, robot ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| For each small dataset domain, we compare the performance of the RT-1-X model, and for each large dataset we consider both the RT-1-X and ... | definition/direction/unit from same section | p. 5 (V. EXPERIMENTAL RESULTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In the largedataset setting, the RT-1-X model does not outperform the RT-1 baseline trained on only the embodiment-specific dataset, which indicates underfitting for that ... | comparison identity and matched condition | p. 5 (V. EXPERIMENTAL RESULTS) |
| Throughout this evaluation we compare with two baseline models: (1) The model developed by the creators of the dataset trained only on that respective ... | comparison identity and matched condition | p. 5 (V. EXPERIMENTAL RESULTS) |
| We also note that the 55B model has significantly higher success rate in the Emergent Skills compared to the 5B model (row (2) vs ... | comparison identity and matched condition | p. 6 (V. EXPERIMENTAL RESULTS) |
| Comparing rows (1) and (2), we find that RT-2-X outperforms RT-2 by ∼3×, suggesting that incorporating data from other robots into the training improves ... | comparison identity and matched condition | p. 6 (V. EXPERIMENTAL RESULTS) |
| Fig. 2: The Open X-Embodiment Dataset. (a): the dataset consists of 60 individual datasets across 22 embodiments. (b): the Franka robot has the largest ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Our next ablation involves removing the Bridge dataset from RT-2-X training: Row (3) shows the results for RT-2X that includes all data used for ... | component/input/data sensitivity | p. 6 (V. EXPERIMENTAL RESULTS) |
| Row Model Size History Length Dataset Co-Trained w/ Web Initial Checkpoint Emergent Skills Evaluation RT-2 Generalization Evaluation (1) RT-2 55B none Google Robot action ... | component/input/data sensitivity | p. 6 (V. EXPERIMENTAL RESULTS) |
| Our experiments answer three questions about the effect of X-embodiment training: (1) Can policies trained on our X-embodiment dataset effectively enable positive transfer, such ... | component/input/data sensitivity | p. 5 (V. EXPERIMENTAL RESULTS) |
| Fig. 2: The Open X-Embodiment Dataset. (a): the dataset consists of 60 individual datasets across 22 embodiments. (b): the Franka robot has the largest ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| Fig. 1: We propose an open, large-scale dataset for robot learning curated from 21 institutions across the globe. The dataset represents diverse behaviors, robot ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Addressing goal (1), our empirical contribution is to demonstrate that several recent robotic learning methods, with minimal modification, can utilize X-embodiment data and enable ... | Our results showed that the RT-1X policy has a 50% higher success rate than the original, state-of-the-art methods contributed by different collaborating institutions, while ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 1 (Figure/Table caption) |
| Primary metric/result | However, the larger RT-2-X model outperforms both the Original Method and RT-1 suggesting that X-robot training can improve performance in the data-rich domains, but ... | numeric claim only at cited anchor | p. 5 (V. EXPERIMENTAL RESULTS) |

- Numeric sentences retained from the body:
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** Our results suggest that co-training with data from other platforms imbues the RT-2X controller with additional skills for the platform that are not present in ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** Our next ablation involves removing the Bridge dataset from RT-2-X training: Row (3) shows the results for RT-2X that includes all data used for RT-2-X ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** DISCUSSION, FUTURE WORK, AND OPEN PROBLEMS We presented a consolidated dataset that combines data from 22 robotic embodiments collected through a collaboration between 21 institutions, ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** Our results showed that the RT-1X policy has a 50% higher success rate than the original, state-of-the-art methods contributed by different collaborating institutions, while the ...
- **p. 2 / Abstract - extractive body cue:** We assemble a dataset from 22 different robots collected through a collaboration between 21 institutions, demonstrating 527 skills (160266 tasks).
- **p. 3 / III. THE OPEN X-EMBODIMENT REPOSITORY - extractive body cue:** More specifically, we provide and maintain the following open-source resources to the broader community: • Open X-Embodiment Dataset: robot learning dataset with 1M+ robot trajectories ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In the largedataset setting, the RT-1-X model does not outperform the RT-1 baseline trained on only the embodiment-specific dataset, which indicates underfitting for that ... | p. 5 (V. EXPERIMENTAL RESULTS) |
| body limitation/failure cue | DISCUSSION, FUTURE WORK, AND OPEN PROBLEMS We presented a consolidated dataset that combines data from 22 robotic embodiments collected through a collaboration between 21 ... | p. 6 (V. EXPERIMENTAL RESULTS) |
| body limitation/failure cue | 5: To assess transfer between embodiments, we evaluate the RT-2-X model on out-of-distribution skills. | p. 6 (V. EXPERIMENTAL RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| At inference time, each model is run at the rate required for the robot (3-10 Hz), with RT-1 run locally and RT-2 hosted on ... | p. 5 (IV. RT-X DESIGN) |
| To answer these questions we conduct the total number of 3600 evaluation trials across 6 different robots. | p. 5 (V. EXPERIMENTAL RESULTS) |
| While RT-X demonstrates a step towards a X-embodied robot generalist, many more steps are needed to make this future a reality. | p. 6 (V. EXPERIMENTAL RESULTS) |
| In addition, we provided multiple resources for the robotics community to explore the Xembodiment robot learning research, including: the unified X-robot and X-institution dataset, ... | p. 6 (V. EXPERIMENTAL RESULTS) |
| In domains from NLP to Computer Vision, this has led to a consolidation of pretrained models, with general pretrained backbones serving as a starting ... | p. 1 (Abstract) |
| However, these lessons are difficult to apply in robotics: any single robotic domain might be too narrow, and while computer vision and NLP can ... | p. 2 (I. INTRODUCTION) |
| We introduce the Open X-Embodiment Repository (robotics-transformer-x.github.io) - an open-source repository which includes large-scale data along with pre-trained model checkpoints for X-embodied robot learning ... | p. 3 (III. THE OPEN X-EMBODIMENT REPOSITORY) |
| More specifically, we provide and maintain the following open-source resources to the broader community: • Open X-Embodiment Dataset: robot learning dataset with 1M+ robot ... | p. 3 (III. THE OPEN X-EMBODIMENT REPOSITORY) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / V. EXPERIMENTAL RESULTS - extractive body cue:** In the largedataset setting, the RT-1-X model does not outperform the RT-1 baseline trained on only the embodiment-specific dataset, which indicates underfitting for that model ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** DISCUSSION, FUTURE WORK, AND OPEN PROBLEMS We presented a consolidated dataset that combines data from 22 robotic embodiments collected through a collaboration between 21 institutions, ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** 5: To assess transfer between embodiments, we evaluate the RT-2-X model on out-of-distribution skills.

- **PDF anchors reviewed:** datasets p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), metrics p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 5 (Figure/Table caption), p. 1 (Figure/Table caption), p. 5 (V. EXPERIMENTAL RESULTS), baselines p. 5 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 3 (Figure/Table caption), results p. 6 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
