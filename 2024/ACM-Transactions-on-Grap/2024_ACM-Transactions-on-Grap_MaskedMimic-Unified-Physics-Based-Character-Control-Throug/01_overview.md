# MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://research.nvidia.com/labs/par/maskedmimic/.
> PDF retrieval source: https://research.nvidia.com/labs/par/maskedmimic/. Reading tracker status/evidence was not changed.

- Year/Venue: 2024 / ACM Transactions on Graphics
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, humanoid, whole-body control, motion imitation, NVIDIA
- Official paper: https://research.nvidia.com/labs/par/maskedmimic/
- Full-text retrieval: https://research.nvidia.com/labs/par/maskedmimic/
- Code/Project: https://research.nvidia.com/labs/par/maskedmimic/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 Prior works in physics-based simulation has addressed these challenges by developing specialized controllers for specific tasks such as locomotion, object interaction, and VR tracking.를 문제로 두고, Our framework consists of two stages.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 2 / 1 INTRODUCTION - extractive body cue:** The development of virtual characters capable of following dynamic user instructions and interacting with diverse scenes has been a significant challenge in computer graphics.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This challenge spans a wide range of applications, including gaming, digital humans, virtual reality, and many more.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** For instance, a character might be instructed to "Climb the hill to the castle, wave to the guard, go inside, navigate to the throne room, ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This scenario requires the integration of multiple complex behaviors: locomotion across uneven terrain, text-guided animation, and object interaction.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Prior works in physics-based simulation has addressed these challenges by developing specialized controllers for specific tasks such as locomotion, object interaction, and VR tracking.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** For example, a typical problem in VR is to generate full-body motion from only head and hands sensors.

## Core Idea

- **p. 4 / 3 PRELIMINARIES - extractive body cue:** Our framework consists of two stages.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Training on masked motion sequences enables the model to generalize to novel combinations of objectives.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We propose a framework that trains a versatile control model by leveraging the rich multi-modal information within existing motion capture datasets, such as kinematic trajectories, ...
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** We now review the fundamental concepts and notations behind our framework.
- **p. 5 / 3. Inference - extractive body cue:** 5 FULLY-CONSTRAINED CONTROLLER In the first stage of our framework, we train a fully-constrained motion tracking controller 𝜋FC using reinforcement learning.
- **p. 7 / 3. Inference - extractive body cue:** The decoder D(𝑎𝑡/𝑠𝑡,𝑧𝑡) is then conditioned on a latent sampled from the encoder's distribution, and produces an action for the simulated character.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** To train a versatile controller that can be directed using partial goals, we propose a simple training scheme that trains the controller on randomly masked ...
- **p. 8 / 3. Inference - extractive body cue:** The encoder and decoder are modeled as fully-connected networks, and observe a flattened concatenation of the input features.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (2) 𝑝(𝑠,𝑔/𝜋) denotes the distribution of states and goals observed under the student policy. | proprioception, reference pose/motion, visual or language command | p. 4 (3 PRELIMINARIES), p. 5 (3. Inference) |
| State/latent | denotes, distribution, states, goals, observed, under, student, policy, Character, Observations, step, observes | whole-body pose, balance/contact state와 skill/mode | p. 4 (3 PRELIMINARIES), p. 5 (3. Inference), p. 4 (3 PRELIMINARIES) |
| Output/action | Character Observations: At each step, 𝜋FC observes the current humanoid state 𝑠𝑡, consisting of the 3D body pose and velocity, canonicalized with respect to the character's local coordinate frame: 𝑠𝑡= (𝜃𝑡⊖𝜃root 𝑡 ... | joint/whole-body action, motion target 또는 task trajectory | p. 5 (3. Inference), p. 4 (3 PRELIMINARIES), p. 5 (3. Inference) |
| Objective/outcome | The agent's objective is to learn a policy that maximizes the discounted cumulative reward: 𝐽= E𝑝(𝜏/𝜋) " 𝑇 ∑︁ 𝑡=0 𝛾𝑡𝑟𝑡 # , (1) where 𝑝(𝜏/𝜋) = 𝑝(𝑠0)Π𝑇-1 𝑡=0 𝑝(𝑠𝑡+1/𝑠𝑡,𝑎𝑡)𝜋(𝑎𝑡/𝑠𝑡,𝑔𝑡) is the ... | tracking, balance, skill/task success와 recovery | p. 4 (3 PRELIMINARIES), p. 7 (3. Inference), p. 5 (3. Inference) |

