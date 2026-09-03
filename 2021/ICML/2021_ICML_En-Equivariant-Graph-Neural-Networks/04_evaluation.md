# Evaluation - E(n) Equivariant Graph Neural Networks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2102.09844; PDF retrieval source: https://arxiv.org/pdf/2102.09844. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (5.1. Modelling a dynamical system - N-body system), p. 15 (Figure/Table caption), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 5 (5.1. Modelling a dynamical system - N-body system), p. 6 (5.1. Modelling a dynamical system - N-body system)): Results As shown in Table 2 our model significantly outperforms the other equivariant and non-equivariant alternatives while still being efficient in terms of running time.

## Evaluation Body Digest

- **p. 5 / 5.1. Modelling a dynamical system - N-body system - extractive body cue:** Dataset: We sampled 3.000 trajectories for training, 2.000 for validation and 2.000 for testing.
- **p. 5 / 5.1. Modelling a dynamical system - N-body system - extractive body cue:** This is an equivariant task since rotations and translations on the input set of particles result in the same transformations throughout the entire trajectory.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. In the Table at the left we report the Binary Cross Entropy, % Error and F1 scores for the test partition on the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Mean Absolute Error for the molecular property prediction benchmark in QM9 dataset. *DimeNet++ uses slightly different train/val/test partitions than the other papers listed ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2. Mean Squared Error in the N-body experiment for the Ra- dial Field, GNN and EGNN methods when sweeping over different amounts of training ...
- **p. 5 / 5.1. Modelling a dynamical system - N-body system - extractive body cue:** It reduces the error with respect to the second best performing method by a 32%.
- **p. 15 / Figure/Table caption - extractive body cue:** Table 4. Analysis of the % of wrong edges and F1 score for different n embedding sizes {2, 4, 8 } for the GNN, Noise-GNN ...
- **p. 6 / 5.1. Modelling a dynamical system - N-body system - extractive body cue:** We compare the performances of our EGNN vs its non-equivariant GNN counterpart and the Radial Field algorithm.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.1. Modelling a dynamical system - N-body system | SYSTEM / EVALUATION SCOPE UNRESOLVED | Results As shown in Table 2 our model significantly outperforms the other equivariant and non-equivariant alternatives while still being efficient in terms of running ... | p. 5 (5.1. Modelling a dynamical system - N-body system) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 4. Analysis of the % of wrong edges and F1 score for different n embedding sizes {2, 4, 8 } for the GNN, ... | p. 15 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 3. Mean Absolute Error for the molecular property prediction benchmark in QM9 dataset. *DimeNet++ uses slightly different train/val/test partitions than the other papers ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 1. Example of rotation equivariance on a graph with a graph neural network φ Recently, various forms and methods to achieve E(3) or ... | p. 1 (Figure/Table caption) |
| 5.1. Modelling a dynamical system - N-body system | SYSTEM / EVALUATION SCOPE UNRESOLVED | Analysis for different number of training samples: We want to analyze the performance of our EGNN in the small and large data regime. | p. 5 (5.1. Modelling a dynamical system - N-body system) |

## Dataset / Benchmark Role

