# Method - MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=3eTr9dGwJv; PDF retrieval source: https://openreview.net/pdf/3f888689e829f4172ae97d1dfac5f1b62ddb30c3.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 6 (4 METHOD), p. 6 (4 METHOD), p. 5 (4 METHOD), p. 5 (4 METHOD), p. 19 (A.3 TRAINING CURVE), p. 7 (4 METHOD)): To address these limitations, we introduce MomaGraph-Scenes, the first dataset designed to provide a more comprehensive and task-relevant scene representation.

## Method Body Digest

- **p. 6 / 4 METHOD - extractive body cue:** To address these limitations, we introduce MomaGraph-Scenes, the first dataset designed to provide a more comprehensive and task-relevant scene representation.
- **p. 6 / 4 METHOD - extractive body cue:** After the agent executes an action at and observes the new environment state st+1, the scene graph is refined as: G(t+1) T = U  ...
- **p. 5 / 4 METHOD - extractive body cue:** Reinforcement learning offers a more principled approach by encouraging the model to explore, reason, and iteratively refine its representations through outcome-driven feedback.
- **p. 5 / 4 METHOD - extractive body cue:** 4.2 VLMS LEARN SCENE GRAPH REPRESENTATIONS WITH REINFORCEMENT LEARNING Existing open-source VLMs have demonstrated limited capability in generating accurate taskoriented scene graphs GT from multi-view ...
- **p. 19 / A.3 TRAINING CURVE - extractive body cue:** The format reward quickly reaches 1.0 within the first 25 steps, showing the model rapidly learns to produce valid JSON-structured outputs.
- **p. 7 / 4 METHOD - extractive body cue:** This flexible setup better reflects realistic perception conditions, where embodied agents must reason across partial and diverse observations to build consistent scene graph representations.
- **p. 7 / 4 METHOD - extractive body cue:** This design encourages the model to learn how to ground natural instructions into the appropriate set of objects and relationships, rather than relying on object ...
- **p. 5 / 4 METHOD - extractive body cue:** The objective is to construct an instruction-conditioned, task-oriented scene graph GT = (NT , ET s , ET f ).

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, our work makes the following key contributions: • We propose MomaGraph, the first scene graph representation that jointly models spatial and functional relationships ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To achieve this goal, we present MomaGraph, a novel scene representation specifically designed for embodied agents.
- **p. 6 / 4 METHOD - extractive body cue:** To address these limitations, we introduce MomaGraph-Scenes, the first dataset designed to provide a more comprehensive and task-relevant scene representation.

## Source Evidence Cues

