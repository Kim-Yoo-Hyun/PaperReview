# Method - SATA: Safe and Adaptive Torque-Based Locomotion Policies Inspired by Animal Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p124.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p124.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (A. Implementation of the Growth Mechanism), p. 5 (IV. GROWTH-BASED TRAINING), p. 6 (A. Implementation of the Growth Mechanism), p. 6 (A. Implementation of the Growth Mechanism)): Instead of granting the policy full access to the action space from the star of training, we propose that partially limiting the robot's abilities can promote more efficient exploration Additionally, ...

## Method Body Digest

- **p. 5 / A. Implementation of the Growth Mechanism - extractive PDF cue:** Instead of granting the policy full access to the action space from the star of training, we propose that partially limiting the robot's abilities can ...
- **p. 5 / IV. GROWTH-BASED TRAINING - extractive PDF cue:** Due to the highly nonlinear nature of the torque space, training a torque-based policy poses greater challenges than a position-based one, especially during early-stage exploration. ...
- **p. 6 / A. Implementation of the Growth Mechanism - extractive PDF cue:** We utilize Proximal Policy Optimization (PPO) to train the control policy, The hyperparameters and neural network architecture are consistent with [33]. including a multilayer perceptron ...
- **p. 6 / A. Implementation of the Growth Mechanism - extractive PDF cue:** ‘Domain randomization is applied during training to simulate real-world variability. ‘The specific randomization settings are as follows: Added base mass: Randomly increased by up to ...
- **p. 6 / A. Implementation of the Growth Mechanism - extractive PDF cue:** Similarly, G(0) allows the robot to adapt reward priorities to align with specific training objectives.
- **p. 6 / A. Implementation of the Growth Mechanism - extractive PDF cue:** As G(t) evolves, the rewards shift focus from encouraging basic behaviors, such as forward motion, to more complex objectives like maintaining body height and tracking ...
- **p. 5 / IV. GROWTH-BASED TRAINING - extractive PDF cue:** Our strategy also aligns conceptually with reward scheduling techniques, where the learning signal evolves in tandem with the agent's growing capabilities (70, 71].
- **p. 2 / 1. Iyrropuction - extractive PDF cue:** Learning-based controllers typically use position-based action spaces, where the policy directly outputs position com- ‘mands for the actuators. ‘These commands are subsequently converted to torque ...

## Design Rationale

- **p. 2 / 1. Iyrropuction - extractive PDF cue:** + Stable and Efficient Torque-Based Learning: We propose «novel framework for learning torque-based loco- ‘motion policies with a growth mechanism that gradually. unlocks torque limits, ...
- **p. 5 / IV. GROWTH-BASED TRAINING - extractive PDF cue:** Due to the highly nonlinear nature of the torque space, training a torque-based policy poses greater challenges than a position-based one, especially during early-stage exploration. ...
- **p. 2 / 1. Iyrropuction - extractive PDF cue:** By directly controlling actuation in torque space, this approach enables finer interaction with the environment, leading to more dynamic and robust locomotion, Moreover. torque control ...

## Source Evidence Cues

