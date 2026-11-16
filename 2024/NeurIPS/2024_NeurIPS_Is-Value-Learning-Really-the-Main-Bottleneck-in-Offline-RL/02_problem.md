# Is Value Learning Really the Main Bottleneck in Offline RL?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Problem and Bottleneck

Offline RL이 BC보다 낮을 때 원인이 항상 value 오차인지 묻는다.

## Formulation and Robotics Loop

같은 offline data·가치함수 → 서로 다른 policy extraction → ID/OOD 상태 행동.

Value learning·policy extraction·test-state 일반화를 분리해 비교하고 policy 개선 대안을 분석한다.

## Assumptions to Verify

critic 고정·extraction 예산·평가 state coverage·test-time 최적화 비용.

위 항목은 연구자의 확인 질문이며 논문이 명시한 가정·실패로 확정한 것이 아니다.

## Prior Work and Why It Matters

IQL/AWAC·TD3+BC → policy extraction 진단 → WCM·FQL의 이득 분해.

단일 VLA critic 개선 후보가 actor 학습·coverage 효과를 놓치지 않도록 하는 핵심 원인 분석이다.

## Evidence Boundary

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2024/hash/8ffb4e3118280a66b192b6f06e0e2596-Abstract-Conference.html). 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
