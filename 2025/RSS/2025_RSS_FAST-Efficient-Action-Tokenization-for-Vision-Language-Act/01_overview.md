# FAST: Efficient Action Tokenization for Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-19 표본 감사에서 요약과 관련 본문 표현을 원문에 대조해 교정했다. [원문](https://arxiv.org/html/2501.09747)
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p012.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p012.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: CORE
- Tags: Robotics, VLA, action tokenization, high-frequency control, cross-embodiment, efficiency
- Official paper: https://www.roboticsproceedings.org/rss21/p012.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p012.pdf
- Code/Project: https://www.pi.website/research/fast
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

FAST는 여러 시점의 로봇 행동을 짧은 토큰열로 바꾸어 자기회귀 VLA가 고주파 제어를 학습할 수 있게 한다. [원문](https://arxiv.org/html/2501.09747)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Autoregressive sequence models, such as, Transformer-based vision-language action (VLA) policies, can be tremendously effective for capturing complex and generalizable robotic behaviors.
- **p. 1 / Abstract - extractive body cue:** However, such models require tus to choose a tokenization of our continuous action signals, which determines how the diserete symbols predicted by the ‘model map ...
- **p. 1 / Abstract - extractive body cue:** We find that current approaches for robot action tokenization, based on simple per-dimension, per-timestep binning schemes, typically perform poorly when learning dexterous skills from. high-frequency ...
- **p. 1 / Abstract - extractive body cue:** Our tokenization approach, Frequency space Action Sequence Tokenization (FAST), enables tus to train autoregressive VLAs for highly dexterous and high-frequency tasks where standard discretization methods ...
- **p. 1 / Abstract - extractive body cue:** Based on FAST, we release FAST, a universal robot action tokenizer, trained on IM real robot action trajectories.
- **p. 4 / 1. INTRODUCTION - source paraphrase:** The authors illustrate redundancy in high-frequency action token sequences with a spline prediction task.
- **p. 4 / 1. INTRODUCTION - extractive body cue:** This greatly slows down the rate of convergence during training and can make it challenging to fit complex, high-frequency datasets Indeed, such challenges have been ...

## Core Idea

FAST는 정규화한 연속 행동 청크에 차원별 이산 코사인 변환(DCT)을 적용한다. 변환 계수를 양자화한 뒤 byte-pair encoding으로 압축해 자기회귀 VLA가 예측할 토큰열을 만든다. [원문](https://arxiv.org/html/2501.09747)

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | An alternative approach directly trains VLAs to output low-level robot control commands given image and language instruction inputs. | image/video, language instruction, proprioception과 history | p. 3 (1. INTRODUCTION), p. 1 (1. INTRODUCTION) |
| State/latent | alternative, directly, trains, VLAS, output, ow-level, robot, control, commands, given, image, language | language-grounded task state와 action-policy context | p. 3 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 10 (C. Universal Action Tokenizer) |
| Output/action | FAST encodes continuous action chunks as discrete tokens using time-series compression. | continuous action, pose 또는 action chunk | p. 1 (1. INTRODUCTION), p. 10 (C. Universal Action Tokenizer), p. 2 (1. INTRODUCTION) |
| Objective/outcome | After the data is normalized, we apply the discrete cosine transform to each action dimension separately. ‘To compress the DCT-converted signal we can simply omit insignificant coefficients, which we implement through a ... | instruction following, task success, generalization과 latency | p. 4 (B. The FAST Tokenization Algorithm), p. 5 (B. The FAST Tokenization Algorithm), p. 5 (B. The FAST Tokenization Algorithm) |

## Main Claims and Actual Contribution

시간축 압축이 단순한 시점별 이산화에 비해 고주파 조작에서 자기회귀 정책의 학습을 개선하는지 비교했다. 정책 간 비교에서는 토크나이저와 행동 생성 방식을 구별해야 한다. [원문](https://arxiv.org/html/2501.09747)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (A. Experimental Setup), p. 2 (Figure/Table caption) |
| Embodiment/environment | fon a large dataset of IM action sequences trained the universal tokenizer on the most diverse real robot dataset we could assemble, which includes data from our real robot evaluation tasks. | hardware/simulator version and reset protocol | p. 7 (A. Experimental Setup), p. 6 (A. Experimental Setup) |
| Dataset/benchmark | We then compare π₀ models trained with FAST tokenization to the state-of-the-art π₀ flow-matching (diffusion) VLA, and test the scaling of autoregressive VLA training with FAST to large, cross-embodied datasets with 10k ... | role, split, size and leakage | p. 7 (A. Experimental Setup), p. 6 (A. Experimental Setup), p. 6 (VI. EXPERIMENTS), p. 7 (A. Experimental Setup) |
| Metric | We report success rate on individual clothing items. | definition, denominator, direction and uncertainty | p. 7 (A. Experimental Setup), p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup) |
| Baseline/ablation | We then compare π₀ models trained with FAST tokenization to the state-of-the-art π₀ flow-matching (diffusion) VLA, and test the scaling of autoregressive VLA training with FAST to large, cross-embodied datasets with 10k ... | fair input/data/compute/action matching | p. 6 (VI. EXPERIMENTS), p. 1 (Figure/Table caption), p. 2 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / B. Comparing Action Tokenizers for VLA Training - extractive body cue:** Even unsuccessful trials show sensible behavior, like approaching the handles of microwave and dish washer doors, even if ultimately failing to open them, We show ...
- **p. 9 / C. Universal Action Tokenizer - extractive body cue:** One current limitation of the autoregressive VLA is its inference speed: while 7» with diffusion typically predicts one second action chunks within 100ms on an ...
- **p. 9 / C. Universal Action Tokenizer - extractive body cue:** We will leave a detailed investigation of the language following abilities of diffusion and autoregressive VLAS to future work.
- **p. 8 / B. Comparing Action Tokenizers for VLA Training - extractive body cue:** While far from perfect, the level of generality and robustness of this policy substantially exceeds that of prior DROID policies.
- **p. 10 / C. Universal Action Tokenizer - extractive body cue:** ‘To summarize, we have demonstrated that FAST tokenization allows us to train autoregressive VLA on complex, dexterous robot tasks that prior tokenization schemes completely fail ...

## Why Read It

FAST는 행동 토크나이저이며 π₀-FAST는 이 표현으로 학습한 정책이다. 같은 행동 데이터에서 표현 방식과 정책 학습의 효과를 비교할 때 이 구분이 필요하다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (19 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** We observe that correlations between time steps are a major challenge for naive tokenization strategies when predicting sequences of (p. 1, 1. INTRODUCTION).
- **Actual contribution:** FAST는 정규화한 연속 행동 청크에 차원별 이산 코사인 변환(DCT)을 적용한다. 변환 계수를 양자화한 뒤 byte-pair encoding으로 압축해 자기회귀 VLA가 예측할 토큰열을 만든다. [원문](https://arxiv.org/html/2501.09747)
- **Evaluation boundary:** We develop a suite of 7 evaluation tasks 6 real robot, 1 simulated; see Figure 5), designed to test VLA performance on both, highly dexterous tasks like laundry folding, and ... (p. 6, A. Experimental Setup).
- **Explicit failure boundary:** We do ‘not measure success rates during these evaluations, but provide ‘numerous qualitative videos of successes and failures to help readers get a sense of the policy's capabilities (p. 18, B. Discussion of Alternative Compression Approaches).
