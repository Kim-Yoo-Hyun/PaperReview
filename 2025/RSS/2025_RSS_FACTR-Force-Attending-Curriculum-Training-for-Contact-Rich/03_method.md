# Method - FACTR: Force-Attending Curriculum Training for Contact-Rich Policy Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p079.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p079.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (A. Problem Statement and Base Model), p. 5 (A. Problem Statement and Base Model), p. 4 (A. Problem Statement and Base Model), p. 4 (A. Problem Statement and Base Model)): Visual observations and force readings are converted into tokens, fed to the encoder, then decoded into action tokens through cross attention.

## Method Body Digest

- **p. 5 / A. Problem Statement and Base Model - extractive body cue:** Visual observations and force readings are converted into tokens, fed to the encoder, then decoded into action tokens through cross attention.
- **p. 5 / A. Problem Statement and Base Model - extractive body cue:** then tokenized by a vision encoder and a force encoder before fed into an action transformer to regress joint position targets gee.
- **p. 4 / A. Problem Statement and Base Model - extractive body cue:** We consider a policy o(- / -) that produces a chunk of future actions of length k d..++1 (joint positions) given visual observation [, (image ...
- **p. 4 / A. Problem Statement and Base Model - extractive body cue:** Each trajectory in D comprises tuples (I;,7:, 1).
- **p. 5 / A. Problem Statement and Base Model - extractive body cue:** attends to vision vs. force tokens at layer [, and will be the Finally, we project the decoder output H/? to action space,
- **p. 4 / A. Problem Statement and Base Model - extractive body cue:** Where ques are the expert's future joint position targets and dut+k are the policy's predictions.

## Design Rationale

- **p. 5 / A. Problem Statement and Base Model - extractive body cue:** For the decoder, we introduce & action tokens, A ¢ R**¢.
- **p. 5 / A. Problem Statement and Base Model - extractive body cue:** 4: FACTR allows our policy to beter integrate force information without overfittng to visual information, resulting in better generalization

## Source Evidence Cues

- **p. 5 / A. Problem Statement and Base Model - extractive body cue:** Visual observations and force readings are converted into tokens, fed to the encoder, then decoded into action tokens through cross attention.
- **p. 5 / A. Problem Statement and Base Model - extractive body cue:** then tokenized by a vision encoder and a force encoder before fed into an action transformer to regress joint position targets gee.
- **p. 4 / A. Problem Statement and Base Model - extractive body cue:** We consider a policy o(- / -) that produces a chunk of future actions of length k d..++1 (joint positions) given visual observation [, (image ...
- **p. 4 / A. Problem Statement and Base Model - extractive body cue:** Each trajectory in D comprises tuples (I;,7:, 1).
- **Detected method headings:** A. Problem Statement and Base Model (p. 4); C. Policy Evaluation (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multi-modal contact encoding | vision과 touch를 contact feature로 결합한다 | tactile image/force, vision, proprioception | tactile encoder, calibration, fusion 또는 temporal feature extraction을 수행 | contact feature/state | Visual observations and force readings are converted into tokens, fed to the encoder, then decoded into action tokens through cross attention. | p. 5 (A. Problem Statement and Base Model), p. 5 (A. Problem Statement and Base Model) |
| Contact / dynamics inference | contact mode와 object response를 추정한다 | contact feature와 action history | mode classifier, force/dynamics model 또는 state estimator를 update | contact/force prediction | then tokenized by a vision encoder and a force encoder before fed into an action transformer to regress joint position targets gee. | p. 5 (A. Problem Statement and Base Model), p. 4 (A. Problem Statement and Base Model) |
| Force-aware action correction | interaction feedback으로 command를 보정한다 | predicted contact와 current wrench/touch | policy/control law가 action, force 또는 grasp를 재계산 | contact-safe action/torque | We consider a policy o(- / -) that produces a chunk of future actions of length k d..++1 (joint positions) given visual ... | p. 4 (A. Problem Statement and Base Model), p. 4 (A. Problem Statement and Base Model) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** visual/tactile/proprioceptive contact history -> contact-aware action/force -> contact prediction/control error -> slip/contact success and safe interaction.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | consider, policy, produces, chunk, future, actions, length, joint, positions, given, visual, observation, image, time | tactile image/force, vision과 proprioceptive history | body cue; exact tensor/frame verify |
| State/latent | consider, policy, produces, chunk, future, actions, length, joint, positions, given | contact geometry, force state 또는 latent dynamics | body cue; notation verify |
| Action/output | decoder, introduce, action, tokens, FACTR, allows, policy, beter, integrate, force | grasp/contact action, force command 또는 object motion | body cue; unit/decoder verify |
| Objective/constraint | not recovered | contact prediction/control error | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / A. Problem Statement and Base Model - extractive body cue:** We consider a policy o(- / -) that produces a chunk of future actions of length k d..++1 (joint positions) given visual observation [, (image ...
- **p. 5 / A. Problem Statement and Base Model - extractive body cue:** attends to vision vs. force tokens at layer [, and will be the Finally, we project the decoder output H/? to action space,
- **p. 5 / A. Problem Statement and Base Model - extractive body cue:** Visual observations and force readings are converted into tokens, fed to the encoder, then decoded into action tokens through cross attention.
- **p. 4 / A. Problem Statement and Base Model - extractive body cue:** Where ques are the expert's future joint position targets and dut+k are the policy's predictions.
- **Normalized interface:** observation=tactile image/force, vision과 proprioceptive history; state=contact geometry, force state 또는 latent dynamics; output/action=grasp/contact action, force command 또는 object motion.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | contact episode 또는 action chunk horizon; contact event timing이 핵심이다. | We let dues be the predicted future joint position targets over the next k time steps. | episode/sequence/action-chunk boundary |
| Rate / latency | tactile sampling/control loop가 visual policy rate와 다를 수 있다; numeric values 확인 필요. | + ACT (Vision-Only) [32]: Action Chunking Transformer | Hz/fps, inference time and control rate |
| Memory | recent tactile/force history와 visual state; recurrent memory 여부 확인 필요. | Specifically, we visualize the cross attention of the action tokens to the memory tokens denoted as a{ and a") for the first ... | window and reset |
| Compute | sensor fusion, contact inference와 high-frequency correction이 latency를 결정한다. | For each object in each task, we evaluated 5-10 trials. | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / C. Policy Evaluation - extractive body cue:** We collected 50 demonstrations with our teleoperation system, We trained each method with the same hyperparameters, where details can be found in the Appendix X, ...
- **p. 9 / C. Policy Evaluation - extractive body cue:** the force oF vision tokens of the first decoder layer during policy rollout.
- **p. 9 / C. Policy Evaluation - extractive body cue:** We evaluate only on the five test objects for five trials each, since they are more indicative of policy performance than train objects.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Visual, observations, force, readings, converted, tokens, encoder, then, decoded, action, through, cross, attention, tokenized, vision, before, transformer, regress, joint, position.
- **Relevant PDF headings:** A. Problem Statement and Base Model (p. 4); C. Policy Evaluation (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multi-modal contact encoding | These asks are challenging as they require the robot to perceive and respond to the force feedback as it manipulates objects with ... | p. 7 (B. Teleoperation Evaluation), p. 8 (C. Policy Evaluation) |
| Contact / dynamics inference | ‘+ How does FACTR perform compared to baseline approaches that do not use force feedback and ones that use force feedback without ... | p. 7 (C. Policy Evaluation), p. 7 (B. Teleoperation Evaluation) |
| Force-aware action correction | For the test objects, the vision-only policy achieves a success rate of 21.3% on average, which is significantly worse than policies incorporating ... | p. 8 (C. Policy Evaluation), p. 8 (C. Policy Evaluation) |

## Failure and Ablation Link

- **p. 7 / C. Policy Evaluation - extractive body cue:** We discuss more detailed ablations ‘on the curriculum in See.
- **p. 7 / C. Policy Evaluation - extractive body cue:** ‘+ How does FACTR perform compared to baseline approaches that do not use force feedback and ones that use force feedback without FACTR?
- **p. 8 / C. Policy Evaluation - extractive body cue:** While without the curriculum, the policy does not pay enough attention 10 force, and either fails to lift or balance the novel boxes.
- **p. 8 / C. Policy Evaluation - extractive body cue:** Without a curriculum, policies naively incorporating force achieve a success rate of 61.2%, ‘hile FACTR achieves a success rate of 87.5%, which shows that FACTR ...
- **p. 9 / C. Policy Evaluation - extractive body cue:** We choose the task of pivoting, one of the hardest tasks from our task suite, for the ablations.
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: FACTR allows our policy to beter integrate force information without overfittng to visual information, resulting in better generalization
- **p. 9 / VI. CONCLUSION AND LIMITATIONS - extractive body cue:** Developing. adaptive or self-tuning curriculum strategies could help mitigate this issue by dynamically adjusting hyperparameters based on task-specific requirements, Addressing these limitations could further enhance ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (A. Problem Statement and Base Model), p. 5 (A. Problem Statement and Base Model), p. 4 (A. Problem Statement and Base Model), p. 4 (A. Problem Statement and Base Model), objective 본문 anchor 없음, temporal p. 4 (A. Problem Statement and Base Model), p. 7 (C. Policy Evaluation), p. 7 (C. Policy Evaluation), p. 8 (C. Policy Evaluation), p. 8 (C. Policy Evaluation), p. 9 (C. Policy Evaluation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
