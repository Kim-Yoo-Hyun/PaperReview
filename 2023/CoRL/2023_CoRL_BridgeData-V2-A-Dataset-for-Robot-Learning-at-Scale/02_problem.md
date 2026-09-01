# Problem - BridgeData V2: A Dataset for Robot Learning at Scale

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2308.12952; PDF retrieval source: https://arxiv.org/pdf/2308.12952. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction)): However, in practice, assembling a dataset with the right features to accelerate research in large-scale robot learning presents a significant challenge.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** We introduce BridgeData V2, a large and diverse dataset of robotic manipulation behaviors designed to facilitate research on scalable robot learning.
- **p. 1 / Abstract - extractive PDF cue:** BridgeData V2 contains 60,096 trajectories collected across 24 environments on a publicly available low-cost robot.
- **p. 1 / Abstract - extractive PDF cue:** BridgeData V2 provides extensive task and environment variability, leading to skills that can generalize across environments, domains, and institutions, making the dataset a useful resource ...
- **p. 1 / Abstract - extractive PDF cue:** Additionally, the dataset is compatible with a wide variety of openvocabulary, multi-task learning methods conditioned on goal images or natural language instructions.
- **p. 1 / Abstract - extractive PDF cue:** In our experiments, we train 6 state-of-the-art imitation learning and offline reinforcement learning methods on our dataset, and find that they succeed on a suite ...
- **p. 2 / 1 Introduction - extractive PDF cue:** However, in practice, assembling a dataset with the right features to accelerate research in large-scale robot learning presents a significant challenge.
- **p. 2 / 1 Introduction - extractive PDF cue:** A useful robotic system needs skills that generalize across the wide variety of conditions found in the real world.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, in practice, assembling a dataset with the right features to accelerate research in large-scale robot learning presents a significant challenge. | demonstration으로 정의된 robot task distribution | body wording is the source claim |
| Observation / input | First, given the observation and goal images, we feed them separately through a ResNet-34 encoder instead of a 3-layer CNN image encoder ... | observation history와 expert trajectory/action | exact sensor/frame/preprocessing from PDF |
| State / latent | First, given, observation, goal, images, feed, them, separately, through, ResNet-34 | behavior policy와 temporal action context | notation and tensor shape require body check |
| Output / action | Additionally, dataset, should, support, flexible, task, conditioning, through | predicted action 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | closed-loop task success and robustness | imitation error, task success, robustness와 compounding error | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | observation history o_{t−H:t}; body terms: First, given, observation, goal, images, feed, them, separately, through, ResNet-34 | p. 14 (B.4 Contrastive RL), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Decision / output variable | expert-like action/chunk a_{t:t+H}; body terms: dataset, call, BridgeData, Figure, because, greatly, expands, previously | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 15 (B.4 Contrastive RL) |
| Objective / loss / cost | imitation or action-distribution loss; cue terms: contrastive, objective, retains, temporal-difference, style, DDPM, Denoising, Diffusion | p. 14 (B.4 Contrastive RL), p. 14 (B.2 Diffusion goal-conditioned behavior cloning) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 14 (B.4 Contrastive RL), p. 14 (B.2 Diffusion goal-conditioned behavior cloning), p. 15 (B.5 Language-conditioned behavior cloning) |
| Success / guarantee | closed-loop task success and robustness | p. 8 (5 Experiments), p. 6 (5 Experiments), p. 6 (5 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive PDF cue:** A useful robotic system needs skills that generalize across the wide variety of conditions found in the real world.

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 15 (B.4 Contrastive RL)): In this paper, we propose a new dataset, which we call BridgeData V2 (Figure 1) because it greatly expands on the previously released Bridge Dataset [6].

- **p. 2 / 1 Introduction - extractive PDF cue:** Our contributions are a new dataset of robotic manipulation behaviors as well as the empirical study of state-of-the-art offline learning methods using the introduced dataset.
- **p. 15 / B.4 Contrastive RL - extractive PDF cue:** The greater size and diversity of BridgeData V2 enables significantly better generalization to these unseen tasks.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | 6 Discussion, Limitations, and Future Work We presented BridgeData V2, a dataset with 60,096 trajectories of robotic manipulation ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | While this policy fails frequently, we can run it autonomously to collect a large amount of pick-and-place data ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Additionally, the "put eggplant in pot" is a very challenging task in both labs since the eggplant easily ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Training on a combination of the largest datasets released so far is an exciting and promising direction for ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

il writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 14 (B.4 Contrastive RL), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 14 (B.1 Goal-conditioned behavior cloning). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 14 (B.4 Contrastive RL), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 14 (B.1 Goal-conditioned behavior cloning), objective p. 14 (B.4 Contrastive RL), p. 14 (B.2 Diffusion goal-conditioned behavior cloning).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
