# Method - ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p066.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p066.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (B. Phase-based Motion Tracking Policy Training), p. 5 (B. Training Delta Action Model), p. 5 (B. Training Delta Action Model), p. 10 (B. Different Usage of Delta Action Model), p. 4 (B. Phase-based Motion Tracking Policy Training), p. 10 (A. Key Factors in Training Delta Action Models)): ‘The policy trained in the first stage can track the reference motion in the real-world but does not achieve high motion quality. ‘Thus, during the second stage, as shown in ...

## Method Body Digest

- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** ‘The policy trained in the first stage can track the reference motion in the real-world but does not achieve high motion quality. ‘Thus, during the ...
- **p. 5 / B. Training Delta Action Model - extractive body cue:** As illustrated in Figure 2 (b), the delta action model is defined as Ady = (se, 44)» where the policy 77> leams to output corrective ...
- **p. 5 / B. Training Delta Action Model - extractive body cue:** The RL environment incorporates this delta action model by modifying the simulator dynamies as follows: sey1 F(se,a; + Nay) where f° represents the simulator's dynamics, ...
- **p. 10 / B. Different Usage of Delta Action Model - extractive body cue:** ‘To answer QS (How to best use the delta action model of ASAP?), we compare multiple strategies: fixed-point iteration, gradient-based optimization, and reinforcement learning (RL).
- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** To ‘optimize the policy. we use the proximal policy optimization (PPO) {80}, aiming to maximize the cumulative discounted reward E (SP In) We identify several ...
- **p. 10 / A. Key Factors in Training Delta Action Models - extractive body cue:** ‘essential principles for effectively training a high-performing delta action model.
- **p. 11 / A. Learning-based Methods for Humanoid Control - extractive body cue:** Primarily leveraging reinforcement learning algorithms [80] within physics simulators [58, 63, 88], humanoid robots have earned a wide range of skills, including robust locomo
- **p. 10 / B. Different Usage of Delta Action Model - extractive body cue:** We consider two RL-free methods: fixed-point iteration and gradient-based optimization, Fixed:-point iteration refines #(s) iteratively, while gradient-based optimization minimizes a loss function to achieve a ...

## Design Rationale

- **p. 1 / Abstract - extractive body cue:** mnparal- or result in overly conservative policies that sacrifice a yaper, we present ASAP
- **p. 2 / Abstract - extractive body cue:** To this end, we propose ASAP, a two-stage framework that aligns the dynamics mismatch between simulation and realworld physics, enabling agile humanoid whole-body skills ASAP ...
- **p. 3 / Abstract - extractive body cue:** 1) We introduce ASAP, a framework that bridges the simto-real gap by leveraging a delta action model trained via reinforcement learning (RL) with real-world data

## Source Evidence Cues

- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** ‘The policy trained in the first stage can track the reference motion in the real-world but does not achieve high motion quality. ‘Thus, during the ...
- **p. 5 / B. Training Delta Action Model - extractive body cue:** As illustrated in Figure 2 (b), the delta action model is defined as Ady = (se, 44)» where the policy 77> leams to output corrective ...
- **p. 5 / B. Training Delta Action Model - extractive body cue:** The RL environment incorporates this delta action model by modifying the simulator dynamies as follows: sey1 F(se,a; + Nay) where f° represents the simulator's dynamics, ...
- **p. 10 / B. Different Usage of Delta Action Model - extractive body cue:** ‘To answer QS (How to best use the delta action model of ASAP?), we compare multiple strategies: fixed-point iteration, gradient-based optimization, and reinforcement learning (RL).
- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** To ‘optimize the policy. we use the proximal policy optimization (PPO) {80}, aiming to maximize the cumulative discounted reward E (SP In) We identify several ...
- **p. 10 / A. Key Factors in Training Delta Action Models - extractive body cue:** ‘essential principles for effectively training a high-performing delta action model.
- **p. 11 / A. Learning-based Methods for Humanoid Control - extractive body cue:** Primarily leveraging reinforcement learning algorithms [80] within physics simulators [58, 63, 88], humanoid robots have earned a wide range of skills, including robust locomo
- **Detected method headings:** B. Phase-based Motion Tracking Policy Training (p. 3); B. Training Delta Action Model (p. 4); C. Fine-tuning Motion Tracking Policy under New Dynamics (p. 5); B. Comparison of Policy Fine-Tuning Performance (p. 7); A. Key Factors in Training Delta Action Models (p. 9); B. Different Usage of Delta Action Model (p. 10); A. Learning-based Methods for Humanoid Control (p. 11)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | ‘The policy trained in the first stage can track the reference motion in the real-world but does not achieve high motion quality. ... | p. 4 (B. Phase-based Motion Tracking Policy Training), p. 5 (B. Training Delta Action Model) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | As illustrated in Figure 2 (b), the delta action model is defined as Ady = (se, 44)» where the policy 77> leams ... | p. 5 (B. Training Delta Action Model), p. 5 (B. Training Delta Action Model) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | The RL environment incorporates this delta action model by modifying the simulator dynamies as follows: sey1 F(se,a; + Nay) where f° represents ... | p. 5 (B. Training Delta Action Model), p. 10 (B. Different Usage of Delta Action Model) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 10 / B. Different Usage of Delta Action Model - extractive body cue:** We consider two RL-free methods: fixed-point iteration and gradient-based optimization, Fixed:-point iteration refines #(s) iteratively, while gradient-based optimization minimizes a loss function to achieve a ...
- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** To ‘optimize the policy. we use the proximal policy optimization (PPO) {80}, aiming to maximize the cumulative discounted reward E (SP In) We identify several ...
- **p. 5 / B. Training Delta Action Model - extractive body cue:** 2) A reward signal is computed to minimize the diserepancy between the simulated state s,.1 and the recorded real-world state sf, with an additional sction ...
- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** 4d) Reward Terms: We define the reward function ry with the sum of three terms: 1) penalty, 2) regularization, and 3) task rewards, A detailed ...
- **p. 3 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** The specific reward terms can be found in Table I.
- **p. 3 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** Using the agent's proprioception SP and the goal state sf, we define the reward as ry = Rs!
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 10 (B. Different Usage of Delta Action Model), p. 10 (B. Different Usage of Delta Action Model), p. 11 (B. Different Usage of Delta Action Model).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | illustrated, Figure, delta, action, model, defined, Ady, where, policy, leams, output, corrective, actions, current | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | illustrated, Figure, delta, action, model, defined, Ady, where, policy, leams | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | mnparal-, result, overly, conservative, policies, sacrifice, yaper, present, ASAP, two-stage | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | consider, RL-free, methods, fixed-point, iteration, gradient-based, optimization, Fixed, point, refines | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / B. Training Delta Action Model - extractive body cue:** As illustrated in Figure 2 (b), the delta action model is defined as Ady = (se, 44)» where the policy 77> leams to output corrective ...
- **p. 2 / Abstract - extractive body cue:** Wwe tin the dea action model by minimizing the discrepancy between simulation sales; and real-world sates () Policy Fine-taning: We freeze the ‘eli action model ...
- **p. 2 / Abstract - extractive body cue:** However, directly deploying this policy on real hardware results in degraded performance due to the dynamics mismatch, To address this, the post training stage collects ...
- **p. 3 / Abstract - extractive body cue:** Finally, we fine-tune the pre-trained policy using the delta action model, allowing it to adapt effectively to real-world physics.
- **p. 3 / Abstract - extractive body cue:** system, The collected data are then replayed in simulation, Where the dynamics mismatch manifests as tracking errors We then train a delta action model that ...
- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** PosT-TRAINING: TRAINING DELTA ACTION MODEL AND FINE-TUNING MOTION TRACKING POLICY
- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** ‘The policy trained in the first stage can track the reference motion in the real-world but does not achieve high motion quality. ‘Thus, during the ...
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | The proprioception s? is defined as 3P 2 [de aes de an ea Gear Mesa], With Sestep history of joint position q, ... | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | At each timestep 1, we use' a motion capture device and onboard sensors to record the state: s¢ = [p"*, vp", ab™*, ... | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | The proprioception s? is defined as 3P 2 [de aes de an ea Gear Mesa], With Sestep history of joint position q, ... | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** ‘The policy trained in the first stage can track the reference motion in the real-world but does not achieve high motion quality. ‘Thus, during the ...
- **p. 5 / B. Training Delta Action Model - extractive body cue:** The RL environment incorporates this delta action model by modifying the simulator dynamies as follows: sey1 F(se,a; + Nay) where f° represents the simulator's dynamics, ...
- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** To ‘optimize the policy. we use the proximal policy optimization (PPO) {80}, aiming to maximize the cumulative discounted reward E (SP In) We identify several ...
- **p. 10 / A. Key Factors in Training Delta Action Models - extractive body cue:** ‘essential principles for effectively training a high-performing delta action model.
- **p. 3 / 3) Extensive experiments in both simulation and real-world - extractive body cue:** 4) To facilitate smooth transfer between simulators, we develop and open-source a multi-simulstor training and evaluation codebase for help accelerate further research.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** policy, trained, first, stage, track, reference, motion, real-world, does, achieve, high, quality, Thus, during, second, Figure, leverage, data, rolled, pre-trained.
- **Relevant PDF headings:** B. Phase-based Motion Tracking Policy Training (p. 3); B. Training Delta Action Model (p. 4); C. Fine-tuning Motion Tracking Policy under New Dynamics (p. 5); B. Comparison of Policy Fine-Tuning Performance (p. 7); A. Key Factors in Training Delta Action Models (p. 9); B. Different Usage of Delta Action Model (p. 10); A. Learning-based Methods for Humanoid Control (p. 11).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | This process ensures accurate motion retargeting and produces the cleuned robot trajectory dataset DG as shown in Figure 3 (). | p. 3 (3) Extensive experiments in both simulation and real-world), p. 3 (3) Extensive experiments in both simulation and real-world) |
| Balance-aware whole-body execution | Fig. 10. Analysis of dataset size, waning horizon, and scion aorm on the performance of x. (a) Dataset Size: Mean Per Joint ... | p. 10 (Figure/Table caption), p. 10 (Figure/Table caption) |
| Recovery / adaptation | Fig. 10. Analysis of dataset size, waning horizon, and scion aorm on the performance of x. (a) Dataset Size: Mean Per Joint ... | p. 10 (Figure/Table caption), p. 11 (C. Does ASAP Fine-Tuning Outperform Random Action Noise) |

