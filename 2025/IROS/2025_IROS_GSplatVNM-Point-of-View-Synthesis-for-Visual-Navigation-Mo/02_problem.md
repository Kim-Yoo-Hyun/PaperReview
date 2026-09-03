# Problem - GSplatVNM: Point-of-View Synthesis for Visual Navigation Models Using Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2503.05152; PDF retrieval source: https://arxiv.org/pdf/2503.05152. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): Efficient robot navigation relies on the availability of sufficient environmental information; however, the associated data collection costs cannot always be justified.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** This paper presents a novel approach to imagegoal navigation by integrating 3D Gaussian Splatting (3DGS) with Visual Navigation Models (VNMs), a method we refer to ...
- **p. 1 / Abstract - extractive body cue:** VNMs offer a promising paradigm for image-goal navigation by guiding a robot through a sequence of point-of-view images without requiring metrical localization or environment-specific training.
- **p. 1 / Abstract - extractive body cue:** However, constructing a dense and traversable sequence of target viewpoints from start to goal remains a central challenge, particularly when the available image database is ...
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we propose a 3DGS-based viewpoint synthesis framework for VNMs that synthesizes intermediate viewpoints to seamlessly bridge gaps in sparse data while ...
- **p. 1 / Abstract - extractive body cue:** Experimental results in a photorealistic simulator demonstrate that our approach not only enhances navigation efficiency but also exhibits robustness under varying levels of image database ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Efficient robot navigation relies on the availability of sufficient environmental information; however, the associated data collection costs cannot always be justified.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Notably, GSplatVNM can even navigate to a point-of-view that has been seen but not visited, a task that has proven difficult for ITG-based methods.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Efficient robot navigation relies on the availability of sufficient environmental information; however, the associated data collection costs cannot always be justified. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Zero-shot Local Planning and Control with NoMaD NoMaD [3] is a visual subgoal-conditioned policy that generates spatial waypoints from a sequence of ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | Zero-shot, Local, Planning, Control, NoMaD, visual, subgoal-conditioned, policy, generates, spatial | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | ITG, stateof-the-art, zero-shot, navigation, policy, rather, conducting, broad | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: Zero-shot, Local, Planning, Control, NoMaD, visual, subgoal-conditioned, policy, generates, spatial | p. 4 (IV. VISUAL NAVIGATION WITH 3DGS), p. 4 (IV. VISUAL NAVIGATION WITH 3DGS), p. 5 (2) Pre-Collection) |
| Decision / output variable | path/waypoint/velocity; body terms: DGS, neural, model, enables, high-quality, reconstruction, environment, pre-collected | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (A. ITG-based Visual Navigation) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: optimize, global, start, goal, poses, qstart, qgoal, minimizing | p. 3 (IV. VISUAL NAVIGATION WITH 3DGS), p. 3 (IV. VISUAL NAVIGATION WITH 3DGS), p. 1 (I. INTRODUCTION), p. 2 (III. 3DGS AS ENVIRONMENT REPRESENTATION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (III. 3DGS AS ENVIRONMENT REPRESENTATION), p. 2 (A. ITG-based Visual Navigation), p. 3 (IV. VISUAL NAVIGATION WITH 3DGS) |
| Success / guarantee | goal reach with collision-free execution | p. 4 (V. EXPERIMENTS), p. 5 (Figure/Table caption), p. 4 (V. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** Notably, GSplatVNM can even navigate to a point-of-view that has been seen but not visited, a task that has proven difficult for ITG-based methods.

## What the Paper Changes

PDF body contribution framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (A. ITG-based Visual Navigation), p. 2 (A. ITG-based Visual Navigation)): 3DGS is a neural model that enables high-quality 3D reconstruction of the environment from a pre-collected image database (DB) and can further synthesize novel images for arbitrary viewpoints not present ...

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose GSplatVNM, a new visionbased navigation framework that requires reduced data collection.
- **p. 2 / A. ITG-based Visual Navigation - extractive body cue:** In contrast, our method uses 3DGS as an offline environment model solely to synthesize a sequence of target viewpoints.
- **p. 2 / A. ITG-based Visual Navigation - extractive body cue:** Our core contribution is therefore the integration of 3DGS as a viewpoint generator to guide a localization-free policy, rather than using it as a map ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 3 | The second term is a collision penalty to avoid the infeasibility of global planning. | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | A* search considers collisions between the robot and the 3DGS as well as the loss function (2). | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | In our experiments, we assume that the robot is equipped with a collision avoidance system independent of NoMaD. | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Consequently, the simulator restricts the robot from leaving the traversable area, and collision avoidance performance is not evaluated2. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (IV. VISUAL NAVIGATION WITH 3DGS), p. 4 (IV. VISUAL NAVIGATION WITH 3DGS), p. 5 (2) Pre-Collection), p. 2 (A. ITG-based Visual Navigation). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 4 (IV. VISUAL NAVIGATION WITH 3DGS), p. 4 (IV. VISUAL NAVIGATION WITH 3DGS), p. 5 (2) Pre-Collection), p. 2 (A. ITG-based Visual Navigation), objective p. 3 (IV. VISUAL NAVIGATION WITH 3DGS), p. 3 (IV. VISUAL NAVIGATION WITH 3DGS), p. 1 (I. INTRODUCTION), p. 2 (III. 3DGS AS ENVIRONMENT REPRESENTATION).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
