# Method - Decision Transformer: Reinforcement Learning via Sequence Modeling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2106.01345; PDF retrieval source: https://arxiv.org/pdf/2106.01345. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3 Method), p. 4 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 5 (3 Method), p. 5 (3 Method)): In this section, we present Decision Transformer, which models trajectories autoregressively with minimal modification to the transformer architecture, as summarized in Figure 1 and Algorithm 1.

## Method Body Digest

- **p. 4 / 3 Method - extractive body cue:** In this section, we present Decision Transformer, which models trajectories autoregressively with minimal modification to the transformer architecture, as summarized in Figure 1 and Algorithm ...
- **p. 4 / 3 Method - extractive body cue:** The key desiderata in our choice of trajectory representation are that it should enable transformers to learn meaningful patterns and we should be able to ...
- **p. 6 / 3 Method - extractive body cue:** In particular, our primary points of comparison are modelfree offline RL algorithms based on TD-learning, since our Decision Transformer architecture is fundamentally model-free in nature ...
- **p. 6 / 3 Method - extractive body cue:** In addition, we also compare against other prior model-free RL algorithms like BEAR [18] and BRAC [19]. • Imitation learning: this regime similarly uses supervised ...
- **p. 5 / 3 Method - extractive body cue:** The tokens are then processed by a GPT [9] model, which predicts future action tokens via autoregressive modeling.
- **p. 5 / 3 Method - extractive body cue:** We feed the last K timesteps into Decision Transformer, for a total of 3K tokens (one for each modality: return-to-go, state, or action).
- **p. 7 / 3 Method - extractive body cue:** Decision Transformer (DT) outperforms conventional RL algorithms on almost all tasks.
- **p. 4 / 3 Method - extractive body cue:** As a result, instead of feeding the rewards directly, we feed the model with the returns-to-go bRt = PT t′=t rt′.

## Design Rationale

- **p. 3 / 1 Introduction - extractive body cue:** Training dataset consists of random walk trajectories and their per-node returns-to-go (middle).
- **p. 4 / 1 Introduction - extractive body cue:** Motivated by this observation, we propose Decision Transformer, where we use the GPT architecture to autoregressively model trajectories (shown in Figure 1).
- **p. 4 / 3 Method - extractive body cue:** In this section, we present Decision Transformer, which models trajectories autoregressively with minimal modification to the transformer architecture, as summarized in Figure 1 and Algorithm ...

## Source Evidence Cues

