# Insights — Search3D: Hierarchical Open-Vocabulary 3D Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2409.18431; PDF retrieval source: https://arxiv.org/pdf/2409.18431. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** To summarize our key contributions: • We propose a hierarchical open-vocabulary 3D segmentation method capable of segmenting both entire objects and their parts given arbitrary ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To evaluate our method, we introduce a novel evaluation suite for open-vocabulary scene-scale 3D part segmentation based on MultiScan [16].
- **p. 3 / III. METHOD - extractive body cue:** We introduce a novel hierarchical 3D scene representation enabling open-vocabulary segmentation for scene entities at multiple granularities, including objects and their parts.
- **p. 1 / I. INTRODUCTION - extractive body cue:** 1: We propose Search3D, a method for open-vocabulary 3D search at multiple levels of granularity.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This enables searching across objects, parts, and attributes matching any given user query (right). critical to scene interaction.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Object-centric open-vocabulary 3D segmentation methods typically first extract a set of class-agnostic 3D object instance masks and then compute a feature representation per object, represented ...
- **p. 4 / 2) Computing open-vocabulary features for the scene repre - extractive body cue:** These 2D segment crops are then passed through the SigLIP [32] image encoder, producing feature vectors of dimension D for each segment.
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)

### Strongest assumption and failure boundary

- **p. 2 / I. INTRODUCTION - extractive body cue:** Finally, the least obvious limitation is derived from the way these models compute the point-level features: Although the projected open-vocabulary features are fine-grained at the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, storing these per-point features is memoryintensive, they are inherently noisy, and they lack instance-level information - a critical requirement for real-world applications in which ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** A purely object-centric understanding fails to provide this level of detail.
- **p. 1 / I. INTRODUCTION - extractive body cue:** While effective for these predefined classes, such approaches struggle to generalize to novel classes.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Nevertheless, there are limitations to the geometrical segmentation method we employ for part segmentation, as it relies on surface normals.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Discussion and Limitations One limitation of our work is the reliance on a simple geometrical over-segmentation method for identifying object parts.
- **Boundary to test:** Nevertheless, there are limitations to the geometrical segmentation method we employ for part segmentation, as it relies on surface normals.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To summarize our key contributions: • We propose a hierarchical open-vocabulary 3D segmentation method capable of segmenting both entire objects and their parts given arbitrary textual queries, by aggregating features anchored to ... | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | It demonstrates the strong open-vocabulary part-segmentation performance of our segment-level features, with at least + 13.8 AP improvement over baseline methods. | p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Failure/limitation | Nevertheless, there are limitations to the geometrical segmentation method we employ for part segmentation, as it relies on surface normals. | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 This representation is built upon 3D scenes reconstructed using posed RGB-D image sequences, as shown in Fig.를 This enables searching across objects, parts, and attributes matching any given user query (right). critical to scene interaction.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Nevertheless, there are limitations to the geometrical segmentation method we employ for part segmentation, as it relies on surface normals.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To summarize our key contributions: • We propose a hierarchical open-vocabulary 3D segmentation method capable of segmenting both entire objects and their parts given arbitrary textual queries, by aggregating features anchored to ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `3D Vision, semantic`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Nevertheless, there are limitations to the geometrical segmentation method we employ for part segmentation, as it relies on surface normals.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 3D Material Segmentation Next, we perform an analysis on 3D material segmentation task using the object-level material annotations from the 3RScan dataset [18]..
3. Compare against the body-reported baseline or a matched simpler baseline: First, we evaluate the quality of our segment features for identifying object parts using an oracle mask experiment, isolating feature quality from the effect of 3D geometric part segmentation quality..
4. Report the body metric and its denominator/aggregation: Additionally, averaging the objectlevel and part-level similarity scores yields slightly better results than using the maximum of these scores..
5. Re-run the body-reported ablation/failure condition: Aggr. search AP AP50 AP25 (1) Ours ✓ 4.7 8.2 17.6 (2) Ours ✓ ✓ 6.6 11.4 23.7 (3) Ours ✓ ✓ ✓(max.) 7.5 13.5 28.4 (4) Ours ✓ ✓ ✓(avg.) 7.9 ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD); the primary result is directionally consistent at p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summarize, contributions, hierarchical mechanism이 First, we evaluate the quality of our segment features for identifying object parts using an oracle ... 대비 Additionally, averaging the objectlevel and part-level similarity scores yields slightly better results than using the maximum of these ...을 개선하고, Nevertheless, there are limitations to the geometrical segmentation method we employ for part segmentation, as it ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
