# Act2Goal: From World Model To General Goal-conditioned Policy

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Pengfei Zhou, Liliang Chen, Shengcong Chen, Di Chen, Wenzhi Zhao, Rongjun Jin, Guanghui Ren, Jianlan Luo
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: goal-conditioning, world-model, manipulation, hindsight
- Aliases: Act2Goal
- Official paper: https://www.roboticsproceedings.org/rss22/p015.html
- Venue verification: https://www.roboticsproceedings.org/rss22/p015.html
- Code/Project: https://act2goal.github.io/
- Code: not_identified
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. RSS 공식 abstract를 기준으로 기록. Project는 접근되지만 이번 웹 도구에서 본문을 읽지 못해 코드 공개 상태는 not identified다. Visual-goal 정책을 언어 지시 VLA와 동일시하지 않는다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

Act2Goal은 현재 영상과 목표 영상 사이의 중간 장면을 예측해 긴 조작 과제에서도 국소적인 행동을 수정할 수 있게 한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss22/p015.pdf#page=1)

## Core Idea and Contribution

- 예측한 영상 중 가까운 미래는 촘촘히, 먼 미래는 드물게 선택해 정밀 제어와 장기 목표 유지에 필요한 정보를 함께 정책에 전달한다. [PDF 3쪽](https://www.roboticsproceedings.org/rss22/p015.pdf#page=3) · [PDF 4쪽](https://www.roboticsproceedings.org/rss22/p015.pdf#page=4)
- 실제 배포에서 로봇이 달성한 결과로 목표를 다시 붙이고 LoRA로 정책을 갱신해 외부 보상 없이 낯선 조작 조건에 적응하는지를 검증했다. [PDF 5쪽](https://www.roboticsproceedings.org/rss22/p015.pdf#page=5) · [PDF 7쪽](https://www.roboticsproceedings.org/rss22/p015.pdf#page=7) · [PDF 8쪽](https://www.roboticsproceedings.org/rss22/p015.pdf#page=8)

## Observation–State–Action Interface

현재 영상·목표 영상 → imagined frames의 가까운/먼 시간 표현 → motor action.

## Evaluation Scope and Claim Boundary

시뮬레이션·실물 장시간 조작과 보상 없는 online 적응을 보고한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p015.html) · [저자 project/code](https://act2goal.github.io/). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Hindsight 목표 변경·world model·단일 정책 연결의 직접 선행이며 언어 VLA와 시각 목표 정책의 경계를 드러낸다.

## Verification Boundary

본문에서 확인할 항목: 시각 목표 접근·hindsight 도달 상태·LoRA 갱신 범위·online 비용. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
