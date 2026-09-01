# Method - NavBench: Probing Multimodal Large Language Models for Embodied Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=nf8PKQKtl2; PDF retrieval source: https://openreview.net/pdf/1ef1a313c6a3eea3eea8cfe4ac568866df673dec.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction), p. 7 (C Progress Level), p. 6 (C Progress Level), p. 2 (1 Introduction)): To support real-world deployment, we introduce a pipeline that converts MLLMs' outputs into robotic actions.

## Method Body Digest

- **p. 1 / Abstract - extractive PDF cue:** To support real-world deployment, we introduce a pipeline that converts MLLMs' outputs into robotic actions.
- **p. 1 / Abstract - extractive PDF cue:** NavBench consists of two components: (1) navigation comprehension, assessed through three cognitively grounded tasks including global instruction alignment, temporal progress estimation, and local observation-action reasoning, ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Local Observation-Action Inference evaluates the model's ability to reason about the spatial consequences of individual actions by either predicting the future observation given an action ...
- **p. 7 / C Progress Level - extractive PDF cue:** It consists of three modules: (1) a Waypoint Predictor that extracts RGB and depth inputs to generate candidate waypoints, (2) an MLLM Decision Module that ...
- **p. 6 / C Progress Level - extractive PDF cue:** Local Observation-Action Reasoning We design two multiple-choice reasoning tasks to evaluate a model's capacity for local spatial and action reasoning inference.
- **p. 2 / 1 Introduction - extractive PDF cue:** First, can the model comprehend what a navigation behavior represents, such as identifying the intent behind a completed trajectory?
- **p. 3 / 1 Introduction - extractive PDF cue:** Finally, to bridge the gap between simulator-based evaluation and real-world deployment, we design a practical navigation pipeline that connects MLLM outputs to executable actions on ...
- **p. 6 / C Progress Level - extractive PDF cue:** To ensure data quality and minimize ambiguity, we applied a combination of automatic filtering and manual validation to retain instruction-path pairs with well-defined temporal boundaries ...

## Design Rationale

- **p. 3 / 1 Introduction - extractive PDF cue:** In summary, our main contributions are as follows: (1) We introduce NavBench, a benchmark for evaluating MLLMs in embodied navigation under zero-shot settings.
- **p. 2 / 1 Introduction - extractive PDF cue:** To fill these gaps, we introduce NavBench, a benchmark designed to systematically evaluate MLLMs in embodied navigation under zero-shot settings.
- **p. 3 / 1 Introduction - extractive PDF cue:** This pipeline includes a waypoint selection module, an MLLM-based navigator, and a low-level controller, demonstrating the deployability of our framework in physical environments.

## Source Evidence Cues

