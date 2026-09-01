# Problem - GravMAD: Grounded Spatial Value Maps Guided Action Diffusion for Generalized 3D Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (33 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=qPzYF2EpXb; PDF retrieval source: https://openreview.net/pdf/ecd829e279f0682dcfeefecc82736686079eb078.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION)): However, these policies often lack the language understanding and generalization abilities of foundation models.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive PDF cue:** Robots' ability to follow language instructions and execute diverse 3D manipulation tasks is vital in robot learning.
- **p. 1 / ABSTRACT - extractive PDF cue:** Traditional imitation learning-based methods perform well on seen tasks but struggle with novel, unseen ones due to variability.
- **p. 1 / ABSTRACT - extractive PDF cue:** Recent approaches leverage large foundation models to assist in understanding novel tasks, thereby mitigating this issue.
- **p. 1 / ABSTRACT - extractive PDF cue:** However, these methods lack a taskspecific learning process, which is essential for an accurate understanding of 3D environments, often leading to execution failures.
- **p. 1 / ABSTRACT - extractive PDF cue:** In this paper, we introduce GravMAD, a sub-goal-driven, language-conditioned action diffusion framework that combines the strengths of imitation learning and foundation models.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** However, these policies often lack the language understanding and generalization abilities of foundation models.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** However, this decoupling often leads to a limited understanding of scenes and manipulation tasks (Huang et al., 2024), allowing robots to conceptually grasp tasks but ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, these policies often lack the language understanding and generalization abilities of foundation models. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Our goal is to learn a policy π : (O, L, G) 7→A, which maps observations ot, sub-goals gt, and instructions ℓto ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | goal, learn, policy, maps, observations, sub-goals, instructions, actions, keypose, corresponding | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | designing, various, learning, frameworks, incorporating, different, representations, Shridhar | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: goal, learn, policy, maps, observations, sub-goals, instructions, actions, keypose, corresponding | p. 5 (3 METHOD), p. 6 (3 METHOD), p. 2 (1 INTRODUCTION) |
| Decision / output variable | action, pose, option or chunk a; body terms: summary, contributions, leveraging, sub-goals, manipulation, tasks, bridge, between | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Objective / loss / cost | policy/action modeling objective; cue terms: loss, maximizes, similarity, between, positive, pairs, minimizes, negative | p. 7 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD) |
| Success / guarantee | instruction-conditioned task success | p. 9 (4 EXPERIMENTS), p. 10 (Figure/Table caption), p. 8 (4 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** However, this decoupling often leads to a limited understanding of scenes and manipulation tasks (Huang et al., 2024), allowing robots to conceptually grasp tasks but ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** However, these policies often overfit to specific tasks (Xie et al., 2024; Zhang et al., 2024), leading to significant performance degradation or even failure when ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** In summary, our contributions are: 1) We propose leveraging key sub-goals in 3D manipulation tasks to bridge the gap between foundation models and learned policies.
- **p. 4 / 1 INTRODUCTION - extractive PDF cue:** Recent works have combined the reasoning capabilities of foundation models with fine-grained control in 3D manipulation to overcome this limitation (Huang et al., 2024; Sharan ...

## What the Paper Changes

PDF contribution framing (p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 4 (3 METHOD)): In summary, our contributions are: 1) We propose leveraging key sub-goals in 3D manipulation tasks to bridge the gap between foundation models and learned policies.

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** To this end, inspired by the approach of introducing task sub-goals to achieve efficient execution in robotic manipulation (Black et al., 2024; Kang et al., ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** 3) We propose a new action diffusion framework, GravMAD, guided by GravMaps.
- **p. 4 / 1 INTRODUCTION - extractive PDF cue:** Our method combines the learning power of diffusion architectures with the generalization of VLMs.
- **p. 4 / 3 METHOD - extractive PDF cue:** In this section, we introduce GravMAD, a multi-task, sub-goal-driven, language-conditioned diffusion framework for 3D manipulation, as shown in Fig.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 26 | Figure 11: Failure cause analysis, including (a) visualization of failure examples; (b) comparison of imprecise labels and expected ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | During testing, except for the novel task "push buttons light", which must be completed in 3 time steps, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | For further analysis of failure cases, please refer to Appendix B.3. | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | In contrast, omitting the cost map causes zero-gradient issues during training, leading to incorrect predictions and task failure. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 5 (3 METHOD), p. 6 (3 METHOD), p. 2 (1 INTRODUCTION), p. 4 (1 INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), interface p. 5 (3 METHOD), p. 6 (3 METHOD), p. 2 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), objective p. 7 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
