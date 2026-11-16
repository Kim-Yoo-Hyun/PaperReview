# Reinforcement Learning for Real-Time Vision-Language-Action Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Problem and Bottleneck

VLA 계산 중 늦어진 관측으로 행동하면 동적 과제에서 분포 이동이 생긴다.

## Formulation and Robotics Loop

느린 VLA action chunk + 최신 관측 → 경량 edit policy → 즉시 로봇 행동.

느린 VLA chunk 생성과 최신 관측을 사용하는 빠른 action edit를 분리해 EXPO-FT를 실시간 RL로 확장한다.

## Assumptions to Verify

edit 주파수·관측 timestamp·동기화·robot interaction 비용·단일 정책 여부.

위 항목은 연구자의 확인 질문이며 논문이 명시한 가정·실패로 확정한 것이 아니다.

## Prior Work and Why It Matters

EXPO-FT·asynchronous chunk 실행 → Real-Time EXPO-FT → unified VLA와 지연 대응 비교.

지연·feedback 공백의 직접 선행이자 단일 정책 선호와 별도로 보존할 강한 editor pipeline baseline이다.

## Evidence Boundary

[공식 paper/abstract](https://arxiv.org/abs/2609.18207). arXiv v1와 저자 project/code에서 EXPO-FT 원 방법과 real-time branch의 구분 확인. 공식 conference acceptance는 확인하지 않았다.
