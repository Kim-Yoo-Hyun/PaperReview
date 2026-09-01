# Problem - SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (39 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=dt940loCBT; PDF retrieval source: https://openreview.net/pdf/050ee02bf65d6e2e7aa5ba14d172add1b64f86fa.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction)): However, these safety mechanisms cannot be directly applied to VLAs, as there is a substantial gap between the abstract safety concerns at the model intention level [25, 26] and the ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Vision-language-action models (VLAs) show potential as generalist robot policies.
- **p. 1 / Abstract - extractive PDF cue:** However, these models pose extreme safety challenges during real-world deployment, including the risk of harm to the environment, the robot itself, and humans.
- **p. 1 / Abstract - extractive PDF cue:** How can safety constraints be explicitly integrated into VLAs?
- **p. 1 / Abstract - extractive PDF cue:** We address this by exploring an integrated safety approach (ISA), systematically modeling safety requirements, then actively eliciting diverse unsafe behaviors, effectively constraining VLA policies via ...
- **p. 1 / Abstract - extractive PDF cue:** Leveraging the constrained Markov decision process (CMDP) paradigm, ISA optimizes VLAs from a min-max perspective against elicited safety risks.
- **p. 1 / 1 Introduction - extractive PDF cue:** However, these safety mechanisms cannot be directly applied to VLAs, as there is a substantial gap between the abstract safety concerns at the model intention ...
- **p. 1 / 1 Introduction - extractive PDF cue:** While significant progress has been made in task performance, the explicit integration of safety mechanisms remains an open challenge.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, these safety mechanisms cannot be directly applied to VLAs, as there is a substantial gap between the abstract safety concerns at ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | The reward rt is a function of the current state st and the language instruction l: rt = r(st+1/st, at, l) (4) ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | reward, function, current, state, language, instruction, total, immediate, cost, aggregation | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Building, emergence, large, language, models, LLMs, vision-language, VLMs | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: reward, function, current, state, language, instruction, total, immediate, cost, aggregation | p. 31 (C.1 Details of SafeRL Training), p. 32 (C.1 Details of SafeRL Training), p. 1 (1 Introduction) |
| Decision / output variable | action, pose, option or chunk a; body terms: study, details, interconnected, aspects, contribute, more, holistic, safety | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | policy/action modeling objective; cue terms: combined, loss, balances, reward, maximization, constraint, satisfaction, Lagrangian | p. 31 (C.1 Details of SafeRL Training), p. 32 (C.1 Details of SafeRL Training), p. 32 (C.1 Details of SafeRL Training), p. 31 (C.1 Details of SafeRL Training), p. 33 (C.3 Model Selection) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 31 (C.1 Details of SafeRL Training), p. 32 (C.1 Details of SafeRL Training), p. 33 (C.3 Model Selection) |
| Success / guarantee | instruction-conditioned task success | p. 8 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive PDF cue:** While significant progress has been made in task performance, the explicit integration of safety mechanisms remains an open challenge.
- **p. 2 / 1 Introduction - extractive PDF cue:** To tackle this challenge, we make the first systematic explorations into VLA safety alignment.
- **p. 2 / 1 Introduction - extractive PDF cue:** This fundamental limitation motivates an urgent need to explore methodologies capable of explicitly embedding safety constraints into the VLAs [36, 37].
- **p. 3 / 1 Introduction - extractive PDF cue:** high-risk actions and a drastic reduction in unsafe incident severity; and (III) robust generalization of learned safety behaviors to out-of-distribution (OOD) perturbations.

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 33 (C.3 Model Selection)): Our study details how these interconnected aspects contribute to a more holistic safety alignment. • Environment: Addressing the gap in comprehensive VLA safety assessment, we introduce Safety-CHORES.

- **p. 1 / 1 Introduction - extractive PDF cue:** However, these safety mechanisms cannot be directly applied to VLAs, as there is a substantial gap between the abstract safety concerns at the model intention ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Our main contributions are: • Integrated Safety Approach (ISA) Exploration: We conduct a comprehensive investigation into an ISA for VLA safety alignment.
- **p. 1 / 1 Introduction - extractive PDF cue:** Embodied AI aims to develop a generalist policy that can perform perception, interaction, reasoning, and adaptation in the physical world [1].
- **p. 33 / C.3 Model Selection - extractive PDF cue:** 2) Long-Horizon Reasoning: The 100-frame transformer context window (Table 6 in SPOC) allows modeling temporal dependencies critical for anticipating and avoiding cumulative safety risks during ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 26 | Figure 11: Qualitative comparison of ISA-aligned VLA and unaligned VLA behaviors. Left: Trajectory comparison for a representative task. ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Crucially, aligned policies showed robust safety assurance, mitigating long-tail risks and generalizing to out-of-distribution perturbations and extreme failures, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Figure 8: Setup for sim-to-real validation. The physical platform consists of dual Realman RM75- 6F arms equipped with ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 28 | Table 5: GPT-4 Response. Blind Spots The robot, while executing the action move-ahead in the LivingRoom, collided with ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 31 (C.1 Details of SafeRL Training), p. 32 (C.1 Details of SafeRL Training), p. 1 (1 Introduction), p. 1 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), interface p. 31 (C.1 Details of SafeRL Training), p. 32 (C.1 Details of SafeRL Training), p. 1 (1 Introduction), p. 1 (1 Introduction), objective p. 31 (C.1 Details of SafeRL Training), p. 32 (C.1 Details of SafeRL Training), p. 32 (C.1 Details of SafeRL Training), p. 31 (C.1 Details of SafeRL Training), p. 33 (C.3 Model Selection).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
