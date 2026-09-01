# Method - OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=oL1WEZQal8; PDF retrieval source: https://arxiv.org/pdf/2406.08858. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (1 Introduction), p. 8 (1 Introduction), p. 8 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (1 Introduction)): To tackle this issue, We first train a teacher policy that uses privileged state information and then distill it to a student policy with limited state space.

## Method Body Digest

- **p. 4 / 1 Introduction - extractive body cue:** To tackle this issue, We first train a teacher policy that uses privileged state information and then distill it to a student policy with limited ...
- **p. 8 / 1 Introduction - extractive body cue:** We draw two key conclusions: (1) The Diffusion Policy significantly outperforms vanilla BC with ResNet; (2) In our LfD training, predicting a sequence of actions ...
- **p. 8 / 1 Introduction - extractive body cue:** We benchmark a variety of imitation learning algorithms on four tasks in our collected dataset (shown in Figure 7), including Diffusion Policy [58] with Denoising ...
- **p. 2 / 1 Introduction - extractive body cue:** We propose a pipeline to train a robust whole-body motion imitation policy via teach-student distillation and identify key factors in obtaining a stable control policy ...
- **p. 2 / 1 Introduction - extractive body cue:** In conclusion, our contributions are as follows: (1) We propose a pipeline to train a robust humanoid control policy that supports whole-body dexterous loco-manipulation with ...
- **p. 5 / 1 Introduction - extractive body cue:** As shown in Figure 3(c), we use the hand poses estimated by VR [52, 53], and directly compute joint targets based on inverse kinematics for ...
- **p. 7 / 1 Introduction - extractive body cue:** We use the same policy πOmniH2O across all tests, whether with fixed standing motion goals or motion goals controlled by joysticks, either moving forward or ...
- **p. 3 / 1 Introduction - extractive body cue:** We apply the Proximal Policy Optimization algorithm (PPO) [48] to maximize the cumulative discounted reward E hPT t=1 γt-1rt i .

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** In conclusion, our contributions are as follows: (1) We propose a pipeline to train a robust humanoid control policy that supports whole-body dexterous loco-manipulation with ...
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we propose OmniH2O, a learning-based system for whole-body humanoid teleoperation and autonomy.
- **p. 4 / 1 Introduction - extractive body cue:** To encourage standing still and taking large steps during locomotion, we propose a key reward function max feet height for each step.

## Source Evidence Cues

