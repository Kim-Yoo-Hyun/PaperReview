# Method - OpenObject-NAV: Open-Vocabulary Object-Oriented Navigation Based on Dynamic Carrier-Relationship Scene Graph

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2409.18743; PDF retrieval source: https://arxiv.org/pdf/2409.18743. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 2 (III. METHOD), p. 4 (III. METHOD), p. 2 (III. METHOD)): The robot selects the next action at ∈A based on the current state St according to a specific policy π(·) in (8). at = π(St) (8) policy π(·): Given current ...

## Method Body Digest

- **p. 3 / III. METHOD - extractive PDF cue:** The robot selects the next action at ∈A based on the current state St according to a specific policy π(·) in (8). at = π(St) ...
- **p. 4 / III. METHOD - extractive PDF cue:** Leveraging the LLM's commonsense understanding of object-carrier relationships (e.g., "a cup is unlikely to be placed on a toilet"), the LLM identifies the carrier object ...
- **p. 3 / III. METHOD - extractive PDF cue:** The OpenObject-NAV system framework consists of two main modules.
- **p. 2 / III. METHOD - extractive PDF cue:** Unlike ConceptGraph [19], each instance object Oi ∈O (O is the set of all objects) not only contains a CLIP feature V Fi but also ...
- **p. 4 / III. METHOD - extractive PDF cue:** The RGB images are processed through CropFormer [38], Tokenize Anything model [35], CLIP [22] and SBERT [36] to obtain instance masks, captions, encoded CLIP features ...
- **p. 2 / III. METHOD - extractive PDF cue:** If the target is a daily item (e.g., a cup) that is being carried, the robot evaluates whether the item remains in its original location ...
- **p. 2 / III. METHOD - extractive PDF cue:** The cost function is defined as follows: P L = T X t=1 Length(Lt, Lt+1) (1) Let Lt represent the position of the exploration target ...
- **p. 4 / III. METHOD - extractive PDF cue:** Since some candidates in CTt may be carried by objects in CRobserved, CTt is updated to CTt ∗after these candidates are removed.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** In summary, our contributions are as follows: • We present an adaptable carrier relationship scene graph (CRSG) that primarily describes the dynamic carrier and carried ...
- **p. 3 / III. METHOD - extractive PDF cue:** The OpenObject-NAV system framework consists of two main modules.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** 2Zibo Zheng are with School of Mechanical Engineering, University of Nottingham Ningbo China, Ningbo, 315100, China. †: Equal contribution.

## Source Evidence Cues

