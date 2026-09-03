# Method - Denoising Diffusion Probabilistic Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2006.11239; PDF retrieval source: https://arxiv.org/pdf/2006.11239. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (Abstract), p. 5 (2 Background), p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 4 (2 Background)): Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models and denoising score matching with Langevin dynamics, and ...

## Method Body Digest

- **p. 1 / Abstract - extractive body cue:** Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models and denoising score ...
- **p. 5 / 2 Background - extractive body cue:** Model IS FID NLL Test (Train) Conditional EBM [11] 8.30 37.9 JEM [17] 8.76 38.4 BigGAN [3] 9.22 14.73 StyleGAN2 + ADA (v1) [29] 10.06 ...
- **p. 2 / 1 Introduction - extractive body cue:** When the diffusion consists of small amounts of Gaussian noise, it is sufficient to set the sampling chain transitions to conditional Gaussians too, allowing for ...
- **p. 1 / Abstract - extractive body cue:** We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics.
- **p. 2 / 1 Introduction - extractive body cue:** In addition, we show that a certain parameterization of diffusion models reveals an equivalence with denoising score matching over multiple noise levels during training and ...
- **p. 4 / 2 Background - extractive body cue:** 3.3 Data scaling, reverse process decoder, and L0 We assume that image data consists of integers in {0, 1, . . . , 255} scaled ...
- **p. 3 / 2 Background - extractive body cue:** 3 Diffusion models and denoising autoencoders Diffusion models might appear to be a restricted class of latent variable models, but they allow a large number ...
- **p. 5 / 2 Background - extractive body cue:** In particular, our diffusion process setup in Section 4 causes the simplified objective to down-weight loss terms corresponding to small t.

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** We present a more refined analysis of this phenomenon in the language of lossy compression, and we show that the sampling procedure of diffusion models ...
- **p. 2 / 1 Introduction - extractive body cue:** When the diffusion consists of small amounts of Gaussian noise, it is sufficient to set the sampling chain transitions to conditional Gaussians too, allowing for ...
- **p. 1 / Abstract - extractive body cue:** We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics.

## Source Evidence Cues