- **p. 5 / 5.1. Modelling a dynamical system - N-body system - extractive body cue:** Dataset: We sampled 3.000 trajectories for training, 2.000 for validation and 2.000 for testing.
- **p. 5 / 5.1. Modelling a dynamical system - N-body system - extractive body cue:** This is an equivariant task since rotations and translations on the input set of particles result in the same transformations throughout the entire trajectory.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Example of rotation equivariance on a graph with a graph neural network φ Recently, various forms and methods to achieve E(3) or SE(3) ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1. Comparison over different works from the literature under the message passing framework notation. We created this table with the aim to provide a ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2. Mean Squared Error for the future position estimation in the N-body system experiment, and forward time in seconds for a batch size of ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2. Mean Squared Error in the N-body experiment for the Ra- dial Field, GNN and EGNN methods when sweeping over different amounts of training ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Visual representation of a Graph Autoencoder for a 4 nodes cycle graph. The bottom row illustrates that adding noise at the input graph ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. In the Table at the left we report the Binary Cross Entropy, % Error and F1 scores for the test partition on the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Mean Absolute Error for the molecular property prediction benchmark in QM9 dataset. *DimeNet++ uses slightly different train/val/test partitions than the other papers listed ...
- **p. 15 / Figure/Table caption - extractive body cue:** Table 4. Analysis of the % of wrong edges and F1 score for different n embedding sizes {2, 4, 8 } for the GNN, Noise-GNN ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Dataset: We sampled 3.000 trajectories for training, 2.000 for validation and 2.000 for testing. | embodiment, simulator version and control stack | p. 5 (5.1. Modelling a dynamical system - N-body system), p. 5 (5.1. Modelling a dynamical system - N-body system) |
| Task/environment | This is an equivariant task since rotations and translations on the input set of particles result in the same transformations throughout the entire trajectory. | reset, timeout, object/scene variation | p. 5 (5.1. Modelling a dynamical system - N-body system) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 6 (5.2. Graph Autoencoder), p. 2 (2.1. Equivariance) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1. Introduction), p. 7 (5.2. Graph Autoencoder) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 5. In the Table at the left we report the Binary Cross Entropy, % Error and F1 scores for the test partition on ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 3. Mean Absolute Error for the molecular property prediction benchmark in QM9 dataset. *DimeNet++ uses slightly different train/val/test partitions than the other papers ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 2. Mean Squared Error in the N-body experiment for the Ra- dial Field, GNN and EGNN methods when sweeping over different amounts of ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| It reduces the error with respect to the second best performing method by a 32%. | definition/direction/unit from same section | p. 5 (5.1. Modelling a dynamical system - N-body system) |
| Table 4. Analysis of the % of wrong edges and F1 score for different n embedding sizes {2, 4, 8 } for the GNN, ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| We compare the performances of our EGNN vs its non-equivariant GNN counterpart and the Radial Field algorithm. | definition/direction/unit from same section | p. 6 (5.1. Modelling a dynamical system - N-body system) |
| Figure 1. Example of rotation equivariance on a graph with a graph neural network φ Recently, various forms and methods to achieve E(3) or ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| In this section we analyze the equivariance properties of our model for E(3) symmetries (i.e. properties 1 and 2 stated in section 2.1). | definition/direction/unit from same section | p. 3 (3.1. Analysis on E(n) equivariance) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| A Linear model that simply considers the motion equation p(t) = p(0) + v(0)t is also included as a baseline. | comparison identity and matched condition | p. 5 (5.1. Modelling a dynamical system - N-body system) |
| Results As shown in Table 2 our model significantly outperforms the other equivariant and non-equivariant alternatives while still being efficient in terms of running ... | comparison identity and matched condition | p. 5 (5.1. Modelling a dynamical system - N-body system) |
| Table 4. Analysis of the % of wrong edges and F1 score for different n embedding sizes {2, 4, 8 } for the GNN, ... | comparison identity and matched condition | p. 15 (Figure/Table caption) |
| Table 1. Comparison over different works from the literature under the message passing framework notation. We created this table with the aim to provide ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Inductively, a composition of EGCLs will also be equivariant. | component/input/data sensitivity | p. 3 (3.1. Analysis on E(n) equivariance) |
| Therefore the output hl+1 is E(n) invariant and xl+1 is E(n) equivariant to xl. | component/input/data sensitivity | p. 3 (3.1. Analysis on E(n) equivariance) |
| This is an equivariant task since rotations and translations on the input set of particles result in the same transformations throughout the entire trajectory. | component/input/data sensitivity | p. 5 (5.1. Modelling a dynamical system - N-body system) |
| Results As shown in Table 2 our model significantly outperforms the other equivariant and non-equivariant alternatives while still being efficient in terms of running ... | component/input/data sensitivity | p. 5 (5.1. Modelling a dynamical system - N-body system) |
| We compare the performances of our EGNN vs its non-equivariant GNN counterpart and the Radial Field algorithm. | component/input/data sensitivity | p. 6 (5.1. Modelling a dynamical system - N-body system) |
| E(n) Equivariant Graph Neural Networks 50.000 samples and we sweep over different amounts of data from 100 to 50.000 samples. | component/input/data sensitivity | p. 6 (5.1. Modelling a dynamical system - N-body system) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this section we introduce the relevant materials on equivariance and graph neural networks which will later complement the definition of our method. | Results As shown in Table 2 our model significantly outperforms the other equivariant and non-equivariant alternatives while still being efficient in terms of running ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (5.1. Modelling a dynamical system - N-body system), p. 15 (Figure/Table caption), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 5 (5.1. Modelling a dynamical system - N-body system), p. 6 (5.1. Modelling a dynamical system - N-body system) |
| Primary metric/result | Table 4. Analysis of the % of wrong edges and F1 score for different n embedding sizes {2, 4, 8 } for the GNN, ... | numeric claim only at cited anchor | p. 15 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 5.1. Modelling a dynamical system - N-body system - extractive body cue:** Dataset: We sampled 3.000 trajectories for training, 2.000 for validation and 2.000 for testing.
- **p. 5 / 5.1. Modelling a dynamical system - N-body system - extractive body cue:** All algorithms are composed of 4 layers and have been trained under the same conditions, batch size 100, 10.000 epochs, Adam optimizer, the learning rate ...
- **p. 5 / 5.1. Modelling a dynamical system - N-body system - extractive body cue:** We also provide the average forward pass time in seconds for each of the models for a batch of 100 samples in a GTX 1080 ...
- **p. 5 / 5.1. Modelling a dynamical system - N-body system - extractive body cue:** Mean Squared Error for the future position estimation in the N-body system experiment, and forward time in seconds for a batch size of 100 samples ...
- **p. 6 / 5.1. Modelling a dynamical system - N-body system - extractive body cue:** E(n) Equivariant Graph Neural Networks 50.000 samples and we sweep over different amounts of data from 100 to 50.000 samples.
- **p. 7 / 5.2. Graph Autoencoder - extractive body cue:** In the Figure at the right, we report the F1 score when overfitting a training partition of 100 samples in the Erdos&Renyi dataset for different ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Although we observed that adding noise to the GNN improves the results, it is difficult to exactly measure the impact of the symmetry limitation ... | p. 7 (5.2. Graph Autoencoder) |
| body limitation/failure cue | Table 3. Mean Absolute Error for the molecular property prediction benchmark in QM9 dataset. *DimeNet++ uses slightly different train/val/test partitions than the other papers ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | The symmetry problem: The above stated autoencoder may seem straightforward to implement at first sight but in some cases there is a strong limitation ... | p. 6 (5.2. Graph Autoencoder) |
| body limitation/failure cue | To avoid this limitation, all models exchange messages among all nodes and the edge information is provided as edge attributes aij = Aij in ... | p. 7 (5.2. Graph Autoencoder) |
| body limitation/failure cue | This method introduces noise sampled from a Gaussian distribution into the input node features of the graph h0 i ∼N(0, σI). | p. 6 (5.2. Graph Autoencoder) |
| body limitation/failure cue | Table 4. Analysis of the % of wrong edges and F1 score for different n embedding sizes {2, 4, 8 } for the GNN, ... | p. 15 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All algorithms are composed of 4 layers and have been trained under the same conditions, batch size 100, 10.000 epochs, Adam optimizer, the learning ... | p. 5 (5.1. Modelling a dynamical system - N-body system) |
| Mean Squared Error for the future position estimation in the N-body system experiment, and forward time in seconds for a batch size of 100 ... | p. 5 (5.1. Modelling a dynamical system - N-body system) |
| All four models have 4 layers, 64 features for the hidden layers, the Swish activation function as a non-linearity and they were all trained ... | p. 7 (5.2. Graph Autoencoder) |
| Implementation details: Our Equivariant Graph AutoEncoder is composed of an EGNN encoder followed by the decoder from Equation 9. | p. 7 (5.2. Graph Autoencoder) |
| Next, Equation 4 computes xl+1 i by a weighted sum of differences (xi -xj) which is added to xi, this transforms as a type-1 ... | p. 3 (3.1. Analysis on E(n) equivariance) |
| Visual representation of a Graph Autoencoder for a 4 nodes cycle graph. | p. 6 (5.2. Graph Autoencoder) |
| In this experiment section we use our EGNN to build an Equivariant Graph Autoencoder. | p. 6 (5.2. Graph Autoencoder) |
| Further implementation details are reported in Appendix. | p. 8 (5.2. Graph Autoencoder) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 5.2. Graph Autoencoder - extractive body cue:** Although we observed that adding noise to the GNN improves the results, it is difficult to exactly measure the impact of the symmetry limitation in ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Mean Absolute Error for the molecular property prediction benchmark in QM9 dataset. *DimeNet++ uses slightly different train/val/test partitions than the other papers listed ...
- **p. 6 / 5.2. Graph Autoencoder - extractive body cue:** The symmetry problem: The above stated autoencoder may seem straightforward to implement at first sight but in some cases there is a strong limitation regarding ...
- **p. 7 / 5.2. Graph Autoencoder - extractive body cue:** To avoid this limitation, all models exchange messages among all nodes and the edge information is provided as edge attributes aij = Aij in all ...
- **p. 6 / 5.2. Graph Autoencoder - extractive body cue:** This method introduces noise sampled from a Gaussian distribution into the input node features of the graph h0 i ∼N(0, σI).
- **p. 15 / Figure/Table caption - extractive body cue:** Table 4. Analysis of the % of wrong edges and F1 score for different n embedding sizes {2, 4, 8 } for the GNN, Noise-GNN ...

- **Evidence anchors reviewed:** datasets p. 5 (5.1. Modelling a dynamical system - N-body system), p. 5 (5.1. Modelling a dynamical system - N-body system), metrics p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 5 (Figure/Table caption), p. 5 (5.1. Modelling a dynamical system - N-body system), p. 15 (Figure/Table caption), p. 6 (5.1. Modelling a dynamical system - N-body system), baselines p. 5 (5.1. Modelling a dynamical system - N-body system), p. 5 (5.1. Modelling a dynamical system - N-body system), p. 15 (Figure/Table caption), p. 4 (Figure/Table caption), results p. 5 (5.1. Modelling a dynamical system - N-body system), p. 15 (Figure/Table caption), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 5 (5.1. Modelling a dynamical system - N-body system), p. 6 (5.1. Modelling a dynamical system - N-body system).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
