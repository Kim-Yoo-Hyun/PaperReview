# Problem - Training language models to follow instructions with human feedback

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (68 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2203.02155; PDF retrieval source: https://arxiv.org/pdf/2203.02155. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 4 (1 Introduction), p. 1 (1 Introduction), p. 4 (1 Introduction)): Finally we give an extended discussion of our work in Section 5, including implications for alignment research (5.1), what we are aligning to (5.2), limitations (5.3), open questions (5.4), and ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Making language models bigger does not inherently make them better at following a user's intent.
- **p. 1 / Abstract - extractive PDF cue:** For example, large language models can generate outputs that are untruthful, toxic, or simply not helpful to the user.
- **p. 1 / Abstract - extractive PDF cue:** In other words, these models are not aligned with their users.
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we show an avenue for aligning language models with user intent on a wide range of tasks by fine-tuning with human feedback.
- **p. 1 / Abstract - extractive PDF cue:** Starting with a set of labeler-written prompts and prompts submitted through the OpenAI API, we collect a dataset of labeler demonstrations of the desired model ...
- **p. 4 / 1 Introduction - extractive PDF cue:** Finally we give an extended discussion of our work in Section 5, including implications for alignment research (5.1), what we are aligning to (5.2), limitations ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Current affiliations: AA: Anthropic; PC: Alignment Research Center. arXiv:2203.02155v1 [cs.CL] 4 Mar 2022

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Finally we give an extended discussion of our work in Section 5, including implications for alignment research (5.1), what we are aligning ... | 논문이 정의한 robot/embodied environment | body wording is the source claim |
| Observation / input | We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning ... | 논문이 명시한 observation과 task input | exact sensor/frame/preprocessing from PDF |
| State / latent | then, collect, dataset, rankings, model, outputs, further, fine-tune, supervised, reinforcement | task state 또는 decision variable | notation and tensor shape require body check |
| Output / action | InstructGPT, models, generate, more, appropriate, outputs, according, labelers | paper-specific output/action | exact unit/frame/decoder require body check |
| Target outcome | source task metric; robot link not established | primary task objective와 closed-loop behavior | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | source-defined input o; body terms: then, collect, dataset, rankings, model, outputs, further, fine-tune, supervised, reinforcement | p. 1 (Abstract), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Decision / output variable | prediction/embedding/sample ŷ; body terms: See, Section, more, details, sizes, parameters, models, GPT-3 | p. 3 (1 Introduction), p. 4 (1 Introduction), p. 1 (Abstract) |
| Objective / loss / cost | paper-specific objective; cue terms: Finally, reward, function, fine-tune, supervised, learning, baseline, maximize | p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction) |
| Success / guarantee | source task metric; robot link not established | p. 43 (Figure/Table caption), p. 57 (Figure/Table caption), p. 14 (4 Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive PDF cue:** Current affiliations: AA: Anthropic; PC: Alignment Research Center. arXiv:2203.02155v1 [cs.CL] 4 Mar 2022
- **p. 4 / 1 Introduction - extractive PDF cue:** Our models generalize to the preferences of "held-out" labelers that did not produce any training data.

## What the Paper Changes

PDF contribution framing (p. 3 (1 Introduction), p. 4 (1 Introduction), p. 1 (Abstract)): See Section 3 for more details on our method. sizes (1.3B, 6B, and 175B parameters), and all of our models use the GPT-3 architecture.

- **p. 4 / 1 Introduction - extractive PDF cue:** The rest of this paper is structured as follows: We first detail related work in Section 2, before diving into our method and experiment details ...
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we show an avenue for aligning language models with user intent on a wide range of tasks by fine-tuning with human feedback.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 20 | In the longer term, alignment failures could lead to more severe consequences, particularly if these models are deployed ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 18 | We then consider areas for improvement before a larger discussion of the limitations of our work in Section ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 18 | the real world with customers.10 This enables an important feedback loop on the techniques' effectiveness and limitations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 19 | Perhaps the greatest limitation of our models is that, in most cases, they follow the user's instruction, even ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

upstream writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (Abstract), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 4 (1 Introduction), p. 1 (1 Introduction), p. 4 (1 Introduction), interface p. 1 (Abstract), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), objective p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
