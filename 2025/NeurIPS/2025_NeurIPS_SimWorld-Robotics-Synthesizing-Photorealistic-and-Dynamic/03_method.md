# Method - SimWorld-Robotics: Synthesizing Photorealistic and Dynamic Urban Environments for Multimodal Robot Navigation and Collaboration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (41 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=EyOtIOmMUh; PDF retrieval source: https://arxiv.org/pdf/2512.10046. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (1 Introduction), p. 1 (1 Introduction), p. 1 (Abstract), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction)): In sum, our key contributions include: (1) a new embodied AI simulator, SimWorld-Robotics (SWR), that supports the creation and simulation of photorealistic and dynamic urban environments with diverse embodied agents; ...

## Method Body Digest

- **p. 3 / 1 Introduction - extractive body cue:** In sum, our key contributions include: (1) a new embodied AI simulator, SimWorld-Robotics (SWR), that supports the creation and simulation of photorealistic and dynamic urban ...
- **p. 1 / 1 Introduction - extractive body cue:** Training these models requires a large amount of data, much of which can be generated in high-fidelity embodied simulators, such as Habitat 3 [40], RoboTHOR ...
- **p. 1 / Abstract - extractive body cue:** Our experimental results demonstrate that stateof-the-art models, including vision-language models (VLMs), struggle with our tasks, lacking robust perception, reasoning, and planning abilities necessary for urban ...
- **p. 3 / 1 Introduction - extractive body cue:** Our experimental results demonstrate that existing models, including state-of-the-art vision-language models (VLMs), fail to achieve meaningful success on our benchmarks.
- **p. 2 / 1 Introduction - extractive body cue:** There have been urban simulators developed in recent years.
- **p. 2 / 1 Introduction - extractive body cue:** Together, these features accelerate progress toward stronger embodied intelligence.
- **p. 1 / 1 Introduction - extractive body cue:** There has been tremendous progress in engineering general-purpose robotics that can follow human instructions and perform open-ended tasks [2, 28, 15, 27, 46], thanks to ...
- **p. 2 / 1 Introduction - extractive body cue:** As shown in 4, the first is a multimodal instruction following benchmark, SIMWORLDMMNAV, for robot navigation, in which a robot must follow vision and language ...

## Design Rationale

- **p. 3 / 1 Introduction - extractive body cue:** In sum, our key contributions include: (1) a new embodied AI simulator, SimWorld-Robotics (SWR), that supports the creation and simulation of photorealistic and dynamic urban ...
- **p. 3 / 1 Introduction - extractive body cue:** To address this gap, we introduce SimWorld-20K, a large-scale dataset for benchmarking multimodal robot navigation in photo-realistic urban environments.
- **p. 2 / 1 Introduction - extractive body cue:** It offers diverse high-fidelity building and object assets, supports embodied agents with rich action spaces, includes a background traffic system powered by city-scale waypoint generation, ...

## Source Evidence Cues

