# Insights — From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=fzmittHfq3; PDF retrieval source: https://openreview.net/pdf/d6aae457099a5d9e50bba1a6bbc48d8756a15c91.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** We propose FALCON (From Spatial to Action), a novel paradigm that integrates richer and more representative 3D spatial tokens into VLAs through an improved injection ...
- **p. 2 / 1 Introduction - extractive body cue:** Overall Benchmark Bridge Calvin (Zero-shot) Google Robot Calvin Real-World Real-World (Few-Shot) Figure 1 We propose FALCON, a vision-language-action model that achieves robust 3D spatial understanding ...
- **p. 3 / 1 Introduction - extractive body cue:** For limitation (2) of poor modality transferability, we introduce an Embodied Spatial Model that can optionally integrate extra 3D modalities (e.g., depth, poses).
- **p. 4 / 3 Methodology - extractive body cue:** We introduce a lightweight fusion mechanism that aligns and combines these complementary representations (see Sec.
- **p. 4 / 3 Methodology - extractive body cue:** To this end, we propose FALCON, a generalist robot policy that overcomes limitations of prior VLAs by integrating rich geometric priors from spatial foundation models ...
- **p. 6 / 3 Methodology - extractive body cue:** These are then concatenated with a learnable camera token tcam ∈RDs and fed into a Spatial Encoder Espl(·), which consists of N cross-attention and self-attention ...
- **p. 4 / 3 Methodology - extractive body cue:** 2, FALCON is an end-to-end VLA consists of three core components: (1) a 2D VLM for multimodal semantic representation, (2) an ESM for extracting 3D ...
- **Contribution anchor:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (3 Methodology), p. 4 (3 Methodology), p. 6 (3 Methodology)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** This discrepancy results in a critical gap: current VLAs lack reliable 3D spatial understanding, leading to persistent challenges in generalization and adaptability.
- **p. 2 / 1 Introduction - extractive body cue:** These limitations now form a major bottleneck in developing reliable generalist robot policies.
- **p. 3 / 1 Introduction - extractive body cue:** To overcome limitation (3) of alignment challenges, we draw inspiration from the brain's division of labor.
- **p. 3 / 1 Introduction - extractive body cue:** For limitation (2) of poor modality transferability, we introduce an Embodied Spatial Model that can optionally integrate extra 3D modalities (e.g., depth, poses).
- **p. 9 / 4 Experiments - extractive body cue:** For larger blocks, collisions frequently occur during the placement of the blue block, while smaller blocks are prematurely released before placement, leading to task failure.
- **p. 11 / 5 Conclusion - extractive body cue:** In this work, we introduce FALCON, a vision-language-action model that augments generalist robot policies with robust 3D spatial understanding.
- **p. 11 / 5 Conclusion - extractive body cue:** Experiments across both simulation and real-world tasks show that FALCON consistently surpasses existing VLA methods, achieving state-of-the-art performance and robustness on spatially demanding tasks.
- **Boundary to test:** For larger blocks, collisions frequently occur during the placement of the blue block, while smaller blocks are prematurely released before placement, leading to task failure.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We propose FALCON (From Spatial to Action), a novel paradigm that integrates richer and more representative 3D spatial tokens into VLAs through an improved injection scheme. | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | 3, FALCON achieves the highest average success rate of 70.0% across all nine task suites, outperforming the advanced method SpatialVLA [31] (44.4%) by 25.6%. | p. 8 (4 Experiments), p. 7 (4 Experiments) |
| Failure/limitation | For larger blocks, collisions frequently occur during the placement of the blue block, while smaller blocks are prematurely released before placement, leading to task failure. | p. 9 (4 Experiments), p. 11 (5 Conclusion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 3.1 Problem Definition We study the problem of task-oriented robot control, where a robot must interpret visual observations Ot = {I1 t , . . . , In t } at time ...를 At timestep t, the VLM processes visual observations Ot and language instructions L to produce a semantic action token ˆtact.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 For larger blocks, collisions frequently occur during the placement of the blue block, while smaller blocks are prematurely released before placement, leading to task failure.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We propose FALCON (From Spatial to Action), a novel paradigm that integrates richer and more representative 3D spatial tokens into VLAs through an improved injection scheme.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Robotics, 3D Vision`.
- **Reading predecessor in the generated track queue:** SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** For larger blocks, collisions frequently occur during the placement of the blue block, while smaller blocks are prematurely released before placement, leading to task failure.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: All models are initially pre-trained on a mixture of the Open X-Embodiment dataset [29] and then fine-tuned with multi-task real-robot data..
3. Compare against the body-reported baseline or a matched simpler baseline: 2 reports the results on the Bridge-WidowX setup, where FALCON consistently outperforms all baselines and achieves best performance..
4. Report the body metric and its denominator/aggregation: In contrast, our method exhibits strong robustness to scale variations, avoiding these issues and achieving the highest success rates in both scenarios..
5. Re-run the body-reported ablation/failure condition: To verify the effectiveness of our strategy for injecting 3D information into the action head, we evaluate a variant following the approach of most 3D-based VLAs, where spatial tokens from the ESM ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 6 (3 Methodology), p. 4 (3 Methodology), p. 6 (3 Methodology); the primary result is directionally consistent at p. 8 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 FALCON, Spatial, Action mechanism이 2 reports the results on the Bridge-WidowX setup, where FALCON consistently outperforms all baselines and achieves ... 대비 In contrast, our method exhibits strong robustness to scale variations, avoiding these issues and achieving the highest success ...을 개선하고, For larger blocks, collisions frequently occur during the placement of the blue block, while smaller blocks ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
