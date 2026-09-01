# Evaluation - ManiGaussian: Dynamic Gaussian Splatting for Multi-task Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5194_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05194.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 11 (4 Experiments), p. 12 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments)): Our method achieves the best performance with an average success rate of 44.8%, which is state-of-the-art, outperforming the previous arts including both perceptive and generative-based methods by a sizable margin.

## Evaluation Body Digest

- **p. 11 / 4 Experiments - extractive body cue:** On the contrary, our ManiGaussian learns the scene dynamics with the proposed dynamic Gaussian Splatting framework, so that the robotic agent can complete human instructions ...
- **p. 10 / 4 Experiments - extractive body cue:** We evaluated 25 episodes in the testing set for each task to avoid result bias from noise.
- **p. 10 / 4 Experiments - extractive body cue:** The evaluation metric is the task success rate, which measures the percentage of completed episodes.
- **p. 11 / 4 Experiments - extractive body cue:** We evaluate 25 episodes per task for the final checkpoint on 10 challenging tasks from RLBench and report the success rates (%), where the second ...
- **p. 12 / 4 Experiments - extractive body cue:** Lu et al. illustrate the effectiveness of our proposed method across multiple languageconditioned robotic manipulation tasks.
- **p. 12 / 4 Experiments - extractive body cue:** We first implement a vanilla baseline without any proposed technique, where we directly train the representation model and the action decoder to predict the robot ...
- **p. 13 / 4 Experiments - extractive body cue:** The red mark signifies the pose deviates severely from the expert demonstration, whereas the green mark indicates that the pose aligns with the expert trajectory.
- **p. 13 / 4 Experiments - extractive body cue:** In contrast, ManiGaussian returns to the red square and successfully slides the square to the yellow target, owing to that our method can correctly understand ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 10).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method achieves the best performance with an average success rate of 44.8%, which is state-of-the-art, outperforming the previous arts including both perceptive and ... | p. 11 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Though the dynamic loss may slightly impact short-term results due to the balance of different loss items, it significantly improves overall performance. | p. 12 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | The diversity of these tasks requires the agent to acquire generalizable knowledge about the intrinsical scene-level spatial-temporal dynamics for manipulation, rather than solely relying ... | p. 10 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | As a result, our method outperforms the second-best GNFactor method by a relative improvement of 41.3%. | p. 11 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | By adding the Gaussian regressor to predict the Gaussian parameters, the performance improves by 15.6% compared with the baseline. | p. 12 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 11 / 4 Experiments - extractive body cue:** On the contrary, our ManiGaussian learns the scene dynamics with the proposed dynamic Gaussian Splatting framework, so that the robotic agent can complete human instructions ...
- **p. 10 / 4 Experiments - extractive body cue:** We evaluated 25 episodes in the testing set for each task to avoid result bias from noise.
- **p. 10 / 4 Experiments - extractive body cue:** The evaluation metric is the task success rate, which measures the percentage of completed episodes.
- **p. 11 / 4 Experiments - extractive body cue:** We evaluate 25 episodes per task for the final checkpoint on 10 challenging tasks from RLBench and report the success rates (%), where the second ...
- **p. 12 / 4 Experiments - extractive body cue:** Lu et al. illustrate the effectiveness of our proposed method across multiple languageconditioned robotic manipulation tasks.
- **p. 12 / 4 Experiments - extractive body cue:** We first implement a vanilla baseline without any proposed technique, where we directly train the representation model and the action decoder to predict the robot ...
- **p. 13 / 4 Experiments - extractive body cue:** The red mark signifies the pose deviates severely from the expert demonstration, whereas the green mark indicates that the pose aligns with the expert trajectory.
- **p. 13 / 4 Experiments - extractive body cue:** In contrast, ManiGaussian returns to the red square and successfully slides the square to the yellow target, owing to that our method can correctly understand ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: Consider the human instruction "stack two rose blocks", where the task is con- sidered successful if two rose blocks are stacked upon the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 2: The overall pipeline of ManiGaussian, which primarily consists of a dynamic Gaussian Splatting framework and a Gaussian world model. The dynamic Gaussian Splatting ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 1: Multi-task Test Results. We evaluate 25 episodes per task for the final checkpoint on 10 challenging tasks from RLBench and report the success ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 2: Comparison of Methods with Different Techniques. Following [15], we manually group the 10 RLBench tasks into 6 categories according to their main challenges ...
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 3: Learning Curve. Com- parison of our ManiGaussian with GNFactor in performance and speed. For a fair comparison, we exclude auxiliary losses from the
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 4: Case Study. The red mark signifies the pose deviates severely from the ex- pert demonstration, whereas the green mark indicates that the pose ...
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 5: Novel View Synthesis Results. We remove the action loss here for better visualization. Our ManiGaussian is capable of both current scene reconstruction and ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | On the contrary, our ManiGaussian learns the scene dynamics with the proposed dynamic Gaussian Splatting framework, so that the robotic agent can complete human ... | embodiment, simulator version and control stack | p. 11 (4 Experiments), p. 10 (4 Experiments) |
| Task/environment | We evaluated 25 episodes in the testing set for each task to avoid result bias from noise. | reset, timeout, object/scene variation | p. 10 (4 Experiments), p. 10 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (3 Approach), p. 5 (3 Approach) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 8 (3 Approach), p. 8 (3 Approach) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Our method achieves the best performance with an average success rate of 44.8%, which is state-of-the-art, outperforming the previous arts including both perceptive and ... | definition/direction/unit from same section | p. 11 (4 Experiments) |
| By adding the semantic features and the related consistency loss, we observe that the average success rate increases by 2.4% than the only geometric ... | definition/direction/unit from same section | p. 12 (4 Experiments) |
| The evaluation metric is the task success rate, which measures the percentage of completed episodes. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| The diversity of these tasks requires the agent to acquire generalizable knowledge about the intrinsical scene-level spatial-temporal dynamics for manipulation, rather than solely relying ... | definition/direction/unit from same section | p. 10 (4 Experiments) |
| We evaluate 25 episodes per task for the final checkpoint on 10 challenging tasks from RLBench and report the success rates (%), where the ... | definition/direction/unit from same section | p. 11 (4 Experiments) |
| 0 5 10 15 20 25 30 35 Time of T raining (hours) 0 5 10 15 20 25 30 35 40 Average Success ... | definition/direction/unit from same section | p. 12 (4 Experiments) |
| In contrast, ManiGaussian returns to the red square and successfully slides the square to the yellow target, owing to that our method can correctly ... | definition/direction/unit from same section | p. 13 (4 Experiments) |
| This qualitative result demonstrates that our ManiGaussian learns the intricate scene-level dynamics successfully. | definition/direction/unit from same section | p. 14 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 4: Case Study. The red mark signifies the pose deviates severely from the ex- pert demonstration, whereas the green mark indicates that the ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |
| Our method achieves the best performance with an average success rate of 44.8%, which is state-of-the-art, outperforming the previous arts including both perceptive and ... | comparison identity and matched condition | p. 11 (4 Experiments) |
| By adding the Gaussian regressor to predict the Gaussian parameters, the performance improves by 15.6% compared with the baseline. | comparison identity and matched condition | p. 12 (4 Experiments) |
| Then we compare our method with the state-of-the-art approaches to show the superiority in success rate (Section 4.2), and conduct an ablation study to ... | comparison identity and matched condition | p. 10 (4 Experiments) |
| Planning Long Tools Motion Screw Occlusion Average ✗ ✗ ✗ 36.0 2.0 25.3 52.0 4.0 28.0 23.6 ✓ ✗ ✗ 46.0 4.0 52.0 52.0 ... | comparison identity and matched condition | p. 11 (4 Experiments) |
| We first implement a vanilla baseline without any proposed technique, where we directly train the representation model and the action decoder to predict the ... | comparison identity and matched condition | p. 12 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Then we compare our method with the state-of-the-art approaches to show the superiority in success rate (Section 4.2), and conduct an ablation study to ... | component/input/data sensitivity | p. 10 (4 Experiments) |
| We conduct an ablation study to verify the effectiveness of each presented component in Table 2. | component/input/data sensitivity | p. 12 (4 Experiments) |
| We first implement a vanilla baseline without any proposed technique, where we directly train the representation model and the action decoder to predict the ... | component/input/data sensitivity | p. 12 (4 Experiments) |
| We remove the action loss here for better visualization. | component/input/data sensitivity | p. 14 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions can be summarized as follows: - We propose a dynamic Gaussian Splatting framework to learn the scenelevel spatiotemporal dynamics in general robotic ... | Our method achieves the best performance with an average success rate of 44.8%, which is state-of-the-art, outperforming the previous arts including both perceptive and ... | PDF body cue; verify exact table/figure and matched conditions | p. 11 (4 Experiments), p. 12 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments) |
| Primary metric/result | Though the dynamic loss may slightly impact short-term results due to the balance of different loss items, it significantly improves overall performance. | numeric claim only at cited anchor | p. 12 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 10 / 4 Experiments - extractive body cue:** We evaluated 25 episodes in the testing set for each task to avoid result bias from noise.
- **p. 10 / 4 Experiments - extractive body cue:** For visual observation, we employ RGB-D images captured by a single front camera with a resolution of 128×128.
- **p. 10 / 4 Experiments - extractive body cue:** An episode is considered successful if the agent completes the goal specified in natural language within a maximum of 25 steps.
- **p. 10 / 4 Experiments - extractive body cue:** All the compared methods are trained on two NVIDIA RTX 4090 GPUs for 100k iterations with a batch size of 2.
- **p. 10 / 4 Experiments - extractive body cue:** We employ LAMB optimizer [72] with an initial learning rate 5×10-4.
- **p. 11 / 4 Experiments - extractive body cue:** We evaluate 25 episodes per task for the final checkpoint on 10 challenging tasks from RLBench and report the success rates (%), where the second ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The limitations stem from the necessity of multiple view supervision with camera calibration for the Gaussian Splatting framework. | p. 14 (5 Conclusion) |
| body limitation/failure cue | Fig. 1: Consider the human instruction "stack two rose blocks", where the task is con- sidered successful if two rose blocks are stacked upon ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | First, based on the front view observation where the gripper shape cannot be seen, our ManiGaussian offers superior detail in modeling cubes in novel ... | p. 14 (4 Experiments) |
| body limitation/failure cue | We evaluated 25 episodes in the testing set for each task to avoid result bias from noise. | p. 10 (4 Experiments) |
| body limitation/failure cue | However, it ignores the scene-level spatiotemporal dynamics that demonstrate the interaction among objects, and the predicted actions still fail to achieve human goals because ... | p. 11 (4 Experiments) |
| body limitation/failure cue | Planning Long Tools Motion Screw Occlusion Average ✗ ✗ ✗ 36.0 2.0 25.3 52.0 4.0 28.0 23.6 ✓ ✗ ✗ 46.0 4.0 52.0 52.0 ... | p. 11 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We employ LAMB optimizer [72] with an initial learning rate 5×10-4. | p. 10 (4 Experiments) |
| All the compared methods are trained on two NVIDIA RTX 4090 GPUs for 100k iterations with a batch size of 2. | p. 10 (4 Experiments) |
| We evaluate 25 episodes per task for the final checkpoint on 10 challenging tasks from RLBench and report the success rates (%), where the ... | p. 11 (4 Experiments) |
| We first implement a vanilla baseline without any proposed technique, where we directly train the representation model and the action decoder to predict the ... | p. 12 (4 Experiments) |
| Particularly, the proposed deformation predictor improves the task completion of 4 out of 6 task types, which demonstrates the importance of the scenelevel dynamics ... | p. 12 (4 Experiments) |
| Both the compared methods get convergence within 100k training steps. | p. 13 (4 Experiments) |
| For dynamic Gaussian Splatting, we leverage a Gaussian regressor to infer the Gaussian distribution of geometric and semantic features in the scene based on ... | p. 6 (3 Approach) |
| (2) The positions, colors, rotations, scales, and opacities with the superscript t represent their counterparts at the tth step in the propagation, and f ... | p. 7 (3 Approach) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 14 / 5 Conclusion - extractive body cue:** The limitations stem from the necessity of multiple view supervision with camera calibration for the Gaussian Splatting framework.
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: Consider the human instruction "stack two rose blocks", where the task is con- sidered successful if two rose blocks are stacked upon the ...
- **p. 14 / 4 Experiments - extractive body cue:** First, based on the front view observation where the gripper shape cannot be seen, our ManiGaussian offers superior detail in modeling cubes in novel views.
- **p. 10 / 4 Experiments - extractive body cue:** We evaluated 25 episodes in the testing set for each task to avoid result bias from noise.
- **p. 11 / 4 Experiments - extractive body cue:** However, it ignores the scene-level spatiotemporal dynamics that demonstrate the interaction among objects, and the predicted actions still fail to achieve human goals because of ...
- **p. 11 / 4 Experiments - extractive body cue:** Planning Long Tools Motion Screw Occlusion Average ✗ ✗ ✗ 36.0 2.0 25.3 52.0 4.0 28.0 23.6 ✓ ✗ ✗ 46.0 4.0 52.0 52.0 24.0 ...

- **PDF anchors reviewed:** datasets p. 11 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments), metrics p. 11 (4 Experiments), p. 12 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), baselines p. 13 (Figure/Table caption), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), results p. 11 (4 Experiments), p. 12 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
