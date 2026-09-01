# Evaluation - Body Transformer: Leveraging Robot Embodiment for Policy Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=Oce2215aJE; PDF retrieval source: https://arxiv.org/pdf/2408.06316. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (5 Experiments), p. 6 (5 Experiments), p. 5 (5 Experiments), p. 7 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments)): We report results in the table shown in Figure 3a, where BoT consistently outperforms the MLP and transformer baselines.

## Evaluation Body Digest

- **p. 5 / 5 Experiments - extractive PDF cue:** With the following experiments, we aim to answer the following questions: • Does masked attention benefit imitation learning in terms of performance and generalization? • ...
- **p. 7 / 5 Experiments - extractive PDF cue:** To verify that our architecture is suitable for real-world applications, e.g., running in real time, we deploy one of the BoT policies trained above to ...
- **p. 6 / 5 Experiments - extractive PDF cue:** Finally, we adapt the A1-Walk environment, which is part of the Legged Gym repository [32], where the task is for a Unitree A1 quadruped robot ...
- **p. 5 / 5 Experiments - extractive PDF cue:** 5.1 Imitation Learning Experiments We evaluate the imitation learning performance of the BoT architecture in a body-tracking task defined through the MoCapAct dataset [29], which ...
- **p. 6 / 5 Experiments - extractive PDF cue:** 5.2 Reinforcement Learning Experiments We evaluate the RL performance of BoT and baselines using PPO [30] on 4 robotic control tasks in Isaac Gym [31]: ...
- **p. 7 / 5 Experiments - extractive PDF cue:** 5.3 Real World Experiments The Isaac Gym simulated locomotion environments are widely popular for sim-to-real transfer of RL policies without requiring adaptation in the real-world ...
- **p. 6 / 5 Experiments - extractive PDF cue:** Statistics of the various architecturecriterion combinations are shown with two values, the leftside being the maximum value recorded during training, and the rightside being the ...
- **p. 5 / 5 Experiments - extractive PDF cue:** We evaluate mean returns normalized by the length of a clip, in addition to the normalized length of an episode, which terminates when the tracking ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** 5 Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | We report results in the table shown in Figure 3a, where BoT consistently outperforms the MLP and transformer baselines. | p. 5 (5 Experiments) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The result shows that BoT-Mix consistently outperforms both the MLP and vanilla transformer baselines in terms of sample efficiency and asymptotic performance, highlighting the ... | p. 6 (5 Experiments) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | While the multi-clip policy is competitive with the vanilla transformer baseline, it is strongly outperformed by our architecture. | p. 5 (5 Experiments) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | We note that for simplicity we did not make use of teacherstudent training or memory mechanisms [35] as common in the locomotion literature, which ... | p. 7 (5 Experiments) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results are averaged across five seeds. | p. 6 (5 Experiments) |

## Dataset / Benchmark Role

