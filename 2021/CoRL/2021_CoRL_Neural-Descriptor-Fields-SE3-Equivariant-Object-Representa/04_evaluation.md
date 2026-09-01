# Evaluation - Neural Descriptor Fields: SE(3)-Equivariant Object Representations for Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2112.05124; PDF retrieval source: https://arxiv.org/pdf/2112.05124. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (II. METHOD), p. 6 (II. METHOD), p. 7 (II. METHOD), p. 7 (II. METHOD), p. 5 (II. METHOD), p. 3 (II. METHOD)): For objects in arbitrary poses (bottom row), DON's performance suffers, while NDFs maintains higher success rates due to their equivariance to SE(3) transformations. to achieve success rate above 10%.

## Evaluation Body Digest

- **p. 7 / II. METHOD - extractive body cue:** Next, we consider a harder setting: while the demonstrations are all performed on upright-posed objects, the robot must subsequently execute the task on objects in ...
- **p. 5 / II. METHOD - extractive body cue:** We provide 10 demonstrations for each task, and measure execution success rates on unseen object instances with randomly sampled initial poses and a random
- **p. 3 / II. METHOD - extractive body cue:** On first glance, this would require setting up a training objective for correspondence matching, and consequently, collection and labeling of a custom dataset.
- **p. 3 / II. METHOD - extractive body cue:** These latent codes are obtained as the output of a PointNet [32]- based point cloud encoder E that takes as input a point cloud P, ...
- **p. 6 / II. METHOD - extractive body cue:** To pretrain DON [10] and NDF, we generate a dataset of 100,000 objects of mug, bowl and bottle categories at random tabletop poses.
- **p. 7 / II. METHOD - extractive body cue:** Real World Execution Finally, we validate that NDFs enable manipulation of novel object instances in novel poses on the real robot.
- **p. 4 / II. METHOD - extractive body cue:** 4: Energy landscape induced by NDFs - Given a demonstration in the form of a pointcloud-point tuple (ˆP, ˆx), and the pointcloud of an unseen ...
- **p. 6 / II. METHOD - extractive body cue:** We assume a segmented object point cloud and a static environment that remains fixed between demonstration-time and test-time.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| II. METHOD | EMPIRICAL / REAL-ROBOT OR HARDWARE | For objects in arbitrary poses (bottom row), DON's performance suffers, while NDFs maintains higher success rates due to their equivariance to SE(3) transformations. to ... | p. 6 (II. METHOD) |
| II. METHOD | EMPIRICAL / REAL-ROBOT OR HARDWARE | For objects in upright poses (top row), NDFs perform on par with DON on grasp success rate, but outperforms DON on overall pick-and-place success ... | p. 6 (II. METHOD) |
| II. METHOD | EMPIRICAL / REAL-ROBOT OR HARDWARE | We find that while the performance of NDFs decreases significantly in the singledemonstration case, it still significantly outperforms DON, and more demonstrations yield significant ... | p. 7 (II. METHOD) |
| II. METHOD | EMPIRICAL / REAL-ROBOT OR HARDWARE | In contrast, we find that NDF's performance, while not at the same level as in the upright task, suffers dramatically less, maintaining a high ... | p. 7 (II. METHOD) |
| II. METHOD | EMPIRICAL / REAL-ROBOT OR HARDWARE | We provide 10 demonstrations for each task, and measure execution success rates on unseen object instances with randomly sampled initial poses and a random | p. 5 (II. METHOD) |

## Dataset / Benchmark Role

