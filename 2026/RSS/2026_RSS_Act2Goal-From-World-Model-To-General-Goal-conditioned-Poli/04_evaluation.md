# Act2Goal: From World Model To General Goal-conditioned Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Source-Supported Evaluation Scope

시뮬레이션·실물 장시간 조작과 보상 없는 online 적응을 보고한다.

## Metrics, Baselines, and Generalization

시각 목표 접근·hindsight 도달 상태·LoRA 갱신 범위·online 비용.

정확한 dataset/split·trial 수·baseline budget·metric 정의·ablation 수치는 이번 초록 정리에서 확정하지 않았다. 이는 원문에 미보고됐다는 뜻이 아니다.

## Reproducibility and Limitations

RSS 공식 abstract를 기준으로 기록. Project는 접근되지만 이번 웹 도구에서 본문을 읽지 못해 코드 공개 상태는 not identified다. Visual-goal 정책을 언어 지시 VLA와 동일시하지 않는다.

공개 code/project가 있어도 실행 재현을 뜻하지 않는다. 실제 로봇·simulation·이론/survey의 범위를 위 평가 설명대로 구별한다.

## Proposed Comparison — Researcher Interpretation

동일 rollout에서 원 목표·hindsight 목표·성공 subset 모방을 같은 update 수로 비교한다.

아직 실행하지 않았으며 예상 이득을 측정 결과로 기록하지 않는다.

## Evidence

[공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p015.html). Code/project·확인 날짜는 [overview](./01_overview.md)를 따른다.
