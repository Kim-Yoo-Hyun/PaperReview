# Evaluation - Denoising Diffusion Probabilistic Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2006.11239; PDF retrieval source: https://arxiv.org/pdf/2006.11239. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (4 Experiments), p. 5 (4 Experiments), p. 6 (4 Experiments), p. 8 (4 Experiments), p. 13 (Figure/Table caption)): With our FID score of 3.17, our unconditional model achieves better sample quality than most models in the literature, including class conditional models.

## Evaluation Body Digest

- **p. 5 / 4 Experiments - extractive body cue:** Our FID score is computed with respect to the training set, as is standard practice; when we compute it with respect to the test set, ...
- **p. 7 / 4 Experiments - extractive body cue:** (A stochastic reconstruction x0 ∼pθ(x0/xt) is also valid, but we do not consider it here because it makes distortion more difficult to evaluate.) Figure 5 ...
- **p. 7 / 4 Experiments - extractive body cue:** 0 200 400 600 800 1,000 0 20 40 60 80 Reverse process steps (T -t) Distortion (RMSE) 0 200 400 600 800 1,000 0 ...
- **p. 6 / 4 Experiments - extractive body cue:** We find that the baseline option of predicting ˜µ works well only when trained on the true variational bound instead of unweighted mean squared error, ...
- **p. 6 / 4 Experiments - extractive body cue:** 4.2 Reverse process parameterization and training objective ablation In Table 2, we show the sample quality effects of reverse process parameterizations and training objectives (Section ...
- **p. 5 / 4 Experiments - extractive body cue:** 4.1 Sample quality Table 1 shows Inception scores, FID scores, and negative log likelihoods (lossless codelengths) on CIFAR10.
- **p. 6 / 4 Experiments - extractive body cue:** Still, while our lossless codelengths are better than the large estimates reported for energy based models and score matching using annealed importance sampling [11], they ...
- **p. 6 / 4 Experiments - extractive body cue:** Treating the variational bound terms L1 +· · ·+LT as rate and L0 as distortion, our CIFAR10 model with the highest quality samples has a ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4 Experiments (p. 5); B Experimental details (p. 14).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | With our FID score of 3.17, our unconditional model achieves better sample quality than most models in the literature, including class conditional models. | p. 5 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 4.1 Sample quality Table 1 shows Inception scores, FID scores, and negative log likelihoods (lossless codelengths) on CIFAR10. | p. 5 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Still, while our lossless codelengths are better than the large estimates reported for energy based models and score matching using annealed importance sampling [11], ... | p. 6 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Larger t results in coarser and more varied interpolations, with novel samples at t = 1000 (Appendix Fig. | p. 8 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 3: FID scores for LSUN 256 × 256 datasets | p. 13 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / 4 Experiments - extractive body cue:** Our FID score is computed with respect to the training set, as is standard practice; when we compute it with respect to the test set, ...
- **p. 7 / 4 Experiments - extractive body cue:** (A stochastic reconstruction x0 ∼pθ(x0/xt) is also valid, but we do not consider it here because it makes distortion more difficult to evaluate.) Figure 5 ...
- **p. 7 / 4 Experiments - extractive body cue:** 0 200 400 600 800 1,000 0 20 40 60 80 Reverse process steps (T -t) Distortion (RMSE) 0 200 400 600 800 1,000 0 ...
- **p. 6 / 4 Experiments - extractive body cue:** We find that the baseline option of predicting ˜µ works well only when trained on the true variational bound instead of unweighted mean squared error, ...
- **p. 6 / 4 Experiments - extractive body cue:** 4.2 Reverse process parameterization and training objective ablation In Table 2, we show the sample quality effects of reverse process parameterizations and training objectives (Section ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Generated samples on CelebA-HQ 256 × 256 (left) and unconditional CIFAR10 (right) 34th Conference on Neural Information Processing Systems (NeurIPS 2020), Vancouver, Canada. ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: The directed graphical model considered in this work. This paper presents progress in diffusion probabilistic models [53]. A diffusion probabilistic model (which we ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1: CIFAR10 results. NLL measured in bits/dim.
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2: Unconditional CIFAR10 reverse process parameterization and training objec- tive ablation. Blank entries were unstable to train and generated poor samples with out-of- range ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: LSUN Church samples. FID=7.89
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: LSUN Bedroom samples. FID=4.90 Algorithm 3 Sending x0 1: Send xT ∼q(xT /x0) using p(xT ) 2: for t = T -1, . ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Unconditional CIFAR10 test set rate-distortion vs. time. Distortion is measured in root mean squared error on a [0, 255] scale. See Table 4 ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6: Unconditional CIFAR10 progressive generation (ˆx0 over time, from left to right). Extended samples and sample quality metrics over time in the appendix (Figs. ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Our FID score is computed with respect to the training set, as is standard practice; when we compute it with respect to the test ... | embodiment, simulator version and control stack | p. 5 (4 Experiments), p. 7 (4 Experiments) |
| Task/environment | (A stochastic reconstruction x0 ∼pθ(x0/xt) is also valid, but we do not consider it here because it makes distortion more difficult to evaluate.) Figure ... | reset, timeout, object/scene variation | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 4 (2 Background) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 4 (2 Background), p. 1 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 4.1 Sample quality Table 1 shows Inception scores, FID scores, and negative log likelihoods (lossless codelengths) on CIFAR10. | definition/direction/unit from same section | p. 5 (4 Experiments) |
| Still, while our lossless codelengths are better than the large estimates reported for energy based models and score matching using annealed importance sampling [11], ... | definition/direction/unit from same section | p. 6 (4 Experiments) |
| Treating the variational bound terms L1 +· · ·+LT as rate and L0 as distortion, our CIFAR10 model with the highest quality samples has ... | definition/direction/unit from same section | p. 6 (4 Experiments) |
| At each time t, the distortion is calculated as the root mean squared error p ∥x0 -ˆx0∥2/D, and the rate is calculated as the ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| With our FID score of 3.17, our unconditional model achieves better sample quality than most models in the literature, including class conditional models. | definition/direction/unit from same section | p. 5 (4 Experiments) |
| Figure 5: Unconditional CIFAR10 test set rate-distortion vs. time. Distortion is measured in root mean squared error on a [0, 255] scale. See Table ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 3: FID scores for LSUN 256 × 256 datasets | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| Figure 1: Generated samples on CelebA-HQ 256 × 256 (left) and unconditional CIFAR10 (right) 34th Conference on Neural Information Processing Systems (NeurIPS 2020), Vancouver, ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Prior work has shown that such reorderings introduce inductive biases that have an impact on sample quality [38], so we speculate that the Gaussian ... | comparison identity and matched condition | p. 8 (4 Experiments) |
| We find that the baseline option of predicting ˜µ works well only when trained on the true variational bound instead of unweighted mean squared ... | comparison identity and matched condition | p. 6 (4 Experiments) |
| We also see that learning reverse process variances (by incorporating a parameterized diagonal Σθ(xt) into the variational bound) leads to unstable training and poorer ... | comparison identity and matched condition | p. 6 (4 Experiments) |
| Figure 8: Interpolations of CelebA-HQ 256x256 images with 500 timesteps of diffusion. be a fully expressive conditional distribution. With these choices, DKL(q(xT ) ∥p(xT ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Table 2: Unconditional CIFAR10 reverse process parameterization and training objec- tive ablation. Blank entries were unstable to train and generated poor samples with out-of- ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 4.2 Reverse process parameterization and training objective ablation In Table 2, we show the sample quality effects of reverse process parameterizations and training objectives ... | component/input/data sensitivity | p. 6 (4 Experiments) |
| In effect, we use the reverse process to remove artifacts from linearly interpolating corrupted versions of the source images, as depicted in Fig. | component/input/data sensitivity | p. 8 (4 Experiments) |
| Table 2: Unconditional CIFAR10 reverse process parameterization and training objec- tive ablation. Blank entries were unstable to train and generated poor samples with out-of- ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present a more refined analysis of this phenomenon in the language of lossy compression, and we show that the sampling procedure of diffusion ... | With our FID score of 3.17, our unconditional model achieves better sample quality than most models in the literature, including class conditional models. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (4 Experiments), p. 5 (4 Experiments), p. 6 (4 Experiments), p. 8 (4 Experiments), p. 13 (Figure/Table caption) |
| Primary metric/result | 4.1 Sample quality Table 1 shows Inception scores, FID scores, and negative log likelihoods (lossless codelengths) on CIFAR10. | numeric claim only at cited anchor | p. 5 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 5 / 4 Experiments - extractive body cue:** 4.1 Sample quality Table 1 shows Inception scores, FID scores, and negative log likelihoods (lossless codelengths) on CIFAR10.
- **p. 6 / 4 Experiments - extractive body cue:** 1 for CIFAR10 and CelebA-HQ 256 × 256 samples, Fig.
- **p. 6 / 4 Experiments - extractive body cue:** 4 for LSUN 256 × 256 samples [71], and Appendix D for more.
- **p. 4 / 2 Background - extractive body cue:** To obtain discrete log likelihoods, we set the last term of the reverse process to an independent discrete decoder derived from the Gaussian N(x0; µθ(x1, ...
- **p. 5 / 2 Background - extractive body cue:** Model IS FID NLL Test (Train) Conditional EBM [11] 8.30 37.9 JEM [17] 8.76 38.4 BigGAN [3] 9.22 14.73 StyleGAN2 + ADA (v1) [29] 10.06 ...
- **p. 5 / 2 Background - extractive body cue:** Objective IS FID ˜µ prediction (baseline) L, learned diagonal Σ 7.28±0.10 23.69 L, fixed isotropic Σ 8.06±0.09 13.22 ∥˜µ -˜µθ∥2 - - ϵ prediction (ours) ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Blank entries were unstable to train and generated poor samples with out-ofrange scores. | p. 5 (2 Background) |
| body limitation/failure cue | We also see that learning reverse process variances (by incorporating a parameterized diagonal Σθ(xt) into the variational bound) leads to unstable training and poorer ... | p. 6 (4 Experiments) |
| body limitation/failure cue | We can therefore interpret the Gaussian diffusion model (2) as a kind of autoregressive model with a generalized bit ordering that cannot be expressed ... | p. 8 (4 Experiments) |
| body limitation/failure cue | (It would be straightforward to instead incorporate a more powerful decoder like a conditional autoregressive model, but we leave that to future work.) Similar ... | p. 4 (2 Background) |
| body limitation/failure cue | (LT does not appear because the forward process variances βt are fixed.) Algorithm 1 displays the complete training procedure with this simplified objective. | p. 5 (2 Background) |
| body limitation/failure cue | Figure 2: The directed graphical model considered in this work. This paper presents progress in diffusion probabilistic models [53]. A diffusion probabilistic model (which ... | p. 2 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 4.1 Sample quality Table 1 shows Inception scores, FID scores, and negative log likelihoods (lossless codelengths) on CIFAR10. | p. 5 (4 Experiments) |
| Our FID score is computed with respect to the training set, as is standard practice; when we compute it with respect to the test ... | p. 5 (4 Experiments) |
| More than half of the lossless codelength describes imperceptible distortions. | p. 6 (4 Experiments) |
| 4.3 Progressive coding Table 1 also shows the codelengths of our CIFAR10 models. | p. 6 (4 Experiments) |
| Progressive generation We also run a progressive unconditional generation process given by progressive decompression from random bits. | p. 7 (4 Experiments) |
| 0 200 400 600 800 1,000 0 20 40 60 80 Reverse process steps (T -t) Distortion (RMSE) 0 200 400 600 800 1,000 ... | p. 7 (4 Experiments) |
| 4.4 Interpolation We can interpolate source images x0, x′ 0 ∼q(x0) in latent space using q as a stochastic encoder, xt, x′ t ∼q(xt/x0), ... | p. 8 (4 Experiments) |
| 3 Diffusion models and denoising autoencoders Diffusion models might appear to be a restricted class of latent variable models, but they allow a large ... | p. 3 (2 Background) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 2 Background - extractive body cue:** Blank entries were unstable to train and generated poor samples with out-ofrange scores.
- **p. 6 / 4 Experiments - extractive body cue:** We also see that learning reverse process variances (by incorporating a parameterized diagonal Σθ(xt) into the variational bound) leads to unstable training and poorer sample ...
- **p. 8 / 4 Experiments - extractive body cue:** We can therefore interpret the Gaussian diffusion model (2) as a kind of autoregressive model with a generalized bit ordering that cannot be expressed by ...
- **p. 4 / 2 Background - extractive body cue:** (It would be straightforward to instead incorporate a more powerful decoder like a conditional autoregressive model, but we leave that to future work.) Similar to ...
- **p. 5 / 2 Background - extractive body cue:** (LT does not appear because the forward process variances βt are fixed.) Algorithm 1 displays the complete training procedure with this simplified objective.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: The directed graphical model considered in this work. This paper presents progress in diffusion probabilistic models [53]. A diffusion probabilistic model (which we ...

- **PDF anchors reviewed:** datasets p. 5 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments), metrics p. 5 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 5 (4 Experiments), p. 7 (Figure/Table caption), baselines p. 8 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments), p. 8 (Figure/Table caption), p. 5 (Figure/Table caption), results p. 5 (4 Experiments), p. 5 (4 Experiments), p. 6 (4 Experiments), p. 8 (4 Experiments), p. 13 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
