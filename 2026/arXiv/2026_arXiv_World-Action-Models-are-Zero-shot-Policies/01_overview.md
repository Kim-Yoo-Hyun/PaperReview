# World Action Models are Zero-shot Policies

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (36 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2602.15922.
> PDF retrieval source: https://arxiv.org/pdf/2602.15922. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / arXiv
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics, VLA, world model, zero-shot policy, action representation
- Official paper: https://arxiv.org/abs/2602.15922
- Full-text retrieval: https://arxiv.org/pdf/2602.15922
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (36 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 safety 문제를 이해하기 위해 읽는다. 본문은 Although VLM priors encode what to do at a semantic level, they lack representations of how actions should be executed with precise spatial awareness, aligned with geometry, dynamics, and motor control (Chen ...를 문제로 두고, Second, and more surprisingly, we show that DreamZero enables few-shot embodiment adaptation: a model pretrained on AgiBot G1 adapts to an entirely new robot (YAM) with only 30 minutes of play data, ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 2 / Abstract - extractive body cue:** State-of-the-art Vision-Language-Action (VLA) models excel at semantic generalization but struggle to generalize to unseen physical motions in novel environments.
- **p. 2 / Abstract - extractive body cue:** We introduce DreamZero, a World Action Model (WAM) built upon a pretrained video diffusion backbone.
- **p. 2 / Abstract - extractive body cue:** Unlike VLAs, WAMs learn physical dynamics by predicting future world states and actions, using video as a dense representation of how the world evolves.
- **p. 2 / Abstract - extractive body cue:** By jointly modeling video and action, DreamZero learns diverse skills effectively from heterogeneous robot data without relying on repetitive demonstrations.
- **p. 2 / Abstract - extractive body cue:** This results in over 2× improvement in generalization to new tasks and environments compared to state-of-the-art VLAs in realrobot experiments.
- **p. 2 / 1. Introduction - extractive body cue:** Although VLM priors encode what to do at a semantic level, they lack representations of how actions should be executed with precise spatial awareness, aligned ...
- **p. 2 / 1. Introduction - extractive body cue:** While VLAs successfully inherit linguistic priors to generalize across diverse language instructions, especially manipulating diverse objects (Brohan et al., 2023), their generalization to novel environments ...

## Core Idea

- **p. 3 / 1. Introduction - extractive body cue:** Second, and more surprisingly, we show that DreamZero enables few-shot embodiment adaptation: a model pretrained on AgiBot G1 adapts to an entirely new robot (YAM) ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we present DreamZero, a 14B robot foundation model built upon a pretrained image-tovideo diffusion backbone (Team Wan, 2025).
- **p. 3 / 1. Introduction - extractive body cue:** To address the computational overhead inherent to video diffusion models, we introduce a suite of optimizations spanning three categories: (1) algorithmic improvements, including decoupled video ...
- **p. 2 / 1. Introduction - extractive body cue:** Consequently, we observe that this enables (1) effective learning from robot data that are heterogeneous trajectories collected during the execution of useful behaviors in real-world ...
- **p. 7 / 3.1. Model Architecture - extractive body cue:** We introduce autoregressive modeling only for the video modality to avoid error propagation coming from closed-loop action prediction.
- **p. 7 / 3.1. Model Architecture - extractive body cue:** To retain the generalization capability of video models, we introduce minimal additional parameters: state encoders, action encoders, and decoders.
- **p. 7 / 3.1. Model Architecture - extractive body cue:** Autoregressive generation possesses the following advantages: (1) it enables faster inference speed by utilizing KV-cache, (2) the policy model can leverage the visual observation history ...
- **p. 6 / 3.1. Model Architecture - extractive body cue:** DreamZero jointly predicts video o𝑙:𝑙+𝐻and actions a𝑙:𝑙+𝐻conditioned on language instruction c, proprioceptive state q𝑙and visual observation including the current and the past history o0:𝑙 where ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | DreamZero jointly predicts video o𝑙:𝑙+𝐻and actions a𝑙:𝑙+𝐻conditioned on language instruction c, proprioceptive state q𝑙and visual observation including the current and the past history o0:𝑙 where 𝐻> 0 is a fixed horizon and ... | observation, uncertainty/risk estimate와 task command | p. 6 (3.1. Model Architecture), p. 2 (1. Introduction) |
| State/latent | DreamZero, jointly, predicts, video, actions, conditioned, language, instruction, proprioceptive, state, visual, observation | safe set, recovery state 또는 constraint margin | p. 6 (3.1. Model Architecture), p. 2 (1. Introduction), p. 7 (3.1. Model Architecture) |
| Output/action | Initialized from video diffusion models trained on web-scale video data, WAMs leverage rich spatiotemporal priors to jointly generate future frames and actions conditioned on language instructions and observations. | shielded, recovery 또는 safe action | p. 2 (1. Introduction), p. 7 (3.1. Model Architecture), p. 2 (1. Introduction) |
| Objective/outcome | When cosine similarity between successive velocities exceeds a threshold, we reuse cached velocities, reducing effective DiT steps from 16 to 4 with minimal quality loss on action prediction. | task return과 violation/failure probability | p. 8 (3.2.3. System-level Optimizations), p. 7 (3.1. Model Architecture), p. 7 (3.1. Model Architecture) |

## Main Claims and Actual Contribution

- **p. 3 / 1. Introduction - extractive body cue:** Second, and more surprisingly, we show that DreamZero enables few-shot embodiment adaptation: a model pretrained on AgiBot G1 adapts to an entirely new robot (YAM) ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we present DreamZero, a 14B robot foundation model built upon a pretrained image-tovideo diffusion backbone (Team Wan, 2025).
- **p. 3 / 1. Introduction - extractive body cue:** To address the computational overhead inherent to video diffusion models, we introduce a suite of optimizations spanning three categories: (1) algorithmic improvements, including decoupled video ...
- **p. 2 / 1. Introduction - extractive body cue:** Consequently, we observe that this enables (1) effective learning from robot data that are heterogeneous trajectories collected during the execution of useful behaviors in real-world ...
- **p. 7 / 3.1. Model Architecture - extractive body cue:** We introduce autoregressive modeling only for the video modality to avoid error propagation coming from closed-loop action prediction.
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 10: Posttraining Results. WAMs enable stronger post-training results across three tasks, indicating that environment generalization of DreamZero is retained after post-training. Q3. Do WAMs ...
- **p. 16 / Figure/Table caption - extractive body cue:** Table 2: Cross-Embodiment Transfer Results. Average task progress on unseen tasks (± standard error). Both transfer settings improve over baseline (result from Table 9) using ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Joint Video and Action Prediction. DreamZero jointly generates video and action. We observe that the predicted actions closely align with the generated video. ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 15 (Figure/Table caption), p. 16 (Figure/Table caption) |
| Embodiment/environment | As shown in Figure 6, each episode averages around 4.4 minutes and encompasses approximately 42 subtasks-significantly longer-horizon than typical robotic manipulation datasets (Khazatsky et al., 2024; Walke et al., 2023). | hardware/simulator version and reset protocol | p. 10 (4.1. Pretraining), p. 11 (4.1. Pretraining) |
| Dataset/benchmark | For seen tasks, we select 10 tasks from the pretraining distribution, including pick-and-place variants, stacking, wiping, and folding; we run 8 rollouts per task across 4 robots, each in different environments and ... | role, split, size and leakage | p. 10 (4.1. Pretraining), p. 11 (4.1. Pretraining), p. 12 (4.1. Pretraining), p. 11 (4.1. Pretraining) |
| Metric | Table 2: Cross-Embodiment Transfer Results. Average task progress on unseen tasks (± standard error). Both transfer settings improve over baseline (result from Table 9) using only 10-20 minutes of video-only demonstration data. ... | definition, denominator, direction and uncertainty | p. 16 (Figure/Table caption), p. 13 (5.1. Main Results), p. 12 (4.1. Pretraining) |
| Baseline/ablation | Figure 2: Joint Video and Action Prediction. DreamZero jointly generates video and action. We observe that the predicted actions closely align with the generated video. The examples are from totally unseen tasks. ... | fair input/data/compute/action matching | p. 3 (Figure/Table caption), p. 13 (Figure/Table caption), p. 13 (5.1. Main Results) |

## Explicit Limitations and Failure Boundary

- **p. 19 / 6. Discussion and Future Work - extractive body cue:** While DreamZero generalizes broadly across tasks and environments, it inherits limitations common to behavior cloning on tasks requiring sub-centimeter precision, such as key insertion or ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 9: Zero-shot Generalization to Unseen Tasks. DreamZero achieves non-trivial task progress on 10 tasks absent from training, while VLAs struggle across both embodiments. alignment ...
- **p. 18 / 6. Discussion and Future Work - extractive body cue:** We leave this direction as future work.
- **p. 18 / 6. Discussion and Future Work - extractive body cue:** We leave deep investigation on scaling laws for WAMs as future work.
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 13: Bidirectional vs. Autoregressive WAMs. When the sampling point falls mid-task (T=20), bidirec- tional WAMs must subsample video to align with the language caption, ...
- **p. 9 / 3.2.4. Implementation-level Optimizations - extractive body cue:** However, naively reducing steps degrades action quality because residual visual noise propagates into action predictions.
- **p. 10 / 4. Experimental Setup - extractive body cue:** We pretrain separately for each embodiment, leaving multi-embodiment training for future work.

## Why Read It

VLA and generalist robot policies의 safety 문제를 이해하기 위해 읽는다. 본문은 Although VLM priors encode what to do at a semantic level, they lack representations of how actions should be executed with precise spatial awareness, aligned with geometry, dynamics, and motor control (Chen ...를 문제로 두고, Second, and more surprisingly, we show that DreamZero enables few-shot embodiment adaptation: a model pretrained on AgiBot G1 adapts to an entirely new robot (YAM) with only 30 minutes of play data, ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 3 (1. Introduction), p. 7 (3.1. Model Architecture), p. 7 (3.1. Model Architecture) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
