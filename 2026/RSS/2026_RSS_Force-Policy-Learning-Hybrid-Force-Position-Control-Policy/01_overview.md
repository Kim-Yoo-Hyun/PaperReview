# Force Policy: Learning Hybrid Force-Position Control Policy under Interaction Frame for Contact-Rich Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Hongjie Fang, Shirun Tang, Mingyu Mei, Haoxiang Qin, Zihao He, Jingjing Chen, Feng Ying, Chenxi Wang, Wanxi Liu, Zaixing He, Cewu Lu, Shiquan Wang
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: force-control, contact, hybrid-control, interaction-frame
- Aliases: Force Policy
- Official paper: https://roboticsproceedings.org/rss22/p128.html
- Venue verification: https://roboticsproceedings.org/rss22/p128.html
- Code/Project: https://force-policy.github.io/
- Code: https://github.com/force-policy/ForcePolicy
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인. Force Policy 원 논문만 등록하며 FP2 후속 extension의 평가를 합치지 않는다. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

Force Policy는 접촉 중 힘을 조절할 방향과 위치를 제어할 방향을 나누는 좌표계를 시연에서 복원해 접촉 조작에 사용한다. [PDF 1쪽](https://roboticsproceedings.org/rss22/p128.pdf#page=1)

## Core Idea and Contribution

- 비접촉 구간의 움직임은 전역 시각 정책이 정하고 접촉 중에는 고주파 힘 피드백을 쓰는 국소 정책이 좌표계를 추정해 힘·위치를 함께 제어한다. [PDF 3쪽](https://roboticsproceedings.org/rss22/p128.pdf#page=3) · [PDF 4쪽](https://roboticsproceedings.org/rss22/p128.pdf#page=4) · [PDF 5쪽](https://roboticsproceedings.org/rss22/p128.pdf#page=5)
- 실제 로봇의 접촉 과제에서 물체 형상과 물성이 달라질 때 작업 성공뿐 아니라 목표 힘의 추종 정도와 접촉 안정성도 평가했다. [PDF 6쪽](https://roboticsproceedings.org/rss22/p128.pdf#page=6) · [PDF 7쪽](https://roboticsproceedings.org/rss22/p128.pdf#page=7) · [PDF 8쪽](https://roboticsproceedings.org/rss22/p128.pdf#page=8)

## Observation–State–Action Interface

vision으로 접근하고 접촉 시 힘 피드백·interaction frame으로 제어한다.

## Evaluation Scope and Claim Boundary

실제 contact-rich 조작과 새로운 형상·물성 객체를 평가한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p128.html) · [저자 project/code](https://force-policy.github.io/) · [공식 code](https://github.com/force-policy/ForcePolicy). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Unified VLA의 접촉 기여가 분리된 고주파 힘 제어보다 나은지 판단할 비교 기준이다.

## Verification Boundary

frame label 생성과 수동 조정, 접촉 전환 조건, 정책·controller 주기을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
