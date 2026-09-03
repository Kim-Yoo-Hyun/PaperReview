# Evaluation - Geometry-aware RL for Manipulation of Varying Shapes and Deformable Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=7BLXhmWvwF; PDF retrieval source: https://arxiv.org/pdf/2502.07005. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 25 (Figure/Table caption), p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS)): Figure 4: Performance of different models on the Cloth-Hanging task across varying sample spaces. Overall, performance improves as the sample space decreases. In terms of final performance, het- erogeneous models ...

## Evaluation Body Digest

- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Overall, HEPi generalizes well to unseen objects, performs consistently across resolutions, and handles noise effectively, making it suitable for real-world tasks.
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** 4.1 EXPERIMENTAL SETUP Task Design Our task design, illustrated in Figure 2, emphasizes testing the role of geometric structure and information exchange between objects and ...
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** We then introduce a novel task, Rope-Shaping, which increases complexity by requiring the rope to form a specific shape (a "W" from the LASA dataset ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** 4.2 RESULTS AND DISCUSSIONS In the main evaluations, we generate 1000 scenes per task (sampled according to Appendix B) and compute the undiscounted return over ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Finally, we evaluate the generalization of these models to unseen objects on two rigid tasks: rigidsliding and rigid-insertion.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** HEPi and EMPN perform similarly on the 2D tasks, but as tasks scale up to 3D environments, such as cloth-hanging-3D, HEPi shows a significant advantage, ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** The computational overhead is measured as the ratio of training time per iteration (over seven tasks) relative to HEPi. and three (plus, star, pentagon)-and tested ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** However, in tasks with a lower-dimensional action space, such as 2D environments, well-tuned PPO performs comparably to TRPL in terms of final average return, though ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4: Performance of different models on the Cloth-Hanging task across varying sample spaces. Overall, performance improves as the sample space decreases. In terms ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 20: Performance of different models on the Cloth-Hanging task across various sample spaces. Assuming the global scene located at r = [0, 1, ... | p. 25 (Figure/Table caption) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Adding attention significantly increases the training time but does not improve performance, as shown on the right. | p. 9 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | However, HeteroGNN requires more samples, whereas HEPi's use of EMPN significantly improves sample efficiency by leveraging equivariant constraints in large 3D spaces. | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our experimental setup aims to answer the following key questions: (1) Can explicitly modeling heterogeneity between actuators and objects, combined with SE(3) equivariance, improve ... | p. 7 (4 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Overall, HEPi generalizes well to unseen objects, performs consistently across resolutions, and handles noise effectively, making it suitable for real-world tasks.
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** 4.1 EXPERIMENTAL SETUP Task Design Our task design, illustrated in Figure 2, emphasizes testing the role of geometric structure and information exchange between objects and ...
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** We then introduce a novel task, Rope-Shaping, which increases complexity by requiring the rope to form a specific shape (a "W" from the LASA dataset ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** 4.2 RESULTS AND DISCUSSIONS In the main evaluations, we generate 1000 scenes per task (sampled according to Appendix B) and compute the undiscounted return over ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Finally, we evaluate the generalization of these models to unseen objects on two rigid tasks: rigidsliding and rigid-insertion.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** HEPi and EMPN perform similarly on the 2D tasks, but as tasks scale up to 3D environments, such as cloth-hanging-3D, HEPi shows a significant advantage, ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** The computational overhead is measured as the ratio of training time per iteration (over seven tasks) relative to HEPi. and three (plus, star, pentagon)-and tested ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** However, in tasks with a lower-dimensional action space, such as 2D environments, well-tuned PPO performs comparably to TRPL in terms of final average return, though ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Left: A Cloth-Hanging task represented by a heterogeneous graph that comprises two disjoint node sets, objects, and actuators, connected through directed, fully-connected inter-edges. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2: Illustration of our diverse and challenging manipulation tasks, involving both rigid and deformable objects. These tasks require precise control under complex geometric constraints, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Evaluation curves for our seven manipulation tasks, comparing HEPi (ours), EMPN, and Transformer baselines. Results are averaged over 10 seeds, using IQM with ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Performance of different models on the Cloth-Hanging task across varying sample spaces. Overall, performance improves as the sample space decreases. In terms of ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Left: Analysis of noise sensitivity and scalability to high-resolution objects in the Rigid- Pushing task. Heatmaps show average returns under varying levels of ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 7: Performance comparison on tasks with and without attention mechanisms over 10 seeds. Adding attention significantly increases the training time but does not improve ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 8: Performance comparison between HEPi and Transformer models with TRPL and PPO over 10 seeds. TRPL shows stable performance across all tasks, while PPO ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 9: Demonstration of graph with overlapping and non-overlapping nodes. Actuator nodes are in red, object nodes are in either white or orange. messages from ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Overall, HEPi generalizes well to unseen objects, performs consistently across resolutions, and handles noise effectively, making it suitable for real-world tasks. | embodiment, simulator version and control stack | p. 8 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Task/environment | 4.1 EXPERIMENTAL SETUP Task Design Our task design, illustrated in Figure 2, emphasizes testing the role of geometric structure and information exchange between objects ... | reset, timeout, object/scene variation | p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 1 (1 INTRODUCTION), p. 3 (3 METHODOLOGY) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Full task details, including reward definitions, are provided in Appendix B. | definition/direction/unit from same section | p. 6 (4 EXPERIMENTS) |
| Our experimental setup aims to answer the following key questions: (1) Can explicitly modeling heterogeneity between actuators and objects, combined with SE(3) equivariance, improve ... | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| 4.2 RESULTS AND DISCUSSIONS In the main evaluations, we generate 1000 scenes per task (sampled according to Appendix B) and compute the undiscounted return ... | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| As shown in Figure 5 (left), HEPi maintains high performance across resolutions with only mild degradation at higher noise levels, demonstrating its scalability and ... | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| Figure 18: Sample space of the Cloth-Hanging task. Reward Function The total reward consists of the following sub-rewards: • Hole-hanger alignment reward: Rhole-hanger = ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |
| Figure 1: Left: A Cloth-Hanging task represented by a heterogeneous graph that comprises two disjoint node sets, objects, and actuators, connected through directed, fully-connected ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| These tasks present a range of manipulation challenges, emphasizing the role of geometric structure and requiring complex exploration strategies to coordinate the agents in ... | definition/direction/unit from same section | p. 6 (4 EXPERIMENTS) |
| Overall, performance improves as the sample space decreases. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 3: Evaluation curves for our seven manipulation tasks, comparing HEPi (ours), EMPN, and Transformer baselines. Results are averaged over 10 seeds, using IQM ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| HEPi and EMPN perform similarly on the 2D tasks, but as tasks scale up to 3D environments, such as cloth-hanging-3D, HEPi shows a significant ... | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| In terms of final performance, heterogeneous models outperform homogeneous baselines in most cases, demonstrating the benefits of explicit heterogeneity modeling. | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| Figure 7: Performance comparison on tasks with and without attention mechanisms over 10 seeds. Adding attention significantly increases the training time but does not ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| Figure 20: Performance of different models on the Cloth-Hanging task across various sample spaces. Assuming the global scene located at r = [0, 1, ... | comparison identity and matched condition | p. 25 (Figure/Table caption) |
| In this section, we outline the experimental setup and present the results comparing the proposed HEPi against other baselines. | comparison identity and matched condition | p. 6 (4 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 23: Ablation on different k-nearest neighbors for obj-to-act edges in MPNN + VNLocal (in Section 3.3) updates, evaluated on the Rigid-Insertion task with ... | component/input/data sensitivity | p. 26 (Figure/Table caption) |
| In addition, for the Cloth-Hanging task, we evaluate two additional baselines, Heterogeneous GNN (HeteroGNN) and a naive GNN to highlight the effectiveness of incorporating ... | component/input/data sensitivity | p. 7 (4 EXPERIMENTS) |
| GNNs naturally capture locality through message passing, allowing them to scale effectively to higher-resolution graphs without retraining (Li et al., 2020; Freymuth et al., ... | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| Figure 21: Ablation on different k-nearest neighbors choices for obj-to-act edges in MPNN + VNLocal updates (in Section 3.3), evaluated across multiple tasks: rigid-insertion, ... | component/input/data sensitivity | p. 25 (Figure/Table caption) |
| Figure 5: Left: Analysis of noise sensitivity and scalability to high-resolution objects in the Rigid- Pushing task. Heatmaps show average returns under varying levels ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Next, Rigid-Pushing removes the physical connection between the actuator and the object, allowing the actuator to move freely in the x-y plane to push ... | component/input/data sensitivity | p. 6 (4 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To evaluate our approach and future advancements in this direction, we propose a novel suite of seven tasks, realized using NIVIDA IsaacLab (Mittal et ... | Figure 4: Performance of different models on the Cloth-Hanging task across varying sample spaces. Overall, performance improves as the sample space decreases. In terms ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 25 (Figure/Table caption), p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Primary metric/result | Figure 20: Performance of different models on the Cloth-Hanging task across various sample spaces. Assuming the global scene located at r = [0, 1, ... | numeric claim only at cited anchor | p. 25 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Results are averaged over 10 seeds, using IQM with 95% confidence intervals.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** 4.2 RESULTS AND DISCUSSIONS In the main evaluations, we generate 1000 scenes per task (sampled according to Appendix B) and compute the undiscounted return over ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Limitation In our current setup, we abstract away the robot body, focusing solely on end-effector movements. | p. 10 (6 CONCLUSION) |
| body limitation/failure cue | This limitation could be addressed by integrating state-of-the-art computer vision techniques to extract keypoints from cameras (Tumanyan et al., 2024; Hou et al., 2024), ... | p. 10 (6 CONCLUSION) |
| body limitation/failure cue | As shown in Figure 5 (left), HEPi maintains high performance across resolutions with only mild degradation at higher noise levels, demonstrating its scalability and ... | p. 8 (4 EXPERIMENTS) |
| body limitation/failure cue | Overall, as depicted in Figure 8, in tasks requiring high exploration such as cloth-hanging-3D, PPO struggles to maintain conservative updates, often resulting in unstable ... | p. 9 (4 EXPERIMENTS) |
| body limitation/failure cue | Figure 23: Ablation on different k-nearest neighbors for obj-to-act edges in MPNN + VNLocal (in Section 3.3) updates, evaluated on the Rigid-Insertion task with ... | p. 26 (Figure/Table caption) |
| body limitation/failure cue | For final performance on rigid tasks, firstly in rigid-slding-2D and rigid-insertion-2D+z tasks, HEPi and Transformer policies perform comparably, suggesting that the limited task complexity ... | p. 7 (4 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 4.2 RESULTS AND DISCUSSIONS In the main evaluations, we generate 1000 scenes per task (sampled according to Appendix B) and compute the undiscounted return ... | p. 7 (4 EXPERIMENTS) |
| Adding attention significantly increases the training time but does not improve performance, as shown on the right. | p. 9 (4 EXPERIMENTS) |
| Additionally, adding attention significantly increases training time without improving performance, e.g., for HEPi it almost doubled. | p. 9 (4 EXPERIMENTS) |
| We introduce two categories of tasks: rigid manipulation on diverse geometries and deformable object manipulation, all implemented in NVIDIA IsaacLab (Mittal et al., 2023) ... | p. 6 (4 EXPERIMENTS) |
| Results are averaged over 10 seeds, using IQM with 95% confidence intervals. | p. 7 (4 EXPERIMENTS) |
| The value function is computed as V (s) = MLPouter  P v∈V MLPinner(sv)  , where sv represents the feature of node v. | p. 5 (3 METHODOLOGY) |
| This, however, requires careful hyperparameters turning to make it work stably, as pointed out by Andrychowicz et al. | p. 5 (3 METHODOLOGY) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 6 CONCLUSION - extractive body cue:** Limitation In our current setup, we abstract away the robot body, focusing solely on end-effector movements.
- **p. 10 / 6 CONCLUSION - extractive body cue:** This limitation could be addressed by integrating state-of-the-art computer vision techniques to extract keypoints from cameras (Tumanyan et al., 2024; Hou et al., 2024), using ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** As shown in Figure 5 (left), HEPi maintains high performance across resolutions with only mild degradation at higher noise levels, demonstrating its scalability and robustness ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Overall, as depicted in Figure 8, in tasks requiring high exploration such as cloth-hanging-3D, PPO struggles to maintain conservative updates, often resulting in unstable performance.
- **p. 26 / Figure/Table caption - extractive body cue:** Figure 23: Ablation on different k-nearest neighbors for obj-to-act edges in MPNN + VNLocal (in Section 3.3) updates, evaluated on the Rigid-Insertion task with varying ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** For final performance on rigid tasks, firstly in rigid-slding-2D and rigid-insertion-2D+z tasks, HEPi and Transformer policies perform comparably, suggesting that the limited task complexity does ...

- **Evidence anchors reviewed:** datasets p. 8 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), metrics p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 23 (Figure/Table caption), p. 2 (Figure/Table caption), baselines p. 7 (Figure/Table caption), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (Figure/Table caption), p. 25 (Figure/Table caption), p. 6 (4 EXPERIMENTS), results p. 8 (Figure/Table caption), p. 25 (Figure/Table caption), p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
