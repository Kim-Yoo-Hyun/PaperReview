# Insights — Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=5i888dLp8N; PDF retrieval source: https://openreview.net/pdf/95685162fa940bca32702d659b96eebf84138a75.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** Based on these insights, we introduce SOMA, a VLA framework for out-of-vision manipulation that equips the robot with persistent spatial memory for reasoning and action.
- **p. 2 / 1. Introduction - extractive body cue:** In particular, integrating angular-wise observations into a coherent spatial-semantic memory enables globally consistent reasoning and effective manipulation even when task-relevant objects are temporarily out of ...
- **p. 3 / 3. Method - extractive body cue:** By maintaining a globally consistent spatial memory, SOMA enables robust reasoning and manipulation even when task-relevant objects lie outside the current field of view.
- **p. 1 / 1. Introduction - extractive body cue:** However, most existing VLAs are developed under fixedview tabletop manipulation setups, typically relying on a single static camera or a third-person viewpoint.
- **p. 1 / 1. Introduction - extractive body cue:** The development of VLAs have become a central direction in robotic action modeling research (Zhao et al., 2025; Chen et al., 2025c; Kim et al., ...
- **p. 3 / 3.1. Spatial Memory Construction - extractive body cue:** Each sampled frame fi ∈˜V is processed by a unified perception pipeline consisting of: (1) a geometry prior network (VGGT (Wang et al., 2025b)) for ...
- **p. 3 / 3. Method - extractive body cue:** During manipulation, the model receives the current observation ot c, the user instruction, robot states, and a noised action sequence, where c ∈{l, r, h} ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1. Spatial Memory Construction)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** Without a mechanism to maintain a persistent spatial representation of the scene, the perception-action loop becomes strictly viewdependent: when a target object is not observed, ...
- **p. 2 / 1. Introduction - extractive body cue:** Addressing this gap requires mechanisms that both acquire spatial evidence beyond the current view and retain it in a persistent scene representation.
- **p. 1 / 1. Introduction - extractive body cue:** However, most existing VLAs are developed under fixedview tabletop manipulation setups, typically relying on a single static camera or a third-person viewpoint.
- **p. 1 / 1. Introduction - extractive body cue:** As a result, these models implicitly operate under a view-bound assumption-namely, that the object referenced in the instruction is visible within the robot's current camera ...
- **p. 20 / Figure/Table caption - extractive body cue:** Table 15. Failure mode analysis on the fully observable RoboCasa Tabletop GR1 simulation (50 sampled failures, 10 per category). Under full observability, failures reflect limitations ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Illustration of the Out-of-Vision (OOV) limitation in existing VLA models. Most VLAs rely on purely reactive percep- tion-actions are driven only by what ...
- **p. 8 / 5. Conclusion - extractive body cue:** We propose SOMA, a spatial memory framework for VisionLanguage-Action models that addresses the fundamental limitation of view-bound perception in out-of-vision manip8
- **Boundary to test:** Table 15. Failure mode analysis on the fully observable RoboCasa Tabletop GR1 simulation (50 sampled failures, 10 per category). Under full observability, failures reflect limitations of the memory mechanism itself rather than ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Based on these insights, we introduce SOMA, a VLA framework for out-of-vision manipulation that equips the robot with persistent spatial memory for reasoning and action. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | In Figure 4, SOMA achieves the highest success rates across all five real-world out-of-vision (OOV) manipulation tasks. | p. 7 (4.3. Real World Results), p. 7 (4.3. Real World Results) |
| Failure/limitation | Table 15. Failure mode analysis on the fully observable RoboCasa Tabletop GR1 simulation (50 sampled failures, 10 per category). Under full observability, failures reflect limitations of the memory mechanism itself rather than ... | p. 20 (Figure/Table caption), p. 1 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 These systems typically extend large-scale pre-trained Multimodal Large Language Models (MLLMs) (Bjorck et al., 2025; Yang et al., 2025a) with an action head or specialized action module that maps multimodal inputs-such as ...를 During manipulation, the model receives the current observation ot c, the user instruction, robot states, and a noised action sequence, where c ∈{l, r, h} denotes the left arm, right arm, and ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Table 15. Failure mode analysis on the fully observable RoboCasa Tabletop GR1 simulation (50 sampled failures, 10 per category). Under full observability, failures reflect limitations of the memory mechanism itself rather than ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Based on these insights, we introduce SOMA, a VLA framework for out-of-vision manipulation that equips the robot with persistent spatial memory for reasoning and action.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Robotics, 3D Vision`.
- **Reading predecessor in the generated track queue:** ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Table 15. Failure mode analysis on the fully observable RoboCasa Tabletop GR1 simulation (50 sampled failures, 10 per category). Under full observability, failures reflect limitations of the memory mechanism itself rather than ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: SimplerEnv offers a standardized real-to-sim benchmark for evaluating policy success rates across simulated environments reflecting real-world robotic systems (Zitkovich et al., 2023)..
3. Compare against the body-reported baseline or a matched simpler baseline: Table 5. Ablation study on different components of the proposed memory design. "Geo." and "Obj." denote Geometric cues and object semantics, respectively. SimplerEnv Results. Table 4 reports the performance com- parison across ....
4. Report the body metric and its denominator/aggregation: Table 10. Detailed Ablation studies on Robocasa Tabletop GR-1 benchmark. We compare different Update Strategies, Retrieval Modules, and Memory Representations. Reported values are success rates (%). "SimEMA" denotes the normal EMA updat ....
5. Re-run the body-reported ablation/failure condition: Table 2. Ablation study on scan-based exploration and spatial mem- ory for real-world OOV manipulation. Scan+GR00T performs head scanning and uses the detected target frame as a fixed visual input for a ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (3.1. Spatial Memory Construction), p. 3 (3. Method), p. 4 (3.1. Spatial Memory Construction); the primary result is directionally consistent at p. 7 (4.3. Real World Results), p. 7 (4.3. Real World Results), p. 8 (4.4. Simulation Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 insights, introduce, SOMA mechanism이 Table 5. Ablation study on different components of the proposed memory design. "Geo." and "Obj." denote ... 대비 Table 10. Detailed Ablation studies on Robocasa Tabletop GR-1 benchmark. We compare different Update Strategies, Retrieval Modules, and ...을 개선하고, Table 15. Failure mode analysis on the fully observable RoboCasa Tabletop GR1 simulation (50 sampled failures, ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
