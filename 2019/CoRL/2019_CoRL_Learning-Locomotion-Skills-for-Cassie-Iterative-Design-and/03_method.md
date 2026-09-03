# Method - Learning Locomotion Skills for Cassie: Iterative Design and Sim-to-Real

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.cs.ubc.ca/~van/papers/2019-CORL-cassie/index.html; PDF retrieval source: https://arxiv.org/pdf/1903.09537. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (IV. METHODS), p. 3 (IV. METHODS), p. 4 (IV. METHODS), p. 4 (IV. METHODS), p. 6 (VI. POLICY COMPRESSION AND DISTILLATION), p. 6 (VI. POLICY COMPRESSION AND DISTILLATION)): For policies such as walking that produce a limit cycle trajectory, recording the actions of Algorithm 1 DASS 1: Initialize D = {} 2: Reset from some initial state distribution ...

## Method Body Digest

- **p. 3 / IV. METHODS - extractive body cue:** For policies such as walking that produce a limit cycle trajectory, recording the actions of Algorithm 1 DASS 1: Initialize D = {} 2: Reset ...
- **p. 3 / IV. METHODS - extractive body cue:** 2: A walking policy produces a limit cycle, represented by the blue closed curve, and the green arrows indicate the required feedback to return to ...
- **p. 4 / IV. METHODS - extractive body cue:** At each iteration, we will estimate ∇θtJrl using the usual policy gradient algorithm, and update θ according to θt+1 = θt + α(∇θtJrl -w∇θtJsp).
- **p. 4 / IV. METHODS - extractive body cue:** Finally, we can design rewards so that the new policy satisfies additional specific objectives that we desire, such as smoother movement or lifting the feet ...
- **p. 6 / VI. POLICY COMPRESSION AND DISTILLATION - extractive body cue:** Policies Distillation After training a network for a skill, we may want the policy to learn additional skills.
- **p. 6 / VI. POLICY COMPRESSION AND DISTILLATION - extractive body cue:** Policy Compression In deep reinforcement learning, network size often plays an important role in determining the end result [9].
- **p. 5 / VI. POLICY COMPRESSION AND DISTILLATION - extractive body cue:** We stop the training when the training error
- **p. 3 / IV. METHODS - extractive body cue:** Data Collection If we assume πe(. / s) and πθ(. / s) are Gaussian distributions with the same covariance, minimizing the imitation objective function (1) ...

## Design Rationale

- **p. 3 / IV. METHODS - extractive body cue:** In this section, we present our method for collecting stateaction pairs as a dataset for imitation learning, and how this dataset can be used to ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To summarize, this paper makes the following contributions: • We present a simple-yet-effective technique to reconstruct policies from only a small number of samples, and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we propose a DRL design process that reflects and supports the iterative nature of control policy design.

## Source Evidence Cues

