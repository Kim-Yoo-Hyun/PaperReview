# Problem - ElasticFusion: Dense SLAM Without A Pose Graph

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss11/p01.html; PDF retrieval source: https://www.roboticsproceedings.org/rss11/p01.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): However, existing dense SLAM methods suitable for incremental, real-time operation struggle when the sensor makes movements which are both of extended duration and often criss-cross loop back on themselves.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We present a novel approach to real-time dense visual SLAM.
- **p. 1 / Abstract - extractive body cue:** Our system is capable of capturing comprehensive dense globally consistent surfel-based maps of room scale environments explored using an RGB-D camera in an incremental online ...
- **p. 1 / Abstract - extractive body cue:** This is accomplished by using dense frame-tomodel camera tracking and windowed surfel-based fusion coupled with frequent model refinement through non-rigid surface deformations.
- **p. 1 / Abstract - extractive body cue:** Our approach applies local model-to-model surface loop closure optimisations as often as possible to stay close to the mode of the map distribution, while utilising ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In dense 3D SLAM, a space is mapped by fusing the data from a moving sensor into a representation of the continuous surfaces it contains, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, existing dense SLAM methods suitable for incremental, real-time operation struggle when the sensor makes movements which are both of extended duration and often criss-cross ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** As we show in our evaluation of the system in Section VII, this approach to dense SLAM achieves state-of-the-art performance with trajectory estimation results on ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, existing dense SLAM methods suitable for incremental, real-time operation struggle when the sensor makes movements which are both of extended duration ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | As we show in our evaluation of the system in Section VII, this approach to dense SLAM achieves state-of-the-art performance with trajectory ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | evaluation, system, Section, VII, dense, SLAM, achieves, state-of-the-art, performance, trajectory | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | After, pose, graph, optimisation, final, created, merging, surfel | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: evaluation, system, Section, VII, dense, SLAM, achieves, state-of-the-art, performance, trajectory | p. 2 (I. INTRODUCTION), p. 2 (II. APPROACH OVERVIEW), p. 1 (I. INTRODUCTION) |
| Decision / output variable | path/waypoint/velocity; body terms: following, summarise, elements, component, inspired, surfelbased, fusion, system | p. 2 (II. APPROACH OVERVIEW), p. 2 (1) Estimate a fused surfel-based model of the environment), p. 1 (I. INTRODUCTION) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: not recovered | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | goal reach with collision-free execution | p. 7 (VII. EVALUATION), p. 7 (VII. EVALUATION), p. 8 (VII. EVALUATION) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive body cue:** As we show in our evaluation of the system in Section VII, this approach to dense SLAM achieves state-of-the-art performance with trajectory estimation results on ...

## What the Paper Changes

PDF body contribution framing (p. 2 (II. APPROACH OVERVIEW), p. 2 (1) Estimate a fused surfel-based model of the environment), p. 1 (I. INTRODUCTION)): In the following, we summarise the key elements of our method.

- **p. 2 / 1) Estimate a fused surfel-based model of the environment - extractive body cue:** This component of our method is inspired by the surfelbased fusion system of Keller et al.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Pose graph SLAM systems primarily focus on optimising the camera trajectory, whereas our approach (utilising a deformation graph) instead focuses on optimising the map.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | In future work we wish to address the problem of map scalability beyond whole rooms and also investigate ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | We evaluate our approach on all four trajectories in the living room scene (including synthetic noise) providing surface ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (I. INTRODUCTION), p. 2 (II. APPROACH OVERVIEW), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 2 (I. INTRODUCTION), p. 2 (II. APPROACH OVERVIEW), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
