# Evaluation - Marigold: Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (33 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2312.02145; PDF retrieval source: https://arxiv.org/pdf/2312.02145. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies), p. 6 (4.2. Evaluation), p. 6 (4.1. Implementation), p. 4 (Figure/Table caption), p. 5 (4.1. Implementation)): 2, training with multi-resolution noise significantly improves the depth prediction accuracy over using standard Gaussian noise.

## Evaluation Body Digest

- **p. 6 / 4.2. Evaluation - extractive PDF cue:** In the case of the ScanNet dataset, we randomly sampled 800 images from the 312 official validation scenes for testing.
- **p. 6 / 4.2. Evaluation - extractive PDF cue:** Hypersim [37] is a photorealistic dataset with 461 indoor scenes.
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** When fine-tuned on a single synthetic dataset, the pretrained LDM can already be adapted for monocular depth estimation to a certain degree, while the more ...
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** To better understand the impact of the synthetic datasets used for our fine-tuning protocol, we ablate on a photorealistic street-scene Virtual KITTI [7], and a ...
- **p. 7 / 4.3. Ablation Studies - extractive PDF cue:** Qualitative comparison (depth) of monocular depth estimation methods across different datasets.
- **p. 5 / 4.1. Implementation - extractive PDF cue:** We implement Marigold using PyTorch and utilize Stable Diffusion v2 [38] as our backbone, following the original pre-training setup with a v-objective [42].
- **p. 7 / 4.3. Ablation Studies - extractive PDF cue:** Marigold excels at capturing thin structures (e.g., chair legs) and preserving overall layout of the scene (e.g., walls in ETH3D example and chairs in DIODE ...
- **p. 6 / 4.1. Implementation - extractive PDF cue:** All metrics† are presented in percentage terms; bold numbers are the best, underscored second best.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Implementation (p. 5); 4.2. Evaluation (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | 2, training with multi-resolution noise significantly improves the depth prediction accuracy over using standard Gaussian noise. | p. 8 (4.3. Ablation Studies) |
| 4.3. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | Hypersim [37] delivers strong results; Virtual KITTI [7] improves outdoor performance. | p. 8 (4.3. Ablation Studies) |
| 4.2. Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | 1, Marigold outperforms prior art in most cases and secures the highest overall ranking. | p. 6 (4.2. Evaluation) |
| 4.1. Implementation | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method outperforms other methods on both indoor and outdoor scenes in most cases, without having seen a real depth sample. | p. 6 (4.1. Implementation) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 2. Overview of the Marigold fine-tuning protocol. Start- ing from pretrained Stable Diffusion, we encode the image x and depth d into the ... | p. 4 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 4.2. Evaluation - extractive PDF cue:** In the case of the ScanNet dataset, we randomly sampled 800 images from the 312 official validation scenes for testing.
- **p. 6 / 4.2. Evaluation - extractive PDF cue:** Hypersim [37] is a photorealistic dataset with 461 indoor scenes.
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** When fine-tuned on a single synthetic dataset, the pretrained LDM can already be adapted for monocular depth estimation to a certain degree, while the more ...
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** To better understand the impact of the synthetic datasets used for our fine-tuning protocol, we ablate on a photorealistic street-scene Virtual KITTI [7], and a ...
- **p. 7 / 4.3. Ablation Studies - extractive PDF cue:** Qualitative comparison (depth) of monocular depth estimation methods across different datasets.
- **p. 5 / 4.1. Implementation - extractive PDF cue:** We implement Marigold using PyTorch and utilize Stable Diffusion v2 [38] as our backbone, following the original pre-training setup with a v-objective [42].
- **p. 7 / 4.3. Ablation Studies - extractive PDF cue:** Marigold excels at capturing thin structures (e.g., chair legs) and preserving overall layout of the scene (e.g., walls in ETH3D example and chairs in DIODE ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We present Marigold, a diffusion model and associated fine-tuning protocol for monocular depth estimation. Its core principle is to leverage the rich visual ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of the Marigold fine-tuning protocol. Start- ing from pretrained Stable Diffusion, we encode the image x and depth d into the latent ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Overview of the Marigold inference scheme. Given an input image x, we encode it with the original Stable Diffusion VAE into the latent ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative comparison of Marigold with SOTA affine-invariant depth estimators on several zero-shot benchmarks. All metrics† are presented in percentage terms; bold numbers are ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative comparison (depth) of monocular depth estimation methods across different datasets. Marigold excels at capturing thin structures (e.g., chair legs) and preserving overall ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5. Qualitative comparison (unprojected, colored as normals) of monocular depth estimation methods across different datasets. Marigold stands out for its superior reconstruction of flat ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6. Ablation of ensemble size. We observe a monotonic improvement with the growth of ensemble size. This improvement starts to diminish after 10 predictions ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2. Ablation of training noise. Multi-resolution noise im- proves over Gaussian noise; annealing yields further improvement. Multi-res. noise Annealed NYUv2 KITTI AbsRel↓

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In the case of the ScanNet dataset, we randomly sampled 800 images from the 312 official validation scenes for testing. | embodiment, simulator version and control stack | p. 6 (4.2. Evaluation), p. 6 (4.2. Evaluation) |
| Task/environment | Hypersim [37] is a photorealistic dataset with 461 indoor scenes. | reset, timeout, object/scene variation | p. 6 (4.2. Evaluation), p. 8 (4.3. Ablation Studies) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3.2. Network Architecture), p. 4 (3.2. Network Architecture) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (3.3. Fine-Tuning Protocol), p. 5 (3.4. Inference) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| All metrics† are presented in percentage terms; bold numbers are the best, underscored second best. | definition/direction/unit from same section | p. 6 (4.1. Implementation) |
| The second metric, δ1 accuracy, measures the proportion of pixels satisfying max(ai/di, di/ai) < 1.25. | definition/direction/unit from same section | p. 6 (4.2. Evaluation) |
| 2, training with multi-resolution noise significantly improves the depth prediction accuracy over using standard Gaussian noise. | definition/direction/unit from same section | p. 8 (4.3. Ablation Studies) |
| Ensembling 10 predictions reduces the absolute relative error 4.2 11.9 19.7 27.5 35.2 AbsRel (%) NYUv2 AbsRel δ1 1 2 4 10 25 50 ... | definition/direction/unit from same section | p. 8 (4.3. Ablation Studies) |
| We use the Adam optimizer with a learning rate of 3 · 10-5. | definition/direction/unit from same section | p. 5 (4.1. Implementation) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 1. Quantitative comparison of Marigold with SOTA affine-invariant depth estimators on several zero-shot benchmarks. All metrics† are presented in percentage terms; bold numbers ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| We compare Marigold to six baselines, each claiming zero-shot generalization. | comparison identity and matched condition | p. 6 (4.2. Evaluation) |
| Figure 1. We present Marigold, a diffusion model and associated fine-tuning protocol for monocular depth estimation. Its core principle is to leverage the rich ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Qualitative comparison (depth) of monocular depth estimation methods across different datasets. | comparison identity and matched condition | p. 7 (4.3. Ablation Studies) |
| Refer to supplementary sections for extra ablations and discussion. | comparison identity and matched condition | p. 8 (4.3. Ablation Studies) |
| Figure 7. Ablation of denoising steps. The performance improves as the number of denoising steps increases, while we observe satu- ration after 10 steps. | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 1. Quantitative comparison of Marigold with SOTA affine-invariant depth estimators on several zero-shot benchmarks. All metrics† are presented in percentage terms; bold numbers ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| It also shows that our fine-tuning protocol was successful in adapting Stable Diffusion for this task without unlearning such visual priors. | component/input/data sensitivity | p. 6 (4.2. Evaluation) |
| We evaluate the effect of the re-spaced inference denoising steps driven by the DDIM scheduler [49]. | component/input/data sensitivity | p. 8 (4.3. Ablation Studies) |
| Refer to supplementary sections for extra ablations and discussion. | component/input/data sensitivity | p. 8 (4.3. Ablation Studies) |
| Figure 2. Overview of the Marigold fine-tuning protocol. Start- ing from pretrained Stable Diffusion, we encode the image x and depth d into the ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Figure 1. We present Marigold, a diffusion model and associated fine-tuning protocol for monocular depth estimation. Its core principle is to leverage the rich ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Capitalizing on that, we propose the following test-time ensembling scheme, capable of combining multiple inference passes over the same input. | 2, training with multi-resolution noise significantly improves the depth prediction accuracy over using standard Gaussian noise. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies), p. 6 (4.2. Evaluation), p. 6 (4.1. Implementation), p. 4 (Figure/Table caption), p. 5 (4.1. Implementation) |
| Primary metric/result | Hypersim [37] delivers strong results; Virtual KITTI [7] improves outdoor performance. | numeric claim only at cited anchor | p. 8 (4.3. Ablation Studies) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Implementation - extractive PDF cue:** At inference time, we apply the DDIM scheduler [49] and only sample 50 steps.
- **p. 5 / 4.1. Implementation - extractive PDF cue:** To fit one GPU, we accumulate gradients for 16 steps.
- **p. 5 / 4.1. Implementation - extractive PDF cue:** Training our method to convergence takes approximately 2.5 days on a single Nvidia RTX 4090 GPU card.
- **p. 6 / 4.2. Evaluation - extractive PDF cue:** We use the official split with around 54K samples from 365 scenes for training.
- **p. 6 / 4.2. Evaluation - extractive PDF cue:** The second dataset, Virtual KITTI [7] is a synthetic street-scene dataset featuring 5 scenes under varying conditions like weather or camera perspectives.
- **p. 6 / 4.2. Evaluation - extractive PDF cue:** We crop the images to the KITTI benchmark resolution [17] and set the far plane to 80 meters.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Future research directions to overcome current limitations include improving inference efficiency, ensuring that similar inputs yield consistent outputs despite the model's generative nature, and ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | During training, we apply the DDPM noise scheduler [20] with 1000 diffusion steps. | p. 5 (4.1. Implementation) |
| body limitation/failure cue | For the final prediction, we aggregate results from 10 inference runs with varying starting noise. | p. 5 (4.1. Implementation) |
| body limitation/failure cue | We investigate the impact of three types of noise during the training phase. | p. 8 (4.3. Ablation Studies) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| At inference time, we apply the DDIM scheduler [49] and only sample 50 steps. | p. 5 (4.1. Implementation) |
| To fit one GPU, we accumulate gradients for 16 steps. | p. 5 (4.1. Implementation) |
| We also noticed that training with multi-resolution noise leads to more consistent predictions given different initial noise at inference time and annealing further enhances ... | p. 8 (4.3. Ablation Studies) |
| At inference time, the depth latent code is decoded once at the end of diffusion, and the average of three channels is taken as ... | p. 4 (3.2. Network Architecture) |
| For HDN [60] we show the ScanNet results from Metric3D, as no source code is available. ∗Image-text data is used in the pretrained model. | p. 6 (4.1. Implementation) |
| As expected, we obtain better results when using more denoising steps. | p. 8 (4.3. Ablation Studies) |
| At training time, parameters θ are updated by taking a data pair (x, d) from the training set, noising d with sampled noise ϵ ... | p. 3 (3.1. Generative Formulation) |
| The canonical standard noise objective L is given as follows [20]: \mathcal {L} = \ma t hb b {E} _ {\depth _0, \noise \sim ... | p. 3 (3.1. Generative Formulation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive PDF cue:** Future research directions to overcome current limitations include improving inference efficiency, ensuring that similar inputs yield consistent outputs despite the model's generative nature, and better ...
- **p. 5 / 4.1. Implementation - extractive PDF cue:** During training, we apply the DDPM noise scheduler [20] with 1000 diffusion steps.
- **p. 5 / 4.1. Implementation - extractive PDF cue:** For the final prediction, we aggregate results from 10 inference runs with varying starting noise.
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** We investigate the impact of three types of noise during the training phase.

- **PDF anchors reviewed:** datasets p. 6 (4.2. Evaluation), p. 6 (4.2. Evaluation), p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies), p. 7 (4.3. Ablation Studies), p. 5 (4.1. Implementation), metrics p. 6 (4.1. Implementation), p. 6 (4.2. Evaluation), p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies), p. 5 (4.1. Implementation), baselines p. 6 (Figure/Table caption), p. 6 (4.2. Evaluation), p. 1 (Figure/Table caption), p. 7 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies), p. 8 (Figure/Table caption), results p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies), p. 6 (4.2. Evaluation), p. 6 (4.1. Implementation), p. 4 (Figure/Table caption), p. 5 (4.1. Implementation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
