# ActMem-VLA: Action-History Memory with Dual-Expert Denoising for Long-Horizon Vision-Language-Action Policies

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, memory, action-history, long-horizon
- Aliases: ActMem-VLA
- Official paper: https://arxiv.org/abs/2609.37307
- Venue verification: https://arxiv.org/abs/2609.37307
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-12: 공식 abstract/metadata·명시한 project 확인. v2 abstract 확인. 공식 채택·공식 code/project URL 미확인. 행동 이력은 물리적 과제 완료의 증거가 아니다. 새 5-note는 초록 수준이며 과거 N1/N2의 지정 본문/source 검토는 work/sources/vla_masters_gap_scout_2026-11-12.json을 따른다. 사용자 정독·코드 재현을 뜻하지 않는다.

## Problem and Importance

현재 관측이 비슷한 서로 다른 작업 단계에서 행동이 모호해지는 문제를 다룬다.

## Core Idea and Contribution

Mamba 행동 이력 memory와 PreAction Expert를 학습하고 frozen action expert에 denoising을 넘긴다.

## Observation–State–Action Interface

실행 행동 이력·현재 맥락 → memory/PAE → frozen AE의 행동 refinement.

## Evaluation Scope and Claim Boundary

LIBERO-Mem과 네 실제 조작 과제에서 memory 및 기존 VLA와 비교한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.37307). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

행동 이력 memory의 강한 비교 자료이며 결과 기반 기억이라는 질문의 기존 대안을 구체화한다.

## Verification Boundary

본문에서 확인할 항목: memory reset·실제 실행 이력의 정의·효과 피드백 접근권·분할과 예산. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
