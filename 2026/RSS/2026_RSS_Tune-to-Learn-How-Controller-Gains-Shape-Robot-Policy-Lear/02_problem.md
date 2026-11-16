# Tune to Learn: How Controller Gains Shape Robot Policy Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Problem and Bottleneck

Position controller gain 선택이 로봇 정책 학습에 미치는 영향을 묻는다.

## Formulation and Robotics Loop

정책의 목표 위치 → gain이 정한 controller → 로봇 상태 → 정책 feedback.

정책과 제어 동역학의 상호작용을 바탕으로 BC·RL·sim-to-real에서 gain regime을 비교한다.

## Assumptions to Verify

gain 단위·controller rate·policy 반응·hyperparameter 예산·sim-to-real 차이.

위 항목은 연구자의 확인 질문이며 논문이 명시한 가정·실패로 확정한 것이 아니다.

## Prior Work and Why It Matters

Impedance control → gain별 learnability 분석 → CompVLA·CONTACT-RL 공정 비교.

접촉 VLA RL의 이득을 baseline gain 튜닝과 분리해야 함을 보이는 직접 선행이다.

## Evidence Boundary

[공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p139.html). RSS의 Shape 제목을 사용하고 저자 페이지의 Affect 제목은 alias로 연결한다. Workshop award를 RSS 수상으로 기록하지 않는다.
