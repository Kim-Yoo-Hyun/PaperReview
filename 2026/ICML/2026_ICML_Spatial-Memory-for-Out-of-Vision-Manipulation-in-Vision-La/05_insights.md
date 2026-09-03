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

- **Paper-specific interface:** During manipulation, the model receives the current observation ot c, the user instruction, robot states, and a noised action sequence, where c ∈{l, r, h} denotes the left arm, right ... (p. 3, 3. Method).
- **Paper-specific mechanism:** Based on these insights, we introduce SOMA, a VLA framework for out-of-vision manipulation that equips the robot with persistent spatial memory for reasoning and action. (p. 2, 1. Introduction).
- **Evidence boundary:** the reported outcome is Table 5. Ablation study on different components of the proposed memory design. "Geo." and "Obj." denote Geometric cues and object semantics, respectively. SimplerEnv Results. Table 4 reports the performance com- ... (p. 8, Figure/Table caption); the relevant task/metric cue is In contrast, SOMA maintains consistently higher success rates across both Pick and Place stages, with the performance gap widening as task complexity increases. (p. 7, 4.3. Real World Results). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** The fixed-head variant fails once either the target or the goal leaves the field of view, confirming the brittleness of view-bound policies under partial observability. (p. 7, 4.3. Real World Results).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Robotics, 3D Vision`.
- **Reading predecessor in the generated track queue:** ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Table 15. Failure mode analysis on the fully observable RoboCasa Tabletop GR1 simulation (50 sampled failures, 10 per category). Under full observability, failures reflect limitations of the memory mechanism itself rather than ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: During manipulation, the model receives the current observation ot c, the user instruction, robot states, and a noised action sequence, where c ∈{l, r, h} denotes the left arm, right ... (p. 3, 3. Method); preserve the objective/update rule: New observations from the head view ot h are incorporated to update M0 into ˆ Mt through Dynamic Memory Refinement, which performs similarity-aware fusion to preserve global consistency while accommodating ... (p. 3, 3. Method).
2. Use the paper-reported task/data/environment cue: SimplerEnv offers a standardized real-to-sim benchmark for evaluating policy success rates across simulated environments reflecting real-world robotic systems (Zitkovich et al., 2023). (p. 6, 4.1. Benchmarks).
3. Compare against the reported or matched baseline: No-Scan SOMA slightly outperforms Scan+GR00T despite using only a single-view initialization, highlighting the benefit of an explicit memory structure even without multi-view coverage. (p. 7, 4.3. Real World Results).
4. Report the body metric with its denominator and aggregation: In contrast, SOMA maintains consistently higher success rates across both Pick and Place stages, with the performance gap widening as task complexity increases. (p. 7, 4.3. Real World Results).
5. Re-run the reported ablation or stress/failure condition: The fixed-head variant fails once either the target or the goal leaves the field of view, confirming the brittleness of view-bound policies under partial observability. (p. 7, 4.3. Real World Results); if none is reported, design one around: The fixed-head variant fails once either the target or the goal leaves the field of view, confirming the brittleness of view-bound policies under partial observability. (p. 7, 4.3. Real World Results).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1. Introduction), p. 2 (1. Introduction), match the reported outcome at p. 8 (Figure/Table caption), p. 8 (4.3. Real World Results), p. 8 (4.4. Simulation Results), and measure the boundary at p. 7 (4.3. Real World Results), p. 2 (1. Introduction).

## Falsifiable research question

Under the paper's stated interface (During manipulation, the model receives the current observation ot c, the user instruction, robot states, and a noised action sequence, where c ...), does the paper-specific mechanism (Based on these insights, we introduce SOMA, a VLA framework for out-of-vision manipulation that equips the robot with persistent spatial memory for ...) retain the reported evaluation outcome (In contrast, SOMA maintains consistently higher success rates across both Pick and Place stages, with the performance gap ...) when tested against the paper's strongest explicit boundary (The fixed-head variant fails once either the target or the goal leaves the field of view, confirming the ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (In contrast, SOMA maintains consistently higher success rates across both Pick and Place stages, with the performance gap ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (24 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Based on these insights, we introduce SOMA, a VLA framework for out-of-vision manipulation that equips the robot with persistent spatial memory for reasoning and action. (p. 2, 1. Introduction).
- **Paper-supported outcome:** Table 5. Ablation study on different components of the proposed memory design. "Geo." and "Obj." denote Geometric cues and object semantics, respectively. SimplerEnv Results. Table 4 reports the performance com- ... (p. 8, Figure/Table caption).
- **Strongest explicit boundary:** The fixed-head variant fails once either the target or the goal leaves the field of view, confirming the brittleness of view-bound policies under partial observability. (p. 7, 4.3. Real World Results).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
