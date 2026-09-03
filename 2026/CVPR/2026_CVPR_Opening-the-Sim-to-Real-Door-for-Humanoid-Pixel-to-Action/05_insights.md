# Insights — Opening the Sim-to-Real Door for Humanoid Pixel-to-Action Policy Transfer

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Xue_Opening_the_Sim-to-Real_Door_for_Humanoid_Pixel-to-Action_Policy_Transfer_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Xue_Opening_the_Sim-to-Real_Door_for_Humanoid_Pixel-to-Action_Policy_Transfer_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1. Introduction - extractive body cue:** To summarize, the main contributions of our work are: • We present the first end-to-end humanoid sim-to-real policy capable of diverse articulated loco-manipulation from pure ...
- **p. 3 / 1. Introduction - extractive body cue:** To address the first challenge, we introduce a novel, scalable teacher-student-bootstrap learning pipeline.
- **p. 4 / 2.2. Multi-Stage Whole-Body Loco-Manipulation - extractive body cue:** Here, we present the design of a robust teacher training pipeline for whole-body loco-manipulation tasks.
- **p. 4 / 2.2. Multi-Stage Whole-Body Loco-Manipulation - extractive body cue:** To address this, we introduce a staged reset law α = (α1, . . . , αK), K X y=1 αy = 1, (1) which ...
- **p. 5 / 2.4. Massive-Scale Simulation Randomization - extractive body cue:** Compared with prior work such as InfinigenSim [21], our IsaacLab-native implementation significantly improves physical realism and enables contact simulation that is both accurate and efficient ...
- **p. 3 / 1. Introduction - extractive body cue:** To improve training efficiency, we introduce an exploration scheme that resets environments from late-stage snapshots, leveraging the recoverability of the simulator.
- **p. 6 / 2.4. Massive-Scale Simulation Randomization - extractive body cue:** To balance rendering quality and performance while training an RL policy in parallel, we use the RTX Real-Time renderer in performance mode, with post-processing effects ...
- **Contribution anchor:** p. 3 (1. Introduction), p. 3 (1. Introduction), p. 4 (2.2. Multi-Stage Whole-Body Loco-Manipulation), p. 4 (2.2. Multi-Stage Whole-Body Loco-Manipulation), p. 5 (2.4. Massive-Scale Simulation Randomization), p. 3 (1. Introduction)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** These requirements remain unmet in prior work; and (ii) the visual sim-to-real gap spans a vast space of appearance and physics variation, requiring broad, heterogeneous ...
- **p. 4 / 2.2. Multi-Stage Whole-Body Loco-Manipulation - extractive body cue:** These challenges have not been foreseen in the prior success of RL whole-body control literature.
- **p. 2 / 1. Introduction - extractive body cue:** DARPA-Robotics-Challenge-era systems [29] depended heavily on scripting and operator intervention, while more recent teleoperation-centered pipelines [22] remain brittle.
- **p. 3 / 1. Introduction - extractive body cue:** To address the first challenge, we introduce a novel, scalable teacher-student-bootstrap learning pipeline.
- **p. 3 / 1. Introduction - extractive body cue:** To tackle the second challenge, we build a large-scale domain randomization pipeline in IsaacLab [28] that spans both physics and appearance variation at scale.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 8. Teacher training progress with different reset buffer sizes of 0, 10 and 100. reset buffer, as the policy finds it difficult to enter ...
- **p. 7 / 3.4. Effect of Staged Reset Exploration - extractive body cue:** The exploration fails when not using the 6648
- **Boundary to test:** Figure 8. Teacher training progress with different reset buffer sizes of 0, 10 and 100. reset buffer, as the policy finds it difficult to enter stage 2 (grasping door handle), which is ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To summarize, the main contributions of our work are: • We present the first end-to-end humanoid sim-to-real policy capable of diverse articulated loco-manipulation from pure RGB perception. • We introduce a teacher-student-bootstrap ... | p. 3 (1. Introduction), p. 3 (1. Introduction) |
| Reported outcome | Figure 7. Training progress of student policy bootstrapping with improvements in task success rate. The dashed lines are teacher policy success rates. cies can consistently achieve 80-90% success rate, the ini- tial ... | p. 7 (Figure/Table caption), p. 7 (3.2. Effect of Photorealistic Visual Randomization) |
| Failure/limitation | Figure 8. Teacher training progress with different reset buffer sizes of 0, 10 and 100. reset buffer, as the policy finds it difficult to enter stage 2 (grasping door handle), which is ... | p. 8 (Figure/Table caption), p. 7 (3.4. Effect of Staged Reset Exploration) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, reference pose/motion, visual or language command → whole-body pose, balance/contact state와 skill/mode → joint/whole-body action, motion target 또는 task trajectory`.
- 이 논문의 재사용 가능한 지점은 While the student policy has access to non-privileged proprioception information, such as joint angles q, joint velocities ˙q, and root angular velocities ˙ω ∈R3, its perception of the task relies mostly on ...를 In humanoid wholebody control literature, the policy is responsible for outputting target joint positions, which, in the case of a Unitree G1 robot, includes 29 body joints and 14 hand joints, resulting ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 whole-body pose, balance/contact state와 skill/mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 8. Teacher training progress with different reset buffer sizes of 0, 10 and 100. reset buffer, as the policy finds it difficult to enter stage 2 (grasping door handle), which is ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To summarize, the main contributions of our work are: • We present the first end-to-end humanoid sim-to-real policy capable of diverse articulated loco-manipulation from pure RGB perception. • We introduce a teacher-student-bootstrap ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, humanoid, pixel-to-action, visual sim-to-real, articulated object manipulation`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 8. Teacher training progress with different reset buffer sizes of 0, 10 and 100. reset buffer, as the policy finds it difficult to enter stage 2 (grasping door handle), which is ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Real-world visuals are unseen during training..
3. Compare against the body-reported baseline or a matched simpler baseline: In this section, we will establish real-world comparison with human baselines..
4. Report the body metric and its denominator/aggregation: Success rate and completion time are evaluated at when the robot traverses through the door and reaches a point 1 m beyond the door frame on the opposite side..
5. Re-run the body-reported ablation/failure condition: Finally, we run ablation study to investigate the effect of staged reset exploration on the stability of teacher training..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (1. Introduction), p. 3 (1. Introduction), p. 6 (2.4. Massive-Scale Simulation Randomization); the primary result is directionally consistent at p. 7 (Figure/Table caption), p. 7 (3.2. Effect of Photorealistic Visual Randomization), p. 6 (3.1. Surpassing Human-Teleop Baseline); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summarize, main, contributions mechanism이 In this section, we will establish real-world comparison with human baselines. 대비 Success rate and completion time are evaluated at when the robot traverses through the door and reaches a ...을 개선하고, Figure 8. Teacher training progress with different reset buffer sizes of 0, 10 and 100. reset ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
