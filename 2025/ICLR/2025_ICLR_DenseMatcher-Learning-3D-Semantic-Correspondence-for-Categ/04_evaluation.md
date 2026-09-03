# Evaluation - DenseMatcher: Learning 3D Semantic Correspondence for Category-Level Manipulation from a Single Demo

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=8oFvUBvF1u; PDF retrieval source: https://openreview.net/pdf/be9894ba90b07c5ec0bd2deda17f1b1b8eeab2aa.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (6.1.2 RESULTS), p. 7 (6.1.2 RESULTS), p. 9 (6.1.2 RESULTS), p. 9 (6.1.2 RESULTS), p. 7 (6.1.2 RESULTS), p. 8 (6.1.2 RESULTS)): As can be seen, the mapping obtained with our method significantly outperforms baselines in terms of accuracy and continuity.

## Evaluation Body Digest

- **p. 7 / 6.1.2 RESULTS - extractive body cue:** 6.2 ZERO-SHOT REAL WORLD ROBOTIC MANIPULATION We create six real-world manipulation environments, exploring the performance of DenseMatcher on daily life tasks by comparing the shape, ...
- **p. 8 / 6.1.2 RESULTS - extractive body cue:** The classification of tasks is based on the differences between the objects manipulated in the human demonstration and manipulated by the robot.
- **p. 8 / 6.1.2 RESULTS - extractive body cue:** We use a RealSense L515 RGB-D camera and a UR5 robot arm to conduct all the real-world experiments.
- **p. 7 / 6 EXPERIMENTS - extractive body cue:** We perform exhaustive evaluation across a spectrum of tasks, encompassing 3D Dense Matching, Color Transfer, and Zero-Shot Robot Manipulation.
- **p. 9 / 6.1.2 RESULTS - extractive body cue:** Preprint Figure 8: KeyFrames of 6 robotic tasks.
- **p. 9 / 6.1.2 RESULTS - extractive body cue:** 6.2.3 ROBOT MANIPULATION RESULTS In Tab.
- **p. 18 / A.3.3 INFERENCE RUNTIME ANALYSIS - extractive body cue:** Overall, computing correspondences between a pair of meshes with our algorithm consumes between 8.4 and 12.4 seconds on a single A100 GPU, allowing time-sensitive applications ...
- **p. 10 / 6.1.2 RESULTS - extractive body cue:** (2023) shows that dense correspondences can be used to transfer object appeareances in 2D images.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 6 EXPERIMENTS (p. 7); 6.1.2 RESULTS (p. 7); A.1.2 DATASET FILTERING (p. 16); A.3 EXPERIMENT DETAILS (p. 18).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 6.1.2 RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | As can be seen, the mapping obtained with our method significantly outperforms baselines in terms of accuracy and continuity. | p. 10 (6.1.2 RESULTS) |
| 6.1.2 RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Additionally, due to the generalization capability of pre-trained 2D backbones, we achieve much higher accuracy on out-of-distribution test categories listed in Tab. | p. 7 (6.1.2 RESULTS) |
| 6.1.2 RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | For each task, we measure the task success rates over five trials. | p. 9 (6.1.2 RESULTS) |
| 6.1.2 RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | 3, we compare the success rate of Robo-ABC with our method in the real world, and use task success rates as the evaluation metric. | p. 9 (6.1.2 RESULTS) |
| 6.1.2 RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | 1, we found that our model achieves better AUC and Err compared to the baseline model. | p. 7 (6.1.2 RESULTS) |

## Dataset / Benchmark Role

