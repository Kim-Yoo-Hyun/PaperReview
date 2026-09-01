# Method - Rapid Locomotion via Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss18/p022.html; PDF retrieval source: https://arxiv.org/pdf/2205.02824. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (III. METHOD), p. 3 (III. METHOD), p. 2 (III. METHOD), p. 3 (III. METHOD)): As detailed in Section III-C, the policy πθ(·) takes as input a history of previous observations and actions denoted by ot-H:t where ot = [qt, ˙qt, gori t , at-1].

## Method Body Digest

- **p. 2 / III. METHOD - extractive PDF cue:** As detailed in Section III-C, the policy πθ(·) takes as input a history of previous observations and actions denoted by ot-H:t where ot = [qt, ...
- **p. 3 / III. METHOD - extractive PDF cue:** (hθa) x[t-h:t-1] (42 × 15) [256, 32] zt (8) Body (πθb) xt (42), zt (8) [512, 256, 128] at (12) TABLE II: Network architecture for ...
- **p. 2 / III. METHOD - extractive PDF cue:** Our goal is to learn a policy πθ(.) with parameters θ that takes as input sensory data and velocity commands and gives as output joint ...
- **p. 3 / III. METHOD - extractive PDF cue:** The main idea is that accurately matching the teacher's actions forces the student to implicitly infer domain parameters (dt) from a state history of h ...
- **p. 3 / III. METHOD - extractive PDF cue:** The policy πT (xt, dt), commonly referred to as a teacher policy, is trained using an RL algorithm to maximize the expected sum of rewards.
- **p. 2 / III. METHOD - extractive PDF cue:** Reward Function closely follows [35] with task reward terms for linear and angular velocity tracking, as well as a set of auxiliary terms for stability ...
- **p. 3 / III. METHOD - extractive PDF cue:** The details of the reward function are in Table VI (Appendix).
- **p. 3 / III. METHOD - extractive PDF cue:** The policy is tasked to follow a range of velocity commands that are generated via curriculum strategy described in Section III-D. roll, pitch, height), smoothness ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** RL algorithms * Equal contribution.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** 1: An end-to-end learned controller enables the MIT Mini Cheetah to execute: (a) fast sprinting at 3.9 m/s (top); (b) a rough terrain 10-meter sprint ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** The same policy can spin the robot at 5.7 rad/s on flat ground and also enables the robot to spin on the more challenging icy ...

## Source Evidence Cues

