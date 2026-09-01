# Insights — Tactile-Driven Non-Prehensile Object Manipulation via Extrinsic Contact Mode Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p135.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p135.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 5 / IV. METHODOLOGY - extractive body cue:** The key contribution of our method is to formulate the contact trajectory optimization precisely to address these requirements while also being amenable to gradient-based optimization ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** An integral part of our method is the use of tactile sensors.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our method is able to produce a variety of "manipulation skills" and is amenable to gradient-based optimization by exploiting differentiability within contact modes (e.g., specifications ...
- **p. 3 / IV. METHODOLOGY - extractive body cue:** Our method is composed of 4 core components: i) a stateestimation pipeline using the feedback from the tactile sensor to estimate object pose and extrinsic ...
- **p. 5 / IV. METHODOLOGY - extractive body cue:** Trajectory Optimization Overview: Given a desired trajectory of the extrinsic object {xeo,k}K k=1 as well as the contact modes {ck}K k=1, our method optimizes the ...
- **p. 3 / IV. METHODOLOGY - extractive body cue:** The main contributions of our work are in components (iii) and (iv) where we augment the model in (ii) with contact-aware constraints for object poses ...
- **p. 5 / IV. METHODOLOGY - extractive body cue:** Extrinsic Contact Trajectory Optimization The goal of the controller is to generate a trajectory of endeffector and grasped object poses that results in the desired ...
- **Contribution anchor:** p. 5 (IV. METHODOLOGY), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY), p. 3 (IV. METHODOLOGY)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** These failures are due to the nonlinear, discontinuous, and multimodal nature of contact interactions.
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** The key technical challenges are computing trajectories that obey the many unilateral and hybrid contact constraints, kinematic constraints imposed by geometry, accounting for the compliance ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we consider the class of problems in which the robot is tasked with using an object grasped with tactile sensors to: i) ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** This makes our approach more robust to uncertainty and accessible given the lower technical barrier to entery.
- **p. 10 / V. EXPERIMENTS AND RESULTS - extractive body cue:** Furthermore, our approach does not reason about the physical limitations of the bubbles in terms of achievable forces and torques.
- **p. 10 / V. EXPERIMENTS AND RESULTS - extractive body cue:** DISCUSSION, LIMITATIONS, AND FUTURE WORK In this paper, we proposed an approach to extrinsic object manipulation leveraging tactile sensor compliance, tactile sensor measurements, and contact ...
- **p. 6 / V. EXPERIMENTS AND RESULTS - extractive body cue:** In this instance, the contacts between the object and the environment must be sticking, i.e. fc,i ∈int Fc,i. • Grasped Object Pivoting: The goal is ...
- **Boundary to test:** Furthermore, our approach does not reason about the physical limitations of the bubbles in terms of achievable forces and torques.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The key contribution of our method is to formulate the contact trajectory optimization precisely to address these requirements while also being amenable to gradient-based optimization and capable of producing a variety of ... | p. 5 (IV. METHODOLOGY), p. 2 (I. INTRODUCTION) |
| Reported outcome | While the current model yields satisfactory results, exploring higher-dimensional models with improved accuracy could further enhance performance. | p. 10 (V. EXPERIMENTS AND RESULTS), p. 7 (V. EXPERIMENTS AND RESULTS) |
| Failure/limitation | Furthermore, our approach does not reason about the physical limitations of the bubbles in terms of achievable forces and torques. | p. 10 (V. EXPERIMENTS AND RESULTS), p. 10 (V. EXPERIMENTS AND RESULTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `tactile image/force, vision과 proprioceptive history → contact geometry, force state 또는 latent dynamics → grasp/contact action, force command 또는 object motion`.
- 이 논문의 재사용 가능한 지점은 Our method is composed of 4 core components: i) a stateestimation pipeline using the feedback from the tactile sensor to estimate object pose and extrinsic contacts; ii) a passive compliance model for ...를 Here, we use high-resolution and highly deformable tactile sensors (Soft Bubbles [2]) because they: i) allow for state-estimation that provides key feedback for controls that would not be available without the sensors, ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 contact geometry, force state 또는 latent dynamics가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Furthermore, our approach does not reason about the physical limitations of the bubbles in terms of achievable forces and torques.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: The key contribution of our method is to formulate the contact trajectory optimization precisely to address these requirements while also being amenable to gradient-based optimization and capable of producing a variety of ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, contact-rich manipulation, tactile sensing, non-prehensile manipulation`.
- **Reading predecessor in the generated track queue:** Global Planning for Contact-Rich Manipulation via Local Smoothing of Quasi-Dynamic Contact Models (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** RoboPack: Learning Tactile-Informed Dynamics Models for Dense Packing (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Furthermore, our approach does not reason about the physical limitations of the bubbles in terms of achievable forces and torques.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: This expansion would significantly broaden the applicability of our method to real-world manipulation tasks involving intricate object shapes and diverse robot motions..
3. Compare against the body-reported baseline or a matched simpler baseline: To ensure a fair comparison with the baseline methods, we evaluate two different versions of each: one with 100 QP queries and another with 1000 queries..
4. Report the body metric and its denominator/aggregation: We observe that we achieve errors below 1N for force and in the order of a millimeter accuracy for the pose tracking error..
5. Re-run the body-reported ablation/failure condition: We report the mean absolute error for each of the wrench and pose components..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (IV. METHODOLOGY), p. 3 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY); the primary result is directionally consistent at p. 10 (V. EXPERIMENTS AND RESULTS), p. 7 (V. EXPERIMENTS AND RESULTS), p. 8 (V. EXPERIMENTS AND RESULTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contribution, formulate, contact mechanism이 To ensure a fair comparison with the baseline methods, we evaluate two different versions of each: ... 대비 We observe that we achieve errors below 1N for force and in the order of a millimeter accuracy ...을 개선하고, Furthermore, our approach does not reason about the physical limitations of the bubbles in terms of ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