- **p. 3 / III. METHOD - extractive PDF cue:** The robot selects the next action at ∈A based on the current state St according to a specific policy π(·) in (8). at = π(St) ...
- **p. 4 / III. METHOD - extractive PDF cue:** Leveraging the LLM's commonsense understanding of object-carrier relationships (e.g., "a cup is unlikely to be placed on a toilet"), the LLM identifies the carrier object ...
- **p. 3 / III. METHOD - extractive PDF cue:** The OpenObject-NAV system framework consists of two main modules.
- **p. 2 / III. METHOD - extractive PDF cue:** Unlike ConceptGraph [19], each instance object Oi ∈O (O is the set of all objects) not only contains a CLIP feature V Fi but also ...
- **p. 4 / III. METHOD - extractive PDF cue:** The RGB images are processed through CropFormer [38], Tokenize Anything model [35], CLIP [22] and SBERT [36] to obtain instance masks, captions, encoded CLIP features ...
- **p. 2 / III. METHOD - extractive PDF cue:** If the target is a daily item (e.g., a cup) that is being carried, the robot evaluates whether the item remains in its original location ...
- **Detected method headings:** III. METHOD (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | The robot selects the next action at ∈A based on the current state St according to a specific policy π(·) in (8). ... | p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Leveraging the LLM's commonsense understanding of object-carrier relationships (e.g., "a cup is unlikely to be placed on a toilet"), the LLM identifies ... | p. 4 (III. METHOD), p. 3 (III. METHOD) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | The OpenObject-NAV system framework consists of two main modules. | p. 3 (III. METHOD), p. 2 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / III. METHOD - extractive PDF cue:** The cost function is defined as follows: P L = T X t=1 Length(Lt, Lt+1) (1) Let Lt represent the position of the exploration target ...
- **p. 4 / III. METHOD - extractive PDF cue:** Since some candidates in CTt may be carried by objects in CRobserved, CTt is updated to CTt ∗after these candidates are removed.
- **p. 4 / III. METHOD - extractive PDF cue:** After the comparison, the carried objects on Ocr match are updated accordingly: they are either added, removed, or left unchanged.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 4 (III. METHOD), p. 4 (III. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | robot, selects, next, action, current, state, according, specific, policy, Given, CRt, CTt, then, Stop | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | robot, selects, next, action, current, state, according, specific, policy, Given | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | summary, contributions, follows, present, adaptable, carrier, relationship, scene, graph, CRSG | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | cost, function, defined, follows, Length, Let, represent, position, exploration, target | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. METHOD - extractive PDF cue:** The robot selects the next action at ∈A based on the current state St according to a specific policy π(·) in (8). at = π(St) ...
- **p. 3 / III. METHOD - extractive PDF cue:** We model the exploration of a displaced object as a fixedpolicy Markov decision process (MDP) below. state space S: In the current step t, we ...
- **p. 4 / III. METHOD - extractive PDF cue:** Leveraging the LLM's commonsense understanding of object-carrier relationships (e.g., "a cup is unlikely to be placed on a toilet"), the LLM identifies the carrier object ...
- **p. 4 / III. METHOD - extractive PDF cue:** If the input command is an image, an LLM-based image comparison is also performed.
- **p. 2 / III. METHOD - extractive PDF cue:** If the target is a daily item (e.g., a cup) that is being carried, the robot evaluates whether the item remains in its original location ...
- **p. 2 / III. METHOD - extractive PDF cue:** We select specific point clouds from M and project them onto the x -y plane: wall point clouds within a certain height range from the ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** In the process of robot navigation, new observations are matched with carrier objects in the carrier layer.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | An overview of the system framework is provided in Fig. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | The cost function is defined as follows: P L = T X t=1 Length(Lt, Lt+1) (1) Let Lt represent the position of ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** robot, selects, next, action, current, state, according, specific, policy, Given, CRt, CTt, then, Stop, Leveraging, LLM, commonsense, understanding, object-carrier, relationships.
- **Relevant PDF headings:** III. METHOD (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Real-World Validation We validated our algorithm using an Autolabor robot in a real scene, equipped with an industrial computer featuring an NVIDIA ... | p. 6 (1. Does the carrier-relationship scene graph (CRSG) im), p. 3 (III. METHOD) |
| Global / local decision | The resulting feature is then compared with the SBERT or CLIP features of each object in the CRSG S G using cosine ... | p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Motion execution / recovery | 4 illustrates an example of long-sequence navigation, where the efficiency of navigating to the target significantly improves as the number of navigated ... | p. 5 (1. Does the carrier-relationship scene graph (CRSG) im), p. 4 (1. Does the carrier-relationship scene graph (CRSG) im) |

## Failure and Ablation Link

- **p. 6 / 1. Does the carrier-relationship scene graph (CRSG) im - extractive PDF cue:** IV-B, while the second and third figures show the results of the ablation experiments with and without CRSG updates in Sec.
- **p. 6 / 1. Does the carrier-relationship scene graph (CRSG) im - extractive PDF cue:** Ablation Study To further investigate the role of CRSG updates in efficient navigation to everyday objects, we conducted ablation experiments on one long-sequence navigation tasks ...
- **p. 4 / III. METHOD - extractive PDF cue:** Since some candidates in CTt may be carried by objects in CRobserved, CTt is updated to CTt ∗after these candidates are removed.
- **p. 4 / III. METHOD - extractive PDF cue:** After the comparison, the carried objects on Ocr match are updated accordingly: they are either added, removed, or left unchanged.
- **p. 4 / 1. Does the carrier-relationship scene graph (CRSG) im - extractive PDF cue:** If the robot fails to reach the target, the SPL score is zero.
- **p. 5 / 1. Does the carrier-relationship scene graph (CRSG) im - extractive PDF cue:** VLMap Ours ConceptGraph Result: Success Result: Success Result: Failed ---Find a chair Result: Failed ---Find yellow bottle Result: Failed ---Find chairs Task 1: black bottle ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 2 (III. METHOD), p. 4 (III. METHOD), p. 2 (III. METHOD), objective p. 2 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), temporal p. 2 (III. METHOD), p. 2 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 1 (Abstract), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
