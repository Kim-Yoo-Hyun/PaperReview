# Method - RMA: Rapid Motor Adaptation for Legged Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2107.04034; PDF retrieval source: https://arxiv.org/pdf/2107.04034. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (10 Hz), p. 2 (10 Hz), p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 4 (III. RAPID MOTOR ADAPTATION), p. 5 (B. Adaptation Module)): In the first phase, the base policy π takes as input the current state xt, previous action at-1 and the privileged environmental factors et which is encoded into the latent ...

## Method Body Digest

- **p. 2 / 10 Hz - extractive body cue:** In the first phase, the base policy π takes as input the current state xt, previous action at-1 and the privileged environmental factors et which ...
- **p. 2 / 10 Hz - extractive body cue:** The environment configuration vector et is first encoded into a latent feature space zt using an encoder network µ.
- **p. 1 / Abstract - extractive body cue:** RMA consists of two components: a base policy and an adaptation module.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This transfer has proven quite challenging, because the sim-to-real gap itself is the result of multiple factors: (a) the physical robot and its model in ...
- **p. 4 / III. RAPID MOTOR ADAPTATION - extractive body cue:** We jointly train the base policy π and the environmental factor encoder µ end to end using model-free reinforcement learning.
- **p. 5 / B. Adaptation Module - extractive body cue:** To train the adaptation module, we just need the state-action history and the target value of zt (given by the environmental factor encoder µ).
- **p. 5 / B. Adaptation Module - extractive body cue:** Alternately, we could have trained a base policy which directly takes the state and action history as input without decoupling them into the two modules.
- **p. 4 / III. RAPID MOTOR ADAPTATION - extractive body cue:** First, the reward function is motivated from bioenergetic constraints of minimizing work and ground impact [42].

## Design Rationale

- **p. 1 / Abstract - extractive body cue:** The combination of these components enables the robot to adapt to novel situations in fractions of a second.
- **p. 1 / Abstract - extractive body cue:** RMA consists of two components: a base policy and an adaptation module.
- **p. 2 / 10 Hz - extractive body cue:** If we introduce the quadruped onto a rocky surface with no prior experience, the robot policy would fail often, causing serious damage to the robot.

## Source Evidence Cues

