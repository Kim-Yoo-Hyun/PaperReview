# Masked Visual Pre-training for Motor Control

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2203.06173.
> PDF retrieval source: https://arxiv.org/abs/2203.06173. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / arXiv
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: Robotics, representation learning, Visual Pretraining, Imitation Learning
- Official paper: https://arxiv.org/abs/2203.06173
- Full-text retrieval: https://arxiv.org/abs/2203.06173
- Code/Project: https://mvp-playground.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 il 문제를 이해하기 위해 읽는다. 본문은 Control inputs are high-dimensional and difficult to search (e.g., 23 DoF robot with a multi-finger hand).를 문제로 두고, We also compare our method to visual encoders trained by supervised learning on ImageNet (Deng et al., 2009), the choice of encoder in most vision tasks.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** This paper shows that self-supervised visual pretraining from real-world images is effective for learning motor control tasks from pixels.
- **p. 1 / Abstract - extractive body cue:** We first train the visual representations by masked modeling of natural images.
- **p. 1 / Abstract - extractive body cue:** We then freeze the visual encoder and train neural network controllers on top with reinforcement learning.
- **p. 1 / Abstract - extractive body cue:** We do not perform any task-specific fine-tuning of the encoder; the same visual representations are used for all motor control tasks.
- **p. 1 / Abstract - extractive body cue:** To the best of our knowledge, this is the first self-supervised model to exploit real-world images at scale for motor control.
- **p. 1 / 1. Introduction - extractive body cue:** Control inputs are high-dimensional and difficult to search (e.g., 23 DoF robot with a multi-finger hand).
- **p. 2 / 1. Introduction - extractive body cue:** While conceptually appealing, the latter has two main challenges in practice.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** We also compare our method to visual encoders trained by supervised learning on ImageNet (Deng et al., 2009), the choice of encoder in most vision ...
- **p. 4 / 3.1. Motivation - extractive body cue:** To this end, we introduce a new benchmark suite for Pixel Motor Control, which we call PixMC.
- **p. 1 / 1. Introduction - extractive body cue:** We show that we are able to solve a range of motor control tasks with variations in robots, scenes, and objects.
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we show that self-supervised visual pretraining on real-world images is effective for learning motor control tasks from pixels.
- **p. 2 / 1. Introduction - extractive body cue:** We call our approach MVP (for Masked Visual Pre-training for Motor Control).
- **p. 3 / 2.2. Learning Motor Control from Pixels - extractive body cue:** Specifically, we use the proximal policy optimization (PPO) algorithm (Schulman et al., 2017).
- **p. 3 / 2.1. Masked Visual Pre-training - extractive body cue:** We adopt masked modeling as our self-supervision objective-specifically, we use masked autoencoder (MAE) (He et al., 2021).
- **p. 2 / 2) Our self-supervised approach consistently outperforms - extractive body cue:** We believe that our work is a promising step in this direction and release the benchmark suite, pre-trained models, and the training code on the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | First, training is computationally expensive and has poor sample complexity (especially with high-dimensional inputs and actions). | observation history와 expert trajectory/action | p. 2 (1. Introduction), p. 3 (2.2. Learning Motor Control from Pixels) |
| State/latent | First, training, computationally, expensive, poor, sample, complexity, especially, high-dimensional, inputs, actions, PPO | behavior policy와 temporal action context | p. 2 (1. Introduction), p. 3 (2.2. Learning Motor Control from Pixels), p. 2 (1. Introduction) |
| Output/action | PPO is a state-of-theart policy gradient method that has shown excellent performance on complex motor control tasks and successful transfer to real hardware (OpenAI et al., 2020; 2019). | predicted action 또는 action chunk | p. 3 (2.2. Learning Motor Control from Pixels), p. 2 (1. Introduction), p. 4 (3.4. Observations and Actions) |
| Objective/outcome | We adopt masked modeling as our self-supervision objective-specifically, we use masked autoencoder (MAE) (He et al., 2021). | imitation error, task success, robustness와 compounding error | p. 3 (2.1. Masked Visual Pre-training), p. 3 (2.2. Learning Motor Control from Pixels), p. 4 (3.6. Distributed Training) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** We also compare our method to visual encoders trained by supervised learning on ImageNet (Deng et al., 2009), the choice of encoder in most vision ...
- **p. 4 / 3.1. Motivation - extractive body cue:** To this end, we introduce a new benchmark suite for Pixel Motor Control, which we call PixMC.
- **p. 1 / 1. Introduction - extractive body cue:** We show that we are able to solve a range of motor control tasks with variations in robots, scenes, and objects.
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we show that self-supervised visual pretraining on real-world images is effective for learning motor control tasks from pixels.
- **p. 2 / 1. Introduction - extractive body cue:** We call our approach MVP (for Masked Visual Pre-training for Motor Control).
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. Sample complexity. We plot the success rate as a function of environment steps on the 8 PixMC tasks. Each task uses either the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 10. Learning rate and seed stability. For each model, we train 15 instances of the model with 3 learning rates and 5 seeds. We ...
- **p. 6 / 5.1. Sample Complexity - extractive body cue:** The supervised baseline is flat at zero success rate on the pick and move tasks with both robots; MVP rivals the oracle on the pick ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Embodiment/environment | The benchmark provides proprioceptive information for the robots, as well as hand-engineered states typically including 3D poses or relevant objects, goals, and their relations. | hardware/simulator version and reset protocol | p. 4 (3.4. Observations and Actions), p. 4 (3.1. Motivation) |
| Dataset/benchmark | We consider the oracle state model (i.e., position, orientation, and velocity of the object, goal and robot in world-coordinate system, which is difficult to estimate in real-world settings) as the upper bound ... | role, split, size and leakage | p. 4 (3.4. Observations and Actions), p. 4 (3.1. Motivation), p. 6 (5.1. Sample Complexity), p. 6 (5.2. Generalization) |
| Metric | We plot the success rate as a function of environment steps on the 8 PixMC tasks. | definition, denominator, direction and uncertainty | p. 5 (3.6. Distributed Training), p. 6 (4. Experimental Setup), p. 6 (5.2. Generalization) |
| Baseline/ablation | The MVP approach significantly outperforms the supervised baseline on 7 tasks and closely matches the oracle state model (considered the upper bound of RL) on 5 tasks at convergence. | fair input/data/compute/action matching | p. 5 (3.6. Distributed Training), p. 6 (5.1. Sample Complexity), p. 8 (5.4. Additional Comparisons) |

