# Evaluation - Classifier-Free Diffusion Guidance

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2207.12598; PDF retrieval source: https://arxiv.org/pdf/2207.12598. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS)): At w = 0.3, our model's FID score on 128 × 128 ImageNet outperforms the classifier-guided ADM-G, and at w = 4.0, our model outperforms BigGAN-deep at both FID and ...

## Evaluation Body Digest

- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We obtain the best FID results with a small amount of guidance (w = 0.1 or w = 0.3, depending on the dataset) and the ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Based on these findings, we conclude that only a relatively small portion of the model capacity of the diffusion model needs to be dedicated to ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: The effect of guidance on a mixture of three Gaussians, each mixture component represent- ing data conditioned on a class. The leftmost plot ...
- **p. 5 / 4 EXPERIMENTS - extractive body cue:** We train diffusion models with classifier-free guidance on area-downsampled class-conditional ImageNet (Russakovsky et al., 2015), the standard setting for studying tradeoffs between FID and Inception ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We consider w ∈{0, 0.1, 0.2, . . . , 4} and calculate FID and Inception Scores with 50000 samples for each value following the ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** At w = 0.3, our model's FID score on 128 × 128 ImageNet outperforms the classifier-guided ADM-G, and at w = 4.0, our model outperforms ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Because we used the same model architecture as ADM-G, the fair comparison in terms of sampling speed would be our T = 128 setting, which ...
- **p. 5 / 4 EXPERIMENTS - extractive body cue:** The purpose of our experiments is to serve as a proof of concept to demonstrate that classifier-free guidance is able to attain a FID/IS tradeoff ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | At w = 0.3, our model's FID score on 128 × 128 ImageNet outperforms the classifier-guided ADM-G, and at w = 4.0, our model ... | p. 7 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Nevertheless, our classifier-free guided models still produce competitive sample quality metrics and sometimes outperform prior work, as can be seen in the following sections. | p. 6 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Note that T = 256 is approximately the same number of sampling steps used by ADM-G (Dhariwal & Nichol, 2021), which is outperformed by ... | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | As expected, sample quality improves when T is increased, and for this model T = 256 attains a good balance between sample quality and ... | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | We train diffusion models with classifier-free guidance on area-downsampled class-conditional ImageNet (Russakovsky et al., 2015), the standard setting for studying tradeoffs between FID and ... | p. 5 (4 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We obtain the best FID results with a small amount of guidance (w = 0.1 or w = 0.3, depending on the dataset) and the ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Based on these findings, we conclude that only a relatively small portion of the model capacity of the diffusion model needs to be dedicated to ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Classifier-free guidance on the malamute class for a 64x64 ImageNet diffusion model. Left to right: increasing amounts of classifier-free guidance, starting from non-guided ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: The effect of guidance on a mixture of three Gaussians, each mixture component represent- ing data conditioned on a class. The leftmost plot ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Classifier-free guidance on 128x128 ImageNet. Left: non-guided samples, right: classifier- free guided samples with w = 3.0. Interestingly, strongly guided samples such as ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: ImageNet 64x64 results (w = 0.0 refers to non-guided models). 50 100 150 200 250 0 10
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: IS/FID curves over guidance strengths for ImageNet 64x64 models. Each curve represents a model with unconditional training probability puncond. Accompanies Table 1. 7
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: ImageNet 128x128 results (w = 0.0 refers to non-guided models). 8
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: IS/FID curves over guidance strengths for ImageNet 128x128 models. Each curve represents sampling with a different number of timesteps T. Accompanies Table 2. ...
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 6: Classifier-free guidance on ImageNet 64x64. Left: random classes. Right: single class (malamute). The same random seed was used for sampling in each subfigure. ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We obtain the best FID results with a small amount of guidance (w = 0.1 or w = 0.3, depending on the dataset) and ... | embodiment, simulator version and control stack | p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Task/environment | Based on these findings, we conclude that only a relatively small portion of the model capacity of the diffusion model needs to be dedicated ... | reset, timeout, object/scene variation | p. 8 (4 EXPERIMENTS) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 1 (1 INTRODUCTION), p. 4 (2 BACKGROUND) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 3 (2 BACKGROUND), p. 3 (2 BACKGROUND) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 2: The effect of guidance on a mixture of three Gaussians, each mixture component represent- ing data conditioned on a class. The leftmost ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| We train diffusion models with classifier-free guidance on area-downsampled class-conditional ImageNet (Russakovsky et al., 2015), the standard setting for studying tradeoffs between FID and ... | definition/direction/unit from same section | p. 5 (4 EXPERIMENTS) |
| We consider w ∈{0, 0.1, 0.2, . . . , 4} and calculate FID and Inception Scores with 50000 samples for each value following ... | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| At w = 0.3, our model's FID score on 128 × 128 ImageNet outperforms the classifier-guided ADM-G, and at w = 4.0, our model ... | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| Because we used the same model architecture as ADM-G, the fair comparison in terms of sampling speed would be our T = 128 setting, ... | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| Based on these findings, we conclude that only a relatively small portion of the model capacity of the diffusion model needs to be dedicated ... | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| The purpose of our experiments is to serve as a proof of concept to demonstrate that classifier-free guidance is able to attain a FID/IS ... | definition/direction/unit from same section | p. 5 (4 EXPERIMENTS) |
| Interestingly, strongly guided samples such as these display saturated colors. | definition/direction/unit from same section | p. 6 (4 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Nevertheless, our classifier-free guided models still produce competitive sample quality metrics and sometimes outperform prior work, as can be seen in the following sections. | comparison identity and matched condition | p. 6 (4 EXPERIMENTS) |
| Because we used the same model architecture as ADM-G, the fair comparison in terms of sampling speed would be our T = 128 setting, ... | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| At w = 0.3, our model's FID score on 128 × 128 ImageNet outperforms the classifier-guided ADM-G, and at w = 4.0, our model ... | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| Note that T = 256 is approximately the same number of sampling steps used by ADM-G (Dhariwal & Nichol, 2021), which is outperformed by ... | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| Furthermore, since we amortize the conditional and unconditional models into the same architecture without an extra classifier, we in fact are using less model ... | comparison identity and matched condition | p. 6 (4 EXPERIMENTS) |
| Figure 2: The effect of guidance on a mixture of three Gaussians, each mixture component represent- ing data conditioned on a class. The leftmost ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 2: The effect of guidance on a mixture of three Gaussians, each mixture component represent- ing data conditioned on a class. The leftmost ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| Figures 1, 3 and 6 to 8 show randomly generated samples from our model for different levels of guidance: here we clearly see that ... | component/input/data sensitivity | p. 7 (4 EXPERIMENTS) |
| Here, we study the effect of training models on varying puncond on 64 × 64 ImageNet. | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| 5 show the effect of varying T ∈{128, 256, 1024} over a range of guidance strengths. | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| Furthermore, since we amortize the conditional and unconditional models into the same architecture without an extra classifier, we in fact are using less model ... | component/input/data sensitivity | p. 6 (4 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To resolve these questions, we present classifier-free guidance, our guidance method which avoids any classifier entirely. | At w = 0.3, our model's FID score on 128 × 128 ImageNet outperforms the classifier-guided ADM-G, and at w = 4.0, our model ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Primary metric/result | Nevertheless, our classifier-free guided models still produce competitive sample quality metrics and sometimes outperform prior work, as can be seen in the following sections. | numeric claim only at cited anchor | p. 6 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** We apply our proposed classifier-free guidance to 64×64 and 128×128 class-conditional ImageNet generation.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We consider w ∈{0, 0.1, 0.2, . . . , 4} and calculate FID and Inception Scores with 50000 samples for each value following the ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Therefore, our classifier-free guided sampler follows step directions that do not resemble classifier gradients at all and thus cannot be interpreted as a gradient-based ... | p. 9 (5 DISCUSSION) |
| body limitation/failure cue | It would be an interesting avenue of future work to try to boost sample quality while maintaining sample diversity. | p. 9 (5 DISCUSSION) |
| body limitation/failure cue | The 64 × 64 models used sampler noise interpolation coefficient v = 0.3 and were trained for 400 thousand steps; the 128 × 128 ... | p. 7 (4 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 4.2 VARYING THE UNCONDITIONAL TRAINING PROBABILITY The main hyperparameter of classifier-free guidance at training time is puncond, the probability of training on unconditional generation ... | p. 8 (4 EXPERIMENTS) |
| For this purpose, we use the same model architectures and hyperparameters as the guided diffusion models of Dhariwal & Nichol (2021) (apart from continuous ... | p. 6 (4 EXPERIMENTS) |
| The 64 × 64 models used sampler noise interpolation coefficient v = 0.3 and were trained for 400 thousand steps; the 128 × 128 ... | p. 7 (4 EXPERIMENTS) |
| Note that T = 256 is approximately the same number of sampling steps used by ADM-G (Dhariwal & Nichol, 2021), which is outperformed by ... | p. 8 (4 EXPERIMENTS) |
| Each curve represents sampling with a different number of timesteps T. | p. 9 (4 EXPERIMENTS) |
| These models have delivered audio synthesis performance rivaling the quality of autoregressive models with substantially fewer inference steps (Chen et al., 2021; Kong et ... | p. 1 (1 INTRODUCTION) |
| We train diffusion models in continuous time (Song et al., 2021b; Chen et al., 2021; Kingma et al., 2021): letting x ∼p(x) and z ... | p. 2 (2 BACKGROUND) |
| Note that the variances simplify to ˜σ2 λ′/λ as λ′ →λ, so v has an effect only when sampling with non-infinitesimal timesteps as done ... | p. 3 (2 BACKGROUND) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 5 DISCUSSION - extractive body cue:** Therefore, our classifier-free guided sampler follows step directions that do not resemble classifier gradients at all and thus cannot be interpreted as a gradient-based adversarial ...
- **p. 9 / 5 DISCUSSION - extractive body cue:** It would be an interesting avenue of future work to try to boost sample quality while maintaining sample diversity.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** The 64 × 64 models used sampler noise interpolation coefficient v = 0.3 and were trained for 400 thousand steps; the 128 × 128 models ...

- **Evidence anchors reviewed:** datasets p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), metrics p. 2 (Figure/Table caption), p. 5 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), baselines p. 6 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 2 (Figure/Table caption), results p. 7 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
