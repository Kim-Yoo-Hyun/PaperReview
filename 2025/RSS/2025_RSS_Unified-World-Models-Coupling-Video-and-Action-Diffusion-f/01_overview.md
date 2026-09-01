# Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://roboticsconference.org/2025/program/papers/15/.
> PDF retrieval source: https://arxiv.org/pdf/2504.02792. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, VLA, world model, video diffusion, action diffusion, robot data
- Official paper: https://roboticsconference.org/2025/program/papers/15/
- Full-text retrieval: https://arxiv.org/pdf/2504.02792
- Code/Project: https://weirdlabuw.github.io/uwm/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 However, it is not yet clear how the ability of these world models to capture temporal dynamics can be brought to bear on improving the robustness and generalization of robotic controllers synthesized ...를 문제로 두고, We show that this learning framework leads to improved policies compared to standard imitation learning since, (1) the unified architecture enables feature sharing between actions and pixels, resulting in additional supervision from ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Imitation learning has emerged as a promising approach towards building generalist robots.
- **p. 1 / Abstract - extractive body cue:** However, scaling imitation learning for large robot foundation models remains challenging due to its reliance on high-quality expert demonstrations.
- **p. 1 / Abstract - extractive body cue:** Meanwhile, large amounts of video data depicting a wide range of environments and diverse behaviors are readily available.
- **p. 1 / Abstract - extractive body cue:** This data provides a rich source of information about realworld dynamics and agent-environment interactions.
- **p. 1 / Abstract - extractive body cue:** Leveraging this data directly for imitation learning, however, has proven difficult due to the lack of action annotation.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, it is not yet clear how the ability of these world models to capture temporal dynamics can be brought to bear on improving the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Through this investigation of UWM, we take a step towards bridging the gap between policies and world models for robot learning.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** We show that this learning framework leads to improved policies compared to standard imitation learning since, (1) the unified architecture enables feature sharing between actions ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Concretely, a UWM consists of a coupled score model that predicts action scores and future image scores, conditioned on the current image and separate diffusion ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose a new diffusion-based learning framework that unifies imitation learning and world modeling, incorporating knowledge of temporal dynamics gleaned from large ...
- **p. 3 / III. METHOD - extractive body cue:** In this section, we introduce Unified World Models as a way to incorporate temporal dynamics into diffusion-based action prediction models, proving a bridge between the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** During inference, UWM enables flexible sampling from various distributions by manipulating the diffusion timesteps independently.
- **p. 4 / III. METHOD - extractive body cue:** Encoder Decoder Encoder Unpatchify Patchify Encoder Decoder Encoder Patchify Unified World Model Training UWM UWM Marginal Inference (Policy) 𝑡! 𝑡"# Conditional Inference (Inverse Dynamics) Encoder ...
- **p. 3 / III. METHOD - extractive body cue:** Unified World Models via Coupled Video-Action Diffusion The core idea of a UWM is to develop a single diffusion model that can be trained on ...
- **p. 4 / III. METHOD - extractive body cue:** To train a joint noise prediction diffusion model (ϵθ a, ϵθ o′) = sθ(o′ to′, ata, o, ta, to′), we independently sample action timestep ta ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In this context, several different models may be desired: (1) a policy p(a/o) (often referred to as π(a/o)) that samples optimal actions to execute at a particular observation, (2) a dynamics model ... | observation, uncertainty/risk estimate와 task command | p. 3 (III. METHOD), p. 2 (I. INTRODUCTION) |
| State/latent | context, several, different, models, desired, policy, often, referred, samples, optimal, actions, execute | safe set, recovery state 또는 constraint margin | p. 3 (III. METHOD), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD) |
| Output/action | In particular, a UWM can generate samples from (1) forward dynamics, (2) inverse dynamics (3) marginal action distribution (policy), (4) marginal image distribution (video generative model). | shielded, recovery 또는 safe action | p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Objective/outcome | To train a joint noise prediction diffusion model (ϵθ a, ϵθ o′) = sθ(o′ to′, ata, o, ta, to′), we independently sample action timestep ta and next observation timestep to′, draw noisy ... | task return과 violation/failure probability | p. 4 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** We show that this learning framework leads to improved policies compared to standard imitation learning since, (1) the unified architecture enables feature sharing between actions ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Concretely, a UWM consists of a coupled score model that predicts action scores and future image scores, conditioned on the current image and separate diffusion ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose a new diffusion-based learning framework that unifies imitation learning and world modeling, incorporating knowledge of temporal dynamics gleaned from large ...
- **p. 3 / III. METHOD - extractive body cue:** In this section, we introduce Unified World Models as a way to incorporate temporal dynamics into diffusion-based action prediction models, proving a bridge between the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** During inference, UWM enables flexible sampling from various distributions by manipulating the diffusion timesteps independently.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6. Average success rates across all real robot tasks and in-distribution and out-of-distribution settings. UWM exhibits strong performance and can further improve by co-training ...
- **p. 9 / IV. EXPERIMENTS - extractive body cue:** We find that given the same time limit as the trajectory length, the inverse dynamics model achieves a higher success rate than the policy.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** PAD achieves the lowest success across the board.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 9 (IV. EXPERIMENTS) |
| Embodiment/environment | The LIBERO-100 benchmark consists of 90 training environments across multiple scenes and 10 evaluation environments, each with accompanying expert demonstrations. | hardware/simulator version and reset protocol | p. 8 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Dataset/benchmark | The pretraining dataset (LIBERO-90) consists of 90 tasks sampled across the kitchen, living room, and study scenes. | role, split, size and leakage | p. 8 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Metric | Average success rates across all real robot tasks and in-distribution and out-of-distribution settings. | definition, denominator, direction and uncertainty | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS) |
| Baseline/ablation | Despite a slight performance drop compared to the ID setting, we find UWM to outperform the baselines, showcasing strong robustness under distribution shifts. | fair input/data/compute/action matching | p. 8 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 10 / VII. LIMITATIONS - extractive body cue:** Firstly, the proposed model does not yet learn from large scale human videos, bridging the embodiment gap.
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1. Unified World Models integrates action and video diffusion in a unified transformer architecture controlled by modality-specific diffusion timesteps. The model can be trained ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** The third row highlights the out-of-distribution (OOD) configurations designed to evaluate the robustness of each method.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Unlike other baselines, GR1 does not model a distribution over data using a diffusion process.
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 10. Training models from scratch vs finetuning pretrained models. UWM scales more effectively with pretraining than DP. promising, they are still heavily reliant on ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** This set of experiments tests the models' robustness to distribution shifts.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Average success rates across all real robot tasks and in-distribution and out-of-distribution settings.

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 However, it is not yet clear how the ability of these world models to capture temporal dynamics can be brought to bear on improving the robustness and generalization of robotic controllers synthesized ...를 문제로 두고, We show that this learning framework leads to improved policies compared to standard imitation learning since, (1) the unified architecture enables feature sharing between actions and pixels, resulting in additional supervision from ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. METHOD), p. 3 (III. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
