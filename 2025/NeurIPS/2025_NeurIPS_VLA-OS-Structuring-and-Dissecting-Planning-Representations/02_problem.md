# Problem - VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=PQYazNKEYo; PDF retrieval source: https://arxiv.org/pdf/2506.17561. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction)): 3) Bottleneck: Between task planning and policy learning, which presents a greater challenge for current manipulation tasks?

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Recent studies on Vision-Language-Action (VLA) models have shifted from the end-to-end action-generation paradigm toward a pipeline involving task planning followed by action generation, demonstrating improved ...
- **p. 1 / Abstract - extractive body cue:** However, existing approaches vary significantly in terms of network architectures, planning paradigms, representations, and training data sources, making it challenging for researchers to identify the ...
- **p. 1 / Abstract - extractive body cue:** To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we introduce VLA-OS, a ...
- **p. 1 / Abstract - extractive body cue:** Our results demonstrate that: 1) visually grounded planning representations are generally better than language planning representations; 2) the Hierarchical-VLA paradigm generally achieves superior or comparable ...
- **p. 1 / 1 Introduction - extractive body cue:** Building intelligent and generalizable robots capable of perceiving, reasoning about, and interacting with physical environments remains a persistent challenge in the robotics community [34, 23].
- **p. 2 / 1 Introduction - extractive body cue:** 3) Bottleneck: Between task planning and policy learning, which presents a greater challenge for current manipulation tasks?
- **p. 2 / 1 Introduction - extractive body cue:** However, current task-planning approaches in VLA are mainly based on intuitive designs and lack fair and systematic comparisons, as these methods vary along multiple dimensions, ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | 3) Bottleneck: Between task planning and policy learning, which presents a greater challenge for current manipulation tasks? | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | This action head can take as input the images, proprioception observations, and the planning representations to generate actions. | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | action, head, take, input, images, proprioception, observations, planning, representations, generate | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | action, head, take, multi-view, depth, images, input, fuse | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: action, head, take, input, images, proprioception, observations, planning, representations, generate | p. 6 (3.1 Preliminaries), p. 8 (3.1 Preliminaries), p. 5 (3.1 Preliminaries) |
| Decision / output variable | action, pose, option or chunk a; body terms: systematically, investigate, impacts, different, planning, paradigms, representations, isolating | p. 1 (Abstract), p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Objective / loss / cost | policy/action modeling objective; cue terms: implicit, planning, MDT, PIDM, goal, image, foresight, generation | p. 4 (1 Introduction), p. 7 (3.1 Preliminaries), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 6 (3.1 Preliminaries), p. 6 (3.1 Preliminaries) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (3.1 Preliminaries), p. 8 (3.1 Preliminaries), p. 1 (Abstract) |
| Success / guarantee | instruction-conditioned task success | p. 2 (Figure/Table caption), p. 8 (3.1 Preliminaries), p. 7 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** However, current task-planning approaches in VLA are mainly based on intuitive designs and lack fair and systematic comparisons, as these methods vary along multiple dimensions, ...
- **p. 3 / 1 Introduction - extractive body cue:** The problem is that their VLMs and low-level skills usually cannot be trained with further datasets, which frequently places them at a disadvantage compared to ...
- **p. 1 / 1 Introduction - extractive body cue:** Building intelligent and generalizable robots capable of perceiving, reasoning about, and interacting with physical environments remains a persistent challenge in the robotics community [34, 23].
- **p. 3 / 1 Introduction - extractive body cue:** Furthermore, to answer the bottleneck question, we designed a novel set of evaluation metrics tailored to separately assess the performance of task planning and policy ...

## What the Paper Changes

PDF body contribution framing (p. 1 (Abstract), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 8 (3.1 Preliminaries), p. 1 (1 Introduction)): To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we introduce VLA-OS, a unified VLA architecture series capable ...

- **p. 3 / 1 Introduction - extractive body cue:** Furthermore, to answer the bottleneck question, we designed a novel set of evaluation metrics tailored to separately assess the performance of task planning and policy ...
- **p. 3 / 1 Introduction - extractive body cue:** We show in Table 1 that VLA-OS exhibits superior performance compared to most existing VLA methods with fewer parameters and without pretraining.
- **p. 8 / 3.1 Preliminaries - extractive body cue:** For qualitative comparisons, we show in Figure 5 an example that when VLA-OS-H uses the same planning heads as VLA-OS-I-E where there are some planning ...
- **p. 1 / 1 Introduction - extractive body cue:** Recent studies have increasingly emphasized the development of foundational models for robot manipulation tasks by training large Vision-Language-Action models (VLAs) on extensive datasets [8, 82, ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 2 | Figure 1: Left: four different VLA paradigms. Note that in this paper, we didn't explore PlanningOnly- VLA since ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | L V IF DCS IFS DCS IFS DCS IFS VLA-OS-I-I 0.79 - 0.83 - 0.92 - VLA-OS-H 0.81 ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | For qualitative comparisons, we show in Figure 5 an example that when VLA-OS-H uses the same planning heads ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | 5 Conclusion and Limitation We provide a systematic investigation across different VLA paradigms and task planning representations through ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 6 (3.1 Preliminaries), p. 8 (3.1 Preliminaries), p. 5 (3.1 Preliminaries), p. 4 (3.1 Preliminaries). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction), interface p. 6 (3.1 Preliminaries), p. 8 (3.1 Preliminaries), p. 5 (3.1 Preliminaries), p. 4 (3.1 Preliminaries), objective p. 4 (1 Introduction), p. 7 (3.1 Preliminaries), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 6 (3.1 Preliminaries), p. 6 (3.1 Preliminaries).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
