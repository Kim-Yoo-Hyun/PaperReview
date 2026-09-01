# Method - Classifier-Free Diffusion Guidance

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2207.12598; PDF retrieval source: https://arxiv.org/pdf/2207.12598. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND), p. 4 (2 BACKGROUND), p. 5 (2 BACKGROUND), p. 5 (2 BACKGROUND)): Because the loss for ϵθ(zλ) is denoising score matching for all λ, the score ϵθ(zλ) learned by our model estimates the gradient of the log-density of the distribution of our ...

## Method Body Digest

- **p. 3 / 2 BACKGROUND - extractive PDF cue:** Because the loss for ϵθ(zλ) is denoising score matching for all λ, the score ϵθ(zλ) learned by our model estimates the gradient of the log-density ...
- **p. 3 / 2 BACKGROUND - extractive PDF cue:** If the model xθ is correct, then as T →∞, we obtain samples from an SDE whose sample paths are distributed as p(z) (Song et ...
- **p. 4 / 2 BACKGROUND - extractive PDF cue:** We use a single neural network to parameterize both models, where for the unconditional model we can simply input a null token ∅for the class ...
- **p. 4 / 2 BACKGROUND - extractive PDF cue:** Algorithm 1 Joint training a diffusion model with classifier-free guidance Require: puncond: probability of unconditional training 1: repeat 2: (x, c) ∼p(x, c) ▷Sample data ...
- **p. 5 / 2 BACKGROUND - extractive PDF cue:** (It would certainly be possible to train separate models instead of jointly training them together, but we choose joint training because it is extremely simple ...
- **p. 5 / 2 BACKGROUND - extractive PDF cue:** The former is constructed from the scaled classifier gradient ϵ∗(zλ, c)-ϵ∗(zλ); the latter is constructed from the estimate ϵθ(zλ, c)-ϵθ(zλ), and this expression is not ...
- **p. 1 / ABSTRACT - extractive PDF cue:** Classifier guidance combines the score estimate of a diffusion model with the gradient of an image classifier and thereby requires training an image classifier separate ...
- **p. 4 / 2 BACKGROUND - extractive PDF cue:** The effect is that of up-weighting the probability of data for which the classifier pθ(c/zλ) assigns high likelihood to the correct label: data that can ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** To resolve these questions, we present classifier-free guidance, our guidance method which avoids any classifier entirely.
- **p. 1 / ABSTRACT - extractive PDF cue:** We show that guidance can be indeed performed by a pure generative model without such a classifier: in what we call classifier-free guidance, we jointly ...
- **p. 5 / 2 BACKGROUND - extractive PDF cue:** Nevertheless, in Section 4, we show empirically that classifier-free guidance is able to trade off FID and IS in the same way as classifier guidance.

## Source Evidence Cues

- **p. 3 / 2 BACKGROUND - extractive PDF cue:** Because the loss for ϵθ(zλ) is denoising score matching for all λ, the score ϵθ(zλ) learned by our model estimates the gradient of the log-density ...
- **p. 3 / 2 BACKGROUND - extractive PDF cue:** If the model xθ is correct, then as T →∞, we obtain samples from an SDE whose sample paths are distributed as p(z) (Song et ...
- **p. 4 / 2 BACKGROUND - extractive PDF cue:** We use a single neural network to parameterize both models, where for the unconditional model we can simply input a null token ∅for the class ...
- **p. 4 / 2 BACKGROUND - extractive PDF cue:** Algorithm 1 Joint training a diffusion model with classifier-free guidance Require: puncond: probability of unconditional training 1: repeat 2: (x, c) ∼p(x, c) ▷Sample data ...
- **p. 5 / 2 BACKGROUND - extractive PDF cue:** (It would certainly be possible to train separate models instead of jointly training them together, but we choose joint training because it is extremely simple ...
- **p. 5 / 2 BACKGROUND - extractive PDF cue:** The former is constructed from the scaled classifier gradient ϵ∗(zλ, c)-ϵ∗(zλ); the latter is constructed from the estimate ϵθ(zλ, c)-ϵθ(zλ), and this expression is not ...
- **p. 1 / ABSTRACT - extractive PDF cue:** Classifier guidance combines the score estimate of a diffusion model with the gradient of an image classifier and thereby requires training an image classifier separate ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | Because the loss for ϵθ(zλ) is denoising score matching for all λ, the score ϵθ(zλ) learned by our model estimates the gradient ... | p. 3 (2 BACKGROUND), p. 3 (2 BACKGROUND) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | If the model xθ is correct, then as T →∞, we obtain samples from an SDE whose sample paths are distributed as ... | p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | We use a single neural network to parameterize both models, where for the unconditional model we can simply input a null token ... | p. 4 (2 BACKGROUND), p. 4 (2 BACKGROUND) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 2 BACKGROUND - extractive PDF cue:** Algorithm 1 Joint training a diffusion model with classifier-free guidance Require: puncond: probability of unconditional training 1: repeat 2: (x, c) ∼p(x, c) ▷Sample data ...
- **p. 3 / 2 BACKGROUND - extractive PDF cue:** Because the loss for ϵθ(zλ) is denoising score matching for all λ, the score ϵθ(zλ) learned by our model estimates the gradient of the log-density ...
- **p. 4 / 2 BACKGROUND - extractive PDF cue:** The effect is that of up-weighting the probability of data for which the classifier pθ(c/zλ) assigns high likelihood to the correct label: data that can ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Classifier guidance instead mixes a diffusion model's score estimate with the input gradient of the log probability of a Figure 1: Classifier-free guidance on the ...
- **p. 3 / 2 BACKGROUND - extractive PDF cue:** This objective is denoising score matching (Vincent, 2011; Hyv¨arinen & Dayan, 2005) over multiple noise scales (Song & Ermon, 2019), and when p(λ) is uniform, ...
- **p. 1 / ABSTRACT - extractive PDF cue:** Classifier guidance combines the score estimate of a diffusion model with the gradient of an image classifier and thereby requires training an image classifier separate ...
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 3 (2 BACKGROUND), p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Classifier, guidance, instead, mixes, diffusion, model, score, estimate, input, gradient, probability, Figure, Classifier-free, malamute | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | Classifier, guidance, instead, mixes, diffusion, model, score, estimate, input, gradient | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | resolve, questions, present, classifier-free, guidance, avoids, classifier, entirely, indeed, performed | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | Algorithm, Joint, training, diffusion, model, classifier-free, guidance, Require, puncond, probability | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Classifier guidance instead mixes a diffusion model's score estimate with the input gradient of the log probability of a Figure 1: Classifier-free guidance on the ...
- **p. 4 / 2 BACKGROUND - extractive PDF cue:** 3.2 CLASSIFIER-FREE GUIDANCE While classifier guidance successfully trades off IS and FID as expected from truncation or low temperature sampling, it is nonetheless reliant on ...
- **p. 3 / 2 BACKGROUND - extractive PDF cue:** The only modification to the model is that the reverse process function approximator receives c as input, as in ϵθ(zλ, c).
- **p. 3 / 2 BACKGROUND - extractive PDF cue:** The reverse process mean comes from an estimate xθ(zλ) ≈x plugged into q(zλ′/zλ, x) (Ho et al., 2020; Kingma et al., 2021) (xθ also receives ...
- **p. 4 / 2 BACKGROUND - extractive PDF cue:** We use a single neural network to parameterize both models, where for the unconditional model we can simply input a null token ∅for the class ...
- **p. 5 / 2 BACKGROUND - extractive PDF cue:** The former is constructed from the scaled classifier gradient ϵ∗(zλ, c)-ϵ∗(zλ); the latter is constructed from the estimate ϵθ(zλ, c)-ϵθ(zλ), and this expression is not ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Dhariwal & Nichol (2021) proposed classifier guidance, a technique to boost the sample quality of a diffusion model using an extra trained classifier.
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | Each curve represents sampling with a different number of timesteps T. | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | During sampling, we apply this transition along an increasing sequence λmin = λ1 < · · · < λT = λmax for ... | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not recovered | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 2 BACKGROUND - extractive PDF cue:** Because the loss for ϵθ(zλ) is denoising score matching for all λ, the score ϵθ(zλ) learned by our model estimates the gradient of the log-density ...
- **p. 4 / 2 BACKGROUND - extractive PDF cue:** Algorithm 1 Joint training a diffusion model with classifier-free guidance Require: puncond: probability of unconditional training 1: repeat 2: (x, c) ∼p(x, c) ▷Sample data ...
- **p. 5 / 2 BACKGROUND - extractive PDF cue:** (It would certainly be possible to train separate models instead of jointly training them together, but we choose joint training because it is extremely simple ...
- **p. 5 / 2 BACKGROUND - extractive PDF cue:** The former is constructed from the scaled classifier gradient ϵ∗(zλ, c)-ϵ∗(zλ); the latter is constructed from the estimate ϵθ(zλ, c)-ϵθ(zλ), and this expression is not ...
- **p. 1 / ABSTRACT - extractive PDF cue:** Classifier guidance combines the score estimate of a diffusion model with the gradient of an image classifier and thereby requires training an image classifier separate ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** 4.2 VARYING THE UNCONDITIONAL TRAINING PROBABILITY The main hyperparameter of classifier-free guidance at training time is puncond, the probability of training on unconditional generation during ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Because, loss, denoising, score, matching, learned, model, estimates, gradient, log-density, distribution, noisy, data, note, however, unconstrained, neural, networks, define, there.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | We obtain the best FID results with a small amount of guidance (w = 0.1 or w = 0.3, depending on the ... | p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Denoiser / vector field | Nevertheless, our classifier-free guided models still produce competitive sample quality metrics and sometimes outperform prior work, as can be seen in the ... | p. 6 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Sampling / downstream interface | At w = 0.3, our model's FID score on 128 × 128 ImageNet outperforms the classifier-guided ADM-G, and at w = 4.0, ... | p. 7 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2: The effect of guidance on a mixture of three Gaussians, each mixture component represent- ing data conditioned on a class. The leftmost plot ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** Figures 1, 3 and 6 to 8 show randomly generated samples from our model for different levels of guidance: here we clearly see that increasing ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Here, we study the effect of training models on varying puncond on 64 × 64 ImageNet.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** 5 show the effect of varying T ∈{128, 256, 1024} over a range of guidance strengths.
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** Furthermore, since we amortize the conditional and unconditional models into the same architecture without an extra classifier, we in fact are using less model capacity ...
- **p. 9 / 5 DISCUSSION - extractive PDF cue:** Therefore, our classifier-free guided sampler follows step directions that do not resemble classifier gradients at all and thus cannot be interpreted as a gradient-based adversarial ...
- **p. 9 / 5 DISCUSSION - extractive PDF cue:** It would be an interesting avenue of future work to try to boost sample quality while maintaining sample diversity.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND), p. 4 (2 BACKGROUND), p. 5 (2 BACKGROUND), p. 5 (2 BACKGROUND), objective p. 4 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND), p. 1 (1 INTRODUCTION), p. 3 (2 BACKGROUND), p. 1 (ABSTRACT), temporal p. 9 (4 EXPERIMENTS), p. 3 (2 BACKGROUND), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 3 (2 BACKGROUND).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
