# Problem - Point Transformer

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2012.09164; PDF retrieval source: https://arxiv.org/pdf/2012.09164. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): A variety of approaches to deep learning on 3D point clouds have arisen in response to this challenge.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Self-attention networks have revolutionized natural language processing and are making impressive strides in image analysis tasks such as image classification and object detection.
- **p. 1 / Abstract - extractive body cue:** Inspired by this success, we investigate the application of self-attention networks to 3D point cloud processing.
- **p. 1 / Abstract - extractive body cue:** We design self-attention layers for point clouds and use these to construct self-attention networks for tasks such as semantic scene segmentation, object part segmentation, and ...
- **p. 1 / Abstract - extractive body cue:** Our Point Transformer design improves upon prior work across domains and tasks.
- **p. 1 / Abstract - extractive body cue:** For example, on the challenging S3DIS dataset for large-scale semantic scene segmentation, the Point Transformer attains an mIoU of 70.4% on Area 5, outperforming the ...
- **p. 1 / 1. Introduction - extractive body cue:** A variety of approaches to deep learning on 3D point clouds have arisen in response to this challenge.
- **p. 1 / 1. Introduction - extractive body cue:** Sparse convolutional networks relieve these limitations by operating only on voxels that are not empty [9, 3].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | A variety of approaches to deep learning on 3D point clouds have arisen in response to this challenge. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Denote the point set provided as input to the transition down module as P1 and denote the output point set as P2. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Denote, point, provided, input, transition, down, module, output, mAcc, DShapeNets | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | transformer, family, models, particularly, appropriate, point, cloud, processing | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Denote, point, provided, input, transition, down, module, output, mAcc, DShapeNets | p. 5 (3.5. Network Architecture), p. 6 (Method), p. 1 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: consists, models, shape, categories, training, testing, summary, main | p. 6 (4.3. Object Part Segmentation), p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Note, loss-balancing, during, training, boost, category, mIoU, feature | p. 6 (4.3. Object Part Segmentation), p. 5 (3.5. Network Architecture) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (4.3. Object Part Segmentation), p. 5 (3.5. Network Architecture) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 5 (4.1. Semantic Segmentation), p. 5 (4. Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** Sparse convolutional networks relieve these limitations by operating only on voxels that are not empty [9, 3].
- **p. 2 / 1. Introduction - extractive body cue:** We conduct controlled studies to examine specific choices in the Point Transformer design and set the new state of the art on multiple highly competitive ...

## What the Paper Changes

PDF body contribution framing (p. 6 (4.3. Object Part Segmentation), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction)): It consists of 16,880 models from 16 shape categories, with 14,006 3D models for training and 2,874 for testing.

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions include the following. • We design a highly expressive Point Transformer layer for point cloud processing.
- **p. 1 / 1. Introduction - extractive body cue:** We show that Point Transformers are remarkably effective in 3D deep learning tasks, both at the level of detailed object analysis and large-scale parsing of ...
- **p. 1 / 1. Introduction - extractive body cue:** We flesh out this intuition and develop a self-attention layer for 3D point cloud processing.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| no explicit assumption/failure cue | domain stress test only | not a paper claim |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (3.5. Network Architecture), p. 6 (Method), p. 1 (1. Introduction), p. 6 (4.2. Shape Classification). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 5 (3.5. Network Architecture), p. 6 (Method), p. 1 (1. Introduction), p. 6 (4.2. Shape Classification), objective p. 6 (4.3. Object Part Segmentation), p. 5 (3.5. Network Architecture).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
