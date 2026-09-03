# Insights — OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2509.26633; PDF retrieval source: https://arxiv.org/pdf/2509.26633. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / Abstract - extractive body cue:** To address this, we introduce OMNIRETARGET, an interactionpreserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and ...
- **p. 1 / Abstract - extractive body cue:** Moreover, preserving task-relevant interactions enables efficient data augmentation, from a single demonstration to different robot embodiments, terrains, and object configurations.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This challenge is further amplified on humanoids, whose high-dimensional action spaces and complex dynamics make learning natural, expressive behaviors from scratch both difficult and inefficient.
- **Contribution anchor:** p. 1 (Abstract), p. 1 (Abstract), p. 1 (I. INTRODUCTION)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** This challenge is further amplified on humanoids, whose high-dimensional action spaces and complex dynamics make learning natural, expressive behaviors from scratch both difficult and inefficient.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This embodiment gap means that simply adapting human motions is in ...
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 10: Histograms from the downstream RL evaluation showing the failure patterns for the baselines in different tasks. VideoMimic, which fails systematically due to poor ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Cross-embodiment robot-object-terrain interaction. Drake [52], which correctly handles the differential geometry of rotations on the S3 manifold [53]. Our interaction-mesh-based kinematic pipeline is ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Additional hardware results showing diverse, agile and human-like behaviors. • Observation noise: ±0.05 for orientation in Rot6D, ±0.5 m/s and ±0.2 rad/s for ...
- **Boundary to test:** Fig. 10: Histograms from the downstream RL evaluation showing the failure patterns for the baselines in different tasks. VideoMimic, which fails systematically due to poor inter- action preservation. This task therefore measures ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To address this, we introduce OMNIRETARGET, an interactionpreserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, ... | p. 1 (Abstract), p. 1 (Abstract) |
| Reported outcome | Fig. 7: Artifacts resulting from the retargeting baselines. trained on our augmented data instead yield reliable success (see video for comparison). Admittedly, additional reward engineering could help, but it contradicts our minimal ... | p. 7 (Figure/Table caption), p. 12 (Figure/Table caption) |
| Failure/limitation | Fig. 10: Histograms from the downstream RL evaluation showing the failure patterns for the baselines in different tasks. VideoMimic, which fails systematically due to poor inter- action preservation. This task therefore measures ... | p. 12 (Figure/Table caption), p. 4 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, reference pose/motion, visual or language command → whole-body pose, balance/contact state와 skill/mode → joint/whole-body action, motion target 또는 task trajectory`.
- 이 논문의 재사용 가능한 지점은 Thanks to the high-quality interaction-preserving motion retargeting, these policies are trained and deployed in a minimal and unified way: it involves only 5 rewards, 4 robot domain randomization terms, and a purely ...를 To address these challenges, imitating human motions offers a powerful alternative for learning whole-body control, especially for complex scene interactions.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 whole-body pose, balance/contact state와 skill/mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Fig. 10: Histograms from the downstream RL evaluation showing the failure patterns for the baselines in different tasks. VideoMimic, which fails systematically due to poor inter- action preservation. This task therefore measures ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To address this, we introduce OMNIRETARGET, an interactionpreserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, humanoid, loco-manipulation, motion retargeting`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 10: Histograms from the downstream RL evaluation showing the failure patterns for the baselines in different tasks. VideoMimic, which fails systematically due to poor inter- action preservation. This task therefore measures ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The quest to enable humanoid robots to perform complex whole-body scene- and object-interaction tasks has long been constrained by a fundamental data bottleneck..
3. Compare against the body-reported baseline or a matched simpler baseline: Fig. 7: Artifacts resulting from the retargeting baselines. trained on our augmented data instead yield reliable success (see video for comparison). Admittedly, additional reward engineering could help, but it contradicts our minimal ....
4. Report the body metric and its denominator/aggregation: Fig. 10: Histograms from the downstream RL evaluation showing the failure patterns for the baselines in different tasks. VideoMimic, which fails systematically due to poor inter- action preservation. This task therefore measures ....
5. Re-run the body-reported ablation/failure condition: Fig. 2: OMNIRETARGET overview. Human demonstrations are retargeted to the robot via interaction-mesh-based constrained optimization. Each spatial and shape augmentation is solved as a new optimization, producing diverse trajectories tha ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 1 (Abstract), p. 1 (I. INTRODUCTION); the primary result is directionally consistent at p. 7 (Figure/Table caption), p. 12 (Figure/Table caption), p. 3 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 address, introduce, OMNIRETARGET mechanism이 Fig. 7: Artifacts resulting from the retargeting baselines. trained on our augmented data instead yield reliable ... 대비 Fig. 10: Histograms from the downstream RL evaluation showing the failure patterns for the baselines in different tasks. ...을 개선하고, Fig. 10: Histograms from the downstream RL evaluation showing the failure patterns for the baselines in ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
