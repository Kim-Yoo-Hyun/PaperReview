# 3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss20/p067.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss20/p067.html. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RSS
- Authors: Yanjie Ze, Gu Zhang, Kangning Zhang, Chenyuan Hu, Muhan Wang, Huazhe Xu
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: CORE
- Tags: Robotics, 3D representation, point cloud, diffusion policy, Imitation Learning, visuomotor control
- Official paper: https://www.roboticsproceedings.org/rss20/p067.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss20/p067.html
- Code/Project: https://3d-diffusion-policy.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 To collect the required extensive number of demonstrations, the entire data-gathering process can span several days due to its long-horizon nature and failure-prone process.를 문제로 두고, To this end, we introduce 3D Diffusion Policy (DP3), which mainly consists of two critical parts: (a) Perception.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Imitation learning provides an efficient way to teach robots dexterous skills; however, learning complex skills robustly and generalizablely usually consumes large amounts of human demonstrations.
- **p. 1 / Abstract - extractive body cue:** To tackle this challenging problem, we present 3D Diffusion Policy (DP3), a novel visual imitation learning approach that incorporates the power of 3D visual representations ...
- **p. 1 / Abstract - extractive body cue:** The core design of DP3 is the utilization of a compact 3D visual representation, extracted from sparse point clouds with an efficient point encoder.
- **p. 1 / Abstract - extractive body cue:** In our experiments involving 72 simulation tasks, DP3 successfully handles most tasks with just 10 demonstrations and surpasses baselines with a 24.2% relative improvement.
- **p. 1 / Abstract - extractive body cue:** In 4 real robot tasks, DP3 demonstrates precise control with a high success rate of 85%, given only 40 demonstrations of each task, and shows ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To collect the required extensive number of demonstrations, the entire data-gathering process can span several days due to its long-horizon nature and failure-prone process.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Nevertheless, online learning in real-world scenarios introduces its own challenges, such as safety considerations, the necessity for automatic resetting, human intervention, and additional robot hardware ...

## Core Idea