- **p. 7 / II. METHOD - extractive body cue:** Next, we consider a harder setting: while the demonstrations are all performed on upright-posed objects, the robot must subsequently execute the task on objects in ...
- **p. 5 / II. METHOD - extractive body cue:** We provide 10 demonstrations for each task, and measure execution success rates on unseen object instances with randomly sampled initial poses and a random
- **p. 3 / II. METHOD - extractive body cue:** On first glance, this would require setting up a training objective for correspondence matching, and consequently, collection and labeling of a custom dataset.
- **p. 3 / II. METHOD - extractive body cue:** These latent codes are obtained as the output of a PointNet [32]- based point cloud encoder E that takes as input a point cloud P, ...
- **p. 6 / II. METHOD - extractive body cue:** To pretrain DON [10] and NDF, we generate a dataset of 100,000 objects of mug, bowl and bottle categories at random tabletop poses.
- **p. 7 / II. METHOD - extractive body cue:** Real World Execution Finally, we validate that NDFs enable manipulation of novel object instances in novel poses on the real robot.
- **p. 4 / II. METHOD - extractive body cue:** 4: Energy landscape induced by NDFs - Given a demonstration in the form of a pointcloud-point tuple (ˆP, ˆx), and the pointcloud of an unseen ...
- **p. 6 / II. METHOD - extractive body cue:** We assume a segmented object point cloud and a static environment that remains fixed between demonstration-time and test-time.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Given a few (∼5-10) demonstrations of a manipulation task (left), Neural Descriptor Fields (NDFs) generalize the task to novel object instances in any ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Point Descriptor Fields - We propose to parameterize a Neural Point Descriptor Field f as the concatenation of the layer- wise activations of ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: Pose Descriptor Fields - NDFs can extract pose descriptors by representing a pose via its action on a query pointcloud X, and then ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: Energy landscape induced by NDFs - Given a demon- stration in the form of a pointcloud-point tuple (ˆP, ˆx), and the pointcloud of ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5: Equivariance and generalization of NDFs - Absolute descriptor differences for a 2D target point ˆx ∈R2. The point de- scriptor field succeeds in ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6: Effect of different query points - (a) (Top) Given a set of reference mugs and query points X distributed near the rim of ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 7: Pose regression with NDFs - Given a demonstration point cloud and gripper pose (left), our method enables solving for the gripper pose (orange) ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 8: Qualitative Examples of Grasp Predictions - Both DON and NDF predict successful grasps on upright mugs. When mugs exhibit arbitrary poses, DON fails ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Next, we consider a harder setting: while the demonstrations are all performed on upright-posed objects, the robot must subsequently execute the task on objects ... | embodiment, simulator version and control stack | p. 7 (II. METHOD), p. 5 (II. METHOD) |
| Task/environment | We provide 10 demonstrations for each task, and measure execution success rates on unseen object instances with randomly sampled initial poses and a random | reset, timeout, object/scene variation | p. 5 (II. METHOD), p. 3 (II. METHOD) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 3 (II. METHOD), p. 3 (II. METHOD) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 4 (II. METHOD), p. 4 (II. METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For objects in arbitrary poses (bottom row), DON's performance suffers, while NDFs maintains higher success rates due to their equivariance to SE(3) transformations. to ... | definition/direction/unit from same section | p. 6 (II. METHOD) |
| In contrast, we find that NDF's performance, while not at the same level as in the upright task, suffers dramatically less, maintaining a high ... | definition/direction/unit from same section | p. 7 (II. METHOD) |
| We provide 10 demonstrations for each task, and measure execution success rates on unseen object instances with randomly sampled initial poses and a random | definition/direction/unit from same section | p. 5 (II. METHOD) |
| For objects in upright poses (top row), NDFs perform on par with DON on grasp success rate, but outperforms DON on overall pick-and-place success ... | definition/direction/unit from same section | p. 6 (II. METHOD) |
| Analysis We now analyze NDF's dependence on the occupancy network parameterization, the number of demonstrations, and Random NDF Last Layer OccNet First Layer OccNet ... | definition/direction/unit from same section | p. 7 (II. METHOD) |
| Fig. 1: Given a few (∼5-10) demonstrations of a manipulation task (left), Neural Descriptor Fields (NDFs) generalize the task to novel object instances in ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Instead, we propose and demonstrate that we may leverage recently proposed neural implicit shape representations [5, 21, 27] to parameterize f and learn its ... | definition/direction/unit from same section | p. 3 (II. METHOD) |
| This bottleneck forces the model to use these few latent variables to parameterize the salient features of the object category, which is impressively demonstrated ... | definition/direction/unit from same section | p. 3 (II. METHOD) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For objects in upright poses (top row), NDFs perform on par with DON on grasp success rate, but outperforms DON on overall pick-and-place success ... | comparison identity and matched condition | p. 6 (II. METHOD) |
| We find that across mugs, bowls, and bottles, NDFs dramatically outperform DON on placing, and perform significantly better on grasping (Table I, top). | comparison identity and matched condition | p. 7 (II. METHOD) |
| We find that while the performance of NDFs decreases significantly in the singledemonstration case, it still significantly outperforms DON, and more demonstrations yield significant ... | comparison identity and matched condition | p. 7 (II. METHOD) |
| Prior work has leveraged this property of the activations of Φ to classify which semantic part of an object a given coordinate x belongs ... | comparison identity and matched condition | p. 3 (II. METHOD) |
| We then conduct ablation studies of the choice of parameterizing NDFs as the concatenation of pretrained | comparison identity and matched condition | p. 6 (II. METHOD) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 6: Effect of different query points - (a) (Top) Given a set of reference mugs and query points X distributed near the rim ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| We then conduct ablation studies of the choice of parameterizing NDFs as the concatenation of pretrained | component/input/data sensitivity | p. 6 (II. METHOD) |
| 6 highlights this issue by visualizing the effect of different ways of distributing the points in X. | component/input/data sensitivity | p. 5 (II. METHOD) |
| We further study the effect of the scale of the query point cloud X for representing the grasping and placing pose descriptors. | component/input/data sensitivity | p. 7 (II. METHOD) |
| In Table II, we analyze the effect of parameterizing NDFs with features from a randomly initialized occupancy network, as well as with only the ... | component/input/data sensitivity | p. 7 (II. METHOD) |
| Fig. 1: Given a few (∼5-10) demonstrations of a manipulation task (left), Neural Descriptor Fields (NDFs) generalize the task to novel object instances in ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present a novel representation that models dense correspondence across object instances at the level of points and local coordinate frames. | For objects in arbitrary poses (bottom row), DON's performance suffers, while NDFs maintains higher success rates due to their equivariance to SE(3) transformations. to ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (II. METHOD), p. 6 (II. METHOD), p. 7 (II. METHOD), p. 7 (II. METHOD), p. 5 (II. METHOD), p. 3 (II. METHOD) |
| Primary metric/result | For objects in upright poses (top row), NDFs perform on par with DON on grasp success rate, but outperforms DON on overall pick-and-place success ... | numeric claim only at cited anchor | p. 6 (II. METHOD) |

- Numeric sentences retained from the body:
- **p. 6 / II. METHOD - extractive body cue:** To pretrain DON [10] and NDF, we generate a dataset of 100,000 objects of mug, bowl and bottle categories at random tabletop poses.
- **p. 6 / II. METHOD - extractive body cue:** To pretrain DON [10] and NDF, we generate a dataset of 100,000 objects of mug, bowl and bottle categories at random tabletop poses.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Several limitations and avenues for future work remain. | p. 8 (VI. DISCUSSION AND CONCLUSION) |
| body limitation/failure cue | (Bottom) In contrast, placing query points near the bottom of the mug leads to a transferred pose that is biased toward the bottom of ... | p. 6 (II. METHOD) |
| body limitation/failure cue | We find that DON's failures are usually a function of either insufficient precision in keypoint predictions, or failed registration of testtime keypoints to the ... | p. 7 (II. METHOD) |
| body limitation/failure cue | Fig. 8: Qualitative Examples of Grasp Predictions - Both DON and NDF predict successful grasps on upright mugs. When mugs exhibit arbitrary poses, DON ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Furthermore, we assume the placement target remains static: future work may explore similarly inferring an object-centric representation of the placement target. | p. 8 (VI. DISCUSSION AND CONCLUSION) |
| body limitation/failure cue | This is an attractive property, as at test time, we regularly only observe partial point clouds of objects due to occlusions. | p. 3 (II. METHOD) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| This guarantees that we can generalize to arbitrary object poses, including those completely unobserved at training time. | p. 4 (II. METHOD) |
| In Section II-A, we introduce a continuous function f(x/P) that maps a 3D coordinate x and a point cloud P to a spatial descriptor ... | p. 2 (II. METHOD) |
| We demonstrate that we can represent this function using a neural network trained in a task-agnostic manner via 3D reconstruction, and that this training ... | p. 2 (II. METHOD) |
| Both the point cloud encoder and the point descriptor function can be pretrained with a 3D reconstruction task. | p. 3 (II. METHOD) |
| That is, for mugs, descriptors should encode information about how far x is away from the mug's handle, rim, etc. | p. 3 (II. METHOD) |
| With this setup, an initial decision is how to encode local reference frames expressed as SE(3) poses. | p. 4 (II. METHOD) |
| 7 we visualize the optimization steps taken by (11) for optimizing a grasp pose of the end-effector. | p. 5 (II. METHOD) |
| We then leverage (10) to encode each pose Ti ∗ into its vector of descriptors Zi ∗, conditional on the respective object point cloud ... | p. 5 (II. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / VI. DISCUSSION AND CONCLUSION - extractive body cue:** Several limitations and avenues for future work remain.
- **p. 6 / II. METHOD - extractive body cue:** (Bottom) In contrast, placing query points near the bottom of the mug leads to a transferred pose that is biased toward the bottom of the ...
- **p. 7 / II. METHOD - extractive body cue:** We find that DON's failures are usually a function of either insufficient precision in keypoint predictions, or failed registration of testtime keypoints to the demonstration ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 8: Qualitative Examples of Grasp Predictions - Both DON and NDF predict successful grasps on upright mugs. When mugs exhibit arbitrary poses, DON fails ...
- **p. 8 / VI. DISCUSSION AND CONCLUSION - extractive body cue:** Furthermore, we assume the placement target remains static: future work may explore similarly inferring an object-centric representation of the placement target.
- **p. 3 / II. METHOD - extractive body cue:** This is an attractive property, as at test time, we regularly only observe partial point clouds of objects due to occlusions.

- **PDF anchors reviewed:** datasets p. 7 (II. METHOD), p. 5 (II. METHOD), p. 3 (II. METHOD), p. 3 (II. METHOD), p. 6 (II. METHOD), p. 7 (II. METHOD), metrics p. 6 (II. METHOD), p. 7 (II. METHOD), p. 5 (II. METHOD), p. 6 (II. METHOD), p. 7 (II. METHOD), p. 1 (Figure/Table caption), baselines p. 6 (II. METHOD), p. 7 (II. METHOD), p. 7 (II. METHOD), p. 3 (II. METHOD), p. 6 (II. METHOD), results p. 6 (II. METHOD), p. 6 (II. METHOD), p. 7 (II. METHOD), p. 7 (II. METHOD), p. 5 (II. METHOD), p. 3 (II. METHOD).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
