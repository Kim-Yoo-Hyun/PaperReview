# Method - WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=Czs2xH9114; PDF retrieval source: https://arxiv.org/pdf/2406.06005. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (1 Introduction), p. 6 (1 Introduction), p. 1 (1 Introduction), p. 1 (Abstract), p. 5 (1 Introduction), p. 5 (1 Introduction)): To develop RL-based controllers for these tasks, we formulate the policy learning problem as an extended Markov Decision Process (MDP) M = ⟨S, A, T , R, γ, Gcon, Gtask⟩of ...

## Method Body Digest

- **p. 3 / 1 Introduction - extractive body cue:** To develop RL-based controllers for these tasks, we formulate the policy learning problem as an extended Markov Decision Process (MDP) M = ⟨S, A, T ...
- **p. 6 / 1 Introduction - extractive body cue:** Lower Row: We transfer the policy to the real world, testing jumps with double-foot contacts at different heights and a "hug" posture. provided current and ...
- **p. 1 / 1 Introduction - extractive body cue:** Provided specific contact plans, the typical solution is to employ model-based motion planning or trajectory optimization to generate whole-body references for tracking [2, 3, 4].
- **p. 1 / Abstract - extractive body cue:** Humanoid activities involving sequential contacts are crucial for complex robotic interactions and operations in the real world and are traditionally solved by model-based motion planning, ...
- **p. 5 / 1 Introduction - extractive body cue:** [28, 40], we stack 3 control steps of previous joint states and actions, and append them to the policy observations to enhance the robustness by ...
- **p. 5 / 1 Introduction - extractive body cue:** Specifically, 1) we first train policies without domain randomization until they converge, 2) then resume training with domain randomization until convergence, and 3) afterwards increase ...
- **p. 2 / 1 Introduction - extractive body cue:** This then transforms each challenge to a question: Q1: How to reach desired contact states within each stage?
- **p. 3 / 1 Introduction - extractive body cue:** The objective is to maximize the expected return E [P t γtrt] by finding an optimal policy at = π∗(st/gcon i:I , gtask i:I ).

## Design Rationale

- **p. 3 / 1 Introduction - extractive body cue:** In Section 4, we show how our framework, WoCoCo, can be applied to a variety of challenging dynamic tasks with flexible definitions and representations of ...
- **p. 5 / 1 Introduction - extractive body cue:** 4 Case Studies In this section, we show how our framework, WoCoCo, can be applied to various challenging tasks with different contact sequences.
- **p. 3 / 1 Introduction - extractive body cue:** In this paper, we study tasks where contact stages are predefined (e.g., heuristically designed), and our method can seamlessly be integrated with high-level contact planners ...

## Source Evidence Cues

