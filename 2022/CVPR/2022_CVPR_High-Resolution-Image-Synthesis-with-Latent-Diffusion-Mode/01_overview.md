# High-Resolution Image Synthesis with Latent Diffusion Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (45 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2112.10752.
> PDF retrieval source: https://arxiv.org/pdf/2112.10752. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Foundations: Generative Models
- Tier: REFERENCE
- Tags: Diffusion, latent representation, Generation
- Official paper: https://arxiv.org/abs/2112.10752
- Full-text retrieval: https://arxiv.org/pdf/2112.10752
- Code/Project: https://github.com/CompVis/latent-diffusion
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (45 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Foundations: Generative Models의 generative 문제를 이해하기 위해 읽는다. 본문은 (iii) We show that, in contrast to previous work [93] which learns both an encoder/decoder architecture and a score-based prior simultaneously, our approach does not require a delicate weighting of reconstruction and ...를 문제로 두고, In sum, our work makes the following contributions: (i) In contrast to purely transformer-based approaches [23,66], our method scales more graceful to higher dimensional data and can thus (a) work on a ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** By decomposing the image formation process into a sequential application of denoising autoencoders, diffusion models (DMs) achieve state-of-the-art synthesis results on image data and beyond.
- **p. 1 / Abstract - extractive body cue:** Additionally, their formulation allows for a guiding mechanism to control the image generation process without retraining.
- **p. 1 / Abstract - extractive body cue:** However, since these models typically operate directly in pixel space, optimization of powerful DMs often consumes hundreds of GPU days and inference is expensive due ...
- **p. 1 / Abstract - extractive body cue:** To enable DM training on limited computational resources while retaining their quality and flexibility, we apply them in the latent space of powerful pretrained autoencoders.
- **p. 1 / Abstract - extractive body cue:** In contrast to previous work, training diffusion models on such a representation allows for the first time to reach a near-optimal point between complexity reduction ...
- **p. 2 / 1. Introduction - extractive body cue:** (iii) We show that, in contrast to previous work [93] which learns both an encoder/decoder architecture and a score-based prior simultaneously, our approach does not ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In sum, our work makes the following contributions: (i) In contrast to purely transformer-based approaches [23,66], our method scales more graceful to higher dimensional data ...
- **p. 2 / 1. Introduction - extractive body cue:** We propose latent diffusion models (LDMs) as an effective generative model and a separate mild compression stage that only eliminates imperceptible details.
- **p. 3 / 3. Method - extractive body cue:** We propose to circumvent this drawback by introducing an explicit separation of the compressive from the generative learning phase (see Fig.
- **p. 3 / 3.1. Perceptual Image Compression - extractive body cue:** Our perceptual compression model is based on previous work [23] and consists of an autoencoder trained by combination of a perceptual loss [106] and a ...
- **p. 4 / 3.3. Conditioning Mechanisms - extractive body cue:** To pre-process y from various modalities (such as language prompts) we introduce a domain specific encoder τθ that projects y to an intermediate representation τθ(y) ...
- **p. 4 / 3.2. Latent Diffusion Models - extractive body cue:** Unlike previous work that relied on autoregressive, attention-based transformer models in a highly compressed, discrete latent space [23,66,103], we can take advantage of image-specific inductive ...
- **p. 3 / 3. Method - extractive body cue:** To lower the computational demands of training diffusion models towards high-resolution image synthesis, we observe that although diffusion models allow to ignore perceptually irrelevant details ...
- **p. 5 / 3.3. Conditioning Mechanisms - extractive body cue:** (unmasked) transformers [97] when y are text prompts (see Sec.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In the context of image synthesis, however, combining the generative power of DMs with other types of conditionings beyond class-labels [15] or blurred variants of the input image [72] is so far ... | conditioning observation와 noisy/intermediate sample | p. 4 (3.3. Conditioning Mechanisms), p. 4 (3.3. Conditioning Mechanisms) |
| State/latent | context, image, synthesis, however, combining, generative, power, DMs, other, types, conditionings, beyond | latent/noise variable와 conditional distribution | p. 4 (3.3. Conditioning Mechanisms), p. 4 (3.3. Conditioning Mechanisms), p. 1 (1. Introduction) |
| Output/action | We turn DMs into more flexible conditional image generators by augmenting their underlying UNet backbone with the cross-attention mechanism [97], which is effective for learning attention-based models of various input modalities [35,36]. | generated sample, action chunk 또는 trajectory | p. 4 (3.3. Conditioning Mechanisms), p. 1 (1. Introduction), p. 3 (3. Method) |
| Objective/outcome | This ensures that the reconstructions are confined to the image manifold by enforcing local realism and avoids bluriness introduced by relying solely on pixel-space losses such as L2 or L1 objectives. | distribution fit, multimodality, sample quality와 latency | p. 3 (3.1. Perceptual Image Compression), p. 3 (3.1. Perceptual Image Compression), p. 4 (3.2. Latent Diffusion Models) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In sum, our work makes the following contributions: (i) In contrast to purely transformer-based approaches [23,66], our method scales more graceful to higher dimensional data ...
- **p. 2 / 1. Introduction - extractive body cue:** We propose latent diffusion models (LDMs) as an effective generative model and a separate mild compression stage that only eliminates imperceptible details.
- **p. 3 / 3. Method - extractive body cue:** We propose to circumvent this drawback by introducing an explicit separation of the compressive from the generative learning phase (see Fig.
- **p. 3 / 3.1. Perceptual Image Compression - extractive body cue:** Our perceptual compression model is based on previous work [23] and consists of an autoencoder trained by combination of a perceptual loss [106] and a ...
- **p. 4 / 3.3. Conditioning Mechanisms - extractive body cue:** To pre-process y from various modalities (such as language prompts) we introduce a domain specific encoder τθ that projects y to an intermediate representation τθ(y) ...
- **p. 5 / 4.1. On Perceptual Compression Tradeoffs - extractive body cue:** Especially compared to pixel-based LDM-1, they achieve much lower FID scores while simultaneously significantly increasing sample throughput.
- **p. 23 / Figure/Table caption - extractive body cue:** Table 11. ×4 upscaling results on ImageNet-Val. (2562); †: FID features computed on validation split, ‡: FID features computed on train split. We also include ...
- **p. 6 / 4.2. Image Generation with Latent Diffusion - extractive body cue:** We outperform prior diffusion based approaches on all but the LSUN-Bedrooms dataset, where our score is close to ADM [15], despite utilizing half its parameters ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 5 (4.1. On Perceptual Compression Tradeoffs), p. 23 (Figure/Table caption) |
| Embodiment/environment | Complex datasets such as ImageNet require reduced compression rates to avoid reducing quality. | hardware/simulator version and reset protocol | p. 5 (4.1. On Perceptual Compression Tradeoffs), p. 5 (4.1. On Perceptual Compression Tradeoffs) |
| Dataset/benchmark | Comparing LDMs with varying compression on the CelebA-HQ (left) and ImageNet (right) datasets. | role, split, size and leakage | p. 5 (4.1. On Perceptual Compression Tradeoffs), p. 5 (4.1. On Perceptual Compression Tradeoffs), p. 6 (4.2. Image Generation with Latent Diffusion), p. 6 (4.2. Image Generation with Latent Diffusion) |
| Metric | The dashed line shows the FID scores for 200 steps, indicating the strong performance of LDM- {4-8}. | definition, denominator, direction and uncertainty | p. 6 (4.2. Image Generation with Latent Diffusion), p. 5 (4.1. On Perceptual Compression Tradeoffs), p. 5 (4.1. On Perceptual Compression Tradeoffs) |
| Baseline/ablation | On CelebA-HQ, we report a new state-of-the-art FID of 5.11, outperforming previous likelihood-based models as well as GANs. | fair input/data/compute/action matching | p. 5 (4.2. Image Generation with Latent Diffusion), p. 7 (Figure/Table caption), p. 23 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 5. Limitations & Societal Impact - extractive body cue:** Limitations While LDMs significantly reduce computational requirements compared to pixel-based approaches, their sequential sampling process is still slower than that of GANs.
- **p. 23 / Figure/Table caption - extractive body cue:** Figure 18. LDM-BSR generalizes to arbitrary inputs and can be used as a general-purpose upsampler, upscaling samples from a class- conditional LDM (image cf. Fig. ...
- **p. 5 / 4. Experiments - extractive body cue:** Interestingly, we find that LDMs trained in VQregularized latent spaces sometimes achieve better sample quality, even though the reconstruction capabilities of VQregularized first stage models ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Task 1: Subjects were shown ground truth and generated image and asked for preference. Task 2: Subjects had to decide between two generated ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 10. ImageNet 64→256 super-resolution on ImageNet-Val. LDM-SR has advantages at rendering realistic textures but SR3 can synthesize more coherent fine structures. See appendix for ...
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 15. Illustrating the effect of latent space rescaling on convolutional sampling, here for semantic image synthesis on landscapes. See Sec. 4.3.2 and Sec. D.1. ...

## Why Read It

Foundations: Generative Models의 generative 문제를 이해하기 위해 읽는다. 본문은 (iii) We show that, in contrast to previous work [93] which learns both an encoder/decoder architecture and a score-based prior simultaneously, our approach does not require a delicate weighting of reconstruction and ...를 문제로 두고, In sum, our work makes the following contributions: (i) In contrast to purely transformer-based approaches [23,66], our method scales more graceful to higher dimensional data and can thus (a) work on a ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 4 (3.3. Conditioning Mechanisms), p. 3 (3.1. Perceptual Image Compression), p. 4 (3.2. Latent Diffusion Models), p. 3 (3. Method), p. 5 (3.3. Conditioning Mechanisms) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
