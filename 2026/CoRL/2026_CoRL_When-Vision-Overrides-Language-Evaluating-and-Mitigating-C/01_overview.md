# When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CoRL
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
- Source audit: 2026-11-12: 공식 abstract/metadata·명시한 project 확인. 최신 v3 abstract 확인. 저자/arXiv는 CoRL 2026 Spotlight를 표기하지만 이번 공식 proceedings/forum 검색으로 확인하지 못해 arXiv로 등록한다. GitHub 공개는 native 재현 성공이 아니다. 새 5-note는 초록 수준이며 과거 N1/N2의 지정 본문/source 검토는 work/sources/vla_masters_gap_scout_2026-11-12.json을 따른다. 사용자 정독·코드 재현을 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

LIBERO-CF는 같은 장면에서 실행 가능한 지시만 바꿔 VLA가 시각적으로 익숙한 동작과 현재 지시 중 어느 쪽을 따르는지 평가한다. [PDF 1쪽](https://arxiv.org/pdf/2602.17659v3#page=1)

## Core Idea and Contribution

- 동일한 물체 배치에 다른 목표를 지정하고 지시된 대상을 선택했는지와 실제 과제를 마쳤는지를 나누어 측정한다. [PDF 3쪽](https://arxiv.org/pdf/2602.17659v3#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2602.17659v3#page=4)
- 언어를 제공한 분기와 제공하지 않은 분기의 행동 예측 차이를 증폭하는 CAG를 제안하고, LIBERO-CF와 실물에서 언어 대응과 성공률을 비교했다. [PDF 5쪽](https://arxiv.org/pdf/2602.17659v3#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2602.17659v3#page=6) · [PDF 8쪽](https://arxiv.org/pdf/2602.17659v3#page=8)

## Observation–State–Action Interface

같은 LIBERO 장면의 대체 지시 → VLA/VA 분기 → 조작 행동.

## Evaluation Scope and Claim Boundary

LIBERO-CF와 실제 로봇에서 언어 grounding과 task success를 구별해 평가한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2602.17659) · [저자 project/code](https://vla-cf.github.io/) · [공식 code](https://github.com/yuffish/VLA-CF). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

LANGRET의 공개 장면·지시쌍·평가기 source이며 기존 counterfactual benchmark와의 중복을 드러낸다.

## Verification Boundary

본문에서 확인할 항목: focused suite의 장면 변경·OR/target-only 종료·두 목표의 기본 능력·guidance 비용. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
