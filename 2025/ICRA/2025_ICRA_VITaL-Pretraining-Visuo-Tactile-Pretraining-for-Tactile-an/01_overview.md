# VITaL Pretraining: Visuo-Tactile Pretraining for Tactile and Non-Tactile Manipulation Policies

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf.
> PDF retrieval source: https://arxiv.org/pdf/2403.11898v2. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics
- Official paper: https://www.proceedings.com/content/081/081087webtoc.pdf
- Full-text retrieval: https://arxiv.org/pdf/2403.11898v2
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 tactile 문제를 이해하기 위해 읽는다. 본문은 Achieving proficiency in complex manipulation tasks remains a longstanding challenge in robotics, with applications ranging from industrial automation to clay sculpting [1], [2].를 문제로 두고, Next, we propose a new methodology for using tactile data in imitation learning: VITaL (Vison-only Imitation using Tactile Latent) pretraining, in which we discard the tactile encoder and use the pretrained vision ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Tactile information is a critical tool for dexterous manipulation.
- **p. 1 / Abstract - extractive body cue:** As humans, we rely heavily on tactile information to understand objects in our environments and how to interact with them.
- **p. 1 / Abstract - extractive body cue:** We use touch not only to perform manipulation tasks but also to learn how to perform these tasks.
- **p. 1 / Abstract - extractive body cue:** Therefore, to create robotic agents that can learn to complete manipulation tasks at a human or super-human level of performance, we need to properly incorporate ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we investigate how we can incorporate tactile information into imitation learning platforms to improve performance on manipulation tasks.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Achieving proficiency in complex manipulation tasks remains a longstanding challenge in robotics, with applications ranging from industrial automation to clay sculpting [1], [2].
- **p. 1 / I. INTRODUCTION - extractive body cue:** Critical to addressing this challenge is the integration of tactile information, which provides both an understanding of the objects being interacted with and a detailed ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** Next, we propose a new methodology for using tactile data in imitation learning: VITaL (Vison-only Imitation using Tactile Latent) pretraining, in which we discard the ...
- **p. 3 / III. METHODS - extractive body cue:** A vision projection head, pϕV : Z →L, and a tactile projection head, qϕT : Z, P →L, each of which consists of a single ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our primary contribution is a pretraining strategy for these SOTA imitation learning frameworks, leveraging the multimodal nature of our data to incorporate a temporalbased visual-tactile ...
- **p. 4 / III. METHODS - extractive body cue:** 2) Diffusion Policy: Our approach to diffusion policy was based on the implementation by [11] that generates action sequences conditioned on observations with DDPM.
- **p. 4 / III. METHODS - extractive body cue:** We used the Oculus Virtual Reality (VR) teleoperation pipeline developed by [38], which tracks the Quest's controller using the headset.
- **p. 3 / III. METHODS - extractive body cue:** First, we replaced the stock Resnet vision encoder with the vision encoder from the contrastive pretraining step and added a separate tactile encoder (also from ...
- **p. 2 / 1) Action - extractive body cue:** Chunking Transformers: Action Chunking Transformers (ACT) [10] train a Conditional Variational Auto Encoder (CVAE) built upon a transformer backbone to predict a series of actions ...
- **p. 2 / 1) Action - extractive body cue:** 2) Diffusion Policy: To address the challenge of complex multi-modal action spaces, Diffusion Policy [11] formulates control policies as Denoising Diffusion Probabilistic Models (DDPM) [35], ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Chunking Transformers: Action Chunking Transformers (ACT) [10] train a Conditional Variational Auto Encoder (CVAE) built upon a transformer backbone to predict a series of actions (in the form of goal positions) conditioned ... | tactile image/force, vision과 proprioceptive history | p. 2 (1) Action), p. 4 (III. METHODS) |
| State/latent | Chunking, Transformers, Action, ACT, train, Conditional, Variational, Auto, Encoder, CVAE, built, upon | contact geometry, force state 또는 latent dynamics | p. 2 (1) Action), p. 4 (III. METHODS), p. 2 (1) Action) |
| Output/action | 2) Diffusion Policy: Our approach to diffusion policy was based on the implementation by [11] that generates action sequences conditioned on observations with DDPM. | grasp/contact action, force command 또는 object motion | p. 4 (III. METHODS), p. 2 (1) Action), p. 1 (I. INTRODUCTION) |
| Objective/outcome | The encoders (and the projection heads) are then trained to maximize the cross-modality dot-product similarity of latent representations from the same scene while minimizing the crossmodality similarity of latent representations from di ... | slip/contact success, force/pose error와 robustness | p. 3 (III. METHODS), p. 2 (1) Action), p. 3 (III. METHODS) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** Next, we propose a new methodology for using tactile data in imitation learning: VITaL (Vison-only Imitation using Tactile Latent) pretraining, in which we discard the ...
- **p. 3 / III. METHODS - extractive body cue:** A vision projection head, pϕV : Z →L, and a tactile projection head, qϕT : Z, P →L, each of which consists of a single ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our primary contribution is a pretraining strategy for these SOTA imitation learning frameworks, leveraging the multimodal nature of our data to incorporate a temporalbased visual-tactile ...
- **p. 4 / III. METHODS - extractive body cue:** 2) Diffusion Policy: Our approach to diffusion policy was based on the implementation by [11] that generates action sequences conditioned on observations with DDPM.
- **p. 4 / III. METHODS - extractive body cue:** We used the Oculus Virtual Reality (VR) teleoperation pipeline developed by [38], which tracks the Quest's controller using the headset.
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** This is significantly higher than the 20% and 45% success rates that learning from vision only with ACT and diffusion policy (respectively) achieves.
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** In all block stacking experiments, as with cable plugging, we observed that visuo-tactile pretraining improved performance for both visuo-tactile and vision-only agents, and that a ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 7. Success rate for our experiment tasks. All experiments were run 20 times, with the total success rate shown. The use of visuo-tactile pretraining ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Embodiment/environment | In this task, the robot has to navigate to a USB cable, unplug it from its holder, and plug it into the last port of a USB hub. | hardware/simulator version and reset protocol | p. 5 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION) |
| Dataset/benchmark | For both pretrained and non-pretrained tactileonly diffusion policies, the robot would pick up the USB cable, but then would alternate between trying to move back to the USB holder, trying to move ... | role, split, size and leakage | p. 5 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Metric | Comparing the two imitation learning methods, we found that Diffusion Policy's success rate was less sensitive than ACT, with a higher accuracy for the non-pretrained visiononly policy (where ACT did quite poorly), ... | definition, denominator, direction and uncertainty | p. 5 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Baseline/ablation | Interestingly, the nonpretrained ACT model outperformed the pretrained model in this task. | fair input/data/compute/action matching | p. 5 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION) |

## Explicit Limitations and Failure Boundary

- **p. 6 / V. CONCLUSIONS - extractive body cue:** A major limitation of this work is that task-specific data was used for pretraining.
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** Although this is relatively small in absolute terms, it corresponds to a 50% and 20% decrease in failures for ACT and Diffusion Policy, respectively.
- **p. 6 / V. CONCLUSIONS - extractive body cue:** Evaluating this alternative approach is left for future work.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. Imitation learning networks. ACT (left) is trained as an autoencoder, predicting a sequence of actions at each timestep (at). At inference, the latent ...
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** To increase the task's difficulty, we added random noise with a standard deviation of 2.5mm to the agent's actions during inference.

## Why Read It

VLA and generalist robot policies의 tactile 문제를 이해하기 위해 읽는다. 본문은 Achieving proficiency in complex manipulation tasks remains a longstanding challenge in robotics, with applications ranging from industrial automation to clay sculpting [1], [2].를 문제로 두고, Next, we propose a new methodology for using tactile data in imitation learning: VITaL (Vison-only Imitation using Tactile Latent) pretraining, in which we discard the tactile encoder and use the pretrained vision ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. METHODS), p. 3 (III. METHODS), p. 2 (1) Action), p. 2 (1) Action) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
