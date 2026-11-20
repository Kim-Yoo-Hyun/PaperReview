# Learning from Hindsight for VLA Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Iris Xu, Sunshine Jiang, John Marangola, Pulkit Agrawal, Zhang-Wei Hong
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, hindsight-relabeling, online-RL, sample-efficiency
- Aliases: LfH, Learning More from Less: Reinforcement Learning from Hindsight
- Official paper: https://arxiv.org/abs/2607.09042
- Venue verification: https://arxiv.org/abs/2607.09042
- Code/Project: https://iamxjy.github.io/lfh-website/
- Code: project_only
- Source audit: 2026-11-07: 공식 metadata/abstract·저자 project/README 확인. arXiv v2(2026-10-05) 제목·저자·abstract 기준. Project는 과거 제목과 Code placeholder를 유지한다. Main-conference 채택/실행 code는 미확인. Dossier의 지정 본문 검토를 이 5개 노트의 전체 정독으로 승격하지 않는다. 사용자 reading status UNREAD 유지.

## Problem and Importance

원 지시 실패에만 보상 0을 주면 실제 수행한 유용한 행동도 VLA 강화학습에 활용하지 못한다.

## Core Idea and Contribution

VLM으로 실패에서 달성한 행동을 보조 언어 목표로 붙이고 원 과제와 함께 정책을 학습한다.

## Observation–State–Action Interface

관측·원 지시 → VLA 행동; 수집 후 rollout을 VLM이 해석하여 보조 목표와 학습 신호를 만든다. 배포 제어기와 학습 relabeler를 구분한다.

## Evaluation Scope and Claim Boundary

v2 abstract는 LIBERO-PRO의 분포 이동 조작과 실제 Franka 학습을 보고한다. 샘플 효율 개선은 해당 비교 조건의 저자 주장이다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2607.09042) · [저자 project/code](https://iamxjy.github.io/lfh-website/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

실패 재사용 자체가 새 기여가 아님을 보여 주는 HINDSIGHT의 가장 가까운 선행. 참인 보조 목표들 사이의 원 과제 전이를 연구하려면 먼저 비교해야 한다.

## Verification Boundary

v2의 importance correction·label filtering·모방 대조와 우리 selector의 정확한 차이, VLM 감독 비용과 rollout 분모, 원 지시 평가 독립성을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