- **p. 4 / 1 Introduction - extractive body cue:** To tackle this issue, We first train a teacher policy that uses privileged state information and then distill it to a student policy with limited ...
- **p. 8 / 1 Introduction - extractive body cue:** We draw two key conclusions: (1) The Diffusion Policy significantly outperforms vanilla BC with ResNet; (2) In our LfD training, predicting a sequence of actions ...
- **p. 8 / 1 Introduction - extractive body cue:** We benchmark a variety of imitation learning algorithms on four tasks in our collected dataset (shown in Figure 7), including Diffusion Policy [58] with Denoising ...
- **p. 2 / 1 Introduction - extractive body cue:** We propose a pipeline to train a robust whole-body motion imitation policy via teach-student distillation and identify key factors in obtaining a stable control policy ...
- **p. 2 / 1 Introduction - extractive body cue:** In conclusion, our contributions are as follows: (1) We propose a pipeline to train a robust humanoid control policy that supports whole-body dexterous loco-manipulation with ...
- **p. 5 / 1 Introduction - extractive body cue:** As shown in Figure 3(c), we use the hand poses estimated by VR [52, 53], and directly compute joint targets based on inverse kinematics for ...
- **p. 7 / 1 Introduction - extractive body cue:** We use the same policy πOmniH2O across all tests, whether with fixed standing motion goals or motion goals controlled by joysticks, either moving forward or ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | To tackle this issue, We first train a teacher policy that uses privileged state information and then distill it to a student ... | p. 4 (1 Introduction), p. 8 (1 Introduction) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | We draw two key conclusions: (1) The Diffusion Policy significantly outperforms vanilla BC with ResNet; (2) In our LfD training, predicting a ... | p. 8 (1 Introduction), p. 8 (1 Introduction) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | We benchmark a variety of imitation learning algorithms on four tasks in our collected dataset (shown in Figure 7), including Diffusion Policy ... | p. 8 (1 Introduction), p. 2 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 1 Introduction - extractive body cue:** We apply the Proximal Policy Optimization algorithm (PPO) [48] to maximize the cumulative discounted reward E hPT t=1 γt-1rt i .
- **p. 2 / 1 Introduction - extractive body cue:** Regularization rewards are used to shape the desired motion but need to be applied with a curriculum.
- **p. 4 / 1 Introduction - extractive body cue:** Previous work [18, 3] often uses regularization rewards like feet air time or feet height to shape the lowerbody motions.
- **p. 4 / 1 Introduction - extractive body cue:** To train πprivileged that is suitable as a teacher for a real-world deployable student policy, we employ both imitation rewards and regularization rewards.
- **p. 5 / 1 Introduction - extractive body cue:** To update πOmniH2O, the loss is: L = ∥atprivileged -at∥2 2.
- **p. 1 / Abstract - extractive body cue:** We develop an RL-based sim-to-real pipeline, which involves large-scale retargeting and augmentation of human motion datasets, learning a real-world deployable policy with sparse sensor input ...
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 5 (1 Introduction), p. 2 (1 Introduction), p. 8 (1 Introduction), p. 8 (1 Introduction), p. 4 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | design, learning, demonstration, policy, LfD, pSparse-lfd, where, outputs, frames, motion, goals, given, image, input | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | design, learning, demonstration, policy, LfD, pSparse-lfd, where, outputs, frames, motion | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | conclusion, contributions, follows, pipeline, train, robust, humanoid, control, policy, supports | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | apply, Proximal, Policy, Optimization, algorithm, PPO, maximize, cumulative, discounted, reward | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 8 / 1 Introduction - extractive body cue:** We design our learning from demonstration policy to be πLfD(ˆpSparse-lfd t:t+ϕ /It), where πLfD outputs ϕ frames of motion goals given the image input It.
- **p. 3 / 1 Introduction - extractive body cue:** Based on proprioception sp t, goal state sg t, and action at, we define the reward rt = R  sp t, sg t, at  ...
- **p. 5 / 1 Introduction - extractive body cue:** For proprioception, the student policy sp-real t ≜(dt-25:t, ˙dt-25:t, ωroot t-25:t, gt-25:t, at-25-1:t-1) uses values easily accessible in the real-world, which includes 25-step history of ...
- **p. 6 / 1 Introduction - extractive body cue:** In Table 1(d), we find that linear velocity information does not boost performance in simulation, but it introduces significant challenges in real-world deployment (details illustrated ...
- **p. 1 / Abstract - extractive body cue:** We develop an RL-based sim-to-real pipeline, which involves large-scale retargeting and augmentation of human motion datasets, learning a real-world deployable policy with sparse sensor input ...
- **p. 3 / 1 Introduction - extractive body cue:** We formulate the learning problem as goal-conditioned RL for a Markov Decision Process (MDP) defined by the tuple M = ⟨S, A, T , R, ...
- **p. 5 / 1 Introduction - extractive body cue:** Note that no global linear velocity vt information is included in our observations and the policy implicitly learns velocity using history information.
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | 4.1.2 Real-world Motion-Tracking Results Table 2: Real-world motion tracking evaluation on 20 standing motions in ˆ Q Tested sequences Method State Dimensions ... | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | We train our deployable teleoperation policy πOmniH2O following the DAgger [51] framework: for each episode, we roll out the student policy πOmniH2O(at/sp-real ... | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | 4.1.2 Real-world Motion-Tracking Results Table 2: Real-world motion tracking evaluation on 20 standing motions in ˆ Q Tested sequences Method State Dimensions ... | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | 4.1.2 Real-world Motion-Tracking Results Table 2: Real-world motion tracking evaluation on 20 standing motions in ˆ Q Tested sequences Method State Dimensions ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 1 Introduction - extractive body cue:** To tackle this issue, We first train a teacher policy that uses privileged state information and then distill it to a student policy with limited ...
- **p. 8 / 1 Introduction - extractive body cue:** We draw two key conclusions: (1) The Diffusion Policy significantly outperforms vanilla BC with ResNet; (2) In our LfD training, predicting a sequence of actions ...
- **p. 2 / 1 Introduction - extractive body cue:** We propose a pipeline to train a robust whole-body motion imitation policy via teach-student distillation and identify key factors in obtaining a stable control policy ...
- **p. 2 / 1 Introduction - extractive body cue:** In conclusion, our contributions are as follows: (1) We propose a pipeline to train a robust humanoid control policy that supports whole-body dexterous loco-manipulation with ...
- **p. 8 / 1 Introduction - extractive body cue:** The training hyperparameters are in Appendix L.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** tackle, issue, first, train, teacher, policy, uses, privileged, state, information, then, distill, student, limited, space, draw, conclusions, Diffusion, significantly, outperforms.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | We benchmark a variety of imitation learning algorithms on four tasks in our collected dataset (shown in Figure 7), including Diffusion Policy ... | p. 8 (1 Introduction), p. 8 (1 Introduction) |
| Balance-aware whole-body execution | Figure 8: The illustration of using ZED camera VIO module, and the comparison of the velocity estimation of VIO with neural state ... | p. 22 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Recovery / adaptation | We draw two key conclusions: (1) The Diffusion Policy significantly outperforms vanilla BC with ResNet; (2) In our LfD training, predicting a ... | p. 8 (1 Introduction), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 22 / Figure/Table caption - extractive body cue:** Figure 8: The illustration of using ZED camera VIO module, and the comparison of the velocity estimation of VIO with neural state estimators. H Ablation ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: (a) Source motion; (b) Retar- geted motion; (c) Standing variant; (d) Squatting variant. Human Motion Retargeting. We train our motion imitation policy using ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Quantitative LfD average per- formance on 4 tasks over 10 runs. Metrics All Tasks (a) Ablation on Data size 25%data 50%data 100%data
- **p. 8 / 1 Introduction - extractive body cue:** Metrics All Tasks (a) Ablation on Data size 25%data 50%data 100%data MSE Loss 1.30E-2 7.48E-3 5.25E-4 Succ rate 4/10 6.5/10 8/10 (b) Ablation on Sequence ...
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 9: The ablation of data augmentation. I Additional Physical Teleoperation Results Additional VR-based and RGB-based teleoperation demo are shown in Figure 10. 22
- **p. 24 / Figure/Table caption - extractive body cue:** Table 17: Quantitative LfD autonomous agents performance for 4 tasks. Metrics Catch-Release Squat Hammer-Catch Rock-Paper-Scissors (a) Ablation on Data size 25%data
- **p. 21 / Figure/Table caption - extractive body cue:** Table 15: Reward components and weights: penalty rewards for preventing undesired behaviors for sim-to-real transfer, regularization to refine motion, and task reward to achieve successful ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (1 Introduction), p. 8 (1 Introduction), p. 8 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (1 Introduction), objective p. 3 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 1 (Abstract), temporal p. 6 (1 Introduction), p. 5 (1 Introduction), p. 5 (1 Introduction), p. 6 (1 Introduction), p. 7 (1 Introduction), p. 2 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
