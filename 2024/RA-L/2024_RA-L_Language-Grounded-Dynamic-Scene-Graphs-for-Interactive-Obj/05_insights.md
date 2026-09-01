# Insights — Language-Grounded Dynamic Scene Graphs for Interactive Object Search with Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2403.08605; PDF retrieval source: https://arxiv.org/pdf/2403.08605. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our approach incorporates a scene understanding module that, given object detections, constructs open-vocabulary scene ∗Equal contribution.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these challenges, we propose grounding LLMs in dynamically built scene graphs.
- **p. 3 / IV. MOMA-LLM - extractive body cue:** To address the challenges of interactive open-vocabulary household tasks, we propose MoMa-LLM, which intertwines high-level reasoning with scalable dynamic scene representations.
- **p. 4 / IV. MOMA-LLM - extractive body cue:** It consists of the path on the Voronoi graph GV, and the Euclidean distances d from the Voronoi nodes no and nvp to the object ...
- **p. 4 / IV. MOMA-LLM - extractive body cue:** It consists of the following high-level actions: navigate(room_name, object_name): Navigation to an object in a room via an A∗planner in the explored BEV-map Bt, inflated ...
- **p. 1 / Abstract - extractive body cue:** In this work, we propose MoMa-LLM, a novel approach that grounds language models within structured representations derived from openvocabulary scene graphs, dynamically updated as the ...
- **p. 1 / 2 Toyota Motor Europe (TME) - extractive body cue:** These diverse representations are then tightly interweaved with an object-centric action space.
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (IV. MOMA-LLM), p. 4 (IV. MOMA-LLM), p. 4 (IV. MOMA-LLM), p. 1 (Abstract)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these challenges, we propose grounding LLMs in dynamically built scene graphs.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Furthermore, the presence of interactive scenes and articulated objects introduces a multitude of potential states and failure cases.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Furthermore, the agent was able to react to the (unseen) subpolicy failures, such as re-trying to open a drawer when the gripper slipped off the ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** The two failures stemmed from irrecoverable failures of the subpolicies, in particular, collisions of the base during navigation or of the arm while opening the ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Object interactions, distance travelled and infeasible actions averaged over all episodes, including early terminated failures.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** This metric does not take into account the costs of object interactions.
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6. We construct a real-world apartment covering four rooms and 54 objects and transfer the model to a Toyota HSR robot. these objects would ...
- **Boundary to test:** Furthermore, the agent was able to react to the (unseen) subpolicy failures, such as re-trying to open a drawer when the gripper slipped off the handle.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our approach incorporates a scene understanding module that, given object detections, constructs open-vocabulary scene ∗Equal contribution. | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Reported outcome | Similarly, while HIMOS achieves a high success rate, it is unable to explore efficiently. | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |
| Failure/limitation | Furthermore, the agent was able to react to the (unseen) subpolicy failures, such as re-trying to open a drawer when the gripper slipped off the handle. | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `egocentric RGB-D, language/task goal, base-arm proprioception → map/object/contact state와 base-arm coordination decision → base motion plus arm/gripper action`.
- 이 논문의 재사용 가능한 지점은 We rely on a simple success state to the action history, stating "success", "failure", or "invalid argument" in case the output of the LLM could not be matched to the scene graph.를 If a subpolicy attempted execution but failed to complete its task, we re-encode the latest scene, update the action history, and let the LLM make a normal next decision with the updated ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 map/object/contact state와 base-arm coordination decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Furthermore, the agent was able to react to the (unseen) subpolicy failures, such as re-trying to open a drawer when the gripper slipped off the handle.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our approach incorporates a scene understanding module that, given object detections, constructs open-vocabulary scene ∗Equal contribution.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, Graph Reasoning`.
- **Reading predecessor in the generated track queue:** VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Furthermore, the agent was able to react to the (unseen) subpolicy failures, such as re-trying to open a drawer when the gripper slipped off the handle.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Simulation Experiments We instantiate the task in the iGibson simulator [32] with a Fetch robot..
3. Compare against the body-reported baseline or a matched simpler baseline: Unstructured LLM: This baseline provides the scene graph in a JSON format without any additional structure to the language model..
4. Report the body metric and its denominator/aggregation: In contrast, MoMa-LLM achieves similar success rates as HIMOS with a much higher search efficiency, both in terms of SPL and AUC-E..
5. Re-run the body-reported ablation/failure condition: Unstructured LLM: This baseline provides the scene graph in a JSON format without any additional structure to the language model..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 1 (Abstract), p. 4 (IV. MOMA-LLM), p. 1 (2 Toyota Motor Europe (TME)); the primary result is directionally consistent at p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 incorporates, scene, understanding mechanism이 Unstructured LLM: This baseline provides the scene graph in a JSON format without any additional structure ... 대비 In contrast, MoMa-LLM achieves similar success rates as HIMOS with a much higher search efficiency, both in terms ...을 개선하고, Furthermore, the agent was able to react to the (unseen) subpolicy failures, such as re-trying to ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
