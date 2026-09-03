# Method - HumanPlus: Humanoid Shadowing and Imitation from Humans

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=WnSl42M9Z4; PDF retrieval source: https://arxiv.org/pdf/2406.10454. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1. Introduction), p. 7 (6. Imitation of Human Skills), p. 5 (4. Human Body and Hand Data), p. 3 (1. Introduction), p. 7 (6. Imitation of Human Skills), p. 1 (Abstract)): We leverage this dataset by first retargeting human poses to humanoid poses and then training a task-agnostic low-level policy called Humanoid Shadowing Transformer conditioning on the retargeted humanoid poses.

## Method Body Digest

- **p. 2 / 1. Introduction - extractive body cue:** We leverage this dataset by first retargeting human poses to humanoid poses and then training a task-agnostic low-level policy called Humanoid Shadowing Transformer conditioning on ...
- **p. 7 / 6. Imitation of Human Skills - extractive body cue:** In this work, we modify the Action Chunking Transformer [104] by removing its encoder-decoder architecture to develop a decoder-only Humanoid Imitation Transformer (HIT) for skill ...
- **p. 5 / 4. Human Body and Hand Data - extractive body cue:** Our system consists of a decoder-only transformer for low-level control, Humanoid Shadowing Transformer, and a decoder-only transformer for imitation learning, Humanoid Imitation Transformer.
- **p. 3 / 1. Introduction - extractive body cue:** We build upon the recent success of imitation learning from human-provided demonstrations [11, 104], and introduce a transformer-based architecture that blends action prediction and forward ...
- **p. 7 / 6. Imitation of Human Skills - extractive body cue:** We incorporate an L2 feature loss on these predicted image features, compelling the transformer to predict corresponding image feature tokens for future states after execution ...
- **p. 1 / Abstract - extractive body cue:** We first train a low-level policy in simulation via reinforcement learning using existing 40-hour human motion datasets.
- **p. 2 / 1. Introduction - extractive body cue:** The complex dynamics and high-dimensional state and action spaces of humanoids pose difficulties in both perception and control.
- **p. 6 / 5. Shadowing of Human Motion - extractive body cue:** We use PPO [74] to train our Humanoid Shadowing Transformer in simulation by maximizing discounted expected return E hPT-1 t=0 γtrt i , where rt ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we present a full-stack system for humanoids to learn motion and autonomous skills from human data.
- **p. 3 / 1. Introduction - extractive body cue:** Core to this system is both (1) a real-time shadowing system that allows human operators to whole-body control humanoids using a single RGB camera and ...
- **p. 3 / 1. Introduction - extractive body cue:** Using forward dynamics prediction on image features, our method shows improved performance by regularizing on image feature spaces and preventing the vision-based skill policy from ...

## Source Evidence Cues

