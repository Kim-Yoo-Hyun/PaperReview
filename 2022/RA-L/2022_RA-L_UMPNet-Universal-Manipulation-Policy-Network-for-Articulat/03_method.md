# Method - UMPNet: Universal Manipulation Policy Network for Articulated Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2109.05668; PDF retrieval source: https://arxiv.org/pdf/2109.05668. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (III. APPROACH), p. 3 (III. APPROACH), p. 4 (III. APPROACH), p. 4 (III. APPROACH), p. 2 (III. APPROACH), p. 2 (III. APPROACH)): We use a U-Net architecture for this task, the network is supervised by the outcome of the executed action (one out of W ×H pixels).

## Method Body Digest

- **p. 3 / III. APPROACH - extractive body cue:** We use a U-Net architecture for this task, the network is supervised by the outcome of the executed action (one out of W ×H pixels).
- **p. 3 / III. APPROACH - extractive body cue:** DistDecoder is a fully-connected neural network trained using MSE loss Ldist for the executed action at.
- **p. 4 / III. APPROACH - extractive body cue:** In the first half of each sequence, we select action with positive AoT prediction for execution to move the object away from its initial state.
- **p. 4 / III. APPROACH - extractive body cue:** Then by executing the actions with a reversed Arrow-of-Time (i.e., negative AoT), the policy tries to move object back to the "past", which will effectively ...
- **p. 2 / III. APPROACH - extractive body cue:** The goal of the manipulation policy π is to generate a sequence of actions to interact with a random articulated object which would result in ...
- **p. 2 / III. APPROACH - extractive body cue:** These three requirements directly correspond to the three key components of our algorithm, which are action position selection (a), action distance (b) and Arrow-of-Time inference ...
- **p. 3 / III. APPROACH - extractive body cue:** The network is trained with Binary Cross-Entropy loss.
- **p. 4 / III. APPROACH - extractive body cue:** The model is trained as a three-way classification with Cross-Entropy loss LAoT.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, we present a unified framework that discovers possible manipulation policies for an articulated object from visual observations.
- **p. 3 / III. APPROACH - extractive body cue:** To address this issue, we proposes an "Arrow-of-Time" (AoT) action attribute that indicates
- **p. 2 / I. INTRODUCTION - extractive body cue:** We validate our approach on two manipulation tasks (1) open-ended state exploration and (2) goal-conditioned manipulation.

## Source Evidence Cues

