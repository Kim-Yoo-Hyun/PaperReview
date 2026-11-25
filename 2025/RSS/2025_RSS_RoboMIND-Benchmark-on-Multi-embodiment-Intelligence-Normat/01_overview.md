# RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p152.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p152.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: Kun Wu, Chengkai Hou, Jiaming Liu, Zhengping Che, Xiaozhu Ju, Zhuqin Yang, Meng Li, Yinuo Zhao, Zhiyuan Xu, Guang Yang, Shichao Fan, Xinhua Wang, Fei Liao, Zhen Zhao, Guangyu Li, Zhao Jin, Lecheng Wang, Jilei Mao, Ning Liu, Pei Ren, Qiang Zhang, Yaoxu Lyu, Mengzhen Liu, Jingyang He, Yulin Luo, Zeyu Gao, Chenxuan Li, Chenyang Gu, Yankai Fu, Di Wu, Xingyu Wang, Sixiang Chen, Zhenyu Wang, Pengju An, Siyuan Qian, Shanghang Zhang, Jian Tang
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Dataset, Benchmark, multi-embodiment, robot data, long-horizon manipulation, failure data
- Official paper: https://www.roboticsproceedings.org/rss21/p152.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p152.pdf
- Code/Project: https://x-humanoid-robomind.github.io/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (21 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RoboMIND는 네 가지 로봇 형태에서 공통 수집 규약으로 기록한 실제 원격조작 시연과 원인이 표시된 실패 사례를 제공한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p152.pdf#page=1)

## Problem and Motivation

- **p. 2 / Abstract - extractive body cue:** Developing robust and general-purpose manipula tion policies is a key goal in robotics.
- **p. 2 / Abstract - extractive body cue:** To achieve effective generalization, i is essential to construct comprehensive datasets that encompass a large number of demonstration trajectories ‘and diverse tasks.
- **p. 2 / Abstract - extractive body cue:** Unlike vision or language data, which can be sourced from the internet, robotic datasets require detailed observations and manipulation actions, necessitating significant investments in both ...
- **p. 2 / Abstract - extractive body cue:** While existing works have focused on assembling various individual robot datasets, there is stil a lack of a unified data col lection standard and insufficient ...
- **p. 2 / Abstract - extractive body cue:** In this paper, we introduce RoboMIND (Multi-embodiment Intelligence Normative Data for Robot Manipulation), a dataset containing 107k demonstration trajectories across 479 diverse tasks involving 96 ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In contrast 0 the acquisition of vision or language data, which can often be sourced through web-based collection methods (32, 55], collecting robotic data is ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** Given the critical role of 3D spatial information in complex manipulation tasks, several works [116, 35, 94, 33] explore the encoding of point cloud data ...

## Core Idea

- **p. 3 / I. INTRODUCTION - extractive body cue:** demonstrate that RoboMIND can be effectively utilized by various single-task imitation learning algorithms and suecessfully adapted t0 VLA large models. ‘The high-quality information provided by ...
- **p. 12 / C. Vision-Language-Action Large Models - extractive body cue:** The first category consists of tasks similar to those performed by the single-arm Franka robot, which are intended to evaluate the model's performance across different ...
- **p. 4 / I. INTRODUCTION - extractive body cue:** To support the development of such a large-scale dataset, we develop an intelligent data platform designed to collect, filter, and process the dataset efficiently. ‘This ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** One of the aspirations of any professional in the field of robotics is to develop a versatile, general-purpose robotic ‘model capable of performing a broad ...
- **p. 4 / I. INTRODUCTION - extractive body cue:** General-purpose simulators (19, 52, 67, 76] replicate the physical world and provide virtual ‘environments for training policy models, significantly reducing the costs and time associated ...
- **p. 10 / B. Single-task Imitation Learning Models - extractive body cue:** In terms of the im tation learning algorithms, we used three well-known and commonly used methods: ACT [116], Diffusion Policy {17}, and BAKU [39].
- **p. 10 / B. Single-task Imitation Learning Models - extractive body cue:** Using the three algorithms, we trained the singletask model from scratch for each dataset.
- **p. 12 / C. Vision-Language-Action Large Models - extractive body cue:** It is noting that RoboMIND contains valuable data from diverse robots including the Tien Kung humanoid robots with dexterous hands, and we applied this dataset ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In contrast, recent works [73, 27, 28] incorporate visual observations as input to predict action poses. | standardized observation, action, task state와 evaluation split | p. 3 (I. INTRODUCTION), p. 3 (I. INTRODUCTION) |
| State/latent | contrast, recent, works, incorporate, visual, observations, input, predict, action, poses, Driven, advancements | benchmark state/goal와 method decision | p. 3 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 4 (I. INTRODUCTION) |
| Output/action | Driven by advancements in diffusion-based generative models [41, 95, 89], diffusion policy [17] and subsequent works [82, 86, 105] focus on transforming random Gaussian noise into coherent action sequences, with methods such ... | policy/controller trajectory 또는 measured result | p. 3 (I. INTRODUCTION), p. 4 (I. INTRODUCTION), p. 4 (I. INTRODUCTION) |
| Objective/outcome | This discrepancy could be attributed to the hyper-parameter settings from the original BAKU paper, which is primarily optimized for simulation environments rather than real-world robotic platforms tested in our experiments. | success metric, robustness, generalization과 reproducibility | p. 11 (B. Single-task Imitation Learning Models) |

