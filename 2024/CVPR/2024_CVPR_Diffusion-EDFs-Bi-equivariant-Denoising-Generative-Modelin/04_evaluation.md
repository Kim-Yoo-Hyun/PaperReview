# Evaluation - Diffusion-EDFs: Bi-equivariant Denoising Generative Modeling on SE(3) for Visual Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Ryu_Diffusion-EDFs_Bi-equivariant_Denoising_Generative_Modeling_on_SE3_for_Visual_Robotic_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Ryu_Diffusion-EDFs_Bi-equivariant_Denoising_Generative_Modeling_on_SE3_for_Visual_Robotic_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (5. Experiments and Results), p. 6 (5. Experiments and Results), p. 7 (5. Experiments and Results), p. 7 (5. Experiments and Results), p. 2 (Figure/Table caption)): Without object segmentation, R-NDFs achieve zero success rates due to the lack of locality in their method design [15, 37, 61].

## Evaluation Body Digest

- **p. 6 / 5. Experiments and Results - extractive body cue:** The mug-on-a-hanger task is similar to the one in the simulation benchmark.
- **p. 6 / 5. Experiments and Results - extractive body cue:** Diffusion-EDFs successfully learned to solve this task from only ten human demonstrations, demonstrating their ability to perform 1) accurate 6DoF manipulation tasks with 2) previously ...
- **p. 7 / 5. Experiments and Results - extractive body cue:** Real Hardware Experiment Pipeline 1) The scene point cloud is observed via 3D SLAM algorithm with the wrist-mounted RGB-D Camera.
- **p. 7 / 5. Experiments and Results - extractive body cue:** 3) The robot executes picking if the pose is reachable.
- **p. 5 / 4.1. Diffusion Origin Selection Mechanism - extractive body cue:** For most manipulation tasks, specific local sub-geometries are more significant than the global geometry of the target object in determining its pose.
- **p. 5 / 4.2. Architecture of Equivariant Descriptor Fields - extractive body cue:** For denoising, the receptive field of our model should cover the whole scene.
- **p. 6 / 5. Experiments and Results - extractive body cue:** While slightly better than R-NDFs, SE(3)- DiffusionFields also record low success rates, presumably due to the lack of SE(3)-equivariance.
- **p. 6 / 5. Experiments and Results - extractive body cue:** On the other hand, Diffusion-EDFs maintain total success rates around 80% even in the most adversarial scenarios due to the local equivariance [37, 61] inherited ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** 4. Implementation (p. 4); 5. Experiments and Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5. Experiments and Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Without object segmentation, R-NDFs achieve zero success rates due to the lack of locality in their method design [15, 37, 61]. | p. 6 (5. Experiments and Results) |
| 5. Experiments and Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | In particular, we measure the pick-andplace success rate for two different object categories: mugs and bottles (see Fig. | p. 6 (5. Experiments and Results) |
| 5. Experiments and Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Pick-and-place success rates in various out-of-distribution settings in simulated environment. | p. 7 (5. Experiments and Results) |
| 5. Experiments and Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Diffusion-EDFs successfully learned the task from four human demonstrations (consisting of three sequential pickand-place subtasks for each bottle), showcasing their robustness to stochastic and ... | p. 7 (5. Experiments and Results) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1. Overview of Diffusion-EDFs. (a) The target end-effector pose g0 is bi-equivariantly diffused for the training of Diffusion-EDFs. (b) The end-effector pose is ... | p. 2 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 5. Experiments and Results - extractive body cue:** The mug-on-a-hanger task is similar to the one in the simulation benchmark.
- **p. 6 / 5. Experiments and Results - extractive body cue:** Diffusion-EDFs successfully learned to solve this task from only ten human demonstrations, demonstrating their ability to perform 1) accurate 6DoF manipulation tasks with 2) previously ...
- **p. 7 / 5. Experiments and Results - extractive body cue:** Real Hardware Experiment Pipeline 1) The scene point cloud is observed via 3D SLAM algorithm with the wrist-mounted RGB-D Camera.
- **p. 7 / 5. Experiments and Results - extractive body cue:** 3) The robot executes picking if the pose is reachable.
- **p. 5 / 4.1. Diffusion Origin Selection Mechanism - extractive body cue:** For most manipulation tasks, specific local sub-geometries are more significant than the global geometry of the target object in determining its pose.
- **p. 5 / 4.2. Architecture of Equivariant Descriptor Fields - extractive body cue:** For denoising, the receptive field of our model should cover the whole scene.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. Overview of Diffusion-EDFs. (a) The target end-effector pose g0 is bi-equivariantly diffused for the training of Diffusion-EDFs. (b) The end-effector pose is sampled ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2. Architecture of multiscale EDF. Our multiscale EDF model is composed of a feature extracting part and a field model part. See Fig. 7 ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Simulation Experiments. (a) In the Mug-on-a-Hanger task, a red mug should be picked up by its rim and placed on a green hanger ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Pick-and-place success rates in various out-of-distribution settings in simulated environment.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Real Hardware Experiment Pipeline 1) The scene point cloud is observed via 3D SLAM algorithm with the wrist-mounted RGB-D Camera. 2) Diffusion-EDFs infer ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Real Hardware Experiments. (a) In the mug-on-a- hanger task, the white mug must be picked and placed on the white hanger. (b) In ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. Key challenges of each task SE(3)-Equivariant Graph Neural Networks. SO(3)- and SE(3)-equivariant graph neural networks (GNNs) [19, 22, 26, 45, 46, 62, 74] ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The mug-on-a-hanger task is similar to the one in the simulation benchmark. | embodiment, simulator version and control stack | p. 6 (5. Experiments and Results), p. 6 (5. Experiments and Results) |
| Task/environment | Diffusion-EDFs successfully learned to solve this task from only ten human demonstrations, demonstrating their ability to perform 1) accurate 6DoF manipulation tasks with 2) ... | reset, timeout, object/scene variation | p. 6 (5. Experiments and Results), p. 7 (5. Experiments and Results) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 2 (2.1. SO(3) Group Representation Theory), p. 3 (3.1. Problem Formulation) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 2 (2.1. SO(3) Group Representation Theory), p. 5 (4. Implementation) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| While slightly better than R-NDFs, SE(3)- DiffusionFields also record low success rates, presumably due to the lack of SE(3)-equivariance. | definition/direction/unit from same section | p. 6 (5. Experiments and Results) |
| On the other hand, Diffusion-EDFs maintain total success rates around 80% even in the most adversarial scenarios due to the local equivariance [37, 61] ... | definition/direction/unit from same section | p. 6 (5. Experiments and Results) |
| Pick-and-place success rates in various out-of-distribution settings in simulated environment. | definition/direction/unit from same section | p. 7 (5. Experiments and Results) |
| Figure 1. Overview of Diffusion-EDFs. (a) The target end-effector pose g0 is bi-equivariantly diffused for the training of Diffusion-EDFs. (b) The end-effector pose is ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Diffusion-EDFs successfully learned the task from four human demonstrations (consisting of three sequential pickand-place subtasks for each bottle), showcasing their robustness to stochastic and ... | definition/direction/unit from same section | p. 7 (5. Experiments and Results) |
| For faster sampling, we separate our implementation of EDFs into the feature extractor and the field model (see Fig. | definition/direction/unit from same section | p. 5 (4.2. Architecture of Equivariant Descriptor Fields) |
| We find that this strategy enables our models to pay more attention to such contact-rich and relevant sub-geometries without explicit supervision. | definition/direction/unit from same section | p. 5 (4.1. Diffusion Origin Selection Mechanism) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 1, Diffusion-EDFs consistently outperform both the SE(3)-equivariant baseline (R-NDFs [68]) and diffusion model baseline (SE(3)-DiffusionFields [75]) in almost all scenarios, despite not being provided ... | comparison identity and matched condition | p. 6 (5. Experiments and Results) |
| In particular, the baseline models completely fail with unsegmented observations. | comparison identity and matched condition | p. 6 (5. Experiments and Results) |
| Scenario Method Without Pretraining Without Obj. | comparison identity and matched condition | p. 7 (5. Experiments and Results) |
| We find that this strategy enables our models to pay more attention to such contact-rich and relevant sub-geometries without explicit supervision. | comparison identity and matched condition | p. 5 (4.1. Diffusion Origin Selection Mechanism) |
| We address this issue with our U-Net-like multiscale architecture, which maintains a wide receptive field without losing local high-frequency details. | comparison identity and matched condition | p. 5 (4.2. Architecture of Equivariant Descriptor Fields) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Scenario Method Without Pretraining Without Obj. | component/input/data sensitivity | p. 7 (5. Experiments and Results) |
| Figure 1. Overview of Diffusion-EDFs. (a) The target end-effector pose g0 is bi-equivariantly diffused for the training of Diffusion-EDFs. (b) The end-effector pose is ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| We train Diffusion-EDFs in a fully end-to-end manner without using any pre-training or object segmentation. | component/input/data sensitivity | p. 6 (5. Experiments and Results) |
| In contrast, we evaluate R-NDFs and SE(3)- Diffusion Fields for both with and without object segmentation pipelines. | component/input/data sensitivity | p. 6 (5. Experiments and Results) |
| In this section, we first provide the specific implementation of the bi-equivariant diffusion frame selection mechanism, which was postponed in Sec. | component/input/data sensitivity | p. 4 (4. Implementation) |
| Several works have addressed the importance of incorporating such locality in equivariant methods [9, 15, 20, 37, 61]. | component/input/data sensitivity | p. 5 (4.1. Diffusion Origin Selection Mechanism) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| This enables our method to be trained end-to-end from only 5∼10 human demonstrations without requiring any pre-training and object segmentation, yet are highly generalizable ... | Without object segmentation, R-NDFs achieve zero success rates due to the lack of locality in their method design [15, 37, 61]. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (5. Experiments and Results), p. 6 (5. Experiments and Results), p. 7 (5. Experiments and Results), p. 7 (5. Experiments and Results), p. 2 (Figure/Table caption) |
| Primary metric/result | In particular, we measure the pick-andplace success rate for two different object categories: mugs and bottles (see Fig. | numeric claim only at cited anchor | p. 6 (5. Experiments and Results) |

- Numeric sentences retained from the body:
- **p. 5 / 4.3. Score Model - extractive body cue:** [61] for ρ(x/O) ρ(x/Oe) = X q∈Q(Oe) w(x/Oe)δ(3)(x -q) (31) where Q(·) : Oe 7→{qn}Nq n=1 is the query points function which outputs the set ...
- **p. 6 / 5. Experiments and Results - extractive body cue:** It took 20∼45 minutes to train Diffusion-EDFs for single pick or place task with RTX 3090 GPU and i9-12900k CPU.
- **p. 5 / 4.3. Score Model - extractive body cue:** [61] for ρ(x/O) ρ(x/Oe) = X q∈Q(Oe) w(x/Oe)δ(3)(x -q) (31) where Q(·) : Oe 7→{qn}Nq n=1 is the query points function which outputs the set ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | One limitation of Diffusion-EDFs is the inability of control-level or trajectory-level inference. | p. 8 (7. Conclusion) |
| body limitation/failure cue | The other limitation is the necessity of the grasp observation procedure, which prevents its application to closed-loop inference. | p. 8 (7. Conclusion) |
| body limitation/failure cue | In this task, even a minor error of a centimeter can result in complete failure due to noisy observation and the small size of ... | p. 6 (5. Experiments and Results) |
| body limitation/failure cue | E.2 for more details. on object segmentation are also unable to solve this task, as they cannot differentiate between bottles that are already placed ... | p. 7 (5. Experiments and Results) |
| body limitation/failure cue | In particular, the baseline models completely fail with unsegmented observations. | p. 6 (5. Experiments and Results) |
| body limitation/failure cue | Pick-and-place success rates in various out-of-distribution settings in simulated environment. | p. 7 (5. Experiments and Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| It takes the encoded feature points from the feature extractor as input and computes the field value at a given query point. | p. 5 (4.2. Architecture of Equivariant Descriptor Fields) |
| The feature extractor is a deep SE(3)-equivariant GNN encoder that is run only once at the beginning of the denoising process. | p. 5 (4.2. Architecture of Equivariant Descriptor Fields) |
| It took 20∼45 minutes to train Diffusion-EDFs for single pick or place task with RTX 3090 GPU and i9-12900k CPU. | p. 6 (5. Experiments and Results) |
| In this section, we first provide the specific implementation of the bi-equivariant diffusion frame selection mechanism, which was postponed in Sec. | p. 4 (4. Implementation) |
| For the implementation of the query weight field w(x/O), we use an EDF with a single scalar (type-0) output. | p. 6 (4.3. Score Model) |
| Real Hardware Experiment Pipeline 1) The scene point cloud is observed via 3D SLAM algorithm with the wrist-mounted RGB-D Camera. | p. 7 (5. Experiments and Results) |
| In these models, we compute the translational and rotational score using two different types of equivariant fields: 1) the equivariant density field ρ□;t(·/Oe) : ... | p. 4 (3.5. Bi-equivariant Score Model) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 7. Conclusion - extractive body cue:** One limitation of Diffusion-EDFs is the inability of control-level or trajectory-level inference.
- **p. 8 / 7. Conclusion - extractive body cue:** The other limitation is the necessity of the grasp observation procedure, which prevents its application to closed-loop inference.
- **p. 6 / 5. Experiments and Results - extractive body cue:** In this task, even a minor error of a centimeter can result in complete failure due to noisy observation and the small size of mug ...
- **p. 7 / 5. Experiments and Results - extractive body cue:** E.2 for more details. on object segmentation are also unable to solve this task, as they cannot differentiate between bottles that are already placed on ...
- **p. 6 / 5. Experiments and Results - extractive body cue:** In particular, the baseline models completely fail with unsegmented observations.
- **p. 7 / 5. Experiments and Results - extractive body cue:** Pick-and-place success rates in various out-of-distribution settings in simulated environment.

- **PDF anchors reviewed:** datasets p. 6 (5. Experiments and Results), p. 6 (5. Experiments and Results), p. 7 (5. Experiments and Results), p. 7 (5. Experiments and Results), p. 5 (4.1. Diffusion Origin Selection Mechanism), p. 5 (4.2. Architecture of Equivariant Descriptor Fields), metrics p. 6 (5. Experiments and Results), p. 6 (5. Experiments and Results), p. 7 (5. Experiments and Results), p. 2 (Figure/Table caption), p. 7 (5. Experiments and Results), p. 5 (4.2. Architecture of Equivariant Descriptor Fields), baselines p. 6 (5. Experiments and Results), p. 6 (5. Experiments and Results), p. 7 (5. Experiments and Results), p. 5 (4.1. Diffusion Origin Selection Mechanism), p. 5 (4.2. Architecture of Equivariant Descriptor Fields), results p. 6 (5. Experiments and Results), p. 6 (5. Experiments and Results), p. 7 (5. Experiments and Results), p. 7 (5. Experiments and Results), p. 2 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
