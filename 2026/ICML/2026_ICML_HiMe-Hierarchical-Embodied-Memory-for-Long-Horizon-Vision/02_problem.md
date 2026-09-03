# Problem - HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=vVVbGj9cMC; PDF retrieval source: https://openreview.net/pdf/1158a6b1525482f72ae519b3be5d06e0abef1732.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction)): However, these training-based methods are often constrained by limited context windows and the inherent difficulty of optimizing long-range causal dependencies over hundreds of steps.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Current Vision-Language-Action (VLA) models excel at robotic manipulation but often struggle with non-Markovian tasks requiring long-term memory and reasoning due to their reliance on immediate ...
- **p. 1 / Abstract - extractive body cue:** Existing solutions face a "frequency-competence paradox," where stronger reasoning models are too slow for real-time control, while faster models lack sufficient reasoning capabilities.
- **p. 1 / Abstract - extractive body cue:** To resolve this architectural misalignment, we propose HiMe, a Hierarchical Embodied Memory framework that decouples embodied intelligence into a high-frequency Executor for execution, a Sentry ...
- **p. 1 / Abstract - extractive body cue:** We also introduce a dynamic knowledge system based on cross-modal semantic schemas and active management mechanisms, allowing robots to maintain memory plasticity through "Add, Update, ...
- **p. 1 / Abstract - extractive body cue:** This hierarchical design effectively balances the conflict between real-time execution and slow thinking planning, significantly improving success rates in long-horizon tasks.
- **p. 2 / 1 Introduction - extractive body cue:** However, these training-based methods are often constrained by limited context windows and the inherent difficulty of optimizing long-range causal dependencies over hundreds of steps.
- **p. 1 / 1 Introduction - extractive body cue:** This inherent limitation prevents them from maintaining a persistent belief of the environment in non-Markovian settings.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, these training-based methods are often constrained by limited context windows and the inherent difficulty of optimizing long-range causal dependencies over hundreds ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Most existing architectures rely on the Markov assumption, where the policy 𝑝(𝑎𝑡/𝑜𝑡, 𝑙) predicts the action 𝑎𝑡at time step 𝑡conditioned only on ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | Most, existing, architectures, rely, Markov, assumption, where, policy, predicts, action | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Current, Vision-Language-Action, VLA, models, excel, robotic, manipulation, often | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Most, existing, architectures, rely, Markov, assumption, where, policy, predicts, action | p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract) |
| Decision / output variable | action, pose, option or chunk a; body terms: core, contributions, summarized, follows, Hierarchical, Memory, Management, framework | p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Objective / loss / cost | policy/action modeling objective; cue terms: scale, constraint, turn, limits, internal, world, knowledge, generalization | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 3 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (1 Introduction), p. 1 (Abstract), p. 3 (1 Introduction) |
| Success / guarantee | instruction-conditioned task success | p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** This inherent limitation prevents them from maintaining a persistent belief of the environment in non-Markovian settings.
- **p. 2 / 1 Introduction - extractive body cue:** To overcome these limitations, one intuitive approach is to imbue VLA models with native memory capabilities through specialized training or auxiliary losses [3, 4].
- **p. 1 / 1 Introduction - extractive body cue:** Most existing architectures rely on the Markov assumption, where the policy 𝑝(𝑎𝑡/𝑜𝑡, 𝑙) predicts the action 𝑎𝑡at time step 𝑡conditioned only on the transient observation ...
- **p. 3 / 1 Introduction - extractive body cue:** Experimental results show that our approach significantly outperforms existing flat-memory baselines in both success rate and computational efficiency.

## What the Paper Changes

PDF body contribution framing (p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction)): Our core contributions are summarized as follows: • We propose a Hierarchical Memory Management framework that decouples robotic control into transient (Executor), working (Sentry), and episodic (Planner) memory layers, resolving ...

- **p. 2 / 1 Introduction - extractive body cue:** 1, motivated by this temporal and scale mismatch, we introduce HiMe, a Hierarchical Embodied Memory framework that decouples embodied intelligence into three functional layers with ...
- **p. 3 / 1 Introduction - extractive body cue:** In contrast to passive storage, we introduce explicit Add, Update, and Delete operations to grant the robot knowledge plasticity.
- **p. 1 / Abstract - extractive body cue:** To resolve this architectural misalignment, we propose HiMe, a Hierarchical Embodied Memory framework that decouples embodied intelligence into a high-frequency Executor for execution, a Sentry ...
- **p. 2 / 1 Introduction - extractive body cue:** This organization allows the Planner to retrieve not only vi2

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | The fundamental limitation of such contextual memory is the lack of consolidation: a simple FIFO queue cannot distinguish ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | In Counting, even with Sentry stabilization (Transient Memory w/ Sentry), the robot still fails (23%) due to the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | It ensures that execution loops are eventually broken even when the Sentry fails to trigger. | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | Since the Sentry is prone to False Negatives (missing the "Done" event), we design a fixed-interval Planner fallback. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction), interface p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), objective p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 3 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
