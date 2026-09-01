# Problem - PartGen: Part-level 3D Generation and Reconstruction with Multi-view Diffusion Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Background on 3D generation), p. 4 (3.1. Background on 3D generation)): This has the benefit of removing most of the ambiguity in the reconstruction task, which is important because the 3D reconstructor network is deterministic and cannot handle ambiguity well.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Text- or image-to-3D generators and 3D scanners can now produce 3D assets with high-quality shapes and textures, but as single, fused entities lacking meaningful structure.
- **p. 1 / Abstract - extractive PDF cue:** In contrast, most applications and creative workflows require 3D assets to be composed of distinct, meaningful parts that can be independently manipulated.
- **p. 1 / Abstract - extractive PDF cue:** To bridge this gap, we introduce PartGen, a novel approach for generating, from text, images, or unstructured 3D objects, 3D objects composed of meaningful parts.
- **p. 1 / Abstract - extractive PDF cue:** Our method leverages a multi-view diffusion model to extract plausible and view-consistent part segmentations from multiple views of a Work completed during Minghao Chen's internship ...
- **p. 1 / Abstract - extractive PDF cue:** 3D object, dividing it into meaningful components.
- **p. 2 / 1. Introduction - extractive PDF cue:** This has the benefit of removing most of the ambiguity in the reconstruction task, which is important because the 3D reconstructor network is deterministic and ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Furthermore, current 3D reconstruction and generation methods only model an object's visible outer surface, omitting internal details.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This has the benefit of removing most of the ambiguity in the reconstruction task, which is important because the 3D reconstructor network ... | high-dimensional data 또는 robot action-trajectory distribution | body wording is the source claim |
| Observation / input | The input to the model is a multi-view image I, and the output is a set of multi-view part masks M 1, ... | conditioning observation와 noisy/intermediate sample | exact sensor/frame/preprocessing from PDF |
| State / latent | input, model, multi-view, image, output, part, masks, corresponding, parts, addition | latent/noise variable와 conditional distribution | notation and tensor shape require body check |
| Output / action | first, stage, given, prompt, image, generator, outputs, several | generated sample, action chunk 또는 trajectory | exact unit/frame/decoder require body check |
| Target outcome | sample quality, diversity and latency | distribution fit, multimodality, sample quality와 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | data x₀, noisy state x_t, condition c; body terms: input, model, multi-view, image, output, part, masks, corresponding, parts, addition | p. 4 (3.2. Multi-view part segmentation), p. 3 (3.1. Background on 3D generation), p. 3 (3.1. Background on 3D generation) |
| Decision / output variable | sample/action x̂ or trajectory; body terms: assess, empirically, large, collection, assets, produced, artists, scanned | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method) |
| Objective / loss / cost | distribution/denoising/flow objective; cue terms: Addressing, object, segmentation, through, lens, multi-view, diffusion, offers | p. 5 (3.5. Training data) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.2. Multi-view part segmentation), p. 4 (3.1. Background on 3D generation) |
| Success / guarantee | sample quality, diversity and latency | p. 7 (4.1. Part Segmentation), p. 6 (4.1. Part Segmentation), p. 8 (4.2. Part completion and reconstruction) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** Furthermore, current 3D reconstruction and generation methods only model an object's visible outer surface, omitting internal details.
- **p. 3 / 3.1. Background on 3D generation - extractive PDF cue:** In addition to text and images, the input y can also be an existing 3D model.
- **p. 4 / 3.1. Background on 3D generation - extractive PDF cue:** Our method begins with text, single images, or existing 3D objects to obtain an initial grid view of the object.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method), p. 3 (3. Method), p. 4 (3.1. Background on 3D generation)): We assess our method empirically on a large collection of 3D assets produced by 3D artists or scanned, both quantitatively and qualitatively.

- **p. 2 / 1. Introduction - extractive PDF cue:** Inspired by these requirements, we introduce PartGen, a method to upgrade existing 3D generation pipelines from producing unstructured 3D objects to generating compositions of meaningful ...
- **p. 3 / 3. Method - extractive PDF cue:** This section introduces PartGen, our framework for generating 3D objects composed of several 3D parts.
- **p. 3 / 3. Method - extractive PDF cue:** 3.1, we introduce the necessary background on multiview diffusion and briefly describe how PartGen can be applied to text, image, or 3D model inputs.
- **p. 4 / 3.1. Background on 3D generation - extractive PDF cue:** Our method begins with text, single images, or existing 3D objects to obtain an initial grid view of the object.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Second, we concatenate the four orthogonal views in a multi-view image I and fine-tune SAM2 to predict the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | We then compare ˆJ to the ground-truth render J using Peak Signalto-Noise Ratio (PSNR) of the foreground pixels, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | 6, PartGen can effectively generate 3D objects with distinct and completed parts, even in challenging cases with heavy ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

generative writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3.2. Multi-view part segmentation), p. 3 (3.1. Background on 3D generation), p. 3 (3.1. Background on 3D generation), p. 4 (3.2. Multi-view part segmentation). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Background on 3D generation), p. 4 (3.1. Background on 3D generation), interface p. 4 (3.2. Multi-view part segmentation), p. 3 (3.1. Background on 3D generation), p. 3 (3.1. Background on 3D generation), p. 4 (3.2. Multi-view part segmentation), objective p. 5 (3.5. Training data).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
