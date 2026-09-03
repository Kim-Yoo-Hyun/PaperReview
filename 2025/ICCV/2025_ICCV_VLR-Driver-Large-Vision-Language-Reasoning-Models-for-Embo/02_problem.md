# Problem - VLR-Driver: Large Vision-Language-Reasoning Models for Embodied Autonomous Driving

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (Body text (section not recovered)), p. 2 (Body text (section not recovered)), p. 4 (3.2.1. Perception Level CoT), p. 4 (3.1. Overview)): However, existing CoT-based methods typically rely on openended language generation for reasoning, which lacks structural constraints.

## PDF Body Digest

- **p. 1 / Body text (section not recovered) - extractive body cue:** This ICCV paper is the Open Access version, provided by the Computer Vision Foundation.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Except for this watermark, it is identical to the accepted version; the final published version of the proceedings is available on IEEE Xplore.
- **p. 2 / Body text (section not recovered) - extractive body cue:** However, the decision-making process of VLMs often functions as a "black box", making it challenging to trace and interpret their underlying logic.
- **p. 2 / Body text (section not recovered) - extractive body cue:** This makes it difficult for AD systems to be fully trusted by drivers when encountering complex and emergency situations, such as illegal roadside parking, navigating ...
- **p. 2 / Body text (section not recovered) - extractive body cue:** Moreover, most VLMs are trained on internet data, lacking spatial understanding and specialized training in the field of AD, making it difficult for them to ...
- **p. 2 / Body text (section not recovered) - extractive body cue:** However, existing CoT-based methods typically rely on openended language generation for reasoning, which lacks structural constraints.
- **p. 4 / 3.2.1. Perception Level CoT - extractive body cue:** A critical aspect of safe driving is identifying potential risk points within the current lane.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, existing CoT-based methods typically rely on openended language generation for reasoning, which lacks structural constraints. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | The forward pass is computed as: y = W ′x =  W0 + α r B · A  x, (2) ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | forward, pass, computed, where, output, input, Subsequently, compressed, cropped, image | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | processes, visual, inputs, multi-view, images, alongside, textual, information | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: forward, pass, computed, where, output, input, Subsequently, compressed, cropped, image | p. 6 (3.3. Training Paradigm), p. 4 (3.1. Overview), p. 4 (3.1. Overview) |
| Decision / output variable | geometry/map/query r; body terms: enables, VLR, model, describe, current, driving, scenario, construct | p. 4 (3.2.1. Perception Level CoT), p. 2 (Body text (section not recovered)), p. 4 (3. Method) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: core, principle, GRPO, optimize, strategies, assigning, relative, rewards | p. 6 (3.3. Training Paradigm) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.2. Spatiotemporal CoT Reasoning), p. 5 (3.3. Training Paradigm), p. 5 (3.2.2. Decision Level CoT) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (5.2. Metrics), p. 7 (Figure/Table caption), p. 8 (5.2. Metrics) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / Body text (section not recovered) - extractive body cue:** Moreover, most VLMs are trained on internet data, lacking spatial understanding and specialized training in the field of AD, making it difficult for them to ...
- **p. 4 / 3.2.1. Perception Level CoT - extractive body cue:** A critical aspect of safe driving is identifying potential risk points within the current lane.
- **p. 4 / 3.1. Overview - extractive body cue:** At the same time, there are also the current position (x, y) of ego vehicle, the speed v, the target point position (p, q).

## What the Paper Changes

PDF body contribution framing (p. 4 (3.2.1. Perception Level CoT), p. 2 (Body text (section not recovered)), p. 4 (3. Method), p. 5 (3.2.1. Perception Level CoT), p. 5 (3.2.1. Perception Level CoT)): Our method enables VLR model to describe the current driving scenario, construct real-time spatial layout and dynamic changes of the environment, and achieve long-term planning for driving decisions.

- **p. 2 / Body text (section not recovered) - extractive body cue:** We introduce VLR-Driver, a visual-language-reasoning model developed for embodied AD.
- **p. 4 / 3. Method - extractive body cue:** We present the motivation and design details of our VLRDriver framework.
- **p. 5 / 3.2.1. Perception Level CoT - extractive body cue:** To address this limitation, we introduce consecutive frames I = {If, Ifr, Ifl, Ib, Ibl, Ibr}Tnow t=Tnow-T into the model, allowing it to track temporal ...
- **p. 5 / 3.2.1. Perception Level CoT - extractive body cue:** In this scenario, where some vehicles are illegally parked ahead and blocking the lane, our method can conduct hierarchical patiotemporal reasoning analysis and make a ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | CP, CV, CL, RL, SS, OR, AB, YEV correspond to the Collision with a Pedestrian, Collision with another ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Figure 2. Overview of VLR-Driver framework. We introduce VLR-Driver Dataset, an advanced visual-language-reasoning dataset designed for AD, featuring ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 6 (3.3. Training Paradigm), p. 4 (3.1. Overview), p. 4 (3.1. Overview), p. 2 (Body text (section not recovered)). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (Body text (section not recovered)), p. 2 (Body text (section not recovered)), p. 4 (3.2.1. Perception Level CoT), p. 4 (3.1. Overview), interface p. 6 (3.3. Training Paradigm), p. 4 (3.1. Overview), p. 4 (3.1. Overview), p. 2 (Body text (section not recovered)), objective p. 6 (3.3. Training Paradigm).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
