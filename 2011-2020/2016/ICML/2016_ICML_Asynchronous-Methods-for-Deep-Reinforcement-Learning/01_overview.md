# Asynchronous Methods for Deep Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v48/mniha16.html.
> PDF retrieval source: https://proceedings.mlr.press/v48/mniha16.html. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2016 / ICML
- Authors: Volodymyr Mnih, Adria Puigdomenech Badia, Mehdi Mirza, Alex Graves, Timothy Lillicrap, Tim Harley, David Silver, Koray Kavukcuoglu
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Robotics, Reinforcement Learning, actor-critic, A3C
- Official paper: https://proceedings.mlr.press/v48/mniha16.html
- Full-text retrieval: https://proceedings.mlr.press/v48/mniha16.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://proceedings.mlr.press/v48/mniha16.pdf) 기준이다.

## Why This Paper Is Here

이 연구는 병렬로 환경과 상호작용하는 여러 학습자가 공유 신경망을 비동기적으로 갱신하는 심층 강화학습을 제안한다. [PDF 1쪽](https://proceedings.mlr.press/v48/mniha16.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We propose a conceptually simple and lightweight framework for deep reinforcement learning that uses asynchronous gradient descent for optimization of deep neural network controllers.
- **p. 1 / Abstract - extractive body cue:** We present asynchronous variants of four standard reinforcement learning algorithms and show that parallel actor-learners have a stabilizing effect on training allowing all four methods ...
- **p. 1 / Abstract - extractive body cue:** The best performing method, an asynchronous variant of actor-critic, surpasses the current state-of-the-art on the Atari domain while training for half the time on a ...
- **p. 1 / Abstract - extractive body cue:** Furthermore, we show that asynchronous actor-critic succeeds on a wide variety of continuous motor control problems as well as on a new task of navigating ...
- **p. 1 / 1. Introduction - extractive body cue:** Deep neural networks provide rich representations that can enable reinforcement learning (RL) algorithms to perform effectively.

## Core Idea

- **p. 1 / Abstract - extractive body cue:** We present asynchronous variants of four standard reinforcement learning algorithms and show that parallel actor-learners have a stabilizing effect on training allowing all four methods ...
- **p. 1 / Abstract - extractive body cue:** We propose a conceptually simple and lightweight framework for deep reinforcement learning that uses asynchronous gradient descent for optimization of deep neural network controllers.
- **p. 3 / 4. Asynchronous RL Framework - extractive body cue:** Keeping the learners on a single machine removes the communication costs of sending gradients and parameters and enables us to use Hogwild!
- **p. 3 / 4. Asynchronous RL Framework - extractive body cue:** Initialize thread step counter t ←0 Initialize target network weights θ-←θ Initialize network gradients dθ ←0 Get initial state s repeat Take action a with ...
- **p. 4 / 4. Asynchronous RL Framework - extractive body cue:** In order to compute a single update, the algorithm first selects actions using its exploration policy for up to tmax steps or until a terminal ...
- **p. 3 / 4. Asynchronous RL Framework - extractive body cue:** We use a shared and slowly changing target network in computing the Q-learning loss, as was proposed in the DQN training method.
- **p. 4 / 4. Asynchronous RL Framework - extractive body cue:** The algorithm then computes gradients for n-step Q-learning updates for each of the state-action pairs encountered since the last update.
- **p. 2 / 3. Reinforcement Learning Background - extractive body cue:** In value-based model-free reinforcement learning methods, the action value function is represented using a function approximator, such as a neural network.

## Observation, State, and Output Interface

여러 actor-learner가 공유 파라미터를 비동기로 갱신한다. Atari에서 여러 알고리즘을 비교하고 A3C를 MuJoCo의 상태 또는 영상 조건 제어와 Labyrinth의 RGB 미로 탐색에 적용했다. [PDF 5쪽](https://proceedings.mlr.press/v48/mniha16.pdf#page=5) · [PDF 6쪽](https://proceedings.mlr.press/v48/mniha16.pdf#page=6)

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The action value Qπ(s, a) = E [Rt/st = s, a] is the expected return for selecting action a in state s and following policy π. | 환경별 물리 상태 또는 픽셀, 미로의 RGB 관측 및 보상 | p. 2 (3. Reinforcement Learning Background), p. 2 (3. Reinforcement Learning Background) |
| State/latent | action, value, Rt/st, expected, return, selecting, state, following, policy, optimal, function, gives | 병렬 학습자가 공유하는 정책·가치 파라미터 | p. 2 (3. Reinforcement Learning Background), p. 2 (3. Reinforcement Learning Background), p. 3 (3. Reinforcement Learning Background) |
| Output/action | The optimal value function Q∗(s, a) = maxπ Qπ(s, a) gives the maximum action value for state s and action a achievable by any policy. | 이산 또는 연속 환경 행동 | p. 2 (3. Reinforcement Learning Background), p. 3 (3. Reinforcement Learning Background), p. 3 (4. Asynchronous RL Framework) |
| Objective/outcome | Initialize thread step counter t ←0 Initialize target network weights θ-←θ Initialize network gradients dθ ←0 Get initial state s repeat Take action a with ϵ-greedy policy based on Q(s, a; θ) ... | 학습 시간과 환경별 점수·누적 보상 | p. 3 (4. Asynchronous RL Framework), p. 2 (3. Reinforcement Learning Background), p. 4 (4. Asynchronous RL Framework) |

## Main Claims and Actual Contribution

- 가치 기반 기법 및 actor–critic의 비동기 버전을 설계하고 서로 다른 학습자가 수집한 궤적으로 공유 매개변수를 갱신한다. [PDF 3쪽](https://proceedings.mlr.press/v48/mniha16.pdf#page=3) · [PDF 4쪽](https://proceedings.mlr.press/v48/mniha16.pdf#page=4)
- Atari의 학습 시간과 점수를 비교하고 비동기 actor–critic을 연속 제어와 시각적 미로 탐색에도 평가했다. [PDF 5쪽](https://proceedings.mlr.press/v48/mniha16.pdf#page=5) · [PDF 6쪽](https://proceedings.mlr.press/v48/mniha16.pdf#page=6) · [PDF 7쪽](https://proceedings.mlr.press/v48/mniha16.pdf#page=7) · [PDF 8쪽](https://proceedings.mlr.press/v48/mniha16.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 5 (5.1. Atari 2600 Games), p. 5 (5.1. Atari 2600 Games) |
| Embodiment/environment | This is one of the most commonly used benchmark environments for RL algorithms. | hardware/simulator version and reset protocol | p. 4 (5. Experiments), p. 4 (5. Experiments) |
| Dataset/benchmark | MuJoCo (Todorov, 2015) is a physics simulator for evaluating agents on continuous motor control tasks with contact dynamics. | role, split, size and leakage | p. 4 (5. Experiments), p. 4 (5. Experiments), p. 5 (5. Experiments), p. 6 (5.3. Continuous Action Control Using the MuJoCo) |
| Metric | Labyrinth is a new 3D environment where the agent must learn to find rewards in randomly generated mazes from a visual input. | definition, denominator, direction and uncertainty | p. 5 (5. Experiments), p. 6 (5.4. Labyrinth), p. 6 (5.4. Labyrinth) |
| Baseline/ablation | We also compared the four asynchronous methods on the TORCS 3D car racing game (Wymann et al., 2013). | fair input/data/compute/action matching | p. 5 (5.2. TORCS Car Racing Simulator), p. 5 (5.1. Atari 2600 Games), p. 4 (5. Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 6. Conclusions and Discussion - extractive body cue:** While this shows that stable online Q-learning is possible without experience replay, which was used for this purpose in DQN, it does not mean that ...
- **p. 6 / 5.5. Scalability and Data Efficiency - extractive body cue:** Somewhat surprisingly, asynchronous one-step Q-learning and Sarsa algorithms exhibit superlinear speedups that cannot be explained by purely computational gains.
- **p. 7 / 5.6. Robustness and Stability - extractive body cue:** Finally, we analyzed the stability and robustness of the four proposed asynchronous algorithms.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (Abstract), p. 3 (4. Asynchronous RL Framework), p. 4 (4. Asynchronous RL Framework)이다.
