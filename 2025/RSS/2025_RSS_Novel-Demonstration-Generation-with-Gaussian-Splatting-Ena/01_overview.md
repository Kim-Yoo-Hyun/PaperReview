# Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p146.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p146.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: Sizhe Yang, Wenye Yu, Jia Zeng, Jun Lv, Kerui Ren, Cewu Lu, Dahua Lin, Jiangmiao Pang
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, synthetic data, demonstration generation, 3D perception, sim-to-real, manipulation
- Official paper: https://www.roboticsproceedings.org/rss21/p146.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p146.pdf
- Code/Project: https://yangsizhe.github.io/robosplat/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RoboSplat은 한 번의 실제 시연을 3D 가우시안 장면으로 재구성하고 이를 편집해 새로운 관측과 조작 시연을 합성한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p146.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Visuomotor policies learned from teleoperated, demonstrations face challenges such as lengthy data collection, high costs, and ting approaches address these issues by augmenting image observations ...
- **p. 1 / Abstract - extractive body cue:** However, the former is constrained to 2D data augmentation, while the latler suffers from imprecise physical
- **p. 1 / Abstract - extractive body cue:** Scene, and augment data across six types of generalization with, five techniques: 3D Gaussian replacement for varying object types, scene appearance, and robot embodiments; equivariant ...
- **p. 1 / Abstract - extractive body cue:** fe real-world experiments demonstrate that ces the generalization of visuomo
- **p. 1 / Abstract - extractive body cue:** tor policies under diverse disturbances.
- **p. 1 / 1. INrRopucTION - extractive body cue:** However, the Sim-to-Real gap presents
- **p. 3 / C. Gaussian planting in Roboties - extractive body cue:** However, importing reconstructed real-world objects to simulation is a strenuous process, and physical interactions tend to suffer from large sim-to-real gaps due to the flawed ...

## Core Idea

- **p. 3 / C. Gaussian planting in Roboties - extractive body cue:** Our method enables autonomous editing of the reconstructed scene to generate diverse demonstrations with various configurations.
- **p. 3 / IV. METHODOLOGY - extractive body cue:** To generate high-fidelity and diverse data from a single expert trajectory, we present RoboSplat, a novel demonstration generation approach based on 3DGS.
- **p. 2 / 1. INrRopucTION - extractive body cue:** Thanks t0 its explicit representation of the scene, 3DGS enables interpretable editing ofthe reconstructed scene, which paves the way for generating novel manipulation configurations, Furthermore, ...
- **p. 2 / 1. INrRopucTION - extractive body cue:** Based on that, we propose RoboSplat, a novel and efficacious approach to demonstration generation with Gaussian ‘Splatting.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation
- **p. 2 / A. Generalizable Policy in Robot Manipulation - extractive body cue:** Instead of adopting generalizable policy architecture, auxiliary learning objectives ‘and powerful foundation models, our work is concentrated on generating high-quality, diverse, and realistic data to ...
- **p. 6 / C. Policy Training - extractive body cue:** The latent of images and robot state is fed into a transformer encoder.
- **p. 6 / C. Policy Training - extractive body cue:** We employ a modem, widely adopted transformer-based architecture [18, 51, 38, 55] to serve as the policy network, which is detailed in Appendix C.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The images. camera poses, and depth prior serve as inputs to 3DGS [25], which returns 3D. ‘Gaussians representing the entire scene Gucene, Which contains 3D Gaussians corresponding to the robot, dubbed Grope«. | observation history와 expert trajectory/action | p. 4 (A. Reconstruction and Preprocessing), p. 6 (C. Policy Training) |
| State/latent | images, camera, poses, depth, prior, serve, inputs, DGS, returns, Gaussians, representing, entire | behavior policy와 temporal action context | p. 4 (A. Reconstruction and Preprocessing), p. 6 (C. Policy Training), p. 6 (C. Policy Training) |
| Output/action | We denote 0, # (Ii, 4x) as the observation at the k-th frame of demonstrations D, and as our policy. | predicted action 또는 action chunk | p. 6 (C. Policy Training), p. 6 (C. Policy Training), p. 2 (B. Data Augmentation for Policy Learning) |
| Objective/outcome | The camera extrinsies are optimized through gradient descent, with the optimization objective: | imitation error, task success, robustness와 compounding error | p. 5 (A. Reconstruction and Preprocessing), p. 6 (C. Policy Training), p. 6 (C. Policy Training) |

## Main Claims and Actual Contribution

