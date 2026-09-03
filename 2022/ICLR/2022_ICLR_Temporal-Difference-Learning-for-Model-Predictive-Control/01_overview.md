# Temporal Difference Learning for Model Predictive Control

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2203.04955.
> PDF retrieval source: https://arxiv.org/pdf/2203.04955. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: Robotics, world model, model predictive control, Reinforcement Learning
- Official paper: https://arxiv.org/abs/2203.04955
- Full-text retrieval: https://arxiv.org/pdf/2203.04955
- Code/Project: https://www.nicklashansen.com/td-mpc/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 To overcome these challenges, we make three key changes to model learning.를 문제로 두고, (Top) We present a framework for MPC using a task-oriented latent dynamics model and value function learned jointly by temporal difference learning.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Data-driven model predictive control has two key advantages over model-free methods: a potential for improved sample efficiency through model learning, and better performance as computational ...
- **p. 1 / Abstract - extractive body cue:** However, it is both costly to plan over long horizons and challenging to obtain an accurate model of the environment.
- **p. 1 / Abstract - extractive body cue:** In this work, we combine the strengths of model-free and model-based methods.
- **p. 1 / Abstract - extractive body cue:** We use a learned task-oriented latent dynamics model for local trajectory optimization over a short horizon, and use a learned terminal value function to estimate ...
- **p. 1 / Abstract - extractive body cue:** Our method, TD-MPC, achieves superior sample efficiency and asymptotic performance over prior work on both state and image-based continuous control tasks from DMControl and MetaWorld.
- **p. 2 / 1. Introduction - extractive body cue:** To overcome these challenges, we make three key changes to model learning.
- **p. 2 / 1. Introduction - extractive body cue:** While prior work learns a model through state or video prediction, we argue that it is remarkably inefficient to model everything in the environment, including ...

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** (Top) We present a framework for MPC using a task-oriented latent dynamics model and value function learned jointly by temporal difference learning.
- **p. 1 / 1. Introduction - extractive body cue:** (Bottom) Episode return of our method, SAC, and MPC with a ground-truth simulator on challenging, highdimensional Humanoid and Dog tasks (Tassa et al., 2018).
- **p. 2 / 1. Introduction - extractive body cue:** Lastly, we propose a modality-agnostic prediction loss in latent space that enforces temporal consistency in the learned representation without explicit state or image prediction.
- **p. 2 / 1. Introduction - extractive body cue:** In particular, our method solves Humanoid and Dog locomotion tasks with up to 38-dimensional continuous action spaces in as little as 1M environment steps (see ...
- **p. 3 / 3. TD-Learning for Model Predictive Control - extractive body cue:** We summarize our framework in Figure 1 and Algorithm 1.
- **p. 4 / 4. Task-Oriented Latent Dynamics Model - extractive body cue:** Our proposed TOLD consists of five learned components hθ, dθ, Rθ, Qθ, πθ that predict the following quantities: Representation: zt = hθ(st) Latent dynamics: zt+1 ...
- **p. 5 / 4. Task-Oriented Latent Dynamics Model - extractive body cue:** Instead, we propose to regularize TOLD with a latent state consistency loss (shown in Equation 10) that forces a future latent state prediction zt+1 = ...
- **p. 4 / 4. Task-Oriented Latent Dynamics Model - extractive body cue:** During training, we minimize a temporally weighted objective J (θ; Γ) = t+H X i=t λi-tL(θ; Γi) , (7) where Γ ∼B is a trajectory ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (2015)) control for planning (denoted Πθ), learned models dθ, Rθ of the (latent) dynamics and reward signal, respectively, a terminal state-action value function Qθ, and a parameterized policy πθ that helps guide ... | observation, uncertainty/risk estimate와 task command | p. 3 (3. TD-Learning for Model Predictive Control), p. 3 (3. TD-Learning for Model Predictive Control) |
| State/latent | control, planning, denoted, learned, models, latent, dynamics, reward, signal, respectively, terminal, state-action | safe set, recovery state 또는 constraint margin | p. 3 (3. TD-Learning for Model Predictive Control), p. 3 (3. TD-Learning for Model Predictive Control), p. 5 (4. Task-Oriented Latent Dynamics Model) |
| Output/action | H from N(µj-1, (σj-1)2I) 4: Sample Nπ traj. of length H using πθ, dθ // Estimate trajectory returns φΓ using dθ, Rθ, Qθ, starting from zt and initially letting φΓ = 0: ... | shielded, recovery 또는 safe action | p. 3 (3. TD-Learning for Model Predictive Control), p. 5 (4. Task-Oriented Latent Dynamics Model), p. 2 (2. Preliminaries) |
| Objective/outcome | During training, we minimize a temporally weighted objective J (θ; Γ) = t+H X i=t λi-tL(θ; Γi) , (7) where Γ ∼B is a trajectory (st, at, rt, st+1)t:t+H sampled from a ... | task return과 violation/failure probability | p. 4 (4. Task-Oriented Latent Dynamics Model), p. 5 (4. Task-Oriented Latent Dynamics Model), p. 5 (4. Task-Oriented Latent Dynamics Model) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** (Top) We present a framework for MPC using a task-oriented latent dynamics model and value function learned jointly by temporal difference learning.
- **p. 1 / 1. Introduction - extractive body cue:** (Bottom) Episode return of our method, SAC, and MPC with a ground-truth simulator on challenging, highdimensional Humanoid and Dog tasks (Tassa et al., 2018).
- **p. 2 / 1. Introduction - extractive body cue:** Lastly, we propose a modality-agnostic prediction loss in latent space that enforces temporal consistency in the learned representation without explicit state or image prediction.
- **p. 2 / 1. Introduction - extractive body cue:** In particular, our method solves Humanoid and Dog locomotion tasks with up to 38-dimensional continuous action spaces in as little as 1M environment steps (see ...
- **p. 3 / 3. TD-Learning for Model Predictive Control - extractive body cue:** We summarize our framework in Figure 1 and Algorithm 1.
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 14. Individual Meta-World tasks. Success rate of our method (TD-MPC) and SAC on diverse manipulation tasks from Meta- World (Yu et al., 2019). We ...
- **p. 17 / Figure/Table caption - extractive body cue:** Table 8. Meta-World MT10. As our performance metric reported in Figure 5 differs from that of the Meta-World v2 benchmark proposal (Yu et al., 2019), ...
- **p. 8 / 5. Experiments - extractive body cue:** Success rate on 50 goal-conditioned Meta-World tasks using individual policies, and a multi-task policy trained on 10 tasks simultaneously (Meta-World MT10).

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 19 (Figure/Table caption), p. 17 (Figure/Table caption) |
| Embodiment/environment | TD-Learning for MPC 0 250 500 750 1000 Episode return Average 0 100 200 300 400 Acrobot Swingup 0 250 500 750 1000 Cartpole Swingup 0 250 500 750 1000 Cartpole Swingup ... | hardware/simulator version and reset protocol | p. 6 (5. Experiments), p. 7 (5. Experiments) |
| Dataset/benchmark | Throughout, we benchmark performance on relatively few environment steps, e.g., 3M steps for Humanoid tasks whereas prior work typically runs for 30M steps (10×). | role, split, size and leakage | p. 6 (5. Experiments), p. 7 (5. Experiments), p. 7 (5. Experiments), p. 5 (5. Experiments) |
| Metric | In contrast, a blind agent that does not 0.0 0.2 0.4 0.6 0.8 1.0 0.00 0.25 0.50 0.75 1.00 Success rate Meta-World (Goal-Conditioned) 0 1 2 3 0.00 0.25 0.50 0.75 1.00 ... | definition, denominator, direction and uncertainty | p. 8 (5. Experiments), p. 8 (Figure/Table caption), p. 19 (Figure/Table caption) |
| Baseline/ablation | Figure 4. Learning from pixels. Return of our method (TD-MPC) and state-of-the-art algorithms on 12 challenging image-based DMControl tasks. We follow prior work (Hafner et al., 2020b;a; Yarats et al., 2021) and ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 8 (5. Experiments), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 5. Experiments - extractive body cue:** Due to dimensionality explosion under discretization, MuZero and EfficientZero cannot feasibly solve tasks with higher-dimensional action spaces, e.g., Walker Walk and Cheetah Run (A ∈R6), ...
- **p. 8 / 5. Experiments - extractive body cue:** Mean of 5 runs. have access to the egocentric camera fails.
- **p. 8 / 5. Experiments - extractive body cue:** Performance of LOOP is similar to SAC, and MPC with a simulator (MPC:sim) performs well on locomotion tasks but fails in tasks with sparse rewards.

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 To overcome these challenges, we make three key changes to model learning.를 문제로 두고, (Top) We present a framework for MPC using a task-oriented latent dynamics model and value function learned jointly by temporal difference learning.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 4 (4. Task-Oriented Latent Dynamics Model), p. 5 (4. Task-Oriented Latent Dynamics Model) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
