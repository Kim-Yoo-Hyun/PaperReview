# Method - Learned Perceptive Forward Dynamics Model for Safe and Platform-aware Robotic Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p001.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p001.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (B. Model Architecture), p. 2 (A. Dynamics Modeling), p. 6 (B. Model Architecture), p. 3 (A. Dynamics Modeling), p. 3 (A. Dynamics Modeling), p. 4 (A. Dynamics Modeling)): The Forward Dynamics Model loss £ consists of supervised terms for network outputs.

## Method Body Digest

- **p. 5 / B. Model Architecture - extractive body cue:** The Forward Dynamics Model loss £ consists of supervised terms for network outputs.
- **p. 2 / A. Dynamics Modeling - extractive body cue:** Lately, world models have emerged, which encode system dynamics in a latent space, enabling policy optimization through imagined rollouts [19 20) Such models can also ...
- **p. 6 / B. Model Architecture - extractive body cue:** The FDM runs onboard using an NVIDIA Jetson Orin AGX, with the planner running at 7 Hz. using 2048 trajectories and a model inference time ...
- **p. 3 / A. Dynamics Modeling - extractive body cue:** To address this, we aim to learn an approximate dynamics model f that predicts a subset of state 5 based on the action a, and ...
- **p. 3 / A. Dynamics Modeling - extractive body cue:** The robot evolves according to a forward dynamics model that maps the current state and action to the next state:
- **p. 4 / A. Dynamics Modeling - extractive body cue:** Consequently, the objective of the dynamics ‘model becomes minimizing a combined loss comprising pose prediction Cyoge and failure risk prediction Lyi
- **p. 2 / A. Dynamics Modeling - extractive body cue:** ‘The field of dynamics learning has predominantly focused oon data-driven solutions [1-4, 7, I1, 12], as models derived from first principles and calibrated via system ...
- **p. 3 / B. Model Predictive Path Integral Control - extractive body cue:** The selection over a set of C' candidates is performed by maximizing 4 reward function defined over the future states 8, and the goal pose ...

## Design Rationale

- **p. 1 / Front matter - extractive body cue:** To overcome these issues, we propose a novel learned perceptive
- **p. 3 / B. Planning - extractive body cue:** Our method addresses domain discrepancies by incorporating real-world data into the ‘dynamics model while maintaining platform awareness through earning from past experiences.
- **p. 5 / B. Model Architecture - extractive body cue:** The Forward Dynamics Model loss £ consists of supervised terms for network outputs.

## Source Evidence Cues