- **p. 5 / 5 Experiments - extractive PDF cue:** With the following experiments, we aim to answer the following questions: • Does masked attention benefit imitation learning in terms of performance and generalization? • ...
- **p. 7 / 5 Experiments - extractive PDF cue:** To verify that our architecture is suitable for real-world applications, e.g., running in real time, we deploy one of the BoT policies trained above to ...
- **p. 6 / 5 Experiments - extractive PDF cue:** Finally, we adapt the A1-Walk environment, which is part of the Legged Gym repository [32], where the task is for a Unitree A1 quadruped robot ...
- **p. 5 / 5 Experiments - extractive PDF cue:** 5.1 Imitation Learning Experiments We evaluate the imitation learning performance of the BoT architecture in a body-tracking task defined through the MoCapAct dataset [29], which ...
- **p. 6 / 5 Experiments - extractive PDF cue:** 5.2 Reinforcement Learning Experiments We evaluate the RL performance of BoT and baselines using PPO [30] on 4 robotic control tasks in Isaac Gym [31]: ...
- **p. 7 / 5 Experiments - extractive PDF cue:** 5.3 Real World Experiments The Isaac Gym simulated locomotion environments are widely popular for sim-to-real transfer of RL policies without requiring adaptation in the real-world ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Body Transformer (BoT) is an architecture that considers physical agents as graphs of sensors and actuators as nodes, and edges reflecting the structure ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Formulation of Embodiment Mask. The mask M is constructed by adding a diagonal of 1s to the embodiment graph's adjacency matrices. Here, we ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3: BoT Performance on Imitation Learning.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4: Adroit Hand Door, Hammer, and Relocate Tasks (See Results in the Appendix). 5.2 Reinforcement Learning Experiments We evaluate the RL performance of BoT ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5: Reinforcement Learning Performance on Robotic Control Tasks. Meanwhile, BoT-Hard performs better than the vanilla transformer on simpler tasks (A1-Walk and Humanoid-Mod), but shows ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6: Computational Analysis of the Custom Masked Attention Implementation. Across 10,000 randomly sampled masks, we found that our custom implementation provides a 200% speed- ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Figure 7: Real-World Deployment. Frame over- lay demonstrating the deployment of the BoT walking policy to a Unitree A1 quadruped robot. We deployed the RL ...
- **p. 13 / Figure/Table caption - extractive PDF cue:** Figure 8: Rules for Allocating Quantities to Nodes. As a rule of thumb, observations or actions that spanned multiple nodes were assigned to the closest ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | With the following experiments, we aim to answer the following questions: • Does masked attention benefit imitation learning in terms of performance and generalization? ... | embodiment, simulator version and control stack | p. 5 (5 Experiments), p. 7 (5 Experiments) |
| Task/environment | To verify that our architecture is suitable for real-world applications, e.g., running in real time, we deploy one of the BoT policies trained above ... | reset, timeout, object/scene variation | p. 7 (5 Experiments), p. 6 (5 Experiments) |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 4 (3 Background), p. 1 (Abstract) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 2 (1 Introduction), p. 5 (3 Background) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Statistics of the various architecturecriterion combinations are shown with two values, the leftside being the maximum value recorded during training, and the rightside being ... | definition/direction/unit from same section | p. 6 (5 Experiments) |
| We evaluate mean returns normalized by the length of a clip, in addition to the normalized length of an episode, which terminates when the ... | definition/direction/unit from same section | p. 5 (5 Experiments) |
| The solid curve corresponds to the mean, and the shaded area to the standard error over five seeds. | definition/direction/unit from same section | p. 6 (5 Experiments) |
| 0.0 0.5 1.0 1.5 env steps 1e8 0 20 40 episode return A1-Walk 0 2 4 6 env steps 1e8 5000 6000 7000 8000 ... | definition/direction/unit from same section | p. 7 (5 Experiments) |
| We assess the performance of BoT across imitation learning and reinforcement learning settings. | definition/direction/unit from same section | p. 5 (5 Experiments) |
| (b) Snapshots of successful rollouts of BoT policies. | definition/direction/unit from same section | p. 7 (5 Experiments) |
| We measure the average runtime of each implementation of the attention mechanism across 10,000 set of randomly generated Q, K, V , and M. | definition/direction/unit from same section | p. 8 (5 Experiments) |
| For each randomization, the generated masks M have a diagonal of 1s and sparsity equal to that used in the MoCapAct experiments (β = ... | definition/direction/unit from same section | p. 8 (5 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We report results in the table shown in Figure 3a, where BoT consistently outperforms the MLP and transformer baselines. | comparison identity and matched condition | p. 5 (5 Experiments) |
| While the multi-clip policy is competitive with the vanilla transformer baseline, it is strongly outperformed by our architecture. | comparison identity and matched condition | p. 5 (5 Experiments) |
| The result shows that BoT-Mix consistently outperforms both the MLP and vanilla transformer baselines in terms of sample efficiency and asymptotic performance, highlighting the ... | comparison identity and matched condition | p. 6 (5 Experiments) |
| 5.2 Reinforcement Learning Experiments We evaluate the RL performance of BoT and baselines using PPO [30] on 4 robotic control tasks in Isaac Gym ... | comparison identity and matched condition | p. 6 (5 Experiments) |
| For a fair computational comparison, we re-implement the scaled dot product in Equation (1) using CPU-based NumPy and evaluate on a 7 | comparison identity and matched condition | p. 7 (5 Experiments) |
| 5.3 Real World Experiments The Isaac Gym simulated locomotion environments are widely popular for sim-to-real transfer of RL policies without requiring adaptation in the ... | comparison identity and matched condition | p. 7 (5 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We keep the same structure as in Figure 1 and only replace the BoT encoder with the various baseline architectures to single out the ... | component/input/data sensitivity | p. 5 (5 Experiments) |
| 5.3 Real World Experiments The Isaac Gym simulated locomotion environments are widely popular for sim-to-real transfer of RL policies without requiring adaptation in the ... | component/input/data sensitivity | p. 7 (5 Experiments) |
| Figure 11: Additional RL Experimental Results on the Effect of Per-Node (De)Tokenizers. 15 | component/input/data sensitivity | p. 15 (Figure/Table caption) |
| Figure 10: Additional RL Experimental Results on the Effect of Body-induced Masking. BoT relies on masked attention with its mask determined by the embodiment ... | component/input/data sensitivity | p. 15 (Figure/Table caption) |
| Figure 9: Additional Imitation Learning Experiments. In this section we provide several ablations on the MoCapAct dataset, in addition to those presented in Section ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| Humanoid-Mod features the classical running task on flat ground, while in Humanoid-Hill we replaced the flat ground with an irregular hilly terrain. | component/input/data sensitivity | p. 6 (5 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are listed below: • We propose the BoT architecture, which augments the transformer architecture with a novel masking that leverages the morphology ... | We report results in the table shown in Figure 3a, where BoT consistently outperforms the MLP and transformer baselines. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (5 Experiments), p. 6 (5 Experiments), p. 5 (5 Experiments), p. 7 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments) |
| Primary metric/result | The result shows that BoT-Mix consistently outperforms both the MLP and vanilla transformer baselines in terms of sample efficiency and asymptotic performance, highlighting the ... | numeric claim only at cited anchor | p. 6 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 6 / 5 Experiments - extractive PDF cue:** normalized episode return normalized episode length train val train val MLP 0.623 / 0.572 ± 0.022 0.568 / 0.534 ± 0.025 0.808 / 0.762 ± ...
- **p. 7 / 5 Experiments - extractive PDF cue:** 0.0 0.5 1.0 1.5 env steps 1e8 0 20 40 episode return A1-Walk 0 2 4 6 env steps 1e8 5000 6000 7000 8000 9000 ...
- **p. 8 / 5 Experiments - extractive PDF cue:** For each randomization, the generated masks M have a diagonal of 1s and sparsity equal to that used in the MoCapAct experiments (β = 0.908) ...
- **p. 4 / 3 Background - extractive PDF cue:** The mask M is constructed by adding a diagonal of 1s to the embodiment graph's adjacency matrices.
- **p. 4 / 3 Background - extractive PDF cue:** Here, we visualize a simple example of a mask M for an arbitrary agent's embodiment where n = 10.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We leave the extension of BoT to the temporal dimension as future work, as it promises to further improve real world deployment of robot ... | p. 8 (6 Conclusion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We measure the average runtime of each implementation of the attention mechanism across 10,000 set of randomly generated Q, K, V , and M. | p. 8 (5 Experiments) |
| Across 10,000 randomly sampled masks, we found that our custom implementation provides a 200% speedup in runtime at sequence lengths up to 128 nodes ... | p. 8 (5 Experiments) |
| We run the evaluations both on the training and the (unseen) validation clips. | p. 5 (5 Experiments) |
| We keep the same structure as in Figure 1 and only replace the BoT encoder with the various baseline architectures to single out the ... | p. 5 (5 Experiments) |
| Results are averaged across five seeds. | p. 6 (5 Experiments) |
| The solid curve corresponds to the mean, and the shaded area to the standard error over five seeds. | p. 6 (5 Experiments) |
| For a fair computational comparison, we re-implement the scaled dot product in Equation (1) using CPU-based NumPy and evaluate on a 7 | p. 7 (5 Experiments) |
| To verify that our architecture is suitable for real-world applications, e.g., running in real time, we deploy one of the BoT policies trained above ... | p. 7 (5 Experiments) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6 Conclusion - extractive PDF cue:** We leave the extension of BoT to the temporal dimension as future work, as it promises to further improve real world deployment of robot policies, ...

- **PDF anchors reviewed:** datasets p. 5 (5 Experiments), p. 7 (5 Experiments), p. 6 (5 Experiments), p. 5 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments), metrics p. 6 (5 Experiments), p. 5 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments), p. 5 (5 Experiments), p. 7 (5 Experiments), baselines p. 5 (5 Experiments), p. 5 (5 Experiments), p. 6 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments), p. 7 (5 Experiments), results p. 5 (5 Experiments), p. 6 (5 Experiments), p. 5 (5 Experiments), p. 7 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
