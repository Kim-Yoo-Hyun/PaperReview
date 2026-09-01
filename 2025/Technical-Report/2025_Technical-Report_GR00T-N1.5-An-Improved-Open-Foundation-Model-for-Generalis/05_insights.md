# Insights — GR00T N1.5: An Improved Open Foundation Model for Generalist Humanoid Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: official NVIDIA technical page body (no public PDF identified) checked on 2026-09-02 (1 source page(s); official NVIDIA technical page body (no public PDF identified); extraction quality: high); canonical paper source: https://research.nvidia.com/labs/gear/gr00t-n1_5/; body source: https://research.nvidia.com/labs/gear/gr00t-n1_5/. The note is an evidence-anchored official source body analysis; exact tables/equations or section details remain at the cited source anchors. Evidence boundary: selected official source body statements and source anchors were used; no PDF was identified at review time. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected official source body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots - extractive body cue:** We introduce GR00T N1.5, an upgraded version of the GR00T N1 foundation model for humanoid robots.
- **p. 1 / Learning to manipulate novel objects from human ego videos - extractive body cue:** As shown in the FLARE project , future latent representation alignment enables learning directly from human ego videos.
- **p. 1 / Joint Policy Learning and World Modeling Objective - extractive body cue:** We used FLARE loss coefficient 0.2 for both pretraining and posttraining.
- **p. 1 / Model and Data Updates - extractive body cue:** The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions.
- **Contribution anchor:** p. 1 (GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots), p. 1 (Learning to manipulate novel objects from human ego videos), p. 1 (Joint Policy Learning and World Modeling Objective), p. 1 (Model and Data Updates)

### Strongest assumption and failure boundary

- **p. 1 / Learning to manipulate novel objects from human ego videos - extractive body cue:** Novel object generalization performance.
- **p. 1 / Model and Data Updates - extractive body cue:** We found that these modifications greatly improved language following and generalization.
- **p. 1 / Generalization to novel behaviors using Neural Trajectories - extractive body cue:** Although these new verbs can be considered "zero-shot" in the sense that we never collected teleoperation data for these tasks, we still train explicitly on ...
- **p. 1 / Model and Data Updates - extractive body cue:** The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions.
- **Boundary to test:** Although these new verbs can be considered "zero-shot" in the sense that we never collected teleoperation data for these tasks, we still train explicitly on them via DreamGen trajectories; leaving full zero-shot ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We introduce GR00T N1.5, an upgraded version of the GR00T N1 foundation model for humanoid robots. | p. 1 (GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots), p. 1 (Learning to manipulate novel objects from human ego videos) |
| Reported outcome | It achieves higher success rate, can use more diverse data sources, and has significantly improved language following capabilities. | p. 1 (Post-training on Unitree G1), p. 1 (Architecture validation) |
| Failure/limitation | Although these new verbs can be considered "zero-shot" in the sense that we never collected teleoperation data for these tasks, we still train explicitly on them via DreamGen trajectories; leaving full zero-shot ... | p. 1 (Generalization to novel behaviors using Neural Trajectories), p. 1 (Model and Data Updates) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, reference pose/motion, visual or language command → whole-body pose, balance/contact state와 skill/mode → joint/whole-body action, motion target 또는 task trajectory`.
- 이 논문의 재사용 가능한 지점은 The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions.를 GR00T N1.5 Policy rollout with language prompt: "Pick the apple from table to plate"로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 whole-body pose, balance/contact state와 skill/mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Although these new verbs can be considered "zero-shot" in the sense that we never collected teleoperation data for these tasks, we still train explicitly on them via DreamGen trajectories; leaving full zero-shot ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We introduce GR00T N1.5, an upgraded version of the GR00T N1 foundation model for humanoid robots.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `VLA, humanoid, foundation model, Flow Matching, world model, robot data`.
- **Reading predecessor in the generated track queue:** Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** GR00T N1.6: An Improved Open Foundation Model for Generalist Humanoid Robots (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Although these new verbs can be considered "zero-shot" in the sense that we never collected teleoperation data for these tasks, we still train explicitly on them via DreamGen trajectories; leaving full zero-shot ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: In order to tune the model architecture for N1.5, we trained policies from scratch on two sim robot benchmarks requiring language following: Language Table and a set of five simulated GR-1 tasks ....
3. Compare against the body-reported baseline or a matched simpler baseline: We expect users of N1.5 should observe better performance compared to N1, in particular improved generalization and better language following ability..
4. Report the body metric and its denominator/aggregation: We find that GR00T N1.5 achieved a 38.3% success rate across 12 DreamGen tasks, versus 13.1% for GR00T N1..
5. Re-run the body-reported ablation/failure condition: Distribution of training data in GR00T N1.5 pretraining..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 1 (Joint Policy Learning and World Modeling Objective), p. 1 (Model and Data Updates); the primary result is directionally consistent at p. 1 (Post-training on Unitree G1), p. 1 (Architecture validation); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 introduce, GR00T, upgraded mechanism이 We expect users of N1.5 should observe better performance compared to N1, in particular improved generalization ... 대비 We find that GR00T N1.5 achieved a 38.3% success rate across 12 DreamGen tasks, versus 13.1% for GR00T ...을 개선하고, Although these new verbs can be considered "zero-shot" in the sense that we never collected teleoperation ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
