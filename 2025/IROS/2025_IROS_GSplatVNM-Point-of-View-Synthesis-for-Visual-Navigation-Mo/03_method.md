# Method - GSplatVNM: Point-of-View Synthesis for Visual Navigation Models Using Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2503.05152; PDF retrieval source: https://arxiv.org/pdf/2503.05152. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (IV. VISUAL NAVIGATION WITH 3DGS), p. 3 (IV. VISUAL NAVIGATION WITH 3DGS), p. 3 (IV. VISUAL NAVIGATION WITH 3DGS), p. 4 (IV. VISUAL NAVIGATION WITH 3DGS), p. 2 (III. 3DGS AS ENVIRONMENT REPRESENTATION), p. 5 (2) Pre-Collection)): NoMaD consists of three networks: • A subgoal image-conditioned vision encoder, ct = fenc(Oobs,Itarget), that extracts context features from the observation Oobs and target subgoal image Itarget. • A diffusion ...

## Method Body Digest

- **p. 4 / IV. VISUAL NAVIGATION WITH 3DGS - extractive body cue:** NoMaD consists of three networks: • A subgoal image-conditioned vision encoder, ct = fenc(Oobs,Itarget), that extracts context features from the observation Oobs and target subgoal ...
- **p. 3 / IV. VISUAL NAVIGATION WITH 3DGS - extractive body cue:** Given the start and goal images, we first estimate the robot's start and goal poses in 3DGS and then plan a global trajectory within the ...
- **p. 3 / IV. VISUAL NAVIGATION WITH 3DGS - extractive body cue:** Specifically, we use the Learned Perceptual Image Patch Similarity (LPIPS) metric [27], which is computed from the feature maps of AlexNet [28] and ranges from ...
- **p. 4 / IV. VISUAL NAVIGATION WITH 3DGS - extractive body cue:** These rendered images are then used to condition the NoMaD policy to generate spatial waypoints.
- **p. 2 / III. 3DGS AS ENVIRONMENT REPRESENTATION - extractive body cue:** By training the parameters of 3DGS to minimize a reprojection error across multiple views, we obtain a compact and renderable representation of the environment.
- **p. 5 / 2) Pre-Collection - extractive body cue:** The shortest path length is computed using the Dijkstra algorithm on the traversable area map provided by the simulator.
- **p. 5 / 2) Pre-Collection - extractive body cue:** Therefore, we utilize variants of the same NoMaD policy for all methods to ensure a fair comparison of the representation itself.
- **p. 3 / IV. VISUAL NAVIGATION WITH 3DGS - extractive body cue:** In this work, we optimize the global start and goal poses, qstart and qgoal, by minimizing the following loss function L: L(q∗) = Limg(I∗,Irendered(q∗))+1collision[dmin(q∗) ≤r], ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** 3DGS is a neural model that enables high-quality 3D reconstruction of the environment from a pre-collected image database (DB) and can further synthesize novel images ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose GSplatVNM, a new visionbased navigation framework that requires reduced data collection.
- **p. 2 / A. ITG-based Visual Navigation - extractive body cue:** In contrast, our method uses 3DGS as an offline environment model solely to synthesize a sequence of target viewpoints.

## Source Evidence Cues

