# Strengthening Generative Robot Policies through Predictive World Modeling

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=0.875); canonical paper source: https://computationalrobotics.seas.harvard.edu/GPC/.
> PDF retrieval source: https://arxiv.org/pdf/2502.00622. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RA-L
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: Robotics, world model, diffusion policy, model-based planning, contact-rich manipulation
- Official paper: https://computationalrobotics.seas.harvard.edu/GPC/
- Full-text retrieval: https://arxiv.org/pdf/2502.00622
- Code/Project: https://computationalrobotics.seas.harvard.edu/GPC/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=0.875)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 However, some tasks involve rewards that are difficult or even infeasible to specify.를 문제로 두고, GPC consists of three components: • Generative policy training.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present generative predictive control (GPC), a framework for inference-time enhancement of pretrained behavior-cloning policies.
- **p. 1 / Abstract - extractive body cue:** Rather than retraining or fine-tuning, GPC augments a frozen diffusion policy at deployment by coupling it with a predictive world model.
- **p. 1 / Abstract - extractive body cue:** Concretely, we train an action-conditioned world model on expert demonstrations and random exploration rollouts to forecast the consequences of action proposals produced by the diffusion ...
- **p. 1 / Abstract - extractive body cue:** This combination of a generative prior with predictive foresight enables test-time adaptation.
- **p. 1 / Abstract - extractive body cue:** Across diverse robotic manipulation tasks-state- and visionbased, in simulation and on real hardware-GPC consistently outperforms standard behavior cloning and compares favorably to other inference-time adaptation ...
- **p. 3 / III. OVERVIEW OF GENERATIVE PREDICTIVE CONTROL - extractive body cue:** However, some tasks involve rewards that are difficult or even infeasible to specify.
- **p. 1 / B EHAVIOR cloning (BC) with generative models has - extractive body cue:** Lacking explicit mechanisms for test-time correction or recovery, small deviations from the training distribution can compound over time and degrade performance [5].

## Core Idea

