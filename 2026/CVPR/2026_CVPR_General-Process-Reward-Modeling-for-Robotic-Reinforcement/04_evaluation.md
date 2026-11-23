# General Process Reward Modeling for Robotic Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. 평가표에서 직접 대조한 항목에 해당 쪽수를 표시했다.
> Source audit: 2026-11-23 원문의 실물 평가표에서 성공률과 시행 수를 대조했다.

## Evaluation in One Sentence

시뮬레이션 열 과제와 실물 여덟 과제에서 최종 성공률과 표본 효율을 비교했다. [표 3](https://openaccess.thecvf.com/content/CVPR2026/papers/Tan_General_Process_Reward_Modeling_for_Robotic_Reinforcement_Learning_CVPR_2026_paper.pdf#page=8)

## Evaluation Type and Scope

시뮬레이션과 실물에서 보고한 결과 중 아래에 명시한 평가표의 항목을 확인했다.

## Dataset / Benchmark Role

Simulation·실제 조작에서 reward 평가와 policy 학습을 보고한다.

Resource 이름은 위 source가 evaluation 용도로 명시한 경우만 사용한다. 정확한 training/evaluation role, split, size와 데이터 중복은 not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Metrics and Success Definition

실물 여덟 과제에서 Dopamine-RL의 최종 평균 성공률은 95.2%였다. 표 3의 150회는 각 방법이 자기 최종 성공률의 80%에 도달할 때까지의 에피소드 수다. 같은 표에서 희소 보상 RL은 최종 68.0%, 183회를 기록했다. [표 3 및 지표 정의](https://openaccess.thecvf.com/content/CVPR2026/papers/Tan_General_Process_Reward_Modeling_for_Robotic_Reinforcement_Learning_CVPR_2026_paper.pdf#page=8)

## Baselines and Fairness

표 3의 기준선은 시연 50개를 쓴 행동 복제와 희소 보상 RL이다. 각 방법의 보상 접근 조건과 총 학습 비용을 맞췄는지는 별도 확인이 필요하다. [표 3](https://openaccess.thecvf.com/content/CVPR2026/papers/Tan_General_Process_Reward_Modeling_for_Robotic_Reinforcement_Learning_CVPR_2026_paper.pdf#page=8)

## Ablations and Sensitivity

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다.

## Generalization and Failure Cases

not recorded — 이번 abstract/project 조사에서 확인하지 못한 항목이며, 논문 자체의 미보고를 뜻하지 않는다. 특히 보존 정리의 가정, 종료 처리, multi-view 특권, task별 추가 시연을 점검한다.

## Statistics, Efficiency, and Reproducibility

표 4는 Insert Square, Circuit, Cap Pen 세 과제에서 각 정책·조건별 20회 중 성공 횟수를 보고한다. 독립 학습 시드 수와 성공률의 신뢰구간은 추가 확인이 필요하다. [표 4](https://openaccess.thecvf.com/content/CVPR2026/papers/Tan_General_Process_Reward_Modeling_for_Robotic_Reinforcement_Learning_CVPR_2026_paper.pdf#page=8)

## Proposed Evaluation — Researcher Interpretation

보상 오류를 독립 측정하고 sparse-only, 직접 dense, invariant shaping을 같은 rollout budget으로 비교한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Tan_General_Process_Reward_Modeling_for_Robotic_Reinforcement_Learning_CVPR_2026_paper.html) · [저자 project/code](https://robo-dopamine.github.io/) · [공식 code](https://github.com/FlagOpen/Robo-Dopamine). 그 밖의 표와 부록의 실패 사례는 추가 확인이 필요하다.
