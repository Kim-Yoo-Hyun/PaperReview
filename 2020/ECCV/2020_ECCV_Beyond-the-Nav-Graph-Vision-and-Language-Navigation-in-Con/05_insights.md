# Insights — Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2004.02857; PDF retrieval source: https://arxiv.org/pdf/2004.02857. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1 Introduction - extractive body cue:** In this work, we develop a continuous setting that enables these types of studies and take a first step towards integrating VLN agents with control ...
- **p. 1 / 1 Introduction - extractive body cue:** This paradigm enables efficient data collection and high visual fidelity compared to 3D scanning or creating synthetic environments; however, scenes are only observed from a ...
- **p. 4 / 1 Introduction - extractive body cue:** To summarize our contributions, we: - Lift the VLN task to continuous 3D environments - removing many unrealistic assumptions imposed by the nav-graph-based representation.
- **p. 1 / 1 Introduction - extractive body cue:** Many of these tasks have been developed from datasets of panoramic images captured in real scenes - e.g.
- **p. 3 / 1 Introduction - extractive body cue:** We develop agent architectures for this task and explore how popular mechanisms for VLN transfer to the VLN-CE setting.
- **p. 3 / 1 Introduction - extractive body cue:** Specifically, we develop a simple sequence-to-sequence baseline architecture as well as a cross-modal attentionbased model.
- **p. 2 / 1 Introduction - extractive body cue:** Our VLN-CE setting (b) lifts these assumptions by instantiating the task in continuous environments with low-level actions - providing a more realistic testbed for robot ...
- **Contribution anchor:** p. 3 (1 Introduction), p. 1 (1 Introduction), p. 4 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction)

### Strongest assumption and failure boundary

- **p. 3 / 1 Introduction - extractive body cue:** However, these techniques are each independently far from perfect and such an agent would need to learn the limitations of these lowerlevel control systems - ...
- **p. 2 / 1 Introduction - extractive body cue:** Taken together, these assumptions make current settings poor reflections of the real world both in terms of control (ignoring actuation, navigation, and localization error) and ...
- **p. 3 / 1 Introduction - extractive body cue:** This setting introduces many challenges ignored in prior work.
- **p. 2 / 1 Introduction - extractive body cue:** However, precise localization indoors is still a challenging problem.
- **p. 4 / 1 Introduction - extractive body cue:** We find significant gaps in performance between these settings indicative of the strong prior provided by the nav-graph.
- **p. 14 / 5 Experiments - extractive body cue:** The second example shows a failure of the agent - it navigates towards the wrong windows and fails to first "pass the kitchen" - stopping ...
- **p. 14 / 5 Experiments - extractive body cue:** We also observe failures when the agent never sees the object(s) referred to by the instruction in the scene - with a limited egocentric field-of-view, ...
- **Boundary to test:** The second example shows a failure of the agent - it navigates towards the wrong windows and fails to first "pass the kitchen" - stopping instead at the nearest couch.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this work, we develop a continuous setting that enables these types of studies and take a first step towards integrating VLN agents with control via low-level actions. | p. 3 (1 Introduction), p. 1 (1 Introduction) |
| Reported outcome | Despite having no learned components nor processing any input, both these agents achieve approximately 3% success rates in val-unseen. | p. 12 (5 Experiments), p. 12 (5 Experiments) |
| Failure/limitation | The second example shows a failure of the agent - it navigates towards the wrong windows and fails to first "pass the kitchen" - stopping instead at the nearest couch. | p. 14 (5 Experiments), p. 14 (5 Experiments) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `standardized observation, action, task state와 evaluation split → benchmark state/goal와 method decision → policy/controller trajectory 또는 measured result`.
- 이 논문의 재사용 가능한 지점은 Our VLN-CE setting (b) lifts these assumptions by instantiating the task in continuous environments with low-level actions - providing a more realistic testbed for robot instruction following. - a static topological representation ...를 We perform a number of input-modality ablations to assess the biases and baselines in this new setting (including models without perception or instructions as suggested in [27]).로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 benchmark state/goal와 method decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 The second example shows a failure of the agent - it navigates towards the wrong windows and fails to first "pass the kitchen" - stopping instead at the nearest couch.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this work, we develop a continuous setting that enables these types of studies and take a first step towards integrating VLN agents with control via low-level actions.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `Vision-Language Navigation, Robotics, Navigation, Benchmark`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The second example shows a failure of the agent - it navigates towards the wrong windows and fails to first "pass the kitchen" - stopping instead at the nearest couch.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: This Cross-Modal Attention PM+DA*+Aug model achieves an SPL of 0.35 on val-seen and 0.30 on val-unseen - succeeding on 32% of episodes in new environments..
3. Compare against the body-reported baseline or a matched simpler baseline: Our baseline Seq2Seq model significantly outperforms the random and hand-crafted baselines, successfully reaching the goal in 20% of val-unseen episodes..
4. Report the body metric and its denominator/aggregation: We report standard metrics for visual navigation tasks defined in [2,4,18] - trajectory length in meters (TL), navigation error in meters from goal at termination (NE), oracle success rate (OS), success rate ....
5. Re-run the body-reported ablation/failure condition: We believe that depth enable agents to quickly begin traversing environments effectively (e.g. without collisions) and without this it is very difficult to bootstrap to instruction following..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction); the primary result is directionally consistent at p. 12 (5 Experiments), p. 12 (5 Experiments), p. 11 (5 Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 develop, continuous, setting mechanism이 Our baseline Seq2Seq model significantly outperforms the random and hand-crafted baselines, successfully reaching the goal in ... 대비 We report standard metrics for visual navigation tasks defined in [2,4,18] - trajectory length in meters (TL), navigation ...을 개선하고, The second example shows a failure of the agent - it navigates towards the wrong windows ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
