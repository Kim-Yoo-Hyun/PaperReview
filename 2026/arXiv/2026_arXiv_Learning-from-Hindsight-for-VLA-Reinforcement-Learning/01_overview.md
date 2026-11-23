# Learning from Hindsight for VLA Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
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
- Source audit: 2026-11-07: 공식 metadata/abstract·저자 project/README 확인. arXiv v2(2026-10-05) 제목·저자·abstract 기준. Project는 과거 제목과 Code placeholder를 유지한다. Main-conference 채택/실행 code는 미확인. Dossier의 지정 본문 검토를 이 5개 노트의 전체 정독으로 승격하지 않는다. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

LfH는 VLA가 원래 지시를 달성하지 못한 실행에서도 실제 이룬 보조 목표를 찾아 강화학습 신호로 활용한다. [PDF 1쪽](https://arxiv.org/pdf/2607.09042v2#page=1)

## Core Idea and Contribution

- 사전학습 시각언어 모델이 실패 궤적을 달성한 행동으로 다시 기술하고 정책을 원래 과제와 재명명한 보조 과제에 함께 학습시킨다. [PDF 4쪽](https://arxiv.org/pdf/2607.09042v2#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2607.09042v2#page=5)
- 실제 Franka FR3에서 녹색 용기를 그릇에 넣는 과제를 160회 훈련한 뒤 성공률은 재명명을 적용한 GRPO가 56%, 기준 GRPO가 22%였다. [PDF 8쪽](https://arxiv.org/pdf/2607.09042v2#page=8)

## Observation–State–Action Interface

관측·원 지시 → VLA 행동; 수집 후 rollout을 VLM이 해석하여 보조 목표와 학습 신호를 만든다. 배포 제어기와 학습 relabeler를 구분한다.

## Evaluation Scope and Claim Boundary

v2 abstract는 LIBERO-PRO의 분포 이동 조작과 실제 Franka 학습을 보고한다. 샘플 효율 개선은 해당 비교 조건의 저자 주장이다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2607.09042) · [저자 project/code](https://iamxjy.github.io/lfh-website/). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

실패 재사용 자체가 새 기여가 아님을 보여 주는 HINDSIGHT의 가장 가까운 선행. 참인 보조 목표들 사이의 원 과제 전이를 연구하려면 먼저 비교해야 한다.

## Verification Boundary

v2의 importance correction·label filtering·모방 대조와 우리 selector의 정확한 차이, VLM 감독 비용과 rollout 분모, 원 지시 평가 독립성을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
