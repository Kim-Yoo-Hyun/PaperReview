# Method - TD-MPC2: Scalable, Robust World Models for Continuous Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2310.16828; PDF retrieval source: https://arxiv.org/pdf/2310.16828. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (2 BACKGROUND), p. 1 (ABSTRACT), p. 5 (2 BACKGROUND), p. 2 (1 INTRODUCTION), p. 4 (2 BACKGROUND), p. 3 (2 BACKGROUND)): The TD-MPC2 architecture is shown in Figure 3 and consists of five components: Encoder z = h(s, e) ▷Maps observations to their latent representations Latent dynamics z′ = d(z, a, ...

## Method Body Digest

- **p. 3 / 2 BACKGROUND - extractive body cue:** The TD-MPC2 architecture is shown in Figure 3 and consists of five components: Encoder z = h(s, e) ▷Maps observations to their latent representations Latent ...
- **p. 1 / ABSTRACT - extractive body cue:** TD-MPC is a model-based reinforcement learning (RL) algorithm that performs local trajectory optimization in the latent space of a learned implicit (decoderfree) world model.
- **p. 5 / 2 BACKGROUND - extractive body cue:** To do so, we zero-pad all model inputs and outputs to their largest respective dimensions, and mask out invalid action dimensions in predictions made by ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our algorithm, which builds upon TD-MPC (Hansen et al., 2022), performs local trajectory optimization in the latent space of a learned implicit (decoder-free) world model.
- **p. 4 / 2 BACKGROUND - extractive body cue:** Specifically, our approach leverages the MPC framework for local trajectory optimization using Model Predictive Path Integral (MPPI) (Williams et al., 2015) as a derivative-free optimizer ...
- **p. 3 / 2 BACKGROUND - extractive body cue:** The model then recurrently predicts actions ˆa, rewards ˆr, and terminal values ˆq, without decoding future observations.
- **p. 2 / 2 BACKGROUND - extractive body cue:** Reinforcement Learning (RL) aims to learn a policy from interaction with an environment, formulated as a Markov Decision Process (MDP) (Bellman, 1957).
- **p. 4 / 2 BACKGROUND - extractive body cue:** The h, d, R, Q components are jointly optimized to minimize the objective L (θ) .= E (s,a,r,s′)0:H∼B   H X t=0 λt  ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this work, we present TDMPC2: a significant step towards achieving this goal.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our algorithmic contributions, which have been key to achieving this milestone, are two-fold: (1) improved algorithmic robustness by revisiting core design choices, and (2) careful ...
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we present TD-MPC2: a series of improvements upon the TD-MPC algorithm.

## Source Evidence Cues

