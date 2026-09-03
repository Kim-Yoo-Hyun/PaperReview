# Method - Perpetual Humanoid Control for Real-time Simulated Avatars

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2023/html/Luo_Perpetual_Humanoid_Control_for_Real-time_Simulated_Avatars_ICCV_2023_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2023/html/Luo_Perpetual_Humanoid_Control_for_Real-time_Simulated_Avatars_ICCV_2023_paper.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.1. Goal Conditioned Motion Imitation with Ad), p. 4 (3.1. Goal Conditioned Motion Imitation with Ad), p. 5 (3.2. Progressive Multiplicative Control Policy), p. 3 (3.1. Goal Conditioned Motion Imitation with Ad), p. 3 (3.1. Goal Conditioned Motion Imitation with Ad), p. 5 (3.1. Goal Conditioned Motion Imitation with Ad)): (1) For the discriminator, we use the same observations, loss formulation, and gradient penalty as AMP [33].

## Method Body Digest

- **p. 4 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** (1) For the discriminator, we use the same observations, loss formulation, and gradient penalty as AMP [33].
- **p. 4 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** We use a proportional derivative (PD) controller at each DoF of the humanoid and the action at specifies the PD target.
- **p. 5 / 3.2. Progressive Multiplicative Control Policy - extractive body cue:** Thus, we propose a progressive multiplicative control policy (PMCP), which allocates new subnetworks (primitives P) to learn harder sequences.
- **p. 3 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** The physics simulation determines state st ∈S and transition dynamics T while our policy πPHC computes per-step action at ∈A.
- **p. 3 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** The simulation state st ≜(sp t, sg t) consists of humanoid proprioception sp t and the goal state sg t.
- **p. 5 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** We use a similar hard negative mining procedure as in UHC [20] and define hard sequences by whether or not our controller can successfully imitate ...
- **p. 6 / 3.3. Connecting with Motion Estimators - extractive body cue:** For language-based motion generation, we use the Motion Diffusion Model (MDM) [41].
- **p. 3 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** The policy's goal is to maximize the discounted reward E hPT t=1 γt-1rt i , and we use the proximal policy gradient (PPO) [35] to ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our contributions are as follows: (1) we propose a Perpetual Humanoid Controller that can successfully imitate 98.9% of the AMASS dataset without applying ...
- **p. 5 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** Thus, we propose Relaxed Early Termination (RET), which allows the humanoid's ankle and toes to slightly deviate from the MoCap motion to remain balanced.
- **p. 3 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** The simulation state st ≜(sp t, sg t) consists of humanoid proprioception sp t and the goal state sg t.

## Source Evidence Cues

