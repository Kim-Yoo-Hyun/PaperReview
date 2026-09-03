# Problem - RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.neurips.cc/paper_files/paper/2024/hash/46a126492ea6fb87410e55a58df2e189-Abstract-Conference.html; PDF retrieval source: https://proceedings.neurips.cc/paper_files/paper/2024/hash/46a126492ea6fb87410e55a58df2e189-Abstract-Conference.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1.1 Hz), p. 2 (1.1 Hz), p. 1 (1 Introduction)): While existing MLLM-based policies can handle a range of basic tasks, they still face challenges in two aspects.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** A fundamental objective in robot manipulation is to enable models to comprehend visual scenes and execute actions.
- **p. 1 / Abstract - extractive body cue:** Although existing Vision-Language-Action (VLA) models for robots can handle a range of basic tasks, they still face challenges in two areas: (1) insufficient reasoning ability ...
- **p. 1 / Abstract - extractive body cue:** The recently proposed state space model (SSM) known as Mamba demonstrates promising capabilities in non-trivial sequence modeling with linear inference complexity.
- **p. 1 / Abstract - extractive body cue:** Inspired by this, we introduce RoboMamba, an end-to-end robotic VLA model that leverages Mamba to deliver both robotic reasoning and action capabilities, while maintaining efficient ...
- **p. 1 / Abstract - extractive body cue:** Specifically, we first integrate the vision encoder with Mamba, aligning visual tokens with language embedding through co-training, empowering our model with visual common sense and ...
- **p. 2 / 1.1 Hz - extractive body cue:** While existing MLLM-based policies can handle a range of basic tasks, they still face challenges in two aspects.
- **p. 2 / 1.1 Hz - extractive body cue:** As shown in Figure 1 (reasoning example), this deficiency presents challenges for fine-tuned robot MLLMs when they encounter complex reasoning tasks.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | While existing MLLM-based policies can handle a range of basic tasks, they still face challenges in two aspects. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | In summary, our contributions are as follows: • We introduce RoboMamba, an efficient VLA model that integrates a vision encoder with the ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | summary, contributions, follows, introduce, RoboMamba, efficient, VLA, model, integrates, vision | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | other, hand, Vision-Language-Action, VLA, models, leverage, inherent, capabilities | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: summary, contributions, follows, introduce, RoboMamba, efficient, VLA, model, integrates, vision | p. 3 (1.1 Hz), p. 3 (1.1 Hz), p. 1 (1 Introduction) |
| Decision / output variable | action, pose, option or chunk a; body terms: summary, contributions, follows, introduce, RoboMamba, efficient, VLA, model | p. 3 (1.1 Hz), p. 2 (1.1 Hz), p. 2 (1.1 Hz) |
| Objective / loss / cost | policy/action modeling objective; cue terms: fundamental, objective, robot, manipulation, enable, models, comprehend, visual | p. 1 (Abstract) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (1.1 Hz), p. 2 (1.1 Hz), p. 3 (1.1 Hz) |
| Success / guarantee | instruction-conditioned task success | p. 7 (4 Experiment), p. 9 (Figure/Table caption), p. 7 (4 Experiment) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1.1 Hz - extractive body cue:** As shown in Figure 1 (reasoning example), this deficiency presents challenges for fine-tuned robot MLLMs when they encounter complex reasoning tasks.
- **p. 1 / 1 Introduction - extractive body cue:** The scaling up of data has significantly propelled research on Large Language Models (LLMs) [1-3], showcasing notable advancements in reasoning and generalization abilities within Natural ...

## What the Paper Changes

PDF body contribution framing (p. 3 (1.1 Hz), p. 2 (1.1 Hz), p. 2 (1.1 Hz), p. 1 (Abstract)): In summary, our contributions are as follows: • We introduce RoboMamba, an efficient VLA model that integrates a vision encoder with the linear-complexity Mamba LLM, which possesses visual common sense ...

- **p. 2 / 1.1 Hz - extractive body cue:** Drawing inspiration from this, we raise a question: "Can we develop an efficient robotic VLA model that possesses strong reasoning capabilities while also acquiring robot ...
- **p. 2 / 1.1 Hz - extractive body cue:** Subsequently, we introduce an efficient fine-tuning strategy to equip RoboMamba with pose prediction abilities, requiring a few dozen minutes to fine-tune a simple policy head ...
- **p. 1 / Abstract - extractive body cue:** Inspired by this, we introduce RoboMamba, an end-to-end robotic VLA model that leverages Mamba to deliver both robotic reasoning and action capabilities, while maintaining efficient ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | Prediction of past and future actions is crucial in robotic manipulation, as it not only enables effective rethinking ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Meanwhile, as shown in Figure 5, we also visualize the failure cases of RoboMamba's predictions in both reasoning ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 20 | Figure 6: The visualization of reasoning failure cases. In the bottom right corner of the image, we re-select ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 17 | Due to space limitations, we provide additional details of the proposed method in this supplementary material. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (1.1 Hz), p. 3 (1.1 Hz), p. 1 (1 Introduction), p. 2 (1.1 Hz). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1.1 Hz), p. 2 (1.1 Hz), p. 1 (1 Introduction), interface p. 3 (1.1 Hz), p. 3 (1.1 Hz), p. 1 (1 Introduction), p. 2 (1.1 Hz), objective p. 1 (Abstract).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (26 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** While existing MLLM-based policies can handle a range of basic tasks, they still face challenges in two aspects. (p. 2, 1.1 Hz).
- **Formulation-changing contribution:** Drawing inspiration from this, we raise a question: "Can we develop an efficient robotic VLA model that possesses strong reasoning capabilities while also acquiring robot manipulation skills in a cost-effective ... (p. 2, 1.1 Hz).
- **Assumption/failure evidence:** Or a speech-to-text system might not be used reliably to provide closed captions for online lectures because it fails to handle technical jargon. • The authors should discuss the computational ... (p. 21, 2. Limitations).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
