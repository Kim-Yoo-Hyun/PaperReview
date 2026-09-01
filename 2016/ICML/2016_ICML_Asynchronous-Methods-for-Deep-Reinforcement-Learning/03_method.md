# Method - Asynchronous Methods for Deep Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v48/mniha16.html; PDF retrieval source: https://proceedings.mlr.press/v48/mniha16.html. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 1 (Abstract), p. 3 (4. Asynchronous RL Framework), p. 4 (4. Asynchronous RL Framework), p. 1 (Abstract), p. 3 (4. Asynchronous RL Framework), p. 4 (4. Asynchronous RL Framework)): We propose a conceptually simple and lightweight framework for deep reinforcement learning that uses asynchronous gradient descent for optimization of deep neural network controllers.

## Method Body Digest

- **p. 1 / Abstract - extractive PDF cue:** We propose a conceptually simple and lightweight framework for deep reinforcement learning that uses asynchronous gradient descent for optimization of deep neural network controllers.
- **p. 3 / 4. Asynchronous RL Framework - extractive PDF cue:** Initialize thread step counter t ←0 Initialize target network weights θ-←θ Initialize network gradients dθ ←0 Get initial state s repeat Take action a with ...
- **p. 4 / 4. Asynchronous RL Framework - extractive PDF cue:** In order to compute a single update, the algorithm first selects actions using its exploration policy for up to tmax steps or until a terminal ...
- **p. 1 / Abstract - extractive PDF cue:** We present asynchronous variants of four standard reinforcement learning algorithms and show that parallel actor-learners have a stabilizing effect on training allowing all four methods ...
- **p. 3 / 4. Asynchronous RL Framework - extractive PDF cue:** We use a shared and slowly changing target network in computing the Q-learning loss, as was proposed in the DQN training method.
- **p. 4 / 4. Asynchronous RL Framework - extractive PDF cue:** The algorithm then computes gradients for n-step Q-learning updates for each of the state-action pairs encountered since the last update.
- **p. 2 / 3. Reinforcement Learning Background - extractive PDF cue:** In value-based model-free reinforcement learning methods, the action value function is represented using a function approximator, such as a neural network.
- **p. 2 / 3. Reinforcement Learning Background - extractive PDF cue:** In one-step Q-learning, the parameters θ of the action value function Q(s, a; θ) are learned by iteratively minimizing a sequence of loss functions, where ...

## Design Rationale

- **p. 1 / Abstract - extractive PDF cue:** We present asynchronous variants of four standard reinforcement learning algorithms and show that parallel actor-learners have a stabilizing effect on training allowing all four methods ...
- **p. 1 / Abstract - extractive PDF cue:** We propose a conceptually simple and lightweight framework for deep reinforcement learning that uses asynchronous gradient descent for optimization of deep neural network controllers.
- **p. 3 / 4. Asynchronous RL Framework - extractive PDF cue:** Keeping the learners on a single machine removes the communication costs of sending gradients and parameters and enables us to use Hogwild!

## Source Evidence Cues

