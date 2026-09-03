# TactAlign: Human-to-Robot Policy Transfer via Tactile Alignment

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://roboticsconference.org/program/papers/6/.
> PDF retrieval source: https://roboticsconference.org/program/papers/6/. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, tactile, cross-embodiment, human-to-robot transfer, contact-rich manipulation, dexterity, representation alignment
- Official paper: https://roboticsconference.org/program/papers/6/
- Full-text retrieval: https://roboticsconference.org/program/papers/6/
- Code/Project: https://roboticsconference.org/program/papers/6/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 This strict pairing can be prohibitively difficult to maintain during contact-rich interactions involving sliding contact or dynamic object motion necessary for general manipulation.를 문제로 두고, Our method consists of two stages: self-supervised representation learning and cross-embodiment alignment via pseudo-pairs.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Human demonstrations collected by wearable devices (e.g., tactile gloves) provide fast and dexterous supervision for policy learning, and are guided by rich, natural tactile feedback.
- **p. 1 / Abstract - extractive body cue:** However, a key challenge is how to transfer humancollected tactile signals to robots despite the differences in sensing modalities and embodiment.
- **p. 1 / Abstract - extractive body cue:** Existing human-to-robot (H2R) approaches that incorporate touch often assume identical tactile sensors, require paired data, and involve little to no embodiment gap between human demonstrator ...
- **p. 1 / Abstract - extractive body cue:** We propose TactAlign, a crossembodiment tactile alignment method that transfers humancollected tactile signals to a robot with different embodiment.
- **p. 1 / Abstract - extractive body cue:** TactAlign transforms human and robot tactile observations into a shared latent representation using a rectified flow, without paired datasets, manual labels, or privileged information.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This strict pairing can be prohibitively difficult to maintain during contact-rich interactions involving sliding contact or dynamic object motion necessary for general manipulation.
- **p. 1 / I. INTRODUCTION - extractive body cue:** While effective, many of these approaches assume identical tactile sensors or little to no embodiment gap, which simplifies transfer but limits applicability across diverse robot ...

## Core Idea

- **p. 3 / III. METHODOLOGY - extractive body cue:** Our method consists of two stages: self-supervised representation learning and cross-embodiment alignment via pseudo-pairs.
- **p. 2 / I. INTRODUCTION - extractive body cue:** The core contributions of our work are: • We propose TactAlign, a method for aligning crosssensor tactile data from unpaired demonstrations of the same task.
- **p. 2 / I. INTRODUCTION - extractive body cue:** TactAlign leverages rectified flow with noisy pseudo-pairs to learn a latent mapping that enables H2R policy transfer between humans and robots equipped with heterogeneous tactile ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Second: We propose incorporating pseudo-pairs into rectified flow to guide the velocity field toward desired correspondences between the source and target distributions.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In contrast, our proposed method enables tactile transfer from unpaired datasets of the same task without requiring such pairing assumptions.
- **p. 3 / III. METHODOLOGY - extractive body cue:** We use a learnable length-1 query between the encoder and decoder to produce a fixed-dimensional latent representation via cross-attention pooling.
- **p. 3 / III. METHODOLOGY - extractive body cue:** A learnable length 1 query is implemented between the encoder and decoder to output a fixeddimensional latent representations after the cross-attention module.
- **p. 2 / III. METHODOLOGY - extractive body cue:** Problem Statement Our goal is to learn a latent-space mapping that transfers human tactile observations to robot tactile observations.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | However, most existing human-to-robot (H2R) approaches omit tactile feedback entirely and instead focus on transferring more readily available observations such as egocentric vision or state-action pairs in configuration space. | tactile image/force, vision과 proprioceptive history | p. 1 (I. INTRODUCTION), p. 2 (III. METHODOLOGY) |
| State/latent | However, most, existing, human-to-robot, H2R, approaches, omit, tactile, feedback, entirely, instead, focus | contact geometry, force state 또는 latent dynamics | p. 1 (I. INTRODUCTION), p. 2 (III. METHODOLOGY), p. 2 (I. INTRODUCTION) |
| Output/action | Problem Statement Our goal is to learn a latent-space mapping that transfers human tactile observations to robot tactile observations. | grasp/contact action, force command 또는 object motion | p. 2 (III. METHODOLOGY), p. 2 (I. INTRODUCTION), p. 4 (III. METHODOLOGY) |
| Objective/outcome | In step2, we aggregate the learned latents from both domains to construct pseudo-pairs (h∗, r∗), and learn a velocity field vθ that transports the glove latent distribution to the robot latent distribution. ... | slip/contact success, force/pose error와 robustness | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |

