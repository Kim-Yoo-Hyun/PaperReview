# Method - Dream to Control: Learning Behaviors by Latent Imagination

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1912.01603; PDF retrieval source: https://arxiv.org/pdf/1912.01603. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 5 (B Sequence length), p. 2 (1 INTRODUCTION), p. 5 (B Sequence length), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 4 (B Sequence length)): We apply the representation model to the first 5 images of two hold-out trajectories and predict forward for 45 steps using the latent dynamics, given only the actions.

## Method Body Digest

- **p. 5 / B Sequence length - extractive body cue:** We apply the representation model to the first 5 images of two hold-out trajectories and predict forward for 45 steps using the latent dynamics, given ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** As outlined in Figure 3 and detailed in Algorithm 1, Dreamer performs the following operations throughout the agent's life time, either interleaved or in parallel: ...
- **p. 5 / B Sequence length - extractive body cue:** Learning objective To update the action and value models, we first compute the value estimates Vλ(sτ) for all states sτ along the imagined trajectories.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Latent dynamics Dreamer uses a latent dynamics model that consists of three components.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** When the sensory inputs are high-dimensional images, latent dynamics models can abstract observations to predict forward in compact state spaces (Watter et al., 2015; Oh ...
- **p. 4 / B Sequence length - extractive body cue:** We use dense neural networks for the action and value models with parameters φ and ψ, respectively.
- **p. 6 / B Sequence length - extractive body cue:** The world model consists of the following components, where the observation model is only used to provide a learning signal, Representation model: pθ(st / st-1, ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The values optimize Bellman consistency for imagined rewards and the policy maximizes the values by propagating their analytic gradients back through the dynamics.

## Design Rationale

- **p. 1 / 1 INTRODUCTION - extractive body cue:** We present Dreamer, an agent that learns long-horizon behaviors from images purely by latent imagination.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Latent dynamics Dreamer uses a latent dynamics model that consists of three components.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Compared to predictions in image space, latent states have a small memory footprint that enables imagining thousands of trajectories in parallel.

## Source Evidence Cues

- **p. 5 / B Sequence length - extractive body cue:** We apply the representation model to the first 5 images of two hold-out trajectories and predict forward for 45 steps using the latent dynamics, given ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** As outlined in Figure 3 and detailed in Algorithm 1, Dreamer performs the following operations throughout the agent's life time, either interleaved or in parallel: ...
- **p. 5 / B Sequence length - extractive body cue:** Learning objective To update the action and value models, we first compute the value estimates Vλ(sτ) for all states sτ along the imagined trajectories.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Latent dynamics Dreamer uses a latent dynamics model that consists of three components.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** When the sensory inputs are high-dimensional images, latent dynamics models can abstract observations to predict forward in compact state spaces (Watter et al., 2015; Oh ...
- **p. 4 / B Sequence length - extractive body cue:** We use dense neural networks for the action and value models with parameters φ and ψ, respectively.
- **p. 6 / B Sequence length - extractive body cue:** The world model consists of the following components, where the observation model is only used to provide a learning signal, Representation model: pθ(st / st-1, ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | We apply the representation model to the first 5 images of two hold-out trajectories and predict forward for 45 steps using the ... | p. 5 (B Sequence length), p. 2 (1 INTRODUCTION) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | As outlined in Figure 3 and detailed in Algorithm 1, Dreamer performs the following operations throughout the agent's life time, either interleaved ... | p. 2 (1 INTRODUCTION), p. 5 (B Sequence length) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | Learning objective To update the action and value models, we first compute the value estimates Vλ(sτ) for all states sτ along the ... | p. 5 (B Sequence length), p. 2 (1 INTRODUCTION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / 1 INTRODUCTION - extractive body cue:** The values optimize Bellman consistency for imagined rewards and the policy maximizes the values by propagating their analytic gradients back through the dynamics.
- **원문 대조:** 학습한 latent dynamics를 imagination MDP로 사용하고 policy에 대해 expected discounted imagined reward를 최대화한다. Imagination은 과거 experience에서 얻은 model state에서 시작한다. ([PDF p. 3](https://arxiv.org/pdf/1912.01603#page=3), §3 Imagination environment).
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The value model optimizes Bellman consistency for imagined rewards and the action model is updated by propagating gradients of value estimates back through the neural ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** For this, we propagate stochastic gradients of multi-step returns through neural network predictions of actions, states, rewards, and values using reparameterization.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Often, imagined rewards are maximized with a parametric policy (Sutton, 1991; Ha and Schmidhuber, 2018; Zhang et al., 2019) or by online planning (Chua et ...
- **원문 대조:** 실제 환경의 visual-control 문제를 continuous-action POMDP로 정의하고 episode의 expected reward 합을 최대화하는 agent를 목표로 한다. §3의 learned-model imagination objective와 구분한다. ([PDF p. 2](https://arxiv.org/pdf/1912.01603#page=2), §2 Control with World Models, Reinforcement learning).
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 5 (B Sequence length), p. 2 (1 INTRODUCTION), p. 5 (B Sequence length), p. 1 (1 INTRODUCTION), p. 1 (Abstract), p. 2 (1 INTRODUCTION).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | When, sensory, inputs, high-dimensional, images, latent, dynamics, models, abstract, observations, predict, forward, compact, state | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | When, sensory, inputs, high-dimensional, images, latent, dynamics, models, abstract, observations | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | present, Dreamer, agent, learns, long-horizon, behaviors, images, purely, latent, imagination | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | values, optimize, Bellman, consistency, imagined, rewards, policy, maximizes, propagating, analytic | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1 INTRODUCTION - extractive body cue:** When the sensory inputs are high-dimensional images, latent dynamics models can abstract observations to predict forward in compact state spaces (Watter et al., 2015; Oh ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The representation model encodes observations and actions to create continuous vector-valued model states st with Markovian transitions (Watter et al., 2015; Zhang et al., 2019; ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** (a) From the dataset of past experience, the agent learns to encode observations and actions into compact latent states ( ), for example via reconstruction, ...
- **p. 6 / B Sequence length - extractive body cue:** (10) We implement the transition model as a recurrent state space model (RSSM; Hafner et al., 2018), the representation model by combining the RSSM with ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Training purely by imagination in a latent space lets us efficiently learn the policy by propagating analytic value gradients back through the latent dynamics. • ...
- **p. 6 / B Sequence length - extractive body cue:** We can also encourage mutual information between model states and observations by instead predicting the states from the images (Guo et al., 2018).
- **p. 1 / 1 INTRODUCTION - extractive body cue:** For this, we predict state values and actions in the learned latent space as summarized in Figure 1.
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | 2. // Environment interaction o1 ←env.reset() for time step t = 1..T do Compute st ∼pθ(st / st-1, at-1, ot) from history. | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | Agent observations are images of shape 64 × 64 × 3, actions range from 1 to 12 dimensions, rewards range from 0 ... | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | 2. // Environment interaction o1 ←env.reset() for time step t = 1..T do Compute st ∼pθ(st / st-1, at-1, ot) from history. | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | Agent observations are images of shape 64 × 64 × 3, actions range from 1 to 12 dimensions, rewards range from 0 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / 6 EXPERIMENTS - extractive body cue:** The training time for our Dreamer implementation is about 3 hours per 106 environment steps on the control suite, compared to 11 hours for online ...
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** We use a single Nvidia V100 GPU and 10 CPU cores for each training run.

## Method-Specific Formal Details

- **Body-defined terms:** apply, representation, model, first, images, hold-out, trajectories, predict, forward, steps, latent, dynamics, given, only, actions, outlined, Figure, detailed, Algorithm, Dreamer.
- **Relevant PDF headings:** not reliably recovered.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | These tasks pose a variety of challenges, including sparse rewards, contact dynamics, and 3D scenes. | p. 8 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS) |
| Filtering / recovery | The training time for our Dreamer implementation is about 3 hours per 106 environment steps on the control suite, compared to 11 ... | p. 8 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS) |
| Monitoring / re-entry | Baseline methods The highest reported performance on the continuous tasks is achieved by D4PG (Barth-Maron et al., 2018), an improved variant of ... | p. 8 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 8 / 6 EXPERIMENTS - extractive body cue:** PlaNet (Hafner et al., 2018) learns the same world model as Dreamer and selects actions via online planning without an action model and drastically improves ...
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** Baseline methods The highest reported performance on the continuous tasks is achieved by D4PG (Barth-Maron et al., 2018), an improved variant of DDPG (Lillicrap et ...
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** Further ablations are included in the appendix of the paper.
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** For this, we learn an action model to maximize imagined rewards without a value model and compare to online planning using PlaNet.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3: Components of Dreamer. (a) From the dataset of past experience, the agent learns to encode observations and actions into compact latent states ( ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6: Performance comparison to existing methods. Dreamer inherits the data-efficiency of PlaNet while exceeding the asymptotic performance of the best model-free agents. After 5 ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: Image observations for 5 of the 20 visual control tasks used in our experiments. The tasks pose a variety of challenges including contact ...

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (B Sequence length), p. 2 (1 INTRODUCTION), p. 5 (B Sequence length), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 4 (B Sequence length), objective p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), temporal p. 3 (1 INTRODUCTION), p. 8 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 2 (1 INTRODUCTION), p. 5 (B Sequence length), p. 9 (6 EXPERIMENTS).

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** When the sensory inputs are high-dimensional images, latent dynamics models can abstract observations to predict forward in compact state spaces (Watter et al., 2015; Oh et al., 2017; Gregor et ... (p. 1, 1 INTRODUCTION).
- **Objective/update evidence:** The value model optimizes Bellman consistency for imagined rewards and the action model is updated by propagating gradients of value estimates back through the neural network dynamics. • Executing the ... (p. 2, 1 INTRODUCTION).
- **Temporal/runtime evidence:** Agent observations are images of shape 64 × 64 × 3, actions range from 1 to 12 dimensions, rewards range from 0 to 1, episodes last for 1000 steps and ... (p. 8, 6 EXPERIMENTS).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