- **p. 2 / III. METHOD - extractive PDF cue:** As detailed in Section III-C, the policy πθ(·) takes as input a history of previous observations and actions denoted by ot-H:t where ot = [qt, ...
- **p. 3 / III. METHOD - extractive PDF cue:** (hθa) x[t-h:t-1] (42 × 15) [256, 32] zt (8) Body (πθb) xt (42), zt (8) [512, 256, 128] at (12) TABLE II: Network architecture for ...
- **p. 2 / III. METHOD - extractive PDF cue:** Our goal is to learn a policy πθ(.) with parameters θ that takes as input sensory data and velocity commands and gives as output joint ...
- **p. 3 / III. METHOD - extractive PDF cue:** The main idea is that accurately matching the teacher's actions forces the student to implicitly infer domain parameters (dt) from a state history of h ...
- **Detected method headings:** III. METHOD (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Command / terrain state | body state와 terrain/task context를 표현한다 | proprioception, terrain/perception, velocity command | history encoder, reference, terrain latent 또는 behavior mode를 구성 | locomotion context | As detailed in Section III-C, the policy πθ(·) takes as input a history of previous observations and actions denoted by ot-H:t where ... | p. 2 (III. METHOD), p. 3 (III. METHOD) |
| Whole-body policy / controller | context에서 joint target 또는 torque를 만든다 | context, body state, contact | RL policy, reference tracking, inverse dynamics 또는 whole-body control을 적용 | joint action/torque | (hθa) x[t-h:t-1] (42 × 15) [256, 32] zt (8) Body (πθb) xt (42), zt (8) [512, 256, 128] at (12) TABLE II: ... | p. 3 (III. METHOD), p. 2 (III. METHOD) |
| Adaptation / recovery | disturbance와 contact mismatch에 대응한다 | new observation/history와 failure signal | latent adaptation, foothold change, recovery 또는 replan을 수행 | updated command | Our goal is to learn a policy πθ(.) with parameters θ that takes as input sensory data and velocity commands and gives ... | p. 2 (III. METHOD), p. 3 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. METHOD - extractive PDF cue:** The policy πT (xt, dt), commonly referred to as a teacher policy, is trained using an RL algorithm to maximize the expected sum of rewards.
- **p. 2 / III. METHOD - extractive PDF cue:** Reward Function closely follows [35] with task reward terms for linear and angular velocity tracking, as well as a set of auxiliary terms for stability ...
- **p. 3 / III. METHOD - extractive PDF cue:** The details of the reward function are in Table VI (Appendix).
- **Formal bridge:** body/proprioceptive/terrain state -> joint action/torque/footstep -> return, tracking or stability objective -> progress, balance and terrain robustness.
- **Equation/algorithm anchors:** p. 3 (III. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | goal, learn, policy, parameters, takes, input, sensory, data, velocity, commands, gives, output, joint, position | proprioception, terrain/perception observation과 velocity command | body cue; exact tensor/frame verify |
| State/latent | goal, learn, policy, parameters, takes, input, sensory, data, velocity, commands | body/contact state, foothold 또는 behavior mode | body cue; notation verify |
| Action/output | algorithms, Equal, contribution, end-to-end, learned, controller, enables, MIT, Mini, Cheetah | joint target, torque, footstep 또는 locomotion action | body cue; unit/decoder verify |
| Objective/constraint | policy, commonly, referred, teacher, trained, algorithm, maximize, expected, rewards, Reward | return, tracking or stability objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / III. METHOD - extractive PDF cue:** Our goal is to learn a policy πθ(.) with parameters θ that takes as input sensory data and velocity commands and gives as output joint ...
- **p. 2 / III. METHOD - extractive PDF cue:** As detailed in Section III-C, the policy πθ(·) takes as input a history of previous observations and actions denoted by ot-H:t where ot = [qt, ...
- **p. 3 / III. METHOD - extractive PDF cue:** The policy is tasked to follow a range of velocity commands that are generated via curriculum strategy described in Section III-D. roll, pitch, height), smoothness ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** An alternative is to amortize the cost of trajectory optimization by learning a direct mapping from sensory observations to actions (a policy) using high-reward trajectories ...
- **p. 3 / III. METHOD - extractive PDF cue:** The main idea is that accurately matching the teacher's actions forces the student to implicitly infer domain parameters (dt) from a state history of h ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Reinforcement learning (RL) provides a way to learn such a policy.
- **Normalized interface:** observation=proprioception, terrain/perception observation과 velocity command; state=body/contact state, foothold 또는 behavior mode; output/action=joint target, torque, footstep 또는 locomotion action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | gait/skill episode horizon과 short-horizon body control이 계층적으로 분리된다. | The main idea is that accurately matching the teacher's actions forces the student to implicitly infer domain parameters (dt) from a state ... | episode/sequence/action-chunk boundary |
| Rate / latency | high-level command, policy rate와 low-level torque rate를 구분; exact rate 확인 필요. | We collect 400 million simulated timesteps using 4000 parallel agents for policy training. | Hz/fps, inference time and control rate |
| Memory | proprioceptive history, terrain latent와 contact/body state. | The main idea is that accurately matching the teacher's actions forces the student to implicitly infer domain parameters (dt) from a state ... | window and reset |
| Compute | policy inference, adaptation encoder와 whole-body/control solve가 latency를 결정한다. | Our neural network controller runs at 50 Hz on an onboard NVIDIA Jetson TX2 NX computer. | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** detailed, Section, III-C, policy, takes, input, history, previous, observations, actions, denoted, ot-H, where, gori, at-1, Body, TABLE, Network, architecture, encoder.
- **Relevant PDF headings:** III. METHOD (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Command / terrain state | The maximum attainable speed is intimately tied to the robot's hardware properties, such as its weight, motor strength, and leg length. | p. 6 (IV. RESULTS), p. 7 (IV. RESULTS) |
| Whole-body policy / controller | Unlike our learned controller, the baseline did not recover from (1) slipping down the gravelly incline and (4) tripping over the barrier. | p. 7 (IV. RESULTS), p. 6 (IV. RESULTS) |
| Adaptation / recovery | The performance of the system is improved substantially by implementing the Box Curriculum. | p. 6 (IV. RESULTS), p. 6 (IV. RESULTS) |

## Failure and Ablation Link

- **p. 6 / IV. RESULTS - extractive PDF cue:** We observe that the policy trained without any curriculum fails to learn.
- **p. 6 / IV. RESULTS - extractive PDF cue:** The results reveal that online system identification leads to better tracking of the velocity command of 6.0 m/s in simulation (speed of 5.46 m/s with ...
- **p. 7 / IV. RESULTS - extractive PDF cue:** Ablation Studies 1) Impact of Online System Identification: System identification can become both more critical and more challenging as locomotion speed increases; this has been ...
- **p. 8 / VI. DISCUSSION - extractive PDF cue:** Our system also does not use vision, so in general, it cannot perform tasks that require planning ahead of time, like efficiently ascending stairs or ...
- **p. 8 / VI. DISCUSSION - extractive PDF cue:** We cannot use motion capture to record the robot's state outdoors as we do in the lab.
- **p. 7 / IV. RESULTS - extractive PDF cue:** Response to Terrain Changes and Hardware Failures We tested our system in a diverse set of challenging real-world scenarios: (1) ascending a steep incline made ...
- **p. 7 / IV. RESULTS - extractive PDF cue:** While these results highlight the robustness of policies, we want to emphasize that we are not claiming that such (or even more) robustness cannot be ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (III. METHOD), p. 3 (III. METHOD), p. 2 (III. METHOD), p. 3 (III. METHOD), objective p. 3 (III. METHOD), p. 2 (III. METHOD), p. 3 (III. METHOD), temporal p. 3 (III. METHOD), p. 2 (II. EXPERIMENTAL SETUP), p. 2 (II. EXPERIMENTAL SETUP), p. 3 (III. METHOD), p. 4 (1) Teacher), p. 1 (I. INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