## Main Claims and Actual Contribution

- **p. 3 / III. METHODOLOGY - extractive body cue:** Our method consists of two stages: self-supervised representation learning and cross-embodiment alignment via pseudo-pairs.
- **p. 2 / I. INTRODUCTION - extractive body cue:** The core contributions of our work are: • We propose TactAlign, a method for aligning crosssensor tactile data from unpaired demonstrations of the same task.
- **p. 2 / I. INTRODUCTION - extractive body cue:** TactAlign leverages rectified flow with noisy pseudo-pairs to learn a latent mapping that enables H2R policy transfer between humans and robots equipped with heterogeneous tactile ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Second: We propose incorporating pseudo-pairs into rectified flow to guide the velocity field toward desired correspondences between the source and target distributions.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In contrast, our proposed method enables tactile transfer from unpaired datasets of the same task without requiring such pairing assumptions.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 8: Lid Closing Task. With randomized grasps, the policy uses touch to perform search, alignment, and closing between the lid and the bottle. We ...
- **p. 5 / IV. EXPERIMENTS AND RESULTS - extractive body cue:** Successful execution therefore depends on detecting contact onset and reasoning about contact throughout the task as in Fig.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 5 (IV. EXPERIMENTS AND RESULTS) |
| Embodiment/environment | The dataset includes 1,472 robot force samples (24:1 train:test split) and 1,527 human force samples used only for evaluation. | hardware/simulator version and reset protocol | p. 5 (IV. EXPERIMENTS AND RESULTS), p. 5 (IV. EXPERIMENTS AND RESULTS) |
| Dataset/benchmark | Robot demonstrations are collected using Xela sensors Action Sequence Transformer Decoder Attentive Pooling ... ... | role, split, size and leakage | p. 5 (IV. EXPERIMENTS AND RESULTS), p. 5 (IV. EXPERIMENTS AND RESULTS), p. 4 (IV. EXPERIMENTS AND RESULTS), p. 4 (IV. EXPERIMENTS AND RESULTS) |
| Metric | Fig. 10: ℓ1 force prediction error (mean ± std) along each axis, averaged over five evaluations. G →R evaluates force prediction on the robot using human tactile signals, with (blue) and without ... | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 5 (IV. EXPERIMENTS AND RESULTS) |
| Baseline/ablation | Fig. 10: ℓ1 force prediction error (mean ± std) along each axis, averaged over five evaluations. G →R evaluates force prediction on the robot using human tactile signals, with (blue) and without ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / V. LIMITATION - extractive body cue:** Moreover, tactile alignment alone does not address visual discrepancies between human and robot embodiments.
- **p. 8 / V. LIMITATION - extractive body cue:** Incorporating vision and other modalities into a unified multi-modal policy is also an important direction for future work.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Red and blue indicate two subsets of the source distribution. The left side of each of the three panels shows the provided training ...
- **p. 5 / IV. EXPERIMENTS AND RESULTS - extractive body cue:** We use Manus glove [25] with OSMO tactile sensors [45] for robust hand pose estimation under visual occlusions from the lamp shade and light bulb.
- **p. 5 / IV. EXPERIMENTS AND RESULTS - extractive body cue:** We record fingertip poses only, as the Manus glove does not provide wrist pose information.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 8: Lid Closing Task. With randomized grasps, the policy uses touch to perform search, alignment, and closing between the lid and the bottle. We ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 This strict pairing can be prohibitively difficult to maintain during contact-rich interactions involving sliding contact or dynamic object motion necessary for general manipulation.를 문제로 두고, Our method consists of two stages: self-supervised representation learning and cross-embodiment alignment via pseudo-pairs.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** This strict pairing can be prohibitively difficult to maintain during contact-rich interactions involving sliding contact or dynamic object motion necessary for general manipulation. (p. 1, I. INTRODUCTION).
- **Actual contribution:** The core contributions of our work are: • We propose TactAlign, a method for aligning crosssensor tactile data from unpaired demonstrations of the same task. (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** The dataset includes 1,472 robot force samples (24:1 train:test split) and 1,527 human force samples used only for evaluation. (p. 5, IV. EXPERIMENTS AND RESULTS).
- **Explicit failure boundary:** Without alignment, the success rate is also 0%, with failures primarily arising from jamming, from which the policy cannot recover, often leading to complete unscrewing of the light bulb. (p. 7, 8. The pivoting and insertion).
