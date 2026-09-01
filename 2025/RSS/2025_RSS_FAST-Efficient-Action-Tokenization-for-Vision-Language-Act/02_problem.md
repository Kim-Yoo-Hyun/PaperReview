# Problem - FAST: Efficient Action Tokenization for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (19 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p012.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p012.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 4 (1. INTRODUCTION), p. 4 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 1 (1. INTRODUCTION)): ‘To illustrate the challenge of training autoregressive poli cies with current action tokenization approaches, we star With a simple didactic example.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Autoregressive sequence models, such as, Transformer-based vision-language action (VLA) policies, can be tremendously effective for capturing complex and generalizable robotic behaviors.
- **p. 1 / Abstract - extractive body cue:** However, such models require tus to choose a tokenization of our continuous action signals, which determines how the diserete symbols predicted by the ‘model map ...
- **p. 1 / Abstract - extractive body cue:** We find that current approaches for robot action tokenization, based on simple per-dimension, per-timestep binning schemes, typically perform poorly when learning dexterous skills from. high-frequency ...
- **p. 1 / Abstract - extractive body cue:** Our tokenization approach, Frequency space Action Sequence Tokenization (FAST), enables tus to train autoregressive VLAs for highly dexterous and high-frequency tasks where standard discretization methods ...
- **p. 1 / Abstract - extractive body cue:** Based on FAST, we release FAST, a universal robot action tokenizer, trained on IM real robot action trajectories.
- **p. 4 / 1. INTRODUCTION - extractive body cue:** ‘To illustrate the challenge of training autoregressive poli cies with current action tokenization approaches, we star With a simple didactic example.
- **p. 4 / 1. INTRODUCTION - extractive body cue:** This greatly slows down the rate of convergence during training and can make it challenging to fit complex, high-frequency datasets Indeed, such challenges have been ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | ‘To illustrate the challenge of training autoregressive poli cies with current action tokenization approaches, we star With a simple didactic example. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | An alternative approach directly trains VLAS to output ow-level robot control commands given image and language instruction inputs. | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | alternative, directly, trains, VLAS, output, ow-level, robot, control, commands, given | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | developed, FAST, universal, action, tokenizer, serve, strong, default | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: alternative, directly, trains, VLAS, output, ow-level, robot, control, commands, given | p. 3 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 10 (C. Universal Action Tokenizer) |
| Decision / output variable | action, pose, option or chunk a; body terms: FAS, nple, effective, tokenization, robot, action, trajectories, time-series | p. 1 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 3 (1. INTRODUCTION) |
| Objective / loss / cost | policy/action modeling objective; cue terms: After, data, normalized, apply, discrete, cosine, transform, action | p. 4 (B. The FAST Tokenization Algorithm), p. 5 (B. The FAST Tokenization Algorithm), p. 5 (B. The FAST Tokenization Algorithm), p. 7 (B. Comparing Action Tokenizers for VLA Training) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (B. The FAST Tokenization Algorithm), p. 7 (B. Comparing Action Tokenizers for VLA Training), p. 8 (B. Comparing Action Tokenizers for VLA Training) |
| Success / guarantee | instruction-conditioned task success | p. 7 (A. Experimental Setup), p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 4 / 1. INTRODUCTION - extractive body cue:** This greatly slows down the rate of convergence during training and can make it challenging to fit complex, high-frequency datasets Indeed, such challenges have been ...
- **p. 1 / 1. INTRODUCTION - extractive body cue:** We observe that correlations between time steps are a major challenge for naive tokenization strategies when predicting sequences of
- **p. 3 / 1. INTRODUCTION - extractive body cue:** We train a small autoregressive transformer model on a didactic interpolation task, in which the network must predict the black dashed curve given the four ...
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Prior robotic policies of this sort typically use naive tokenization strategies based on a per-dimension, per-timestep binning scheme [9, 10, 40].

## What the Paper Changes

PDF contribution framing (p. 1 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION)): 1: We propose FAS nple yet effective approach for tokenization of robot action trajectories via time-series compression, FAST enables training of autoregressive VLAs that solve complex dexterous manipulation tasks and ...

- **p. 3 / 1. INTRODUCTION - extractive body cue:** We introduce a new action tokenization approach that allows us to train the first autoregressive VLAs ‘on dexterous and high-frequency robot data
- **p. 3 / 1. INTRODUCTION - extractive body cue:** We find that this scheme struggles to scale to high-frequency robot control tasks, We propose a new tokenization scheme for robot actions, based on time-series ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** In this work, we propose a new tokenization strategy from first principles.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** We therefore base our method off of the discrete cosine transform (DCT) encoding, which is widely used for ‘compressing continuous signals stich as images (€.g., ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Even unsuccessful trials show sensible behavior, like approaching the handles of microwave and dish washer doors, even if ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | One current limitation of the autoregressive VLA is its inference speed: while 7» with diffusion typically predicts one ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | We will leave a detailed investigation of the language following abilities of diffusion and autoregressive VLAS to future ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | While far from perfect, the level of generality and robustness of this policy substantially exceeds that of prior ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 10 (C. Universal Action Tokenizer), p. 2 (1. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 4 (1. INTRODUCTION), p. 4 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), interface p. 3 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 10 (C. Universal Action Tokenizer), p. 2 (1. INTRODUCTION), objective p. 4 (B. The FAST Tokenization Algorithm), p. 5 (B. The FAST Tokenization Algorithm), p. 5 (B. The FAST Tokenization Algorithm), p. 7 (B. Comparing Action Tokenizers for VLA Training).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
