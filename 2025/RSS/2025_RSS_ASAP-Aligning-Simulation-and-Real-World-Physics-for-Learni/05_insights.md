# Insights — ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p066.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p066.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / Abstract - extractive body cue:** mnparal- or result in overly conservative policies that sacrifice a yaper, we present ASAP
- **p. 2 / Abstract - extractive body cue:** To this end, we propose ASAP, a two-stage framework that aligns the dynamics mismatch between simulation and realworld physics, enabling agile humanoid whole-body skills ASAP ...
- **p. 3 / Abstract - extractive body cue:** 1) We introduce ASAP, a framework that bridges the simto-real gap by leveraging a delta action model trained via reinforcement learning (RL) with real-world data
- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** To mitigate this issue, we introduce a termination curriculum that progressively refines the motion error tolerance throughout training, guiding the policy toward improved tracking performance, ...
- **p. 5 / C. Fine-tuning Motion Tracking Policy under New Dynamics - extractive body cue:** In this section, we present extensive experimental results oon three policy transfers: IsaaeGym [58] to IsaacSim [63], IsaaeGym to Genesis [6], and IsiaeGym to real-world ...
- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** ‘The policy trained in the first stage can track the reference motion in the real-world but does not achieve high motion quality. ‘Thus, during the ...
- **p. 5 / B. Training Delta Action Model - extractive body cue:** As illustrated in Figure 2 (b), the delta action model is defined as Ady = (se, 44)» where the policy 77> leams to output corrective ...
- **Contribution anchor:** p. 1 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 4 (B. Phase-based Motion Tracking Policy Training), p. 5 (C. Fine-tuning Motion Tracking Policy under New Dynamics), p. 4 (B. Phase-based Motion Tracking Policy Training)

### Strongest assumption and failure boundary

- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** However, a successful backflip requires ‘mastering the landing first-if the policy cannot land correctly,
- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** Crucially, because the actor does not depend on position-based motion targets, ‘our approach eliminates the need for odometry during real world deployment-overcoming a well-documented challenge ...
- **p. 2 / Abstract - extractive body cue:** the sim-to-teal gap, especially when real-world dynamics fall outside the modeled distribution.
- **p. 2 / Abstract - extractive body cue:** However, most prior work [46, 74, 47, 73, 107, 19, 95, 50] has primarily focused ‘on locomotion, treating the legs as a means of mobility.
- **p. 3 / Abstract - extractive body cue:** This model effectively serves as a residual correction term for the dynamics gap.
- **p. 11 / C. Does ASAP Fine-Tuning Outperform Random Action Noise - extractive body cue:** Such structured discrepancies cannot be effectively captured by merely adding uniform action noise.
- **p. 12 / B. Offine and Online System Identification for Roboties - extractive body cue:** + Hardware Constraints: Agile whole-body motions exert significant stress on robots, leading to motor overheating, and hardware failure during data collection.
- **Boundary to test:** Such structured discrepancies cannot be effectively captured by merely adding uniform action noise.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | mnparal- or result in overly conservative policies that sacrifice a yaper, we present ASAP | p. 1 (Abstract), p. 2 (Abstract) |
| Reported outcome | Fig. 10. Analysis of dataset size, waning horizon, and scion aorm on the performance of x. (a) Dataset Size: Mean Per Joint Position Eror (MPIPE) is evaluted for both in-distbution (grea) and ... | p. 10 (Figure/Table caption) |
| Failure/limitation | Such structured discrepancies cannot be effectively captured by merely adding uniform action noise. | p. 11 (C. Does ASAP Fine-Tuning Outperform Random Action Noise), p. 12 (B. Offine and Online System Identification for Roboties) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** ‘To answer QS (How to best use the delta action model of ASAP?), we compare multiple strategies: fixed-point iteration, gradient-based optimization, and reinforcement learning (RL). (p. 10, B. Different Usage of Delta Action Model).
- **Paper-specific mechanism:** Primarily leveraging reinforcement learning algorithms [80] within physics simulators [58, 63, 88], humanoid robots have earned a wide range of skills, including robust locomo (p. 11, A. Learning-based Methods for Humanoid Control).
- **Evidence boundary:** the reported outcome is This process ensures accurate motion retargeting and produces the cleuned robot trajectory dataset DG as shown in Figure 3 (). (p. 3, 3) Extensive experiments in both simulation and real-world); the relevant task/metric cue is settings demonstrate that ASAP effectively reduces dyrnamies mismatch, enabling highly agile motions on robots and significantly reducing motion tracking errors. (p. 3, 3) Extensive experiments in both simulation and real-world). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** For instance, when imitating a jumping motion, the policy often fails early in training and learns 10 remain on the ground to avoid landing penalties. (p. 4, B. Phase-based Motion Tracking Policy Training).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, humanoid, whole-body control, sim-to-real, residual dynamics`.
- **Reading predecessor in the generated track queue:** HumanPlus: Humanoid Shadowing and Imitation from Humans (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** LangWBC: Language-Directed Humanoid Whole-Body Control via End-to-End Learning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Such structured discrepancies cannot be effectively captured by merely adding uniform action noise.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: ‘To answer QS (How to best use the delta action model of ASAP?), we compare multiple strategies: fixed-point iteration, gradient-based optimization, and reinforcement learning (RL). (p. 10, B. Different Usage of Delta Action Model); preserve the objective/update rule: To ‘optimize the policy. we use the proximal policy optimization (PPO) {80}, aiming to maximize the cumulative discounted reward E (SP In) We identify several design choices that are crucial ... (p. 4, B. Phase-based Motion Tracking Policy Training).
2. Use the paper-reported task/data/environment cue: This process ensures accurate motion retargeting and produces the cleuned robot trajectory dataset DG as shown in Figure 3 (). (p. 3, 3) Extensive experiments in both simulation and real-world).
3. Compare against the reported or matched baseline: Fig. 10. Analysis of dataset size, waning horizon, and scion aorm on the performance of x. (a) Dataset Size: Mean Per Joint Position Eror (MPIPE) is evaluted for both in-distbution ... (p. 10, Figure/Table caption).
4. Report the body metric with its denominator and aggregation: settings demonstrate that ASAP effectively reduces dyrnamies mismatch, enabling highly agile motions on robots and significantly reducing motion tracking errors. (p. 3, 3) Extensive experiments in both simulation and real-world).
5. Re-run the reported ablation or stress/failure condition: Fig. 10. Analysis of dataset size, waning horizon, and scion aorm on the performance of x. (a) Dataset Size: Mean Per Joint Position Eror (MPIPE) is evaluted for both in-distbution ... (p. 10, Figure/Table caption); if none is reported, design one around: For instance, when imitating a jumping motion, the policy often fails early in training and learns 10 remain on the ground to avoid landing penalties. (p. 4, B. Phase-based Motion Tracking Policy Training).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 11 (A. Learning-based Methods for Humanoid Control), p. 1 (Abstract), match the reported outcome at p. 3 (3) Extensive experiments in both simulation and real-world), p. 10 (Figure/Table caption), p. 3 (3) Extensive experiments in both simulation and real-world), and measure the boundary at p. 4 (B. Phase-based Motion Tracking Policy Training), p. 4 (B. Phase-based Motion Tracking Policy Training).

## Falsifiable research question

Under the paper's stated interface (‘To answer QS (How to best use the delta action model of ASAP?), we compare multiple strategies: fixed-point iteration, gradient-based optimization, and ...), does the paper-specific mechanism (Primarily leveraging reinforcement learning algorithms [80] within physics simulators [58, 63, 88], humanoid robots have earned a wide range of skills, including ...) retain the reported evaluation outcome (settings demonstrate that ASAP effectively reduces dyrnamies mismatch, enabling highly agile motions on robots and significantly reducing motion ...) when tested against the paper's strongest explicit boundary (For instance, when imitating a jumping motion, the policy often fails early in training and learns 10 remain ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (settings demonstrate that ASAP effectively reduces dyrnamies mismatch, enabling highly agile motions on robots and significantly reducing motion ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Primarily leveraging reinforcement learning algorithms [80] within physics simulators [58, 63, 88], humanoid robots have earned a wide range of skills, including robust locomo (p. 11, A. Learning-based Methods for Humanoid Control).
- **Paper-supported outcome:** This process ensures accurate motion retargeting and produces the cleuned robot trajectory dataset DG as shown in Figure 3 (). (p. 3, 3) Extensive experiments in both simulation and real-world).
- **Strongest explicit boundary:** For instance, when imitating a jumping motion, the policy often fails early in training and learns 10 remain on the ground to avoid landing penalties. (p. 4, B. Phase-based Motion Tracking Policy Training).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
