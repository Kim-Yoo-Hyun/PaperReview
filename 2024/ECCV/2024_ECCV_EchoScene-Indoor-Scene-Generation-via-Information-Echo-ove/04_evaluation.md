# Evaluation - EchoScene: Indoor Scene Generation via Information Echo over Scene Graph Diffusion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3146_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03146.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 12 (Figure/Table caption), p. 10 (5 Experiments), p. 11 (Figure/Table caption)): Fig. 4: Comparisons with other generative methods. Input scene graphs have more edges between two nodes than the ones visualized here. Red rectangles highlight the inconsistent generation. (Zoom for details) ...

## Evaluation Body Digest

- **p. 10 / 5 Experiments - extractive PDF cue:** We conduct our experiments on SG-FRONT dataset [58], which provides scene-graph annotations for the high-quality 3D-FRONT [16] with household environments.
- **p. 10 / 5 Experiments - extractive PDF cue:** SG-FRONT contains 15 relationship types and 45K object instances from three types of scenes.
- **p. 10 / 5 Experiments - extractive PDF cue:** To measure the scene graph consistency, we follow the scene graph constraints [15], which measure the accuracy of a set of relations on a generated ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Table 1: Scene generation realism as measured by FID, FIDCLIP and KID (⇥0.001) scores at 2562 pixels between the top-down rendering of generated and real ...
- **p. 10 / 5 Experiments - extractive PDF cue:** We follow the metrics used in [32, 57, 58], to measure the fidelity and diversity of generated scenes, where we adopt Fréchet Inception Distance (FID) ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Fig. 3: One Step of Dual-Branch Information Echo. For each time step, we encourage the layout (left) and shape (right) branches to exchange information within ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: EchoScene Schematic. EchoScene uses a dual-branch diffusion model to generate 3D scenes from scene graphs. In both branches, each node is allocated a ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 2: Overview of EchoScene. Our pipeline consists of graph preprocessing and two collaborative branches Layout Branch and Shape Branch. The details of two branches ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 5 Experiments (p. 10).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 4: Comparisons with other generative methods. Input scene graphs have more edges between two nodes than the ones visualized here. Red rectangles highlight ... | p. 12 (Figure/Table caption) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | To measure the scene graph consistency, we follow the scene graph constraints [15], which measure the accuracy of a set of relations on a ... | p. 10 (5 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 1: Scene generation realism as measured by FID, FIDCLIP and KID (⇥0.001) scores at 2562 pixels between the top-down rendering of generated and ... | p. 11 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 10 / 5 Experiments - extractive PDF cue:** We conduct our experiments on SG-FRONT dataset [58], which provides scene-graph annotations for the high-quality 3D-FRONT [16] with household environments.
- **p. 10 / 5 Experiments - extractive PDF cue:** SG-FRONT contains 15 relationship types and 45K object instances from three types of scenes.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: EchoScene Schematic. EchoScene uses a dual-branch diffusion model to generate 3D scenes from scene graphs. In both branches, each node is allocated a ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 2: Overview of EchoScene. Our pipeline consists of graph preprocessing and two collaborative branches Layout Branch and Shape Branch. The details of two branches ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Fig. 3: One Step of Dual-Branch Information Echo. For each time step, we encourage the layout (left) and shape (right) branches to exchange information within ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Table 1: Scene generation realism as measured by FID, FIDCLIP and KID (⇥0.001) scores at 2562 pixels between the top-down rendering of generated and real ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Fig. 4: Comparisons with other generative methods. Input scene graphs have more edges between two nodes than the ones visualized here. Red rectangles highlight the ...
- **p. 13 / Figure/Table caption - extractive PDF cue:** Table 2: Scene graph constraints (higher is better). Top: Relationship change mode. Middle: Node addition mode. Bottom: No manipulation (i.e., generation only). The decrease in ...
- **p. 14 / Figure/Table caption - extractive PDF cue:** Fig. 5: Off-the-shelf texture creation. A bedroom (top) and living room (bottom) generated by EchoScene and textured in different styles by SceneTex [9].
- **p. 14 / Figure/Table caption - extractive PDF cue:** Table 3: Inter-object Consistency. The consistent object shapes within a scene are indicated by low CD values (⇥0.001). Ablation FID FIDCLIP KID mSG Ours w/o ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We conduct our experiments on SG-FRONT dataset [58], which provides scene-graph annotations for the high-quality 3D-FRONT [16] with household environments. | embodiment, simulator version and control stack | p. 10 (5 Experiments), p. 10 (5 Experiments) |
| Task/environment | SG-FRONT contains 15 relationship types and 45K object instances from three types of scenes. | reset, timeout, object/scene variation | p. 10 (5 Experiments) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 8 (4 Method), p. 2 (1 Introduction) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 2 (1 Introduction), p. 6 (4 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| To measure the scene graph consistency, we follow the scene graph constraints [15], which measure the accuracy of a set of relations on a ... | definition/direction/unit from same section | p. 10 (5 Experiments) |
| Table 1: Scene generation realism as measured by FID, FIDCLIP and KID (⇥0.001) scores at 2562 pixels between the top-down rendering of generated and ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |
| We follow the metrics used in [32, 57, 58], to measure the fidelity and diversity of generated scenes, where we adopt Fréchet Inception Distance ... | definition/direction/unit from same section | p. 10 (5 Experiments) |
| Fig. 3: One Step of Dual-Branch Information Echo. For each time step, we encourage the layout (left) and shape (right) branches to exchange information ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Fig. 1: EchoScene Schematic. EchoScene uses a dual-branch diffusion model to generate 3D scenes from scene graphs. In both branches, each node is allocated ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Fig. 2: Overview of EchoScene. Our pipeline consists of graph preprocessing and two collaborative branches Layout Branch and Shape Branch. The details of two ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Fig. 4: Comparisons with other generative methods. Input scene graphs have more edges between two nodes than the ones visualized here. Red rectangles highlight ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| Table 2: Scene graph constraints (higher is better). Top: Relationship change mode. Middle: Node addition mode. Bottom: No manipulation (i.e., generation only). The decrease ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 2: Scene graph constraints (higher is better). Top: Relationship change mode. Middle: Node addition mode. Bottom: No manipulation (i.e., generation only). The decrease ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |
| Table 4: Ablations under three cir- cumstances. mSG means average graph constraints. observe a marginal decrease, indicating even without ⇡(t), the model still learns ... | comparison identity and matched condition | p. 14 (Figure/Table caption) |
| Fig. 4: Comparisons with other generative methods. Input scene graphs have more edges between two nodes than the ones visualized here. Red rectangles highlight ... | comparison identity and matched condition | p. 12 (Figure/Table caption) |
| Table 3: Inter-object Consistency. The consistent object shapes within a scene are indicated by low CD values (⇥0.001). Ablation FID FIDCLIP KID mSG Ours ... | comparison identity and matched condition | p. 14 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 4: Ablations under three cir- cumstances. mSG means average graph constraints. observe a marginal decrease, indicating even without ⇡(t), the model still learns ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| Table 3: Inter-object Consistency. The consistent object shapes within a scene are indicated by low CD values (⇥0.001). Ablation FID FIDCLIP KID mSG Ours ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce an information echo scheme inside each branch of EchoScene that allows multiple denoising processes to exchange their denoising status among each other ... | Fig. 4: Comparisons with other generative methods. Input scene graphs have more edges between two nodes than the ones visualized here. Red rectangles highlight ... | PDF body cue; verify exact table/figure and matched conditions | p. 12 (Figure/Table caption), p. 10 (5 Experiments), p. 11 (Figure/Table caption) |
| Primary metric/result | To measure the scene graph consistency, we follow the scene graph constraints [15], which measure the accuracy of a set of relations on a ... | numeric claim only at cited anchor | p. 10 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Method - extractive PDF cue:** EchoScene 7 B.2 Shape Branch Denoiser εθ Shape Encoder S Xt Xt-1 S' X0 XT ··· ··· ··· ··· Shape Decoder Noise A.2 Latent Contextual ...
- **p. 8 / 4 Method - extractive PDF cue:** Initially, each bounding box bi 0 has 7 parameters, e.g., location (x, y, z), size (l, h, w), and a yaw angle ✓.
- **p. 8 / 4 Method - extractive PDF cue:** Thereby, the final representation contains 8 parameters: bi 0 = {x, y, z, l, h, w, sin ✓, cos ✓}, as shown in Fig.
- **p. 9 / 4 Method - extractive PDF cue:** Shape Branch A.3 Parameter Diffusion B.3 Dimension Alignment Denoiser γθ Denoiser γθ Denoiser εθ Denoiser εθ Fig.
- **p. 11 / 11 Method - extractive PDF cue:** 5.1 Scene Fidelity As a generation task, the fidelity of scene synthesis is essential to measure.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 2: Overview of EchoScene. Our pipeline consists of graph preprocessing and two collaborative branches Layout Branch and Shape Branch. The details of two ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Fig. 3: One Step of Dual-Branch Information Echo. For each time step, we encourage the layout (left) and shape (right) branches to exchange information ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | Table 4: Ablations under three cir- cumstances. mSG means average graph constraints. observe a marginal decrease, indicating even without ⇡(t), the model still learns ... | p. 14 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Training is optimized with AdamW with an initial learning rate of 1e-4. | p. 10 (5 Experiments) |
| The training, evaluation, and visualization are carried out on a single NVIDIA A40 GPU with 40 GB of memory. | p. 10 (5 Experiments) |
| EchoScene evolves the contextual graph to the latent space utilizing an encoder and a manipulator based on triplet-GCN, as shown in Fig. | p. 5 (4 Method) |
| To make the layout and shape branches aware of the semantic and spatial information among the objects, we first encode the contextual graph to ... | p. 6 (4 Method) |
| In analogy to an echo in the real world, a node can send its information and receive it back along with information from other ... | p. 7 (4 Method) |
| As each generation proceeds individually, there is no awareness of scene content during the denoising steps, which makes the generation inconsistent with global constraints ... | p. 7 (4 Method) |
| 3.A.1, in the implementation, we substitute denoising data di t to the diffused bounding box bi t, resulting in VDt 7! | p. 8 (4 Method) |
| We follow a normal DDPM training routine, in which we set 1000 time steps for all diffusion processes with weight-shared γ✓. | p. 8 (4 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 2: Overview of EchoScene. Our pipeline consists of graph preprocessing and two collaborative branches Layout Branch and Shape Branch. The details of two branches ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Fig. 3: One Step of Dual-Branch Information Echo. For each time step, we encourage the layout (left) and shape (right) branches to exchange information within ...
- **p. 14 / Figure/Table caption - extractive PDF cue:** Table 4: Ablations under three cir- cumstances. mSG means average graph constraints. observe a marginal decrease, indicating even without ⇡(t), the model still learns temporal ...

- **PDF anchors reviewed:** datasets p. 10 (5 Experiments), p. 10 (5 Experiments), metrics p. 10 (5 Experiments), p. 11 (Figure/Table caption), p. 10 (5 Experiments), p. 9 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (Figure/Table caption), baselines p. 13 (Figure/Table caption), p. 14 (Figure/Table caption), p. 12 (Figure/Table caption), p. 14 (Figure/Table caption), results p. 12 (Figure/Table caption), p. 10 (5 Experiments), p. 11 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
