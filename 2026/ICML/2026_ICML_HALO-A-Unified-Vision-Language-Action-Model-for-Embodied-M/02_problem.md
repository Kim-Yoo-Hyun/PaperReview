# Problem - HALO: A Unified Vision-Language-Action Model for Embodied Multimodal Chain-of-Thought Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=lduY9csXqw; PDF retrieval source: https://openreview.net/pdf/f0a4b4b3d1775cb04d6e602c68bf3c4914033562.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 2 (1. Introduction), p. 2 (1. Introduction)): However, most existing VLAs map perceptual inputs directly to motor commands, lacking explicit mechanisms for reasoning about task structure or anticipating how the environment will evolve under motion and contact.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Vision-Language-Action (VLA) models have shown strong performance in robotic manipulation, but often struggle in long-horizon or out-of-distribution scenarios due to the lack of explicit mechanisms ...
- **p. 1 / Abstract - extractive PDF cue:** Recent works introduce textual chain-ofthought or visual subgoal prediction within VLA models to reason, but still fail to offer a unified human-like reasoning framework for ...
- **p. 1 / Abstract - extractive PDF cue:** To this end, we propose HALO, a unified VLA model that enables embodied multimodal chain-of-thought (EM-CoT) reasoning through a sequential process of textual task reasoning, ...
- **p. 1 / Abstract - extractive PDF cue:** We instantiate HALO with a Mixture-of-Transformers (MoT) architecture that decouples semantic reasoning, visual foresight, and action prediction into specialized experts while allowing seamless cross-expert collaboration.
- **p. 1 / Abstract - extractive PDF cue:** To enable HALO learning at scale, we introduce an automated pipeline to synthesize EM-CoT training data along with a carefully crafted training recipe.
- **p. 1 / 1. Introduction - extractive PDF cue:** However, most existing VLAs map perceptual inputs directly to motor commands, lacking explicit mechanisms for reasoning about task structure or anticipating how the environment will ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Recent work has sought to address this limitation by introducing intermediate reasoning processes like human.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, most existing VLAs map perceptual inputs directly to motor commands, lacking explicit mechanisms for reasoning about task structure or anticipating how ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Traditional VLA models typically learn a monolithic policy πθ(at:t+m / l, ot-k:t) that directly maps history observations and instructions to action chunks. | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | Traditional, VLA, models, typically, learn, monolithic, policy, ot-k, directly, maps | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | pipeline, converts, robotic, trajectories, EM-CoT, data, three, phases | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Traditional, VLA, models, typically, learn, monolithic, policy, ot-k, directly, maps | p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation), p. 5 (3.3. EM-CoT Data Pipeline) |
| Decision / output variable | action, pose, option or chunk a; body terms: address, HALO, unified, VLA, model, enables, embodied, multimodal | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Objective / loss / cost | policy/action modeling objective; cue terms: fine-tuning, objective, minimizes, joint, loss, Lft, where, represent | p. 6 (3.4. Training Recipe), p. 5 (3.3. EM-CoT Data Pipeline), p. 5 (3.4. Training Recipe), p. 6 (3.4. Training Recipe), p. 16 (C. Training Implementation) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (3.4. Training Recipe), p. 16 (C. Training Implementation), p. 3 (3. Method) |
| Success / guarantee | instruction-conditioned task success | p. 8 (4.5. Real-World Results), p. 7 (4.2. Simulation Results), p. 7 (4.2. Simulation Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** Recent work has sought to address this limitation by introducing intermediate reasoning processes like human.
- **p. 3 / 3.1. Problem Formulation - extractive PDF cue:** Such purely reactive policies often suffer from performance degradation when facing long-horizon or complex manipulation tasks due to a lack of intermediate reasoning.
- **p. 2 / 1. Introduction - extractive PDF cue:** Third, we propose a carefully designed training recipe that combines broad generalization with embodied reasoning specialization.
- **p. 2 / 1. Introduction - extractive PDF cue:** Consequently, a unified architecture that jointly supports multimodal reasoning, visual generation, and action prediction remains an open problem.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 5 (3.4. Training Recipe)): To address this, we propose HALO, a unified VLA model that enables embodied multimodal chain-of-thought (EM-CoT) reasoning.

- **p. 2 / 1. Introduction - extractive PDF cue:** Third, we propose a carefully designed training recipe that combines broad generalization with embodied reasoning specialization.
- **p. 1 / 1. Introduction - extractive PDF cue:** Existing approaches (Zhao et al., 2025; Gu et al., 2025) often tightly couple visual *Equal contribution. †Corresponding author.
- **p. 1 / 1. Introduction - extractive PDF cue:** This limitation becomes particularly pronounced in long-horizon or out-of-distribution scenarios-such as novel layouts, unfamiliar objects, or contact-rich interactions-where successful execution depends more on deliberation and ...
- **p. 5 / 3.4. Training Recipe - extractive PDF cue:** This diversity ensures the model develops a generalized representation capable of supporting complex downstream reasoning. • VQA (Mutilmodal understanding): We use LLaVA-NeXT-779k (Liu et al., ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Notably, without any pre-training (w/o V+T+A), the model's performance falls to a complete 0% on hard tasks, demonstrating ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Particularly, the consistent huge relative performance gap (i.e., 73.5% and 62.0%) between HALO and π0 especially on Hard ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | While the baselines suffer noticeable performance degradation in the presence of visual distractions, lighting and background variations, and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Figure 3. Attention Masking Strategy for EM-CoT. (1) Spa- tial and semantic tokens utilize bidirectional attention within frames. ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation), p. 5 (3.3. EM-CoT Data Pipeline), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation), p. 5 (3.3. EM-CoT Data Pipeline), p. 2 (1. Introduction), objective p. 6 (3.4. Training Recipe), p. 5 (3.3. EM-CoT Data Pipeline), p. 5 (3.4. Training Recipe), p. 6 (3.4. Training Recipe), p. 16 (C. Training Implementation).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
