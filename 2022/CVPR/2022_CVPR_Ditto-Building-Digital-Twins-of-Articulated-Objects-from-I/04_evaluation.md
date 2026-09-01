# Evaluation - Ditto: Building Digital Twins of Articulated Objects from Interaction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2202.08227; PDF retrieval source: https://arxiv.org/pdf/2202.08227. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5.5. Ablation Studies), p. 7 (5.4. Articulated Object Reconstruction), p. 7 (5.4. Articulated Object Reconstruction), p. 8 (5.5. Ablation Studies), p. 12 (Figure/Table caption), p. 6 (Dataset)): 1, Ditto achieves superior or at least on-par performance on all metrics.

## Evaluation Body Digest

- **p. 7 / 5.2. Baselines - extractive body cue:** Reconstructed unseen articulated objects in Shape2Motion [55] (top) and synthetic [1] (bottom) dataset.
- **p. 6 / 5.1. Datasets - extractive body cue:** The synthetic dataset contains procedurally generated articulated objects.
- **p. 6 / 5.1. Datasets - extractive body cue:** We conduct experiments on two 3D articulated object datasets, the synthetic objects dataset provided by Abbatematteo et al.
- **p. 8 / 5.4. Articulated Object Reconstruction - extractive body cue:** We use Ditto trained in simulated datasets to build the digital twin of these physical objects.
- **p. 8 / 5.6. Real-World Experiments - extractive body cue:** Moreover, we import the digital twin of the faucet into Robosuite [62], a robot learning simulation framework.
- **p. 7 / 5.4. Articulated Object Reconstruction - extractive body cue:** On both datasets, Ditto gets significantly better results on all metrics compared with the baselines.
- **p. 7 / 5.3. Evaluation Metrics - extractive body cue:** For the revolute joint, we also measure the axis position error (Pos Err) using the minimum distance between the predicted and ground truth rotation axis.
- **p. 8 / 5.5. Ablation Studies - extractive body cue:** Suffering from a limited capacity, this baseline obtains sub-optimal performance on MobileCD and joint angle errors.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** Dataset (p. 6); 5. Experiments (p. 6); 5.1. Datasets (p. 6); 5.3. Evaluation Metrics (p. 7); 5.6. Real-World Experiments (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.5. Ablation Studies | EMPIRICAL / SIMULATION | 1, Ditto achieves superior or at least on-par performance on all metrics. | p. 8 (5.5. Ablation Studies) |
| 5.4. Articulated Object Reconstruction | EMPIRICAL / SIMULATION | On both datasets, Ditto gets significantly better results on all metrics compared with the baselines. | p. 7 (5.4. Articulated Object Reconstruction) |
| 5.4. Articulated Object Reconstruction | EMPIRICAL / SIMULATION | In contrast, Ditto achieves precise part-level geometry reconstruction as well as accurate joint estimation. | p. 7 (5.4. Articulated Object Reconstruction) |
| 5.5. Ablation Studies | EMPIRICAL / SIMULATION | Share Feature baseline has the worst performance in Mobile CD. | p. 8 (5.5. Ablation Studies) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Table 4. Quantitative results of joint type prediction accuracy on the Shape2Motion [55] dataset. articulated objects. | p. 12 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 5.2. Baselines - extractive body cue:** Reconstructed unseen articulated objects in Shape2Motion [55] (top) and synthetic [1] (bottom) dataset.
- **p. 6 / 5.1. Datasets - extractive body cue:** The synthetic dataset contains procedurally generated articulated objects.
- **p. 6 / 5.1. Datasets - extractive body cue:** We conduct experiments on two 3D articulated object datasets, the synthetic objects dataset provided by Abbatematteo et al.
- **p. 8 / 5.4. Articulated Object Reconstruction - extractive body cue:** We use Ditto trained in simulated datasets to build the digital twin of these physical objects.
- **p. 8 / 5.6. Real-World Experiments - extractive body cue:** Moreover, we import the digital twin of the faucet into Robosuite [62], a robot learning simulation framework.
- **p. 7 / 5.4. Articulated Object Reconstruction - extractive body cue:** On both datasets, Ditto gets significantly better results on all metrics compared with the baselines.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We build digital twins of articulated objects through in- teractive perception. Given visual observations before and after interaction, our method jointly reconstructs the ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Model architecture of Ditto. The input consists of point cloud observations before and after interaction. After a PointNet++ [44] encoder, we fuse the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative results of geometry reconstruction and articulation estimation on Shape2Motion [55] and synthetic [1] datasets.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Reconstructed unseen articulated objects in Shape2Motion [55] (top) and synthetic [1] (bottom) dataset. Static parts are colored grey while mobile parts are colored ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Real-world results. We use Ditto trained in simulated datasets to build the digital twin of these physical objects. The recreated faucet model is ...
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 5. Qualitative results of generalizing to unseen categories.
- **p. 12 / Figure/Table caption - extractive body cue:** Table 2. Quantitative results of reconstruction on the Synthetic [1]
- **p. 12 / Figure/Table caption - extractive body cue:** Table 3. Quantitative results of articulated motion synthesis on the Synthetic [1] dataset.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Reconstructed unseen articulated objects in Shape2Motion [55] (top) and synthetic [1] (bottom) dataset. | embodiment, simulator version and control stack | p. 7 (5.2. Baselines), p. 6 (5.1. Datasets) |
| Task/environment | The synthetic dataset contains procedurally generated articulated objects. | reset, timeout, object/scene variation | p. 6 (5.1. Datasets), p. 6 (5.1. Datasets) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3. Problem Formulation), p. 3 (3. Problem Formulation) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (4.2. Implicit Decoders), p. 4 (4.2. Implicit Decoders) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For the revolute joint, we also measure the axis position error (Pos Err) using the minimum distance between the predicted and ground truth rotation ... | definition/direction/unit from same section | p. 7 (5.3. Evaluation Metrics) |
| Suffering from a limited capacity, this baseline obtains sub-optimal performance on MobileCD and joint angle errors. | definition/direction/unit from same section | p. 8 (5.5. Ablation Studies) |
| For both types of joints, we measure the axis orientation error (Angle Err). | definition/direction/unit from same section | p. 7 (5.3. Evaluation Metrics) |
| Table 4. Quantitative results of joint type prediction accuracy on the Shape2Motion [55] dataset. articulated objects. | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| We also apply the loss function of ScrewNet to train the model. | definition/direction/unit from same section | p. 6 (5.2. Baselines) |
| The synthetic dataset contains procedurally generated articulated objects. | definition/direction/unit from same section | p. 6 (5.1. Datasets) |
| Share Feature baseline has the worst performance in Mobile CD. | definition/direction/unit from same section | p. 8 (5.5. Ablation Studies) |
| Figure 2. Model architecture of Ditto. The input consists of point cloud observations before and after interaction. After a PointNet++ [44] encoder, we fuse ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| On both datasets, Ditto gets significantly better results on all metrics compared with the baselines. | comparison identity and matched condition | p. 7 (5.4. Articulated Object Reconstruction) |
| This baseline has the same output as Ditto. | comparison identity and matched condition | p. 6 (5.2. Baselines) |
| In addition to the external baselines above, we also use the following ablated versions of our model to validate our design choices: Concat Fusion. | comparison identity and matched condition | p. 6 (5.2. Baselines) |
| Both the Correspondence [7] and Global Joint [18] baselines perform poorly on articulation estimation. | comparison identity and matched condition | p. 7 (5.4. Articulated Object Reconstruction) |
| Share Feature baseline has the worst performance in Mobile CD. | comparison identity and matched condition | p. 8 (5.5. Ablation Studies) |
| Finally, the Share Decoder baseline applies one decoder for both geometry and motion features. | comparison identity and matched condition | p. 8 (5.5. Ablation Studies) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Qualitative results and analysis of ablation study are in the appendix. | component/input/data sensitivity | p. 8 (5.5. Ablation Studies) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Given visual observations before and after interaction, our method jointly reconstructs the part-level geometry and articulation model of the object. | 1, Ditto achieves superior or at least on-par performance on all metrics. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5.5. Ablation Studies), p. 7 (5.4. Articulated Object Reconstruction), p. 7 (5.4. Articulated Object Reconstruction), p. 8 (5.5. Ablation Studies), p. 12 (Figure/Table caption), p. 6 (Dataset) |
| Primary metric/result | On both datasets, Ditto gets significantly better results on all metrics compared with the baselines. | numeric claim only at cited anchor | p. 7 (5.4. Articulated Object Reconstruction) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Failure of joint estimation also harms segmentation prediction because the joint parameter decoders and the segmentation decoder share the same feature planes. | p. 7 (5.4. Articulated Object Reconstruction) |
| body limitation/failure cue | 3, A-SDF fails to reconstruct the shape details of unseen objects, especially the objects with prismatic joints. | p. 8 (5.4. Articulated Object Reconstruction) |
| body limitation/failure cue | We observe that using the same 3D and 2D features for geometry and articulation makes training unstable, and 2D features would harm the reconstruction ... | p. 8 (5.5. Ablation Studies) |
| body limitation/failure cue | In comparison, Ditto does not suffer from such a bottleneck as an end-to-end method. | p. 7 (5.4. Articulated Object Reconstruction) |
| body limitation/failure cue | Even though we use multi-view depth images, the point cloud may still be incomplete due to the self-occlusion of the objects. | p. 6 (5.1. Datasets) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Then the displacement can be computed as lpin = Rpin(pin -qpin) + qpin. | p. 5 (4.3. Training) |
| The ground truth displacement ˆlpin can be computed similarly with the ground truth parameters. | p. 5 (4.3. Training) |
| To validate our choice of dense joint representation, we modify our model and use decoders that predict joint parameters from a global feature. | p. 6 (5.2. Baselines) |
| Besides, we use correspondence to compute the moving distance of every point and segment the mobile points with a threshold of 0.02 on this ... | p. 6 (5.2. Baselines) |
| This ablated version uses a shared decoder instead. | p. 7 (5.2. Baselines) |
| In our current model, we use two separate decoders in PointNet++ for geometry and articulation. | p. 7 (5.2. Baselines) |
| This decoder needs to reason about geometry and articulation simultaneously. | p. 8 (5.5. Ablation Studies) |
| Finally, the Share Decoder baseline applies one decoder for both geometry and motion features. | p. 8 (5.5. Ablation Studies) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 5.4. Articulated Object Reconstruction - extractive body cue:** Failure of joint estimation also harms segmentation prediction because the joint parameter decoders and the segmentation decoder share the same feature planes.
- **p. 8 / 5.4. Articulated Object Reconstruction - extractive body cue:** 3, A-SDF fails to reconstruct the shape details of unseen objects, especially the objects with prismatic joints.
- **p. 8 / 5.5. Ablation Studies - extractive body cue:** We observe that using the same 3D and 2D features for geometry and articulation makes training unstable, and 2D features would harm the reconstruction due ...
- **p. 7 / 5.4. Articulated Object Reconstruction - extractive body cue:** In comparison, Ditto does not suffer from such a bottleneck as an end-to-end method.
- **p. 6 / 5.1. Datasets - extractive body cue:** Even though we use multi-view depth images, the point cloud may still be incomplete due to the self-occlusion of the objects.

- **PDF anchors reviewed:** datasets p. 7 (5.2. Baselines), p. 6 (5.1. Datasets), p. 6 (5.1. Datasets), p. 8 (5.4. Articulated Object Reconstruction), p. 8 (5.6. Real-World Experiments), p. 7 (5.4. Articulated Object Reconstruction), metrics p. 7 (5.3. Evaluation Metrics), p. 8 (5.5. Ablation Studies), p. 7 (5.3. Evaluation Metrics), p. 12 (Figure/Table caption), p. 6 (5.2. Baselines), p. 6 (5.1. Datasets), baselines p. 7 (5.4. Articulated Object Reconstruction), p. 6 (5.2. Baselines), p. 6 (5.2. Baselines), p. 7 (5.4. Articulated Object Reconstruction), p. 8 (5.5. Ablation Studies), p. 8 (5.5. Ablation Studies), results p. 8 (5.5. Ablation Studies), p. 7 (5.4. Articulated Object Reconstruction), p. 7 (5.4. Articulated Object Reconstruction), p. 8 (5.5. Ablation Studies), p. 12 (Figure/Table caption), p. 6 (Dataset).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