- **p. 7 / 6.1.2 RESULTS - extractive body cue:** 6.2 ZERO-SHOT REAL WORLD ROBOTIC MANIPULATION We create six real-world manipulation environments, exploring the performance of DenseMatcher on daily life tasks by comparing the shape, ...
- **p. 8 / 6.1.2 RESULTS - extractive body cue:** The classification of tasks is based on the differences between the objects manipulated in the human demonstration and manipulated by the robot.
- **p. 8 / 6.1.2 RESULTS - extractive body cue:** We use a RealSense L515 RGB-D camera and a UR5 robot arm to conduct all the real-world experiments.
- **p. 7 / 6 EXPERIMENTS - extractive body cue:** We perform exhaustive evaluation across a spectrum of tasks, encompassing 3D Dense Matching, Color Transfer, and Zero-Shot Robot Manipulation.
- **p. 9 / 6.1.2 RESULTS - extractive body cue:** Preprint Figure 8: KeyFrames of 6 robotic tasks.
- **p. 9 / 6.1.2 RESULTS - extractive body cue:** 6.2.3 ROBOT MANIPULATION RESULTS In Tab.
- **p. 18 / A.3.3 INFERENCE RUNTIME ANALYSIS - extractive body cue:** Overall, computing correspondences between a pair of meshes with our algorithm consumes between 8.4 and 12.4 seconds on a single A100 GPU, allowing time-sensitive applications ...
- **p. 10 / 6.1.2 RESULTS - extractive body cue:** (2023) shows that dense correspondences can be used to transfer object appeareances in 2D images.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: (a) Zero-shot color transfer between 3D assets. (b) In real-world robotic experi- ments, we use DenseMatcher to transfer a manipulation sequence to the ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: The 4 types of correspon- dence. The reference image is on the left, while the right side demonstrates 1) 3D dense, 2) 3D ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3: Predicted correspondences on few-shot categories. DenseMatcher can generalize across diverse topological variations, given only 5 training examples per category. To ensure that the ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 4: Semantic group annotations examples of apple, banana, animals (deer, tiger, elephant), and chairs. Different colors represent different semantic groups across the same category. ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 5: Two possible partitioning schemes for a hand are shown. The definition of correspondence is inherently subjective. For instance, elephant tusks and rhino tusks ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 6: DenseMatcher model architecture. SD-DINO (Zhang et al., 2023) fuses 2D features from DINOv2 and Stable Diffusion, which are aggregated and fed into a ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Performance comparison on DenseCorr3D shape matching benchmark. We report the results on both the full test set and the held-out set. Ablation studies ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7: Real-World Experiment Workflow. We obtain template mesh and contact points from a human demonstration with hand-object detector (Shan et al., 2020). We then ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 6.2 ZERO-SHOT REAL WORLD ROBOTIC MANIPULATION We create six real-world manipulation environments, exploring the performance of DenseMatcher on daily life tasks by comparing the ... | embodiment, simulator version and control stack | p. 7 (6.1.2 RESULTS), p. 8 (6.1.2 RESULTS) |
| Task/environment | The classification of tasks is based on the differences between the objects manipulated in the human demonstration and manipulated by the robot. | reset, timeout, object/scene variation | p. 8 (6.1.2 RESULTS), p. 8 (6.1.2 RESULTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 5 (1 INTRODUCTION), p. 19 (A.4.1 PRELIMINARY) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For each task, we measure the task success rates over five trials. | definition/direction/unit from same section | p. 9 (6.1.2 RESULTS) |
| 3, we compare the success rate of Robo-ABC with our method in the real world, and use task success rates as the evaluation metric. | definition/direction/unit from same section | p. 9 (6.1.2 RESULTS) |
| Additionally, due to the generalization capability of pre-trained 2D backbones, we achieve much higher accuracy on out-of-distribution test categories listed in Tab. | definition/direction/unit from same section | p. 7 (6.1.2 RESULTS) |
| As can be seen, the mapping obtained with our method significantly outperforms baselines in terms of accuracy and continuity. | definition/direction/unit from same section | p. 10 (6.1.2 RESULTS) |
| 1, we perform several ablation studies by (i) skipping DiffusionNet and directly feeding normalized fmultiview into functional map (ii) training our model without loss ... | definition/direction/unit from same section | p. 10 (6.1.2 RESULTS) |
| We evaluate its performance when respectively trained on FAUST (Bogo et al., 2014a) and DenseCorr3D. | definition/direction/unit from same section | p. 7 (6 EXPERIMENTS) |
| After obtaining the template mesh and keypoints, we calculate the dense descriptors for both the template mesh and the target mesh using DenseMatcher, and ... | definition/direction/unit from same section | p. 8 (6.1.2 RESULTS) |
| Task Peel a Banana Flower Arrangement Place Shoes Decorate Chrismas Tree Pull Out the Carrot Point Object Parts with Pen Overall Robo-ABC† 2/5 1/5 ... | definition/direction/unit from same section | p. 8 (6.1.2 RESULTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 1, we found that our model achieves better AUC and Err compared to the baseline model. | comparison identity and matched condition | p. 7 (6.1.2 RESULTS) |
| As can be seen, the mapping obtained with our method significantly outperforms baselines in terms of accuracy and continuity. | comparison identity and matched condition | p. 10 (6.1.2 RESULTS) |
| ConsistFMap (Cao & Bernard, 2022) utilizes cycle-consistency for robust multi-shape matching across shape collections, making it a strong baseline in unsupervised shape matching. | comparison identity and matched condition | p. 7 (6 EXPERIMENTS) |
| Figure 9: Color transfer results between (i) banana and eggplant, (ii) tomato and kabocha squash, and (iii) wine bottles (iii) gloves. 6.2.2 BASELINE Robo-ABC ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| We compare functional map with two baselines in Fig. | comparison identity and matched condition | p. 10 (6.1.2 RESULTS) |
| Table 5: Runtime of functional map and baselines. All units are in seconds. | comparison identity and matched condition | p. 19 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 10: Ablation study on dense correspondence results. (a) Effect of using different features (HKS, WKS) with functional maps. (b) Comparison of matching methods ... | component/input/data sensitivity | p. 10 (Figure/Table caption) |
| 1, we perform several ablation studies by (i) skipping DiffusionNet and directly feeding normalized fmultiview into functional map (ii) training our model without loss ... | component/input/data sensitivity | p. 10 (6.1.2 RESULTS) |
| In addition, we perform ablation studies on individual components of our model. | component/input/data sensitivity | p. 7 (6 EXPERIMENTS) |
| Since Robo-ABC has its own collected affordance memory, we compared two variants: one with full memory capabilities and another where Robo-ABC's affordance memory is ... | component/input/data sensitivity | p. 9 (6.1.2 RESULTS) |
| In addition, we ran Hungarian matching on the pairwise vertex feature distance matrix for the 500vertex case and 2000-vertex case, purely matching features without ... | component/input/data sensitivity | p. 18 (A.3.3 INFERENCE RUNTIME ANALYSIS) |
| Table 1: Performance comparison on DenseCorr3D shape matching benchmark. We report the results on both the full test set and the held-out set. Ablation ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, we make the following contributions: (i) a novel 3d matching dataset that remedies the lack of texture information and categories in previous ... | As can be seen, the mapping obtained with our method significantly outperforms baselines in terms of accuracy and continuity. | PDF body cue; verify exact table/figure and matched conditions | p. 10 (6.1.2 RESULTS), p. 7 (6.1.2 RESULTS), p. 9 (6.1.2 RESULTS), p. 9 (6.1.2 RESULTS), p. 7 (6.1.2 RESULTS), p. 8 (6.1.2 RESULTS) |
| Primary metric/result | Additionally, due to the generalization capability of pre-trained 2D backbones, we achieve much higher accuracy on out-of-distribution test categories listed in Tab. | numeric claim only at cited anchor | p. 7 (6.1.2 RESULTS) |

- Numeric sentences retained from the body:
- **p. 9 / 6.1.2 RESULTS - extractive body cue:** 6.2.3 ROBOT MANIPULATION RESULTS In Tab.
- **p. 18 / A.3.2 TRAINING DENSEMATCHER - extractive body cue:** We pre-train FeatUp parameters for 10,000 steps on ImageNet (Deng et al., 2009).
- **p. 18 / A.3.2 TRAINING DENSEMATCHER - extractive body cue:** We freeze the 2D backbone models during training, and optimize a 4-block DiffusionNet with 512 channels on DenseCorr3Dfor 6000 steps with a batch size of ...
- **p. 18 / A.3.2 TRAINING DENSEMATCHER - extractive body cue:** In total, training for 50 epochs takes ~12h hours on 8xNvidia A100 GPUs.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Additionally, due to the generalization capability of pre-trained 2D backbones, we achieve much higher accuracy on out-of-distribution test categories listed in Tab. | p. 7 (6.1.2 RESULTS) |
| body limitation/failure cue | ConsistFMap (Cao & Bernard, 2022) utilizes cycle-consistency for robust multi-shape matching across shape collections, making it a strong baseline in unsupervised shape matching. | p. 7 (6 EXPERIMENTS) |
| body limitation/failure cue | To avoid occlusion, we track the object and trace the contact points back to the first frame, thereby obtaining the template keypoint on the ... | p. 8 (6.1.2 RESULTS) |
| body limitation/failure cue | In order to make our model robust to the number of vertices, we randomly set the re-meshing target to between 500 and 2500 vertices ... | p. 18 (A.3.2 TRAINING DENSEMATCHER) |
| body limitation/failure cue | We study the performance of our model under occlusion in two cases. | p. 21 (A.5 PERFORMANCE UNDER OCCLUSION) |
| body limitation/failure cue | Figure 11: Robot experiments visualization under occlusion conditions. A.5.2 PARTIAL SOURCE AND FULL TARGET In the second case, the source mesh is a partial ... | p. 22 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We freeze the 2D backbone models during training, and optimize a 4-block DiffusionNet with 512 channels on DenseCorr3Dfor 6000 steps with a batch size ... | p. 18 (A.3.2 TRAINING DENSEMATCHER) |
| (Coleman et al., 2014) to compute transformation from the target end-effector pose to joint position trajectories. | p. 8 (6.1.2 RESULTS) |
| For each task, we measure the task success rates over five trials. | p. 9 (6.1.2 RESULTS) |
| 10b: Hungarian matching and nearest neighbor retrieval, where we compute a pairwise feature distance matrix between vertices using the same feature from our model. | p. 10 (6.1.2 RESULTS) |
| In total, training for 50 epochs takes ~12h hours on 8xNvidia A100 GPUs. | p. 18 (A.3.2 TRAINING DENSEMATCHER) |
| We also derive theoretical runtime from SpiderMatch (Roetzer & Bernard, 2024) and compare them below in Tab. | p. 19 (A.3.3 INFERENCE RUNTIME ANALYSIS) |
| Method 500-vertex 2000-vertex Functional Map (our implementation) 0.8 2.2 SpiderMatch (Roetzer & Bernard, 2024) ~10 >200 Hungarian Matching (no spatial consistency) 0.01-0.4 0.5-2.5 | p. 19 (A.3.3 INFERENCE RUNTIME ANALYSIS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 6.1.2 RESULTS - extractive body cue:** Additionally, due to the generalization capability of pre-trained 2D backbones, we achieve much higher accuracy on out-of-distribution test categories listed in Tab.
- **p. 7 / 6 EXPERIMENTS - extractive body cue:** ConsistFMap (Cao & Bernard, 2022) utilizes cycle-consistency for robust multi-shape matching across shape collections, making it a strong baseline in unsupervised shape matching.
- **p. 8 / 6.1.2 RESULTS - extractive body cue:** To avoid occlusion, we track the object and trace the contact points back to the first frame, thereby obtaining the template keypoint on the template ...
- **p. 18 / A.3.2 TRAINING DENSEMATCHER - extractive body cue:** In order to make our model robust to the number of vertices, we randomly set the re-meshing target to between 500 and 2500 vertices during ...
- **p. 21 / A.5 PERFORMANCE UNDER OCCLUSION - extractive body cue:** We study the performance of our model under occlusion in two cases.
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 11: Robot experiments visualization under occlusion conditions. A.5.2 PARTIAL SOURCE AND FULL TARGET In the second case, the source mesh is a partial mesh, ...

- **Evidence anchors reviewed:** datasets p. 7 (6.1.2 RESULTS), p. 8 (6.1.2 RESULTS), p. 8 (6.1.2 RESULTS), p. 7 (6 EXPERIMENTS), p. 9 (6.1.2 RESULTS), p. 9 (6.1.2 RESULTS), metrics p. 9 (6.1.2 RESULTS), p. 9 (6.1.2 RESULTS), p. 7 (6.1.2 RESULTS), p. 10 (6.1.2 RESULTS), p. 10 (6.1.2 RESULTS), p. 7 (6 EXPERIMENTS), baselines p. 7 (6.1.2 RESULTS), p. 10 (6.1.2 RESULTS), p. 7 (6 EXPERIMENTS), p. 9 (Figure/Table caption), p. 10 (6.1.2 RESULTS), p. 19 (Figure/Table caption), results p. 10 (6.1.2 RESULTS), p. 7 (6.1.2 RESULTS), p. 9 (6.1.2 RESULTS), p. 9 (6.1.2 RESULTS), p. 7 (6.1.2 RESULTS), p. 8 (6.1.2 RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (22 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Table 1: Performance comparison on DenseCorr3D shape matching benchmark. We report the results on both the full test set and the held-out set. Ablation studies are listed in Section 6.4. ... (p. 7, Figure/Table caption).
- **Metric evidence:** We evaluate its performance when respectively trained on FAUST (Bogo et al., 2014a) and DenseCorr3D. (p. 7, 6 EXPERIMENTS).
- **Baseline/ablation evidence:** 1, we found that our model achieves better AUC and Err compared to the baseline model. (p. 7, 6.1.2 RESULTS).
- **Failure/negative evidence:** As a result, prior methods generating dense 3D features can be divided into two categories: (1) 3D networks that only utilize geometry information and are trained on category-specific datasets (Cao ... (p. 2, 1 INTRODUCTION).