## Main Claims and Actual Contribution

- **p. 4 / 3 PRELIMINARIES - extractive body cue:** Our framework consists of two stages.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Training on masked motion sequences enables the model to generalize to novel combinations of objectives.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We propose a framework that trains a versatile control model by leveraging the rich multi-modal information within existing motion capture datasets, such as kinematic trajectories, ...
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** We now review the fundamental concepts and notations behind our framework.
- **p. 5 / 3. Inference - extractive body cue:** 5 FULLY-CONSTRAINED CONTROLLER In the first stage of our framework, we train a fully-constrained motion tracking controller 𝜋FC using reinforcement learning.
- **p. 15 / 8 RESULTS - extractive body cue:** While MaskedMimic demonstrates high success rates in generating diverse motions, there are three notable areas for improvement in terms of motion quality.
- **p. 11 / 8 RESULTS - extractive body cue:** We attribute these performance improvements to our architecture and data augmentation techniques.
- **p. 9 / 7.2 Evaluation - extractive body cue:** For each tasks, we report a success rate metric and an error rate metric.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 15 (8 RESULTS), p. 11 (8 RESULTS) |
| Embodiment/environment | To evaluate the effectiveness of our framework, we construct a benchmark consisting of common tasks introduced by prior systems. | hardware/simulator version and reset protocol | p. 9 (7.2 Evaluation), p. 10 (7.2 Evaluation) |
| Dataset/benchmark | Additionally, MaskedMimic is designed to tackle a wide range of tasks across diverse scenes, which likely contributes to the model's enhanced generalization capabilities. | role, split, size and leakage | p. 9 (7.2 Evaluation), p. 10 (7.2 Evaluation), p. 11 (8 RESULTS), p. 12 (8 RESULTS) |
| Metric | We evaluate versions of the model with key components removed (Section 6), and measure the impact on the average success rate and error (i.e. average minimal distance from a valid sitting position ... | definition, denominator, direction and uncertainty | p. 14 (8 RESULTS), p. 9 (7.2 Evaluation), p. 11 (8 RESULTS) |
| Baseline/ablation | This test establishes the baseline capability for motion generation, both in terms of success rates and tracking quality, and allows comparison to prior systems for motion tracking. | fair input/data/compute/action matching | p. 10 (7.2 Evaluation), p. 10 (7.2 Evaluation), p. 11 (8 RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 15 / 8 RESULTS - extractive body cue:** 9 LIMITATIONS AND FUTURE WORK Although MaskedMimic presents a unified model for controlling physically simulated humanoids, there remains a number of limitations with our model.
- **p. 11 / 8 RESULTS - extractive body cue:** 2023, 2024], reducing the tracking failure rate on unseen motions by 62.5%.
- **p. 11 / 8 RESULTS - extractive body cue:** In addition to a lower failure rate, our controller also supports a wider range of motions, irregular terrains, and object interactions.
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3. The MaskedMimic framework: The first phase produces a fully- constrained controller 𝜋FC. This full-body tracker is trained using reinforce- ment learning to imitate ...
- **p. 15 / 8 RESULTS - extractive body cue:** We hypothesize that this limitation stems from the naive mapping of motions from flat to irregular terrains based on the root-to-floor distance normalization.
- **p. 14 / 8 RESULTS - extractive body cue:** Notably, MaskedMimic does not produce a single solution.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. Training scene (screenshot): The top region consists of standard flat terrain, enabling the controller to reproduce the original motions in a setting that ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 Prior works in physics-based simulation has addressed these challenges by developing specialized controllers for specific tasks such as locomotion, object interaction, and VR tracking.를 문제로 두고, Our framework consists of two stages.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (3 PRELIMINARIES), p. 7 (3. Inference), p. 4 (3 PRELIMINARIES), p. 8 (3. Inference) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
