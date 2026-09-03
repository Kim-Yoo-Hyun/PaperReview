# Insights — Rethinking Serialization in Linear 3D Vision: Decoupling Anisotropic Geometry from Isotropic Semantics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=MSVQM8Ub2y; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/328620. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** Based on this observation, we propose AnIsoNet, which decouples local anisotropic geometry modeling from global semantic aggregation.
- **p. 3 / 3.1. Overview - extractive body cue:** The framework consists of two complementary modules: 1.
- **p. 3 / 3.1. Overview - extractive body cue:** To address this limitation, we propose AnIsoNet, a unified framework that decouples these two processes (Figure 2).
- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are as follows: • We identify serialization bias as a key bottleneck in 3D SSMs and propose a decoupling paradigm that addresses local ...
- **p. 5 / 3.1. Overview - extractive body cue:** The recurrence ht = f(ht-1, xt) inherently requires a sequential ordering, so 3D point clouds must be artificially serialized and the contribution of xs to ...
- **p. 4 / 3.1. Overview - extractive body cue:** Following the DeLA architecture (Chen et al., 2023), we use dataset-specific hierarchical LAGM encoders (Figure 2a).
- **p. 4 / 3.1. Overview - extractive body cue:** The projected ESE feature is injected into the stage representation and then aggregated on the k-NN graph.
- **Contribution anchor:** p. 2 (1. Introduction), p. 3 (3.1. Overview), p. 3 (3.1. Overview), p. 2 (1. Introduction), p. 5 (3.1. Overview), p. 4 (3.1. Overview)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** Effective 3D point cloud understanding must reconcile local anisotropic geometry with global isotropic semantics, but the irregular and unordered nature of point sets makes this ...
- **p. 2 / 1. Introduction - extractive body cue:** However, unlike Transformers that support noncausal attention, the strict recurrent path dependency of SSMs (where state ht strictly depends on ht-1) introduces a new serialization ...
- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are as follows: • We identify serialization bias as a key bottleneck in 3D SSMs and propose a decoupling paradigm that addresses local ...
- **p. 1 / 1. Introduction - extractive body cue:** Early architectures, exemplified by PointNet++ (Qi et al., 2017b), prioritized local anisotropy through hierarchical grouping, yet struggled to maintain long-range global semantic coherence.
- **p. 7 / 4.3. Analysis and Ablation - extractive body cue:** A mismatched mode therefore causes noticeable degradation rather than collapse.
- **p. 7 / 4.3. Analysis and Ablation - extractive body cue:** Because our claim concerns robustness rather than strict permutation invariance, we directly test the task-relevant notion of robustness by perturbing the inference-time input order on ...
- **Boundary to test:** A mismatched mode therefore causes noticeable degradation rather than collapse.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Based on this observation, we propose AnIsoNet, which decouples local anisotropic geometry modeling from global semantic aggregation. | p. 2 (1. Introduction), p. 3 (3.1. Overview) |
| Reported outcome | Overall, the figure shows that AnIsoNet improves accuracy while remaining in a much smaller parameter regime, rather than trading scale for performance. | p. 8 (4.4. Efficiency Analysis), p. 6 (4.1. Experimental Setup) |
| Failure/limitation | A mismatched mode therefore causes noticeable degradation rather than collapse. | p. 7 (4.3. Analysis and Ablation), p. 7 (4.3. Analysis and Ablation) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 In Mamba (Gu & Dao, 2024), the state evolves as: ht = ¯A · ht-1 + ¯Bt · xt, yt = Ct · ht, (9) where ht is the recurrent hidden state, ...를 Unlike standard DeltaNet (Yang et al., 2024) which maintains a matrix state S ∈RD×D to capture cross-dimensional interactions, we employ a dimension-wise vector state st ∈RD, initialized as s0 = 0, that ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 A mismatched mode therefore causes noticeable degradation rather than collapse.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Based on this observation, we propose AnIsoNet, which decouples local anisotropic geometry modeling from global semantic aggregation.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `semantic, alignment, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** A mismatched mode therefore causes noticeable degradation rather than collapse.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Dataset Regime Protocol Identity/Default (%) Hilbert (%) Morton (%) S3DIS Dense scene Mode ablation 82.62 74.46 74.68 ScanObjectNN Sparse object Mode ablation 92.51 93.86 94.21 Order Robustness in Dense Scenes..
3. Compare against the body-reported baseline or a matched simpler baseline: Relative to linear-complexity baselines, it outperforms PCM (Zhang et al., 2025) by 3.0% and Sonata (lin.) by 10.3%..
4. Report the body metric and its denominator/aggregation: Overall, the figure shows that AnIsoNet improves accuracy while remaining in a much smaller parameter regime, rather than trading scale for performance..
5. Re-run the body-reported ablation/failure condition: Figure 2. Overview of our AnIsoNet framework. (a) LAGM (Local Anisotropy Geometric Modeling) shows a representative hierarchical architecture; the number of stages is dataset-specific. Each stage combines sampling/downsampling, Ellipsoi ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3.1. Overview), p. 4 (3.1. Overview), p. 3 (3.1. Overview); the primary result is directionally consistent at p. 8 (4.4. Efficiency Analysis), p. 6 (4.1. Experimental Setup), p. 6 (4.2. Main Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 observation, AnIsoNet, decouples mechanism이 Relative to linear-complexity baselines, it outperforms PCM (Zhang et al., 2025) by 3.0% and Sonata (lin.) ... 대비 Overall, the figure shows that AnIsoNet improves accuracy while remaining in a much smaller parameter regime, rather than ...을 개선하고, A mismatched mode therefore causes noticeable degradation rather than collapse. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
