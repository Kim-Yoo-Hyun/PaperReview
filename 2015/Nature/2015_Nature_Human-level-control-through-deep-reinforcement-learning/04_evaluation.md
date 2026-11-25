# Evaluation - Human-level control through deep reinforcement learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1038/nature14236; PDF retrieval source: https://doi.org/10.1038/nature14236. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 7. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../work/sources/pdf_note_review_followup_2026-10-23.json).

## Evaluation in One Sentence

그림 3은 무작위 에이전트를 0%, 전문 플레이어를 100%로 두고 게임별 점수를 정규화한다. 49개 중 29개 게임에서 DQN이 사람 기준 점수의 75% 이상에 도달했다. [PDF 2쪽](https://www.nature.com/articles/nature14236.pdf#page=2) · [PDF 3쪽](https://www.nature.com/articles/nature14236.pdf#page=3)

## Evaluation Body Digest

- **p. 5 / 2 6 F E B R U A R Y - extractive body cue:** Reinforcement learning for robot soccer.
- **p. 5 / 2 6 F E B R U A R Y - extractive body cue:** Reinforcement learning for robots using neural networks.
- **p. 6 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** The human performanceis theaverage rewardachievedfromaround20episodesofeachgamelastingamaximumof5 min each, following around 2 h of practice playing each game.
- **p. 6 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** This had a minimal effect: changing the normalized DQN performance by more than 5% in only six games (Boxing, Breakout, Crazy Climber, Demon Attack, Krull ...
- **p. 7 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** First, we use a technique known as experience replay23 in which we store the agent's experiences at each time-step, et5(st,at, rt,st 1 1), in a ...
- **p. 12 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** Note that these evaluation episodes were not truncated at 5 min leading to higher scores on Enduro than the ones reported in Extended Data Table ...
- **p. 12 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** Each agent was evaluated every 250,000 training frames for 135,000 validation frames and the highest average episode score is reported.
- **p. 4 / 2 6 F E B R U A R Y - extractive body cue:** Object recognition with features inspired by visual cortex.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** robot mechanism의 state와 task-space dynamics.
- **Input boundary:** joint/task state, reference와 sensor feedback.
- **Output/decision under evaluation:** torque, force, velocity 또는 position command.
- **Primary target:** tracking, stability, constraint satisfaction과 contact behavior.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess | SYSTEM / EVALUATION SCOPE UNRESOLVED | The human performanceis theaverage rewardachievedfromaround20episodesofeachgamelastingamaximumof5 min each, following around 2 h of practice playing each game. | p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess | SYSTEM / EVALUATION SCOPE UNRESOLVED | This had a minimal effect: changing the normalized DQN performance by more than 5% in only six games (Boxing, Breakout, Crazy Climber, Demon Attack, ... | p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess | SYSTEM / EVALUATION SCOPE UNRESOLVED | Rectified linear units improve restricted Boltzmann machines. | p. 7 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess | SYSTEM / EVALUATION SCOPE UNRESOLVED | Because the absolute value loss function jxj has a derivative of 21 for all negative values of x and a derivative of 1 for ... | p. 7 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| 2 6 F E B R U A R Y | SYSTEM / EVALUATION SCOPE UNRESOLVED | In this work, we demonstrate that a single architecture can successfullylearncontrolpoliciesinarangeofdifferentenvironmentswithonly very minimal prior knowledge, receiving only the pixels and the game scoreasinputs,andusingthesamealgori ... | p. 4 (2 6 F E B R U A R Y) |

## Dataset / Benchmark Role

- **p. 5 / 2 6 F E B R U A R Y - extractive body cue:** Reinforcement learning for robot soccer.
- **p. 5 / 2 6 F E B R U A R Y - extractive body cue:** Reinforcement learning for robots using neural networks.
- **p. 6 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** The human performanceis theaverage rewardachievedfromaround20episodesofeachgamelastingamaximumof5 min each, following around 2 h of practice playing each game.
- **p. 6 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** This had a minimal effect: changing the normalized DQN performance by more than 5% in only six games (Boxing, Breakout, Crazy Climber, Demon Attack, Krull ...
- **p. 7 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** First, we use a technique known as experience replay23 in which we store the agent's experiences at each time-step, et5(st,at, rt,st 1 1), in a ...
- **p. 12 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** Note that these evaluation episodes were not truncated at 5 min leading to higher scores on Enduro than the ones reported in Extended Data Table ...
- **p. 12 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** Each agent was evaluated every 250,000 training frames for 135,000 validation frames and the highest average episode score is reported.
- **p. 4 / 2 6 F E B R U A R Y - extractive body cue:** Object recognition with features inspired by visual cortex.

## Figures / Tables as Body Evidence

- figure/table caption cue 없음

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Reinforcement learning for robot soccer. | embodiment, simulator version and control stack | p. 5 (2 6 F E B R U A R Y), p. 5 (2 6 F E B R U A R Y) |
| Task/environment | Reinforcement learning for robots using neural networks. | reset, timeout, object/scene variation | p. 5 (2 6 F E B R U A R Y), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| Observation/sensor | joint/task state, reference와 sensor feedback | calibration, preprocessing, privileged input | p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| Output/decision | torque, force, velocity 또는 position command | action frame, controller and termination | p. 2 (2 6 F E B R U A R Y), p. 2 (2 6 F E B R U A R Y) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Clipping the rewards in this manner limits the scale of the error derivatives and makesiteasierto use thesamelearningrateacrossmultiplegames. | definition/direction/unit from same section | p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| In addition it receives a reward rt representing the change in game score. | definition/direction/unit from same section | p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| In this work, we demonstrate that a single architecture can successfullylearncontrolpoliciesinarangeofdifferentenvironmentswithonly very minimal prior knowledge, receiving only the pixels and the game scoreasinputs,andusingthesamealgori ... | definition/direction/unit from same section | p. 4 (2 6 F E B R U A R Y) |
| A neural substrate of prediction and reward. | definition/direction/unit from same section | p. 4 (2 6 F E B R U A R Y) |
| Because the absolute value loss function jxj has a derivative of 21 for all negative values of x and a derivative of 1 for ... | definition/direction/unit from same section | p. 7 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| Note the figures in the last column indicate the performance of DQN relative to the human games tester, expressed as a percentage, that is, ... | definition/direction/unit from same section | p. 11 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| Bellman TD error의 update contribution을 [−1,1]로 clip한다. 큰 residual에 대해서 absolute-value loss와 같은 bounded-gradient 효과를 설명한다. | Training stabilization choice; evaluation metric이나 reward clipping과 구분 | PDF p. 7 Methods |
| Each of the peaks in the value function curve corresponds to a reward obtained by clearing a brick. | definition/direction/unit from same section | p. 9 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The random agent served as a baseline comparison and chose a random action at 10 Hz which is every sixth frame, repeating its last ... | comparison identity and matched condition | p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| Extended Data Table 4 / Comparison of DQN performance with linear function approximator The performance of the DQN agent is compared with the performance ... | comparison identity and matched condition | p. 13 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| Taken together, our work illustrates the power of harnessing state-of-the-art machine learning techniques with biologically inspired mechanisms to create agents that are capable of ... | comparison identity and matched condition | p. 4 (2 6 F E B R U A R Y) |
| This had a minimal effect: changing the normalized DQN performance by more than 5% in only six games (Boxing, Breakout, Crazy Climber, Demon Attack, ... | comparison identity and matched condition | p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| This modification makes the algorithm more stable compared to standard online Q-learning, where an update thatincreasesQ(st,at)oftenalsoincreasesQ(st 1 1,a)forallaandhencealsoincreases the target yj, possibly leading to ... | comparison identity and matched condition | p. 7 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| Note also that the number of training frames was shorter (10 million frames) as compared to the main results presented in Extended Data Table ... | comparison identity and matched condition | p. 12 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Because running the emulator forward for one step requires much less computationthan having the agent select an action, this technique allows the agent to ... | component/input/data sensitivity | p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| This was necessary to remove flickering that is present in games where some objects appear only in even frames while other objects appear only ... | component/input/data sensitivity | p. 6 (2 6 F E B R U A R Y) |
| The algorithm modifies standard online Q-learning in two ways to make it suitable for training large neural networks without diverging. | component/input/data sensitivity | p. 7 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| Note that this algorithm is model-free: it solves the reinforcement learning task directly using samples from the emulator, without explicitly estimating the reward and ... | component/input/data sensitivity | p. 7 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Notably, our method was able to train large neural networks using a reinforcementlearningsignalandstochasticgradientdescentinastablemannerillustrated by the temporal evolution of two indices of learning (the agent's ... | The human performanceis theaverage rewardachievedfromaround20episodesofeachgamelastingamaximumof5 min each, following around 2 h of practice playing each game. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 7 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 7 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 4 (2 6 F E B R U A R Y), p. 11 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| Primary metric/result | This had a minimal effect: changing the normalized DQN performance by more than 5% in only six games (Boxing, Breakout, Crazy Climber, Demon Attack, ... | numeric claim only at cited anchor | p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |

- Numeric sentences retained from the body:
- **p. 6 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** The random agent served as a baseline comparison and chose a random action at 10 Hz which is every sixth frame, repeating its last action ...
- **p. 6 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** 10 Hz is about the fastest that a human player can select the ‘fire' button, and setting the random agent to this frequency avoids spurious ...
- **p. 6 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** As in the original Atari 2600 environment, the emulator was run at 60 Hz and the audio output was disabled: as such, the sensory input ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory. | p. 5 (2 6 F E B R U A R Y) |
| body limitation/failure cue | At the same time, it could affect the performance of our agent since it cannot differentiate between rewards of different magnitude. | p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| body limitation/failure cue | Thevaluesofallthehyperparametersandoptimizationparameterswereselected by performing an informal search on the games Pong, Breakout, Seaquest, Space Invaders and Beam Rider. | p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| body limitation/failure cue | At time point 2, the agent starts moving the paddle towards the ball and the value of the ‘up' action stays high while the ... | p. 9 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| body limitation/failure cue | The final term is the variance of the targets, which does not depend on the parameters hi that we are currently optimizing, and may ... | p. 7 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| body limitation/failure cue | This approach is in some respects limited because the memory buffer does not differentiate important transitions and always overwrites with recent transitions owing to ... | p. 7 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |

## Statistics, Efficiency, and Reproducibility

- 그림 3의 오차 막대는 시작 조건을 달리한 평가 에피소드 30개에서 얻은 점수의 표준편차다. [PDF 3쪽](https://www.nature.com/articles/nature14236.pdf#page=3)

| Body reproducibility cue | Anchor |
|---|---|
| Extended Data Table 3 / The effects of replay and separating the target Q-network DQN agents were trained for 10 million frames using standard ... | p. 12 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| In this work, we demonstrate that a single architecture can successfullylearncontrolpoliciesinarangeofdifferentenvironmentswithonly very minimal prior knowledge, receiving only the pixels and the game scoreasinputs,andusingthesamealgori ... | p. 4 (2 6 F E B R U A R Y) |
| Deep auto-encoder neural networks in reinforcement learning. | p. 5 (2 6 F E B R U A R Y) |
| The main advantageof this type of architecture is the ability tocompute Q-valuesforall possibleactionsinagivenstatewithonlyasingleforwardpassthroughthenetwork. | p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| Thevaluesofallthehyperparametersandoptimizationparameterswereselected by performing an informal search on the games Pong, Breakout, Seaquest, Space Invaders and Beam Rider. | p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| 2 with respect to the network parameters h Every C steps reset ^Q~Q End For End For 31. | p. 7 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |
| We did not perform a systematic grid search owing to the high computational cost, although it is conceivable that even better results could be ... | p. 10 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess) |

## Limitations and Verification Questions

- **p. 5 / 2 6 F E B R U A R Y - extractive body cue:** Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory.
- **p. 6 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** At the same time, it could affect the performance of our agent since it cannot differentiate between rewards of different magnitude.
- **p. 6 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** Thevaluesofallthehyperparametersandoptimizationparameterswereselected by performing an informal search on the games Pong, Breakout, Seaquest, Space Invaders and Beam Rider.
- **p. 9 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** At time point 2, the agent starts moving the paddle towards the ball and the value of the ‘up' action stays high while the value ...
- **p. 7 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** The final term is the variance of the targets, which does not depend on the parameters hi that we are currently optimizing, and may therefore ...
- **p. 7 / 84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess - extractive body cue:** This approach is in some respects limited because the memory buffer does not differentiate important transitions and always overwrites with recent transitions owing to the ...

- **Evidence anchors reviewed:** datasets p. 5 (2 6 F E B R U A R Y), p. 5 (2 6 F E B R U A R Y), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 7 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 12 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), metrics p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 4 (2 6 F E B R U A R Y), p. 4 (2 6 F E B R U A R Y), p. 7 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 11 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), baselines p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 13 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 4 (2 6 F E B R U A R Y), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 7 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 12 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), results p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 6 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 7 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 7 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess), p. 4 (2 6 F E B R U A R Y), p. 11 (84 3 84.The functionw fromalgorithm1 described belowappliesthispreprocess).

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)
