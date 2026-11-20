# Active Perception for Grasp Detection via Neural Graspness Field

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

- Year/Venue: 2024 / NeurIPS
- Authors: Haoxiang Ma, Modi Shi, Boyang Gao, Di Huang
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: active perception, next-best-view, grasp detection
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2024/hash/4364fef031fdf7bfd9d1c9c56b287084-Abstract-Conference.html
- Code/Project: not identified

## 연구 질문과 기여

파지 가능성의 시점 간 불일치로 카메라를 움직여 파지 자세를 추정한다.

여러 관측에서 신경 파지 가능성 필드를 구성한다. 불일치가 큰 방향을 선택해 새 관측을 실제 파지 검출에 반영한다.

## 평가 범위

GraspNet 기반 능동 파지 평가와 실물 파지에서 관측 시간과 성공의 교환관계를 측정했다. [원문 및 평가 절](https://proceedings.neurips.cc/paper_files/paper/2024/file/4364fef031fdf7bfd9d1c9c56b287084-Paper-Conference.pdf#page=8)

## 선정 근거

재구성 품질 대신 파지 목표에 대한 불확실성으로 카메라 시점을 고르는 기준이다.
