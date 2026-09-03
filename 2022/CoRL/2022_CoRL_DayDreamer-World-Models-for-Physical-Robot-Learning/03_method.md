# Method - DayDreamer: World Models for Physical Robot Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v205/wu23c.html; PDF retrieval source: https://arxiv.org/pdf/2206.14176. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (2 Approach), p. 4 (2 Approach), p. 3 (2 Approach), p. 4 (2 Approach)): The world model is based on the Recurrent State-Space Model (RSSM; Hafner et al., 2018), which consists of four components: Encoder Network: encθ(st / st-1, at-1, xt) Decoder Network: decθ(st) ...

## Method Body Digest

- **p. 3 / 2 Approach - extractive body cue:** The world model is based on the Recurrent State-Space Model (RSSM; Hafner et al., 2018), which consists of four components: Encoder Network: encθ(st / st-1, ...
- **p. 4 / 2 Approach - extractive body cue:** The actor critic algorithm consists of two neural networks: Actor Network: π(at / st) Critic Network: v(st) (2) The role of the actor network is ...
- **p. 3 / 2 Approach - extractive body cue:** The dynamics model learns to predict the sequence of stochastic representations by using its recurrent state ht.
- **p. 4 / 2 Approach - extractive body cue:** Different gradient estimators are available for computing the policy gradient for optimizing the actor, such as Reinforce (Williams, 1992) and the reparameterization trick (Kingma and ...
- **p. 3 / 2 Approach - extractive body cue:** Using manually specified rewards as a function of the decoded sensory inputs is also possible.
- **p. 3 / 2 Approach - extractive body cue:** In our experiments, the robot has to discover task rewards by interacting with the real world, which the reward network learns to predict.
- **p. 3 / 1 Introduction - extractive body cue:** A recurrent state-space model (RSSM) is trained to predict future codes given actions, without observing intermediate inputs.
- **p. 4 / 2 Approach - extractive body cue:** (2020), we choose reparameterization gradients for continuous control tasks and Reinforce gradients for tasks with discrete actions.

## Design Rationale

- **p. 3 / 1 Introduction - extractive body cue:** Dreamer consists of two neural network components.
- **p. 3 / 2 Approach - extractive body cue:** The world model is based on the Recurrent State-Space Model (RSSM; Hafner et al., 2018), which consists of four components: Encoder Network: encθ(st / st-1, ...
- **p. 4 / 2 Approach - extractive body cue:** The actor critic algorithm consists of two neural networks: Actor Network: π(at / st) Critic Network: v(st) (2) The role of the actor network is ...

## Source Evidence Cues

- **p. 3 / 2 Approach - extractive body cue:** The world model is based on the Recurrent State-Space Model (RSSM; Hafner et al., 2018), which consists of four components: Encoder Network: encθ(st / st-1, ...
- **p. 4 / 2 Approach - extractive body cue:** The actor critic algorithm consists of two neural networks: Actor Network: π(at / st) Critic Network: v(st) (2) The role of the actor network is ...
- **p. 3 / 2 Approach - extractive body cue:** The dynamics model learns to predict the sequence of stochastic representations by using its recurrent state ht.
- **p. 4 / 2 Approach - extractive body cue:** Different gradient estimators are available for computing the policy gradient for optimizing the actor, such as Reinforce (Williams, 1992) and the reparameterization trick (Kingma and ...
- **Detected method headings:** 2 Approach (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | The world model is based on the Recurrent State-Space Model (RSSM; Hafner et al., 2018), which consists of four components: Encoder Network: ... | p. 3 (2 Approach), p. 4 (2 Approach) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | The actor critic algorithm consists of two neural networks: Actor Network: π(at / st) Critic Network: v(st) (2) The role of the ... | p. 4 (2 Approach), p. 3 (2 Approach) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | The dynamics model learns to predict the sequence of stochastic representations by using its recurrent state ht. | p. 3 (2 Approach), p. 4 (2 Approach) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 2 Approach - extractive body cue:** The actor critic algorithm consists of two neural networks: Actor Network: π(at / st) Critic Network: v(st) (2) The role of the actor network is ...
- **p. 4 / 2 Approach - extractive body cue:** Different gradient estimators are available for computing the policy gradient for optimizing the actor, such as Reinforce (Williams, 1992) and the reparameterization trick (Kingma and ...
- **p. 3 / 2 Approach - extractive body cue:** Using manually specified rewards as a function of the decoded sensory inputs is also possible.
- **p. 3 / 2 Approach - extractive body cue:** In our experiments, the robot has to discover task rewards by interacting with the real world, which the reward network learns to predict.
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 4 (2 Approach), p. 4 (2 Approach), p. 3 (2 Approach).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | world, model, Recurrent, State-Space, RSSM, Hafner, consists, four, components, Encoder, Network, st-1, at-1, Decoder | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | world, model, Recurrent, State-Space, RSSM, Hafner, consists, four, components, Encoder | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | Dreamer, consists, neural, network, components, world, model, Recurrent, State-Space, RSSM | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | actor, critic, algorithm, consists, neural, networks, Network, role, learn, distribution | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 2 Approach - extractive body cue:** The world model is based on the Recurrent State-Space Model (RSSM; Hafner et al., 2018), which consists of four components: Encoder Network: encθ(st / st-1, ...
- **p. 3 / 1 Introduction - extractive body cue:** A recurrent state-space model (RSSM) is trained to predict future codes given actions, without observing intermediate inputs.
- **p. 4 / 2 Approach - extractive body cue:** The actor critic algorithm consists of two neural networks: Actor Network: π(at / st) Critic Network: v(st) (2) The role of the actor network is ...
- **p. 4 / 2 Approach - extractive body cue:** (2020), we choose reparameterization gradients for continuous control tasks and Reinforce gradients for tasks with discrete actions.
- **p. 2 / 1 Introduction - extractive body cue:** World models also learn representations that fuse multiple sensor modalities and integrate them into latent states, removing the need for manual state estimation.
- **p. 2 / 1 Introduction - extractive body cue:** The tasks cover a range of challenges, including different action spaces, sensory modalities, and reward structures. • Walking in 1 Hour We teach a quadruped ...
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | As the goal is fixed, after 100 environment steps, we end the episode and randomize the robot's position through a sequence of ... | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | As shown in Figure 7, Dreamer achieves an average distance to the goal of 0.15, measured in units of the area size ... | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | We control the high-performance UR5 robot from Universal Robotics at 2 Hz. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3 Experiments - extractive body cue:** 0 20 40 60 Minutes 5 7 9 11 Avg Reward A1 Quadruped Walking Dreamer SAC Figure 4: A1 Quadruped Walking Starting from lying on ...
- **p. 5 / 3 Experiments - extractive body cue:** The graph shows a single training run with the shaded area indicating one standard deviation within each time bin.
- **p. 3 / 2 Approach - extractive body cue:** In our implementation, a learner thread continuously trains the world model and actor critic behavior, while an actor thread in parallel computes actions for environment ...
- **p. 3 / 2 Approach - extractive body cue:** This reduces accumulating errors and enables massively parallel training with a large batch size.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** world, model, Recurrent, State-Space, RSSM, Hafner, consists, four, components, Encoder, Network, st-1, at-1, Decoder, Dynamics, Reward, Physical, robots, often, equipped.
- **Relevant PDF headings:** 2 Approach (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | 3.2 UR5 Multi-Object Visual Pick and Place Common in warehouse and logistics environments, pick and place tasks require a robot manipulator to ... | p. 6 (3 Experiments), p. 7 (3 Experiments) |
| Filtering / recovery | The state-of-the-art baseline in this category is DrQv2 (Yarats et al., 2021), which uses image augmentation to increase sample-efficiency. | p. 5 (3 Experiments), p. 1 (Figure/Table caption) |
| Monitoring / re-entry | We find that DrQv2, a model-free algorithm specifically designed to continuous control from pixels, achieves similar performance. | p. 7 (3 Experiments), p. 7 (3 Experiments) |

## Failure and Ablation Link

- **p. 4 / 3 Experiments - extractive body cue:** Specifically, we aim to answer the following research questions: • Does Dreamer enable robot learning directly in the real world, without simulators? • Does Dreamer ...
- **p. 5 / 3 Experiments - extractive body cue:** In contrast, we train in the end-toend reinforcement learning setting directly on the robot, without simulators or resets.
- **p. 5 / 3 Experiments - extractive body cue:** Due to space constraints, we manually intervene when the robot has reached the end of the available training area, without modifying the joint configuration or ...
- **p. 7 / 3 Experiments - extractive body cue:** While soft objects would be challenging to model accurately in a simulator, Dreamer avoids this issue by directly learning on the real robot without a ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3: Neural Network Training We leverage the Dreamer algorithm (Hafner et al., 2019; 2020) for fast robot learning in real world. Dreamer consists of ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: To study the applicability of Dreamer for sample-efficient robot learning, we apply the algorithm to learn robot locomotion, manipulation, and navigation tasks from ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: Dreamer follows a simple pipeline for online learning on robot hardware without simulators. The cur- rent learned policy collects experience on the robot. ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (2 Approach), p. 4 (2 Approach), p. 3 (2 Approach), p. 4 (2 Approach), objective p. 4 (2 Approach), p. 4 (2 Approach), p. 3 (2 Approach), p. 3 (2 Approach), temporal p. 7 (3 Experiments), p. 7 (3 Experiments), p. 5 (3 Experiments), p. 2 (1 Introduction), p. 5 (3 Experiments), p. 6 (3 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** The world model is based on the Recurrent State-Space Model (RSSM; Hafner et al., 2018), which consists of four components: Encoder Network: encθ(st / st-1, at-1, xt) Decoder Network: decθ(st) ... (p. 3, 2 Approach).
- **Objective/update evidence:** Different gradient estimators are available for computing the policy gradient for optimizing the actor, such as Reinforce (Williams, 1992) and the reparameterization trick (Kingma and Welling, 2013; Rezende et al., ... (p. 4, 2 Approach).
- **Temporal/runtime evidence:** As the goal is fixed, after 100 environment steps, we end the episode and randomize the robot's position through a sequence of high power random motor actions. (p. 7, 3 Experiments).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
