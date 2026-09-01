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

- **Closed-loop position:** `proprioception, reference pose/motion, visual or language command → whole-body pose, balance/contact state와 skill/mode → joint/whole-body action, motion target 또는 task trajectory`.
- 이 논문의 재사용 가능한 지점은 Phase 1: In simulation, a privileged RL teacher policy ωteacher receives full-state proprioception and exteroception of the task information and outputs WBC commands.를 At time step t, the teacher ωteacher(at/opriv t ) outputs a high-level command for the low-level WBC policy given privileged observation.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 whole-body pose, balance/contact state와 skill/mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Note that VIRAL framework does not have designs overfitting to specific WBC policy, and can be extended to other humanoid WBC controllers [44, 78].에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Proprioception consists of oprop-priv t = [vt, ωt, gt, at→1, qt, ˙qt, f finger t ] where vt, ωt are base linear and angular velocities, gt is base projected gravity, at→1 is ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, humanoid, visual sim-to-real, loco-manipulation, teacher-student learning`.
- **Reading predecessor in the generated track queue:** HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Language-Grounded Dynamic Scene Graphs for Interactive Object Search with Mobile Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Note that VIRAL framework does not have designs overfitting to specific WBC policy, and can be extended to other humanoid WBC controllers [44, 78].; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We assess real-world generalization by systematically varying the environment along multiple factors, including tray start position, robot start pose, table height, lighting, table cloth, table type and color, and object category (Figur ....
3. Compare against the body-reported baseline or a matched simpler baseline: These results show that although expert-level success remains challenging, VIRAL achieves near-expert success performance while being faster than the expert, and it substantially outperforms non-experts in both reliability and efficienc ....
4. Report the body metric and its denominator/aggregation: Figure 14. Scaling compute for teacher training. Rewards (left) and success rates (right) for 1-16 GPUs. More GPUs yield faster convergence and better asymptotic performance..
5. Re-run the body-reported ablation/failure condition: Figure 9. Ablations of teacher policy training. Training rewards (left) and success rates (right) for the full method (RSI + delta ac- tion), without demonstration resets, and without delta action space, showing ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (2.1. Key Elements of Teacher Training), p. 4 (2.2. Key Elements of Student Training), p. 3 (2.1. Key Elements of Teacher Training); the primary result is directionally consistent at p. 6 (3.1. Robustness), p. 6 (Figure/Table caption), p. 5 (3. Real-World Results of VIRAL); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Proprioception, consists, oprop-priv mechanism이 These results show that although expert-level success remains challenging, VIRAL achieves near-expert success performance while being ... 대비 Figure 14. Scaling compute for teacher training. Rewards (left) and success rates (right) for 1-16 GPUs. More GPUs ...을 개선하고, Note that VIRAL framework does not have designs overfitting to specific WBC policy, and can be ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
