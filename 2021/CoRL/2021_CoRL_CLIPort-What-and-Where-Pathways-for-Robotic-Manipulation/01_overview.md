# CLIPort: What and Where Pathways for Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2109.12098.
> PDF retrieval source: https://arxiv.org/pdf/2109.12098. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: CORE
- Tags: Robotics, Vision-Language-Action, CLIP, manipulation
- Official paper: https://arxiv.org/abs/2109.12098
- Full-text retrieval: https://arxiv.org/pdf/2109.12098
- Code/Project: https://cliport.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, these models lack a fine-grained understanding on how to manipulate objects, i.e. physical affordances. †Work done partly while the author was a part-time intern at NVIDIA.를 문제로 두고, We propose 10 language-conditioned tasks with 1000s of unique instances per task that require both semantic and spatial reasoning (see Figure 1 a-j).를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** How can we imbue robots with the ability to manipulate objects precisely but also to reason about them in terms of abstract concepts?
- **p. 1 / Abstract - extractive body cue:** Recent works in manipulation have shown that end-to-end networks can learn dexterous skills that require precise spatial reasoning, but these methods often fail to generalize ...
- **p. 1 / Abstract - extractive body cue:** In parallel, there has been great progress in learning generalizable semantic representations for vision and language by training on large-scale internet data, however these representations ...
- **p. 1 / Abstract - extractive body cue:** To this end, we propose a framework that combines the best of both worlds: a two-stream architecture with semantic and spatial pathways for vision-based manipulation.
- **p. 1 / Abstract - extractive body cue:** Specifically, we present CLIPORT, a language-conditioned imitationlearning agent that combines the broad semantic understanding (what) of CLIP [1] with the spatial precision (where) of Transporter ...
- **p. 1 / 1 Introduction - extractive body cue:** However, these models lack a fine-grained understanding on how to manipulate objects, i.e. physical affordances. †Work done partly while the author was a part-time intern ...
- **p. 1 / 1 Introduction - extractive body cue:** While language-grounding for manipulation has been explored in the past [7, 8, 9, 10], these pipelines are limited by object-centric representations that cannot handle granular ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** We propose 10 language-conditioned tasks with 1000s of unique instances per task that require both semantic and spatial reasoning (see Figure 1 a-j).
- **p. 2 / 1 Introduction - extractive body cue:** Specifically, we present CLIPORT, a languageconditioned imitation-learning agent that integrates the semantic understanding (what) of CLIP [1] with the spatial precision (where) of Transporter [2].
- **p. 3 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • An extended benchmark of language-grounding tasks for manipulation in Ravens [2]. • Two-stream architecture for using internet ...
- **p. 1 / Abstract - extractive body cue:** To this end, we propose a framework that combines the best of both worlds: a two-stream architecture with semantic and spatial pathways for vision-based manipulation.
- **p. 1 / Abstract - extractive body cue:** Experiments in simulated and real-world settings show that our approach is data efficient in few-shot settings and generalizes effectively to seen and unseen semantic concepts.
- **p. 2 / 1 Introduction - extractive body cue:** The key insight of the approach is formulating tabletop manipulation as a series of pick-and-place affordance predictions, where the objective is to detect actions rather ...
- **p. 2 / 1 Introduction - extractive body cue:** We introduce a two-stream architecture for manipulation with semantic and spatial pathways broadly inspired by (or vaguely analogous to) the two-stream hypothesis in cognitive psychology ...
- **p. 1 / 1 Introduction - extractive body cue:** In parallel, there has been great progress in learning models for visual representations [11, 12] and aligning representations of vision and language [13, 14, 15] ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The key insight of the approach is formulating tabletop manipulation as a series of pick-and-place affordance predictions, where the objective is to detect actions rather than detect objects and then learn a ... | image/video, language instruction, proprioception과 history | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| State/latent | insight, formulating, tabletop, manipulation, series, pick-and-place, affordance, predictions, where, objective, detect, actions | language-grounded task state와 action-policy context | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (Abstract) |
| Output/action | In realistic human-robot interaction settings, collecting additional demonstrations or providing goal-images is often infeasible and unscalable. | continuous action, pose 또는 action chunk | p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction) |
| Objective/outcome | The key insight of the approach is formulating tabletop manipulation as a series of pick-and-place affordance predictions, where the objective is to detect actions rather than detect objects and then learn a ... | instruction following, task success, generalization과 latency | p. 2 (1 Introduction), p. 1 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** We propose 10 language-conditioned tasks with 1000s of unique instances per task that require both semantic and spatial reasoning (see Figure 1 a-j).
- **p. 2 / 1 Introduction - extractive body cue:** Specifically, we present CLIPORT, a languageconditioned imitation-learning agent that integrates the semantic understanding (what) of CLIP [1] with the spatial precision (where) of Transporter [2].
- **p. 3 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • An extended benchmark of language-grounding tasks for manipulation in Ravens [2]. • Two-stream architecture for using internet ...
- **p. 1 / Abstract - extractive body cue:** To this end, we propose a framework that combines the best of both worlds: a two-stream architecture with semantic and spatial pathways for vision-based manipulation.
- **p. 1 / Abstract - extractive body cue:** Experiments in simulated and real-world settings show that our approach is data efficient in few-shot settings and generalizes effectively to seen and unseen semantic concepts.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Language-Conditioned Test Results. Task success scores (mean %) from 100 evaluation instances vs. # of training demonstrations (1, 10, 100, or 1000). The ...
- **p. 22 / Figure/Table caption - extractive body cue:** Table 6. Demo-Conditioned Tasks. Validation task success scores (mean %) from 100 evaluation instances vs. # of demonstration episodes (1, 10, 100, or 1000) used ...
- **p. 7 / 4 Results - extractive body cue:** Tasks that require generalizing to novel colors, shapes, and objects are more difficult and all our agents achieve relatively lower performance on these tasks, as ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 22 (Figure/Table caption) |
| Embodiment/environment | For packing objects, we use 56 tabletop objects from the Google Scanned Objects dataset [61] and split them into 37 seen and 19 unseen objects. | hardware/simulator version and reset protocol | p. 6 (4 Results), p. 8 (4 Results) |
| Dataset/benchmark | The setup provides a systematic and reproducible environment for evaluation, especially for benchmarking the ability to ground semantic concepts like colors and object categories. | role, split, size and leakage | p. 6 (4 Results), p. 8 (4 Results), p. 6 (4 Results), p. 8 (4 Results) |
| Metric | Success rates (%) of a multi-task model trained an evaluated 9 real-world tasks (see Figure 1). | definition, denominator, direction and uncertainty | p. 8 (4 Results), p. 6 (4 Results), p. 7 (4 Results) |
| Baseline/ablation | We perform experiments both in simulation and hardware aimed at answering the following questions: 1) How effective is the language-conditioned two-stream architecture for fine-grained manipulation compared to one-stream alternatives an ... | fair input/data/compute/action matching | p. 6 (4 Results), p. 6 (4 Results), p. 21 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5 Conclusion - extractive body cue:** As such, it cannot handle complex partially-observable scenes, or output continuous control for multi-fingered hands, or predict task-completion (see Appendix I for an extended discussion).
- **p. 6 / 4 Results - extractive body cue:** Although Transporter-only does not receive any language goals, it shows what can be achieved through chance by exploiting the most likely actions seen during training.
- **p. 7 / 4 Results - extractive body cue:** Future works could use better sampling methods that balance tasks according to their average time horizon.
- **p. 6 / 4 Results - extractive body cue:** Each camera has a resolution of 640 × 480 and is noiseless.
- **p. 7 / 4 Results - extractive body cue:** It also validates a trait of data-driven approaches where training on lots of diverse data leads to more robust and generalizable representations [1, 63].
- **p. 8 / 4 Results - extractive body cue:** We estimate that for more robust real-world performance at least 50 to 100 training demonstrations are necessary, as evident in Figure 3.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, these models lack a fine-grained understanding on how to manipulate objects, i.e. physical affordances. †Work done partly while the author was a part-time intern at NVIDIA.를 문제로 두고, We propose 10 language-conditioned tasks with 1000s of unique instances per task that require both semantic and spatial reasoning (see Figure 1 a-j).를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (24 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, these models lack a fine-grained understanding on how to manipulate objects, i.e. physical affordances. †Work done partly while the author was a part-time intern at NVIDIA. (p. 1, 1 Introduction).
- **Actual contribution:** We propose 10 language-conditioned tasks with 1000s of unique instances per task that require both semantic and spatial reasoning (see Figure 1 a-j). (p. 2, 1 Introduction).
- **Evaluation boundary:** Table 1. Language-Conditioned Test Results. Task success scores (mean %) from 100 evaluation instances vs. # of training demonstrations (1, 10, 100, or 1000). The challenges pertaining to each task ... (p. 7, Figure/Table caption).
- **Explicit failure boundary:** While language-grounding for manipulation has been explored in the past [7, 8, 9, 10], these pipelines are limited by object-centric representations that cannot handle granular or deformable objects and often ... (p. 1, 1 Introduction).
