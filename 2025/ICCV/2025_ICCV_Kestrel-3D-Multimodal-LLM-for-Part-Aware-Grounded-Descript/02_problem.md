# Problem - Kestrel: 3D Multimodal LLM for Part-Aware Grounded Description

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Ahmed_Kestrel_3D_Multimodal_LLM_for_Part-Aware_Grounded_Description_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Ahmed_Kestrel_3D_Multimodal_LLM_for_Part-Aware_Grounded_Description_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): However, a critical limitation persists: existing 3D MLLMs often fail to capture the fine-grained details of object parts and their material properties, which are essential for precise real-world interaction.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** In this paper, we introduce Part-Aware Point Grounded Description (PaPGD), a challenging task aimed at advancing 3D multimodal learning for fine-grained, partaware segmentation grounding and ...
- **p. 1 / Abstract - extractive PDF cue:** Existing 3D datasets largely focus on either vision-only part segmentation or vision-language scene segmentation, lacking the fine-grained multimodal segmentation needed for robotic navigation and interaction ...
- **p. 1 / Abstract - extractive PDF cue:** To address this gap, we present the 3DCoMPaT Grounded Instructions (3DCoMPaT-GrIn) Dataset, a comprehensive resource that pairs rich point cloud descriptions with corresponding part-level segmentation ...
- **p. 1 / Abstract - extractive PDF cue:** This dataset encompasses extensive samples designed for both PaPGD and fine-grained singlepart grounding tasks.
- **p. 1 / Abstract - extractive PDF cue:** To tackle the inherent challenges of grounding objects and generating grounded descriptions at the part level, we propose Kestrel, a part-aware 3D multimodal large language ...
- **p. 2 / 1. Introduction - extractive PDF cue:** However, a critical limitation persists: existing 3D MLLMs often fail to capture the fine-grained details of object parts and their material properties, which are essential ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Both armrests are also leather with a sleek black finish, matching the seat support, which is made of leather in brown.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, a critical limitation persists: existing 3D MLLMs often fail to capture the fine-grained details of object parts and their material properties, ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | The point encoder and LLM take a point-aware instruction and point cloud as input, generating a detailed part-level description of the point ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | point, encoder, LLM, take, point-aware, instruction, cloud, input, generating, detailed | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Recognizing, existing, dataset, supports, training, evaluating, fine-grained, vision-language | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: point, encoder, LLM, take, point-aware, instruction, cloud, input, generating, detailed | p. 4 (4.1. Kestrel), p. 4 (4. Method), p. 2 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: summary, contributions, follows, introduce, Part-Aware, Point, Grounded, Description | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (4. Method) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: achieve, utilize, auto-regressive, cross-entropy, loss, LCE, text, generation | p. 3 (4. Method), p. 5 (4.2. Training Objective), p. 5 (4.2. Training Objective) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (4.2. Training Objective), p. 4 (4.1. Kestrel), p. 6 (Model) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (Figure/Table caption), p. 5 (5. Experiments), p. 5 (5. Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** Both armrests are also leather with a sleek black finish, matching the seat support, which is made of leather in brown.
- **p. 2 / 1. Introduction - extractive PDF cue:** These breakthroughs have spurred a growing trend to adapt MLLMs for 3D applications [22-24, 46, 56, 64] to bridge the gap between human and machine ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (4. Method), p. 4 (4.1. Kestrel), p. 1 (1. Introduction)): In summary, our contributions are as follows: • We introduce Part-Aware Point Grounded Description (PaPGD), a novel task that challenges 3D MLLMs to achieve detailed object understanding through materialaware, part-level ...

- **p. 2 / 1. Introduction - extractive PDF cue:** To tackle the challenges posed by PaPGD, we propose Kestrel, a novel part-aware 3D MLLM designed to capture the intricate spatial and compositional details required ...
- **p. 3 / 4. Method - extractive PDF cue:** To bridge this gap, we propose Kestrel, which combines a 3D MLLM with a query refinement mechanism to enable fine-grained part segmentation along with detailed ...
- **p. 4 / 4.1. Kestrel - extractive PDF cue:** We introduce projector P1 to align the latent space of language and 3D vision.
- **p. 1 / 1. Introduction - extractive PDF cue:** While global scene segmentation has made significant strides, achieving compositional 3D grounded reasoning-where models can accurately identify and segment object parts while understanding their material ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Table 1. Part-Aware Point Grounded Description Results. Comparison of models on language understanding and multi-part grounding. Results marked ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Our work establishes a robust benchmark for part-aware 3D vision-language understanding, paving the way for future research in ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | 5.4, we showcase the robustness and potential applications of Kestrel when the point cloud distribution deviates from the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Figure 5. Real-Word Demos. Kestrel shows a certain degree of robustness to noisy and incomplete real-world inputs. # ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (4.1. Kestrel), p. 4 (4. Method), p. 2 (1. Introduction), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 4 (4.1. Kestrel), p. 4 (4. Method), p. 2 (1. Introduction), p. 1 (1. Introduction), objective p. 3 (4. Method), p. 5 (4.2. Training Objective), p. 5 (4.2. Training Objective).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
