# Problem - High-Resolution Image Synthesis with Latent Diffusion Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (45 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2112.10752; PDF retrieval source: https://arxiv.org/pdf/2112.10752. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction)): (iii) We show that, in contrast to previous work [93] which learns both an encoder/decoder architecture and a score-based prior simultaneously, our approach does not require a delicate weighting of ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** By decomposing the image formation process into a sequential application of denoising autoencoders, diffusion models (DMs) achieve state-of-the-art synthesis results on image data and beyond.
- **p. 1 / Abstract - extractive PDF cue:** Additionally, their formulation allows for a guiding mechanism to control the image generation process without retraining.
- **p. 1 / Abstract - extractive PDF cue:** However, since these models typically operate directly in pixel space, optimization of powerful DMs often consumes hundreds of GPU days and inference is expensive due ...
- **p. 1 / Abstract - extractive PDF cue:** To enable DM training on limited computational resources while retaining their quality and flexibility, we apply them in the latent space of powerful pretrained autoencoders.
- **p. 1 / Abstract - extractive PDF cue:** In contrast to previous work, training diffusion models on such a representation allows for the first time to reach a near-optimal point between complexity reduction ...
- **p. 2 / 1. Introduction - extractive PDF cue:** (iii) We show that, in contrast to previous work [93] which learns both an encoder/decoder architecture and a score-based prior simultaneously, our approach does not ...
- **p. 2 / 1. Introduction - extractive PDF cue:** In sum, our work makes the following contributions: (i) In contrast to purely transformer-based approaches [23,66], our method scales more graceful to higher dimensional data ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | (iii) We show that, in contrast to previous work [93] which learns both an encoder/decoder architecture and a score-based prior simultaneously, our ... | high-dimensional data 또는 robot action-trajectory distribution | body wording is the source claim |
| Observation / input | In the context of image synthesis, however, combining the generative power of DMs with other types of conditionings beyond class-labels [15] or ... | conditioning observation와 noisy/intermediate sample | exact sensor/frame/preprocessing from PDF |
| State / latent | context, image, synthesis, however, combining, generative, power, DMs, other, types | latent/noise variable와 conditional distribution | notation and tensor shape require body check |
| Output / action | image, synthesis, beyond, define, state-of-the-art, class-conditional, super-resolution, Finally | generated sample, action chunk 또는 trajectory | exact unit/frame/decoder require body check |
| Target outcome | sample quality, diversity and latency | distribution fit, multimodality, sample quality와 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | data x₀, noisy state x_t, condition c; body terms: context, image, synthesis, however, combining, generative, power, DMs, other, types | p. 4 (3.3. Conditioning Mechanisms), p. 4 (3.3. Conditioning Mechanisms), p. 1 (1. Introduction) |
| Decision / output variable | sample/action x̂ or trajectory; body terms: makes, following, contributions, contrast, purely, transformer-based, approaches, scales | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method) |
| Objective / loss / cost | distribution/denoising/flow objective; cue terms: ensures, reconstructions, confined, image, manifold, enforcing, local, realism | p. 3 (3.1. Perceptual Image Compression), p. 3 (3.1. Perceptual Image Compression), p. 4 (3.2. Latent Diffusion Models), p. 4 (3.1. Perceptual Image Compression) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.2. Latent Diffusion Models), p. 4 (3.1. Perceptual Image Compression), p. 5 (3.3. Conditioning Mechanisms) |
| Success / guarantee | sample quality, diversity and latency | p. 6 (4.2. Image Generation with Latent Diffusion), p. 5 (4.1. On Perceptual Compression Tradeoffs), p. 5 (4.1. On Perceptual Compression Tradeoffs) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** (iii) We show that, in contrast to previous work [93] which learns both an encoder/decoder architecture and a score-based prior simultaneously, our approach does not ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method), p. 3 (3.1. Perceptual Image Compression), p. 4 (3.3. Conditioning Mechanisms)): In sum, our work makes the following contributions: (i) In contrast to purely transformer-based approaches [23,66], our method scales more graceful to higher dimensional data and can thus (a) work ...

- **p. 2 / 1. Introduction - extractive PDF cue:** We propose latent diffusion models (LDMs) as an effective generative model and a separate mild compression stage that only eliminates imperceptible details.
- **p. 3 / 3. Method - extractive PDF cue:** We propose to circumvent this drawback by introducing an explicit separation of the compressive from the generative learning phase (see Fig.
- **p. 3 / 3.1. Perceptual Image Compression - extractive PDF cue:** Our perceptual compression model is based on previous work [23] and consists of an autoencoder trained by combination of a perceptual loss [106] and a ...
- **p. 4 / 3.3. Conditioning Mechanisms - extractive PDF cue:** To pre-process y from various modalities (such as language prompts) we introduce a domain specific encoder τθ that projects y to an intermediate representation τθ(y) ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Limitations While LDMs significantly reduce computational requirements compared to pixel-based approaches, their sequential sampling process is still slower ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 23 | Figure 18. LDM-BSR generalizes to arbitrary inputs and can be used as a general-purpose upsampler, upscaling samples from ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Interestingly, we find that LDMs trained in VQregularized latent spaces sometimes achieve better sample quality, even though the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Table 4. Task 1: Subjects were shown ground truth and generated image and asked for preference. Task 2: ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

generative writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3.3. Conditioning Mechanisms), p. 4 (3.3. Conditioning Mechanisms), p. 1 (1. Introduction), p. 3 (3. Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), interface p. 4 (3.3. Conditioning Mechanisms), p. 4 (3.3. Conditioning Mechanisms), p. 1 (1. Introduction), p. 3 (3. Method), objective p. 3 (3.1. Perceptual Image Compression), p. 3 (3.1. Perceptual Image Compression), p. 4 (3.2. Latent Diffusion Models), p. 4 (3.1. Perceptual Image Compression).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
