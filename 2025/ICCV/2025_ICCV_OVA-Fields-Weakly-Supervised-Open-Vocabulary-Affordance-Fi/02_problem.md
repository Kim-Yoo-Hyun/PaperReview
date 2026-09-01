# Problem - OVA-Fields: Weakly Supervised Open-Vocabulary Affordance Fields for Robot Operational Part Detection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Su_OVA-Fields_Weakly_Supervised_Open-Vocabulary_Affordance_Fields_for_Robot_Operational_Part_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Su_OVA-Fields_Weakly_Supervised_Open-Vocabulary_Affordance_Fields_for_Robot_Operational_Part_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction)): The first challenge is that current models mainly predict affordances for single objects [5, 6, 25, 36], relying on isolated 2D images or high-quality 3D point clouds that require precise ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** In recent years, affordance detection has become essential for robotic manipulation in real-world scenes, where robots must autonomously interpret commands and perform actions.
- **p. 1 / Abstract - extractive PDF cue:** Current methods often focus on individual point cloud objects or simple semantic queries, limiting their effectiveness in diverse scenes and complex instructions.
- **p. 1 / Abstract - extractive PDF cue:** To address this, we introduce OVA-Fields, a framework for affordance detection in 3D scenes with complex semantics.
- **p. 1 / Abstract - extractive PDF cue:** By integrating multilevel geometric encoding and enhanced semantic affordance embeddings, OVA-Fields maps user commands directly to operational parts, embedding enriched affordance information into the 3D ...
- **p. 1 / Abstract - extractive PDF cue:** Experimental results demonstrate that OVA-Fields achieves 52.4% mIoU on complex semantic real-world scenes and 90% success rate in real-world robot manipulation tasks (e.g., "take out ...
- **p. 1 / 1. Introduction - extractive PDF cue:** The first challenge is that current models mainly predict affordances for single objects [5, 6, 25, 36], relying on isolated 2D images or high-quality 3D ...
- **p. 2 / 1. Introduction - extractive PDF cue:** The second challenge is that existing affordance detection models often fail to handle complex user instructions effectively [1, 2, 9, 15, 19, 42, 44], limiting ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The first challenge is that current models mainly predict affordances for single objects [5, 6, 25, 36], relying on isolated 2D images ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | In the OVA-Fields, our approach uses a sequence of RGB-D images, along with pose data and camera intrinsics, as input to build ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | OVA-Fields, uses, sequence, RGB-D, images, along, pose, data, camera, intrinsics | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | learnable, temperature, parameter, further, optimizes, OVA-Fields, ability, distinguish | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: OVA-Fields, uses, sequence, RGB-D, images, along, pose, data, camera, intrinsics | p. 3 (3.2. Spatial Feature Extraction and Feature Fusion), p. 2 (1. Introduction), p. 4 (3.2. Spatial Feature Extraction and Feature Fusion) |
| Decision / output variable | action, pose, option or chunk a; body terms: Here, introduce, framework, OVA-Fields, enables, accurate, affordance, detection | p. 3 (3. Methods), p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Objective / loss / cost | policy/action modeling objective; cue terms: loss, maximizes, similarity, between, correct, affordance, point, features | p. 3 (3.1. Multi-Modal Affordance Perception), p. 4 (3.2. Spatial Feature Extraction and Feature Fusion), p. 4 (3.2. Spatial Feature Extraction and Feature Fusion), p. 5 (3.2. Spatial Feature Extraction and Feature Fusion) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3.1. Multi-Modal Affordance Perception), p. 4 (3.2. Spatial Feature Extraction and Feature Fusion), p. 3 (3.1. Multi-Modal Affordance Perception) |
| Success / guarantee | instruction-conditioned task success | p. 7 (4.3. Ablation Study), p. 8 (5. Real Robot Experiments), p. 8 (5. Real Robot Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** The second challenge is that existing affordance detection models often fail to handle complex user instructions effectively [1, 2, 9, 15, 19, 42, 44], limiting ...
- **p. 2 / 1. Introduction - extractive PDF cue:** However, existing models trained on manually annotated, high-quality affordance datasets often struggle to generalize to unseen real-world scenes, as their performance heavily depends on the ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Unlike controlled and single-object settings, real-world environments are often cluttered and unstructured, making it difficult to distinguish or isolate the objects with which a robot ...

## What the Paper Changes

PDF contribution framing (p. 3 (3. Methods), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Multi-Modal Affordance Perception)): Here, we introduce our framework, OVA-Fields, which enables accurate affordance detection in 3D scenes based on natural language queries.

- **p. 2 / 1. Introduction - extractive PDF cue:** Our main contributions are summarized as follows: • We propose OVA-Fields, a novel framework for affordance detection in 3D real-world scenes.
- **p. 1 / 1. Introduction - extractive PDF cue:** Our framework directly maps the user's open-vocabulary semantic queries to actionable affordance locations in the complex 3D scenes, allowing robots to identify and interact with ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To address these challenges, we introduce the OVA-Fields framework, a robot-centric affordance detection framework that operates robustly with sparse and noisy sensor inputs.
- **p. 3 / 3.1. Multi-Modal Affordance Perception - extractive PDF cue:** 2a), our method first extracts pixel embeddings from each RGB image.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | The key limitations emerge in handling articulated objects (e.g., doors/drawers). | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Although grasp positions are reliably detected, the current implementation cannot infer required force application directions or kinematic movement ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | This approach demonstrates particular strength in multimodal feature fusion, as 89.3% of failure cases in singlemodality baselines result ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Our dynamic weighting shows that static blending fails to handle feature conflicts in open-vocabulary settings. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3.2. Spatial Feature Extraction and Feature Fusion), p. 2 (1. Introduction), p. 4 (3.2. Spatial Feature Extraction and Feature Fusion), p. 5 (3.3. Query Mapping). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), interface p. 3 (3.2. Spatial Feature Extraction and Feature Fusion), p. 2 (1. Introduction), p. 4 (3.2. Spatial Feature Extraction and Feature Fusion), p. 5 (3.3. Query Mapping), objective p. 3 (3.1. Multi-Modal Affordance Perception), p. 4 (3.2. Spatial Feature Extraction and Feature Fusion), p. 4 (3.2. Spatial Feature Extraction and Feature Fusion), p. 5 (3.2. Spatial Feature Extraction and Feature Fusion).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
