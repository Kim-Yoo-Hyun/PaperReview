# Method - Learning Latent Dynamics for Planning from Pixels

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1811.04551; PDF retrieval source: https://arxiv.org/pdf/1811.04551. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (2. Latent Space Planning), p. 3 (3. Recurrent State Space Model), p. 4 (3. Recurrent State Space Model), p. 3 (3. Recurrent State Space Model), p. 4 (3. Recurrent State Space Model), p. 2 (2 Initialize model parameters θ randomly)): We define a discrete time step t, hidden states st, image observations ot, continuous action vectors at, and scalar rewards rt, that follow the stochastic dynamics Transition function: st ∼p(st ...

## Method Body Digest

- **p. 2 / 2. Latent Space Planning - extractive body cue:** We define a discrete time step t, hidden states st, image observations ot, continuous action vectors at, and scalar rewards rt, that follow the stochastic ...
- **p. 3 / 3. Recurrent State Space Model - extractive body cue:** Instead, we use an encoder q(s1:T / o1:T , a1:T ) = QT t=1 q(st / st-1, at-1, ot) to infer approximate state posteriors from ...
- **p. 4 / 3. Recurrent State Space Model - extractive body cue:** We use such a model, shown in Figure 2c, that we name recurrent state-space model (RSSM), Deterministic state model: ht = f(ht-1, st-1, at-1) Stochastic ...
- **p. 3 / 3. Recurrent State Space Model - extractive body cue:** In this section, we remind the reader of latent state-space models and then describe our dynamics model.
- **p. 4 / 3. Recurrent State Space Model - extractive body cue:** We use the filtering posterior that conditions on past observations since we are ultimately interested in using the model for planning, but one may also ...
- **p. 2 / 2 Initialize model parameters θ randomly - extractive body cue:** 13 for action repeat k = 1..R do 14 rk t , ok t+1 ←env.step(at) 15 rt, ot+1 ←PR k=1 rk t , oR t+1 ...
- **p. 3 / 2 Initialize model parameters θ randomly - extractive body cue:** CEM is a populationbased optimization algorithm that infers a distribution over action sequences that maximize the objective.
- **p. 4 / 3. Recurrent State Space Model - extractive body cue:** Estimating the outer expectations using a single reparameterized sample yields an efficient objective for inference and learning in non-linear latent variable models that can be ...

## Design Rationale

- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we propose the Deep Planning Network (PlaNet), a model-based agent that learns the environment dynamics from pixels and chooses actions through online ...
- **p. 1 / 1. Introduction - extractive body cue:** Key contributions of this work are summarized as follows: • Planning in latent spaces We solve a variety of tasks from the DeepMind control suite, ...
- **p. 2 / 2. Latent Space Planning - extractive body cue:** In this section, we introduce notation for the environment and describe the general implementation of our model-based agent.

## Source Evidence Cues