- **p. 2 / 10 Hz - extractive body cue:** In the first phase, the base policy π takes as input the current state xt, previous action at-1 and the privileged environmental factors et which ...
- **p. 2 / 10 Hz - extractive body cue:** The environment configuration vector et is first encoded into a latent feature space zt using an encoder network µ.
- **p. 1 / Abstract - extractive body cue:** RMA consists of two components: a base policy and an adaptation module.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This transfer has proven quite challenging, because the sim-to-real gap itself is the result of multiple factors: (a) the physical robot and its model in ...
- **p. 4 / III. RAPID MOTOR ADAPTATION - extractive body cue:** We jointly train the base policy π and the environmental factor encoder µ end to end using model-free reinforcement learning.
- **p. 5 / B. Adaptation Module - extractive body cue:** To train the adaptation module, we just need the state-action history and the target value of zt (given by the environmental factor encoder µ).
- **p. 5 / B. Adaptation Module - extractive body cue:** Alternately, we could have trained a base policy which directly takes the state and action history as input without decoupling them into the two modules.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Command / terrain state | body state와 terrain/task context를 표현한다 | proprioception, terrain/perception, velocity command | history encoder, reference, terrain latent 또는 behavior mode를 구성 | locomotion context | In the first phase, the base policy π takes as input the current state xt, previous action at-1 and the privileged environmental ... | p. 2 (10 Hz), p. 2 (10 Hz) |
| Whole-body policy / controller | context에서 joint target 또는 torque를 만든다 | context, body state, contact | RL policy, reference tracking, inverse dynamics 또는 whole-body control을 적용 | joint action/torque | The environment configuration vector et is first encoded into a latent feature space zt using an encoder network µ. | p. 2 (10 Hz), p. 1 (Abstract) |
| Adaptation / recovery | disturbance와 contact mismatch에 대응한다 | new observation/history와 failure signal | latent adaptation, foothold change, recovery 또는 replan을 수행 | updated command | RMA consists of two components: a base policy and an adaptation module. | p. 1 (Abstract), p. 1 (I. INTRODUCTION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / III. RAPID MOTOR ADAPTATION - extractive body cue:** First, the reward function is motivated from bioenergetic constraints of minimizing work and ground impact [42].
- **p. 4 / III. RAPID MOTOR ADAPTATION - extractive body cue:** RL maximizes the following expected return of the policy π: J(π) = Eτ∼p(τ/π) " T -1 X t=0 γtrt # , where τ = {(x0, ...
- **p. 1 / Abstract - extractive body cue:** We train RMA on a varied terrain generator using bioenergetics-inspired rewards and deploy it on a variety of difficult terrains including rocky, slippery, deformable surfaces ...
- **p. 2 / 10 Hz - extractive body cue:** This asynchronous design was critical for seamless deployment on low-cost robots like A1 with limited on-board compute.
- **p. 3 / 10 Hz - extractive body cue:** Our novel aspects are the use of a varied terrain generator and "natural" reward functions motivated by bioenergetics which allows us to learn walking policies ...
- **p. 5 / B. Adaptation Module - extractive body cue:** Both of these are available in simulation, and hence, φ can be trained via supervised learning to minimize: MSE( ˆzt, zt) = ∥ˆzt -zt∥2, where ...
- **Formal bridge:** body/proprioceptive/terrain state -> joint action/torque/footstep -> return, tracking or stability objective -> progress, balance and terrain robustness.
- **Equation/algorithm anchors:** p. 4 (III. RAPID MOTOR ADAPTATION), p. 4 (III. RAPID MOTOR ADAPTATION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | first, phase, base, policy, takes, input, current, state, previous, action, at-1, privileged, environmental, factors | proprioception, terrain/perception observation과 velocity command | body cue; exact tensor/frame verify |
| State/latent | first, phase, base, policy, takes, input, current, state, previous, action | body/contact state, foothold 또는 behavior mode | body cue; notation verify |
| Action/output | combination, components, enables, robot, adapt, novel, situations, fractions, second, RMA | joint target, torque, footstep 또는 locomotion action | body cue; unit/decoder verify |
| Objective/constraint | First, reward, function, motivated, bioenergetic, constraints, minimizing, ground, impact, maximizes | return, tracking or stability objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 10 Hz - extractive body cue:** In the first phase, the base policy π takes as input the current state xt, previous action at-1 and the privileged environmental factors et which ...
- **p. 5 / B. Adaptation Module - extractive body cue:** Alternately, we could have trained a base policy which directly takes the state and action history as input without decoupling them into the two modules.
- **p. 2 / 10 Hz - extractive body cue:** This latent vector zt, which we call the extrinsics, is then fed into the base policy along with the current state xt and the previous ...
- **p. 5 / B. Adaptation Module - extractive body cue:** One way to collect the state-action history is to unroll the trained base policy π with the ground truth zt.
- **p. 3 / 10 Hz - extractive body cue:** Specifically, the goal of φ is to estimate the extrinsics vector zt from the robot's recent state and action history, without assuming any access to ...
- **p. 4 / III. RAPID MOTOR ADAPTATION - extractive body cue:** We additionally define the joint angles as q, joint velocities as ˙q, joint torques as τ, ground reaction forces at the feet as f, velocity ...
- **p. 3 / 10 Hz - extractive body cue:** The base policy just uploads the most recent prediction of the extrinsics vector zt from the adaptation module to predict action at.
- **Normalized interface:** observation=proprioception, terrain/perception observation과 velocity command; state=body/contact state, foothold 또는 behavior mode; output/action=joint target, torque, footstep 또는 locomotion action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | gait/skill episode horizon과 short-horizon body control이 계층적으로 분리된다. | The control frequency of the policy is 100 Hz, and the simulation time step is 0.025s. | episode/sequence/action-chunk boundary |
| Rate / latency | high-level command, policy rate와 low-level torque rate를 구분; exact rate 확인 필요. | The adaptation policy is slow because it operates on the state-action history of 50 time steps, roughly updating the extrinsic vector ˆzt ... | Hz/fps, inference time and control rate |
| Memory | proprioceptive history, terrain latent와 contact/body state. | The adaptation policy is slow because it operates on the state-action history of 50 time steps, roughly updating the extrinsic vector ˆzt ... | window and reset |
| Compute | policy inference, adaptation encoder와 whole-body/control solve가 latency를 결정한다. | The control frequency of the policy is 100 Hz, and the simulation time step is 0.025s. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / III. RAPID MOTOR ADAPTATION - extractive body cue:** We jointly train the base policy π and the environmental factor encoder µ end to end using model-free reinforcement learning.
- **p. 5 / B. Adaptation Module - extractive body cue:** To train the adaptation module, we just need the state-action history and the target value of zt (given by the environmental factor encoder µ).
- **p. 5 / B. Adaptation Module - extractive body cue:** Alternately, we could have trained a base policy which directly takes the state and action history as input without decoupling them into the two modules.
- **p. 6 / IV. EXPERIMENTAL SETUP - extractive body cue:** Learning Base Policy and Environmental Factor Encoder Network: We jointly train the base policy and the environment encoder network using PPO [48] for 15, 000 ...
- **p. 3 / 10 Hz - extractive body cue:** That is at runtime, but at training time, life is easier.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** first, phase, base, policy, takes, input, current, state, previous, action, at-1, privileged, environmental, factors, encoded, latent, extrinsics, vector, factor, encoder.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Command / terrain state | Environment Details Hardware Details: We use A1 robot from Unitree for all our real-world experiments. | p. 5 (IV. EXPERIMENTAL SETUP), p. 5 (IV. EXPERIMENTAL SETUP) |
| Whole-body policy / controller | Overall, the proposed method consistently dominates the baseline methods. | p. 6 (IV. EXPERIMENTAL SETUP), p. 7 (V. RESULTS AND ANALYSIS) |
| Adaptation / recovery | Fig. 1: We demonstrate the performance of RMA on several challenging environments. The robot is successfully able to walk on sand, mud, ... | p. 1 (Figure/Table caption), p. 6 (IV. EXPERIMENTAL SETUP) |

## Failure and Ablation Link

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We demonstrate the performance of RMA on several challenging environments. The robot is successfully able to walk on sand, mud, hiking trails, tall ...
- **p. 6 / IV. EXPERIMENTAL SETUP - extractive body cue:** We compare RMA to A1's controller and RMA without the adaptation module.
- **p. 7 / V. RESULTS AND ANALYSIS - extractive body cue:** 2) Robustness through Domain Randomization (Robust): The base policy is trained without zt to be robust to the variations in the training range [52, 40].
- **p. 7 / V. RESULTS AND ANALYSIS - extractive body cue:** 4) RMA w/o Adaptation: We can also evaluate the performance of the base policy without the adaptation module to ablate the importance of the adaptation ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We demonstrate the performance of RMA on several challenging environments. The robot is successfully able to walk on sand, mud, hiking trails, tall ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: We evaluate RMA in several out-of-distribution setups in the real world. We compare RMA to A1's controller and RMA without the adaptation module. ...
- **p. 8 / 6) Advantage Weighted Regression for Domain Adaptation - extractive body cue:** The controller was destabilized by unstable footholds in most of its failures.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (10 Hz), p. 2 (10 Hz), p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 4 (III. RAPID MOTOR ADAPTATION), p. 5 (B. Adaptation Module), objective p. 4 (III. RAPID MOTOR ADAPTATION), p. 4 (III. RAPID MOTOR ADAPTATION), p. 1 (Abstract), p. 2 (10 Hz), p. 3 (10 Hz), p. 5 (B. Adaptation Module), temporal p. 5 (IV. EXPERIMENTAL SETUP), p. 5 (B. Adaptation Module), p. 6 (IV. EXPERIMENTAL SETUP), p. 4 (III. RAPID MOTOR ADAPTATION), p. 1 (Abstract), p. 6 (IV. EXPERIMENTAL SETUP).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** In the first phase, the base policy π takes as input the current state xt, previous action at-1 and the privileged environmental factors et which is encoded into the latent ... (p. 2, 10 Hz).
- **Objective/update evidence:** First, the reward function is motivated from bioenergetic constraints of minimizing work and ground impact [42]. (p. 4, III. RAPID MOTOR ADAPTATION).
- **Temporal/runtime evidence:** The control frequency of the policy is 100 Hz, and the simulation time step is 0.025s. (p. 5, IV. EXPERIMENTAL SETUP).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
