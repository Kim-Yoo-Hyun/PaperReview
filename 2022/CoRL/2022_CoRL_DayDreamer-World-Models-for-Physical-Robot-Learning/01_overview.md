# DayDreamer: World Models for Physical Robot Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v205/wu23c.html.
> PDF retrieval source: https://arxiv.org/pdf/2206.14176. Reading tracker status/evidence was not changed.

- Year/Venue: 2022 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: CORE
- Tags: Robotics, world model, real robot, model-based reinforcement learning
- Official paper: https://proceedings.mlr.press/v205/wu23c.html
- Full-text retrieval: https://arxiv.org/pdf/2206.14176
- Code/Project: https://danijar.com/project/daydreamer/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 Despite the promises of world models, learning accurate world models for the real world is a big open challenge.를 문제로 두고, Dreamer consists of two neural network components.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 2 / 1 Introduction - extractive body cue:** Replay Buffer Real World Actor Critic World Model Figure 2: Dreamer follows a simple pipeline for online learning on robot hardware without simulators.
- **p. 2 / 1 Introduction - extractive body cue:** The current learned policy collects experience on the robot.
- **p. 2 / 1 Introduction - extractive body cue:** This experience is added to the replay buffer.
- **p. 2 / 1 Introduction - extractive body cue:** The world model is trained on replayed off-policy sequences through supervised learning.
- **p. 2 / 1 Introduction - extractive body cue:** An actor critic algorithm optimizes a neural network policy from imagined rollouts in the latent space of the world model.
- **p. 2 / 1 Introduction - extractive body cue:** Despite the promises of world models, learning accurate world models for the real world is a big open challenge.
- **p. 2 / 1 Introduction - extractive body cue:** However, current algorithms require too much interaction with the environment to learn successful behaviors, making them impractical for many real world tasks.

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** Dreamer consists of two neural network components.
- **p. 3 / 2 Approach - extractive body cue:** The world model is based on the Recurrent State-Space Model (RSSM; Hafner et al., 2018), which consists of four components: Encoder Network: encθ(st / st-1, ...
- **p. 4 / 2 Approach - extractive body cue:** The actor critic algorithm consists of two neural networks: Actor Network: π(at / st) Critic Network: v(st) (2) The role of the actor network is ...
- **p. 2 / 1 Introduction - extractive body cue:** Deep reinforcement learning (RL) offers a popular approach to robot learning that enables robots to improve their behavior over time through trial and error.
- **p. 2 / 1 Introduction - extractive body cue:** The key contributions of this paper are summarized as follows: • Dreamer on Robots We apply Dreamer to 4 robots, demonstrating successful learning directly in ...
- **p. 3 / 2 Approach - extractive body cue:** The dynamics model learns to predict the sequence of stochastic representations by using its recurrent state ht.
- **p. 4 / 2 Approach - extractive body cue:** Different gradient estimators are available for computing the policy gradient for optimizing the actor, such as Reinforce (Williams, 1992) and the reparameterization trick (Kingma and ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The world model is based on the Recurrent State-Space Model (RSSM; Hafner et al., 2018), which consists of four components: Encoder Network: encθ(st / st-1, at-1, xt) Decoder Network: decθ(st) ≈xt Dynamics ... | observation, uncertainty/risk estimate와 task command | p. 3 (2 Approach), p. 3 (1 Introduction) |
| State/latent | world, model, Recurrent, State-Space, RSSM, Hafner, consists, four, components, Encoder, Network, st-1 | safe set, recovery state 또는 constraint margin | p. 3 (2 Approach), p. 3 (1 Introduction), p. 4 (2 Approach) |
| Output/action | A recurrent state-space model (RSSM) is trained to predict future codes given actions, without observing intermediate inputs. | shielded, recovery 또는 safe action | p. 3 (1 Introduction), p. 4 (2 Approach), p. 4 (2 Approach) |
| Objective/outcome | The actor critic algorithm consists of two neural networks: Actor Network: π(at / st) Critic Network: v(st) (2) The role of the actor network is to learn a distribution over successful actions ... | task return과 violation/failure probability | p. 4 (2 Approach), p. 4 (2 Approach), p. 3 (2 Approach) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** Dreamer consists of two neural network components.
- **p. 3 / 2 Approach - extractive body cue:** The world model is based on the Recurrent State-Space Model (RSSM; Hafner et al., 2018), which consists of four components: Encoder Network: encθ(st / st-1, ...
- **p. 4 / 2 Approach - extractive body cue:** The actor critic algorithm consists of two neural networks: Actor Network: π(at / st) Critic Network: v(st) (2) The role of the actor network is ...
- **p. 2 / 1 Introduction - extractive body cue:** Deep reinforcement learning (RL) offers a popular approach to robot learning that enables robots to improve their behavior over time through trial and error.
- **p. 2 / 1 Introduction - extractive body cue:** The key contributions of this paper are summarized as follows: • Dreamer on Robots We apply Dreamer to 4 robots, demonstrating successful learning directly in ...
- **p. 7 / 3 Experiments - extractive body cue:** We find that DrQv2, a model-free algorithm specifically designed to continuous control from pixels, achieves similar performance.
- **p. 7 / 3 Experiments - extractive body cue:** Dreamer learns a policy that enables the XArm to achieve an average pick rate of 3.1 objects per minute in 10 hours of time, which ...
- **p. 5 / 3 Experiments - extractive body cue:** We choose Rainbow (Hessel et al., 2018) as a powerful representative of this category, an algorithm that combines many improvements of DQN.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (3 Experiments), p. 7 (3 Experiments) |
| Embodiment/environment | 3.2 UR5 Multi-Object Visual Pick and Place Common in warehouse and logistics environments, pick and place tasks require a robot manipulator to transport items from one bin into another. | hardware/simulator version and reset protocol | p. 6 (3 Experiments), p. 7 (3 Experiments) |
| Dataset/benchmark | While soft objects would be challenging to model accurately in a simulator, Dreamer avoids this issue by directly learning on the real robot without a simulator. | role, split, size and leakage | p. 6 (3 Experiments), p. 7 (3 Experiments), p. 7 (3 Experiments), p. 4 (3 Experiments) |
| Metric | Dreamer overcomes the challenges of visual localization and sparse rewards on this task, learning a successful strategy within a few hours of autonomous operation. | definition, denominator, direction and uncertainty | p. 6 (3 Experiments), p. 6 (3 Experiments), p. 7 (3 Experiments) |
| Baseline/ablation | The state-of-the-art baseline in this category is DrQv2 (Yarats et al., 2021), which uses image augmentation to increase sample-efficiency. | fair input/data/compute/action matching | p. 5 (3 Experiments), p. 1 (Figure/Table caption), p. 4 (3 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5 Discussion - extractive body cue:** Limitations While Dreamer shows promising results, learning on hardware over many hours creates wear on robots that may require human intervention or repair.
- **p. 6 / 3 Experiments - extractive body cue:** In comparison, SAC quickly learns to roll off its back but fails to stand up or walk given the small data budget.
- **p. 5 / 3 Experiments - extractive body cue:** Prior work in quadruped locomotion requires either extensive training in simulation under domain randomization, using recovery controllers to avoid unsafe states, or defining the action ...
- **p. 5 / 3 Experiments - extractive body cue:** The filled circles indicate times where the robot fell on its back, requiring the learning of a robust strategy for getting back up.
- **p. 6 / 3 Experiments - extractive body cue:** We hypothesize that Rainbow DQN and PPO fail because they require larger amounts of experience, which is not feasible for us to collect in the ...

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 Despite the promises of world models, learning accurate world models for the real world is a big open challenge.를 문제로 두고, Dreamer consists of two neural network components.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (2 Approach), p. 4 (2 Approach), p. 3 (2 Approach) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
