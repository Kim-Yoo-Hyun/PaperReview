# VLM-GroNav: Robot Navigation Using Physically Grounded Vision-Language Models in Outdoor Environments

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/icra55743.2025.11128264.
> PDF retrieval source: https://arxiv.org/pdf/2409.20445v1. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICRA
- Authors: Mohamed Elnoor, Kasun Weerakoon, Gershom Seneviratne, Ruiqi Xian, Tianrui Guan, Mohamed Khalid M Jaffar, Vignesh Rajagopal, Dinesh Manocha
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Vision-Language Model, Robotics, Navigation
- Official paper: https://api.crossref.org/works/10.1109/icra55743.2025.11128264
- Full-text retrieval: https://arxiv.org/pdf/2409.20445v1
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

VLM-GroNav는 야외 지형의 시각적 의미와 로봇이 직접 느낀 미끄러짐·변형 단서를 결합해 주행 가능성을 갱신한다. [PDF 1쪽](https://arxiv.org/pdf/2409.20445v1#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present a novel autonomous robot navigation algorithm for outdoor environments that is capable of handling diverse terrain traversability conditions.
- **p. 1 / Abstract - extractive body cue:** Our approach, VLMGroNav, uses vision-language models (VLMs) and integrates them with physical grounding that is used to assess intrinsic terrain properties such as deformability and ...
- **p. 1 / Abstract - extractive body cue:** We use proprioceptive-based sensing, which provides direct measurements of these physical properties, and enhances the overall semantic understanding of the terrains.
- **p. 1 / Abstract - extractive body cue:** Our formulation uses in-context learning to ground the VLM's semantic understanding with proprioceptive data to allow dynamic updates of traversability estimates based on the robot's ...
- **p. 1 / Abstract - extractive body cue:** We use the updated traversability estimations to inform both the local and global planners for real-time trajectory replanning.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, using such imagery for effective terrain analysis presents additional challenges; these images may lack sufficient detail to capture the complex characteristics of natural terrain ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, current proprioception methods typically lack the ability to predict the traversability of the terrain in the vicinity of the robot, thereby reducing their effectiveness ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** Main contributions: We present VLM-GroNav, a novel navigation method that integrates Vision-Language Models (VLMs) with proprioception-based sensing.
- **p. 2 / I. INTRODUCTION - extractive body cue:** This process allows for dynamic trajectory re-planning, informed by both visual cues and updated traversability estimates. • A real-time adaptive local planner: We introduce a ...
- **p. 3 / IV. OUR APPROACH - extractive body cue:** We propose a novel navigation method that integrates Vision-Language Models (VLMs) with proprioceptive sensing to enable adaptive and robust navigation across complex outdoor terrains.
- **p. 1 / I. INTRODUCTION - extractive body cue:** 1: Overview of our VLM-GroNav system: Our method uses the given information to achieve a navigation objective.
- **p. 3 / IV. OUR APPROACH - extractive body cue:** The overall architecture of our method is shown in Fig 2.
- **p. 5 / IV. OUR APPROACH - extractive body cue:** To integrate terrain traversability into the planning process, we introduce a new cost term, the frontier cost, into the DWA's objective function.
- **p. 6 / A method - extractive body cue:** All metrics are averaged over both the successful and unsuccessful trails (reaching the goal). • ViNT [50]: A general-purpose foundation model for visual navigation that ...
- **p. 4 / IV. OUR APPROACH - extractive body cue:** The VLM is then prompted with this marked image and a navigation objective Tobjective to select the optimal sequence of waypoints that lead to the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | It leverages VLMs to process visual inputs (aerial imagery and front camera views), and integrates real-time feedback from the robot's local sensors. | camera/depth stream, pose, map와 language goal | p. 4 (IV. OUR APPROACH), p. 3 (III. BACKGROUND) |
| State/latent | leverages, VLMs, process, visual, inputs, aerial, imagery, front, camera, views, integrates, real-time | robot pose, free-space/semantic map와 local goal | p. 4 (IV. OUR APPROACH), p. 3 (III. BACKGROUND), p. 4 (IV. OUR APPROACH) |
| Output/action | The global planner leverages aerial imagery and GPS to generate high-level global waypoints, while the local planner uses real-time sensory feedback, including proprioception to adjust the robot's trajectory based on terrain conditions. | collision-free trajectory 또는 velocity command | p. 3 (III. BACKGROUND), p. 4 (IV. OUR APPROACH), p. 2 (I. INTRODUCTION) |
| Objective/outcome | To integrate terrain traversability into the planning process, we introduce a new cost term, the frontier cost, into the DWA's objective function. | goal reach, safety, localization error와 replanning latency | p. 5 (IV. OUR APPROACH), p. 5 (A method), p. 4 (IV. OUR APPROACH) |

## Main Claims and Actual Contribution

- 지면을 통과할 때 얻은 고유수용감각을 시각·언어 모델의 문맥 예시로 사용하고, 갱신된 지형 비용을 지역 및 전역 경로 계획에 반영한다. [PDF 3쪽](https://arxiv.org/pdf/2409.20445v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2409.20445v1#page=4)
- 사족 로봇 Ghost Vision 60과 바퀴형 Clearpath Husky를 서로 다른 야외 지형에서 주행시켜 물리 경험을 반영한 경로 선택과 성공률을 평가했다. [PDF 5쪽](https://arxiv.org/pdf/2409.20445v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2409.20445v1#page=6)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 1 (Figure/Table caption) |
| Embodiment/environment | Implementation For the real-world experiments, we utilize both the Ghost Vision 60 legged robot and the Clearpath Husky wheeled robot. | hardware/simulator version and reset protocol | p. 5 (V. RESULTS AND ANALYSIS) |
| Dataset/benchmark | Implementation For the real-world experiments, we utilize both the Ghost Vision 60 legged robot and the Clearpath Husky wheeled robot. | role, split, size and leakage | p. 5 (V. RESULTS AND ANALYSIS) |
| Metric | Comparison Methods • DWA [30]: A baseline motion planner that performs simple collision avoidance and goal-reaching behaviors. • GA-Nav [4]: | definition, denominator, direction and uncertainty | p. 5 (V. RESULTS AND ANALYSIS), p. 4 (Figure/Table caption), p. 5 (Figure/Table caption) |
| Baseline/ablation | Comparison Methods • DWA [30]: A baseline motion planner that performs simple collision avoidance and goal-reaching behaviors. • GA-Nav [4]: | fair input/data/compute/action matching | p. 5 (V. RESULTS AND ANALYSIS), p. 5 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 3. VLM-GroNav consistently achieves the highest success - extractive body cue:** We observe that this results in errors in predicting the terrain's traversbility while navigating, which in turn ill-informs the local and global planners, causing failures.
- **p. 4 / IV. OUR APPROACH - extractive body cue:** The difference between these measurements reflects the degree of slippage experienced by the robot.
- **p. 4 / IV. OUR APPROACH - extractive body cue:** The traversability indicator (τsinkage and τslip) are time-shifted to match the visual inputs, τshifted(t) = τ(t -∆t).
- **p. 5 / V. RESULTS AND ANALYSIS - extractive body cue:** Comparison Methods • DWA [30]: A baseline motion planner that performs simple collision avoidance and goal-reaching behaviors. • GA-Nav [4]:
- **p. 6 / 3. VLM-GroNav consistently achieves the highest success - extractive body cue:** Scenarios 3 and 4 involve the wheeled robot navigating through unstructured and slippery terrains, VLM-GroNav excels at maintaining a high success rate and reduced IMU ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (IV. OUR APPROACH), p. 5 (IV. OUR APPROACH), p. 6 (A method)이다.
