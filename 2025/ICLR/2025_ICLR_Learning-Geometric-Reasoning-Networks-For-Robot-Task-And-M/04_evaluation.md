# Evaluation - Learning Geometric Reasoning Networks For Robot Task And Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ajxAJ8GUX4; PDF retrieval source: https://openreview.net/pdf/4c142fb0625912332eff11ad284991e6692f7016.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (6 RESULTS), p. 8 (6 RESULTS), p. 9 (6 RESULTS), p. 10 (6 RESULTS), p. 8 (6 RESULTS), p. 10 (6 RESULTS)): The results show that GRN achieves a better performance than the state-of-the-art on robots with various kinematics.

## Evaluation Body Digest

- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** Panda-3D-4: This is dataset is composed of 3D environments containing 4 movable objects, 1 to 4 structures and 0 to 4 obstacles and is annotated ...
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** (2020b), we generate a dataset consisting of tabletop environments with 0 structures, 4 movable objects and up to 4 obstacles, all placed on the same ...
- **p. 9 / 6 RESULTS - extractive PDF cue:** This is due to the smaller number of training data of the PR2 dataset and the harder kinematics of the PR2 robot.
- **p. 10 / 6 RESULTS - extractive PDF cue:** We also test GRN planner in real-world setups, on both a Panda and a PR2 robots.
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** Dataset Panda-3D-4 Panda-Tabletop-4 PR2-3D-4 Task Action (F1) Grasp (F1) Action (F1) Grasp (F1) Action (F1) Grasp (F1) F-SVM - - 0.884 0.415 (± 0.220) - ...
- **p. 10 / 6 RESULTS - extractive PDF cue:** Published as a conference paper at ICLR 2025 Table 4: Evaluation of the generalizability to 3D environments with a higher number of objects compared to ...
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2025 Table 1: Comparison with SOTA methods trained and tested on different datasets.
- **p. 9 / 6 RESULTS - extractive PDF cue:** 6.3 GENERALIZABILITY EVALUATION Applicability to other robots.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 5 EXPERIMENTS (p. 6); 6 RESULTS (p. 8); A IMPLEMENTATION DETAILS (p. 14); C.2 REAL-WORLD EXPERIMENTS (p. 19); C.3 ADDITIONAL SIMULATION EXPERIMENTS (p. 19).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 6 RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results show that GRN achieves a better performance than the state-of-the-art on robots with various kinematics. | p. 9 (6 RESULTS) |
| 6 RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | This allows our model to achieve an F1 score up to 10.3% higher than other GNN-based baselines on action feasibility prediction, and up to ... | p. 8 (6 RESULTS) |
| 6 RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Moreover, the improved performance obtained using EGAT instead of classical GAT Veliˇckovi´c et al. | p. 9 (6 RESULTS) |
| 6 RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results demonstrate that our approach outperforms stateof-the-art methods, generalizing better to complex environments and robots. | p. 10 (6 RESULTS) |
| 6 RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | 6.1 COMPARISON TO PRIOR WORK Table 1 shows that our proposed model outperforms all prior works on both action feasibility and grasp types feasibility ... | p. 8 (6 RESULTS) |

## Dataset / Benchmark Role

- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** Panda-3D-4: This is dataset is composed of 3D environments containing 4 movable objects, 1 to 4 structures and 0 to 4 obstacles and is annotated ...
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** (2020b), we generate a dataset consisting of tabletop environments with 0 structures, 4 movable objects and up to 4 obstacles, all placed on the same ...
- **p. 9 / 6 RESULTS - extractive PDF cue:** This is due to the smaller number of training data of the PR2 dataset and the harder kinematics of the PR2 robot.
- **p. 10 / 6 RESULTS - extractive PDF cue:** We also test GRN planner in real-world setups, on both a Panda and a PR2 robots.
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** Dataset Panda-3D-4 Panda-Tabletop-4 PR2-3D-4 Task Action (F1) Grasp (F1) Action (F1) Grasp (F1) Action (F1) Grasp (F1) F-SVM - - 0.884 0.415 (± 0.220) - ...
- **p. 10 / 6 RESULTS - extractive PDF cue:** Published as a conference paper at ICLR 2025 Table 4: Evaluation of the generalizability to 3D environments with a higher number of objects compared to ...
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2025 Table 1: Comparison with SOTA methods trained and tested on different datasets.
- **p. 9 / 6 RESULTS - extractive PDF cue:** 6.3 GENERALIZABILITY EVALUATION Applicability to other robots.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 1: Visualization of GRN predictions on two manipulation problems, Access (Panda arm) and Clutter (PR2 Robot, predictions shown for its right arm). A single ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 2: Complete GRN architecture. A scene graph is constructed from the input 3D environ- ment. Node features of movable objects are given to IK ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 1: Comparison with SOTA methods trained and tested on different datasets. For grasp types feasibility prediction, the mean (± standard deviation) of F1 scores ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Comparison of the number of parameters and inference time on a 3D environment with 4 movable objects and 15 fixed objects (4 queries).
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 3: Ablation Study on the Panda-3D-4 dataset. For each task related to grasp types, we report the mean (± standard deviation) across all grasp ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 4: Evaluation of the generalizability to 3D environments with a higher number of objects compared to SOTA methods, when trained on the Panda-3D-4 dataset. ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 5: Performance of GRN planner compared to a non-informed planner on the Access and Clutter problems. Results are average over 10 runs on 10 ...
- **p. 14 / Figure/Table caption - extractive PDF cue:** Table 6: Decomposition of the inference time of GRN on a 3D environment with 4 mov- able objects and 15 fixed objects. Step Inference Time ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Panda-3D-4: This is dataset is composed of 3D environments containing 4 movable objects, 1 to 4 structures and 0 to 4 obstacles and is ... | embodiment, simulator version and control stack | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Task/environment | (2020b), we generate a dataset consisting of tabletop environments with 0 structures, 4 movable objects and up to 4 obstacles, all placed on the ... | reset, timeout, object/scene variation | p. 7 (5 EXPERIMENTS), p. 9 (6 RESULTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 6 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Comparing the standard deviations across F1 scores of each grasp type shows that our proposed method has a more consistent performance across the different ... | definition/direction/unit from same section | p. 8 (6 RESULTS) |
| For grasp types feasibility prediction, the mean (± standard deviation) of F1 scores of the 5 grasp types are reported. | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| Training the model without the proposed data augmentation method, yields a lower performance on all tasks, particularly on grasp types feasibility prediction and GO ... | definition/direction/unit from same section | p. 9 (6 RESULTS) |
| Results show that, although there is a decrease in F1-scores compared to the one obtained on Panda-3D-4, GRN maintains a good performance on 3D ... | definition/direction/unit from same section | p. 9 (6 RESULTS) |
| Problem Method Success Planning Nb Geometric Rate (%) time (s) Planner Calls Access Bouhsain et al. | definition/direction/unit from same section | p. 10 (6 RESULTS) |
| The proposed model is able to accurately predict action and grasp feasibility, as well as reasons of infeasibility, from estimated objects' poses in both ... | definition/direction/unit from same section | p. 10 (6 RESULTS) |
| We conduct a series of experiments in order to evaluate the performance of our proposed method compared to existing approaches, and showcase the generalization ... | definition/direction/unit from same section | p. 6 (5 EXPERIMENTS) |
| We generate a number of datasets following the method described in Appendix B. | definition/direction/unit from same section | p. 7 (5 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 6.1 COMPARISON TO PRIOR WORK Table 1 shows that our proposed model outperforms all prior works on both action feasibility and grasp types feasibility ... | comparison identity and matched condition | p. 8 (6 RESULTS) |
| MLP: This is a simple baseline which uses a 4-layer MLP that takes as input the feature vector x of an object to predict ... | comparison identity and matched condition | p. 7 (5 EXPERIMENTS) |
| Our full model shows a 7.1% gain in performance compared to the one without IK feasibility and GO predictions. | comparison identity and matched condition | p. 9 (6 RESULTS) |
| Published as a conference paper at ICLR 2025 Table 4: Evaluation of the generalizability to 3D environments with a higher number of objects compared ... | comparison identity and matched condition | p. 10 (6 RESULTS) |
| We conduct a series of experiments in order to evaluate the performance of our proposed method compared to existing approaches, and showcase the generalization ... | comparison identity and matched condition | p. 6 (5 EXPERIMENTS) |
| Feasibility-GAT (F-GAT): This baseline is an adapted version of the methods proposed by Silver et al. | comparison identity and matched condition | p. 7 (5 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We conduct two ablations to demonstrate the effectiveness of our training strategy. | component/input/data sensitivity | p. 9 (6 RESULTS) |
| MLP: This is a simple baseline which uses a 4-layer MLP that takes as input the feature vector x of an object to predict ... | component/input/data sensitivity | p. 7 (5 EXPERIMENTS) |
| Published as a conference paper at ICLR 2025 Table 3: Ablation Study on the Panda-3D-4 dataset. | component/input/data sensitivity | p. 9 (6 RESULTS) |
| Feasibility-GCN (F-GCN): This baseline uses the same scene representation as F-GAT, except that GAT is replaced with a Graph Convolution Network (GCN), which does ... | component/input/data sensitivity | p. 7 (5 EXPERIMENTS) |
| During the fine-tuning stage, the complete GRN model is trained for 100 epochs with a batch size of 2048 and a learning rate of ... | component/input/data sensitivity | p. 14 (A IMPLEMENTATION DETAILS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The contributions of this paper are threefold: (1) We propose a novel GNN-based model for efficient and accurate action and grasp feasibility prediction in ... | The results show that GRN achieves a better performance than the state-of-the-art on robots with various kinematics. | PDF body cue; verify exact table/figure and matched conditions | p. 9 (6 RESULTS), p. 8 (6 RESULTS), p. 9 (6 RESULTS), p. 10 (6 RESULTS), p. 8 (6 RESULTS), p. 10 (6 RESULTS) |
| Primary metric/result | This allows our model to achieve an F1 score up to 10.3% higher than other GNN-based baselines on action feasibility prediction, and up to ... | numeric claim only at cited anchor | p. 8 (6 RESULTS) |

- Numeric sentences retained from the body:
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2025 conduct our experiments using mainly the Franka Emika Panda, which is a 7 degrees-of-freedom (DOF) robotic arm ...
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** Dataset Panda-3D-4 Panda-Tabletop-4 PR2-3D-4 Task Action (F1) Grasp (F1) Action (F1) Grasp (F1) Action (F1) Grasp (F1) F-SVM - - 0.884 0.415 (± 0.220) - ...
- **p. 10 / 6 RESULTS - extractive PDF cue:** Test set Panda-3D-10 Panda-3D-15 Panda-3D-20 Task Action (F1) Grasp (F1) Action (F1) Grasp (F1) Action (F1) Grasp (F1) MLP 0.773 0.624 (± 0.028) 0.766 0.616 ...
- **p. 14 / A IMPLEMENTATION DETAILS - extractive PDF cue:** During the pre-training stage, each module is trained for 100 epochs.
- **p. 14 / A IMPLEMENTATION DETAILS - extractive PDF cue:** During the fine-tuning stage, the complete GRN model is trained for 100 epochs with a batch size of 2048 and a learning rate of 0.0001.
- **p. 14 / A IMPLEMENTATION DETAILS - extractive PDF cue:** The full training process takes approximately 15 hours.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 5: Annotations statistics for the Panda-3D-4 training set. (a) Number of feasible and infeasi- ble actions (b) Number of feasible and infeasi- ble ... | p. 16 (Figure/Table caption) |
| body limitation/failure cue | CNN-based methods, DVH and AGFP-Net, fall short compared to our approach, with a difference in F1 score on the Panda-3D-4 of 10% (resp. | p. 8 (6 RESULTS) |
| body limitation/failure cue | Feasibility-GCN (F-GCN): This baseline uses the same scene representation as F-GAT, except that GAT is replaced with a Graph Convolution Network (GCN), which does ... | p. 7 (5 EXPERIMENTS) |
| body limitation/failure cue | Future work will include graph pooling layers to evaluate motion infeasibility across the entire scene graph. | p. 10 (6 RESULTS) |
| body limitation/failure cue | 7 DISCUSSION AND FUTURE WORK In this work, we propose a framework for action and grasp feasibility prediction in 3D environments. | p. 10 (6 RESULTS) |
| body limitation/failure cue | Indeed, image-based scene representation suffers from occlusions due to the 3D nature of the environment, resulting in inaccurate predictions for occluded objects. | p. 8 (6 RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| During the fine-tuning stage, the complete GRN model is trained for 100 epochs with a batch size of 2048 and a learning rate of ... | p. 14 (A IMPLEMENTATION DETAILS) |
| We use a batch size of 8192 and a learning rate of 0.001 for the IK feasibility classifier and the GO estimator. | p. 14 (A IMPLEMENTATION DETAILS) |
| In robotic manipulation planning, feasibility prediction must not only be accurate, it must also have a low inference time and memory footprint. | p. 8 (6 RESULTS) |
| The inference time incorporates the complete prediction process from the model's input construction to the output, for each movable object in the environment. | p. 8 (6 RESULTS) |
| Furthermore, GRN has a 99.6% lower inference time than traditional geometric planning. | p. 9 (6 RESULTS) |
| 0.915 0.903 (± 0.013) 0.990 (± 0.001) 0.044 (± 0.002) Full model (Trained from scratch) 0.932 0.925 (± 0.011) 0.994 (± 0.001) 0.038 (± ... | p. 9 (6 RESULTS) |
| Alternatively, embeddings from off-the-shelf shape encoders (e.g., meshes or point clouds) could enhance node features, though computational efficiency remains a challenge. | p. 10 (6 RESULTS) |
| The proposed model is able to accurately predict action and grasp feasibility, as well as reasons of infeasibility, from estimated objects' poses in both ... | p. 10 (6 RESULTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 16 / Figure/Table caption - extractive PDF cue:** Figure 5: Annotations statistics for the Panda-3D-4 training set. (a) Number of feasible and infeasi- ble actions (b) Number of feasible and infeasi- ble cases ...
- **p. 8 / 6 RESULTS - extractive PDF cue:** CNN-based methods, DVH and AGFP-Net, fall short compared to our approach, with a difference in F1 score on the Panda-3D-4 of 10% (resp.
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** Feasibility-GCN (F-GCN): This baseline uses the same scene representation as F-GAT, except that GAT is replaced with a Graph Convolution Network (GCN), which does not ...
- **p. 10 / 6 RESULTS - extractive PDF cue:** Future work will include graph pooling layers to evaluate motion infeasibility across the entire scene graph.
- **p. 10 / 6 RESULTS - extractive PDF cue:** 7 DISCUSSION AND FUTURE WORK In this work, we propose a framework for action and grasp feasibility prediction in 3D environments.
- **p. 8 / 6 RESULTS - extractive PDF cue:** Indeed, image-based scene representation suffers from occlusions due to the 3D nature of the environment, resulting in inaccurate predictions for occluded objects.

- **PDF anchors reviewed:** datasets p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (6 RESULTS), p. 10 (6 RESULTS), p. 8 (5 EXPERIMENTS), p. 10 (6 RESULTS), metrics p. 8 (6 RESULTS), p. 8 (5 EXPERIMENTS), p. 9 (6 RESULTS), p. 9 (6 RESULTS), p. 10 (6 RESULTS), p. 10 (6 RESULTS), baselines p. 8 (6 RESULTS), p. 7 (5 EXPERIMENTS), p. 9 (6 RESULTS), p. 10 (6 RESULTS), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), results p. 9 (6 RESULTS), p. 8 (6 RESULTS), p. 9 (6 RESULTS), p. 10 (6 RESULTS), p. 8 (6 RESULTS), p. 10 (6 RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
