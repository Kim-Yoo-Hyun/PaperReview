# When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Yu Fang, Yuchun Feng, Dong Jing, Jiaqi Liu, Yue Yang, Zhenyu Wei, Daniel Szafir, Mingyu Ding
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, Benchmark, language-grounding, counterfactual
- Aliases: LIBERO-CF, CAG
- Official paper: https://arxiv.org/abs/2602.17659
- Venue verification: https://www.corl.org/program/accepted-papers
- Code/Project: https://vla-cf.github.io/
- Code: https://github.com/yuffish/VLA-CF
- Source audit: 2026-11-12: 공식 abstract/metadata·명시한 project 확인. 최신 v3 abstract 확인. 저자/arXiv는 CoRL 2026 Spotlight를 표기하지만 이번 공식 proceedings/forum 검색으로 확인하지 못해 arXiv로 등록한다. GitHub 공개는 native 재현 성공이 아니다. 새 5-note는 초록 수준이며 과거 N1/N2의 지정 본문/source 검토는 work/sources/vla_masters_gap_scout_2026-11-12.json을 따른다. 사용자 정독·코드 재현을 뜻하지 않는다.

## Problem and Importance

장면의 학습 편향 때문에 VLA가 다른 유효한 언어 지시보다 익숙한 행동을 반복한다.

## Core Idea and Contribution

LIBERO-CF로 반사실적 지시 수행을 평가하고 언어 조건부·비조건부 분기의 차이로 행동을 유도한다.

## Observation–State–Action Interface

같은 LIBERO 장면의 대체 지시 → VLA/VA 분기 → 조작 행동.

## Evaluation Scope and Claim Boundary

LIBERO-CF와 실제 로봇에서 언어 grounding과 task success를 구별해 평가한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2602.17659) · [저자 project/code](https://vla-cf.github.io/) · [공식 code](https://github.com/yuffish/VLA-CF). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

LANGRET의 공개 장면·지시쌍·평가기 source이며 기존 counterfactual benchmark와의 중복을 드러낸다.

## Verification Boundary

본문에서 확인할 항목: focused suite의 장면 변경·OR/target-only 종료·두 목표의 기본 능력·guidance 비용. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