- **p. 3 / 2 BACKGROUND - extractive body cue:** The TD-MPC2 architecture is shown in Figure 3 and consists of five components: Encoder z = h(s, e) ▷Maps observations to their latent representations Latent ...
- **p. 1 / ABSTRACT - extractive body cue:** TD-MPC is a model-based reinforcement learning (RL) algorithm that performs local trajectory optimization in the latent space of a learned implicit (decoderfree) world model.
- **p. 5 / 2 BACKGROUND - extractive body cue:** To do so, we zero-pad all model inputs and outputs to their largest respective dimensions, and mask out invalid action dimensions in predictions made by ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our algorithm, which builds upon TD-MPC (Hansen et al., 2022), performs local trajectory optimization in the latent space of a learned implicit (decoder-free) world model.
- **p. 4 / 2 BACKGROUND - extractive body cue:** Specifically, our approach leverages the MPC framework for local trajectory optimization using Model Predictive Path Integral (MPPI) (Williams et al., 2015) as a derivative-free optimizer ...
- **p. 3 / 2 BACKGROUND - extractive body cue:** The model then recurrently predicts actions ˆa, rewards ˆr, and terminal values ˆq, without decoding future observations.
- **p. 2 / 2 BACKGROUND - extractive body cue:** Reinforcement Learning (RL) aims to learn a policy from interaction with an environment, formulated as a Markov Decision Process (MDP) (Bellman, 1957).
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | The TD-MPC2 architecture is shown in Figure 3 and consists of five components: Encoder z = h(s, e) ▷Maps observations to their ... | p. 3 (2 BACKGROUND), p. 1 (ABSTRACT) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | TD-MPC is a model-based reinforcement learning (RL) algorithm that performs local trajectory optimization in the latent space of a learned implicit (decoderfree) ... | p. 1 (ABSTRACT), p. 5 (2 BACKGROUND) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | To do so, we zero-pad all model inputs and outputs to their largest respective dimensions, and mask out invalid action dimensions in ... | p. 5 (2 BACKGROUND), p. 2 (1 INTRODUCTION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 2 BACKGROUND - extractive body cue:** The h, d, R, Q components are jointly optimized to minimize the objective L (θ) .= E (s,a,r,s′)0:H∼B   H X t=0 λt  ...
- **p. 3 / 2 BACKGROUND - extractive body cue:** Model Predictive Control (MPC) is a general framework for model-based control that optimizes action sequences at:t+H of finite length such that return is maximized (or ...
- **p. 5 / 2 BACKGROUND - extractive body cue:** Notably, Equation 6 estimates the full RL objective introduced in Section 2 by bootstrapping with the learned terminal value function beyond horizon H.
- **p. 3 / 2 BACKGROUND - extractive body cue:** The TD-MPC2 architecture is shown in Figure 3 and consists of five components: Encoder z = h(s, e) ▷Maps observations to their latent representations Latent ...
- **p. 4 / 2 BACKGROUND - extractive body cue:** As the magnitude of rewards may differ drastically between tasks, TD-MPC2 formulates reward and value prediction as a discrete regression (multiclass classification) problem in a ...
- **p. 5 / 2 BACKGROUND - extractive body cue:** Equation 6 is solved by iteratively sampling action sequences from N(µ, σ2), evaluating their expected return, and updating µ, σ based on a weighted average.
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 4 (2 BACKGROUND), p. 4 (2 BACKGROUND), p. 5 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 5 (2 BACKGROUND).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | TD-MPC2, architecture, Figure, consists, five, components, Encoder, Maps, observations, latent, representations, dynamics, Models, forward | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | TD-MPC2, architecture, Figure, consists, five, components, Encoder, Maps, observations, latent | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | present, TDMPC2, significant, step, towards, achieving, goal, algorithmic, contributions, have | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | components, jointly, optimized, minimize, objective, Joint-embedding, prediction, Reward, Value, where | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 2 BACKGROUND - extractive body cue:** The TD-MPC2 architecture is shown in Figure 3 and consists of five components: Encoder z = h(s, e) ▷Maps observations to their latent representations Latent ...
- **p. 5 / 2 BACKGROUND - extractive body cue:** To do so, we zero-pad all model inputs and outputs to their largest respective dimensions, and mask out invalid action dimensions in predictions made by ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Tasks include high-dimensional state and action spaces (up to A ∈R39), image observations, sparse rewards, multi-object manipulation, physiologically accurate musculoskeletal motor control, complex locomotion (e.g.
- **p. 2 / 2 BACKGROUND - extractive body cue:** Reinforcement Learning (RL) aims to learn a policy from interaction with an environment, formulated as a Markov Decision Process (MDP) (Bellman, 1957).
- **p. 3 / 2 BACKGROUND - extractive body cue:** The model then recurrently predicts actions ˆa, rewards ˆr, and terminal values ˆq, without decoding future observations.
- **p. 5 / 2 BACKGROUND - extractive body cue:** (ii) how to accommodate multiple observation and action spaces without specific domain knowledge?
- **p. 1 / 1 INTRODUCTION - extractive body cue:** While researchers have recently extended this paradigm to robotics (Reed et al., 2022; Brohan et al., 2023), a generalist embodied agent that learns to perform ...
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | The h, d, R, Q components are jointly optimized to minimize the objective L (θ) .= E (s,a,r,s′)0:H∼B   H X ... | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | Episode return as a function of environment steps in Humanoid (A ∈R21) and Dog (A ∈R38) locomotion tasks from DMControl. | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | Score of a 19M parameter TD-MPC2 agent trained on 70 tasks and finetuned online to each of 10 heldout tasks for 20k ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 2 BACKGROUND - extractive body cue:** To do so, we zero-pad all model inputs and outputs to their largest respective dimensions, and mask out invalid action dimensions in predictions made by ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** TD-MPC2, architecture, Figure, consists, five, components, Encoder, Maps, observations, latent, representations, dynamics, Models, forward, Reward, Predicts, transition, Terminal, value, discounted.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | However, TD-MPC2 can be readily applied to tasks with other input 120k environment steps corresponds to 20 episodes in DMControl and 100 ... | p. 8 (4.1 RESULTS), p. 6 (4 EXPERIMENTS) |
| Filtering / recovery | TD-MPC2 outperforms baselines by a large margin on these tasks, despite using the same hyperparameters across all tasks. | p. 6 (4.1 RESULTS), p. 6 (4 EXPERIMENTS) |
| Monitoring / re-entry | Figure 13. Single-task Meta-World results. Success rate (%) as a function of environment steps. TD-MPC2 performance is comparable to existing methods on ... | p. 22 (Figure/Table caption), p. 23 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / 4.1 RESULTS - extractive body cue:** Our ablations highlight the relative importance of each design choice; red is the default formulation of TD-MPC2.
- **p. 8 / 4.1 RESULTS - extractive body cue:** Our main ablations, shown in Figure 9, are conducted on three of the most difficult online RL tasks, as well as largescale multitask training (80 ...
- **p. 9 / 4.1 RESULTS - extractive body cue:** TD-MPC2 performs comparably to the two best baselines, DrQ-v2 and DreamerV3, without any changes to hyperparameters.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. The TD-MPC2 architecture. Observations s are encoded into their (normalized) latent representation z. The model then recurrently predicts actions ˆa, rewards ˆr, and ...
- **p. 19 / Figure/Table caption - extractive body cue:** Table 5. MyoSuite. We consider a total of 10 continuous control tasks from the MyoSuite domain. The MyoSuite benchmark is designed for high-dimensional physiologically accurate ...
- **p. 25 / Figure/Table caption - extractive body cue:** Figure 18. Normalized task embeddings. Normalized score of 19M parameter multitask (80 tasks) TD-MPC2 agents, with and without normalized task embeddings e as described in ...
- **p. 25 / Figure/Table caption - extractive body cue:** Figure 19. T-SNE of task embeddings with and without normalization. T-SNE (van der Maaten & Hinton, 2008) visualizations of task embeddings learned by TD-MPC2 agent ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (2 BACKGROUND), p. 1 (ABSTRACT), p. 5 (2 BACKGROUND), p. 2 (1 INTRODUCTION), p. 4 (2 BACKGROUND), p. 3 (2 BACKGROUND), objective p. 4 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 5 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND), p. 5 (2 BACKGROUND), temporal p. 4 (2 BACKGROUND), p. 6 (4 EXPERIMENTS), p. 7 (4.1 RESULTS), p. 8 (4.1 RESULTS), p. 3 (2 BACKGROUND), p. 6 (4 EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (31 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** The TD-MPC2 architecture is shown in Figure 3 and consists of five components: Encoder z = h(s, e) ▷Maps observations to their latent representations Latent dynamics z′ = d(z, a, ... (p. 3, 2 BACKGROUND).
- **Objective/update evidence:** The h, d, R, Q components are jointly optimized to minimize the objective L (θ) .= E (s,a,r,s′)0:H∼B   H X t=0 λt   ∥z′ t -sg(h(s′ t))∥2 ... (p. 4, 2 BACKGROUND).
- **Temporal/runtime evidence:** Episode return as a function of environment steps in Humanoid (A ∈R21) and Dog (A ∈R38) locomotion tasks from DMControl. (p. 6, 4 EXPERIMENTS).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
