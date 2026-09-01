# DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (33 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2602.06949.
> PDF retrieval source: https://arxiv.org/abs/2602.06949. Reading tracker status/evidence was not changed.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, world model, human video, generalist policy, NVIDIA
- Official paper: https://arxiv.org/abs/2602.06949
- Full-text retrieval: https://arxiv.org/abs/2602.06949
- Code/Project: https://research.nvidia.com/labs/gear/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (33 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 Additionally, existing datasets predominantly consist of expert demonstrations, lacking the stochasticity in intentions necessary for learning strong action controllability.를 문제로 두고, By scaling up human videos and introducing continuous latent actions as unified proxy, we present DreamDojo, the first world model of its kind that shows zero-shot generalization to unseen objects and novel ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Being able to simulate the outcomes of actions in varied environments will revolutionize the development of generalist agents at scale.
- **p. 1 / Abstract - extractive body cue:** However, modeling these world dynamics, especially for dexterous robotics tasks, poses significant challenges due to limited data coverage and scarce action labels.
- **p. 1 / Abstract - extractive body cue:** As an endeavor towards this end, we introduce DreamDojo, a foundation world model that learns diverse interactions and dexterous controls from 44k hours of egocentric ...
- **p. 1 / Abstract - extractive body cue:** Our data mixture represents the largest video dataset to date for world model pretraining, spanning a wide range of daily scenarios with diverse objects and ...
- **p. 1 / Abstract - extractive body cue:** To address the scarcity of action labels, we introduce continuous latent actions as unified proxy actions, enhancing interaction knowledge transfer from unlabeled videos.
- **p. 2 / 1. Introduction - extractive body cue:** Additionally, existing datasets predominantly consist of expert demonstrations, lacking the stochasticity in intentions necessary for learning strong action controllability.
- **p. 3 / 1. Introduction - extractive body cue:** DreamDojo can robustly generalize to various objects and environments, facilitating large-scale policy evaluation without real-world deployment.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** By scaling up human videos and introducing continuous latent actions as unified proxy, we present DreamDojo, the first world model of its kind that shows ...
- **p. 2 / 1. Introduction - extractive body cue:** In this work, we introduce DreamDojo, a foundation world model for open-world dexterous robot tasks.
- **p. 3 / 3.1. Overview - extractive body cue:** Our whole training procedure consists of three phases: 3
- **p. 5 / 3.3.1. Model Architecture - extractive body cue:** To realize precise action following, we propose two improvements based on the original architecture.
- **p. 3 / 1. Introduction - extractive body cue:** It also enables live teleoperation and online model-based planning.
- **p. 6 / 3.3.1. Model Architecture - extractive body cue:** DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos x1 x2 Latent Action Encoder Latent Action Decoder ât ft ft+1 ft+1 ft+1 ft+1 ft+1 ...
- **p. 7 / 3.3.2. Pretraining from Human Videos - extractive body cue:** We establish a latent action model as a VAE (Kingma and Welling, 2013) using the spatiotemporal Transformer architecture (Bruce et al., 2024).
- **p. 6 / 3.3.1. Model Architecture - extractive body cue:** [Left]: The information bottleneck design of our latent action model enforces action disentanglement, producing a continuous latent vector that represents actions between frames.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | First, instead of using the absolute robot joint poses, we transform them into relative actions by rebaselining the inputs with the pose at the beginning of each latent frame (i.e., every 4 ... | observation, uncertainty/risk estimate와 task command | p. 5 (3.3.1. Model Architecture), p. 2 (1. Introduction) |
| State/latent | First, instead, absolute, robot, joint, poses, transform, them, relative, actions, rebaselining, inputs | safe set, recovery state 또는 constraint margin | p. 5 (3.3.1. Model Architecture), p. 2 (1. Introduction), p. 3 (2. Preliminary) |
| Output/action | Naively training on passive videos overlooks the causality between video observations and actions, leading to inferior knowledge transfer for action-conditioned world simulation. | shielded, recovery 또는 safe action | p. 2 (1. Introduction), p. 3 (2. Preliminary), p. 3 (2. Preliminary) |
| Objective/outcome | To supervise the student's prediction, we randomly select a window of size 𝑁, which receives gradients via the ℒdistill loss (Eq. | task return과 violation/failure probability | p. 8 (3.3.4. Distillation), p. 8 (3.3.4. Distillation), p. 7 (3.3.2. Pretraining from Human Videos) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** By scaling up human videos and introducing continuous latent actions as unified proxy, we present DreamDojo, the first world model of its kind that shows ...
- **p. 2 / 1. Introduction - extractive body cue:** In this work, we introduce DreamDojo, a foundation world model for open-world dexterous robot tasks.
- **p. 3 / 3.1. Overview - extractive body cue:** Our whole training procedure consists of three phases: 3
- **p. 5 / 3.3.1. Model Architecture - extractive body cue:** To realize precise action following, we propose two improvements based on the original architecture.
- **p. 3 / 1. Introduction - extractive body cue:** It also enables live teleoperation and online model-based planning.
- **p. 13 / Figure/Table caption - extractive body cue:** Table 7: Generalization ability after distillation. Thanks to our strong pretraining, DreamDojo shows consistently better generalization than the baseline after distillation. Lastly, we ablate the ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 6: Live teleoperation. We can teleoperate a virtual G1 robot using the PICO VR controller in real time. to DreamDojo to predict future video ...
- **p. 12 / 4.5. Ablations of Our Design Choices - extractive body cue:** Both relative actions and chunked injection can significantly improve simulation quality, indicating their importance for achieving precise action controllability.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 13 (Figure/Table caption), p. 14 (Figure/Table caption) |
| Embodiment/environment | Our curated data mixture excels in both scale and diversity, encompassing 15× longer duration, 96× more skills, and 2,000× more scenes than the previously largest dataset for world model training. †Estimated by ... | hardware/simulator version and reset protocol | p. 5 (3.2. DreamDojo-HV Dataset), p. 9 (4. Experiments) |
| Dataset/benchmark | It contains several new objects and new verbs that are unseen in our default robot training dataset. | role, split, size and leakage | p. 5 (3.2. DreamDojo-HV Dataset), p. 9 (4. Experiments), p. 5 (3.2. DreamDojo-HV Dataset), p. 10 (0.219 Method) |
| Metric | The final success rate is averaged across all 20 scenes for both real-world and DreamDojo. | definition, denominator, direction and uncertainty | p. 13 (4.7. Downstream Applications), p. 13 (4.7. Downstream Applications), p. 14 (4.7. Downstream Applications) |
| Baseline/ablation | Table 7: Generalization ability after distillation. Thanks to our strong pretraining, DreamDojo shows consistently better generalization than the baseline after distillation. Lastly, we ablate the choice of teacher model in Tab. 7, ... | fair input/data/compute/action matching | p. 13 (Figure/Table caption), p. 8 (4. Experiments), p. 10 (0.219 Method) |

## Explicit Limitations and Failure Boundary

- **p. 15 / 5. Conclusion - extractive body cue:** Additionally, when conducting policy evaluation, the absolute success rates in DreamDojo are often higher than their real counterparts, indicating a limitation in accurately generating nuanced ...
- **p. 4 / 3.2. DreamDojo-HV Dataset - extractive body cue:** As a result, training on these datasets often fails to preserve the model's abilities when extending to out-of-distribution scenarios.
- **p. 15 / 5. Conclusion - extractive body cue:** Future work should explore how to cover broader action distribution, e.g., using policy rollouts (Ho et al., 2025; Zhu et al., 2025).
- **p. 4 / 3.2. DreamDojo-HV Dataset - extractive body cue:** To address this limitation, one might consider increasing the scale of real robot data.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Latent action model. [Left]: The information bottleneck design of our latent action model enforces action disentanglement, producing a continuous latent vector that represents ...
- **p. 16 / 5. Conclusion - extractive body cue:** In contrast, we introduce the first foundation world model for dexterous manipulation, which exhibits strong generalization in simulating diverse out-of-distribution manipulation skills across multiple embodiments.
- **p. 16 / 5. Conclusion - extractive body cue:** Inspired by these explorations, we extract latent actions as a unified proxy for our foundation world model and investigate how this approach can promote robust ...

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 Additionally, existing datasets predominantly consist of expert demonstrations, lacking the stochasticity in intentions necessary for learning strong action controllability.를 문제로 두고, By scaling up human videos and introducing continuous latent actions as unified proxy, we present DreamDojo, the first world model of its kind that shows zero-shot generalization to unseen objects and novel ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 6 (3.3.1. Model Architecture), p. 7 (3.3.2. Pretraining from Human Videos), p. 5 (3.3.1. Model Architecture) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
