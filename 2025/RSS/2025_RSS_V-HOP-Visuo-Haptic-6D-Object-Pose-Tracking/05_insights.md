# Insights — V-HOP: Visuo-Haptic 6D Object Pose Tracking

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p037.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p037.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1. INTRODUCTION - extractive body cue:** First, we introduce a novel unified haptic representation that facilitates cross-embodiment learning.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** To address these challenges, we propose V-HOP (Fig.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Second, we propose 4 transformer-based object pose tracker to fuse visual and haptic features.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Our method demonstrates remarkable robustness and significantly outperforms FoundationPose, which could lose object tracks entirely (Fig.
- **p. 3 / III. MeTHODOLOGY - extractive body cue:** Later, we introduce our visuo-haptic model and how it is trained.
- **p. 3 / III. MeTHODOLOGY - extractive body cue:** We first outline the core representations used in our haptic modality: gripper and object representations.
- **Contribution anchor:** p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 3 (III. MeTHODOLOGY), p. 3 (III. MeTHODOLOGY)

### Strongest assumption and failure boundary

- **p. 1 / 1. INTRODUCTION - extractive body cue:** (i) Domain generalization: Compared to visual-only baselines, visuo-tactile approaches struggle to generalize, hindered by insufficient data diversity and model scalability.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** To address these challenges, we propose V-HOP (Fig.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** In this section, we first define the problem formally and then review existing haptic representations and our proposed unified representation,
- **p. 2 / 1. INTRODUCTION - extractive body cue:** based visual pose tracking problem [66, 7]. while the inputs
- **p. 7 / B. Bimanual Handover Experiment - extractive body cue:** 1) If the grasp attempt fails, the robot must detect the failure based on the real-time object pose and reattempt the grasp.
- **p. 8 / C. Can-in-Mug Experiment - extractive body cue:** Successful execution hinges on precise pose estimation for both objects, as any noise in their poses can lead to failure.
- **p. 7 / B. Bimanual Handover Experiment - extractive body cue:** Inaccurate tracking results could lead to collision during the handover.
- **Boundary to test:** 1) If the grasp attempt fails, the robot must detect the failure based on the real-time object pose and reattempt the grasp.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | First, we introduce a novel unified haptic representation that facilitates cross-embodiment learning. | p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION) |
| Reported outcome | Our results show that \V-HOP consistently outperforms FoundationPose in both ADD and ADD-S metrics under different levels of occlusion. ‘These results underscore the importance of integrating visual and haptic information to improve ... | p. 7 (experiment), p. 7 (experiment) |
| Failure/limitation | 1) If the grasp attempt fails, the robot must detect the failure based on the real-time object pose and reattempt the grasp. | p. 7 (B. Bimanual Handover Experiment), p. 8 (C. Can-in-Mug Experiment) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Accurately tracking object poses is a core capability for robotic manipulation, and would enable contact-tich and dexterous manipulations with efficent imitation or reinforcement learning (68, 31, 23]. (p. 1, 1. INTRODUCTION).
- **Paper-specific mechanism:** First, we introduce a novel unified haptic representation that facilitates cross-embodiment learning. (p. 1, 1. INTRODUCTION).
- **Evidence boundary:** the reported outcome is Our results show that \V-HOP consistently outperforms FoundationPose in both ADD and ADD-S metrics under different levels of occlusion. ‘These results underscore the importance of integrating visual and haptic information ... (p. 7, experiment); the relevant task/metric cue is V-HOP achieves 1 32% lower ADD-S error compared to NeuralFeels and has a similar ADD-S-0.1d score. (p. 7, experiment). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** 1) If the grasp attempt fails, the robot must detect the failure based on the real-time object pose and reattempt the grasp. (p. 7, B. Bimanual Handover Experiment).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, visuo-haptic perception, 6D pose, tactile sensing, state estimation, manipulation`.
- **Reading predecessor in the generated track queue:** DexterityGen: Foundation Controller for Unprecedented Dexterity (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** PP-Tac: Paper Picking Using Omnidirectional Tactile Feedback in Dexterous Robotic Hands (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 1) If the grasp attempt fails, the robot must detect the failure based on the real-time object pose and reattempt the grasp.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Accurately tracking object poses is a core capability for robotic manipulation, and would enable contact-tich and dexterous manipulations with efficent imitation or reinforcement learning (68, 31, 23]. (p. 1, 1. INTRODUCTION); preserve the objective/update rule: Later, we introduce our visuo-haptic model and how it is trained. (p. 3, III. MeTHODOLOGY).
2. Use the paper-reported task/data/environment cue: Our synthesized dataset exemplifies this principle and supports our robust real-world performance. (p. 5, A. Multi-embodied Dataset).
3. Compare against the reported or matched baseline: V-HOP achieves 1 32% lower ADD-S error compared to NeuralFeels and has a similar ADD-S-0.1d score. (p. 7, experiment).
4. Report the body metric with its denominator and aggregation: V-HOP achieves 1 32% lower ADD-S error compared to NeuralFeels and has a similar ADD-S-0.1d score. (p. 7, experiment).
5. Re-run the reported ablation or stress/failure condition: For instance, a human may move the object during task execution, remove it from the gripper, or reposition it on the table (Fig. (p. 7, B. Bimanual Handover Experiment); if none is reported, design one around: 1) If the grasp attempt fails, the robot must detect the failure based on the real-time object pose and reattempt the grasp. (p. 7, B. Bimanual Handover Experiment).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), match the reported outcome at p. 7 (experiment), p. 7 (experiment), p. 8 (Figure/Table caption), and measure the boundary at p. 7 (B. Bimanual Handover Experiment), p. 8 (C. Can-in-Mug Experiment).

## Falsifiable research question

Under the paper's stated interface (Accurately tracking object poses is a core capability for robotic manipulation, and would enable contact-tich and dexterous manipulations with efficent imitation or ...), does the paper-specific mechanism (First, we introduce a novel unified haptic representation that facilitates cross-embodiment learning.) retain the reported evaluation outcome (V-HOP achieves 1 32% lower ADD-S error compared to NeuralFeels and has a similar ADD-S-0.1d score.) when tested against the paper's strongest explicit boundary (1) If the grasp attempt fails, the robot must detect the failure based on the real-time object pose ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (V-HOP achieves 1 32% lower ADD-S error compared to NeuralFeels and has a similar ADD-S-0.1d score.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** First, we introduce a novel unified haptic representation that facilitates cross-embodiment learning. (p. 1, 1. INTRODUCTION).
- **Paper-supported outcome:** Our results show that \V-HOP consistently outperforms FoundationPose in both ADD and ADD-S metrics under different levels of occlusion. ‘These results underscore the importance of integrating visual and haptic information ... (p. 7, experiment).
- **Strongest explicit boundary:** 1) If the grasp attempt fails, the robot must detect the failure based on the real-time object pose and reattempt the grasp. (p. 7, B. Bimanual Handover Experiment).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
