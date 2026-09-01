# Evaluation - Learning 3D Object Spatial Relationships from Pre-trained 2D Diffusion Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Baik_Learning_3D_Object_Spatial_Relationships_from_Pre-trained_2D_Diffusion_Models_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Baik_Learning_3D_Object_Spatial_Relationships_from_Pre-trained_2D_Diffusion_Models_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4. Experiments), p. 7 (4.1. Pairwise OOR Generation), p. 6 (4.1. Pairwise OOR Generation), p. 7 (4.2. Multi-object OOR Generation), p. 8 (4.3. Applications of OOR), p. 5 (Figure/Table caption)): 4.2 demonstrates our advanced sampling approach produces significantly better results compared to text-to-3D models.

## Evaluation Body Digest

- **p. 7 / 4.2. Multi-object OOR Generation - extractive PDF cue:** We evaluate 20 scenes where 3 to 5 objects have spatial relations with each other.
- **p. 7 / 4.3. Applications of OOR - extractive PDF cue:** We demonstrate the efficacy of our proposed scene arrangement methods using ParaHome DB [27], which provides 3D scenes with separate object meshes.
- **p. 6 / 4.1. Pairwise OOR Generation - extractive PDF cue:** We evaluate our method and the baselines on a total of 150 scenes derived from 30 category pairs with 5 scenes generated per prompt.
- **p. 6 / 4.1. Pairwise OOR Generation - extractive PDF cue:** Thus, we compare ours with LLM-based methods that pursue similar goals: SceneMotifCoder (SMC) [58], which focuses on 3D object alignments, and SceneTeller [39], which deals ...
- **p. 8 / 4.3. Applications of OOR - extractive PDF cue:** First, we begin with the initial scene with two objects and the human interacting with them.
- **p. 8 / 4.3. Applications of OOR - extractive PDF cue:** Human Motion Synthesis for Two-Object Interaction.
- **p. 7 / 4.2. Multi-object OOR Generation - extractive PDF cue:** 2 further demonstrates the superiority of our method, especially in the case of VLM score and user study.
- **p. 7 / 4.2. Multi-object OOR Generation - extractive PDF cue:** However, for per-image scores such as CLIP score and VQA score, we apply them only to the ControlNet-generated images.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4. Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 4.2 demonstrates our advanced sampling approach produces significantly better results compared to text-to-3D models. | p. 6 (4. Experiments) |
| 4.1. Pairwise OOR Generation | EMPIRICAL / SOURCE-REPORTED EVALUATION | 1 shows that our method outperforms baselines for all metrics. | p. 7 (4.1. Pairwise OOR Generation) |
| 4.1. Pairwise OOR Generation | EMPIRICAL / SOURCE-REPORTED EVALUATION | The CLIP score [45] measures textimage alignment by averaging CLIP model logits. | p. 6 (4.1. Pairwise OOR Generation) |
| 4.2. Multi-object OOR Generation | EMPIRICAL / SOURCE-REPORTED EVALUATION | 2 further demonstrates the superiority of our method, especially in the case of VLM score and user study. | p. 7 (4.2. Multi-object OOR Generation) |
| 4.3. Applications of OOR | EMPIRICAL / SOURCE-REPORTED EVALUATION | Results of editing the original ParaHome scene, which includes a table, chair, teacup, and teapot, using our OOR diffusion. | p. 8 (4.3. Applications of OOR) |

## Dataset / Benchmark Role

