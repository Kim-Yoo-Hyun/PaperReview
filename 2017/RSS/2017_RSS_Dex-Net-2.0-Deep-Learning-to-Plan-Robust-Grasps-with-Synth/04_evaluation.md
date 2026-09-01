# Evaluation - Dex-Net 2.0: Deep Learning to Plan Robust Grasps with Synthetic Point Clouds and Analytic Grasp Metrics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1703.09312; PDF retrieval source: https://arxiv.org/pdf/1703.09312. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 8 (VI. EXPERIMENTS), p. 8 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS)): We found that GQ planned grasps 3× faster than REG and achieved a high 93% success rate and 94% precision.

## Evaluation Body Digest

- **p. 7 / VI. EXPERIMENTS - extractive PDF cue:** To benchmark the architecture outside of our datasets, we trained on the Cornell Grasping Dataset [31] (containing 8,019 examples) and achieved a 93.0% recognition rate ...
- **p. 6 / VI. EXPERIMENTS - extractive PDF cue:** 5 illustrates the physical object datasets used in the benchmark: 1) Train: A validation set of 8 3D-printed objects with adversarial geometric features such as ...
- **p. 6 / VI. EXPERIMENTS - extractive PDF cue:** We used four different GQ-CNN training datasets to study the effect on performance, each with a 80-20 image-wise training and validation split: 1) Adv-Synth: Synthetic ...
- **p. 8 / VI. EXPERIMENTS - extractive PDF cue:** IGQ REG GQ-Adv-Phys GQ-Adv GQ-S GQ Success Rate (%) 60±13 52±14 68±13 74±12 72±12 80±11 Precision (%) N/A N/A 68 87 92 100 Robust Grasp ...
- **p. 5 / VI. EXPERIMENTS - extractive PDF cue:** [16] to benchmark the performance of grasping a single object.
- **p. 5 / VI. EXPERIMENTS - extractive PDF cue:** Physical Benchmark Description We created a benchmark for grasping single objects on a tabletop to compare grasp planning methods.
- **p. 7 / VI. EXPERIMENTS - extractive PDF cue:** Amount of Pretraining We trained three GQ-CNNs on the synthetic dataset of adversarial training objects (Adv-Synth) to study the effect of pretraining with Dex-Net for ...
- **p. 8 / VI. EXPERIMENTS - extractive PDF cue:** The dataset contains rigid, articulated, and deformable objects.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** VI. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| VI. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | We found that GQ planned grasps 3× faster than REG and achieved a high 93% success rate and 94% precision. | p. 7 (VI. EXPERIMENTS) |
| VI. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results also suggest that training on the full Dex-Net 2.0 dataset was necessary to achieve higher than 90% success. | p. 7 (VI. EXPERIMENTS) |
| VI. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | IGQ REG GQ-Adv-Phys GQ-Adv GQ-S GQ Success Rate (%) 60±13 52±14 68±13 74±12 72±12 80±11 Precision (%) N/A N/A 68 87 92 100 Robust ... | p. 8 (VI. EXPERIMENTS) |
| VI. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Performance decreases with smaller training datasets, but the GQ-CNN methods outperform the image-based grasp quality metrics (IGQ) and point cloud registration (REG). | p. 8 (VI. EXPERIMENTS) |
| VI. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | 2) Precision: The success rate on grasps that are have an estimated robustness higher than 50%. | p. 6 (VI. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 7 / VI. EXPERIMENTS - extractive PDF cue:** To benchmark the architecture outside of our datasets, we trained on the Cornell Grasping Dataset [31] (containing 8,019 examples) and achieved a 93.0% recognition rate ...
- **p. 6 / VI. EXPERIMENTS - extractive PDF cue:** 5 illustrates the physical object datasets used in the benchmark: 1) Train: A validation set of 8 3D-printed objects with adversarial geometric features such as ...
- **p. 6 / VI. EXPERIMENTS - extractive PDF cue:** We used four different GQ-CNN training datasets to study the effect on performance, each with a 80-20 image-wise training and validation split: 1) Adv-Synth: Synthetic ...
- **p. 8 / VI. EXPERIMENTS - extractive PDF cue:** IGQ REG GQ-Adv-Phys GQ-Adv GQ-S GQ Success Rate (%) 60±13 52±14 68±13 74±12 72±12 80±11 Precision (%) N/A N/A 68 87 92 100 Robust Grasp ...
- **p. 5 / VI. EXPERIMENTS - extractive PDF cue:** [16] to benchmark the performance of grasping a single object.
- **p. 5 / VI. EXPERIMENTS - extractive PDF cue:** Physical Benchmark Description We created a benchmark for grasping single objects on a tabletop to compare grasp planning methods.
- **p. 7 / VI. EXPERIMENTS - extractive PDF cue:** Amount of Pretraining We trained three GQ-CNNs on the synthetic dataset of adversarial training objects (Adv-Synth) to study the effect of pretraining with Dex-Net for ...
- **p. 8 / VI. EXPERIMENTS - extractive PDF cue:** The dataset contains rigid, articulated, and deformable objects.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: Dex-Net 2.0 Architecture. (Center) The Grasp Quality Convolutional Neural Network (GQ-CNN) is trained offline to predict the robustness candidate grasps from depth images ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2: Graphical model for robust parallel-jaw grasping of objects on a table surface based on point clouds. Blue nodes are variables included in the ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2. Second, the relationship between point clouds, grasps, and metrics over a large datset of objects may be complex and difficult to learn with ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 3: Dex-Net 2.0 pipeline for training dataset generation. (Left) The database contains 1,500 3D object mesh models. (Top) For each object, we sample hundreds ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 4: (Left) Architecture of the Grasp Quality Convolutional Neural Network (GQ-CNN). Planar grasp candidates u = (i, j, ϕ, z) are generated from a ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 3. We compute these parameters by transforming grasps into the camera frame of reference using the camera pose Tc and projecting the 3D grasp ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 5: (Left) The experimental platform for benchmarking grasping with the ABB YuMi. We registered the camera to the robot with a chessboard before each ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 6: Receiver operating character- istic comparing the performance of learning models on Adv-Synth. The GQ-CNN models all perform simi- larly and have a significantly ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To benchmark the architecture outside of our datasets, we trained on the Cornell Grasping Dataset [31] (containing 8,019 examples) and achieved a 93.0% recognition ... | embodiment, simulator version and control stack | p. 7 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS) |
| Task/environment | 5 illustrates the physical object datasets used in the benchmark: 1) Train: A validation set of 8 3D-printed objects with adversarial geometric features such ... | reset, timeout, object/scene variation | p. 6 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 2 (III. PROBLEM STATEMENT), p. 3 (III. PROBLEM STATEMENT) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 3 (III. PROBLEM STATEMENT), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Comparions of Methods GQ-CNN Parameter Sensitivity Random IGQ ML-RF ML-SVM REG GQ-L-Adv GQ-S-Adv GQ-Adv GQ-Adv-Phys GQ-Adv-FC GQ-Adv-LowU GQ-Adv-HighU Success Rate (%) 58±11 70±10 75±9 ... | definition/direction/unit from same section | p. 7 (VI. EXPERIMENTS) |
| 2) Precision: The success rate on grasps that are have an estimated robustness higher than 50%. | definition/direction/unit from same section | p. 6 (VI. EXPERIMENTS) |
| We found that GQ planned grasps 3× faster than REG and achieved a high 93% success rate and 94% precision. | definition/direction/unit from same section | p. 7 (VI. EXPERIMENTS) |
| GQ performs best in terms of success rate and precision, with 100% precision (zero false positives among 29 positive classifications). | definition/direction/unit from same section | p. 8 (VI. EXPERIMENTS) |
| 1) Success Rate: The percentage of grasps that were able to lift, transport, and hold a desired object after shaking. | definition/direction/unit from same section | p. 6 (VI. EXPERIMENTS) |
| Fig. 4: (Left) Architecture of the Grasp Quality Convolutional Neural Network (GQ-CNN). Planar grasp candidates u = (i, j, ϕ, z) are generated from ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| The CEM-augmented Dex-Net 2.0 grasp planner achieved 94% success and 99% precision (68 successes out of 69 grasps classified as robust), and it took ... | definition/direction/unit from same section | p. 8 (VI. EXPERIMENTS) |
| Fig. 1: Dex-Net 2.0 Architecture. (Center) The Grasp Quality Convolutional Neural Network (GQ-CNN) is trained offline to predict the robustness candidate grasps from depth ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Grasp Planning Methods Used for Comparison We compared a number of grasp planning methods on simulated and real data. | comparison identity and matched condition | p. 6 (VI. EXPERIMENTS) |
| Performance Comparison on Novel Objects We also compared the performance of the methods on the ten novel test objects from Test to evaluate generalization ... | comparison identity and matched condition | p. 7 (VI. EXPERIMENTS) |
| We also compared the performance of a Random Forest with 200 | comparison identity and matched condition | p. 6 (VI. EXPERIMENTS) |
| The GQ-CNNs outperformed ML-RF and ML-SVM, achieving near-perfect validation accuracy. | comparison identity and matched condition | p. 7 (VI. EXPERIMENTS) |
| Performance decreases with smaller training datasets, but the GQ-CNN methods outperform the image-based grasp quality metrics (IGQ) and point cloud registration (REG). | comparison identity and matched condition | p. 8 (VI. EXPERIMENTS) |
| Each method was tested for 50 trials, and details on the methods used for comparison can be found in Section VI-C. | comparison identity and matched condition | p. 8 (VI. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We also trained several variants to evaluate sensitivity to several parameters: Dataset Size. | component/input/data sensitivity | p. 7 (VI. EXPERIMENTS) |
| Amount of Pretraining We trained three GQ-CNNs on the synthetic dataset of adversarial training objects (Adv-Synth) to study the effect of pretraining with Dex-Net ... | component/input/data sensitivity | p. 7 (VI. EXPERIMENTS) |
| A human operator was required to reset the object in the workspace on each trial, and therefore blinded operators from which grasp planning method ... | component/input/data sensitivity | p. 5 (VI. EXPERIMENTS) |
| Pretraining does not appear to affect performance. cient of µ = 0.5 in 50 physical trials per object in Train (400 datapoints). | component/input/data sensitivity | p. 6 (VI. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our primary contributions are: 1) the Dexterity Network (Dex-Net) 2.0, a dataset associating 6.7 million point clouds and analytic grasp quality metrics with parallel-jaw ... | We found that GQ planned grasps 3× faster than REG and achieved a high 93% success rate and 94% precision. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 8 (VI. EXPERIMENTS), p. 8 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS) |
| Primary metric/result | The results also suggest that training on the full Dex-Net 2.0 dataset was necessary to achieve higher than 90% success. | numeric claim only at cited anchor | p. 7 (VI. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / VI. EXPERIMENTS - extractive PDF cue:** (Top-Right) The training set of 8 objects with adversarial geometric features such as smooth curved surfaces and narrow openings for grasping known objects.
- **p. 7 / VI. EXPERIMENTS - extractive PDF cue:** Comparions of Methods GQ-CNN Parameter Sensitivity Random IGQ ML-RF ML-SVM REG GQ-L-Adv GQ-S-Adv GQ-Adv GQ-Adv-Phys GQ-Adv-FC GQ-Adv-LowU GQ-Adv-HighU Success Rate (%) 58±11 70±10 75±9 80±9 ...
- **p. 7 / VI. EXPERIMENTS - extractive PDF cue:** Each method was tested for 80 trials (10 trials per object).
- **p. 7 / VI. EXPERIMENTS - extractive PDF cue:** GQ) using the thresholded robust epsilon metric with δ = 0.002 [25] for 5 epochs on Dex-Net-Large (all of Dex-Net 2.0) using Gaussian process image ...
- **p. 7 / VI. EXPERIMENTS - extractive PDF cue:** Training took approximately 48 hours on an NVIDIA GeForce 1080.
- **p. 7 / VI. EXPERIMENTS - extractive PDF cue:** The first layer of 7×7 convolution filters are shown in the right panel of Fig.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The most common failure modes were related to: (left) missing sensor data for an important part of the object geometry, such as thin parts ... | p. 8 (I. Failure Modes) |
| body limitation/failure cue | A second type of failure occured due to collisions with the object. | p. 8 (I. Failure Modes) |
| body limitation/failure cue | Fig. 3: Dex-Net 2.0 pipeline for training dataset generation. (Left) The database contains 1,500 3D object mesh models. (Top) For each object, we sample ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Fig. 4: (Left) Architecture of the Grasp Quality Convolutional Neural Network (GQ-CNN). Planar grasp candidates u = (i, j, ϕ, z) are generated from ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | Fig. 9: (Left) Grasp robustness predicted by a Grasp Quality Convolutional Neural Network (GQ-CNN) trained with Dex-Net 2.0 over the space of depth images ... | p. 10 (Figure/Table caption) |
| body limitation/failure cue | We chose objects based on geometric features under three constraints: (a) small enough to fit within the workspace, (b) weight less than 0.25kg, the ... | p. 6 (VI. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We used TensorFlow [1] with a batch size of 128, a momentum term of 0.9, and an exponentially decaying learning rate with step size ... | p. 7 (VI. EXPERIMENTS) |
| Each method was run for 50 trials (5 per object). | p. 7 (VI. EXPERIMENTS) |
| All experiments ran on a Desktop running Ubuntu 14.04 with a 2.7 GHz Intel Core i5-6400 Quad-Core CPU and an NVIDIA GeForce 980, and ... | p. 5 (VI. EXPERIMENTS) |
| Pretraining does not appear to affect performance. cient of µ = 0.5 in 50 physical trials per object in Train (400 datapoints). | p. 6 (VI. EXPERIMENTS) |
| In each trial a human operator sampled an object pose by shaking the object in a box and placing it upside down in the ... | p. 6 (VI. EXPERIMENTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / I. Failure Modes - extractive PDF cue:** The most common failure modes were related to: (left) missing sensor data for an important part of the object geometry, such as thin parts of ...
- **p. 8 / I. Failure Modes - extractive PDF cue:** A second type of failure occured due to collisions with the object.
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 3: Dex-Net 2.0 pipeline for training dataset generation. (Left) The database contains 1,500 3D object mesh models. (Top) For each object, we sample hundreds ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 4: (Left) Architecture of the Grasp Quality Convolutional Neural Network (GQ-CNN). Planar grasp candidates u = (i, j, ϕ, z) are generated from a ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Fig. 9: (Left) Grasp robustness predicted by a Grasp Quality Convolutional Neural Network (GQ-CNN) trained with Dex-Net 2.0 over the space of depth images and ...
- **p. 6 / VI. EXPERIMENTS - extractive PDF cue:** We chose objects based on geometric features under three constraints: (a) small enough to fit within the workspace, (b) weight less than 0.25kg, the payload ...

- **PDF anchors reviewed:** datasets p. 7 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 8 (VI. EXPERIMENTS), p. 5 (VI. EXPERIMENTS), p. 5 (VI. EXPERIMENTS), metrics p. 7 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 8 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 5 (Figure/Table caption), baselines p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 8 (VI. EXPERIMENTS), p. 8 (VI. EXPERIMENTS), results p. 7 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 8 (VI. EXPERIMENTS), p. 8 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
