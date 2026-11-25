# GR00T N1.5: An Improved Open Foundation Model for Generalist Humanoid Robots

> Evidence maturity: `FULL_TEXT_CHECKED`.
> 요약과 기여의 링크는 NVIDIA가 공개한 N1.5 보고서의 해당 절로 이동한다. 본문의 기존 쪽수는 같은 보고서를 2026-09-03에 인쇄한 3쪽짜리 사본의 위치다.

- Year/Venue: 2025 / Technical Report
- Authors: Johan Bjorck, Valts Blukis, Fernando Castañeda, Nikita Cherniadev, Xingye Da, Runyu Ding, Linxi "Jim" Fan, Yu Fang, Dieter Fox, Fengyuan Hu, Spencer Huang, Joel Jang, Xiaowei Jiang, Kaushil Kundalia, Jan Kautz, Zhiqi Li, Kevin Lin, Zongyu Lin, Loic Magne, Yunze Man, Ajay Mandlekar, Avnish Narayan, Soroush Nasiriany, Scott Reed, You Liang Tan, Guanzhi Wang, Jing Wang, Qi Wang, Shihao Wang, Jiannan Xiang, Yuqi Xie, Yinzhen Xu, Seonghyeon Ye, Zhiding Yu, Yizhou Zhao, Zhe Zhang, Ruijie Zheng, Yuke Zhu
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, humanoid, foundation model, Flow Matching, world model, robot data
- Official paper: https://research.nvidia.com/labs/gear/gr00t-n1_5/
- Full-text retrieval: https://research.nvidia.com/labs/gear/gr00t-n1_5/
- Code/Project: https://research.nvidia.com/labs/gear/gr00t-n1_5/
- Paper type: theory_or_foundation
- Source audit: 2026-11-23 NVIDIA 공식 웹 기술보고서 본문 대조.

## Why This Paper Is Here

