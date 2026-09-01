# Insights — HumanPlus: Humanoid Shadowing and Imitation from Humans

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=WnSl42M9Z4; PDF retrieval source: https://arxiv.org/pdf/2406.10454. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we present a full-stack system for humanoids to learn motion and autonomous skills from human data.
- **p. 3 / 1. Introduction - extractive body cue:** Core to this system is both (1) a real-time shadowing system that allows human operators to whole-body control humanoids using a single RGB camera and ...
- **p. 3 / 1. Introduction - extractive body cue:** Using forward dynamics prediction on image features, our method shows improved performance by regularizing on image feature spaces and preventing the vision-based skill policy from ...
- **p. 4 / 4. Human Body and Hand Data - extractive body cue:** Each of the humanoid hip and shoulder joints consists of 3 orthogonal revolute joints, so can be viewed as one spherical joints.
- **p. 5 / 5. Shadowing of Human Motion - extractive body cue:** The humanoid target pose consists of target forward and lateral velocities, target roll and pitch, target yaw velocity and target joint angles, and is retargeted ...
- **p. 2 / 1. Introduction - extractive body cue:** We leverage this dataset by first retargeting human poses to humanoid poses and then training a task-agnostic low-level policy called Humanoid Shadowing Transformer conditioning on ...
- **p. 7 / 6. Imitation of Human Skills - extractive body cue:** In this work, we modify the Action Chunking Transformer [104] by removing its encoder-decoder architecture to develop a decoder-only Humanoid Imitation Transformer (HIT) for skill ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 3 (1. Introduction), p. 3 (1. Introduction), p. 4 (4. Human Body and Hand Data), p. 5 (5. Shadowing of Human Motion), p. 2 (1. Introduction)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** This problem is further exacerbated by the lack of off-the-shelf and integrated hardware platforms.
- **p. 2 / 1. Introduction - extractive body cue:** Traditional approaches, such as decoupling the problem into perception, planning and tracking, and separate modularization of control for arms and legs [10, 10, 23, 40], ...
- **p. 3 / 1. Introduction - extractive body cue:** Shadowing provides an efficient data collection pipeline for diverse real-world tasks, bypassing the sim-to-real gap of RGB perception.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: Robustness Evaluation. Our low-level policy (Ours) can withstand large disturbance forces, has a shorter recovery time, and enables more whole-body skills than the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Teleop Comparisons & User Studies. We report averaged completion time for 6 participants on 2 tasks. target poses while saving energy and avoiding ...
- **p. 10 / 9. Experiments on Imitation - extractive body cue:** Throughout the development of our system, we encountered several limitations.
- **p. 10 / 9. Experiments on Imitation - extractive body cue:** It fails the Wear a Shoe and Walk task completely, where depth perception is crucial.
- **Boundary to test:** Table 4: Robustness Evaluation. Our low-level policy (Ours) can withstand large disturbance forces, has a shorter recovery time, and enables more whole-body skills than the manufacturer controller (H1 Default). Kinesthetic Teaching ALOH ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this paper, we present a full-stack system for humanoids to learn motion and autonomous skills from human data. | p. 2 (1. Introduction), p. 3 (1. Introduction) |
| Reported outcome | Our HIT achieves higher success rates than other baselines across all tasks. | p. 10 (9. Experiments on Imitation), p. 9 (Figure/Table caption) |
| Failure/limitation | Table 4: Robustness Evaluation. Our low-level policy (Ours) can withstand large disturbance forces, has a shorter recovery time, and enables more whole-body skills than the manufacturer controller (H1 Default). Kinesthetic Teaching ALOH ... | p. 8 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, reference pose/motion, visual or language command → whole-body pose, balance/contact state와 skill/mode → joint/whole-body action, motion target 또는 task trajectory`.
- 이 논문의 재사용 가능한 지점은 Using state-of-the-art human body and hand pose estimation algorithms [58, 81], we can estimate real-time human motion and retarget it to humanoid motion, which is passed as input to the low-level policy.를 At each time step, the input to the policy is humanoid proprioception and a humanoid target pose.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 whole-body pose, balance/contact state와 skill/mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Table 4: Robustness Evaluation. Our low-level policy (Ours) can withstand large disturbance forces, has a shorter recovery time, and enables more whole-body skills than the manufacturer controller (H1 Default). Kinesthetic Teaching ALOH ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this paper, we present a full-stack system for humanoids to learn motion and autonomous skills from human data.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, humanoid, human-to-humanoid, Imitation Learning, teleoperation`.
- **Reading predecessor in the generated track queue:** Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Table 4: Robustness Evaluation. Our low-level policy (Ours) can withstand large disturbance forces, has a shorter recovery time, and enables more whole-body skills than the manufacturer controller (H1 Default). Kinesthetic Teaching ALOH ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Shown in Table 5, we compare our imitation learning method Humanoid Imitation Transformer with three baseline methods: HIT policies with monocular inputs (Monocular), ACT [104], and Open-loop trajectory replay, across all tasks: ....
3. Compare against the body-reported baseline or a matched simpler baseline: Overall HIT (Ours) outperforms others..
4. Report the body metric and its denominator/aggregation: In contrast, our system has the lowest timeto-completion, has the highest success rate of stable standing, and is the only method that can be used for whole-body teleoperation, solving the Rearrange Lower ....
5. Re-run the body-reported ablation/failure condition: The participants are tasked to perform the Rearrange Objects task and its variant, Rearrange Lower Objects, where an object is placed on a lower table of height 0.55m, requiring the robot to ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (1. Introduction), p. 7 (6. Imitation of Human Skills), p. 5 (4. Human Body and Hand Data); the primary result is directionally consistent at p. 10 (9. Experiments on Imitation), p. 9 (Figure/Table caption), p. 9 (8.1. Comparisons with Other Teleoperation); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 present, full-stack, system mechanism이 Overall HIT (Ours) outperforms others. 대비 In contrast, our system has the lowest timeto-completion, has the highest success rate of stable standing, and is ...을 개선하고, Table 4: Robustness Evaluation. Our low-level policy (Ours) can withstand large disturbance forces, has a shorter ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
