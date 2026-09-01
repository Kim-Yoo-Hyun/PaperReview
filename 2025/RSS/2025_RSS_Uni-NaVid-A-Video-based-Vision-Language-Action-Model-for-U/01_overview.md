# Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p013.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p013.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, Navigation, embodied navigation, video policy, low-level control, robot data
- Official paper: https://www.roboticsproceedings.org/rss21/p013.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p013.pdf
- Code/Project: https://github.com/jzhzhang/Uni-NaVid
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (17 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, due to the limited rendering quality and diversity of simulators, these approaches often encounter the "sim-to-teal" gap and suffer from poor generalization across diverse navigation tasks (27, 5, 38].를 문제로 두고, However, our goal is to train and ‘evaluate our method on mainstream datasets to clearly justify the performance of our approach.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Embodied Navigation is a fundamental capability for intelligent robots, requiring robots to follow human commands ‘and moye autonomously within physical environments.
- **p. 1 / Abstract - extractive body cue:** Despite Significant advancements, most existing navigation approaches are tailored to specific navigation tasks, such as instruction following, searching objects, answering questions, tracking people, and more.
- **p. 1 / Abstract - extractive body cue:** However, the increasing demands on advanced embodied
- **p. 1 / Abstract - extractive body cue:** ractical navigation mm tasks naturally ‘and benefits from the synergy between these tasks.
- **p. 1 / Abstract - extractive body cue:** To this end, we present Uni 2 video-based vision-language-action (VLA) ‘model to unify different paradigms of navigation tasks and improve navigation performance by encouraging the ...
- **p. 2 / 1. Ivrropuction - extractive body cue:** However, due to the limited rendering quality and diversity of simulators, these approaches often encounter the "sim-to-teal" gap and suffer from poor generalization across diverse ...
- **p. 3 / 1. Ivrropuction - extractive body cue:** However, it faces efficiency challenges in longhorizon tasks.

## Core Idea

- **p. 3 / 1. Ivrropuction - extractive body cue:** However, our goal is to train and ‘evaluate our method on mainstream datasets to clearly justify the performance of our approach.
- **p. 2 / 1. Ivrropuction - extractive body cue:** ‘We conduct extensive experiments on benchmarks across the aforementioned four navigation tasks and compared our method with strong baselines specifically designed for each task.
- **p. 1 / Abstract - extractive body cue:** To efficiently process extensive RGB video streams, we propose an online token merge strategy that spatially and {temporally consolidates similar visual information which improves the ...
- **p. 1 / Abstract - extractive body cue:** To this end, we present Uni 2 video-based vision-language-action (VLA) ‘model to unify different paradigms of navigation tasks and improve navigation performance by encouraging the ...
- **p. 2 / 1. Ivrropuction - extractive body cue:** To this end, we propose an online token merging mechanism to compress near historical frames with a relatively low ratio while compressing far
- **p. 7 / B. Training Strategy of Uni-NaVid - extractive body cue:** To incorporate openworld knowledge, we follow previous Vision-and-Language Action models (100, 9]. integrating open-world video questionanswering during training, Specifically, we adopt a two-stage training process ...
- **p. 7 / B. Training Strategy of Uni-NaVid - extractive body cue:** During training, the vision encoder (EVACLIP (77) and large language model (Vicuna-7B [20)) are preloaded with default pre-trained weight.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | This VLA model can directly take natural language instructions and RGB video streams as inputs and output low-level robotic actions in an end-to-end manner. | camera/depth stream, pose, map와 language goal | p. 1 (Abstract), p. 2 (1. Ivrropuction) |
| State/latent | VLA, model, directly, take, natural, language, instructions, RGB, video, streams, inputs, output | robot pose, free-space/semantic map와 local goal | p. 1 (Abstract), p. 2 (1. Ivrropuction), p. 3 (1. Ivrropuction) |
| Output/action | Uni-NaVid_ takes egocentric RGB video streams and natural language instructions as inputs, and directly generates low-level actions for navigation in continuous environments. ‘To achieve multi-task navigation While supporting efficient ... | collision-free trajectory 또는 velocity command | p. 2 (1. Ivrropuction), p. 3 (1. Ivrropuction), p. 3 (1. Ivrropuction) |
| Objective/outcome | Following the training strategy of VLM [SI], we optimize the trainable parameters for only 1 epoch | goal reach, safety, localization error와 replanning latency | p. 7 (B. Training Strategy of Uni-NaVid) |

## Main Claims and Actual Contribution

- **p. 3 / 1. Ivrropuction - extractive body cue:** However, our goal is to train and ‘evaluate our method on mainstream datasets to clearly justify the performance of our approach.
- **p. 2 / 1. Ivrropuction - extractive body cue:** ‘We conduct extensive experiments on benchmarks across the aforementioned four navigation tasks and compared our method with strong baselines specifically designed for each task.
- **p. 1 / Abstract - extractive body cue:** To efficiently process extensive RGB video streams, we propose an online token merge strategy that spatially and {temporally consolidates similar visual information which improves the ...
- **p. 1 / Abstract - extractive body cue:** To this end, we present Uni 2 video-based vision-language-action (VLA) ‘model to unify different paradigms of navigation tasks and improve navigation performance by encouraging the ...
- **p. 2 / 1. Ivrropuction - extractive body cue:** To this end, we propose an online token merging mechanism to compress near historical frames with a relatively low ratio while compressing far
- **p. 8 / B. Individual Task Results - extractive body cue:** The results in Table V demonstrate that our method achieves significant improvement over the zero-shot method (VLFM [93] and even outperforms the fine-tuned method (DAgRL+0D ...
- **p. 8 / B. Individual Task Results - extractive body cue:** significant improvements, with a +25.7% increase in Success Rate (SR) on R2R.
- **p. 11 / C. Qualitative Results in Real-World - extractive body cue:** The results demonstrate the synergistic benefits of multi-task learning, which yields consistent performance improvements across all navigation tasks, Notably, VLN, ObjectNav, and EQA exhibit more ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (B. Individual Task Results), p. 8 (B. Individual Task Results) |
| Embodiment/environment | The robot then executes the predicted actions and calls STOP once the first predicted action is a stop action, For VLN and EQA tasks, we directly use the text instruction provided by ... | hardware/simulator version and reset protocol | p. 7 (VI. EXPERIMENT), p. 7 (VI. EXPERIMENT) |
| Dataset/benchmark | During navigation, the robot asynchronously compresses and uploads the latest ‘observations to the model while executing pending actions, Refer to the supplementary video for real-world navigation performance. | role, split, size and leakage | p. 7 (VI. EXPERIMENT), p. 7 (VI. EXPERIMENT), p. 8 (VI. EXPERIMENT), p. 11 (C. Qualitative Results in Real-World) |
| Metric | standard evaluation metrics [4], including success rate (SR), oracle success rate (OS), success weighted by path length (SPL) [3], trajectory length (TL), following rate (FR) [65], collision rate (CR) [65] and navigation ... | definition, denominator, direction and uncertainty | p. 7 (VI. EXPERIMENT), p. 8 (B. Individual Task Results), p. 8 (B. Individual Task Results) |
| Baseline/ablation | Compared to ‘mainstream baselines, we find that Uni-NaVid archives the best performance on four metrics, including BLUE-1 (417.9%), ROUGE (5.7%), METEOR (+ 16.2%), and CIDEr (413.1%) ‘This proves the superiority of our ... | fair input/data/compute/action matching | p. 9 (B. Individual Task Results), p. 7 (VI. EXPERIMENT), p. 8 (B. Individual Task Results) |

## Explicit Limitations and Failure Boundary

- **p. 7 / VI. EXPERIMENT - extractive body cue:** standard evaluation metrics [4], including success rate (SR), oracle success rate (OS), success weighted by path length (SPL) [3], trajectory length (TL), following rate (FR) ...
- **p. 11 / C. Qualitative Results in Real-World - extractive body cue:** Despite the promising results, Uni-NaVid has several limitations.
- **p. 11 / C. Qualitative Results in Real-World - extractive body cue:** This limitation could be alleviated by extending the moel to predict
- **p. 10 / B. Individual Task Results - extractive body cue:** gies, while also highlighting robust open-world understanding capabilities.

## Why Read It

VLA and generalist robot policies의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, due to the limited rendering quality and diversity of simulators, these approaches often encounter the "sim-to-teal" gap and suffer from poor generalization across diverse navigation tasks (27, 5, 38].를 문제로 두고, However, our goal is to train and ‘evaluate our method on mainstream datasets to clearly justify the performance of our approach.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Ivrropuction), p. 3 (1. Ivrropuction), p. 1 (1. Ivrropuction), p. 1 (1. Ivrropuction), p. 2 (1. Ivrropuction), p. 7 (B. Training Strategy of Uni-NaVid) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
