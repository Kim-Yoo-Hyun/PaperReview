# ContextFlow: In-Context Flow Matching for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 표시한 평가 항목을 확인했다.
> Source audit: 2026-11-24 원문 대조.

## Evaluation in One Sentence

LIBERO 미학습 구성에서 평균 성공률은 ContextFlow 73.5%, ICRT 38.5%로 35%p 차이다. 실물의 빨간 펜을 왼손부터 잡아 뚜껑을 여는 조건에서는 각각 4/10과 0/10이었다. [PDF 10쪽](https://arxiv.org/pdf/2609.06852v1#page=10) · [PDF 14쪽](https://arxiv.org/pdf/2609.06852v1#page=14)

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT AND SIMULATION`.

## Dataset / Benchmark Role

LIBERO-Spatial·Object의 미학습 구성과 실물 단팔·양팔 조작을 별도 표로 비교했다. [PDF 10쪽](https://arxiv.org/pdf/2609.06852v1#page=10) · [PDF 14쪽](https://arxiv.org/pdf/2609.06852v1#page=14)

## Metrics and Success Definition

시뮬레이션 표는 구성별 성공률과 평균을, 실물 표는 성공 횟수와 시행 수를 보고한다. [PDF 10쪽](https://arxiv.org/pdf/2609.06852v1#page=10) · [PDF 14쪽](https://arxiv.org/pdf/2609.06852v1#page=14)

## Baselines and Fairness

두 평가 모두 ICRT와 비교한다. [PDF 10쪽](https://arxiv.org/pdf/2609.06852v1#page=10) · [PDF 14쪽](https://arxiv.org/pdf/2609.06852v1#page=14)

## Statistics, Efficiency, and Reproducibility

실물 표 8의 각 모델·구성 조합은 시행 10회다. [PDF 14쪽](https://arxiv.org/pdf/2609.06852v1#page=14)

## Proposed Evaluation — Researcher Interpretation

동일 정책 규모와 새 시연으로 context-only·gradient adaptation을 대조한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://link.springer.com/chapter/10.1007/978-3-032-37531-5_16) · [저자 project/code](https://dingjiansw101.github.io/contextflow-page/) · [공식 code](https://github.com/dingjiansw101/ContextFlow).
