# GR00T N1.6: An Improved Open Foundation Model for Generalist Humanoid Robots

> Evidence maturity: `FULL_TEXT_CHECKED`.
> 요약과 기여의 링크는 NVIDIA가 공개한 N1.6 보고서의 해당 절로 이동한다. 본문의 기존 쪽수는 같은 보고서를 2026-09-03에 인쇄한 2쪽짜리 사본의 위치다.

- Year/Venue: 2025 / Technical Report
- Authors: GEAR Team, Allison Azzolini, Johan Bjorck, Valts Blukis, Fernando Castañeda, Rahul Chand, Yan Chang, Danyi Chen, Nikita Cherniadev, Xingye Da, Runyu Ding, Shunjia Ding, Hassan Eslami, Linxi "Jim" Fan, Yu Fang, Max Fu, Shenyuan Gao, Yunhao Ge, Fengyuan Hu, Spencer Huang, Joel Jang, Xiaowei Jiang, Yunfan Jiang, Ryan Julian, Kaushil Kundalia, Jan Kautz, Zhiqi Li, Kevin Lin, Wei Liu, Runyu Lu, Zhengyi Luo, Loic Magne, Yunze Man, Ajay Mandlekar, Abhishek Mishra, Avnish Narayan, Connor Pederson, Nadun Ranawaka, Scott Reed, Sunil Srinivasa, You Liang Tan, Guanzhi Wang, Jing Wang, Qi Wang, Shihao Wang, Jimmy Wu, Yubo Wu, Yuqi Xie, Tianyi Xiong, Mengda Xu, Yinzhen Xu, Fu-En Yang, Seonghyeon Ye, Zhiding Yu, K.R. Zentner, Zhe Zhang, Kaiyuan Zheng, Ruijie Zheng, Yuke Zhu
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, humanoid, foundation model, loco-manipulation, long-horizon, robot data
- Official paper: https://research.nvidia.com/labs/gear/gr00t-n1_6/
- Full-text retrieval: https://research.nvidia.com/labs/gear/gr00t-n1_6/
- Code/Project: https://research.nvidia.com/labs/gear/gr00t-n1_6/
- Paper type: theory_or_foundation
- Source audit: 2026-11-23 NVIDIA 공식 웹 기술보고서 본문 대조.

## Why This Paper Is Here

