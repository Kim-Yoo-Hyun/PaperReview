# RynnVLA-001: Using Human Demonstrations to Improve Robot Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html.
> PDF retrieval source: https://arxiv.org/pdf/2509.15212v1. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Robotics
- Official paper: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html
- Full-text retrieval: https://arxiv.org/pdf/2509.15212v1
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Another line of studies works on exploiting massive prior knowledge from pretrained generative models (Cheang et al., 2024; Hu et al., 2024) or VLMs (Zitkovich et al., 2023; Kim et al., 2024; ...를 문제로 두고, In this work, we propose RynnVLA-001, a VLA model enhanced by video generation pretraining.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** The past few years have witnessed rapid progress in large language models (Comanici et al., 2025; Anthropic; OpenAI, 2025; Grattafiori et al., 2024; Guo et ...
- **p. 1 / 1 Introduction - extractive body cue:** The success in these fields is attributed to the availability of large-scale datasets.
- **p. 1 / 1 Introduction - extractive body cue:** For instance, large language models benefit from abundant training data readily accessible from web sources.
- **p. 1 / 1 Introduction - extractive body cue:** In contrast, progress in Vision-Language-Action (VLA) models is constrained by the scarcity of large-scale robot manipulation data.
- **p. 1 / 1 Introduction - extractive body cue:** Collecting such data typically relies on human teleoperation on physical robots to record manipulation trajectories, making large-scale dataset construction both labor-intensive and costly.
- **p. 1 / 1 Introduction - extractive body cue:** Another line of studies works on exploiting massive prior knowledge from pretrained generative models (Cheang et al., 2024; Hu et al., 2024) or VLMs (Zitkovich ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, a gap remains between the high-level visual observations and the low-level action spaces required to control real robots.

## Core Idea

- **p. 1 / 1 Introduction - extractive body cue:** In this work, we propose RynnVLA-001, a VLA model enhanced by video generation pretraining.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To ensure the smoothness and temporal coherence of predicted actions, we propose ActionVAE, a variational autoencoder that encodes action chunks into compact embeddings.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our framework leverages three types of training data: (1) Ego-Centric Video Generative Pretraining uses millions of ego-centric human manipulation videos for future frame prediction.
- **p. 4 / 3 METHODOLOGY - extractive body cue:** The training consists of three stages: (1) Ego-Centric Video Generative Pretraining trains a transformer-based Image-to-Video (I2V) model for future frame prediction.
- **p. 5 / 3 METHODOLOGY - extractive body cue:** To provide the model with proprioceptive information, we introduce state embeddings (blue blocks in Fig.
- **p. 4 / 3 METHODOLOGY - extractive body cue:** Stage1: language Encoder Decoder Action chunks decoded Action chunks Action Representation Learning via ActionVAE Transformer Stage2: language Transformer Human-Centric Trajectory-Aware Video Modeling Ego-Centric Video Generative ...
- **p. 6 / 3 METHODOLOGY - extractive body cue:** 2, the ActionVAE consists of an encoder that compresses an "action chunk" into a compact and continuous latent embedding, and a decoder that reconstructs the ...
- **p. 6 / 3 METHODOLOGY - extractive body cue:** During training, the model is optimized with two concurrent objectives: 1) Robot Action Prediction: The hidden state corresponding to the output of the <ACTION_PLACEHOLDER> token ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In a typical VLA setting, actions are predicted conditioned on current observations (e.g., visual inputs and robot states) and a language instruction. | image/video, language instruction, proprioception과 history | p. 4 (3 Methodology), p. 4 (3 Methodology) |
| State/latent | typical, VLA, setting, actions, predicted, conditioned, current, observations, visual, inputs, robot, states | language-grounded task state와 action-policy context | p. 4 (3 Methodology), p. 4 (3 Methodology), p. 2 (1 INTRODUCTION) |
| Output/action | 3) Robot-Centric Vision-Language-Action Modeling: The VLA model inherits the weights from the previous stages and is trained on robot data using language instructions and current observations (including two-view observations and joint s ... | continuous action, pose 또는 action chunk | p. 4 (3 Methodology), p. 2 (1 INTRODUCTION), p. 6 (3 METHODOLOGY) |
| Objective/outcome | During training, the model is optimized with two concurrent objectives: 1) Robot Action Prediction: The hidden state corresponding to the output of the <ACTION_PLACEHOLDER> token is fed into the newly initialized action ... | instruction following, task success, generalization과 latency | p. 6 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 6 (3 METHODOLOGY) |

## Main Claims and Actual Contribution

- **p. 1 / 1 Introduction - extractive body cue:** In this work, we propose RynnVLA-001, a VLA model enhanced by video generation pretraining.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To ensure the smoothness and temporal coherence of predicted actions, we propose ActionVAE, a variational autoencoder that encodes action chunks into compact embeddings.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our framework leverages three types of training data: (1) Ego-Centric Video Generative Pretraining uses millions of ego-centric human manipulation videos for future frame prediction.
- **p. 4 / 3 METHODOLOGY - extractive body cue:** The training consists of three stages: (1) Ego-Centric Video Generative Pretraining trains a transformer-based Image-to-Video (I2V) model for future frame prediction.
- **p. 5 / 3 METHODOLOGY - extractive body cue:** To provide the model with proprioceptive information, we introduce state embeddings (blue blocks in Fig.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** In contrast, RynnVLA-001-Video achieves a significant performance improvement, indicating that priors learned from ego-centric videos are effective for VLA adaptation.
- **p. 12 / 5 EXPERIMENTS - extractive body cue:** In contrast, our full RynnVLA-001 model, trained on our comprehensive dataset including distractors, achieves a 90% success rate (9/10) on this task.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** For Pi0, when distractor objects appear on the desk, the success rates drop significantly, indicating its limited instruction-following capability.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (5 EXPERIMENTS), p. 12 (5 EXPERIMENTS) |
| Embodiment/environment | To train and evaluate our proposed RynnVLA-001 model, we collect a new real-world manipulation dataset using a LeRobot SO100 robotic arm (Cadene et al., 2024). | hardware/simulator version and reset protocol | p. 7 (5 Experiments), p. 8 (5 EXPERIMENTS) |
| Dataset/benchmark | The dataset comprises expert demonstrations collected through human teleoperation. | role, split, size and leakage | p. 7 (5 Experiments), p. 8 (5 EXPERIMENTS), p. 7 (5 Experiments), p. 8 (5 EXPERIMENTS) |
| Metric | However, it exhibits a limited localization capability, capping its performance at a success rate of 50.0%. | definition, denominator, direction and uncertainty | p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Baseline/ablation | We compare our model with two strong open-source baselines, namely GR00T N1.5 (Bjorck et al., 2025a) and Pi0 (Black et al., 2024). | fair input/data/compute/action matching | p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 5 EXPERIMENTS - extractive body cue:** At a lower resolution of 256 × 256, the VQGAN's reconstruction quality degrades, the VQGAN fails to generate high-fidelity reconstructions, resulting in imprecise visual tokens ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** A trial is marked as a failure under any of the following conditions: 1) The time limit is exceeded.
- **p. 12 / 5 EXPERIMENTS - extractive body cue:** A total of 5 failure cases of the 10 trials consistently select a distractor object.
- **p. 12 / 5 EXPERIMENTS - extractive body cue:** However, when we elevate the front camera, altering the scene's projective geometry, the model fails to insert 12
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** 2) The model makes more than five consecutive failed attempts to grasp a target object.
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** This degradation is attributed to the resolution mismatch with the VQGAN component, which is pretrained exclusively on 512 × 512 images.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Another line of studies works on exploiting massive prior knowledge from pretrained generative models (Cheang et al., 2024; Hu et al., 2024) or VLMs (Zitkovich et al., 2023; Kim et al., 2024; ...를 문제로 두고, In this work, we propose RynnVLA-001, a VLA model enhanced by video generation pretraining.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 2 (1 INTRODUCTION), p. 1 (1 Introduction), p. 2 (1 INTRODUCTION), p. 4 (3 METHODOLOGY), p. 6 (3 METHODOLOGY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
