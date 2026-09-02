# Learning Robotic Manipulation Policies from Point Clouds with Conditional Flow Matching

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2409.07343.
> PDF retrieval source: https://arxiv.org/pdf/2409.07343. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, point cloud, conditional flow matching, Imitation Learning
- Official paper: https://arxiv.org/abs/2409.07343
- Full-text retrieval: https://arxiv.org/pdf/2409.07343
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 il 문제를 이해하기 위해 읽는다. 본문은 To overcome these limitations, Conditional Flow Matching (CFM) has been proposed as an efficient generalization of diffusion models [12, 13, 11].를 문제로 두고, Inspired by recent flow-based generative models, we propose PointFlowMatch, a novel imitation learning algorithm for robotic manipulation.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Learning from expert demonstrations is a promising approach for training robotic manipulation policies from limited data.
- **p. 1 / Abstract - extractive body cue:** However, imitation learning algorithms require a number of design choices ranging from the input modality, training objective, and 6-DoF end-effector pose representation.
- **p. 1 / Abstract - extractive body cue:** Diffusion-based methods have gained popularity as they enable predicting long-horizon trajectories and handle multimodal action distributions.
- **p. 1 / Abstract - extractive body cue:** Recently, Conditional Flow Matching (CFM) (or Rectified Flow) has been proposed as a more flexible generalization of diffusion models.
- **p. 1 / Abstract - extractive body cue:** In this paper, we investigate the application of CFM in the context of robotic policy learning and specifically study the interplay with the other design ...
- **p. 2 / 1 Introduction - extractive body cue:** To overcome these limitations, Conditional Flow Matching (CFM) has been proposed as an efficient generalization of diffusion models [12, 13, 11].
- **p. 1 / 1 Introduction - extractive body cue:** Recently, generative models have been demonstrated to be effective at tackling some of these challenges.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Inspired by recent flow-based generative models, we propose PointFlowMatch, a novel imitation learning algorithm for robotic manipulation.
- **p. 1 / 1 Introduction - extractive body cue:** In recent years, imitation learning has gained popularity in the robot learning community, as leveraging the prior knowledge of the expert demonstrator allows training complex ...
- **p. 2 / 1 Introduction - extractive body cue:** As CFM is able to model arbitrary probability paths, it also allows formulating the regression on the R3 × SO(3) manifold.
- **p. 1 / Abstract - extractive body cue:** We show that CFM gives the best performance when combined with point cloud input observations.
- **p. 1 / Abstract - extractive body cue:** However, imitation learning algorithms require a number of design choices ranging from the input modality, training objective, and 6-DoF end-effector pose representation.
- **p. 1 / 1 Introduction - extractive body cue:** The primary approach to learning an IL policy is Behavior Cloning (BC) [4, 5], where a deterministic mapping from state to actions is learned in ...
- **p. 2 / 1 Introduction - extractive body cue:** We evaluate the performance of our proposed method on the popular RLBench benchmark [14] and compare it against strong recent baselines with both image and ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We evaluate the performance of our proposed method on the popular RLBench benchmark [14] and compare it against strong recent baselines with both image and point cloud observations: Diffusion Policy [6], 3D ... | observation history와 expert trajectory/action | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| State/latent | evaluate, performance, popular, RLBench, benchmark, compare, against, strong, recent, baselines, image, point | behavior policy와 temporal action context | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (Abstract) |
| Output/action | The primary approach to learning an IL policy is Behavior Cloning (BC) [4, 5], where a deterministic mapping from state to actions is learned in a supervised manner from the available data. | predicted action 또는 action chunk | p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction) |
| Objective/outcome | However, imitation learning algorithms require a number of design choices ranging from the input modality, training objective, and 6-DoF end-effector pose representation. | imitation error, task success, robustness와 compounding error | p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (Abstract) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** Inspired by recent flow-based generative models, we propose PointFlowMatch, a novel imitation learning algorithm for robotic manipulation.
- **p. 1 / 1 Introduction - extractive body cue:** In recent years, imitation learning has gained popularity in the robot learning community, as leveraging the prior knowledge of the expert demonstrator allows training complex ...
- **p. 2 / 1 Introduction - extractive body cue:** As CFM is able to model arbitrary probability paths, it also allows formulating the regression on the R3 × SO(3) manifold.
- **p. 1 / Abstract - extractive body cue:** We show that CFM gives the best performance when combined with point cloud input observations.
- **p. 1 / Abstract - extractive body cue:** We perform extensive experiments on RLBench which demonstrate that our proposed PointFlowMatch approach achieves a state-of-the-art average success rate of 67.8% over eight tasks, double ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Performance comparison of PointFlowMatch with different baseline methods on the RLBench set of tasks. We report the success rate (SR) (↑) as well ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Ablation of observation type (images vs point clouds), vector field formulation (R6 vs SO(3)), and training objective (DDIM vs CFM) for our method, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Comparison of CFM and DDIM for varying values of the number of inference steps k. We compare the inference time (↓) measured in ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 1 (Abstract), p. 6 (Figure/Table caption) |
| Embodiment/environment | Learning from expert demonstrations is a promising approach for training robotic manipulation policies from limited data. | hardware/simulator version and reset protocol | p. 1 (Abstract), p. 1 (1 Introduction) |
| Dataset/benchmark | Inspired by recent flow-based generative models, we propose PointFlowMatch, a novel imitation learning algorithm for robotic manipulation. | role, split, size and leakage | p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Metric | Table 1: Performance comparison of PointFlowMatch with different baseline methods on the RLBench set of tasks. We report the success rate (SR) (↑) as well as the delta to our method. On ... | definition, denominator, direction and uncertainty | p. 6 (Figure/Table caption), p. 1 (Abstract), p. 7 (Figure/Table caption) |
| Baseline/ablation | Table 1: Performance comparison of PointFlowMatch with different baseline methods on the RLBench set of tasks. We report the success rate (SR) (↑) as well as the delta to our method. On ... | fair input/data/compute/action matching | p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (Abstract) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5 Conclusion - extractive body cue:** In addition to this, as usual in the fixed-data imitation learning setting, CFM cannot extrapolate out of distribution and thus, only learns motion correction behavior ...
- **p. 8 / 5 Conclusion - extractive body cue:** Limitations: There are a few limitations to our proposed method.
- **p. 2 / 1 Introduction - extractive body cue:** To overcome these limitations, Conditional Flow Matching (CFM) has been proposed as an efficient generalization of diffusion models [12, 13, 11].
- **p. 1 / 1 Introduction - extractive body cue:** The forward diffusion process starts with expert robot trajectories and gradually adds Gaussian noise until the signal approximates pure noise.
- **p. 1 / 1 Introduction - extractive body cue:** This is a stochastic process that results in Gaussian conditional probability paths mapping Gaussian noise to data, with specific choices of mean and standard deviation ...
- **p. 2 / 1 Introduction - extractive body cue:** CFM is a simulation-free approach, i.e. it starts directly from noise without requiring a forward diffusion process.

## Why Read It

Manipulation, contact, tactile, and dexterity의 il 문제를 이해하기 위해 읽는다. 본문은 To overcome these limitations, Conditional Flow Matching (CFM) has been proposed as an efficient generalization of diffusion models [12, 13, 11].를 문제로 두고, Inspired by recent flow-based generative models, we propose PointFlowMatch, a novel imitation learning algorithm for robotic manipulation.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
