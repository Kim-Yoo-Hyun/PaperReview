# Insights — VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=PQYazNKEYo; PDF retrieval source: https://arxiv.org/pdf/2506.17561. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / Abstract - extractive body cue:** To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we introduce VLA-OS, a ...
- **p. 3 / 1 Introduction - extractive body cue:** Furthermore, to answer the bottleneck question, we designed a novel set of evaluation metrics tailored to separately assess the performance of task planning and policy ...
- **p. 3 / 1 Introduction - extractive body cue:** We show in Table 1 that VLA-OS exhibits superior performance compared to most existing VLA methods with fewer parameters and without pretraining.
- **p. 8 / 3.1 Preliminaries - extractive body cue:** For qualitative comparisons, we show in Figure 5 an example that when VLA-OS-H uses the same planning heads as VLA-OS-I-E where there are some planning ...
- **p. 1 / 1 Introduction - extractive body cue:** Recent studies have increasingly emphasized the development of foundational models for robot manipulation tasks by training large Vision-Language-Action models (VLAs) on extensive datasets [8, 82, ...
- **p. 6 / 3.1 Preliminaries - extractive body cue:** As shown in Figure 2, we use the VLM together with planning heads for task planning, and modify the action head to an encoder-decoder transformer ...
- **p. 4 / 3.1 Preliminaries - extractive body cue:** Then, we use a separate set of weights as an action head for the robotics-specific tokens (action and proprioception states).
- **Contribution anchor:** p. 1 (Abstract), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 8 (3.1 Preliminaries), p. 1 (1 Introduction), p. 6 (3.1 Preliminaries)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** 3) Bottleneck: Between task planning and policy learning, which presents a greater challenge for current manipulation tasks?
- **p. 2 / 1 Introduction - extractive body cue:** However, current task-planning approaches in VLA are mainly based on intuitive designs and lack fair and systematic comparisons, as these methods vary along multiple dimensions, ...
- **p. 3 / 1 Introduction - extractive body cue:** The problem is that their VLMs and low-level skills usually cannot be trained with further datasets, which frequently places them at a disadvantage compared to ...
- **p. 1 / 1 Introduction - extractive body cue:** Building intelligent and generalizable robots capable of perceiving, reasoning about, and interacting with physical environments remains a persistent challenge in the robotics community [34, 23].
- **p. 3 / 1 Introduction - extractive body cue:** Furthermore, to answer the bottleneck question, we designed a novel set of evaluation metrics tailored to separately assess the performance of task planning and policy ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Left: four different VLA paradigms. Note that in this paper, we didn't explore PlanningOnly- VLA since they usually cannot be trained with the ...
- **p. 9 / 3.1 Preliminaries - extractive body cue:** L V IF DCS IFS DCS IFS DCS IFS VLA-OS-I-I 0.79 - 0.83 - 0.92 - VLA-OS-H 0.81 0.84 0.86 0.93 0.94 0.90 It is ...
- **Boundary to test:** Figure 1: Left: four different VLA paradigms. Note that in this paper, we didn't explore PlanningOnly- VLA since they usually cannot be trained with the provided datasets and perform worse than others. ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we introduce VLA-OS, a unified VLA architecture series capable of vario ... | p. 1 (Abstract), p. 3 (1 Introduction) |
| Reported outcome | Figure 1: Left: four different VLA paradigms. Note that in this paper, we didn't explore PlanningOnly- VLA since they usually cannot be trained with the provided datasets and perform worse than others. ... | p. 2 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Failure/limitation | Figure 1: Left: four different VLA paradigms. Note that in this paper, we didn't explore PlanningOnly- VLA since they usually cannot be trained with the provided datasets and perform worse than others. ... | p. 2 (Figure/Table caption), p. 9 (3.1 Preliminaries) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 This action head can take as input the images, proprioception observations, and the planning representations to generate actions.를 Instead, Hierarchical-VLA will not only take in the raw visual observation and language instruction as inputs, but also confine the planning accumulation errors exclusively to the explicit representation level, rather than allowing ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 1: Left: four different VLA paradigms. Note that in this paper, we didn't explore PlanningOnly- VLA since they usually cannot be trained with the provided datasets and perform worse than others. ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we introduce VLA-OS, a unified VLA architecture series capable of vario ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Robotics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 1: Left: four different VLA paradigms. Note that in this paper, we didn't explore PlanningOnly- VLA since they usually cannot be trained with the provided datasets and perform worse than others. ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 4.3 More Performance, Generalization, and Benefit from Planning Head Pretraining To further compare different planning paradigms, we perform additional experiments to explore their performance on: 1) more manipulation benchmarks includi ....
3. Compare against the body-reported baseline or a matched simpler baseline: Table 1: Sanity check. Success rates on four LIBERO benchmarks. Baseline results are from their papers [43, 8, 44]. Our results are the average of top-3 checkpoints averaged over 20 rollouts for ....
4. Report the body metric and its denominator/aggregation: Figure 1: Left: four different VLA paradigms. Note that in this paper, we didn't explore PlanningOnly- VLA since they usually cannot be trained with the provided datasets and perform worse than others. ....
5. Re-run the body-reported ablation/failure condition: For 3), a lot of literature [27, 48, 13, 72, 94, 91] claim that the primary advantage of using task planning in VLA rather than ActionOnly-VLA is that their task-planning components can ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 6 (3.1 Preliminaries), p. 1 (Abstract), p. 4 (3.1 Preliminaries); the primary result is directionally consistent at p. 2 (Figure/Table caption), p. 7 (Figure/Table caption), p. 9 (3.1 Preliminaries); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 systematically, investigate, impacts mechanism이 Table 1: Sanity check. Success rates on four LIBERO benchmarks. Baseline results are from their papers ... 대비 Figure 1: Left: four different VLA paradigms. Note that in this paper, we didn't explore PlanningOnly- VLA since ...을 개선하고, Figure 1: Left: four different VLA paradigms. Note that in this paper, we didn't explore PlanningOnly- ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
