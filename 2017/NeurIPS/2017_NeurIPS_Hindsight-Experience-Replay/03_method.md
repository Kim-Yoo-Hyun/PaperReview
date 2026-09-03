# Method - Hindsight Experience Replay

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1707.01495; PDF retrieval source: https://arxiv.org/pdf/1707.01495. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (2 Background), p. 2 (2 Background), p. 2 (1 Introduction), p. 3 (2 Background), p. 3 (2 Background), p. 4 (2 Background)): Notice that the goal being pursued influences the agent's actions but not the environment dynamics and therefore we can replay each trajectory with an arbitrary goal assuming that we use ...

## Method Body Digest

- **p. 4 / 2 Background - extractive body cue:** Notice that the goal being pursued influences the agent's actions but not the environment dynamics and therefore we can replay each trajectory with an arbitrary ...
- **p. 2 / 2 Background - extractive body cue:** In this section we introduce reinforcement learning formalism used in the paper as well as RL algorithms we use in our experiments.
- **p. 2 / 1 Introduction - extractive body cue:** In this paper we introduce a technique called Hindsight Experience Replay (HER) which allows the algorithm to perform exactly this kind of reasoning and can ...
- **p. 3 / 2 Background - extractive body cue:** 2.3 Deep Deterministic Policy Gradients (DDPG) Deep Deterministic Policy Gradients (DDPG) (Lillicrap et al., 2015) is a model-free RL algorithm for continuous action spaces.
- **p. 3 / 2 Background - extractive body cue:** In DDPG we maintain two neural networks: a target policy (also called an actor) π : S →A and an action-value function approximator (called the ...
- **p. 4 / 2 Background - extractive body cue:** In the simplest version of our algorithm we replay each trajectory with the goal m(sT ), i.e. the goal which is achieved in the final ...
- **p. 1 / Abstract - extractive body cue:** It can be combined with an arbitrary off-policy RL algorithm and may be seen as a form of implicit curriculum.
- **p. 2 / 2 Background - extractive body cue:** The network is trained using mini-batch gradient descent on the loss L which encourages the approximated Q-function to satisfy the Bellman equation: L = E ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** In this paper we introduce a technique called Hindsight Experience Replay (HER) which allows the algorithm to perform exactly this kind of reasoning and can ...
- **p. 1 / Abstract - extractive body cue:** We present a novel technique called Hindsight Experience Replay which allows sample-efficient learning from rewards which are sparse and binary and therefore avoid the need ...
- **p. 4 / 2 Background - extractive body cue:** In order to solve this problem we introduce the technique of Hindsight Experience Replay which is the crux of our approach.

## Source Evidence Cues

- **p. 4 / 2 Background - extractive body cue:** Notice that the goal being pursued influences the agent's actions but not the environment dynamics and therefore we can replay each trajectory with an arbitrary ...
- **p. 2 / 2 Background - extractive body cue:** In this section we introduce reinforcement learning formalism used in the paper as well as RL algorithms we use in our experiments.
- **p. 2 / 1 Introduction - extractive body cue:** In this paper we introduce a technique called Hindsight Experience Replay (HER) which allows the algorithm to perform exactly this kind of reasoning and can ...
- **p. 3 / 2 Background - extractive body cue:** 2.3 Deep Deterministic Policy Gradients (DDPG) Deep Deterministic Policy Gradients (DDPG) (Lillicrap et al., 2015) is a model-free RL algorithm for continuous action spaces.
- **p. 3 / 2 Background - extractive body cue:** In DDPG we maintain two neural networks: a target policy (also called an actor) π : S →A and an action-value function approximator (called the ...
- **p. 4 / 2 Background - extractive body cue:** In the simplest version of our algorithm we replay each trajectory with the goal m(sT ), i.e. the goal which is achieved in the final ...
- **p. 1 / Abstract - extractive body cue:** It can be combined with an arbitrary off-policy RL algorithm and may be seen as a form of implicit curriculum.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Policy / value representation | state에서 action과 return estimate를 표현한다 | state/observation과 task context | actor, critic, value, Q 또는 sequence policy를 계산 | policy/value estimate | Notice that the goal being pursued influences the agent's actions but not the environment dynamics and therefore we can replay each trajectory ... | p. 4 (2 Background), p. 2 (2 Background) |
| Rollout / target construction | interaction에서 update target을 만든다 | state, action, reward, next state | return, advantage, TD target 또는 trajectory statistics를 구성 | training target | In this section we introduce reinforcement learning formalism used in the paper as well as RL algorithms we use in our experiments. | p. 2 (2 Background), p. 2 (1 Introduction) |
| Policy / value update | 목표를 최적화해 다음 policy를 만든다 | target, replay/data와 parameters | gradient, trust region, entropy, replay 또는 constraint update를 수행 | updated policy/controller | In this paper we introduce a technique called Hindsight Experience Replay (HER) which allows the algorithm to perform exactly this kind of ... | p. 2 (1 Introduction), p. 3 (2 Background) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 2 Background - extractive body cue:** The network is trained using mini-batch gradient descent on the loss L which encourages the approximated Q-function to satisfy the Bellman equation: L = E ...
- **p. 1 / 1 Introduction - extractive body cue:** (2017) use a cost function consisting of five relatively complicated terms which need to be carefully weighted in order to train a policy for stacking ...
- **p. 1 / 1 Introduction - extractive body cue:** However, a common challenge, especially for robotics, is the need to engineer a reward function that not only reflects the task at hand but is ...
- **p. 2 / 2 Background - extractive body cue:** The agent's goal is to maximize its expected return Es0[R0/s0].
- **p. 3 / 2 Background - extractive body cue:** Every goal g ∈G corresponds to some reward function rg : S × A →R.
- **p. 3 / 2 Background - extractive body cue:** We investigate the results of reward shaping experimentally in Sec.
- **Formal bridge:** s_t/o_t -> a_t sampled or selected by πθ -> expected return / constrained return -> task return, success and safe execution.
- **Equation/algorithm anchors:** p. 2 (2 Background), p. 2 (2 Background), p. 3 (2 Background), p. 3 (2 Background).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | deterministic, policy, mapping, states, actions, setup, possible, train, approximator, Q-function, direct, bootstrapping, Bellman, equation | state 또는 observation, action, reward와 transition history | body cue; exact tensor/frame verify |
| State/latent | deterministic, policy, mapping, states, actions, setup, possible, train, approximator, Q-function | policy/value state와 action-selection variable | body cue; notation verify |
| Action/output | introduce, technique, called, Hindsight, Experience, Replay, HER, allows, algorithm, perform | action policy와 induced trajectory | body cue; unit/decoder verify |
| Objective/constraint | network, trained, mini-batch, gradient, descent, loss, encourages, approximated, Q-function, satisfy | expected return / constrained return | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 2 Background - extractive body cue:** A deterministic policy is a mapping from states to actions: π : S →A.
- **p. 3 / 2 Background - extractive body cue:** (2015a) show that in this setup it is possible to train an approximator to the Q-function using direct bootstrapping from the Bellman equation (just like ...
- **p. 2 / 1 Introduction - extractive body cue:** Our approach is based on training universal policies (Schaul et al., 2015a) which take as input not only the current state, but also a goal ...
- **p. 3 / 2 Background - extractive body cue:** The Q-function now depends not only on a state-action pair but also on a goal Qπ(st, at, g) = E[Rt/st, at, g].
- **p. 4 / 2 Background - extractive body cue:** A universal policy can be trained using an arbitrary RL algorithm by sampling goals and initial states from some distributions, running the agent for some ...
- **p. 4 / 2 Background - extractive body cue:** Notice that the goal being pursued influences the agent's actions but not the environment dynamics and therefore we can replay each trajectory with an arbitrary ...
- **p. 1 / Abstract - extractive body cue:** It can be combined with an arbitrary off-policy RL algorithm and may be seen as a form of implicit curriculum.
- **Normalized interface:** observation=state 또는 observation, action, reward와 transition history; state=policy/value state와 action-selection variable; output/action=action policy와 induced trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | rollout/return horizon과 episode termination; exact n-step/discount는 exact value was not selected from the PDF body. | 4.5) 0 50 100 150 200 epoch number (every epoch = 800 episodes = 800x50 timesteps) 0% 20% 40% 60% 80% 100% ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 environment step이 분리되며 deployment control rate는 별도 contract다. | Three dimensions specify the desired relative gripper position at the next timestep. | Hz/fps, inference time and control rate |
| Memory | replay/rollout buffer와 actor/critic parameters; recurrent history 여부 확인 필요. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | environment interaction, value/policy update와 batch size가 비용을 결정한다. | 4.5) 0 50 100 150 200 epoch number (every epoch = 800 episodes = 800x50 timesteps) 0% 20% 40% 60% 80% 100% ... | hardware, batch and throughput |

## Training vs Inference

- **p. 9 / 4 Experiments - extractive body cue:** The top row shows the highest (across the training epochs) test performance and the bottom row shows the average test performance across all training epochs.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Notice, goal, being, pursued, influences, agent, actions, environment, dynamics, therefore, replay, trajectory, arbitrary, assuming, off-policy, algorithm, like, DQN, Mnih, DDPG.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Policy / value representation | We decided to use manipulation environments based on an existing hardware robot to ensure that the challenges we face correspond as closely ... | p. 5 (4 Experiments), p. 10 (4 Experiments) |
| Rollout / target construction | 4.2 we compare the performance of DDPG with and without HER. | p. 5 (4 Experiments), p. 5 (4 Experiments) |
| Policy / value update | 4.3 we check if HER improves performance in the single-goal setup. | p. 5 (4 Experiments), p. 7 (4 Experiments) |

## Failure and Ablation Link

- **p. 8 / 4 Experiments - extractive body cue:** In this section we check how the performance of DDPG with and without HER changes if we replace this reward with one which is shaped.
- **p. 5 / 4 Experiments - extractive body cue:** 4.6 that the trained policies perform well on the physical robot without any finetuning.
- **p. 6 / 4 Experiments - extractive body cue:** 3This was necessary because we could not successfully train any policies for this task without using the demonstration state.
- **p. 6 / 4 Experiments - extractive body cue:** We have later discovered that training is possible without this trick if only the goal position is sometimes on the table and sometimes in the ...
- **p. 7 / 4 Experiments - extractive body cue:** 7We also evaluated DQN (without HER) on our tasks and it was not able to solve any of them.
- **p. 7 / 4 Experiments - extractive body cue:** In order to verify if HER improves performance we evaluate DDPG with and without HER on all 3 tasks.
- **p. 9 / 4 Experiments - extractive body cue:** 1 2 4 8 16 all 0.0 0.2 0.4 0.6 0.8 1.0 highest success rate pushing no HER final random episode future 1 2 4 ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (2 Background), p. 2 (2 Background), p. 2 (1 Introduction), p. 3 (2 Background), p. 3 (2 Background), p. 4 (2 Background), objective p. 2 (2 Background), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (2 Background), p. 3 (2 Background), p. 3 (2 Background), temporal p. 7 (4 Experiments), p. 7 (4 Experiments), p. 4 (2 Background), p. 2 (2 Background), p. 6 (4 Experiments), p. 8 (4 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Notice that the goal being pursued influences the agent's actions but not the environment dynamics and therefore we can replay each trajectory with an arbitrary goal assuming that we use ... (p. 4, 2 Background).
- **Objective/update evidence:** The network is trained using mini-batch gradient descent on the loss L which encourages the approximated Q-function to satisfy the Bellman equation: L = E (Q(st, at) -yt)2, where yt ... (p. 2, 2 Background).
- **Temporal/runtime evidence:** To make exploration in this task easier we recorded a single state in which the box is grasped and start half of the training episodes from this state3. (p. 6, 4 Experiments).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
