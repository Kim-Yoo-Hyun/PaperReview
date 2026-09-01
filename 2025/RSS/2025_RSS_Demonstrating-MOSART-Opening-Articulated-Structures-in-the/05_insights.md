# Insights — Demonstrating MOSART: Opening Articulated Structures in the Real World

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (25 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p033.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p033.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Iyrropucrion - extractive body cue:** We considered two broad ways of putting together such a system: a modular approach and an end-to-end learning approach, bat ultimately favored a modular approach, ...
- **p. 4 / B. Generating Motion Plans - extractive body cue:** In contrast to these approaches, we develop a system that operates on novel object instances in novel environments in a zero-shot manner without requiring any ...
- **p. 1 / Front matter - extractive body cue:** g novel cabinets, drawers, and ovens
- **p. 1 / Front matter - extractive body cue:** Specifically, we develop MOSART, a MOdular System for opening ARTiculated structures, and conduct extensive testing
- **p. 2 / Abstract - extractive body cue:** ‘models developed in isolation struggle when faced with robot ‘centric viewpoints.
- **p. 20 / A. Robot Utility Models - extractive body cue:** We provide additional details about Robot Utility Models (RUM) [16].
- **Contribution anchor:** p. 2 (1. Iyrropucrion), p. 4 (B. Generating Motion Plans), p. 1 (Front matter), p. 1 (Front matter), p. 2 (Abstract), p. 20 (A. Robot Utility Models)

### Strongest assumption and failure boundary

- **p. 2 / 1. Iyrropucrion - extractive body cue:** Finally, we also consluct experiments to understand a) how MOSART compares to an end-to-end leaming approach, ) how sensitive MOSART is to the performance of ...
- **p. 3 / 1. Iyrropucrion - extractive body cue:** It is not as much a failure in estimating articulation parameters, but the detection of target objects and estimation of the handle location in 3D ...
- **p. 3 / 1. Iyrropucrion - extractive body cue:** In comparison, an imitation learning system will need to recollect a large amount of training data for tackling a new articulation type. * The failure ...
- **p. 2 / 1. Iyrropucrion - extractive body cue:** A major obstacle to realizing this vision lies in the lack of strong generalization capabilities: current systems struggle to adapt to novel objects and unfamiliar ...
- **p. 1 / Abstract - extractive body cue:** Our large-scale study reveals a number of surprising findings: a) modular systems outperform end-to-end learned systems for this task, even when the end-to-end learned systems ...
- **p. 10 / Discussion - extractive body cue:** Other failures were during execution, where the handle would slip out, and during navigation, where navigating ‘on carpets was less accurate than on tiles.
- **p. 9 / V. Limitations - extractive body cue:** Finally, there are limitations of the embodiment we use (e.g. it cannot reach cabinets high up, or exert enough force to pull open fridge doors).
- **Boundary to test:** Other failures were during execution, where the handle would slip out, and during navigation, where navigating ‘on carpets was less accurate than on tiles.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We considered two broad ways of putting together such a system: a modular approach and an end-to-end learning approach, bat ultimately favored a modular approach, Our approach, called MOSART for a MOdular ... | p. 2 (1. Iyrropucrion), p. 4 (B. Generating Motion Plans) |
| Reported outcome | Overall, our system achieves a 61% success rate across 31 unseen cabinets and drawers in unseen real world environments. | p. 7 (IV. EXPERIMENTS), p. 3 (Figure/Table caption) |
| Failure/limitation | Other failures were during execution, where the handle would slip out, and during navigation, where navigating ‘on carpets was less accurate than on tiles. | p. 10 (Discussion), p. 9 (V. Limitations) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `egocentric RGB-D, language/task goal, base-arm proprioception → map/object/contact state와 base-arm coordination decision → base motion plus arm/gripper action`.
- 이 논문의 재사용 가능한 지점은 We also add additional heads to Mask RCNN; however, rather than directly predicting 3D outputs from the RGB-D input, we adopt a two-stage approach involving 2D prediction from RGB images followed by ...를 Researchers have extensively looked at different aspects: a) construction of various datasets (from simulation (40, 14, 20], real world images [76, 36, 1], and real world 3D scans [2¢ 77), b) use ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 map/object/contact state와 base-arm coordination decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Other failures were during execution, where the handle would slip out, and during navigation, where navigating ‘on carpets was less accurate than on tiles.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We considered two broad ways of putting together such a system: a modular approach and an end-to-end learning approach, bat ultimately favored a modular approach, Our approach, called MOSART for a MOdular ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, mobile manipulation, articulated objects, real-world evaluation`.
- **Reading predecessor in the generated track queue:** AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Other failures were during execution, where the handle would slip out, and during navigation, where navigating ‘on carpets was less accurate than on tiles.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: In each test, the robot is placed approximately 1.5m from the target object with the camera oriented so as to have the target ‘object in view..
3. Compare against the body-reported baseline or a matched simpler baseline: This includes evaluating the quality of our MaskRCNN-based perception module (as well as a Detic-based perception model) on real world images, comparing APM to two recent articulation parameter prediction systems [53, 76], ....
4. Report the body metric and its denominator/aggregation: Overall, our system achieves a 61% success rate across 31 unseen cabinets and drawers in unseen real world environments..
5. Re-run the body-reported ablation/failure condition: This includes evaluating the quality of our MaskRCNN-based perception module (as well as a Detic-based perception model) on real world images, comparing APM to two recent articulation parameter prediction systems [53, 76], ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 20 (A. Robot Utility Models); the primary result is directionally consistent at p. 7 (IV. EXPERIMENTS), p. 3 (Figure/Table caption), p. 6 (IV. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 considered, broad, ways mechanism이 This includes evaluating the quality of our MaskRCNN-based perception module (as well as a Detic-based perception ... 대비 Overall, our system achieves a 61% success rate across 31 unseen cabinets and drawers in unseen real world ...을 개선하고, Other failures were during execution, where the handle would slip out, and during navigation, where navigating ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
