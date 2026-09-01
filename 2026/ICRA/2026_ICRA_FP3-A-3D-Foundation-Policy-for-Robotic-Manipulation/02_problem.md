# Problem - FP3: A 3D Foundation Policy for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://2026.ieee-icra.org/awards/; PDF retrieval source: https://arxiv.org/pdf/2503.08950. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): One potential limitation of current policy foundation models is their exclusive reliance on 2D image observations, lacking 3D observation inputs.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Following its success in natural language processing and computer vision, foundation models that are pre-trained on large-scale multi-task datasets have also shown great potential in ...
- **p. 1 / Abstract - extractive PDF cue:** However, most existing robot foundation models rely solely on 2D image observations, ignoring 3D geometric information, which is essential for robots to perceive and reason ...
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we introduce FP3, a first ∗denotes equal contribution. ‡ denotes equal advising. †: work done during the internship at Shanghai AI Laboratory ...
- **p. 1 / Abstract - extractive PDF cue:** FP3 builds on a scalable diffusion transformer architecture and is pre-trained on 60k trajectories with point cloud observations.
- **p. 1 / Abstract - extractive PDF cue:** With the model design and diverse pre-training data, FP3 can be efficiently fine-tuned for downstream tasks while exhibiting strong generalization capabilities.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** One potential limitation of current policy foundation models is their exclusive reliance on 2D image observations, lacking 3D observation inputs.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** However, these learned policies often show limited or even zero generalization capability to unseen scenarios, new objects, and distractors [66].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | One potential limitation of current policy foundation models is their exclusive reliance on 2D image observations, lacking 3D observation inputs. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | It takes the 3D point cloud observation, language, and robot proprioceptive state as input and predicts action chunks of future actions. | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | takes, point, cloud, observation, language, robot, proprioceptive, state, input, predicts | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Formally, formalize, problem, language-conditioned, visuomotor, control, modeling, distribution | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: takes, point, cloud, observation, language, robot, proprioceptive, state, input, predicts | p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD) |
| Decision / output variable | action, pose, option or chunk a; body terms: introduce, Foundation, Policy, FP3, first, point, cloud-based, language-visuomotor | p. 2 (I. INTRODUCTION), p. 4 (III. METHOD), p. 3 (III. METHOD) |
| Objective / loss / cost | policy/action modeling objective; cue terms: weight, decay, gradient, clipping, However, pre-trained, large-scale, foundation | p. 4 (III. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Success / guarantee | instruction-conditioned task success | p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 6 (4) Can FP3 correctly execute the corresponding tasks fol) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** However, these learned policies often show limited or even zero generalization capability to unseen scenarios, new objects, and distractors [66].

## What the Paper Changes

PDF contribution framing (p. 2 (I. INTRODUCTION), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 2 (I. INTRODUCTION)): In this work, we introduce 3D Foundation Policy (FP3), the first 3D point cloud-based language-visuomotor policy foundation model for robotic manipulation that exhibits strong generalizability and sample efficiency.

- **p. 4 / III. METHOD - extractive PDF cue:** Thanks to the effective initialization from pre-training, this small amount of fine-tuning data enables zero-shot deployment to novel environments and objects.
- **p. 3 / III. METHOD - extractive PDF cue:** We introduce the 3D Foundation Policy (FP3) model for generalist robotic manipulation, achieving high data efficiency and generalization capability.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** We summarize our main contributions as follows:

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | This phenomenon happens probably because the fine-tuning data is limited, thus the policies without pre-training can fall into ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | While FP3 shows strong performance as a policy foundation model, it still has several limitations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | One limitation is that although FP3 enables efficient and generalizable downstream fine-tuning, the base model exhibits limited zero-shot ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Qualitatively, we find that the failures of all baseline algorithms are mainly due to issues in the details, ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 2 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 2 (I. INTRODUCTION), objective p. 4 (III. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
