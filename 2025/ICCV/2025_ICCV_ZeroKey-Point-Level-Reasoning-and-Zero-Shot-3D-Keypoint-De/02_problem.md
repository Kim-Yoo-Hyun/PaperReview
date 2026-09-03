# Problem - ZeroKey: Point-Level Reasoning and Zero-Shot 3D Keypoint Detection from Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Gong_ZeroKey_Point-Level_Reasoning_and_Zero-Shot_3D_Keypoint_Detection_from_Large_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Gong_ZeroKey_Point-Level_Reasoning_and_Zero-Shot_3D_Keypoint_Detection_from_Large_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3. Motivation), p. 4 (3. Motivation), p. 3 (3. Motivation)): In general, we can observe an increased level of difficulty when going from complete objects to object parts and, finally, to specific points or small regions.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We propose a novel zero-shot approach for keypoint detection on 3D shapes.
- **p. 1 / Abstract - extractive body cue:** Point-level reasoning on visual data is challenging as it requires precise localization capability, posing problems even for powerful models like DINO or CLIP.
- **p. 1 / Abstract - extractive body cue:** Traditional methods for 3D keypoint detection rely heavily on annotated 3D datasets and extensive supervised training, limiting their scalability and applicability to new categories or ...
- **p. 1 / Abstract - extractive body cue:** In contrast, our method utilizes the rich knowledge embedded within Multi-Modal Large Language Models (MLLMs).
- **p. 1 / Abstract - extractive body cue:** Specifically, we demonstrate, for the first time, that pixel-level annotations used to train recent MLLMs can be exploited for both extracting and naming salient keypoints ...
- **p. 2 / 1. Introduction - extractive body cue:** In general, we can observe an increased level of difficulty when going from complete objects to object parts and, finally, to specific points or small ...
- **p. 2 / 1. Introduction - extractive body cue:** Through this study, we characterize the strengths and limitations of the 3D awareness imparted to models through training with pixel-level annotations.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | In general, we can observe an increased level of difficulty when going from complete objects to object parts and, finally, to specific ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | It processes both images and text as input and generates text as output. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | processes, images, text, input, generates, output, example, Point, left, wing | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | detect, precise, coordinates, candidate, keypoint, utilize, Molmo, state-of-the-art | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: processes, images, text, input, generates, output, example, Point, left, wing | p. 7 (Method), p. 4 (4.2. Prompting Molmo to Detect 2D Keypoints), p. 4 (4.2. Prompting Molmo to Detect 2D Keypoints) |
| Decision / output variable | geometry/map/query r; body terms: Inspired, recent, developments, investigating, MLLMs, endowed, point-level, reasoning | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (4.2. Prompting Molmo to Detect 2D Keypoints) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: learns, keypoints, optimizing, text, embeddings, latent, diffusion, models | p. 5 (4.3. Zero-Shot 3D Keypoint Detection) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (Method) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (6.1. Setup and Dataset), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** Through this study, we characterize the strengths and limitations of the 3D awareness imparted to models through training with pixel-level annotations.
- **p. 4 / 3. Motivation - extractive body cue:** Furthermore, the recent MLLMs that incorporate 3D data [18, 51, 58] are typically trained with explicit alignment against pre-trained traditional vision-language models, and thus inherit ...
- **p. 4 / 3. Motivation - extractive body cue:** Existing methods for the 3D keypoint detection problem typically formulate the problem as either a supervised learning task, by exploiting the ground truth annotations, e.g., ...
- **p. 3 / 3. Motivation - extractive body cue:** Localization and naming of points in an image or a 3D shape is an extremely challenging problem.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (4.2. Prompting Molmo to Detect 2D Keypoints), p. 7 (Method), p. 7 (Method)): Inspired by these recent developments, we propose investigating MLLMs endowed with point-level reasoning in the context of 3D shape understanding and specifically for zero-shot keypoint detection.

- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we analyze the 3D understanding encoded in Molmo through our method by leveraging Schelling Points and evaluating the describability of keypoints.
- **p. 4 / 4.2. Prompting Molmo to Detect 2D Keypoints - extractive body cue:** The prompt to Molmo consists of the image Vj and the instruction to localize the keypoint ki.
- **p. 7 / Method - extractive body cue:** We then lift these 2D keypoints to 3D using the same backprojection technique described in our method.
- **p. 7 / Method - extractive body cue:** We lift the prediction of this method to 3D using the same lifting procedure used in our method to compare 3D Zero-shot keypoint detection.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Figure 6. We compare against baselines CLIP-DINOiser and Red- Circle. While both baselines identify some prominent regions, they ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Side-by-side comparisons between ground truth keypoints and our Zero-Shot predictions, a figure of GPT-4o fails to precisely locate ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Our evaluations demonstrate the efficacy of our approach and suggest that point-level reasoning is an effective way to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Figure 1. Zero-shot 3D Keypoint Detection. Without any ground truth labels or supervised training, our method leverages the ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 7 (Method), p. 4 (4.2. Prompting Molmo to Detect 2D Keypoints), p. 4 (4.2. Prompting Molmo to Detect 2D Keypoints), p. 7 (Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3. Motivation), p. 4 (3. Motivation), p. 3 (3. Motivation), interface p. 7 (Method), p. 4 (4.2. Prompting Molmo to Detect 2D Keypoints), p. 4 (4.2. Prompting Molmo to Detect 2D Keypoints), p. 7 (Method), objective p. 5 (4.3. Zero-Shot 3D Keypoint Detection).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
