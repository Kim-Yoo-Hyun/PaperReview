# Insights — Marigold: Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (33 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2312.02145; PDF retrieval source: https://arxiv.org/pdf/2312.02145. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 5 / 3.4. Inference - extractive body cue:** Capitalizing on that, we propose the following test-time ensembling scheme, capable of combining multiple inference passes over the same input.
- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our contributions are: 1.
- **p. 5 / 3.4. Inference - extractive body cue:** This scheme enables a flexible trade-off between computation efficiency and prediction quality by choosing N accordingly.
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we set out to explore this option and develop Marigold, a latent diffusion model (LDM) based on Stable Diffusion [38], along with ...
- **p. 4 / 3.3. Fine-Tuning Protocol - extractive body cue:** This normalization allows Marigold to focus on pure affine-invariant depth estimation.
- **p. 4 / 3.2. Network Architecture - extractive body cue:** One of our main objectives is training efficiency since diffusion models are often extremely resource-intensive to train.
- **p. 4 / 3.1. Generative Formulation - extractive body cue:** The adapted inference procedure involves one extra step - the decoder D reconstructing the data ˆd from the estimated clean latent z(d) 0 : ˆd ...
- **Contribution anchor:** p. 5 (3.4. Inference), p. 2 (1. Introduction), p. 5 (3.4. Inference), p. 2 (1. Introduction), p. 4 (3.3. Fine-Tuning Protocol), p. 4 (3.2. Network Architecture)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** Empowered by the underlying diffusion prior of natural images, Marigold exhibits excellent zero-shot generalization: Without ever having seen real depth maps, it attains state-ofthe-art performance ...
- **p. 1 / 1. Introduction - extractive body cue:** Clearly, undoing the projection from the 3D world to a 2D image is a geometrically ill-posed problem and can 1.
- **p. 2 / 1. Introduction - extractive body cue:** only be solved with the help of prior knowledge, such as typical object shapes and sizes, likely scene layouts, occlusion patterns, etc.
- **p. 8 / 5. Conclusion - extractive body cue:** Future research directions to overcome current limitations include improving inference efficiency, ensuring that similar inputs yield consistent outputs despite the model's generative nature, and better ...
- **p. 5 / 4.1. Implementation - extractive body cue:** During training, we apply the DDPM noise scheduler [20] with 1000 diffusion steps.
- **p. 5 / 4.1. Implementation - extractive body cue:** For the final prediction, we aggregate results from 10 inference runs with varying starting noise.
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** We investigate the impact of three types of noise during the training phase.
- **Boundary to test:** Future research directions to overcome current limitations include improving inference efficiency, ensuring that similar inputs yield consistent outputs despite the model's generative nature, and better handling of distant scene parts.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Capitalizing on that, we propose the following test-time ensembling scheme, capable of combining multiple inference passes over the same input. | p. 5 (3.4. Inference), p. 2 (1. Introduction) |
| Reported outcome | 2, training with multi-resolution noise significantly improves the depth prediction accuracy over using standard Gaussian noise. | p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies) |
| Failure/limitation | Future research directions to overcome current limitations include improving inference efficiency, ensuring that similar inputs yield consistent outputs despite the model's generative nature, and better handling of distant scene parts. | p. 8 (5. Conclusion), p. 5 (4.1. Implementation) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 Given that the encoder, which is designed for 3-channel (RGB) inputs, receives a single-channel depth map, we replicate the depth map into three channels to simulate an RGB image.를 To implement the conditioning of the latent denoiser ϵθ(z(d) t , z(x), t) on input image x, we concatenate the image and depth latent codes into a single input zt = cat(z(d) ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Future research directions to overcome current limitations include improving inference efficiency, ensuring that similar inputs yield consistent outputs despite the model's generative nature, and better handling of distant scene parts.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Capitalizing on that, we propose the following test-time ensembling scheme, capable of combining multiple inference passes over the same input.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `Diffusion, Generation, depth, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Future research directions to overcome current limitations include improving inference efficiency, ensuring that similar inputs yield consistent outputs despite the model's generative nature, and better handling of distant scene parts.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: In the case of the ScanNet dataset, we randomly sampled 800 images from the 312 official validation scenes for testing..
3. Compare against the body-reported baseline or a matched simpler baseline: Table 1. Quantitative comparison of Marigold with SOTA affine-invariant depth estimators on several zero-shot benchmarks. All metrics† are presented in percentage terms; bold numbers are the best, underscored second best. Our method ....
4. Report the body metric and its denominator/aggregation: All metrics† are presented in percentage terms; bold numbers are the best, underscored second best..
5. Re-run the body-reported ablation/failure condition: Table 1. Quantitative comparison of Marigold with SOTA affine-invariant depth estimators on several zero-shot benchmarks. All metrics† are presented in percentage terms; bold numbers are the best, underscored second best. Our method ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (3.4. Inference), p. 4 (3.2. Network Architecture), p. 4 (3.1. Generative Formulation); the primary result is directionally consistent at p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies), p. 6 (4.2. Evaluation); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Capitalizing, following, test-time mechanism이 Table 1. Quantitative comparison of Marigold with SOTA affine-invariant depth estimators on several zero-shot benchmarks. All ... 대비 All metrics† are presented in percentage terms; bold numbers are the best, underscored second best.을 개선하고, Future research directions to overcome current limitations include improving inference efficiency, ensuring that similar inputs yield ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
