# SafeLoop: Risk-Aware Rollback for Vision-Language-Action Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 쪽수를 붙인 문장을 원문과 대조했다.
> Source audit: 2026-11-24에 아래 쪽수의 평가 설정과 결과를 대조했다.

## Evaluation in One Sentence

시뮬레이션은 LIBERO 24개 과제에 시드 16개씩을 사용해 방법별 384회 시행했다. 실물 검증은 세 과제를 각각 25회 수행해 위해 사건과 작업 성공을 기록했다. [PDF 5쪽](https://arxiv.org/pdf/2609.26313v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2609.26313v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2609.26313v1#page=7)

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT AND SIMULATION`.

LIBERO에서 위험 상황을 포함한 조작을 시험하고 실제 로봇에서 세 가지 과제를 별도로 수행했다. [PDF 5쪽](https://arxiv.org/pdf/2609.26313v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2609.26313v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2609.26313v1#page=7)

## Dataset / Benchmark Role

24개 가상 과제와 3개 실물 과제로 위험 감시와 복구의 전이를 확인했다. [PDF 5쪽](https://arxiv.org/pdf/2609.26313v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2609.26313v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2609.26313v1#page=7)

## Metrics and Success Definition

과제 성공과 로봇 몸체 충돌·물체 실패의 발생을 별도로 집계한다. [PDF 5쪽](https://arxiv.org/pdf/2609.26313v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2609.26313v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2609.26313v1#page=7)

## Baselines and Fairness

같은 기반 정책을 단독 실행한 조건과 위험 예측·후퇴를 사용하는 조건을 비교했다. [PDF 5쪽](https://arxiv.org/pdf/2609.26313v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2609.26313v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2609.26313v1#page=7)

## Ablations and Sensitivity

표 II는 같은 π₀ 기반 정책에서 후퇴·재표집과 위험 예측의 시간 구간을 바꾸어 성공과 위해 사건을 비교한다. [PDF 6쪽](https://arxiv.org/pdf/2609.26313v1#page=6)

## Generalization and Failure Cases

실물에서는 위험 예측기를 조정한 뒤 시뮬레이션에서 학습한 의사결정기를 재사용했다. 위험을 감지했을 때 정지하는 방법은 작업을 조기에 끝낼 수 있다. [PDF 6쪽](https://arxiv.org/pdf/2609.26313v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2609.26313v1#page=7)

## Statistics, Efficiency, and Reproducibility

- 시뮬레이션은 과제별 시드 16개로 방법별 롤아웃 384회를 실행했다. [PDF 5쪽](https://arxiv.org/pdf/2609.26313v1#page=5)
- 실물은 각 과제에서 롤아웃 25회를 수행했다. [PDF 7쪽](https://arxiv.org/pdf/2609.26313v1#page=7)

## Proposed Evaluation — Researcher Interpretation

같은 event 이후 continue·hold·rollback의 실제 object/task 상태를 비교한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

LIBERO 조작과 실물 과제에서 충돌·물체 실패와 작업 성공을 함께 측정해 후퇴 전략을 비교했다. [PDF 5쪽](https://arxiv.org/pdf/2609.26313v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2609.26313v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2609.26313v1#page=7)
