# Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICLR
- Authors: Asher Hancock, Xindi Wu, Lihan Zha, Olga Russakovsky, Anirudha Majumdar
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, action-interface, cross-embodiment
- Aliases: VLM2VLA
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/7a0f8055c838df8e62329a76c7c6403d-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2026/hash/7a0f8055c838df8e62329a76c7c6403d-Abstract-Conference.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

Robot action 학습 중 VLM의 일반 의미 능력 손실을 줄인다.

## Core Idea and Contribution

자연어로 low-level action을 표현하고 parameter-efficient adaptation을 사용한다.

## Observation–State–Action Interface

영상·언어 → 언어형 action 표현 → robot 명령.

## Evaluation Scope and Claim Boundary

Robot manipulation과 VQA 능력 보존을 함께 보고한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/7a0f8055c838df8e62329a76c7c6403d-Abstract-Conference.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

의미 능력 보존이라는 넓은 방향의 직접 선행이며 action interface 비교에도 필요하다.

## Verification Boundary

action decoding, LoRA 범위, VQA/robot split과 robot controller을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
