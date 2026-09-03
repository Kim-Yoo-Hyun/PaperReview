# Problem - PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_PALM_Progress-Aware_Policy_Learning_via_Affordance_Reasoning_for_Long-Horizon_Robotic_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_PALM_Progress-Aware_Policy_Learning_via_Affordance_Reasoning_for_Long-Horizon_Robotic_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation)): In addition, existing VLAs lack mechanisms for continuously estimating progress within a subtask.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Recent advancements in vision-language-action (VLA) models have shown promise in robotic manipulation, yet they continue to struggle with long-horizon, multi-step tasks.
- **p. 1 / Abstract - extractive body cue:** Existing methods lack internal reasoning mechanisms that can identify task-relevant interaction cues or track progress within a subtask, leading to critical execution errors such as ...
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we introduce PALM, a VLA framework that structures policy learning around interaction-centric affordance reasoning and subtask progress cues.
- **p. 1 / Abstract - extractive body cue:** PALM distills complementary affordance representations that capture object relevance, contact geometry, spatial placements, and motion dynamics, and serve as task-relevant anchors for visuomotor control.
- **p. 1 / Abstract - extractive body cue:** To further stabilize long-horizon execution, PALM predicts continuous within-subtask progress, enabling seamless subtask transitions.
- **p. 2 / 1. Introduction - extractive body cue:** In addition, existing VLAs lack mechanisms for continuously estimating progress within a subtask.
- **p. 2 / 1. Introduction - extractive body cue:** Although existing models may infer the final goal and produce intermediate actions [18, 38, 112, 143, 146, 148], they lack internal representations that disambiguate which ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | In addition, existing VLAs lack mechanisms for continuously estimating progress within a subtask. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | PALM processes three synchronized inputs: a language instruction l, an image observation ot, and a robot state st. | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | PALM, processes, three, synchronized, inputs, language, instruction, image, observation, robot | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Much, progress, driven, Vision-Language-Action, VLA, models, leverage, pre-trained | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: PALM, processes, three, synchronized, inputs, language, instruction, image, observation, robot | p. 3 (3.2. PALM Architecture), p. 5 (3.4. Progress-aware Policy via Inverse Dynamics), p. 2 (1. Introduction) |
| Decision / output variable | action, pose, option or chunk a; body terms: contributions, follows, introduce, PALM, unified, VLA, framework, integrates | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation) |
| Objective / loss / cost | policy/action modeling objective; cue terms: Training, follows, standard, diffusion, objective, LDiT, Etd, where | p. 5 (3.4. Progress-aware Policy via Inverse Dynamics) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3.1. Problem Formulation), p. 4 (3.2. PALM Architecture), p. 5 (3.4. Progress-aware Policy via Inverse Dynamics) |
| Success / guarantee | instruction-conditioned task success | p. 7 (4.2. Ablation Studies), p. 6 (4.1. Simulation Experiments), p. 6 (4.1. Simulation Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** Although existing models may infer the final goal and produce intermediate actions [18, 38, 112, 143, 146, 148], they lack internal representations that disambiguate which ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** At time t, given observations ot "O, and task specification ⌧"T , and conditioned on the predicted affordance latent, the policy jointly decodes an action ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 5 (3.4. Progress-aware Policy via Inverse Dynamics)): Our contributions are as follows: • We introduce PALM, a unified VLA framework that integrates structured affordance reasoning and progress-aware policy generation to enable reliable execution across longhorizon, contact-rich manipulati ...

- **p. 2 / 1. Introduction - extractive body cue:** To address these gaps, we introduce PALM, a novel end-to-end framework for learning scalable, long-horizon manipulation.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** At time t, given observations ot "O, and task specification ⌧"T , and conditioned on the predicted affordance latent, the policy jointly decodes an action ...
- **p. 5 / 3.4. Progress-aware Policy via Inverse Dynamics - extractive body cue:** In addition to predicting where to act via affordances, we introduce a progress-aware prediction task that estimates how far execution has advanced within the current ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | PALM achieves stateof-the-art results on two benchmarks, with a 12.5% improvement on CALVIN ABC→D and 91.8% success on ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | As shown in Table 5, results demonstrate PALM's superior generalization over baselines as the task sequence length increases, ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3.2. PALM Architecture), p. 5 (3.4. Progress-aware Policy via Inverse Dynamics), p. 2 (1. Introduction), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation), interface p. 3 (3.2. PALM Architecture), p. 5 (3.4. Progress-aware Policy via Inverse Dynamics), p. 2 (1. Introduction), p. 2 (1. Introduction), objective p. 5 (3.4. Progress-aware Policy via Inverse Dynamics).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** In addition, existing VLAs lack mechanisms for continuously estimating progress within a subtask. (p. 2, 1. Introduction).
- **Formulation-changing contribution:** Our contributions are as follows: • We introduce PALM, a unified VLA framework that integrates structured affordance reasoning and progress-aware policy generation to enable reliable execution across longhorizon, contact-rich manipulati ... (p. 2, 1. Introduction).
- **Assumption/failure evidence:** This absence of temporal grounding leads to characteristic long-horizon failure modes: repeated or unnecessary actions, skipped required subtasks, premature termination, and even declaring success in incorrect states. (p. 2, 1. Introduction).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
