# Evaluation - GotenNet: Rethinking Efficient 3D Equivariant Graph Neural Networks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=5wxCQDtbMo; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/111955. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS)): GotenNetB demonstrates further improvements, achieving best performance on eleven targets and significantly improving aggregated metrics, reducing standard MAE by over 16% and log MAE by 3% compared to the best ...

## Evaluation Body Digest

- **p. 8 / 4 EXPERIMENTS - extractive body cue:** This dataset contains over 29× more graphs than QM9, with approximately 1.6× and 1.9× increases in the average number of nodes and edges per graph, ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Split Random Scaffold Task µ εHOMO εLUMO ∆ε std. log ∆ε GIN-Virtual .0882 .0692 .0632 .1036 .0592 -2.87 .2371 SchNet .0532 .0275 .0265 .0428 .0263 ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** The rMD17 dataset (Christensen & Von Lilienfeld, 2020) is a revised version of the MD17 benchmark, featuring 10 small organic molecules with 100,000 conformations per ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** The best log error of -4.65 in the random split further demonstrates the model's robustness on larger datasets.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** As shown in Table 2, GotenNet maintains its superior performance even on this larger Molecule3D dataset, achieving the lowest errors across all tasks, including µ, ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We evaluated the models on QM9, rMD17, MD22, and Molecule3D datasets.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** The proposed method is evaluated against a comprehensive set of baselines using the QM9 dataset (Ruddigkeit et al., 2012; Ramakrishnan et al., 2014).
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** We follow the standard split (Christensen & Von Lilienfeld, 2020) of 950 training, 50 validation, and the remaining conformations for testing.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | GotenNetB demonstrates further improvements, achieving best performance on eleven targets and significantly improving aggregated metrics, reducing standard MAE by over 16% and log MAE ... | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | The largest variant GotenNetL achieves state-of-the-art performance across all metrics, although the relative improvement decreases compared to GotenNetB, which suggests that dataset size may ... | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | The inclusion of structural embedding (SE), self-attention (SEA), geometric encoding (GE), and HTR generally leads to improved results, as shown in rows 1, 7, ... | p. 10 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | For molecules such as Tetrapeptide and AT-AT, GotenNet achieves notable reductions in energy errors, with improvements of 18.6% and 29.5% over the previous best ... | p. 9 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our proposed model, GotenNet, consistently outperforms state-of-the-art methods across all evaluated molecules, demonstrating superior performance in both energy and force predictions. | p. 9 (4 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 8 / 4 EXPERIMENTS - extractive body cue:** This dataset contains over 29× more graphs than QM9, with approximately 1.6× and 1.9× increases in the average number of nodes and edges per graph, ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Split Random Scaffold Task µ εHOMO εLUMO ∆ε std. log ∆ε GIN-Virtual .0882 .0692 .0632 .1036 .0592 -2.87 .2371 SchNet .0532 .0275 .0265 .0428 .0263 ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** The rMD17 dataset (Christensen & Von Lilienfeld, 2020) is a revised version of the MD17 benchmark, featuring 10 small organic molecules with 100,000 conformations per ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** The best log error of -4.65 in the random split further demonstrates the model's robustness on larger datasets.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** As shown in Table 2, GotenNet maintains its superior performance even on this larger Molecule3D dataset, achieving the lowest errors across all tasks, including µ, ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We evaluated the models on QM9, rMD17, MD22, and Molecule3D datasets.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** The proposed method is evaluated against a comprehensive set of baselines using the QM9 dataset (Ruddigkeit et al., 2012; Ramakrishnan et al., 2014).
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** We follow the standard split (Christensen & Von Lilienfeld, 2020) of 950 training, 50 validation, and the remaining conformations for testing.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Comparison of GotenNet and baseline models on the QM9 dataset. The x-axis shows the logarithmic MAE across all targets, while the y-axis shows ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Architecture of GotenNet. The overall framework (a) includes an embedding, an interaction module, and a decoder; (b) shows the geometry-aware tensor attention (GATA); ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Performance comparisons on QM9 dataset. † denotes using different data partitions. Task α ∆ε εHOMO εLUMO µ Cν
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Performance comparisons on Molecule3D
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3: Comparison of training latency of the models with respect to node count on the Molecule3D dataset. 4.2 MOLECULE3D DATASET Dataset. We further evaluate ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Comprehensive comparison of various molecular modeling methods on MD22 dataset. The results are reported in MAE of energy (kcal/mol) and forces (kcal/mol/Å) denoted ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 4: The table presents MAE for energy (kcal/mol) and forces (kcal/mol/Å) on the rMD17 dataset. Molecule NequIP ACE UNiTE Allegro BOTNet MACE
- **p. 10 / Figure/Table caption - extractive body cue:** Table 5: Ablation study on QM9 dataset. # L Lmax SE SEA GE HTR std

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This dataset contains over 29× more graphs than QM9, with approximately 1.6× and 1.9× increases in the average number of nodes and edges per ... | embodiment, simulator version and control stack | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Task/environment | Split Random Scaffold Task µ εHOMO εLUMO ∆ε std. log ∆ε GIN-Virtual .0882 .0692 .0632 .1036 .0592 -2.87 .2371 SchNet .0532 .0275 .0265 .0428 ... | reset, timeout, object/scene variation | p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (ABSTRACT), p. 2 (B L) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (B L), p. 1 (ABSTRACT) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The best log error of -4.65 in the random split further demonstrates the model's robustness on larger datasets. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| Simultaneously, force prediction errors are reduced by up to 30.4%, underscoring GotenNet's balanced performance across both metrics. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| Figure 4: Mean absolute error of the molecules for energy and forces. K RMD17 VISUALIZATIONS Figure 5 presents the MAE for energy and force ... | definition/direction/unit from same section | p. 24 (Figure/Table caption) |
| Figure 5: Mean absolute error of the molecules on rMD17 dataset for energy and forces. share the fundamental requirement of processing geometric relationships while ... | definition/direction/unit from same section | p. 25 (Figure/Table caption) |
| GotenNetB demonstrates further improvements, achieving best performance on eleven targets and significantly improving aggregated metrics, reducing standard MAE by over 16% and log MAE ... | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| These results highlight GotenNet's robustness and its ability to accurately model molecular properties, outperforming prior methods on rMD17 dataset. | definition/direction/unit from same section | p. 10 (4 EXPERIMENTS) |
| In this section, we compare the performance of GotenNet with other state-of-the-art methods. | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| Model Performance and Size Scaling Analysis. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As shown in Table 1, even our smallest variant GotenNetS outperforms baseline methods on nine out of twelve targets while surpassing baselines on std. | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| GotenNetB demonstrates further improvements, achieving best performance on eleven targets and significantly improving aggregated metrics, reducing standard MAE by over 16% and log MAE ... | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| Our proposed model, GotenNet, consistently outperforms state-of-the-art methods across all evaluated molecules, demonstrating superior performance in both energy and force predictions. | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| Table 6: Hyper-parameters for the datasets GotenNet compared against the baselines. The parameters are for GotenNetB if multiple variations exists. Hyper-parameters QM9 Molecule3D MD22 ... | comparison identity and matched condition | p. 20 (Figure/Table caption) |
| Figure 1: Comparison of GotenNet and baseline models on the QM9 dataset. The x-axis shows the logarithmic MAE across all targets, while the y-axis ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| In this section, we compare the performance of GotenNet with other state-of-the-art methods. | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The removal of any one of these components results in a significant degradation in performance, particularly in the cases without geometric encoding (row 4) ... | component/input/data sensitivity | p. 10 (4 EXPERIMENTS) |
| 4.5 ABLATION STUDY Table 5: Ablation study on QM9 dataset. # L Lmax SE SEA GE HTR std log 4 2 ✓ ✓ ✓ ... | component/input/data sensitivity | p. 10 (4 EXPERIMENTS) |
| As shown in Table 1, even our smallest variant GotenNetS outperforms baseline methods on nine out of twelve targets while surpassing baselines on std. | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| We evaluate three model variants - small (S), base (B), and large (L) - to analyze both performance and scaling behavior, with detailed specifications ... | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| Both GotenNetS and GotenNetB variants maintain consistent efficiency across all node counts, demonstrating their suitability for large-scale applications where computational overhead is critical. | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| Following the data splits from (Chmiela et al., 2023), we evaluate GotenNet against several baselines, including sDGML (Chmiela et al., 2018), ET (Thölke & ... | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address this gap, we propose a novel Geometric Tensor Network (GotenNet) that effectively models the geometric intricacies of 3D graphs while ensuring strict ... | GotenNetB demonstrates further improvements, achieving best performance on eleven targets and significantly improving aggregated metrics, reducing standard MAE by over 16% and log MAE ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |
| Primary metric/result | The largest variant GotenNetL achieves state-of-the-art performance across all metrics, although the relative improvement decreases compared to GotenNetB, which suggests that dataset size may ... | numeric claim only at cited anchor | p. 8 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** The full model with 12 layers (row 8) achieves the best performance, with the lowest std MAE of 0.56 and log MAE of -6.34.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Future work could further enhance its scalability to larger molecular systems and explore applications in molecular dynamics and materials science. | p. 10 (5 CONCLUSION) |
| body limitation/failure cue | Figure 5: Mean absolute error of the molecules on rMD17 dataset for energy and forces. share the fundamental requirement of processing geometric relationships while ... | p. 25 (Figure/Table caption) |
| body limitation/failure cue | Figure 2: Architecture of GotenNet. The overall framework (a) includes an embedding, an interaction module, and a decoder; (b) shows the geometry-aware tensor attention ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | The best log error of -4.65 in the random split further demonstrates the model's robustness on larger datasets. | p. 9 (4 EXPERIMENTS) |
| body limitation/failure cue | These results highlight the robustness and versatility of GotenNet in handling diverse molecular structures, establishing it as a leading model in both energy and ... | p. 9 (4 EXPERIMENTS) |
| body limitation/failure cue | The results are averaged over five predefined splits to ensure robust evaluation. | p. 10 (4 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Experiments were conducted with an NVIDIA A100 GPU with 80GB video memory, 512GB RAM, and an AMD EPYC 7713P CPU. | p. 7 (4 EXPERIMENTS) |
| The x-axis shows the node count, while the y-axis shows the training time per batch in milliseconds. | p. 9 (4 EXPERIMENTS) |
| We analyze computational efficiency by measuring training time across varying node counts (10-140 nodes per graph). | p. 9 (4 EXPERIMENTS) |
| Additional details on hyperparameters and scalability, as well as additional experiments, can be found in the Appendix E. | p. 7 (4 EXPERIMENTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 5 CONCLUSION - extractive body cue:** Future work could further enhance its scalability to larger molecular systems and explore applications in molecular dynamics and materials science.
- **p. 25 / Figure/Table caption - extractive body cue:** Figure 5: Mean absolute error of the molecules on rMD17 dataset for energy and forces. share the fundamental requirement of processing geometric relationships while preserving ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Architecture of GotenNet. The overall framework (a) includes an embedding, an interaction module, and a decoder; (b) shows the geometry-aware tensor attention (GATA); ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** The best log error of -4.65 in the random split further demonstrates the model's robustness on larger datasets.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** These results highlight the robustness and versatility of GotenNet in handling diverse molecular structures, establishing it as a leading model in both energy and force ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** The results are averaged over five predefined splits to ensure robust evaluation.

- **Evidence anchors reviewed:** datasets p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), metrics p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 24 (Figure/Table caption), p. 25 (Figure/Table caption), p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), baselines p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 20 (Figure/Table caption), p. 1 (Figure/Table caption), p. 7 (4 EXPERIMENTS), results p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
