# Problem - Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (43 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2201.11903; PDF retrieval source: https://arxiv.org/pdf/2201.11903. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (3.2 Results), p. 8 (3.2 Results), p. 5 (3.2 Results)): Both of the above ideas, however, have key limitations.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** We explore how generating a chain of thought-a series of intermediate reasoning steps-significantly improves the ability of large language models to perform complex reasoning.
- **p. 1 / Abstract - extractive PDF cue:** In particular, we show how such reasoning abilities emerge naturally in sufficiently large language models via a simple method called chain-ofthought prompting, where a few ...
- **p. 1 / Abstract - extractive PDF cue:** Experiments on three large language models show that chain-of-thought prompting improves performance on a range of arithmetic, commonsense, and symbolic reasoning tasks.
- **p. 1 / Abstract - extractive PDF cue:** The empirical gains can be striking.
- **p. 1 / Abstract - extractive PDF cue:** For instance, prompting a PaLM 540B with just eight chain-of-thought exemplars achieves state-of-the-art accuracy on the GSM8K benchmark of math word problems, surpassing even finetuned ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Both of the above ideas, however, have key limitations.
- **p. 2 / 1 Introduction - extractive PDF cue:** In this paper, we combine the strengths of these two ideas in a way that avoids their limitations.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Both of the above ideas, however, have key limitations. | 논문이 정의한 robot/embodied environment | body wording is the source claim |
| Observation / input | Model Input Model Output Model Output Model Input Figure 1: Chain-of-thought prompting enables large language models to tackle complex arithmetic, commonsense, and ... | 논문이 명시한 observation과 task input | exact sensor/frame/preprocessing from PDF |
| State / latent | Model, Input, Output, Figure, Chain-of-thought, prompting, enables, large, language, models | task state 또는 decision variable | notation and tensor shape require body check |
| Output / action | Specifically, explore, ability, language, models, perform, few-shot, prompting | paper-specific output/action | exact unit/frame/decoder require body check |
| Target outcome | source task metric; robot link not established | primary task objective와 closed-loop behavior | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | source-defined input o; body terms: Model, Input, Output, Figure, Chain-of-thought, prompting, enables, large, language, models | p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Decision / output variable | prediction/embedding/sample ŷ; body terms: chain-ofthought, prompting, only, enables, language, models, perform, symbolic | p. 8 (3.2 Results), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | paper-specific objective; cue terms: prompting, only, important, because, does, require, large, training | p. 2 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Success / guarantee | source task metric; robot link not established | p. 6 (3.2 Results), p. 5 (3.2 Results), p. 5 (3.2 Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive PDF cue:** In this paper, we combine the strengths of these two ideas in a way that avoids their limitations.
- **p. 5 / 3.2 Results - extractive PDF cue:** For datasets of one-step or two-step problems, however, we find that equation only prompting does improve performance, since the equation can be easily derived from ...
- **p. 8 / 3.2 Results - extractive PDF cue:** As for the OOD evaluations, standard prompting fails for both tasks.
- **p. 5 / 3.2 Results - extractive PDF cue:** 0 20 40 60 GSM8K solve rate (%) LaMDA GPT PaLM Standard prompting Chain-of-thought prompting Prior supervised best 0 20 40 60 80 SVAMP solve ...

## What the Paper Changes

PDF contribution framing (p. 8 (3.2 Results), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (3.2 Results), p. 1 (Abstract)): We show that chain-ofthought prompting not only enables language models to perform symbolic reasoning tasks that are challenging in the standard prompting setting, but also facilitates length generalization to inference-time ...

- **p. 2 / 1 Introduction - extractive PDF cue:** Specifically, we explore the ability of language models to perform few-shot prompting for reasoning tasks, given a prompt that consists of triples: ⟨input, chain of ...
- **p. 2 / 1 Introduction - extractive PDF cue:** We present empirical evaluations on arithmetic, commonsense, and symbolic reasoning benchmarks, showing that chain-of-thought prompting outperforms standard prompting, sometimes to a striking degree.
- **p. 5 / 3.2 Results - extractive PDF cue:** 0 20 40 60 GSM8K solve rate (%) LaMDA GPT PaLM Standard prompting Chain-of-thought prompting Prior supervised best 0 20 40 60 80 SVAMP solve ...
- **p. 1 / Abstract - extractive PDF cue:** Model Input Model Output Model Output Model Input Figure 1: Chain-of-thought prompting enables large language models to tackle complex arithmetic, commonsense, and symbolic reasoning tasks.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | As for limitations, we first qualify that although chain of thought emulates the thought processes of human reasoners, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Third, there is no guarantee of correct reasoning paths, which can lead to both correct and incorrect answers; ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | As for the OOD evaluations, standard prompting fails for both tasks. | reported limitation/failure wording; scope must be verified |
| body cue at p. 23 | Table 6: Ablation and robustness results for arithmetic reasoning datasets. Chain of thought generally outperforms ablations by a ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

upstream writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (3.2 Results), p. 8 (3.2 Results), p. 5 (3.2 Results), interface p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), objective p. 2 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
