# VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=PQYazNKEYo.
> PDF retrieval source: https://arxiv.org/pdf/2506.17561. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://openreview.net/forum?id=PQYazNKEYo
- Full-text retrieval: https://arxiv.org/pdf/2506.17561
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 3) Bottleneck: Between task planning and policy learning, which presents a greater challenge for current manipulation tasks?를 문제로 두고, To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we introduce VLA-OS, a unified VLA architecture series capable of vario ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent studies on Vision-Language-Action (VLA) models have shifted from the end-to-end action-generation paradigm toward a pipeline involving task planning followed by action generation, demonstrating improved ...
- **p. 1 / Abstract - extractive body cue:** However, existing approaches vary significantly in terms of network architectures, planning paradigms, representations, and training data sources, making it challenging for researchers to identify the ...
- **p. 1 / Abstract - extractive body cue:** To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we introduce VLA-OS, a ...
- **p. 1 / Abstract - extractive body cue:** Our results demonstrate that: 1) visually grounded planning representations are generally better than language planning representations; 2) the Hierarchical-VLA paradigm generally achieves superior or comparable ...
- **p. 1 / 1 Introduction - extractive body cue:** Building intelligent and generalizable robots capable of perceiving, reasoning about, and interacting with physical environments remains a persistent challenge in the robotics community [34, 23].
- **p. 2 / 1 Introduction - extractive body cue:** 3) Bottleneck: Between task planning and policy learning, which presents a greater challenge for current manipulation tasks?
- **p. 2 / 1 Introduction - extractive body cue:** However, current task-planning approaches in VLA are mainly based on intuitive designs and lack fair and systematic comparisons, as these methods vary along multiple dimensions, ...

## Core Idea

