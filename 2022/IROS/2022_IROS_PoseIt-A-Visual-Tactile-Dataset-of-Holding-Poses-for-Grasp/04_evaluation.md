# PoseIt: A Visual-Tactile Dataset of Holding Poses for Grasp Stability Analysis

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Evaluation in One Sentence

저자 자료는 26개 물체의 실물 기록을 제공하며 초록은 미관측 물체와 자세에 대한 예측을 평가한다. 자세 이동 중 실패와 마지막 흔들기 결과는 별개다.

## Evaluation Type and Scope

Abstract/project에 명시된 평가 범위만 기록한다. 아래의 확인 필요 항목과 연구자가 제안한 실험을 paper-reported result로 합치지 않는다.

## Dataset / Benchmark Role

저자 자료는 26개 물체의 실물 기록을 제공하며 초록은 미관측 물체와 자세에 대한 예측을 평가한다. 자세 이동 중 실패와 마지막 흔들기 결과는 별개다.

Resource 이름은 위 source가 evaluation 용도로 명시한 경우만 사용한다. 정확한 training/evaluation role, split, size와 데이터 중복은 not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Metrics and Success Definition

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Baselines and Fairness

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다. Baseline identity, 같은 observation/action, demonstration/interaction, reward access와 compute 조건을 본문에서 대조한다.

## Ablations and Sensitivity

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Generalization and Failure Cases

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다. 특히 물체 분할, 파지 명령이 변경된 시점과 단계별 실패 라벨의 의미을 점검한다.

## Statistics, Efficiency, and Reproducibility

Trials/seeds, confidence interval, checkpoint/commit, reset/timeout, hardware와 control latency는 not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Proposed Evaluation — Researcher Interpretation

물체를 분리한 검증에서 이동 중 실패와 흔들기 실패를 나누고 같은 힘 예산의 단순 대조를 포함한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://ieeexplore.ieee.org/document/9981562/) · [저자 project/code](https://publish.illinois.edu/robotouch/poseit-a-visual-tactile-dataset-of-holding-poses-for-grasp-stability-analysis/) · [공식 code](https://github.com/Robo-Touch/PoseIt). Main table·appendix·negative result는 본문 수동 확인 필요.