GR00T N1.5는 기존 N1의 시각언어 표현과 정책 학습을 바꾼 버전으로, 언어 지시가 있는 시뮬레이션과 실제 GR-1에서 평가했다. [Introduction](https://research.nvidia.com/labs/gear/gr00t-n1_5/#:~:text=Introduction)

## Problem and Motivation

- **p. 1 / Introduction - extractive body cue:** We introduce GR00T N1.5, an upgraded version of the GR00T N1 foundation model for humanoid robots.
- **p. 1 / Introduction - extractive body cue:** With several architecture, data and modeling improvements, we find that N1.5 outperforms N1 on both simulated manipulation benchmarks and on the real GR-1 robot, detailed ...
- **p. 1 / Introduction - extractive body cue:** We expect users of N1.5 should observe better performance compared to N1, in particular improved generalization and better language following ability.
- **p. 1 / Architecture - extractive body cue:** We found that these modifications greatly improved language following and generalization.
- **p. 2 / Generalization to novel behaviors using Neural Trajectories - extractive body cue:** GR00T N1 showed only weak generalization to new verbs, only repeating the tasks contained in pretraining
- **p. 2 / Learning to manipulate novel objects from human ego videos - extractive body cue:** To evaluate the model's generalization ability, we evaluate pick and place performance using a set of 10 novel objects not seen during pretraining.
- **p. 3 / Post-training on Unitree G1 - extractive body cue:** We observe that the post-trained GR00T N1.5 achieves much higher success rate than N1 for previously seen objects (toy fruits seen in the GR-1 pretraining ...

## Core Idea

- **p. 1 / Introduction - extractive body cue:** We introduce GR00T N1.5, an upgraded version of the GR00T N1 foundation model for humanoid robots.
- **p. 2 / Learning to manipulate novel objects from human ego videos - extractive body cue:** Novel Objects As shown in the FLARE project, future latent representation alignment enables learning directly from human ego videos.
- **p. 2 / Learning to manipulate novel objects from human ego videos - extractive body cue:** This allows learning to manipulate novel objects from human videos and minimal robot demonstrations.
- **p. 3 / Post-training on Unitree G1 - extractive body cue:** Model / GR00T N1, 1K Demos / GR00T N1.5, 1K Demos / GR00T N1.5, 1K Demos Task / Place 1 of 2 fruits onto plate; ...
- **p. 1 / Architecture - extractive body cue:** We used FLARE loss coefficient 0.2 for both pretraining and posttraining.
- **p. 1 / Architecture - extractive body cue:** The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions.
- **p. 2 / Architecture validation - extractive body cue:** We find that the N1.5 architecture achieves significantly higher success rates on both benchmarks, indicating stronger language-conditioned control ability.
- **p. 2 / Data-limited post-training in simulated environments - extractive body cue:** Following the GR00T N1 evaluation protocol, we evaluate N1.5's performance in data-limited post-training.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions. | proprioception, reference pose/motion, visual or language command | p. 1 (Architecture), p. 1 (Architecture) |
| State/latent | vision-language, embeddings, VLM, then, cross-attended, DiT, processes, state, noised, actions, find, adding | whole-body pose, balance/contact state와 skill/mode | p. 1 (Architecture), p. 1 (Architecture), p. 2 (Real GR-1 language following) |
| Output/action | We find that adding FLARE both improves policy performance and unlocks the ability to learn from human videos. | joint/whole-body action, motion target 또는 task trajectory | p. 1 (Architecture), p. 2 (Real GR-1 language following), p. 2 (Learning to manipulate novel objects from human ego videos) |
| Objective/outcome | Joint Policy Learning and World Modeling Objective | tracking, balance, skill/task success와 recovery | p. 1 (Architecture), p. 1 (Architecture), p. 3 (Post-training on Unitree G1) |

## Main Claims and Actual Contribution

- 행동의 flow matching 손실에 미래 영상의 잠재 표현을 맞추는 FLARE 목적을 추가해 사람 영상도 학습에 활용했다. [Joint Policy Learning and World Modeling Objective](https://research.nvidia.com/labs/gear/gr00t-n1_5/#:~:text=Joint%20Policy%20Learning%20and%20World%20Modeling%20Objective)
- 실물 GR-1 앞에 두 과일을 놓고 목표 과일의 위치를 바꿔, 지시한 과일을 접시에 옮기는지를 N1과 비교했다. [Real GR-1 language following](https://research.nvidia.com/labs/gear/gr00t-n1_5/#:~:text=Real%20GR-1%20language%20following)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 3 (Discussion), p. 2 (Architecture validation) |
| Embodiment/environment | With several architecture, data and modeling improvements, we find that N1.5 outperforms N1 on both simulated manipulation benchmarks and on the real GR-1 robot, detailed below. | hardware/simulator version and reset protocol | p. 1 (Introduction), p. 3 (Post-training on Unitree G1) |
| Dataset/benchmark | Demonstrations using a novel object, captured from a GoPro (left) and the GR-1 robot (right). | role, split, size and leakage | p. 1 (Introduction), p. 3 (Post-training on Unitree G1), p. 2 (Learning to manipulate novel objects from human ego videos), p. 2 (Learning to manipulate novel objects from human ego videos) |
| Metric | We find that the N1.5 architecture achieves significantly higher success rates on both benchmarks, indicating stronger language-conditioned control ability. | definition, denominator, direction and uncertainty | p. 2 (Architecture validation), p. 2 (Real GR-1 language following), p. 3 (Generalization to novel behaviors using Neural Trajectories) |
| Baseline/ablation | We expect users of N1.5 should observe better performance compared to N1, in particular improved generalization and better language following ability. | fair input/data/compute/action matching | p. 1 (Introduction), p. 1 (Introduction), p. 1 (Architecture) |

## Explicit Limitations and Failure Boundary

- **p. 3 / Generalization to novel behaviors using Neural Trajectories - extractive body cue:** Although these new verbs can be considered "zero-shot" in the sense that we never collected teleoperation data for these tasks, we still train explicitly on ...
- **p. 1 / Architecture - extractive body cue:** The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (Introduction), p. 1 (Architecture), p. 2 (Generalization to novel behaviors using Neural Trajectories), p. 2 (Learning to manipulate novel objects from human ego videos), p. 3 (Post-training on Unitree G1)이다.

## 원문과 공개 자료

- 코드 — N1.5 배포 태그의 정책 모델 · gr00t/model/gr00t_n1.py [배포 파일](https://raw.githubusercontent.com/NVIDIA/Isaac-GR00T/4af2b622892f7dcb5aae5a3fb70bcb02dc217b96/gr00t/model/gr00t_n1.py)
- 가중치 — NVIDIA N1.5-3B 모델 배포본 · model-00001-of-00003.safetensors [배포 파일](https://huggingface.co/nvidia/GR00T-N1.5-3B/blob/869830fc749c35f34771aa5209f923ac57e4564e/model-00001-of-00003.safetensors)
- 데이터 — N1.5 태그에 포함된 모의 집기 시연 · demo_data/robot_sim.PickNPlace/data/chunk-000/episode_000000.parquet [배포 파일](https://raw.githubusercontent.com/NVIDIA/Isaac-GR00T/4af2b622892f7dcb5aae5a3fb70bcb02dc217b96/demo_data/robot_sim.PickNPlace/data/chunk-000/episode_000000.parquet)
- 코드와 소형 시연은 NVIDIA의 해당 버전 배포 태그에서 확인했다. 전체 사전학습 데이터 범위는 미확인이다.