- **p. 3 / III. APPROACH - extractive body cue:** We use a U-Net architecture for this task, the network is supervised by the outcome of the executed action (one out of W ×H pixels).
- **p. 3 / III. APPROACH - extractive body cue:** DistDecoder is a fully-connected neural network trained using MSE loss Ldist for the executed action at.
- **p. 4 / III. APPROACH - extractive body cue:** In the first half of each sequence, we select action with positive AoT prediction for execution to move the object away from its initial state.
- **p. 4 / III. APPROACH - extractive body cue:** Then by executing the actions with a reversed Arrow-of-Time (i.e., negative AoT), the policy tries to move object back to the "past", which will effectively ...
- **p. 2 / III. APPROACH - extractive body cue:** The goal of the manipulation policy π is to generate a sequence of actions to interact with a random articulated object which would result in ...
- **p. 2 / III. APPROACH - extractive body cue:** These three requirements directly correspond to the three key components of our algorithm, which are action position selection (a), action distance (b) and Arrow-of-Time inference ...
- **Detected method headings:** III. APPROACH (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | We use a U-Net architecture for this task, the network is supervised by the outcome of the executed action (one out of ... | p. 3 (III. APPROACH), p. 3 (III. APPROACH) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | DistDecoder is a fully-connected neural network trained using MSE loss Ldist for the executed action at. | p. 3 (III. APPROACH), p. 4 (III. APPROACH) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | In the first half of each sequence, we select action with positive AoT prediction for execution to move the object away from ... | p. 4 (III. APPROACH), p. 4 (III. APPROACH) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. APPROACH - extractive body cue:** The network is trained with Binary Cross-Entropy loss.
- **p. 4 / III. APPROACH - extractive body cue:** The model is trained as a three-way classification with Cross-Entropy loss LAoT.
- **p. 3 / III. APPROACH - extractive body cue:** DistDecoder is a fully-connected neural network trained using MSE loss Ldist for the executed action at.
- **p. 4 / III. APPROACH - extractive body cue:** The final loss for direction inference is: L = λLdist +LAoT, where λ = 100 in our experiments.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (III. APPROACH), p. 3 (III. APPROACH), p. 4 (III. APPROACH), p. 4 (III. APPROACH).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Problem, formulation, task, defined, follows, given, visual, observation, articulated, object, form, RGB-D, image, initial | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Problem, formulation, task, defined, follows, given, visual, observation, articulated, object | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, present, unified, framework, discovers, possible, manipulation, policies, articulated, object | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | network, trained, Binary, Cross-Entropy, loss, model, three-way, classification, LAoT, DistDecoder | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. APPROACH - extractive body cue:** Problem formulation The task is defined as follows: given a visual observation of an articulated object in the form of an RGB-D image at the ...
- **p. 4 / III. APPROACH - extractive body cue:** The key idea for performing the goal-conditioned task is to swap out the initial observation with the goal state observation as the input to the ...
- **p. 2 / III. APPROACH - extractive body cue:** The goal of the manipulation policy π is to generate a sequence of actions to interact with a random articulated object which would result in ...
- **p. 4 / III. APPROACH - extractive body cue:** Goal conditioned manipulation with reversed AoT While open-ended interaction is useful for exploring and collecting information about the environment, most manipulation tasks are goal conditioned ...
- **p. 3 / III. APPROACH - extractive body cue:** 2d) takes both embedding vector ψ(ot) and action a as input, and outputs a scalar as the distance prediction ˜rdist(adir t ).
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, to avoid the back-and-forth actions, the network takes the history state as input and infers an additional "Arrow-of-Time (AoT)" attribute for each action.
- **p. 1 / I. INTRODUCTION - extractive body cue:** The action trajectories inferred by the policy network (shown in Fig.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | To achieve this goal, we formulate an action trajectory by its initial 3D position and a sequence of action directions, which allows ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Both [ Where2Act ] and [ SingleStep ] only take the current observation as input and infer actions for one step; hence, ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | Both [ Where2Act ] and [ SingleStep ] only take the current observation as input and infer actions for one step; hence, ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | The initial state may be moved to ensure the task can be accomplished in 15 steps. | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / III. APPROACH - extractive body cue:** DistDecoder is a fully-connected neural network trained using MSE loss Ldist for the executed action at.
- **p. 2 / III. APPROACH - extractive body cue:** These three requirements directly correspond to the three key components of our algorithm, which are action position selection (a), action distance (b) and Arrow-of-Time inference ...
- **p. 3 / III. APPROACH - extractive body cue:** DistDecoder is a fully-connected neural network trained using MSE loss Ldist for the executed action at.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** U-Net, architecture, task, network, supervised, outcome, executed, action, pixels, DistDecoder, fully-connected, neural, trained, MSE, loss, Ldist, first, half, sequence, select.
- **Relevant PDF headings:** III. APPROACH (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Being able to effectively explore the possible states of an object without a specific goal is a critical first step for many ... | p. 5 (IV. EVALUATION), p. 7 (IV. EVALUATION) |
| Semantic / temporal fusion | Compared to [ AoTOnly ], we can observe that by explicitly predicting the distance value for each action candidate, [ UMPNet ] ... | p. 5 (IV. EVALUATION), p. 6 (IV. EVALUATION) |
| Robot query / planning handoff | When combined with heuristic filter, the performance improves slightly. | p. 5 (IV. EVALUATION), p. 5 (IV. EVALUATION) |

## Failure and Ablation Link

- **p. 5 / IV. EVALUATION - extractive body cue:** Being able to effectively explore the possible states of an object without a specific goal is a critical first step for many robot learning algorithms ...
- **p. 6 / IV. EVALUATION - extractive body cue:** Effect of decomposing AoT and distance prediction.
- **p. 5 / IV. EVALUATION - extractive body cue:** This heuristic helps to avoid back-and-forth actions, however cannot be applied for goal-conditioned manipulation. • SingleStep: Single-step version of our method that only takes the ...
- **p. 7 / IV. EVALUATION - extractive body cue:** Limitations and failure cases Assumptions: To allow goal-conditioned manipulation with reversed AoT actions, we assume the action trajectories are bi-directional in time (i.e., they are ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Typical failure cases. UR5 robot, and a suction gripper. Fig. 8 (a) shows the real- world setup. In this experiment, we directly tested ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: Open-ended state exploration. Arrow length indicates the inferred distance value, color indicates the inferred AoT label. We visualized the uniform samples to better ...
- **p. 5 / IV. EVALUATION - extractive body cue:** I we can see that [ Where2Act ] is able to achieve similar performance in "single action effects", however, both [ Where2Act ] and [ ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (III. APPROACH), p. 3 (III. APPROACH), p. 4 (III. APPROACH), p. 4 (III. APPROACH), p. 2 (III. APPROACH), p. 2 (III. APPROACH), objective p. 3 (III. APPROACH), p. 4 (III. APPROACH), p. 3 (III. APPROACH), p. 4 (III. APPROACH), temporal p. 1 (I. INTRODUCTION), p. 5 (IV. EVALUATION), p. 1 (I. INTRODUCTION), p. 2 (II. RELATED WORK), p. 5 (IV. EVALUATION), p. 6 (IV. EVALUATION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** 2d) takes both embedding vector ψ(ot) and action a as input, and outputs a scalar as the distance prediction ˜rdist(adir t ). (p. 3, III. APPROACH).
- **Objective/update evidence:** The network is trained with Binary Cross-Entropy loss. (p. 3, III. APPROACH).
- **Temporal/runtime evidence:** Both [ Where2Act ] and [ SingleStep ] only take the current observation as input and infer actions for one step; hence, they do not need to understand the interaction ... (p. 5, IV. EVALUATION).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