- **p. 1 / Abstract - extractive body cue:** Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models and denoising score ...
- **p. 5 / 2 Background - extractive body cue:** Model IS FID NLL Test (Train) Conditional EBM [11] 8.30 37.9 JEM [17] 8.76 38.4 BigGAN [3] 9.22 14.73 StyleGAN2 + ADA (v1) [29] 10.06 ...
- **p. 2 / 1 Introduction - extractive body cue:** When the diffusion consists of small amounts of Gaussian noise, it is sufficient to set the sampling chain transitions to conditional Gaussians too, allowing for ...
- **p. 1 / Abstract - extractive body cue:** We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics.
- **p. 2 / 1 Introduction - extractive body cue:** In addition, we show that a certain parameterization of diffusion models reveals an equivalence with denoising score matching over multiple noise levels during training and ...
- **p. 4 / 2 Background - extractive body cue:** 3.3 Data scaling, reverse process decoder, and L0 We assume that image data consists of integers in {0, 1, . . . , 255} scaled ...
- **p. 3 / 2 Background - extractive body cue:** 3 Diffusion models and denoising autoencoders Diffusion models might appear to be a restricted class of latent variable models, but they allow a large number ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models ... | p. 1 (Abstract), p. 5 (2 Background) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | Model IS FID NLL Test (Train) Conditional EBM [11] 8.30 37.9 JEM [17] 8.76 38.4 BigGAN [3] 9.22 14.73 StyleGAN2 + ADA ... | p. 5 (2 Background), p. 2 (1 Introduction) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | When the diffusion consists of small amounts of Gaussian noise, it is sufficient to set the sampling chain transitions to conditional Gaussians ... | p. 2 (1 Introduction), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 2 Background - extractive body cue:** In particular, our diffusion process setup in Section 4 causes the simplified objective to down-weight loss terms corresponding to small t.
- **p. 1 / Abstract - extractive body cue:** Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models and denoising score ...
- **p. 2 / 1 Introduction - extractive body cue:** We present a more refined analysis of this phenomenon in the language of lossy compression, and we show that the sampling procedure of diffusion models ...
- **p. 3 / 2 Background - extractive body cue:** Efficient training is therefore possible by optimizing random terms of L with stochastic gradient descent.
- **p. 4 / 2 Background - extractive body cue:** 2 6: until converged Algorithm 2 Sampling 1: xT ∼N(0, I) 2: for t = T, . . . , 1 do 3: z ∼N(0, ...
- **p. 4 / 2 Background - extractive body cue:** (12) is equal to (one term of) the variational bound for the Langevin-like reverse process (11), we see that optimizing an objective resembling denoising score ...
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 5 (2 Background), p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (2 Background), p. 3 (2 Background).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | unconditional, CIFAR10, dataset, obtain, Inception, score, state-of-the-art, FID, ensures, neural, network, reverse, process, operates | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | unconditional, CIFAR10, dataset, obtain, Inception, score, state-of-the-art, FID, ensures, neural | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | present, more, refined, analysis, phenomenon, language, lossy, compression, sampling, procedure | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | particular, diffusion, process, setup, Section, causes, simplified, objective, down-weight, loss | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Abstract - extractive body cue:** On the unconditional CIFAR10 dataset, we obtain an Inception score of 9.46 and a state-of-the-art FID score of 3.17.
- **p. 4 / 2 Background - extractive body cue:** This ensures that the neural network reverse process operates on consistently scaled inputs starting from the standard normal prior p(xT ).
- **p. 4 / 2 Background - extractive body cue:** Since xt is available as input to the model, we may choose the parameterization µθ(xt, t) = ˜µt  xt, 1 √¯αt (xt - √ ...
- **p. 1 / Abstract - extractive body cue:** We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics.
- **p. 2 / 1 Introduction - extractive body cue:** We find that the majority of our models' lossless codelengths are consumed to describe imperceptible image details (Section 4.3).
- **p. 2 / 1 Introduction - extractive body cue:** We present a more refined analysis of this phenomenon in the language of lossy compression, and we show that the sampling procedure of diffusion models ...
- **p. 3 / 2 Background - extractive body cue:** Second, to represent the mean µθ(xt, t), we propose a specific parameterization motivated by the following analysis of Lt.
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | A notable property of the forward process is that it admits sampling xt at an arbitrary timestep t in closed form: using ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | When applied to x0 ∼q(x0), Algorithms 3 and 4 transmit xT , . . . , x0 in sequence using a total ... | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | 4.1 Sample quality Table 1 shows Inception scores, FID scores, and negative log likelihoods (lossless codelengths) on CIFAR10. | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Abstract - extractive body cue:** Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models and denoising score ...
- **p. 5 / 2 Background - extractive body cue:** Model IS FID NLL Test (Train) Conditional EBM [11] 8.30 37.9 JEM [17] 8.76 38.4 BigGAN [3] 9.22 14.73 StyleGAN2 + ADA (v1) [29] 10.06 ...
- **p. 2 / 1 Introduction - extractive body cue:** In addition, we show that a certain parameterization of diffusion models reveals an equivalence with denoising score matching over multiple noise levels during training and ...
- **p. 5 / 4 Experiments - extractive body cue:** Our FID score is computed with respect to the training set, as is standard practice; when we compute it with respect to the test set, ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** best, obtained, training, weighted, variational, bound, designed, according, novel, connection, between, diffusion, probabilistic, models, denoising, score, matching, Langevin, dynamics, naturally.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | Our FID score is computed with respect to the training set, as is standard practice; when we compute it with respect to ... | p. 5 (4 Experiments), p. 7 (4 Experiments) |
| Denoiser / vector field | Prior work has shown that such reorderings introduce inductive biases that have an impact on sample quality [38], so we speculate that ... | p. 8 (4 Experiments), p. 6 (4 Experiments) |
| Sampling / downstream interface | With our FID score of 3.17, our unconditional model achieves better sample quality than most models in the literature, including class conditional ... | p. 5 (4 Experiments), p. 5 (4 Experiments) |

## Failure and Ablation Link

- **p. 6 / 4 Experiments - extractive body cue:** 4.2 Reverse process parameterization and training objective ablation In Table 2, we show the sample quality effects of reverse process parameterizations and training objectives (Section ...
- **p. 8 / 4 Experiments - extractive body cue:** In effect, we use the reverse process to remove artifacts from linearly interpolating corrupted versions of the source images, as depicted in Fig.
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2: Unconditional CIFAR10 reverse process parameterization and training objec- tive ablation. Blank entries were unstable to train and generated poor samples with out-of- range ...
- **p. 5 / 2 Background - extractive body cue:** Blank entries were unstable to train and generated poor samples with out-ofrange scores.
- **p. 6 / 4 Experiments - extractive body cue:** We also see that learning reverse process variances (by incorporating a parameterized diagonal Σθ(xt) into the variational bound) leads to unstable training and poorer sample ...
- **p. 8 / 4 Experiments - extractive body cue:** We can therefore interpret the Gaussian diffusion model (2) as a kind of autoregressive model with a generalized bit ordering that cannot be expressed by ...
- **p. 4 / 2 Background - extractive body cue:** (It would be straightforward to instead incorporate a more powerful decoder like a conditional autoregressive model, but we leave that to future work.) Similar to ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (Abstract), p. 5 (2 Background), p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 4 (2 Background), objective p. 5 (2 Background), p. 1 (Abstract), p. 2 (1 Introduction), p. 3 (2 Background), p. 4 (2 Background), p. 4 (2 Background), temporal p. 2 (2 Background), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 4 (2 Background).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (25 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models and denoising score matching with Langevin dynamics, and ... (p. 1, Abstract).
- **Objective/update evidence:** Efficient training is therefore possible by optimizing random terms of L with stochastic gradient descent. (p. 3, 2 Background).
- **Temporal/runtime evidence:** When applied to x0 ∼q(x0), Algorithms 3 and 4 transmit xT , . . . , x0 in sequence using a total expected codelength equal to Eq. (p. 6, 4 Experiments).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
