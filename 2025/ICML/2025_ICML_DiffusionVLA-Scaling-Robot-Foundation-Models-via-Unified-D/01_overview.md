# DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=VdwdU81Uzy.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/166841. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics, Diffusion
- Official paper: https://openreview.net/forum?id=VdwdU81Uzy
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/166841
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, simply combining these elements does not fully exploit the reasoning potential, as there is often an implicit gap between logical reasoning and actionable robot policies.를 문제로 두고, In this section, we introduce the overall framework of our method in Section 3.1 and explore the design choices that inform our model architecture in Section 3.2.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In this paper, we present DiffusionVLA, a novel framework that integrates autoregressive reason
- **p. 1 / Abstract - extractive body cue:** 1Midea Group, Shanghai, China 2East China Normal University, Shanghai, China 3Shanghai University, Shanghai, China.
- **p. 1 / Abstract - extractive body cue:** Central to our approach is autoregressive reasoning - a task decomposition and explanation process enabled by a pre-trained VLM - to guide diffusion-based action policies.
- **p. 1 / Abstract - extractive body cue:** To tightly couple reasoning with action generation, we introduce a reasoning injection module that directly embeds self-generated reasoning phrases into the 1
- **p. 2 / Abstract - extractive body cue:** Scaling Robot Foundation Models via Unified Diffusion and Autoregression policy learning process.
- **p. 2 / 1. Introduction - extractive body cue:** However, simply combining these elements does not fully exploit the reasoning potential, as there is often an implicit gap between logical reasoning and actionable robot ...
- **p. 2 / 1. Introduction - extractive body cue:** However, despite the advantages of diffusion models for policy learning, they lack the reasoning capabilities crucial for VLA models to solve complex tasks effectively, a ...

## Core Idea

- **p. 3 / 3. Methodology - extractive body cue:** In this section, we introduce the overall framework of our method in Section 3.1 and explore the design choices that inform our model architecture in ...
- **p. 2 / 1. Introduction - extractive body cue:** In this work, we propose a unified model, named DiffusionVLA (DiVLA in short), that integrates autoregression with a diffusion model.
- **p. 2 / 1. Introduction - extractive body cue:** To bridge this gap, we propose a reasoning injection module, which reuses reasoning outputs and embeds them directly into the policy head, thus enriching the ...
- **p. 5 / 3.2. Model Design Choices - extractive body cue:** We illustrate the training strategy and other techniques that we used to improve the efficiency and effectiveness of our method.
- **p. 5 / 3.1. Architecture - extractive body cue:** Unlike most autoregressive VLAs, which require a recursive setup - converting reasoning outputs into inputs for subsequent model runs - our method proposes a more ...
- **p. 5 / 3.2. Model Design Choices - extractive body cue:** Because larger models typically needs more data for training, we use OXE and Droid together for pre-training DiVLA-72B.
- **p. 3 / 3. Methodology - extractive body cue:** Developing such an integrated model presents substantial challenges, with key issues centered on: (i) designing an architecture that seamlessly and efficiently integrates both autoregressive and ...
- **p. 4 / 3.1. Architecture - extractive body cue:** If multiple embodiments are evolved, instead of making a copy of a separate action decoder (Octo Model Team et al., 2024), we simply initialized a ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | These data contain only robotic actions, paired partially with observations and language instructions. | image/video, language instruction, proprioception과 history | p. 5 (3.2. Model Design Choices), p. 5 (3.1. Architecture) |
| State/latent | data, contain, only, robotic, actions, paired, partially, observations, language, instructions, embedding, reasoning | language-grounded task state와 action-policy context | p. 5 (3.2. Model Design Choices), p. 5 (3.1. Architecture), p. 2 (1. Introduction) |
| Output/action | By embedding reasoning directly within the policy model, we avoid the computational and operational complexities of iterative input-output cycles, enabling faster and more seamless reasoning incorporation. | continuous action, pose 또는 action chunk | p. 5 (3.1. Architecture), p. 2 (1. Introduction), p. 3 (3. Methodology) |
| Objective/outcome | Given a batch of input sequences, the overall training loss is formulated as a combination of the diffusion loss and the next-token prediction (ntp) loss: L = Ldiff + αLntp, where α ... | instruction following, task success, generalization과 latency | p. 5 (3.2. Model Design Choices), p. 5 (3.2. Model Design Choices) |

## Main Claims and Actual Contribution

