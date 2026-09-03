# Insights — UrbanGS: Efficient and Scalable Architecture for Geometrically Accurate Large-Scene Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=L3utaw6SD9; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/248058. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our main contributions are summarized below: • We propose a Depth-Consistent D-Normal Regularizer that enables holistic optimization of all Gaussian parameters (position, rotation), addressing the ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To overcome this limitation, we introduce a Depth-Consistent D-Normal Regularization framework.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We propose UrbanGS, a strategy that achieves high geometric accuracy, fidelity, and efficiency in large-scale scene reconstruction.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** To meet the memory and computational demands of urban-scale reconstruction, we propose a Spatially Adaptive Gaussian Pruning (SAGP) method.
- **p. 4 / 3.1 PRELIMINARIES - extractive body cue:** (4) In our method, the depth map is rendered by performing a weighted sum of depths (Bae & Davison, 2024; Chen et al., 2024b; Yu ...
- **p. 7 / 3.1 PRELIMINARIES - extractive body cue:** First, when obtaining the global coarse 3DGS model, we first eliminate redundant Gaussians through SAGP pruning to prevent these redundant Gaussians from attracting non-contributing views ...
- **p. 4 / 3.1 PRELIMINARIES - extractive body cue:** To reconstruct scene surfaces, we enforce normal priors N predicted by a pretrained monocular deep neural network (Bae & Davison, 2024) to supervise the rendered ...
- **Contribution anchor:** p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (3.1 PRELIMINARIES), p. 7 (3.1 PRELIMINARIES)

### Strongest assumption and failure boundary

- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, due to the unstructured nature of 3DGS, accurately representing surfaces-especially in large-scale complex scenes-remains a significant challenge.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** These limitations underscore the urgent need for a unified framework that balances geometric precision, memory efficiency, and seamless scalability.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our main contributions are summarized below: • We propose a Depth-Consistent D-Normal Regularizer that enables holistic optimization of all Gaussian parameters (position, rotation), addressing the ...
- **p. 5 / 3.1 PRELIMINARIES - extractive body cue:** In urban-scale scenes, D-Normal regularization optimizes geometry through normal-depth associations but lacks explicit cross-view depth constraints, frequently causing building misalignment and street distortion-especially in distant/co ...
- **p. 6 / 3.1 PRELIMINARIES - extractive body cue:** To overcome these limitations, we propose a unified, spatially adaptive pruning framework.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Detailed geometry evaluation on the GauU-Scene dataset (Xiong et al., 2024). "NaN" indicates that the method produced invalid numerical results, while "FAIL" denotes ...
- **p. 25 / C SUPPLEMENTATION TO THE PARTITIONING STRATEGY - extractive body cue:** Qualitative results in Figure F show that rendered views remain visually consistent across different weight combinations, with no catastrophic failures even for suboptimal settings.
- **Boundary to test:** Table 2: Detailed geometry evaluation on the GauU-Scene dataset (Xiong et al., 2024). "NaN" indicates that the method produced invalid numerical results, while "FAIL" denotes a failure to extract a valid mesh. ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our main contributions are summarized below: • We propose a Depth-Consistent D-Normal Regularizer that enables holistic optimization of all Gaussian parameters (position, rotation), addressing the limitation of incomplete geometric upda ... | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | Quantitative results reveal consistent improvements across all evaluation metrics, with notable gains in F1-score (from 0.453 to 0.503) and PSNR (from 24.59 to 26.44), validating the critical importance of this component for ... | p. 10 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Failure/limitation | Table 2: Detailed geometry evaluation on the GauU-Scene dataset (Xiong et al., 2024). "NaN" indicates that the method produced invalid numerical results, while "FAIL" denotes a failure to extract a valid mesh. ... | p. 9 (Figure/Table caption), p. 25 (C SUPPLEMENTATION TO THE PARTITIONING STRATEGY) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 First, the rendered depth map is back-projected into point clouds{dk(n, p)}, using the camera intrinsic matrix.를 D.5) and ensures that a Gaussian is retained only when it simultaneously exhibits high visibility, frequent observation across views, and appropriate geometric scale.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Table 2: Detailed geometry evaluation on the GauU-Scene dataset (Xiong et al., 2024). "NaN" indicates that the method produced invalid numerical results, while "FAIL" denotes a failure to extract a valid mesh. ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our main contributions are summarized below: • We propose a Depth-Consistent D-Normal Regularizer that enables holistic optimization of all Gaussian parameters (position, rotation), addressing the limitation of incomplete geometric upda ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `3D reconstruction, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Table 2: Detailed geometry evaluation on the GauU-Scene dataset (Xiong et al., 2024). "NaN" indicates that the method produced invalid numerical results, while "FAIL" denotes a failure to extract a valid mesh. ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We compare our method with existing surface reconstruction approaches on the GauU-Scene datasets (Xiong et al., 2024)..
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 4: Qualitative mesh and texture comparison between SOTA and our method on GauU-Scene dataset (Xiong et al., 2024). 4.2 MAIN RESULTS Novel View Synthesis. As shown in Table 1 and Fig. ....
4. Report the body metric and its denominator/aggregation: In particular, compared with CityGS-X, our approach attains higher F1 scores across all scenes by improving recall while maintaining comparable precision..
5. Re-run the body-reported ablation/failure condition: Method PSNR↑ SSIM↑ LPIPS↓ F1↑ w/o D-Normal 25.02 0.743 0.215 0.463 w/o Depth Consistency 24.59 0.792 0.201 0.453 w/o Geometry-Aware Confidence 26.02 0.795 0.163 0.493 Full 26.44 0.805 0.157 0.503 4.3 ABLATION ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 7 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES), p. 15 (A IMPLEMENTATION DETAILS); the primary result is directionally consistent at p. 10 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 main, contributions, summarized mechanism이 Figure 4: Qualitative mesh and texture comparison between SOTA and our method on GauU-Scene dataset (Xiong ... 대비 In particular, compared with CityGS-X, our approach attains higher F1 scores across all scenes by improving recall while ...을 개선하고, Table 2: Detailed geometry evaluation on the GauU-Scene dataset (Xiong et al., 2024). "NaN" indicates that ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
