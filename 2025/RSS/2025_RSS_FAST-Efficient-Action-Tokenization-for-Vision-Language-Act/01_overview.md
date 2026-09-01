# FAST: Efficient Action Tokenization for Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (19 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p012.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p012.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, VLA, action tokenization, high-frequency control, cross-embodiment, efficiency
- Official paper: https://www.roboticsproceedings.org/rss21/p012.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p012.pdf
- Code/Project: https://www.pi.website/research/fast
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (19 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 ‘To illustrate the challenge of training autoregressive poli cies with current action tokenization approaches, we star With a simple didactic example.를 문제로 두고, 1: We propose FAS nple yet effective approach for tokenization of robot action trajectories via time-series compression, FAST enables training of autoregressive VLAs that solve complex dexterous manipulation tasks and generalize broadly ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Autoregressive sequence models, such as, Transformer-based vision-language action (VLA) policies, can be tremendously effective for capturing complex and generalizable robotic behaviors.
- **p. 1 / Abstract - extractive body cue:** However, such models require tus to choose a tokenization of our continuous action signals, which determines how the diserete symbols predicted by the ‘model map ...
- **p. 1 / Abstract - extractive body cue:** We find that current approaches for robot action tokenization, based on simple per-dimension, per-timestep binning schemes, typically perform poorly when learning dexterous skills from. high-frequency ...
- **p. 1 / Abstract - extractive body cue:** Our tokenization approach, Frequency space Action Sequence Tokenization (FAST), enables tus to train autoregressive VLAs for highly dexterous and high-frequency tasks where standard discretization methods ...
- **p. 1 / Abstract - extractive body cue:** Based on FAST, we release FAST, a universal robot action tokenizer, trained on IM real robot action trajectories.
- **p. 4 / 1. INTRODUCTION - extractive body cue:** ‘To illustrate the challenge of training autoregressive poli cies with current action tokenization approaches, we star With a simple didactic example.
- **p. 4 / 1. INTRODUCTION - extractive body cue:** This greatly slows down the rate of convergence during training and can make it challenging to fit complex, high-frequency datasets Indeed, such challenges have been ...

## Core Idea

- **p. 1 / 1. INTRODUCTION - extractive body cue:** 1: We propose FAS nple yet effective approach for tokenization of robot action trajectories via time-series compression, FAST enables training of autoregressive VLAs that solve ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** We introduce a new action tokenization approach that allows us to train the first autoregressive VLAs ‘on dexterous and high-frequency robot data
- **p. 3 / 1. INTRODUCTION - extractive body cue:** We find that this scheme struggles to scale to high-frequency robot control tasks, We propose a new tokenization scheme for robot actions, based on time-series ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** In this work, we propose a new tokenization strategy from first principles.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** We therefore base our method off of the discrete cosine transform (DCT) encoding, which is widely used for ‘compressing continuous signals stich as images (€.g., ...
- **p. 4 / B. The FAST Tokenization Algorithm - extractive body cue:** We first normalize the input actions, such that the Ist and 99th quantile of values in the training dataset for each action dimension maps to ...
- **p. 5 / B. The FAST Tokenization Algorithm - extractive body cue:** xerleaving action di ‘mensions by including all low-frequency components first, and train a byte pair encoding (BPE) tokenizer [27] to losslessly ‘compress it into dense ...
- **p. 4 / B. The FAST Tokenization Algorithm - extractive body cue:** We use quantiles to be robust to outlier actions which occasionally occur in large robot datasets.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | An alternative approach directly trains VLAS to output ow-level robot control commands given image and language instruction inputs. | image/video, language instruction, proprioception과 history | p. 3 (1. INTRODUCTION), p. 1 (1. INTRODUCTION) |
| State/latent | alternative, directly, trains, VLAS, output, ow-level, robot, control, commands, given, image, language | language-grounded task state와 action-policy context | p. 3 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 10 (C. Universal Action Tokenizer) |
| Output/action | 1: We propose FAS nple yet effective approach for tokenization of robot action trajectories via time-series compression, FAST enables training of autoregressive VLAs that solve complex dexterous manipulation tasks and generalize broadly ... | continuous action, pose 또는 action chunk | p. 1 (1. INTRODUCTION), p. 10 (C. Universal Action Tokenizer), p. 2 (1. INTRODUCTION) |
| Objective/outcome | After the data is normalized, we apply the discrete cosine transform to each action dimension separately. ‘To compress the DCT-converted signal we can simply omit insignificant coefficients, which we implement through a ... | instruction following, task success, generalization과 latency | p. 4 (B. The FAST Tokenization Algorithm), p. 5 (B. The FAST Tokenization Algorithm), p. 5 (B. The FAST Tokenization Algorithm) |

## Main Claims and Actual Contribution

- **p. 1 / 1. INTRODUCTION - extractive body cue:** 1: We propose FAS nple yet effective approach for tokenization of robot action trajectories via time-series compression, FAST enables training of autoregressive VLAs that solve ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** We introduce a new action tokenization approach that allows us to train the first autoregressive VLAs ‘on dexterous and high-frequency robot data
- **p. 3 / 1. INTRODUCTION - extractive body cue:** We find that this scheme struggles to scale to high-frequency robot control tasks, We propose a new tokenization scheme for robot actions, based on time-series ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** In this work, we propose a new tokenization strategy from first principles.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** We therefore base our method off of the discrete cosine transform (DCT) encoding, which is widely used for ‘compressing continuous signals stich as images (€.g., ...
- **p. 7 / A. Experimental Setup - extractive body cue:** We report success rate on individual clothing items.
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: Left: FAST tokenization enables training of autoregres- sive Transformers for dexterous robot control via simple next token prediction. Right: FAST outperforms popular binning ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 11: Comparison of x)-FAST and diffusion x [7] generalist policies. zp-FAST matches the performance of Aiffusion 7p while requiring significantly less compute for training. ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (A. Experimental Setup), p. 2 (Figure/Table caption) |
| Embodiment/environment | fon a large dataset of IM action sequences trained the universal tokenizer on the most diverse real robot dataset we could assemble, which includes data from our real robot evaluation tasks. | hardware/simulator version and reset protocol | p. 7 (A. Experimental Setup), p. 6 (A. Experimental Setup) |
| Dataset/benchmark | We then compare 7 models trained with FAST tokenization to the state-of-the-art 79 flow-matching (diffusion) VLA, and test the scaling of autoregressive VLA training with FAST to large, cross-embodied datasets with 10k ... | role, split, size and leakage | p. 7 (A. Experimental Setup), p. 6 (A. Experimental Setup), p. 6 (VI. EXPERIMENTS), p. 7 (A. Experimental Setup) |
| Metric | We report success rate on individual clothing items. | definition, denominator, direction and uncertainty | p. 7 (A. Experimental Setup), p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup) |
| Baseline/ablation | We then compare 7 models trained with FAST tokenization to the state-of-the-art 79 flow-matching (diffusion) VLA, and test the scaling of autoregressive VLA training with FAST to large, cross-embodied datasets with 10k ... | fair input/data/compute/action matching | p. 6 (VI. EXPERIMENTS), p. 1 (Figure/Table caption), p. 2 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / B. Comparing Action Tokenizers for VLA Training - extractive body cue:** Even unsuccessful trials show sensible behavior, like approaching the handles of microwave and dish washer doors, even if ultimately failing to open them, We show ...
- **p. 9 / C. Universal Action Tokenizer - extractive body cue:** One current limitation of the autoregressive VLA is its inference speed: while 7» with diffusion typically predicts one second action chunks within 100ms on an ...
- **p. 9 / C. Universal Action Tokenizer - extractive body cue:** We will leave a detailed investigation of the language following abilities of diffusion and autoregressive VLAS to future work.
- **p. 8 / B. Comparing Action Tokenizers for VLA Training - extractive body cue:** While far from perfect, the level of generality and robustness of this policy substantially exceeds that of prior DROID policies.
- **p. 10 / C. Universal Action Tokenizer - extractive body cue:** ‘To summarize, we have demonstrated that FAST tokenization allows us to train autoregressive VLA on complex, dexterous robot tasks that prior tokenization schemes completely fail ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 ‘To illustrate the challenge of training autoregressive poli cies with current action tokenization approaches, we star With a simple didactic example.를 문제로 두고, 1: We propose FAS nple yet effective approach for tokenization of robot action trajectories via time-series compression, FAST enables training of autoregressive VLAs that solve complex dexterous manipulation tasks and generalize broadly ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 4 (1. INTRODUCTION), p. 4 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 4 (B. The FAST Tokenization Algorithm) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
