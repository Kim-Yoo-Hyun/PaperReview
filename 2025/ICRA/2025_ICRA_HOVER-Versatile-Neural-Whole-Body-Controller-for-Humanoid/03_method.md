# Method - HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://api.crossref.org/works/10.1109/icra55743.2025.11128549; PDF retrieval source: https://research.nvidia.com/labs/lpr/publication/he2025hover/. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 4 (II. METHOD), p. 3 (II. METHOD), p. 2 (II. METHOD), p. 2 (II. METHOD), p. 3 (II. METHOD), p. 4 (II. METHOD)): The student policy πstudent is then updated by minimizing the loss function: L = ∥ˆat -at∥2 2, where ˆat is the reference action from the oracle, and at is the ...

## Method Body Digest

- **p. 4 / II. METHOD - extractive body cue:** The student policy πstudent is then updated by minimizing the loss function: L = ∥ˆat -at∥2 2, where ˆat is the reference action from the ...
- **p. 3 / II. METHOD - extractive body cue:** We use the same policy network structure with [9], a three-layer MLP with layer dimensions of [512, 256, 128].
- **원문 대조:** 보상은 proprioceptive state와 goal state의 함수 R(s_t^p,s_t^g)로 정의한다. 정책 action은 19차원 목표 관절 위치이며 PD controller에 전달한다. 보상 정의 자체가 recovery 절차를 명시하는 것은 아니다. ([PDF p. 2](https://hover-versatile-humanoid.github.io/resources/HOVER_paper.pdf#page=2), §II-A Goal-Conditioned RL for Humanoid Control).
- **p. 2 / II. METHOD - extractive body cue:** We employ the proximal policy optimization (PPO) algorithm [18] to maximize the cumulative discounted reward E hPT t=1 γt-1rt i .
- **p. 3 / II. METHOD - extractive body cue:** Oracle Policy Training from Large-Scale Human Motions State Space Design.
- **p. 4 / II. METHOD - extractive body cue:** Using these oracle states, we query the oracle teacher policy πoracle(ˆat/sp-oracle t , sg-oracle t ) to obtain the reference action ˆat.
- **p. 3 / II. METHOD - extractive body cue:** We formulate the reward rt as the sum of three components: 1) penalty, 2) regularization, and 3) task rewards, detailed in Table II.
- **p. 3 / II. METHOD - extractive body cue:** Term Weight Term Weight Penalty Torque limits -2 DoF position limits -1.25e2 Termination -2.5e2 DoF velocity limits -5e1 Regularization DoF acceleration -1.1e-5 DoF velocity -4e-3 ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** To summarize, our contributions are threefold: 1) we present HOVER, a unified neural controller for humanoid whole-body control supporting multiple control modes; 2) we show ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To this end, we present HOVER, a unified neural controller for humanoid whole-body control that supports diverse control modes as shown in Figure 1, including ...
- **p. 3 / II. METHOD - extractive body cue:** In our framework, as shown in Figure 1, a one-hot masking vector is introduced to specify which components of the command space are activated for ...

## Source Evidence Cues

