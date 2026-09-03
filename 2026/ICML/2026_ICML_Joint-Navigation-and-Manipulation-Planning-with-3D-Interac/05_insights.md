# Insights — Joint Navigation and Manipulation Planning with 3D Interaction Chains

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=oVB2xYWvpv; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/327408. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** In summary, we propose 3D Interaction Chains (3D-IC) for the OVMM task in this paper.
- **p. 2 / 1. Introduction - extractive body cue:** Our 3D-IC includes: (1) a 3D feature map that captures information needed for both navigation and manipulation, (2) an interaction chain that enables unified planning ...
- **p. 5 / 4.2. 3D-IC Construction - extractive body cue:** Following frontier-based exploration (FBE) (Yamauchi, 1997), repeatedly navigating to frontier locations enables the robot to progressively reveal unknown areas and discover targets.
- **p. 3 / 4.1. Unified Modeling of Multi-stage Interaction - extractive body cue:** Formally, given RGB-D observations It, the robot first builds a 3D feature map Mt.
- **p. 3 / 4.1. Unified Modeling of Multi-stage Interaction - extractive body cue:** On the action side, the policy is decomposed into: (1) a high-level policy operating on Mt that outputs a sequence of interaction waypoints and action ...
- **p. 4 / 4.1. Unified Modeling of Multi-stage Interaction - extractive body cue:** In the chain decision stage, joint planning is employed to ultimately select the interaction waypoints for execution, which are then dispatched to the local policy ...
- **p. 5 / 4.2. 3D-IC Construction - extractive body cue:** To obtain an interaction chain ct = {(wk, uk)}K k=1, candidate interaction waypoints wk and their associated action tokens uk are first generated from the ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (4.2. 3D-IC Construction), p. 3 (4.1. Unified Modeling of Multi-stage Interaction), p. 3 (4.1. Unified Modeling of Multi-stage Interaction), p. 4 (4.1. Unified Modeling of Multi-stage Interaction)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** However, such independently designed policies and limited heuristics struggle to generalize across diverse situations.
- **p. 2 / 1. Introduction - extractive body cue:** To bridge this gap, a 3D feature map (Wang et al., 2025b; Wang & Lee, 2025) is constructed to fuse map-level context with egocentric visual ...
- **p. 1 / 1. Introduction - extractive body cue:** Existing OVMM methods can be broadly categorized into modular and reinforcement learning (RL)-based approaches.
- **p. 1 / 1. Introduction - extractive body cue:** (a) Existing methods for OVMM typically plan navigation and manipulation as separate stages, which can result in navigation endpoints that are suboptimal for subsequent interaction.
- **p. 3 / 3. Preliminaries of Mobile Manipulation - extractive body cue:** Since the two policies differ in both inputs and action spaces, existing approaches, whether modular pipelines or RL-based methods, typically make decisions with independent policies.
- **p. 7 / 5.2. Evaluation Results - extractive body cue:** Each Move tomato from table to counter Move apple from couch to table Move knife from cabinet to table baseline baseline 3D-IC 3D-IC High Navigation ...
- **p. 8 / 5.3. Real-world Evaluation - extractive body cue:** Consequently, the agent navigated back to a nightstand in the initial room to complete the placement, thereby avoiding a potential failure.
- **Boundary to test:** Each Move tomato from table to counter Move apple from couch to table Move knife from cabinet to table baseline baseline 3D-IC 3D-IC High Navigation Cost Low Navigation Cost Pick failed due ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, we propose 3D Interaction Chains (3D-IC) for the OVMM task in this paper. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Experimental results validate improvements in both success rate and efficiency (SPL). | p. 7 (5.2. Evaluation Results), p. 9 (Figure/Table caption) |
| Failure/limitation | Each Move tomato from table to counter Move apple from couch to table Move knife from cabinet to table baseline baseline 3D-IC 3D-IC High Navigation Cost Low Navigation Cost Pick failed due ... | p. 7 (5.2. Evaluation Results), p. 8 (5.3. Real-world Evaluation) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `egocentric RGB-D, language/task goal, base-arm proprioception → map/object/contact state와 base-arm coordination decision → base motion plus arm/gripper action`.
- 이 논문의 재사용 가능한 지점은 The navigation policy πn takes mt as input and outputs base actions an t ∈{Forward, Left, Right}, whereas the manipulation policy πm takes the single-step observation It as input and outputs continuous ...를 Our goal is joint planning for OVMM, while navigation and manipulation differ substantially in both inputs and outputs: navigation typically conditions on the accumulated history of observations (e.g., a semantic map) and ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 map/object/contact state와 base-arm coordination decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Each Move tomato from table to counter Move apple from couch to table Move knife from cabinet to table baseline baseline 3D-IC 3D-IC High Navigation Cost Low Navigation Cost Pick failed due ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, we propose 3D Interaction Chains (3D-IC) for the OVMM task in this paper.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Manipulation, contact, tactile, and dexterity`; tags: `Vision-Language Model, Robotics, 3D Vision, Navigation`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Each Move tomato from table to counter Move apple from couch to table Move knife from cabinet to table baseline baseline 3D-IC 3D-IC High Navigation Cost Low Navigation Cost Pick failed due ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: In the OVMM benchmark, the "steps" metric calculates the average number of steps across all episodes where the agent actively terminates, including failed episodes..
3. Compare against the body-reported baseline or a matched simpler baseline: Our method consistently outperforms prior works, establishing new state-of-the-art performance across all metrics..
4. Report the body metric and its denominator/aggregation: Experimental results validate improvements in both success rate and efficiency (SPL)..
5. Re-run the body-reported ablation/failure condition: Ablation on 3D Interaction Point Representations..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (4.1. Unified Modeling of Multi-stage Interaction), p. 3 (4.1. Unified Modeling of Multi-stage Interaction), p. 4 (4.1. Unified Modeling of Multi-stage Interaction); the primary result is directionally consistent at p. 7 (5.2. Evaluation Results), p. 9 (Figure/Table caption), p. 9 (5.4. Comparison with SOTA Methods); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, Interaction, Chains mechanism이 Our method consistently outperforms prior works, establishing new state-of-the-art performance across all metrics. 대비 Experimental results validate improvements in both success rate and efficiency (SPL).을 개선하고, Each Move tomato from table to counter Move apple from couch to table Move knife from ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
