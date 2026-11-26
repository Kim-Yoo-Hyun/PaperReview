# RePlan-Bot: Multi-Level Replanning for Embodied Instruction Following

> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 쪽수를 붙인 문장을 원문과 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CVPR-Workshop
- Authors: Xicheng Gong, Guozheng Sun, Peiran Xu, Yadong Mu
- Category: Planning and Long-Horizon Reasoning
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: Planning, language, execution, embodied navigation
- Aliases:
- Official paper: https://openaccess.thecvf.com/content/CVPR2026W/GRAIL-V/html/Gong_RePlan-Bot_Multi-Level_Replanning_for_Embodied_Instruction_Following_CVPRW_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026W/GRAIL-V/papers/Gong_RePlan-Bot_Multi-Level_Replanning_for_Embodied_Instruction_Following_CVPRW_2026_paper.pdf
- Venue verification: https://openaccess.thecvf.com/content/CVPR2026W/GRAIL-V/html/Gong_RePlan-Bot_Multi-Level_Replanning_for_Embodied_Instruction_Following_CVPRW_2026_paper.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-24에 한 줄 요약과 핵심 기여 두 개를 아래 PDF 쪽수에 대조했다.

## Problem and Importance

RePlan-Bot은 자연어 지시를 수행하면서 관측을 바탕으로 다음 하위목표와 당장 실행할 저수준 행동을 각각 수정한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026W/GRAIL-V/papers/Gong_RePlan-Bot_Multi-Level_Replanning_for_Embodied_Instruction_Following_CVPRW_2026_paper.pdf#page=1)

## Core Idea and Contribution

- 언어모형이 진행 상황을 점검하고 다층 물체 지도로 대상을 찾으며 시각 트랜스포머가 위험한 저수준 행동을 사전에 교정한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026W/GRAIL-V/papers/Gong_RePlan-Bot_Multi-Level_Replanning_for_Embodied_Instruction_Following_CVPRW_2026_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026W/GRAIL-V/papers/Gong_RePlan-Bot_Multi-Level_Replanning_for_Embodied_Instruction_Following_CVPRW_2026_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026W/GRAIL-V/papers/Gong_RePlan-Bot_Multi-Level_Replanning_for_Embodied_Instruction_Following_CVPRW_2026_paper.pdf#page=5)
- ALFRED의 본 환경과 보지 못한 환경을 나눠 성공률을 비교하고 각 수준의 재계획이 실패에 미치는 영향을 분석했다. [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2026W/GRAIL-V/papers/Gong_RePlan-Bot_Multi-Level_Replanning_for_Embodied_Instruction_Following_CVPRW_2026_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2026W/GRAIL-V/papers/Gong_RePlan-Bot_Multi-Level_Replanning_for_Embodied_Instruction_Following_CVPRW_2026_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026W/GRAIL-V/papers/Gong_RePlan-Bot_Multi-Level_Replanning_for_Embodied_Instruction_Following_CVPRW_2026_paper.pdf#page=8)

## Observation–State–Action Interface

지시·환경 관측 → subgoal/map 판단 → 행동 보정.

## Evaluation Scope and Claim Boundary

ALFRED instruction following 평가를 보고한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026W/GRAIL-V/html/Gong_RePlan-Bot_Multi-Level_Replanning_for_Embodied_Instruction_Following_CVPRW_2026_paper.html). 추가 수치와 실패 조건은 해당 실험의 표·설정을 확인해야 한다.

## 검색 태그 근거

ALFRED에서 LLM이 하위 목표를 감사하고, RGB에서 추정한 깊이와 인스턴스 마스크로 3차원 지도를 만든다. 중간 단계의 탐색과 하위 행동 보정을 따로 평가한다. 깊이는 추정한 중간 표현이다. [원문 4쪽](https://openaccess.thecvf.com/content/CVPR2026W/GRAIL-V/papers/Gong_RePlan-Bot_Multi-Level_Replanning_for_Embodied_Instruction_Following_CVPRW_2026_paper.pdf#page=4) · [원문 6쪽](https://openaccess.thecvf.com/content/CVPR2026W/GRAIL-V/papers/Gong_RePlan-Bot_Multi-Level_Replanning_for_Embodied_Instruction_Following_CVPRW_2026_paper.pdf#page=6)

## Why This Paper Is Here — Researcher Interpretation

D3의 multi-level replanning이 이미 존재하는 workshop 비교군이다.

## Verification Boundary

ALFRED predicate, oracle map 접근, action executor, VLA와의 차이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
