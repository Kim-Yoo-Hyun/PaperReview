# Insights — JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=RnuB0Nlbd5; PDF retrieval source: https://openreview.net/pdf/3a4cf4bcb2788c66a1d7b5ee498986d37ab4fa87.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1 INTRODUCTION - extractive body cue:** In summary, our contributions are as follows: • We introduce a novel dual implicit memory paradigm for VLN.
- **p. 4 / 3 METHOD - extractive body cue:** To address these challenges, we introduce the VGGT as a spatial geometry encoder and propose a novel dual implicit memory paradigm for VLN research in ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To this end, we introduce JanusVLN, a dual implicit memory framework for VLN that features both spatialgeometric and visual-semantic memory in Figure 1.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Inspired by the human brain's hemispheric specialization for navigation, where the left hemisphere handles semantic understanding and the right manages 3D spatial cognition to form ...
- **p. 6 / 3 METHOD - extractive body cue:** Building upon the dual implicit memory paradigm, we propose JanusVLN in Figure 2, enhances the spatial understanding capabilities without requiring costly 3D data (e.g., depth).
- **p. 4 / 3 METHOD - extractive body cue:** VGGT (Wang et al., 2025a), which is based on a transformer feed-forward architecture, comprises three key components: an encoder for extracting single-image feature, a fusion ...
- **p. 5 / 3 METHOD - extractive body cue:** These KV, derived from the output of attention modules such as transformers, constitute high-level semantic abstractions and structured representations of the past environment.
- **Contribution anchor:** p. 3 (1 INTRODUCTION), p. 4 (3 METHOD), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 6 (3 METHOD), p. 4 (3 METHOD)

### Strongest assumption and failure boundary

- **p. 3 / 1 INTRODUCTION - extractive body cue:** Inspired by human cognitive science, this framework simultaneously captures visual semantics and spatial geometry to overcome the inherent limitations of existing navigation LLM. • We ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This makes it exceedingly difficult for the model to extract critical information from a vast, cluttered, and fragmented memory, thereby leading to severe inefficiency.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Navigation is an inherently 3D physical interaction, yet the visual encoders of existing VLA models almost exclusively inherit the CLIP paradigm pre-trained on 2D image-text ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Unlike the visual encoders of general MLLMs, which are predominantly trained on 2D image-text data, this spatial geometry model is typically trained on pixel-3D point ...
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 9: Visualization and presentation of the types of failure cases. on relatively simple instructions (1-150 words). However, their performance declines on moderately complex instructions ...
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 8: Performance on various instruction lengths/complexity. larger-scale external datasets, akin to the approaches of StreamVLN and NaVILA, is reserved for future work to construct ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** Finally, when we omit the preservation of the initial window's KV, a slight performance degradation is observed, indicating that the first few frames of memory ...
- **Boundary to test:** Figure 9: Visualization and presentation of the types of failure cases. on relatively simple instructions (1-150 words). However, their performance declines on moderately complex instructions (150-400 words), indicating a need to enhanc ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, our contributions are as follows: • We introduce a novel dual implicit memory paradigm for VLN. | p. 3 (1 INTRODUCTION), p. 4 (3 METHOD) |
| Reported outcome | Compared to methods utilizing multiple input types like panoramic views and odometry, JanusVLN achieves a 10.5-35.5 improvement in SR using only a single RGB input, demonstrating the effectiveness of our approach. | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Failure/limitation | Figure 9: Visualization and presentation of the types of failure cases. on relatively simple instructions (1-150 words). However, their performance declines on moderately complex instructions (150-400 words), indicating a need to enhanc ... | p. 21 (Figure/Table caption), p. 20 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 Vision-and-Language Navigation (VLN) is a foundational task in embodied AI, requiring an agent to navigate through unseen environments guided by visual inputs and natural language instructions.를 Upon executing the action at`1, the agent receives a new observation xt`1.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 9: Visualization and presentation of the types of failure cases. on relatively simple instructions (1-150 words). However, their performance declines on moderately complex instructions (150-400 words), indicating a need to enhanc ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, our contributions are as follows: • We introduce a novel dual implicit memory paradigm for VLN.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `Vision-Language Model, 3D Vision, Navigation, semantic`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 9: Visualization and presentation of the types of failure cases. on relatively simple instructions (1-150 words). However, their performance declines on moderately complex instructions (150-400 words), indicating a need to enhanc ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: These datasets comprise trajectories collected from Matterport3D (Chang et al., 2017) scenes using the Habitat simulator (Savva et al., 2019)..
3. Compare against the body-reported baseline or a matched simpler baseline: Consistent with prior work (Cheng et al., 2025; Dai et al., 2025; Yin et al., 2025; Lu et al., 2024), we report performance on the unseen splits using standard VLN metrics, including ....
4. Report the body metric and its denominator/aggregation: Consistent with prior work (Cheng et al., 2025; Dai et al., 2025; Yin et al., 2025; Lu et al., 2024), we report performance on the unseen splits using standard VLN metrics, including ....
5. Re-run the body-reported ablation/failure condition: We provide an ablation study in Table 4 to investigate the effect of introducing additional encoders..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3 METHOD), p. 5 (3 METHOD), p. 4 (3 METHOD); the primary result is directionally consistent at p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, contributions, follows mechanism이 Consistent with prior work (Cheng et al., 2025; Dai et al., 2025; Yin et al., 2025; ... 대비 Consistent with prior work (Cheng et al., 2025; Dai et al., 2025; Yin et al., 2025; Lu et ...을 개선하고, Figure 9: Visualization and presentation of the types of failure cases. on relatively simple instructions (1-150 ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
