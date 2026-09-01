# Certifiably-Correct Mapping for Safe Navigation Despite Odometry Drift

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (24 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p007.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p007.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, safe navigation, mapping, state estimation, uncertainty, formal guarantee
- Official paper: https://www.roboticsproceedings.org/rss21/p007.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p007.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (24 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 navigation 문제를 이해하기 위해 읽는다. 본문은 Without quantified error bounds, guaranteeing the safety of a closed-loop robotic system remains a challenge.를 문제로 두고, In Section IV and V we introduce the deflation mechanism for both map representations, In Section VI we propose methods to use the certified maps to acheive safe navigation, Finally in Section ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 2 / 1. INTRODUCTION - extractive body cue:** In Section IV and V we introduce the deflation mechanism for both map representations, In Section VI we propose methods to use the certified maps ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** In contrast to [27], this paper assumes that the incremental pose estimate is bounded in a Lie-algebraic sense, which allows ‘our methods to be applied ...
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Our main contributions are as follows:
- **p. 1 / Abstract - extractive body cue:** Simulations using the Replica dataset highlight the efficacy of our methods compared to state of-the-art techniques.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Although recent advances have achieved significant accuracy improvements (11, 12, 13, 14, 15}, formal error analysis is often lacking.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** The primary goals of these advancements have been to enhance localization and mapping accuracy, improve robustness under diverse environmental conditions, and develop algorithms with lower ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Perception methods have seen significant advancements lover the past few decades, driven by improvements in algorithms, sensors, and computational capabilities (17, 18].
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 6. Rover Experimental Results. (,b) shows snapshots of the reconstructed obstacle map and de estimated rover pose with (a) the baseline method and (©) ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

World models, safety, uncertainty, and recovery의 navigation 문제를 이해하기 위해 읽는다. 본문은 Without quantified error bounds, guaranteeing the safety of a closed-loop robotic system remains a challenge.를 문제로 두고, In Section IV and V we introduce the deflation mechanism for both map representations, In Section VI we propose methods to use the certified maps to acheive safe navigation, Finally in Section ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
