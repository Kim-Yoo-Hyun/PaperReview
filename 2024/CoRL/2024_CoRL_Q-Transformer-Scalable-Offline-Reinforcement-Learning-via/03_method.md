# Method - Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2309.10150; PDF retrieval source: https://arxiv.org/pdf/2309.10150. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3 Background), p. 4 (3 Background), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 5 (3 Background), p. 2 (1 Introduction)): FiLM EfficientNet + Transformer Positional encoding Universal Sentence Encoder Self-Attention Layers (8x) Camera images Language instruction Pick sponge… Q-values for each action bin One-hot action Feed previously predicted action dimen ...

## Method Body Digest

- **p. 4 / 3 Background - extractive body cue:** FiLM EfficientNet + Transformer Positional encoding Universal Sentence Encoder Self-Attention Layers (8x) Camera images Language instruction Pick sponge… Q-values for each action bin One-hot action ...
- **p. 4 / 3 Background - extractive body cue:** 4 Q-Transformer In this section, we introduce Q-Transformer, an architecture for offline Q-learning with Transformer models, which is based on three main ingredients.
- **p. 1 / 1 Introduction - extractive body cue:** Human demonstrations Autonomous data Conservative regularization Autoregressive Q-learning Monte-Carlo returns Mixed quality data environment step action dimension … … Q-values per action dimension Q-Transformer Figure ...
- **p. 2 / 1 Introduction - extractive body cue:** training high-capacity models such as Transformers using RL algorithms has proven more difficult to instantiate effectively at large scale.
- **p. 5 / 3 Background - extractive body cue:** Based on this observation, we propose a simple improvement to Q-Transformer that we found to be quite effective in practice.
- **p. 2 / 1 Introduction - extractive body cue:** We propose a specific regularizer that minimizes values of every action that was not taken in the dataset and show that our method can learn ...
- **p. 1 / Abstract - extractive body cue:** We present several design decisions that enable good performance with offline RL training, and show that Q-Transformer outperforms prior offline RL algorithms and imitation learning ...
- **p. 5 / 3 Background - extractive body cue:** The key insight behind our design is that, rather than minimizing the Q-values on actions not in the data, we can instead regularize these Q-values ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** We propose a specific regularizer that minimizes values of every action that was not taken in the dataset and show that our method can learn ...
- **p. 4 / 3 Background - extractive body cue:** Next, we introduce a particular conservative Q-function regularizer that enables learning from offline datasets.
- **p. 1 / 1 Introduction - extractive body cue:** Human demonstrations Autonomous data Conservative regularization Autoregressive Q-learning Monte-Carlo returns Mixed quality data environment step action dimension … … Q-values per action dimension Q-Transformer Figure ...

## Source Evidence Cues

