# Insights — VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/He_VIRAL_Visual_Sim-to-Real_at_Scale_for_Humanoid_Loco-Manipulation_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/He_VIRAL_Visual_Sim-to-Real_at_Scale_for_Humanoid_Loco-Manipulation_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 2.1. Key Elements of Teacher Training - extractive body cue:** Proprioception consists of oprop-priv t = [vt, ωt, gt, at→1, qt, ˙qt, f finger t ] where vt, ωt are base linear and angular velocities, ...
- **p. 2 / 1. Introduction - extractive body cue:** Our goal is not to propose yet another novel RL or sim-to-real algorithm, but to provide a technical recipe on the full stack required to ...
- **p. 4 / 2.2. Key Elements of Student Training - extractive body cue:** For the student's vision backbone, we adopt a state-of-the-art image encoder [61] to extract high-quality RGB features, which are fused with proprioceptive to the policy ...
- **p. 3 / 2.1. Key Elements of Teacher Training - extractive body cue:** At time step t, the teacher ωteacher(at/opriv t ) outputs a high-level command for the low-level WBC policy given privileged observation.
- **p. 4 / 2.2. Key Elements of Student Training - extractive body cue:** This mixed-policy rollout combines the fast initialization of BC with the state-coverage benefits of DAgger, producing a more resilient vision-based controller.
- **p. 5 / 2.2. Key Elements of Student Training - extractive body cue:** We identify scaling up GPUs for both teacher and student training as critical in our ablation studies in Figure 14 and Figure 15.
- **p. 5 / 2.2. Key Elements of Student Training - extractive body cue:** This implementation preserves the simplicity of single-GPU training while enabling near-linear scaling to large clusters for high-throughput visual sim-to-real learning.
- **Contribution anchor:** p. 3 (2.1. Key Elements of Teacher Training), p. 2 (1. Introduction), p. 4 (2.2. Key Elements of Student Training), p. 3 (2.1. Key Elements of Teacher Training), p. 4 (2.2. Key Elements of Student Training), p. 5 (2.2. Key Elements of Student Training)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** Yet, despite rapid progress in hardware and control, current humanoids have delivered limited real, sustained productivity outside of carefully engineered demos [21].
- **p. 2 / 1. Introduction - extractive body cue:** In other words, if we treat humanoid mobile manipulation as "just another data problem," the required scale may be prohibitively expensive in practice.
- **p. 2 / 1. Introduction - extractive body cue:** In real-world experiments, VIRAL shows not only the robustness of the high success rate that is near the human expert teleoperation performance, but also generalization ...
- **p. 3 / 2.1. Key Elements of Teacher Training - extractive body cue:** Note that VIRAL framework does not have designs overfitting to specific WBC policy, and can be extended to other humanoid WBC controllers [44, 78].
- **p. 3 / 2.1. Key Elements of Teacher Training - extractive body cue:** With a stable and robust WBC policy as an API layer, the action space of VIRAL policy is limited to a safe and reliable region ...
- **p. 4 / 2.1. Key Elements of Teacher Training - extractive body cue:** Visual randomization on image, lighting, material, and camera-extrinsics randomization for sim-to-real robustness.
- **p. 4 / 2.2. Key Elements of Student Training - extractive body cue:** The distinction between DAgger and BC lies solely in the source of observations: teacher rollouts provide clean, near-optimal demonstrations that rapidly imprint strong priors on ...
- **Boundary to test:** Note that VIRAL framework does not have designs overfitting to specific WBC policy, and can be extended to other humanoid WBC controllers [44, 78].

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Proprioception consists of oprop-priv t = [vt, ωt, gt, at→1, qt, ˙qt, f finger t ] where vt, ωt are base linear and angular velocities, gt is base projected gravity, at→1 is ... | p. 3 (2.1. Key Elements of Teacher Training), p. 2 (1. Introduction) |
| Reported outcome | These results show that although expert-level success remains challenging, VIRAL achieves near-expert success performance while being faster than the expert, and it substantially outperforms non-experts in both reliability and efficienc ... | p. 6 (3.1. Robustness), p. 6 (Figure/Table caption) |
| Failure/limitation | Note that VIRAL framework does not have designs overfitting to specific WBC policy, and can be extended to other humanoid WBC controllers [44, 78]. | p. 3 (2.1. Key Elements of Teacher Training), p. 3 (2.1. Key Elements of Teacher Training) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Humanoid robots are often framed as the natural embodiment of general-purpose physical intelligence: machines that could ultimately take on a large fraction of physical work for society. (p. 1, 1. Introduction).
- **Paper-specific mechanism:** Our goal is not to propose yet another novel RL or sim-to-real algorithm, but to provide a technical recipe on the full stack required to make RGBbased humanoid loco-manipulation work ... (p. 2, 1. Introduction).
- **Evidence boundary:** the reported outcome is Figure 8. Real-world generalization of VIRAL RGB-based policy under variations in tray and object position, robot start pose, table height and type, tablecloth color, lighting, and object category. Videos are ... (p. 6, Figure/Table caption); the relevant task/metric cue is As shown in Figure 7, the expert attains a 100% success rate with a 21.4 s cycle time, slightly higher than the 20.2 s cycle time of VIRAL. (p. 6, 3.1. Robustness). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** We find that compute scale is critical: scaling simulation to tens of GPUs (up to 64) makes both teacher and student training reliable, while low-compute regimes often fail. (p. 1, Abstract).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, humanoid, visual sim-to-real, loco-manipulation, teacher-student learning`.
- **Reading predecessor in the generated track queue:** HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Language-Grounded Dynamic Scene Graphs for Interactive Object Search with Mobile Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Note that VIRAL framework does not have designs overfitting to specific WBC policy, and can be extended to other humanoid WBC controllers [44, 78].; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Humanoid robots are often framed as the natural embodiment of general-purpose physical intelligence: machines that could ultimately take on a large fraction of physical work for society. (p. 1, 1. Introduction); preserve the objective/update rule: Therefore, we define four key rewards: 1. (p. 3, 2.1. Key Elements of Teacher Training).
2. Use the paper-reported task/data/environment cue: We assess real-world generalization by systematically varying the environment along multiple factors, including tray start position, robot start pose, table height, lighting, table cloth, table type and color, and object ... (p. 6, 3.2. Generalization).
3. Compare against the reported or matched baseline: Across these variations, VIRAL consistently completes the task without additional tuning, indicating strong robustness. (p. 6, 3.2. Generalization).
4. Report the body metric with its denominator and aggregation: As shown in Figure 7, the expert attains a 100% success rate with a 21.4 s cycle time, slightly higher than the 20.2 s cycle time of VIRAL. (p. 6, 3.1. Robustness).
5. Re-run the reported ablation or stress/failure condition: Figure 9. Ablations of teacher policy training. Training rewards (left) and success rates (right) for the full method (RSI + delta ac- tion), without demonstration resets, and without delta action ... (p. 6, Figure/Table caption); if none is reported, design one around: We find that compute scale is critical: scaling simulation to tens of GPUs (up to 64) makes both teacher and student training reliable, while low-compute regimes often fail. (p. 1, Abstract).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1. Introduction), p. 1 (Abstract), match the reported outcome at p. 6 (Figure/Table caption), p. 6 (3.2. Generalization), p. 6 (3.1. Robustness), and measure the boundary at p. 1 (Abstract), p. 2 (1. Introduction).

## Falsifiable research question

Under the paper's stated interface (Humanoid robots are often framed as the natural embodiment of general-purpose physical intelligence: machines that could ultimately take on a large fraction ...), does the paper-specific mechanism (Our goal is not to propose yet another novel RL or sim-to-real algorithm, but to provide a technical recipe on the full ...) retain the reported evaluation outcome (As shown in Figure 7, the expert attains a 100% success rate with a 21.4 s cycle time, ...) when tested against the paper's strongest explicit boundary (We find that compute scale is critical: scaling simulation to tens of GPUs (up to 64) makes both ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (As shown in Figure 7, the expert attains a 100% success rate with a 21.4 s cycle time, ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Our goal is not to propose yet another novel RL or sim-to-real algorithm, but to provide a technical recipe on the full stack required to make RGBbased humanoid loco-manipulation work ... (p. 2, 1. Introduction).
- **Paper-supported outcome:** Figure 8. Real-world generalization of VIRAL RGB-based policy under variations in tray and object position, robot start pose, table height and type, tablecloth color, lighting, and object category. Videos are ... (p. 6, Figure/Table caption).
- **Strongest explicit boundary:** We find that compute scale is critical: scaling simulation to tens of GPUs (up to 64) makes both teacher and student training reliable, while low-compute regimes often fail. (p. 1, Abstract).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
