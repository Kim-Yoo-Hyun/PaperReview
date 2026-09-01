# Octopi: Object Property Reasoning with Large Tactile-Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2405.02794.
> PDF retrieval source: https://arxiv.org/pdf/2405.02794. Reading tracker status/evidence was not changed.

- Year/Venue: 2024 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, tactile sensing, Vision-Language, object properties, multimodal reasoning
- Official paper: https://arxiv.org/abs/2405.02794
- Full-text retrieval: https://arxiv.org/pdf/2405.02794
- Code/Project: https://octopi-tactile-lvlm.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 To bridge this gap, we contribute the PHYSICLEAR dataset, which comprises GelSight images on a variety of real world objects, along with object labels and part annotations.를 문제로 두고, PHYSICLEAR and OCTOPI (with key contributions starred).를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Physical reasoning is important for effective robot manipulation.
- **p. 1 / Abstract - extractive body cue:** Recent work has investigated both vision and language modalities for physical reasoning; vision can reveal information about objects in the environment and language serves as ...
- **p. 1 / Abstract - extractive body cue:** Although these works have demonstrated success on a variety of physical reasoning tasks, they are limited to physical properties that can be inferred from visual ...
- **p. 1 / Abstract - extractive body cue:** In this work, we investigate combining tactile perception with language, which enables embodied systems to obtain physical properties through interaction and apply commonsense reasoning.
- **p. 1 / Abstract - extractive body cue:** We contribute a new dataset PHYSICLEAR, which comprises both physical/property reasoning tasks and annotated tactile videos obtained using a GelSight tactile sensor.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To bridge this gap, we contribute the PHYSICLEAR dataset, which comprises GelSight images on a variety of real world objects, along with object labels and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Using commonsense reasoning, OCTOPI infers that it is ripe and fulfils the user's request. domain gap between natural images that typical LVLMs are trained with ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** PHYSICLEAR and OCTOPI (with key contributions starred).
- **p. 2 / I. INTRODUCTION - extractive body cue:** Dataset Property Label Availability Property Diversity Object Diversity Material Diversity Hardness Dataset (2016) [59] Yes (only hardness) Yes Yes Medium Clothing Dataset (2018) [61] Yes ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In experiments, we show that OCTOPI is able to use its tactile modality to predict object properties and reason about scenarios including avocado ripeness. arXiv:2405.02794v2 ...
- **p. 1 / Abstract - extractive body cue:** In this work, we investigate combining tactile perception with language, which enables embodied systems to obtain physical properties through interaction and apply commonsense reasoning.
- **p. 4 / III. PHYSICLEAR - TACTILE AND PHYSICAL - extractive body cue:** Our framework consists of CLIP's visual encoder, a projection module with two linear layers, and Vicuna v1.5 as the LLM.
- **p. 4 / IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED - extractive body cue:** We leverage the capabilities of pre-trained vision models, notably the CLIP [39] visual encoder ViT-L/14, as the foundation for our tactile encoder to derive meaningful ...
- **p. 1 / Abstract - extractive body cue:** We then introduce OCTOPI, a system that leverages both tactile representation learning and large vision-language models to predict and reason about tactile inputs with minimal ...
- **p. 6 / IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED - extractive body cue:** Tactile Feature Alignment We discard the fine-tuned CLIP's classification layers and use the outputs from its visual encoder as output embeddings.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | All five tasks use tactile data and natural language instructions as inputs (Table IV). | tactile image/force, vision과 proprioceptive history | p. 4 (III. PHYSICLEAR - TACTILE AND PHYSICAL), p. 1 (I. INTRODUCTION) |
| State/latent | five, tasks, tactile, data, natural, language, instructions, inputs, Table, sensor, OCTOPI, identifies | contact geometry, force state 또는 latent dynamics | p. 4 (III. PHYSICLEAR - TACTILE AND PHYSICAL), p. 1 (I. INTRODUCTION), p. 1 (Abstract) |
| Output/action | Using inputs from its tactile sensor, OCTOPI identifies the left avocado as softer. | grasp/contact action, force command 또는 object motion | p. 1 (I. INTRODUCTION), p. 1 (Abstract), p. 3 (III. PHYSICLEAR - TACTILE AND PHYSICAL) |
| Objective/outcome | Finally, we add three separate classification heads to ViFiCLIP, each of which predicts a label for one property (i.e. hardness, roughness or bumpiness), and train all three classification heads simultaneously using the ... | slip/contact success, force/pose error와 robustness | p. 6 (IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED), p. 6 (3) Can OCTOPI's understanding of the physical properties) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** PHYSICLEAR and OCTOPI (with key contributions starred).
- **p. 2 / I. INTRODUCTION - extractive body cue:** Dataset Property Label Availability Property Diversity Object Diversity Material Diversity Hardness Dataset (2016) [59] Yes (only hardness) Yes Yes Medium Clothing Dataset (2018) [61] Yes ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In experiments, we show that OCTOPI is able to use its tactile modality to predict object properties and reason about scenarios including avocado ripeness. arXiv:2405.02794v2 ...
- **p. 1 / Abstract - extractive body cue:** In this work, we investigate combining tactile perception with language, which enables embodied systems to obtain physical properties through interaction and apply commonsense reasoning.
- **p. 7 / VI. EXPERIMENTAL RESULTS - extractive body cue:** For both OCTOPI7b and OCTOPI-13b, including the object property significantly improves performance, which supports our overall hypothesis that leveraging these properties is helpful for these ...
- **p. 8 / VI. EXPERIMENTAL RESULTS - extractive body cue:** For avocado property prediction, OCTOPI-13b achieves an accuracy of 35.50%, which is significantly higher than that of the random baseline (3.70%).
- **p. 6 / VI. EXPERIMENTAL RESULTS - extractive body cue:** To address the above questions, we evaluated OCTOPI using (i) accuracy on the physical understanding tasks in PHYSICLEAR's test set, (ii) accuracy on scenario reasoning ...
- **p. 7 / VI. EXPERIMENTAL RESULTS - extractive body cue:** This suggests that OCTOPI's physical understanding improves significantly with LLM size.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (VI. EXPERIMENTAL RESULTS), p. 8 (VI. EXPERIMENTAL RESULTS) |
| Embodiment/environment | To address the above questions, we evaluated OCTOPI using (i) accuracy on the physical understanding tasks in PHYSICLEAR's test set, (ii) accuracy on scenario reasoning tasks, (iii) task success rate on a ... | hardware/simulator version and reset protocol | p. 6 (VI. EXPERIMENTAL RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS) |
| Dataset/benchmark | PG-InstructBLIP was trained to infer a predetermined set of physical properties from visual images of real objects in the EgoObjects dataset [65]. | role, split, size and leakage | p. 6 (VI. EXPERIMENTAL RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS), p. 8 (VI. EXPERIMENTAL RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS) |
| Metric | To address the above questions, we evaluated OCTOPI using (i) accuracy on the physical understanding tasks in PHYSICLEAR's test set, (ii) accuracy on scenario reasoning tasks, (iii) task success rate on a ... | definition, denominator, direction and uncertainty | p. 6 (VI. EXPERIMENTAL RESULTS), p. 8 (VI. EXPERIMENTAL RESULTS), p. 8 (VI. EXPERIMENTAL RESULTS) |
| Baseline/ablation | OCTOPI13b outperforms OCTOPI-7b by 6.96% on PC, 9.33% on PSS and 16.04% on POM. | fair input/data/compute/action matching | p. 7 (VI. EXPERIMENTAL RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS), p. 8 (VI. EXPERIMENTAL RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 8 / VI. EXPERIMENTAL RESULTS - extractive body cue:** This suggests that OCTOPI-13b's physical property prediction capability is robust to differences in tactile exploratory procedures.

## Why Read It

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 To bridge this gap, we contribute the PHYSICLEAR dataset, which comprises GelSight images on a variety of real world objects, along with object labels and part annotations.를 문제로 두고, PHYSICLEAR and OCTOPI (with key contributions starred).를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. PHYSICLEAR - TACTILE AND PHYSICAL), p. 4 (IV. OCTOPI - VISION-LANGUAGE PROPERTY-GUIDED), p. 1 (Abstract) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
