# Method - Mobile ALOHA: Learning Bimanual Mobile Manipulation using Low-Cost Whole-Body Teleoperation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2401.02117; PDF retrieval source: https://arxiv.org/pdf/2401.02117. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3. Mobile ALOHA Hardware), p. 2 (1. Introduction), p. 5 (3. Mobile ALOHA Hardware), p. 2 (1. Introduction), p. 4 (3. Mobile ALOHA Hardware), p. 1 (Abstract)): The training objective for a mobile manipulation policy πm for a task m is E(oi,aiarms,ai base)∼Dm mobile  L(ai arms, ai base, πm(oi))  + E(oi,aiarms)∼Dstatic  L(ai arms, [0, ...

## Method Body Digest

- **p. 5 / 3. Mobile ALOHA Hardware - extractive body cue:** The training objective for a mobile manipulation policy πm for a task m is E(oi,aiarms,ai base)∼Dm mobile  L(ai arms, ai base, πm(oi))  + ...
- **p. 2 / 1. Introduction - extractive body cue:** While many recent works demonstrate that highly expressive policy classes such as diffusion models and transformers can perform well on fine-grained, multi-modal manipulation tasks, it ...
- **p. 5 / 3. Mobile ALOHA Hardware - extractive body cue:** In this work, we use a co-training pipeline that leverages the existing static ALOHA datasets to improve the performance of imitation learning for mobile manipulation, ...
- **p. 2 / 1. Introduction - extractive body cue:** On the imitation learning front, we observe that simply concatenating the base and arm actions then training via direct imitation learning can yield strong performance.
- **p. 4 / 3. Mobile ALOHA Hardware - extractive body cue:** We also record the joint positions of all 4 robot arms to be used as policy observations and actions.
- **p. 1 / Abstract - extractive body cue:** Using data collected with Mobile ALOHA, we then perform supervised behavior cloning and find that co-training with existing static ALOHA datasets boosts performance on mobile ...
- **p. 4 / 3. Mobile ALOHA Hardware - extractive body cue:** We record the linear and angular velocities of the mobile base to be used as actions of the learned policy.
- **p. 1 / Abstract - extractive body cue:** We first present Mobile ALOHA, a low-cost and whole-body teleoperation system for data collection.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** On the hardware front, we present Mobile ALOHA, a low-cost and whole-body teleoperation system for collecting bimanual mobile manipulation data.
- **p. 2 / 1. Introduction - extractive body cue:** The main contribution of this paper is a system for learning complex mobile bimanual manipulation tasks.
- **p. 1 / 1. Introduction - extractive body cue:** Imitation learning from human-provided demonstrations is a promising tool for developing generalist robots, as it allows people to teach arbitrary skills to robots.

## Source Evidence Cues

