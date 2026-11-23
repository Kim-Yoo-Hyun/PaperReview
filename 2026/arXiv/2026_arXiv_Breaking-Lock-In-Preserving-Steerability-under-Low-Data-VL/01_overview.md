# Breaking Lock-In: Preserving Steerability under Low-Data VLA Post-Training

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
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
- Source audit: 2026-11-12: 공식 abstract/metadata·명시한 project 확인. v1 abstract와 저자 project 확인. Code Coming Soon; 공식 채택 미확인. 이전 지정 본문 검토는 별도 원장에 보존한다. 새 5-note는 초록 수준이며 과거 N1/N2의 지정 본문/source 검토는 work/sources/vla_masters_gap_scout_2026-11-12.json을 따른다. 사용자 정독·코드 재현을 뜻하지 않는다.

## Problem and Importance

소량 시연 SFT 뒤 VLA가 학습 물체·공간에 고착되어 새로운 지시를 따르지 못한다.

## Core Idea and Contribution

후학습 중 시각 grounding을 보존하고 추론 시 contrastive prompt guidance로 denoising을 조절한다.

## Observation–State–Action Interface

영상·언어 → 시각 grounding을 보존한 VLA → 지시 조건부 동작.

## Evaluation Scope and Claim Boundary

Simulation과 실제 로봇의 여덟 평가에서 새로운 지시에 대한 일반화를 비교한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2604.23121) · [저자 project/code](https://suninghuang19.github.io/delock_page/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

단순히 지시 보존·semantic freezing을 도입하는 것을 새 연구 기여로 주장하지 않도록 한다.

## Verification Boundary

본문에서 확인할 항목: 시각 보존 손실·guidance 입력·새 지시 split·RL과 SFT의 데이터/비용 차이. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
