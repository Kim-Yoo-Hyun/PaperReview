# Method - Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v205/margolis23a.html; PDF retrieval source: https://arxiv.org/pdf/2212.03238. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3 Method), p. 6 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 8 (3 Method), p. 7 (3 Method)): The observation space ot consists of joint positions and velocities qt, ˙qt (measured by joint encoders) and the gravity vector in the body frame gt (measured by accelerometer).

## Method Body Digest

- **p. 5 / 3 Method - extractive body cue:** The observation space ot consists of joint positions and velocities qt, ˙qt (measured by joint encoders) and the gravity vector in the body frame gt ...
- **p. 6 / 3 Method - extractive body cue:** 4 Experimental Results 4.1 Sim-to-Real Transfer and Gait Switching We deploy the controller learned in simulation in the real world and first evaluate its performance ...
- **p. 5 / 3 Method - extractive body cue:** The action at consists of position targets for each of the twelve joints.
- **p. 6 / 3 Method - extractive body cue:** After training using a generic locomotion objective, one might wish to tune a controller's behavior to optimize a new metric in the original environment.
- **p. 8 / 3 Method - extractive body cue:** MoB confers a single learned policy a structured and controllable space of diverse locomotion behaviors for each state and task in the training distribution.
- **p. 7 / 3 Method - extractive body cue:** In the real world, there is also always a long tail of environments that are not modeled in training.
- **p. 7 / 3 Method - extractive body cue:** Hacking through thick bushes: Extremely thick bushes pose a methodological challenge for state-ofthe-art perceptive locomotion controllers.
- **p. 5 / 3 Method - extractive body cue:** This way, the agent is always rewarded for progress towards the task, more when auxiliary objectives are satisfied and less when they are not.

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** We present a framework for policy learning that enables improved performance in out-of-distribution scenarios under some assumptions detailed below.
- **p. 2 / 1 Introduction - extractive body cue:** To facilitate generalization to diverse scenarios, we propose a technique, Multiplicity of Behavior (MoB), that given the same observation history and a small set of ...
- **p. 5 / 3 Method - extractive body cue:** The action at consists of position targets for each of the twelve joints.

## Source Evidence Cues

