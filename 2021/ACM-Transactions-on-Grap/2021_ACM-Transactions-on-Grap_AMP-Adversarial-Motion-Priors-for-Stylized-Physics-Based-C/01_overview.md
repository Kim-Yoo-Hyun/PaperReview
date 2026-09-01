# AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://doi.org/10.1145/3450626.3459670.
> PDF retrieval source: https://doi.org/10.1145/3450626.3459670. Reading tracker status/evidence was not changed.

- Year/Venue: 2021 / ACM Transactions on Graphics
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: CORE
- Tags: Robotics, humanoid, Reinforcement Learning, motion imitation, whole-body control
- Official paper: https://doi.org/10.1145/3450626.3459670
- Full-text retrieval: https://doi.org/10.1145/3450626.3459670
- Code/Project: https://xbpeng.github.io/projects/AMP/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 However, it can be exceptionally difficult to design a style-reward 𝑟𝑆 that leads a character to learn naturalistic behaviors, or behaviors that conform to a particular style.를 문제로 두고, The central contribution of this work is an adversarial learning approach for physics-based character animation that combines goalconditioned reinforcement with an adversarial motion prior, which enables the style of a character's movem ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 INTRODUCTION - extractive body cue:** Synthesizing natural and life-like motions for virtual characters is a crucial element for breathing life into immersive experiences, such as films and games.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The demand for realistic motions becomes even more apparent for VR applications, where users are provided with rich modalities through which to interact with virtual ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Developing control strategies that are able to replicate the properties of naturalistic behaviors is also of interest for robotic systems, as natural motions implicitly encode ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** While examples of natural motions are commonplace, identifying the underlying characteristics that constitute these behaviors is nonetheless challenging, and more difficult still to replicate in ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** So what are the characteristics that constitute natural and lifelike behaviors?
- **p. 5 / 4 BACKGROUND - extractive body cue:** However, it can be exceptionally difficult to design a style-reward 𝑟𝑆 that leads a character to learn naturalistic behaviors, or behaviors that conform to a ...
- **p. 5 / 4 BACKGROUND - extractive body cue:** However, this loss tends to lead to optimization challenges due to vanishing gradients as the sigmoid function saturates, which can hamper training of the policy ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** The central contribution of this work is an adversarial learning approach for physics-based character animation that combines goalconditioned reinforcement with an adversarial motion prior, which ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We present one of the first adversarial learning systems that is able to produce high-quality full-body motions for physically simulated characters.
- **p. 5 / 4 BACKGROUND - extractive body cue:** We propose to model the style-reward with a learned discriminator, which we refer to as an adversarial motion prior (AMP), by analogy to the adversarial ...
- **p. 6 / 4 BACKGROUND - extractive body cue:** 6.1 States and Actions The state s𝑡consists of a set of features that describes the configuration of the character's body.
- **p. 7 / 4 BACKGROUND - extractive body cue:** 7 TASKS To evaluate AMP's effectiveness for controlling the style of a character's motions, we apply our framework to train complex 3D simulated characters to ...
- **p. 7 / 4 BACKGROUND - extractive body cue:** 6.2 Network Architecture Each policy 𝜋is modeled by a neural network that maps a given state s𝑡and goal g to a Gaussian distribution over actions ...
- **p. 4 / 4 BACKGROUND - extractive body cue:** At each time step 𝑡, the agent observes the state s𝑡∈S of the system, then samples an action a𝑡∈A from a policy a𝑡∼𝜋(a𝑡/s𝑡, g).
- **p. 4 / 4 BACKGROUND - extractive body cue:** GAIL addresses some of the limitations of behavioral cloning by learning an objective function that measures the similarity between the policy and the demonstrations, and ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 6.2 Network Architecture Each policy 𝜋is modeled by a neural network that maps a given state s𝑡and goal g to a Gaussian distribution over actions 𝜋(a𝑡/s𝑡, g) = N (𝜇(s𝑡, g), Σ), ... | proprioception, reference pose/motion, visual or language command | p. 7 (4 BACKGROUND), p. 4 (4 BACKGROUND) |
| State/latent | Network, Architecture, policy, modeled, neural, maps, given, state, goal, Gaussian, distribution, over | whole-body pose, balance/contact state와 skill/mode | p. 7 (4 BACKGROUND), p. 4 (4 BACKGROUND), p. 5 (4 BACKGROUND) |
| Output/action | Behavioral cloning can be used to directly fit a policy to map from states observed in M to their corresponding actions using supervised learning [Bojarski et al. | joint/whole-body action, motion target 또는 task trajectory | p. 4 (4 BACKGROUND), p. 5 (4 BACKGROUND), p. 4 (4 BACKGROUND) |
| Objective/outcome | 5.2 Least-Squares Discriminator The standard GAN objective detailed in Equation 5 typically uses a sigmoid cross-entropy loss function. | tracking, balance, skill/task success와 recovery | p. 5 (4 BACKGROUND), p. 5 (4 BACKGROUND), p. 4 (4 BACKGROUND) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** The central contribution of this work is an adversarial learning approach for physics-based character animation that combines goalconditioned reinforcement with an adversarial motion prior, which ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We present one of the first adversarial learning systems that is able to produce high-quality full-body motions for physically simulated characters.
- **p. 5 / 4 BACKGROUND - extractive body cue:** We propose to model the style-reward with a learned discriminator, which we refer to as an adversarial motion prior (AMP), by analogy to the adversarial ...
- **p. 6 / 4 BACKGROUND - extractive body cue:** 6.1 States and Actions The state s𝑡consists of a set of features that describes the configuration of the character's body.
- **p. 7 / 4 BACKGROUND - extractive body cue:** 7 TASKS To evaluate AMP's effectiveness for controlling the style of a character's motions, we apply our framework to train complex 3D simulated characters to ...
- **p. 9 / 8 RESULTS - extractive body cue:** Training the motion prior with a diverse dataset results in more flexible and optimal policies that are able to achieve a wider range of target ...
- **p. 10 / 8 RESULTS - extractive body cue:** Our method achieves comparable performance across the various tasks, while also producing higher fidelity motions. order to fulfill the high-level task objectives.
- **p. 9 / 8 RESULTS - extractive body cue:** As a result, these policies are not able to achieve the faster target speeds.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 9 (8 RESULTS), p. 10 (8 RESULTS) |
| Embodiment/environment | Each environment is denoted by "Character: Task (Dataset)". | hardware/simulator version and reset protocol | p. 8 (8 RESULTS), p. 9 (8 RESULTS) |
| Dataset/benchmark | Policies trained using the larger Locomotion dataset is able to more closely follow the various target speeds by imitating different gaits. our policies can in large part be attributed to the motion ... | role, split, size and leakage | p. 8 (8 RESULTS), p. 9 (8 RESULTS), p. 9 (8 RESULTS), p. 12 (8 RESULTS) |
| Metric | Since AMP does not use a phase variable to synchronize the policy with the reference motion, the motions may progress at different rates, resulting in de-synchronization that can lead to large pose ... | definition, denominator, direction and uncertainty | p. 11 (8 RESULTS), p. 11 (8 RESULTS), p. 18 (Figure/Table caption) |
| Baseline/ablation | AMP produces results of comparable quality when compared to prior tracking-based methods, without requiring a manually designed reward function or synchronization between the policy and reference motion. | fair input/data/compute/action matching | p. 12 (8 RESULTS), p. 10 (8 RESULTS), p. 7 (8 RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 8 RESULTS - extractive body cue:** These additional motion clips then enable our character to recover from a fall and continue to perform a given task (Figure 3(c)).
- **p. 9 / 8 RESULTS - extractive body cue:** When the character falls forward, it tucks its body into a roll during the fall in order to more quickly transition into a getup behavior.
- **p. 11 / 8 RESULTS - extractive body cue:** However, for some motions, such as the Front-Flip, AMP is prone to converging to locally optimal behaviors, where instead of performing a flip, the character ...
- **p. 12 / 8 RESULTS - extractive body cue:** 9 DISCUSSION AND LIMITATIONS In this work, we presented an adversarial learning system for physicsbased character animation that enables characters to imitate diverse behaviors from ...
- **p. 11 / 8 RESULTS - extractive body cue:** Unlike previous motion tracking methods, our approach does not require a manually designed tracking objective or a phase-based synchronization of the reference motion and the ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 However, it can be exceptionally difficult to design a style-reward 𝑟𝑆 that leads a character to learn naturalistic behaviors, or behaviors that conform to a particular style.를 문제로 두고, The central contribution of this work is an adversarial learning approach for physics-based character animation that combines goalconditioned reinforcement with an adversarial motion prior, which enables the style of a character's movem ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 5 (4 BACKGROUND), p. 5 (4 BACKGROUND), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 7 (4 BACKGROUND) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
