# NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2310.07896.
> PDF retrieval source: https://arxiv.org/pdf/2310.07896. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: NEXT
- Tags: Robotics, Navigation, diffusion policy, exploration
- Official paper: https://arxiv.org/abs/2310.07896
- Full-text retrieval: https://arxiv.org/pdf/2310.07896
- Code/Project: https://general-navigation-models.github.io/nomad/
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 navigation 문제를 이해하기 위해 읽는다. 본문은 Prior works have often addressed this challenge by training a separate high-level policy or goal proposal system that generates suitable exploratory tasks, for example using high-level planning [1], hierarchical reinforcement learning [ ...를 문제로 두고, In this paper, we present a design for such a policy by combining a Transformer backbone for encoding the highdimensional stream of visual observations with diffusion models for modeling a sequence of ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robotic learning for navigation in unfamiliar environments needs to provide policies for both task-oriented navigation (i.e., reaching a goal that the robot has located), and ...
- **p. 1 / Abstract - extractive body cue:** Typically, these roles are handled by separate models, for example by using subgoal proposals, planning, or separate navigation strategies.
- **p. 1 / Abstract - extractive body cue:** In this paper, we describe how we can train a single unified diffusion policy to handle both goal-directed navigation and goal-agnostic exploration, with the latter ...
- **p. 1 / Abstract - extractive body cue:** We show that this unified policy results in better overall performance when navigating to visually indicated goals in novel environments, as compared to approaches that ...
- **p. 1 / Abstract - extractive body cue:** We instantiate our method by using a large-scale Transformerbased policy trained on data from multiple ground robots, with a diffusion model decoder to flexibly handle ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Prior works have often addressed this challenge by training a separate high-level policy or goal proposal system that generates suitable exploratory tasks, for example using ...
- **p. 2 / III. PRELIMINARIES - extractive body cue:** While ViNT shows state-of-the-art performance in goal-conditioned navigation, it cannot perform undirected exploration and requires an external subgoal proposal mechanism.

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present a design for such a policy by combining a Transformer backbone for encoding the highdimensional stream of visual observations with ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The main contribution of our work is Navigation with Goal Masked Diffusion, or NoMaD, a novel architecture for robotic navigation in previously unseen environments.
- **p. 4 / IV. METHOD - extractive body cue:** The noise prediction network, ϵθ, consists of a 1D conditional U-Net [29, 31] with 15 convolutional layers.
- **p. 4 / IV. METHOD - extractive body cue:** Note that we model the conditional (and not joint) action distribution, excluding ct from the output of the denoising process, which enables real-time control and ...
- **p. 3 / IV. METHOD - extractive body cue:** Training a shared policy across both behaviors allows the model to learn a more expressive prior over actions at, which can be used for both ...
- **p. 4 / IV. METHOD - extractive body cue:** For the ViNT observation encoder, we use EfficientNet-B0 [39] to tokenize observations and goals into 256-dimensional embeddings, followed by a Transformer decoder with 4 layers ...
- **p. 3 / IV. METHOD - extractive body cue:** To effectively model such complex distributions, we use a diffusion model [23] to approximate the conditional distribution p(at/ct), where ct is the observation context obtained ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our objective is to design a control policy π for visual navigation that takes the robot's current and past RGB observations as input ot := ot-P :t and outputs a distribution over ... | camera/depth stream, pose, map와 language goal | p. 2 (III. PRELIMINARIES), p. 1 (I. INTRODUCTION) |
| State/latent | objective, design, control, policy, visual, navigation, takes, robot, current, past, RGB, observations | robot pose, free-space/semantic map와 local goal | p. 2 (III. PRELIMINARIES), p. 1 (I. INTRODUCTION), p. 2 (III. PRELIMINARIES) |
| Output/action | In this paper, we present a design for such a policy by combining a Transformer backbone for encoding the highdimensional stream of visual observations with diffusion models for modeling a sequence of ... | collision-free trajectory 또는 velocity command | p. 1 (I. INTRODUCTION), p. 2 (III. PRELIMINARIES), p. 3 (IV. METHOD) |
| Objective/outcome | The predicted noise is compared to the actual noise through the mean squared error (MSE) loss. | goal reach, safety, localization error와 replanning latency | p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 3 (IV. METHOD) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present a design for such a policy by combining a Transformer backbone for encoding the highdimensional stream of visual observations with ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The main contribution of our work is Navigation with Goal Masked Diffusion, or NoMaD, a novel architecture for robotic navigation in previously unseen environments.
- **p. 4 / IV. METHOD - extractive body cue:** The noise prediction network, ϵθ, consists of a 1D conditional U-Net [29, 31] with 15 convolutional layers.
- **p. 4 / IV. METHOD - extractive body cue:** Note that we model the conditional (and not joint) action distribution, excluding ct from the output of the denoising process, which enables real-time control and ...
- **p. 3 / IV. METHOD - extractive body cue:** Training a shared policy across both behaviors allows the model to learn a more expressive prior over actions at, which can be used for both ...
- **p. 5 / V. EVALUATION - extractive body cue:** NoMaD consistently outperforms all baselines and results in smooth, reactive policies.
- **p. 5 / V. EVALUATION - extractive body cue:** Success Masked ViNTm 15M 50% 1.0 30% VIB [17] 6M 30% 4.0 15% Autoregressivem 19M 90% 2.0 60% Random Subgoals [3] 30M 70% 2.7 90% ...
- **p. 6 / V. EVALUATION - extractive body cue:** NoMaD outperforms both the ViT- and CNN-based architectures, successfully reaching the goal while avoiding collisions.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (V. EVALUATION), p. 5 (V. EVALUATION) |
| Embodiment/environment | Benchmarking Performance Towards understanding Q1, we compare NoMaD to six performant baselines for exploration and navigation in 6 challenging real-world environments. | hardware/simulator version and reset protocol | p. 4 (V. EVALUATION), p. 4 (V. EVALUATION) |
| Dataset/benchmark | Success Masked ViNTm 15M 50% 1.0 30% VIB [17] 6M 30% 4.0 15% Autoregressivem 19M 90% 2.0 60% Random Subgoals [3] 30M 70% 2.7 90% Subgoal Diffusion [3] 335M 77% 1.7 90% ... | role, split, size and leakage | p. 4 (V. EVALUATION), p. 4 (V. EVALUATION), p. 5 (V. EVALUATION), p. 5 (V. EVALUATION) |
| Metric | We report the mean success rate for each baseline, as well as the mean number of collisions per experiment. | definition, denominator, direction and uncertainty | p. 4 (V. EVALUATION), p. 6 (V. EVALUATION), p. 6 (V. EVALUATION) |
| Baseline/ablation | Most notably, NoMaD outperforms the state-of-the-art (Subgoal Diffusion) by 25%, while also avoiding collisions and requiring 15× fewer parameters. mThese baselines that use goal masking. images, which are used by the policy ... | fair input/data/compute/action matching | p. 5 (V. EVALUATION), p. 5 (V. EVALUATION), p. 6 (V. EVALUATION) |

## Explicit Limitations and Failure Boundary

- **p. 6 / VI. DISCUSSION - extractive body cue:** While our experiments provide a proof of concept that unified policies can provide more effective navigation in new environments, our system has a number of ...
- **p. 3 / 8 Future - extractive body cue:** Exploration with topological maps: While goalconditioned policies can exhibit useful affordances and collision-avoidance behavior, they may be insufficient for navigation in large environments that require ...
- **p. 4 / V. EVALUATION - extractive body cue:** We report the mean success rate for each baseline, as well as the mean number of collisions per experiment.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Visualizing the task-agnostic (yellow) and goal-directed pathways for two goal images (green, blue) learned by NoMaD. NoMaD predicts a bimodal distribution of collision-free ...
- **p. 5 / V. EVALUATION - extractive body cue:** VIB and Masked ViNT struggle in all the environments we tested and frequently end in collisions, likely due to challenges with effectively modeling multimodal action ...
- **p. 5 / V. EVALUATION - extractive body cue:** For exploratory goal discovery, NoMaD outperforms the best published baseline (Subgoal Diffusion) by over 25% in terms of both efficiency and collision avoidance, and succeeds ...
- **p. 6 / V. EVALUATION - extractive body cue:** NoMaD outperforms both the ViT- and CNN-based architectures, successfully reaching the goal while avoiding collisions.

## Why Read It

Planning and control의 navigation 문제를 이해하기 위해 읽는다. 본문은 Prior works have often addressed this challenge by training a separate high-level policy or goal proposal system that generates suitable exploratory tasks, for example using high-level planning [1], hierarchical reinforcement learning [ ...를 문제로 두고, In this paper, we present a design for such a policy by combining a Transformer backbone for encoding the highdimensional stream of visual observations with diffusion models for modeling a sequence of ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 2 (III. PRELIMINARIES), p. 1 (I. INTRODUCTION), p. 2 (III. PRELIMINARIES), p. 4 (IV. METHOD), p. 3 (IV. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** In this work, we study a particularly important instance of this problem in the domain of robotic navigation, where the user might specify a destination visually (i.e., via a picture), ... (p. 1, I. INTRODUCTION).
- **Actual contribution:** The main contribution of our work is Navigation with Goal Masked Diffusion, or NoMaD, a novel architecture for robotic navigation in previously unseen environments. (p. 1, I. INTRODUCTION).
- **Evaluation boundary:** Benchmarking Performance Towards understanding Q1, we compare NoMaD to six performant baselines for exploration and navigation in 6 challenging real-world environments. (p. 4, V. EVALUATION).
- **Explicit failure boundary:** VIB and Masked ViNT struggle in all the environments we tested and frequently end in collisions, likely due to challenges with effectively modeling multimodal action distributions. (p. 5, V. EVALUATION).
