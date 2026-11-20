# Insights — Back to the Familiar Future: Failure Recovery for VLA Policies via Pre-Imagined Milestone Selection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## Paper-supported conclusion

예정 경로에서 벗어난 상태를 미래 시각 조건으로 되돌려 연결한다. 하위 행동 생성기의 추가 미세조정 없이 복구를 평가한다. [원문 및 평가 절](https://arxiv.org/pdf/2606.09258#page=6)

## Researcher interpretation

복구가 가능한 시점에서 미래 시각 목표만 바꾸는 대조군을 제공한다.

- 기본 LIBERO 평가에 실패를 주입하는 프로토콜을 추가한다. §4.1. 관계 대상은 평가 환경이다. [pr-0042 · 원문](https://arxiv.org/pdf/2606.09258#page=5)

## 최소 비교 실험

감지 시점의 지연을 고정하고 이정표 선택과 단순 재계획을 비교한다.