- **p. 1 / Abstract - extractive PDF cue:** To support real-world deployment, we introduce a pipeline that converts MLLMs' outputs into robotic actions.
- **p. 1 / Abstract - extractive PDF cue:** NavBench consists of two components: (1) navigation comprehension, assessed through three cognitively grounded tasks including global instruction alignment, temporal progress estimation, and local observation-action reasoning, ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Local Observation-Action Inference evaluates the model's ability to reason about the spatial consequences of individual actions by either predicting the future observation given an action ...
- **p. 7 / C Progress Level - extractive PDF cue:** It consists of three modules: (1) a Waypoint Predictor that extracts RGB and depth inputs to generate candidate waypoints, (2) an MLLM Decision Module that ...
- **p. 6 / C Progress Level - extractive PDF cue:** Local Observation-Action Reasoning We design two multiple-choice reasoning tasks to evaluate a model's capacity for local spatial and action reasoning inference.
- **p. 2 / 1 Introduction - extractive PDF cue:** First, can the model comprehend what a navigation behavior represents, such as identifying the intent behind a completed trajectory?
- **p. 3 / 1 Introduction - extractive PDF cue:** Finally, to bridge the gap between simulator-based evaluation and real-world deployment, we design a practical navigation pipeline that connects MLLM outputs to executable actions on ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | To support real-world deployment, we introduce a pipeline that converts MLLMs' outputs into robotic actions. | p. 1 (Abstract), p. 1 (Abstract) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | NavBench consists of two components: (1) navigation comprehension, assessed through three cognitively grounded tasks including global instruction alignment, temporal progress estimation, and ... | p. 1 (Abstract), p. 2 (1 Introduction) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | Local Observation-Action Inference evaluates the model's ability to reason about the spatial consequences of individual actions by either predicting the future observation ... | p. 2 (1 Introduction), p. 7 (C Progress Level) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / C Progress Level - extractive PDF cue:** To ensure data quality and minimize ambiguity, we applied a combination of automatic filtering and manual validation to retain instruction-path pairs with well-defined temporal boundaries ...
- **p. 4 / C Progress Level - extractive PDF cue:** (2) Future-Action Prediction - the model observes two consecutive views and must identify the action that caused the transition.
- **p. 4 / C Progress Level - extractive PDF cue:** To ensure a fair and standardized evaluation protocol, we evaluate MLLMs via viewpoint selection rather than low-level action prediction (e.g., turning or moving forward).
- **p. 1 / Abstract - extractive PDF cue:** However, most models struggle with temporal understanding, particularly in estimating progress during navigation, which may pose a key challenge.
- **p. 1 / Abstract - extractive PDF cue:** NavBench consists of two components: (1) navigation comprehension, assessed through three cognitively grounded tasks including global instruction alignment, temporal progress estimation, and local observation-action reasoning, ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Step-by-step Navigation Comprehension - Progress Level Given the steps taken so far, how far along am I in the instruction?
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | NavBench, consists, components, navigation, comprehension, assessed, through, three, cognitively, grounded, tasks, including, global, instruction | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | NavBench, consists, components, navigation, comprehension, assessed, through, three, cognitively, grounded | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | summary, main, contributions, follows, introduce, NavBench, benchmark, evaluating, MLLMs, embodied | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | ensure, data, quality, minimize, ambiguity, applied, combination, automatic, filtering, manual | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Abstract - extractive PDF cue:** NavBench consists of two components: (1) navigation comprehension, assessed through three cognitively grounded tasks including global instruction alignment, temporal progress estimation, and local observation-action reasoning, ...
- **p. 4 / C Progress Level - extractive PDF cue:** This evaluates the model's capacity to monitor task progress and comprehend the temporal structure of instructions. • Local Level - Local Observation-Action Reasoning: To evaluate ...
- **p. 5 / C Progress Level - extractive PDF cue:** Formally, at each step t of a navigation episode, the MLLM receives an instruction x " tw1, w2, ..., wLu of length L, a set ...
- **p. 1 / 1 Introduction - extractive PDF cue:** In comparison, navigation is a core embodied task that involves interpreting natural language instructions, analyzing visual observations, and making a sequence of decisions to reach ...
- **p. 5 / C Progress Level - extractive PDF cue:** The image extraction process involves traversing agent paths, sampling intermediate viewpoints, and rendering corresponding visual observations.
- **p. 7 / C Progress Level - extractive PDF cue:** It consists of three modules: (1) a Waypoint Predictor that extracts RGB and depth inputs to generate candidate waypoints, (2) an MLLM Decision Module that ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Local Observation-Action Inference evaluates the model's ability to reason about the spatial consequences of individual actions by either predicting the future observation given an action ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | This is likely because the task itself already follows a step-by-step process: at each time step, the model receives the full instruction ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | NavBench consists of two components: (1) navigation comprehension, assessed through three cognitively grounded tasks including global instruction alignment, temporal progress estimation, and ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | This is likely because the task itself already follows a step-by-step process: at each time step, the model receives the full instruction ... | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | NavBench consists of two components: (1) navigation comprehension, assessed through three cognitively grounded tasks including global instruction alignment, temporal progress estimation, and ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 Introduction - extractive PDF cue:** Local Observation-Action Inference evaluates the model's ability to reason about the spatial consequences of individual actions by either predicting the future observation given an action ...
- **p. 6 / C Progress Level - extractive PDF cue:** Local Observation-Action Reasoning We design two multiple-choice reasoning tasks to evaluate a model's capacity for local spatial and action reasoning inference.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** support, real-world, deployment, introduce, pipeline, converts, MLLMs, outputs, robotic, actions, NavBench, consists, components, navigation, comprehension, assessed, through, three, cognitively, grounded.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Real-World Validation To assess the feasibility of our real-world deployment pipeline, we conduct a pilot study in an indoor environment using GPT-4o ... | p. 10 (5.3 Discussion), p. 7 (C Progress Level) |
| Global / local decision | As shown in Figure 7, models show consistent performance across both, with GPT-4o clearly outperforming all others, consistent with its strong results ... | p. 9 (5.3 Discussion), p. 10 (5.3 Discussion) |
| Motion execution / recovery | As shown in Table 2, the presence of map information consistently improves success rates, with the largest gain observed under medium difficulty, ... | p. 9 (5.3 Discussion), p. 8 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 9 / 5.3 Discussion - extractive PDF cue:** Effect of Map Information on Action Decisions Although our benchmark evaluations assume no access to map information, reflecting real-world constraints, we investigate whether providing map ...
- **p. 10 / 5.3 Discussion - extractive PDF cue:** Avg Accuracy SR SPL SR SPL SR SPL GPT-4o 51.33 42.90 65.80 53.34 67.36 54.31 41.67 35.71 27.78 21.15 41.33 GPT-4o + CoT 60.42 40.20 ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: NavBench evaluates MLLMs across three comprehension tasks and a step-by-step execution task, assessing their ability to understand navigation behavior, track progress, reason about ...
- **p. 9 / 5.3 Discussion - extractive PDF cue:** Using GPT-4o, we compare performance with and without map input across different difficulty levels.
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 3: Performance comparison with and without CoT prompting.
- **p. 10 / 5.3 Discussion - extractive PDF cue:** This suggests execution failures often stem from temporal and spatial reasoning limitations, reinforcing the diagnostic value of NavBench.
- **p. 10 / 5.3 Discussion - extractive PDF cue:** Based on thought traces and action sequences, we identify four common error types: (a) Incorrect Plan: the plan misaligns with the instruction; (b) Misaligned Action: ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction), p. 7 (C Progress Level), p. 6 (C Progress Level), p. 2 (1 Introduction), objective p. 6 (C Progress Level), p. 4 (C Progress Level), p. 4 (C Progress Level), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction), temporal p. 10 (5.3 Discussion), p. 1 (Abstract), p. 5 (C Progress Level), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (C Progress Level).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
