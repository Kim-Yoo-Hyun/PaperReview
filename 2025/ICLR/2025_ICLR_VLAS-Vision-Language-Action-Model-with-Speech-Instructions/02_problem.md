# Problem - VLAS: Vision-Language-Action Model with Speech Instructions for Customized Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=K4FAFNRpko; PDF retrieval source: https://openreview.net/pdf/5f77b9b6bd43ed1a7a7d7ba9fc75c64727d77792.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): Failure Textual instruction: "Please pick up my cup." Speech instruction: "Please pick up my cup." Success I don't know which cup you want.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive PDF cue:** Vision-language-action models (VLAs) have become increasingly popular in robot manipulation for their end-to-end design and remarkable performance.
- **p. 1 / ABSTRACT - extractive PDF cue:** However, existing VLAs rely heavily on vision-language models (VLMs) that only support text-based instructions, neglecting the more natural speech modality for human-robot interaction.
- **p. 1 / ABSTRACT - extractive PDF cue:** Traditional speech integration methods usually involves a separate speech recognition system, which complicates the model and introduces error propagation.
- **p. 1 / ABSTRACT - extractive PDF cue:** Moreover, the transcription procedure would lose nonsemantic information in the raw speech, such as voiceprint, which may be crucial for robots to successfully complete customized ...
- **p. 1 / ABSTRACT - extractive PDF cue:** To overcome above challenges, we propose VLAS, a novel end-to-end VLA that integrates speech recognition directly into the robot policy model.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Failure Textual instruction: "Please pick up my cup." Speech instruction: "Please pick up my cup." Success I don't know which cup you want.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** These models demonstrate enhanced generalization to novel objects and semantically diverse instructions, as well as a range of emergent capabilities.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Failure Textual instruction: "Please pick up my cup." Speech instruction: "Please pick up my cup." Success I don't know which cup you ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | 3.1 ARCHITECTURE OF VLAS Overall Framework VLAS takes human speech instructions s and visual observations O as input to directly generate robot ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | ARCHITECTURE, VLAS, Overall, Framework, takes, human, speech, instructions, visual, observations | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | input, image, speech, instruction, represented, frequency, Besides, robot | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: ARCHITECTURE, VLAS, Overall, Framework, takes, human, speech, instructions, visual, observations | p. 3 (3 METHOD), p. 1 (1 INTRODUCTION), p. 3 (3 METHOD) |
| Decision / output variable | action, pose, option or chunk a; body terms: main, contributions, listed, follows, VLAS, first, vision-language-action, model | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective / loss / cost | policy/action modeling objective; cue terms: not recovered | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | instruction-conditioned task success | p. 10 (Figure/Table caption), p. 8 (1. I have a blue), p. 8 (1. I have a blue) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** These models demonstrate enhanced generalization to novel objects and semantically diverse instructions, as well as a range of emergent capabilities.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Given these practical needs and existing technologies, a key question arises: How can we integrate visionlanguage-action models with speech modality to produce a simpler and ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** To alleviate these two problems, we present VLAS, an innovative end-toend policy model that seamlessly integrates speech modality for robot manipulation.

## What the Paper Changes

PDF contribution framing (p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 METHOD), p. 1 (1 INTRODUCTION)): To sum up, the main contributions of this work are listed as follows: 1) We propose VLAS, the first vision-language-action model that integrates speech for robot manipulation without needing external ...

- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Based on the above analysis, we propose guiding a robot's behavior through speech rather than text.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** 3) Besides the robot policy model, we introduce VLAS-Base, which extends the widely used vision-language model LLaVA to accept speech instructions.
- **p. 3 / 3 METHOD - extractive PDF cue:** We present VLAS, a VLA model directly supporting speech instructions for robot manipulation.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** These models demonstrate enhanced generalization to novel objects and semantically diverse instructions, as well as a range of emergent capabilities.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 15 | Figure 8: Demonstration of failure cases of VLAS on the customization benchmark. We conducted additional analysis on the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 16 | Figure 9: Demonstration of failure cases of VLA on the customization benchmark. B.2 COMPARISON WITH ROBOFLAMINGO ON THE ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Our future work may focus on exploring other auxiliary information in human speech or environmental sounds to enable ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Moreover, although VLAS-Base falls behind LLaVA with ground-truth textual instructions on the SGQA benchmark, it still surpasses BLIP-2. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3 METHOD), p. 1 (1 INTRODUCTION), p. 3 (3 METHOD), p. 2 (1 INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 3 (3 METHOD), p. 1 (1 INTRODUCTION), p. 3 (3 METHOD), p. 2 (1 INTRODUCTION), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
