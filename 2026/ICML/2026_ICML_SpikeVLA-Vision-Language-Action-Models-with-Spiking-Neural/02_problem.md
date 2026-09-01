# Problem - SpikeVLA: Vision-Language-Action Models with Spiking Neural Networks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=W86R5sIsxE; PDF retrieval source: https://openreview.net/pdf/27ac3094b9d6afc1c8c39e0ae99418fd937e0219.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction)): To address this challenge, previous work has explored efficiency-oriented designs.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Vision-Language-Action (VLA) models have become a dominant paradigm for embodied intelligence.
- **p. 1 / Abstract - extractive PDF cue:** However, most existing approaches are built on large-scale transformers, resulting in substantial inference latency and energy consumption that limit their practical deployment in low-power, real-time ...
- **p. 1 / Abstract - extractive PDF cue:** We propose SpikeVLA, a spiking VLA architecture for embodied navigation with energy-efficient inference, consisting of three key components.
- **p. 1 / Abstract - extractive PDF cue:** (i) A spiking vision encoder, Spike-V, that replaces dense continuous layers with event-driven spiking layers to reduce the energy consumption of visual representation learning.
- **p. 1 / Abstract - extractive PDF cue:** (ii) A multi-modal spiking large language model, Spike-L, that reformulates cross-modal reasoning with spiking dynamics and token-level event-driven sparsity to further lower computational cost.
- **p. 1 / 1. Introduction - extractive PDF cue:** To address this challenge, previous work has explored efficiency-oriented designs.
- **p. 2 / 1. Introduction - extractive PDF cue:** To address these challenges, we propose SpikeVLA, the first VLA architecture built on spiking neural networks, which represents a trade-off between performance and efficiency, as ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | To address this challenge, previous work has explored efficiency-oriented designs. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | At timestep t, the actor maps the observation st to a policy πθ(· / st) = N(µt, σt) and samples an action ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | timestep, actor, maps, observation, policy, samples, action, while, critic, estimates | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Decoder, parameters, updated, independently, output, populations, corresponding, action | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: timestep, actor, maps, observation, policy, samples, action, while, critic, estimates | p. 6 (3.4. Spiking Neural Network for Action Policy), p. 5 (3.4. Spiking Neural Network for Action Policy), p. 6 (3.4. Spiking Neural Network for Action Policy) |
| Decision / output variable | action, pose, option or chunk a; body terms: SpikeVLA, consists, three, complementary, modules, first, VLA, framework | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Spike Neural Network Vision Encoder) |
| Objective / loss / cost | policy/action modeling objective; cue terms: optimize, policy, maximizing, clipped, surrogate, objective, Equation, specifies | p. 4 (3.2. Spike Neural Network Vision Encoder), p. 4 (3.2. Spike Neural Network Vision Encoder), p. 3 (3.1. Architecture), p. 6 (3.4. Spiking Neural Network for Action Policy), p. 6 (3.4. Spiking Neural Network for Action Policy), p. 3 (3.2. Spike Neural Network Vision Encoder) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3.1. Architecture), p. 3 (3.1. Architecture), p. 6 (3.4. Spiking Neural Network for Action Policy) |
| Success / guarantee | instruction-conditioned task success | p. 6 (4.1. Experimental Setups), p. 15 (Figure/Table caption), p. 7 (4.2. Main Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** To address these challenges, we propose SpikeVLA, the first VLA architecture built on spiking neural networks, which represents a trade-off between performance and efficiency, as ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Spike Neural Network Vision Encoder), p. 3 (3.1. Architecture), p. 4 (3.2. Spike Neural Network Vision Encoder)): SpikeVLA consists of three complementary modules.

- **p. 2 / 1. Introduction - extractive PDF cue:** 1) We propose SpikeVLA, the first VLA framework built on spiking neural networks.
- **p. 3 / 3.2. Spike Neural Network Vision Encoder - extractive PDF cue:** We propose an SNN-based visual encoder that fuses the current frame with history frames to provide temporal context for time-dependent VLA tasks.
- **p. 3 / 3.1. Architecture - extractive PDF cue:** We propose SpikeVLA, an end-to-end spiking VLA architecture for embodied navigation, consisting of a spiking vision encoder (Spike-V), a multimodal spiking language model (Spike-L), and ...
- **p. 4 / 3.2. Spike Neural Network Vision Encoder - extractive PDF cue:** Building on differential coding, we introduce differential spiking neurons and perform unified differential conversion of linear and nonlinear operators in SigLIPv2, thereby obtaining a spiking ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | For low-level locomotion, we quantify command tracking and safety using linear and angular velocity tracking errors and the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | This approach transforms continuous observations into sparse and robust spike events, improving the stability and noise robustness of ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Therefore, SpikeVLA does not simply trade accuracy for efficiency. instead, it achieves higher energy efficiency through a sparse, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | We evaluated SpikeVLA in the VLN-CE-Isaac simulator using the Unitree Go2 platform to assess its transferability to closedloop ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 6 (3.4. Spiking Neural Network for Action Policy), p. 5 (3.4. Spiking Neural Network for Action Policy), p. 6 (3.4. Spiking Neural Network for Action Policy), p. 3 (3.1. Architecture). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 6 (3.4. Spiking Neural Network for Action Policy), p. 5 (3.4. Spiking Neural Network for Action Policy), p. 6 (3.4. Spiking Neural Network for Action Policy), p. 3 (3.1. Architecture), objective p. 4 (3.2. Spike Neural Network Vision Encoder), p. 4 (3.2. Spike Neural Network Vision Encoder), p. 3 (3.1. Architecture), p. 6 (3.4. Spiking Neural Network for Action Policy), p. 6 (3.4. Spiking Neural Network for Action Policy), p. 3 (3.2. Spike Neural Network Vision Encoder).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