GR00T N1.6은 N1.5의 시각언어 백본과 행동 생성기를 바꾸고 실제 양팔·휴머노이드 데이터를 확대한 후속 버전이다. [Introduction](https://research.nvidia.com/labs/gear/gr00t-n1_6/#:~:text=Introduction)

## Problem and Motivation

- **p. 1 / Introduction - extractive body cue:** We introduce GR00T N1.6, an improved version of the GR00T N1.5 foundation model for humanoid robots.
- **p. 1 / Introduction - extractive body cue:** With several architecture, data and modeling improvements, we find that N1.6 outperforms N1.5 on both simulated manipulation benchmarks and on real bimanual YAM, Agibot Genie-1 ...
- **p. 1 / Introduction - extractive body cue:** We expect users of N1.6 should observe better post-training performance compared to N1.5.
- **p. 2 / Discussion - extractive body cue:** Multi-task language following and out-of-distribution task generalization continue to be challenging for current VLA models.
- **p. 2 / Discussion - extractive body cue:** More fine-grained subtask annotation can improve language following, but not yet reaching robust generalization.

## Core Idea

- **p. 1 / Introduction - extractive body cue:** We introduce GR00T N1.6, an improved version of the GR00T N1.5 foundation model for humanoid robots.
- **p. 1 / Model and Data Improvements - extractive body cue:** Predicts state-relative action chunks for most embodiments, rather than absolute joint angles or EEF positions.
- **p. 1 / Model and Data Improvements - extractive body cue:** Removes N1.5's post-VLM 4-layer transformer adapter.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Predicts state-relative action chunks for most embodiments, rather than absolute joint angles or EEF positions. | proprioception, reference pose/motion, visual or language command | p. 1 (Model and Data Improvements), p. 1 (Model and Data Improvements) |
| State/latent | Predicts, state-relative, action, chunks, most, embodiments, rather, absolute, joint, angles, EEF, positions | whole-body pose, balance/contact state와 skill/mode | p. 1 (Model and Data Improvements), p. 1 (Model and Data Improvements), p. 2 (Discussion) |
| Output/action | The VLM is trained on both general vision-language tasks and embodied reasoning tasks like next action prediction. | joint/whole-body action, motion target 또는 task trajectory | p. 1 (Model and Data Improvements), p. 2 (Discussion), p. 2 (Discussion) |
| Objective/outcome | The VLM is trained on both general vision-language tasks and embodied reasoning tasks like next action prediction. | tracking, balance, skill/task success와 recovery | p. 1 (Model and Data Improvements) |

## Main Claims and Actual Contribution

- Cosmos-2B 계열 백본과 확장한 확산 트랜스포머를 사용하고 대부분의 로봇에서 현재 상태에 상대적인 행동 묶음을 예측한다. [Model and Data Improvements](https://research.nvidia.com/labs/gear/gr00t-n1_6/#:~:text=Model%20and%20Data%20Improvements)
- 상대 행동이 움직임을 매끄럽게 하는 경우와 소량 데이터에서 오차가 누적되는 경우를 구분하고 G1·양팔 YAM에서 비동기 실행을 다뤘다. [Discussion](https://research.nvidia.com/labs/gear/gr00t-n1_6/#:~:text=Discussion)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 1 (Discussion), p. 1 (Introduction) |
| Embodiment/environment | In the following robot experiments, we further post-train on small task-specific datasets; typically 10K-30K steps with global batch size 1K or less. | hardware/simulator version and reset protocol | p. 1 (Experiments), p. 1 (Discussion) |
| Dataset/benchmark | We expect users to benefit from improved performance in bimanual manipulation and locomanipulation tasks. | role, split, size and leakage | p. 1 (Experiments), p. 1 (Discussion), p. 2 (Discussion), p. 2 (Discussion) |
| Metric | When scaling up real-world experiments, we incorporate various lessons learned from the robot learning community to improve model success rates during rollouts. | definition, denominator, direction and uncertainty | p. 1 (Discussion), p. 1 (Discussion), p. 2 (Discussion) |
| Baseline/ablation | We expect users of N1.6 should observe better post-training performance compared to N1.5. | fair input/data/compute/action matching | p. 1 (Introduction), p. 1 (Introduction), p. 1 (Model and Data Improvements) |

## Explicit Limitations and Failure Boundary

- **p. 2 / Discussion - extractive body cue:** More fine-grained subtask annotation can improve language following, but not yet reaching robust generalization.
- **p. 2 / Discussion - extractive body cue:** Test-time and train-time RTC provide performance boosts to motion smoothness and robustness during asynchronous rollouts.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (Discussion), p. 1 (Model and Data Improvements), p. 1 (Discussion), p. 1 (Introduction)이다.

## 원문과 공개 자료

- 코드 — N1.6 배포 태그의 정책 모델 · gr00t/model/gr00t_n1d6/gr00t_n1d6.py [배포 파일](https://raw.githubusercontent.com/NVIDIA/Isaac-GR00T/ead52833afbbf4243f8cd5e7664f48a94de03b19/gr00t/model/gr00t_n1d6/gr00t_n1d6.py)
- 가중치 — NVIDIA N1.6-3B 모델 배포본 · model-00001-of-00002.safetensors [배포 파일](https://huggingface.co/nvidia/GR00T-N1.6-3B/blob/d0814e7ecb19202e7c8468b46098b0b7ef3a6d61/model-00001-of-00002.safetensors)
- 데이터 — N1.6 태그에 포함된 cube-to-bowl 시연 · demo_data/cube_to_bowl_5/data/chunk-000/episode_000000.parquet [배포 파일](https://media.githubusercontent.com/media/NVIDIA/Isaac-GR00T/ead52833afbbf4243f8cd5e7664f48a94de03b19/demo_data/cube_to_bowl_5/data/chunk-000/episode_000000.parquet)
- 코드와 소형 시연은 NVIDIA의 해당 버전 배포 태그에서 확인했다. 전체 사전학습 데이터 범위는 미확인이다.