- **p. 6 / 4 METHOD - extractive body cue:** To address these limitations, we introduce MomaGraph-Scenes, the first dataset designed to provide a more comprehensive and task-relevant scene representation.
- **p. 6 / 4 METHOD - extractive body cue:** After the agent executes an action at and observes the new environment state st+1, the scene graph is refined as: G(t+1) T = U  ...
- **p. 5 / 4 METHOD - extractive body cue:** Reinforcement learning offers a more principled approach by encouraging the model to explore, reason, and iteratively refine its representations through outcome-driven feedback.
- **p. 5 / 4 METHOD - extractive body cue:** 4.2 VLMS LEARN SCENE GRAPH REPRESENTATIONS WITH REINFORCEMENT LEARNING Existing open-source VLMs have demonstrated limited capability in generating accurate taskoriented scene graphs GT from multi-view ...
- **p. 19 / A.3 TRAINING CURVE - extractive body cue:** The format reward quickly reaches 1.0 within the first 25 steps, showing the model rapidly learns to produce valid JSON-structured outputs.
- **p. 7 / 4 METHOD - extractive body cue:** This flexible setup better reflects realistic perception conditions, where embodied agents must reason across partial and diverse observations to build consistent scene graph representations.
- **p. 7 / 4 METHOD - extractive body cue:** This design encourages the model to learn how to ground natural instructions into the appropriate set of objects and relationships, rather than relying on object ...
- **Detected method headings:** 4 METHOD (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | To address these limitations, we introduce MomaGraph-Scenes, the first dataset designed to provide a more comprehensive and task-relevant scene representation. | p. 6 (4 METHOD), p. 6 (4 METHOD) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | After the agent executes an action at and observes the new environment state st+1, the scene graph is refined as: G(t+1) T ... | p. 6 (4 METHOD), p. 5 (4 METHOD) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | Reinforcement learning offers a more principled approach by encouraging the model to explore, reason, and iteratively refine its representations through outcome-driven feedback. | p. 5 (4 METHOD), p. 5 (4 METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4 METHOD - extractive body cue:** The objective is to construct an instruction-conditioned, task-oriented scene graph GT = (NT , ET s , ET f ).
- **p. 5 / 4 METHOD - extractive body cue:** The final reward function integrates these task-oriented design principles with format validation and length control, where Rformat ensures valid JSON structure and Rlength penalizes overly ...
- **p. 6 / 4 METHOD - extractive body cue:** This reward design directly implements our core insight: scene graphs must simultaneously capture spatial layout (ET s ) and functional relationships (ET f ) while ...
- **p. 19 / A.3 TRAINING CURVE - extractive body cue:** The overall reward converges to ∼0.93, while accuracy reward stabilizes at ∼0.9.
- **p. 19 / A.3 TRAINING CURVE - extractive body cue:** The format reward quickly reaches 1.0 within the first 25 steps, showing the model rapidly learns to produce valid JSON-structured outputs.
- **p. 6 / 4 METHOD - extractive body cue:** 4.3 STATE-AWARE DYNAMIC SCENE GRAPH UPDATE In realistic environments, multiple objects of the same category may coexist, and their task-related correspondences are often initially uncertain.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 5 (4 METHOD), p. 5 (4 METHOD), p. 6 (4 METHOD), p. 6 (4 METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | focus, agent, interaction, policy, instead, emphasis, lies, capture, incorporate, observed, state, changes, environment, scene | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | focus, agent, interaction, policy, instead, emphasis, lies, capture, incorporate, observed | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | summary, makes, following, contributions, MomaGraph, first, scene, graph, representation, jointly | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | objective, construct, instruction-conditioned, task-oriented, scene, graph, final, reward, function, integrates | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 4 METHOD - extractive body cue:** In this work, we do not focus on the agent's interaction policy; instead, our emphasis lies on how to capture and incorporate observed state changes ...
- **p. 5 / 4 METHOD - extractive body cue:** 4.1 MOMAGRAPH DEFINITION Given a single indoor room, the agent receives as input a set of multi-view images {Ii}n i=1 and a natural language instruction ...
- **p. 5 / 4 METHOD - extractive body cue:** 4.2 VLMS LEARN SCENE GRAPH REPRESENTATIONS WITH REINFORCEMENT LEARNING Existing open-source VLMs have demonstrated limited capability in generating accurate taskoriented scene graphs GT from multi-view ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** VLMs (OpenAI, 2023; Team et al., 2025; Ahn et al., 2022) have gained significant attention in robotic task planning (Niu et al., 2024; Yue et ...
- **p. 6 / 4 METHOD - extractive body cue:** After the agent executes an action at and observes the new environment state st+1, the scene graph is refined as: G(t+1) T = U  ...
- **p. 7 / 4 METHOD - extractive body cue:** This design encourages the model to learn how to ground natural instructions into the appropriate set of objects and relationships, rather than relying on object ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To support this representation, we build MomaGraph-Scenes, the first dataset that jointly models spatial and functional relationships with part-level annotations, encompassing multi-view observations, executed actions, ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Beyond these core capabilities, we further design tasks on Dynamic Verification and Long-horizon Task Decomposition to evaluate temporal reasoning and multi-steps planning. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Formally, at time step t, the task-oriented scene graph is represented as: G(t) T =  N (t) T , ET ,(t) s ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | Published as a conference paper at ICLR 2026 Table 4: DAPO Training Configuration Parameter Value Model Configuration Base Model Qwen2.5-VL-7B-Instruct Mixed Precision ... | hardware, batch and throughput |

## Training vs Inference

- **p. 21 / A.4.1 BENCHMARK DESIGN - extractive body cue:** Published as a conference paper at ICLR 2026 Table 4: DAPO Training Configuration Parameter Value Model Configuration Base Model Qwen2.5-VL-7B-Instruct Mixed Precision bfloat16 Training Setup ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** address, limitations, introduce, MomaGraph-Scenes, first, dataset, designed, provide, more, comprehensive, task-relevant, scene, representation, After, agent, executes, action, observes, environment, state.
- **Relevant PDF headings:** 4 METHOD (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | To rigorously evaluate spatial-functional reasoning and task planning capabilities, we design a comprehensive multi-choice VQA benchmark based on the scenes and tasks ... | p. 19 (A.4.1 BENCHMARK DESIGN), p. 17 (A.1.1 REAL-WORLD DATASET SOURCE AND COLLECTION) |
| Global / local decision | Across all models, the w/ Graph setting consistently outperforms the w/o Graph baseline, demonstrating that explicitly structuring task-oriented scene graphs provides a ... | p. 9 (6 EXPERIMENTS), p. 10 (6 EXPERIMENTS) |
| Motion execution / recovery | As shown in Figure 6, our system achieves an 80% success rate in graph generation, 87.5% success rate in planning (conditioned on ... | p. 11 (6 EXPERIMENTS), p. 22 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 9 / 6 EXPERIMENTS - extractive body cue:** We report accuracy (%) across four tiers (T1-T4) and the overall score, with and without graph-based reasoning.
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1: Comparison between MomaGraph-R1and LLaVA variants across task tiers. Models T1 T2 T3 T4 Overall Models
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 13: Training reward curves during MomaGraph-R1 training. correctness of the benchmark, all generated questions and answers undergo several rounds of manual verification, during which ...
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 14: Validation reward curves during MomaGraph-R1 training. B ADDITIONAL ABLATION STUDIES B.1 COMPARISON WITH SFT AND ICL BASELINES To validate our choice of RL-based ...
- **p. 22 / Figure/Table caption - extractive body cue:** Table 6: Sensitivity analysis of reward weights (wa, wf, wl) in our DAPO training. The model's performance remains stable across different weight configurations. As shown ...
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** Closed-source models still maintain the highest absolute performance, benefiting from larger-scale pretraining and proprietary data.
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 6: Quantitative real-robot evaluation. (a) Environment setup of the real-robot experiment. (b) Failure analysis illustrating success/failure rates across different reasoning stages. Task Setup. We ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 6 (4 METHOD), p. 6 (4 METHOD), p. 5 (4 METHOD), p. 5 (4 METHOD), p. 19 (A.3 TRAINING CURVE), p. 7 (4 METHOD), objective p. 5 (4 METHOD), p. 5 (4 METHOD), p. 6 (4 METHOD), p. 19 (A.3 TRAINING CURVE), p. 19 (A.3 TRAINING CURVE), p. 6 (4 METHOD), temporal p. 8 (4 METHOD), p. 6 (4 METHOD), p. 7 (4 METHOD), p. 11 (6 EXPERIMENTS), p. 8 (4 METHOD), p. 9 (6 EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
