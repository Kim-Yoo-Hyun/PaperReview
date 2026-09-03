# Insights — Towards Physically Executable 3D Gaussian for Embodied Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=HB6KvsqcAn; PDF retrieval source: https://openreview.net/pdf/5cdfb5b83429401e057b422d807ffd76daa429d7.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We introduce a 3DGS-Mesh Hybrid Representation: starting from our mesh scene data, we extract collision bodies for each object as the physics layer, while using ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this work, we present SAGE-3D (Semantically and Physically Aligned Gaussian Environments for 3D Navigation), a paradigm that upgrades 3DGS from a purely perceptual scene ...
- **p. 15 / A IMPLEMENTATION DETAILS - extractive body cue:** The training data did not include any VLN-CE R2R or RxR samples.
- **p. 15 / A IMPLEMENTATION DETAILS - extractive body cue:** We selected 500k "trajectory-instruction" pairs from SAGE-Bench, with no overlap with the test set.
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 15 (A IMPLEMENTATION DETAILS), p. 15 (A IMPLEMENTATION DETAILS)

### Strongest assumption and failure boundary

- **p. 2 / 1 INTRODUCTION - extractive body cue:** (2) Lack of a physically executable structure.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Consequently, deriving reliable collision geometries from 3DGS is difficult, and aligning semantics with appearance is non-trivial.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Overview of SAGE-Bench. SAGE-Bench includes a hierarchical instruction generation scheme, two major task types, two episode complexity categories, and three newly designed natural ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 4 corroborate this finding: the NaVILA model (blue trajectory) exhibits unsmooth movement and persistent collisions that conventional metrics fail to reveal.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Traditional 3DGS vs. Our work. Compared with traditional 3DGS, our InteriorGS pro- vides object-level 3DGS annotations across diverse indoor and outdoor scenes, including ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Overview of SAGE-3D, which consists of two key components: (1) Object-Level Semantic Grounding, 3DGS data is annotated by expect at the object level, ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** An episode is terminated immediately if a collision occurs, and the maximum episode time is set to 120 seconds.
- **Boundary to test:** Figure 3: Overview of SAGE-Bench. SAGE-Bench includes a hierarchical instruction generation scheme, two major task types, two episode complexity categories, and three newly designed natural continuity metrics for navigation. 2.3 PHYSICS ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We introduce a 3DGS-Mesh Hybrid Representation: starting from our mesh scene data, we extract collision bodies for each object as the physics layer, while using 3DGS to provide photorealistic appearance. | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | Even the recent SOTA model NaVILA achieves only a 0.39 success rate on high-level instructions, significantly lower than its 0.56 success rate on low-level instructions. | p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Failure/limitation | Figure 3: Overview of SAGE-Bench. SAGE-Bench includes a hierarchical instruction generation scheme, two major task types, two episode complexity categories, and three newly designed natural continuity metrics for navigation. 2.3 PHYSICS ... | p. 5 (Figure/Table caption), p. 9 (4 EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 Vision-and-Language Navigation (VLN) is a core capability for Vision-Language Action (VLA) models, enabling them to follow natural language instructions and navigate complex indoor spaces (Wei et al., 2025; Zhang et al., 2024).를 For data, we provide a hierarchical instruction scheme that combines high-level semantic goals (especially task-causal ones like "I'm thirsty, get water from the table") with low-level actions (e.g., "move from stool to ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 3: Overview of SAGE-Bench. SAGE-Bench includes a hierarchical instruction generation scheme, two major task types, two episode complexity categories, and three newly designed natural continuity metrics for navigation. 2.3 PHYSICS ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We introduce a 3DGS-Mesh Hybrid Representation: starting from our mesh scene data, we extract collision bodies for each object as the physics layer, while using 3DGS to provide photorealistic appearance.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `3D Vision, Navigation, Gaussian Splatting`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 3: Overview of SAGE-Bench. SAGE-Bench includes a hierarchical instruction generation scheme, two major task types, two episode complexity categories, and three newly designed natural continuity metrics for navigation. 2.3 PHYSICS ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Data in # Train SAGE-Bench VLN #Scenes #Samples SR ↑ OSR ↑ SPL ↑ CSR ↑ ICP ↓ PS ↑ 800 240k 0.42 0.47 0.42 0.50 0.61 0.63 800 120k 0.40 0.43 ....
3. Compare against the body-reported baseline or a matched simpler baseline: 4, models trained entirely on SAGE-Bench data (without any VLN-CE data) achieved clear performance improvements over their respective baselines..
4. Report the body metric and its denominator/aggregation: In addition to the three novel metrics we proposed in Section 3.3 for evaluating the natural continuity of model navigation - CSR, ICP, and PS - we also adopt common metrics used ....
5. Re-run the body-reported ablation/failure condition: 4, models trained entirely on SAGE-Bench data (without any VLN-CE data) achieved clear performance improvements over their respective baselines..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 15 (A IMPLEMENTATION DETAILS), p. 15 (A IMPLEMENTATION DETAILS); the primary result is directionally consistent at p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 introduce, DGS-Mesh, Hybrid mechanism이 4, models trained entirely on SAGE-Bench data (without any VLN-CE data) achieved clear performance improvements over ... 대비 In addition to the three novel metrics we proposed in Section 3.3 for evaluating the natural continuity of ...을 개선하고, Figure 3: Overview of SAGE-Bench. SAGE-Bench includes a hierarchical instruction generation scheme, two major task types, ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
