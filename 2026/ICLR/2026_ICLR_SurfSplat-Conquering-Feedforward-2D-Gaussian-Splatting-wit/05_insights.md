# Insights — SurfSplat: Conquering Feedforward 2D Gaussian Splatting with Surface Continuity Priors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=o1sF4XaFdY; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/247825. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, the main contributions of this work are as follows: • We propose SurfSplat, a feedforward network that reconstructs 3D scenes using 2D Gaussian ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our model leverages a surface continuity prior and forced alpha blending to significantly improve reconstruction quality. • We introduce HRRC, a high-resolution rendering-based metric that ...
- **p. 6 / 3.1 PRELIMINARIES - extractive body cue:** 3.6 HIGH-RESOLUTION RENDERING CONSISTENCY (HRRC) To better evaluate the geometric fidelity of reconstructed 3D scenes, we propose a novel evaluation metric: High-Resolution Rendering Consistency (HRRC).
- **p. 5 / 3.1 PRELIMINARIES - extractive body cue:** To address these issues, we start by an observation: most visible geometry in real-world scenes consists of smooth, continuous surfaces.
- **p. 6 / 3.1 PRELIMINARIES - extractive body cue:** To address this, we propose a forced alpha blending strategy that explicitly constrains each Gaussian's opacity.
- **p. 4 / 3.1 PRELIMINARIES - extractive body cue:** In the multi-view branch, input images are first converted into low-resolution feature maps, which are then processed by multiple layers of self- and cross-attention Vaswani ...
- **p. 4 / 3.1 PRELIMINARIES - extractive body cue:** To integrate these complementary sources effectively, we adopt a dual-path for feature extraction within our model architecture.
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 6 (3.1 PRELIMINARIES), p. 5 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES)

### Strongest assumption and failure boundary

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Furthermore, most datasets lack out-of-distribution viewpoints for reliable assessment.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, we observe that existing feedforward methods tend to generate degraded 3D scenes.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Without effective regularization, the generated 3D scenes often lack realistic and continuous surfaces.
- **p. 6 / 3.1 PRELIMINARIES - extractive body cue:** To address this limitation, we render each reconstructed scene at a higher resolution (e.g., 2× or 4× the original), resulting in an output ˆIHR.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Despite these advancements, prior feedforward methods primarily rely on 3DGS primitives.
- **p. 10 / 5 CONCLUSION - extractive body cue:** These limitations open opportunities for future research on joint pose elimination and compact, adaptive representations.
- **p. 10 / 5 CONCLUSION - extractive body cue:** By introducing a surface continuity prior and a forced alpha blending strategy, our method addresses key limitations of previous approaches, eliminating surface discontinuities and overcoming ...
- **Boundary to test:** These limitations open opportunities for future research on joint pose elimination and compact, adaptive representations.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, the main contributions of this work are as follows: • We propose SurfSplat, a feedforward network that reconstructs 3D scenes using 2D Gaussian surfels from sparse inputs. | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | Since using more primitives generally improves performance, we focus our core comparisons on the latter group to ensure a fair comparison. | p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT) |
| Failure/limitation | These limitations open opportunities for future research on joint pose elimination and compact, adaptive representations. | p. 10 (5 CONCLUSION), p. 10 (5 CONCLUSION) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 This behavior rapidly boosts image quality for near-input viewpoints, but under the alpha-blending rendering rule, occluded Gaussians contribute minimally to the output: C = X i∈N ciαi i-1 Y j=1 (1 -αj), ...를 Given a collection of V input images {Iv}V v=1 with corresponding camera intrinsics {kv}V v=1 and poses {Tv}V v=1, the network fθ predicts Gaussian parameters for each pixel as: fθ : {(Iv, ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 These limitations open opportunities for future research on joint pose elimination and compact, adaptive representations.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, the main contributions of this work are as follows: • We propose SurfSplat, a feedforward network that reconstructs 3D scenes using 2D Gaussian surfels from sparse inputs.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `Gaussian Splatting, 3D reconstruction, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** These limitations open opportunities for future research on joint pose elimination and compact, adaptive representations.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Both datasets provide precomputed camera poses and we adhere to the official train-test splits used in prior work..
3. Compare against the body-reported baseline or a matched simpler baseline: We compare our method to state-of-the-art sparse-view generalizable methods for novel view synthesis, including PixelSplat Charatan et al..
4. Report the body metric and its denominator/aggregation: This observation highlights a key limitation of conventional NVS metrics and underscores the value of our proposed HRRC metric, which drops significantly when surface continuity is not enforced..
5. Re-run the body-reported ablation/failure condition: Figure 5: Ablation study: Visualization of recon- structed 3D scenes. Our full model yields contin- uous and coherent surfaces, while ablated variants exhibit visible artifacts and spatial inconsistencies. We conduct extensive ablation ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES), p. 15 (A.1 ENCODER ARCHITECTURE); the primary result is directionally consistent at p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 10 (4 EXPERIMENT); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, main, contributions mechanism이 We compare our method to state-of-the-art sparse-view generalizable methods for novel view synthesis, including PixelSplat Charatan ... 대비 This observation highlights a key limitation of conventional NVS metrics and underscores the value of our proposed HRRC ...을 개선하고, These limitations open opportunities for future research on joint pose elimination and compact, adaptive representations. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
