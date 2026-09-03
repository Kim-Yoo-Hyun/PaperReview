# Insights — CityGaussianV2: Efficient and Geometrically Accurate Reconstruction for Large-Scale Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=a3ptUbuzbW; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/114864. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, our contributions are four-fold: • A novel optimization strategy for 2DGS, that accelerates its convergence under large-scale scenes and enables it to be ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Furthermore, our contribution-based vectree quantization enables a tenfold reduction in storage requirements for large-scale 2DGS.
- **p. 6 / 3 METHOD - extractive body cue:** To resolve these issues, we propose a novel pipeline, as shown in Fig.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** TrimGS (Fan et al., 2024) further provides a novel per-Gaussian contribution definition to remove inaccurate geometry.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** One of the most seminal contributions to this field is Neural Radiance Fields (NeRF) (Mildenhall et al., 2021), which implicitly models target scenes using multi-layer ...
- **p. 4 / 3 METHOD - extractive body cue:** 4, it first pre-trains a coarse model on full training data with the schedule of 3DGS.
- **p. 6 / 3 METHOD - extractive body cue:** To bypass the distillation step, we use an SH degree of 2 from the start, reducing the SH feature dimension from 48 to 27.
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 6 (3 METHOD), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (3 METHOD)

### Strongest assumption and failure boundary

- **p. 2 / 1 INTRODUCTION - extractive body cue:** On the one hand, existing methods face significant challenges related to scalability and generalization ability.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In response to these challenges, we introduce CityGaussianV2, a geometrically accurate yet efficient strategy for large-scale scene reconstruction.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Though these algorithms have been proven to be successful on small scenes or single objects, the challenges behind scaling up, including performance degradation, densification stability, ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Despite these advances, the issue of geometry accuracy has been largely overlooked due to the lack of reliable benchmarks.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Our work addresses this gap, proposing a reliable benchmark along with a novel algorithm for both economical training, high fidelity, and accurate geometry.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** As shown, NeRF-based methods are more prone to failure due to the NaN outputs of the MLP or poor convergence under sparse supervision in large-scale ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Due to page limitations, detailed parameters for block partition and quantization are provided in the Appendix.
- **Boundary to test:** As shown, NeRF-based methods are more prone to failure due to the NaN outputs of the MLP or poor convergence under sparse supervision in large-scale scenes.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, our contributions are four-fold: • A novel optimization strategy for 2DGS, that accelerates its convergence under large-scale scenes and enables it to be scaled up to high capacity (Sec. | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | For MatrixCity-Aerial, our method achieves the best surface quality among all algorithms, with the F1 score being twice that of 2DGS and outperforming CityGaussian by a significant margin. | p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Failure/limitation | As shown, NeRF-based methods are more prone to failure due to the NaN outputs of the MLP or poor convergence under sparse supervision in large-scale scenes. | p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 5, we begin by initializing a 3DGS field with the ground-truth point cloud, then traverse all training views to rasterize and count visible frequency through the output visible mask.를 Secondly, for mesh extraction, occlusion and lack of observation hinder reconstruction of some road surfaces and building facades.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 As shown, NeRF-based methods are more prone to failure due to the NaN outputs of the MLP or poor convergence under sparse supervision in large-scale scenes.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, our contributions are four-fold: • A novel optimization strategy for 2DGS, that accelerates its convergence under large-scale scenes and enables it to be scaled up to high capacity (Sec.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `Gaussian Splatting, 3D reconstruction, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** As shown, NeRF-based methods are more prone to failure due to the NaN outputs of the MLP or poor convergence under sparse supervision in large-scale scenes.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Therefore, we utilize the realistic dataset GauU-Scene (Xiong et al., 2024) and the synthetic dataset MatrixCity (Li et al., 2023a)..
3. Compare against the body-reported baseline or a matched simpler baseline: 5.2 COMPARISON WITH SOTA METHODS In this section, we compare CityGaussianV2 with state-of-the-art (SOTA) methods both quantitatively and qualitatively..
4. Report the body metric and its denominator/aggregation: Figure 1: Illustration of the superiority of CityGaussianV2. (a) Our method reconstructs large-scale complex scenes with accurate geometry from multi-view RGB images, restoring intricate structures of woods, buildings, and roads. (b) "O ....
5. Re-run the body-reported ablation/failure condition: Figure 10: Qualitative ablation of 7K iteration results among different methods. This section provides additional qualitative comparisons. As illustrated in Fig. 8, the mesh produced by GOF is obscured by a near-ground ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3 METHOD), p. 6 (3 METHOD), p. 5 (3 METHOD); the primary result is directionally consistent at p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, contributions, four-fold mechanism이 5.2 COMPARISON WITH SOTA METHODS In this section, we compare CityGaussianV2 with state-of-the-art (SOTA) methods both ... 대비 Figure 1: Illustration of the superiority of CityGaussianV2. (a) Our method reconstructs large-scale complex scenes with accurate geometry ...을 개선하고, As shown, NeRF-based methods are more prone to failure due to the NaN outputs of the ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
