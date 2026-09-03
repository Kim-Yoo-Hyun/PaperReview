# Evaluation - LaGeM: A Large Geometry Model for 3D Representation Learning and Diffusion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=72OSO38a2z; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/114810. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS)): While for LaGeM-Objaverse, there is a large improvement in both training cost and quantitative results.

## Evaluation Body Digest

- **p. 9 / 4 EXPERIMENTS - extractive body cue:** The objects from these datasets vary from daily objects, CAD models, human models, and synthetic objects.
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** Since most 3D models in this dataset are not watertight, 6
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Our trained model is capable of doing inference on several existing datasets.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** It can be applied on non-watertight datasets like ABO and pix3d even if the model is trained on watertight datasets.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** From the metrics, we can see that LaGeM-Objaverse is able to represent different kinds of objects with highly detailed geometry and sharp features.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We use Chamfer distance and Fscore as the metrics.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Chamfer ↓(×100) F-Score ↑(×100) Dataset # Meshes Manifold VS LaGeM(∆) VS LaGeM(∆) Thingi10k (Zhou & Jacobson, 2016) 10k Yes 4.52 2.99 -1.53 92.75 97.19 4.44 ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** In the end, we generate Z1 conditioned on both Z3 and Z2.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | While for LaGeM-Objaverse, there is a large improvement in both training cost and quantitative results. | p. 7 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | The quantitative results show an improvement of almost 50 percent averaged across the complete dataset in terms of the metric Chamfer. | p. 7 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | We show autoencoding results on ShapeNet. | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our results are better than VecSet in all categories. | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | 11 for some unconditional generation results. | p. 9 (4 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 9 / 4 EXPERIMENTS - extractive body cue:** The objects from these datasets vary from daily objects, CAD models, human models, and synthetic objects.
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** Since most 3D models in this dataset are not watertight, 6
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Our trained model is capable of doing inference on several existing datasets.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** It can be applied on non-watertight datasets like ABO and pix3d even if the model is trained on watertight datasets.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** From the metrics, we can see that LaGeM-Objaverse is able to represent different kinds of objects with highly detailed geometry and sharp features.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Autoencoders. We show different autoencoder architectures here, including AE (AutoEn- coder), U-Net, VAE (Kingma, 2013), NVAE (Vahdat & Kautz, 2020), VecSet (Zhang et ...
- **p. 3 / Figure/Table caption - extractive body cue:** Table 1: Geometric Latent Representation and Generation.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Pipeline. We proposed a U-Net-style transformer for the autoencoding. In this way, we obtain a hierarchical latent space, which contains several levels of ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Geometry Autoencoder. The design from VecSet (Zhang et al., 2023) can be seen as a special case of the proposed LaGeM network with ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4: LaGeM architecture. We show an illustration with 3 levels of latents. 3
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2: Regularization in the Bottleneck. We compare the proposed regularization (NBAE) and VAE. We do not need an explicit loss to regularize the latent ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Cascaded Latent Diffusion.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3: Running Statistics of LaGeM. When using a small number (512) of latent vectors, our model uses 0.87x time and 0.66x memory during training. ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The objects from these datasets vary from daily objects, CAD models, human models, and synthetic objects. | embodiment, simulator version and control stack | p. 9 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Task/environment | Since most 3D models in this dataset are not watertight, 6 | reset, timeout, object/scene variation | p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 4 (3 METHODOLOGY), p. 5 (3 METHODOLOGY) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 5 (3 METHODOLOGY), p. 6 (3 METHODOLOGY) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We use Chamfer distance and Fscore as the metrics. | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| Chamfer ↓(×100) F-Score ↑(×100) Dataset # Meshes Manifold VS LaGeM(∆) VS LaGeM(∆) Thingi10k (Zhou & Jacobson, 2016) 10k Yes 4.52 2.99 -1.53 92.75 97.19 ... | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| In the end, we generate Z1 conditioned on both Z3 and Z2. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| Then we use Z3 as a condition to generate Z2, which adds major details to the models. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| Figure 13: Latent with red color Z means it is replaced by Gaussian noise. Latent with blue color Z means it is generated with ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| Figure 1: Autoencoders. We show different autoencoder architectures here, including AE (AutoEn- coder), U-Net, VAE (Kingma, 2013), NVAE (Vahdat & Kautz, 2020), VecSet (Zhang ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Table 2: Regularization in the Bottleneck. We compare the proposed regularization (NBAE) and VAE. We do not need an explicit loss to regularize the ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Table 7: Results on different regularizers. Loss 16 epochs 32 epochs 48 epochs 60 epochs 72 epochs KL | definition/direction/unit from same section | p. 18 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Both models are compared against VecSet (Zhang et al., 2023). | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| Since ShapeNet is a relatively small and easy dataset compared to Objaverse, we choose smaller latents which are 32×32, 128×16, and 512×8. | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| Again, we use VecSet's model as the baseline. | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| Figure 15: Our generated results. Compared to Fig. 14, we can generate clean, sharp, and detailed shapes. | comparison identity and matched condition | p. 18 (Figure/Table caption) |
| Table 6: Generative result comparison. chair 3DILG VecSet Ours table 3DILG VecSet | comparison identity and matched condition | p. 17 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 13: Latent with red color Z means it is replaced by Gaussian noise. Latent with blue color Z means it is generated with ... | component/input/data sensitivity | p. 16 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We summarize our contributions as follows: • We propose a hierarchical autoencoder architecture with faster training time and low memory consumption. | While for LaGeM-Objaverse, there is a large improvement in both training cost and quantitative results. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Primary metric/result | The quantitative results show an improvement of almost 50 percent averaged across the complete dataset in terms of the metric Chamfer. | numeric claim only at cited anchor | p. 7 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** The three levels of latents are 128×64, 512×32, and 2048×16 (where 64, 32, and 16 are channels of the latents).
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Since ShapeNet is a relatively small and easy dataset compared to Objaverse, we choose smaller latents which are 32×32, 128×16, and 512×8.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** We trained the model for around 200 hours with 4 A100 GPUs.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** The model is trained on 16 A100 GPUs for around 100 hours.
- **p. 6 / 3 METHODOLOGY - extractive body cue:** When using a small number (512) of latent vectors, our model uses 0.87x time and 0.66x memory during training.
- **p. 6 / 3 METHODOLOGY - extractive body cue:** For larger models (2k latent vectors), the advantage is even more significant (0.7x time and 0.58x memory).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Due to failures of modeling loading and conversion, we obtained around 600k watertight models for training. | p. 7 (4 EXPERIMENTS) |
| body limitation/failure cue | Our method does not solve the high training cost problem of diffusion itself. | p. 10 (5 CONCLUSION) |
| body limitation/failure cue | Figure 13: Latent with red color Z means it is replaced by Gaussian noise. Latent with blue color Z means it is generated with ... | p. 16 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We can see that, LaGeM-ShapeNet has almost the same number of parameters as VecSet, but with much shorter training time and less training memory. | p. 7 (4 EXPERIMENTS) |
| Some other hyperparameters of the network can also be found in Table 3. | p. 7 (4 EXPERIMENTS) |
| For Objaverse-10k, due to limited training GPU resources, we select a subset of 10k models from Objaverse and train the unconditional generative model. | p. 9 (4 EXPERIMENTS) |
| This severely affects the training time when M is large. | p. 4 (3 METHODOLOGY) |
| VecSet LaGeM VecSet LaGeM VecSet LaGeM Batch Size 64 8 4 Self Attn Layers 24 8/8/8 24 8/8/8 24 8/8/8 Attn Channels 512 512/512/512 ... | p. 6 (3 METHODOLOGY) |
| Now we can decode a continuous function. | p. 4 (3 METHODOLOGY) |
| (7) Thus we name it Normalized Bottleneck Autoencoder (NBAE). | p. 5 (3 METHODOLOGY) |
| 3), we interpret the cross attention in the encoder part as a down-sampling operator. | p. 5 (3 METHODOLOGY) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Due to failures of modeling loading and conversion, we obtained around 600k watertight models for training.
- **p. 10 / 5 CONCLUSION - extractive body cue:** Our method does not solve the high training cost problem of diffusion itself.
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 13: Latent with red color Z means it is replaced by Gaussian noise. Latent with blue color Z means it is generated with the ...

- **Evidence anchors reviewed:** datasets p. 9 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), metrics p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 16 (Figure/Table caption), p. 2 (Figure/Table caption), baselines p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 18 (Figure/Table caption), p. 17 (Figure/Table caption), results p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