- **p. 4 / 3 Method - extractive body cue:** In this section, we present Decision Transformer, which models trajectories autoregressively with minimal modification to the transformer architecture, as summarized in Figure 1 and Algorithm ...
- **p. 4 / 3 Method - extractive body cue:** The key desiderata in our choice of trajectory representation are that it should enable transformers to learn meaningful patterns and we should be able to ...
- **p. 6 / 3 Method - extractive body cue:** In particular, our primary points of comparison are modelfree offline RL algorithms based on TD-learning, since our Decision Transformer architecture is fundamentally model-free in nature ...
- **p. 6 / 3 Method - extractive body cue:** In addition, we also compare against other prior model-free RL algorithms like BEAR [18] and BRAC [19]. • Imitation learning: this regime similarly uses supervised ...
- **p. 5 / 3 Method - extractive body cue:** The tokens are then processed by a GPT [9] model, which predicts future action tokens via autoregressive modeling.
- **p. 5 / 3 Method - extractive body cue:** We feed the last K timesteps into Decision Transformer, for a total of 3K tokens (one for each modality: return-to-go, state, or action).
- **p. 7 / 3 Method - extractive body cue:** Decision Transformer (DT) outperforms conventional RL algorithms on almost all tasks.
- **Detected method headings:** 3 Method (p. 2); 3 Method (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Policy / value representation | state에서 action과 return estimate를 표현한다 | state/observation과 task context | actor, critic, value, Q 또는 sequence policy를 계산 | policy/value estimate | In this section, we present Decision Transformer, which models trajectories autoregressively with minimal modification to the transformer architecture, as summarized in Figure ... | p. 4 (3 Method), p. 4 (3 Method) |
| Rollout / target construction | interaction에서 update target을 만든다 | state, action, reward, next state | return, advantage, TD target 또는 trajectory statistics를 구성 | training target | The key desiderata in our choice of trajectory representation are that it should enable transformers to learn meaningful patterns and we should ... | p. 4 (3 Method), p. 6 (3 Method) |
| Policy / value update | 목표를 최적화해 다음 policy를 만든다 | target, replay/data와 parameters | gradient, trust region, entropy, replay 또는 constraint update를 수행 | updated policy/controller | In particular, our primary points of comparison are modelfree offline RL algorithms based on TD-learning, since our Decision Transformer architecture is fundamentally ... | p. 6 (3 Method), p. 6 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3 Method - extractive body cue:** As a result, instead of feeding the rewards directly, we feed the model with the returns-to-go bRt = PT t′=t rt′.
- **p. 4 / 3 Method - extractive body cue:** It is nontrivial to model rewards since we would like the model to generate actions based on future desired returns, rather than past rewards.
- **p. 5 / 3 Method - extractive body cue:** After executing the generated action for the current state, we decrement the target return by the achieved reward and repeat until episode termination.
- **p. 5 / 3 Method - extractive body cue:** The prediction head corresponding to the input token st is trained to predict at - either with cross-entropy loss for discrete actions or mean-squared error ...
- **p. 6 / 3 Method - extractive body cue:** 4.1 Atari The Atari benchmark [10] is challenging due to its high-dimensional visual inputs and difficulty of credit assignment arising from the delay between actions ...
- **p. 6 / 3 Method - extractive body cue:** In addition, we also compare against other prior model-free RL algorithms like BEAR [18] and BRAC [19]. • Imitation learning: this regime similarly uses supervised ...
- **Formal bridge:** s_t/o_t -> a_t sampled or selected by πθ -> expected return / constrained return -> task return, success and safe execution.
- **Equation/algorithm anchors:** p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | training, autoregressive, model, sequences, states, actions, returns, reduce, policy, sampling, generative, modeling, denote, state | state 또는 observation, action, reward와 transition history | body cue; exact tensor/frame verify |
| State/latent | training, autoregressive, model, sequences, states, actions, returns, reduce, policy, sampling | policy/value state와 action-selection variable | body cue; notation verify |
| Action/output | Training, dataset, consists, random, walk, trajectories, per-node, returns-to-go, middle, Motivated | action policy와 induced trajectory | body cue; unit/decoder verify |
| Objective/constraint | result, instead, feeding, rewards, directly, feed, model, returns-to-go, bRt, nontrivial | expected return / constrained return | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 1 Introduction - extractive body cue:** By training an autoregressive model on sequences of states, actions, and returns, we reduce policy sampling to autoregressive generative modeling.
- **p. 4 / 2 Preliminaries - extractive body cue:** We use st, at, and rt = R(st, at) to denote the state, action, and reward at timestep t, respectively.
- **p. 4 / 2 Preliminaries - extractive body cue:** The MDP tuple consists of states s ∈S, actions a ∈A, transition dynamics P(s′/s, a), and a reward function r = R(s, a).
- **p. 5 / 3 Method - extractive body cue:** For environments with visual inputs, the state is fed into a convolutional encoder instead of a linear layer.
- **p. 5 / 3 Method - extractive body cue:** We feed the last K timesteps into Decision Transformer, for a total of 3K tokens (one for each modality: return-to-go, state, or action).
- **p. 6 / 3 Method - extractive body cue:** 4.1 Atari The Atari benchmark [10] is challenging due to its high-dimensional visual inputs and difficulty of credit assignment arising from the delay between actions ...
- **p. 3 / 1 Introduction - extractive body cue:** Thus, by combining the tools of sequence modeling with hindsight return information, we achieve policy improvement without the need for dynamic programming. ... goal -2 ...
- **Normalized interface:** observation=state 또는 observation, action, reward와 transition history; state=policy/value state와 action-selection variable; output/action=action policy와 induced trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | rollout/return horizon과 episode termination; exact n-step/discount는 exact value was not selected from the PDF body. | We feed the last K timesteps into Decision Transformer, for a total of 3K tokens (one for each modality: return-to-go, state, or ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 environment step이 분리되며 deployment control rate는 별도 contract다. | Additionally, an embedding for each timestep is learned and added to each token - note this is different than the standard positional ... | Hz/fps, inference time and control rate |
| Memory | replay/rollout buffer와 actor/critic parameters; recurrent history 여부 확인 필요. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | environment interaction, value/policy update와 batch size가 비용을 결정한다. | [13], representing 500 thousand of the 50 million transitions observed by an online DQN agent [20] during training; we report the mean ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3 Method - extractive body cue:** In addition, we also compare against other prior model-free RL algorithms like BEAR [18] and BRAC [19]. • Imitation learning: this regime similarly uses supervised ...
- **p. 6 / 3 Method - extractive body cue:** [13], representing 500 thousand of the 50 million transitions observed by an online DQN agent [20] during training; we report the mean and standard deviation ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** section, present, Decision, Transformer, models, trajectories, autoregressively, minimal, modification, architecture, summarized, Figure, Algorithm, desiderata, choice, trajectory, representation, should, enable, transformers.
- **Relevant PDF headings:** 3 Method (p. 2); 3 Method (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Policy / value representation | To evaluate this, we consider a delayed return version of the D4RL benchmarks where the agent does not receive any rewards along ... | p. 10 (Dataset), p. 10 (Dataset) |
| Rollout / target construction | Table 2: Results for D4RL datasets3. We report the mean and variance for three seeds. Decision Transformer (DT) outperforms conventional RL algorithms ... | p. 7 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Policy / value update | Table 3: Comparison between Decision Transformer (DT) and Percentile Behavior Cloning (%BC). In contrast, when we study low data regimes - such ... | p. 8 (Figure/Table caption), p. 21 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 9 / Figure/Table caption - extractive body cue:** Table 5: Ablation on context length. Decision Transformer (DT) performs better when using a longer context length (K = 50 for Pong, K = 30 ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Comparison between Decision Transformer (DT) and Percentile Behavior Cloning (%BC). In contrast, when we study low data regimes - such as Atari, where ...
- **p. 9 / 5 Discussion - extractive body cue:** TD learning (CQL) cannot effectively propagate Q-values over the long horizons involved and gets poor performance.
- **p. 11 / Dataset - extractive body cue:** This act of optimizing a learned function can exacerbate and exploit any inaccuracies in the value function approximation, causing failures in policy improvement.
- **p. 12 / 7 Conclusion - extractive body cue:** Transformer models can also be used to model the state evolution of trajectory, potentially serving as an alternative to model-based RL, and we hope to ...
- **p. 10 / Dataset - extractive body cue:** Decision Transformer (DT) and imitation learning are minimally affected by the removal of dense rewards, while CQL fails.
- **p. 10 / Dataset - extractive body cue:** To evaluate this, we consider a delayed return version of the D4RL benchmarks where the agent does not receive any rewards along the trajectory, and ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3 Method), p. 4 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 5 (3 Method), p. 5 (3 Method), objective p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method), temporal p. 5 (3 Method), p. 5 (3 Method), p. 7 (3 Method), p. 7 (3 Method), p. 8 (5 Discussion), p. 10 (Dataset).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (21 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** The key desiderata in our choice of trajectory representation are that it should enable transformers to learn meaningful patterns and we should be able to conditionally generate actions at test ... (p. 4, 3 Method).
- **Objective/update evidence:** As a result, instead of feeding the rewards directly, we feed the model with the returns-to-go bRt = PT t′=t rt′. (p. 4, 3 Method).
- **Temporal/runtime evidence:** We feed the last K timesteps into Decision Transformer, for a total of 3K tokens (one for each modality: return-to-go, state, or action). (p. 5, 3 Method).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
