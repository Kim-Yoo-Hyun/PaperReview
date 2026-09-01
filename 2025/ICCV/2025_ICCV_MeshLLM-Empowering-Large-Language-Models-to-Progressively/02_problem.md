# Problem - MeshLLM: Empowering Large Language Models to Progressively Understand and Generate 3D Mesh

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Fang_MeshLLM_Empowering_Large_Language_Models_to_Progressively_Understand_and_Generate_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Fang_MeshLLM_Empowering_Large_Language_Models_to_Progressively_Understand_and_Generate_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction)): Despite pioneering the exploration of understanding and generating text-serialized mesh, LLaMA-Mesh poses new challenges to the research community: 1) Data scale limitations: As suggested by the Scaling Law [36], large-scale ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** We present MeshLLM, a novel framework that leverages large language models (LLMs) to understand and generate text-serialized 3D meshes.
- **p. 1 / Abstract - extractive PDF cue:** Our approach addresses key limitations in existing methods, including the limited dataset scale when catering to LLMs' token length and the loss of 3D structural ...
- **p. 1 / Abstract - extractive PDF cue:** We introduce a Primitive-Mesh decomposition strategy, which divides 3D meshes into structurally meaningful subunits.
- **p. 1 / Abstract - extractive PDF cue:** This enables the creation of a large-scale dataset with 1500k+ samples, almost 50× larger than previous methods, which aligns better with the LLM scaling law ...
- **p. 1 / Abstract - extractive PDF cue:** Furthermore, we propose inferring face connectivity from vertices and local mesh assembly training strategies, significantly enhancing the LLMs' ability to capture mesh topology and spatial ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Despite pioneering the exploration of understanding and generating text-serialized mesh, LLaMA-Mesh poses new challenges to the research community: 1) Data scale limitations: As suggested by ...
- **p. 2 / 1. Introduction - extractive PDF cue:** However, due to the limitation of LLMs' token length, LLaMA-Mesh discards a large number of long mesh sequences, and only 31k samples are used for ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Despite pioneering the exploration of understanding and generating text-serialized mesh, LLaMA-Mesh poses new challenges to the research community: 1) Data scale limitations: ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Large Language Model output input mesh understanding mesh generation (1) pretrain on clustered primitive-mesh (2) pretrain on semantic primitive-mesh a muscular humanoid ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | Large, Language, Model, output, input, mesh, understanding, generation, pretrain, clustered | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | design, motivated, observation, LLMs, benefit, truncated, local, text | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Large, Language, Model, output, input, mesh, understanding, generation, pretrain, clustered | p. 4 (3.2. Primitive-Mesh), p. 5 (3.4. SFT Data Curation), p. 3 (3.2. Primitive-Mesh) |
| Decision / output variable | geometry/map/query r; body terms: main, contributions, follows, introduce, mesh, decomposition, strategy, create | p. 2 (1. Introduction), p. 3 (3. Method), p. 3 (3. Method) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Given, vertex, coordinates, corresponding, faces, LLM, optimized, according | p. 4 (3.3. Training Task Design), p. 5 (3.3. Training Task Design), p. 4 (3.3. Training Task Design), p. 5 (3.4. SFT Data Curation) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.3. Training Task Design), p. 5 (3.3. Training Task Design), p. 5 (3.4. SFT Data Curation) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (4.1. Implementation Details), p. 6 (4.1. Implementation Details), p. 7 (4.3. Performance Evaluation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** However, due to the limitation of LLMs' token length, LLaMA-Mesh discards a large number of long mesh sequences, and only 31k samples are used for ...
- **p. 1 / 1. Introduction - extractive PDF cue:** With the rapid development of virtual reality and robotic interaction, equipping LLMs with 3D perception and spatial reasoning capabilities has become a pressing challenge.
- **p. 1 / 1. Introduction - extractive PDF cue:** Against this backdrop, existing research has attempted to integrate LLMs with 3D data [11, 21, 26, 33, 69, 71].

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 3 (3. Method), p. 3 (3. Method), p. 2 (1. Introduction), p. 4 (3.3. Training Task Design)): The main contributions of our work are as follows: • We introduce a mesh decomposition strategy to create 1500k+ Primitive-Meshes, expanding the scale of the trainable dataset by nearly 50 ...

- **p. 3 / 3. Method - extractive PDF cue:** Next, we introduce the concept of Primitive-Mesh.
- **p. 3 / 3. Method - extractive PDF cue:** The set of faces F = {fj}Nf j=1 consists of Nf triangular face elements defined by three vertex indices.
- **p. 2 / 1. Introduction - extractive PDF cue:** This simple approach enables us to quickly construct a largescale dataset comprising 1500k+ training samples.
- **p. 4 / 3.3. Training Task Design - extractive PDF cue:** This task enables the LLM to predict face connectivity given vertices, thereby learning the topological relationships between vertices.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | While MeshLLM shows the potential of LLMs for 3D mesh understanding and generation, certain limitations remain, highlighting future ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | In this paper, we propose MeshLLM, a novel approach that rethinks the paradigm of generating text-serialized meshes using ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3.2. Primitive-Mesh), p. 5 (3.4. SFT Data Curation), p. 3 (3.2. Primitive-Mesh), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), interface p. 4 (3.2. Primitive-Mesh), p. 5 (3.4. SFT Data Curation), p. 3 (3.2. Primitive-Mesh), p. 1 (1. Introduction), objective p. 4 (3.3. Training Task Design), p. 5 (3.3. Training Task Design), p. 4 (3.3. Training Task Design), p. 5 (3.4. SFT Data Curation).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
