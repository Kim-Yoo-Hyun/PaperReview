# Tune to Learn: How Controller Gains Shape Robot Policy Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Method and Contribution

정책과 제어 동역학의 상호작용을 바탕으로 BC·RL·sim-to-real에서 gain regime을 비교한다.

## Observation, State, and Action

정책의 목표 위치 → gain이 정한 controller → 로봇 상태 → 정책 feedback.

## Objective and Training / Inference Boundary

초록에서 확인한 학습 구성이다. 정확한 loss·gradient 경로·학습/추론 차이·controller 또는 memory 시간 단위는 본문 확인이 필요하다.

점검 항목: gain 단위·controller rate·policy 반응·hyperparameter 예산·sim-to-real 차이.

## Method-Specific Comparison — Researcher Interpretation

고정 gain grid와 학습 gain을 같은 정책·데이터·튜닝 예산에서 비교한다.

이 비교는 제안이며 실행 결과나 논문의 ablation이 아니다.

## Evidence Boundary

[공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p139.html). RSS의 Shape 제목을 사용하고 저자 페이지의 Affect 제목은 alias로 연결한다. Workshop award를 RSS 수상으로 기록하지 않는다.
