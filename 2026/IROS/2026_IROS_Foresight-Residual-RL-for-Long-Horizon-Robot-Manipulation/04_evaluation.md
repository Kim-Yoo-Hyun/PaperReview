# Foresight Residual RL for Long-Horizon Robot Manipulation with Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 쪽수를 붙인 문장을 원문과 대조했다.
> Source audit: 2026-11-24에 아래 쪽수의 평가 설정과 결과를 대조했다.

## Evaluation in One Sentence

표 II의 각 단계는 전문가 상태에서 시작하고 전체 작업은 처음부터 실행한다. Isaac Gym의 전체 조립 성공률은 기본 잔차 정책 54.5%, 다음 단계 성공 가능성을 보상에 반영한 정책 85.6%다. [PDF 6쪽](https://arxiv.org/pdf/2607.16506v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2607.16506v1#page=7)

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.

Isaac Gym에서 Kuka IIWA와 세 손가락 그리퍼로 렌치를 잡고 너트에 삽입한 뒤 회전시켰다. [PDF 6쪽](https://arxiv.org/pdf/2607.16506v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2607.16506v1#page=7)

## Dataset / Benchmark Role

렌치 조립을 파지·이동과 삽입·회전의 세 단계로 구성했다. [PDF 6쪽](https://arxiv.org/pdf/2607.16506v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2607.16506v1#page=7)

## Metrics and Success Definition

표 II는 단계·연속 두 단계·전체 작업의 성공률을 구분한다. 회전 성공에는 삽입을 유지하며 너트를 60도 이상 돌리는 조건이 있다. [PDF 6쪽](https://arxiv.org/pdf/2607.16506v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2607.16506v1#page=7)

## Baselines and Fairness

전체 동작을 직접 학습한 π₀, 단계별 π₀, 기본 잔차 RL과 후속 성공을 반영한 잔차 RL을 비교했다. [PDF 6쪽](https://arxiv.org/pdf/2607.16506v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2607.16506v1#page=7)

## Ablations and Sensitivity

표 II에서 기본 잔차 정책과 후속 성공 가능성을 반영한 정책을 같은 조립 과제에서 비교한다. 표 III는 두 정책이 도달한 인계 상태의 예측 점수를 보고한다. [PDF 7쪽](https://arxiv.org/pdf/2607.16506v1#page=7)

## Generalization and Failure Cases

저자가 명시한 범위는 단계가 정해진 한 가지 시뮬레이션 조립 작업이다. [PDF 8쪽](https://arxiv.org/pdf/2607.16506v1#page=8)

## Statistics, Efficiency, and Reproducibility

- 방법별 평가에 시드 4개와 총 에피소드 512개를 사용했다. 성공률은 평균과 표준편차로 보고한다. [PDF 6쪽](https://arxiv.org/pdf/2607.16506v1#page=6)

## Proposed Evaluation — Researcher Interpretation

동일 rollout budget에서 local reward·foresight reward·outcome ranker를 비교한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

Isaac Gym의 렌치 조립 과제에서 단계별 성공과 전체 조립 성공을 따로 비교해 단계 사이 인계 상태의 영향을 측정했다. [PDF 6쪽](https://arxiv.org/pdf/2607.16506v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2607.16506v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2607.16506v1#page=8)