- **p. 3 / III. METHOD - extractive body cue:** To this end, we introduce 3D Diffusion Policy (DP3), which mainly consists of two critical parts: (a) Perception.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To tackle this challenging problem, we introduce 3D Diffusion Policy (DP3), a simple yet effective visual imitation learning algorithm that integrates the strengths of 3D ...
- **p. 3 / III. METHOD - extractive body cue:** The network, termed as DP3 Encoder, is conceptually simple: it consists of a three-layer MLP, a max-pooling function as an order-equivariant operation to pool point ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To comprehensively evaluate DP3, we have developed a simulation benchmark comprising 72 diverse robotic tasks from 7 domains, alongside 4 real-world tasks including challenging dexterous ...
- **p. 3 / III. METHOD - extractive body cue:** The decision module in DP3 is formulated as a conditional denoising diffusion model [23, 10, 39] that conditions on 3D visual features v and robot ...
- **p. 4 / III. METHOD - extractive body cue:** We use DDIM [62] as the noise scheduler and use sample prediction instead of epsilon prediction for better high-dimensional action generation, with 100 timesteps at ...
- **p. 4 / III. METHOD - extractive body cue:** (a) End-to-End Training Policy Expert Demonstrations (b) Evaluation Action Observation Decision: Diffusion Policy Single-view Point Cloud Crop FPS Linear Perception: Compact 3D Representations from Point ...
- **p. 6 / 2) Learning efficiency. While we train all the algorithms - extractive body cue:** We replace the visual observation and the corresponding encoder in DP3 to evaluate different 3D representations.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (a) End-to-End Training Policy Expert Demonstrations (b) Evaluation Action Observation Decision: Diffusion Policy Single-view Point Cloud Crop FPS Linear Perception: Compact 3D Representations from Point Clouds Compact 3D Repr. | RGB-D/point cloud, object state와 contact/task observation | p. 4 (III. METHOD), p. 3 (III. METHOD) |
| State/latent | End-to-End, Training, Policy, Expert, Demonstrations, Evaluation, Action, Observation, Decision, Diffusion, Single-view, Point | object geometry, affordance, contact mode 또는 end-effector state | p. 4 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Output/action | Given a small set of expert demonstrations that contain complex robot skill trajectories, we want to learn a visuomotor policy π : O 7→A that maps the visual observations o ∈O to ... | grasp, pose, force 또는 end-effector trajectory | p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 6 (2) Learning efficiency. While we train all the algorithms) |
| Training objective / implementation boundary | 원문 대조: 식 (2)는 3D visual feature v와 robot pose q에 조건화한 noise-prediction MSE를 설명한다. 같은 페이지의 구현 설명은 DDIM과 sample prediction을 사용한다고 명시하므로, 개념식과 실제 prediction parameterization을 구분해야 한다. ([PDF p. 4](https://www.roboticsproceedings.org/rss20/p067.pdf#page=4), §III-C Decision, Eq. (2) and Implementation details) | 개념 noise loss와 실제 sample prediction을 구분 | [PDF p. 4](https://www.roboticsproceedings.org/rss20/p067.pdf#page=4), §III-C Decision, Eq. (2) and Implementation details |

## Main Claims and Actual Contribution

- **p. 3 / III. METHOD - extractive body cue:** To this end, we introduce 3D Diffusion Policy (DP3), which mainly consists of two critical parts: (a) Perception.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To tackle this challenging problem, we introduce 3D Diffusion Policy (DP3), a simple yet effective visual imitation learning algorithm that integrates the strengths of 3D ...
- **p. 3 / III. METHOD - extractive body cue:** The network, termed as DP3 Encoder, is conceptually simple: it consists of a three-layer MLP, a max-pooling function as an order-equivariant operation to pool point ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To comprehensively evaluate DP3, we have developed a simulation benchmark comprising 72 diverse robotic tasks from 7 domains, alongside 4 real-world tasks including challenging dexterous ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Overview of 3D Diffusion Policy (DP3). Above: In the training phase, DP3 simultaneously trains its perception module and decision-making process in an end-to-end ...
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** We observe that DP3 achieves a success rate exceeding 90% in TABLE III: Task suite of DP3, including Adroit [49], BiDexHands [8], DexArt [5], DexDeform ...
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** The success rates for experts are given in Appendix C.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Learning efficiency. We sample 12 simulation tasks and show the learning curves of DP3 and Diffusion Policy. DP3 demonstrates a rapid convergence towards ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 4 (Figure/Table caption), p. 5 (IV. SIMULATION EXPERIMENTS) |
| Embodiment/environment | Simulation Benchmark (72 Tasks) Domain Robo Object Simulator ActD #Task #Demo Adroit Shadow Rigid/Art MuJoCo 28 3 10 Bi-DexHands Shadow Rigid/Art IsaacGym 52 6 10 DexArt Allegro Art Sapien 22 4 100 ... | hardware/simulator version and reset protocol | p. 5 (IV. SIMULATION EXPERIMENTS), p. 7 (V. REAL WORLD EXPERIMENTS) |
| Dataset/benchmark | This discrepancy underscores two key aspects: (a) the importance of real robot experiments and (b) the necessity of large-scale diverse simulation tasks for more sci | role, split, size and leakage | p. 5 (IV. SIMULATION EXPERIMENTS), p. 7 (V. REAL WORLD EXPERIMENTS), p. 4 (IV. SIMULATION EXPERIMENTS), p. 4 (IV. SIMULATION EXPERIMENTS) |
| Metric | The success rates for experts are given in Appendix C. | definition, denominator, direction and uncertainty | p. 5 (IV. SIMULATION EXPERIMENTS), p. 5 (IV. SIMULATION EXPERIMENTS), p. 4 (Figure/Table caption) |
| Baseline/ablation | To this end, our main baseline is the image-based diffusion policy [10], simply referred to as Diffusion Policy. | fair input/data/compute/action matching | p. 5 (IV. SIMULATION EXPERIMENTS), p. 4 (Figure/Table caption), p. 6 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Generalization in 3D space with few data. We use MetaWorld Reach as an example task, given only 5 demonstra- tions (visualized by •). ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6: Efficient scaling with demonstrations. We sample 10 simulation tasks and train DP3 and Diffusion Policy with an increasing number of demonstrations. DP3 addresses ...
- **p. 8 / 2) Dumpling. The Allegro hand first wraps the plasticine - extractive body cue:** For instance, the image-based diffusion policy excels in the Drill task but fails entirely in Roll-Up.
- **p. 8 / 2) Dumpling. The Allegro hand first wraps the plasticine - extractive body cue:** It is noteworthy that the depthbased diffusion policy also does not incorporate color as input.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: 3D Diffusion Policy (DP3) is a visual imitation learning algorithm that marries 3D visual representations with diffusion policies, achieving surprising effectiveness in diverse ...
- **p. 9 / 2) Dumpling. The Allegro hand first wraps the plasticine - extractive body cue:** Accurate transformation isn't necessary due to the robustness of our network.

## Why Read It

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 To collect the required extensive number of demonstrations, the entire data-gathering process can span several days due to its long-horizon nature and failure-prone process.를 문제로 두고, To this end, we introduce 3D Diffusion Policy (DP3), which mainly consists of two critical parts: (a) Perception.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Nevertheless, online learning in real-world scenarios introduces its own challenges, such as safety considerations, the necessity for automatic resetting, human intervention, and additional robot hardware costs. (p. 1, I. INTRODUCTION).
- **Actual contribution:** To this end, we introduce 3D Diffusion Policy (DP3), which mainly consists of two critical parts: (a) Perception. (p. 3, III. METHOD).
- **Evaluation boundary:** Fig. 2: Overview of 3D Diffusion Policy (DP3). Above: In the training phase, DP3 simultaneously trains its perception module and decision-making process in an end-to-end manner using expert demonstrations. During ... (p. 4, Figure/Table caption).
- **Explicit failure boundary:** DP3 learns the generalizable skill in 3D space; Diffusion Policy and IBC [11] only succeed in partial space; BC-RNN [35] fails to learn such a simple skill with limited data. (p. 4, III. METHOD).