- **p. 5 / A. Implementation of the Growth Mechanism - extractive PDF cue:** Instead of granting the policy full access to the action space from the star of training, we propose that partially limiting the robot's abilities can ...
- **p. 5 / IV. GROWTH-BASED TRAINING - extractive PDF cue:** Due to the highly nonlinear nature of the torque space, training a torque-based policy poses greater challenges than a position-based one, especially during early-stage exploration. ...
- **p. 6 / A. Implementation of the Growth Mechanism - extractive PDF cue:** We utilize Proximal Policy Optimization (PPO) to train the control policy, The hyperparameters and neural network architecture are consistent with [33]. including a multilayer perceptron ...
- **p. 6 / A. Implementation of the Growth Mechanism - extractive PDF cue:** ‘Domain randomization is applied during training to simulate real-world variability. ‘The specific randomization settings are as follows: Added base mass: Randomly increased by up to ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Command / terrain state | body state와 terrain/task context를 표현한다 | proprioception, terrain/perception, velocity command | history encoder, reference, terrain latent 또는 behavior mode를 구성 | locomotion context | Instead of granting the policy full access to the action space from the star of training, we propose that partially limiting the ... | p. 5 (A. Implementation of the Growth Mechanism), p. 5 (IV. GROWTH-BASED TRAINING) |
| Whole-body policy / controller | context에서 joint target 또는 torque를 만든다 | context, body state, contact | RL policy, reference tracking, inverse dynamics 또는 whole-body control을 적용 | joint action/torque | Due to the highly nonlinear nature of the torque space, training a torque-based policy poses greater challenges than a position-based one, especially ... | p. 5 (IV. GROWTH-BASED TRAINING), p. 6 (A. Implementation of the Growth Mechanism) |
| Adaptation / recovery | disturbance와 contact mismatch에 대응한다 | new observation/history와 failure signal | latent adaptation, foothold change, recovery 또는 replan을 수행 | updated command | We utilize Proximal Policy Optimization (PPO) to train the control policy, The hyperparameters and neural network architecture are consistent with [33]. including ... | p. 6 (A. Implementation of the Growth Mechanism), p. 6 (A. Implementation of the Growth Mechanism) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / A. Implementation of the Growth Mechanism - extractive PDF cue:** Similarly, G(0) allows the robot to adapt reward priorities to align with specific training objectives.
- **p. 6 / A. Implementation of the Growth Mechanism - extractive PDF cue:** As G(t) evolves, the rewards shift focus from encouraging basic behaviors, such as forward motion, to more complex objectives like maintaining body height and tracking ...
- **p. 5 / IV. GROWTH-BASED TRAINING - extractive PDF cue:** Due to the highly nonlinear nature of the torque space, training a torque-based policy poses greater challenges than a position-based one, especially during early-stage exploration. ...
- **p. 5 / IV. GROWTH-BASED TRAINING - extractive PDF cue:** Our strategy also aligns conceptually with reward scheduling techniques, where the learning signal evolves in tandem with the agent's growing capabilities (70, 71].
- **Formal bridge:** body/proprioceptive/terrain state -> joint action/torque/footstep -> return, tracking or stability objective -> progress, balance and terrain robustness.
- **Equation/algorithm anchors:** p. 6 (A. Implementation of the Growth Mechanism), p. 6 (A. Implementation of the Growth Mechanism).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Learning-based, controllers, typically, position-based, action, spaces, where, policy, directly, outputs, position, com-, mands, actuators | proprioception, terrain/perception observation과 velocity command | body cue; exact tensor/frame verify |
| State/latent | Learning-based, controllers, typically, position-based, action, spaces, where, policy, directly, outputs | body/contact state, foothold 또는 behavior mode | body cue; notation verify |
| Action/output | Stable, Efficient, Torque-Based, Learning, novel, framework, loco-, motion, policies, growth | joint target, torque, footstep 또는 locomotion action | body cue; unit/decoder verify |
| Objective/constraint | Similarly, allows, robot, adapt, reward, priorities, align, specific, training, objectives | return, tracking or stability objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Iyrropuction - extractive PDF cue:** Learning-based controllers typically use position-based action spaces, where the policy directly outputs position com- ‘mands for the actuators. ‘These commands are subsequently converted to torque ...
- **p. 4 / A. Biomechanical Modet - extractive PDF cue:** 1) Activation Model: Output by our policy network, the action signal a, first passes through the activation model [55].
- **p. 2 / 1. Iyrropuction - extractive PDF cue:** [12] successfully trained torque policy by incorporating additional reward terms and action scaling.
- **p. 3 / 1. Iyrropuction - extractive PDF cue:** ‘ployment using simulted IMU data Sod temporal roprocepien observations (Grey), o help condition our policy on the (estimated) curremt robot velocity
- **p. 3 / 1. Iyrropuction - extractive PDF cue:** In contrast, tonque-based policies, where the policy directly ‘outputs motor torques, eliminate the need for tuning low= level controller parameters.
- **p. 4 / A. Biomechanical Modet - extractive PDF cue:** 3) Internal State Model: Our internal state model does not directly participate in torque calculation but serves as a feedback mechanism to provide the robot ...
- **p. 5 / A. Implementation of the Growth Mechanism - extractive PDF cue:** Instead of granting the policy full access to the action space from the star of training, we propose that partially limiting the robot's abilities can ...
- **Normalized interface:** observation=proprioception, terrain/perception observation과 velocity command; state=body/contact state, foothold 또는 behavior mode; output/action=joint target, torque, footstep 또는 locomotion action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | gait/skill episode horizon과 short-horizon body control이 계층적으로 분리된다. | Instead of granting the policy full access to the action space from the star of training, we propose that partially limiting the ... | episode/sequence/action-chunk boundary |
| Rate / latency | high-level command, policy rate와 low-level torque rate를 구분; exact rate 확인 필요. | Leveraging this framework, we achieve efficient policy learning within 20 minutes/ 3000 episodes. ‘The maximum episode length is set to 10 seconds. ... | Hz/fps, inference time and control rate |
| Memory | proprioceptive history, terrain latent와 contact/body state. | not recovered | window and reset |
| Compute | policy inference, adaptation encoder와 whole-body/control solve가 latency를 결정한다. | Leveraging this framework, we achieve efficient policy learning within 20 minutes/ 3000 episodes. ‘The maximum episode length is set to 10 seconds. ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / A. Implementation of the Growth Mechanism - extractive PDF cue:** Instead of granting the policy full access to the action space from the star of training, we propose that partially limiting the robot's abilities can ...
- **p. 5 / IV. GROWTH-BASED TRAINING - extractive PDF cue:** Due to the highly nonlinear nature of the torque space, training a torque-based policy poses greater challenges than a position-based one, especially during early-stage exploration. ...
- **p. 6 / A. Implementation of the Growth Mechanism - extractive PDF cue:** We utilize Proximal Policy Optimization (PPO) to train the control policy, The hyperparameters and neural network architecture are consistent with [33]. including a multilayer perceptron ...
- **p. 6 / A. Implementation of the Growth Mechanism - extractive PDF cue:** ‘Domain randomization is applied during training to simulate real-world variability. ‘The specific randomization settings are as follows: Added base mass: Randomly increased by up to ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Instead, granting, policy, full, access, action, space, star, training, partially, limiting, robot, abilities, promote, more, efficient, exploration, Additionally, gradually, increasing.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Command / terrain state | ‘To validate the effectiveness of our approach, we deployed it on a Unitree Go2 quadruped robot in real-world scenarios. | p. 7 (B. Lab Level Experiments), p. 6 (A. Implementation of the Growth Mechanism) |
| Whole-body policy / controller | We also compared its performance against several baseline methods, including Unitree's built-in, MPC-based controller, | p. 7 (B. Lab Level Experiments), p. 7 (A. Simulation Experiments) |
| Adaptation / recovery | Sa, SATA significantly outperforms SATA w/o growth in early stages of training, demonstrating the impact of this mechanism in early stage exploration. | p. 7 (A. Simulation Experiments), p. 7 (A. Simulation Experiments) |