- **p. 2 / 1. Introduction - extractive body cue:** We leverage this dataset by first retargeting human poses to humanoid poses and then training a task-agnostic low-level policy called Humanoid Shadowing Transformer conditioning on ...
- **p. 7 / 6. Imitation of Human Skills - extractive body cue:** In this work, we modify the Action Chunking Transformer [104] by removing its encoder-decoder architecture to develop a decoder-only Humanoid Imitation Transformer (HIT) for skill ...
- **p. 5 / 4. Human Body and Hand Data - extractive body cue:** Our system consists of a decoder-only transformer for low-level control, Humanoid Shadowing Transformer, and a decoder-only transformer for imitation learning, Humanoid Imitation Transformer.
- **p. 3 / 1. Introduction - extractive body cue:** We build upon the recent success of imitation learning from human-provided demonstrations [11, 104], and introduce a transformer-based architecture that blends action prediction and forward ...
- **p. 7 / 6. Imitation of Human Skills - extractive body cue:** We incorporate an L2 feature loss on these predicted image features, compelling the transformer to predict corresponding image feature tokens for future states after execution ...
- **p. 1 / Abstract - extractive body cue:** We first train a low-level policy in simulation via reinforcement learning using existing 40-hour human motion datasets.
- **p. 2 / 1. Introduction - extractive body cue:** The complex dynamics and high-dimensional state and action spaces of humanoids pose difficulties in both perception and control.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | We leverage this dataset by first retargeting human poses to humanoid poses and then training a task-agnostic low-level policy called Humanoid Shadowing ... | p. 2 (1. Introduction), p. 7 (6. Imitation of Human Skills) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | In this work, we modify the Action Chunking Transformer [104] by removing its encoder-decoder architecture to develop a decoder-only Humanoid Imitation Transformer ... | p. 7 (6. Imitation of Human Skills), p. 5 (4. Human Body and Hand Data) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | Our system consists of a decoder-only transformer for low-level control, Humanoid Shadowing Transformer, and a decoder-only transformer for imitation learning, Humanoid Imitation ... | p. 5 (4. Human Body and Hand Data), p. 3 (1. Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 5. Shadowing of Human Motion - extractive body cue:** We use PPO [74] to train our Humanoid Shadowing Transformer in simulation by maximizing discounted expected return E hPT-1 t=0 γtrt i , where rt ...
- **p. 2 / 1. Introduction - extractive body cue:** Typically, learning-based low-level policies are designed to be task-specific due to time-consuming reward engineering [19, 68], enabling the humanoid hardware to demonstrate only one skill ...
- **p. 5 / 4. Human Body and Hand Data - extractive body cue:** Reward Teams Expressions target xy velocities exp(-/[vx, vy] -[vtg x , vtg y ]/) target yaw velocities exp(-/vyaw -vtg yaw/) target joint positions -/q -qtg/2 ...
- **p. 6 / 5. Shadowing of Human Motion - extractive body cue:** The reward r is the sum of terms encouraging matching 6
- **p. 7 / 5. Shadowing of Human Motion - extractive body cue:** We list all the reward terms in the Table 1.
- **p. 7 / 6. Imitation of Human Skills - extractive body cue:** We incorporate an L2 feature loss on these predicted image features, compelling the transformer to predict corresponding image feature tokens for future states after execution ...
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 7 (6. Imitation of Human Skills).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | state-of-the-art, human, body, hand, pose, estimation, algorithms, estimate, real-time, motion, retarget, humanoid, passed, input | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | state-of-the-art, human, body, hand, pose, estimation, algorithms, estimate, real-time, motion | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | present, full-stack, system, humanoids, learn, motion, autonomous, skills, human, data | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | PPO, train, Humanoid, Shadowing, Transformer, simulation, maximizing, discounted, expected, return | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** Using state-of-the-art human body and hand pose estimation algorithms [58, 81], we can estimate real-time human motion and retarget it to humanoid motion, which is ...
- **p. 5 / 5. Shadowing of Human Motion - extractive body cue:** At each time step, the input to the policy is humanoid proprioception and a humanoid target pose.
- **p. 2 / 1. Introduction - extractive body cue:** The complex dynamics and high-dimensional state and action spaces of humanoids pose difficulties in both perception and control.
- **p. 3 / 1. Introduction - extractive body cue:** A skill policy takes in humanoid binocular egocentric RGB vision as inputs and predicts the desired humanoid body and hand poses.
- **p. 5 / 5. Shadowing of Human Motion - extractive body cue:** The humanoid proprioception contains root state (row, pitch, and base angular velocities), joint positions, joint velocities and last action.
- **p. 6 / 5. Shadowing of Human Motion - extractive body cue:** Our low-level policy operates at 50Hz and has a context length of 8, so it can adapt to different environments given the observation history [67].
- **p. 3 / 1. Introduction - extractive body cue:** Using forward dynamics prediction on image features, our method shows improved performance by regularizing on image feature spaces and preventing the vision-based skill policy from ...
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | We use PPO [74] to train our Humanoid Shadowing Transformer in simulation by maximizing discounted expected return E hPT-1 t=0 γtrt i ... | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | At each time step, the input to the policy is humanoid proprioception and a humanoid target pose. | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | The body pose estimation and retargeting runs at 25 fps on an NVIDIA RTX4090 GPU. | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1. Introduction - extractive body cue:** We leverage this dataset by first retargeting human poses to humanoid poses and then training a task-agnostic low-level policy called Humanoid Shadowing Transformer conditioning on ...
- **p. 1 / Abstract - extractive body cue:** We first train a low-level policy in simulation via reinforcement learning using existing 40-hour human motion datasets.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** leverage, dataset, first, retargeting, human, poses, humanoid, then, training, task-agnostic, low-level, policy, called, Shadowing, Transformer, conditioning, retargeted, modify, Action, Chunking.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | Shown in Table 5, we compare our imitation learning method Humanoid Imitation Transformer with three baseline methods: HIT policies with monocular inputs ... | p. 10 (9. Experiments on Imitation), p. 10 (8.1. Comparisons with Other Teleoperation) |
| Balance-aware whole-body execution | Overall HIT (Ours) outperforms others. | p. 9 (8. Experiments on Shadowing), p. 9 (8.1. Comparisons with Other Teleoperation) |
| Recovery / adaptation | Our HIT achieves higher success rates than other baselines across all tasks. | p. 10 (9. Experiments on Imitation), p. 9 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 9 / 8.1. Comparisons with Other Teleoperation - extractive body cue:** The participants are tasked to perform the Rearrange Objects task and its variant, Rearrange Lower Objects, where an object is placed on a lower table ...
- **p. 10 / 9. Experiments on Imitation - extractive body cue:** Although each skill policy solves its task continuously autonomously without stopping, we document the success rates of consecutive sub-tasks within each task for better analysis.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: Robustness Evaluation. Our low-level policy (Ours) can withstand large disturbance forces, has a shorter recovery time, and enables more whole-body skills than the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Teleop Comparisons & User Studies. We report averaged completion time for 6 participants on 2 tasks. target poses while saving energy and avoiding ...
- **p. 10 / 9. Experiments on Imitation - extractive body cue:** Throughout the development of our system, we encountered several limitations.
- **p. 10 / 9. Experiments on Imitation - extractive body cue:** It fails the Wear a Shoe and Walk task completely, where depth perception is crucial.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1. Introduction), p. 7 (6. Imitation of Human Skills), p. 5 (4. Human Body and Hand Data), p. 3 (1. Introduction), p. 7 (6. Imitation of Human Skills), p. 1 (Abstract), objective p. 6 (5. Shadowing of Human Motion), p. 2 (1. Introduction), p. 5 (4. Human Body and Hand Data), p. 6 (5. Shadowing of Human Motion), p. 7 (5. Shadowing of Human Motion), p. 7 (6. Imitation of Human Skills), temporal p. 6 (5. Shadowing of Human Motion), p. 5 (5. Shadowing of Human Motion), p. 10 (8.2. Robustness Evaluation), p. 10 (8.2. Robustness Evaluation), p. 4 (2. Related Work), p. 2 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Using state-of-the-art human body and hand pose estimation algorithms [58, 81], we can estimate real-time human motion and retarget it to humanoid motion, which is passed as input to the ... (p. 2, 1. Introduction).
- **Objective/update evidence:** Typically, learning-based low-level policies are designed to be task-specific due to time-consuming reward engineering [19, 68], enabling the humanoid hardware to demonstrate only one skill at a time, such as ... (p. 2, 1. Introduction).
- **Temporal/runtime evidence:** More recovery steps result in jittery behavior and compromise manipulation performance. (p. 10, 8.2. Robustness Evaluation).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