- 물체·장면·로봇 형상 교체, 자세 변환과 새 시점 렌더링을 이용해 시연의 공간·시각 조건을 바꾼다. [PDF 3쪽](https://www.roboticsproceedings.org/rss21/p146.pdf#page=3) · [PDF 4쪽](https://www.roboticsproceedings.org/rss21/p146.pdf#page=4)
- 여섯 종류의 변화가 가해진 실제 조작에서 단일 시연 기반 학습을 다수 시연 및 2D 증강 기준선과 비교했다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p146.pdf#page=1) · [PDF 6쪽](https://www.roboticsproceedings.org/rss21/p146.pdf#page=6)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 10 (Figure/Table caption), p. 7 (A. Experimental Setup) |
| Embodiment/environment | We design five manipulation tasks for real-world evaluation: Pick Object, Close Drawer, Pick-PlaceClose, Dual Pick-Place and Sweep, whose details are elaborated in Sec. | hardware/simulator version and reset protocol | p. 7 (A. Experimental Setup), p. 6 (A. Experimental Setup) |
| Dataset/benchmark | In Sweep task, the robot should first pick up a broom and then sweeps the chocolate beans into a dustpan. | role, split, size and leakage | p. 7 (A. Experimental Setup), p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup), p. 7 (A. Experimental Setup) |
| Metric | Success rate (SR) is chosen as the evaluation metric in all experiments. | definition, denominator, direction and uncertainty | p. 7 (A. Experimental Setup), p. 9 (Figure/Table caption), p. 10 (Figure/Table caption) |
| Baseline/ablation | Fig. 3: Comparison of frame alignment results between ICP and fine-grained optimization with differentiable ren- dering. The semi-transparent orange overlay represents the ground truth rendered with URDE from the same camera view: ... | fair input/data/compute/action matching | p. 4 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 6 / A. Experimental Setup - extractive body cue:** The drawer is placed in a Sem%Sem workspace, with a fixed orientation, The target object is located in a 1em> 10em workspace, whose rotation falls ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Starting from a single expert demonstration and multi-view images, our method generates diverse and visu realistic data for policy learning, enabling robust performance ...
- **p. 7 / B. Eficiency of Augmenting Demonstrations - extractive body cue:** Robustness when Facing Various Deployment Settings
- **p. 8 / 2) Scene Appearance - extractive body cue:** In particular, our policy achieves 100% success rate on the Pick Object task, showcasing strong robustness against various background appearance.
- **p. 8 / 4) 3200 generated demonstrations with camera view aug - extractive body cue:** Notably, our policy achieves nearly 100% success rate (on Close Drawer task, manifesting strong robustness against novel camera views and moving cameras,
- **p. 9 / 3) 6400 demonstrations generated by our pipeline with ob - extractive body cue:** The data is collected in the original setting, ‘When deploying the trained policy, we modify object poses, lighting conditions, scene appearance, camera views, object types, ...
- **p. 9 / 5) Embodiment Type - extractive body cue:** To prove that, based on one demonstration collected with the Franka Research 3, we generate novel demonstrations for a URSe robot equipped with a Robotiq ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. INrRopucTION), p. 3 (C. Gaussian planting in Roboties), p. 2 (B. Data Augmentation for Policy Learning), p. 1 (Abstract), p. 2 (1. INrRopucTION), p. 2 (A. Generalizable Policy in Robot Manipulation)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, importing reconstructed real-world objects to simulation is a strenuous process, and physical interactions tend to suffer from large sim-to-real gaps due to the flawed geometric reconstruc tion and lack ... (p. 3, C. Gaussian planting in Roboties).
- **Actual contribution:** To generate high-fidelity and diverse data from a single expert trajectory, we present RoboSplat, a novel demonstration generation approach based on 3DGS. (p. 3, IV. METHODOLOGY).
- **Evaluation boundary:** Success rate (SR) is chosen as the evaluation metric in all experiments. (p. 7, A. Experimental Setup).
- **Explicit failure boundary:** The drawer is placed in a Sem%Sem workspace, with a fixed orientation, The target object is located in a 1em> 10em workspace, whose rotation falls into range [~E, 3]. (p. 6, A. Experimental Setup).

## 원문과 공개 자료

- 코드 · 3D 장면 편집으로 단일 시연을 증강하는 구현 · data_aug/generate_demo.py [배포 파일](https://raw.githubusercontent.com/InternRobotics/robosplat/372c9c735555ea79ffab1361afd4ca20f4ff1105/data_aug/generate_demo.py)
- 데이터 · RoboSplat 저자 배포처의 데이터 및 장면 자산 압축본 · data.zip [배포 파일](https://drive.google.com/file/d/1i8bmdUAE_bf4ZP3-E5slG-PIoto9fyaA/view)
