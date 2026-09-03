# Problem - Dynam3D: Dynamic Layered 3D Tokens Empower VLM for Vision-and-Language Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=s6k9l5yX8e; PDF retrieval source: https://arxiv.org/pdf/2505.11383. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction)): 2) These models lack mechanisms for structured scene memory.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Vision-and-Language Navigation (VLN) is a core task where embodied agents leverage their spatial mobility to navigate in 3D environments toward designated destinations based on natural ...
- **p. 1 / Abstract - extractive body cue:** Recently, video-language large models (Video-VLMs) with strong generalization capabilities and rich commonsense knowledge have shown remarkable performance when applied to VLN tasks.
- **p. 1 / Abstract - extractive body cue:** However, these models still encounter the following challenges when applied to real-world 3D navigation: 1) Insufficient understanding of 3D geometry and spatial semantics; 2) Limited ...
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we propose Dynam3D, a dynamic layered 3D representation model that leverages language-aligned, generalizable, and hierarchical 3D representations as visual input to ...
- **p. 1 / Abstract - extractive body cue:** Given posed RGB-D images, our Dynam3D projects 2D CLIP features into 3D space and constructs multi-level 3D patch-instance-zone representations for 3D geometric and semantic understanding ...
- **p. 1 / 1 Introduction - extractive body cue:** 2) These models lack mechanisms for structured scene memory.
- **p. 1 / 1 Introduction - extractive body cue:** Despite these recent advances, several limitations still remain: 1) Video-based models struggle to capture spatial geometry and semantics in large-scale 3D environments.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | 2) These models lack mechanisms for structured scene memory. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | To address these limitations, we propose Dynam3D, a dynamic layered 3D representation model that leverages language-aligned, generalizable, and hierarchical 3D representations as ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | address, limitations, Dynam3D, dynamic, layered, representation, model, leverages, language-aligned, generalizable | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | models, pre-trained, large-scale, internet, data, demonstrate, strong, language | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: address, limitations, Dynam3D, dynamic, layered, representation, model, leverages, language-aligned, generalizable | p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Decision / output variable | path/waypoint/velocity; body terms: summary, main, contributions, include, Dynam3D, multi-level, patch-instance-zone, representation | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: practical, constraint, most, robots, equipped, monocular, cameras, instead | p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Success / guarantee | goal reach with collision-free execution | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** Despite these recent advances, several limitations still remain: 1) Video-based models struggle to capture spatial geometry and semantics in large-scale 3D environments.
- **p. 2 / 1 Introduction - extractive body cue:** We propose Dynam3D to alleviate the limitations mentioned above.
- **p. 2 / 1 Introduction - extractive body cue:** As a result, this enables high-level comprehension of layouts, e.g. bedrooms, kitchens, etc that instance-level features alone cannot capture. our Dynam3D updates the scene dynamically ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (1 Introduction)): In summary, our main contributions include: • We propose Dynam3D, a multi-level patch-instance-zone 3D representation model that performs online 3D instance and zone-level encoding and real-time hierarchical updates in dynamic ...

- **p. 2 / 1 Introduction - extractive body cue:** We propose Dynam3D to alleviate the limitations mentioned above.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we propose Dynam3D, a dynamic layered 3D representation model that leverages language-aligned, generalizable, and hierarchical 3D representations as visual input to ...
- **p. 1 / 1 Introduction - extractive body cue:** As illustrated in Figure 1(a), recent works [5-7] have predominantly focused on using video-based large models [8-10] to develop monocular VLN systems.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 2 | Figure 1: Different vision-language large models for monocular VLN tasks. Compared to previous video-based representations (a), our Dynam3D ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | The navigation performance significantly decreases without Subspace Alignment supervision (Table 6, row 3), highlighting the limitations of naive ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | In the dynamic setting (Figure 4 and Table 5), the target is manually moved to another location once ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), objective p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