## Explicit Limitations and Failure Boundary

- **p. 4 / 3.1. Motivation - extractive body cue:** While there exist a number of excellent benchmarks for motor control, e.g., DMC (Tassa et al., 2018), RLBench (James et al., 2020), Robosuite (Zhu et ...
- **p. 7 / 5.3. Ablations - extractive body cue:** The random model fails on 6 out of 8 PixMC tasks (0 success rate).
- **p. 7 / 5.3. Ablations - extractive body cue:** We observed unstable training (the loss goes to NaN), and we decreased the learning rate until training successfully completed.
- **p. 8 / 5.3. Ablations - extractive body cue:** We observe that the larger encoder does not improve performance.
- **p. 8 / 5.3. Ablations - extractive body cue:** We do not observe clear gains from preliminary model scaling and believe that scaling data and model size is an exciting area for future work.
- **p. 5 / 4. Experimental Setup - extractive body cue:** Other hyperparams use defaults: Adam optimizer with β1 = 0.9 and β2 = 0.999, gradient norm of 1, initial noise standard deviation of 1.0.
- **p. 6 / 5.2. Generalization - extractive body cue:** A robust model from pixels should pick up the object used for training.

## Why Read It

Planning and control의 il 문제를 이해하기 위해 읽는다. 본문은 Control inputs are high-dimensional and difficult to search (e.g., 23 DoF robot with a multi-finger hand).를 문제로 두고, We also compare our method to visual encoders trained by supervised learning on ImageNet (Deng et al., 2009), the choice of encoder in most vision tasks.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Motivation), p. 3 (2.2. Learning Motor Control from Pixels), p. 3 (2.1. Masked Visual Pre-training) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
