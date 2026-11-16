# HIQL: Offline Goal-Conditioned RL with Latent States as Actions

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Problem and Bottleneck

긴 목표 거리에서 가치 추정 오차가 offline goal-reaching 정책을 망가뜨린다.

## Formulation and Robotics Loop

상태·최종 목표 → latent subgoal → 실제 행동; 공유 value에서 두 정책 학습.

하나의 action-free 가치함수에서 latent subgoal 정책과 그 목표에 도달하는 하위 정책을 추출한다.

## Assumptions to Verify

goal relabeling·latent 목표 표현·subgoal 거리·action-free 데이터 범위.

위 항목은 연구자의 확인 질문이며 논문이 명시한 가정·실패로 확정한 것이 아니다.

## Prior Work and Why It Matters

UVFA·IQL → HIQL → SHARSA/OGBench·VLA 장기 조작.

공유 가치함수와 계층 정책을 단일 actor 공동 학습과 구별하고 장기 credit 문제의 강한 대안으로 비교한다.

## Evidence Boundary

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6d7c4a0727e089ed6cdd3151cbe8d8ba-Abstract-Conference.html). 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
