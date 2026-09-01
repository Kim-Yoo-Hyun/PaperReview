# Insights — SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (50 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v229/rana23a.html; PDF retrieval source: https://arxiv.org/pdf/2307.06135. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** Firstly, we present a mechanism that enables the LLM to conduct a semantic search for a taskrelevant subgraph G′ by manipulating the nodes of a ...
- **p. 2 / 1 Introduction - extractive body cue:** To this end, we present a scalable approach to ground LLM-based task planners across environments spanning multiple rooms and floors.
- **p. 3 / 1 Introduction - extractive body cue:** We evaluate our framework across a range of 90 tasks organised into four levels of difficulty.
- **p. 1 / 1 Introduction - extractive body cue:** This enables robots to plan complex strategies for a diverse range of tasks that require a substantial amount of background knowledge and semantic comprehension.
- **p. 3 / 1 Introduction - extractive body cue:** Our approach SayPlan ensures feasible and grounded plan generation for a mobile manipulator robot operating in large-scale environments spanning multiple floors and rooms.
- **p. 13 / A Implementation Details - extractive body cue:** We utilise GPT-4 [3] as the underlying LLM agent unless otherwise stated.
- **p. 13 / A Implementation Details - extractive body cue:** During semantic search, both the 3D Scene Graph and Memory components of the input prompt get updated at each step, while during iterative replanning only ...
- **Contribution anchor:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction), p. 13 (A Implementation Details)

### Strongest assumption and failure boundary

- **p. 3 / 1 Introduction - extractive body cue:** We evaluate our framework across a range of 90 tasks organised into four levels of difficulty.
- **p. 1 / 1 Introduction - extractive body cue:** The challenge lies in scaling these models.
- **p. 1 / 1 Introduction - extractive body cue:** The associated challenges permeate every aspect of robotics, encompassing navigation, perception, manipulation as well as high-level task planning.
- **p. 2 / 1 Introduction - extractive body cue:** We can leverage a JSON representation of this graph as input to a pre-trained LLM, however, to ensure the scalability of the plans to expansive ...
- **p. 2 / 1 Introduction - extractive body cue:** Finally, to ensure the feasibility of the proposed plan, we introduce an iterative replanning pipeline that verifies and refines the initial plan using feedback from ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: 3D Scene Graph Token Count Number of tokens required for the full graph vs. collapsed graph. An odd failure case in the simple ...
- **p. 46 / Figure/Table caption - extractive body cue:** Figure 8: Evaluating the performance of SayPlan's causal planning capabilities as the scale of the environment increases. For the office environment used in this study, ...
- **Boundary to test:** Table 2: 3D Scene Graph Token Count Number of tokens required for the full graph vs. collapsed graph. An odd failure case in the simple search instructions involved negation, where the agent ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Firstly, we present a mechanism that enables the LLM to conduct a semantic search for a taskrelevant subgraph G′ by manipulating the nodes of a ‘collapsed' 3DSG, which exposes only the top ... | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | The table shows the semantic search success rate in finding a suitable subgraph for planning. | p. 6 (5 Results), p. 7 (Figure/Table caption) |
| Failure/limitation | Table 2: 3D Scene Graph Token Count Number of tokens required for the full graph vs. collapsed graph. An odd failure case in the simple search instructions involved negation, where the agent ... | p. 7 (Figure/Table caption), p. 46 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `egocentric RGB-D, language/task goal, base-arm proprioception → map/object/contact state와 base-arm coordination decision → base motion plus arm/gripper action`.
- 이 논문의 재사용 가능한 지점은 Finally, to ensure the feasibility of the proposed plan, we introduce an iterative replanning pipeline that verifies and refines the initial plan using feedback from a scene graph simulator in order to ...를 For LLMs to be effective planners in robotics, they must be grounded in reality, that is, they must adhere to the constraints presented by the physical environment in which the robot operates, ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 map/object/contact state와 base-arm coordination decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Table 2: 3D Scene Graph Token Count Number of tokens required for the full graph vs. collapsed graph. An odd failure case in the simple search instructions involved negation, where the agent ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Firstly, we present a mechanism that enables the LLM to conduct a semantic search for a taskrelevant subgraph G′ by manipulating the nodes of a ‘collapsed' 3DSG, which exposes only the top ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, 3D Vision, LLM planning, 3D Scene Graph, replanning, mobile manipulation`.
- **Reading predecessor in the generated track queue:** Inner Monologue: Embodied Reasoning through Planning with Language Models (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** XSkill: Cross Embodiment Skill Discovery (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Table 2: 3D Scene Graph Token Count Number of tokens required for the full graph vs. collapsed graph. An odd failure case in the simple search instructions involved negation, where the agent ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: This static prompt is both task- and environment-agnostic and takes up ≈3900 tokens of the LLM's input..
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 3: Scene Graph Token Progression Dur- ing Semantic Search. This graph illustrates the scalability of our approach to large-scale 3D scene graphs. Note the importance of node contraction in maintaining a ....
4. Report the body metric and its denominator/aggregation: The table shows the semantic search success rate in finding a suitable subgraph for planning..
5. Re-run the body-reported ablation/failure condition: Figure 5: 3D Scene Graph - Fully Expanded Office Environment. Full 3D scene graph exposing all the rooms, assets and objects available in the scene. Note that the LLM agent never sees ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 13 (A Implementation Details), p. 13 (A Implementation Details); the primary result is directionally consistent at p. 6 (5 Results), p. 7 (Figure/Table caption), p. 46 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Firstly, present, mechanism mechanism이 Figure 3: Scene Graph Token Progression Dur- ing Semantic Search. This graph illustrates the scalability of ... 대비 The table shows the semantic search success rate in finding a suitable subgraph for planning.을 개선하고, Table 2: 3D Scene Graph Token Count Number of tokens required for the full graph vs. ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
