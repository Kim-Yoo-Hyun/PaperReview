# ReViP: Mitigating False Completion in Vision-Language-Action Models with Vision-Proprioception Rebalance

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Zhuohao Li, Yinghao Li, Jian-Jian Jiang, Lang Zhou, Tianyu Zhang, Jiadong Yin, Mu Lin, Yi-Lin Wei, Wei-Shi Zheng
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, proprioception, robustness
- Aliases: ReViP: Reducing False Completion in Vision-Language-Action Models with Vision–Proprioception Rebalance
- Official paper: https://arxiv.org/abs/2601.16667
- Venue verification: https://arxiv.org/abs/2601.16667
- Code/Project: https://isee-laboratory.github.io/ReViP/
- Code: not_released
- Source audit: 2026-10-21: official abstract / author project 확인. 5개 note는 abstract 기반이며 사용자 정독을 의미하지 않는다. 최신 arXiv v3 title과 project 확인; 이전 Reducing title은 alias로 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

ReViP는 조작이 눈앞에서 실패했는데도 자신의 관절 상태만 보고 작업이 끝났다고 행동하는 VLA의 오류를 다룬다. [PDF 1쪽](https://arxiv.org/pdf/2601.16667v3#page=1)

## Core Idea and Contribution

- 현재 영상에서 작업 단계를 추정하는 관찰기를 두고, 추정 결과로 시각과 고유수용감각 특징의 결합을 조절한다. [PDF 3쪽](https://arxiv.org/pdf/2601.16667v3#page=3) · [PDF 7쪽](https://arxiv.org/pdf/2601.16667v3#page=7)
- 물체 낙하·방해물 교체·재배치가 있는 여덟 과제에서 잘못된 완료와 성공을 평가하고 실물 조작으로도 검증했다. [PDF 1쪽](https://arxiv.org/pdf/2601.16667v3#page=1) · [PDF 7쪽](https://arxiv.org/pdf/2601.16667v3#page=7)

## Observation–State–Action Interface

영상·언어·state와 stage cue → corrective action.

## Evaluation Scope and Claim Boundary

Object Drop, Distractor Swap, Relayout 및 robot manipulation 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2601.16667) · [저자 project/code](https://isee-laboratory.github.io/ReViP/). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

D1에서 단순 vision 강화나 stage feedback을 새 기여로 재주장하지 않게 하는 NEXT다.

## Verification Boundary

arXiv v3와 최신 project 방법 차이, observer latency, 공개 코드을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