- **p. 2 / 2. Latent Space Planning - extractive body cue:** We define a discrete time step t, hidden states st, image observations ot, continuous action vectors at, and scalar rewards rt, that follow the stochastic ...
- **p. 3 / 3. Recurrent State Space Model - extractive body cue:** Instead, we use an encoder q(s1:T / o1:T , a1:T ) = QT t=1 q(st / st-1, at-1, ot) to infer approximate state posteriors from ...
- **p. 4 / 3. Recurrent State Space Model - extractive body cue:** We use such a model, shown in Figure 2c, that we name recurrent state-space model (RSSM), Deterministic state model: ht = f(ht-1, st-1, at-1) Stochastic ...
- **p. 3 / 3. Recurrent State Space Model - extractive body cue:** In this section, we remind the reader of latent state-space models and then describe our dynamics model.
- **p. 4 / 3. Recurrent State Space Model - extractive body cue:** We use the filtering posterior that conditions on past observations since we are ultimately interested in using the model for planning, but one may also ...
- **p. 2 / 2 Initialize model parameters θ randomly - extractive body cue:** 13 for action repeat k = 1..R do 14 rk t , ok t+1 ←env.step(at) 15 rt, ot+1 ←PR k=1 rk t , oR t+1 ...
- **Detected method headings:** 2 Initialize model parameters θ randomly (p. 2); 3. Recurrent State Space Model (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | We define a discrete time step t, hidden states st, image observations ot, continuous action vectors at, and scalar rewards rt, that ... | p. 2 (2. Latent Space Planning), p. 3 (3. Recurrent State Space Model) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | Instead, we use an encoder q(s1:T / o1:T , a1:T ) = QT t=1 q(st / st-1, at-1, ot) to infer approximate ... | p. 3 (3. Recurrent State Space Model), p. 4 (3. Recurrent State Space Model) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | We use such a model, shown in Figure 2c, that we name recurrent state-space model (RSSM), Deterministic state model: ht = f(ht-1, ... | p. 4 (3. Recurrent State Space Model), p. 3 (3. Recurrent State Space Model) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 2 Initialize model parameters θ randomly - extractive body cue:** CEM is a populationbased optimization algorithm that infers a distribution over action sequences that maximize the objective.
- **p. 4 / 3. Recurrent State Space Model - extractive body cue:** Estimating the outer expectations using a single reparameterized sample yields an efficient objective for inference and learning in non-linear latent variable models that can be ...
- **p. 2 / 2 Initialize model parameters θ randomly - extractive body cue:** 6 Compute loss L(θ) from Equation 3.
- **p. 2 / 2 Initialize model parameters θ randomly - extractive body cue:** The goal is to implement a policy p(at / o≤t, a<t) that maximizes the expected sum of rewards Ep  PT t=1 rt  , ...
- **p. 3 / 3. Recurrent State Space Model - extractive body cue:** It defines the generative process of the images and rewards using a hidden state sequence {st}T t=1, Transition model: st ∼p(st / st-1, at-1) Observation ...
- **p. 4 / 3. Recurrent State Space Model - extractive body cue:** For simplicity, we write losses for predicting only the observations - the reward losses follow by analogy.
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 2 (2 Initialize model parameters θ randomly), p. 4 (3. Recurrent State Space Model), p. 2 (2. Latent Space Planning), p. 3 (2 Initialize model parameters θ randomly), p. 3 (3. Recurrent State Space Model), p. 4 (3. Recurrent State Space Model).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | define, discrete, time, step, hidden, states, image, observations, continuous, action, vectors, scalar, rewards, follow | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | define, discrete, time, step, hidden, states, image, observations, continuous, action | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | Deep, Planning, Network, PlaNet, model-based, agent, learns, environment, dynamics, pixels | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | CEM, populationbased, optimization, algorithm, infers, distribution, over, action, sequences, maximize | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 2. Latent Space Planning - extractive body cue:** We define a discrete time step t, hidden states st, image observations ot, continuous action vectors at, and scalar rewards rt, that follow the stochastic ...
- **p. 3 / 3. Recurrent State Space Model - extractive body cue:** Instead, we use an encoder q(s1:T / o1:T , a1:T ) = QT t=1 q(st / st-1, at-1, ot) to infer approximate state posteriors from ...
- **p. 2 / 2. Latent Space Planning - extractive body cue:** Problem setup Since individual image observations generally do not reveal the full state of the environment, we consider a partially observable Markov decision process (POMDP).
- **p. 3 / 2 Initialize model parameters θ randomly - extractive body cue:** Because the reward is modeled as a function of the latent state, the planner can operate purely in latent space without generating images, which allows ...
- **p. 4 / 3. Recurrent State Space Model - extractive body cue:** Importantly, all information about the observations must pass through the sampling step of the encoder to avoid a deterministic shortcut from inputs to reconstructions.
- **p. 4 / 3. Recurrent State Space Model - extractive body cue:** We use such a model, shown in Figure 2c, that we name recurrent state-space model (RSSM), Deterministic state model: ht = f(ht-1, st-1, at-1) Stochastic ...
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we propose the Deep Planning Network (PlaNet), a model-based agent that learns the environment dynamics from pixels and chooses actions through online ...
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | We define a discrete time step t, hidden states st, image observations ot, continuous action vectors at, and scalar rewards rt, that ... | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | As detailed in Algorithm 2 in the appendix, we initialize a time-dependent diagonal Gaussian belief over optimal action sequences at:t+H ∼Normal(µt:t+H, σ2 ... | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | 7 Update model parameters θ ←θ -α∇θL(θ). // Data collection 8 o1 ←env.reset() 9 for time step t = 1..  T ... | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | The training time of 10 to 20 hours (depending on the task) on a single Nvidia V100 GPU compares favorably to that ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3. Recurrent State Space Model - extractive body cue:** We use the filtering posterior that conditions on past observations since we are ultimately interested in using the model for planning, but one may also ...
- **p. 6 / 5. Experiments - extractive body cue:** The training time of 10 to 20 hours (depending on the task) on a single Nvidia V100 GPU compares favorably to that of A3C and ...
- **p. 3 / 2 Initialize model parameters θ randomly - extractive body cue:** Starting from a small amount of S seed episodes collected under random actions, we train the model and add one additional episode to the data ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** define, discrete, time, step, hidden, states, image, observations, continuous, action, vectors, scalar, rewards, follow, stochastic, dynamics, Transition, function, st-1, at-1.
- **Relevant PDF headings:** 2 Initialize model parameters θ randomly (p. 2); 3. Recurrent State Space Model (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | The cartpole swingup task requires a long planning horizon and to memorize the cart when it is out of view, reacher has ... | p. 6 (5. Experiments), p. 6 (5. Experiments) |
| Filtering / recovery | The agent solves all tasks while learning slower compared to individually trained agents. | p. 6 (5. Experiments), p. 6 (5. Experiments) |
| Monitoring / re-entry | Within less than one hundredth the episodes, PlaNet outperforms A3C (Mnih et al., 2016) and achieves similar performance to the top model-free ... | p. 6 (5. Experiments), p. 6 (5. Experiments) |

## Failure and Ablation Link

- **p. 6 / 5. Experiments - extractive body cue:** The stochastic component is even more important - the agent does not learn without it.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Comparison of agent designs. Plots show test performance over the number of collected episodes. We compare PlaNet, a version that collects data under ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 11: Open-loop state diagnostics. We freeze the dynamics model of a PlaNet agent and learn small neural networks to predict the true positions, velocities, ...
- **p. 8 / 7. Discussion - extractive body cue:** Directions for future work include learning temporal abstraction instead of using a fixed action repeat, possibly through hierarchical models.
- **p. 6 / 5. Experiments - extractive body cue:** The cartpole swingup task requires a long planning horizon and to memorize the cart when it is out of view, reacher has a sparse reward ...
- **p. 6 / 5. Experiments - extractive body cue:** The noise might also add a safety margin to the planning objective that results in more robust action sequences.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Comparison of PlaNet to model-free algorithms and other model designs. Plots show test performance over the number of collected episodes. We compare PlaNet ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (2. Latent Space Planning), p. 3 (3. Recurrent State Space Model), p. 4 (3. Recurrent State Space Model), p. 3 (3. Recurrent State Space Model), p. 4 (3. Recurrent State Space Model), p. 2 (2 Initialize model parameters θ randomly), objective p. 3 (2 Initialize model parameters θ randomly), p. 4 (3. Recurrent State Space Model), p. 2 (2 Initialize model parameters θ randomly), p. 2 (2 Initialize model parameters θ randomly), p. 3 (3. Recurrent State Space Model), p. 4 (3. Recurrent State Space Model), temporal p. 2 (2. Latent Space Planning), p. 3 (2 Initialize model parameters θ randomly), p. 6 (5. Experiments), p. 2 (2 Initialize model parameters θ randomly), p. 6 (5. Experiments), p. 3 (3. Recurrent State Space Model).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** We define a discrete time step t, hidden states st, image observations ot, continuous action vectors at, and scalar rewards rt, that follow the stochastic dynamics Transition function: st ∼p(st ... (p. 2, 2. Latent Space Planning).
- **Objective/update evidence:** Estimating the outer expectations using a single reparameterized sample yields an efficient objective for inference and learning in non-linear latent variable models that can be optimized using gradient ascent (Kingma ... (p. 4, 3. Recurrent State Space Model).
- **Temporal/runtime evidence:** Agent designs Figure 5 compares PlaNet, a version collecting episodes under random actions rather than by planning, and a version that at each environment step selects the best action out ... (p. 6, 5. Experiments).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
