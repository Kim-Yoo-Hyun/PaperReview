# NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance

> Evidence maturity: `ABSTRACT_CHECKED`. 개요 전반은 초록 수준이며, 아래 요약과 두 기여에는 확인한 본문 위치를 표시했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICRA
- Authors: Wenzhe Cai, Jiaqi Peng, Yuqiang Yang, Yujian Zhang, Meng Wei, Hanqing Wang, Yilun Chen, Tai Wang, Jiangmiao Pang
- Category: Embodied Navigation and Mapping
- Primary track: Planning and control
- Tier: NEXT
- Tags: Navigation, diffusion-policy, privileged-training
- Aliases: NavDP
- Official paper: https://arxiv.org/abs/2505.08712
- Venue verification: https://github.com/InternRobotics/NavDP
- Code/Project: https://github.com/InternRobotics/NavDP
- Code: https://github.com/InternRobotics/NavDP
- Source audit: 2026-11-23 요약과 핵심 기여 두 개를 원문 본문에 대조했다. 나머지 세부 분석은 기존 초록·공식 자료에 근거한다.

## Problem and Importance

NavDP는 시뮬레이션의 특권 정보로 궤적 평가를 학습하고 배포 시에는 근방의 RGB-D 관측으로 주행 경로를 생성·선택한다. [PDF 1쪽](https://arxiv.org/pdf/2505.08712v3#page=1)

## Core Idea and Contribution

- 시뮬레이션에서 대조 궤적과 평가 점수를 만들고 하나의 트랜스포머에서 확산 기반 궤적 생성과 가치 예측을 함께 학습한다. [PDF 2쪽](https://arxiv.org/pdf/2505.08712v3#page=2) · [PDF 4쪽](https://arxiv.org/pdf/2505.08712v3#page=4)
- 실물과 시뮬레이션의 서로 다른 환경과 로봇에서 추가 학습 없는 주행을 평가하고 일반화에 영향을 주는 요소를 비교했다. [PDF 1쪽](https://arxiv.org/pdf/2505.08712v3#page=1) · [PDF 6쪽](https://arxiv.org/pdf/2505.08712v3#page=6)

## Observation–State–Action Interface

Local visual observation + point/image goal 또는 no-goal setting → trajectory/action proposal; privileged 정보의 train/test 경계 확인 필요.

## Evaluation Scope and Claim Boundary

저자 project는 no-goal exploration, point-goal/image-goal navigation과 cross-embodiment real-world transfer를 설명한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2505.08712) · [저자 project/code](https://github.com/InternRobotics/NavDP). 그 밖의 수치, 기준선의 비교 조건, 실패 범위는 별도 대조가 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Current trend. Simulation training에서 real-world cross-embodiment local navigation으로 이어지는 경로를 보충한다. NoMaD/ViNT의 local policy와 비교할 대상이며, 논문 자체를 language-conditioned VLA RL로 부르지는 않는다.

## Verification Boundary

Training oracle, depth/pose 입력, trajectory selector, robot footprint와 controller 한계을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 원문과 공개 자료

- 코드 — 원래 NavDP의 궤적 추론 서버 · baselines/navdp/navdp_server.py [배포 파일](https://raw.githubusercontent.com/InternRobotics/NavDP/bff5eb8857f50e082243fb455d312409daabc3aa/baselines/navdp/navdp_server.py)
- 데이터 — NavDP 평가 장면의 시작·목표 쌍 · assets/scenes/cluttered_easy/easy_0/pointgoal_start_goal_pairs.npy [배포 파일](https://raw.githubusercontent.com/InternRobotics/NavDP/bff5eb8857f50e082243fb455d312409daabc3aa/assets/scenes/cluttered_easy/easy_0/pointgoal_start_goal_pairs.npy)
