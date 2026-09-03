# BridgeData V2: A Dataset for Robot Learning at Scale

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2308.12952.
> PDF retrieval source: https://arxiv.org/pdf/2308.12952. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, Dataset, Imitation Learning, robot manipulation, data scaling, generalization
- Official paper: https://arxiv.org/abs/2308.12952
- Full-text retrieval: https://arxiv.org/pdf/2308.12952
- Code/Project: https://rail-berkeley.github.io/bridgedata/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 il 문제를 이해하기 위해 읽는다. 본문은 However, in practice, assembling a dataset with the right features to accelerate research in large-scale robot learning presents a significant challenge.를 문제로 두고, In this paper, we propose a new dataset, which we call BridgeData V2 (Figure 1) because it greatly expands on the previously released Bridge Dataset [6].를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce BridgeData V2, a large and diverse dataset of robotic manipulation behaviors designed to facilitate research on scalable robot learning.
- **p. 1 / Abstract - extractive body cue:** BridgeData V2 contains 60,096 trajectories collected across 24 environments on a publicly available low-cost robot.
- **p. 1 / Abstract - extractive body cue:** BridgeData V2 provides extensive task and environment variability, leading to skills that can generalize across environments, domains, and institutions, making the dataset a useful resource ...
- **p. 1 / Abstract - extractive body cue:** Additionally, the dataset is compatible with a wide variety of openvocabulary, multi-task learning methods conditioned on goal images or natural language instructions.
- **p. 1 / Abstract - extractive body cue:** In our experiments, we train 6 state-of-the-art imitation learning and offline reinforcement learning methods on our dataset, and find that they succeed on a suite ...
- **p. 2 / 1 Introduction - extractive body cue:** However, in practice, assembling a dataset with the right features to accelerate research in large-scale robot learning presents a significant challenge.
- **p. 2 / 1 Introduction - extractive body cue:** A useful robotic system needs skills that generalize across the wide variety of conditions found in the real world.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we propose a new dataset, which we call BridgeData V2 (Figure 1) because it greatly expands on the previously released Bridge Dataset ...
- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are a new dataset of robotic manipulation behaviors as well as the empirical study of state-of-the-art offline learning methods using the introduced dataset.
- **p. 15 / B.4 Contrastive RL - extractive body cue:** The greater size and diversity of BridgeData V2 enables significantly better generalization to these unseen tasks.
- **p. 14 / B.2 Diffusion goal-conditioned behavior cloning - extractive body cue:** We use the DDPM (Denoising Diffusion Probabilistic Models) style objective as introduced by Ho et al.
- **p. 14 / B.4 Contrastive RL - extractive body cue:** Those image encodings then pass through two MLPs to get representations of the observation and the goal.
- **p. 15 / B.6 RT-1 - extractive body cue:** We use the same hyper-parameters as the original RT-1 paper [7], except for increasing the sequence length of the transformer from 6 to 15 to ...
- **p. 13 / B Learning Method Implementation Details - extractive body cue:** During training, the goal associated with an observation is selected by uniformly sampling an observation from the future timesteps in the trajectory.
- **p. 15 / B.5 Language-conditioned behavior cloning - extractive body cue:** The language instruction is first encoded with a frozen MUSE encoder and passed through 2 fully connected layers.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | First, given the observation and goal images, we feed them separately through a ResNet-34 encoder instead of a 3-layer CNN image encoder to get output encodings. | observation history와 expert trajectory/action | p. 14 (B.4 Contrastive RL), p. 2 (1 Introduction) |
| State/latent | First, given, observation, goal, images, feed, them, separately, through, ResNet-34, encoder, instead | behavior policy와 temporal action context | p. 14 (B.4 Contrastive RL), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Output/action | These methods cover a range of key design decisions involving the policy architecture, the use of observation histories, action discretization, and action prediction horizon. | predicted action 또는 action chunk | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 14 (B.1 Goal-conditioned behavior cloning) |
| Objective/outcome | Our contrastive RL objective retains the temporal-difference (TD) style used in [53]. | imitation error, task success, robustness와 compounding error | p. 14 (B.4 Contrastive RL), p. 14 (B.2 Diffusion goal-conditioned behavior cloning), p. 15 (B.5 Language-conditioned behavior cloning) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we propose a new dataset, which we call BridgeData V2 (Figure 1) because it greatly expands on the previously released Bridge Dataset ...
- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are a new dataset of robotic manipulation behaviors as well as the empirical study of state-of-the-art offline learning methods using the introduced dataset.
- **p. 15 / B.4 Contrastive RL - extractive body cue:** The greater size and diversity of BridgeData V2 enables significantly better generalization to these unseen tasks.
- **p. 8 / 5 Experiments - extractive body cue:** ResNet-18 ResNet-34 ResNet-50 Image Encoder 0.0 0.2 0.4 0.6 0.8 1.0 Average Success Rate 0.25 0.50 0.75 1.00 Proportion of Dataset 0.0 0.2 0.4 0.6 ...
- **p. 7 / 5 Experiments - extractive body cue:** Note that these evaluations were performed zero-shot, without any new data collected in Lab 2, and we expect fine-tuning on a small amount of data ...
- **p. 8 / 5 Experiments - extractive body cue:** We found that performance on an unseen pickand place task was significantly improved by training on data with greater skill diversity.
- **p. 6 / 5 Experiments - extractive body cue:** The goal-conditioned methods are comparable to each other in success rate.
- **p. 6 / 5 Experiments - extractive body cue:** To obtain success rates for each method, we collected 10 trials for each task, varying the positions of objects and distractors between trials.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 8 (5 Experiments), p. 7 (5 Experiments) |
| Embodiment/environment | Assembling a large real-world dataset is time-consuming and expensive, so there has also been significant work on developing simulated environments and datasets for robotic manipulation [15, 40, 41, 42] and navigation [43, ... | hardware/simulator version and reset protocol | p. 3 (Dataset), p. 3 (Dataset) |
| Dataset/benchmark | Annotators were asked to describe the task being performed by the robot in each trajectory, with particular emphasis on the final location of any moved objects. | role, split, size and leakage | p. 3 (Dataset), p. 3 (Dataset), p. 4 (Dataset), p. 7 (5 Experiments) |
| Metric | ResNet-18 ResNet-34 ResNet-50 Image Encoder 0.0 0.2 0.4 0.6 0.8 1.0 Average Success Rate 0.25 0.50 0.75 1.00 Proportion of Dataset 0.0 0.2 0.4 0.6 0.8 1.0 Average Success Rate Seen Unseen ... | definition, denominator, direction and uncertainty | p. 8 (5 Experiments), p. 6 (5 Experiments), p. 6 (5 Experiments) |
| Baseline/ablation | Once again, RT-1 greatly outperformed the LCBC baseline. | fair input/data/compute/action matching | p. 7 (5 Experiments), p. 6 (5 Experiments), p. 8 (5 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5 Experiments - extractive body cue:** 6 Discussion, Limitations, and Future Work We presented BridgeData V2, a dataset with 60,096 trajectories of robotic manipulation behaviors designed to enable research on scalable ...
- **p. 4 / Dataset - extractive body cue:** While this policy fails frequently, we can run it autonomously to collect a large amount of pick-and-place data for a wide range of objects more ...
- **p. 7 / 5 Experiments - extractive body cue:** Additionally, the "put eggplant in pot" is a very challenging task in both labs since the eggplant easily slips out of the gripper.
- **p. 3 / Dataset - extractive body cue:** Training on a combination of the largest datasets released so far is an exciting and promising direction for future work.
- **p. 3 / Dataset - extractive body cue:** However, it is difficult to replicate the complexity of the real world (e.g., objects, environments, lighting, and physics) in a simulator well enough to thoroughly ...
- **p. 4 / Dataset - extractive body cue:** Methods that benefit from suboptimal data, such as offline RL, can leverage this autonomous data to learn more robust behaviors.
- **p. 7 / 5 Experiments - extractive body cue:** RT-1 especially showed only a small degradation in performance.

## Why Read It

Manipulation, contact, tactile, and dexterity의 il 문제를 이해하기 위해 읽는다. 본문은 However, in practice, assembling a dataset with the right features to accelerate research in large-scale robot learning presents a significant challenge.를 문제로 두고, In this paper, we propose a new dataset, which we call BridgeData V2 (Figure 1) because it greatly expands on the previously released Bridge Dataset [6].를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 14 (B.2 Diffusion goal-conditioned behavior cloning), p. 14 (B.4 Contrastive RL), p. 15 (B.6 RT-1), p. 13 (B Learning Method Implementation Details) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
