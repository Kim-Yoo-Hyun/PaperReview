# Problem - EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminaries)): Nevertheless, all of them share two limitations in embodied scenarios:

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Understanding a 3D scene immediately with its exploration is essential for embodied tasks, where an agent must construct and comprehend the 3D representation in an ...
- **p. 1 / Abstract - extractive body cue:** In this study, we propose EmbodiedSplat, an online feed-forward 3DGS for open-vocabulary scene understanding that enables simultaneous online 3D reconstruction and 3D semantic understanding from ...
- **p. 1 / Abstract - extractive body cue:** Unlike existing openvocabulary 3DGS methods, our objectives are two-fold: 1) Reconstructs the semantic-embedded 3DGS of the entire scene from over 300 streaming images in an ...
- **p. 1 / 1. Introduction - extractive body cue:** Embodied tasks such as robotic manipulation and navigation [3, 25, 32, 45, 46, 54, 55, 57] require an agent to perceive the 3D scene immediately ...
- **p. 1 / 1. Introduction - extractive body cue:** Specifically, the embodied agent equipped with a precise SLAM system collects posed RGB or RGB-D images to understand the 3D scene, follow human instructions, and ...
- **p. 2 / 1. Introduction - extractive body cue:** Nevertheless, all of them share two limitations in embodied scenarios:
- **p. 1 / 1. Introduction - extractive body cue:** 3DGS is the recent 3D representation that supports real-time novel view synthesis with explicit structure which existing repreThis CVPR paper is the Open Access version, ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Nevertheless, all of them share two limitations in embodied scenarios: | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Specifically, the embodied agent equipped with a precise SLAM system collects posed RGB or RGB-D images to understand the 3D scene, follow ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Specifically, embodied, agent, equipped, precise, SLAM, system, collects, posed, RGB | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Since, FreeSplat, designed, offline, modify, inference, pipeline, enable | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Specifically, embodied, agent, equipped, precise, SLAM, system, collects, posed, RGB | p. 1 (1. Introduction), p. 3 (3. Preliminaries), p. 3 (3. Preliminaries) |
| Decision / output variable | geometry/map/query r; body terms: contributions, follows, Novel, framework, embodied, perception, enables, online | p. 2 (1) They require per-scene optimization that cannot be gen), p. 2 (1) They require per-scene optimization that cannot be gen), p. 1 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: resulting, total, cost, L-1, precompute, global, codebook, where | p. 2 (1) They require per-scene optimization that cannot be gen), p. 4 (4.1. EmbodiedSplat), p. 4 (4.1. EmbodiedSplat), p. 5 (4.1. EmbodiedSplat), p. 6 (Method), p. 6 (Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (4.1. EmbodiedSplat), p. 4 (4.1. EmbodiedSplat), p. 2 (1) They require per-scene optimization that cannot be gen) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 8 (5.2. Ablation Studies), p. 6 (Figure/Table caption), p. 7 (5.2. Ablation Studies) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** 3DGS is the recent 3D representation that supports real-time novel view synthesis with explicit structure which existing repreThis CVPR paper is the Open Access version, ...
- **p. 2 / 1. Introduction - extractive body cue:** Its distinct competency motivates the current research to explore the open-vocabulary scene understanding with 3DGS.
- **p. 3 / 3. Preliminaries - extractive body cue:** Given the current frame It ∈RH×W ×3, we select N past frames from time steps t-N to t-1 to reflect the online setting.

## What the Paper Changes

PDF body contribution framing (p. 2 (1) They require per-scene optimization that cannot be gen), p. 2 (1) They require per-scene optimization that cannot be gen), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3. Preliminaries)): Our contributions are as follows: • Novel framework for embodied 3D perception which enables online, whole-scene reconstruction for languageembedded 3DGS with up to 5-6 FPS inference speed. • Combination of ...

- **p. 2 / 1) They require per-scene optimization that cannot be gen - extractive body cue:** To this end, we propose EmbodiedSplat, a novel online framework to endow pretrained feed-forward 3DGS [44] with open-vocabulary capability.
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, our objective is to develop an embodied perception model that meets the above five conditions by leveraging 3D Gaussian Splatting (3DGS) [20].
- **p. 1 / 1. Introduction - extractive body cue:** 3DGS is the recent 3D representation that supports real-time novel view synthesis with explicit structure which existing repreThis CVPR paper is the Open Access version, ...
- **p. 3 / 3. Preliminaries - extractive body cue:** Since FreeSplat++ is designed for offline use, we modify its inference pipeline to enable online perception from streaming images: 1) Input selection.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Due to the huge domain gap between the real-world and synthetic dataset, our EmbodiedSplat fails to achieve the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Splat [18] shares the same limitations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Our model shows strong semantics generalizability in ScanNet++ →ScanNet transfer with performance degradation remaining below 1 mIoU compared ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (1. Introduction), p. 3 (3. Preliminaries), p. 3 (3. Preliminaries), p. 4 (4.1. EmbodiedSplat). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminaries), interface p. 1 (1. Introduction), p. 3 (3. Preliminaries), p. 3 (3. Preliminaries), p. 4 (4.1. EmbodiedSplat), objective p. 2 (1) They require per-scene optimization that cannot be gen), p. 4 (4.1. EmbodiedSplat), p. 4 (4.1. EmbodiedSplat), p. 5 (4.1. EmbodiedSplat), p. 6 (Method), p. 6 (Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
