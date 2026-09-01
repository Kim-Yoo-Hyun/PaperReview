# Evaluation - Neural Point Cloud Diffusion for Disentangled 3D Shape and Appearance Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Schroppel_Neural_Point_Cloud_Diffusion_for_Disentangled_3D_Shape_and_Appearance_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Schroppel_Neural_Point_Cloud_Diffusion_for_Disentangled_3D_Shape_and_Appearance_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.4. 3D diffusion comparison), p. 7 (4.3. Disentangled generation), p. 8 (Figure/Table caption), p. 5 (4. Experiments), p. 6 (4.2. Metrics), p. 8 (4.6. Analysis)): Our NPCD model achieves better scores than DiffRF and Functa.

## Evaluation Body Digest

- **p. 5 / 4.1. Datasets and experimental setup - extractive PDF cue:** The dataset contains 15,576 objects and features more realistic textures on top of ShapeNet meshes.
- **p. 7 / 4.3. Disentangled generation - extractive PDF cue:** Note that our method performs an actual recombination and does more than retrieval of objects from the training dataset.
- **p. 5 / 4.1. Datasets and experimental setup - extractive PDF cue:** Additionally, we use the PhotoShape Chairs dataset [30].
- **p. 7 / 4.4. 3D diffusion comparison - extractive PDF cue:** We compare NPCD with Functa [10], SSDNeRF [8], and DiffRF [26], previous works that generate 3D shape and appearance on medium-scale datasets with 3D diffusion ...
- **p. 6 / 4.2. Metrics - extractive PDF cue:** We use the images of the test set objects as the reference set.
- **p. 6 / 4.2. Metrics - extractive PDF cue:** For comparability, we follow the evaluation procedures of previous works: on SRN Cars and Chairs, we generate the same number of objects as in the ...
- **p. 6 / 4.2. Metrics - extractive PDF cue:** Furthermore, for the shape-only evaluation of our generated point clouds representing the coarse geometry, we employ 1-nearest-neighbor accuracy w.r.t.
- **p. 7 / 4.4. 3D diffusion comparison - extractive PDF cue:** Our NPCD model achieves better scores than DiffRF and Functa.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Datasets and experimental setup (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.4. 3D diffusion comparison | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our NPCD model achieves better scores than DiffRF and Functa. | p. 7 (4.4. 3D diffusion comparison) |
| 4.3. Disentangled generation | EMPIRICAL / SOURCE-REPORTED EVALUATION | The numbers show that we clearly outperform previous generative models that allow disentangled generation. | p. 7 (4.3. Disentangled generation) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 4. Auto-decoded feature similarity. We compute per-point mean cosine similarities between optimized neural point features of 10 training examples for 100 different seeds. ... | p. 8 (Figure/Table caption) |
| 4. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | In this section, we provide experimental results for the presented NPCD method. | p. 5 (4. Experiments) |
| 4.2. Metrics | EMPIRICAL / SOURCE-REPORTED EVALUATION | Furthermore, for the shape-only evaluation of our generated point clouds representing the coarse geometry, we employ 1-nearest-neighbor accuracy w.r.t. | p. 6 (4.2. Metrics) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Datasets and experimental setup - extractive PDF cue:** The dataset contains 15,576 objects and features more realistic textures on top of ShapeNet meshes.
- **p. 7 / 4.3. Disentangled generation - extractive PDF cue:** Note that our method performs an actual recombination and does more than retrieval of objects from the training dataset.
- **p. 5 / 4.1. Datasets and experimental setup - extractive PDF cue:** Additionally, we use the PhotoShape Chairs dataset [30].
- **p. 7 / 4.4. 3D diffusion comparison - extractive PDF cue:** We compare NPCD with Functa [10], SSDNeRF [8], and DiffRF [26], previous works that generate 3D shape and appearance on medium-scale datasets with 3D diffusion ...
- **p. 6 / 4.2. Metrics - extractive PDF cue:** We use the images of the test set objects as the reference set.
- **p. 6 / 4.2. Metrics - extractive PDF cue:** For comparability, we follow the evaluation procedures of previous works: on SRN Cars and Chairs, we generate the same number of objects as in the ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We present a method to model 3D radiance field distributions using neural point denoising diffusion (left). Since our representa- tion disentangles coarse object ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of neural point cloud diffusion (NCPD). In the center we have a neural point cloud representation, where each point has a position ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3. Qualitative examples of disentangled generation on SRN cars, SRN chairs, PhotoShape chairs. (a) Appearance-only gener- ation: we show a generated object and objects ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Comparison to disentanglement-capable approaches. The numbers show that we clearly outperform previous generative models that allow disentangled generation.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Comparison to 3D diffusion models for uncondi- tional 3D shape and appearance generation. Our NPCD model achieves better scores than DiffRF and Functa. ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Shape-only comparison. We evaluate the point cloud generation part of our approach individually. Despite being just the coarse structure of a finer radiance ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4. Comparison against previous generative models that allow disentangled generation.: While we present the first diffusion model allowing disentangled generation, earlier works are GAN-based. ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Auto-decoded feature similarity. We compute per-point mean cosine similarities between optimized neural point features of 10 training examples for 100 different seeds. Zero ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The dataset contains 15,576 objects and features more realistic textures on top of ShapeNet meshes. | embodiment, simulator version and control stack | p. 5 (4.1. Datasets and experimental setup), p. 7 (4.3. Disentangled generation) |
| Task/environment | Note that our method performs an actual recombination and does more than retrieval of objects from the training dataset. | reset, timeout, object/scene variation | p. 7 (4.3. Disentangled generation), p. 5 (4.1. Datasets and experimental setup) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 4 (3.2. Autodecoding for diffusion), p. 5 (3.3. Neural point cloud diffusion) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 5 (3.3. Neural point cloud diffusion), p. 4 (3.3. Neural point cloud diffusion) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Furthermore, for the shape-only evaluation of our generated point clouds representing the coarse geometry, we employ 1-nearest-neighbor accuracy w.r.t. | definition/direction/unit from same section | p. 6 (4.2. Metrics) |
| Our NPCD model achieves better scores than DiffRF and Functa. | definition/direction/unit from same section | p. 7 (4.4. 3D diffusion comparison) |
| Chamfer and Earth Mover's Distance [45]. | definition/direction/unit from same section | p. 6 (4.2. Metrics) |
| Here, we analyze the effects of different initialization strategies, feature dimensionality and regularization methods in the category-level 8791 | definition/direction/unit from same section | p. 7 (4.6. Analysis) |
| It can be seen that our model generates examples in much higher quality, as also evident from the metrics in Tab. | definition/direction/unit from same section | p. 8 (4.6. Analysis) |
| Overall, we found an appropriate initialization and regularization to be key ingredients for successful neural point cloud diffusion. | definition/direction/unit from same section | p. 8 (4.6. Analysis) |
| Figure 1. We present a method to model 3D radiance field distributions using neural point denoising diffusion (left). Since our representa- tion disentangles coarse ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. Overview of neural point cloud diffusion (NCPD). In the center we have a neural point cloud representation, where each point has a ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The numbers show that we clearly outperform previous generative models that allow disentangled generation. | comparison identity and matched condition | p. 7 (4.3. Disentangled generation) |
| Thus, to complement existing comparisons, we also provide a shapeonly comparison in Sec. | comparison identity and matched condition | p. 5 (4. Experiments) |
| Next, we compare against recent diffusion models without disentangling capabilities in Sec. | comparison identity and matched condition | p. 5 (4. Experiments) |
| 1 and a qualitative comparison in Fig. | comparison identity and matched condition | p. 7 (4.3. Disentangled generation) |
| Comparison against previous generative models that allow disentangled generation.: While we present the first diffusion model allowing disentangled generation, earlier works are GAN-based. | comparison identity and matched condition | p. 8 (4.6. Analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Next, we compare against recent diffusion models without disentangling capabilities in Sec. | component/input/data sensitivity | p. 5 (4. Experiments) |
| As diffusion on hybrid point clouds and local radiance fields has not been done before, we conduct ablation studies and analyze various novel design ... | component/input/data sensitivity | p. 7 (4.6. Analysis) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In contrast, we propose a method that enables individual generation of shape and appearance by introducing a hybrid approach that consists of a neural ... | Our NPCD model achieves better scores than DiffRF and Functa. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.4. 3D diffusion comparison), p. 7 (4.3. Disentangled generation), p. 8 (Figure/Table caption), p. 5 (4. Experiments), p. 6 (4.2. Metrics), p. 8 (4.6. Analysis) |
| Primary metric/result | The numbers show that we clearly outperform previous generative models that allow disentangled generation. | numeric claim only at cited anchor | p. 7 (4.3. Disentangled generation) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Datasets and experimental setup - extractive PDF cue:** We extract point clouds with 30k points from the mesh and subsample them to 512 points with farthest point sampling.
- **p. 5 / 4.1. Datasets and experimental setup - extractive PDF cue:** The dataset contains 15,576 objects and features more realistic textures on top of ShapeNet meshes.
- **p. 5 / 4.1. Datasets and experimental setup - extractive PDF cue:** We use the same test split as DiffRF [26] with 1, 552 objects.
- **p. 5 / 4.1. Datasets and experimental setup - extractive PDF cue:** From the remaining objects, we randomly select 2, 480 objects for training.
- **p. 5 / 4.1. Datasets and experimental setup - extractive PDF cue:** We use a resolution of 128x128 pixels and the same point clouds with 512 points as for SRN chairs.
- **p. 6 / 4.2. Metrics - extractive PDF cue:** For comparability, we follow the evaluation procedures of previous works: on SRN Cars and Chairs, we generate the same number of objects as in the ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Further details on the denoiser architecture, diffusion model parameters, and training parameters are provided in the supplementals. | p. 6 (4.1. Datasets and experimental setup) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Finally, we analyze many-toone mappings due to auto-decoded features as a problem for diffusion models and propose regularization methods as effective countermeasures in Sec. | p. 5 (4. Experiments) |
| In the Point-NeRF autodecoder, we optimize the reconstruction loss in Eq. | p. 6 (4.1. Datasets and experimental setup) |
| conduct a quantitative analysis by reporting the per-point mean cosine similarities between optimized neural point features of 10 random training examples over 100 different ... | p. 7 (4.2. Metrics) |
| Point-NeRF autodecoder and diffusion model. | p. 8 (4.6. Analysis) |
| 4 indicates that the simple measure of zero initialization is able to largely mitigate the many-to-one mappings in the MLP decoder and provide much ... | p. 8 (4.6. Analysis) |
| We discuss characteristics of autodecoder schemes in Sec. | p. 3 (3. Method) |
| At the center of our method is an autodecoder with a neural point representation for the latent codes, which is further described in Sec. | p. 3 (3. Method) |
| Second, the decoder learns to be more robust to small changes in f due to the sampling procedure. | p. 4 (3.2. Autodecoding for diffusion) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4.1. Datasets and experimental setup - extractive PDF cue:** Further details on the denoiser architecture, diffusion model parameters, and training parameters are provided in the supplementals.

- **PDF anchors reviewed:** datasets p. 5 (4.1. Datasets and experimental setup), p. 7 (4.3. Disentangled generation), p. 5 (4.1. Datasets and experimental setup), p. 7 (4.4. 3D diffusion comparison), p. 6 (4.2. Metrics), p. 6 (4.2. Metrics), metrics p. 6 (4.2. Metrics), p. 7 (4.4. 3D diffusion comparison), p. 6 (4.2. Metrics), p. 7 (4.6. Analysis), p. 8 (4.6. Analysis), p. 8 (4.6. Analysis), baselines p. 7 (4.3. Disentangled generation), p. 5 (4. Experiments), p. 5 (4. Experiments), p. 7 (4.3. Disentangled generation), p. 8 (4.6. Analysis), results p. 7 (4.4. 3D diffusion comparison), p. 7 (4.3. Disentangled generation), p. 8 (Figure/Table caption), p. 5 (4. Experiments), p. 6 (4.2. Metrics), p. 8 (4.6. Analysis).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