## Failure and Ablation Link

- **p. 6 / A. Simulation Experiments - extractive PDF cue:** 1) Ablation Study: "To evaluate the contribution of each component of our approach, we compare the performance of the complete framework (SATA) with variants that ...
- **p. 6 / A. Implementation of the Growth Mechanism - extractive PDF cue:** Ablation study of the proposed framework. showing successful traning in green and failurofpremature convergence in red, SATA ts compared with varans that lack the Biomechanical ...
- **p. 7 / A. Simulation Experiments - extractive PDF cue:** Training rewards (), without GiQ) adgptation, and cumulative rewards in simulation test (6), when Commanded to fun at '8 ms (lightly OOD),
- **p. 7 / A. Simulation Experiments - extractive PDF cue:** this biomechanical model is removed, the robot converges to unnatural gaits, such as three-legged support pattems, which reduce stability and limit energy efficiency.
- **p. 5 / A. Implementation of the Growth Mechanism - extractive PDF cue:** To unify these components, We introduce a time-dependent general scale C(t), derived from the Gompertz. model [72], « well-established framework for modeling growth:
- **p. 9 / 1 Saco case - extractive PDF cue:** [Locomotion on wet slippery surfaces, showing both sucess (a) and failure (b), Even when the foot ofthe robot sip and fall down in Tile cases, ...
- **p. 9 / 1 Saco case - extractive PDF cue:** In contrast, Figure 11b shows a failure case, where the robot is given an abrupt command on the slippery surface.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (A. Implementation of the Growth Mechanism), p. 5 (IV. GROWTH-BASED TRAINING), p. 6 (A. Implementation of the Growth Mechanism), p. 6 (A. Implementation of the Growth Mechanism), objective p. 6 (A. Implementation of the Growth Mechanism), p. 6 (A. Implementation of the Growth Mechanism), p. 5 (IV. GROWTH-BASED TRAINING), p. 5 (IV. GROWTH-BASED TRAINING), temporal p. 5 (A. Implementation of the Growth Mechanism), p. 6 (A. Implementation of the Growth Mechanism), p. 4 (A. Biomechanical Modet), p. 2 (1. Iyrropuction), p. 5 (A. Implementation of the Growth Mechanism), p. 6 (A. Implementation of the Growth Mechanism).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
