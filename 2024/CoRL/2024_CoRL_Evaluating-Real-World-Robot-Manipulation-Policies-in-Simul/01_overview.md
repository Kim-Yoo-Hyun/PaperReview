# Evaluating Real-World Robot Manipulation Policies in Simulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=LZh48DTg71.
> PDF retrieval source: https://arxiv.org/pdf/2405.05941.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Benchmark, simulation, real-to-sim, policy evaluation, generalist policy
- Official paper: https://openreview.net/forum?id=LZh48DTg71
- Full-text retrieval: https://arxiv.org/pdf/2405.05941.pdf
- Code/Project: https://simpler-env.github.io/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-02 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 benchmark 문제를 이해하기 위해 읽는다. 본문은 However, performing simulated evaluations for robotic manipulation poses additional challenges due to the diverse interactions between agent and environment.를 문제로 두고, In summary, our contributions are as follows: • We introduce SIMPLER, a suite of simulated evaluation environments for commonly-used real robot manipulation setups. • We address the challenges inherent in simulated manipulation ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The field of robotics has made significant advances towards generalist robot manipulation policies.
- **p. 1 / Abstract - extractive body cue:** However, realworld evaluation of such policies is not scalable and faces reproducibility challenges, which are likely to worsen as policies broaden the spectrum of tasks ...
- **p. 1 / Abstract - extractive body cue:** In this work, we demonstrate that simulation-based evaluation can be a scalable, reproducible, and reliable proxy for real-world evaluation.
- **p. 1 / Abstract - extractive body cue:** We identify control and visual disparities between real and simulated environments as key challenges for reliable simulated evaluation and propose approaches for mitigating these gaps ...
- **p. 1 / Abstract - extractive body cue:** We then employ these approaches to create SIMPLER, a collection of simulated environments for manipulation policy evaluation on common real robot setups.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, performing simulated evaluations for robotic manipulation poses additional challenges due to the diverse interactions between agent and environment.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This underlines a growing challenge in robot manipulation research: as we scale the capabilities of robot policies, how do we correspondingly scale our ability to ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, our contributions are as follows: • We introduce SIMPLER, a suite of simulated evaluation environments for commonly-used real robot manipulation setups. • We ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose simulated evaluation as a possible answer, in which manipulation policies trained on real data are evaluated in purpose-built simulated environments ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** 2: We introduce SIMPLER, a suite of open-source simulated evaluation environments for common real robot manipulation setups, namely the Google Robot evaluations from the RT-series ...
- **p. 1 / Abstract - extractive body cue:** We then employ these approaches to create SIMPLER, a collection of simulated environments for manipulation policy evaluation on common real robot setups.
- **p. 2 / I. INTRODUCTION - extractive body cue:** As such, SIMPLER is a first step towards using simulated evaluation as a tool for reliable, scalable, and reproducible manipulation policy evaluation.
- **p. 1 / I. INTRODUCTION - extractive body cue:** These advances are underpinned by large-scale datasets [11, 66] and expressive models [1, 6, 29].

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Simulated Manipulation Policy Evaluation for Real Robot Setups SIMPLER Pick Coke Can Move Near Open/Close Drawer Put Object in Drawer Google Robot Put Carrot on Plate Stack Cubes Put Eggplant in Basket ... | standardized observation, action, task state와 evaluation split | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| State/latent | Simulated, Manipulation, Policy, Evaluation, Real, Robot, Setups, SIMPLER, Pick, Coke, Move, Near | benchmark state/goal와 method decision | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Abstract) |
| Output/action | We then propose and evaluate approaches for mitigating these differences based on offline system identification, "green-screening" simulation observations using realworld backgrounds, and object texture baking from real-world images. | policy/controller trajectory 또는 measured result | p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 1 (Abstract) |
| Objective/outcome | Remarkable progress has been made in recent years towards building generalist real-world robot manipulation policies [6, 50], i.e., policies that can perform a wide range of tasks across many environments and even ... | success metric, robustness, generalization과 reproducibility | p. 1 (I. INTRODUCTION) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, our contributions are as follows: • We introduce SIMPLER, a suite of simulated evaluation environments for commonly-used real robot manipulation setups. • We ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose simulated evaluation as a possible answer, in which manipulation policies trained on real data are evaluated in purpose-built simulated environments ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** 2: We introduce SIMPLER, a suite of open-source simulated evaluation environments for common real robot manipulation setups, namely the Google Robot evaluations from the RT-series ...
- **p. 10 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** Thus, the approaches we introduced in Section IV-B for narrowing the visual gap between simulated and real scene can significantly improve real-andsim evaluation performance correlation, ...
- **p. 7 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** For Octo simulated evaluations, since the model involves a non-deterministic diffusion head, we average its success rates across three different random seeds to produce a ...
- **p. 7 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** We observe a strong correlation between the relative performances in simulation and in the real world across most policy checkpoints 0.0 0.2 0.4 0.6 0.8 ...
- **p. 8 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** For simulated results and realworld results, we report the difference in success rate with and without each distribution shift: ∆Success(shift) = 1 2 2 X ...
- **p. 10 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** To investigate whether our results are sensitive to the underlying physics simulator, we reproduce the Google Robot evaluation in Isaac Simulator Ablation SAPIEN MMRV = ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 10 (2) Can simulated evaluations not only capture the perfor), p. 7 (2) Can simulated evaluations not only capture the perfor) |
| Embodiment/environment | Models that obtain low real-world performance, such as RT1 (Begin) on Google Robot tasks and RT-1-X on BridgeData V2 tasks, similarly have low performance in SIMPLER evaluations in simulation. | hardware/simulator version and reset protocol | p. 8 (2) Can simulated evaluations not only capture the perfor), p. 9 (2) Can simulated evaluations not only capture the perfor) |
| Dataset/benchmark | In this section, we empirically test the performance correlation between real-world robot evaluations and simulated evaluations in SIMPLER environments for a representative set of open-source generalist robot manipulation policies. | role, split, size and leakage | p. 8 (2) Can simulated evaluations not only capture the perfor), p. 9 (2) Can simulated evaluations not only capture the perfor), p. 7 (VI. EXPERIMENTAL RESULTS), p. 9 (2) Can simulated evaluations not only capture the perfor) |
| Metric | For Octo simulated evaluations, since the model involves a non-deterministic diffusion head, we average its success rates across three different random seeds to produce a lowervariance estimate of the policy's simulation performance. | definition, denominator, direction and uncertainty | p. 7 (2) Can simulated evaluations not only capture the perfor), p. 7 (2) Can simulated evaluations not only capture the perfor), p. 9 (2) Can simulated evaluations not only capture the perfor) |
| Baseline/ablation | Furthermore, "Visual Matching" (VisMatch) outperforms "Variant Aggregation" (VarAgg). | fair input/data/compute/action matching | p. 8 (2) Can simulated evaluations not only capture the perfor), p. 10 (2) Can simulated evaluations not only capture the perfor), p. 8 (2) Can simulated evaluations not only capture the perfor) |

