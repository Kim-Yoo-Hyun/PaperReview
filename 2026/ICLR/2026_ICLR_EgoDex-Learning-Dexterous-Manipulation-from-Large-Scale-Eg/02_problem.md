# EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video

> Evidence maturity: `ABSTRACT_CHECKED`.
> Source audit: 2026-11-16: 공식 초록·ICLR 목록·repository 확인. abstract 기반 — 본문 수동 확인 필요. 사용자 상태 UNREAD 유지.
> Canonical metadata: [01_overview.md](./01_overview.md).

## Target Problem and Assumptions

일상 손 조작 영상만으로 행동의 공간적 구조를 학습하기 어렵다. EgoDex는 추적된 손/손목 pose와 언어를 연결한다. [초록](https://arxiv.org/abs/2505.11709).

## Robotics Closed Loop

직접 제어기보다 사전학습 자료에 해당한다. 사람 pose→로봇 가동 범위/접촉/좌표계를 연결하는 가정이 남는다. 사람 예측 오차의 감소를 로봇 성공 증가로 자동 해석하지 않는다.
