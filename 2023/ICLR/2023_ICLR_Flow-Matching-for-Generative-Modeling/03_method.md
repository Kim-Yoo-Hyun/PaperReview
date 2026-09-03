# Method - Flow Matching for Generative Modeling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2023/poster/11309; PDF retrieval source: https://openreview.net/pdf?id=PqvMRDCJT9t. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 4 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 1 (1 INTRODUCTION)): Preprint In particular, we propose the Flow Matching objective (Section 3), a simple and intuitive training objective to regress onto a target vector field that generates a desired probability path.

## Method Body Digest

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Preprint In particular, we propose the Flow Matching objective (Section 3), a simple and intuitive training objective to regress onto a target vector field that ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Then, inspired by denoising score matching, we show that a per-example training objective, termed Conditional Flow Matching (CFM), provides equivalent gradients and does not require ...
- **p. 1 / ABSTRACT - extractive body cue:** We introduce a new paradigm for generative modeling built on Continuous Normalizing Flows (CNFs), allowing us to train CNFs at unprecedented scale.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Instead, we propose a simpler objective, which surprisingly will result in the same optima as the original objective.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our first key observation is this: The marginal vector field (equation 8) generates the marginal probability path (equation 6).
- **p. 1 / 1 INTRODUCTION - extractive body cue:** (2022), is mostly facilitated by the scalable and relatively stable training of diffusion-based models Ho et al.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Upon reaching zero loss, the learned CNF model will generate pt(x).
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Our second key observation is therefore: The FM (equation 5) and CFM (equation 9) objectives have identical gradients w.r.t. θ.

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Preprint In particular, we propose the Flow Matching objective (Section 3), a simple and intuitive training objective to regress onto a target vector field that ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Instead, we propose a simpler objective, which surprisingly will result in the same optima as the original objective.
- **p. 1 / ABSTRACT - extractive body cue:** We introduce a new paradigm for generative modeling built on Continuous Normalizing Flows (CNFs), allowing us to train CNFs at unprecedented scale.

