# Problem - ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=72UR53jN7T; PDF retrieval source: https://arxiv.org/pdf/2507.16815. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation)): While this manner enables long-form reasoning without step-level supervision, the reliance on QA-style reward signals limits their ability to support long-horizon planning and makes it difficult to connect reasoning with ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Vision-language-action (VLA) reasoning tasks require agents to interpret multimodal instructions, perform long-horizon planning, and act adaptively in dynamic environments.
- **p. 1 / Abstract - extractive body cue:** Existing approaches typically train VLA models in an end-to-end fashion, directly mapping inputs to actions without explicit reasoning, which hinders their ability to plan over ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose ThinkAct, a dual-system framework that bridges high-level reasoning with low-level action execution via reinforced visual latent planning.
- **p. 1 / Abstract - extractive body cue:** ThinkAct trains a multimodal LLM to generate embodied reasoning plans guided by reinforcing action-aligned visual rewards based on goal completion and trajectory consistency.
- **p. 1 / Abstract - extractive body cue:** These reasoning plans are compressed into a visual plan latent that conditions a downstream action model for robust action execution on target environments.
- **p. 2 / 1. Introduction - extractive body cue:** While this manner enables long-form reasoning without step-level supervision, the reliance on QA-style reward signals limits their ability to support long-horizon planning and makes it ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** To tackle this problem, we propose ThinkAct, a unified framework that aims to leverage an MLLM ℱ𝜃to reason the high-level plans while connecting with an ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | While this manner enables long-form reasoning without step-level supervision, the reliance on QA-style reward signals limits their ability to support long-horizon planning ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | (2023)), which predicts actions based on the current state composed of visual observations and language instructions. | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | predicts, actions, current, state, composed, visual, observations, language, instructions, timestep | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Given, observation, instruction, ThinkAct, advances, actionaligned, rewards, derived | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: predicts, actions, current, state, composed, visual, observations, language, instructions, timestep | p. 5 (3.3. Reasoning-Enhanced Action Adaptation), p. 3 (3.1. Problem Formulation), p. 4 (3.1. Problem Formulation) |
| Decision / output variable | action, pose, option or chunk a; body terms: main, contributions, summarized, follows, ThinkAct, dual-system, framework, mutually | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation) |
| Objective / loss / cost | policy/action modeling objective; cue terms: Thus, optimize, maximizing, following, objective, GRPO, where, mean | p. 5 (3.2. Reinforced Visual Latent Planning for Embodied Reasoning), p. 4 (3.2. Reinforced Visual Latent Planning for Embodied Reasoning), p. 5 (3.3. Reasoning-Enhanced Action Adaptation) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.1. Problem Formulation), p. 6 (3.4. Learning Strategy and Inference), p. 6 (3.3. Reasoning-Enhanced Action Adaptation) |
| Success / guarantee | instruction-conditioned task success | p. 6 (4.1. Experimental Setup), p. 7 (4.2. Quantitative Evaluation), p. 10 (4.5. Analysis of ThinkAct) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 3 / 3.1. Problem Formulation - extractive body cue:** To tackle this problem, we propose ThinkAct, a unified framework that aims to leverage an MLLM ℱ𝜃to reason the high-level plans while connecting with an ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 4 (3.2. Reinforced Visual Latent Planning for Embodied Reasoning), p. 4 (3.1. Problem Formulation)): Our main contributions are summarized as follows: • We propose ThinkAct, a dual-system framework that mutually enhances action execution and visualgrounded embodied reasoning connected by visual latent planning. • We ...

- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose ThinkAct, which aims to enable MLLMs with the capability to reason before acting in physical environments.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** To tackle this problem, we propose ThinkAct, a unified framework that aims to leverage an MLLM ℱ𝜃to reason the high-level plans while connecting with an ...
- **p. 4 / 3.2. Reinforced Visual Latent Planning for Embodied Reasoning - extractive body cue:** As a result, to encourage the model to anticipate visual goal completetion, we introduce the goal reward for comparing predicted start and end positions with ...
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** Note that, during inference, 𝜋𝜑and ℱ𝜃could operate asynchronously to enable slow thinking and fast control for VLA reasoning tasks. our ThinkAct enables long-horizon reasoning and ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 11 | Through extensive experiments across embodied reasoning and robot manipulation benchmarks, we demonstrated strong long-horizon planning, few-shot adaptation, and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | (2023) The RoboFail dataset captures robot manipulation failures in both simulation and real-world scenarios. | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | It includes 100 simulated failure cases in the AI2THOR environment and 30 real-world cases collected via UR5e teleoperation. | reported limitation/failure wording; scope must be verified |
| body cue at p. 15 | The MLLM detects the failure and replans the pickup, leading to successful completion. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (3.3. Reasoning-Enhanced Action Adaptation), p. 3 (3.1. Problem Formulation), p. 4 (3.1. Problem Formulation), p. 6 (3.4. Learning Strategy and Inference). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation), interface p. 5 (3.3. Reasoning-Enhanced Action Adaptation), p. 3 (3.1. Problem Formulation), p. 4 (3.1. Problem Formulation), p. 6 (3.4. Learning Strategy and Inference), objective p. 5 (3.2. Reinforced Visual Latent Planning for Embodied Reasoning), p. 4 (3.2. Reinforced Visual Latent Planning for Embodied Reasoning), p. 5 (3.3. Reasoning-Enhanced Action Adaptation).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
