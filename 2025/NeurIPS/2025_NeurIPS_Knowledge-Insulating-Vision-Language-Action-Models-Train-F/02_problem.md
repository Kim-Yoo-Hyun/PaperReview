# Problem - Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=cb0xbZ3APM; PDF retrieval source: https://arxiv.org/pdf/2505.23705. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction)): However, adapting LLMs and VLMs to real-world control requires addressing a number of new challenges.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Vision-language-action (VLA) models provide a powerful approach to training control policies for physical systems, such as robots, by combining end-to-end learning with transfer of semantic ...
- **p. 1 / Abstract - extractive body cue:** However, the constraints of real-time control are often at odds with the design of VLMs: the most powerful VLMs have tens or hundreds of billions ...
- **p. 1 / Abstract - extractive body cue:** To address this challenge, recent VLA models have used specialized modules for efficient continuous control, such as action experts or continuous output heads, which typically ...
- **p. 1 / Abstract - extractive body cue:** While these modules improve real-time and control capabilities, it remains an open question whether they preserve or degrade the semantic knowledge contained in the pretrained ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we study this question in the context of VLAs that include a continuous diffusion or flow matching action expert, showing that naively ...
- **p. 1 / 1 Introduction - extractive body cue:** However, adapting LLMs and VLMs to real-world control requires addressing a number of new challenges.
- **p. 1 / 1 Introduction - extractive body cue:** Autoregressive decoding of discrete tokens is poorly suited to this kind of high-frequency continuous control, both because of the limited resolution of discretized actions and ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, adapting LLMs and VLMs to real-world control requires addressing a number of new challenges. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | While a number of different designs have been successful, a common theme is that models adapted for effective dexterous control typically augment ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | While, number, different, designs, have, been, successful, common, theme, models | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | address, challenge, recent, VLA, models, have, specialized, modules | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: While, number, different, designs, have, been, successful, common, theme, models | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract) |
| Decision / output variable | action, pose, option or chunk a; body terms: address, challenge, training, recipe, addresses, issues, refer, knowledge | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | policy/action modeling objective; cue terms: NOISE, ACTION, EXPERT, continuous, actions, autoregressive, loss, flow | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Success / guarantee | instruction-conditioned task success | p. 10 (Figure/Table caption), p. 8 (6 Experiments), p. 9 (6 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** Autoregressive decoding of discrete tokens is poorly suited to this kind of high-frequency continuous control, both because of the limited resolution of discretized actions and ...
- **p. 2 / 1 Introduction - extractive body cue:** To address this challenge, we propose a training recipe that addresses these issues, which we refer to as knowledge insulation.
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we observe that prior approaches for finetuning VLMs with continuous outputs can, perhaps unsurprisingly, lead to significantly worse training dynamics, as they ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction)): To address this challenge, we propose a training recipe that addresses these issues, which we refer to as knowledge insulation.

- **p. 2 / 1 Introduction - extractive body cue:** Second, using an action expert still enables fast inference.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | 4a) with a common failure mode of being unable to open the drawer. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | A common limitation of many robot policies is that they pay much more attention to images than the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 16 | Figure 10: Comparison of different state representations on "table bussing" task. Our method works well with both text ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Figure 2: Problems with standard VLA recipes. The robot is instructed to bus the spoon into the bin. ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (1 Introduction), objective p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
