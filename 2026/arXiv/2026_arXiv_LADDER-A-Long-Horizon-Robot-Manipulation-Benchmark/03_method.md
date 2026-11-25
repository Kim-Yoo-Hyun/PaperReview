# LADDER: A Long-Horizon Robot Manipulation Benchmark

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

같은 환경에서 하위 목표 수를 1–10개로 바꾸고 직접 지시, 하위 지시, 도구 선택을 비교한다.

## Observation–State–Action Interface

언어 지시와 관측을 받는 실행 정책 또는 상위 조정기가 하위 동작·도구를 선택한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 시스템별 사용 가능한 성공 판정, 재시도 권한과 평가 예산.

Source가 명시한 evaluation 범위: 저자는 3개 시뮬레이션 평가군, 145과제, 시스템당 2,024회와 두 로봇 구성의 실물 실험을 보고했다. 시스템별 제어·추론 예산을 함께 봐야 한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 과제·정책·남은 시간을 맞춘 실행 쌍에서 단계별 완료와 다음 물체의 실제 접촉을 대조한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.18053) · [저자 project/code](https://ladder.insait.ai/) · [공식 code](https://github.com/insait-institute/ladder). 수식·세부 구현·코드 실행은 미검증이다.
