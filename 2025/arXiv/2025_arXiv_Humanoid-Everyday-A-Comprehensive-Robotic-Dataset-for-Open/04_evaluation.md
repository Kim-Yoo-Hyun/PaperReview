# Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`.
> Source audit: 2026-11-16: arXiv abstract·공식 project/repository 확인. abstract 기반 — 본문 수동 확인 필요. ICRA 게재는 공식 근거 확인 대기.
> Canonical metadata: [01_overview.md](./01_overview.md).

## Evaluation Type and Scope

DATASET / BENCHMARK. [공식 project](https://humanoideveryday.github.io/)의10.3k trajectories·3M+ frames·260tasks/7categories는 수집 규모다. 평가 trial 수나 성공률 분모로 옮기지 않는다.

## Dataset / Benchmark Role

Unitree G1/H1의 open-world 조작 학습 자료. Ψ₀에서 쓰는 subset과 전체 corpus를 구분한다.

## Metrics and Success Definition

not recorded — 이번 초록/project 검토만으로 정확한 학습/평가 split·trial·metric 정의를 확정하지 않는다.

## Baselines and Fairness

not recorded — embodiment별 action dimensionality·teleop 방식·작업/scene 누수를 본문에서 대조해야 한다.

## Ablations and Sensitivity

not recorded — 본문 수동 확인 필요.

## Generalization and Failure Cases

넓은 시연 범위가 unseen robot/scene의 성능 입증은 아니다. Sensor 결측·action 변환·서로 다른 controller 지원 범위가 재사용 제약이다.

## Statistics, Efficiency, and Reproducibility

[공식 code/data 링크](https://github.com/physical-superintelligence-lab/Humanoid-Everyday) 확인. Project의 cloud 평가 안내와 repository 링크 상태가 다르므로 서비스가 실제 작동한다고 기록하지 않는다. 다운로드·runtime 검증은 하지 않았다.
