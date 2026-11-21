# Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/icra55743.2025.11127328.
> PDF retrieval source: https://arxiv.org/pdf/2503.05189v1. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICRA
- Authors: Justin Yu, Kush Hari, Karim El-Refai, Arnav Dalal, Justin Kerr, Chung Min Kim, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, Gaussian Splatting, Reinforcement Learning
- Official paper: https://api.crossref.org/works/10.1109/icra55743.2025.11127328
- Full-text retrieval: https://arxiv.org/pdf/2503.05189v1
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

POGS는 초기에 여러 시점에서 관측한 물체의 자세를 이후 스테레오 관측으로 갱신해 조작 중에도 추적을 유지한다. [PDF 1쪽](https://arxiv.org/pdf/2503.05189v1#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Tracking and manipulating irregularly-shaped, previously unseen objects in dynamic environments is important for robotic applications in manufacturing, assembly, and logistics.
- **p. 1 / Abstract - extractive body cue:** Recently introduced Gaussian Splats [1] efficiently model object geometry, but lack persistent state estimation for taskoriented manipulation.
- **p. 1 / Abstract - extractive body cue:** POGS updates object states without requiring expensive rescanning or prior CAD models of objects.
- **p. 1 / Abstract - extractive body cue:** After an initial multi-view scene capture and training phase, POGS uses a single stereo camera to integrate depth estimates along with self-supervised vision encoder features ...
- **p. 1 / Abstract - extractive body cue:** POGS supports grasping, reorientation, and natural language-driven manipulation by refining object pose estimates, facilitating sequential object reset operations with human-induced object perturbations and tool servoing, ...
- **p. 1 / Abstract - extractive body cue:** The challenge is greater when dealing with irregularly shaped objects for which obtaining an accurate Computer-Aided Design (CAD) model is impractical.
- **p. 3 / 6) Object surfaces exhibit low specularity for more robust - extractive body cue:** After each object reset, a human will randomly reconfigure both objects to different poses and the process is repeated until failure.

## Core Idea

- **p. 2 / Abstract - extractive body cue:** This paper makes the following contributions: • Persistent Object Gaussian Splat (POGS), a novel feature field representation for tracking and manipulating previously unseen irregularly shaped ...
- **p. 1 / Abstract - extractive body cue:** To enable online state estimation, tracking, and manipulation of unseen objects in dynamic environments, we present Persistent Object Gaussian Splat (POGS), an editable objectcentric feature ...
- **p. 1 / Abstract - extractive body cue:** (Bottom) A POGS unified representation enables language querying, grasp sampling, and continuous tracking of irregular objects as they move.
- **p. 4 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** The drill handle is fully occluded by the motor body, yet our POGS unified representation enables handle grasping based on previously observed geometry.
- **p. 2 / Abstract - extractive body cue:** Our approach aims to achieve robust online object tracking and scene updating with
- **p. 4 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** We use Nerfstudio's [55] Splatfacto implementation of Gaussian Splatting with the gsplat [53] backend and modify it with the aforementioned image encoders and feature supervision ...
- **p. 4 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** These features are then supervised into the gaussians, enabling the model to render them at deployment time for optimizing object tracking objectives, similar to the ...
- **p. 2 / Abstract - extractive body cue:** Training images are used to optimize a 3DGS, and features extracted from 2D foundation models are distilled into feature fields, producing our POGS unified representation.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | As such objects are moved by humans or robots, POGS can update their state online, allowing for flexible, multi-step tasks that require continuous interaction with dynamic objects, eliminating the need to re-scan ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (Abstract), p. 3 (3) Persistent Object Tracking phase for online tracking) |
| State/latent | objects, moved, humans, robots, POGS, update, state, online, allowing, flexible, multi-step, tasks | geometry, map, object/relationship state | p. 2 (Abstract), p. 3 (3) Persistent Object Tracking phase for online tracking), p. 4 (3) Persistent Object Tracking phase for online tracking) |
| Output/action | To distill 2D object masks into 3D gaussian partitions, we borrow principles from [49, 50] and train a feature embedding encoder Femb that passes an input gaussian mean position⃗ x ∈R3 through ... | point map, pose, scene graph, affordance 또는 query result | p. 3 (3) Persistent Object Tracking phase for online tracking), p. 4 (3) Persistent Object Tracking phase for online tracking), p. 1 (Abstract) |
| Objective/outcome | [50], which operates through two complementary mechanisms: (1) attracting features that belong to the same object mask by minimizing their distance in embedding space, and (2) repelling features from different object masks ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (3) Persistent Object Tracking phase for online tracking), p. 3 (Abstract), p. 4 (3) Persistent Object Tracking phase for online tracking) |

