# Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=c3BVcHcSiR.
> PDF retrieval source: https://openreview.net/pdf/7c6c1101cef920f79b251ef422b6399d7e8f4ae1.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics, Diffusion
- Official paper: https://openreview.net/forum?id=c3BVcHcSiR
- Full-text retrieval: https://openreview.net/pdf/7c6c1101cef920f79b251ef422b6399d7e8f4ae1.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 OpenVLA (Kim et al., 2024), π0-FAST (Pertsch et al., 2025)); and (2) a separate action head that employs MLP or continuous diffusion to map VLM output latent tokens to executable actions (e.g., ...를 문제로 두고, In summary, our contributions are threefold: 1) We introduce the first discrete diffusion VLA, unifying action generation with vision-language modeling in one transformer, demonstrating superior retention of pretrained VL capabilities.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models adapt large vision-language backbones to map images and instructions into robot actions.
- **p. 1 / Abstract - extractive body cue:** However, prevailing VLAs either generate actions autoregressively in a fixed left-to-right order with poor performance or attach separate diffusion heads outside the backbone that fragments ...
- **p. 1 / Abstract - extractive body cue:** Instead, we present Discrete Diffusion VLA that discretizes action chunks and models them with discrete diffusion pattern retaining progressive refinement inside the unified transformer backbone.
- **p. 1 / Abstract - extractive body cue:** Our method achieves an adaptive decoding order that resolves high-confidence action elements before harder ones and employs secondary re-masking to revisit uncertain predictions, enabling robust ...
- **p. 1 / Abstract - extractive body cue:** This design preserves pretrained vision-language priors, supports parallel decoding, and improves the efficiency.
- **p. 1 / 1. Introduction - extractive body cue:** OpenVLA (Kim et al., 2024), π0-FAST (Pertsch et al., 2025)); and (2) a separate action head that employs MLP or continuous diffusion to map VLM ...
- **p. 1 / 1. Introduction - extractive body cue:** Current approaches fall into two paradigms: (1) an autoregressive (AR) approach, inspired by GPT-style transformers, that predicts discretized action tokens sequentially (e.g.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are threefold: 1) We introduce the first discrete diffusion VLA, unifying action generation with vision-language modeling in one transformer, demonstrating superior ...
- **p. 2 / 1. Introduction - extractive body cue:** 2) We develop an adaptive decoding strategy with secondary re-masking that enables confidence-based actiontoken decoding and robust error correction, improving both effectiveness and efficiency.
- **p. 1 / 1. Introduction - extractive body cue:** Drawing on recent advances in discrete diffusion and discrete flow-matching for language and multi-modal generation (Nie et al., 2025a; Shi et al., 2024b; Gat et ...
- **p. 5 / 3.5. Adaptive Decoding and Secondary Re-Masking - extractive body cue:** As illustrated above, the inference pipeline starts from a fully masked action chunk a1 = ML with mask ratio γ1=1, and then performs T refinement ...
- **p. 3 / 3.1. Overview - extractive body cue:** Given image observations (single- or multi-view) and a language instruction, the model extends a VLM backbone to generate actions via discrete diffusion.
- **p. 3 / 3.1. Overview - extractive body cue:** A unified transformer jointly attends to visual features, language embeddings, and partially unmasked action tokens, progressively demasking remaining masked action tokens according to a diffusion ...
- **p. 4 / 3.4. Algorithmic Pipeline - extractive body cue:** No additional loss terms, auxiliary objectives, or special training procedures are involved.
- **p. 4 / 3.3. Architecture of Discrete Diffusion VLA - extractive body cue:** All tokens pass through the unified transformer, with hidden states at action positions projected to a 256-way vocabulary via a shared classification head.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given image observations (single- or multi-view) and a language instruction, the model extends a VLM backbone to generate actions via discrete diffusion. | image/video, language instruction, proprioception과 history | p. 3 (3.1. Overview), p. 1 (1. Introduction) |
| State/latent | Given, image, observations, single-, multi-view, language, instruction, model, extends, VLM, backbone, generate | language-grounded task state와 action-policy context | p. 3 (3.1. Overview), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | Modern VLA frameworks typically adapt a large pretrained vision-language model (VLM) by adding an action-generation head that outputs motor commands (either continuous trajectories or discrete tokens). | continuous action, pose 또는 action chunk | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Objective/outcome | In implementation, we follow mask diffusion formulations and collapse the multi-step chain into a single masked-token prediction objective. | instruction following, task success, generalization과 latency | p. 4 (3.2. Formulation of Discrete Diffusion over Actions), p. 4 (3.4. Algorithmic Pipeline), p. 3 (3.1. Overview) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are threefold: 1) We introduce the first discrete diffusion VLA, unifying action generation with vision-language modeling in one transformer, demonstrating superior ...
- **p. 2 / 1. Introduction - extractive body cue:** 2) We develop an adaptive decoding strategy with secondary re-masking that enables confidence-based actiontoken decoding and robust error correction, improving both effectiveness and efficiency.
- **p. 1 / 1. Introduction - extractive body cue:** Drawing on recent advances in discrete diffusion and discrete flow-matching for language and multi-modal generation (Nie et al., 2025a; Shi et al., 2024b; Gat et ...
- **p. 6 / 4.3. Extended Evaluation Across Robot Platforms - extractive body cue:** 5 shows Discrete Diffusion VLA achieves SOTA performance with 54.2% overall, outperforming all continuous diffusion/flowmatching policies (π0: 40.1%, +14.1%; GR00T-N1: 49.5%, +4.7%) and discrete baselines ...
- **p. 7 / 4.4. Ablation Study - extractive body cue:** Discrete diffusion achieves the best average performance across all LIBERO suites, outperforming AR, FAST, parallel decoding, and continuous diffusion, confirming that the advantage is intrinsic ...
- **p. 7 / 4.4. Ablation Study - extractive body cue:** 8 shows that linear decay from 1.0 to 0.0 achieves 96.8%, outperforming hard argmax (96.2%) and fixed temperature (96.4%).
- **p. 6 / 4.1. Simulation Benchmarks and Baselines - extractive body cue:** Notably, while OpenVLAOFT (L1) achieves the highest in-distribution (ID) accuracy, Discrete Diffusion VLA attains the best absolute OOD performance with the smallest degradation under both ...
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Ranking tokens by instance-wise confidence improves over one-shot parallel, and our max confidence yields the best accuracy (96.8%).

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4.3. Extended Evaluation Across Robot Platforms), p. 7 (4.4. Ablation Study) |
| Embodiment/environment | We evaluate Discrete Diffusion VLA on three different robot settings: (i) Franka Panda arm on LIBERO (Liu et al., 2023) (four suites: Spatial, Object, Goal, Long; 10 tasks and 500 demos per ... | hardware/simulator version and reset protocol | p. 5 (4.1. Simulation Benchmarks and Baselines), p. 8 (4.6. Real-Robot Evaluation) |
| Dataset/benchmark | Each column is a LIBERO task suite; values are averaged over 500 rollouts per suite (10 tasks × 50 episodes). | role, split, size and leakage | p. 5 (4.1. Simulation Benchmarks and Baselines), p. 8 (4.6. Real-Robot Evaluation), p. 6 (4.1. Simulation Benchmarks and Baselines), p. 6 (4.1. Simulation Benchmarks and Baselines) |
| Metric | On LIBERO-Goal, success rates are 95.6%, 95.8%, 96.6%, and 96.8% respectively (Tab. | definition, denominator, direction and uncertainty | p. 7 (4.4. Ablation Study), p. 8 (4.4. Ablation Study), p. 6 (4.1. Simulation Benchmarks and Baselines) |
| Baseline/ablation | 5 shows Discrete Diffusion VLA achieves SOTA performance with 54.2% overall, outperforming all continuous diffusion/flowmatching policies (π0: 40.1%, +14.1%; GR00T-N1: 49.5%, +4.7%) and discrete baselines (π0-FAST: 48.3%, +5.9%). | fair input/data/compute/action matching | p. 6 (4.3. Extended Evaluation Across Robot Platforms), p. 5 (4.1. Simulation Benchmarks and Baselines), p. 6 (4.3. Extended Evaluation Across Robot Platforms) |

## Explicit Limitations and Failure Boundary

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of Discrete Diffusion VLA architecture. We extend the VLM backbone that encodes multi-view RGB images (SigLIP+DINOv2 ViTs) and linguistic instruction to decode ...
- **p. 5 / 4.1. Simulation Benchmarks and Baselines - extractive body cue:** Beyond standard in-distribution (ID) evaluation, we assess out-of-distribution (OOD) generalization under two perturbation axes following LIBERO-PRO (Zhou et al., 2025): Language Augmentation, which paraphrases task ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Out-of-distribution performance on LIBERO-Goal
- **p. 6 / 4.1. Simulation Benchmarks and Baselines - extractive body cue:** Vision degradation is similarly reduced at 20.4%, against 22.6%, 29.0%, and 23.2% respectively.
- **p. 8 / 4.7. Visualization of Adaptive Decoding Order - extractive body cue:** Among these, training frequency serves as the most accessible and informative proxy, as tokens appearing more frequently tend to be learned more robustly.
- **p. 8 / 4.5. Inference Efficiency - extractive body cue:** Discrete Diffusion VLA denoises the entire chunk in T steps, where each step is a single forward pass predicting posteriors for all currently masked tokens.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 OpenVLA (Kim et al., 2024), π0-FAST (Pertsch et al., 2025)); and (2) a separate action head that employs MLP or continuous diffusion to map VLM output latent tokens to executable actions (e.g., ...를 문제로 두고, In summary, our contributions are threefold: 1) We introduce the first discrete diffusion VLA, unifying action generation with vision-language modeling in one transformer, demonstrating superior retention of pretrained VL capabilities.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.5. Adaptive Decoding and Secondary Re-Masking), p. 3 (3.1. Overview) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
