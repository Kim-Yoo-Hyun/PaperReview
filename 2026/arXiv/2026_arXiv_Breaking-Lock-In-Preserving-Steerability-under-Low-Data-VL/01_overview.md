# Breaking Lock-In: Preserving Steerability under Low-Data VLA Post-Training

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Suning Huang, Jiaqi Shao, Ke Wang, Qianzhong Chen, Jiankai Sun, Yanjiang Guo, Mac Schwager, Jeannette Bohg
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, fine-tuning, language-grounding, generalization
- Aliases: DeLock
- Official paper: https://arxiv.org/abs/2604.23121
- Venue verification: https://arxiv.org/abs/2604.23121
- Code/Project: https://suninghuang19.github.io/delock_page/
- Code: not_released
- Source audit: 2026-11-12: 공식 abstract/metadata·명시한 project 확인. v1 abstract와 저자 project 확인. Code Coming Soon; 공식 채택 미확인. 이전 지정 본문 검토는 별도 원장에 보존한다. 새 5-note는 초록 수준이며 과거 N1/N2의 지정 본문/source 검토는 work/sources/vla_masters_gap_scout_2026-11-12.json을 따른다. 사용자 정독·코드 재현을 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

DeLock은 적은 시연으로 후학습한 VLA가 훈련에 나오던 물체나 위치에 고착돼 새로운 지시를 따르기 어려워지는 현상을 다룬다. [PDF 1쪽](https://arxiv.org/pdf/2604.23121v1#page=1)

## Core Idea and Contribution

- 미세조정 중 시각 표현의 대응 관계를 보존하고 실행할 때 서로 다른 프롬프트를 대조해 행동 생성의 잡음 제거 방향을 조절한다. [PDF 3쪽](https://arxiv.org/pdf/2604.23121v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2604.23121v1#page=4)
- 익숙하지 않은 개념과 공간 목표를 분리한 시뮬레이션 및 실물 평가에서 후학습 전후의 지시 반응과 각 보정 요소의 기여를 비교했다. [PDF 6쪽](https://arxiv.org/pdf/2604.23121v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2604.23121v1#page=7)

## Observation–State–Action Interface

영상·언어 → 시각 grounding을 보존한 VLA → 지시 조건부 동작.

## Evaluation Scope and Claim Boundary

Simulation과 실제 로봇의 여덟 평가에서 새로운 지시에 대한 일반화를 비교한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2604.23121) · [저자 project/code](https://suninghuang19.github.io/delock_page/). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

단순히 지시 보존·semantic freezing을 도입하는 것을 새 연구 기여로 주장하지 않도록 한다.

## Verification Boundary

본문에서 확인할 항목: 시각 보존 손실·guidance 입력·새 지시 split·RL과 SFT의 데이터/비용 차이. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
