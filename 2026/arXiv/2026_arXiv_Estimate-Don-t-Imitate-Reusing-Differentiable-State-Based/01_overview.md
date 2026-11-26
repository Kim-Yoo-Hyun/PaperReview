# Estimate, Don't Imitate: Reusing Differentiable State-Based Policies for Visuomotor Control

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Denis Shcherba, Adrian Abel, Eckart Cobo-Briesewitz, Paul Mattes, Wojciech Samek, Marc Toussaint
- Category: Robotics-Enabling 3D Perception
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: state estimation, visuomotor control, policy reuse, manipulation
- Aliases: EDI, Estimate, Don't Imitate
- Official paper: https://arxiv.org/abs/2609.34018
- Venue verification: https://arxiv.org/abs/2609.34018
- Code/Project: not identified
- Code: not_identified
- 방법·평가 확인 (2026-11-25): [원문 3, 4, 5, 6, 7, 8쪽](https://arxiv.org/pdf/2609.34018v1#page=3) · [다축 분류와 공개 범위](../../../work/sources/batches/core_next_10.yaml)
- Source audit: 2026-11-18: arXiv 초록·공식 publication/project를 확인한 등록. Abstract 기반 — 본문 수동 확인 필요. 연구 dossier의 지정 절 검토와 paper별 5-note의 evidence를 구별하며 사용자 읽기 상태는 변경하지 않음. 저자 dataset card의 ICRA2026 표기는 공식 proceedings 확인이 없어 채택하지 않음. 연결된 HHI-Robot-Learning/26-DistillingSGRL은 404이며 미공개 이유를 추정하지 않음. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 시각 정책이 전문가 행동을 다시 배우는 대신 영상에서 필요한 상태를 복원하고 고정된 상태 기반 전문가가 행동을 결정하도록 한다. [PDF 1쪽](https://arxiv.org/pdf/2609.34018v1#page=1)

## Core Idea and Contribution

- 직접 상태 감독으로 시작해 미분 가능한 전문가를 통해 역전파한 행동 일치 손실의 비중을 늘림으로써 제어에 영향을 주는 추정 오차를 줄인다. [PDF 3쪽](https://arxiv.org/pdf/2609.34018v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2609.34018v1#page=4)
- 실제 Panda의 큐브 과제에서 성공률은 완료한 에피소드 기준 19/25(76.0%), 관절 한계로 중단하고 재시작한 두 시도를 포함하면 19/27(70.4%)였다. [PDF 7쪽](https://arxiv.org/pdf/2609.34018v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2609.34018v1#page=8)

## Observation–State–Action Interface

영상 → 추정된 물리 상태 → 고정 expert → 로봇 행동. 추정기만 학습하며 VLA나 언어 조건 정책을 전제로 한 방법은 아니다.

## Evaluation Scope and Claim Boundary

초록은 goal-conditioned 조작 5개와 실제 Panda의 sim-to-real 평가를 보고한다. Trial 구성·각 조건별 성공 수·시연 분할은 이번 등록에서 확인하지 않았다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.34018). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

현재 geometry 후보의 action-consistency 대조를 정하는 직접 NEXT다. 행동에 중요한 추정 오차를 학습한다는 원리를 신규성에서 제외하게 한다.

## Verification Boundary

Expert의 미분 가능성·state/goal 정의·loss schedule·occlusion·held-out split·실제 로봇 trial 및 코드 release를 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
