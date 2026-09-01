# Problem - Octopi: Object Property Reasoning with Large Tactile-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2405.02794; PDF retrieval source: https://arxiv.org/pdf/2405.02794. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): To bridge this gap, we contribute the PHYSICLEAR dataset, which comprises GelSight images on a variety of real world objects, along with object labels and part annotations.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Physical reasoning is important for effective robot manipulation.
- **p. 1 / Abstract - extractive body cue:** Recent work has investigated both vision and language modalities for physical reasoning; vision can reveal information about objects in the environment and language serves as ...
- **p. 1 / Abstract - extractive body cue:** Although these works have demonstrated success on a variety of physical reasoning tasks, they are limited to physical properties that can be inferred from visual ...
- **p. 1 / Abstract - extractive body cue:** In this work, we investigate combining tactile perception with language, which enables embodied systems to obtain physical properties through interaction and apply commonsense reasoning.
- **p. 1 / Abstract - extractive body cue:** We contribute a new dataset PHYSICLEAR, which comprises both physical/property reasoning tasks and annotated tactile videos obtained using a GelSight tactile sensor.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To bridge this gap, we contribute the PHYSICLEAR dataset, which comprises GelSight images on a variety of real world objects, along with object labels and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Using commonsense reasoning, OCTOPI infers that it is ripe and fulfils the user's request. domain gap between natural images that typical LVLMs are trained with ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | To bridge this gap, we contribute the PHYSICLEAR dataset, which comprises GelSight images on a variety of real world objects, along with ... | contact-rich manipulation scene | body wording is the source claim |
| Observation / input | All five tasks use tactile data and natural language instructions as inputs (Table IV). | tactile image/force, vision과 proprioceptive history | exact sensor/frame/preprocessing from PDF |
| State / latent | five, tasks, tactile, data, natural, language, instructions, inputs, Table, sensor | contact geometry, force state 또는 latent dynamics | notation and tensor shape require body check |
| Output / action | Although, works, have, demonstrated, success, variety, physical, reasoning | grasp/contact action, force command 또는 object motion | exact unit/frame/decoder require body check |
| Target outcome | slip/contact success and safe interaction | slip/contact success, force/pose error와 robustness | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | visual/tactile/proprioceptive contact history; body terms: five, tasks, tactile, data, natural, language, instructions, inputs, Table, sensor | p. 4 (III. PHYSICLEAR - TACTILE AND PHYSICAL), p. 1 (I. INTRODUCTION), p. 1 (Abstract) |
| Decision / output variable | contact-aware action/force; body terms: PHYSICLEAR, OCTOPI, contributions, starred, Dataset, Property, Label, Availability | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective / loss / cost | contact prediction/control error; cue terms: Finally, three, separate, classification, heads, ViFiCLIP, predicts, label | p. 6 (IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED), p. 6 (3) Can OCTOPI's understanding of the physical properties) |
| Success / guarantee | slip/contact success and safe interaction | p. 6 (VI. EXPERIMENTAL RESULTS), p. 8 (VI. EXPERIMENTAL RESULTS), p. 8 (VI. EXPERIMENTAL RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** Using commonsense reasoning, OCTOPI infers that it is ripe and fulfils the user's request. domain gap between natural images that typical LVLMs are trained with ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We further compare against existing datasets across three diversity measures.

## What the Paper Changes

PDF contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (Abstract)): PHYSICLEAR and OCTOPI (with key contributions starred).

- **p. 2 / I. INTRODUCTION - extractive body cue:** Dataset Property Label Availability Property Diversity Object Diversity Material Diversity Hardness Dataset (2016) [59] Yes (only hardness) Yes Yes Medium Clothing Dataset (2018) [61] Yes ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In experiments, we show that OCTOPI is able to use its tactile modality to predict object properties and reason about scenarios including avocado ripeness. arXiv:2405.02794v2 ...
- **p. 1 / Abstract - extractive body cue:** In this work, we investigate combining tactile perception with language, which enables embodied systems to obtain physical properties through interaction and apply commonsense reasoning.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | This suggests that OCTOPI-13b's physical property prediction capability is robust to differences in tactile exploratory procedures. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

tactile writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (III. PHYSICLEAR - TACTILE AND PHYSICAL), p. 1 (I. INTRODUCTION), p. 1 (Abstract), p. 3 (III. PHYSICLEAR - TACTILE AND PHYSICAL). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 4 (III. PHYSICLEAR - TACTILE AND PHYSICAL), p. 1 (I. INTRODUCTION), p. 1 (Abstract), p. 3 (III. PHYSICLEAR - TACTILE AND PHYSICAL), objective p. 6 (IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