- **p. 5 / 3 Method - extractive body cue:** The observation space ot consists of joint positions and velocities qt, ˙qt (measured by joint encoders) and the gravity vector in the body frame gt ...
- **p. 6 / 3 Method - extractive body cue:** 4 Experimental Results 4.1 Sim-to-Real Transfer and Gait Switching We deploy the controller learned in simulation in the real world and first evaluate its performance ...
- **p. 5 / 3 Method - extractive body cue:** The action at consists of position targets for each of the twelve joints.
- **p. 6 / 3 Method - extractive body cue:** After training using a generic locomotion objective, one might wish to tune a controller's behavior to optimize a new metric in the original environment.
- **p. 8 / 3 Method - extractive body cue:** MoB confers a single learned policy a structured and controllable space of diverse locomotion behaviors for each state and task in the training distribution.
- **p. 7 / 3 Method - extractive body cue:** In the real world, there is also always a long tail of environments that are not modeled in training.
- **p. 7 / 3 Method - extractive body cue:** Hacking through thick bushes: Extremely thick bushes pose a methodological challenge for state-ofthe-art perceptive locomotion controllers.
- **Detected method headings:** 3 Method (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Command / terrain state | body state와 terrain/task context를 표현한다 | proprioception, terrain/perception, velocity command | history encoder, reference, terrain latent 또는 behavior mode를 구성 | locomotion context | The observation space ot consists of joint positions and velocities qt, ˙qt (measured by joint encoders) and the gravity vector in the ... | p. 5 (3 Method), p. 6 (3 Method) |
| Whole-body policy / controller | context에서 joint target 또는 torque를 만든다 | context, body state, contact | RL policy, reference tracking, inverse dynamics 또는 whole-body control을 적용 | joint action/torque | 4 Experimental Results 4.1 Sim-to-Real Transfer and Gait Switching We deploy the controller learned in simulation in the real world and first ... | p. 6 (3 Method), p. 5 (3 Method) |
| Adaptation / recovery | disturbance와 contact mismatch에 대응한다 | new observation/history와 failure signal | latent adaptation, foothold change, recovery 또는 replan을 수행 | updated command | The action at consists of position targets for each of the twelve joints. | p. 5 (3 Method), p. 6 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3 Method - extractive body cue:** This way, the agent is always rewarded for progress towards the task, more when auxiliary objectives are satisfied and less when they are not.
- **p. 5 / 3 Method - extractive body cue:** During training, one concern is that the robot might abandon its task or choose an early termination when the task reward is overwhelmed by penalties ...
- **p. 6 / 3 Method - extractive body cue:** After training using a generic locomotion objective, one might wish to tune a controller's behavior to optimize a new metric in the original environment.
- **p. 4 / 3 Method - extractive body cue:** All reward terms are listed in Table 1.
- **p. 4 / 3 Method - extractive body cue:** Auxiliary rewards are used constrain the 4
- **p. 6 / 3 Method - extractive body cue:** The gait-free baseline is trained by the method above, but excludes all augmented auxiliary rewards (Table 1).
- **Formal bridge:** body/proprioceptive/terrain state -> joint action/torque/footstep -> return, tracking or stability objective -> progress, balance and terrain robustness.
- **Equation/algorithm anchors:** p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 7 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | input, policy, step, history, observations, ot-H, commands, ct-H, behaviors, bt-H, previous, actions, at-H-1, timing | proprioception, terrain/perception observation과 velocity command | body cue; exact tensor/frame verify |
| State/latent | input, policy, step, history, observations, ot-H, commands, ct-H, behaviors, bt-H | body/contact state, foothold 또는 behavior mode | body cue; notation verify |
| Action/output | present, framework, policy, learning, enables, improved, performance, out-of-distribution, scenarios, under | joint target, torque, footstep 또는 locomotion action | body cue; unit/decoder verify |
| Objective/constraint | agent, always, rewarded, progress, towards, task, more, when, auxiliary, objectives | return, tracking or stability objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3 Method - extractive body cue:** The input to the policy is a 30-step history of observations ot-H...t, commands ct-H...t, behaviors bt-H...t, previous actions at-H-1...t-1, and timing reference variables tt-H...t.
- **p. 5 / 3 Method - extractive body cue:** Besides the above, the policy input also includes estimated domain parameters: the velocity of the robot body and the ground friction, which are predicted from ...
- **p. 2 / 1 Introduction - extractive body cue:** To facilitate generalization to diverse scenarios, we propose a technique, Multiplicity of Behavior (MoB), that given the same observation history and a small set of ...
- **p. 4 / 3 Method - extractive body cue:** During deployment in a novel environment, a human operator can tune behavior of the policy by changing its input bt.
- **p. 8 / 3 Method - extractive body cue:** MoB confers a single learned policy a structured and controllable space of diverse locomotion behaviors for each state and task in the training distribution.
- **p. 6 / 3 Method - extractive body cue:** We implement an interface based on Lightweight Communications and Marshalling (LCM) [28] to pass sensor data, motor commands, and joystick state between our code and ...
- **p. 4 / 3 Method - extractive body cue:** To obtain MoB, we train a conditional policy π(·/ct, bt) that achieves tasks specified by the command (ct) in multiple ways that result from different ...
- **Normalized interface:** observation=proprioception, terrain/perception observation과 velocity command; state=body/contact state, foothold 또는 behavior mode; output/action=joint target, torque, footstep 또는 locomotion action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | gait/skill episode horizon과 short-horizon body control이 계층적으로 분리된다. | Taken together, the parameters θcmd can express all two-beat quadrupedal contact patterns; Figure 2 provides a visual illustration. f cmd is the ... | episode/sequence/action-chunk boundary |
| Rate / latency | high-level command, policy rate와 low-level torque rate를 구분; exact rate 확인 필요. | The robot first accelerates to a target speed of 3 m/s at a trot while increasing its step frequency from 2 Hz ... | Hz/fps, inference time and control rate |
| Memory | proprioceptive history, terrain latent와 contact/body state. | The input to the policy is a 30-step history of observations ot-H...t, commands ct-H...t, behaviors bt-H...t, previous actions at-H-1...t-1, and timing reference ... | window and reset |
| Compute | policy inference, adaptation encoder와 whole-body/control solve가 latency를 결정한다. | The robot first accelerates to a target speed of 3 m/s at a trot while increasing its step frequency from 2 Hz ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3 Method - extractive body cue:** 4 Experimental Results 4.1 Sim-to-Real Transfer and Gait Switching We deploy the controller learned in simulation in the real world and first evaluate its performance ...
- **p. 6 / 3 Method - extractive body cue:** After training using a generic locomotion objective, one might wish to tune a controller's behavior to optimize a new metric in the original environment.
- **p. 8 / 3 Method - extractive body cue:** MoB confers a single learned policy a structured and controllable space of diverse locomotion behaviors for each state and task in the training distribution.
- **p. 7 / 3 Method - extractive body cue:** In the real world, there is also always a long tail of environments that are not modeled in training.
- **p. 6 / 3 Method - extractive body cue:** An onboard Jetson TX2 NX computer runs our trained policy.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** observation, space, consists, joint, positions, velocities, measured, encoders, gravity, vector, body, frame, accelerometer, Experimental, Sim-to-Real, Transfer, Gait, Switching, deploy, controller.
- **Relevant PDF headings:** 3 Method (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Command / terrain state | In a real-world example, the robot was able to crawl under a 22 cm bar; the robot body thickness is 13 cm, ... | p. 8 (3 Method), p. 5 (3 Method) |
| Whole-body policy / controller | Pacing and trotting yield the best survival time in out-of-distribution deployment, outperforming the gait-free baseline. | p. 7 (3 Method), p. 6 (3 Method) |
| Adaptation / recovery | Table 5: Removing gait constraints results in improved velocity tracking task performance on flat ground. Heat maps (right) break down the mean ... | p. 11 (Figure/Table caption), p. 7 (3 Method) |

## Failure and Ablation Link

- **p. 6 / Figure/Table caption - extractive body cue:** Table 3: Behavior tuning enables interventional studies on the relationship between gait proper- ties and performance criteria within a single policy. Here, we illustrate how ...
- **p. 5 / 3 Method - extractive body cue:** As we are interested in studying out-of-distribution generalization, we only train on flat ground without any randomization of terrain geometry.
- **p. 7 / 3 Method - extractive body cue:** In contrast, with the help of a human pilot, our gait-conditioned policy with high footswing command enables fast and smooth obstacle traversal without tripping, despite ...
- **p. 8 / 3 Method - extractive body cue:** This interferes with performance in other tasks like running efficiently, so learned locomotion controllers without MoB often provide incentive to keep the feet nominally below ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 5: Removing gait constraints results in improved velocity tracking task performance on flat ground. Heat maps (right) break down the mean task reward for ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Multiplicity of Behavior (MoB) enables a human to tune a single quadruped policy trained on flat ground to diverse unseen environments. Top row: ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 5. Forward and Backward Locomotion. During evaluation in the random platforms environment, we found that walking backward leads to fewer failures than walking forward. ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3 Method), p. 6 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 8 (3 Method), p. 7 (3 Method), objective p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 4 (3 Method), p. 4 (3 Method), p. 6 (3 Method), temporal p. 4 (3 Method), p. 8 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 8 (3 Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
