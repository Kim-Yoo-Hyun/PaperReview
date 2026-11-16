# Autonomous Improvement of Instruction Following Skills via Foundation Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Evaluation in One Sentence

공식 abstract는 새로운 실세계 환경의 정책 개선과 5개 tabletop 환경에서 수집한 25K trajectory 데이터 공개를 설명한다. Project는 9개 평가 scene을 설명하므로 두 숫자의 분모를 합치지 않는다.

## Evaluation Type and Scope

Abstract/project에 명시된 평가 범위만 기록한다. 아래의 확인 필요 항목과 연구자가 제안한 실험을 paper-reported result로 합치지 않는다.

## Dataset / Benchmark Role

공식 abstract는 새로운 실세계 환경의 정책 개선과 5개 tabletop 환경에서 수집한 25K trajectory 데이터 공개를 설명한다. Project는 9개 평가 scene을 설명하므로 두 숫자의 분모를 합치지 않는다.

Resource 이름은 위 source가 evaluation 용도로 명시한 경우만 사용한다. 정확한 training/evaluation role, split, size와 데이터 중복은 not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Metrics and Success Definition

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Baselines and Fairness

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다. Baseline identity, 같은 observation/action, demonstration/interaction, reward access와 compute 조건을 본문에서 대조한다.

## Ablations and Sensitivity

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Generalization and Failure Cases

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다. 특히 수집 scene과 평가 scene의 분리, 데이터 release의 실제 접근성, 의미 이해와 운동 능력 개선의 기여, 서로 다른 정책 정보량을 점검한다.

## Statistics, Efficiency, and Reproducibility

Trials/seeds, confidence interval, checkpoint/commit, reset/timeout, hardware와 control latency는 not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Proposed Evaluation — Researcher Interpretation

동일 원 경험·성공 판정·학습 예산을 고정하고 언어와 image-goal 감독의 추가 정보 차이를 먼저 감사한 뒤 지시 성공과 goal-reaching 성공을 분리 평가한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v270/zhou25b.html) · [저자 project/code](https://soar-autonomous-improvement.github.io/) · [공식 code](https://github.com/soar-autonomous-improvement/code-release). Main table·appendix·negative result는 본문 수동 확인 필요.