## Main Claims and Actual Contribution

- 가우시안에 의미·시각·그룹 특징을 저장하고 한 대의 스테레오 카메라가 제공하는 깊이와 특징으로 물체 자세를 맞춘다. [PDF 3쪽](https://arxiv.org/pdf/2503.05189v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2503.05189v1#page=4)
- 사람이 옮긴 물체를 원위치에 놓거나 파지 중 어긋난 도구 자세를 복구하는 실물 과제로 추적을 검증했다. [PDF 5쪽](https://arxiv.org/pdf/2503.05189v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2503.05189v1#page=6)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (3) Persistent Object Tracking phase for online tracking), p. 5 (3) Persistent Object Tracking phase for online tracking) |
| Embodiment/environment | As such objects are moved by humans or robots, POGS can update their state online, allowing for flexible, multi-step tasks that require continuous interaction with dynamic objects, eliminating the need to re-scan ... | hardware/simulator version and reset protocol | p. 2 (Abstract), p. 2 (Abstract) |
| Dataset/benchmark | Human & Robot Manipulation We deploy POGS for tracking human and robot manipulation tasks where objects may be in varying poses compared to their initial positions in the scene capture. | role, split, size and leakage | p. 2 (Abstract), p. 2 (Abstract), p. 4 (3) Persistent Object Tracking phase for online tracking), p. 8 (3) Persistent Object Tracking phase for online tracking) |
| Metric | The performance metrics included the maximum and mean number of consecutive successful object resets without losing tracking, the successful object reset rates, and the mean and standard deviation of the translation error ... | definition, denominator, direction and uncertainty | p. 5 (3) Persistent Object Tracking phase for online tracking), p. 3 (6) Object surfaces exhibit low specularity for more robust), p. 6 (3) Persistent Object Tracking phase for online tracking) |
| Baseline/ablation | Similar performance trends were observed in the other tasks, where POGS consistently outperformed ablations that either had depth perception turned off or were optimized with RGB substituting for DINO features. | fair input/data/compute/action matching | p. 5 (3) Persistent Object Tracking phase for online tracking), p. 4 (3) Persistent Object Tracking phase for online tracking), p. 5 (3) Persistent Object Tracking phase for online tracking) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** Another limitation is that objects that are partially occluded (by a hand, a robot gripper, etc.) have less robust tracking compared to fully unobstructed objects ...
- **p. 3 / 6) Object surfaces exhibit low specularity for more robust - extractive body cue:** After each object reset, a human will randomly reconfigure both objects to different poses and the process is repeated until failure.
- **p. 3 / 6) Object surfaces exhibit low specularity for more robust - extractive body cue:** We evaluate this experiment by recording the maximum number of sequential object resets before failure, the object grasp rate, the object place rate, and the ...
- **p. 5 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** Tracking remains running the entire time, and these consecutive object resets continue until POGS loses tracking of the objects, defined as when repeated grasp planning ...
- **p. 6 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** This variation arises because each trial was executed until a grasping failure occurred-i.e., when the error in object state estimation became too high to recover-resulting ...
- **p. 4 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** mask does not exist) is helpful in reducing group feature noise for the scene background (anything in the scene that is not a tracked object).
- **p. 2 / Abstract - extractive body cue:** Our approach aims to achieve robust online object tracking and scene updating with

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (Abstract), p. 3 (6) Object surfaces exhibit low specularity for more robust), p. 4 (3) Persistent Object Tracking phase for online tracking)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** L I M I TAT I O N S One key limitation of this work is that the online tracking frequency is limited to 5Hz on an NVIDIA 4090 GPU ... (p. 6, 3) Persistent Object Tracking phase for online tracking).
- **Actual contribution:** This paper makes the following contributions: • Persistent Object Gaussian Splat (POGS), a novel feature field representation for tracking and manipulating previously unseen irregularly shaped objects. • A robot system ... (p. 2, Abstract).
- **Evaluation boundary:** Jigsaw to Shelf Clothes Iron to Shelf Shoe to Shoerack Tier 1 Tier 2 Tier 1 Tier 2 Tier 1 Tier 2 No Depth No DINO POGS POGS No Depth ... (p. 6, 3) Persistent Object Tracking phase for online tracking).
- **Explicit failure boundary:** Tracking remains running the entire time, and these consecutive object resets continue until POGS loses tracking of the objects, defined as when repeated grasp planning failures occur due to irrecoverable ... (p. 5, 3) Persistent Object Tracking phase for online tracking).