- **p. 5 / 3. Mobile ALOHA Hardware - extractive body cue:** The training objective for a mobile manipulation policy πm for a task m is E(oi,aiarms,ai base)∼Dm mobile  L(ai arms, ai base, πm(oi))  + ...
- **p. 2 / 1. Introduction - extractive body cue:** While many recent works demonstrate that highly expressive policy classes such as diffusion models and transformers can perform well on fine-grained, multi-modal manipulation tasks, it ...
- **p. 5 / 3. Mobile ALOHA Hardware - extractive body cue:** In this work, we use a co-training pipeline that leverages the existing static ALOHA datasets to improve the performance of imitation learning for mobile manipulation, ...
- **p. 2 / 1. Introduction - extractive body cue:** On the imitation learning front, we observe that simply concatenating the base and arm actions then training via direct imitation learning can yield strong performance.
- **p. 4 / 3. Mobile ALOHA Hardware - extractive body cue:** We also record the joint positions of all 4 robot arms to be used as policy observations and actions.
- **p. 1 / Abstract - extractive body cue:** Using data collected with Mobile ALOHA, we then perform supervised behavior cloning and find that co-training with existing static ALOHA datasets boosts performance on mobile ...
- **p. 4 / 3. Mobile ALOHA Hardware - extractive body cue:** We record the linear and angular velocities of the mobile base to be used as actions of the learned policy.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Scene / interaction state | base·arm·object 관계를 표현한다 | egocentric RGB-D, language goal, proprioception | map, object, reachability, contact 또는 affordance state를 구성 | base-arm interaction state | The training objective for a mobile manipulation policy πm for a task m is E(oi,aiarms,ai base)∼Dm mobile  L(ai arms, ai base, ... | p. 5 (3. Mobile ALOHA Hardware), p. 2 (1. Introduction) |
| Base-arm task decision | 접근·도킹·grasp·manipulation sequence를 결정한다 | interaction state와 task instruction | keypoint, option, trajectory, grasp 또는 joint planning을 수행 | base path plus arm/gripper plan | While many recent works demonstrate that highly expressive policy classes such as diffusion models and transformers can perform well on fine-grained, multi-modal ... | p. 2 (1. Introduction), p. 5 (3. Mobile ALOHA Hardware) |
| Execution / correction | 부분 실행 후 observation으로 계획을 수정한다 | current pose, visual/force feedback | tracking, regrasp, docking correction, recovery 또는 replan을 수행 | next mobile-manipulation action | In this work, we use a co-training pipeline that leverages the existing static ALOHA datasets to improve the performance of imitation learning ... | p. 5 (3. Mobile ALOHA Hardware), p. 2 (1. Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3. Mobile ALOHA Hardware - extractive body cue:** The training objective for a mobile manipulation policy πm for a task m is E(oi,aiarms,ai base)∼Dm mobile  L(ai arms, ai base, πm(oi))  + ...
- **p. 1 / Abstract - extractive body cue:** We first present Mobile ALOHA, a low-cost and whole-body teleoperation system for data collection.
- **p. 2 / 1. Introduction - extractive body cue:** Bimanual mobile manipulators can be costly if purchased off-the-shelf.
- **p. 2 / 1. Introduction - extractive body cue:** Robots like the PR2 and the TIAGo can cost more than $200k USD, making them unaffordable for typical research labs.
- **p. 3 / 3. Mobile ALOHA Hardware - extractive body cue:** Mobile ALOHA inherits the benefits of the original ALOHA system [104], i.e. the low-cost, dex3
- **p. 3 / 3. Mobile ALOHA Hardware - extractive body cue:** We develop Mobile ALOHA, a low-cost mobile manipulator that can perform a broad range of household tasks.
- **Formal bridge:** base-arm-object state and language/task goal -> base plus arm/gripper action -> long-horizon task utility under reachability/contact constraints -> task completion and recovery.
- **Equation/algorithm anchors:** p. 5 (3. Mobile ALOHA Hardware), p. 6 (5. Tasks).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | observation, consistent, across, different, class, state-of-the-art, imitation, learning, methods, including, ACT, Diffusion, Policy, record | egocentric RGB-D, language/task goal, base-arm proprioception | body cue; exact tensor/frame verify |
| State/latent | observation, consistent, across, different, class, state-of-the-art, imitation, learning, methods, including | map/object/contact state와 base-arm coordination decision | body cue; notation verify |
| Action/output | hardware, front, present, Mobile, ALOHA, low-cost, whole-body, teleoperation, system, collecting | base motion plus arm/gripper action | body cue; unit/decoder verify |
| Objective/constraint | training, objective, mobile, manipulation, policy, task, aiarms, base, arms, Dstatic | long-horizon task utility under reachability/contact constraints | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** This observation is also consistent across different class of state-of-the-art imitation learning methods, including ACT [104] and Diffusion Policy [18].
- **p. 4 / 3. Mobile ALOHA Hardware - extractive body cue:** We also record the joint positions of all 4 robot arms to be used as policy observations and actions.
- **p. 2 / 1. Introduction - extractive body cue:** While many recent works demonstrate that highly expressive policy classes such as diffusion models and transformers can perform well on fine-grained, multi-modal manipulation tasks, it ...
- **p. 4 / 3. Mobile ALOHA Hardware - extractive body cue:** We record the linear and angular velocities of the mobile base to be used as actions of the learned policy.
- **p. 5 / 3. Mobile ALOHA Hardware - extractive body cue:** We do not use any special data processing techniques on either the RGB observations or the bimanual actions of the static ALOHA data for our ...
- **p. 5 / 3. Mobile ALOHA Hardware - extractive body cue:** The training objective for a mobile manipulation policy πm for a task m is E(oi,aiarms,ai base)∼Dm mobile  L(ai arms, ai base, πm(oi))  + ...
- **p. 8 / 5. Tasks - extractive body cue:** VINN with chunking, Diffusion Policy, and ACT all achieves good performance on Mobile ALOHA, and benefit from co-training with static ALOHA. the mobile base's velocity ...
- **Normalized interface:** observation=egocentric RGB-D, language/task goal, base-arm proprioception; state=map/object/contact state와 base-arm coordination decision; output/action=base motion plus arm/gripper action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | As a preliminary, all methods we will examine employ "action chunking" [104], where a policy predicts a sequence of future actions instead ... | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | To account for a delay of d steps of the mobile base, our robot executes the first k -d arm actions and ... | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | not recovered | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | It contains 825 episodes with tasks disjoint from the Mobile ALOHA tasks, and has different mounting positions of the two arms. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3. Mobile ALOHA Hardware - extractive body cue:** The training objective for a mobile manipulation policy πm for a task m is E(oi,aiarms,ai base)∼Dm mobile  L(ai arms, ai base, πm(oi))  + ...
- **p. 5 / 3. Mobile ALOHA Hardware - extractive body cue:** In this work, we use a co-training pipeline that leverages the existing static ALOHA datasets to improve the performance of imitation learning for mobile manipulation, ...
- **p. 2 / 1. Introduction - extractive body cue:** On the imitation learning front, we observe that simply concatenating the base and arm actions then training via direct imitation learning can yield strong performance.
- **p. 1 / Abstract - extractive body cue:** Using data collected with Mobile ALOHA, we then perform supervised behavior cloning and find that co-training with existing static ALOHA datasets boosts performance on mobile ...
- **p. 9 / 6.1. Co-training Improves Performance - extractive body cue:** For pre-train, we first train ACT on the static ALOHA data and then fine-tune it with the Mobile ALOHA data. co-training, we simply co-train the ...
- **p. 4 / 3. Mobile ALOHA Hardware - extractive body cue:** All compute during data collection and inference is conducted on a consumer-grade laptop with Nvidia 3070 Ti GPU (8GB VRAM) and Intel i7-12800H.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** training, objective, mobile, manipulation, policy, task, aiarms, base, arms, Dstatic, where, observation, consisting, wrist, camera, RGB, observations, egocentric, mounted, between.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Scene / interaction state | We then evaluate each policy in the real-world, with randomization of robot and objects configurations as described in Figure 3. | p. 8 (6.1. Co-training Improves Performance), p. 8 (6.1. Co-training Improves Performance) |
| Base-arm task decision | Co-train outperforms pre-train on the Wipe Wine task. | p. 9 (6.1. Co-training Improves Performance), p. 8 (6.1. Co-training Improves Performance) |
| Execution / correction | Co-training improves the whole-task success rate in 5 out of the 7 tasks, with a boost of 45%, 20%, 80%, 95% and ... | p. 8 (6.1. Co-training Improves Performance), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / 6.1. Co-training Improves Performance - extractive body cue:** We start with ACT [104], the method introduced with ALOHA, and train it on all 7 tasks with and without co-training.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Hardware Details. Left: Mobile ALOHA has two wrist cameras and one top camera, with onboard power and compute. Middle: The teleoperation setup can ...
- **p. 9 / 6.1. Co-training Improves Performance - extractive body cue:** For pre-train, we first train ACT on the static ALOHA data and then fine-tune it with the Mobile ALOHA data. co-training, we simply co-train the ...
- **p. 10 / 8. User Studies - extractive body cue:** Despite Mobile ALOHA's simplicity and performance, there are still limitations that we hope to address in future works.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Hardware Details. Left: Mobile ALOHA has two wrist cameras and one top camera, with onboard power and compute. Middle: The teleoperation setup can ...
- **p. 8 / 6.1. Co-training Improves Performance - extractive body cue:** In all of these cases, compounding errors appear to be the main source of failure, either from the stochasticity of robot base velocity control or ...
- **p. 9 / 6.1. Co-training Improves Performance - extractive body cue:** The main failure modes are imprecise grasping on Lift Glass and Wipe as well as jerky motion when switching between chunks.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3. Mobile ALOHA Hardware), p. 2 (1. Introduction), p. 5 (3. Mobile ALOHA Hardware), p. 2 (1. Introduction), p. 4 (3. Mobile ALOHA Hardware), p. 1 (Abstract), objective p. 5 (3. Mobile ALOHA Hardware), p. 1 (Abstract), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Mobile ALOHA Hardware), p. 3 (3. Mobile ALOHA Hardware), temporal p. 8 (6. Experiments), p. 8 (6. Experiments), p. 9 (6.1. Co-training Improves Performance), p. 9 (6.1. Co-training Improves Performance), p. 1 (Front matter), p. 2 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
