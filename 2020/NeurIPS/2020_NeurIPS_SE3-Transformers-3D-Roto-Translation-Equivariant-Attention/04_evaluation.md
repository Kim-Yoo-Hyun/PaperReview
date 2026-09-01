# Evaluation - SE(3)-Transformers: 3D Roto-Translation Equivariant Attention Networks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2006.10503; PDF retrieval source: https://arxiv.org/pdf/2006.10503. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 Experiments), p. 7 (4 Experiments), p. 22 (Figure/Table caption), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 7 (4 Experiments)): If both training and test set are not rotated (x = 0 in a), breaking the symmetry of the SE(3)-Transformer by providing the z-component of the coordinates as an additional, ...

## Evaluation Body Digest

- **p. 8 / 4 Experiments - extractive PDF cue:** To test our method, we choose ScanObjectNN, a recently introduced dataset for real-world object classification.
- **p. 7 / 4 Experiments - extractive PDF cue:** Next, we evaluate on a real-world object classification task.
- **p. 8 / 4 Experiments - extractive PDF cue:** Points 128 1024 128 1024 1024 1024 1024 128 1024 128 1024 1024 1024 Accuracy 63.1% 71.4% 72.8 % 73.8% 74.1% 79.2% 79.5% 81.0% 84.3% ...
- **p. 7 / 4 Experiments - extractive PDF cue:** [27], the error is not squared: ∆EQ = ∥LsΦ(f) -ΦLs(f)∥2 / ∥LsΦ(f)∥2 (14) 4.1 N-Body Simulations In this experiment, we use an adaptation of the ...
- **p. 9 / 4 Experiments - extractive PDF cue:** TASK α ∆ε εHOMO εLUMO µ Cν UNITS bohr3 meV meV meV D cal/mol K WaveScatt [11] .160 118 85 76 .340 .049 NMP [10] ...
- **p. 9 / 4 Experiments - extractive PDF cue:** We show results on the test set of Anderson et al.
- **p. 7 / 4 Experiments - extractive PDF cue:** The distance between the two, averaged over samples, yields the equivariance error.
- **p. 7 / 4 Experiments - extractive PDF cue:** The equivariance error shows that our approach is indeed fully rotation equivariant up to the precision of the computations. input label Set Transf. original rotated ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | If both training and test set are not rotated (x = 0 in a), breaking the symmetry of the SE(3)-Transformer by providing the z-component ... | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our model outperforms both an attention-based, but not rotation-equivariant approach (Set Transformer) and a equivariant approach which does not levarage attention (Tensor Field). | p. 7 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 7: Attention block for the QM9 dataset. Each component is listed with a tuple of numbers representing the output feature types and multiplicities, ... | p. 22 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | This results in a performance loss when deploying a fully SO(3) invariant model (see Fig. | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | We see that while not state-of-the-art, we offer competitive performance, especially against Cormorant and TFN, which transform under irreducible representations of SE(3) (like us), ... | p. 9 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 8 / 4 Experiments - extractive PDF cue:** To test our method, we choose ScanObjectNN, a recently introduced dataset for real-world object classification.
- **p. 7 / 4 Experiments - extractive PDF cue:** Next, we evaluate on a real-world object classification task.
- **p. 8 / 4 Experiments - extractive PDF cue:** Points 128 1024 128 1024 1024 1024 1024 128 1024 128 1024 1024 1024 Accuracy 63.1% 71.4% 72.8 % 73.8% 74.1% 79.2% 79.5% 81.0% 84.3% ...
- **p. 7 / 4 Experiments - extractive PDF cue:** [27], the error is not squared: ∆EQ = ∥LsΦ(f) -ΦLs(f)∥2 / ∥LsΦ(f)∥2 (14) 4.1 N-Body Simulations In this experiment, we use an adaptation of the ...
- **p. 9 / 4 Experiments - extractive PDF cue:** TASK α ∆ε εHOMO εLUMO µ Cν UNITS bohr3 meV meV meV D cal/mol K WaveScatt [11] .160 118 85 76 .340 .049 NMP [10] ...
- **p. 9 / 4 Experiments - extractive PDF cue:** We show results on the test set of Anderson et al.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: A) Each layer of the SE(3)-Transformer maps from a point cloud to a point cloud (or graph to graph) while guaranteeing equivariance. For ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 2: Updating the node features using our equivariant attention mechanism in four steps. A more detailed description, especially of step 2, is provided in ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: Predicting future locations and velocities in an electron-proton simulation. Linear DeepSet [46] Tensor Field [28] Set Transformer [16] SE(3)-Transformer MSE x 0.0691
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3: A model based on conventional self-attention (left) and our rotation-equivariant version (right) predict future locations and velocities in a 5-body problem. The respective ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: ScanObjectNN: x-axis shows data augmentation on the test set. The x-value corresponds to the maximum rotation around a random axis in the x-y-plane. ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Classification accuracy on the 'object only' category of the ScanObjectNN dataset4. The performance of the SE(3)-Transformer is averaged over 5 runs (standard deviation ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 3: QM9 Mean Absolute Error. Top: Non-equivariant models. Bottom: Equivariant models. SE(3)-Tr. is averaged over 5 runs. TASK α ∆ε εHOMO εLUMO µ
- **p. 17 / Figure/Table caption - extractive PDF cue:** Figure 5: Spherical harmonics computation of our own implementation compared to the lie-learn library. We found that speeding up the computation of spherical harmonics is ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To test our method, we choose ScanObjectNN, a recently introduced dataset for real-world object classification. | embodiment, simulator version and control stack | p. 8 (4 Experiments), p. 7 (4 Experiments) |
| Task/environment | Next, we evaluate on a real-world object classification task. | reset, timeout, object/scene variation | p. 7 (4 Experiments), p. 8 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (1 Introduction), p. 6 (3 Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 6 (3 Method), p. 5 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The distance between the two, averaged over samples, yields the equivariance error. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| The equivariance error shows that our approach is indeed fully rotation equivariant up to the precision of the computations. input label Set Transf. original ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Table 2: Classification accuracy on the 'object only' category of the ScanObjectNN dataset4. The performance of the SE(3)-Transformer is averaged over 5 runs (standard ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| 0 30 60 90 120 150 180 maximum rotation 0.2 0.3 0.4 0.5 0.6 0.7 0.8 accuracy SE(3)-Transformer +z SE(3)-Transformer Tensor Field SetTransformer DeepSet ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| 4.3 QM9 Table 3: QM9 Mean Absolute Error. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| We see that while not state-of-the-art, we offer competitive performance, especially against Cormorant and TFN, which transform under irreducible representations of SE(3) (like us), ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Figure 1: A) Each layer of the SE(3)-Transformer maps from a point cloud to a point cloud (or graph to graph) while guaranteeing equivariance. ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 5: Spherical harmonics computation of our own implementation compared to the lie-learn library. We found that speeding up the computation of spherical harmonics ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compare to publicly available, state-of-the-art results as well as a set of our own baselines. | comparison identity and matched condition | p. 7 (4 Experiments) |
| Our model outperforms both an attention-based, but not rotation-equivariant approach (Set Transformer) and a equivariant approach which does not levarage attention (Tensor Field). | comparison identity and matched condition | p. 7 (4 Experiments) |
| In Table 2, we compare our model to the current state-of-the-art in object classification4. | comparison identity and matched condition | p. 8 (4 Experiments) |
| We see that while not state-of-the-art, we offer competitive performance, especially against Cormorant and TFN, which transform under irreducible representations of SE(3) (like us), ... | comparison identity and matched condition | p. 9 (4 Experiments) |
| Figure 5: Spherical harmonics computation of our own implementation compared to the lie-learn library. We found that speeding up the computation of spherical harmonics ... | comparison identity and matched condition | p. 17 (Figure/Table caption) |
| Interestingly, the vast majority of current neural network methods work on scalar coordinates without incorporating vector specific inductive biases. | comparison identity and matched condition | p. 8 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Our method sets itself apart by using roto-translation equivariant layers acting directly on the point cloud without prior projection onto a sphere [22, 45, ... | component/input/data sensitivity | p. 8 (4 Experiments) |
| We create an SO(2) invariant version of our algorithm by additionally feeding the z-component as an type-0 field and the x, y position as ... | component/input/data sensitivity | p. 8 (4 Experiments) |
| Figure 1: A) Each layer of the SE(3)-Transformer maps from a point cloud to a point cloud (or graph to graph) while guaranteeing equivariance. ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| The dashed curves show the predicted locations of a perfectly equivariant model. | component/input/data sensitivity | p. 7 (4 Experiments) |
| The N-body problem is an equivariant task: rotation of the input should result in rotated predictions of locations and velocities of the particles. | component/input/data sensitivity | p. 7 (4 Experiments) |
| The table is split into non-equivariant (top) and equivariant models (bottom). | component/input/data sensitivity | p. 9 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we propose the SE(3)-Transformer shown in Fig. | If both training and test set are not rotated (x = 0 in a), breaking the symmetry of the SE(3)-Transformer by providing the z-component ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 Experiments), p. 7 (4 Experiments), p. 22 (Figure/Table caption), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 7 (4 Experiments) |
| Primary metric/result | Our model outperforms both an attention-based, but not rotation-equivariant approach (Set Transformer) and a equivariant approach which does not levarage attention (Tensor Field). | numeric claim only at cited anchor | p. 7 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Experiments - extractive PDF cue:** The right-hand plots show predicted locations and velocities for rotations of the input in steps of 10 degrees.
- **p. 8 / 4 Experiments - extractive PDF cue:** The benchmark provides point clouds of 2902 objects across 15 different categories.
- **p. 9 / 4 Experiments - extractive PDF cue:** TASK α ∆ε εHOMO εLUMO µ Cν UNITS bohr3 meV meV meV D cal/mol K WaveScatt [11] .160 118 85 76 .340 .049 NMP [10] ...
- **p. 5 / 3 Method - extractive PDF cue:** Attention is performed on a per-neighbourhood basis as follows: fℓ out,i = Wℓℓ V fℓ in,i / {z } 3 ⃝self-interaction + X k≥0 X ...
- **p. 6 / 3 Method - extractive PDF cue:** at node i and a set of key vectors {kij}j∈Ni along each edge ij in the neighbourhood Ni where αij = exp(q⊤ i kij) P ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This architecture is guaranteed to be robust to rotations and translations of the input, obviating the need for training time data augmentation and ensuring ... | p. 9 (5 Conclusion) |
| body limitation/failure cue | On the other hand, compared to convential attention, adding the equivariance constraints also increases performance in all of our experiments while at the same ... | p. 9 (5 Conclusion) |
| body limitation/failure cue | Our model outperforms both an attention-based, but not rotation-equivariant approach (Set Transformer) and a equivariant approach which does not levarage attention (Tensor Field). | p. 7 (4 Experiments) |
| body limitation/failure cue | Specifically, we compare to the Set-Transformer [16], a non-equivariant attention model, and Tensor Field Networks [28], which is similar to SE(3)-Transformer but does not ... | p. 7 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The task of the algorithm is then to predict the relative location and velocity 500 time steps into the future. | p. 7 (4 Experiments) |
| The right-hand plots show predicted locations and velocities for rotations of the input in steps of 10 degrees. | p. 7 (4 Experiments) |
| Our nearest models are Cormorant and TFN (own implementation). | p. 9 (4 Experiments) |
| The layer can be broken down into a procedure of steps as shown in Fig. | p. 5 (3 Method) |
| These neighbourhoods are computed either via the nearest-neighbours methods or may already be defined. | p. 5 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 5 Conclusion - extractive PDF cue:** This architecture is guaranteed to be robust to rotations and translations of the input, obviating the need for training time data augmentation and ensuring stability ...
- **p. 9 / 5 Conclusion - extractive PDF cue:** On the other hand, compared to convential attention, adding the equivariance constraints also increases performance in all of our experiments while at the same time ...
- **p. 7 / 4 Experiments - extractive PDF cue:** Our model outperforms both an attention-based, but not rotation-equivariant approach (Set Transformer) and a equivariant approach which does not levarage attention (Tensor Field).
- **p. 7 / 4 Experiments - extractive PDF cue:** Specifically, we compare to the Set-Transformer [16], a non-equivariant attention model, and Tensor Field Networks [28], which is similar to SE(3)-Transformer but does not leverage ...

- **PDF anchors reviewed:** datasets p. 8 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), metrics p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (Figure/Table caption), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), baselines p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 17 (Figure/Table caption), p. 8 (4 Experiments), results p. 8 (4 Experiments), p. 7 (4 Experiments), p. 22 (Figure/Table caption), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 7 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