## Explicit Limitations and Failure Boundary

- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Illustration of Mean Maximum Rank Violation (MMRV, range [0, 1], lower is better) and Pearson correlation coefficient (Pearson r, range [-1, 1], higher ...
- **p. 10 / VII. CONCLUSION - extractive body cue:** Our current set of environments has several limitations.
- **p. 10 / VII. CONCLUSION - extractive body cue:** Additionally, we demonstrate that SIMPLER evaluations accurately capture finegrained characteristics of real-world policies beyond average performance, such as their robustness to various distribution shifts.
- **p. 8 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** We evaluate two RT-1 checkpoints with different robustness behaviors to distribution shifts.
- **p. 8 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** Beyond comparing average policy performances, it would be beneficial to let practitioners gauge more nuanced aspects of a policy's behavior, such as its robustness to ...
- **p. 9 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** See Table VIII for detailed results. robustness to various distribution shifts in the real world.
- **p. 9 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** On the other hand, RT-1-X, also trained on the same Open-X-Embodiment dataset [11], exhibits higher robustness to different simulated robot arm textures.

## Why Read It

RL, IL, offline learning, and robot data의 benchmark 문제를 이해하기 위해 읽는다. 본문은 However, performing simulated evaluations for robotic manipulation poses additional challenges due to the diverse interactions between agent and environment.를 문제로 두고, In summary, our contributions are as follows: • We introduce SIMPLER, a suite of simulated evaluation environments for commonly-used real robot manipulation setups. • We address the challenges inherent in simulated manipulation ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 2 (I. INTRODUCTION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
