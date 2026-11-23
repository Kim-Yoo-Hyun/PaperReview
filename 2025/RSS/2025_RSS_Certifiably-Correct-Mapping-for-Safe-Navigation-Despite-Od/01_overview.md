# Certifiably-Correct Mapping for Safe Navigation Despite Odometry Drift

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p007.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p007.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: Devansh R. Agrawal, Rajiv Govindjee, Taekyung Kim, Trushant Adeshara, Jiangbo Yu, Anurekha Ravikumar, Dimitra Panagou
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, safe navigation, mapping, state estimation, uncertainty, formal guarantee
- Official paper: https://www.roboticsproceedings.org/rss21/p007.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p007.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (24 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

시각 주행거리계의 오차가 누적되어도 현재 로봇 주변의 빈 공간을 보수적으로 인증하는 장애물 지도를 제안했다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p007.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Accurate perception, state estimation and mapping, are essential for safe robotic navigation as planners and con- {rollers rely on these components for safety-critical decisions.
- **p. 1 / Abstract - extractive body cue:** However, existing mapping approaches often assume perfect pose estimates, an unrealistic assumption that ean lead to incorrect fbstacle maps and therefore collisions.
- **p. 1 / Abstract - extractive body cue:** This paper introduces a framework for certifiably-correct mapping that ensures that the obstacle map correctly classifies obstacle-ree regions despite the ‘odometry drift in vision-based localization ...
- **p. 1 / Abstract - extractive body cue:** By deflating the safe region based on the incremental odometry error at each timestep, we ensure that the map remains accurate and reliable locally around ...
- **p. 1 / Abstract - extractive body cue:** ur contributions include two approaches to modify popular obstacle mapping paradigms, (I) Safe Flight Corridors, and (Ud) Signed Distance Fields.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Without quantified error bounds, guaranteeing the safety of a closed-loop robotic system remains a challenge.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Although recent advances have achieved significant accuracy improvements (11, 12, 13, 14, 15}, formal error analysis is often lacking.

## Core Idea

- **p. 2 / 1. INTRODUCTION - extractive body cue:** In Section IV and V we introduce the deflation mechanism for both map representations, In Section VI we propose methods to use the certified maps ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** In contrast to [27], this paper assumes that the incremental pose estimate is bounded in a Lie-algebraic sense, which allows ‘our methods to be applied ...
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Our main contributions are as follows:
- **p. 1 / Abstract - extractive body cue:** Simulations using the Replica dataset highlight the efficacy of our methods compared to state of-the-art techniques.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Accurate state estimation and mapping are essential for safe robotic navigation, as planners and controllers rely on perception outputs to ensure the safety of planned ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Assuming the odometry algorithm reports the pose and the covariance of the incremental transform, we propose deflating the supposedly safe region (Sc. is deflated relative ...
- **p. 1 / Abstract - extractive body cue:** Accurate perception, state estimation and mapping, are essential for safe robotic navigation as planners and con- {rollers rely on these components for safety-critical decisions.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Accurate state estimation and mapping are essential for safe robotic navigation, as planners and controllers rely on perception outputs to ensure the safety of planned trajectories (or control actions. | camera/depth stream, pose, map와 language goal | p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION) |
| State/latent | Accurate, state, estimation, mapping, essential, safe, robotic, navigation, planners, controllers, rely, perception | robot pose, free-space/semantic map와 local goal | p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION) |
| Output/action | (6) depicts the map produced by curret state-of-the-art methods, where dae to edometry dif the map is eoncous: aie thatthe safe region (axonding to the constrated map) kota subset of the fre ... | collision-free trajectory 또는 velocity command | p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION) |
| Objective/outcome | Overview of notation and objectives. | goal reach, safety, localization error와 replanning latency | p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION) |

## Main Claims and Actual Contribution

- 증분 자세 오차의 상한만큼 안전 영역을 축소하는 방식으로 안전 비행 회랑과 부호 거리장 각각에 대한 성질을 증명했다. [PDF 4쪽](https://www.roboticsproceedings.org/rss21/p007.pdf#page=4) · [PDF 6쪽](https://www.roboticsproceedings.org/rss21/p007.pdf#page=6)
- Replica 시뮬레이션과 실물 로버에서 이미 관측한 장애물에 다시 접근할 때 보수적으로 만든 지도가 정지를 유도하는지 평가했다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p007.pdf#page=1) · [PDF 10쪽](https://www.roboticsproceedings.org/rss21/p007.pdf#page=10)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION) |
| Embodiment/environment | Real-world experiments with a robotic rover show that, while baseline methods result in collisions with previously mapped obstacles, the proposed framework enables the rover to safely stop before potential colisions. | hardware/simulator version and reset protocol | p. 1 (Abstract), p. 2 (1. INTRODUCTION) |
| Dataset/benchmark | Simulations using the Replica dataset highlight the efficacy of our methods compared to state of-the-art techniques. | role, split, size and leakage | p. 1 (Abstract), p. 2 (1. INTRODUCTION), p. 1 (Abstract), p. 2 (1. INTRODUCTION) |
| Metric | Although recent advances have achieved significant accuracy improvements (11, 12, 13, 14, 15}, formal error analysis is often lacking. | definition, denominator, direction and uncertainty | p. 1 (1. INTRODUCTION), p. 1 (Abstract), p. 2 (1. INTRODUCTION) |
| Baseline/ablation | Simulations using the Replica dataset highlight the efficacy of our methods compared to state of-the-art techniques. | fair input/data/compute/action matching | p. 1 (Abstract), p. 1 (Abstract), p. 2 (1. INTRODUCTION) |

## Explicit Limitations and Failure Boundary

- **p. 1 / Abstract - extractive body cue:** However, existing mapping approaches often assume perfect pose estimates, an unrealistic assumption that ean lead to incorrect fbstacle maps and therefore collisions.
- **p. 1 / Abstract - extractive body cue:** Real-world experiments with a robotic rover show that, while baseline methods result in collisions with previously mapped obstacles, the proposed framework enables the rover to ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** The rover uses an onboard safety filter to prevent collisions.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Unlike baseline methods which result in collisions, our approach prevents crashes by deflating the safe regions appropriately.
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 6. Rover Experimental Results. (,b) shows snapshots of the reconstructed obstacle map and de estimated rover pose with (a) the baseline method and (©) ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (24 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Without quantified error bounds, guaranteeing the safety of a closed-loop robotic system remains a challenge. (p. 1, 1. INTRODUCTION).
- **Actual contribution:** In Section IV and V we introduce the deflation mechanism for both map representations, In Section VI we propose methods to use the certified maps to acheive safe navigation, Finally ... (p. 2, 1. INTRODUCTION).
- **Evaluation boundary:** Localization and Mapping (SLAM) systems now report translation error rates below 1% (19, 20], enabling more reliable navigation in real-world scenarios. (p. 2, experimental results).
- **Explicit failure boundary:** In the baseline methods, the violation rates are between 6 and 60%, while in the certified methods, the violation rates are between 03%, Note, we cannot expect the certified methods ... (p. 9, Results).
