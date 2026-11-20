# DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2403.12945.
> PDF retrieval source: https://arxiv.org/pdf/2403.12945. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RSS
- Authors: Alexander Khazatsky, Karl Pertsch, Suraj Nair, Ashwin Balakrishna, Sudeep Dasari, Siddharth Karamcheti, Soroush Nasiriany, Mohan Kumar Srirama, Lawrence Yunliang Chen, Kirsty Ellis, Peter David Fagan, Joey Hejna, Masha Itkina, Marion Lepert, Yecheng Jason Ma, Patrick Tree Miller, Jimmy Wu, Suneel Belkhale, Shivin Dass, Huy Ha, Arhan Jain, Abraham Lee, Youngwoon Lee, Marius Memmel, Sungjae Park, Ilija Radosavovic, Kaiyuan Wang, Albert Zhan, Kevin Black, Cheng Chi, Kyle Beltran Hatch, Shan Lin, Jingpei Lu, Jean Mercat, Abdul Rehman, Pannag R Sanketi, Archit Sharma, Cody Simpson, Quan Vuong, Homer Rich Walke, Blake Wulfe, Ted Xiao, Jonathan Heewon Yang, Arefeh Yavary, Tony Z. Zhao, Christopher Agia, Rohan Baijal, Mateo Guaman Castro, Daphne Chen, Qiuyu Chen, Trinity Chung, Jaimyn Drake, Ethan Paul Foster, Jensen Gao, David Antonio Herrera, Minho Heo, Kyle Hsu, Jiaheng Hu, Donovon Jackson, Charlotte Le, Yunshuang Li, Roy Lin, Zehan Ma, Abhiram Maddukuri, Suvir Mirchandani, Daniel Morton, Tony Nguyen, Abigail O'Neill, Rosario Scalise, Derick Seale, Victor Son, Stephen Tian, Emi Tran, Andrew E. Wang, Yilin Wu, Annie Xie, Jingyun Yang, Patrick Yin, Yunchu Zhang, Osbert Bastani, Glen Berseth, Jeannette Bohg, Ken Goldberg, Abhinav Gupta, Abhishek Gupta, Dinesh Jayaraman, Joseph J Lim, Jitendra Malik, Roberto Martín-Martín, Subramanian Ramamoorthy, Dorsa Sadigh, Shuran Song, Jiajun Wu, Michael C. Yip, Yuke Zhu, Thomas Kollar, Sergey Levine, Chelsea Finn
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: Robotics, Dataset, in-the-wild, robot manipulation, data diversity, generalist policy
- Official paper: https://arxiv.org/abs/2403.12945
- Full-text retrieval: https://arxiv.org/pdf/2403.12945
- Code/Project: https://droid-dataset.github.io/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0)