- **p. 7 / 4.2. Multi-object OOR Generation - extractive PDF cue:** We evaluate 20 scenes where 3 to 5 objects have spatial relations with each other.
- **p. 7 / 4.3. Applications of OOR - extractive PDF cue:** We demonstrate the efficacy of our proposed scene arrangement methods using ParaHome DB [27], which provides 3D scenes with separate object meshes.
- **p. 6 / 4.1. Pairwise OOR Generation - extractive PDF cue:** We evaluate our method and the baselines on a total of 150 scenes derived from 30 category pairs with 5 scenes generated per prompt.
- **p. 6 / 4.1. Pairwise OOR Generation - extractive PDF cue:** Thus, we compare ours with LLM-based methods that pursue similar goals: SceneMotifCoder (SMC) [58], which focuses on 3D object alignments, and SceneTeller [39], which deals ...
- **p. 8 / 4.3. Applications of OOR - extractive PDF cue:** First, we begin with the initial scene with two objects and the human interacting with them.
- **p. 8 / 4.3. Applications of OOR - extractive PDF cue:** Human Motion Synthesis for Two-Object Interaction.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Object-Object Spatial Relationships (OOR). Given a textual description of the spatial relationship between two objects, our method models OOR, representing their relative poses ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Our Coordinate Systems. We conceptually model the transformation from a scale-normalized space, where the tightest 3D bounding box of each object is normalized ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Dataset Generation Overview. For a given text prompt related to an object pair, we obtain multi-view images and point clouds using off-the-shelf models. ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Training Process of OOR Diffusion. Our OOR diffu- sion generates OOR samples by taking the context c, base object category B, and target ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 5. Scene Graph Example. The scene graph for multi-object OOR is represented as a connected DAG with one start node. starting node (global base), ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 6. Qualitative Comparisons of Pairwise OOR Generation. Our method models object-object spatial relationships better than LLM-based baselines. Metrics SMC [58] SceneTeller [39] Ours CLIP ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative Comparisons of Pairwise OOR Gen- eration. For each method, we evaluate CLIP score [45], VQA score [33], our proposed VLM score [65], ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 7. Qualitative Comparisons of Multi-object OOR Gen- eration. We generate multi-object OOR by combining each sample from our pairwise OOR diffusion model. Our method ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate 20 scenes where 3 to 5 objects have spatial relations with each other. | embodiment, simulator version and control stack | p. 7 (4.2. Multi-object OOR Generation), p. 7 (4.3. Applications of OOR) |
| Task/environment | We demonstrate the efficacy of our proposed scene arrangement methods using ParaHome DB [27], which provides 3D scenes with separate object meshes. | reset, timeout, object/scene variation | p. 7 (4.3. Applications of OOR), p. 6 (4.1. Pairwise OOR Generation) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 3 (3.2. 3D OOR Samples Generation), p. 3 (3.2. 3D OOR Samples Generation) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 4 (3.2. 3D OOR Samples Generation), p. 4 (3.2. 3D OOR Samples Generation) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 2 further demonstrates the superiority of our method, especially in the case of VLM score and user study. | definition/direction/unit from same section | p. 7 (4.2. Multi-object OOR Generation) |
| However, for per-image scores such as CLIP score and VQA score, we apply them only to the ControlNet-generated images. | definition/direction/unit from same section | p. 7 (4.2. Multi-object OOR Generation) |
| The CLIP score [45] measures textimage alignment by averaging CLIP model logits. | definition/direction/unit from same section | p. 6 (4.1. Pairwise OOR Generation) |
| The VQA score [33] leverages a VQA model to assess object composition and relations. | definition/direction/unit from same section | p. 6 (4.1. Pairwise OOR Generation) |
| Figure 4. Training Process of OOR Diffusion. Our OOR diffu- sion generates OOR samples by taking the context c, base object category B, and ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| 4.1, we show that our diffusion model generates OORs that fit the text context 8422 | definition/direction/unit from same section | p. 5 (4. Experiments) |
| We demonstrate this by synthesizing human motion interacting with two objects using generated OORs. | definition/direction/unit from same section | p. 8 (4.3. Applications of OOR) |
| We assume two objects and a human interacting initially, and synthesize human motion using the generated OOR and contact consistency. | definition/direction/unit from same section | p. 8 (4.3. Applications of OOR) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In contrast, our OOR diffusion demonstrates superior sampling capabilities compared to the baselines, leveraging its effective learning of 8423 | comparison identity and matched condition | p. 6 (4.1. Pairwise OOR Generation) |
| 1 shows that our method outperforms baselines for all metrics. | comparison identity and matched condition | p. 7 (4.1. Pairwise OOR Generation) |
| Our method models object-object spatial relationships better than LLM-based baselines. | comparison identity and matched condition | p. 6 (4. Experiments) |
| Our method better captures multi-object OOR compared to the diffusion-based text-to-3D model. | comparison identity and matched condition | p. 7 (4.1. Pairwise OOR Generation) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| However, due to the inherent limitation of estimating 3D information without direct 3D data, it lacks fine-grained control. | component/input/data sensitivity | p. 6 (4.1. Pairwise OOR Generation) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our main contributions are as follows: (1) We formulate a novel representation for object-object spatial relationships (OOR); (2) We introduce an effective ... | 4.2 demonstrates our advanced sampling approach produces significantly better results compared to text-to-3D models. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4. Experiments), p. 7 (4.1. Pairwise OOR Generation), p. 6 (4.1. Pairwise OOR Generation), p. 7 (4.2. Multi-object OOR Generation), p. 8 (4.3. Applications of OOR), p. 5 (Figure/Table caption) |
| Primary metric/result | 1 shows that our method outperforms baselines for all metrics. | numeric claim only at cited anchor | p. 7 (4.1. Pairwise OOR Generation) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Pairwise OOR Generation - extractive PDF cue:** We evaluate our method and the baselines on a total of 150 scenes derived from 30 category pairs with 5 scenes generated per prompt.
- **p. 7 / 4.2. Multi-object OOR Generation - extractive PDF cue:** We evaluate 20 scenes where 3 to 5 objects have spatial relations with each other.
- **p. 7 / 4.3. Applications of OOR - extractive PDF cue:** In practice, optimization is completed within 50 steps.
- **p. 5 / 3.3. OOR Diffusion - extractive PDF cue:** As a result, we train our model for 475 distinct contexts with 23750 text prompts, each capturing various spatial relationships between object pairs across 188 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | However, due to the inherent limitation of estimating 3D information without direct 3D data, it lacks fine-grained control. | p. 6 (4.1. Pairwise OOR Generation) |
| body limitation/failure cue | 7, GraphDreamer often fails to capture OOR (e.g., "A knife cuts an apple."). | p. 7 (4.2. Multi-object OOR Generation) |
| body limitation/failure cue | Since SMC and SceneTeller cannot be directly extended to multi-object OOR using only pairwise OOR data, we compare our model to another baseline GraphDreamer ... | p. 7 (4.2. Multi-object OOR Generation) |
| body limitation/failure cue | (a) adding random noise to the original scene and then rearranging it. | p. 8 (4.3. Applications of OOR) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Thus, we compare ours with LLM-based methods that pursue similar goals: SceneMotifCoder (SMC) [58], which focuses on 3D object alignments, and SceneTeller [39], which ... | p. 6 (4.1. Pairwise OOR Generation) |
| In practice, optimization is completed within 50 steps. | p. 7 (4.3. Applications of OOR) |
| It even omits certain objects, such as a computer mouse or a salt shaker. | p. 7 (4.2. Multi-object OOR Generation) |
| Specifically, we take c, B, and T as text input and encode them with the pre-trained T5 text encoder [46]. | p. 4 (3.3. OOR Diffusion) |
| From this registration, we compute their relative spatial transformation Trel, which is parameterized by Eq. | p. 4 (3.2. 3D OOR Samples Generation) |
| Pose and Scale T5 Encoder Text Prompt Base Category Target Category MLP MLP MLP MLP MLP MLP Figure 4. | p. 5 (3.3. OOR Diffusion) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4.1. Pairwise OOR Generation - extractive PDF cue:** However, due to the inherent limitation of estimating 3D information without direct 3D data, it lacks fine-grained control.
- **p. 7 / 4.2. Multi-object OOR Generation - extractive PDF cue:** 7, GraphDreamer often fails to capture OOR (e.g., "A knife cuts an apple.").
- **p. 7 / 4.2. Multi-object OOR Generation - extractive PDF cue:** Since SMC and SceneTeller cannot be directly extended to multi-object OOR using only pairwise OOR data, we compare our model to another baseline GraphDreamer [13], ...
- **p. 8 / 4.3. Applications of OOR - extractive PDF cue:** (a) adding random noise to the original scene and then rearranging it.

- **PDF anchors reviewed:** datasets p. 7 (4.2. Multi-object OOR Generation), p. 7 (4.3. Applications of OOR), p. 6 (4.1. Pairwise OOR Generation), p. 6 (4.1. Pairwise OOR Generation), p. 8 (4.3. Applications of OOR), p. 8 (4.3. Applications of OOR), metrics p. 7 (4.2. Multi-object OOR Generation), p. 7 (4.2. Multi-object OOR Generation), p. 6 (4.1. Pairwise OOR Generation), p. 6 (4.1. Pairwise OOR Generation), p. 5 (Figure/Table caption), p. 5 (4. Experiments), baselines p. 6 (4.1. Pairwise OOR Generation), p. 7 (4.1. Pairwise OOR Generation), p. 6 (4. Experiments), p. 7 (4.1. Pairwise OOR Generation), results p. 6 (4. Experiments), p. 7 (4.1. Pairwise OOR Generation), p. 6 (4.1. Pairwise OOR Generation), p. 7 (4.2. Multi-object OOR Generation), p. 8 (4.3. Applications of OOR), p. 5 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
