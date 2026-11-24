# RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2406.02523.
> PDF retrieval source: https://arxiv.org/pdf/2406.02523. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RSS
- Authors: Soroush Nasiriany, Abhiram Maddukuri, Lance Zhang, Adeet Parikh, Aaron Lo, Abhishek Joshi, Ajay Mandlekar, Yuke Zhu
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics, Benchmark, simulation, household manipulation, long-horizon tasks, generalist policy
- Official paper: https://arxiv.org/abs/2406.02523
- Full-text retrieval: https://arxiv.org/pdf/2406.02523
- Code/Project: https://robocasa.ai/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://www.roboticsproceedings.org/rss20/p050.pdf) 기준이다.

## Why This Paper Is Here

RoboCasa는 다양한 주방 장면에서 일상 조작을 학습하고 평가하도록 물체·가구 자산, 과제, 시연 수집 절차를 제공한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss20/p050.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent advancements in Artificial Intelligence (AI) have largely been propelled by scaling.
- **p. 1 / Abstract - extractive body cue:** In Robotics, scaling is hindered by the lack of access to massive robot datasets.
- **p. 1 / Abstract - extractive body cue:** We advocate using realistic physical simulation as a means to scale environments, tasks, and datasets for robot learning methods.
- **p. 1 / Abstract - extractive body cue:** We present RoboCasa, a large-scale simulation framework for training generalist robots in everyday environments.
- **p. 1 / Abstract - extractive body cue:** RoboCasa features realistic and diverse scenes focusing on kitchen environments.
- **p. 1 / I. INTRODUCTION - extractive body cue:** While these datasets have advanced robots' generalization abilities in narrow domains, there remains a considerable gap between the capabilities achieved thus far and general-purpose robots ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We find that generated data significantly improves generalization, hinting at a promising path for scaling in robotics.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** We summarize our contributions as follows: • We develop the RoboCasa simulation framework featuring diverse, realistic kitchen scenes, thousands of high-quality object assets, and cross-embodiment ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We present RoboCasa, a large-scale simulation framework centered around home environments for training generalist robots.
- **p. 3 / III. ROBOCASA SIMULATION - extractive body cue:** Core Simulation Platform We adopt RoboSuite [51] as the core simulation platform on which we develop RoboCasa.
- **p. 3 / III. ROBOCASA SIMULATION - extractive body cue:** We chose RoboSuite because of its focus on physical realism, high speed, and modular design, which allows us to scale to large-scale scenes.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We employ generative AI tools to create environment textures and 3D objects. • We introduce a set of 100 tasks for systematic evaluation, including 25 ...
- **p. 5 / 8) Navigation. These skills do not constitute an exhaustive - extractive body cue:** We first use human teleoperation to collect a base set of demonstrations and then use automated trajectory generation methods to expand this to a much ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** First, once a feature-rich, highfidelity simulator is created, we can generate large amounts of robot data at low cost.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Recent breakthroughs in Artificial Intelligence have been driven by training giant neural network models on Internetscale datasets.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | It allows us to represent rich interactions, such as closing a microwave door or turning on a stove. | standardized observation, action, task state와 evaluation split | p. 4 (III. ROBOCASA SIMULATION), p. 4 (III. ROBOCASA SIMULATION) |
| State/latent | allows, represent, rich, interactions, closing, microwave, door, turning, stove, Furthermore, appliances, undergo | benchmark state/goal와 method decision | p. 4 (III. ROBOCASA SIMULATION), p. 4 (III. ROBOCASA SIMULATION), p. 5 (8) Navigation. These skills do not constitute an exhaustive) |
| Output/action | Furthermore, these appliances undergo state changes, e.g., when we turn a stove knob on, the corresponding burner turns on to simulate heat. | policy/controller trajectory 또는 measured result | p. 4 (III. ROBOCASA SIMULATION), p. 5 (8) Navigation. These skills do not constitute an exhaustive), p. 6 (3) Can large-scale simulation datasets facilitate knowledge) |
| Objective/outcome | First, once a feature-rich, highfidelity simulator is created, we can generate large amounts of robot data at low cost. | success metric, robustness, generalization과 reproducibility | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 6 (3) Can large-scale simulation datasets facilitate knowledge) |

## Main Claims and Actual Contribution

- 주방 배치·물체 외관을 다양화하고 기본 행동과 여러 단계를 결합한 과제로 100개 평가 과제를 구성했다. [PDF 4쪽](https://www.roboticsproceedings.org/rss20/p050.pdf#page=4) · [PDF 5쪽](https://www.roboticsproceedings.org/rss20/p050.pdf#page=5) · [PDF 6쪽](https://www.roboticsproceedings.org/rss20/p050.pdf#page=6)
- 사람 시연에서 자동 생성한 궤적을 늘릴 때 모방 정책의 성과를 측정하고 실물 조작 전이를 별도 실험으로 확인했다. [PDF 7쪽](https://www.roboticsproceedings.org/rss20/p050.pdf#page=7) · [PDF 8쪽](https://www.roboticsproceedings.org/rss20/p050.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 6 (3) Can large-scale simulation datasets facilitate knowledge) |
| Embodiment/environment | We conduct experiments in a real-world kitchen environment with a Franka Emika Panda robot running on the DROID hardware infrastructure [20]. | hardware/simulator version and reset protocol | p. 8 (3) Can large-scale simulation datasets facilitate knowledge), p. 6 (3) Can large-scale simulation datasets facilitate knowledge) |
| Dataset/benchmark | For each seed, we evaluate the model over five seen object categories and 3 unseen object categories (unseen with respect to the real-world demonstrations). | role, split, size and leakage | p. 8 (3) Can large-scale simulation datasets facilitate knowledge), p. 6 (3) Can large-scale simulation datasets facilitate knowledge), p. 8 (3) Can large-scale simulation datasets facilitate knowledge), p. 6 (3) Can large-scale simulation datasets facilitate knowledge) |
| Metric | In Figure 10, we report policy success rates (mean and standard deviation, in percentage) averaged over 3 seeds. | definition, denominator, direction and uncertainty | p. 8 (3) Can large-scale simulation datasets facilitate knowledge), p. 6 (3) Can large-scale simulation datasets facilitate knowledge), p. 7 (3) Can large-scale simulation datasets facilitate knowledge) |
| Baseline/ablation | Fig. 7: Comparison between human demonstrations and machine-generated datasets. We present learning results across 24 atomic tasks spanning diverse robot skills. We compare training on four different multi-task datasets, including a hum ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 7 (3) Can large-scale simulation datasets facilitate knowledge), p. 8 (3) Can large-scale simulation datasets facilitate knowledge) |

## Explicit Limitations and Failure Boundary

- **p. 8 / VI. CONCLUSION - extractive body cue:** We now pinpoint limitations and discuss exciting avenues for future future.
- **p. 8 / VI. CONCLUSION - extractive body cue:** While the generated trajectories are technically considered successful, many exhibited undesirable effects, such as jerky motions and collisions.
- **p. 7 / 3) Can large-scale simulation datasets facilitate knowledge - extractive body cue:** Some common failure modes include difficulty with fine-grained manipulation and difficulty effectively transitioning to the next stage of the task.
- **p. 7 / 3) Can large-scale simulation datasets facilitate knowledge - extractive body cue:** The choice of policy architecture, learning algorithm, and finetuning strategy may play a critical role in performance, and these factors warrant investigation in future work.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 5 (8) Navigation. These skills do not constitute an exhaustive)이다.
