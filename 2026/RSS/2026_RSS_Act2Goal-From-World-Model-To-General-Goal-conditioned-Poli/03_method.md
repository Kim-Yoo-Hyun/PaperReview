# Act2Goal: From World Model To General Goal-conditioned Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Method and Contribution

목표 조건부 world model의 미래 영상과 multi-scale temporal hashing을 action expert에 연결하고 hindsight goal relabeling으로 적응한다.

## Observation, State, and Action

현재 영상·목표 영상 → imagined frames의 가까운/먼 시간 표현 → motor action.

## Objective and Training / Inference Boundary

초록에서 확인한 학습 구성이다. 정확한 loss·gradient 경로·학습/추론 차이·controller 또는 memory 시간 단위는 본문 확인이 필요하다.

점검 항목: 시각 목표 접근·hindsight 도달 상태·LoRA 갱신 범위·online 비용.

## Method-Specific Comparison — Researcher Interpretation

동일 rollout에서 원 목표·hindsight 목표·성공 subset 모방을 같은 update 수로 비교한다.

이 비교는 제안이며 실행 결과나 논문의 ablation이 아니다.

## Evidence Boundary

[공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p015.html). RSS 공식 abstract를 기준으로 기록. Project는 접근되지만 이번 웹 도구에서 본문을 읽지 못해 코드 공개 상태는 not identified다. Visual-goal 정책을 언어 지시 VLA와 동일시하지 않는다.
