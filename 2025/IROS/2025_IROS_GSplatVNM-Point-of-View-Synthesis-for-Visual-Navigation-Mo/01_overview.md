# GSplatVNM: Point-of-View Synthesis for Visual Navigation Models Using Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2503.05152.
> PDF retrieval source: https://arxiv.org/pdf/2503.05152. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / IROS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Navigation, Gaussian Splatting
- Official paper: https://arxiv.org/abs/2503.05152
- Full-text retrieval: https://arxiv.org/pdf/2503.05152
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Efficient robot navigation relies on the availability of sufficient environmental information; however, the associated data collection costs cannot always be justified.를 문제로 두고, 3DGS is a neural model that enables high-quality 3D reconstruction of the environment from a pre-collected image database (DB) and can further synthesize novel images for arbitrary viewpoints not present in the ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** This paper presents a novel approach to imagegoal navigation by integrating 3D Gaussian Splatting (3DGS) with Visual Navigation Models (VNMs), a method we refer to ...
- **p. 1 / Abstract - extractive body cue:** VNMs offer a promising paradigm for image-goal navigation by guiding a robot through a sequence of point-of-view images without requiring metrical localization or environment-specific training.
- **p. 1 / Abstract - extractive body cue:** However, constructing a dense and traversable sequence of target viewpoints from start to goal remains a central challenge, particularly when the available image database is ...
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we propose a 3DGS-based viewpoint synthesis framework for VNMs that synthesizes intermediate viewpoints to seamlessly bridge gaps in sparse data while ...
- **p. 1 / Abstract - extractive body cue:** Experimental results in a photorealistic simulator demonstrate that our approach not only enhances navigation efficiency but also exhibits robustness under varying levels of image database ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Efficient robot navigation relies on the availability of sufficient environmental information; however, the associated data collection costs cannot always be justified.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Notably, GSplatVNM can even navigate to a point-of-view that has been seen but not visited, a task that has proven difficult for ITG-based methods.

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** 3DGS is a neural model that enables high-quality 3D reconstruction of the environment from a pre-collected image database (DB) and can further synthesize novel images ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose GSplatVNM, a new visionbased navigation framework that requires reduced data collection.
- **p. 2 / A. ITG-based Visual Navigation - extractive body cue:** In contrast, our method uses 3DGS as an offline environment model solely to synthesize a sequence of target viewpoints.
- **p. 2 / A. ITG-based Visual Navigation - extractive body cue:** Our core contribution is therefore the integration of 3DGS as a viewpoint generator to guide a localization-free policy, rather than using it as a map ...
- **p. 4 / IV. VISUAL NAVIGATION WITH 3DGS - extractive body cue:** NoMaD consists of three networks: • A subgoal image-conditioned vision encoder, ct = fenc(Oobs,Itarget), that extracts context features from the observation Oobs and target subgoal ...
- **p. 3 / IV. VISUAL NAVIGATION WITH 3DGS - extractive body cue:** Given the start and goal images, we first estimate the robot's start and goal poses in 3DGS and then plan a global trajectory within the ...
- **p. 3 / IV. VISUAL NAVIGATION WITH 3DGS - extractive body cue:** Specifically, we use the Learned Perceptual Image Patch Similarity (LPIPS) metric [27], which is computed from the feature maps of AlexNet [28] and ranges from ...
- **p. 4 / IV. VISUAL NAVIGATION WITH 3DGS - extractive body cue:** These rendered images are then used to condition the NoMaD policy to generate spatial waypoints.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Zero-shot Local Planning and Control with NoMaD NoMaD [3] is a visual subgoal-conditioned policy that generates spatial waypoints from a sequence of observation images at time (t), Oobs = {It-p,...,It} (with p=3 ... | camera/depth stream, pose, map와 language goal | p. 4 (IV. VISUAL NAVIGATION WITH 3DGS), p. 4 (IV. VISUAL NAVIGATION WITH 3DGS) |
| State/latent | Zero-shot, Local, Planning, Control, NoMaD, visual, subgoal-conditioned, policy, generates, spatial, waypoints, sequence | robot pose, free-space/semantic map와 local goal | p. 4 (IV. VISUAL NAVIGATION WITH 3DGS), p. 4 (IV. VISUAL NAVIGATION WITH 3DGS), p. 5 (2) Pre-Collection) |
| Output/action | NoMaD consists of three networks: • A subgoal image-conditioned vision encoder, ct = fenc(Oobs,Itarget), that extracts context features from the observation Oobs and target subgoal image Itarget. • A diffusion model [33]-based ... | collision-free trajectory 또는 velocity command | p. 4 (IV. VISUAL NAVIGATION WITH 3DGS), p. 5 (2) Pre-Collection), p. 2 (A. ITG-based Visual Navigation) |
| Objective/outcome | In this work, we optimize the global start and goal poses, qstart and qgoal, by minimizing the following loss function L: L(q∗) = Limg(I∗,Irendered(q∗))+1collision[dmin(q∗) ≤r], (2) dmin(q∗) = min i∈{0,...,N-1}di(q∗), ∗∈{start,goal}, wh ... | goal reach, safety, localization error와 replanning latency | p. 3 (IV. VISUAL NAVIGATION WITH 3DGS), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** 3DGS is a neural model that enables high-quality 3D reconstruction of the environment from a pre-collected image database (DB) and can further synthesize novel images ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose GSplatVNM, a new visionbased navigation framework that requires reduced data collection.
- **p. 2 / A. ITG-based Visual Navigation - extractive body cue:** In contrast, our method uses 3DGS as an offline environment model solely to synthesize a sequence of target viewpoints.
- **p. 2 / A. ITG-based Visual Navigation - extractive body cue:** Our core contribution is therefore the integration of 3DGS as a viewpoint generator to guide a localization-free policy, rather than using it as a map ...
- **p. 4 / V. EXPERIMENTS - extractive body cue:** In our experiments, we compare the proposed method with conventional methods in terms of success rate, path efficiency, and robustness with respect to the number ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. Overview of the proposed GSplatVNM. In a conventional ITG-based approach, the environment is represented by ITG, and the target point-of-views given to the ...
- **p. 4 / V. EXPERIMENTS - extractive body cue:** Consequently, the simulator restricts the robot from leaving the traversable area, and collision avoidance performance is not evaluated2.
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3. Comparison of the SPL on each environment. where Ntrials is the number of trials, Li is the path length of the i-th trial, ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 4 (V. EXPERIMENTS), p. 3 (Figure/Table caption) |
| Embodiment/environment | Simulation Setup 1) Robot Setup: We simulate a circular wheeled robot (radius: 0.5 m) that navigates the environment using the Habitat simulator API, with state updates every 0.5 seconds. | hardware/simulator version and reset protocol | p. 4 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS) |
| Dataset/benchmark | Simulation Setup 1) Robot Setup: We simulate a circular wheeled robot (radius: 0.5 m) that navigates the environment using the Habitat simulator API, with state updates every 0.5 seconds. | role, split, size and leakage | p. 4 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS) |
| Metric | In our experiments, we compare the proposed method with conventional methods in terms of success rate, path efficiency, and robustness with respect to the number of pre-collected images in the image DB. | definition, denominator, direction and uncertainty | p. 4 (V. EXPERIMENTS), p. 5 (Figure/Table caption), p. 4 (V. EXPERIMENTS) |
| Baseline/ablation | Fig. 4. Trajectories of the image collection and selected navigation results for each environment. GSplatVNM can generate point-of-view images that are not included in the pre-collected image DB, enabling the robot to ... | fair input/data/compute/action matching | p. 6 (Figure/Table caption), p. 5 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 3 / IV. VISUAL NAVIGATION WITH 3DGS - extractive body cue:** The second term is a collision penalty to avoid the infeasibility of global planning.
- **p. 3 / IV. VISUAL NAVIGATION WITH 3DGS - extractive body cue:** A* search considers collisions between the robot and the 3DGS as well as the loss function (2).
- **p. 4 / V. EXPERIMENTS - extractive body cue:** In our experiments, we assume that the robot is equipped with a collision avoidance system independent of NoMaD.
- **p. 4 / V. EXPERIMENTS - extractive body cue:** Consequently, the simulator restricts the robot from leaving the traversable area, and collision avoidance performance is not evaluated2.
- **p. 5 / 2) Pre-Collection - extractive body cue:** In contrast, GSplatVNM demonstrates robustness with respect to the image DB size in terms of SPL.
- **p. 5 / 2) Pre-Collection - extractive body cue:** In contrast, NoMaD w/ ITG shows significant degradation in SPL as the image DB size decreases-especially in the Ribera and skokloster-castle environments-due to a reduced ...
- **p. 6 / 2) Pre-Collection - extractive body cue:** In this case, while the baseline methods failed, GSplatVNM succeeded by synthesizing the missing point-of-view images for areas that were observed but not visited.

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Efficient robot navigation relies on the availability of sufficient environmental information; however, the associated data collection costs cannot always be justified.를 문제로 두고, 3DGS is a neural model that enables high-quality 3D reconstruction of the environment from a pre-collected image database (DB) and can further synthesize novel images for arbitrary viewpoints not present in the ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (IV. VISUAL NAVIGATION WITH 3DGS), p. 3 (IV. VISUAL NAVIGATION WITH 3DGS), p. 3 (IV. VISUAL NAVIGATION WITH 3DGS), p. 4 (IV. VISUAL NAVIGATION WITH 3DGS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
