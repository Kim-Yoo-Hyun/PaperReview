# When Life Gives You BC, Make Q-functions: Extracting Q-values from Behavior Cloning for On-Robot Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Evaluation in One Sentence

D4RL·robomimic과 Franka의 실물 조립·부품 배치를 평가했다. 먼저 사전학습한 행동 복제(BC) 정책으로 환경을 실행해 그 정책의 Q값을 추정한다. 이어지는 온라인 단계는 BC와 RL이 제안한 행동을 각각 평가한다. 그림 3은 초기 Q 추정에 쓴 환경 상호작용도 가로축에 포함한다. [방법과 그림 3](https://roboticsproceedings.org/rss22/p153.pdf#page=4) · [상호작용 예산](https://roboticsproceedings.org/rss22/p153.pdf#page=5) · [실물 평가](https://roboticsproceedings.org/rss22/p153.pdf#page=8)

## Evaluation Type and Scope

Abstract/project에 명시된 평가 범위만 기록한다. 아래의 확인 필요 항목과 연구자가 제안한 실험을 paper-reported result로 합치지 않는다.

## Dataset / Benchmark Role

D4RL·robomimic과 실제 pipe assembly·kitting을 평가한다.

Resource 이름은 위 source가 evaluation 용도로 명시한 경우만 사용한다. 정확한 training/evaluation role, split, size와 데이터 중복은 not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Metrics and Success Definition

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Baselines and Fairness

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다. Baseline identity, 같은 observation/action, demonstration/interaction, reward access와 compute 조건을 본문에서 대조한다.

## Ablations and Sensitivity

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Generalization and Failure Cases

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다. 특히 Q 초기화에 필요한 상호작용, 두 정책 유지 비용, gating의 행동 분포 변화을 점검한다.

## Statistics, Efficiency, and Reproducibility

Trials/seeds, confidence interval, checkpoint/commit, reset/timeout, hardware와 control latency는 not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Proposed Evaluation — Researcher Interpretation

초기 BC와 환경 예산을 고정하고 gating 유무 및 BC 유지 regularization을 교차 대조한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p153.html) · [저자 project/code](https://pages.rai-inst.com/q2rl_website/) · [공식 code](https://github.com/rai-opensource/q2rl). Main table·appendix·negative result는 본문 수동 확인 필요.
