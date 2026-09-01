# Problem - An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2010.11929; PDF retrieval source: https://arxiv.org/pdf/2010.11929. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): Thanks to Transformers' computational efficiency and scalability, it has become possible to train models of unprecedented size, with over 100B parameters (Brown et al., 2020; Lepikhin et al., 2020).

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive PDF cue:** While the Transformer architecture has become the de-facto standard for natural language processing tasks, its applications to computer vision remain limited.
- **p. 1 / ABSTRACT - extractive PDF cue:** In vision, attention is either applied in conjunction with convolutional networks, or used to replace certain components of convolutional networks while keeping their overall structure ...
- **p. 1 / ABSTRACT - extractive PDF cue:** We show that this reliance on CNNs is not necessary and a pure transformer applied directly to sequences of image patches can perform very well ...
- **p. 1 / ABSTRACT - extractive PDF cue:** When pre-trained on large amounts of data and transferred to multiple mid-sized or small image recognition benchmarks (ImageNet, CIFAR-100, VTAB, etc.), Vision Transformer (ViT) attains ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Self-attention-based architectures, in particular Transformers (Vaswani et al., 2017), have become the model of choice in natural language processing (NLP).
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Thanks to Transformers' computational efficiency and scalability, it has become possible to train models of unprecedented size, with over 100B parameters (Brown et al., 2020; ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Published as a conference paper at ICLR 2021 inherent to CNNs, such as translation equivariance and locality, and therefore do not generalize well when trained ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Thanks to Transformers' computational efficiency and scalability, it has become possible to train models of unprecedented size, with over 100B parameters (Brown ... | 논문이 정의한 robot/embodied environment | body wording is the source claim |
| Observation / input | Similar to BERT's [class] token, we prepend a learnable embedding to the sequence of embedded patches (z0 0 = xclass), whose state ... | 논문이 명시한 observation과 task input | exact sensor/frame/preprocessing from PDF |
| State / latent | Similar, BERT, class, token, prepend, learnable, embedding, sequence, embedded, patches | task state 또는 decision variable | notation and tensor shape require body check |
| Output / action | alternative, image, patches, input, sequence, formed, feature, maps | paper-specific output/action | exact unit/frame/decoder require body check |
| Target outcome | source task metric; robot link not established | primary task objective와 closed-loop behavior | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | source-defined input o; body terms: Similar, BERT, class, token, prepend, learnable, embedding, sequence, embedded, patches | p. 3 (3 METHOD), p. 3 (3 METHOD), p. 4 (3 METHOD) |
| Decision / output variable | prediction/embedding/sample ŷ; body terms: Transformer, encoder, Vaswani, consists, alternating, layers, multiheaded, selfattention | p. 3 (3 METHOD) |
| Objective / loss / cost | paper-specific objective; cue terms: Vision, Transformer, handle, arbitrary, sequence, lengths, memory, constraints | p. 4 (3 METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3 METHOD), p. 3 (3 METHOD) |
| Success / guarantee | source task metric; robot link not established | p. 6 (4 EXPERIMENTS), p. 20 (Figure/Table caption), p. 5 (4 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Published as a conference paper at ICLR 2021 inherent to CNNs, such as translation equivariance and locality, and therefore do not generalize well when trained ...

## What the Paper Changes

PDF contribution framing (p. 3 (3 METHOD)): The Transformer encoder (Vaswani et al., 2017) consists of alternating layers of multiheaded selfattention (MSA, see Appendix A) and MLP blocks (Eq.

- additional contribution cue 없음

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Further analysis of few-shot properties of ViT is an exciting direction of future work. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | In this setting data size does not bottleneck the models' performances, and we assess performance versus pre-training cost ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

upstream writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3 METHOD), p. 3 (3 METHOD), p. 4 (3 METHOD), p. 4 (3 METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 3 (3 METHOD), p. 3 (3 METHOD), p. 4 (3 METHOD), p. 4 (3 METHOD), objective p. 4 (3 METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
