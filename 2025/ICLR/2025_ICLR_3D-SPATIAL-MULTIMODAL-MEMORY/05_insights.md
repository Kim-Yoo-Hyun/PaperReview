# Insights — 3D-SPATIAL MULTIMODAL MEMORY

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=XYdstv3ySl; PDF retrieval source: https://openreview.net/pdf/49718e82c4fa24eac05ec11d26bd767cd526299a.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Specifically, we propose to store the original high-dimensional 2D feature maps in a memory bank called principal scene components and use the low-dimensional principal queries ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these issues, we present MultiModal Memory (M3), a better integration of Gaussian splatting and multimodal foundation models that efficiently store expressive multimodal memory ...
- **p. 3 / 3 METHOD - extractive body cue:** A real-world visual perception scene (V) consists of both structure (S) and knowledge (I).
- **p. 4 / 3 METHOD - extractive body cue:** We introduce optimizable attribute queries (q) to Gaussian primitives, and apply a Gaussian Memory Attention (Agm) mechanism to produce the final rendered features ( ˆR), ...
- **p. 4 / 3 METHOD - extractive body cue:** To maintain efficiency while preserving the global representation of foundation model features, we compress the extracted features from foundation models into principal scene components (PSC) ...
- **p. 3 / 3 METHOD - extractive body cue:** The organic integration of Gaussian splatting and Foundation Models infuses scene structure with multi3
- **p. 3 / 3 METHOD - extractive body cue:** Gaussian splatting serves as a framework for constructing scene structure with finest granularity, represented as gaussian primitives, while foundation models provide vast world knowledge spanning ...
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 METHOD), p. 4 (3 METHOD), p. 4 (3 METHOD), p. 3 (3 METHOD)

### Strongest assumption and failure boundary

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We observe two key issues: First, due to the computational limitations, the feature vector dimensions in Gaussian primitives are significantly reduced compared to the original ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, these models lack the capability to retain the semantic understanding of the scene like humans.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, for larger-scale environments, our understanding tends to remain more coarse and generalized.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** SEEM and LLaMA3 features extraction failed on FSplat, which we assume was mainly due to the ground truth feature extraction procedure, where duplication was performed ...
- **Boundary to test:** SEEM and LLaMA3 features extraction failed on FSplat, which we assume was mainly due to the ground truth feature extraction procedure, where duplication was performed to each segmentation to get pixel-level features.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Specifically, we propose to store the original high-dimensional 2D feature maps in a memory bank called principal scene components and use the low-dimensional principal queries from 3D Gaussians as indices. | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | Our method, M3, outperforms F-Splat while reducing significantly compute than F-3DGS. | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Failure/limitation | SEEM and LLaMA3 features extraction failed on FSplat, which we assume was mainly due to the ground truth feature extraction procedure, where duplication was performed to each segmentation to get pixel-level features. | p. 8 (4 EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 We formally define the input of M3 as a video sequence with frames, where each frame corresponds to a view V∗.를 Visual granularity (VG) typically represents the clustering pixel scope of an image, a concept introduced in Semantic-SAM [20].로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 SEEM and LLaMA3 features extraction failed on FSplat, which we assume was mainly due to the ground truth feature extraction procedure, where duplication was performed to each segmentation to get pixel-level features.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Specifically, we propose to store the original high-dimensional 2D feature maps in a memory bank called principal scene components and use the low-dimensional principal queries from 3D Gaussians as indices.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `Robotics, 3D Vision, Gaussian Splatting`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** SEEM and LLaMA3 features extraction failed on FSplat, which we assume was mainly due to the ground truth feature extraction procedure, where duplication was performed to each segmentation to get pixel-level features.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: To support extensive quantitative and qualitative evaluation, we perform experiments using several existing scene datasets [3; 18; 10] and collected a custom robot dataset (M3-Robot) using a quadruped robot and a drone..
3. Compare against the body-reported baseline or a matched simpler baseline: 4.2 QUANTITATIVE RESULTS Baseline Implementation For quantitative experiments, we compare M3 with two recent distillation-based feature GS methods [26; 51]..
4. Report the body metric and its denominator/aggregation: M3 demonstrates superior downstream task accuracy with reduced training costs and shows practical utility when deployed on a real robot..
5. Re-run the body-reported ablation/failure condition: 3 shows the ablation of the number of foundation models involved in M3..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3 METHOD), p. 4 (3 METHOD), p. 3 (3 METHOD); the primary result is directionally consistent at p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Specifically, store, original mechanism이 4.2 QUANTITATIVE RESULTS Baseline Implementation For quantitative experiments, we compare M3 with two recent distillation-based feature ... 대비 M3 demonstrates superior downstream task accuracy with reduced training costs and shows practical utility when deployed on a ...을 개선하고, SEEM and LLaMA3 features extraction failed on FSplat, which we assume was mainly due to the ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
