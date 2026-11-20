# Robo3R: Enhancing Robotic Manipulation with Accurate Feed-Forward 3D Reconstruction

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
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
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인.

## Problem and Importance

깊이 센서와 기존 재구성의 scale/정밀도 오차가 로봇 물리 상호작용을 방해한다.

## Core Idea and Contribution

RGB와 robot state에서 local geometry·camera pose를 추정하고 robot frame의 metric geometry로 정렬한다.

## Observation–State–Action Interface

RGB/로봇 상태 → point map·camera pose·robot-frame scene geometry; 별도 downstream policy에 전달한다.

## Evaluation Scope and Claim Boundary

Robo3R-4M 합성 데이터로 학습하고 imitation·sim-to-real·grasp synthesis·collision-free planning의 downstream 효과를 평가한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p056.html) · [저자 project/code](https://yangsizhe.github.io/robo3r/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

TASK-GEOMETRY가 일반 재구성 정확도 개선의 반복인지 판단할 직접 비교다.

## Verification Boundary

Robot state privilege·similarity transform·훈련 물체 중복·latency을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
