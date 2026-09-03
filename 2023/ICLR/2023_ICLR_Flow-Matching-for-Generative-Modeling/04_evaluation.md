# Evaluation - Flow Matching for Generative Modeling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2023/poster/11309; PDF retrieval source: https://openreview.net/pdf?id=PqvMRDCJT9t. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 1 (Figure/Table caption)): We discuss how sample generation is improved by directly parameterizing the generating vector field and using the Flow Matching objective.

## Evaluation Body Digest

- **p. 7 / 6 EXPERIMENTS - extractive body cue:** We explore the empirical benefits of using Flow Matching on the image datasets of CIFAR10 (Krizhevsky et al., 2009) and ImageNet at resolutions 32, 64, ...
- **p. 7 / 6 EXPERIMENTS - extractive body cue:** We discuss how sample generation is improved by directly parameterizing the generating vector field and using the Flow Matching objective.
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** We follow the evaluation procedure in (Saharia et al., 2022) and compute the FID of the upsampled validation images; baselines include reference (FID of original ...
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** 6.3 CONDITIONAL SAMPLING FROM LOW-RESOLUTION IMAGES Model FID↓ IS↑PSNR↑ SSIM↑ Reference 1.9 240.8 - - Regression 15.2 121.1 27.9 0.801 SR3 (Saharia et al., 2022) ...
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** Preprint 20 40 60 80 100 NFE 10 2 10 1 Error SM-Dif FM-Dif FM-OT 0 20 40 60 80 100 NFE 10 20 30 ...
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** 6.1 DENSITY MODELING AND SAMPLE QUALITY ON IMAGENET We start by comparing the same model architecture, i.e., the U-Net architecture from Dhariwal & Nichol (2021) ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 9: Trajectories of CNFs trained with ScoreFlow (Song et al., 2021) and DDPM (Ho et al., 2020) losses on 2D checkerboard data, using the ...
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** Score Matching w/ Diffusion Flow Matching w/ Diffusion Flow Matching w/ OT Figure 6: Sample paths from the same initial noise with models trained on ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 6 EXPERIMENTS (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 6 EXPERIMENTS | EMPIRICAL / SIMULATION | We discuss how sample generation is improved by directly parameterizing the generating vector field and using the Flow Matching objective. | p. 7 (6 EXPERIMENTS) |
| 6 EXPERIMENTS | EMPIRICAL / SIMULATION | FM-OT achieves similar PSNR and SSIM values to (Saharia et al., 2022) while considerably improving on FID and IS, which as argued by (Saharia ... | p. 9 (6 EXPERIMENTS) |
| 6 EXPERIMENTS | EMPIRICAL / SIMULATION | Secondly, Figure 7 (right) shows how FID changes as a result of the computational cost, where we find FM with OT is able to ... | p. 9 (6 EXPERIMENTS) |
| 6 EXPERIMENTS | EMPIRICAL / SIMULATION | On both CIFAR-10 and ImageNet, FM-OT consistently obtains best results across all our quantitative measures compared to competing methods. | p. 8 (6 EXPERIMENTS) |
| 6 EXPERIMENTS | EMPIRICAL / SIMULATION | Score Matching w/ Diffusion Flow Matching w/ Diffusion Flow Matching w/ OT Figure 6: Sample paths from the same initial noise with models trained ... | p. 8 (6 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 7 / 6 EXPERIMENTS - extractive body cue:** We explore the empirical benefits of using Flow Matching on the image datasets of CIFAR10 (Krizhevsky et al., 2009) and ImageNet at resolutions 32, 64, ...
- **p. 7 / 6 EXPERIMENTS - extractive body cue:** We discuss how sample generation is improved by directly parameterizing the generating vector field and using the Flow Matching objective.
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** We follow the evaluation procedure in (Saharia et al., 2022) and compute the FID of the upsampled validation images; baselines include reference (FID of original ...
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** 6.3 CONDITIONAL SAMPLING FROM LOW-RESOLUTION IMAGES Model FID↓ IS↑PSNR↑ SSIM↑ Reference 1.9 240.8 - - Regression 15.2 121.1 27.9 0.801 SR3 (Saharia et al., 2022) ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Unconditional ImageNet-128 sam- ples of a CNF trained using Flow Matching with Optimal Transport probability paths. and are in particular known to encompass ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2: Compared to the diffusion path's conditional score function, the OT path's conditional vector field has constant direction in time and is arguably simpler ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Diffusion and OT trajectories. Intuitively, particles under the OT displacement map always move in straight line trajectories and with constant speed. Figure 3 ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: (left) Trajectories of CNFs trained with different objectives on 2D checkerboard data. The OT path introduces the checkerboard pattern much earlier, while FM ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Likelihood (BPD), quality of generated samples (FID), and evaluation time (NFE) for the same model trained with different methods. Score Matching w/ Diffusion ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Sample paths from the same initial noise with models trained on ImageNet 64×64. The OT path reduces noise roughly linearly, while diffusion paths ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Image quality during training, ImageNet 64×64. Faster training. While existing works train diffusion models with a very high number of iterations (e.g., 1.3m ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 7: Flow Matching, especially when using OT paths, allows us to use fewer evaluations for sampling while retaining similar numerical error (left) and sample ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We explore the empirical benefits of using Flow Matching on the image datasets of CIFAR10 (Krizhevsky et al., 2009) and ImageNet at resolutions 32, ... | embodiment, simulator version and control stack | p. 7 (6 EXPERIMENTS), p. 7 (6 EXPERIMENTS) |
| Task/environment | We discuss how sample generation is improved by directly parameterizing the generating vector field and using the Flow Matching objective. | reset, timeout, object/scene variation | p. 7 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 5 (1 INTRODUCTION), p. 6 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Preprint 20 40 60 80 100 NFE 10 2 10 1 Error SM-Dif FM-Dif FM-OT 0 20 40 60 80 100 NFE 10 20 ... | definition/direction/unit from same section | p. 9 (6 EXPERIMENTS) |
| 6.1 DENSITY MODELING AND SAMPLE QUALITY ON IMAGENET We start by comparing the same model architecture, i.e., the U-Net architecture from Dhariwal & Nichol ... | definition/direction/unit from same section | p. 8 (6 EXPERIMENTS) |
| Figure 9: Trajectories of CNFs trained with ScoreFlow (Song et al., 2021) and DDPM (Ho et al., 2020) losses on 2D checkerboard data, using ... | definition/direction/unit from same section | p. 19 (Figure/Table caption) |
| Score Matching w/ Diffusion Flow Matching w/ Diffusion Flow Matching w/ OT Figure 6: Sample paths from the same initial noise with models trained ... | definition/direction/unit from same section | p. 8 (6 EXPERIMENTS) |
| In part, this is due to ODE solvers being much more efficient-yielding lower error at similar computational costs (Kloeden et al., 2012)-and the multitude ... | definition/direction/unit from same section | p. 9 (6 EXPERIMENTS) |
| Figure 2: Compared to the diffusion path's conditional score function, the OT path's conditional vector field has constant direction in time and is arguably ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Figure 1: Unconditional ImageNet-128 sam- ples of a CNF trained using Flow Matching with Optimal Transport probability paths. and are in particular known to ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 8: VP Diffusion path's conditional vector field. Compare to Figure 2. ScoreFlow DDPM | definition/direction/unit from same section | p. 19 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| When compared to our ablation models, we find that models trained using Flow Matching with the OT path always result in the most efficient ... | comparison identity and matched condition | p. 9 (6 EXPERIMENTS) |
| On both CIFAR-10 and ImageNet, FM-OT consistently obtains best results across all our quantitative measures compared to competing methods. | comparison identity and matched condition | p. 8 (6 EXPERIMENTS) |
| All models are trained using the same architecture, hyperparameter values and number of training iterations, where baselines are allowed more iterations for better convergence. | comparison identity and matched condition | p. 8 (6 EXPERIMENTS) |
| We follow the evaluation procedure in (Saharia et al., 2022) and compute the FID of the upsampled validation images; baselines include reference (FID of ... | comparison identity and matched condition | p. 9 (6 EXPERIMENTS) |
| Figure 2: Compared to the diffusion path's conditional score function, the OT path's conditional vector field has constant direction in time and is arguably ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The OT path reduces noise roughly linearly, while diffusion paths visibly remove noise only towards the end of the path. | component/input/data sensitivity | p. 8 (6 EXPERIMENTS) |
| Preprint CIFAR-10 ImageNet 32×32 ImageNet 64×64 Model NLL↓ FID↓ NFE↓ NLL↓ FID↓ NFE↓ NLL↓ FID↓ NFE↓ Ablations DDPM 3.12 7.48 274 3.54 6.99 262 ... | component/input/data sensitivity | p. 8 (6 EXPERIMENTS) |
| When compared to our ablation models, we find that models trained using Flow Matching with the OT path always result in the most efficient ... | component/input/data sensitivity | p. 9 (6 EXPERIMENTS) |
| Figure 7: Flow Matching, especially when using OT paths, allows us to use fewer evaluations for sampling while retaining similar numerical error (left) and ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Preprint In particular, we propose the Flow Matching objective (Section 3), a simple and intuitive training objective to regress onto a target vector field ... | We discuss how sample generation is improved by directly parameterizing the generating vector field and using the Flow Matching objective. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 1 (Figure/Table caption) |
| Primary metric/result | FM-OT achieves similar PSNR and SSIM values to (Saharia et al., 2022) while considerably improving on FID and IS, which as argued by (Saharia ... | numeric claim only at cited anchor | p. 9 (6 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** Preprint CIFAR-10 ImageNet 32×32 ImageNet 64×64 Model NLL↓ FID↓ NFE↓ NLL↓ FID↓ NFE↓ NLL↓ FID↓ NFE↓ Ablations DDPM 3.12 7.48 274 3.54 6.99 262 3.32 ...
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** Score Matching w/ Diffusion Flow Matching w/ Diffusion Flow Matching w/ OT Figure 6: Sample paths from the same initial noise with models trained on ...
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** Secondly, Table 1 (right) compares a model trained using Flow Matching with the OT path on ImageNet at resolution 128×128.
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** Results are shown for models trained on ImageNet 32×32, and numerical errors are for the midpoint scheme. models can also be sampled through an SDE ...
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** In particular, upsampling images from 64×64 to 256×256.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** CNFs are capable of modeling arbitrary probability path Figure 1: Unconditional ImageNet-128 samples of a CNF trained using Flow Matching with Optimal Transport probability paths. ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The OT path reduces noise roughly linearly, while diffusion paths visibly remove noise only towards the end of the path. | p. 8 (6 EXPERIMENTS) |
| body limitation/failure cue | Score Matching w/ Diffusion Flow Matching w/ Diffusion Flow Matching w/ OT Figure 6: Sample paths from the same initial noise with models trained ... | p. 8 (6 EXPERIMENTS) |
| body limitation/failure cue | In Figure 7 (left), we compare the per-pixel MSE of low NFE solutions compared with 1000 NFE solutions (we use 256 random noise seeds), ... | p. 9 (6 EXPERIMENTS) |
| body limitation/failure cue | Figure 16: Generated samples from the same initial noise, but with varying number of function evaluations (NFE). Flow matching with OT path trained on ... | p. 27 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For ImageNet-128 Dhariwal & Nichol (2021) train for 4.36m iterations with batch size 256, while FM (with 25% larger model) used 500k iterations with ... | p. 8 (6 EXPERIMENTS) |
| Generated samples can be found in the Appendix, and all implementation details are in Appendix E. | p. 7 (6 EXPERIMENTS) |
| All models are trained using the same architecture, hyperparameter values and number of training iterations, where baselines are allowed more iterations for better convergence. | p. 8 (6 EXPERIMENTS) |
| We next switch to fixed-step solvers and compare low (≤100) NFE samples computed with the ImageNet-32 models from Table 1. | p. 9 (6 EXPERIMENTS) |
| We follow the evaluation procedure in (Saharia et al., 2022) and compute the FID of the upsampled validation images; baselines include reference (FID of ... | p. 9 (6 EXPERIMENTS) |
| However, the restriction to simple diffusion processes leads to a rather confined space of sampling probability paths, resulting in very long training times and ... | p. 1 (1 INTRODUCTION) |
| Importantly, FM breaks the barriers for scalable CNF training beyond diffusion, and sidesteps the need to reason about diffusion processes to directly work with ... | p. 1 (1 INTRODUCTION) |
| We recap more information on CNFs, in particular how to compute the probability p1(x) at an arbitrary point x ∈Rd in Appendix C. | p. 2 (1 INTRODUCTION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6 EXPERIMENTS - extractive body cue:** The OT path reduces noise roughly linearly, while diffusion paths visibly remove noise only towards the end of the path.
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** Score Matching w/ Diffusion Flow Matching w/ Diffusion Flow Matching w/ OT Figure 6: Sample paths from the same initial noise with models trained on ...
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** In Figure 7 (left), we compare the per-pixel MSE of low NFE solutions compared with 1000 NFE solutions (we use 256 random noise seeds), and ...
- **p. 27 / Figure/Table caption - extractive body cue:** Figure 16: Generated samples from the same initial noise, but with varying number of function evaluations (NFE). Flow matching with OT path trained on ImageNet-128. ...

- **Evidence anchors reviewed:** datasets p. 7 (6 EXPERIMENTS), p. 7 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), metrics p. 9 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 19 (Figure/Table caption), p. 8 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 6 (Figure/Table caption), baselines p. 9 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 6 (Figure/Table caption), results p. 7 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (28 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 7: Flow Matching, especially when using OT paths, allows us to use fewer evaluations for sampling while retaining similar numerical error (left) and sample quality (right). Results are shown ... (p. 9, Figure/Table caption).
- **Metric evidence:** Preprint 20 40 60 80 100 NFE 10 2 10 1 Error SM-Dif FM-Dif FM-OT 0 20 40 60 80 100 NFE 10 20 30 40 50 FID Euler Midpoint ... (p. 9, 6 EXPERIMENTS).
- **Baseline/ablation evidence:** When compared to our ablation models, we find that models trained using Flow Matching with the OT path always result in the most efficient sampler, regardless of ODE solver, as ... (p. 9, 6 EXPERIMENTS).
- **Failure/negative evidence:** Another important observation is that, as these probability paths were previously derived as solutions of diffusion processes, they do not actually reach a true noise distribution in finite time. (p. 5, 1 INTRODUCTION).
