# Evaluation - Asynchronous Methods for Deep Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v48/mniha16.html; PDF retrieval source: https://proceedings.mlr.press/v48/mniha16.html. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (5.1. Atari 2600 Games), p. 5 (5.1. Atari 2600 Games), p. 6 (5.5. Scalability and Data Efficiency), p. 6 (5.5. Scalability and Data Efficiency), p. 4 (5. Experiments), p. 7 (5.5. Scalability and Data Efficiency)): A3C significantly improves on state-of-the-art the average score over 57 games in half the training time of the other methods while using only 16 CPU cores and no GPU.

## Evaluation Body Digest

- **p. 4 / 5. Experiments - extractive PDF cue:** This is one of the most commonly used benchmark environments for RL algorithms.
- **p. 4 / 5. Experiments - extractive PDF cue:** We perform most of our experiments using the Arcade Learning Environment (Bellemare et al., 2012), which provides a simulator for Atari 2600 games.
- **p. 5 / 5. Experiments - extractive PDF cue:** MuJoCo (Todorov, 2015) is a physics simulator for evaluating agents on continuous motor control tasks with contact dynamics.
- **p. 6 / 5.3. Continuous Action Control Using the MuJoCo - extractive PDF cue:** Physics Simulator We also examined a set of tasks where the action space is continuous.
- **p. 6 / 5.4. Labyrinth - extractive PDF cue:** This task is much more challenging than the TORCS driving domain because the agent is faced with a new maze in each episode and must ...
- **p. 5 / 5. Experiments - extractive PDF cue:** Labyrinth is a new 3D environment where the agent must learn to find rewards in randomly generated mazes from a visual input.
- **p. 6 / 5.4. Labyrinth - extractive PDF cue:** The specific task we considered involved the agent learning to find rewards in randomly generated mazes.
- **p. 6 / 5.4. Labyrinth - extractive PDF cue:** The final average score of around 50 indicates that the agent learned a reasonable strategy for exploring random 3D maxes using only a visual input.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** robot/environment의 sequential decision process.
- **Input boundary:** state 또는 observation, action, reward와 transition history.
- **Output/decision under evaluation:** action policy와 induced trajectory.
- **Primary target:** expected return, task success, stability와 sample efficiency.
- **Detected evaluation headings:** 5. Experiments (p. 4).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.1. Atari 2600 Games | EMPIRICAL / SIMULATION | A3C significantly improves on state-of-the-art the average score over 57 games in half the training time of the other methods while using only 16 ... | p. 5 (5.1. Atari 2600 Games) |
| 5.1. Atari 2600 Games | EMPIRICAL / SIMULATION | Overall, the policy-based advantage actor-critic method significantly outperforms all three value-based methods. | p. 5 (5.1. Atari 2600 Games) |
| 5.5. Scalability and Data Efficiency | EMPIRICAL / SIMULATION | We observe that one-step methods (one-step Q and one-step Sarsa) often require less data to achieve a particular score when using more parallel actor-learners. | p. 6 (5.5. Scalability and Data Efficiency) |
| 5.5. Scalability and Data Efficiency | EMPIRICAL / SIMULATION | These results show that all four methods achieve substantial speedups from using multiple worker threads, with 16 threads leading to at least an order ... | p. 6 (5.5. Scalability and Data Efficiency) |
| 5. Experiments | EMPIRICAL / SIMULATION | We use the Atari domain to compare against state of the art results (Van Hasselt et al., 2015; Wang et al., 2015; Schaul et ... | p. 4 (5. Experiments) |

## Dataset / Benchmark Role

- **p. 4 / 5. Experiments - extractive PDF cue:** This is one of the most commonly used benchmark environments for RL algorithms.
- **p. 4 / 5. Experiments - extractive PDF cue:** We perform most of our experiments using the Arcade Learning Environment (Bellemare et al., 2012), which provides a simulator for Atari 2600 games.
- **p. 5 / 5. Experiments - extractive PDF cue:** MuJoCo (Todorov, 2015) is a physics simulator for evaluating agents on continuous motor control tasks with contact dynamics.
- **p. 6 / 5.3. Continuous Action Control Using the MuJoCo - extractive PDF cue:** Physics Simulator We also examined a set of tasks where the action space is continuous.
- **p. 6 / 5.4. Labyrinth - extractive PDF cue:** This task is much more challenging than the TORCS driving domain because the agent is faced with a new maze in each episode and must ...
- **p. 5 / 5. Experiments - extractive PDF cue:** Labyrinth is a new 3D environment where the agent must learn to find rewards in randomly generated mazes from a visual input.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 1. Learning speed comparison for DQN and the new asynchronous algorithms on five Atari 2600 games. DQN was trained on a single Nvidia K40 ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1. Mean and median human-normalized scores on 57 Atari games using the human starts evaluation metric. Supplementary Table SS3 shows the raw scores for ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. The average training speedup for each method and num- ber of threads averaged over seven Atari games. To compute the training speed-up on ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 2. Scatter plots of scores obtained by asynchronous advantage actor-critic on five games (Beamrider, Breakout, Pong, Q*bert, Space Invaders) for 50 different learning rates ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 3. Data efficiency comparison of different numbers of actor-learners for three asynchronous methods on five Atari games. The x-axis shows the total number of ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4. Training speed comparison of different numbers of actor-learners on five Atari games. The x-axis shows training time in hours while the y-axis shows ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This is one of the most commonly used benchmark environments for RL algorithms. | embodiment, simulator version and control stack | p. 4 (5. Experiments), p. 4 (5. Experiments) |
| Task/environment | We perform most of our experiments using the Arcade Learning Environment (Bellemare et al., 2012), which provides a simulator for Atari 2600 games. | reset, timeout, object/scene variation | p. 4 (5. Experiments), p. 5 (5. Experiments) |
| Observation/sensor | state 또는 observation, action, reward와 transition history | calibration, preprocessing, privileged input | p. 2 (3. Reinforcement Learning Background), p. 2 (3. Reinforcement Learning Background) |
| Output/decision | action policy와 induced trajectory | action frame, controller and termination | p. 3 (3. Reinforcement Learning Background), p. 3 (4. Asynchronous RL Framework) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Labyrinth is a new 3D environment where the agent must learn to find rewards in randomly generated mazes from a visual input. | definition/direction/unit from same section | p. 5 (5. Experiments) |
| The specific task we considered involved the agent learning to find rewards in randomly generated mazes. | definition/direction/unit from same section | p. 6 (5.4. Labyrinth) |
| The final average score of around 50 indicates that the agent learned a reasonable strategy for exploring random 3D maxes using only a visual ... | definition/direction/unit from same section | p. 6 (5.4. Labyrinth) |
| On each game, there is a wide range of learning rates for which all random initializations acheive good scores. | definition/direction/unit from same section | p. 7 (5.5. Scalability and Data Efficiency) |
| The fact that there are virtually no points with scores of 0 in regions with good learning rates indicates that the methods are stable ... | definition/direction/unit from same section | p. 7 (5.6. Robustness and Stability) |
| Supplementary Table S3 shows the scores on all games. | definition/direction/unit from same section | p. 5 (5.1. Atari 2600 Games) |
| Figure 4. Training speed comparison of different numbers of actor-learners on five Atari games. The x-axis shows training time in hours while the y-axis ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We also compared the four asynchronous methods on the TORCS 3D car racing game (Wymann et al., 2013). | comparison identity and matched condition | p. 5 (5.2. TORCS Car Racing Simulator) |
| Overall, the policy-based advantage actor-critic method significantly outperforms all three value-based methods. | comparison identity and matched condition | p. 5 (5.1. Atari 2600 Games) |
| We performed further comparisons using the TORCS 3D car racing simulator (Wymann et al., 2013). | comparison identity and matched condition | p. 4 (5. Experiments) |
| We performed experiments using four different settings - the agent controlling a slow car with and without opponent bots, and the agent controlling a ... | comparison identity and matched condition | p. 6 (5.2. TORCS Car Racing Simulator) |
| Figure 4. Training speed comparison of different numbers of actor-learners on five Atari games. The x-axis shows training time in hours while the y-axis ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We believe this is due to positive effect of multiple threads to reduce the bias in one-step methods. | component/input/data sensitivity | p. 6 (5.5. Scalability and Data Efficiency) |
| We performed experiments using four different settings - the agent controlling a slow car with and without opponent bots, and the agent controlling a ... | component/input/data sensitivity | p. 6 (5.2. TORCS Car Racing Simulator) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present asynchronous variants of four standard reinforcement learning algorithms and show that parallel actor-learners have a stabilizing effect on training allowing all four ... | A3C significantly improves on state-of-the-art the average score over 57 games in half the training time of the other methods while using only 16 ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (5.1. Atari 2600 Games), p. 5 (5.1. Atari 2600 Games), p. 6 (5.5. Scalability and Data Efficiency), p. 6 (5.5. Scalability and Data Efficiency), p. 4 (5. Experiments), p. 7 (5.5. Scalability and Data Efficiency) |
| Primary metric/result | Overall, the policy-based advantage actor-critic method significantly outperforms all three value-based methods. | numeric claim only at cited anchor | p. 5 (5.1. Atari 2600 Games) |

- Numeric sentences retained from the body:
- **p. 6 / 5.2. TORCS Car Racing Simulator - extractive PDF cue:** A3C was the best performing agent, reaching between roughly 75% and 90% of the score obtained by a human tester on all four game configurations ...
- **p. 6 / 5.3. Continuous Action Control Using the MuJoCo - extractive PDF cue:** In all problems, using either the physical state or pixels as input, Asynchronous Advantage-Critic found good solutions in less than 24 hours of training and ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | While this shows that stable online Q-learning is possible without experience replay, which was used for this purpose in DQN, it does not mean ... | p. 7 (6. Conclusions and Discussion) |
| body limitation/failure cue | Somewhat surprisingly, asynchronous one-step Q-learning and Sarsa algorithms exhibit superlinear speedups that cannot be explained by purely computational gains. | p. 6 (5.5. Scalability and Data Efficiency) |
| body limitation/failure cue | Finally, we analyzed the stability and robustness of the four proposed asynchronous algorithms. | p. 7 (5.6. Robustness and Stability) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| A3C significantly improves on state-of-the-art the average score over 57 games in half the training time of the other methods while using only 16 ... | p. 5 (5.1. Atari 2600 Games) |
| We additionally used the final network weights for evaluation to make the results more comparable to the original results Method Training Time Mean Median ... | p. 5 (5.1. Atari 2600 Games) |
| Whereas previous approaches to deep reinforcement learning rely heavily on specialized hardware such as GPUs (Mnih et al., 2015; Van Hasselt et al., 2015; ... | p. 1 (48. Copyright 2016 by the author(s)) |
| We analyzed the effectiveness of our proposed framework by looking at how the training time and data efficiency changes with the number of parallel ... | p. 6 (5.5. Scalability and Data Efficiency) |
| On each game, there is a wide range of learning rates for which all random initializations acheive good scores. | p. 7 (5.5. Scalability and Data Efficiency) |
| For each of the four algorithms we trained models on five games (Breakout, Beamrider, Pong, Q*bert, Space Invaders) using 50 different learning rates and ... | p. 7 (5.6. Robustness and Stability) |
| The best performing method, an asynchronous variant of actor-critic, surpasses the current state-of-the-art on the Atari domain while training for half the time on ... | p. 1 (Abstract) |
| To compute the training speed-up on a single game we measured the time to required reach a fixed reference score using each method and ... | p. 6 (5.4. Labyrinth) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 6. Conclusions and Discussion - extractive PDF cue:** While this shows that stable online Q-learning is possible without experience replay, which was used for this purpose in DQN, it does not mean that ...
- **p. 6 / 5.5. Scalability and Data Efficiency - extractive PDF cue:** Somewhat surprisingly, asynchronous one-step Q-learning and Sarsa algorithms exhibit superlinear speedups that cannot be explained by purely computational gains.
- **p. 7 / 5.6. Robustness and Stability - extractive PDF cue:** Finally, we analyzed the stability and robustness of the four proposed asynchronous algorithms.

- **PDF anchors reviewed:** datasets p. 4 (5. Experiments), p. 4 (5. Experiments), p. 5 (5. Experiments), p. 6 (5.3. Continuous Action Control Using the MuJoCo), p. 6 (5.4. Labyrinth), p. 5 (5. Experiments), metrics p. 5 (5. Experiments), p. 6 (5.4. Labyrinth), p. 6 (5.4. Labyrinth), p. 7 (5.5. Scalability and Data Efficiency), p. 7 (5.6. Robustness and Stability), p. 5 (5.1. Atari 2600 Games), baselines p. 5 (5.2. TORCS Car Racing Simulator), p. 5 (5.1. Atari 2600 Games), p. 4 (5. Experiments), p. 6 (5.2. TORCS Car Racing Simulator), p. 8 (Figure/Table caption), results p. 5 (5.1. Atari 2600 Games), p. 5 (5.1. Atari 2600 Games), p. 6 (5.5. Scalability and Data Efficiency), p. 6 (5.5. Scalability and Data Efficiency), p. 4 (5. Experiments), p. 7 (5.5. Scalability and Data Efficiency).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
