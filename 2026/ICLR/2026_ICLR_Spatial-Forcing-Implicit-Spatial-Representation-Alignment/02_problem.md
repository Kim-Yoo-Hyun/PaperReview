# Problem - Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=euMVC1DO4k; PDF retrieval source: https://openreview.net/pdf/07eb0e64cea5fe734ad2b3b8e85f2a7a591b91ae.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (2.1 PRELIMINARIES)): However, the VLM backbones of these 2D VLA models are pretrained solely on 2D visual modalities and lack precise spatial awareness (Wang et al., 2025c), making it infeasible to adapt ...

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive PDF cue:** Vision-language-action (VLA) models have recently shown strong potential in enabling robots to follow language instructions and execute precise actions.
- **p. 1 / ABSTRACT - extractive PDF cue:** However, most VLAs are built upon vision-language models pretrained solely on 2D data, which lack accurate spatial awareness and hinder their ability to operate in ...
- **p. 1 / ABSTRACT - extractive PDF cue:** Existing solutions attempt to incorporate explicit 3D sensor inputs such as depth maps or point clouds, but these approaches face challenges due to sensor noise, ...
- **p. 1 / ABSTRACT - extractive PDF cue:** Alternative methods that estimate 3D cues from 2D images also suffer from the limited performance of depth estimators.
- **p. 1 / ABSTRACT - extractive PDF cue:** We propose Spatial Forcing (SF), a simple yet effective alignment strategy that implicitly forces VLA models to develop spatial comprehension capabilities without relying on explicit ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** However, the VLM backbones of these 2D VLA models are pretrained solely on 2D visual modalities and lack precise spatial awareness (Wang et al., 2025c), ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Recently, vision-language-action (VLA) models (Brohan et al., 2022; Zitkovich et al., 2023; Bjorck et al., 2025; Black et al., 2024), capable of instruction following and ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, the VLM backbones of these 2D VLA models are pretrained solely on 2D visual modalities and lack precise spatial awareness (Wang ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Published as a conference paper at ICLR 2026 (a) Explicit 3D Input from depth camera or lidar (depth or point cloud) (c) ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | Published, conference, ICLR, Explicit, Input, depth, camera, lidar, point, cloud | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Recently, vision-language-action, VLA, models, Brohan, Zitkovich, Bjorck, Black | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Published, conference, ICLR, Explicit, Input, depth, camera, lidar, point, cloud | p. 4 (2.1 PRELIMINARIES), p. 4 (2.1 PRELIMINARIES), p. 1 (1 INTRODUCTION) |
| Decision / output variable | action, pose, option or chunk a; body terms: Published, conference, ICLR, provide, observation, depth, probing, supported | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective / loss / cost | policy/action modeling objective; cue terms: final, training, objective, combines, standard, loss, action, generation | p. 5 (2.1 PRELIMINARIES), p. 3 (2.1 PRELIMINARIES), p. 3 (2.1 PRELIMINARIES) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (2.1 PRELIMINARIES), p. 4 (2.1 PRELIMINARIES), p. 7 (2.1 PRELIMINARIES) |
| Success / guarantee | instruction-conditioned task success | p. 7 (2.1 PRELIMINARIES), p. 8 (2.1 PRELIMINARIES), p. 8 (2.1 PRELIMINARIES) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Recently, vision-language-action (VLA) models (Brohan et al., 2022; Zitkovich et al., 2023; Bjorck et al., 2025; Black et al., 2024), capable of instruction following and ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** To bridge the gap, we propose Spatial Forcing (SF), a simple yet effective alignment strategy that implicitly forces VLA models to acquire spatial-aware knowledge.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** 1(c), this observation proves that the original visual embeddings fail to yield meaningful spatial structures, revealing a potential gap in the spatial reasoning capabilities of ...
- **p. 3 / 2.1 PRELIMINARIES - extractive PDF cue:** These challenges motivate our exploration of a universal and scalable training paradigm for 3D VLAs.

## What the Paper Changes

PDF contribution framing (p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (2.1 PRELIMINARIES), p. 5 (2.1 PRELIMINARIES)): Published as a conference paper at ICLR 2026 • We provide an observation based on depth probing, supported by an interpretable analysis, to highlight the insufficiency of spatial information in ...

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** To bridge the gap, we propose Spatial Forcing (SF), a simple yet effective alignment strategy that implicitly forces VLA models to acquire spatial-aware knowledge.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Additional experiments on training iterations and dataset sizes indicate that our method realizes 3.8× training while also exhibiting data efficiency with significantly less data.
- **p. 3 / 2.1 PRELIMINARIES - extractive PDF cue:** The text modality consists of task instructions, which are converted into M linguistic tokens {xL t }M t=1 by a text tokenizer.
- **p. 5 / 2.1 PRELIMINARIES - extractive PDF cue:** We evaluate our methods on diverse tasks.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | We take OpenVLA-OFT (Kim et al., 2025) as the base model and conduct experiments on the LIBERO benchmark ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | However, the reconstruction supervision may not be suitable for VLAs to learn effective representations, as it fails to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | SigLIP excels at semantic understanding through robust imagetext alignment, whereas DINOv2 offers stronger visual grounding owing to its ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (2.1 PRELIMINARIES), p. 4 (2.1 PRELIMINARIES), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (2.1 PRELIMINARIES), interface p. 4 (2.1 PRELIMINARIES), p. 4 (2.1 PRELIMINARIES), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), objective p. 5 (2.1 PRELIMINARIES), p. 3 (2.1 PRELIMINARIES), p. 3 (2.1 PRELIMINARIES).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
