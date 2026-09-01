# Method - Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p045.html; PDF retrieval source: https://arxiv.org/pdf/2402.10329. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (III. METHOD), p. 3 (III. METHOD)): The following sections describe how we enable the above goals through our hardware and policy interface design.

## Method Body Digest

- **p. 3 / III. METHOD - extractive body cue:** The following sections describe how we enable the above goals through our hardware and policy interface design.
- **p. 3 / III. METHOD - extractive body cue:** Universal Manipulation Interface (UMI) is hand-held data collection and policy learning framework that allows direct transfer from in-the-wild human demonstrations to deployable robot policies.
- **p. 2 / I. INTRODUCTION - extractive body cue:** When combined with the GoPro's built-in IMU sensor, we can enable robust tracking under fast motion. • Second, we explore the right policy interface (i.e., ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Concretely, we employ inference-time latency matching to handle different sensor observation and execution latency, use relative trajectory as action representation to remove the need for ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** While users can theoretically collect any actions with these hand-held devices, much of that data can not be transferred to an effective robot policy.
- **p. 1 / I. INTRODUCTION - extractive body cue:** What prevents action transfer in previous work?

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** Unfortunately, neither ∗Indicates equal contribution is sufficient, as teleoperation requires high setup costs for hardware and expert operators, while human videos exhibit a large embodiment ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** 2), we show that UMI is capable of achieving a wide range of manipulation tasks that involve dynamic, bimanual, precise and long-horizon actions by only ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Furthermore, when trained with diverse human demonstrations, the final policy exhibits zero-shot generalization to novel environments and objects, achieving a remarkable 70% success rate in ...

## Source Evidence Cues

