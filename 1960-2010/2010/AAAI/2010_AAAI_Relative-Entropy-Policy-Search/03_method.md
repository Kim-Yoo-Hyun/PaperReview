# Relative Entropy Policy Search

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Method and Contribution

Relative entropy 제약으로 정책 개선을 제한하고 명시적 갱신을 도출한다.

## Observation, State, and Action

정책 분포·return → 정보 제약 최적화 → 새 정책 분포.

## Objective and Training / Inference Boundary

위 설명은 초록에서 확인한 formulation이다. 정리의 가정·증명·구체적 갱신식은 본문 확인이 필요하다.

점검 항목: KL 방향·분포 제약·sample 추정·실제 행동 변화.

## Method-Specific Comparison — Researcher Interpretation

같은 목표 개선 수준에서 KL 방향·상태 분포를 바꾸고 미학습 목표 행동을 비교한다.

이 비교는 제안이며 실행 결과나 논문의 ablation이 아니다.

## Evidence Boundary

[공식 paper/abstract](https://ojs.aaai.org/index.php/AAAI/article/view/7727). 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
