# SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2506.01844.
> PDF retrieval source: https://arxiv.org/pdf/2506.01844. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / arXiv
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, Robotics, efficient deployment, action chunking, community data, real-world manipulation
- Official paper: https://arxiv.org/abs/2506.01844
- Full-text retrieval: https://arxiv.org/pdf/2506.01844
- Code/Project: https://github.com/huggingface/lerobot
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 To address this limitation, a growing body of work has begun exploring robotics foundation models in the form of vision-language-action (VLA) models (Team et al., 2024; O'Neill et al., 2024; Brohan et ...를 문제로 두고, We present SmolVLA, a compact and efficient vision-language agent optimized for training on consumer-grade GPUs and deployment on CPUs.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-language models (VLMs) pretrained on large-scale multimodal datasets encode rich visual and linguistic knowledge, making them a strong foundation for robotics.
- **p. 1 / Abstract - extractive body cue:** Rather than training robotic policies from scratch, recent approaches adapt VLMs into vision-language-action (VLA) models that enable natural language-driven perception and control.
- **p. 1 / Abstract - extractive body cue:** However, existing VLAs are typically massive-often with billions of parameters-leading to high training costs and limited real-world deployability.
- **p. 1 / Abstract - extractive body cue:** Moreover, they rely on academic and industrial datasets, overlooking the growing availability of community-collected data from affordable robotic platforms.
- **p. 1 / Abstract - extractive body cue:** In this work, we present SmolVLA, a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance.
- **p. 2 / 1 Introduction - extractive body cue:** To address this limitation, a growing body of work has begun exploring robotics foundation models in the form of vision-language-action (VLA) models (Team et al., ...
- **p. 2 / 1 Introduction - extractive body cue:** Early results suggest promising gains in generalization capabilities (Black et al., 2024; Brohan et al., 2023).

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** We present SmolVLA, a compact and efficient vision-language agent optimized for training on consumer-grade GPUs and deployment on CPUs.
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we introduce SmolVLA, an open-source initiative featuring a compact yet capable VLA model, released alongside reproducible and efficient training and inference recipes.
- **p. 1 / Abstract - extractive body cue:** SmolVLA consists of a compact pretrained vision-language model, discarding the last L -N layers (scissors icon).
- **p. 1 / Abstract - extractive body cue:** In this work, we present SmolVLA, a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance.
- **p. 2 / 1 Introduction - extractive body cue:** We introduce an optimized asynchronous inference stack that decouples action execution from observation processing and action prediction, reducing latency and enabling fast, resource-efficient inference.
- **p. 1 / Abstract - extractive body cue:** To further improve responsiveness, we introduce an asynchronous inference stack decoupling perception and action prediction from action execution, allowing higher control rates with chunked action ...
- **p. 1 / Abstract - extractive body cue:** Self-Attention Self-Attention Self-Attention Cross-Attention Cross-Attention Self-Attention Task: Grasp the object and put it in the bin State Noisy Actions [at ,at+1 … ,at+H] KV KV ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | These models take multimodal inputs-such as visual observations and natural language instructions-and predict the corresponding robotic actions. | image/video, language instruction, proprioception과 history | p. 2 (1 Introduction), p. 1 (Abstract) |
| State/latent | models, take, multimodal, inputs-such, visual, observations, natural, language, instructions-and, predict, corresponding, robotic | language-grounded task state와 action-policy context | p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract) |
| Output/action | The remaining layers embed three inputs: (i) language instruction, (ii) RGB image(s), and (iii) robot sensorimotor state. | continuous action, pose 또는 action chunk | p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction) |
| Objective/outcome | While encouraging efforts like OpenVLA (Kim et al., 2024) and RT-2-X (O'Neill et al., 2024) demonstrate the feasibility of open VLA systems, they remain large, resource-intensive, and dependent on costly robotic platforms, ... | instruction following, task success, generalization과 latency | p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** We present SmolVLA, a compact and efficient vision-language agent optimized for training on consumer-grade GPUs and deployment on CPUs.
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we introduce SmolVLA, an open-source initiative featuring a compact yet capable VLA model, released alongside reproducible and efficient training and inference recipes.
- **p. 1 / Abstract - extractive body cue:** SmolVLA consists of a compact pretrained vision-language model, discarding the last L -N layers (scissors icon).
- **p. 1 / Abstract - extractive body cue:** In this work, we present SmolVLA, a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance.
- **p. 12 / 4 Experiments - extractive body cue:** Asynchronous inference achieves similar success rates (left) but is significantly faster (middle) and complete more tasks (right) in fixed-time settings.
- **p. 12 / 4 Experiments - extractive body cue:** As shown in Figure 5a, both inference modes achieve comparable success rates across three real-world tasks.
- **p. 14 / 4 Experiments - extractive body cue:** Sampling new observations more frequently (e.g., every 1 or 10 steps) significantly improves performance.
- **p. 11 / 4 Experiments - extractive body cue:** The results show that, pretraining on community datasets leads to a substantial performance improvement (from 51.7 to 78.3).

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 12 (4 Experiments), p. 12 (4 Experiments) |
| Embodiment/environment | For real-world evaluation, we collected three datasets using the SO-100 robot arm (Knight et al.) and 1 with SO-101 arm (Knight et al.), each corresponding to a different manipulation task. | hardware/simulator version and reset protocol | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Dataset/benchmark | For fine-tuning on simulation benchmarks, we train for 100,000 steps with a batch size of 64, while for real-world tasks, we fine-tune for 200,000 steps. | role, split, size and leakage | p. 8 (4 Experiments), p. 8 (4 Experiments), p. 10 (4 Experiments), p. 9 (4 Experiments) |
| Metric | We use a dataset (Kim et al., 2024; Pertsch et al., 2025)1 containing 1,693 episodes covering all tasks, and evaluate with 10 trials per task, reporting average success rates based on binary ... | definition, denominator, direction and uncertainty | p. 8 (4 Experiments), p. 12 (4 Experiments), p. 8 (4 Experiments) |
| Baseline/ablation | SmolVLA outperforms other VLA-based approaches such as Octo (Team et al., 2024) and OpenVLA (Kim et al., 2024), as well as the diffusion policy baseline across both LIBERO and Meta-World. | fair input/data/compute/action matching | p. 10 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 14 / 5 Discussion - extractive body cue:** 5.1 Limitations We identify several limitations remaining in our contribution.
- **p. 12 / 4 Experiments - extractive body cue:** The robot exhibits greater robustness to shifts in object positions and external disturbances, and overall is capable to solve the same tasks a significantly larger ...
- **p. 11 / 4 Experiments - extractive body cue:** Success Rate (%) - Real World Policy In Distribution Out of Distribution Single-task Training ACT 70 40 SmolVLA (0.45B) 90 50 Table 4 ∣ Real-world ...
- **p. 11 / 4 Experiments - extractive body cue:** Similarly, on SO101 (see Table 4), SmolVLA surpasses ACT in both in-distribution and out-of-distribution (OOD) settings.
- **p. 14 / 4 Experiments - extractive body cue:** However, Table 12 shows that both very small and very large values of n degrade performance.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 To address this limitation, a growing body of work has begun exploring robotics foundation models in the form of vision-language-action (VLA) models (Team et al., 2024; O'Neill et al., 2024; Brohan et ...를 문제로 두고, We present SmolVLA, a compact and efficient vision-language agent optimized for training on consumer-grade GPUs and deployment on CPUs.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