- **p. 3 / III. METHOD - extractive body cue:** The following sections describe how we enable the above goals through our hardware and policy interface design.
- **p. 3 / III. METHOD - extractive body cue:** Universal Manipulation Interface (UMI) is hand-held data collection and policy learning framework that allows direct transfer from in-the-wild human demonstrations to deployable robot policies.
- **Detected method headings:** III. METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Demonstration representation | expert trajectory를 training pair/context로 정렬한다 | observation history, goal, expert action | temporal alignment, relabeling 또는 latent context construction을 수행 | training sample/context | The following sections describe how we enable the above goals through our hardware and policy interface design. | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Policy fitting | expert action distribution을 학습한다 | context와 action target | behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화 | policy/action distribution | Universal Manipulation Interface (UMI) is hand-held data collection and policy learning framework that allows direct transfer from in-the-wild human demonstrations to deployable ... | p. 3 (III. METHOD) |
| Closed-loop rollout | distribution shift와 recovery를 확인한다 | current observation/history | action/chunk을 실행하고 feedback으로 다음 prediction을 갱신 | trajectory/failure signal | The following sections describe how we enable the above goals through our hardware and policy interface design. | p. 3 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** observation history o_{t−H:t} -> expert-like action/chunk a_{t:t+H} -> imitation or action-distribution loss -> closed-loop task success and robustness.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | When, combined, GoPro, built-in, IMU, sensor, enable, robust, tracking, under, fast, motion, Second, explore | observation history와 expert trajectory/action | body cue; exact tensor/frame verify |
| State/latent | When, combined, GoPro, built-in, IMU, sensor, enable, robust, tracking, under | behavior policy와 temporal action context | body cue; notation verify |
| Action/output | Unfortunately, neither, Indicates, equal, contribution, sufficient, teleoperation, requires, high, setup | predicted action 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | not recovered | imitation or action-distribution loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / I. INTRODUCTION - extractive body cue:** When combined with the GoPro's built-in IMU sensor, we can enable robust tracking under fast motion. • Second, we explore the right policy interface (i.e., ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Concretely, we employ inference-time latency matching to handle different sensor observation and execution latency, use relative trajectory as action representation to remove the need for ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** While users can theoretically collect any actions with these hand-held devices, much of that data can not be transferred to an effective robot policy.
- **p. 3 / III. METHOD - extractive body cue:** The following sections describe how we enable the above goals through our hardware and policy interface design.
- **p. 3 / III. METHOD - extractive body cue:** Universal Manipulation Interface (UMI) is hand-held data collection and policy learning framework that allows direct transfer from in-the-wild human demonstrations to deployable robot policies.
- **p. 1 / I. INTRODUCTION - extractive body cue:** What prevents action transfer in previous work?
- **Normalized interface:** observation=observation history와 expert trajectory/action; state=behavior policy와 temporal action context; output/action=predicted action 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single-step 또는 action chunk/trajectory horizon; exact chunk length는 exact value not recovered from the selected body cues. | Capability This task pushes the boundaries of robot manipulation capability from several fronts: 1) it is an ultralong horizon task where each ... | episode/sequence/action-chunk boundary |
| Rate / latency | training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인. | Despite the videos from each gripper being relocalized separately, the relative pose between two grippers at each time step can be calculated ... | Hz/fps, inference time and control rate |
| Memory | current observation, temporal history 또는 recurrent/sequence context. | not recovered | window and reset |
| Compute | backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다. | Dish Washing Task The robot needs to execute 7 steps of sequentially dependent actions (turn on faucet, grasp plate, pick up sponge, ... | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / V. CAPABILITY EXPERIMENTS - extractive body cue:** Our policy (with inference time latency matching) achieves 105/120 = 87.5% success rate, counted by the number of objects successfully tossed to their corresponding bin.
- **p. 10 / V. CAPABILITY EXPERIMENTS - extractive body cue:** We test the policy robustness with different inference time perturbations such as moving robot base, novel objects, different lighting conditions, and adding different and more ...
- **p. 9 / V. CAPABILITY EXPERIMENTS - extractive body cue:** No CLIP-pretrained ViT vision encoder.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** following, sections, describe, enable, above, goals, through, hardware, policy, interface, design, Universal, Manipulation, UMI, hand-held, data, collection, learning, framework, allows.
- **Relevant PDF headings:** III. METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Demonstration representation | To access capability and generalization, we evaluate UMI on 4 real-world robotic tasks across both narrow domain and in-the-wild environments, shown in ... | p. 6 (IV. EVALUATIONS), p. 6 (V. CAPABILITY EXPERIMENTS) |
| Policy fitting | (b) Typical failure mode of the baseline/ablation policy. | p. 8 (V. CAPABILITY EXPERIMENTS), p. 7 (V. CAPABILITY EXPERIMENTS) |
| Closed-loop rollout | This baseline only achieves 11/20 = 55% success rate. | p. 7 (V. CAPABILITY EXPERIMENTS), p. 7 (V. CAPABILITY EXPERIMENTS) |

## Failure and Ablation Link

- **p. 8 / V. CAPABILITY EXPERIMENTS - extractive body cue:** Effect of side mirrors [HD3]: To our surprise, directly providing mirror images decreases the performance from 18/20 = 90% (no mirror) to 17/20 = 85%.
- **p. 7 / V. CAPABILITY EXPERIMENTS - extractive body cue:** The next paragraphs will discuss our ablation studies around our key design decisions.
- **p. 7 / V. CAPABILITY EXPERIMENTS - extractive body cue:** … Toss lego to rectangle bin Grasp lego block Toss orange to round bin Init Init Reorient handle to the right Grasp espresso cup Final: ...
- **p. 8 / V. CAPABILITY EXPERIMENTS - extractive body cue:** (b) Typical failure mode of the baseline/ablation policy.
- **p. 9 / V. CAPABILITY EXPERIMENTS - extractive body cue:** No relative inter-gripper proprioception [PD2.3]: Without inter-gripper proprioception information (during both training and eval), the coordination between the two arms becomes significantly worse.
- **p. 9 / V. CAPABILITY EXPERIMENTS - extractive body cue:** Dish Washing Task The robot needs to execute 7 steps of sequentially dependent actions (turn on faucet, grasp plate, pick up sponge, wash and wipe ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6: Relative Trajectory as Action Representation. Relative trajectory, used by UMI, is a sequence of end-effector (EE) poses relative to the same current EE ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (III. METHOD), p. 3 (III. METHOD), objective 본문 anchor 없음, temporal p. 9 (V. CAPABILITY EXPERIMENTS), p. 6 (125 Hz), p. 1 (Front matter), p. 1 (Abstract), p. 3 (III. METHOD), p. 6 (V. CAPABILITY EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
