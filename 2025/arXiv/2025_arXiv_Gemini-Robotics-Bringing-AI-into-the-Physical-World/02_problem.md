# Problem - Gemini Robotics: Bringing AI into the Physical World

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (64 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2503.20020; PDF retrieval source: https://arxiv.org/abs/2503.20020. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 13 (2.0 Flash), p. 3 (1. Introduction), p. 8 (3.5 Sonnet), p. 12 (2.3. Gemini 2.0 Enables Zero and Few-Shot Robot Control), p. 2 (1. Introduction)): However, as a VLM, there are inherent limitations for robot control, especially for more dexterous tasks, due to the intermediate steps needed to connect the model's innate embodied reasoning capabilities ...

## PDF Body Digest

- **p. 1 / 1. Introduction - extractive body cue:** The remarkable progress of modern artificial intelligence (AI) models - with pre-training on largescale datasets - has redefined information processing, demonstrating proficiency and generalization across ...
- **p. 1 / 1. Introduction - extractive body cue:** This has opened a vast landscape of opportunities for interactive and assistive systems within the digital realm, ranging from multimodal chatbots to virtual assistants.
- **p. 1 / 1. Introduction - extractive body cue:** However, realizing the potential of general-purpose autonomous AI in the physical world requires a substantial shift from the digital world, where physically grounded AI agents ...
- **p. 1 / 1. Introduction - extractive body cue:** While, as humans, we take for granted our embodied reasoning abilities - such as perceiving the 3D structure of environments, interpreting complex inter-object relationships, or ...
- **p. 1 / 1. Introduction - extractive body cue:** Furthermore, an embodied AI agent must also go beyond passively understanding the spatial and physical concepts of the real world; it must also learn to ...
- **p. 13 / 2.0 Flash - extractive body cue:** However, as a VLM, there are inherent limitations for robot control, especially for more dexterous tasks, due to the intermediate steps needed to connect the ...
- **p. 3 / 1. Introduction - extractive body cue:** To emphasize the flexibility and generality of the Gemini Robotics models, we also introduce an optional specialization stage, which demonstrates how Gemini Robotics can be ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, as a VLM, there are inherent limitations for robot control, especially for more dexterous tasks, due to the intermediate steps needed ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | backbone dns Local action decoder computer Robot images & state image Figure 14 / Overview of the architecture, input and output of ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | backbone, Local, action, decoder, computer, Robot, images, state, image, Figure | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Then, Gemini, iteratively, takes, images, current, state, scene | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: backbone, Local, action, decoder, computer, Robot, images, state, image, Figure | p. 14 (3. Robot Actions with Gemini Robotics), p. 7 (2.0 Flash. Predicted point labels are not visualized), p. 11 (2.3. Gemini 2.0 Enables Zero and Few-Shot Robot Control) |
| Decision / output variable | action, pose, option or chunk a; body terms: introduce, Gemini, Robotics, family, embodied, models, built, most | p. 2 (1. Introduction), p. 4 (2.1. Embodied Reasoning Question Answering (ERQA) Benchmark), p. 4 (2.1. Embodied Reasoning Question Answering (ERQA) Benchmark) |
| Objective / loss / cost | policy/action modeling objective; cue terms: study, fine-tuning, process, utilizes, re-labeled, version, robot, action | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 17 (3.3. Gemini Robotics can closely follow language instructions), p. 17 (3.3. Gemini Robotics can closely follow language instructions), p. 19 (3.3. Gemini Robotics can closely follow language instructions) |
| Success / guarantee | instruction-conditioned task success | p. 10 (2.0 Pro Experimental) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 3 / 1. Introduction - extractive body cue:** To emphasize the flexibility and generality of the Gemini Robotics models, we also introduce an optional specialization stage, which demonstrates how Gemini Robotics can be ...
- **p. 8 / 3.5 Sonnet - extractive body cue:** Gemini's open-vocabulary and open-world reasoning enables a level of semantic generalization that is difficult to achieve with special-purpose expert models.
- **p. 12 / 2.3. Gemini 2.0 Enables Zero and Few-Shot Robot Control - extractive body cue:** Gemini Robotics: Bringing AI into the Physical World to capture performance across a spectrum of difficulty and objects: from simple grasping (lift a banana) to ...
- **p. 2 / 1. Introduction - extractive body cue:** The models generate dexterous and reactive motions, can be quickly adapted to new embodiments, and use advanced visuo-spatial reasoning to inform actions. on their external ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 4 (2.1. Embodied Reasoning Question Answering (ERQA) Benchmark), p. 4 (2.1. Embodied Reasoning Question Answering (ERQA) Benchmark), p. 7 (2.0 Flash. Predicted point labels are not visualized), p. 1 (1. Introduction)): To this end, we introduce the Gemini Robotics family of embodied AI models, built on top of Gemini 2.0, our most advanced multimodal foundation model.

- **p. 4 / 2.1. Embodied Reasoning Question Answering (ERQA) Benchmark - extractive body cue:** To capture progress in embodied reasoning for VLMs, we introduce ERQA, short for Embodied Reasoning Question Answering, a benchmark that focuses specifically on capabilities likely ...
- **p. 4 / 2.1. Embodied Reasoning Question Answering (ERQA) Benchmark - extractive body cue:** ERQA consists of 400 multiple choice Visual Question Answering (VQA)-style questions across a wide variety of categories, including spatial reasoning, trajectory reasoning, action reasoning, state ...
- **p. 7 / 2.0 Flash. Predicted point labels are not visualized - extractive body cue:** Below we present detailed quantitative and qualitative evaluations of these capabilities with Gemini 2.0 models (Flash, and Pro Experimental), as well as comparisons with other ...
- **p. 1 / 1. Introduction - extractive body cue:** Furthermore, an embodied AI agent must also go beyond passively understanding the spatial and physical concepts of the real world; it must also learn to ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 28 | In addition, while our initial results with Gemini Robotics demonstrate promising generalization capabilities, future work will focus on ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 28 | Robust human-level embodied reasoning is critical for robots and other physically grounded agents. | reported limitation/failure wording; scope must be verified |
| body cue at p. 29 | This involves developing techniques to seamlessly integrate abstract reasoning with precise execution, leading to more robust and generalizable ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 14 (3. Robot Actions with Gemini Robotics), p. 7 (2.0 Flash. Predicted point labels are not visualized), p. 11 (2.3. Gemini 2.0 Enables Zero and Few-Shot Robot Control), p. 13 (2.0 Flash). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 13 (2.0 Flash), p. 3 (1. Introduction), p. 8 (3.5 Sonnet), p. 12 (2.3. Gemini 2.0 Enables Zero and Few-Shot Robot Control), p. 2 (1. Introduction), interface p. 14 (3. Robot Actions with Gemini Robotics), p. 7 (2.0 Flash. Predicted point labels are not visualized), p. 11 (2.3. Gemini 2.0 Enables Zero and Few-Shot Robot Control), p. 13 (2.0 Flash), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
