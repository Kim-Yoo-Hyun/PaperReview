# Problem - RT-1: Robotics Transformer for Real-World Control at Scale

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2212.06817; PDF retrieval source: https://arxiv.org/pdf/2212.06817. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 4 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES), p. 5 (3 PRELIMINARIES)): And does such a model enjoy the benefits observed in other domains, exhibiting zero-shot generalization to new tasks, environments, and objects?

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** By transferring knowledge from large, diverse, task-agnostic datasets, modern machine learning models can solve specific downstream tasks either zero-shot or with small task-specific datasets to ...
- **p. 1 / ABSTRACT - extractive body cue:** While this capability has been demonstrated in other fields such as computer vision, natural language processing or speech recognition, it remains to be shown in ...
- **p. 1 / ABSTRACT - extractive body cue:** We argue that one of the keys to the success of such general robotic models lies with open-ended task-agnostic training, combined with high-capacity architectures that ...
- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we present a model class, dubbed Robotics Transformer, that exhibits promising scalable model properties.
- **p. 1 / ABSTRACT - extractive body cue:** We verify our conclusions in a study of different model classes and their ability to generalize as a function of the data size, model size, ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** And does such a model enjoy the benefits observed in other domains, exhibiting zero-shot generalization to new tasks, environments, and objects?
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Although recent years have seen several large multitask robot policies proposed in the literature (Reed et al., 2022; Jang et al., 2021), such models often ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | And does such a model enjoy the benefits observed in other domains, exhibiting zero-shot generalization to new tasks, environments, and objects? | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | RT-1 takes a short sequence of images and a natural language instruction as input and outputs an action for the robot at ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | RT-1, takes, short, sequence, images, natural, language, instruction, input, outputs | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | timestep, policy, presented, language, instruction, initial, image, observation | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: RT-1, takes, short, sequence, images, natural, language, instruction, input, outputs | p. 4 (3 PRELIMINARIES), p. 2 (3 Hz), p. 3 (3 PRELIMINARIES) |
| Decision / output variable | action, pose, option or chunk a; body terms: novel, architecture, call, RT-1, Robotics, Transformer, encoding, high-dimensional | p. 2 (3 Hz), p. 1 (ABSTRACT), p. 4 (3 PRELIMINARIES) |
| Objective / loss / cost | policy/action modeling objective; cue terms: goal, learn, policy, maximizes, average, reward, expectation, over | p. 6 (3 PRELIMINARIES) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (3 PRELIMINARIES), p. 3 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES) |
| Success / guarantee | instruction-conditioned task success | p. 8 (6 EXPERIMENTS), p. 10 (6 EXPERIMENTS), p. 11 (6 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive body cue:** Although recent years have seen several large multitask robot policies proposed in the literature (Reed et al., 2022; Jang et al., 2021), such models often ...
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** We evaluate the performance of our policies across these different environments, measuring the policy's performance and ability to generalize.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** 4 SYSTEM OVERVIEW The goal of this work is to build and demonstrate a general robot learning system that can absorb large amounts of data ...
- **p. 5 / 3 PRELIMINARIES - extractive body cue:** (2022), we do not patchify the images into visual tokens prior to feeding them to our Transformer backbone.

## What the Paper Changes

PDF body contribution framing (p. 2 (3 Hz), p. 1 (ABSTRACT), p. 4 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES), p. 7 (3 PRELIMINARIES)): We propose a novel architecture that we call RT-1 (Robotics Transformer 1), which by encoding high-dimensional inputs and outputs, including camera images, instructions and motor commands into compact token representations ...

- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we present a model class, dubbed Robotics Transformer, that exhibits promising scalable model properties.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** 2 (a), consists of partial counters and is constructed for large scale data collection.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** Our training data consists of human-provided demonstrations, and we annotate each episode with a textual description of the instruction that the robot just performed.
- **p. 7 / 3 PRELIMINARIES - extractive body cue:** Our primary dataset consists of ∼130k robot demonstrations, collected with a fleet of 13 robots over the course of 17 months.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 30 | Table 13: Various model ablations of RT-1 across seen tasks, generalization to unseen tasks, and robustness to distractors ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Second, it does not use a pre-trained text embedding to encode the language string. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | It also does not include inference time considerations that are necessary for real robots as discussed in Sec. | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | Adding simulation data does not impact the performance on real objects, while significantly improving real performance on objects ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (3 PRELIMINARIES), p. 2 (3 Hz), p. 3 (3 PRELIMINARIES), p. 2 (3 Hz). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 4 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES), p. 5 (3 PRELIMINARIES), interface p. 4 (3 PRELIMINARIES), p. 2 (3 Hz), p. 3 (3 PRELIMINARIES), p. 2 (3 Hz), objective p. 6 (3 PRELIMINARIES).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (31 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** And does such a model enjoy the benefits observed in other domains, exhibiting zero-shot generalization to new tasks, environments, and objects? (p. 1, 1 INTRODUCTION).
- **Formulation-changing contribution:** We propose a novel architecture that we call RT-1 (Robotics Transformer 1), which by encoding high-dimensional inputs and outputs, including camera images, instructions and motor commands into compact token representations ... (p. 2, 3 Hz).
- **Assumption/failure evidence:** 7 CONCLUSIONS, LIMITATIONS AND FUTURE WORK We presented Robotics Transformer 1, RT-1, a robot learning method that can effectively absorb large amounts of data and scales with data quantity and ... (p. 15, 6 EXPERIMENTS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