## Main Claims and Actual Contribution

- 여러 시점의 영상, 로봇 상태, 작업 설명을 공통 플랫폼에서 수집해 로봇별 시연을 같은 방식으로 다루도록 했다. [PDF 4쪽](https://www.roboticsproceedings.org/rss21/p152.pdf#page=4) · [PDF 5쪽](https://www.roboticsproceedings.org/rss21/p152.pdf#page=5)
- 전체 시연의 과제·물체 구성을 분석하고 성공 시연에 더해 실패 원인이 붙은 실제 사례를 포함했다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p152.pdf#page=1) · [PDF 7쪽](https://www.roboticsproceedings.org/rss21/p152.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 11 (Figure/Table caption), p. 15 (Figure/Table caption) |
| Embodiment/environment | In addition to the diversity across robot, the varied task horizons in the dataset directly impact the temporal generalization capabilities of policies in real-world scenarios. | hardware/simulator version and reset protocol | p. 7 (A. Quantitative Analysis), p. 8 (B. Qualitative Analysis) |
| Dataset/benchmark | A manipulation dataset with different robotic embodiment types improves generalization to various actions and joint DoFs in downstream tasks. | role, split, size and leakage | p. 7 (A. Quantitative Analysis), p. 8 (B. Qualitative Analysis), p. 7 (A. Quantitative Analysis), p. 8 (A. Quantitative Analysis) |
| Metric | Fig. 12: Success rates of ACT, Diffusion Policy, and BAKU on RoboMIND. | definition, denominator, direction and uncertainty | p. 11 (Figure/Table caption), p. 15 (Figure/Table caption), p. 9 (B. Qualitative Analysis) |
| Baseline/ablation | 8: Comparison between Open X-Embodiment and RoboMIND. | fair input/data/compute/action matching | p. 9 (B. Qualitative Analysis), p. 7 (A. Quantitative Analysis) |

## Explicit Limitations and Failure Boundary

- **p. 9 / B. Qualitative Analysis - extractive body cue:** In the failure ‘case, the arm fails to locate the correct slot position, causing the plate to slip out of the rack, likely due to ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 9: Visualization of failed data collection cases. We present two examples of failure from Franka and AgileX. In the FR-PlacePlateInP lateRack task (the second ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: We define 8 quality assurance criteria in the data collection process. Touch Excess: Unnecessary contact with objects by the robotic arm; Movement not ...
- **p. 8 / B. Qualitative Analysis - extractive body cue:** We also release Sk trajectories of the robot task failure cases.
- **p. 8 / B. Qualitative Analysis - extractive body cue:** The failure cases documented include scenarios where different types of humane operators filed to complete their assigned tasks, as well as in
- **p. 11 / B. Single-task Imitation Learning Models - extractive body cue:** Each model was tested ten times, and the testers recorded the success or failure of each test and the reasons if there were any failures.
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 15: Top five failure reasons for each embodiment of the ACT algorithm. ‘The x-axis denotes the proportion for each failure among all unsuccessful test ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 4 (I. INTRODUCTION), p. 12 (C. Vision-Language-Action Large Models)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (21 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, the curation of large-scale datasets for training general-purpose robotic models poses significant challenges. (p. 2, I. INTRODUCTION).
- **Actual contribution:** To support the development of such a large-scale dataset, we develop an intelligent data platform designed to collect, filter, and process the dataset efficiently. ‘This platform uses a cloudnative architecture ... (p. 4, I. INTRODUCTION).
- **Evaluation boundary:** RoboMIND features standardized settings to form a large-scale real-world manipulation dataset. ‘As shown in Figure 8, we compare our dataset with Open XEmbodiment, another large-scale robotic learning dataset. (p. 8, B. Qualitative Analysis).
- **Explicit failure boundary:** Touch Excess: Unnecessary contact with objects by the robotic arm; Movement not Smooth: Noticeable jerking or interruptions in robotic arm movements; Secondary Grabbing: Repeated grasping attempts after failures in robotic ... (p. 6, B. Data Preprocessing and Classification).

## 원문과 공개 자료

- 저자 표기와 순서를 표제면에서 확인했다. [저자 원문](https://www.roboticsproceedings.org/rss21/p152.pdf#page=1)
- 코드 — RoboMIND 원격조작 기록을 읽는 예제 · static/quick_start.ipynb [배포 파일](https://raw.githubusercontent.com/x-humanoid-robomind/x-humanoid-robomind.github.io/28ede3eb1bc8a051be76e560a831fe3f0c32319f/static/quick_start.ipynb)
- 데이터 — RoboMIND 1.0 AgileX 시연 · benchmark1_0_compressed/h5_agilex_3rgb/10_packplate.tar.gz.part-aa [배포 파일](https://huggingface.co/datasets/x-humanoid-robomind/RoboMIND/blob/e7ffe31d1fe983a42c3d7b79d192f554fc05b86e/benchmark1_0_compressed/h5_agilex_3rgb/10_packplate.tar.gz.part-aa)