- **p. 3 / IV. METHODS - extractive body cue:** For policies such as walking that produce a limit cycle trajectory, recording the actions of Algorithm 1 DASS 1: Initialize D = {} 2: Reset ...
- **p. 3 / IV. METHODS - extractive body cue:** 2: A walking policy produces a limit cycle, represented by the blue closed curve, and the green arrows indicate the required feedback to return to ...
- **p. 4 / IV. METHODS - extractive body cue:** At each iteration, we will estimate ∇θtJrl using the usual policy gradient algorithm, and update θ according to θt+1 = θt + α(∇θtJrl -w∇θtJsp).
- **p. 4 / IV. METHODS - extractive body cue:** Finally, we can design rewards so that the new policy satisfies additional specific objectives that we desire, such as smoother movement or lifting the feet ...
- **p. 6 / VI. POLICY COMPRESSION AND DISTILLATION - extractive body cue:** Policies Distillation After training a network for a skill, we may want the policy to learn additional skills.
- **p. 6 / VI. POLICY COMPRESSION AND DISTILLATION - extractive body cue:** Policy Compression In deep reinforcement learning, network size often plays an important role in determining the end result [9].
- **p. 5 / VI. POLICY COMPRESSION AND DISTILLATION - extractive body cue:** We stop the training when the training error
- **Detected method headings:** IV. METHODS (p. 3); VI. POLICY COMPRESSION AND DISTILLATION (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Command / terrain state | body state와 terrain/task context를 표현한다 | proprioception, terrain/perception, velocity command | history encoder, reference, terrain latent 또는 behavior mode를 구성 | locomotion context | For policies such as walking that produce a limit cycle trajectory, recording the actions of Algorithm 1 DASS 1: Initialize D = ... | p. 3 (IV. METHODS), p. 3 (IV. METHODS) |
| Whole-body policy / controller | context에서 joint target 또는 torque를 만든다 | context, body state, contact | RL policy, reference tracking, inverse dynamics 또는 whole-body control을 적용 | joint action/torque | 2: A walking policy produces a limit cycle, represented by the blue closed curve, and the green arrows indicate the required feedback ... | p. 3 (IV. METHODS), p. 4 (IV. METHODS) |
| Adaptation / recovery | disturbance와 contact mismatch에 대응한다 | new observation/history와 failure signal | latent adaptation, foothold change, recovery 또는 replan을 수행 | updated command | At each iteration, we will estimate ∇θtJrl using the usual policy gradient algorithm, and update θ according to θt+1 = θt + ... | p. 4 (IV. METHODS), p. 4 (IV. METHODS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / IV. METHODS - extractive body cue:** Data Collection If we assume πe(. / s) and πθ(. / s) are Gaussian distributions with the same covariance, minimizing the imitation objective function (1) ...
- **p. 4 / IV. METHODS - extractive body cue:** Finally, we can design rewards so that the new policy satisfies additional specific objectives that we desire, such as smoother movement or lifting the feet ...
- **p. 4 / IV. METHODS - extractive body cue:** original formulation of the reinforcement learning problem: max θ Jrl(θ) =E " ∞ X t=0 γtr(st, at) # subject to st+1 ∼P(. / st, at) ...
- **p. 5 / VI. POLICY COMPRESSION AND DISTILLATION - extractive body cue:** In the experiment, we update the student policies using ADAM [16] with the supervised loss from Equation 2 with a batch size of 128.
- **p. 3 / IV. METHODS - extractive body cue:** To achieve this goal, we will add a constraint in the
- **Formal bridge:** body/proprioceptive/terrain state -> joint action/torque/footstep -> return, tracking or stability objective -> progress, balance and terrain robustness.
- **Equation/algorithm anchors:** p. 4 (IV. METHODS), p. 5 (VI. POLICY COMPRESSION AND DISTILLATION), p. 4 (IV. METHODS), p. 3 (IV. METHODS), p. 3 (IV. METHODS).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | where, blue, curves, represent, limit, cycle, produced, deterministic, policy, green, arrows, feedback, actions, associated | proprioception, terrain/perception observation과 velocity command | body cue; exact tensor/frame verify |
| State/latent | where, blue, curves, represent, limit, cycle, produced, deterministic, policy, green | body/contact state, foothold 또는 behavior mode | body cue; notation verify |
| Action/output | section, present, collecting, stateaction, pairs, dataset, imitation, learning, combine, reinforcement | joint target, torque, footstep 또는 locomotion action | body cue; unit/decoder verify |
| Objective/constraint | Data, Collection, assume, Gaussian, distributions, same, covariance, minimizing, imitation, objective | return, tracking or stability objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / IV. METHODS - extractive body cue:** 2, where the blue curves represent the limit cycle produced by a deterministic policy, and the green arrows represent the deterministic feedback actions associated with ...
- **p. 3 / IV. METHODS - extractive body cue:** 2: A walking policy produces a limit cycle, represented by the blue closed curve, and the green arrows indicate the required feedback to return to ...
- **p. 2 / III. PRELIMINARIES - extractive body cue:** The MDP is defined by a tuple {S, A, P, r, γ}, where S ∈Rn, A ∈Rm are the state space and action space of ...
- **p. 2 / III. PRELIMINARIES - extractive body cue:** The goal of reinforcement learning is to find a policy π, parameterized by θ, where πθ : S × A →[0, ∞) is the probability ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we propose a DRL design process that reflects and supports the iterative nature of control policy design.
- **p. 4 / IV. METHODS - extractive body cue:** The benefit of this is that we don't need access to the expert policy for the fine-tuning to happen.
- **p. 4 / IV. METHODS - extractive body cue:** For example, the expert can be a policy for a robot walking forward while r is rewarding the robot to walk backward.
- **Normalized interface:** observation=proprioception, terrain/perception observation과 velocity command; state=body/contact state, foothold 또는 behavior mode; output/action=joint target, torque, footstep 또는 locomotion action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | gait/skill episode horizon과 short-horizon body control이 계층적으로 분리된다. | [25], where each rollout is started from some states sampled from the reference motions and is terminated when the height of the ... | episode/sequence/action-chunk boundary |
| Rate / latency | high-level command, policy rate와 low-level torque rate를 구분; exact rate 확인 필요. | In our iterative-design framework, we will consider a previously-learned policy as being the expert for the next iteration of policy optimization. | Hz/fps, inference time and control rate |
| Memory | proprioceptive history, terrain latent와 contact/body state. | not recovered | window and reset |
| Compute | policy inference, adaptation encoder와 whole-body/control solve가 latency를 결정한다. | [25], where each rollout is started from some states sampled from the reference motions and is terminated when the height of the ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / VI. POLICY COMPRESSION AND DISTILLATION - extractive body cue:** Policies Distillation After training a network for a skill, we may want the policy to learn additional skills.
- **p. 5 / VI. POLICY COMPRESSION AND DISTILLATION - extractive body cue:** We stop the training when the training error

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** policies, walking, produce, limit, cycle, trajectory, recording, actions, Algorithm, DASS, Initialize, Reset, some, initial, state, distribution, termination, then, Fig, policy.
- **Relevant PDF headings:** IV. METHODS (p. 3); VI. POLICY COMPRESSION AND DISTILLATION (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Command / terrain state | Rapid deployment and testing is aided by the simulator using the same network-based interface as the physical robot, which means that tests ... | p. 5 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP) |
| Whole-body policy / controller | Fig. 5: Network sizes impact the final result for reinforce- ment learning. We observe that larger network sizes typically learn faster and ... | p. 6 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Adaptation / recovery | Fig. 1: Cassie walking on a treadmill with a neural network policy. gradient updates that combine the supervised learning samples and conventional ... | p. 1 (Figure/Table caption), p. 6 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** At each level, all policies are trained from scratch instead of fine-tuning the previous policies.
- **p. 8 / VIII. CONCLUSION AND DISCUSSION - extractive body cue:** The final policies obtained are robust to unmodeled noise and enable us to transfer them from simulation to the physical robot without difficulty.
- **p. 8 / VIII. CONCLUSION AND DISCUSSION - extractive body cue:** We hypothesize the robustness stems from learning stochastic policies that operate at a low control rate, allowing the final policies to adapt to other noise.
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** [25], where each rollout is started from some states sampled from the reference motions and is terminated when the height of the pelvis is less ...
- **p. 4 / V. EXPERIMENTAL SETUP - extractive body cue:** A benefit of the fixed covariance is that because of the noise constantly injected into the system during training, the resulting policy will adapt itself ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Network sizes impact the final result for reinforce- ment learning. We observe that larger network sizes typically learn faster and yield more stable ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: A walking policy produces a limit cycle, represented by the blue closed curve, and the green arrows indicate the required feedback to return ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (IV. METHODS), p. 3 (IV. METHODS), p. 4 (IV. METHODS), p. 4 (IV. METHODS), p. 6 (VI. POLICY COMPRESSION AND DISTILLATION), p. 6 (VI. POLICY COMPRESSION AND DISTILLATION), objective p. 3 (IV. METHODS), p. 4 (IV. METHODS), p. 4 (IV. METHODS), p. 5 (VI. POLICY COMPRESSION AND DISTILLATION), p. 3 (IV. METHODS), temporal p. 5 (V. EXPERIMENTAL SETUP), p. 3 (IV. METHODS), p. 4 (IV. METHODS), p. 4 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP), p. 7 (VII. ITERATIVE DESIGN WITH CHANGING REWARDS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
