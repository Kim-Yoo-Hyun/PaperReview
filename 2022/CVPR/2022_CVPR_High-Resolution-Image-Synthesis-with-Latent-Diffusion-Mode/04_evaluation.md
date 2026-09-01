# Evaluation - High-Resolution Image Synthesis with Latent Diffusion Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (45 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2112.10752; PDF retrieval source: https://arxiv.org/pdf/2112.10752. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (4.1. On Perceptual Compression Tradeoffs), p. 23 (Figure/Table caption), p. 6 (4.2. Image Generation with Latent Diffusion), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (4.1. On Perceptual Compression Tradeoffs)): Especially compared to pixel-based LDM-1, they achieve much lower FID scores while simultaneously significantly increasing sample throughput.

## Evaluation Body Digest

- **p. 5 / 4.1. On Perceptual Compression Tradeoffs - extractive PDF cue:** Complex datasets such as ImageNet require reduced compression rates to avoid reducing quality.
- **p. 5 / 4.1. On Perceptual Compression Tradeoffs - extractive PDF cue:** 6 shows sample quality as a function of training progress for 2M steps of class-conditional models on the ImageNet [12] dataset.
- **p. 6 / 4.2. Image Generation with Latent Diffusion - extractive PDF cue:** Comparing LDMs with varying compression on the CelebA-HQ (left) and ImageNet (right) datasets.
- **p. 6 / 4.2. Image Generation with Latent Diffusion - extractive PDF cue:** Analyzing the training of class-conditional LDMs with different downsampling factors f over 2M train steps on the ImageNet dataset.
- **p. 6 / 4.2. Image Generation with Latent Diffusion - extractive PDF cue:** The dashed line shows the FID scores for 200 steps, indicating the strong performance of LDM- {4-8}.
- **p. 5 / 4.1. On Perceptual Compression Tradeoffs - extractive PDF cue:** Especially compared to pixel-based LDM-1, they achieve much lower FID scores while simultaneously significantly increasing sample throughput.
- **p. 5 / 4.1. On Perceptual Compression Tradeoffs - extractive PDF cue:** 7, we compare models trained on CelebAHQ [39] and ImageNet in terms sampling speed for different numbers of denoising steps with the DDIM sampler [84] ...
- **p. 6 / 4.2. Image Generation with Latent Diffusion - extractive PDF cue:** FID scores assessed on 5000 samples.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4. Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. On Perceptual Compression Tradeoffs | SYSTEM / EVALUATION SCOPE UNRESOLVED | Especially compared to pixel-based LDM-1, they achieve much lower FID scores while simultaneously significantly increasing sample throughput. | p. 5 (4.1. On Perceptual Compression Tradeoffs) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 11. ×4 upscaling results on ImageNet-Val. (2562); †: FID features computed on validation split, ‡: FID features computed on train split. We also ... | p. 23 (Figure/Table caption) |
| 4.2. Image Generation with Latent Diffusion | SYSTEM / EVALUATION SCOPE UNRESOLVED | We outperform prior diffusion based approaches on all but the LSUN-Bedrooms dataset, where our score is close to ADM [15], despite utilizing half its ... | p. 6 (4.2. Image Generation with Latent Diffusion) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 2. Evaluation of text-conditional image synthesis on the 256 × 256-sized MS-COCO [51] dataset: with 250 DDIM [84] steps our model is on ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Fig. 8. See Sec. D.3 for the quantitative evaluation and im- plementation details. Lastly, following prior work [3, 15, 21, 23], we evalu- ate ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. On Perceptual Compression Tradeoffs - extractive PDF cue:** Complex datasets such as ImageNet require reduced compression rates to avoid reducing quality.
- **p. 5 / 4.1. On Perceptual Compression Tradeoffs - extractive PDF cue:** 6 shows sample quality as a function of training progress for 2M steps of class-conditional models on the ImageNet [12] dataset.
- **p. 6 / 4.2. Image Generation with Latent Diffusion - extractive PDF cue:** Comparing LDMs with varying compression on the CelebA-HQ (left) and ImageNet (right) datasets.
- **p. 6 / 4.2. Image Generation with Latent Diffusion - extractive PDF cue:** Analyzing the training of class-conditional LDMs with different downsampling factors f over 2M train steps on the ImageNet dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Boosting the upper bound on achievable quality with less agressive downsampling. Since diffusion models offer excel- lent inductive biases for spatial data, we ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Illustrating perceptual and semantic compression: Most bits of a digital image correspond to imperceptible details. While DMs allow to suppress this semantically meaningless ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. We condition LDMs either via concatenation or by a more general cross-attention mechanism. See Sec. 3.3 includes the ability to build the underlying ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Samples from LDMs trained on CelebAHQ [39], FFHQ [41], LSUN-Churches [102], LSUN-Bedrooms [102] and class- conditional ImageNet [12], each with a resolution of ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 5. Samples for user-defined text prompts from our model for text-to-image synthesis, LDM-8 (KL), which was trained on the LAION [78] database. Samples generated ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 6. Analyzing the training of class-conditional LDMs with different downsampling factors f over 2M train steps on the Im- ageNet dataset. Pixel-based LDM-1 requires ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 7. Comparing LDMs with varying compression on the CelebA-HQ (left) and ImageNet (right) datasets. Different mark- ers indicate {10, 20, 50, 100, 200} sampling ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Evaluation metrics for unconditional image synthesis. CelebA-HQ results reproduced from [43, 63, 100], FFHQ from [42, 43]. †: N-s refers to N sampling ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Complex datasets such as ImageNet require reduced compression rates to avoid reducing quality. | embodiment, simulator version and control stack | p. 5 (4.1. On Perceptual Compression Tradeoffs), p. 5 (4.1. On Perceptual Compression Tradeoffs) |
| Task/environment | 6 shows sample quality as a function of training progress for 2M steps of class-conditional models on the ImageNet [12] dataset. | reset, timeout, object/scene variation | p. 5 (4.1. On Perceptual Compression Tradeoffs), p. 6 (4.2. Image Generation with Latent Diffusion) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 4 (3.3. Conditioning Mechanisms), p. 4 (3.3. Conditioning Mechanisms) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 1 (1. Introduction), p. 3 (3. Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The dashed line shows the FID scores for 200 steps, indicating the strong performance of LDM- {4-8}. | definition/direction/unit from same section | p. 6 (4.2. Image Generation with Latent Diffusion) |
| Especially compared to pixel-based LDM-1, they achieve much lower FID scores while simultaneously significantly increasing sample throughput. | definition/direction/unit from same section | p. 5 (4.1. On Perceptual Compression Tradeoffs) |
| 7, we compare models trained on CelebAHQ [39] and ImageNet in terms sampling speed for different numbers of denoising steps with the DDIM sampler ... | definition/direction/unit from same section | p. 5 (4.1. On Perceptual Compression Tradeoffs) |
| FID scores assessed on 5000 samples. | definition/direction/unit from same section | p. 6 (4.2. Image Generation with Latent Diffusion) |
| Figure 15. Illustrating the effect of latent space rescaling on convolutional sampling, here for semantic image synthesis on landscapes. See Sec. 4.3.2 and Sec. ... | definition/direction/unit from same section | p. 20 (Figure/Table caption) |
| Table 14. Hyperparameters for the unconditional LDMs trained on the CelebA dataset for the analysis in Fig. 7. All models trained on a single ... | definition/direction/unit from same section | p. 25 (Figure/Table caption) |
| Table 11. ×4 upscaling results on ImageNet-Val. (2562); †: FID features computed on validation split, ‡: FID features computed on train split. We also ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |
| Figure 2. Illustrating perceptual and semantic compression: Most bits of a digital image correspond to imperceptible details. While DMs allow to suppress this semantically ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| On CelebA-HQ, we report a new state-of-the-art FID of 5.11, outperforming previous likelihood-based models as well as GANs. | comparison identity and matched condition | p. 5 (4.2. Image Generation with Latent Diffusion) |
| Table 3. Comparison of a class-conditional ImageNet LDM with recent state-of-the-art methods for class-conditional image gener- ation on ImageNet [12]. A more detailed comparison ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 11. ×4 upscaling results on ImageNet-Val. (2562); †: FID features computed on validation split, ‡: FID features computed on train split. We also ... | comparison identity and matched condition | p. 23 (Figure/Table caption) |
| Fig. 8. See Sec. D.3 for the quantitative evaluation and im- plementation details. Lastly, following prior work [3, 15, 21, 23], we evalu- ate ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| LDM-{4-8} outperform models with unsuitable ratios of perceptual and conceptual compression. | comparison identity and matched condition | p. 5 (4.1. On Perceptual Compression Tradeoffs) |
| Pixel-based LDM-1 requires substantially larger train times compared to models with larger downsampling factors (LDM-{4-16}). | comparison identity and matched condition | p. 6 (4.2. Image Generation with Latent Diffusion) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 15. Illustrating the effect of latent space rescaling on convolutional sampling, here for semantic image synthesis on landscapes. See Sec. 4.3.2 and Sec. ... | component/input/data sensitivity | p. 20 (Figure/Table caption) |
| Figure 10. ImageNet 64→256 super-resolution on ImageNet-Val. LDM-SR has advantages at rendering realistic textures but SR3 can synthesize more coherent fine structures. See appendix ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 11. Qualitative results on object removal with our big, w/ ft inpainting model. For more results, see Fig. 22. instead of 215M. After ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Figure 18. LDM-BSR generalizes to arbitrary inputs and can be used as a general-purpose upsampler, upscaling samples from a class- conditional LDM (image cf. ... | component/input/data sensitivity | p. 23 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In sum, our work makes the following contributions: (i) In contrast to purely transformer-based approaches [23,66], our method scales more graceful to higher dimensional ... | Especially compared to pixel-based LDM-1, they achieve much lower FID scores while simultaneously significantly increasing sample throughput. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (4.1. On Perceptual Compression Tradeoffs), p. 23 (Figure/Table caption), p. 6 (4.2. Image Generation with Latent Diffusion), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (4.1. On Perceptual Compression Tradeoffs) |
| Primary metric/result | Table 11. ×4 upscaling results on ImageNet-Val. (2562); †: FID features computed on validation split, ‡: FID features computed on train split. We also ... | numeric claim only at cited anchor | p. 23 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 4.2. Image Generation with Latent Diffusion - extractive PDF cue:** The dashed line shows the FID scores for 200 steps, indicating the strong performance of LDM- {4-8}.
- **p. 6 / 4.2. Image Generation with Latent Diffusion - extractive PDF cue:** FID scores assessed on 5000 samples.
- **p. 6 / 4.2. Image Generation with Latent Diffusion - extractive PDF cue:** [32] s = 3 Make-A-Scene∗[26] 11.84 - 4B c.f.g for AR models [98] s = 5 LDM-KL-8 23.31 20.03±0.33 1.45B

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Limitations While LDMs significantly reduce computational requirements compared to pixel-based approaches, their sequential sampling process is still slower than that of GANs. | p. 9 (5. Limitations & Societal Impact) |
| body limitation/failure cue | Figure 18. LDM-BSR generalizes to arbitrary inputs and can be used as a general-purpose upsampler, upscaling samples from a class- conditional LDM (image cf. ... | p. 23 (Figure/Table caption) |
| body limitation/failure cue | Interestingly, we find that LDMs trained in VQregularized latent spaces sometimes achieve better sample quality, even though the reconstruction capabilities of VQregularized first stage ... | p. 5 (4. Experiments) |
| body limitation/failure cue | Table 4. Task 1: Subjects were shown ground truth and generated image and asked for preference. Task 2: Subjects had to decide between two ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Figure 10. ImageNet 64→256 super-resolution on ImageNet-Val. LDM-SR has advantages at rendering realistic textures but SR3 can synthesize more coherent fine structures. See appendix ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Figure 15. Illustrating the effect of latent space rescaling on convolutional sampling, here for semantic image synthesis on landscapes. See Sec. 4.3.2 and Sec. ... | p. 20 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In E.2 we list details on architecture, implementation, training and evaluation for all results presented in this section. | p. 5 (4. Experiments) |
| 8 shows hyperparameters and reconstruction performance of the first stage models used for the LDMs compared in this section. | p. 5 (4.1. On Perceptual Compression Tradeoffs) |
| Samples generated with 200 DDIM steps and η = 1.0. | p. 6 (4.2. Image Generation with Latent Diffusion) |
| Results obtained with 100 DDIM steps [84] and κ = 0. | p. 6 (4.2. Image Generation with Latent Diffusion) |
| More precisely, given an image x ∈RH×W ×3 in RGB space, the encoder E encodes x into a latent representa3 | p. 3 (3.1. Perceptual Image Compression) |
| Our perceptual compression model is based on previous work [23] and consists of an autoencoder trained by combination of a perceptual loss [106] and ... | p. 3 (3.1. Perceptual Image Compression) |
| This model can be interpreted as a VQGAN [23] but with the quantization layer absorbed by the decoder. | p. 4 (3.1. Perceptual Image Compression) |
| These models can be interpreted as an equally weighted sequence of denoising autoencoders ϵθ(xt, t); t = 1 . . . | p. 4 (3.2. Latent Diffusion Models) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 5. Limitations & Societal Impact - extractive PDF cue:** Limitations While LDMs significantly reduce computational requirements compared to pixel-based approaches, their sequential sampling process is still slower than that of GANs.
- **p. 23 / Figure/Table caption - extractive PDF cue:** Figure 18. LDM-BSR generalizes to arbitrary inputs and can be used as a general-purpose upsampler, upscaling samples from a class- conditional LDM (image cf. Fig. ...
- **p. 5 / 4. Experiments - extractive PDF cue:** Interestingly, we find that LDMs trained in VQregularized latent spaces sometimes achieve better sample quality, even though the reconstruction capabilities of VQregularized first stage models ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Task 1: Subjects were shown ground truth and generated image and asked for preference. Task 2: Subjects had to decide between two generated ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 10. ImageNet 64→256 super-resolution on ImageNet-Val. LDM-SR has advantages at rendering realistic textures but SR3 can synthesize more coherent fine structures. See appendix for ...
- **p. 20 / Figure/Table caption - extractive PDF cue:** Figure 15. Illustrating the effect of latent space rescaling on convolutional sampling, here for semantic image synthesis on landscapes. See Sec. 4.3.2 and Sec. D.1. ...

- **PDF anchors reviewed:** datasets p. 5 (4.1. On Perceptual Compression Tradeoffs), p. 5 (4.1. On Perceptual Compression Tradeoffs), p. 6 (4.2. Image Generation with Latent Diffusion), p. 6 (4.2. Image Generation with Latent Diffusion), metrics p. 6 (4.2. Image Generation with Latent Diffusion), p. 5 (4.1. On Perceptual Compression Tradeoffs), p. 5 (4.1. On Perceptual Compression Tradeoffs), p. 6 (4.2. Image Generation with Latent Diffusion), p. 20 (Figure/Table caption), p. 25 (Figure/Table caption), baselines p. 5 (4.2. Image Generation with Latent Diffusion), p. 7 (Figure/Table caption), p. 23 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (4.1. On Perceptual Compression Tradeoffs), p. 6 (4.2. Image Generation with Latent Diffusion), results p. 5 (4.1. On Perceptual Compression Tradeoffs), p. 23 (Figure/Table caption), p. 6 (4.2. Image Generation with Latent Diffusion), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (4.1. On Perceptual Compression Tradeoffs).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
