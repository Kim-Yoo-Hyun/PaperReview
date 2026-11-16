# Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`.
> Source audit: 2026-11-16: arXiv abstract·공식 project/repository 확인. abstract 기반 — 본문 수동 확인 필요. ICRA 게재는 공식 근거 확인 대기.
> Canonical metadata: [01_overview.md](./01_overview.md).

## Target Problem

Humanoid의 현실 조작에 필요한 diverse robot data가 부족하다. 서로 다른 환경과 작업에서 수집한 trajectory를 학습 자원으로 제공한다. [초록](https://arxiv.org/abs/2510.08807).

## Assumptions and Closed Loop

센서·상태·행동의 시간/좌표 정렬과 embodiment별 action 해석이 전제다. 학습 데이터 단계의 기여이며 모든 상태 필드가 정책에서 실행 가능한 command라는 뜻은 아니다.
