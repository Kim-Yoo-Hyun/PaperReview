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
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Published as a conference paper at ICLR 2026 Figure 2: Direct planning often fails even for strong closed-source models like GPT-5, producing wrong actions or ...
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

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 In this work, we do not focus on the agent's interaction policy; instead, our emphasis lies on how to capture and incorporate observed state changes in the environment into the scene graph ...를 4.1 MOMAGRAPH DEFINITION Given a single indoor room, the agent receives as input a set of multi-view images {Ii}n i=1 and a natural language instruction T .로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 6: Quantitative real-robot evaluation. (a) Environment setup of the real-robot experiment. (b) Failure analysis illustrating success/failure rates across different reasoning stages. Task Setup. We evaluate the following natural l ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, our work makes the following key contributions: • We propose MomaGraph, the first scene graph representation that jointly models spatial and functional relationships while incorporating part-level interactive nodes, providin ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Vision-Language Model, Robotics, 3D Vision, Graph Reasoning`.
- **Reading predecessor in the generated track queue:** Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 6: Quantitative real-robot evaluation. (a) Environment setup of the real-robot experiment. (b) Failure analysis illustrating success/failure rates across different reasoning stages. Task Setup. We evaluate the following natural l ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: To rigorously evaluate spatial-functional reasoning and task planning capabilities, we design a comprehensive multi-choice VQA benchmark based on the scenes and tasks in our dataset..
3. Compare against the body-reported baseline or a matched simpler baseline: Across all models, the w/ Graph setting consistently outperforms the w/o Graph baseline, demonstrating that explicitly structuring task-oriented scene graphs provides a tangible benefit for downstream planning..
4. Report the body metric and its denominator/aggregation: This evaluation includes success rates and failure analysis across different stages to validate overall system performance under realistic, sequential conditions (see Figure 6)..
5. Re-run the body-reported ablation/failure condition: We report accuracy (%) across four tiers (T1-T4) and the overall score, with and without graph-based reasoning..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 6 (4 METHOD), p. 6 (4 METHOD), p. 5 (4 METHOD); the primary result is directionally consistent at p. 11 (6 EXPERIMENTS), p. 22 (Figure/Table caption), p. 11 (6 EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, makes, following mechanism이 Across all models, the w/ Graph setting consistently outperforms the w/o Graph baseline, demonstrating that explicitly ... 대비 This evaluation includes success rates and failure analysis across different stages to validate overall system performance under realistic, ...을 개선하고, Figure 6: Quantitative real-robot evaluation. (a) Environment setup of the real-robot experiment. (b) Failure analysis illustrating ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
