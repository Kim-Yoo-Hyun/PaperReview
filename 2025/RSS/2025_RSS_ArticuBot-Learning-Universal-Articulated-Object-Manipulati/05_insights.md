# Insights — ArticuBot: Learning Universal Articulated Object Manipulation Policy via Large Scale Simulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p156.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p156.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 5 / B. Policy Learning with a Hierarchical Policy Representation - extractive body cue:** Instead, we propose to use a hilrarchical policy representation, which consists of 4 high-level policy and a low-level policy.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** ‘+ We present a weighted displacement policy representation that scales up well with the number of demonstrations, outperforming alternative policy representations.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** 1 for a visualization of some of the different real-world articulated objects that our policy is able to open, In summary, our contributions are:
- **p. 3 / B. Sim2real Policy Learning - extractive body cue:** In contrast, we train a single model that ean be applied to opening various categories of articulated objects Besides, their system requires a specialized gripper, ...
- **p. 4 / 2. Hierarchical Policy Learning -- Low-level Policy Architecture - extractive body cue:** Middle: We propose a weighted displacement model for the high-level policy, which predicts the sub-goal end-effector pose.
- **p. 4 / 2. Hierarchical Policy Learning -- Low-level Policy Architecture - extractive body cue:** Bottom: We propose a goal-conditioned 3D diffusion policy for the low-level policy, which first applies attention between the current end-effector points, the scene points, and ...
- **p. 7 / B. Policy Learning with a Hierarchical Policy Representation - extractive body cue:** The final latent embedding used for diffusion is the concatenation of the above two features: [fpoo™, fom"! yess, po This latent embedding is used ‘as ...
- **Contribution anchor:** p. 5 (B. Policy Learning with a Hierarchical Policy Representation), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 3 (B. Sim2real Policy Learning), p. 4 (2. Hierarchical Policy Learning -- Low-level Policy Architecture), p. 4 (2. Hierarchical Policy Learning -- Low-level Policy Architecture)

### Strongest assumption and failure boundary

- **p. 2 / 1. INTRODUCTION - extractive body cue:** However, few have demonstrated generalization to manipulating many different articulated objects in the real world without simplifying assumptions (e.g, using a suction gripper (10).
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Many prior works have studied the problem of articulated object' manipulation [58 31, 10, 19, 21, 53, 15, 32].
- **p. 13 / C. Mobile X-Arm Results - extractive body cue:** See Appendix L for visualizations of some of the failure cases of ArticuBot, and some basic failure recovery abilities of ArticuBot.
- **p. 13 / C. Mobile X-Arm Results - extractive body cue:** We leave addressing these limitations as important future work.
- **p. 12 / B. Table-Top Franka Arm Results - extractive body cue:** Common failure ceases for table-top experiments include: 1, The robot arm runs to joint limits while opening the object, due to the limited space of ...
- **p. 12 / B. Table-Top Franka Arm Results - extractive body cue:** The major failure case for FlowBot3D is that the predicted flow is in the wrong direction, e.g., it predicts upwards flows for ‘opening a microwave ...
- **p. 11 / A. Setups - extractive body cue:** We do not input the optional segmentation mask for the target link to open for FlowBot3D, as such masks are not readily available in the ...
- **Boundary to test:** See Appendix L for visualizations of some of the failure cases of ArticuBot, and some basic failure recovery abilities of ArticuBot.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Instead, we propose to use a hilrarchical policy representation, which consists of 4 high-level policy and a low-level policy. | p. 5 (B. Policy Learning with a Hierarchical Policy Representation), p. 2 (1. INTRODUCTION) |
| Reported outcome | If we compute the normalized opening performance for ArticuBot only in cases where the grasp is successful (Le., the same starting conditions as FlowBot3D), the performance of ArticuBot further improves to 0.81 ... | p. 12 (B. Table-Top Franka Arm Results), p. 12 (C. Mobile X-Arm Results) |
| Failure/limitation | See Appendix L for visualizations of some of the failure cases of ArticuBot, and some basic failure recovery abilities of ArticuBot. | p. 13 (C. Mobile X-Arm Results), p. 13 (C. Mobile X-Arm Results) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `egocentric RGB-D, language/task goal, base-arm proprioception → map/object/contact state와 base-arm coordination decision → base motion plus arm/gripper action`.
- 이 논문의 재사용 가능한 지점은 takes 3D point cloud as input and outputs delta endeffector transformations as the actions. + DP3 Transformer, which replaces the simplified PointNet encoder in DP3 with a transformer-based encoder (the same one ...를 The final latent embedding used for diffusion is the concatenation of the above two features: [fpoo™, fom"! yess, po This latent embedding is used ‘as the conditioning for an action generation UNet ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 map/object/contact state와 base-arm coordination decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 See Appendix L for visualizations of some of the failure cases of ArticuBot, and some basic failure recovery abilities of ArticuBot.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Instead, we propose to use a hilrarchical policy representation, which consists of 4 high-level policy and a low-level policy.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, mobile manipulation, simulation, articulated objects`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** See Appendix L for visualizations of some of the failure cases of ArticuBot, and some basic failure recovery abilities of ArticuBot.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Although our training data includes multi-door objects, demonstrations are generated for opening the closest door to the initial pose of the robot..
3. Compare against the body-reported baseline or a matched simpler baseline: ‘The results forall test objects and compared methods in lab A are shown in Fig..
4. Report the body metric and its denominator/aggregation: As shown, ArticuBot achieves a grasping success rate of 0.9 and normalized opening performance of 0.54, showing it can.
5. Re-run the body-reported ablation/failure condition: We think adding a force-torque sensor on the X-Arm to enable impedance control could help alleviate this issue; fine-tuning the policy in the real-world via reinforcement learning or a few demonstrations for ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (2. Hierarchical Policy Learning -- Low-level Policy Architecture), p. 5 (B. Policy Learning with a Hierarchical Policy Representation), p. 7 (B. Policy Learning with a Hierarchical Policy Representation); the primary result is directionally consistent at p. 12 (B. Table-Top Franka Arm Results), p. 12 (C. Mobile X-Arm Results), p. 13 (C. Mobile X-Arm Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Instead, hilrarchical, policy mechanism이 ‘The results forall test objects and compared methods in lab A are shown in Fig. 대비 As shown, ArticuBot achieves a grasping success rate of 0.9 and normalized opening performance of 0.54, showing it ...을 개선하고, See Appendix L for visualizations of some of the failure cases of ArticuBot, and some basic ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
