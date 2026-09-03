# Insights — Dynam3D: Dynamic Layered 3D Tokens Empower VLM for Vision-and-Language Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=s6k9l5yX8e; PDF retrieval source: https://proceedings.neurips.cc/paper_files/paper/2025/file/e1a1847e39a7b79b41199176b152f0e6-Paper-Conference.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** In summary, our main contributions include: • We propose Dynam3D, a multi-level patch-instance-zone 3D representation model that performs online 3D instance and zone-level encoding and ...
- **p. 2 / 1 Introduction - extractive body cue:** We propose Dynam3D to alleviate the limitations mentioned above.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we propose Dynam3D, a dynamic layered 3D representation model that leverages language-aligned, generalizable, and hierarchical 3D representations as visual input to ...
- **p. 1 / 1 Introduction - extractive body cue:** As illustrated in Figure 1(a), recent works [5-7] have predominantly focused on using video-based large models [8-10] to develop monocular VLN systems.
- **p. 2 / 1 Introduction - extractive body cue:** These rendered 3D patch features combined with instance and zone representations serve as visual input to the 3D Vision-Language Model (VLM).
- **p. 1 / Abstract - extractive body cue:** By leveraging large-scale 3D-language pretraining and task-specific adaptation, our Dynam3D sets new state-of-the-art performance on VLN benchmarks including R2R-CE, REVERIE-CE and NavRAG-CE under monocular settings.
- **Contribution anchor:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** 2) These models lack mechanisms for structured scene memory.
- **p. 1 / 1 Introduction - extractive body cue:** Despite these recent advances, several limitations still remain: 1) Video-based models struggle to capture spatial geometry and semantics in large-scale 3D environments.
- **p. 2 / 1 Introduction - extractive body cue:** We propose Dynam3D to alleviate the limitations mentioned above.
- **p. 2 / 1 Introduction - extractive body cue:** As a result, this enables high-level comprehension of layouts, e.g. bedrooms, kitchens, etc that instance-level features alone cannot capture. our Dynam3D updates the scene dynamically ...
- **p. 10 / 4 Experiments - extractive body cue:** This highlights the limitations of naive CLIP feature distillation for 3D instance supervision.
- **p. 10 / Figure/Table caption - extractive body cue:** Table 7: Robustness study on the R2R-CE Val Unseen benchmark with the simulated SLAM noise and depth noise. SLAM Noise Depth Noise NE↓ OSR↑ SR↑ ...
- **p. 8 / 4 Experiments - extractive body cue:** However, this does not conflict with its advantage of maintaining lifelong memory.
- **Boundary to test:** Figure 1: Different vision-language large models for monocular VLN tasks. Compared to previous video-based representations (a), our Dynam3D (b) adopts dynamic hierarchical 3D representations offering advantages in spatial geometry and s ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, our main contributions include: • We propose Dynam3D, a multi-level patch-instance-zone 3D representation model that performs online 3D instance and zone-level encoding and real-time hierarchical updates in dynamic environme ... | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | Our Dynam3D still demonstrates substantial improvements, outperforming NaVid by over 13% in Success Rate (SR) on REVERIE-CE and by over 5% on NavRAG-CE. | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Failure/limitation | Figure 1: Different vision-language large models for monocular VLN tasks. Compared to previous video-based representations (a), our Dynam3D (b) adopts dynamic hierarchical 3D representations offering advantages in spatial geometry and s ... | p. 2 (Figure/Table caption), p. 10 (4 Experiments) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 To address these limitations, we propose Dynam3D, a dynamic layered 3D representation model that leverages language-aligned, generalizable, and hierarchical 3D representations as visual input to train 3D-VLM in navigation action prediction.를 Instruction: "Please go to the kitchen and take the bread out of the microwave for me." … Video-Language Large Model … Action 3D-Language Large Model Action • Large-scale scene exploration and memory ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 1: Different vision-language large models for monocular VLN tasks. Compared to previous video-based representations (a), our Dynam3D (b) adopts dynamic hierarchical 3D representations offering advantages in spatial geometry and s ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, our main contributions include: • We propose Dynam3D, a multi-level patch-instance-zone 3D representation model that performs online 3D instance and zone-level encoding and real-time hierarchical updates in dynamic environme ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `Vision-Language Model, 3D Vision, Navigation`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 1: Different vision-language large models for monocular VLN tasks. Compared to previous video-based representations (a), our Dynam3D (b) adopts dynamic hierarchical 3D representations offering advantages in spatial geometry and s ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Methods Pre-exploration Lifelong Memory R2R-CE Val REVERIE-CE Val NE↓OSR↑SR↑SPL↑NE↓OSR↑SR↑SPL↑ NaVid [5] × × 5.47 49.1 37.4 35.9 6.74 36.3 26.6 20.8 g3D-LF [15] × × 5.70 59.5 47.2 34.6 6.50 41.6 34.4 ....
3. Compare against the body-reported baseline or a matched simpler baseline: Compared to prior state-of-the-art methods, e.g., g3D-LF and Uni-NaVid, our Dynam3D achieves an improvement of nearly 5% in navigation success rate (SR)..
4. Report the body metric and its denominator/aggregation: As shown in Table 7, even with the simultaneous addition of simulated SLAM and depth noise, the navigation success rate (SR) only decreased by approximately 2% (comparing the last row to the ....
5. Re-run the body-reported ablation/failure condition: 4.6 Ablation Study Table 6: Ablation Study of Dynam3D on R2R-CE and REVERIE-CE Val Unseen benchmarks..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction); the primary result is directionally consistent at p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, main, contributions mechanism이 Compared to prior state-of-the-art methods, e.g., g3D-LF and Uni-NaVid, our Dynam3D achieves an improvement of nearly ... 대비 As shown in Table 7, even with the simultaneous addition of simulated SLAM and depth noise, the navigation ...을 개선하고, Figure 1: Different vision-language large models for monocular VLN tasks. Compared to previous video-based representations (a), ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
