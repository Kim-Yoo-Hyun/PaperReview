# Method - High-Resolution Image Synthesis with Latent Diffusion Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (45 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2112.10752; PDF retrieval source: https://arxiv.org/pdf/2112.10752. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.3. Conditioning Mechanisms), p. 3 (3.1. Perceptual Image Compression), p. 4 (3.2. Latent Diffusion Models), p. 3 (3. Method), p. 5 (3.3. Conditioning Mechanisms)): To pre-process y from various modalities (such as language prompts) we introduce a domain specific encoder τθ that projects y to an intermediate representation τθ(y) ∈RM×dτ , which is then ...

## Method Body Digest

- **p. 4 / 3.3. Conditioning Mechanisms - extractive PDF cue:** To pre-process y from various modalities (such as language prompts) we introduce a domain specific encoder τθ that projects y to an intermediate representation τθ(y) ...
- **p. 3 / 3.1. Perceptual Image Compression - extractive PDF cue:** Our perceptual compression model is based on previous work [23] and consists of an autoencoder trained by combination of a perceptual loss [106] and a ...
- **p. 4 / 3.2. Latent Diffusion Models - extractive PDF cue:** Unlike previous work that relied on autoregressive, attention-based transformer models in a highly compressed, discrete latent space [23,66,103], we can take advantage of image-specific inductive ...
- **p. 3 / 3. Method - extractive PDF cue:** To lower the computational demands of training diffusion models towards high-resolution image synthesis, we observe that although diffusion models allow to ignore perceptually irrelevant details ...
- **p. 5 / 3.3. Conditioning Mechanisms - extractive PDF cue:** (unmasked) transformers [97] when y are text prompts (see Sec.
- **p. 3 / 3.1. Perceptual Image Compression - extractive PDF cue:** This ensures that the reconstructions are confined to the image manifold by enforcing local realism and avoids bluriness introduced by relying solely on pixel-space losses ...
- **p. 4 / 3.2. Latent Diffusion Models - extractive PDF cue:** The corresponding objective can be simplified to (Sec.
- **p. 4 / 3.1. Perceptual Image Compression - extractive PDF cue:** The full objective and training details can be found in the supplement.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** In sum, our work makes the following contributions: (i) In contrast to purely transformer-based approaches [23,66], our method scales more graceful to higher dimensional data ...
- **p. 2 / 1. Introduction - extractive PDF cue:** We propose latent diffusion models (LDMs) as an effective generative model and a separate mild compression stage that only eliminates imperceptible details.
- **p. 3 / 3. Method - extractive PDF cue:** We propose to circumvent this drawback by introducing an explicit separation of the compressive from the generative learning phase (see Fig.

## Source Evidence Cues

- **p. 4 / 3.3. Conditioning Mechanisms - extractive PDF cue:** To pre-process y from various modalities (such as language prompts) we introduce a domain specific encoder τθ that projects y to an intermediate representation τθ(y) ...
- **p. 3 / 3.1. Perceptual Image Compression - extractive PDF cue:** Our perceptual compression model is based on previous work [23] and consists of an autoencoder trained by combination of a perceptual loss [106] and a ...
- **p. 4 / 3.2. Latent Diffusion Models - extractive PDF cue:** Unlike previous work that relied on autoregressive, attention-based transformer models in a highly compressed, discrete latent space [23,66,103], we can take advantage of image-specific inductive ...
- **p. 3 / 3. Method - extractive PDF cue:** To lower the computational demands of training diffusion models towards high-resolution image synthesis, we observe that although diffusion models allow to ignore perceptually irrelevant details ...
- **p. 5 / 3.3. Conditioning Mechanisms - extractive PDF cue:** (unmasked) transformers [97] when y are text prompts (see Sec.
- **Detected method headings:** 3. Method (p. 3); 3.2. Latent Diffusion Models (p. 4); Method (p. 23)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | To pre-process y from various modalities (such as language prompts) we introduce a domain specific encoder τθ that projects y to an ... | p. 4 (3.3. Conditioning Mechanisms), p. 3 (3.1. Perceptual Image Compression) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | Our perceptual compression model is based on previous work [23] and consists of an autoencoder trained by combination of a perceptual loss ... | p. 3 (3.1. Perceptual Image Compression), p. 4 (3.2. Latent Diffusion Models) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | Unlike previous work that relied on autoregressive, attention-based transformer models in a highly compressed, discrete latent space [23,66,103], we can take advantage ... | p. 4 (3.2. Latent Diffusion Models), p. 3 (3. Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.1. Perceptual Image Compression - extractive PDF cue:** This ensures that the reconstructions are confined to the image manifold by enforcing local realism and avoids bluriness introduced by relying solely on pixel-space losses ...
- **p. 3 / 3.1. Perceptual Image Compression - extractive PDF cue:** Our perceptual compression model is based on previous work [23] and consists of an autoencoder trained by combination of a perceptual loss [106] and a ...
- **p. 4 / 3.2. Latent Diffusion Models - extractive PDF cue:** The corresponding objective can be simplified to (Sec.
- **p. 4 / 3.1. Perceptual Image Compression - extractive PDF cue:** The full objective and training details can be found in the supplement.
- **p. 5 / 3.3. Conditioning Mechanisms - extractive PDF cue:** Based on image-conditioning pairs, we then learn the conditional LDM via LLDM := EE(x),y,ϵ∼N(0,1),t h ∥ϵ-ϵθ(zt, t, τθ(y))∥2 2 i , (3) where both τθ ...
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 3 (3.1. Perceptual Image Compression), p. 3 (3.1. Perceptual Image Compression), p. 4 (3.2. Latent Diffusion Models), p. 4 (3.1. Perceptual Image Compression).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | context, image, synthesis, however, combining, generative, power, DMs, other, types, conditionings, beyond, class-labels, blurred | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | context, image, synthesis, however, combining, generative, power, DMs, other, types | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | makes, following, contributions, contrast, purely, transformer-based, approaches, scales, more, graceful | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | ensures, reconstructions, confined, image, manifold, enforcing, local, realism, avoids, bluriness | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.3. Conditioning Mechanisms - extractive PDF cue:** In the context of image synthesis, however, combining the generative power of DMs with other types of conditionings beyond class-labels [15] or blurred variants of ...
- **p. 4 / 3.3. Conditioning Mechanisms - extractive PDF cue:** We turn DMs into more flexible conditional image generators by augmenting their underlying UNet backbone with the cross-attention mechanism [97], which is effective for learning ...
- **p. 1 / 1. Introduction - extractive PDF cue:** 8. results in image synthesis [30,85] and beyond [7,45,48,57], and define the state-of-the-art in class-conditional image synthesis [15,31] and super-resolution [72].
- **p. 3 / 3. Method - extractive PDF cue:** (iii) Finally, we obtain general-purpose compression models whose latent space can be used to train multiple generative models and which can also be utilized for ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Input ours (f = 4) PSNR: 27.4 R-FID: 0.58 DALL-E (f = 8) PSNR: 22.8 R-FID: 32.01 VQGAN (f = 16) PSNR: 19.9 R-FID: 4.98 ...
- **p. 2 / 1. Introduction - extractive PDF cue:** This has two consequences for the research community and users in general: Firstly, training such a model requires massive computational resources only available to a ...
- **p. 3 / 3.1. Perceptual Image Compression - extractive PDF cue:** More precisely, given an image x ∈RH×W ×3 in RGB space, the encoder E encodes x into a latent representa3
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | Secondly, evaluating an already trained model is also expensive in time and memory, since the same model architecture must run sequentially for ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | These models can be interpreted as an equally weighted sequence of denoising autoencoders ϵθ(xt, t); t = 1 . . . | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | Secondly, evaluating an already trained model is also expensive in time and memory, since the same model architecture must run sequentially for ... | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3.1. Perceptual Image Compression - extractive PDF cue:** Our perceptual compression model is based on previous work [23] and consists of an autoencoder trained by combination of a perceptual loss [106] and a ...
- **p. 3 / 3. Method - extractive PDF cue:** To lower the computational demands of training diffusion models towards high-resolution image synthesis, we observe that although diffusion models allow to ignore perceptually irrelevant details ...
- **p. 5 / 4. Experiments - extractive PDF cue:** In E.2 we list details on architecture, implementation, training and evaluation for all results presented in this section.
- **p. 3 / 3.1. Perceptual Image Compression - extractive PDF cue:** Our perceptual compression model is based on previous work [23] and consists of an autoencoder trained by combination of a perceptual loss [106] and a ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** pre-process, various, modalities, language, prompts, introduce, domain, specific, encoder, projects, intermediate, representation, then, mapped, layers, UNet, cross-attention, layer, implementing, Attention.
- **Relevant PDF headings:** 3. Method (p. 3); 3.2. Latent Diffusion Models (p. 4); Method (p. 23).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | Complex datasets such as ImageNet require reduced compression rates to avoid reducing quality. | p. 5 (4.1. On Perceptual Compression Tradeoffs), p. 5 (4.1. On Perceptual Compression Tradeoffs) |
| Denoiser / vector field | On CelebA-HQ, we report a new state-of-the-art FID of 5.11, outperforming previous likelihood-based models as well as GANs. | p. 5 (4.2. Image Generation with Latent Diffusion), p. 7 (Figure/Table caption) |
| Sampling / downstream interface | Especially compared to pixel-based LDM-1, they achieve much lower FID scores while simultaneously significantly increasing sample throughput. | p. 5 (4.1. On Perceptual Compression Tradeoffs), p. 23 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 20 / Figure/Table caption - extractive PDF cue:** Figure 15. Illustrating the effect of latent space rescaling on convolutional sampling, here for semantic image synthesis on landscapes. See Sec. 4.3.2 and Sec. D.1. ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 10. ImageNet 64→256 super-resolution on ImageNet-Val. LDM-SR has advantages at rendering realistic textures but SR3 can synthesize more coherent fine structures. See appendix for ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 11. Qualitative results on object removal with our big, w/ ft inpainting model. For more results, see Fig. 22. instead of 215M. After training, ...
- **p. 23 / Figure/Table caption - extractive PDF cue:** Figure 18. LDM-BSR generalizes to arbitrary inputs and can be used as a general-purpose upsampler, upscaling samples from a class- conditional LDM (image cf. Fig. ...
- **p. 9 / 5. Limitations & Societal Impact - extractive PDF cue:** Limitations While LDMs significantly reduce computational requirements compared to pixel-based approaches, their sequential sampling process is still slower than that of GANs.
- **p. 23 / Figure/Table caption - extractive PDF cue:** Figure 18. LDM-BSR generalizes to arbitrary inputs and can be used as a general-purpose upsampler, upscaling samples from a class- conditional LDM (image cf. Fig. ...
- **p. 5 / 4. Experiments - extractive PDF cue:** Interestingly, we find that LDMs trained in VQregularized latent spaces sometimes achieve better sample quality, even though the reconstruction capabilities of VQregularized first stage models ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.3. Conditioning Mechanisms), p. 3 (3.1. Perceptual Image Compression), p. 4 (3.2. Latent Diffusion Models), p. 3 (3. Method), p. 5 (3.3. Conditioning Mechanisms), objective p. 3 (3.1. Perceptual Image Compression), p. 3 (3.1. Perceptual Image Compression), p. 4 (3.2. Latent Diffusion Models), p. 4 (3.1. Perceptual Image Compression), p. 5 (3.3. Conditioning Mechanisms), temporal p. 2 (1. Introduction), p. 4 (3.2. Latent Diffusion Models), p. 4 (3.2. Latent Diffusion Models), p. 5 (4.1. On Perceptual Compression Tradeoffs), p. 5 (4.1. On Perceptual Compression Tradeoffs), p. 6 (4.2. Image Generation with Latent Diffusion).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
