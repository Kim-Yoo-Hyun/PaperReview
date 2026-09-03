# Unified Video Action Model

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p074.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p074.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, world model, video action model, Diffusion, inverse dynamics, generalist policy
- Official paper: https://www.roboticsproceedings.org/rss21/p074.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p074.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 PAD [19] jointly trains video generation and action prediction; however, it cannot predict future actions independently of future image generation, resulting in slower inference.를 문제로 두고, ‘To address these limitations, we propose UVA, « Unified Video and Action Mode! designed to simultaneously model videos and actions - capturing the underlying interactions between visuals and actions to enhance task ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** A unified video and act for robotics, where videos provide rich scene
- **p. 1 / Abstract - extractive body cue:** forprediction, and actions provide dynamics ion for video prediction.
- **p. 1 / Abstract - extractive body cue:** However, effectively combining, video generation and action prediction remains challenging, and ‘current video generation-based methods struggle to match the performance of direct policy learning in ...
- **p. 1 / Abstract - extractive body cue:** To bridge this gap, we introduce the Unified Video Action model (UVA), which jointly optimizes video and action predictions to achieve both high accuracy and ...
- **p. 1 / Abstract - extractive body cue:** The key lies in learning a joint video-action latent representation and decoupling video-action decoding.
- **p. 2 / 1. Iyrropucrion - extractive body cue:** PAD [19] jointly trains video generation and action prediction; however, it cannot predict future actions independently of future image generation, resulting in slower inference.
- **p. 3 / 1. Iyrropucrion - extractive body cue:** However, effectively leveraging video data for policy learning presents challenges such asthe ability to match the high temporal speed required for outputting dense, finegrained motions.

## Core Idea

