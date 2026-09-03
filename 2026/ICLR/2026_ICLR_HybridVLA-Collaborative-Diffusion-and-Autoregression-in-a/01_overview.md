# HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=H1KDMNOKQn.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/245878. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics, Diffusion
- Official paper: https://openreview.net/forum?id=H1KDMNOKQn
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/245878
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Unlike prior diffusion-based VLA methods (Black et al., 2024; Li et al., 2024a) that append an independent diffusion head after the LLM (Figure 1 (a)), we introduce a collaborative training recipe that ...를 문제로 두고, Our contributions are as follows: • We propose HybridVLA, which innovatively leverages a single LLM backbone for iterative action prediction through both autoregressive and diffusion generation within a unified token sequence, harnessin ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** A central objective of manipulation policy design is to enable robots to comprehend human instructions and predict generalized actions in unstructured environments.
- **p. 1 / ABSTRACT - extractive body cue:** Recent autoregressive vision-language-action (VLA) approaches discretize actions into bins to exploit the pretrained reasoning and generation paradigms of visionlanguage models (VLMs).
- **p. 1 / ABSTRACT - extractive body cue:** While these models achieve efficient and scalable training, the discretization undermines the continuity required for precise control.
- **p. 1 / ABSTRACT - extractive body cue:** In contrast, diffusion-based VLA methods incorporate an additional diffusion head to predict continuous actions, but they rely solely on feature representations extracted from the VLM, ...
- **p. 1 / ABSTRACT - extractive body cue:** To integrate the complementary strengths of autoregressive and diffusion generation, we introduce HybridVLA, which innovatively leverages a shared LLM backbone to perform iterative action prediction ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Unlike prior diffusion-based VLA methods (Black et al., 2024; Li et al., 2024a) that append an independent diffusion head after the LLM (Figure 1 (a)), ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Recent diffusion-based VLA methods (Black et al., 2024; Li et al., 2024a; Wen et al., 2024a; Bjorck et al., 2025) incorporate a diffusion head after ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contributions are as follows: • We propose HybridVLA, which innovatively leverages a single LLM backbone for iterative action prediction through both autoregressive and diffusion ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Unlike prior diffusion-based VLA methods (Black et al., 2024; Li et al., 2024a) that append an independent diffusion head after the LLM (Figure 1 (a)), ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Developing intelligent robots capable of performing manipulation tasks demands robust policies (Driess et al., 2023; Huang et al., 2023).
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Given these advantages and limitations, a question arises: "How can we elegantly construct a unified VLA model that integrates the strengths of both autoregressive and ...
- **p. 1 / ABSTRACT - extractive body cue:** In contrast, diffusion-based VLA methods incorporate an additional diffusion head to predict continuous actions, but they rely solely on feature representations extracted from the VLM, ...
- **p. 1 / ABSTRACT - extractive body cue:** A central objective of manipulation policy design is to enable robots to comprehend human instructions and predict generalized actions in unstructured environments.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | A central objective of manipulation policy design is to enable robots to comprehend human instructions and predict generalized actions in unstructured environments. | image/video, language instruction, proprioception과 history | p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION) |
| State/latent | central, objective, manipulation, policy, design, enable, robots, comprehend, human, instructions, predict, generalized | language-grounded task state와 action-policy context | p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Output/action | Moreover, we demonstrate that the autoregressive discrete action outputs of HybridVLA can be replaced with language-based task planning without compromising the stability of diffusion-based action prediction. | continuous action, pose 또는 action chunk | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective/outcome | Our contributions are as follows: • We propose HybridVLA, which innovatively leverages a single LLM backbone for iterative action prediction through both autoregressive and diffusion generation within a unified token sequence, harnessin ... | instruction following, task success, generalization과 latency | p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 1 (ABSTRACT) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contributions are as follows: • We propose HybridVLA, which innovatively leverages a single LLM backbone for iterative action prediction through both autoregressive and diffusion ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Unlike prior diffusion-based VLA methods (Black et al., 2024; Li et al., 2024a) that append an independent diffusion head after the LLM (Figure 1 (a)), ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Developing intelligent robots capable of performing manipulation tasks demands robust policies (Driess et al., 2023; Huang et al., 2023).
- **p. 7 / 12.3 Hz - extractive body cue:** As shown in Table 2, HybridVLA (7B) achieves an average success rate of 78% across 10 distinct tasks, outperforming the previous SOTA autoregressive-based VLA (OpenVLA) ...
- **p. 7 / 12.3 Hz - extractive body cue:** Remarkably, compared to CogACT and π0, HybridVLA-dif (7B) also achieves performance improvements of 12% and 11%, respectively.
- **p. 9 / 12.3 Hz - extractive body cue:** For Pick and place and Unplug charger, HybridVLA achieves success rates of 90% and 95%, respectively, demonstrating accurate object position prediction.
- **p. 8 / 12.3 Hz - extractive body cue:** For collaborative action ensemble, as evidenced by the results of Ex2, Ex4, and Ex5 in Table 3, the performance of HybridVLA (Ex5) is further improved, ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: (a) Unlike recent diffusion-based VLA methods that attach a separate diffusion head after VLMs, (b) HybridVLA innovatively integrates diffusion and autoregressive action prediction ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (12.3 Hz), p. 7 (12.3 Hz) |
| Embodiment/environment | CAE indicates the collaborative action ensemble method, whereas LSP refers to large-scale pretraining on robotic datasets. | hardware/simulator version and reset protocol | p. 8 (12.3 Hz), p. 8 (12.3 Hz) |
| Dataset/benchmark | All methods maintain satisfactory performance, demonstrating that large-scale pretraining on robotic datasets enhances their generalization across diverse data distributions. | role, split, size and leakage | p. 8 (12.3 Hz), p. 8 (12.3 Hz), p. 10 (12.3 Hz), p. 6 (4 EXPERIMENT) |
| Metric | We train all methods in the multi-task setting (Shridhar et al., 2022) and report the success rates (S.R.) and variances (Var.). | definition, denominator, direction and uncertainty | p. 7 (4 EXPERIMENT), p. 7 (12.3 Hz), p. 8 (12.3 Hz) |
| Baseline/ablation | The results show that our method reduces the accuracy drop by approximately 5-16% compared to the baselines under generalization scenarios. | fair input/data/compute/action matching | p. 10 (12.3 Hz), p. 7 (12.3 Hz), p. 9 (12.3 Hz) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 12.3 Hz - extractive body cue:** Additional qualitative results and failure case analyses are provided in Appendix D and Appendix E, respectively, and execution videos are available in the supplementary materials.
- **p. 26 / Figure/Table caption - extractive body cue:** Figure 9: Single-arm Execution Visualization. We visualize key frames of the agent's execution process from the front perspective. E FAILURE CASE ANALYSIS. Through extensive real-world ...
- **p. 8 / 12.3 Hz - extractive body cue:** Due to space limitations, Appendix C.2 provides additional ablation studies on: (1) confidence thresholds in the collaborative action ensemble, (2) the influence of the diffusion-based ...
- **p. 10 / 12.3 Hz - extractive body cue:** One limitation of HybridVLA is that its inference speed is constrained by the slower autoregressive generation, similar to prior autoregressive VLA methods (Kim et al., ...
- **p. 10 / 12.3 Hz - extractive body cue:** 5 CONCLUSION AND LIMITATION In this paper, we introduce HybridVLA, a unified Vision-Language-Action (VLA) framework that equips a single LLM with both diffusion-based and autoregressive ...
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 4: Real-World Assets and Experimental Settings. We provide visualizations of the assets used and the settings for single-arm FR3 robot tasks and dual-arm AgileX ...
- **p. 23 / Figure/Table caption - extractive body cue:** Figure 5: The impact of denoising steps, where the x-axis and y-axis represent the denoising steps and manipulation success rate. that a ratio between AR ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Unlike prior diffusion-based VLA methods (Black et al., 2024; Li et al., 2024a) that append an independent diffusion head after the LLM (Figure 1 (a)), we introduce a collaborative training recipe that ...를 문제로 두고, Our contributions are as follows: • We propose HybridVLA, which innovatively leverages a single LLM backbone for iterative action prediction through both autoregressive and diffusion generation within a unified token sequence, harnessin ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