- **p. 4 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** (1) For the discriminator, we use the same observations, loss formulation, and gradient penalty as AMP [33].
- **p. 4 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** We use a proportional derivative (PD) controller at each DoF of the humanoid and the action at specifies the PD target.
- **p. 5 / 3.2. Progressive Multiplicative Control Policy - extractive body cue:** Thus, we propose a progressive multiplicative control policy (PMCP), which allocates new subnetworks (primitives P) to learn harder sequences.
- **p. 3 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** The physics simulation determines state st ∈S and transition dynamics T while our policy πPHC computes per-step action at ∈A.
- **p. 3 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** The simulation state st ≜(sp t, sg t) consists of humanoid proprioception sp t and the goal state sg t.
- **p. 5 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** We use a similar hard negative mining procedure as in UHC [20] and define hard sequences by whether or not our controller can successfully imitate ...
- **p. 6 / 3.3. Connecting with Motion Estimators - extractive body cue:** For language-based motion generation, we use the Motion Diffusion Model (MDM) [41].
- **Detected method headings:** 3. Method (p. 3); 3.2. Progressive Multiplicative Control Policy (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | (1) For the discriminator, we use the same observations, loss formulation, and gradient penalty as AMP [33]. | p. 4 (3.1. Goal Conditioned Motion Imitation with Ad), p. 4 (3.1. Goal Conditioned Motion Imitation with Ad) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | We use a proportional derivative (PD) controller at each DoF of the humanoid and the action at specifies the PD target. | p. 4 (3.1. Goal Conditioned Motion Imitation with Ad), p. 5 (3.2. Progressive Multiplicative Control Policy) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | Thus, we propose a progressive multiplicative control policy (PMCP), which allocates new subnetworks (primitives P) to learn harder sequences. | p. 5 (3.2. Progressive Multiplicative Control Policy), p. 3 (3.1. Goal Conditioned Motion Imitation with Ad) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** The policy's goal is to maximize the discounted reward E hPT t=1 γt-1rt i , and we use the proximal policy gradient (PPO) [35] to ...
- **p. 4 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** (1) For the discriminator, we use the same observations, loss formulation, and gradient penalty as AMP [33].
- **p. 4 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** The task reward is defined based on the current training objective, which can be chosen by switching the reward function for motion imitation Rimitation and ...
- **p. 3 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** Based on the simulation state st and reference motion ˆqt, the reward function R computes a reward rt = R(st, ˆqt) as the learning signal ...
- **p. 5 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** Notice that the humanoid still receives imitation and discriminator rewards for these body parts, which prevents these joints from moving in a nonhuman manner.
- **p. 5 / 3.2. Progressive Multiplicative Control Policy - extractive body cue:** This amounts to setting the non-root joint goals to be identity when computing the goal states: sg-Fail t ≜(ˆθ′ t⊖θt, ˆp′ t-pt, ˆv′ t-vt, ˆω′ ...
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 4 (3.1. Goal Conditioned Motion Imitation with Ad), p. 3 (3.1. Goal Conditioned Motion Imitation with Ad), p. 4 (3.1. Goal Conditioned Motion Imitation with Ad), p. 5 (3.2. Progressive Multiplicative Control Policy).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | physics, simulation, determines, state, transition, dynamics, while, policy, PHC, computes, per-step, action, shares, same | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | physics, simulation, determines, state, transition, dynamics, while, policy, PHC, computes | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | summarize, contributions, follows, Perpetual, Humanoid, Controller, successfully, imitate, AMASS, dataset | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | policy, goal, maximize, discounted, reward, hPT, t-1rt, proximal, gradient, PPO | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** The physics simulation determines state st ∈S and transition dynamics T while our policy πPHC computes per-step action at ∈A.
- **p. 5 / 3.2. Progressive Multiplicative Control Policy - extractive body cue:** P(F ) shares the same input and output space as P(1) · · · P(k), but since the reference motion does not provide useful information ...
- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our contributions are as follows: (1) we propose a Perpetual Humanoid Controller that can successfully imitate 98.9% of the AMASS dataset without applying ...
- **p. 6 / 3.2. Progressive Multiplicative Control Policy - extractive body cue:** Specifically, our composer C(w1:K+1 t /st) consumes the same input as the primitives and outputs a weight vector w1:K+1 t ∈Rk+1 to activate the primitives.
- **p. 6 / 3.2. Progressive Multiplicative Control Policy - extractive body cue:** Combining our composer and primitives, we have the PHC's output distribution: \scri p tsi z e \pol i c y (\ba _t \ m id ...
- **p. 3 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** Based on the simulation state st and reference motion ˆqt, the reward function R computes a reward rt = R(st, ˆqt) as the learning signal ...
- **p. 2 / 1. Introduction - extractive body cue:** In this work, we consider human poses estimated from video or language input.
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | For rotation-based motion imitation, the goal state sg t is defined as the difference between the next time step reference quantitives and ... | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | { g-recover}}_ t = \ rewardfuncf a i lrec (\ s t ate , \ref p ) = 0.5 r^{\text {g-point}}_t + ... | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | Experiments are run randomly 1000 trials. | hardware, batch and throughput |

## Training vs Inference

- training/inference separation PDF body cue not selected; no claim inferred

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** discriminator, same, observations, loss, formulation, gradient, penalty, AMP, proportional, derivative, controller, DoF, humanoid, action, specifies, target, Thus, progressive, multiplicative, control.
- **Relevant PDF headings:** 3. Method (p. 3); 3.2. Progressive Multiplicative Control Policy (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | PHC is trained on the training split of the AMASS [23] dataset. | p. 7 (4. Experiments), p. 7 (4.1. Motion Imitation) |
| Balance-aware whole-body execution | Similar to results on MoCap Imitation, PHC outperforms the baselines 10901 | p. 7 (4.1. Motion Imitation), p. 7 (4.1. Motion Imitation) |
| Recovery / adaptation | H36M-Test-Video* RET MCP PNN Rotation Fail-Recover Succ ↑ Eg-mpjpe ↓ Empjpe ↓ ✗ ✗ ✗ ✓ ✗ 51.2% 56.2 34.4 ✓ ✗ ... | p. 8 (4.1. Motion Imitation), p. 7 (4.1. Motion Imitation) |

## Failure and Ablation Link

- **p. 8 / 4.1. Motion Imitation - extractive body cue:** Comparing R4 and R5 shows that PMCP is effective in adding fail-state recovery capability without compromising motion imitation.
- **p. 7 / 4. Experiments - extractive body cue:** We compare against UHC both with and without residual force control.
- **p. 7 / 4. Experiments - extractive body cue:** Succ measures whether the humanoid can track the reference motion without losing balance or significantly lags behind.
- **p. 8 / 4.1. Motion Imitation - extractive body cue:** We perform ablation on the noisy input from H36M-Test-Image* to better showcase the controller's ability to imitate noisy data.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: We propose a motion imitator that can naturally recover from falls and walk to far-away reference motion, perpetually controlling simulated avatars without requiring ...
- **p. 8 / 5. Discussions - extractive body cue:** Although we can train single-clip controller to overfit on these sequences (see the supplement), our full controller often fails to learn these sequences.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: (a) Imitating high-quality MoCap - spin and kick. (b) Recover from fallen state and go back to reference motion (indicated by red dots). ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.1. Goal Conditioned Motion Imitation with Ad), p. 4 (3.1. Goal Conditioned Motion Imitation with Ad), p. 5 (3.2. Progressive Multiplicative Control Policy), p. 3 (3.1. Goal Conditioned Motion Imitation with Ad), p. 3 (3.1. Goal Conditioned Motion Imitation with Ad), p. 5 (3.1. Goal Conditioned Motion Imitation with Ad), objective p. 3 (3.1. Goal Conditioned Motion Imitation with Ad), p. 4 (3.1. Goal Conditioned Motion Imitation with Ad), p. 4 (3.1. Goal Conditioned Motion Imitation with Ad), p. 3 (3.1. Goal Conditioned Motion Imitation with Ad), p. 5 (3.1. Goal Conditioned Motion Imitation with Ad), p. 5 (3.2. Progressive Multiplicative Control Policy), temporal p. 3 (3.1. Goal Conditioned Motion Imitation with Ad), p. 6 (3.2. Progressive Multiplicative Control Policy), p. 8 (4.2. Fail-state Recovery), p. 5 (3.2. Progressive Multiplicative Control Policy), p. 6 (3.3. Connecting with Motion Estimators), p. 7 (4.1. Motion Imitation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (10 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** The physics simulation determines state st ∈S and transition dynamics T while our policy πPHC computes per-step action at ∈A. (p. 3, 3.1. Goal Conditioned Motion Imitation with Ad).
- **Objective/update evidence:** The policy's goal is to maximize the discounted reward E hPT t=1 γt-1rt i , and we use the proximal policy gradient (PPO) [35] to learn πPHC. (p. 3, 3.1. Goal Conditioned Motion Imitation with Ad).
- **Temporal/runtime evidence:** During training, we construct each ˆ Q(k) hard by selecting the failed sequences from the previous step ˆ Q(k-1) hard , resulting in a smaller and smaller hard subset: ˆ ... (p. 5, 3.2. Progressive Multiplicative Control Policy).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
