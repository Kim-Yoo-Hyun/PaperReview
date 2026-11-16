# Causeway: Restoring Task Accessibility for Instruction Switching in VLA Policies

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, VLA, instruction-switching, recovery
- Aliases: Causeway
- Official paper: https://arxiv.org/abs/2609.30913
- Venue verification: https://arxiv.org/abs/2609.30913
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-31 공식 서지/abstract·공개 project/code 소개를 재확인했다. 신규 노트는 abstract 기반이며 기존 연구 검토의 지정 본문/code 확인은 work/sources/instruction_revision_review_2026-10-31.json 및 pre_gpu_buildup_review_2026-10-31.json의 별도 범위다. 사용자 정독·native 실행을 뜻하지 않는다.

## Problem and Importance

앞선 작업이 바꾼 물리 상태 때문에 새 목표 작업의 기존 능력에 접근하지 못할 수 있다.

## Core Idea and Contribution

목표 작업의 re-entry pose를 조건으로 frozen decoder를 통한 gradient를 이용해 action-stream 표현을 수정하고, 정책 자체가 복귀 행동을 생성하는 inference-time 개입을 제안한다.

## Observation–State–Action Interface

현재 상태·새 목표·re-entry pose → 동결 VLA 내부 표현 개입 → 복귀 행동과 목표 작업 실행. 재진술만 사용하는 언어 조건과 정보·개입 위치가 다르다.

## Evaluation Scope and Claim Boundary

LIBERO-Goal, LIBERO-Object와 실제 xArm에서 instruction switching과 복구를 보고한다. 정확한 비교 수치·시행 수·특권 정보 조건은 신규 노트에서 본문 정독 완료로 표시하지 않는다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.30913). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

전환 실패를 의미 기억 오류로 오인하지 않기 위한 직접 경쟁 설명이다. 새 목표의 물리적 실행 가능성과 언어 해석을 분리할 NEXT로 추가하며 preprint status를 유지한다.

## Verification Boundary

re-entry pose 획득과 관측 접근, decoder별 개입 위치·계산 비용, 복귀/인계 조건, 실제 로봇 평가 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
