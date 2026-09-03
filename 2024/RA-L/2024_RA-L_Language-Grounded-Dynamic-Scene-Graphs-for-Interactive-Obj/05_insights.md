# Insights — Language-Grounded Dynamic Scene Graphs for Interactive Object Search with Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2403.08605; PDF retrieval source: https://arxiv.org/pdf/2403.08605. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our approach incorporates a scene understanding module that, given object detections, constructs open-vocabulary scene.
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
| Mechanism/contribution | Our approach incorporates a scene understanding module that, given object detections, constructs open-vocabulary scene.
| Reported outcome | Similarly, while HIMOS achieves a high success rate, it is unable to explore efficiently. | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |
| Failure/limitation | Furthermore, the agent was able to react to the (unseen) subpolicy failures, such as re-trying to open a drawer when the gripper slipped off the handle. | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** In this work, we propose MoMa-LLM, a novel approach that grounds language models within structured representations derived from openvocabulary scene graphs, dynamically updated as the environment is explored. (p. 1, Abstract).
- **Paper-specific mechanism:** To address these challenges, we propose grounding LLMs in dynamically built scene graphs. (p. 1, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is This results in an efficiency curve, in which the best policies are located in the top left corner, enabling the comparison of success rates for arbitrary budgets. (p. 6, V. EXPERIMENTS); the relevant task/metric cue is ESC-Interactive: ESC is a recent approach for semantic object search [27] which scores frontiers based on object-object and object-room co-occurrences as well as their distance. (p. 5, V. EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Furthermore, the agent was able to react to the (unseen) subpolicy failures, such as re-trying to open a drawer when the gripper slipped off the handle. (p. 7, V. EXPERIMENTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, Graph Reasoning`.
- **Reading predecessor in the generated track queue:** VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Furthermore, the agent was able to react to the (unseen) subpolicy failures, such as re-trying to open a drawer when the gripper slipped off the handle.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: In this work, we propose MoMa-LLM, a novel approach that grounds language models within structured representations derived from openvocabulary scene graphs, dynamically updated as the environment is explored. (p. 1, Abstract); preserve the objective/update rule: In this work, we propose MoMa-LLM, a novel approach that grounds language models within structured representations derived from openvocabulary scene graphs, dynamically updated as the environment is explored. (p. 1, Abstract).
2. Use the paper-reported task/data/environment cue: Simulation Experiments We instantiate the task in the iGibson simulator [32] with a Fetch robot. (p. 6, V. EXPERIMENTS).
3. Compare against the reported or matched baseline: Unstructured LLM: This baseline provides the scene graph in a JSON format without any additional structure to the language model. (p. 6, V. EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: ESC-Interactive: ESC is a recent approach for semantic object search [27] which scores frontiers based on object-object and object-room co-occurrences as well as their distance. (p. 5, V. EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: Unstructured LLM: This baseline provides the scene graph in a JSON format without any additional structure to the language model. (p. 6, V. EXPERIMENTS); if none is reported, design one around: Furthermore, the agent was able to react to the (unseen) subpolicy failures, such as re-trying to open a drawer when the gripper slipped off the handle. (p. 7, V. EXPERIMENTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (I. INTRODUCTION), p. 1 (2 Toyota Motor Europe (TME)), match the reported outcome at p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), and measure the boundary at p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS).

## Falsifiable research question

Under the paper's stated interface (In this work, we propose MoMa-LLM, a novel approach that grounds language models within structured representations derived from openvocabulary scene graphs, dynamically ...), does the paper-specific mechanism (To address these challenges, we propose grounding LLMs in dynamically built scene graphs.) retain the reported evaluation outcome (ESC-Interactive: ESC is a recent approach for semantic object search [27] which scores frontiers based on object-object and ...) when tested against the paper's strongest explicit boundary (Furthermore, the agent was able to react to the (unseen) subpolicy failures, such as re-trying to open a ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (ESC-Interactive: ESC is a recent approach for semantic object search [27] which scores frontiers based on object-object and ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** To address these challenges, we propose grounding LLMs in dynamically built scene graphs. (p. 1, I. INTRODUCTION).
- **Paper-supported outcome:** This results in an efficiency curve, in which the best policies are located in the top left corner, enabling the comparison of success rates for arbitrary budgets. (p. 6, V. EXPERIMENTS).
- **Strongest explicit boundary:** Furthermore, the agent was able to react to the (unseen) subpolicy failures, such as re-trying to open a drawer when the gripper slipped off the handle. (p. 7, V. EXPERIMENTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
