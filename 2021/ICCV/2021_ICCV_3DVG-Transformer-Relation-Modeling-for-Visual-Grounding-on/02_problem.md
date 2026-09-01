# Problem - 3DVG-Transformer: Relation Modeling for Visual Grounding on Point Clouds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2021/html/Zhao_3DVG-Transformer_Relation_Modeling_for_Visual_Grounding_on_Point_Clouds_ICCV_2021_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2021/papers/Zhao_3DVG-Transformer_Relation_Modeling_for_Visual_Grounding_on_Point_Clouds_ICCV_2021_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction)): Moreover, due to the relatively small scales of recent visual grounding datasets, the existing methods also suffer from the overfitting problem, which also prevents these methods from learning a generalizable ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Visual grounding on 3D point clouds is an emerging vision and language task that benefits various applications in understanding the 3D visual world.
- **p. 1 / Abstract - extractive PDF cue:** By formulating this task as a grounding-by-detection problem, lots of recent works focus on how to exploit more powerful detectors and comprehensive language features, but ...
- **p. 1 / Abstract - extractive PDF cue:** Inspired by the well-known transformer architecture, we propose a relation-aware visual grounding method on 3D point clouds, named as 3DVGTransformer, to fully utilize the contextual ...
- **p. 1 / Abstract - extractive PDF cue:** We validate that our 3DVG-Transformer outperforms the state-of-the-art methods by a large margin, on two point cloud-based visual grounding datasets, ScanRefer and Nr3D/Sr3D from ReferIt3D, ...
- **p. 1 / 1. Introduction - extractive PDF cue:** As one emerging 3D visual understanding task, visual grounding on point clouds, also called as referring 3D object localization, aims to locate the desired objects ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Moreover, due to the relatively small scales of recent visual grounding datasets, the existing methods also suffer from the overfitting problem, which also prevents these ...
- **p. 1 / 1. Introduction - extractive PDF cue:** [7] proposed to tackle visual grounding on 3D point clouds by formulating it as a grounding-by-detection problem, together with two newly developed datasets (i.e., ScanRefer ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Moreover, due to the relatively small scales of recent visual grounding datasets, the existing methods also suffer from the overfitting problem, which ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | The goal of visual grounding on 3D point clouds is to localize the object of interest (i.e., the target object) in each ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | goal, visual, grounding, point, clouds, localize, object, interest, target, cloud | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | emerging, visual, understanding, task, grounding, point, clouds, called | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: goal, visual, grounding, point, clouds, localize, object, interest, target, cloud | p. 3 (3.1. Overview), p. 3 (3.2. Relation-enhanced Proposal Generation), p. 1 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: present, overview, introduce, objective, function, includes, pair, feature | p. 3 (3. Methodology), p. 3 (3. Methodology), p. 2 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: introduce, objective, function, includes, pair, feature, augmentation, strategies | p. 3 (3. Methodology), p. 5 (3.4. Loss Function), p. 5 (3.4. Loss Function) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3. Methodology), p. 5 (3.4. Loss Function), p. 5 (3.4. Loss Function) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (4.2. Comparisons with the state-of-the-art methods), p. 5 (4.1. Datasets and Implementation Details), p. 5 (4.1. Datasets and Implementation Details) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** [7] proposed to tackle visual grounding on 3D point clouds by formulating it as a grounding-by-detection problem, together with two newly developed datasets (i.e., ScanRefer ...

## What the Paper Changes

PDF contribution framing (p. 3 (3. Methodology), p. 3 (3. Methodology), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction)): 3.1, we present an overview of our method.

- **p. 3 / 3. Methodology - extractive PDF cue:** 3.4, we introduce the objective function of our method, which also includes a pair of feature augmentation strategies for alleviating overfitting.
- **p. 2 / 1. Introduction - extractive PDF cue:** The contribution of this work is three-fold: (1) A simple and strong visual grounding framework (referred to as 3DVG-Transformer) specifically designed for point clouds, which ...
- **p. 1 / 1. Introduction - extractive PDF cue:** To this end, we propose a relation-aware visual grounding method on 3D point clouds, named as 3DVGTransformer.
- **p. 1 / 1. Introduction - extractive PDF cue:** While our method follows the ground-bydetection strategy from ScanRefer [6], we additionally exploit various relations among proposals at both the object proposal generation stage and ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | The failure cases of ScanRefer indicate that this baseline method cannot well model complex relations and distinguish ambiguous ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Figure 2. The network structure of our coordinate-guided contex- tual aggregation module (a), which consists of 2 transformer ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3.1. Overview), p. 3 (3.2. Relation-enhanced Proposal Generation), p. 1 (1. Introduction), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), interface p. 3 (3.1. Overview), p. 3 (3.2. Relation-enhanced Proposal Generation), p. 1 (1. Introduction), p. 1 (1. Introduction), objective p. 3 (3. Methodology), p. 5 (3.4. Loss Function), p. 5 (3.4. Loss Function).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