## Source Evidence Cues

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Preprint In particular, we propose the Flow Matching objective (Section 3), a simple and intuitive training objective to regress onto a target vector field that ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Then, inspired by denoising score matching, we show that a per-example training objective, termed Conditional Flow Matching (CFM), provides equivalent gradients and does not require ...
- **p. 1 / ABSTRACT - extractive body cue:** We introduce a new paradigm for generative modeling built on Continuous Normalizing Flows (CNFs), allowing us to train CNFs at unprecedented scale.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Instead, we propose a simpler objective, which surprisingly will result in the same optima as the original objective.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our first key observation is this: The marginal vector field (equation 8) generates the marginal probability path (equation 6).
- **p. 1 / 1 INTRODUCTION - extractive body cue:** (2022), is mostly facilitated by the scalable and relatively stable training of diffusion-based models Ho et al.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Upon reaching zero loss, the learned CNF model will generate pt(x).
- **Detected method headings:** C COMPUTING PROBABILITIES OF THE CNF MODEL (p. 15)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | Preprint In particular, we propose the Flow Matching objective (Section 3), a simple and intuitive training objective to regress onto a target ... | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | Then, inspired by denoising score matching, we show that a per-example training objective, termed Conditional Flow Matching (CFM), provides equivalent gradients and ... | p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | We introduce a new paradigm for generative modeling built on Continuous Normalizing Flows (CNFs), allowing us to train CNFs at unprecedented scale. | p. 1 (ABSTRACT), p. 4 (1 INTRODUCTION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 1 INTRODUCTION - extractive body cue:** Our second key observation is therefore: The FM (equation 5) and CFM (equation 9) objectives have identical gradients w.r.t. θ.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Preprint 3.2 CONDITIONAL FLOW MATCHING Unfortunately, due to the intractable integrals in the definitions of the marginal probability path and VF (equations 6 and 8), ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Then, inspired by denoising score matching, we show that a per-example training objective, termed Conditional Flow Matching (CFM), provides equivalent gradients and does not require ...
- **p. 6 / 1 INTRODUCTION - extractive body cue:** The conditional flow that corresponds to ut(x/x1) is ψt(x) = (1 -(1 -σmin)t)x + tx1, (22) and in this case, the CFM loss (see equations ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** (4) A vector field vt is said to generate a probability density path pt if its flow φt satisfies equation 3.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our first key observation is this: The marginal vector field (equation 8) generates the marginal probability path (equation 6).
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 4 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 6 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | first, observation, marginal, vector, field, equation, generates, probability, path, second, therefore, CFM, objectives, have | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | first, observation, marginal, vector, field, equation, generates, probability, path, second | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | Preprint, particular, Flow, Matching, objective, Section, simple, intuitive, training, regress | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | second, observation, therefore, equation, CFM, objectives, have, identical, gradients, Preprint | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our first key observation is this: The marginal vector field (equation 8) generates the marginal probability path (equation 6).
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Our second key observation is therefore: The FM (equation 5) and CFM (equation 9) objectives have identical gradients w.r.t. θ.
- **p. 5 / 1 INTRODUCTION - extractive body cue:** Another important observation is that, as these probability paths were previously derived as solutions of diffusion processes, they do not actually reach a true noise ...
- **p. 6 / 1 INTRODUCTION - extractive body cue:** An interesting observation is that the OT VF has a constant direction in time, which arguably leads to a simpler regression task.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The goal of this work is to propose Flow Matching (FM), an efficient simulation-free approach to training CNF models, allowing the adoption of general probability ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The recent influx of amazing advances in generative modeling, e.g., for image generation Ramesh et al.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We empirically validate Flow Matching and the construction via Optimal Transport paths on ImageNet, a large and highly diverse image dataset.
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | We next switch to fixed-step solvers and compare low (≤100) NFE samples computed with the ImageNet-32 models from Table 1. | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | In this work we consider the general and deterministic framework of Continuous Normalizing Flows (CNFs; Chen et al. | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Preprint In particular, we propose the Flow Matching objective (Section 3), a simple and intuitive training objective to regress onto a target vector field that ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Then, inspired by denoising score matching, we show that a per-example training objective, termed Conditional Flow Matching (CFM), provides equivalent gradients and does not require ...
- **p. 1 / ABSTRACT - extractive body cue:** We introduce a new paradigm for generative modeling built on Continuous Normalizing Flows (CNFs), allowing us to train CNFs at unprecedented scale.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** (2022), is mostly facilitated by the scalable and relatively stable training of diffusion-based models Ho et al.
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** For ImageNet-128 Dhariwal & Nichol (2021) train for 4.36m iterations with batch size 256, while FM (with 25% larger model) used 500k iterations with batch ...
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** All models are trained using the same architecture, hyperparameter values and number of training iterations, where baselines are allowed more iterations for better convergence.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Preprint, particular, Flow, Matching, objective, Section, simple, intuitive, training, regress, onto, target, vector, field, generates, desired, probability, path, Then, inspired.
- **Relevant PDF headings:** C COMPUTING PROBABILITIES OF THE CNF MODEL (p. 15).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | We explore the empirical benefits of using Flow Matching on the image datasets of CIFAR10 (Krizhevsky et al., 2009) and ImageNet at ... | p. 7 (6 EXPERIMENTS), p. 7 (6 EXPERIMENTS) |
| Denoiser / vector field | When compared to our ablation models, we find that models trained using Flow Matching with the OT path always result in the ... | p. 9 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS) |
| Sampling / downstream interface | We discuss how sample generation is improved by directly parameterizing the generating vector field and using the Flow Matching objective. | p. 7 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 8 / 6 EXPERIMENTS - extractive body cue:** The OT path reduces noise roughly linearly, while diffusion paths visibly remove noise only towards the end of the path.
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** Preprint CIFAR-10 ImageNet 32×32 ImageNet 64×64 Model NLL↓ FID↓ NFE↓ NLL↓ FID↓ NFE↓ NLL↓ FID↓ NFE↓ Ablations DDPM 3.12 7.48 274 3.54 6.99 262 3.32 ...
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** When compared to our ablation models, we find that models trained using Flow Matching with the OT path always result in the most efficient sampler, ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 7: Flow Matching, especially when using OT paths, allows us to use fewer evaluations for sampling while retaining similar numerical error (left) and sample ...
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** The OT path reduces noise roughly linearly, while diffusion paths visibly remove noise only towards the end of the path.
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** Score Matching w/ Diffusion Flow Matching w/ Diffusion Flow Matching w/ OT Figure 6: Sample paths from the same initial noise with models trained on ...
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** In Figure 7 (left), we compare the per-pixel MSE of low NFE solutions compared with 1000 NFE solutions (we use 256 random noise seeds), and ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 4 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), objective p. 4 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 6 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), temporal p. 9 (6 EXPERIMENTS), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 7 (5 RELATED WORK), p. 7 (5 RELATED WORK), p. 9 (7 CONCLUSION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (28 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Preprint In particular, we propose the Flow Matching objective (Section 3), a simple and intuitive training objective to regress onto a target vector field that generates a desired probability path. (p. 2, 1 INTRODUCTION).
- **Objective/update evidence:** Our second key observation is therefore: The FM (equation 5) and CFM (equation 9) objectives have identical gradients w.r.t. θ. (p. 4, 1 INTRODUCTION).
- **Temporal/runtime evidence:** Generated samples can be found in the Appendix, and all implementation details are in Appendix E. (p. 7, 6 EXPERIMENTS).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
