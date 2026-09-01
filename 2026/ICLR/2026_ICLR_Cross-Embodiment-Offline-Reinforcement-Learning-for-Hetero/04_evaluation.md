# Evaluation - Cross-Embodiment Offline Reinforcement Learning for Heterogeneous Robot Datasets

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10010454; PDF retrieval source: https://arxiv.org/pdf/2602.18025. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (1 INTRODUCTION), p. 8 (1 INTRODUCTION), p. 9 (1 INTRODUCTION), p. 14 (Figure/Table caption), p. 10 (1 INTRODUCTION), p. 10 (1 INTRODUCTION)): From the table, EG achieves the most stable and substantial improvement on the 70% Suboptimal Forward dataset (+14.41, +38.34%).

## Evaluation Body Digest

- **p. 7 / 1 INTRODUCTION - extractive PDF cue:** Preprint (a) Embodiment-based similarity matrix (b) Average gradient cosine similarity matrix (c) Embodiment-based similarity vs. mean gradient cosine similarity Figure 3: (a) Embodiment-based similarity matrix ...
- **p. 8 / 1 INTRODUCTION - extractive PDF cue:** 5.3 EMBODIMENT-GROUPED OFFLINE RL UPDATE Algorithm 1 Embodiment-Grouped Offline RL Require: Robot groups {G1, . . . , GM}, dataset D Ensure: Policy θπ; critics/targets ...
- **p. 9 / 1 INTRODUCTION - extractive PDF cue:** The gains are especially large when the dataset contains more suboptimal trajectories, as in the replay and 70% Suboptimal splits.
- **p. 7 / 1 INTRODUCTION - extractive PDF cue:** We represent each robot's embodiment as a graph to quantify inter-robot distances.
- **p. 8 / 1 INTRODUCTION - extractive PDF cue:** Details on the robot graph construction and FGW distance hyperparameters are given in Appendix E.
- **p. 9 / 1 INTRODUCTION - extractive PDF cue:** Tab.4 reports the mean final return and variance on the 70% Suboptimal Forward dataset.
- **p. 10 / 1 INTRODUCTION - extractive PDF cue:** We observe that with the 70% Suboptimal Forward dataset, the advantage of EG persists even after normalization.
- **p. 10 / 1 INTRODUCTION - extractive PDF cue:** 5; performance peaks at small to moderate M, whereas excessive partitioning leads to a slight degradation (e.g., on the 70% Forward dataset the best score ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** offline robot transition/trajectory dataset과 deployment MDP.
- **Input boundary:** dataset state/observation, action, reward와 return-to-go.
- **Output/decision under evaluation:** dataset-supported action sequence.
- **Primary target:** offline policy value, OOD safety와 closed-loop success.
- **Detected evaluation headings:** B DATASET CONSTRUCTION DETAILS (p. 13); B.1 EXPERT DATASET (p. 13); B.2 EXPERT REPLAY DATASET (p. 13); B.3 X% SUBOPTIMAL DATASET (p. 13); C DATASET DETAIL (p. 14).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 1 INTRODUCTION | BENCHMARK / DATASET | From the table, EG achieves the most stable and substantial improvement on the 70% Suboptimal Forward dataset (+14.41, +38.34%). | p. 9 (1 INTRODUCTION) |
| 1 INTRODUCTION | BENCHMARK / DATASET | First, we evaluate performance improvements in cross-embodiment offline RL on six datasets containing varying proportions of suboptimal data. | p. 8 (1 INTRODUCTION) |
| 1 INTRODUCTION | BENCHMARK / DATASET | It is somewhat surprising that the Heuristic split did not improve performance. | p. 9 (1 INTRODUCTION) |
| Figure/Table caption | BENCHMARK / DATASET | Table 7: Reward coefficients rc and curriculum length T for each robot. C DATASET DETAIL Figure 7 overlays histograms of the total reward per ... | p. 14 (Figure/Table caption) |
| 1 INTRODUCTION | BENCHMARK / DATASET | Because M also determines the number of policy updates per batch, smaller M reduces the number of updates and thus improves computational efficiency. | p. 10 (1 INTRODUCTION) |

## Dataset / Benchmark Role

- **p. 7 / 1 INTRODUCTION - extractive PDF cue:** Preprint (a) Embodiment-based similarity matrix (b) Average gradient cosine similarity matrix (c) Embodiment-based similarity vs. mean gradient cosine similarity Figure 3: (a) Embodiment-based similarity matrix ...
- **p. 8 / 1 INTRODUCTION - extractive PDF cue:** 5.3 EMBODIMENT-GROUPED OFFLINE RL UPDATE Algorithm 1 Embodiment-Grouped Offline RL Require: Robot groups {G1, . . . , GM}, dataset D Ensure: Policy θπ; critics/targets ...
- **p. 9 / 1 INTRODUCTION - extractive PDF cue:** The gains are especially large when the dataset contains more suboptimal trajectories, as in the replay and 70% Suboptimal splits.
- **p. 7 / 1 INTRODUCTION - extractive PDF cue:** We represent each robot's embodiment as a graph to quantify inter-robot distances.
- **p. 8 / 1 INTRODUCTION - extractive PDF cue:** Details on the robot graph construction and FGW distance hyperparameters are given in Appendix E.
- **p. 9 / 1 INTRODUCTION - extractive PDF cue:** Tab.4 reports the mean final return and variance on the 70% Suboptimal Forward dataset.
- **p. 10 / 1 INTRODUCTION - extractive PDF cue:** We observe that with the 70% Suboptimal Forward dataset, the advantage of EG persists even after normalization.
- **p. 10 / 1 INTRODUCTION - extractive PDF cue:** 5; performance peaks at small to moderate M, whereas excessive partitioning leads to a slight degradation (e.g., on the 70% Forward dataset the best score ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive PDF cue:** Table 1: BC vs. IQL performance across datasets (mean ± standard error over 5 seeds).
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 1: Comparison of learning curves between cross-embodiment pre-trained networks and net- works trained without cross-embodiment pre-training for Badger, Unitree G1, and Cassie. "leave-one-out" experiment. ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2: Expert vs. 70% Suboptimal IQL performance across robots and avg. gradient cosine similarity C on the 70% subop- timal dataset. Cells shaded blue ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 2: Fraction of negative pairwise gradient cosine sim- ilarities. Expert 30%-suboptimal 70%-suboptimal 0.00 0.05 0.10
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. The resulting correlation, r = 0.815, indicates a strong positive relationship: robots that exhibit positive transfer have more aligned gradients, whereas those with ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3: (a) Embodiment-based similarity matrix (1 - min-max-normalized FGW distance between robot pairs); (b) Gradient cosine similarity matrix in Expert Forward dataset from Section ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: Overview of Embodiment Grouping (EG) for cross-embodiment offline RL. 5.3 EMBODIMENT-GROUPED OFFLINE RL UPDATE Algorithm 1 Embodiment-Grouped Offline RL Require: Robot groups {G1, ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 3: Each Algorithm Performance across Dataset (± is Standard Error, 5 seeds)

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Preprint (a) Embodiment-based similarity matrix (b) Average gradient cosine similarity matrix (c) Embodiment-based similarity vs. mean gradient cosine similarity Figure 3: (a) Embodiment-based similarity ... | embodiment, simulator version and control stack | p. 7 (1 INTRODUCTION), p. 8 (1 INTRODUCTION) |
| Task/environment | 5.3 EMBODIMENT-GROUPED OFFLINE RL UPDATE Algorithm 1 Embodiment-Grouped Offline RL Require: Robot groups {G1, . . . , GM}, dataset D Ensure: Policy θπ; ... | reset, timeout, object/scene variation | p. 8 (1 INTRODUCTION), p. 9 (1 INTRODUCTION) |
| Observation/sensor | dataset state/observation, action, reward와 return-to-go | calibration, preprocessing, privileged input | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Output/decision | dataset-supported action sequence | action frame, controller and termination | p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 7: Reward coefficients rc and curriculum length T for each robot. C DATASET DETAIL Figure 7 overlays histograms of the total reward per ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| 5; performance peaks at small to moderate M, whereas excessive partitioning leads to a slight degradation (e.g., on the 70% Forward dataset the best ... | definition/direction/unit from same section | p. 10 (1 INTRODUCTION) |
| Figure 7: Overlaid histograms of per-episode total reward (x-axis) vs. episode proportion (y-axis) for Forward datasets across all robots. Each panel corresponds to a ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| Table 1: BC vs. IQL performance across datasets (mean ± standard error over 5 seeds). | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Table 3: Each Algorithm Performance across Dataset (± is Standard Error, 5 seeds) | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Method Final return Relative % IQL (baseline) 37.57 ± 0.78 0.00% Random grouping 38.73 ± 2.03 +3.08% Heuristic 34.45 ± 1.97 -8.31% EG (ours) ... | definition/direction/unit from same section | p. 9 (1 INTRODUCTION) |
| Table 6: Reward terms composing the reward function. Coefficients for each robot are listed in | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| Taken together, these results suggest that relatively small values, M=2 ∼4, already yield strong gains; a practical strategy is to start with a small ... | definition/direction/unit from same section | p. 10 (1 INTRODUCTION) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to the IQL cross-embodiment baseline, the average improvement in the Suboptimal datasets 70% is 7.15% for PCGrad, 18.33% for SEL and 33.99% for ... | comparison identity and matched condition | p. 9 (1 INTRODUCTION) |
| To remove this effect, we also run a compute-normalized comparison in which, for the IQL baseline, we multiply the total number of optimizer steps ... | comparison identity and matched condition | p. 10 (1 INTRODUCTION) |
| As single-method baselines, we include Behavior Cloning (BC) using the same network architecture as our offline RL backbones, TD3+BC (Fujimoto & Gu, 2021) as ... | comparison identity and matched condition | p. 8 (1 INTRODUCTION) |
| EG yields consistent benefits across a range of offline learning baselines. | comparison identity and matched condition | p. 9 (1 INTRODUCTION) |
| Figure 1: Comparison of learning curves between cross-embodiment pre-trained networks and net- works trained without cross-embodiment pre-training for Badger, Unitree G1, and Cassie. "leave-one-out" ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Second, we conduct ablation studies to isolate the contributions of (i) grouping strategy, comparing random grouping, an intuitive biped / quadruped split and our ... | comparison identity and matched condition | p. 8 (1 INTRODUCTION) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| (ii) Sensitivity to the group count M We evaluate the effect of the number of Embodiment Grouping clusters M by sweeping M over {1, ... | component/input/data sensitivity | p. 10 (1 INTRODUCTION) |
| Figure 1: Comparison of learning curves between cross-embodiment pre-trained networks and net- works trained without cross-embodiment pre-training for Badger, Unitree G1, and Cassie. "leave-one-out" ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| To remove this effect, we also run a compute-normalized comparison in which, for the IQL baseline, we multiply the total number of optimizer steps ... | component/input/data sensitivity | p. 10 (1 INTRODUCTION) |
| Finally, to assess the effect of our embodiment-based grouping strategy across different learning backbones, we report Embodiment Grouping (EG) counterparts of BC, TD3+BC, and ... | component/input/data sensitivity | p. 8 (1 INTRODUCTION) |
| We denote these variants as BC+EG, TD3+BC+EG, and IQL+EG (ours), respectively. | component/input/data sensitivity | p. 8 (1 INTRODUCTION) |
| The variant that combines IQL with Embodiment Grouping achieves the best average performance. | component/input/data sensitivity | p. 9 (1 INTRODUCTION) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| 3.3 NETWORK ARCHITECTURE In this section, we present our approach to cross-embodiment learning in an offline RL setting. | From the table, EG achieves the most stable and substantial improvement on the 70% Suboptimal Forward dataset (+14.41, +38.34%). | PDF body cue; verify exact table/figure and matched conditions | p. 9 (1 INTRODUCTION), p. 8 (1 INTRODUCTION), p. 9 (1 INTRODUCTION), p. 14 (Figure/Table caption), p. 10 (1 INTRODUCTION), p. 10 (1 INTRODUCTION) |
| Primary metric/result | First, we evaluate performance improvements in cross-embodiment offline RL on six datasets containing varying proportions of suboptimal data. | numeric claim only at cited anchor | p. 8 (1 INTRODUCTION) |

- Numeric sentences retained from the body:
- **p. 7 / 1 INTRODUCTION - extractive PDF cue:** Preprint (a) Embodiment-based similarity matrix (b) Average gradient cosine similarity matrix (c) Embodiment-based similarity vs. mean gradient cosine similarity Figure 3: (a) Embodiment-based similarity matrix ...
- **p. 9 / 1 INTRODUCTION - extractive PDF cue:** Method Final return Relative % IQL (baseline) 37.57 ± 0.78 0.00% Random grouping 38.73 ± 2.03 +3.08% Heuristic 34.45 ± 1.97 -8.31% EG (ours) 51.98 ...
- **p. 10 / 1 INTRODUCTION - extractive PDF cue:** Method (mean ± SEM) Normalized IQL 44.20 ± 2.22 IQL + EG 51.98 ± 1.70 ∆R +7.78 (iii) Compute- and data-normalized comparison EG performs M ...
- **p. 4 / 1 INTRODUCTION - extractive PDF cue:** IQL performance across datasets (mean ± standard error over 5 seeds).
- **p. 4 / 1 INTRODUCTION - extractive PDF cue:** Dataset BC IQL Expert Forward 63.31 ± 0.10 63.39 ± 0.05 Expert Backward 67.17 ± 0.01 67.10 ± 0.01 Expert Replay Forward 49.71 ± 1.06 ...
- **p. 7 / 1 INTRODUCTION - extractive PDF cue:** Preprint (a) Embodiment-based similarity matrix (b) Average gradient cosine similarity matrix (c) Embodiment-based similarity vs. mean gradient cosine similarity Figure 3: (a) Embodiment-based similarity matrix ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We also identified a core failure mode, inter-robot gradient conflicts, whose incidence grows with both the proportion of suboptimal data and the number of ... | p. 10 (7 CONCLUSION) |
| body limitation/failure cue | We leave this combined direction for future work. | p. 10 (7 CONCLUSION) |
| body limitation/failure cue | Table 2: Expert vs. 70% Suboptimal IQL performance across robots and avg. gradient cosine similarity C on the 70% subop- timal dataset. Cells shaded ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | A likely reason is that coarse categories such as leg count cannot capture gradient-relevant factors like actuator placement, link lengths, mass distribution, and joint ... | p. 9 (1 INTRODUCTION) |
| body limitation/failure cue | In contrast, Random yields only a small gain (+1.16, +3.08%), and the intuitive fourway split Heuristic actually degrades performance (-3.14, -8.31%). | p. 9 (1 INTRODUCTION) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| To remove this effect, we also run a compute-normalized comparison in which, for the IQL baseline, we multiply the total number of optimizer steps ... | p. 10 (1 INTRODUCTION) |
| We encode each robot as a morphology graph, compute pairwise distances, and cluster robots accordingly. | p. 2 (1 INTRODUCTION) |
| Second, we conduct ablation studies to isolate the contributions of (i) grouping strategy, comparing random grouping, an intuitive biped / quadruped split and our ... | p. 8 (1 INTRODUCTION) |
| 5, the wall-clock training time grows substantially with M. | p. 10 (1 INTRODUCTION) |
| Collecting manipulation data is time-consuming and expensive, and each new task requires careful teleoperation, specialized hardware, and often manual labeling, making data scaling difficult. | p. 1 (1 INTRODUCTION) |
| Episodes may end according to a terminal condition encoded in the transition tuples through a termination indicator dt ∈{0, 1}. | p. 3 (1 INTRODUCTION) |
| IQL performance across datasets (mean ± standard error over 5 seeds). | p. 4 (1 INTRODUCTION) |
| Specifically, we encode each action with an action encoder to obtain a latent action vector, which we then concatenate with the latent representation of ... | p. 4 (1 INTRODUCTION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 7 CONCLUSION - extractive PDF cue:** We also identified a core failure mode, inter-robot gradient conflicts, whose incidence grows with both the proportion of suboptimal data and the number of embodiments.
- **p. 10 / 7 CONCLUSION - extractive PDF cue:** We leave this combined direction for future work.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2: Expert vs. 70% Suboptimal IQL performance across robots and avg. gradient cosine similarity C on the 70% subop- timal dataset. Cells shaded blue ...
- **p. 9 / 1 INTRODUCTION - extractive PDF cue:** A likely reason is that coarse categories such as leg count cannot capture gradient-relevant factors like actuator placement, link lengths, mass distribution, and joint couplings.
- **p. 9 / 1 INTRODUCTION - extractive PDF cue:** In contrast, Random yields only a small gain (+1.16, +3.08%), and the intuitive fourway split Heuristic actually degrades performance (-3.14, -8.31%).

- **PDF anchors reviewed:** datasets p. 7 (1 INTRODUCTION), p. 8 (1 INTRODUCTION), p. 9 (1 INTRODUCTION), p. 7 (1 INTRODUCTION), p. 8 (1 INTRODUCTION), p. 9 (1 INTRODUCTION), metrics p. 14 (Figure/Table caption), p. 10 (1 INTRODUCTION), p. 15 (Figure/Table caption), p. 4 (Figure/Table caption), p. 9 (Figure/Table caption), p. 9 (1 INTRODUCTION), baselines p. 9 (1 INTRODUCTION), p. 10 (1 INTRODUCTION), p. 8 (1 INTRODUCTION), p. 9 (1 INTRODUCTION), p. 5 (Figure/Table caption), p. 8 (1 INTRODUCTION), results p. 9 (1 INTRODUCTION), p. 8 (1 INTRODUCTION), p. 9 (1 INTRODUCTION), p. 14 (Figure/Table caption), p. 10 (1 INTRODUCTION), p. 10 (1 INTRODUCTION).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
