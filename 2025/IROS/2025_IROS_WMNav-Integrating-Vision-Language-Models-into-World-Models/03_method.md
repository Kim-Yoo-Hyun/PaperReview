# Method - WMNav: Integrating Vision-Language Models into World Models for Object Goal Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2503.02247; PDF retrieval source: https://arxiv.org/pdf/2503.02247. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (III. WMNAV APPROACH), p. 4 (III. WMNAV APPROACH), p. 5 (III. WMNAV APPROACH), p. 3 (III. WMNAV APPROACH), p. 4 (III. WMNAV APPROACH), p. 5 (III. WMNAV APPROACH)): Then, the direction in the panoramic image with the highest score is selected and sent to the navigation policy module.

## Method Body Digest

- **p. 3 / III. WMNAV APPROACH - extractive body cue:** Then, the direction in the panoramic image with the highest score is selected and sent to the navigation policy module.
- **p. 4 / III. WMNAV APPROACH - extractive body cue:** Then M cv t (st in Figure 2) is updated by combining M nav t with the curiosity value map in the previous step M ...
- **p. 5 / III. WMNAV APPROACH - extractive body cue:** Then, actions falling within explored regions are filtered out based on the exploration state map, and the action sequence is further refined by limiting the ...
- **p. 3 / III. WMNAV APPROACH - extractive body cue:** In our framework, the world model consists of PredictVLM and the memory constructed by curiosity value map and cost.
- **p. 4 / III. WMNAV APPROACH - extractive body cue:** The cost is fed into PlanVLM and ReasonVLM as part of their prompts to implicitly optimize the outputs in the navigation policy.
- **p. 5 / III. WMNAV APPROACH - extractive body cue:** The candidate action sequence Acand t = {(rt,j, θt,j)}K′ j=1 in the agent's coordinate system is then mapped back to the image and annotated to ...
- **p. 6 / III. WMNAV APPROACH - extractive body cue:** TF refers to trainingfree, and ZS refers to zero-shot.
- **p. 3 / III. WMNAV APPROACH - extractive body cue:** For PlanVLM and ReasonVLM in the policy module, the cost (the previous step's subtask and the goal flag) is used to configure their prompts, thus ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our contributions can be summarized as follows: • We introduce a new direction for object goal navigation in a complex, unknown environment using a world ...
- **p. 3 / III. WMNAV APPROACH - extractive body cue:** In our framework, the world model consists of PredictVLM and the memory constructed by curiosity value map and cost.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Building on the key insight that VLMs inherently encode comprehensive knowledge about indoor layout and spatial relationships of objects, we propose WMNav as shown in ...

## Source Evidence Cues

- **p. 3 / III. WMNAV APPROACH - extractive body cue:** Then, the direction in the panoramic image with the highest score is selected and sent to the navigation policy module.
- **p. 4 / III. WMNAV APPROACH - extractive body cue:** Then M cv t (st in Figure 2) is updated by combining M nav t with the curiosity value map in the previous step M ...
- **p. 5 / III. WMNAV APPROACH - extractive body cue:** Then, actions falling within explored regions are filtered out based on the exploration state map, and the action sequence is further refined by limiting the ...
- **p. 3 / III. WMNAV APPROACH - extractive body cue:** In our framework, the world model consists of PredictVLM and the memory constructed by curiosity value map and cost.
- **p. 4 / III. WMNAV APPROACH - extractive body cue:** The cost is fed into PlanVLM and ReasonVLM as part of their prompts to implicitly optimize the outputs in the navigation policy.
- **p. 5 / III. WMNAV APPROACH - extractive body cue:** The candidate action sequence Acand t = {(rt,j, θt,j)}K′ j=1 in the agent's coordinate system is then mapped back to the image and annotated to ...
- **p. 6 / III. WMNAV APPROACH - extractive body cue:** TF refers to trainingfree, and ZS refers to zero-shot.
- **Detected method headings:** III. WMNAV APPROACH (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | Then, the direction in the panoramic image with the highest score is selected and sent to the navigation policy module. | p. 3 (III. WMNAV APPROACH), p. 4 (III. WMNAV APPROACH) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Then M cv t (st in Figure 2) is updated by combining M nav t with the curiosity value map in the ... | p. 4 (III. WMNAV APPROACH), p. 5 (III. WMNAV APPROACH) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | Then, actions falling within explored regions are filtered out based on the exploration state map, and the action sequence is further refined ... | p. 5 (III. WMNAV APPROACH), p. 3 (III. WMNAV APPROACH) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / III. WMNAV APPROACH - extractive body cue:** Then M cv t (st in Figure 2) is updated by combining M nav t with the curiosity value map in the previous step M ...
- **p. 3 / III. WMNAV APPROACH - extractive body cue:** For PlanVLM and ReasonVLM in the policy module, the cost (the previous step's subtask and the goal flag) is used to configure their prompts, thus ...
- **p. 4 / III. WMNAV APPROACH - extractive body cue:** The cost is fed into PlanVLM and ReasonVLM as part of their prompts to implicitly optimize the outputs in the navigation policy.
- **p. 3 / III. WMNAV APPROACH - extractive body cue:** The navigation policy module has access to the reward information from the environment.
- **p. 5 / III. WMNAV APPROACH - extractive body cue:** The length constraint on the polar coordinate vectors is removed, and sampling in the navigable regions is made denser to ensure the presence of vectors ...
- **p. 5 / III. WMNAV APPROACH - extractive body cue:** If there is no sofa, then return failure message.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 5 (III. WMNAV APPROACH), p. 4 (III. WMNAV APPROACH), p. 4 (III. WMNAV APPROACH), p. 5 (III. WMNAV APPROACH).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | contributions, summarized, follows, introduce, direction, object, goal, navigation, complex, unknown, environment, world, model, consisting | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | contributions, summarized, follows, introduce, direction, object, goal, navigation, complex, unknown | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | contributions, summarized, follows, introduce, direction, object, goal, navigation, complex, unknown | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Then, Figure, updated, combining, curiosity, value, previous, step, st-1, Cost | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our contributions can be summarized as follows: • We introduce a new direction for object goal navigation in a complex, unknown environment using a world ...
- **p. 5 / III. WMNAV APPROACH - extractive body cue:** Choose your action from the image prompt.' Image Prompt Exploration Stage Action VLM Update Navigable Area Candidate Actions Initial Actions Exploration State Map Filter 2 ...
- **p. 3 / III. WMNAV APPROACH - extractive body cue:** For PlanVLM and ReasonVLM in the policy module, the cost (the previous step's subtask and the goal flag) is used to configure their prompts, thus ...
- **p. 4 / III. WMNAV APPROACH - extractive body cue:** At each time step t, the panoramic image Ipan t is input to PredictVLM, which outputs scores Scoret for each direction in the current panoramic ...
- **p. 5 / III. WMNAV APPROACH - extractive body cue:** Instead, we employ a strategy similar to the action proposer to determine the precise location of the goal when the goal appears in the current ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Panoramic Image Input Getting Observation Fig.
- **p. 4 / III. WMNAV APPROACH - extractive body cue:** The cost is fed into PlanVLM and ReasonVLM as part of their prompts to implicitly optimize the outputs in the navigation policy.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | At each time step t, the agent takes an RGB-D observation Ot of the surroundings and its real-time pose Pt. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | At each time step t, the panoramic image Ipan t is input to PredictVLM, which outputs scores Scoret for each direction in ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | To retain the predicted state of the environment, WMNav proposes the online maintained Curiosity Value Map as part of the world model ... | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / III. WMNAV APPROACH - extractive body cue:** TF refers to trainingfree, and ZS refers to zero-shot.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Similar to the frontier map, our simple and online maintained Curiosity Value Map, without prior information from other detectors, makes full use of the scene ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Then, direction, panoramic, image, highest, score, selected, sent, navigation, policy, module, Figure, updated, combining, curiosity, value, previous, step, st-1, Cost.
- **Relevant PDF headings:** III. WMNAV APPROACH (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Datasets and Evaluation Metrics Datasets The HM3D v0.1 [38] is used in the Habitat 2022 ObjectNav challenge, providing 2000 validation episodes on ... | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Global / local decision | Memory SD TAP SR(%)↑SPL(%)↑ a No ✗ ✗ 65.8 25.8 b No ✓ ✗ 67.4 33.1 c Text-Image ✓ ✗ 62.0 29.6 ... | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Motion execution / recovery | Metrics We adopt Success Rate (SR) and Success Rate Weighted by Inverse Path Length (SPL) as the evaluation metrics. | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** As shown in TABLE II: Ablation study of different modules and memory strategies on HM3D v0.2 [38].
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** So, the agent only needs a VLM base to complete all the processes without any policy modules to train.
- **p. 5 / III. WMNAV APPROACH - extractive body cue:** If there is no sofa, then return failure message.
- **p. 5 / III. WMNAV APPROACH - extractive body cue:** 2) Goal-approaching Stage: Due to the limitations of the existing VLMs' capability, we do not rely on the VLM to estimate the stopping condition directly ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** But textual information cannot accurately describe the spatial relationships in the scene, and it is difficult for LLM to make good spatial decisions.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** However, since VLM is trained on egocentric image data, it does not take advantage of VLM's powerful egocentric reasoning ability.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (III. WMNAV APPROACH), p. 4 (III. WMNAV APPROACH), p. 5 (III. WMNAV APPROACH), p. 3 (III. WMNAV APPROACH), p. 4 (III. WMNAV APPROACH), p. 5 (III. WMNAV APPROACH), objective p. 4 (III. WMNAV APPROACH), p. 3 (III. WMNAV APPROACH), p. 4 (III. WMNAV APPROACH), p. 3 (III. WMNAV APPROACH), p. 5 (III. WMNAV APPROACH), p. 5 (III. WMNAV APPROACH), temporal p. 3 (III. WMNAV APPROACH), p. 4 (III. WMNAV APPROACH), p. 1 (Abstract), p. 2 (I. INTRODUCTION), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
