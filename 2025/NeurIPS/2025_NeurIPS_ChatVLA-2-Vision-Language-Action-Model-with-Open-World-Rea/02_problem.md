# Problem - ChatVLA-2: Vision-Language-Action Model with Open-World Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=1lyKflUOhp; PDF retrieval source: https://openreview.net/pdf/c88d737915ea445cb600d21cb0c7125912b7053b.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction)): Such a gap leads to a natural question: How can we build VLA models that both keep their VLM prior intact and actively leverage it to achieve superior generalization in ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Vision-language-action (VLA) models have emerged as the next generation of models in robotics.
- **p. 1 / Abstract - extractive PDF cue:** However, despite leveraging powerful pre-trained Vision-Language Models (VLMs), existing end-to-end VLA systems often lose key capabilities during fine-tuning as the model adapts to specific robotic ...
- **p. 1 / Abstract - extractive PDF cue:** We argue that a generalizable VLA model should retain and expand upon the VLM's core competencies: 1) Open-world embodied reasoning - the VLA should inherit ...
- **p. 1 / Abstract - extractive PDF cue:** Work done during Zhongyi Zhou's internship at Midea Group. †Corresponding Authors.
- **p. 1 / Abstract - extractive PDF cue:** 39th Conference on Neural Information Processing Systems (NeurIPS 2025).
- **p. 2 / 1 Introduction - extractive PDF cue:** Such a gap leads to a natural question: How can we build VLA models that both keep their VLM prior intact and actively leverage it ...
- **p. 3 / 1 Introduction - extractive PDF cue:** However, the isolated nature of these feature spaces currently limits the transfer of pre-trained knowledge to robotic control tasks.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Such a gap leads to a natural question: How can we build VLA models that both keep their VLM prior intact and ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Consequently, the robot's actions are guided not just by the initial language instructions and image observations but 6 | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | Consequently, robot, actions, guided, just, initial, language, instructions, image, observations | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | outputs, reasoning, tokens, action, distinctive, feature, model, only | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Consequently, robot, actions, guided, just, initial, language, instructions, image, observations | p. 6 (3 Methodology), p. 7 (3 Methodology), p. 5 (3 Methodology) |
| Decision / output variable | action, pose, option or chunk a; body terms: achieve, novel, VLA, model, architecture, employing, dynamic, mixture-ofexperts | p. 3 (1 Introduction), p. 3 (1 Introduction), p. 5 (3 Methodology) |
| Objective / loss / cost | policy/action modeling objective; cue terms: total, training, cost, GPU, hours, Benefiting, large-scale, multi-modal | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 22 (B.1 Training details), p. 4 (3 Methodology), p. 22 (B.1 Training details) |
| Success / guarantee | instruction-conditioned task success | p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 3 / 1 Introduction - extractive PDF cue:** However, the isolated nature of these feature spaces currently limits the transfer of pre-trained knowledge to robotic control tasks.
- **p. 3 / 1 Introduction - extractive PDF cue:** This work represents a significant step toward the development of truly generalizable robotic foundation models that transcend the limitations of fine-tuning data by effectively leveraging ...
- **p. 2 / 1 Introduction - extractive PDF cue:** By doing so, we enable end-to-end robotic systems to generalize across diverse tasks, which traditionally require explicit planning by an external agent.

## What the Paper Changes

PDF contribution framing (p. 3 (1 Introduction), p. 3 (1 Introduction), p. 5 (3 Methodology), p. 6 (3 Methodology), p. 2 (1 Introduction)): To achieve this, we propose a novel VLA model architecture employing a dynamic mixture-ofexperts within the VLM backbone.

- **p. 3 / 1 Introduction - extractive PDF cue:** Additionally, we introduce a straightforward reasoning-enhancement module designed to align the action expert's output more closely with the model's internal reasoning process.
- **p. 5 / 3 Methodology - extractive PDF cue:** We introduce an enhanced reasoning-following module designed to improve reasoning capabilities in action models.
- **p. 6 / 3 Methodology - extractive PDF cue:** To address this, we propose a dual-stage training strategy designed to enhance the smoothness of robotic control and increase the success rate of task completion.
- **p. 2 / 1 Introduction - extractive PDF cue:** In this study, we introduce ChatVLA-2, a significant advancement toward achieving a truly generalizable robotic foundation model.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Upon investigating the cause of the failure, we discovered that for unseen mathematical equations, both dense models fail ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Even ChatVLA, despite its multimodal understanding capability, fails these tasks when the robot control expert is activated. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Similarly, in manipulation tasks, ChatVLA-2 does not significantly outperform models like π0 and DexVLA, which already exhibit near-perfect ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Furthermore, we find that increasing the number of parameters to 7B does not alleviate these conflicts. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 6 (3 Methodology), p. 7 (3 Methodology), p. 5 (3 Methodology), p. 5 (3 Methodology). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), interface p. 6 (3 Methodology), p. 7 (3 Methodology), p. 5 (3 Methodology), p. 5 (3 Methodology), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