- **p. 4 / II. METHOD - extractive body cue:** The student policy πstudent is then updated by minimizing the loss function: L = ∥ˆat -at∥2 2, where ˆat is the reference action from the ...
- **p. 3 / II. METHOD - extractive body cue:** We use the same policy network structure with [9], a three-layer MLP with layer dimensions of [512, 256, 128].
- **원문 대조:** 보상은 proprioceptive state와 goal state의 함수 R(s_t^p,s_t^g)로 정의한다. 정책 action은 19차원 목표 관절 위치이며 PD controller에 전달한다. 보상 정의 자체가 recovery 절차를 명시하는 것은 아니다. ([PDF p. 2](https://hover-versatile-humanoid.github.io/resources/HOVER_paper.pdf#page=2), §II-A Goal-Conditioned RL for Humanoid Control).
- **p. 2 / II. METHOD - extractive body cue:** We employ the proximal policy optimization (PPO) algorithm [18] to maximize the cumulative discounted reward E hPT t=1 γt-1rt i .
- **p. 3 / II. METHOD - extractive body cue:** Oracle Policy Training from Large-Scale Human Motions State Space Design.
- **p. 4 / II. METHOD - extractive body cue:** Using these oracle states, we query the oracle teacher policy πoracle(ˆat/sp-oracle t , sg-oracle t ) to obtain the reference action ˆat.
- **Detected method headings:** II. METHOD (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | The student policy πstudent is then updated by minimizing the loss function: L = ∥ˆat -at∥2 2, where ˆat is the reference ... | p. 4 (II. METHOD), p. 3 (II. METHOD) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | We use the same policy network structure with [9], a three-layer MLP with layer dimensions of [512, 256, 128]. | p. 3 (II. METHOD), p. 2 (II. METHOD) |
| Goal-conditioned RL | 목표 motion tracking을 학습 | Proprioceptive state와 goal state | PPO로 reward 최적화 | 목표 관절 위치; recovery 절차는 이 근거로 확인 불가 | 원문 대조: 보상은 proprioceptive state와 goal state의 함수 R(s_t^p,s_t^g)로 정의한다. 정책 action은 19차원 목표 관절 위치이며 PD controller에 전달한다. 보상 정의 자체가 recovery 절차를 명시하는 것은 아니다. ([PDF p. 2](https://hover-versatile-humanoid.github.io/resources/HOVER_paper.pdf#page=2), §II-A Goal-Conditioned RL for Humanoid Control) | [PDF p. 2](https://hover-versatile-humanoid.github.io/resources/HOVER_paper.pdf#page=2), §II-A Goal-Conditioned RL for Humanoid Control |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / II. METHOD - extractive body cue:** We employ the proximal policy optimization (PPO) algorithm [18] to maximize the cumulative discounted reward E hPT t=1 γt-1rt i .
- **p. 4 / II. METHOD - extractive body cue:** The student policy πstudent is then updated by minimizing the loss function: L = ∥ˆat -at∥2 2, where ˆat is the reference action from the ...
- **원문 대조:** 보상은 proprioceptive state와 goal state의 함수 R(s_t^p,s_t^g)로 정의한다. 정책 action은 19차원 목표 관절 위치이며 PD controller에 전달한다. 보상 정의 자체가 recovery 절차를 명시하는 것은 아니다. ([PDF p. 2](https://hover-versatile-humanoid.github.io/resources/HOVER_paper.pdf#page=2), §II-A Goal-Conditioned RL for Humanoid Control).
- **p. 3 / II. METHOD - extractive body cue:** We formulate the reward rt as the sum of three components: 1) penalty, 2) regularization, and 3) task rewards, detailed in Table II.
- **p. 3 / II. METHOD - extractive body cue:** Term Weight Term Weight Penalty Torque limits -2 DoF position limits -1.25e2 Termination -2.5e2 DoF velocity limits -5e1 Regularization DoF acceleration -1.1e-5 DoF velocity -4e-3 ...
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 4 (II. METHOD), p. 3 (II. METHOD), p. 3 (II. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | oracle, states, query, teacher, policy, at/sp-oracle, sg-oracle, obtain, reference, action, agent, proprioception, goal, state | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | oracle, states, query, teacher, policy, at/sp-oracle, sg-oracle, obtain, reference, action | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | summarize, contributions, threefold, present, HOVER, unified, neural, controller, humanoid, whole-body | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | employ, proximal, policy, optimization, PPO, algorithm, maximize, cumulative, discounted, reward | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / II. METHOD - extractive body cue:** Using these oracle states, we query the oracle teacher policy πoracle(ˆat/sp-oracle t , sg-oracle t ) to obtain the reference action ˆat.
- **원문 대조:** 보상은 proprioceptive state와 goal state의 함수 R(s_t^p,s_t^g)로 정의한다. 정책 action은 19차원 목표 관절 위치이며 PD controller에 전달한다. 보상 정의 자체가 recovery 절차를 명시하는 것은 아니다. ([PDF p. 2](https://hover-versatile-humanoid.github.io/resources/HOVER_paper.pdf#page=2), §II-A Goal-Conditioned RL for Humanoid Control).
- **p. 3 / II. METHOD - extractive body cue:** For the student policy πstudent(sp-student t , sg-student t ) distilled from the oracle teacher πoracle, the proprioception is defined as sp-student t ≜ [q, ...
- **p. 3 / II. METHOD - extractive body cue:** As illustrated in Figure 2, the task command input for the student policy is defined using modebased and sparsity-based masking.
- **p. 4 / II. METHOD - extractive body cue:** The student policy πstudent is then updated by minimizing the loss function: L = ∥ˆat -at∥2 2, where ˆat is the reference action from the ...
- **p. 2 / II. METHOD - extractive body cue:** The state st comprises both the agent's proprioception sp t and the target goal state sg t.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This versatile command space covers most modes used in prior works [9, 10, 12, 13].
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | This setup is framed as a command-tracking task, where the humanoid learns to follow the target commands at each timestep. | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | At each timestep, we also compute the corresponding oracle states (sp-oracle t , sg-oracle t ). | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | Following [9], we stack these terms over the last 25 steps to represent the student's proprioceptive input. | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / II. METHOD - extractive body cue:** Oracle Policy Training from Large-Scale Human Motions State Space Design.
- **p. 4 / III. EXPERIMENT - extractive body cue:** In this section, we present extensive experimental results in both IsaacGym [23] and the real-world Unitree H1 [24] robot to address the following questions: • ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** student, policy, then, updated, minimizing, loss, function, where, reference, action, oracle, taken, same, network, structure, three-layer, MLP, layer, dimensions, agent.
- **Relevant PDF headings:** II. METHOD (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | In this section, we present extensive experimental results in both IsaacGym [23] and the real-world Unitree H1 [24] robot to address the ... | p. 4 (III. EXPERIMENT), p. 5 (III. EXPERIMENT) |
| Balance-aware whole-body execution | To address Q2 (does HOVER outperform other methods of training a multi-mode humanoid controller?), we compare HOVER with a multi-mode RL baseline ... | p. 5 (III. EXPERIMENT), p. 5 (III. EXPERIMENT) |
| Recovery / adaptation | In this section, we present extensive experimental results in both IsaacGym [23] and the real-world Unitree H1 [24] robot to address the ... | p. 4 (III. EXPERIMENT), p. 5 (III. EXPERIMENT) |

## Failure and Ablation Link

- **p. 5 / III. EXPERIMENT - extractive body cue:** Furthermore, this means that even when focusing on a single control mode without considering multi-mode versatility, distilling from an oracle policy still surpasses RL-trained specialists.
- **p. 6 / V. CONCLUSIONS - extractive body cue:** Future work will explore further developing an automated mode-switching module for real-world applications.
- **p. 6 / III. EXPERIMENT - extractive body cue:** The results demonstrate that HOVER can smoothly track motions across different modes, showcasing its robustness for real-world scenarios (e.g., when there are occlusions in the ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (II. METHOD), p. 3 (II. METHOD), p. 2 (II. METHOD), p. 2 (II. METHOD), p. 3 (II. METHOD), p. 4 (II. METHOD), objective p. 2 (II. METHOD), p. 4 (II. METHOD), p. 2 (II. METHOD), p. 3 (II. METHOD), p. 3 (II. METHOD), temporal p. 2 (II. METHOD), p. 4 (II. METHOD), p. 2 (II. METHOD), p. 3 (II. METHOD), p. 3 (II. METHOD), p. 4 (II. METHOD).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **원문 대조:** 보상은 proprioceptive state와 goal state의 함수 R(s_t^p,s_t^g)로 정의한다. 정책 action은 19차원 목표 관절 위치이며 PD controller에 전달한다. 보상 정의 자체가 recovery 절차를 명시하는 것은 아니다. ([PDF p. 2](https://hover-versatile-humanoid.github.io/resources/HOVER_paper.pdf#page=2), §II-A Goal-Conditioned RL for Humanoid Control).
- **Objective/update evidence:** We employ the proximal policy optimization (PPO) algorithm [18] to maximize the cumulative discounted reward E hPT t=1 γt-1rt i . (p. 2, II. METHOD).
- **Temporal/runtime evidence:** This setup is framed as a command-tracking task, where the humanoid learns to follow the target commands at each timestep. (p. 2, II. METHOD).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