- **p. 1 / Abstract - extractive PDF cue:** We propose a conceptually simple and lightweight framework for deep reinforcement learning that uses asynchronous gradient descent for optimization of deep neural network controllers.
- **p. 3 / 4. Asynchronous RL Framework - extractive PDF cue:** Initialize thread step counter t ←0 Initialize target network weights θ-←θ Initialize network gradients dθ ←0 Get initial state s repeat Take action a with ...
- **p. 4 / 4. Asynchronous RL Framework - extractive PDF cue:** In order to compute a single update, the algorithm first selects actions using its exploration policy for up to tmax steps or until a terminal ...
- **p. 1 / Abstract - extractive PDF cue:** We present asynchronous variants of four standard reinforcement learning algorithms and show that parallel actor-learners have a stabilizing effect on training allowing all four methods ...
- **p. 3 / 4. Asynchronous RL Framework - extractive PDF cue:** We use a shared and slowly changing target network in computing the Q-learning loss, as was proposed in the DQN training method.
- **p. 4 / 4. Asynchronous RL Framework - extractive PDF cue:** The algorithm then computes gradients for n-step Q-learning updates for each of the state-action pairs encountered since the last update.
- **p. 2 / 3. Reinforcement Learning Background - extractive PDF cue:** In value-based model-free reinforcement learning methods, the action value function is represented using a function approximator, such as a neural network.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Policy / value representation | state에서 action과 return estimate를 표현한다 | state/observation과 task context | actor, critic, value, Q 또는 sequence policy를 계산 | policy/value estimate | We propose a conceptually simple and lightweight framework for deep reinforcement learning that uses asynchronous gradient descent for optimization of deep neural ... | p. 1 (Abstract), p. 3 (4. Asynchronous RL Framework) |
| Rollout / target construction | interaction에서 update target을 만든다 | state, action, reward, next state | return, advantage, TD target 또는 trajectory statistics를 구성 | training target | Initialize thread step counter t ←0 Initialize target network weights θ-←θ Initialize network gradients dθ ←0 Get initial state s repeat Take ... | p. 3 (4. Asynchronous RL Framework), p. 4 (4. Asynchronous RL Framework) |
| Policy / value update | 목표를 최적화해 다음 policy를 만든다 | target, replay/data와 parameters | gradient, trust region, entropy, replay 또는 constraint update를 수행 | updated policy/controller | In order to compute a single update, the algorithm first selects actions using its exploration policy for up to tmax steps or ... | p. 4 (4. Asynchronous RL Framework), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 4. Asynchronous RL Framework - extractive PDF cue:** Initialize thread step counter t ←0 Initialize target network weights θ-←θ Initialize network gradients dθ ←0 Get initial state s repeat Take action a with ...
- **p. 2 / 3. Reinforcement Learning Background - extractive PDF cue:** In one-step Q-learning, the parameters θ of the action value function Q(s, a; θ) are learned by iteratively minimizing a sequence of loss functions, where ...
- **p. 4 / 4. Asynchronous RL Framework - extractive PDF cue:** The gradient of the full objective function including the entropy regularization term with respect to the policy parameters takes the form ∇θ′ log π(at/st; θ′)(Rt ...
- **p. 3 / 4. Asynchronous RL Framework - extractive PDF cue:** Each thread interacts with its own copy of the environment and at each step computes a gradient of the Q-learning loss.
- **p. 1 / Abstract - extractive PDF cue:** We propose a conceptually simple and lightweight framework for deep reinforcement learning that uses asynchronous gradient descent for optimization of deep neural network controllers.
- **p. 2 / 3. Reinforcement Learning Background - extractive PDF cue:** The goal of the agent is to maximize the expected return from each state st.
- **Formal bridge:** s_t/o_t -> a_t sampled or selected by πθ -> expected return / constrained return -> task return, success and safe execution.
- **Equation/algorithm anchors:** p. 3 (4. Asynchronous RL Framework), p. 4 (4. Asynchronous RL Framework), p. 2 (3. Reinforcement Learning Background), p. 3 (3. Reinforcement Learning Background), p. 4 (4. Asynchronous RL Framework), p. 1 (Abstract).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | action, value, Rt/st, expected, return, selecting, state, following, policy, optimal, function, gives, maximum, achievable | state 또는 observation, action, reward와 transition history | body cue; exact tensor/frame verify |
| State/latent | action, value, Rt/st, expected, return, selecting, state, following, policy, optimal | policy/value state와 action-selection variable | body cue; notation verify |
| Action/output | present, asynchronous, variants, four, standard, reinforcement, learning, algorithms, parallel, actor-learners | action policy와 induced trajectory | body cue; unit/decoder verify |
| Objective/constraint | Initialize, thread, step, counter, target, network, weights, gradients, Get, initial | expected return / constrained return | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 3. Reinforcement Learning Background - extractive PDF cue:** The action value Qπ(s, a) = E [Rt/st = s, a] is the expected return for selecting action a in state s and following policy ...
- **p. 2 / 3. Reinforcement Learning Background - extractive PDF cue:** The optimal value function Q∗(s, a) = maxπ Qπ(s, a) gives the maximum action value for state s and action a achievable by any policy.
- **p. 3 / 3. Reinforcement Learning Background - extractive PDF cue:** When an approximate value function is used as the baseline, the quantity Rt -bt used to scale the policy gradient can be seen as an ...
- **p. 3 / 4. Asynchronous RL Framework - extractive PDF cue:** Initialize thread step counter t ←0 Initialize target network weights θ-←θ Initialize network gradients dθ ←0 Get initial state s repeat Take action a with ...
- **p. 4 / 4. Asynchronous RL Framework - extractive PDF cue:** The policy and the value function are updated after every tmax actions or when a terminal state is reached.
- **p. 4 / 4. Asynchronous RL Framework - extractive PDF cue:** In order to compute a single update, the algorithm first selects actions using its exploration policy for up to tmax steps or until a terminal ...
- **p. 1 / 48. Copyright 2016 by the author(s) - extractive PDF cue:** However, experience replay has several drawbacks: it uses more memory and computation per real interaction; and it requires off-policy learning algorithms that can update from ...
- **Normalized interface:** observation=state 또는 observation, action, reward와 transition history; state=policy/value state와 action-selection variable; output/action=action policy와 induced trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | rollout/return horizon과 episode termination; exact n-step/discount는 exact value not recovered from the selected body cues. | The return Rt = P∞ k=0 γkrt+k is the total accumulated return from time step t with discount factor γ ∈(0, 1]. | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 environment step이 분리되며 deployment control rate는 별도 contract다. | We consider the standard reinforcement learning setting where an agent interacts with an environment E over a number of discrete time steps. | Hz/fps, inference time and control rate |
| Memory | replay/rollout buffer와 actor/critic parameters; recurrent history 여부 확인 필요. | By storing the agent's data in an experience replay memory, the data can be batched (Riedmiller, 2005; Schulman et al., 2015a) or ... | window and reset |
| Compute | environment interaction, value/policy update와 batch size가 비용을 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Abstract - extractive PDF cue:** We present asynchronous variants of four standard reinforcement learning algorithms and show that parallel actor-learners have a stabilizing effect on training allowing all four methods ...
- **p. 3 / 4. Asynchronous RL Framework - extractive PDF cue:** We use a shared and slowly changing target network in computing the Q-learning loss, as was proposed in the DQN training method.
- **p. 5 / 5.1. Atari 2600 Games - extractive PDF cue:** A3C significantly improves on state-of-the-art the average score over 57 games in half the training time of the other methods while using only 16 CPU ...
- **p. 5 / 5.1. Atari 2600 Games - extractive PDF cue:** We additionally used the final network weights for evaluation to make the results more comparable to the original results Method Training Time Mean Median DQN ...
- **p. 6 / 5.5. Scalability and Data Efficiency - extractive PDF cue:** We analyzed the effectiveness of our proposed framework by looking at how the training time and data efficiency changes with the number of parallel actor-learners.
- **p. 7 / 5.6. Robustness and Stability - extractive PDF cue:** For each of the four algorithms we trained models on five games (Breakout, Beamrider, Pong, Q*bert, Space Invaders) using 50 different learning rates and random ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** conceptually, simple, lightweight, framework, deep, reinforcement, learning, uses, asynchronous, gradient, descent, optimization, neural, network, controllers, Initialize, thread, step, counter, target.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Policy / value representation | This is one of the most commonly used benchmark environments for RL algorithms. | p. 4 (5. Experiments), p. 4 (5. Experiments) |
| Rollout / target construction | We also compared the four asynchronous methods on the TORCS 3D car racing game (Wymann et al., 2013). | p. 5 (5.2. TORCS Car Racing Simulator), p. 5 (5.1. Atari 2600 Games) |
| Policy / value update | A3C significantly improves on state-of-the-art the average score over 57 games in half the training time of the other methods while using ... | p. 5 (5.1. Atari 2600 Games), p. 5 (5.1. Atari 2600 Games) |

## Failure and Ablation Link

- **p. 6 / 5.5. Scalability and Data Efficiency - extractive PDF cue:** We believe this is due to positive effect of multiple threads to reduce the bias in one-step methods.
- **p. 6 / 5.2. TORCS Car Racing Simulator - extractive PDF cue:** We performed experiments using four different settings - the agent controlling a slow car with and without opponent bots, and the agent controlling a fast ...
- **p. 7 / 6. Conclusions and Discussion - extractive PDF cue:** While this shows that stable online Q-learning is possible without experience replay, which was used for this purpose in DQN, it does not mean that ...
- **p. 6 / 5.5. Scalability and Data Efficiency - extractive PDF cue:** Somewhat surprisingly, asynchronous one-step Q-learning and Sarsa algorithms exhibit superlinear speedups that cannot be explained by purely computational gains.
- **p. 7 / 5.6. Robustness and Stability - extractive PDF cue:** Finally, we analyzed the stability and robustness of the four proposed asynchronous algorithms.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 1 (Abstract), p. 3 (4. Asynchronous RL Framework), p. 4 (4. Asynchronous RL Framework), p. 1 (Abstract), p. 3 (4. Asynchronous RL Framework), p. 4 (4. Asynchronous RL Framework), objective p. 3 (4. Asynchronous RL Framework), p. 2 (3. Reinforcement Learning Background), p. 4 (4. Asynchronous RL Framework), p. 3 (4. Asynchronous RL Framework), p. 1 (Abstract), p. 2 (3. Reinforcement Learning Background), temporal p. 2 (3. Reinforcement Learning Background), p. 2 (3. Reinforcement Learning Background), p. 1 (1. Introduction), p. 1 (48. Copyright 2016 by the author(s)), p. 4 (5. Experiments), p. 5 (5.2. TORCS Car Racing Simulator).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
