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

- **Paper-specific interface:** Our method is composed of 4 core components: i) a stateestimation pipeline using the feedback from the tactile sensor to estimate object pose and extrinsic contacts; ii) a passive compliance ... (p. 3, IV. METHODOLOGY).
- **Paper-specific mechanism:** The main contributions of our work are in components (iii) and (iv) where we augment the model in (ii) with contact-aware constraints for object poses and force transmission, then formulating ... (p. 3, IV. METHODOLOGY).
- **Evidence boundary:** the reported outcome is While the current model yields satisfactory results, exploring higher-dimensional models with improved accuracy could further enhance performance. (p. 10, V. EXPERIMENTS AND RESULTS); the relevant task/metric cue is We observe that we achieve errors below 1N for force and in the order of a millimeter accuracy for the pose tracking error. (p. 8, V. EXPERIMENTS AND RESULTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Furthermore, our approach does not reason about the physical limitations of the bubbles in terms of achievable forces and torques. (p. 10, V. EXPERIMENTS AND RESULTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, contact-rich manipulation, tactile sensing, non-prehensile manipulation`.
- **Reading predecessor in the generated track queue:** Global Planning for Contact-Rich Manipulation via Local Smoothing of Quasi-Dynamic Contact Models (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** RoboPack: Learning Tactile-Informed Dynamics Models for Dense Packing (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Furthermore, our approach does not reason about the physical limitations of the bubbles in terms of achievable forces and torques.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Our method is composed of 4 core components: i) a stateestimation pipeline using the feedback from the tactile sensor to estimate object pose and extrinsic contacts; ii) a passive compliance ... (p. 3, IV. METHODOLOGY); preserve the objective/update rule: 4) Given the object and robot poses, the external wrench, and the contact forces compute the loss function L and backpropagate the gradients through the different blocks to update the ... (p. 5, IV. METHODOLOGY).
2. Use the paper-reported task/data/environment cue: This expansion would significantly broaden the applicability of our method to real-world manipulation tasks involving intricate object shapes and diverse robot motions. (p. 10, V. EXPERIMENTS AND RESULTS).
3. Compare against the reported or matched baseline: To ensure a fair comparison with the baseline methods, we evaluate two different versions of each: one with 100 QP queries and another with 1000 queries. (p. 9, V. EXPERIMENTS AND RESULTS).
4. Report the body metric with its denominator and aggregation: We observe that we achieve errors below 1N for force and in the order of a millimeter accuracy for the pose tracking error. (p. 8, V. EXPERIMENTS AND RESULTS).
5. Re-run the reported ablation or stress/failure condition: Our experiments show that the closedloop controllers achieve superior performance tracking the desired trajectories than the other tested control approaches. (p. 7, V. EXPERIMENTS AND RESULTS); if none is reported, design one around: Furthermore, our approach does not reason about the physical limitations of the bubbles in terms of achievable forces and torques. (p. 10, V. EXPERIMENTS AND RESULTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 3 (IV. METHODOLOGY), p. 3 (IV. METHODOLOGY), match the reported outcome at p. 10 (V. EXPERIMENTS AND RESULTS), p. 9 (V. EXPERIMENTS AND RESULTS), p. 9 (V. EXPERIMENTS AND RESULTS), and measure the boundary at p. 10 (V. EXPERIMENTS AND RESULTS), p. 10 (V. EXPERIMENTS AND RESULTS).

## Falsifiable research question

Under the paper's stated interface (Our method is composed of 4 core components: i) a stateestimation pipeline using the feedback from the tactile sensor to estimate object ...), does the paper-specific mechanism (The main contributions of our work are in components (iii) and (iv) where we augment the model in (ii) with contact-aware constraints ...) retain the reported evaluation outcome (We observe that we achieve errors below 1N for force and in the order of a millimeter accuracy ...) when tested against the paper's strongest explicit boundary (Furthermore, our approach does not reason about the physical limitations of the bubbles in terms of achievable forces ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (We observe that we achieve errors below 1N for force and in the order of a millimeter accuracy ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** The main contributions of our work are in components (iii) and (iv) where we augment the model in (ii) with contact-aware constraints for object poses and force transmission, then formulating ... (p. 3, IV. METHODOLOGY).
- **Paper-supported outcome:** While the current model yields satisfactory results, exploring higher-dimensional models with improved accuracy could further enhance performance. (p. 10, V. EXPERIMENTS AND RESULTS).
- **Strongest explicit boundary:** Furthermore, our approach does not reason about the physical limitations of the bubbles in terms of achievable forces and torques. (p. 10, V. EXPERIMENTS AND RESULTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