2026-11-20에 RSS 게재본과 저자의 수집 코드·원시 데이터 배포를 확인했다. 원시 궤적의 제어 명령과 영상에 접근하는 방법은 공식 데이터 문서에서 확인할 수 있다. [RSS 게재본](https://www.roboticsproceedings.org/rss20/p120.html) · [수집 코드](https://github.com/droid-dataset/droid) · [데이터 배포 안내](https://github.com/droid-dataset/droid/blob/33ae6a67274f36d2e29525b86f23a56616ef43a7/docs/the-droid-dataset.md)

## Why This Paper Is Here

DROID는 여러 장소에서 공통 로봇 장비로 수집한 실물 조작 시연을 제공하고 데이터 다양성이 정책 일반화에 미치는 영향을 평가한다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The creation of large, diverse, high-quality robot manipulation datasets is an important stepping stone on the path toward more capable and robust robotic manipulation policies.
- **p. 1 / Abstract - extractive body cue:** As a result, even the most general robot manipulation policies today are mostly trained on data collected in a small number of environments with limited ...
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce DROID (Distributed Robot Interaction Dataset), a diverse robot manipulation dataset with ...
- **p. 2 / Abstract - extractive body cue:** 76k demonstration trajectories or 350 hours of interaction data, collected across 564 scenes and 86 tasks by 50 data collectors in North America, Asia, and ...
- **p. 2 / Abstract - extractive body cue:** We demonstrate that training with DROID leads to policies with higher performance and improved generalization ability.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, creating such datasets is challenging: in contrast to vision or language data, training manipulation policies typically requires robot manipulation data with recorded observations and ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Collecting robot manipulation data in diverse environments poses logistical and safety challenges when moving robots outside of controlled lab environments.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, we introduce DROID (Distributed Robot Interaction Dataset), a robot manipulation dataset of unprecedented diversity (see Fig.
- **p. 1 / 13 Institutions - extractive body cue:** 1: We introduce DROID (Distributed Robot Interaction Dataset), an "in-the-wild" robot manipulation dataset with 76k trajectories or 350 hours of interaction data, collected across 564 ...
- **p. 3 / III. DROID DATA COLLECTION SETUP - extractive body cue:** In this section, we introduce our hardware setup and the data collection protocol.
- **p. 4 / III. DROID DATA COLLECTION SETUP - extractive body cue:** The setup consists of a Franka Panda 7DoF robot arm, two adjustable Zed 2 stereo cameras, a wristmounted Zed Mini stereo camera, and an Oculus ...
- **p. 3 / Dataset - extractive body cue:** Collecting such data "in-the-wild" is more common for robot navigation and autonomous driving [4, 18, 28, 48, 49, 55, 57, 64] and enables training of ...
- **p. 6 / IV. DROID DATASET ANALYSIS - extractive body cue:** We use the point of first gripper closing in every episode as a proxy for interactions in the dataset and visualize the 3D location of ...
- **p. 4 / III. DROID DATA COLLECTION SETUP - extractive body cue:** We use the Polymetis controller [33] and record actions both in robot joint space and in end-effector space at a control frequency of 15Hz.
- **p. 4 / III. DROID DATA COLLECTION SETUP - extractive body cue:** For each trajectory, we record the output of all RGB cameras, relevant low level state information from the robot, equivalent robot control commands from various ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | For each trajectory, we record the output of all RGB cameras, relevant low level state information from the robot, equivalent robot control commands from various popular action spaces, a data collector ID, ... | multi-view observation, language/task label과 action trajectory | p. 4 (III. DROID DATA COLLECTION SETUP), p. 2 (I. INTRODUCTION) |
| State/latent | trajectory, record, output, RGB, cameras, relevant, level, state, information, robot, equivalent, control | shared representation, embodiment/task identity와 data distribution | p. 4 (III. DROID DATA COLLECTION SETUP), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Output/action | However, creating such datasets is challenging: in contrast to vision or language data, training manipulation policies typically requires robot manipulation data with recorded observations and actions, which cannot be easily scraped fro ... | dataset sample 또는 learned policy action | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (Dataset) |
| Objective/outcome | We use the same hardware setup across all 13 institutions to streamline data collection while maximizing portability and flexibility. | coverage, cross-embodiment transfer, data efficiency와 task success | p. 4 (III. DROID DATA COLLECTION SETUP), p. 4 (III. DROID DATA COLLECTION SETUP), p. 3 (III. DROID DATA COLLECTION SETUP) |

## Main Claims and Actual Contribution

- 분산 수집을 위한 로봇 구성과 절차를 제시하고 장면·과제·수집자가 다양한 원시 자료를 공개한다.
- DROID를 학습에 추가했을 때 여러 조작 정책의 성공과 새 조건에 대한 강건성이 어떻게 달라지는지 비교한다.

[저자 원문](https://www.roboticsproceedings.org/rss20/p120.pdf)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 9 (Figure/Table caption), p. 7 (V. EXPERIMENTS) |
| Embodiment/environment | Overall, we find that DROID significantly increases diversity in tasks, objects, scenes, viewpoints and interaction locations over existing large scale robot manipulation datasets. | hardware/simulator version and reset protocol | p. 5 (IV. DROID DATASET ANALYSIS), p. 3 (Dataset) |
| Dataset/benchmark | To test how DROID and existing datasets affect policy robustness, we evaluate each task and method in two settings: "in-distribution," which reflects the distribution of tasks in the in-domain demonstrations with noise ... | role, split, size and leakage | p. 5 (IV. DROID DATASET ANALYSIS), p. 3 (Dataset), p. 8 (V. EXPERIMENTS), p. 3 (Dataset) |
| Metric | Fig. 8: Does DROID Improve Policy Performance and Robustness? We find that across all our evaluation tasks, co-training with DROID significantly improves both in distribution and OOD performance over both no co-training ... | definition, denominator, direction and uncertainty | p. 9 (Figure/Table caption), p. 7 (V. EXPERIMENTS), p. 22 (Figure/Table caption) |
| Baseline/ablation | One of the unique benefits of DROID compared to existing robot datasets is its amount of scene diversity. | fair input/data/compute/action matching | p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 8 / V. EXPERIMENTS - extractive body cue:** To test how DROID and existing datasets affect policy robustness, we evaluate each task and method in two settings: "in-distribution," which reflects the distribution of ...
- **p. 16 / Figure/Table caption - extractive body cue:** Fig. 11: DROID data collection GUI. Top left: Screen for entering feasible tasks for the current scene. Tasks can either be selected from a list ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 8: Does DROID Improve Policy Performance and Robustness? We find that across all our evaluation tasks, co-training with DROID significantly improves both in distribution ...
- **p. 17 / Figure/Table caption - extractive body cue:** Fig. 12: Qualitative examples of scenes in DROID. We use GPT-4V to categorize scenes into 9 scene types. DROID contains robot manipulation demonstrations in a ...
- **p. 9 / VI. DISCUSSION - extractive body cue:** Our policy learning evaluations show that DROID is a valuable data resource for improving policy performance and robustness, even in comparison to existing large robot ...
- **p. 3 / Dataset - extractive body cue:** Calibration Public Robot Collection MIME [50] 8.3k 20 1 ✗ ✗ ✓ human teleop RoboTurk [36] 2.1k 2 1 ✗ ✗ ✓ human teleop RoboNet ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** The out of distribution variant consists of toasting novel objects.

## Why Read It

RL, IL, offline learning, and robot data의 robot_data 문제를 이해하기 위해 읽는다. 본문은 However, creating such datasets is challenging: in contrast to vision or language data, training manipulation policies typically requires robot manipulation data with recorded observations and actions, which cannot be easily scraped fro ...를 문제로 두고, In this work, we introduce DROID (Distributed Robot Interaction Dataset), a robot manipulation dataset of unprecedented diversity (see Fig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 6 (IV. DROID DATASET ANALYSIS), p. 4 (III. DROID DATA COLLECTION SETUP), p. 4 (III. DROID DATA COLLECTION SETUP), p. 1 (Abstract) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (26 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, creating such datasets is challenging: in contrast to vision or language data, training manipulation policies typically requires robot manipulation data with recorded observations and actions, which cannot be easily ... (p. 2, I. INTRODUCTION).
- **Actual contribution:** In this work, we introduce DROID (Distributed Robot Interaction Dataset), a robot manipulation dataset of unprecedented diversity (see Fig. (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** Fig. 8: Does DROID Improve Policy Performance and Robustness? We find that across all our evaluation tasks, co-training with DROID significantly improves both in distribution and OOD performance over both ... (p. 9, Figure/Table caption).
- **Explicit failure boundary:** Notably, when testing out of distribution performance, the No Co-training baseline performs quite poorly while the co-trained policies are much more effective. (p. 8, V. EXPERIMENTS).
