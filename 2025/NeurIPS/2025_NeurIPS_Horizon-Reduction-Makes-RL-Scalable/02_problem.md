# Horizon Reduction Makes RL Scalable

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Problem and Bottleneck

데이터·모델을 늘려도 긴 horizon의 offline RL 성능이 포화되는 이유를 분석한다.

## Formulation and Robotics Loop

대규모 goal-conditioned data → horizon을 줄인 value/policy 학습 → 목표 행동.

Horizon 감소 기법을 비교하고 짧은 유효 결정 길이를 활용하는 SHARSA를 제안한다.

## Assumptions to Verify

유효 결정 길이·coverage·데이터 크기·학습 계산량·물리 시간.

위 항목은 연구자의 확인 질문이며 논문이 명시한 가정·실패로 확정한 것이 아니다.

## Prior Work and Why It Matters

Options·HIQL·OGBench → horizon reduction → VLA chunk/return 설계.

Chunk 길이·목표 분해와 데이터 scaling의 효과를 분리할 최신 기준 연구다.

## Evidence Boundary

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0c66099070429b9b49ad8bb19c740c22-Abstract-Conference.html). 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