- **p. 5 / B. Model Architecture - extractive body cue:** The Forward Dynamics Model loss £ consists of supervised terms for network outputs.
- **p. 2 / A. Dynamics Modeling - extractive body cue:** Lately, world models have emerged, which encode system dynamics in a latent space, enabling policy optimization through imagined rollouts [19 20) Such models can also ...
- **p. 6 / B. Model Architecture - extractive body cue:** The FDM runs onboard using an NVIDIA Jetson Orin AGX, with the planner running at 7 Hz. using 2048 trajectories and a model inference time ...
- **p. 3 / A. Dynamics Modeling - extractive body cue:** To address this, we aim to learn an approximate dynamics model f that predicts a subset of state 5 based on the action a, and ...
- **p. 3 / A. Dynamics Modeling - extractive body cue:** The robot evolves according to a forward dynamics model that maps the current state and action to the next state:
- **p. 4 / A. Dynamics Modeling - extractive body cue:** Consequently, the objective of the dynamics ‘model becomes minimizing a combined loss comprising pose prediction Cyoge and failure risk prediction Lyi
- **p. 2 / A. Dynamics Modeling - extractive body cue:** ‘The field of dynamics learning has predominantly focused oon data-driven solutions [1-4, 7, I1, 12], as models derived from first principles and calibrated via system ...
- **Detected method headings:** A. Dynamics Modeling (p. 2); A. Dynamics Modeling (p. 3); B. Model Predictive Path Integral Control (p. 3); B. Model Architecture (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Command / terrain state | body state와 terrain/task context를 표현한다 | proprioception, terrain/perception, velocity command | history encoder, reference, terrain latent 또는 behavior mode를 구성 | locomotion context | The Forward Dynamics Model loss £ consists of supervised terms for network outputs. | p. 5 (B. Model Architecture), p. 2 (A. Dynamics Modeling) |
| Whole-body policy / controller | context에서 joint target 또는 torque를 만든다 | context, body state, contact | RL policy, reference tracking, inverse dynamics 또는 whole-body control을 적용 | joint action/torque | Lately, world models have emerged, which encode system dynamics in a latent space, enabling policy optimization through imagined rollouts [19 20) Such ... | p. 2 (A. Dynamics Modeling), p. 6 (B. Model Architecture) |
| Adaptation / recovery | disturbance와 contact mismatch에 대응한다 | new observation/history와 failure signal | latent adaptation, foothold change, recovery 또는 replan을 수행 | updated command | The FDM runs onboard using an NVIDIA Jetson Orin AGX, with the planner running at 7 Hz. using 2048 trajectories and a ... | p. 6 (B. Model Architecture), p. 3 (A. Dynamics Modeling) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / A. Dynamics Modeling - extractive body cue:** Consequently, the objective of the dynamics ‘model becomes minimizing a combined loss comprising pose prediction Cyoge and failure risk prediction Lyi
- **p. 3 / B. Model Predictive Path Integral Control - extractive body cue:** The selection over a set of C' candidates is performed by maximizing 4 reward function defined over the future states 8, and the goal pose ...
- **p. 6 / B. Model Architecture - extractive body cue:** Consequently, the planning reward R can be simplified to a weighted combination of a goal-oriented pose reward Rpose (terminal reward) and a risk minimization term ...
- **p. 3 / B. Model Predictive Path Integral Control - extractive body cue:** These weights are computed based on the reward 7, of each trajectory, ensuring higherreward trajectories contrite more significantly to the update:
- **p. 5 / B. Model Architecture - extractive body cue:** The final loss for model updates becomes a weighted sum of all individual terms:
- **p. 4 / B. Planning - extractive body cue:** 4 with a reward function compromising position error Rose and failure risk Ryiok given the future states generated by the developed FDM jo
- **Formal bridge:** body/proprioceptive/terrain state -> joint action/torque/footstep -> return, tracking or stability objective -> progress, balance and terrain robustness.
- **Equation/algorithm anchors:** p. 4 (A. Dynamics Modeling), p. 5 (B. Model Architecture), p. 4 (B. Planning), p. 5 (B. Model Architecture), p. 3 (B. Model Predictive Path Integral Control), p. 3 (B. Model Predictive Path Integral Control).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | define, state, tuple, where, SE2, robot, pose, failure, risk, trajectory, indicates, risk-free, catastrophic, actions | proprioception, terrain/perception observation과 velocity command | body cue; exact tensor/frame verify |
| State/latent | define, state, tuple, where, SE2, robot, pose, failure, risk, trajectory | body/contact state, foothold 또는 behavior mode | body cue; notation verify |
| Action/output | overcome, issues, novel, learned, perceptive, addresses, domain, discrepancies, incorporating, real-world | joint target, torque, footstep 또는 locomotion action | body cue; unit/decoder verify |
| Objective/constraint | Consequently, objective, dynamics, model, becomes, minimizing, combined, loss, comprising, pose | return, tracking or stability objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / A. Dynamics Modeling - extractive body cue:** We define ihe state ¥ to be the tuple (p,r), where p © SE2 is the robot's pose and r < {0,1} is the failure ...
- **p. 2 / A. Dynamics Modeling - extractive body cue:** Lately, world models have emerged, which encode system dynamics in a latent space, enabling policy optimization through imagined rollouts [19 20) Such models can also ...
- **p. 3 / A. Dynamics Modeling - extractive body cue:** Given the current observation 0 and sequence of actions a = dy,...esn-1 We predict a sequence of future states
- **p. 5 / B. Model Architecture - extractive body cue:** Model Input: As introduced, the model receives as ‘observations a history of m past states 5,..«-n. proprioceptive readings m}""7,, and a height scan' for traversabil
- **p. 5 / B. Model Architecture - extractive body cue:** The flattened output of the latter and the last embedding of the former are used to initialize the hidden state of the forward prediction GRU. ...
- **p. 1 / Front matter - extractive body cue:** The model, trained with real-world and simulation data, predicts the robots future states given a sequence of velocity actions.
- **p. 4 / B. Planning - extractive body cue:** ‘TABLE I: The observation space of the FDM combines proprioceptive information of the robot state m2" and the joint states m?""* with exteroceptive measurements h. ...
- **Normalized interface:** observation=proprioception, terrain/perception observation과 velocity command; state=body/contact state, foothold 또는 behavior mode; output/action=joint target, torque, footstep 또는 locomotion action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | gait/skill episode horizon과 short-horizon body control이 계층적으로 분리된다. | The future states are collected from the following m states with a frequency of 1/AV,, resulting in 4 prediction horizon of n ... | episode/sequence/action-chunk boundary |
| Rate / latency | high-level command, policy rate와 low-level torque rate를 구분; exact rate 확인 필요. | 1, we illustrate a long-range traversed path, where the goal positions are projected onto the robot's perception range at each time step. | Hz/fps, inference time and control rate |
| Memory | proprioceptive history, terrain latent와 contact/body state. | The future states are collected from the following m states with a frequency of 1/AV,, resulting in 4 prediction horizon of n ... | window and reset |
| Compute | policy inference, adaptation encoder와 whole-body/control solve가 latency를 결정한다. | Across 15 rounds, each collecting 80k samples from 10k parallel environments, updates consist of 8 episodes with a batch sizeof 2048, optimized ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / A. Dynamics Modeling - extractive body cue:** Lately, world models have emerged, which encode system dynamics in a latent space, enabling policy optimization through imagined rollouts [19 20) Such models can also ...
- **p. 6 / B. Model Architecture - extractive body cue:** The FDM runs onboard using an NVIDIA Jetson Orin AGX, with the planner running at 7 Hz. using 2048 trajectories and a model inference time ...
- **p. 6 / B. Model Architecture - extractive body cue:** The FDM runs onboard using an NVIDIA Jetson Orin AGX, with the planner running at 7 Hz. using 2048 trajectories and a model inference time ...
- **p. 7 / B. Model Architecture - extractive body cue:** In later stages, real-world data is integrated with synthetic data, and weights are refined using a small, constant learning rate to capture the full system ...
- **p. 2 / A. Dynamics Modeling - extractive body cue:** Lately, world models have emerged, which encode system dynamics in a latent space, enabling policy optimization through imagined rollouts [19 20) Such models can also ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Forward, Dynamics, Model, loss, consists, supervised, terms, network, outputs, Lately, world, models, have, emerged, encode, system, latent, space, enabling, policy.
- **Relevant PDF headings:** A. Dynamics Modeling (p. 2); A. Dynamics Modeling (p. 3); B. Model Predictive Path Integral Control (p. 3); B. Model Architecture (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Command / terrain state | Second, the failure states observed in simulation environments do not perfectly translate to real-world failures, and real-world data lacks demonstrations. of collisions ... | p. 10 (C. Platform-aware Predictions), p. 10 (C. Platform-aware Predictions) |
| Whole-body policy / controller | Further, the better accuracy compared to the baselines becomes clearly | p. 7 (B. Baseline Comparison), p. 7 (B. Baseline Comparison) |
| Adaptation / recovery | Il, our approach achieves the highest success rate across both environments. | p. 9 (C. Platform-aware Predictions), p. 10 (C. Platform-aware Predictions) |

## Failure and Ablation Link

- **p. 7 / B. Model Architecture - extractive body cue:** Fig, 5: Comparison of the postion error atthe final prediction step in different environments for the presented FDM I, the perceptive FDM by Kim etal ...
- **p. 6 / B. Model Architecture - extractive body cue:** These obstacles cannot be differentiated from walls using only a horizontal 2D sensor without actively changing the observation angle.
- **p. 6 / B. Model Architecture - extractive body cue:** Using a zero-shot MPPI planner allows for adjustments of the planning behavior without retraining, Leveraging the pose and failure risk of the perceptive FDM, there ...
- **p. 7 / B. Model Architecture - extractive body cue:** More details on the sensitivity of learning and planning parameters, alongside discussion of the adaptation required for a new robot platform, ‘can be found in ...
- **p. 9 / C. Platform-aware Predictions - extractive body cue:** The more conservative baseline instead circled around the obstacles, leading to increased path time and length, often without reaching the goal
- **p. 8 / C. Platform-aware Predictions - extractive body cue:** The experiments show that even before the fine-tuning, our FDM performs better than the constant velocity model.
- **p. 9 / C. Platform-aware Predictions - extractive body cue:** In the latter, the failure loss term is replaced by an evaluation of future robot positions on the generated traversability map.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (B. Model Architecture), p. 2 (A. Dynamics Modeling), p. 6 (B. Model Architecture), p. 3 (A. Dynamics Modeling), p. 3 (A. Dynamics Modeling), p. 4 (A. Dynamics Modeling), objective p. 4 (A. Dynamics Modeling), p. 3 (B. Model Predictive Path Integral Control), p. 6 (B. Model Architecture), p. 3 (B. Model Predictive Path Integral Control), p. 5 (B. Model Architecture), p. 4 (B. Planning), temporal p. 5 (V. MeTHopoLoGy), p. 9 (C. Platform-aware Predictions), p. 1 (Front matter), p. 2 (1. Inrropucrion), p. 2 (1. Inrropucrion), p. 3 (B. Model Predictive Path Integral Control).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
