# Insights — Gallant: Voxel Grid-Based Humanoid Locomotion and Local Navigation across 3-D Constrained Terrains

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Ben_Gallant_Voxel_Grid-based_Humanoid_Locomotion_and_Local-navigation_across_3-D_Constrained_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Ben_Gallant_Voxel_Grid-based_Humanoid_Locomotion_and_Local-navigation_across_3-D_Constrained_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** To scale training and narrow the simulation-to-reality (simto-real) gap, we develop a LiDAR simulation pipeline that models sensor noise and latency and enables realistic scanning ...
- **p. 2 / 1. Introduction - extractive body cue:** We propose voxel grid as a lightweight yet geometrypreserving representation for humanoid locomotion and loco-navigation [31] in 3D-constrained environments.
- **p. 3 / 3. Method - extractive body cue:** We introduce Gallant, a voxel-grid-based perceptive learning framework for humanoid locomotion and local navigation [31] in 3D constrained environments.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Episodes end on fall, harsh collision (contact on the torso, hip, or knee links with a force exceeding 100 N), or timeout.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** We formulate humanoid perceptive locomotion as a partially observable Markov decision process (POMDP) M = (S, A, O, P, R, Ω, γ) and train an ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method), p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** While recent systems have progressed from lab prototypes to real-world deployment [17, 23], ensuring operational safety remains a key challenge.
- **p. 2 / 1. Introduction - extractive body cue:** To address these limitations, we introduce Gallant, a voxel-grid-based perception-learning framework for humanoid locomotion and loco-navigation across 3D constrained terrains.
- **p. 5 / 4.2.1. Metrics - extractive body cue:** 4.1), and the policy performance is measured by two distinct metrics: • Success rate E_{\mathrm {succ}}: fraction of episodes that reach the target within a ...
- **p. 7 / 4.2.3. Result - extractive body cue:** 1, using only a height map as the perceptual representation for policy cannot represent multilayer structure; consequently, Only-Height-Map fails on terrains such as Ceiling.
- **p. 8 / 4.4. Further Analyses - extractive body cue:** On other terrains-especially Platforms and Stairs, previously considered unstable due to collision risk [21]-Gallant achieves high success by proactively adjusting foot trajectories.
- **p. 8 / 5. Conclusion - extractive body cue:** In real-world tests, a single LiDAR policy covers the ground obstacles handled by elevation-map controllers while also tackling lateral and overhead structures, and on ground-only ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Method Overview. (a) Curriculum-based training over 8 representative terrains enhances generalization, and realistic voxel path alignment achieved via efficient LiDAR simulation with domain-randomized ...
- **Boundary to test:** 4.1), and the policy performance is measured by two distinct metrics: • Success rate E_{\mathrm {succ}}: fraction of episodes that reach the target within a 10s horizon without falling or incurring any ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To scale training and narrow the simulation-to-reality (simto-real) gap, we develop a LiDAR simulation pipeline that models sensor noise and latency and enables realistic scanning of dynamic objects, including the robot's own ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | With all other settings fixed, Gallant achieves much higher success rates than the variant that ignores dynamic objects (w/o-Self-Scan) across all tasks. | p. 6 (4.2.3. Result), p. 7 (4.2.3. Result) |
| Failure/limitation | 4.1), and the policy performance is measured by two distinct metrics: • Success rate E_{\mathrm {succ}}: fraction of episodes that reach the target within a 10s horizon without falling or incurring any ... | p. 5 (4.2.1. Metrics), p. 7 (4.2.3. Result) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, reference pose/motion, visual or language command → whole-body pose, balance/contact state와 skill/mode → joint/whole-body action, motion target 또는 task trajectory`.
- 이 논문의 재사용 가능한 지점은 In contrast, 3D LiDAR provides detailed scene geometry with a wide FoV, but its raw point clouds are sparse and noisy, which bottlenecks sample-efficient policy learning and real-time inference.를 Actor and critic share all features except privileged inputs, which are critic-only.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 whole-body pose, balance/contact state와 skill/mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 4.1), and the policy performance is measured by two distinct metrics: • Success rate E_{\mathrm {succ}}: fraction of episodes that reach the target within a 10s horizon without falling or incurring any ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To scale training and narrow the simulation-to-reality (simto-real) gap, we develop a LiDAR simulation pipeline that models sensor noise and latency and enables realistic scanning of dynamic objects, including the robot's own ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, humanoid, perceptive locomotion, LiDAR, 3D navigation`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 4.1), and the policy performance is measured by two distinct metrics: • Success rate E_{\mathrm {succ}}: fraction of episodes that reach the target within a 10s horizon without falling or incurring any ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 4.1), and the policy performance is measured by two distinct metrics: • Success rate E_{\mathrm {succ}}: fraction of episodes that reach the target within a 10s horizon without falling or incurring any ....
3. Compare against the body-reported baseline or a matched simpler baseline: Gallant consistently outperforms both baselines across all real-world terrains..
4. Report the body metric and its denominator/aggregation: 4.1), and the policy performance is measured by two distinct metrics: • Success rate E_{\mathrm {succ}}: fraction of episodes that reach the target within a 10s horizon without falling or incurring any ....
5. Re-run the body-reported ablation/failure condition: To assess the effectiveness of core components in Gallant, we compare against the following ablations: • Self-scan..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation); the primary result is directionally consistent at p. 6 (4.2.3. Result), p. 7 (4.2.3. Result), p. 8 (4.4. Further Analyses); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 scale, training, narrow mechanism이 Gallant consistently outperforms both baselines across all real-world terrains. 대비 4.1), and the policy performance is measured by two distinct metrics: • Success rate E_{\mathrm {succ}}: fraction of ...을 개선하고, 4.1), and the policy performance is measured by two distinct metrics: • Success rate E_{\mathrm {succ}}: ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