- **p. 1 / 1. Iyrropucrion - extractive body cue:** ‘To address these limitations, we propose UVA, « Unified Video and Action Mode! designed to simultaneously model videos and actions - capturing the underlying interactions ...
- **p. 2 / 1. Iyrropucrion - extractive body cue:** At inference, this decoupling allows the system to bypass video generation entirely, directly utilizing the latent representation for fast action prediction, This design enables real-time ...
- **p. 1 / 1. Iyrropucrion - extractive body cue:** We propose the following three design choices to achieve this:
- **p. 2 / 1. Iyrropucrion - extractive body cue:** In this work, we propose a unified video and action model, showcasing its ability to address both policy leaning and dynamics modeling within a single ...
- **p. 3 / 1. Iyrropucrion - extractive body cue:** Ae © R/*"" consists of L actions, and each action has m dimensions.
- **p. 4 / C. Decoupled Video and Action Diffusions - extractive body cue:** Previous video generation-based policy learning methods rely on hierarchically generating videos first and then predicting actions, leading to slow speed and accumulated errors. ‘To address ...
- **p. 4 / C. Decoupled Video and Action Diffusions - extractive body cue:** Instead of training the model solely on the task of predicting future observations and actions based on historical data, we propose a masked training approach ...
- **p. 5 / C. Decoupled Video and Action Diffusions - extractive body cue:** This masked training strategy enables the model to perform a diverse range of functions, including acting as a robot policy, video ‘model, forward and inverse ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 3) Mask Training for Flexibility: The ability to predict both videos and actions through unified representations further unlocks the potential to perform a diverse set of functions using masked training, UVA can ... | observation, uncertainty/risk estimate와 task command | p. 2 (1. Iyrropucrion), p. 3 (1. Iyrropucrion) |
| State/latent | Mask, Training, Flexibility, ability, predict, videos, actions, through, unified, representations, further, unlocks | safe set, recovery state 또는 constraint margin | p. 2 (1. Iyrropucrion), p. 3 (1. Iyrropucrion), p. 1 (Body text (section boundary not confidently recovered)) |
| Output/action | Problem Statement: Given a sequence of image observations {Ocners---sOr} and action chunks {Ar-n,.-..Aea}e where his the history horizon, our goal is to predict the future actions {Ay,...,As.,*-1} and observations {Opcis..-,Orsne}s wher ... | shielded, recovery 또는 safe action | p. 3 (1. Iyrropucrion), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (1. Iyrropucrion) |
| Objective/outcome | Masked Training with Flexible Objectives | task return과 violation/failure probability | p. 4 (C. Decoupled Video and Action Diffusions), p. 4 (C. Decoupled Video and Action Diffusions), p. 5 (V. UVA As PoLicy) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Iyrropucrion - extractive body cue:** ‘To address these limitations, we propose UVA, « Unified Video and Action Mode! designed to simultaneously model videos and actions - capturing the underlying interactions ...
- **p. 2 / 1. Iyrropucrion - extractive body cue:** At inference, this decoupling allows the system to bypass video generation entirely, directly utilizing the latent representation for fast action prediction, This design enables real-time ...
- **p. 1 / 1. Iyrropucrion - extractive body cue:** We propose the following three design choices to achieve this:
- **p. 2 / 1. Iyrropucrion - extractive body cue:** In this work, we propose a unified video and action model, showcasing its ability to address both policy leaning and dynamics modeling within a single ...
- **p. 3 / 1. Iyrropucrion - extractive body cue:** Ae © R/*"" consists of L actions, and each action has m dimensions.
- **p. 8 / B. Real-world Benchmarks - extractive body cue:** For example, with changes in goal color, UniPi achieves a success rate of 40%, UVA achieves 64%, while OpenVLA only reaches 32%.
- **p. 8 / B. Real-world Benchmarks - extractive body cue:** All tests are unseen during training, and even with more challenging distractor objects and backgrounds, UVA achieves higher success rates than DP-UML To more rigorously ...
- **p. 7 / B. Real-world Benchmarks - extractive body cue:** We found that the UVA Attention module in the Transformer accounts for half of the inference time, making UVA slightly slower than DP-UML With future ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (B. Real-world Benchmarks), p. 8 (B. Real-world Benchmarks) |
| Embodiment/environment | Trained on a diverse dataset spanning multiple robot embodiments and tasks, xo demonstrates. strong zero-shot and fine-tuned performance. | hardware/simulator version and reset protocol | p. 6 (B. Real-world Benchmarks), p. 5 (B. Real-world Benchmarks) |
| Dataset/benchmark | significantly out-of-distribution with unseen environments, objects, robots, and even gripper colors. | role, split, size and leakage | p. 6 (B. Real-world Benchmarks), p. 5 (B. Real-world Benchmarks), p. 6 (B. Real-world Benchmarks), p. 5 (B. Real-world Benchmarks) |
| Metric | UVA has higher success rate than the baselines in most settings, with a strong performance in multi-task scenatios, Speed is measured by a single faction trajectory inference. | definition, denominator, direction and uncertainty | p. 5 (A. Simulation Benchmarks), p. 5 (B. Real-world Benchmarks), p. 7 (B. Real-world Benchmarks) |
| Baseline/ablation | This evaluation aims to compare ‘our method with a strong baseline in prior works by replicating 4 similar evaluation setup. | fair input/data/compute/action matching | p. 7 (B. Real-world Benchmarks), p. 6 (B. Real-world Benchmarks), p. 7 (B. Real-world Benchmarks) |

## Explicit Limitations and Failure Boundary

- **p. 10 / IX. Discussion - extractive body cue:** Limitation and Future Work: One limitation of our frame- ‘work is that it does not currently leverage large amounts of actionless video data, which could ...
- **p. 7 / B. Real-world Benchmarks - extractive body cue:** However, in this case, the collected failure recovery data is less impactful for our model, as its longer memory window prioritizes learning from extended temporal ...
- **p. 7 / B. Real-world Benchmarks - extractive body cue:** We noticed that the dataset contains extensive recovery data from the moments of failure to correct the policy. ‘This data is particularly useful for models ...
- **p. 10 / IX. Discussion - extractive body cue:** We believe that pretraining the model on web-scale video datasets could significantly enhance its generalization capabilites, and we leave this exploration for future work.
- **p. 6 / B. Real-world Benchmarks - extractive body cue:** We evaluate policy learning results with UVA compared to the baseline methods on a few different axes: 1) action prediction accuracy, 2) inference speed, 3) ...
- **p. 8 / B. Real-world Benchmarks - extractive body cue:** Robustness to History Length: Prior policy learning meth- ‘ods, such as DP-C, often experience performance degradation as the history length increases as shown in Figure ...
- **p. 8 / B. Real-world Benchmarks - extractive body cue:** This explains why DP-C is slower than UVA in Table I and DP-UMI is faster in Table I, ‘Overall, UVA achieves a good balance between ...

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 PAD [19] jointly trains video generation and action prediction; however, it cannot predict future actions independently of future image generation, resulting in slower inference.를 문제로 두고, ‘To address these limitations, we propose UVA, « Unified Video and Action Mode! designed to simultaneously model videos and actions - capturing the underlying interactions between visuals and actions to enhance task ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Iyrropucrion), p. 3 (1. Iyrropucrion), p. 1 (Abstract), p. 1 (Abstract), p. 3 (1. Iyrropucrion), p. 4 (C. Decoupled Video and Action Diffusions) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** PAD [19] jointly trains video generation and action prediction; however, it cannot predict future actions independently of future image generation, resulting in slower inference. (p. 2, 1. Iyrropucrion).
- **Actual contribution:** ‘To address these limitations, we propose UVA, « Unified Video and Action Mode! designed to simultaneously model videos and actions - capturing the underlying interactions between visuals and actions to ... (p. 1, 1. Iyrropucrion).
- **Evaluation boundary:** We evaluate policy learning results with UVA compared to the baseline methods on a few different axes: 1) action prediction accuracy, 2) inference speed, 3) robustness to visual disturbances, 4) ... (p. 6, B. Real-world Benchmarks).
- **Explicit failure boundary:** Limitation and Future Work: One limitation of our frame- ‘work is that it does not currently leverage large amounts of actionless video data, which could provide valuable additional supervision. (p. 10, IX. Discussion).
