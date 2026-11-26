# Robo3R: Enhancing Robotic Manipulation with Accurate Feed-Forward 3D Reconstruction

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Sizhe Yang, Linning Xu, Hao Li, Juncheng Mu, Jia Zeng, Dahua Lin, Jiangmiao Pang
- Category: Robotics-Enabling 3D Perception
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: 3D reconstruction, metric scale, robot state, manipulation
- Aliases: Robo3R
- Official paper: https://roboticsproceedings.org/rss22/p056.html
- Venue verification: https://roboticsproceedings.org/rss22/p056.html
- Code/Project: https://yangsizhe.github.io/robo3r/
- Code: https://github.com/InternRobotics/Robo3R
- 방법·평가 확인 (2026-11-25): [원문 3, 4, 6, 8쪽](https://roboticsproceedings.org/rss22/p056.pdf#page=3) · [다축 분류와 공개 범위](../../../work/sources/batches/core_next_10.yaml)
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

Robo3R은 RGB 영상과 로봇 상태에서 로봇 기준 좌표계의 실제 척도 3차원 장면을 순전파로 복원해 조작에 사용한다. [PDF 1쪽](https://roboticsproceedings.org/rss22/p056.pdf#page=1)

## Core Idea and Contribution

- 시점별 기하와 상대 카메라 자세를 전역 유사 변환으로 정렬하고, 마스크 기반 점 예측과 키포인트 PnP로 물체 경계와 카메라 정합을 개선한다. [PDF 3쪽](https://roboticsproceedings.org/rss22/p056.pdf#page=3) · [PDF 4쪽](https://roboticsproceedings.org/rss22/p056.pdf#page=4)
- 복원 오차와 함께 모방학습·실물 전이·파지 생성·충돌 회피 계획을 평가해 추정한 기하가 후속 로봇 행동에 미치는 영향을 비교했다. [PDF 6쪽](https://roboticsproceedings.org/rss22/p056.pdf#page=6) · [PDF 8쪽](https://roboticsproceedings.org/rss22/p056.pdf#page=8)

## Observation–State–Action Interface

RGB/로봇 상태 → point map·camera pose·robot-frame scene geometry; 별도 downstream policy에 전달한다.

## Evaluation Scope and Claim Boundary

Robo3R-4M 합성 데이터로 학습하고 imitation·sim-to-real·grasp synthesis·collision-free planning의 downstream 효과를 평가한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p056.html) · [저자 project/code](https://yangsizhe.github.io/robo3r/). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

TASK-GEOMETRY가 일반 재구성 정확도 개선의 반복인지 판단할 직접 비교다.

## Verification Boundary

Robot state privilege·similarity transform·훈련 물체 중복·latency을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료의 확인 범위

- Robo3R의 3D 예측 평가 진입점 · eval.py [배포 파일](https://raw.githubusercontent.com/InternRobotics/Robo3R/10fbd8efe40c8a1f4539f2c2c68f649e4e2bff7e/eval.py)
- Robo3R 기하 추정기 체크포인트 · franka_wQpos.pth [배포 파일](https://huggingface.co/yangsizhe/Robo3R/resolve/437d1a3638a33195aae77d5c98b64eaaa151f7db/franka_wQpos.pth)
- Robo3R의 합성 재구성 자료 · 1kScenes_in-gripper_test/1kScenes_in-gripper_test.tar.gz [배포 파일](https://huggingface.co/datasets/yangsizhe/Robo3R/resolve/43a317341c6aa584f303dffc64df942ee92a02b9/1kScenes_in-gripper_test/1kScenes_in-gripper_test.tar.gz)
