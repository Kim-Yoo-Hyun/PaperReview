# DART: Noise Injection for Robust Imitation Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Problem and Bottleneck

시연 분포를 벗어난 BC 정책의 오류 누적과 사람이 제공하는 corrective data 비용을 다룬다.

## Formulation and Robotics Loop

교란된 시연 상황 → 전문가 복구 행동 → offline imitation 정책.

전문가가 시연할 때 noise를 주입하고 학습 정책의 오류에 맞춰 noise 수준을 조절한다.

## Assumptions to Verify

noise 분포·전문가 회복 능력·개입 비용·train-test 교란.

위 항목은 연구자의 확인 질문이며 논문이 명시한 가정·실패로 확정한 것이 아니다.

## Prior Work and Why It Matters

DAgger·BC 분포 이동 → DART → VLA recovery·RL 데이터 수집 비교.

복구 성공을 RL 고유 이득으로 해석하기 전 넘어야 할 강한 데이터 수집·모방 대안이다.

## Evidence Boundary

[공식 paper/abstract](https://proceedings.mlr.press/v78/laskey17a.html). 공식 CoRL abstract 및 저자 project/code 공개 확인. 공개 repository의 simulation 구현과 실제 HSR 재현 경로는 구별한다.
