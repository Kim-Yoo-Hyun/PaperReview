# Problem - EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html; PDF retrieval source: https://arxiv.org/pdf/2511.05397. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): To address these challenges, we present a full-stack system, and present three distinct contributions. • Collaborative training with adaptive horizon control (AdaHorizon).

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** While Vision-Language-Action (VLA) models map visual inputs and language instructions directly to robot actions, they often rely on costly hardware and struggle in novel or ...
- **p. 1 / Abstract - extractive body cue:** We introduce EverydayVLA, a 6DOF manipulator that can be assembled for $300, capable of modest payloads and workspaces.
- **p. 1 / Abstract - extractive body cue:** A single unified model jointly outputs discrete and continuous actions, and our adaptivehorizon ensembler monitors motion uncertainty to trigger onthe-fly replanning for safe, reliable operation.
- **p. 1 / Abstract - extractive body cue:** On LIBERO, EverydayVLA matches state-of-the-art success rates, and in realworld tests it outperforms prior methods by 49% in-distribution and 34.9% out-of-distribution.
- **p. 1 / Abstract - extractive body cue:** By combining a state-of-the-art VLA with cost-effective hardware, EverydayVLA democratizes access to a robotic foundation model, and paves the way for economical use in homes ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these challenges, we present a full-stack system, and present three distinct contributions. • Collaborative training with adaptive horizon control (AdaHorizon).
- **p. 1 / I. INTRODUCTION - extractive body cue:** Yet, even with internet-scale pretraining, they remain brittle under unfamiliar lighting [3], novel objects [4], and visual distractors [5], and often fail to generalize to ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | To address these challenges, we present a full-stack system, and present three distinct contributions. • Collaborative training with adaptive horizon control (AdaHorizon). | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | EveryDayVLA EveryDayVLA ingests as input a demonstration consisting of an image observation ot and a language instruction lt. | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | EveryDayVLA, ingests, input, demonstration, consisting, image, observation, language, instruction, VLA | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Vision-Language-Action, VLA, models, have, transformed, robotics, learning, direct | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: EveryDayVLA, ingests, input, demonstration, consisting, image, observation, language, instruction, VLA | p. 3 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Decision / output variable | action, pose, option or chunk a; body terms: address, challenges, present, full-stack, system, three, distinct, contributions | p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 2 (III. METHOD) |
| Objective / loss / cost | policy/action modeling objective; cue terms: Hardware, built, DOF, robotic, manipulator, Figure, brackets, online | p. 2 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD) |
| Success / guarantee | instruction-conditioned task success | p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** Yet, even with internet-scale pretraining, they remain brittle under unfamiliar lighting [3], novel objects [4], and visual distractors [5], and often fail to generalize to ...

## What the Paper Changes

PDF body contribution framing (p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 2 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION)): To address these challenges, we present a full-stack system, and present three distinct contributions. • Collaborative training with adaptive horizon control (AdaHorizon).

- **p. 3 / III. METHOD - extractive body cue:** We term our method AdaHorizon, and find that it enables discrete actions to match or exceed the precision of continuous controls, even on dexterous tasks ...
- **p. 2 / III. METHOD - extractive body cue:** To further improve performance, we introduce a novel adaptive horizon module, allowing the
- **p. 3 / III. METHOD - extractive body cue:** To harness both strengths, we introduce a more robust uncertainty metric: the mean absolute difference between the continuous and discrete action predictions, which outperforms the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Yet, even with internet-scale pretraining, they remain brittle under unfamiliar lighting [3], novel objects [4], and visual distractors [5], and often fail to generalize to ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | We also experience limitations in executing fine-grained manipulation, which is due to the limited servo precision as well ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | The primary failure mode for EverydayVLA is delayed object release and not finishing the task in a timely ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Fig. 1. EveryDayVLA system. Top: EveryDayVLA finetunes a VLA for a low-cost manipulator to generate continuous and discrete ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | In real-world trials, we evaluate both in-distribution and out-of-distribution scenarios against OpenVLA and OpenVLA-OFT. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 4 (III. METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 3 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 4 (III. METHOD), objective p. 2 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
