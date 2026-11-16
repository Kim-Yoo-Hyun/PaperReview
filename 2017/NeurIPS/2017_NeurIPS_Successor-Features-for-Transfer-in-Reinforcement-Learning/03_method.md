# Successor Features for Transfer in Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Method and Contribution

미래 feature 방문을 보상 가중치와 분리하고 generalized policy improvement로 기존 정책들을 재사용한다.

## Observation, State, and Action

상태·동작 → successor feature; 새 보상 가중치 → 정책 집합에서 행동 선택.

## Objective and Training / Inference Boundary

위 설명은 초록에서 확인한 formulation이다. 정리의 가정·증명·구체적 갱신식은 본문 확인이 필요하다.

점검 항목: 공유 동역학·보상 선형성·feature 근사·정책 coverage.

## Method-Specific Comparison — Researcher Interpretation

보상만 변경한 조건과 동역학까지 변경한 조건을 분리해 동일 전이 절차를 비교한다.

이 비교는 제안이며 실행 결과나 논문의 ablation이 아니다.

## Evidence Boundary

[공식 paper/abstract](https://proceedings.neurips.cc/paper/2017/hash/350db081a661525235354dd3e19b8c05-Abstract.html). 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
