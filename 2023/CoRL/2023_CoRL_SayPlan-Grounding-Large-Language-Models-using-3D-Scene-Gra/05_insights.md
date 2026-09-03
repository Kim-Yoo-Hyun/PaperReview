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

- **Paper-specific interface:** Finally, to ensure the feasibility of the proposed plan, we introduce an iterative replanning pipeline that verifies and refines the initial plan using feedback from a scene graph simulator in ... (p. 2, 1 Introduction).
- **Paper-specific mechanism:** Firstly, we present a mechanism that enables the LLM to conduct a semantic search for a taskrelevant subgraph G′ by manipulating the nodes of a ‘collapsed' 3DSG, which exposes only ... (p. 2, 1 Introduction).
- **Evidence boundary:** the reported outcome is We summarise the results for the semantic search evaluation in Table (p. 6, 5 Results); the relevant task/metric cue is The table shows the semantic search success rate in finding a suitable subgraph for planning. (p. 6, 5 Results). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** An odd failure case in the simple search instructions involved negation, where the agent consistently failed when presented with questions such as "Find me an office that does not have ... (p. 7, 1. SayPlan (GPT-3.5) consistently).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, 3D Vision, LLM planning, 3D Scene Graph, replanning, mobile manipulation`.
- **Reading predecessor in the generated track queue:** Inner Monologue: Embodied Reasoning through Planning with Language Models (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** XSkill: Cross Embodiment Skill Discovery (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Table 2: 3D Scene Graph Token Count Number of tokens required for the full graph vs. collapsed graph. An odd failure case in the simple search instructions involved negation, where the agent ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Finally, to ensure the feasibility of the proposed plan, we introduce an iterative replanning pipeline that verifies and refines the initial plan using feedback from a scene graph simulator in ... (p. 2, 1 Introduction); preserve the objective/update rule: During semantic search, both the 3D Scene Graph and Memory components of the input prompt get updated at each step, while during iterative replanning only the Feedback component gets updated ... (p. 13, A Implementation Details).
2. Use the paper-reported task/data/environment cue: This static prompt is both task- and environment-agnostic and takes up ≈3900 tokens of the LLM's input. (p. 13, A Implementation Details).
3. Compare against the reported or matched baseline: We summarise the results for the semantic search evaluation in Table (p. 6, 5 Results).
4. Report the body metric with its denominator and aggregation: The table shows the semantic search success rate in finding a suitable subgraph for planning. (p. 6, 5 Results).
5. Re-run the reported ablation or stress/failure condition: Figure 5: 3D Scene Graph - Fully Expanded Office Environment. Full 3D scene graph exposing all the rooms, assets and objects available in the scene. Note that the LLM agent ... (p. 20, Figure/Table caption); if none is reported, design one around: An odd failure case in the simple search instructions involved negation, where the agent consistently failed when presented with questions such as "Find me an office that does not have ... (p. 7, 1. SayPlan (GPT-3.5) consistently).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1 Introduction), p. 1 (1 Introduction), match the reported outcome at p. 6 (5 Results), p. 6 (5 Results), p. 7 (Figure/Table caption), and measure the boundary at p. 7 (1. SayPlan (GPT-3.5) consistently), p. 8 (1. SayPlan (GPT-3.5) consistently).

## Falsifiable research question

Under the paper's stated interface (Finally, to ensure the feasibility of the proposed plan, we introduce an iterative replanning pipeline that verifies and refines the initial plan ...), does the paper-specific mechanism (Firstly, we present a mechanism that enables the LLM to conduct a semantic search for a taskrelevant subgraph G′ by manipulating the ...) retain the reported evaluation outcome (The table shows the semantic search success rate in finding a suitable subgraph for planning.) when tested against the paper's strongest explicit boundary (An odd failure case in the simple search instructions involved negation, where the agent consistently failed when presented ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (The table shows the semantic search success rate in finding a suitable subgraph for planning.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (50 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Firstly, we present a mechanism that enables the LLM to conduct a semantic search for a taskrelevant subgraph G′ by manipulating the nodes of a ‘collapsed' 3DSG, which exposes only ... (p. 2, 1 Introduction).
- **Paper-supported outcome:** We summarise the results for the semantic search evaluation in Table (p. 6, 5 Results).
- **Strongest explicit boundary:** An odd failure case in the simple search instructions involved negation, where the agent consistently failed when presented with questions such as "Find me an office that does not have ... (p. 7, 1. SayPlan (GPT-3.5) consistently).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