- **p. 3 / 1 Introduction - extractive body cue:** In sum, our key contributions include: (1) a new embodied AI simulator, SimWorld-Robotics (SWR), that supports the creation and simulation of photorealistic and dynamic urban ...
- **p. 1 / 1 Introduction - extractive body cue:** Training these models requires a large amount of data, much of which can be generated in high-fidelity embodied simulators, such as Habitat 3 [40], RoboTHOR ...
- **p. 1 / Abstract - extractive body cue:** Our experimental results demonstrate that stateof-the-art models, including vision-language models (VLMs), struggle with our tasks, lacking robust perception, reasoning, and planning abilities necessary for urban ...
- **p. 3 / 1 Introduction - extractive body cue:** Our experimental results demonstrate that existing models, including state-of-the-art vision-language models (VLMs), fail to achieve meaningful success on our benchmarks.
- **p. 2 / 1 Introduction - extractive body cue:** There have been urban simulators developed in recent years.
- **p. 2 / 1 Introduction - extractive body cue:** Together, these features accelerate progress toward stronger embodied intelligence.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | In sum, our key contributions include: (1) a new embodied AI simulator, SimWorld-Robotics (SWR), that supports the creation and simulation of photorealistic ... | p. 3 (1 Introduction), p. 1 (1 Introduction) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Training these models requires a large amount of data, much of which can be generated in high-fidelity embodied simulators, such as Habitat ... | p. 1 (1 Introduction), p. 1 (Abstract) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | Our experimental results demonstrate that stateof-the-art models, including vision-language models (VLMs), struggle with our tasks, lacking robust perception, reasoning, and planning abilities ... | p. 1 (Abstract), p. 3 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / 1 Introduction - extractive body cue:** There has been tremendous progress in engineering general-purpose robotics that can follow human instructions and perform open-ended tasks [2, 28, 15, 27, 46], thanks to ...
- **p. 2 / 1 Introduction - extractive body cue:** Together, these features accelerate progress toward stronger embodied intelligence.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | There, been, tremendous, progress, engineering, general-purpose, robotics, follow, human, instructions, perform, open-ended, tasks, thanks | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | There, been, tremendous, progress, engineering, general-purpose, robotics, follow, human, instructions | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | contributions, include, embodied, simulator, SimWorld-Robotics, SWR, supports, creation, simulation, photorealistic | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | There, been, tremendous, progress, engineering, general-purpose, robotics, follow, human, instructions | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1 Introduction - extractive body cue:** There has been tremendous progress in engineering general-purpose robotics that can follow human instructions and perform open-ended tasks [2, 28, 15, 27, 46], thanks to ...
- **p. 1 / Abstract - extractive body cue:** Our experimental results demonstrate that stateof-the-art models, including vision-language models (VLMs), struggle with our tasks, lacking robust perception, reasoning, and planning abilities necessary for urban ...
- **p. 2 / 1 Introduction - extractive body cue:** As shown in 4, the first is a multimodal instruction following benchmark, SIMWORLDMMNAV, for robot navigation, in which a robot must follow vision and language ...
- **p. 3 / 1 Introduction - extractive body cue:** Our experimental results demonstrate that existing models, including state-of-the-art vision-language models (VLMs), fail to achieve meaningful success on our benchmarks.
- **p. 2 / 1 Introduction - extractive body cue:** It offers diverse high-fidelity building and object assets, supports embodied agents with rich action spaces, includes a background traffic system powered by city-scale waypoint generation, ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | The dataset contains 20K training steps sampled from 200 episodes, each averaging 500 m in length, across 100 procedurally generated city environments ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Compared to indoor scenarios, robotics in outdoor environments, in particular, large urban environments, introduces additional challenges, such as (1) 3D perception, spatial ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | Compared to indoor scenarios, robotics in outdoor environments, in particular, large urban environments, introduces additional challenges, such as (1) 3D perception, spatial ... | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | The dataset contains 20K training steps sampled from 200 episodes, each averaging 500 m in length, across 100 procedurally generated city environments ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 1 Introduction - extractive body cue:** In sum, our key contributions include: (1) a new embodied AI simulator, SimWorld-Robotics (SWR), that supports the creation and simulation of photorealistic and dynamic urban ...
- **p. 1 / 1 Introduction - extractive body cue:** Training these models requires a large amount of data, much of which can be generated in high-fidelity embodied simulators, such as Habitat 3 [40], RoboTHOR ...
- **p. 3 / 1 Introduction - extractive body cue:** The dataset contains 20K training steps sampled from 200 episodes, each averaging 500 m in length, across 100 procedurally generated city environments with an average ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** contributions, include, embodied, simulator, SimWorld-Robotics, SWR, supports, creation, simulation, photorealistic, dynamic, urban, environments, diverse, agents, novel, benchmarks, single, robot, navigation.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | In sum, our key contributions include: (1) a new embodied AI simulator, SimWorld-Robotics (SWR), that supports the creation and simulation of photorealistic ... | p. 3 (1 Introduction), p. 2 (1 Introduction) |
| Global / local decision | Figure 11: Example communication for ROCO baseline Baseline 2 - ROCO The ROCO-based [33] setting extends the oracle setup by introducing collaborative ... | p. 30 (Figure/Table caption), p. 3 (1 Introduction) |
| Motion execution / recovery | After fine-tuning on SimWorld-20K, QwenVL2.5-7B achieves a non-zero success rate on the test set and outperforms SOTA proprietary models across several key ... | p. 3 (1 Introduction), p. 3 (1 Introduction) |

## Failure and Ablation Link

- **p. 27 / Figure/Table caption - extractive body cue:** Table 11: Ablation study with key components. Configuration Explicit Reason Separate Perceive/Act Depth Segment
- **p. 3 / 1 Introduction - extractive body cue:** After fine-tuning on SimWorld-20K, QwenVL2.5-7B achieves a non-zero success rate on the test set and outperforms SOTA proprietary models across several key metrics.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Illustration of a multi-robot search task. Hard Setting. We further evaluated realistic obstacle avoidance and traffic rule obedience on models that performed relatively ...
- **p. 32 / Figure/Table caption - extractive body cue:** Figure 13: Qualitative result - lack of distance grounding Spatial Reasoning The VLM exhibits limitations in reasoning about spatial relationships, particularly in estimating distance, maintaining ...
- **p. 33 / Figure/Table caption - extractive body cue:** Figure 15: Qualitative result - lack of perspective-adaptive matching These limitations also manifest when matching buildings from different perspectives. The target building is provided as ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: Most common failure modes in SIMWORLD-MMNAV. Subtask Failure Mode Frequency (%) Moving to Intersection Misestimate the distance to the intersection 53.33 Fail to ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Illustration of a multi-robot search task. Hard Setting. We further evaluated realistic obstacle avoidance and traffic rule obedience on models that performed relatively ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (1 Introduction), p. 1 (1 Introduction), p. 1 (Abstract), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), objective p. 1 (1 Introduction), p. 2 (1 Introduction), temporal p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (2 Related Work), p. 4 (2 Related Work), p. 5 (2 Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
