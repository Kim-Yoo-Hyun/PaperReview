# Act2Goal: From World Model To General Goal-conditioned Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Problem and Bottleneck

시각 목표로 정한 장시간 조작에서 계획의 일관성과 가까운 feedback을 함께 유지한다.

## Formulation and Robotics Loop

현재 영상·목표 영상 → imagined frames의 가까운/먼 시간 표현 → motor action.

목표 조건부 world model의 미래 영상과 multi-scale temporal hashing을 action expert에 연결하고 hindsight goal relabeling으로 적응한다.

## Assumptions to Verify

시각 목표 접근·hindsight 도달 상태·LoRA 갱신 범위·online 비용.

위 항목은 연구자의 확인 질문이며 논문이 명시한 가정·실패로 확정한 것이 아니다.

## Prior Work and Why It Matters

UVFA/HER·world model → Act2Goal → HINDSIGHT 후보의 relabeling 효과 분해.

Hindsight 목표 변경·world model·단일 정책 연결의 직접 선행이며 언어 VLA와 시각 목표 정책의 경계를 드러낸다.

## Evidence Boundary

[공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p015.html). RSS 공식 abstract를 기준으로 기록. Project는 접근되지만 이번 웹 도구에서 본문을 읽지 못해 코드 공개 상태는 not identified다. Visual-goal 정책을 언어 지시 VLA와 동일시하지 않는다.
