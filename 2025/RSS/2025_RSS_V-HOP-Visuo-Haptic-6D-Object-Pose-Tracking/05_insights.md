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

- **Closed-loop position:** `tactile image/force, vision과 proprioceptive history → contact geometry, force state 또는 latent dynamics → grasp/contact action, force command 또는 object motion`.
- 이 논문의 재사용 가능한 지점은 A, Problem Definition We tackle the model-based visu tracking problem, assuming access to: + Visual observations: An RGB-D sensor observes the object in the environment. + Haptic feedback: The object is manipulated ...를 2) A sequence of RGB-D images O ~ {O,}{_. where each observation O, = 1;,.Dj] includes an RGB image I, and a depth map D,로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 contact geometry, force state 또는 latent dynamics가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 1) If the grasp attempt fails, the robot must detect the failure based on the real-time object pose and reattempt the grasp.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: First, we introduce a novel unified haptic representation that facilitates cross-embodiment learning.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, visuo-haptic perception, 6D pose, tactile sensing, state estimation, manipulation`.
- **Reading predecessor in the generated track queue:** DexterityGen: Foundation Controller for Unprecedented Dexterity (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** PP-Tac: Paper Picking Using Omnidirectional Tactile Feedback in Dexterous Robotic Hands (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 1) If the grasp attempt fails, the robot must detect the failure based on the real-time object pose and reattempt the grasp.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Our synthesized dataset exemplifies this principle and supports our robust real-world performance..
3. Compare against the body-reported baseline or a matched simpler baseline: V-HOP achieves 1 32% lower ADD-S error compared to NeuralFeels and has a similar ADD-S-0.1d score..
4. Report the body metric and its denominator/aggregation: ‘TABLE VI: Success rate on bimanual handover task:.
5. Re-run the body-reported ablation/failure condition: For instance, a human may move the object during task execution, remove it from the gripper, or reposition it on the table (Fig..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (III. MeTHODOLOGY), p. 3 (III. MeTHODOLOGY); the primary result is directionally consistent at p. 7 (experiment), p. 7 (experiment), p. 8 (B. Bimanual Handover Experiment); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 First, introduce, novel mechanism이 V-HOP achieves 1 32% lower ADD-S error compared to NeuralFeels and has a similar ADD-S-0.1d score. 대비 ‘TABLE VI: Success rate on bimanual handover task:을 개선하고, 1) If the grasp attempt fails, the robot must detect the failure based on the real-time ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
