# Method - VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2312.03275; PDF retrieval source: https://arxiv.org/pdf/2312.03275. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (III. PROBLEM FORMULATION)): The action space consists of the following: MOVE FORWARD (0.25m), TURN LEFT (30◦), TURN RIGHT (30◦), LOOK UP (30◦), LOOK DOWN (30◦), and STOP.

## Method Body Digest

- **p. 2 / III. PROBLEM FORMULATION - extractive body cue:** The action space consists of the following: MOVE FORWARD (0.25m), TURN LEFT (30◦), TURN RIGHT (30◦), LOOK UP (30◦), LOOK DOWN (30◦), and STOP.
- **p. 1 / I. INTRODUCTION - extractive body cue:** VLFM builds occupancy maps from depth observations to identify frontiers of the explored map region.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We demonstrate VLFM in photorealistic environments within the Habitat [5] simulator, where we achieve stateof-the-art results on the Object Goal Navigation (ObjectNav) task, even when ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose Vision-Language Frontier Maps (VLFM), a zero-shot approach for target-driven semantic navigation to an unseen object in a novel environment.

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose Vision-Language Frontier Maps (VLFM), a zero-shot approach for target-driven semantic navigation to an unseen object in a novel environment.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In contrast to prior language-based zero-shot semantic navigation methods [2]-[4], our method does not rely on object detectors and language models (e.g., ChatGPT, BERT) to ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We also demonstrate our approach in the real world on a Boston Dynamics Spot mobile manipulation platform by navigating efficiently to unseen semantic targets across ...

## Source Evidence Cues

- **p. 2 / III. PROBLEM FORMULATION - extractive body cue:** The action space consists of the following: MOVE FORWARD (0.25m), TURN LEFT (30◦), TURN RIGHT (30◦), LOOK UP (30◦), LOOK DOWN (30◦), and STOP.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | The action space consists of the following: MOVE FORWARD (0.25m), TURN LEFT (30◦), TURN RIGHT (30◦), LOOK UP (30◦), LOOK DOWN (30◦), ... | p. 2 (III. PROBLEM FORMULATION) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | The action space consists of the following: MOVE FORWARD (0.25m), TURN LEFT (30◦), TURN RIGHT (30◦), LOOK UP (30◦), LOOK DOWN (30◦), ... | p. 2 (III. PROBLEM FORMULATION) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | The action space consists of the following: MOVE FORWARD (0.25m), TURN LEFT (30◦), TURN RIGHT (30◦), LOOK UP (30◦), LOOK DOWN (30◦), ... | p. 2 (III. PROBLEM FORMULATION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | VLFM, builds, occupancy, maps, depth, observations, identify, frontiers, explored, region, action, space, consists, following | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | VLFM, builds, occupancy, maps, depth, observations, identify, frontiers, explored, region | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | Vision-Language, Frontier, Maps, VLFM, zero-shot, target-driven, semantic, navigation, unseen, object | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | not recovered | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / I. INTRODUCTION - extractive body cue:** VLFM builds occupancy maps from depth observations to identify frontiers of the explored map region.
- **p. 2 / III. PROBLEM FORMULATION - extractive body cue:** The action space consists of the following: MOVE FORWARD (0.25m), TURN LEFT (30◦), TURN RIGHT (30◦), LOOK UP (30◦), LOOK DOWN (30◦), and STOP.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We demonstrate VLFM in photorealistic environments within the Habitat [5] simulator, where we achieve stateof-the-art results on the Object Goal Navigation (ObjectNav) task, even when ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose Vision-Language Frontier Maps (VLFM), a zero-shot approach for target-driven semantic navigation to an unseen object in a novel environment.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | It does not affect a pixel's semantic value score if that pixel was not seen until the current time step. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | The confidence channel aims to determine how a pixel's value in the semantic value channel should be updated if it has a ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | HM3D's validation split contains 2000 episodes across 20 scenes and 6 object categories. | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** action, space, consists, following, MOVE, FORWARD, TURN, LEFT, RIGHT, LOOK, DOWN, STOP, VLFM, builds, occupancy, maps, depth, observations, identify, frontiers.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | We evaluate our approach using the Habitat [5] simulator on the validation splits of three different datasets of 3D scans of real-world ... | p. 5 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP) |
| Global / local decision | We evaluate VLFM by comparing it to several state-of-the-art (SOTA) techniques for zero-shot object navigation: CLIP on Wheels (CoW) [1], ESC [2], ... | p. 5 (V. EXPERIMENTAL SETUP), p. 1 (Figure/Table caption) |
| Motion execution / recovery | For all approaches, we report success rate (SR) and Success weighted by inverse Path Length (SPL) [31]. | p. 5 (V. EXPERIMENTAL SETUP), p. 1 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: VLFM achieves state-of-the-art semantic Object Goal Navigation performance in unfamiliar environments, without task-specific training, pre-built maps, or prior knowledge of the surroundings. It ...
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** Approach Semantic Nav Gibson HM3D MP3D Training SPL↑SR↑SPL↑SR↑SPL↑SR↑ PONI [19] ObjectNav 41.0 73.6 - - 12.1 31.8 PIRLNav [15] ObjectNav - - 27.1 64.1 - ...
- **p. 6 / VII. CONCLUSION - extractive body cue:** VLFM has a number of limitations that could be addressed by future work.
- **p. 6 / VII. CONCLUSION - extractive body cue:** So, we cannot leverage this map in sequentially executed semantic navigation tasks to different objects or in executing other navigation tasks requiring targets specified by ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (III. PROBLEM FORMULATION), objective 본문 anchor 없음, temporal p. 3 (IV. VISION-LANGUAGE FRONTIER MAPS), p. 3 (IV. VISION-LANGUAGE FRONTIER MAPS), p. 2 (III. PROBLEM FORMULATION), p. 5 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP), p. 4 (IV. VISION-LANGUAGE FRONTIER MAPS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
