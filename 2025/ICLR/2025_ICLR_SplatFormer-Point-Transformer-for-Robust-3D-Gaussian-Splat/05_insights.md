# Insights — SplatFormer: Point Transformer for Robust 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=9NfHbWKqMF; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/111734. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1 INTRODUCTION - extractive body cue:** In summary, we make the following contributions: • We introduce OOD-NVS, a new experimental protocol specifically designed to evaluate the performance of NVS methods when ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To meet these needs, we propose SplatFormer, a novel learning-based feed-forward 3D transformer designed to operate on Gaussian splats.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Existing NVS methods, including MipNeRF360 (Barron et al., 2022), and those designed for sparse inputs like LaRa (Chen et al., 2024a), face challenges in this ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our results demonstrate that existing methods struggle to generalize under the OOD-NVS protocol; • We propose SplatFormer, a novel learning-based model that refines flawed 3D ...
- **p. 15 / B IMPLEMENTATION DETAILS - extractive body cue:** Each MLP branch consists of four linear layers, with hidden dimensions of 512 and ReLU activations for all but the last layer.
- **p. 15 / B IMPLEMENTATION DETAILS - extractive body cue:** The feature decoder is composed of five separate MLP branches, which are responsible for predicting the residuals for the means, opacity, quaternion, scales, and spherical ...
- **p. 16 / B IMPLEMENTATION DETAILS - extractive body cue:** For the training of our full model, we use 8 RTX4090s with one scene per GPU, set gradient accumulation steps as 4, and train for ...
- **Contribution anchor:** p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 15 (B IMPLEMENTATION DETAILS), p. 15 (B IMPLEMENTATION DETAILS)

### Strongest assumption and failure boundary

- **p. 2 / 1 INTRODUCTION - extractive body cue:** 1, existing NVS methods perform poorly on the OOD views when restricted to low-elevation inputs, highlighting the need for a novel approach to address this ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Existing NVS methods, including MipNeRF360 (Barron et al., 2022), and those designed for sparse inputs like LaRa (Chen et al., 2024a), face challenges in this ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our results demonstrate that existing methods struggle to generalize under the OOD-NVS protocol; • We propose SplatFormer, a novel learning-based model that refines flawed 3D ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Traditionally, this problem has been approached using a standard novel view interpolation protocol, where test views are sampled at fixed intervals along the trajectory of ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** A related research problem is 3D reconstruction from sparse input views, where methods often hallucinate unseen content (Liu et al., 2023a; Chan et al., 2023; ...
- **p. 10 / 6 CONCLUSION - extractive body cue:** In this work, we introduced a new out-of-distribution (OOD) novel view synthesis test scenario and demonstrated that most neural rendering methods, including those using regularization ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** Our method has several limitations that provide directions for future work.
- **Boundary to test:** In this work, we introduced a new out-of-distribution (OOD) novel view synthesis test scenario and demonstrated that most neural rendering methods, including those using regularization techniques and data-driven priors, suffer substanti ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, we make the following contributions: • We introduce OOD-NVS, a new experimental protocol specifically designed to evaluate the performance of NVS methods when rendering 3D scenes from novel viewing angles ... | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | While our method still faces challenges with high-frequency texture details, it outperforms previous approaches in terms of fidelity and consistency in out-of-distribution views, which is also supported by the clear quantitative improve ... | p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS) |
| Failure/limitation | In this work, we introduced a new out-of-distribution (OOD) novel view synthesis test scenario and demonstrated that most neural rendering methods, including those using regularization techniques and data-driven priors, suffer substanti ... | p. 10 (6 CONCLUSION), p. 10 (5 EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 It outputs residuals that are added to the input Gaussian attributes.를 While this initial 3D representation effectively integrates multi-view information from the captured images, we observe that the shapes, appearances, and spatial structure of the Gaussian splats become biased toward the input view ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 In this work, we introduced a new out-of-distribution (OOD) novel view synthesis test scenario and demonstrated that most neural rendering methods, including those using regularization techniques and data-driven priors, suffer substanti ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, we make the following contributions: • We introduce OOD-NVS, a new experimental protocol specifically designed to evaluate the performance of NVS methods when rendering 3D scenes from novel viewing angles ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `Gaussian Splatting, point cloud, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In this work, we introduced a new out-of-distribution (OOD) novel view synthesis test scenario and demonstrated that most neural rendering methods, including those using regularization techniques and data-driven priors, suffer substanti ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Following the OOD-NVS protocol, we rendered 20 objects from Google Scanned Objects (GSO) (Downs et al., 2022) and captured 4 real-world scenes..
3. Compare against the body-reported baseline or a matched simpler baseline: Our method also outperforms MipNeRF360 and 2DGS, the best-performing baselines in Objaverse-OOD (Tab..
4. Report the body metric and its denominator/aggregation: To demonstrate this, we evaluate NVS with elevations ϕ ∈[10◦, 90◦] in Objaverse-OOD scenes and compare SplatFormer to 3DGS (Fig..
5. Re-run the body-reported ablation/failure condition: Next, we examine regularized 3DGS variants without external priors, including 2DGS (Huang et al., 2024a) and SplatFields (Mihajlovic et al., 2024)..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 15 (B IMPLEMENTATION DETAILS), p. 16 (B IMPLEMENTATION DETAILS), p. 15 (B IMPLEMENTATION DETAILS); the primary result is directionally consistent at p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, make, following mechanism이 Our method also outperforms MipNeRF360 and 2DGS, the best-performing baselines in Objaverse-OOD (Tab. 대비 To demonstrate this, we evaluate NVS with elevations ϕ ∈[10◦, 90◦] in Objaverse-OOD scenes and compare SplatFormer to ...을 개선하고, In this work, we introduced a new out-of-distribution (OOD) novel view synthesis test scenario and demonstrated ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
