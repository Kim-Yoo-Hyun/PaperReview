# Behavior-Skill: A Fine-Grained Benchmark for Evaluating Vision-Language-Action Policies in Long-Horizon Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Evaluation in One Sentence

50개 household task의 시연으로 구성한 benchmark에서 π0.5와 GR00T 등 정책을 평가한다. 복원된 유효 시작 상태의 개별 능력은 이전 정책이 실제 도달한 상태에서의 연결 실행 성능과 구분한다.

## Evaluation Type and Scope

Abstract/project에 명시된 평가 범위만 기록한다. 아래의 확인 필요 항목과 연구자가 제안한 실험을 paper-reported result로 합치지 않는다.

## Dataset / Benchmark Role

자체 Behavior-Skill benchmark를 구성하고 평가한다. 이는 공식 abstract가 명시한 역할이며, 아래 split·protocol의 미확인 세부사항과 구분한다.

50개 household task의 시연으로 구성한 benchmark에서 π0.5와 GR00T 등 정책을 평가한다. 복원된 유효 시작 상태의 개별 능력은 이전 정책이 실제 도달한 상태에서의 연결 실행 성능과 구분한다.

Resource 이름은 위 source가 evaluation 용도로 명시한 경우만 사용한다. 정확한 training/evaluation role, split, size와 데이터 중복은 not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Metrics and Success Definition

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Baselines and Fairness

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다. Baseline identity, 같은 observation/action, demonstration/interaction, reward access와 compute 조건을 본문에서 대조한다.

## Ablations and Sensitivity

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Generalization and Failure Cases

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다. 특히 공개 release와 논문 정책 쌍의 일치, 시연 reset과 continuation의 차이, 학습/평가 instance 분리, normalizer와 controller·queue·종료 정의을 점검한다.

## Statistics, Efficiency, and Reproducibility

Trials/seeds, confidence interval, checkpoint/commit, reset/timeout, hardware와 control latency는 not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Proposed Evaluation — Researcher Interpretation

같은 task·정책·success checker에서 시연 복원 시작과 실제 navigation 도착 시작을 비교하고, 정책 교체·도착 설정·reset 차이를 분리한다. 현재 P0는 실행 준비 단계이며 실측 효과가 없다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2608.30536) · [저자 project/code](https://github.com/nubot-nudt/Behavior-Skill). Main table·appendix·negative result는 본문 수동 확인 필요.
