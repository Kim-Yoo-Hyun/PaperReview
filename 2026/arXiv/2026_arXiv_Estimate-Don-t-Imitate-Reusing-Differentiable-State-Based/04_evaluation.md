# Estimate, Don't Imitate: Reusing Differentiable State-Based Policies for Visuomotor Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. 평가표에서 직접 대조한 항목에 해당 쪽수를 표시했다.
> Source audit: 2026-11-23 원문의 실물 평가표에서 성공률과 시행 수를 대조했다.

## Evaluation in One Sentence

시뮬레이션 조작 다섯 과제와 실제 Panda의 큐브 과제로 시각 상태 추정과 상태 기반 전문가의 조합을 평가했다. [과제와 실물 전이](https://arxiv.org/pdf/2609.34018v1#page=1) · [표 IV](https://arxiv.org/pdf/2609.34018v1#page=8)

## Evaluation Type and Scope

시뮬레이션과 실물에서 보고한 결과 중 아래에 명시한 평가표의 항목을 확인했다.

## Dataset / Benchmark Role

표 IV의 시뮬레이션 평가는 학습에 쓰지 않은 배경을 포함해 1,000개 에피소드로 수행했다. 실물 전이는 같은 표에서 별도로 보고한다. [표 IV와 주석](https://arxiv.org/pdf/2609.34018v1#page=8)

## Metrics and Success Definition

실제 Panda에서 완료한 에피소드 25회 중 19회 성공해 76.0%였다. 관절 한계 때문에 중단하고 재시작한 두 시도까지 포함하면 전체 27회 중 19회, 70.4%다. 에피소드당 제한은 40초(제어 200스텝)였다. [표 IV와 주석](https://arxiv.org/pdf/2609.34018v1#page=8)

## Baselines and Fairness

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다. Baseline identity, 같은 observation/action, demonstration/interaction, reward access와 compute 조건을 본문에서 대조한다.

## Ablations and Sensitivity

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Generalization and Failure Cases

실물에서 확인된 중단 사유는 제어기의 관절 한계 검사다. 가림, 물체 종류, 시작 자세에 따른 실패율은 추가 확인이 필요하다. [표 IV 주석](https://arxiv.org/pdf/2609.34018v1#page=8)

## Statistics, Efficiency, and Reproducibility

표 IV의 평균 제어 스텝 수와 표준편차는 성공 에피소드에서 계산했다. 독립 학습 시드에 따른 편차와 실물 제어 지연은 추가 확인이 필요하다. [표 IV 주석](https://arxiv.org/pdf/2609.34018v1#page=8)

## Proposed Evaluation — Researcher Interpretation

같은 estimator·expert·시연에서 state-only, action-consistency 혼합, task outcome supervision을 비교한다. 이는 제안이며 원 논문 결과가 아니다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.34018). 그 밖의 표와 부록의 실패 사례는 추가 확인이 필요하다.
