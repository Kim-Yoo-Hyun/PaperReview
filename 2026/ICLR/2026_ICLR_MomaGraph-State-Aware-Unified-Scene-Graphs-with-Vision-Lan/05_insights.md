# Insights — MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=3eTr9dGwJv; PDF retrieval source: https://openreview.net/pdf/3f888689e829f4172ae97d1dfac5f1b62ddb30c3.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, our work makes the following key contributions: • We propose MomaGraph, the first scene graph representation that jointly models spatial and functional relationships ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To achieve this goal, we present MomaGraph, a novel scene representation specifically designed for embodied agents.
- **p. 6 / 4 METHOD - extractive body cue:** To address these limitations, we introduce MomaGraph-Scenes, the first dataset designed to provide a more comprehensive and task-relevant scene representation.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Unlike prior graph-then-plan methods (Dai et al., 2024; Ekpo et al., 2024) that either assume reliable scene graphs or treat graph construction and planning as ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** To overcome this gap, we propose the Graph-then-Plan strategy, which first generates task-specific scene graphs as an intermediate structured representation before high-level planning.
- **p. 6 / 4 METHOD - extractive body cue:** After the agent executes an action at and observes the new environment state st+1, the scene graph is refined as: G(t+1) T = U  ...
- **p. 5 / 4 METHOD - extractive body cue:** Reinforcement learning offers a more principled approach by encouraging the model to explore, reason, and iteratively refine its representations through outcome-driven feedback.
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 6 (4 METHOD), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 6 (4 METHOD)

### Strongest assumption and failure boundary

- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, existing scene graphs suffer from notable limitations.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** However, when directly used as task planners, VLMs (Huang et al., 2023; 2024; Ahn et al., 2022; Zheng et al., 2025a; Yang et al., 2025) ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** (3) They lack task relevance, as they fail to emphasize information directly tied to task execution, thereby reducing efficiency and effectiveness.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** However, existing works often focus on a single type of scene graphs.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Figure 2: Direct planning often fails even for strong closed-source models like GPT-5, producing wrong actions or ...
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 6: Quantitative real-robot evaluation. (a) Environment setup of the real-robot experiment. (b) Failure analysis illustrating success/failure rates across different reasoning stages. Task Setup. We ...
- **p. 11 / 7 CONCLUSION - extractive body cue:** This work addresses to the fundamental limitations of existing scene graphs for embodied agents: reliance on a single type of relationship, inability to adapt to ...
- **Boundary to test:** Figure 6: Quantitative real-robot evaluation. (a) Environment setup of the real-robot experiment. (b) Failure analysis illustrating success/failure rates across different reasoning stages. Task Setup. We evaluate the following natural l ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, our work makes the following key contributions: • We propose MomaGraph, the first scene graph representation that jointly models spatial and functional relationships while incorporating part-level interactive nodes, providin ... | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | As shown in Figure 6, our system achieves an 80% success rate in graph generation, 87.5% success rate in planning (conditioned on correct graphs), and an overall task success rate of 70% ... | p. 11 (6 EXPERIMENTS), p. 22 (Figure/Table caption) |
| Failure/limitation | Figure 6: Quantitative real-robot evaluation. (a) Environment setup of the real-robot experiment. (b) Failure analysis illustrating success/failure rates across different reasoning stages. Task Setup. We evaluate the following natural l ... | p. 11 (Figure/Table caption), p. 11 (7 CONCLUSION) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** 4.1 MOMAGRAPH DEFINITION Given a single indoor room, the agent receives as input a set of multi-view images {Ii}n i=1 and a natural language instruction T . (p. 5, 4 METHOD).
- **Paper-specific mechanism:** In summary, our work makes the following key contributions: • We propose MomaGraph, the first scene graph representation that jointly models spatial and functional relationships while incorporating part-level interactive nodes, ... (p. 2, 1 INTRODUCTION).
- **Evidence boundary:** the reported outcome is Table 2: Performance comparison on the MomaGraph-Bench. We report accuracy (%) across four tiers (T1-T4) and the overall score, with and without graph-based reasoning. Type Models Params MomaGraph Benchmark Tier ... (p. 9, Figure/Table caption); the relevant task/metric cue is We report accuracy (%) across four tiers (T1-T4) and the overall score, with and without graph-based reasoning. (p. 9, 6 EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** (b) Failure analysis illustrating success/failure rates across different reasoning stages. (p. 11, 6 EXPERIMENTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Vision-Language Model, Robotics, 3D Vision, Graph Reasoning`.
- **Reading predecessor in the generated track queue:** Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 6: Quantitative real-robot evaluation. (a) Environment setup of the real-robot experiment. (b) Failure analysis illustrating success/failure rates across different reasoning stages. Task Setup. We evaluate the following natural l ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: 4.1 MOMAGRAPH DEFINITION Given a single indoor room, the agent receives as input a set of multi-view images {Ii}n i=1 and a natural language instruction T . (p. 5, 4 METHOD); preserve the objective/update rule: The overall reward converges to ∼0.93, while accuracy reward stabilizes at ∼0.9. (p. 19, A.3 TRAINING CURVE).
2. Use the paper-reported task/data/environment cue: To rigorously evaluate spatial-functional reasoning and task planning capabilities, we design a comprehensive multi-choice VQA benchmark based on the scenes and tasks in our dataset. (p. 19, A.4.1 BENCHMARK DESIGN).
3. Compare against the reported or matched baseline: Across all models, the w/ Graph setting consistently outperforms the w/o Graph baseline, demonstrating that explicitly structuring task-oriented scene graphs provides a tangible benefit for downstream planning. (p. 9, 6 EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: We report accuracy (%) across four tiers (T1-T4) and the overall score, with and without graph-based reasoning. (p. 9, 6 EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: We report accuracy (%) across four tiers (T1-T4) and the overall score, with and without graph-based reasoning. (p. 9, 6 EXPERIMENTS); if none is reported, design one around: (b) Failure analysis illustrating success/failure rates across different reasoning stages. (p. 11, 6 EXPERIMENTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), match the reported outcome at p. 9 (Figure/Table caption), p. 22 (Figure/Table caption), p. 10 (6 EXPERIMENTS), and measure the boundary at p. 11 (6 EXPERIMENTS), p. 11 (6 EXPERIMENTS).

## Falsifiable research question

Under the paper's stated interface (4.1 MOMAGRAPH DEFINITION Given a single indoor room, the agent receives as input a set of multi-view images {Ii}n i=1 and a ...), does the paper-specific mechanism (In summary, our work makes the following key contributions: • We propose MomaGraph, the first scene graph representation that jointly models spatial ...) retain the reported evaluation outcome (We report accuracy (%) across four tiers (T1-T4) and the overall score, with and without graph-based reasoning.) when tested against the paper's strongest explicit boundary ((b) Failure analysis illustrating success/failure rates across different reasoning stages.)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (We report accuracy (%) across four tiers (T1-T4) and the overall score, with and without graph-based reasoning.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (26 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In summary, our work makes the following key contributions: • We propose MomaGraph, the first scene graph representation that jointly models spatial and functional relationships while incorporating part-level interactive nodes, ... (p. 2, 1 INTRODUCTION).
- **Paper-supported outcome:** Table 2: Performance comparison on the MomaGraph-Bench. We report accuracy (%) across four tiers (T1-T4) and the overall score, with and without graph-based reasoning. Type Models Params MomaGraph Benchmark Tier ... (p. 9, Figure/Table caption).
- **Strongest explicit boundary:** (b) Failure analysis illustrating success/failure rates across different reasoning stages. (p. 11, 6 EXPERIMENTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
