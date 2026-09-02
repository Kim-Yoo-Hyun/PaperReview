# ViNT: A Foundation Model for Visual Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2306.14846.
> PDF retrieval source: https://arxiv.org/pdf/2306.14846. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, Navigation, visual navigation, foundation model, goal-conditioned policy, cross-platform
- Official paper: https://arxiv.org/abs/2306.14846
- Full-text retrieval: https://arxiv.org/pdf/2306.14846
- Code/Project: https://general-navigation-models.github.io/vint/index.html
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 navigation 문제를 이해하기 위해 읽는다. 본문은 Although this paradigm has been successful in many domains, it is difficult to apply in robotics due to the sheer diversity of environments, platforms, and applications.를 문제로 두고, We propose a novel exploration algorithm for the visual navigation paradigm using a diffusion model to propose short-horizon goals, and demonstrate that it enables ViNT to navigate in novel environments.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** General-purpose pre-trained models ("foundation models") have enabled practitioners to produce generalizable solutions for individual machine learning problems with datasets that are significantly smaller than those ...
- **p. 1 / Abstract - extractive body cue:** Such models are typically trained on large and diverse datasets with weak supervision, consuming much more training data than is available for any individual downstream ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we describe the Visual Navigation Transformer (ViNT), a foundation model that aims to bring the success of general-purpose pre-trained models to vision-based ...
- **p. 1 / Abstract - extractive body cue:** ViNT is trained with a general goal-reaching objective that can be used with any navigation dataset, and employs a flexible Transformer-based architecture to learn navigational ...
- **p. 1 / Abstract - extractive body cue:** ViNT is trained on a number of existing navigation datasets, comprising hundreds of hours of robotic navigation from a variety of different robotic platforms, and ...
- **p. 1 / 1 Introduction - extractive body cue:** Although this paradigm has been successful in many domains, it is difficult to apply in robotics due to the sheer diversity of environments, platforms, and ...
- **p. 2 / 1 Introduction - extractive body cue:** We specifically consider the problem of visual navigation, where the robot must navigate its environment solely using egocentric visual observations.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** We propose a novel exploration algorithm for the visual navigation paradigm using a diffusion model to propose short-horizon goals, and demonstrate that it enables ViNT ...
- **p. 2 / 1 Introduction - extractive body cue:** To this end, we propose the Visual Navigation Transformer, or ViNT: a cross-embodiment foundation model for visual navigation with strong zero-shot generalization.
- **p. 20 / B.3 Long-Horizon Physical Search via Topological Graphs - extractive body cue:** Each ResNet consists of 2 residual blocks.
- **p. 19 / B.3 Long-Horizon Physical Search via Topological Graphs - extractive body cue:** For our experiments, we considered three heuristics to demonstrate the flexibility of our approach: • Coverage exploration: We have no long-horizon guidance for coverage exploration, ...
- **p. 18 / B.2 Subgoal Diffusion - extractive body cue:** To produce training pairs for the diffusion model, we first select ot uniformly at random from the training data and then select osi to fall ...
- **p. 18 / B.2 Subgoal Diffusion - extractive body cue:** [49], we use the unweighted training objective, called Lsimple in Ho et al.
- **p. 21 / B.4 Fine-tuning ViNT - extractive body cue:** This architecture is illustrated in Figure 14. • Training: For our experiments, we use "left", "right", and "straight" as our discrete commands.
- **p. 21 / B.4 Fine-tuning ViNT - extractive body cue:** We then pass this into a 2-layer MLP which outputs the prediction of the final token for the transformer.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | It takes an image ot as input and produces samples from g(osi / ot), where osi are candidate subgoal images reachable from ot. | camera/depth stream, pose, map와 language goal | p. 18 (B.2 Subgoal Diffusion), p. 20 (B.3 Long-Horizon Physical Search via Topological Graphs) |
| State/latent | takes, image, input, produces, samples, where, candidate, subgoal, images, reachable, Algorithm, Long-Horizon | robot pose, free-space/semantic map와 local goal | p. 18 (B.2 Subgoal Diffusion), p. 20 (B.3 Long-Horizon Physical Search via Topological Graphs), p. 18 (B.2 Subgoal Diffusion) |
| Output/action | Algorithm 1: Long-Horizon Navigation via Topological Graph 1: while goal G not reached do 2: s ←minf(Ω); 3: P ←ShortestPath(M, ot, s-) 4: for (s, s′) in P do 5: ViNT.GoToGoal(s′); 6: ... | collision-free trajectory 또는 velocity command | p. 20 (B.3 Long-Horizon Physical Search via Topological Graphs), p. 18 (B.2 Subgoal Diffusion), p. 19 (B.3 Long-Horizon Physical Search via Topological Graphs) |
| Objective/outcome | We train a convolutional neural network on the overhead image to predict the probability that the subgoal s is included on a trajectory from ot to G, trained using a contrastive objective ... | goal reach, safety, localization error와 replanning latency | p. 20 (B.3 Long-Horizon Physical Search via Topological Graphs), p. 18 (B.2 Subgoal Diffusion), p. 19 (B.3 Long-Horizon Physical Search via Topological Graphs) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** We propose a novel exploration algorithm for the visual navigation paradigm using a diffusion model to propose short-horizon goals, and demonstrate that it enables ViNT ...
- **p. 2 / 1 Introduction - extractive body cue:** To this end, we propose the Visual Navigation Transformer, or ViNT: a cross-embodiment foundation model for visual navigation with strong zero-shot generalization.
- **p. 20 / B.3 Long-Horizon Physical Search via Topological Graphs - extractive body cue:** Each ResNet consists of 2 residual blocks.
- **p. 19 / B.3 Long-Horizon Physical Search via Topological Graphs - extractive body cue:** For our experiments, we considered three heuristics to demonstrate the flexibility of our approach: • Coverage exploration: We have no long-horizon guidance for coverage exploration, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Adapting ViNT to different goals using a new tunable goal token. Full model fine-tuning: While ViNT demonstrates strong zero-shot generalization to new environments ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Left: ViNT can be fine-tuned end-to-end (Images) or adapted to downstream tasks (Positions and Routing), and outperforms training from scratch and other pre-training ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7: Satellite-guided physical search with ViNT. We visualize a 765m rollout of ViNT with a satellite image-based heuristic from start (orange) to goal (green). ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: ViNT accomplishes long-horizon navigation with a variety of objectives in indoor and outdoor environments; example trajectories between start (orange) and goal (green) visualized ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 6 (Figure/Table caption), p. 9 (Figure/Table caption) |
| Embodiment/environment | [22], we further augment this dataset by allowing the rule-based agent to correct its position and re-center to the lane after a perturbation. | hardware/simulator version and reset protocol | p. 20 (B.4 Fine-tuning ViNT), p. 21 (B.4 Fine-tuning ViNT) |
| Dataset/benchmark | We collect 181 training trajectories (roughly 4 hours) in CARLA's Town 01 environment, and a further 52 trajectories (1 hour) in the held-out Town 02 environment. | role, split, size and leakage | p. 20 (B.4 Fine-tuning ViNT), p. 21 (B.4 Fine-tuning ViNT), p. 20 (B.4 Fine-tuning ViNT), p. 18 (B.2 Subgoal Diffusion) |
| Metric | Figure 7: Satellite-guided physical search with ViNT. We visualize a 765m rollout of ViNT with a satellite image-based heuristic from start (orange) to goal (green). The future action samples ˆa obtained by ... | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 4 (Figure/Table caption), p. 11 (Figure/Table caption) |
| Baseline/ablation | Table 1: ViNT paired with our physical search algorithm consistently outperforms baselines for the task of undirected goal-reaching in indoor and outdoor environments (left). By effectively planning over diffusion subgoal proposals, ViN ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 25 (Figure/Table caption), p. 9 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 11 / 7 Discussion - extractive body cue:** Limitations and Future Work As with many large-scale models, ViNT carries a heavier computational burden at inference time, which can present a challenge for power-constrained ...
- **p. 11 / 7 Discussion - extractive body cue:** For example, it cannot control the altitude of a quadcopter or handle other changes in the action representation, nor accommodate new sensors such as LIDAR.
- **p. 18 / B.2 Subgoal Diffusion - extractive body cue:** To produce training pairs for the diffusion model, we first select ot uniformly at random from the training data and then select osi to fall ...
- **p. 18 / Figure/Table caption - extractive body cue:** Table 5: Comparing merits (✓) and demerits (✗) of different goal-conditioning architectures. While "Early Fusion" works the best for the core navigation task, it does ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 9: Samples from the diffusion model may be invalid subgoals, but ViNT is robust to such proposals. Implicit navigation affor- dances: Ideally, we would ...
- **p. 19 / B.2 Subgoal Diffusion - extractive body cue:** Head Dim 8 Channels (128, 128, 256, 512, 640) Diffusion Type continuous time Noise Schedule linear Hyperparameter Value Diffusion Training Dropout 0.1 Batch Size 128 ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 navigation 문제를 이해하기 위해 읽는다. 본문은 Although this paradigm has been successful in many domains, it is difficult to apply in robotics due to the sheer diversity of environments, platforms, and applications.를 문제로 두고, We propose a novel exploration algorithm for the visual navigation paradigm using a diffusion model to propose short-horizon goals, and demonstrate that it enables ViNT to navigate in novel environments.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 18 (B.2 Subgoal Diffusion), p. 18 (B.2 Subgoal Diffusion), p. 21 (B.4 Fine-tuning ViNT) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
