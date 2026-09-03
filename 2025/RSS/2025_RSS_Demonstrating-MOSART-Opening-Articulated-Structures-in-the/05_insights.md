# Insights — Demonstrating MOSART: Opening Articulated Structures in the Real World

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (25 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p033.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p033.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Iyrropucrion - extractive body cue:** We considered two broad ways of putting together such a system: a modular approach and an end-to-end learning approach, bat ultimately favored a modular approach, ...
- **p. 4 / B. Generating Motion Plans - extractive body cue:** In contrast to these approaches, we develop a system that operates on novel object instances in novel environments in a zero-shot manner without requiring any ...
- **p. 1 / body section boundary not confidently recovered - extractive body cue:** g novel cabinets, drawers, and ovens
- **p. 1 / body section boundary not confidently recovered - extractive body cue:** Specifically, we develop MOSART, a MOdular System for opening ARTiculated structures, and conduct extensive testing
- **p. 2 / Abstract - extractive body cue:** ‘models developed in isolation struggle when faced with robot ‘centric viewpoints.
- **p. 20 / A. Robot Utility Models - extractive body cue:** We provide additional details about Robot Utility Models (RUM) [16].
- **Contribution anchor:** p. 2 (1. Iyrropucrion), p. 4 (B. Generating Motion Plans), p. 1 (body section boundary not confidently recovered), p. 1 (body section boundary not confidently recovered), p. 2 (Abstract), p. 20 (A. Robot Utility Models)

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

- **Paper-specific interface:** We also add additional heads to Mask RCNN; however, rather than directly predicting 3D outputs from the RGB-D input, we adopt a two-stage approach involving 2D prediction from RGB images ... (p. 4, A. Predicting Articulation Parameters).
- **Paper-specific mechanism:** In contrast to these approaches, we develop a system that operates on novel object instances in novel environments in a zero-shot manner without requiring any privileged information. (p. 4, B. Generating Motion Plans).
- **Evidence boundary:** the reported outcome is We first present ‘our end-to-end system test results, evaluating MOSART on 31 novel drawers and cupboards across 10 buildings (Section IV-A), To see how a modular system compares to an ... (p. 6, IV. EXPERIMENTS); the relevant task/metric cue is Overall, our system achieves a 61% success rate across 31 unseen cabinets and drawers in unseen real world environments. (p. 7, IV. EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Other failures were during execution, where the handle would slip out, and during navigation, where navigating ‘on carpets was less accurate than on tiles. (p. 10, Discussion).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, mobile manipulation, articulated objects, real-world evaluation`.
- **Reading predecessor in the generated track queue:** AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Other failures were during execution, where the handle would slip out, and during navigation, where navigating ‘on carpets was less accurate than on tiles.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: We also add additional heads to Mask RCNN; however, rather than directly predicting 3D outputs from the RGB-D input, we adopt a two-stage approach involving 2D prediction from RGB images ... (p. 4, A. Predicting Articulation Parameters); preserve the objective/update rule: We provide additional details about Robot Utility Models (RUM) [16]. (p. 20, A. Robot Utility Models).
2. Use the paper-reported task/data/environment cue: We work with the Stretch RE2 robot. (p. 6, IV. EXPERIMENTS).
3. Compare against the reported or matched baseline: This includes evaluating the quality of our MaskRCNN-based perception module (as well as a Detic-based perception model) on real world images, comparing APM to two recent articulation parameter prediction systems ... (p. 6, IV. EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: Overall, our system achieves a 61% success rate across 31 unseen cabinets and drawers in unseen real world environments. (p. 7, IV. EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: This includes evaluating the quality of our MaskRCNN-based perception module (as well as a Detic-based perception model) on real world images, comparing APM to two recent articulation parameter prediction systems ... (p. 6, IV. EXPERIMENTS); if none is reported, design one around: Other failures were during execution, where the handle would slip out, and during navigation, where navigating ‘on carpets was less accurate than on tiles. (p. 10, Discussion).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 4 (B. Generating Motion Plans), p. 1 (Body text (section boundary not confidently recovered)), match the reported outcome at p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), and measure the boundary at p. 10 (Discussion), p. 9 (V. Limitations).

## Falsifiable research question

Under the paper's stated interface (We also add additional heads to Mask RCNN; however, rather than directly predicting 3D outputs from the RGB-D input, we adopt a ...), does the paper-specific mechanism (In contrast to these approaches, we develop a system that operates on novel object instances in novel environments in a zero-shot manner ...) retain the reported evaluation outcome (Overall, our system achieves a 61% success rate across 31 unseen cabinets and drawers in unseen real world ...) when tested against the paper's strongest explicit boundary (Other failures were during execution, where the handle would slip out, and during navigation, where navigating ‘on carpets ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Overall, our system achieves a 61% success rate across 31 unseen cabinets and drawers in unseen real world ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (25 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In contrast to these approaches, we develop a system that operates on novel object instances in novel environments in a zero-shot manner without requiring any privileged information. (p. 4, B. Generating Motion Plans).
- **Paper-supported outcome:** We first present ‘our end-to-end system test results, evaluating MOSART on 31 novel drawers and cupboards across 10 buildings (Section IV-A), To see how a modular system compares to an ... (p. 6, IV. EXPERIMENTS).
- **Strongest explicit boundary:** Other failures were during execution, where the handle would slip out, and during navigation, where navigating ‘on carpets was less accurate than on tiles. (p. 10, Discussion).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