- **p. 4 / 3 Background - extractive body cue:** FiLM EfficientNet + Transformer Positional encoding Universal Sentence Encoder Self-Attention Layers (8x) Camera images Language instruction Pick sponge… Q-values for each action bin One-hot action ...
- **p. 4 / 3 Background - extractive body cue:** 4 Q-Transformer In this section, we introduce Q-Transformer, an architecture for offline Q-learning with Transformer models, which is based on three main ingredients.
- **p. 1 / 1 Introduction - extractive body cue:** Human demonstrations Autonomous data Conservative regularization Autoregressive Q-learning Monte-Carlo returns Mixed quality data environment step action dimension … … Q-values per action dimension Q-Transformer Figure ...
- **p. 2 / 1 Introduction - extractive body cue:** training high-capacity models such as Transformers using RL algorithms has proven more difficult to instantiate effectively at large scale.
- **p. 5 / 3 Background - extractive body cue:** Based on this observation, we propose a simple improvement to Q-Transformer that we found to be quite effective in practice.
- **p. 2 / 1 Introduction - extractive body cue:** We propose a specific regularizer that minimizes values of every action that was not taken in the dataset and show that our method can learn ...
- **p. 1 / Abstract - extractive body cue:** We present several design decisions that enable good performance with offline RL training, and show that Q-Transformer outperforms prior offline RL algorithms and imitation learning ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Fixed-data support | 온라인 탐색 없이 transition/action 분포를 정의한다 | offline trajectories와 metadata | dataset support, behavior distribution과 task return을 정리 | training batch/support | FiLM EfficientNet + Transformer Positional encoding Universal Sentence Encoder Self-Attention Layers (8x) Camera images Language instruction Pick sponge… Q-values for each action ... | p. 4 (3 Background), p. 4 (3 Background) |
| Value / uncertainty update | dataset 밖 action의 과대추정을 억제한다 | batch transition과 value parameters | conservative, implicit, uncertainty 또는 behavior-regularized update를 수행 | Q/V/uncertainty estimate | 4 Q-Transformer In this section, we introduce Q-Transformer, an architecture for offline Q-learning with Transformer models, which is based on three main ... | p. 4 (3 Background), p. 1 (1 Introduction) |
| Policy extraction / deployment | 학습된 value를 실행 action으로 변환한다 | value와 behavior support | argmax, advantage weighting, sequence decoding 또는 constraint filtering을 적용 | dataset-supported action | Human demonstrations Autonomous data Conservative regularization Autoregressive Q-learning Monte-Carlo returns Mixed quality data environment step action dimension … … Q-values per action ... | p. 1 (1 Introduction), p. 2 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3 Background - extractive body cue:** The key insight behind our design is that, rather than minimizing the Q-values on actions not in the data, we can instead regularize these Q-values ...
- **p. 5 / 3 Background - extractive body cue:** When dealing with sparse rewards R ∈{0, 1}, results in [27] show that the Q-function regularized with a standard conservative objective can take on negative ...
- **p. 3 / 3 Background - extractive body cue:** In RL, we learn policies π that maximizes the expected total reward in a Markov decision process (MDP) with states s, actions a, discount factor ...
- **p. 2 / 1 Introduction - extractive body cue:** We propose a specific regularizer that minimizes values of every action that was not taken in the dataset and show that our method can learn ...
- **p. 1 / 1 Introduction - extractive body cue:** A number of promising recent advances demonstrate the successes of large-scale robotic RL in varied settings, such as robotic grasping and stacking [11, 12], learning ...
- **p. 2 / 1 Introduction - extractive body cue:** Since Transformers model discrete token sequences, we convert the Q-function estimation problem into a discrete token sequence modeling problem, and devise a suitable loss function ...
- **Formal bridge:** dataset transition (s,a,r,s′) -> dataset-supported policy action -> offline value with OOD control -> offline return and deployment safety.
- **Equation/algorithm anchors:** p. 6 (3 Background), p. 2 (1 Introduction), p. 5 (3 Background), p. 5 (3 Background), p. 6 (3 Background), p. 2 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | language, instruction, encoded, Universal, Sentence, Encoder, then, FiLM, EfficientNet, network, together, robot, camera, images | dataset state/observation, action, reward와 return-to-go | body cue; exact tensor/frame verify |
| State/latent | language, instruction, encoded, Universal, Sentence, Encoder, then, FiLM, EfficientNet, network | Q/value 또는 sequence-policy state | body cue; notation verify |
| Action/output | specific, regularizer, minimizes, values, every, action, taken, dataset, learn, narrow | dataset-supported action sequence | body cue; unit/decoder verify |
| Objective/constraint | insight, behind, design, rather, minimizing, Q-values, actions, data, instead, regularize | offline value with OOD control | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3 Background - extractive body cue:** The language instruction is encoded with Universal Sentence Encoder [68] and then fed to FiLM EfficientNet [69, 70] network together with the robot camera images. ...
- **p. 4 / 3 Background - extractive body cue:** FiLM EfficientNet + Transformer Positional encoding Universal Sentence Encoder Self-Attention Layers (8x) Camera images Language instruction Pick sponge… Q-values for each action bin One-hot action ...
- **p. 6 / 3 Background - extractive body cue:** This is because we get a new state and reward only after inferring and executing the whole action as opposed to parts of it, meaning ...
- **p. 3 / 3 Background - extractive body cue:** In RL, we learn policies π that maximizes the expected total reward in a Markov decision process (MDP) with states s, actions a, discount factor ...
- **p. 3 / 3 Background - extractive body cue:** The offline RL setting assumes access to an offline dataset of transitions or episodes, produced by some unknown behavior policy πβ(a/s), but does not assume ...
- **p. 5 / 3 Background - extractive body cue:** Let πβ be the behavioral policy that induced a given dataset D, and let ˜πβ(a/s) = 1 Z(s) · (1.0 -πβ(a/s)) be the distribution over ...
- **p. 1 / 1 Introduction - extractive body cue:** For example, these policies can follow natural language instructions [4, 7], perform multi-stage behaviors [8, 9], and generalize broadly across environments, objects, and even robot ...
- **Normalized interface:** observation=dataset state/observation, action, reward와 return-to-go; state=Q/value 또는 sequence-policy state; output/action=dataset-supported action sequence.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | offline trajectory/discounted return horizon; deployment horizon과 분리한다. | The episodes are on average 35 time steps in length. | episode/sequence/action-chunk boundary |
| Rate / latency | training은 batch update, inference는 environment control tick; exact values 확인 필요. | In this work, we consider tasks with sparse rewards, where a binary reward R ∈{0, 1} (indicating success or failure) is assigned ... | Hz/fps, inference time and control rate |
| Memory | fixed dataset, value/policy parameters와 optional context/history. | Then, for a time window w of state history, we define the Q-value of the action ai t in the i-th dimension ... | window and reset |
| Compute | dataset size, conservative/value update와 sequence/action decoding이 비용을 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / 1 Introduction - extractive body cue:** Human demonstrations Autonomous data Conservative regularization Autoregressive Q-learning Monte-Carlo returns Mixed quality data environment step action dimension … … Q-values per action dimension Q-Transformer Figure ...
- **p. 2 / 1 Introduction - extractive body cue:** training high-capacity models such as Transformers using RL algorithms has proven more difficult to instantiate effectively at large scale.
- **p. 1 / Abstract - extractive body cue:** We present several design decisions that enable good performance with offline RL training, and show that Q-Transformer outperforms prior offline RL algorithms and imitation learning ...
- **p. 8 / 5 Experiments - extractive body cue:** Second, the per-dimension action discretization scheme that we employ may become more cumbersome in higher dimensions (e.g., controlling a humanoid robot), as the sequence length ...
- **p. 6 / 5 Experiments - extractive body cue:** To ensure a fair comparison between Q-Transformer and imitation learning methods, we discard all successful episodes in the autonomously collected data when we train our ...
- **p. 7 / 5 Experiments - extractive body cue:** We also analyze the statistical significance of the results by training with multiple random seeds in Appendix F.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** FiLM, EfficientNet, Transformer, Positional, encoding, Universal, Sentence, Encoder, Self-Attention, Layers, Camera, images, Language, instruction, Pick, sponge, Q-values, action, One-hot, Feed.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Fixed-data support | To evaluate how well Q-Transformer can perform when learning from real-world offline datasets while effectively incorporating autonomously collected failed episodes, we evaluate ... | p. 6 (5 Experiments), p. 8 (5 Experiments) |
| Value / uncertainty update | Q-Transformer has the highest success rate and outperforms both the behavior cloning baseline (RT-1) and offline RL baselines (Decision Transformer, IQL), exceeding ... | p. 7 (5 Experiments), p. 6 (5 Experiments) |
| Policy extraction / deployment | Q-Transformer has the highest success rate and outperforms both the behavior cloning baseline (RT-1) and offline RL baselines (Decision Transformer, IQL), exceeding ... | p. 7 (5 Experiments), p. 8 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / 5 Experiments - extractive body cue:** Training steps Success rate Q-Transformer with softmax Q-Transformer without conservatism Q-Transformer (ours) Q-Transformer without Monte-Carlo n-step ablation n-step 1-step 1-step # of gradient steps 137480 ...
- **p. 7 / 5 Experiments - extractive body cue:** 5.3 Ablations We perform a series of ablations of our method design choices in simulation, with results presented in Figure 6 (left).
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Left: Ablations: changing to softmax conservatism decreases performance. Removing MC returns or conservatism completely collapse performance. Top Right: The n-step return ver- sion ...
- **p. 7 / 5 Experiments - extractive body cue:** When removing conservatism entirely, we observe that performance collapses.
- **p. 8 / 5 Experiments - extractive body cue:** First, we focus on sparse binary reward tasks corresponding to success or failure for each trial.
- **p. 8 / 5 Experiments - extractive body cue:** Our framework does have several limitations.
- **p. 6 / 3 Background - extractive body cue:** Although this does not change convergence, including this maximization speeds up learning (see Section 5.3).

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3 Background), p. 4 (3 Background), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 5 (3 Background), p. 2 (1 Introduction), objective p. 5 (3 Background), p. 5 (3 Background), p. 3 (3 Background), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), temporal p. 6 (5 Experiments), p. 4 (3 Background), p. 4 (3 Background), p. 8 (5 Experiments), p. 8 (5 Experiments), p. 2 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** We present several design decisions that enable good performance with offline RL training, and show that Q-Transformer outperforms prior offline RL algorithms and imitation learning techniques on a large diverse ... (p. 1, Abstract).
- **Objective/update evidence:** The reward is only applied on the last dimension (second line in the equation), as we do not receive any reward before executing the whole action. (p. 5, 3 Background).
- **Temporal/runtime evidence:** The episodes are on average 35 time steps in length. (p. 6, 5 Experiments).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
