# RePlan-Bot: Multi-Level Replanning for Embodied Instruction Following

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CVPR-Workshop
- Authors: Xicheng Gong, Guozheng Sun, Peiran Xu, Yadong Mu
- Category: Planning and Long-Horizon Reasoning
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: Planning, language, execution
- Aliases:
- Official paper: https://openaccess.thecvf.com/content/CVPR2026W/GRAIL-V/html/Gong_RePlan-Bot_Multi-Level_Replanning_for_Embodied_Instruction_Following_CVPRW_2026_paper.html
- Venue verification: https://openaccess.thecvf.com/content/CVPR2026W/GRAIL-V/html/Gong_RePlan-Bot_Multi-Level_Replanning_for_Embodied_Instruction_Following_CVPRW_2026_paper.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

Embodied instruction 실행 중 여러 수준의 계획 실패를 수정한다.

## Core Idea and Contribution

고수준 계획 감사와 탐색·저수준 보정을 연결한다.

## Observation–State–Action Interface

지시·환경 관측 → subgoal/map 판단 → 행동 보정.

## Evaluation Scope and Claim Boundary

ALFRED instruction following 평가를 보고한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026W/GRAIL-V/html/Gong_RePlan-Bot_Multi-Level_Replanning_for_Embodied_Instruction_Following_CVPRW_2026_paper.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

D3의 multi-level replanning이 이미 존재하는 workshop 비교군이다.

## Verification Boundary

ALFRED predicate, oracle map 접근, action executor, VLA와의 차이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
