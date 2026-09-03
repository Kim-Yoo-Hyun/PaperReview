# π0: A Vision-Language-Action Flow Model for General Robot Control

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p010.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p010.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: CORE
- Tags: Robotics, VLA, Flow Matching, generalist policy, cross-embodiment, dexterous manipulation
- Official paper: https://www.roboticsproceedings.org/rss21/p010.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p010.pdf
- Code/Project: https://www.pi.website/research/pi0
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, developing such generalist robot policies - ie., robot foundation models - involves a number of major challenges.를 문제로 두고, ‘of more complex and dexterous behaviors, such as tying shoelaces [58] or cooking shrimp [17], we show that our framework can leam very long tasks, sometimes tens of, minutes in length, for ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robot learning holds tremendous promise to untock the full potential of flexible, general, and dexterous robot systems, as well as to address some of the ...
- **p. 1 / Abstract - extractive body cue:** However, bringing robot learning to the level of generality required for effective real-world systems faces major ‘obstacles in terms of data, gener m, and robustness.
- **p. 1 / Abstract - extractive body cue:** In this paper, we discuss how generalist robot policies (i., robot foundation models) can address these challenges, and how we ean ‘design effective generalist robot ...
- **p. 1 / Abstract - extractive body cue:** We propose a novel flow matching architecture
- **p. 1 / Abstract - extractive body cue:** Physical Intelligence, San Francisco, California, USA.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** However, developing such generalist robot policies - ie., robot foundation models - involves a number of major challenges.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Flexible and general-purpose models that can be tasked variety of robot behaviors have tremendous fications, but they may also offer solutions to some of the ...

## Core Idea

