# Insights — Open-Vocabulary Spatio-Temporal Scene Graph for Robot Perception and Teleoperation Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_5.html; PDF retrieval source: https://arxiv.org/pdf/2509.23107. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** The main contributions of this work can be summarized as follows: 1) We propose ST-OVSG, a novel spatio-temporal openvocabulary scene graph, which explicitly models both ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address this, we propose Spatio-Temporal OpenVocabulary Scene Graph (ST-OVSG), an open-vocabulary spatio-temporal scene graph designed for teleoperation.
- **p. 3 / III. METHODOLOGY - extractive body cue:** To address this, we propose ST-OVSG that integrates object nodes, spatial relations, and temporal correspondences.
- **p. 3 / III. METHODOLOGY - extractive body cue:** Formally, the challenge is to maintain a representation that allows the system to (i) recover the scene as it existed at the command-issue time, (ii) ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** This allows the planner to interpret userissued commands with respect to the scene state observed by the operator.
- **p. 4 / III. METHODOLOGY - extractive body cue:** The planner outputs a sequence of high-level actions π = (a1, . . . , aM) with grounded arguments (e.g., centroids and sizes), which are ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** User commands are used to query node features, filtering relevant nodes to form an ST-OVSG subgraph, which is then serialized into JSON and provided to ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY)

### Strongest assumption and failure boundary

- **p. 2 / I. INTRODUCTION - extractive body cue:** Taken together, these challenges reveal a fundamental gap: latency distorts the temporal alignment between operator intent and robot execution, while static representations fail to capture ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, directly applying these models to teleoperation robotics still faces several challenges.
- **p. 1 / I. INTRODUCTION - extractive body cue:** The second challenge is the static nature of current scene representations.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Failure cases were dominated by residual identity switches under long occlusions, missed detections of small or subtle objects, and unstable temporal associations caused by motion ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** In practice, many predicted actions were semantically correct but expressed with different phrasing or level of detail, which lowers embedding-based similarity without indicating execution failure.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Because our representation is designed for openvocabulary settings, automated evaluation of nodes and edges is unreliable: object categories and relational boundaries under open vocabulary cannot ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Motion blur, viewpoint shifts, and occlusions destabilize open-vocabulary detections.
- **Boundary to test:** Failure cases were dominated by residual identity switches under long occlusions, missed detections of small or subtle objects, and unstable temporal associations caused by motion blur or unusual poses.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The main contributions of this work can be summarized as follows: 1) We propose ST-OVSG, a novel spatio-temporal openvocabulary scene graph, which explicitly models both the spatial structure and temporal dynamics of ... | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | Our method achieved a node accuracy of 74%, outperforming ConceptGraphs [7], while edge accuracy reached 67%, slightly lower than 1Edge precision corresponds to spatial edges in ConceptGraph. | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Failure/limitation | Failure cases were dominated by residual identity switches under long occlusions, missed detections of small or subtle objects, and unstable temporal associations caused by motion blur or unusual poses. | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 The planner outputs a sequence of high-level actions π = (a1, . . . , aM) with grounded arguments (e.g., centroids and sizes), which are parsed into skill parameters for downstream controllers.를 Crucially, because each frame-level graph Mn stores both its capture timestamp τn and estimated latency ∆Tn, the planner can retrieve the scene state aligned with the user's instruction time τu.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Failure cases were dominated by residual identity switches under long occlusions, missed detections of small or subtle objects, and unstable temporal associations caused by motion blur or unusual poses.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: The main contributions of this work can be summarized as follows: 1) We propose ST-OVSG, a novel spatio-temporal openvocabulary scene graph, which explicitly models both the spatial structure and temporal dynamics of ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Planning and control`; tags: `Robotics, Graph Reasoning, semantic`.
- **Reading predecessor in the generated track queue:** Neural Assembler: Learning to Generate Fine-Grained Robotic Assembly Instructions from Multi-View Images (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Lookahead Exploration with Neural Radiance Representation for Continuous Vision-Language Navigation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Failure cases were dominated by residual identity switches under long occlusions, missed detections of small or subtle objects, and unstable temporal associations caused by motion blur or unusual poses.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Unlike static benchmarks, these videos feature continuous scene evolution, where objects are moved, occluded, rotated, duplicated, or removed..
3. Compare against the body-reported baseline or a matched simpler baseline: With ST-OVSG, the average similarity score is 0.1702, compared to 0.164 without STOVSG..
4. Report the body metric and its denominator/aggregation: Across 17 trials, ST-OVSG achieved a success rate of 70.5%..
5. Re-run the body-reported ablation/failure condition: Fig. 3. Execution process of the proposed method in a task. Left: users provide a natural-language grasp-and-place instruction at the local side (issue at 5.5s and communication latency is 500ms). ST-OVSG builds ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 2 (III. METHODOLOGY); the primary result is directionally consistent at p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 main, contributions, summarized mechanism이 With ST-OVSG, the average similarity score is 0.1702, compared to 0.164 without STOVSG. 대비 Across 17 trials, ST-OVSG achieved a success rate of 70.5%.을 개선하고, Failure cases were dominated by residual identity switches under long occlusions, missed detections of small or ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
