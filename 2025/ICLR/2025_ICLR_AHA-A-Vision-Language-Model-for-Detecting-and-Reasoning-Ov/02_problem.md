# Problem - AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=JVkdSi7Ekg; PDF retrieval source: https://openreview.net/pdf/baa69f167306f963174767be4974c69528aa6379.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction)): While these models excel at task execution, they often face challenges in detecting and reasoning over failures-skills that are crucial for navigating dynamic and complex environments.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Robotic manipulation in open-world settings requires not only task execution but also the ability to detect and learn from failures.
- **p. 1 / Abstract - extractive body cue:** While recent advances in vision-language models (VLMs) and large language models (LLMs) have improved robots' spatial reasoning and problem-solving abilities, they still struggle with failure ...
- **p. 1 / Abstract - extractive body cue:** We introduce AHA, an open-source VLM designed to detect and reason about failures in robotic manipulation using natural language.
- **p. 1 / Abstract - extractive body cue:** By framing failure detection as a free-form reasoning task, AHA identifies failures and provides detailed, adaptable explanations across different robots, tasks, and environments.
- **p. 1 / Abstract - extractive body cue:** We fine-tuned AHA using FailGen, a scalable framework that generates the first large-scale dataset of robotic failure trajectories, the AHA dataset.
- **p. 2 / 1 Introduction - extractive body cue:** While these models excel at task execution, they often face challenges in detecting and reasoning over failures-skills that are crucial for navigating dynamic and complex ...
- **p. 2 / 1 Introduction - extractive body cue:** Unlike prior work that treats failure reasoning as a binary detection problem, we frame it as a free-form reasoning task, offering deeper insights into failure ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | While these models excel at task execution, they often face challenges in detecting and reasoning over failures-skills that are crucial for navigating ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | To capture the temporal relationships within the action sequence, the input image was constructed by selecting a single frame that represents the ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | capture, temporal, relationships, within, action, sequence, input, image, constructed, selecting | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Comparing, evaluated, policy, success, rates, different, failure, feedback | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: capture, temporal, relationships, within, action, sequence, input, image, constructed, selecting | p. 7 (4 Method), p. 6 (4 Method), p. 10 (4 Method) |
| Decision / output variable | action, pose, option or chunk a; body terms: introduce, AHA, open-source, vision-language, model, VLM, uses, natural | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 7 (4 Method) |
| Objective / loss / cost | policy/action modeling objective; cue terms: systematically, assess, reasoning, capabilities, different, VLMs, under, budget | p. 9 (4 Method), p. 10 (4 Method), p. 10 (4 Method), p. 7 (4 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 9 (4 Method), p. 10 (4 Method), p. 7 (4 Method) |
| Success / guarantee | instruction-conditioned task success | p. 10 (4 Method), p. 10 (Figure/Table caption), p. 3 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** Unlike prior work that treats failure reasoning as a binary detection problem, we frame it as a free-form reasoning task, offering deeper insights into failure ...
- **p. 1 / 1 Introduction - extractive body cue:** However, despite these advancements, key challenges remain-particularly with hallucinations, where models generate responses that deviate from truth.
- **p. 1 / 1 Introduction - extractive body cue:** Unlike humans, who can intuitively detect and adjust for such errors, these models often lack the mechanisms for recognizing their own mistakes[6, 7, 8]. ∗Equal ...
- **p. 3 / 1 Introduction - extractive body cue:** 21.4% higher than GPT-4 models, highlighting AHA's effectiveness in delivering accurate natural language failure feedback to improve task performance through error correction.

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 7 (4 Method), p. 10 (4 Method), p. 7 (4 Method)): We introduce AHA, an open-source vision-language model (VLM) that uses natural language to detect and reason about failures in robotic manipulation.

- **p. 2 / 1 Introduction - extractive body cue:** We introduce FailGen, a data generation pipeline for the procedural generation of failure demonstration data for robotic manipulation tasks across simulators.
- **p. 7 / 4 Method - extractive body cue:** This structured input enables consistent handling of data across different tasks and viewpoints.
- **p. 10 / 4 Method - extractive body cue:** AHA enables efficient reward synthesis for reinforcement learning.
- **p. 7 / 4 Method - extractive body cue:** To achieve this, we developed FailGen, an environment wrapper that can be easily applied to any robot manipulation simulator.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | Importantly, as is typical of TAMP methods, the original approach checks for a finite set of failures (inverse ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Figure 1: AHA is a Vision-Language Model designed to detect and reason about failures in robotic manipulation. As ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Table 1: AHA datasets for instruction-tuning. We combined the AHA dataset, our large-scale robotic manipulation failure dataset, with ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | This section outlines the failure reasoning problem formulation (Sec.4.1) used to fine-tune and evaluate AHA. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 7 (4 Method), p. 6 (4 Method), p. 10 (4 Method), p. 6 (4 Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction), interface p. 7 (4 Method), p. 6 (4 Method), p. 10 (4 Method), p. 6 (4 Method), objective p. 9 (4 Method), p. 10 (4 Method), p. 10 (4 Method), p. 7 (4 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