- **p. 4 / 1. INTRODUCTION - extractive body cue:** ‘of more complex and dexterous behaviors, such as tying shoelaces [58] or cooking shrimp [17], we show that our framework can leam very long tasks, ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** In this paper, we present a prototype model and learning framework, which we call zo, that illustrates how each of these three bottlenecks could be ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** The contributions of our work consist of a novel generalist robot policy architecture based on VLM pre-training and flow matching, and an empirical investigation of ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** This enables our model to control robots at frequencies of up to 50 Hz for dexterous tasks such as laundry folding (see Figure 1), To ...
- **p. 4 / 1. INTRODUCTION - extractive body cue:** Note that we use PaliGemma for convenience and because of its comparatively small size (which is useful for real-time control), but our framework is compatible ...
- **p. 5 / IV. THE x MODEL - extractive body cue:** Formally, we want to model the data distribution p(A,/o,), where Ar = [ar,r¢1,.rs 11-1] corresponds to an action chunk of future actions (we use H ...
- **p. 5 / IV. THE x MODEL - extractive body cue:** In practice, the network is trained by sampling random noise « ~ \'(0, 1), computing the "noisy actions" Aj = rAy + (1 -r)e, and ...
- **p. 4 / IV. THE x MODEL - extractive body cue:** Our architecture is inspired by Transfusion [59], which trains a single transformer using multiple objectives, with tokens! corresponding to continuous outputs supervised via a flow ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Formally, we want to model the data distribution p(A,/o,), where Ar = [ar,r¢1,.rs 11-1] corresponds to an action chunk of future actions (we use H ~ 50 for our tasks), and 0 ... | image/video, language instruction, proprioception과 history | p. 5 (IV. THE x MODEL), p. 4 (IV. THE x MODEL) |
| State/latent | Formally, want, model, data, distribution, where, corresponds, action, chunk, future, actions, tasks | language-grounded task state와 action-policy context | p. 5 (IV. THE x MODEL), p. 4 (IV. THE x MODEL), p. 3 (1. INTRODUCTION) |
| Output/action | We further augment this backbone with roboties-specific inputs and outputs - namely, proprioceptive state and robot actions. | continuous action, pose 또는 action chunk | p. 4 (IV. THE x MODEL), p. 3 (1. INTRODUCTION), p. 2 (1. INTRODUCTION) |
| Objective/outcome | Our architecture is inspired by Transfusion [59], which trains a single transformer using multiple objectives, with tokens! corresponding to continuous outputs supervised via a flow matching loss and tokens corresponding to discrete ... | instruction following, task success, generalization과 latency | p. 4 (IV. THE x MODEL), p. 5 (IV. THE x MODEL), p. 7 (A. Evaluating the base model) |

## Main Claims and Actual Contribution

- **p. 4 / 1. INTRODUCTION - extractive body cue:** ‘of more complex and dexterous behaviors, such as tying shoelaces [58] or cooking shrimp [17], we show that our framework can leam very long tasks, ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** In this paper, we present a prototype model and learning framework, which we call zo, that illustrates how each of these three bottlenecks could be ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** The contributions of our work consist of a novel generalist robot policy architecture based on VLM pre-training and flow matching, and an empirical investigation of ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** This enables our model to control robots at frequencies of up to 50 Hz for dexterous tasks such as laundry folding (see Figure 1), To ...
- **p. 4 / 1. INTRODUCTION - extractive body cue:** Note that we use PaliGemma for convenience and because of its comparatively small size (which is useful for real-time control), but our framework is compatible ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 9: Language evaluation. We compare "flat" versions of ‘our policies, -#1at, which receive only the overall task com- mand (e.g, "bag the groceries") with ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Out-of-box evaluation results: We evaluate 7p trained for the full 700k steps, a version trained for 160k steps that ‘matches the number of ...
- **p. 7 / VI. EXPERIMENTAL EVALUATION - extractive body cue:** How well does xo follow language commands? ‘These experiments compare xo to xo-Small, a smaller version of our ‘model without VLM initialization, to evaluate its ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 9 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Embodiment/environment | We study this question by directly evaluating 79, with comparisons to other robot foundation models. | hardware/simulator version and reset protocol | p. 7 (VI. EXPERIMENTAL EVALUATION), p. 7 (VI. EXPERIMENTAL EVALUATION) |
| Dataset/benchmark | We study this question by directly evaluating 79, with comparisons to other robot foundation models. | role, split, size and leakage | p. 7 (VI. EXPERIMENTAL EVALUATION), p. 7 (VI. EXPERIMENTAL EVALUATION) |
| Metric | Fig. 9: Language evaluation. We compare "flat" versions of ‘our policies, -#1at, which receive only the overall task com- mand (e.g, "bag the groceries") with a method that receives intermediate commands from ... | definition, denominator, direction and uncertainty | p. 9 (Figure/Table caption), p. 7 (VI. EXPERIMENTAL EVALUATION), p. 1 (Figure/Table caption) |
| Baseline/ablation | Fig. 7: Out-of-box evaluation results: We evaluate 7p trained for the full 700k steps, a version trained for 160k steps that ‘matches the number of updates for baseline models, x-small, and three ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 7 (VI. EXPERIMENTAL EVALUATION), p. 7 (VI. EXPERIMENTAL EVALUATION) |

## Explicit Limitations and Failure Boundary

- **p. 11 / C. Learning new dexterous tasks - extractive body cue:** DISCUSSION, LIMITATIONS, AND FUTURE WORK
- **p. 10 / C. Learning new dexterous tasks - extractive body cue:** This presents challenges due to the egg shape, slipperiness, and the need for careful placement.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, developing such generalist robot policies - ie., robot foundation models - involves a number of major challenges.를 문제로 두고, ‘of more complex and dexterous behaviors, such as tying shoelaces [58] or cooking shrimp [17], we show that our framework can leam very long tasks, sometimes tens of, minutes in length, for ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 4 (1. INTRODUCTION), p. 5 (IV. THE x MODEL) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, developing such generalist robot policies - ie., robot foundation models - involves a number of major challenges. (p. 2, 1. INTRODUCTION).
- **Actual contribution:** The contributions of our work consist of a novel generalist robot policy architecture based on VLM pre-training and flow matching, and an empirical investigation of pre-training/posttraining recipes for such robot ... (p. 3, 1. INTRODUCTION).
- **Evaluation boundary:** Fig. 7: Out-of-box evaluation results: We evaluate 7p trained for the full 700k steps, a version trained for 160k steps that ‘matches the number of updates for baseline models, x-small, ... (p. 8, Figure/Table caption).
- **Explicit failure boundary:** OpenVLA struggles on these tasks because its autoregressive diseretization architecture does not support action chunks. (p. 7, A. Evaluating the base model).
