# Do VLAs Really Follow Instructions? Diagnosing How-Level Instruction Following in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Evaluation in One Sentence

보강된 지시에 대한 행동 반응이 늘어도 작업 성공이 일관되게 높아지지는 않으며, 까다롭거나 분포 밖의 지시에 일반화가 제한된다고 보고한다. SIMPLER-IN의 상세 task·split·trial은 본문 확인 대상이다.

## Evaluation Type and Scope

Abstract/project에 명시된 평가 범위만 기록한다. 아래의 확인 필요 항목과 연구자가 제안한 실험을 paper-reported result로 합치지 않는다.

## Dataset / Benchmark Role

보강된 지시에 대한 행동 반응이 늘어도 작업 성공이 일관되게 높아지지는 않으며, 까다롭거나 분포 밖의 지시에 일반화가 제한된다고 보고한다. SIMPLER-IN의 상세 task·split·trial은 본문 확인 대상이다.

Resource 이름은 위 source가 evaluation 용도로 명시한 경우만 사용한다. 정확한 training/evaluation role, split, size와 데이터 중복은 not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Metrics and Success Definition

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Baselines and Fairness

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다. Baseline identity, 같은 observation/action, demonstration/interaction, reward access와 compute 조건을 본문에서 대조한다.

## Ablations and Sensitivity

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Generalization and Failure Cases

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다. 특히 SIMPLER-IN 조건별 성공 정의와 중립 문장 대조, 지시 보강 학습의 정보·데이터 통제, OOD 범위, 평가 코드와 checkpoint 일치을 점검한다.

## Statistics, Efficiency, and Reproducibility

Trials/seeds, confidence interval, checkpoint/commit, reset/timeout, hardware와 control latency는 not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Proposed Evaluation — Researcher Interpretation

같은 상태의 목표만 지시·제약 포함 지시·의미 동일 재진술을 구분해 기록한다. 자동 의미 갱신과 물리적 수행 실패를 분리하며 아직 정책 실행은 하지 않았다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.21251) · [저자 project/code](https://github.com/sangwu99/how-level-vla-Arxiv). Main table·appendix·negative result는 본문 수동 확인 필요.
