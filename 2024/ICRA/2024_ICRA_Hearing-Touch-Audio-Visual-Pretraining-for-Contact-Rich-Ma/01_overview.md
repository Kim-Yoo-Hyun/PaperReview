# Hearing Touch: Audio-Visual Pretraining for Contact-Rich Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2405.08576.
> PDF retrieval source: https://arxiv.org/pdf/2405.08576. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, tactile sensing, audio-visual pretraining, contact-rich manipulation
- Official paper: https://arxiv.org/abs/2405.08576
- Full-text retrieval: https://arxiv.org/pdf/2405.08576
- Code/Project: https://sites.google.com/view/hearing-touch
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 This gap arises due to the lack of relevant data at a comparable scale for tactile sensing.를 문제로 두고, Our method makes use of Audio-Visual Instance Discrimination (AVID) [14], a selfsupervised learning approach to learn audio-visual representations, pre-trained on Audioset [15], a dataset containing 1Robotics Institute, Carnegie Mellon ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Although pre-training on a large amount of data is beneficial for robot learning, current paradigms only perform large-scale pretraining for visual representations, whereas representations for ...
- **p. 1 / Abstract - extractive body cue:** In contrast to the abundance of visual data, it is unclear what relevant internet-scale data may be used for pretraining other modalities such as tactile ...
- **p. 1 / Abstract - extractive body cue:** Such pretraining becomes increasingly crucial in the low-data regimes common in robotics applications.
- **p. 1 / Abstract - extractive body cue:** In this paper, we address this gap by using contact microphones as an alternative tactile sensor.
- **p. 1 / Abstract - extractive body cue:** Our key insight is that contact microphones capture inherently audio-based information, allowing us to leverage large-scale audio-visual pretraining to obtain representations that boost the performance ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This gap arises due to the lack of relevant data at a comparable scale for tactile sensing.
- **p. 1 / I. INTRODUCTION - extractive body cue:** As a result, current approaches using non-visual sensory modalities are restricted to learning from a limited amount of task-specific data [10], [12].

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method makes use of Audio-Visual Instance Discrimination (AVID) [14], a selfsupervised learning approach to learn audio-visual representations, pre-trained on Audioset [15], a dataset containing ...
- **p. 3 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** Similar to [41], [42] our method is quasi open-loop-at time step t the policy predicts H steps of actions, of which h ≤H steps of ...
- **p. 3 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** Audio and Visual Representation Pretraining Our method uses large-scale audio-visual pre-training to initialize our audio encoder and large-scale visual pretraining to initialize our visual encoder.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Furthermore, our approach outperforms equivalent policies with audio encoders trained from scratch.
- **p. 2 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** We outline further details of our approach in the following sections.
- **p. 3 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** To isolate the effect of large-scale pre-training for our audio encoder, we use R3M [1], a proven method for pre-training visual features in robotic applications, ...
- **p. 3 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** We apply learned positional embeddings to each of the encoded representations and pass the result as input to a transformer decoder network similar to [6].
- **p. 2 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** Sensors At each timestep, we collect image observations vt and two-second clips of contact audio at.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Initializing our encoder with AVID weights, we train a policy with behavior cloning that fuses visual and audio inputs with self-attention in order to predict actions. | tactile image/force, vision과 proprioceptive history | p. 1 (I. INTRODUCTION), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING) |
| State/latent | Initializing, encoder, AVID, weights, train, policy, behavior, cloning, fuses, visual, audio, inputs | contact geometry, force state 또는 latent dynamics | p. 1 (I. INTRODUCTION), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING) |
| Output/action | This approach allows the policy to remain responsive to subtle changes in the audio input while encouraging temporal action consistency and mitigating the effect of non-Markovian behaviors such as pauses in demonstrations. | grasp/contact action, force command 또는 object motion | p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 2 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING) |
| Objective/outcome | We optimize the network to minimize the standard MSE loss ℓ= 1 H PH j=0(at+j-π(vt-i, . . . , vt, st)j)2. | slip/contact success, force/pose error와 robustness | p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method makes use of Audio-Visual Instance Discrimination (AVID) [14], a selfsupervised learning approach to learn audio-visual representations, pre-trained on Audioset [15], a dataset containing ...
- **p. 3 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** Similar to [41], [42] our method is quasi open-loop-at time step t the policy predicts H steps of actions, of which h ≤H steps of ...
- **p. 3 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** Audio and Visual Representation Pretraining Our method uses large-scale audio-visual pre-training to initialize our audio encoder and large-scale visual pretraining to initialize our visual encoder.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Furthermore, our approach outperforms equivalent policies with audio encoders trained from scratch.
- **p. 2 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** We outline further details of our approach in the following sections.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Flipping Scooping Zipping Success % Reward Success % Reward Success % Ours 50.0% 15.4 78.1% 8.9 88.9% BYOL-A 25.0% 2.3 25.0% 3.8 66.7% Scratch 15.4% ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: Success rates across methods and tasks. Our method, shown in blue, outperforms baselines in all but one setup of the zipping task. Furthermore, ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The results show that keeping the pre-trained audio encoder weights frozen during policy learning only slightly diminishes the performance of our method and still outperforms ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 4 (IV. EXPERIMENTS), p. 4 (Figure/Table caption) |
| Embodiment/environment | 2) Scaling Performance: We run evaluations on the scooping task for models trained with dataset sizes 50% (30 demos) and 150% (90 demos) of the original data after collecting more demonstrations. | hardware/simulator version and reset protocol | p. 5 (IV. EXPERIMENTS), p. 3 (IV. EXPERIMENTS) |
| Dataset/benchmark | We address these questions through real-world experiments on our setup described in Section IV-A by evaluating across three tasks (Section IV-B) and four methods (Section IV-C) in the low-data setting under conditions ... | role, split, size and leakage | p. 5 (IV. EXPERIMENTS), p. 3 (IV. EXPERIMENTS), p. 3 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Metric | The selfattention mechanism for fusing audio and visual features is crucial to attaining good performance; both the success rate and the average reward drop by nearly 50% when replacing the transformer with ... | definition, denominator, direction and uncertainty | p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Baseline/ablation | Our method, shown in blue, outperforms baselines in all but one setup of the zipping task. | fair input/data/compute/action matching | p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 6 / V. CONCLUSION - extractive body cue:** Future work may investigate which properties of pre-training datasets are most conducive to learning audio-visual representations for manipulation policies.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** As a result, the baselines suffer heavily from the domain shift and fail to generalize, often moving in jerk motions or away from the object ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Further, our method outperforms or matches the performance of all baselines in 8/9 tasks, displaying a lower variation in performance between different configurations of each ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Despite having access to the same information as our method, the BYOL-A and Scratch baselines fail to reason effectively over the audio and utilize the ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** This is more like the behavior of the training data than the baselines, which often fail to begin digging the spoon into the material as ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 This gap arises due to the lack of relevant data at a comparable scale for tactile sensing.를 문제로 두고, Our method makes use of Audio-Visual Instance Discrimination (AVID) [14], a selfsupervised learning approach to learn audio-visual representations, pre-trained on Audioset [15], a dataset containing 1Robotics Institute, Carnegie Mellon ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 2 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 2 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