- **p. 3 / 1 Introduction - extractive body cue:** To develop RL-based controllers for these tasks, we formulate the policy learning problem as an extended Markov Decision Process (MDP) M = ⟨S, A, T ...
- **p. 6 / 1 Introduction - extractive body cue:** Lower Row: We transfer the policy to the real world, testing jumps with double-foot contacts at different heights and a "hug" posture. provided current and ...
- **p. 1 / 1 Introduction - extractive body cue:** Provided specific contact plans, the typical solution is to employ model-based motion planning or trajectory optimization to generate whole-body references for tracking [2, 3, 4].
- **p. 1 / Abstract - extractive body cue:** Humanoid activities involving sequential contacts are crucial for complex robotic interactions and operations in the real world and are traditionally solved by model-based motion planning, ...
- **p. 5 / 1 Introduction - extractive body cue:** [28, 40], we stack 3 control steps of previous joint states and actions, and append them to the policy observations to enhance the robustness by ...
- **p. 5 / 1 Introduction - extractive body cue:** Specifically, 1) we first train policies without domain randomization until they converge, 2) then resume training with domain randomization until convergence, and 3) afterwards increase ...
- **p. 2 / 1 Introduction - extractive body cue:** This then transforms each challenge to a question: Q1: How to reach desired contact states within each stage?
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | To develop RL-based controllers for these tasks, we formulate the policy learning problem as an extended Markov Decision Process (MDP) M = ... | p. 3 (1 Introduction), p. 6 (1 Introduction) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | Lower Row: We transfer the policy to the real world, testing jumps with double-foot contacts at different heights and a "hug" posture. ... | p. 6 (1 Introduction), p. 1 (1 Introduction) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | Provided specific contact plans, the typical solution is to employ model-based motion planning or trajectory optimization to generate whole-body references for tracking ... | p. 1 (1 Introduction), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 1 Introduction - extractive body cue:** The objective is to maximize the expected return E [P t γtrt] by finding an optimal policy at = π∗(st/gcon i:I , gtask i:I ).
- **p. 2 / 1 Introduction - extractive body cue:** This drives the robot to explore further stages to maximize cumulative rewards, thus mitigating the shortsightedness caused by the RL policy strategically staying in the ...
- **p. 6 / 1 Introduction - extractive body cue:** There are two task-related reward terms, which incentivize minimizing the distances between the hands and the box, and between the box and its destination.
- **p. 7 / 1 Introduction - extractive body cue:** There are two task-related rewards, one encourageing spreading the arms, and the other incentivizing minimizing the distances between the feet and the centers of their ...
- **p. 2 / 1 Introduction - extractive body cue:** Besides, regarding effective policy learning, we also identify three challenges: (1) Contacts are sparse, especially when coupled with other whole-body motion goals such as balancing ...
- **p. 3 / 1 Introduction - extractive body cue:** In addressing Q3, we also propose a general sim-to-real pipeline with domain randomization and regularization rewards (Section 3.2).
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 3 (1 Introduction), p. 5 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | stack, control, steps, previous, joint, states, actions, append, them, policy, observations, enhance, robustness, temporal | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | stack, control, steps, previous, joint, states, actions, append, them, policy | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | Section, framework, WoCoCo, applied, variety, challenging, dynamic, tasks, flexible, definitions | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | objective, maximize, expected, return, finding, optimal, policy, st/gcon, gtask, drives | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 1 Introduction - extractive body cue:** [28, 40], we stack 3 control steps of previous joint states and actions, and append them to the policy observations to enhance the robustness by ...
- **p. 3 / 1 Introduction - extractive body cue:** To develop RL-based controllers for these tasks, we formulate the policy learning problem as an extended Markov Decision Process (MDP) M = ⟨S, A, T ...
- **p. 3 / 1 Introduction - extractive body cue:** The policy observations can include proprioception, exteroception (optional), and goal-related observations, which are detailed in Appendix H.
- **p. 8 / 1 Introduction - extractive body cue:** Another limitation is the requirement for explicit contact feedback (by contact sensors or human observers) to switch contact stages, a process that might be implicitly ...
- **p. 2 / 1 Introduction - extractive body cue:** Similarly, in existing works that showcase task-aware contact sequences in real-world humanoids, such as soccer playing [21] and loco-manipulation [22, 23, 24], each RL policy ...
- **p. 1 / Abstract - extractive body cue:** Although model-free reinforcement learning (RL) has become a powerful tool for versatile and robust whole-body humanoid control, it still requires tedious task-specific tuning and state ...
- **p. 2 / 1 Introduction - extractive body cue:** Besides, regarding effective policy learning, we also identify three challenges: (1) Contacts are sparse, especially when coupled with other whole-body motion goals such as balancing ...
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | We define it as rcon = ncorr -nconnwrong · 1(nstage > 0) + 2n2 conFconFtask, (3) where ncon is the maximal number ... | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | [28, 40], we stack 3 control steps of previous joint states and actions, and append them to the policy observations to enhance ... | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | [28, 40], we stack 3 control steps of previous joint states and actions, and append them to the policy observations to enhance ... | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 1 Introduction - extractive body cue:** Specifically, 1) we first train policies without domain randomization until they converge, 2) then resume training with domain randomization until convergence, and 3) afterwards increase ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** develop, RL-based, controllers, tasks, formulate, policy, learning, problem, extended, Markov, Decision, Process, MDP, Gcon, Gtask, state, action, transition, probability, reward.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | Left Middle Right Figure 4: Learned dancing motions in simulation and the real-world. | p. 7 (1 Introduction), p. 7 (1 Introduction) |
| Balance-aware whole-body execution | Figure 6: We train the dinosaur robot to push the ball towards destinations with different end effec- tors. By altering the destinations, ... | p. 8 (Figure/Table caption), p. 8 (1 Introduction) |
| Recovery / adaptation | Figure 3: Learned whole-body box loco-manipulation behaviors in the real world. Results. As shown in Fig. 3, the humanoid can efficiently turn, ... | p. 6 (Figure/Table caption), p. 6 (1 Introduction) |

## Failure and Ablation Link

- **p. 8 / 1 Introduction - extractive body cue:** In comparison, our curiosity rewards achieves effective exploration without overfitting specific behaviors.
- **p. 6 / 1 Introduction - extractive body cue:** Lower Row: We transfer the policy to the real world, testing jumps with double-foot contacts at different heights and a "hug" posture. provided current and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Learned cliffside climbing behavior in simulation and the real-world. The humanoid exhibited resilience against perturbations and compliance during contact with unseen gravels. Reward. ...
- **p. 8 / 1 Introduction - extractive body cue:** With 0-1 contact rewards r0-1 con = c0-1FconFtask, the humanoid cannot explore to jump over the stones, and tracks upper body postures without moving.
- **p. 8 / 1 Introduction - extractive body cue:** 6 Limitation and Future Works One limitation of our work is the lacking knowledge of when the controller will fail.
- **p. 8 / 1 Introduction - extractive body cue:** Therefore, we may explore failure predictors [56] and other safety assessment methods in the future [57].
- **p. 7 / 1 Introduction - extractive body cue:** The contact goal requires foot contact with the ground in their corresponding bounding boxes (predefined in the world frame), plus hand self-collision if the move ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (1 Introduction), p. 6 (1 Introduction), p. 1 (1 Introduction), p. 1 (Abstract), p. 5 (1 Introduction), p. 5 (1 Introduction), objective p. 3 (1 Introduction), p. 2 (1 Introduction), p. 6 (1 Introduction), p. 7 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), temporal p. 4 (1 Introduction), p. 5 (1 Introduction), p. 1 (Abstract), p. 5 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** To develop RL-based controllers for these tasks, we formulate the policy learning problem as an extended Markov Decision Process (MDP) M = ⟨S, A, T , R, γ, Gcon, Gtask⟩of ... (p. 3, 1 Introduction).
- **Objective/update evidence:** Provided specific contact plans, the typical solution is to employ model-based motion planning or trajectory optimization to generate whole-body references for tracking [2, 3, 4]. (p. 1, 1 Introduction).
- **Temporal/runtime evidence:** Although model-free reinforcement learning (RL) has become a powerful tool for versatile and robust whole-body humanoid control, it still requires tedious task-specific tuning and state machine design and suffers from ... (p. 1, Abstract).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