- **p. 4 / IV. VISUAL NAVIGATION WITH 3DGS - extractive body cue:** NoMaD consists of three networks: • A subgoal image-conditioned vision encoder, ct = fenc(Oobs,Itarget), that extracts context features from the observation Oobs and target subgoal ...
- **p. 3 / IV. VISUAL NAVIGATION WITH 3DGS - extractive body cue:** Given the start and goal images, we first estimate the robot's start and goal poses in 3DGS and then plan a global trajectory within the ...
- **p. 3 / IV. VISUAL NAVIGATION WITH 3DGS - extractive body cue:** Specifically, we use the Learned Perceptual Image Patch Similarity (LPIPS) metric [27], which is computed from the feature maps of AlexNet [28] and ranges from ...
- **p. 4 / IV. VISUAL NAVIGATION WITH 3DGS - extractive body cue:** These rendered images are then used to condition the NoMaD policy to generate spatial waypoints.
- **p. 2 / III. 3DGS AS ENVIRONMENT REPRESENTATION - extractive body cue:** By training the parameters of 3DGS to minimize a reprojection error across multiple views, we obtain a compact and renderable representation of the environment.
- **p. 5 / 2) Pre-Collection - extractive body cue:** The shortest path length is computed using the Dijkstra algorithm on the traversable area map provided by the simulator.
- **p. 5 / 2) Pre-Collection - extractive body cue:** Therefore, we utilize variants of the same NoMaD policy for all methods to ensure a fair comparison of the representation itself.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | NoMaD consists of three networks: • A subgoal image-conditioned vision encoder, ct = fenc(Oobs,Itarget), that extracts context features from the observation Oobs ... | p. 4 (IV. VISUAL NAVIGATION WITH 3DGS), p. 3 (IV. VISUAL NAVIGATION WITH 3DGS) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Given the start and goal images, we first estimate the robot's start and goal poses in 3DGS and then plan a global ... | p. 3 (IV. VISUAL NAVIGATION WITH 3DGS), p. 3 (IV. VISUAL NAVIGATION WITH 3DGS) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | Specifically, we use the Learned Perceptual Image Patch Similarity (LPIPS) metric [27], which is computed from the feature maps of AlexNet [28] ... | p. 3 (IV. VISUAL NAVIGATION WITH 3DGS), p. 4 (IV. VISUAL NAVIGATION WITH 3DGS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / IV. VISUAL NAVIGATION WITH 3DGS - extractive body cue:** In this work, we optimize the global start and goal poses, qstart and qgoal, by minimizing the following loss function L: L(q∗) = Limg(I∗,Irendered(q∗))+1collision[dmin(q∗) ≤r], ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Therefore, reducing overall data collection costs is essential for deploying robots in these settings.
- **p. 1 / I. INTRODUCTION - extractive body cue:** These results demonstrate that GSplatVNM can significantly reduce data collection costs while maintaining a continuous set of feasible target point-of-view images.
- **p. 2 / III. 3DGS AS ENVIRONMENT REPRESENTATION - extractive body cue:** By training the parameters of 3DGS to minimize a reprojection error across multiple views, we obtain a compact and renderable representation of the environment.
- **p. 2 / A. ITG-based Visual Navigation - extractive body cue:** However, as the number of nodes increases, the boundary between ITG and metric maps becomes blurred, and the computational and storage costs increase significantly.
- **p. 3 / IV. VISUAL NAVIGATION WITH 3DGS - extractive body cue:** A* search considers collisions between the robot and the 3DGS as well as the loss function (2).
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 3 (IV. VISUAL NAVIGATION WITH 3DGS), p. 3 (IV. VISUAL NAVIGATION WITH 3DGS), p. 1 (I. INTRODUCTION), p. 2 (III. 3DGS AS ENVIRONMENT REPRESENTATION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Zero-shot, Local, Planning, Control, NoMaD, visual, subgoal-conditioned, policy, generates, spatial, waypoints, sequence, observation, images | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Zero-shot, Local, Planning, Control, NoMaD, visual, subgoal-conditioned, policy, generates, spatial | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | DGS, neural, model, enables, high-quality, reconstruction, environment, pre-collected, image, database | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | optimize, global, start, goal, poses, qstart, qgoal, minimizing, following, loss | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / IV. VISUAL NAVIGATION WITH 3DGS - extractive body cue:** Zero-shot Local Planning and Control with NoMaD NoMaD [3] is a visual subgoal-conditioned policy that generates spatial waypoints from a sequence of observation images at ...
- **p. 4 / IV. VISUAL NAVIGATION WITH 3DGS - extractive body cue:** NoMaD consists of three networks: • A subgoal image-conditioned vision encoder, ct = fenc(Oobs,Itarget), that extracts context features from the observation Oobs and target subgoal ...
- **p. 5 / 2) Pre-Collection - extractive body cue:** ITG) on a stateof-the-art zero-shot navigation policy, rather than conducting a broad comparison of different navigation policies such as GNM [1] or ViNT [2].
- **p. 2 / A. ITG-based Visual Navigation - extractive body cue:** Our core contribution is therefore the integration of 3DGS as a viewpoint generator to guide a localization-free policy, rather than using it as a map ...
- **p. 3 / IV. VISUAL NAVIGATION WITH 3DGS - extractive body cue:** We subsequently render target pointof-view images along the planned trajectory to condition the VNM, i.e., NoMaD [3], which is a state-of-the-art VNM.
- **p. 3 / IV. VISUAL NAVIGATION WITH 3DGS - extractive body cue:** During navigation, NoMaD generates spatial waypoints from the observation images and the synthesized target point-of-view images, and the robot follows these waypoints using Model Predictive ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** We leverage these capabilities of 3DGS to localize the start and goal poses from a given pair of images and connect them by synthesizing a ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | A trial is considered successful if the robot reaches the goal within a specified distance (0.5 m for Greigsville and Ribera, and ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | We validate the proposed GSplatVNM framework in photorealistic simulation environments [8], [9]. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | A trial is considered successful if the robot reaches the goal within a specified distance (0.5 m for Greigsville and Ribera, and ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / III. 3DGS AS ENVIRONMENT REPRESENTATION - extractive body cue:** By training the parameters of 3DGS to minimize a reprojection error across multiple views, we obtain a compact and renderable representation of the environment.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** NoMaD, consists, three, networks, subgoal, image-conditioned, vision, encoder, fenc, Oobs, Itarget, extracts, context, features, observation, target, image, diffusion, model, policy.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Simulation Setup 1) Robot Setup: We simulate a circular wheeled robot (radius: 0.5 m) that navigates the environment using the Habitat simulator ... | p. 4 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS) |
| Global / local decision | Fig. 4. Trajectories of the image collection and selected navigation results for each environment. GSplatVNM can generate point-of-view images that are not ... | p. 6 (Figure/Table caption), p. 5 (Figure/Table caption) |
| Motion execution / recovery | In our experiments, we compare the proposed method with conventional methods in terms of success rate, path efficiency, and robustness with respect ... | p. 4 (V. EXPERIMENTS), p. 3 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 3 / IV. VISUAL NAVIGATION WITH 3DGS - extractive body cue:** The second term is a collision penalty to avoid the infeasibility of global planning.
- **p. 3 / IV. VISUAL NAVIGATION WITH 3DGS - extractive body cue:** A* search considers collisions between the robot and the 3DGS as well as the loss function (2).
- **p. 4 / V. EXPERIMENTS - extractive body cue:** In our experiments, we assume that the robot is equipped with a collision avoidance system independent of NoMaD.
- **p. 4 / V. EXPERIMENTS - extractive body cue:** Consequently, the simulator restricts the robot from leaving the traversable area, and collision avoidance performance is not evaluated2.
- **p. 5 / 2) Pre-Collection - extractive body cue:** In contrast, GSplatVNM demonstrates robustness with respect to the image DB size in terms of SPL.
- **p. 5 / 2) Pre-Collection - extractive body cue:** In contrast, NoMaD w/ ITG shows significant degradation in SPL as the image DB size decreases-especially in the Ribera and skokloster-castle environments-due to a reduced ...
- **p. 6 / 2) Pre-Collection - extractive body cue:** In this case, while the baseline methods failed, GSplatVNM succeeded by synthesizing the missing point-of-view images for areas that were observed but not visited.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (IV. VISUAL NAVIGATION WITH 3DGS), p. 3 (IV. VISUAL NAVIGATION WITH 3DGS), p. 3 (IV. VISUAL NAVIGATION WITH 3DGS), p. 4 (IV. VISUAL NAVIGATION WITH 3DGS), p. 2 (III. 3DGS AS ENVIRONMENT REPRESENTATION), p. 5 (2) Pre-Collection), objective p. 3 (IV. VISUAL NAVIGATION WITH 3DGS), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (III. 3DGS AS ENVIRONMENT REPRESENTATION), p. 2 (A. ITG-based Visual Navigation), p. 3 (IV. VISUAL NAVIGATION WITH 3DGS), temporal p. 4 (V. EXPERIMENTS), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (A. ITG-based Visual Navigation), p. 2 (A. ITG-based Visual Navigation), p. 3 (IV. VISUAL NAVIGATION WITH 3DGS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
