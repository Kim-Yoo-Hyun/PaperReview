# Vision-Language-Action Instruction Tuning: From Understanding to Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (48 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=tsxwloasw5.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/248397. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://openreview.net/forum?id=tsxwloasw5
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/248397
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (48 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 To address these challenges and utilize VLMs more effectively, prior work has primarily adopted two strategies.를 문제로 두고, We propose a unified framework that enables simultaneous multimodal reasoning and language-steered latent action planning using a single VLM (Figure 2 (1) and (2)).를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** To operate effectively in the real world, robots should integrate multimodal reasoning with precise action generation.
- **p. 1 / ABSTRACT - extractive body cue:** However, existing vision-language-action (VLA) models often sacrifice one for the other, narrow their abilities to task-specific manipulation data, and suffer catastrophic forgetting of pre-trained vision-language ...
- **p. 1 / ABSTRACT - extractive body cue:** To bridge this gap, we introduce InstructVLA, an end-to-end VLA model that preserves the flexible reasoning of large vision-language models (VLMs) while delivering leading manipulation ...
- **p. 1 / ABSTRACT - extractive body cue:** InstructVLA introduces a novel training paradigm, Vision-Language-Action Instruction Tuning (VLA-IT), which employs multimodal training with mixture-ofexperts adaptation to jointly optimize embodied reasoning and action generation ...
- **p. 1 / ABSTRACT - extractive body cue:** On in-domain SimplerEnv tasks, InstructVLA achieves 33% improvement over SpatialVLA.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** To address these challenges and utilize VLMs more effectively, prior work has primarily adopted two strategies.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Current attempts to incorporate the reasoning capabilities of VLMs into action learning face three main obstacles: (1) task interference, catastrophic forgetting (French, 1999) of multimodal ...

## Core Idea

- **p. 4 / 3. Atomic-Instruction Manipulation - extractive body cue:** We propose a unified framework that enables simultaneous multimodal reasoning and language-steered latent action planning using a single VLM (Figure 2 (1) and (2)).
- **p. 2 / 3. Atomic-Instruction Manipulation - extractive body cue:** To validate the performance of InstructVLA, we introduce the SimplerEnv-Instruct benchmark, a manually designed evaluation suite featuring 80 zero-shot manipulation tasks.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The first aims to retain general multimodal capabilities while learning manipulation.
- **p. 1 / ABSTRACT - extractive body cue:** To bridge this gap, we introduce InstructVLA, an end-to-end VLA model that preserves the flexible reasoning of large vision-language models (VLMs) while delivering leading manipulation ...
- **p. 2 / 3. Atomic-Instruction Manipulation - extractive body cue:** Building on these observations, we propose InstructVLA, a generalist VLA model that extends pretrained VLMs for accurate action generation while preserving strong multimodal understanding.
- **p. 4 / 3. Atomic-Instruction Manipulation - extractive body cue:** It takes image features from DINOv2 (Oquab et al., 2023) vision encoder, latent actions, noisy action embeddings and optional information such as proprioception, and fuses ...
- **p. 4 / 3. Atomic-Instruction Manipulation - extractive body cue:** The model produces textual outputs to preserve the strong language understanding and multimodal inference capabilities of the pretrained VLM, while subsequently generating latent action representations ...
- **p. 5 / 3. Atomic-Instruction Manipulation - extractive body cue:** We therefore adopt a principled two-stage training paradigm: first, action pretraining to align with the VLM's latent action embeddings; second, vision-language-action instruction tuning to integrate ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our key observation is that once the action expert has been pretrained to follow latent actions generated by the VLM, further adapting the LLM backbone enables the model to handle manipulation tasks ... | image/video, language instruction, proprioception과 history | p. 5 (3. Atomic-Instruction Manipulation), p. 5 (3. Atomic-Instruction Manipulation) |
| State/latent | observation, once, action, expert, been, pretrained, follow, latent, actions, generated, VLM, further | language-grounded task state와 action-policy context | p. 5 (3. Atomic-Instruction Manipulation), p. 5 (3. Atomic-Instruction Manipulation), p. 1 (ABSTRACT) |
| Output/action | Scenario Caption Command Rewriting Context Creation Question Answering Utility Material Appearance Situated Noval Action Long horizon Original Dataset Embodied Scene Understanding Instruction Understanding and Planning Figure 3: Vision- ... | continuous action, pose 또는 action chunk | p. 5 (3. Atomic-Instruction Manipulation), p. 1 (ABSTRACT), p. 2 (3. Atomic-Instruction Manipulation) |
| Objective/outcome | Due to the stability of flow matching and the next token prediction, the final loss is the direct sum of both losses as L = LLM + LF M. | instruction following, task success, generalization과 latency | p. 5 (3. Atomic-Instruction Manipulation), p. 4 (3. Atomic-Instruction Manipulation), p. 4 (3. Atomic-Instruction Manipulation) |

## Main Claims and Actual Contribution

- **p. 4 / 3. Atomic-Instruction Manipulation - extractive body cue:** We propose a unified framework that enables simultaneous multimodal reasoning and language-steered latent action planning using a single VLM (Figure 2 (1) and (2)).
- **p. 2 / 3. Atomic-Instruction Manipulation - extractive body cue:** To validate the performance of InstructVLA, we introduce the SimplerEnv-Instruct benchmark, a manually designed evaluation suite featuring 80 zero-shot manipulation tasks.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The first aims to retain general multimodal capabilities while learning manipulation.
- **p. 1 / ABSTRACT - extractive body cue:** To bridge this gap, we introduce InstructVLA, an end-to-end VLA model that preserves the flexible reasoning of large vision-language models (VLMs) while delivering leading manipulation ...
- **p. 2 / 3. Atomic-Instruction Manipulation - extractive body cue:** Building on these observations, we propose InstructVLA, a generalist VLA model that extends pretrained VLMs for accurate action generation while preserving strong multimodal understanding.
- **p. 8 / 5 EXPERIMENT - extractive body cue:** Meanwhile, InstructVLA (generalist) not only maintains strong performance on SimplerEnv's atomic instructions but also achieves a 31.7% relative improvement on SimplerEnv-Instruct over the state-of-the-art baseline ...
- **p. 9 / 5 EXPERIMENT - extractive body cue:** As shown in Table 3, introducing "language motion" (textual descriptions of low-level actions) supervision enhances the VLM's ability to associate visual cues with manipulation primitives, ...
- **p. 30 / Figure/Table caption - extractive body cue:** Figure 20: Failure case 2 of InstructVLA. The model fails to accurately estimate depth due to the real-to-sim gap, specifically the absence of arm reflection ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (5 EXPERIMENT), p. 9 (5 EXPERIMENT) |
| Embodiment/environment | (b) SimplerEnv: This benchmark (Li et al., 2024d) provides real-to-sim evaluation on large-scale manipulation datasets, incorporating visual matching and variance aggregation to assess generalization. | hardware/simulator version and reset protocol | p. 7 (5 EXPERIMENT), p. 8 (5 EXPERIMENT) |
| Dataset/benchmark | The zero-shot tasks are set in a kitchen environment following the Bridge dataset. | role, split, size and leakage | p. 7 (5 EXPERIMENT), p. 8 (5 EXPERIMENT), p. 8 (5 EXPERIMENT), p. 9 (5 EXPERIMENT) |
| Metric | Table 10: LIBERO benchmark results. We present the success rate and standard error for each method across four task suites, which are averaged over three random seeds with 500 trials. "KI" denotes ... | definition, denominator, direction and uncertainty | p. 26 (Figure/Table caption), p. 44 (Figure/Table caption), p. 9 (5 EXPERIMENT) |
| Baseline/ablation | In Table 2, InstructVLA (expert) outperforms the expert baseline SpatialVLA by 33.3% on SimplerEnv. | fair input/data/compute/action matching | p. 8 (5 EXPERIMENT), p. 8 (5 EXPERIMENT), p. 7 (5 EXPERIMENT) |

## Explicit Limitations and Failure Boundary

- **p. 30 / Figure/Table caption - extractive body cue:** Figure 20: Failure case 2 of InstructVLA. The model fails to accurately estimate depth due to the real-to-sim gap, specifically the absence of arm reflection ...
- **p. 29 / Figure/Table caption - extractive body cue:** Figure 18: Reasoning cases in SimplerEnv-Instruct. Three cases of the VL fine-tuned OpenVLA and InstructVLA-Generalist. "SR" denotes success rate. We present three representative reasoning cases ...
- **p. 30 / Figure/Table caption - extractive body cue:** Figure 19: Failure case 1 of InstructVLA. The model receives only a third-person view image as visual input, making it difficult to estimate depth or ...
- **p. 8 / 5 EXPERIMENT - extractive body cue:** However, GPT-4o faces the same challenges in accurate instruction rewriting as noted in Section 4.1, and fails to outperform InstructVLA (Generalist).
- **p. 46 / Figure/Table caption - extractive body cue:** Figure 34: Light distraction. Stable visual features from DINO and SigLIP enable the model to operate robustly under extreme out-of-distribution lighting conditions. 46
- **p. 8 / 5 EXPERIMENT - extractive body cue:** However, we observe that finetuning OpenVLA on multimodal and manipulation datasets does not fully restore its original multimodal capabilities, although it does improve task performance.
- **p. 23 / Figure/Table caption - extractive body cue:** Figure 13: Case study on multimodal capabilities. OCR represents a unique multimodal skill of VLMs that is absent from typical manipulation datasets. We evaluate two ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 To address these challenges and utilize VLMs more effectively, prior work has primarily adopted two strategies.를 문제로 두고, We propose a unified framework that enables simultaneous multimodal reasoning and language-steered latent action planning using a single VLM (Figure 2 (1) and (2)).를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 4 (3. Atomic-Instruction Manipulation), p. 4 (3. Atomic-Instruction Manipulation), p. 2 (3. Atomic-Instruction Manipulation), p. 5 (3. Atomic-Instruction Manipulation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