## Failure and Ablation Link

- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 10. Analysis of dataset size, waning horizon, and scion aorm on the performance of x. (a) Dataset Size: Mean Per Joint Position Eror (MPIPE) ...
- **p. 11 / C. Does ASAP Fine-Tuning Outperform Random Action Noise - extractive body cue:** Such structured discrepancies cannot be effectively captured by merely adding uniform action noise.
- **p. 12 / B. Offine and Online System Identification for Roboties - extractive body cue:** + Hardware Constraints: Agile whole-body motions exert significant stress on robots, leading to motor overheating, and hardware failure during data collection.
- **p. 12 / B. Offine and Online System Identification for Roboties - extractive body cue:** While ASAP demonstrates promising results in bridging the sim-to-real gap for agile humanoid control, our framework has several real-world limitations that highlights critical challenges in ...
- **p. 11 / C. Does ASAP Fine-Tuning Outperform Random Action Noise - extractive body cue:** However, the performance of the action noise approach (MPJPE of 150) does not match the precision achieved by ASAP (MPIPE of 126).
- **p. 10 / A. Key Factors in Training Delta Action Models - extractive body cue:** However, this trend ‘does not consistently extend to closed-loop performance.
- **p. 3 / 3) Extensive experiments in both simulation and real-world - extractive body cue:** b) Simulation-based Data Cleaning: Since the reconstruction process can introduce noise and errors [25], some estimated motions may not be physically feasible, making them unsuitable ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (B. Phase-based Motion Tracking Policy Training), p. 5 (B. Training Delta Action Model), p. 5 (B. Training Delta Action Model), p. 10 (B. Different Usage of Delta Action Model), p. 4 (B. Phase-based Motion Tracking Policy Training), p. 10 (A. Key Factors in Training Delta Action Models), objective p. 10 (B. Different Usage of Delta Action Model), p. 4 (B. Phase-based Motion Tracking Policy Training), p. 5 (B. Training Delta Action Model), p. 4 (B. Phase-based Motion Tracking Policy Training), p. 3 (B. Phase-based Motion Tracking Policy Training), p. 3 (B. Phase-based Motion Tracking Policy Training), temporal p. 3 (B. Phase-based Motion Tracking Policy Training), p. 4 (A. Data Collection), p. 10 (A. Key Factors in Training Delta Action Models), p. 11 (B. Different Usage of Delta Action Model), p. 12 (B. Offine and Online System Identification for Roboties), p. 2 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