- **p. 1 / B EHAVIOR cloning (BC) with generative models has - extractive body cue:** GPC consists of three components: • Generative policy training.
- **p. 1 / Abstract - extractive body cue:** We present generative predictive control (GPC), a framework for inference-time enhancement of pretrained behavior-cloning policies.
- **p. 3 / III. OVERVIEW OF GENERATIVE PREDICTIVE CONTROL - extractive body cue:** In contrast, GPC-OPT enables continuous action refinement by performing gradientbased optimization from diffusion-policy warm starts, allowing it to improve beyond sampled proposals.
- **p. 4 / V. EXPERIMENTS - extractive body cue:** We further provide ablations and comparisons to illustrate: (i) the influence of K and M on performance, and (ii) how GPC compares with other baselines ...
- **p. 1 / B EHAVIOR cloning (BC) with generative models has - extractive body cue:** We propose generative predictive control (GPC), a framework that strengthens pretrained diffusion-based BC policies at inference time by coupling them with an action-conditioned predictive world ...
- **p. 4 / IV. WORLD MODEL LEARNING - extractive body cue:** We use observation horizon H = 4 in the visual world modeling, and Nd = 3 diffusion steps.
- **p. 4 / IV. WORLD MODEL LEARNING - extractive body cue:** We use the same architecture for Dϕ as [42], containing convolutions, action embedding, and a U-Net (Fig.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | From expert demonstrations, we train a diffusion-based policy that generates shorthorizon action chunks conditioned on past observations, providing a generative prior over plausible behaviors. • Predictive world modeling. | observation, uncertainty/risk estimate와 task command | p. 1 (B EHAVIOR cloning (BC) with generative models has), p. 3 (III. OVERVIEW OF GENERATIVE PREDICTIVE CONTROL) |
| State/latent | expert, demonstrations, train, diffusion-based, policy, generates, shorthorizon, action, chunks, conditioned, past, observations | safe set, recovery state 또는 constraint margin | p. 1 (B EHAVIOR cloning (BC) with generative models has), p. 3 (III. OVERVIEW OF GENERATIVE PREDICTIVE CONTROL), p. 3 (III. OVERVIEW OF GENERATIVE PREDICTIVE CONTROL) |
| Output/action | Policy learning then reduces to supervised learning with input It and output at:t+T . | shielded, recovery 또는 safe action | p. 3 (III. OVERVIEW OF GENERATIVE PREDICTIVE CONTROL), p. 3 (III. OVERVIEW OF GENERATIVE PREDICTIVE CONTROL), p. 4 (IV. WORLD MODEL LEARNING) |
| Objective/outcome | While GPC is related to inference-time planning methods that enhance frozen policies via imagined rollouts in learned world models [8], [9], it is distinguished by combining a diffusion policy with an explicit, ... | task return과 violation/failure probability | p. 1 (B EHAVIOR cloning (BC) with generative models has), p. 4 (IV. WORLD MODEL LEARNING), p. 1 (B EHAVIOR cloning (BC) with generative models has) |

## Main Claims and Actual Contribution

- **p. 1 / B EHAVIOR cloning (BC) with generative models has - extractive body cue:** GPC consists of three components: • Generative policy training.
- **p. 1 / Abstract - extractive body cue:** We present generative predictive control (GPC), a framework for inference-time enhancement of pretrained behavior-cloning policies.
- **p. 3 / III. OVERVIEW OF GENERATIVE PREDICTIVE CONTROL - extractive body cue:** In contrast, GPC-OPT enables continuous action refinement by performing gradientbased optimization from diffusion-policy warm starts, allowing it to improve beyond sampled proposals.
- **p. 4 / V. EXPERIMENTS - extractive body cue:** We further provide ablations and comparisons to illustrate: (i) the influence of K and M on performance, and (ii) how GPC compares with other baselines ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** The results show that (a) GPC-RANK improves performance by ∼10% over the behavior cloning baseline; (b) GPC-OPT yields a ∼15% gain; and (c) GPC-RANK+OPT achieves ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Planning-only methods without a generative policy prior, including model predictive path integral (MPPI), cross-entropy method (CEM), and pure gradient ascent [35], achieve substantially lower performance ...
- **p. 4 / V. EXPERIMENTS - extractive body cue:** In all cases, GPC consistently outperforms the behavior cloning baseline, highlighting its effectiveness as an inference-time enhancement.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Clearly, all GPCRANK, GPC-OPT, and GPC-RANK+OPT variants outperform pure behavior cloning.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Embodiment/environment | We evaluate GPC on (1) a state-based planar pushing task, (2) four vision-based simulation tasks, and (3) two real-world manipulation tasks. | hardware/simulator version and reset protocol | p. 4 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Dataset/benchmark | We study the planar pushing task with the goal of pushing an object from an initial pose to a specified target pose, where the groundtruth pose of the object is available through ... | role, split, size and leakage | p. 4 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Metric | Planning-only methods without a generative policy prior, including model predictive path integral (MPPI), cross-entropy method (CEM), and pure gradient ascent [35], achieve substantially lower performance on vision-based Push-T, with su ... | definition, denominator, direction and uncertainty | p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Baseline/ablation | In all cases, GPC consistently outperforms the behavior cloning baseline, highlighting its effectiveness as an inference-time enhancement. | fair input/data/compute/action matching | p. 4 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 4 / IV. WORLD MODEL LEARNING - extractive body cue:** Without freezing the noise, GPC-OPT fails, as stochastic gradients destabilize the reward optimization in (4).
- **p. 4 / IV. WORLD MODEL LEARNING - extractive body cue:** Dϕ is trained by adding random noises to the clean images and then predicting the noise.

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 However, some tasks involve rewards that are difficult or even infeasible to specify.를 문제로 두고, GPC consists of three components: • Generative policy training.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (III. OVERVIEW OF GENERATIVE PREDICTIVE CONTROL), p. 1 (B EHAVIOR cloning (BC) with generative models has), p. 4 (IV. WORLD MODEL LEARNING), p. 1 (Abstract), p. 3 (III. OVERVIEW OF GENERATIVE PREDICTIVE CONTROL), p. 1 (B EHAVIOR cloning (BC) with generative models has) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
