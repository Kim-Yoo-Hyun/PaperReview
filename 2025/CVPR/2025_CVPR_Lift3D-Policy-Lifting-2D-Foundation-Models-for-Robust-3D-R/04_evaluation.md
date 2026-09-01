# Evaluation - Lift3D Policy: Lifting 2D Foundation Models for Robust 3D Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Jia_Lift3D_Policy_Lifting_2D_Foundation_Models_for_Robust_3D_Robotic_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Jia_Lift3D_Policy_Lifting_2D_Foundation_Models_for_Robust_3D_Robotic_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.1. Simulation Experiment), p. 6 (4.1. Simulation Experiment), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 5 (4.1. Simulation Experiment), p. 5 (4. Experiments)): In Table 1, Lift3D(CLIP) achieves an average success rate of 83.9 on the MetaWorld benchmark, with 78.8 accuracy on medium-level tasks and 82.0 accuracy on hard level tasks.

## Evaluation Body Digest

- **p. 6 / 4.1. Simulation Experiment - extractive PDF cue:** Comparison of manipulation success rates between Lift3D and 2D & 3D baselines in simulation benchmarks. ‘2D Rep.' and ‘3D Rep.' refer to robotic 2D representation ...
- **p. 5 / 4.1. Simulation Experiment - extractive PDF cue:** We select over 30 tasks from three widelyused manipulation simulation benchmarks: MetaWorld [76] and Adroit [57] in the MuJoCo simulator, and RLBench [31] in the ...
- **p. 6 / 4.2. Real-World Experiment - extractive PDF cue:** Additional details of the real-world dataset and assets are provided in Appendix A.
- **p. 5 / 4. Experiments - extractive PDF cue:** In Sections 4.1 and 4.2, we evaluate the manipulation capability of our proposed Lift3D by presenting the experimental settings and results from both simulation and ...
- **p. 6 / 4.1. Simulation Experiment - extractive PDF cue:** In Table 1, Lift3D(CLIP) achieves an average success rate of 83.9 on the MetaWorld benchmark, with 78.8 accuracy on medium-level tasks and 82.0 accuracy on ...
- **p. 6 / 4.1. Simulation Experiment - extractive PDF cue:** We report the average success rate of the best-performing policy models across training.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4. Scalability. Y-axis is the manipulation success rate. in Figure 4. Moreover, Lift3D exhibits better scalability than the original DINOv2 models by leveraging its ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Lift3D empowers 2D foundation models with 3D manipulation capabilities by refining implicit 3D robotic representations through task-related affordance masking and depth reconstruction, while ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Simulation Experiment (p. 5); 4.2. Real-World Experiment (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Simulation Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | In Table 1, Lift3D(CLIP) achieves an average success rate of 83.9 on the MetaWorld benchmark, with 78.8 accuracy on medium-level tasks and 82.0 accuracy ... | p. 6 (4.1. Simulation Experiment) |
| 4.1. Simulation Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | In addition, compared to the previous SOTA 3D policy (DP3), Lift3D achieves an accuracy improvement of 18.6. | p. 6 (4.1. Simulation Experiment) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4. Scalability. Y-axis is the manipulation success rate. in Figure 4. Moreover, Lift3D exhibits better scalability than the original DINOv2 models by leveraging ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1. Lift3D empowers 2D foundation models with 3D manipulation capabilities by refining implicit 3D robotic representations through task-related affordance masking and depth reconstruction, ... | p. 1 (Figure/Table caption) |
| 4.1. Simulation Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | Due to space constraints, the results and details of RLBench are provided in Appendix B. | p. 5 (4.1. Simulation Experiment) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Simulation Experiment - extractive PDF cue:** Comparison of manipulation success rates between Lift3D and 2D & 3D baselines in simulation benchmarks. ‘2D Rep.' and ‘3D Rep.' refer to robotic 2D representation ...
- **p. 5 / 4.1. Simulation Experiment - extractive PDF cue:** We select over 30 tasks from three widelyused manipulation simulation benchmarks: MetaWorld [76] and Adroit [57] in the MuJoCo simulator, and RLBench [31] in the ...
- **p. 6 / 4.2. Real-World Experiment - extractive PDF cue:** Additional details of the real-world dataset and assets are provided in Appendix A.
- **p. 5 / 4. Experiments - extractive PDF cue:** In Sections 4.1 and 4.2, we evaluate the manipulation capability of our proposed Lift3D by presenting the experimental settings and results from both simulation and ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Lift3D empowers 2D foundation models with 3D manipulation capabilities by refining implicit 3D robotic representations through task-related affordance masking and depth reconstruction, while ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Overall pipeline of Lift3D. a) For implicit 3D robotic representation, we leverage CLIP [55] to offline extract image attention maps based on task ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Comparison of manipulation success rates between Lift3D and 2D & 3D baselines in simulation benchmarks. ‘2D Rep.' and ‘3D Rep.' refer to robotic ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Quantitative results for real robot experiments. The training setup is consistent with the real-world experiments de- scribed in the main text. For evaluation, ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Ablation study. In the Task-aware MAE, AMS refers to the affordance-guided masking strategy, Depth and RGB refer to the reconstruction targets, and VD ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4. Generalization. ‘Object', ‘Background', and ‘Brightness' represent different manipulated objects, background scenes, and lighting conditions, respectively. The image above illustrates the three test scenarios, ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 3. The qualitative results of Lift3D in real-world experiments, including the input point cloud examples, manipulation progress, and the task completion end state, are ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4. Scalability. Y-axis is the manipulation success rate. in Figure 4. Moreover, Lift3D exhibits better scalability than the original DINOv2 models by leveraging its ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Comparison of manipulation success rates between Lift3D and 2D & 3D baselines in simulation benchmarks. ‘2D Rep.' and ‘3D Rep.' refer to robotic 2D ... | embodiment, simulator version and control stack | p. 6 (4.1. Simulation Experiment), p. 5 (4.1. Simulation Experiment) |
| Task/environment | We select over 30 tasks from three widelyused manipulation simulation benchmarks: MetaWorld [76] and Adroit [57] in the MuJoCo simulator, and RLBench [31] in ... | reset, timeout, object/scene variation | p. 5 (4.1. Simulation Experiment), p. 6 (4.2. Real-World Experiment) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (3.2. Task-aware Masked Autoencoder), p. 4 (3.2. Task-aware Masked Autoencoder) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 7 (Method), p. 3 (3.1. Problem Statement) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In Table 1, Lift3D(CLIP) achieves an average success rate of 83.9 on the MetaWorld benchmark, with 78.8 accuracy on medium-level tasks and 82.0 accuracy ... | definition/direction/unit from same section | p. 6 (4.1. Simulation Experiment) |
| We report the average success rate of the best-performing policy models across training. | definition/direction/unit from same section | p. 6 (4.1. Simulation Experiment) |
| Figure 4. Scalability. Y-axis is the manipulation success rate. in Figure 4. Moreover, Lift3D exhibits better scalability than the original DINOv2 models by leveraging ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 1. Lift3D empowers 2D foundation models with 3D manipulation capabilities by refining implicit 3D robotic representations through task-related affordance masking and depth reconstruction, ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. Overall pipeline of Lift3D. a) For implicit 3D robotic representation, we leverage CLIP [55] to offline extract image attention maps based on ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Table 3. Ablation study. In the Task-aware MAE, AMS refers to the affordance-guided masking strategy, Depth and RGB refer to the reconstruction targets, and ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 4. Generalization. ‘Object', ‘Background', and ‘Brightness' represent different manipulated objects, background scenes, and lighting conditions, respectively. The image above illustrates the three test ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 3. The qualitative results of Lift3D in real-world experiments, including the input point cloud examples, manipulation progress, and the task completion end state, ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In addition, compared to the previous SOTA 3D policy (DP3), Lift3D achieves an accuracy improvement of 18.6. | comparison identity and matched condition | p. 6 (4.1. Simulation Experiment) |
| Lift3D is compared with the previous SOTA 3D Diffusion Policy (DP3) [78] on MetaWorld and Adroit, and with RVT-2 [24] on RLBench. | comparison identity and matched condition | p. 6 (4.1. Simulation Experiment) |
| Table 4. Generalization. ‘Object', ‘Background', and ‘Brightness' represent different manipulated objects, background scenes, and lighting conditions, respectively. The image above illustrates the three test ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| The effectiveness of each component is validated through an ablation study in Section 4.3. | comparison identity and matched condition | p. 5 (4. Experiments) |
| Table 3. Ablation study. In the Task-aware MAE, AMS refers to the affordance-guided masking strategy, Depth and RGB refer to the reconstruction targets, and ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The effectiveness of each component is validated through an ablation study in Section 4.3. | component/input/data sensitivity | p. 5 (4. Experiments) |
| These results demonstrate that Lift3D effectively enhances the 2D foundation model with robust manipulation capabilities, enabling a deeper understanding of robotic 3D scenes by ... | component/input/data sensitivity | p. 6 (4.1. Simulation Experiment) |
| Table 3. Ablation study. In the Task-aware MAE, AMS refers to the affordance-guided masking strategy, Depth and RGB refer to the reconstruction targets, and ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Figure 1. Lift3D empowers 2D foundation models with 3D manipulation capabilities by refining implicit 3D robotic representations through task-related affordance masking and depth reconstruction, ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Additionally, we examine SPA [87], the previous SOTA 3D robotic pretraining method. | component/input/data sensitivity | p. 6 (4.1. Simulation Experiment) |
| Figure 2. Overall pipeline of Lift3D. a) For implicit 3D robotic representation, we leverage CLIP [55] to offline extract image attention maps based on ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are as follows: • We propose Lift3D, which elevates 2D foundation models 17348 | In Table 1, Lift3D(CLIP) achieves an average success rate of 83.9 on the MetaWorld benchmark, with 78.8 accuracy on medium-level tasks and 82.0 accuracy ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.1. Simulation Experiment), p. 6 (4.1. Simulation Experiment), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 5 (4.1. Simulation Experiment), p. 5 (4. Experiments) |
| Primary metric/result | In addition, compared to the previous SOTA 3D policy (DP3), Lift3D achieves an accuracy improvement of 18.6. | numeric claim only at cited anchor | p. 6 (4.1. Simulation Experiment) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Simulation Experiment - extractive PDF cue:** We select over 30 tasks from three widelyused manipulation simulation benchmarks: MetaWorld [76] and Adroit [57] in the MuJoCo simulator, and RLBench [31] in the ...
- **p. 5 / 4.1. Simulation Experiment - extractive PDF cue:** For MetaWorld, a tabletop environment with a Sawyer arm and two-finger gripper, we select 15 tasks of varying difficulty levels [58].
- **p. 5 / 4.1. Simulation Experiment - extractive PDF cue:** Scripted policies are used in MetaWorld [76], where 25 demonstrations are collected, each consisting of 200 steps.
- **p. 6 / 4.1. Simulation Experiment - extractive PDF cue:** We collect 100 demonstrations, each consisting of 100 steps.
- **p. 6 / 4.1. Simulation Experiment - extractive PDF cue:** Demonstrations in RLBench are collected through pre-defined waypoints and the Open Motion Planning Library [63], with 100 episodes gathered, each containing several key frames.
- **p. 6 / 4.1. Simulation Experiment - extractive PDF cue:** The 2D and 3D visual inputs consist of 224 \times 224 RGB images and single-view point clouds with 1,024 points, respectively.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In terms of limitations, our Lift3D framework focuses on lifting 2D vision models to 3D manipulation tasks, which means it cannot comprehend language conditions. | p. 8 (5. Conclusion and Limitation) |
| body limitation/failure cue | In this paper, we introduce Lift3D, a novel framework that integrates large-scale pretrained 2D foundation models with robust 3D manipulation capabilities. | p. 8 (5. Conclusion and Limitation) |
| body limitation/failure cue | Figure 1. Lift3D empowers 2D foundation models with 3D manipulation capabilities by refining implicit 3D robotic representations through task-related affordance masking and depth reconstruction, ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | These results demonstrate that Lift3D effectively enhances the 2D foundation model with robust manipulation capabilities, enabling a deeper understanding of robotic 3D scenes by ... | p. 6 (4.1. Simulation Experiment) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Following previous work [46], the Adam optimizer is employed with parameters (β1, β2) = (0.9, 0.999) and a learning rate of 1e-3. | p. 6 (4.1. Simulation Experiment) |
| A constant learning rate is used for MetaWorld, while a cosine annealing scheduler with a 0.1 warm-up factor is applied for Adroit. | p. 6 (4.1. Simulation Experiment) |
| Scripted policies are used in MetaWorld [76], where 25 demonstrations are collected, each consisting of 200 steps. | p. 5 (4.1. Simulation Experiment) |
| The output features are then fed into a decoder 2Dd for depth reconstruction, D = 2Dd(2De(I)), where D ∈RW ×H×1. | p. 3 (3.1. Problem Statement) |
| For explicit 3D robotic representation, we directly utilize the 2D foundation model 2De to encode 3D point cloud data P ∈RN×3 and the robot ... | p. 3 (3.1. Problem Statement) |
| Note that the attention value for each token is computed by averaging its pixel-level values. | p. 4 (3.2. Task-aware Masked Autoencoder) |
| The masked tokens and encoded visible tokens are processed by the MAE decoder for depth reconstruction, enhancing 3D spatial awareness. | p. 4 (3.2. Task-aware Masked Autoencoder) |
| These 2D PEs are then used to directly encode the 3D tokens. | p. 5 (3.3. 2D Model-lifting Strategy) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion and Limitation - extractive PDF cue:** In terms of limitations, our Lift3D framework focuses on lifting 2D vision models to 3D manipulation tasks, which means it cannot comprehend language conditions.
- **p. 8 / 5. Conclusion and Limitation - extractive PDF cue:** In this paper, we introduce Lift3D, a novel framework that integrates large-scale pretrained 2D foundation models with robust 3D manipulation capabilities.
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Lift3D empowers 2D foundation models with 3D manipulation capabilities by refining implicit 3D robotic representations through task-related affordance masking and depth reconstruction, while ...
- **p. 6 / 4.1. Simulation Experiment - extractive PDF cue:** These results demonstrate that Lift3D effectively enhances the 2D foundation model with robust manipulation capabilities, enabling a deeper understanding of robotic 3D scenes by leveraging ...

- **PDF anchors reviewed:** datasets p. 6 (4.1. Simulation Experiment), p. 5 (4.1. Simulation Experiment), p. 6 (4.2. Real-World Experiment), p. 5 (4. Experiments), metrics p. 6 (4.1. Simulation Experiment), p. 6 (4.1. Simulation Experiment), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 4 (Figure/Table caption), p. 7 (Figure/Table caption), baselines p. 6 (4.1. Simulation Experiment), p. 6 (4.1. Simulation Experiment), p. 7 (Figure/Table caption), p. 5 (4. Experiments), p. 7 (Figure/Table caption), results p. 6 (4.1. Simulation Experiment), p. 6 (4.1. Simulation Experiment), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 5 (4.1. Simulation Experiment), p. 5 (4. Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