- **p. 3 / 3. Methodology - extractive body cue:** In this section, we introduce the overall framework of our method in Section 3.1 and explore the design choices that inform our model architecture in ...
- **p. 2 / 1. Introduction - extractive body cue:** In this work, we propose a unified model, named DiffusionVLA (DiVLA in short), that integrates autoregression with a diffusion model.
- **p. 2 / 1. Introduction - extractive body cue:** To bridge this gap, we propose a reasoning injection module, which reuses reasoning outputs and embeds them directly into the policy head, thus enriching the ...
- **p. 5 / 3.2. Model Design Choices - extractive body cue:** We illustrate the training strategy and other techniques that we used to improve the efficiency and effectiveness of our method.
- **p. 5 / 3.1. Architecture - extractive body cue:** Unlike most autoregressive VLAs, which require a recursive setup - converting reasoning outputs into inputs for subsequent model runs - our method proposes a more ...
- **p. 8 / 4.6. Adapt to Real-World Bimanual Robot - extractive body cue:** In contrast, the Diffusion Policy and OpenVLA achieve 45.8% and 0% success rates.
- **p. 8 / 4.6. Adapt to Real-World Bimanual Robot - extractive body cue:** For tasks involving both seen and unseen objects, DiVLA achieves up to a 70.8% success rate, a slight decrease in success rate compared to the ...
- **p. 6 / 4.2. Real-World Multi-Task Learning - extractive body cue:** Our evaluation of these scenarios reveals that while all methods experience a decline in performance due to these visual changes, our method consistently maintains the ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (Figure/Table caption), p. 8 (4.6. Adapt to Real-World Bimanual Robot) |
| Embodiment/environment | (c) Seen Tableware (d) Unseen Tableware (a) Bimanual Robot Setup (b) Setup for Table Bussing (e) Seen Trash (f) Unseen Trash Figure 9: (a) Environmental setup for the bimanual robot, (b) Table ... | hardware/simulator version and reset protocol | p. 8 (4.5. Zero-Shot Bin Picking of Unseen Objects), p. 7 (4.5. Zero-Shot Bin Picking of Unseen Objects) |
| Dataset/benchmark | It highlights the potential for applications in dynamic, unstructured environments where robots encounter unfamiliar objects and must perform tasks with minimal human intervention. | role, split, size and leakage | p. 8 (4.5. Zero-Shot Bin Picking of Unseen Objects), p. 7 (4.5. Zero-Shot Bin Picking of Unseen Objects), p. 8 (4.5. Zero-Shot Bin Picking of Unseen Objects), p. 6 (4.3. End-to-End Sorting on Real Robot) |
| Metric | Our evaluation of these scenarios reveals that while all methods experience a decline in performance due to these visual changes, our method consistently maintains the highest average success rate across five different ... | definition, denominator, direction and uncertainty | p. 6 (4.2. Real-World Multi-Task Learning), p. 7 (4.3. End-to-End Sorting on Real Robot), p. 7 (4.3. End-to-End Sorting on Real Robot) |
| Baseline/ablation | Our method outperforms the state-of-the-art robot foundation models by a large margin. | fair input/data/compute/action matching | p. 6 (4. Experiments), p. 5 (Figure/Table caption), p. 5 (4. Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.4. Behavior Analysis of Robot Foundation Model - extractive body cue:** Failure case analysis via self-generated reasoning.
- **p. 8 / 5. Conclusion - extractive body cue:** Additionally, we show that DiVLA has robust generalization capabilities, adapting effectively to new instructions, tasks, and environments.
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1: Experimental Results for Multi-Task Learning on Real Robot. We report the count of pre-trained trajectories. We also report the average success rate for ...
- **p. 5 / 4. Experiments - extractive body cue:** In Section 4.2, we compare DiVLA against other state-of-the-art models within a standard multi-task setting, assessing its performance in both in-distribution and out-of-distribution scenarios.
- **p. 6 / 4. Experiments - extractive body cue:** DiVLA is robust to visual changes in different scenarios.
- **p. 6 / 4.2. Real-World Multi-Task Learning - extractive body cue:** We further evaluate our method in a multi-task setting with visual changes to assess its robustness and adaptability in diverse, dynamic environments.
- **p. 7 / 4.3. End-to-End Sorting on Real Robot - extractive body cue:** DiVLA demonstrates robust performance with an average success rate of 66.2% across all experimental settings.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, simply combining these elements does not fully exploit the reasoning potential, as there is often an implicit gap between logical reasoning and actionable robot policies.를 문제로 두고, In this section, we introduce the overall framework of our method in Section 3.1 and explore the design choices that inform our model architecture in Section 3.2.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Methodology), p. 5 (3.2. Model Design Choices), p. 3 (3. Methodology), p. 4 (3.1. Architecture) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