- **p. 1 / Abstract - extractive body cue:** To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we introduce VLA-OS, a ...
- **p. 3 / 1 Introduction - extractive body cue:** Furthermore, to answer the bottleneck question, we designed a novel set of evaluation metrics tailored to separately assess the performance of task planning and policy ...
- **p. 3 / 1 Introduction - extractive body cue:** We show in Table 1 that VLA-OS exhibits superior performance compared to most existing VLA methods with fewer parameters and without pretraining.
- **p. 8 / 3.1 Preliminaries - extractive body cue:** For qualitative comparisons, we show in Figure 5 an example that when VLA-OS-H uses the same planning heads as VLA-OS-I-E where there are some planning ...
- **p. 1 / 1 Introduction - extractive body cue:** Recent studies have increasingly emphasized the development of foundational models for robot manipulation tasks by training large Vision-Language-Action models (VLAs) on extensive datasets [8, 82, ...
- **p. 6 / 3.1 Preliminaries - extractive body cue:** As shown in Figure 2, we use the VLM together with planning heads for task planning, and modify the action head to an encoder-decoder transformer ...
- **p. 4 / 3.1 Preliminaries - extractive body cue:** Then, we use a separate set of weights as an action head for the robotics-specific tokens (action and proprioception states).
- **p. 2 / 1 Introduction - extractive body cue:** This motivates future work on improving training and inference algorithms for Hierarchical-VLA models. actions, these methods demonstrate stronger capabilities in task reasoning and comprehension for ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | This action head can take as input the images, proprioception observations, and the planning representations to generate actions. | image/video, language instruction, proprioception과 history | p. 6 (3.1 Preliminaries), p. 8 (3.1 Preliminaries) |
| State/latent | action, head, take, input, images, proprioception, observations, planning, representations, generate, actions, Instead | language-grounded task state와 action-policy context | p. 6 (3.1 Preliminaries), p. 8 (3.1 Preliminaries), p. 5 (3.1 Preliminaries) |
| Output/action | Instead, Hierarchical-VLA will not only take in the raw visual observation and language instruction as inputs, but also confine the planning accumulation errors exclusively to the explicit representation level, rather than allowing ... | continuous action, pose 또는 action chunk | p. 8 (3.1 Preliminaries), p. 5 (3.1 Preliminaries), p. 4 (3.1 Preliminaries) |
| Objective/outcome | For implicit planning, MDT [69] and PIDM [77] use goal image foresight generation loss as an auxiliary objective for planning, while RoboBrain [39] and ChatVLA [104] train VLA with auxiliary task reasoning ... | instruction following, task success, generalization과 latency | p. 4 (1 Introduction), p. 7 (3.1 Preliminaries), p. 3 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 1 / Abstract - extractive body cue:** To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we introduce VLA-OS, a ...
- **p. 3 / 1 Introduction - extractive body cue:** Furthermore, to answer the bottleneck question, we designed a novel set of evaluation metrics tailored to separately assess the performance of task planning and policy ...
- **p. 3 / 1 Introduction - extractive body cue:** We show in Table 1 that VLA-OS exhibits superior performance compared to most existing VLA methods with fewer parameters and without pretraining.
- **p. 8 / 3.1 Preliminaries - extractive body cue:** For qualitative comparisons, we show in Figure 5 an example that when VLA-OS-H uses the same planning heads as VLA-OS-I-E where there are some planning ...
- **p. 1 / 1 Introduction - extractive body cue:** Recent studies have increasingly emphasized the development of foundational models for robot manipulation tasks by training large Vision-Language-Action models (VLAs) on extensive datasets [8, 82, ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Left: four different VLA paradigms. Note that in this paper, we didn't explore PlanningOnly- VLA since they usually cannot be trained with the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Sanity check. Success rates on four LIBERO benchmarks. Baseline results are from their papers [43, 8, 44]. Our results are the average of ...
- **p. 9 / 3.1 Preliminaries - extractive body cue:** Finding 11: The performance of all VLA paradigms improves as the amount of action-labeled demonstration data increases, i.e., all VLA paradigms have the data scalability.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 2 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Embodiment/environment | 4.3 More Performance, Generalization, and Benefit from Planning Head Pretraining To further compare different planning paradigms, we perform additional experiments to explore their performance on: 1) more manipulation benchmarks includi ... | hardware/simulator version and reset protocol | p. 8 (3.1 Preliminaries), p. 8 (3.1 Preliminaries) |
| Dataset/benchmark | For data scalability, we use LIBERO-LONG [51], a dataset with 10 tasks with a total of 500 demonstrations. | role, split, size and leakage | p. 8 (3.1 Preliminaries), p. 8 (3.1 Preliminaries), p. 9 (3.1 Preliminaries), p. 9 (3.1 Preliminaries) |
| Metric | Figure 1: Left: four different VLA paradigms. Note that in this paper, we didn't explore PlanningOnly- VLA since they usually cannot be trained with the provided datasets and perform worse than others. ... | definition, denominator, direction and uncertainty | p. 2 (Figure/Table caption), p. 8 (3.1 Preliminaries), p. 7 (Figure/Table caption) |
| Baseline/ablation | Table 1: Sanity check. Success rates on four LIBERO benchmarks. Baseline results are from their papers [43, 8, 44]. Our results are the average of top-3 checkpoints averaged over 20 rollouts for ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 5 (Figure/Table caption), p. 8 (3.1 Preliminaries) |

## Explicit Limitations and Failure Boundary

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Left: four different VLA paradigms. Note that in this paper, we didn't explore PlanningOnly- VLA since they usually cannot be trained with the ...
- **p. 9 / 3.1 Preliminaries - extractive body cue:** L V IF DCS IFS DCS IFS DCS IFS VLA-OS-I-I 0.79 - 0.83 - 0.92 - VLA-OS-H 0.81 0.84 0.86 0.93 0.94 0.90 It is ...
- **p. 8 / 3.1 Preliminaries - extractive body cue:** For qualitative comparisons, we show in Figure 5 an example that when VLA-OS-H uses the same planning heads as VLA-OS-I-E where there are some planning ...
- **p. 11 / 3.1 Preliminaries - extractive body cue:** 5 Conclusion and Limitation We provide a systematic investigation across different VLA paradigms and task planning representations through various kinds of manipulation tasks.
- **p. 11 / 1. Why are visually grounded representations better than language? - extractive body cue:** The limitations of this paper are: 1) despite the VLA-OS family encompassing a wide array of task planning paradigms for VLA, there remain several designs ...
- **p. 8 / 3.1 Preliminaries - extractive body cue:** Meanwhile, the action head does not receive raw visual or language inputs.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 3) Bottleneck: Between task planning and policy learning, which presents a greater challenge for current manipulation tasks?를 문제로 두고, To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we introduce VLA-OS, a unified VLA architecture series capable of vario ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction), p. 6 (3.1 Preliminaries) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
