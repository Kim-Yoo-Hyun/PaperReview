# CompVLA: A Variable Compliance Vision-Language-Action Model for Contact-rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Evaluation in One Sentence

Franka 실물에서 화이트보드 지우기·물체 기울이기·컵 꺼내기는 접촉 과제로, 집어 옮기기는 일반 조작 과제로 평가했다. 표의 평균은 앞의 세 접촉 과제만 포함한다. 지우기 점수는 지운 글자 비율이고 다른 과제의 점수는 에피소드 성공률이다. [과제 정의](https://arxiv.org/pdf/2609.23614v2#page=7) · [실물 결과와 분모](https://arxiv.org/pdf/2609.23614v2#page=8)

## Evaluation Type and Scope

Abstract/project에 명시된 평가 범위만 기록한다. 아래의 확인 필요 항목과 연구자가 제안한 실험을 paper-reported result로 합치지 않는다.

## Dataset / Benchmark Role

접촉 과제에서 vanilla/compliance-aware VLA 및 구성요소 ablation을 비교한다.

Resource 이름은 위 source가 evaluation 용도로 명시한 경우만 사용한다. 정확한 training/evaluation role, split, size와 데이터 중복은 not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Metrics and Success Definition

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Baselines and Fairness

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다. Baseline identity, 같은 observation/action, demonstration/interaction, reward access와 compute 조건을 본문에서 대조한다.

## Ablations and Sensitivity

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Generalization and Failure Cases

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다. 특히 강성–displacement 식별성, force 입력 유무, 데이터·controller 공정성을 점검한다.

## Statistics, Efficiency, and Reproducibility

Trials/seeds, confidence interval, checkpoint/commit, reset/timeout, hardware와 control latency는 not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Proposed Evaluation — Researcher Interpretation

동일 동작·gain 표현에서 imitation과 RL을 같은 초기화로 대조한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.23614) · [저자 project/code](https://compvla.github.io/). Main table·appendix·negative result는 본문 수동 확인 필요.
