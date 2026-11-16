# Force Policy: Learning Hybrid Force-Position Control Policy under Interaction Frame for Contact-Rich Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: force-control, contact, hybrid-control, interaction-frame
- Aliases: Force Policy
- Official paper: https://roboticsproceedings.org/rss22/p128.html
- Venue verification: https://roboticsproceedings.org/rss22/p128.html
- Code/Project: https://force-policy.github.io/
- Code: https://github.com/force-policy/ForcePolicy
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인. Force Policy 원 논문만 등록하며 FP2 후속 extension의 평가를 합치지 않는다. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

전역 시각 행동 결정과 접촉 안정화에는 서로 다른 피드백과 시간척도가 필요하다.

## Core Idea and Contribution

시연에서 interaction frame을 복원해 전역 시각 정책과 국소 hybrid force-position 제어를 구성한다.

## Observation–State–Action Interface

vision으로 접근하고 접촉 시 힘 피드백·interaction frame으로 제어한다.

## Evaluation Scope and Claim Boundary

실제 contact-rich 조작과 새로운 형상·물성 객체를 평가한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p128.html) · [저자 project/code](https://force-policy.github.io/) · [공식 code](https://github.com/force-policy/ForcePolicy). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Unified VLA의 접촉 기여가 분리된 고주파 힘 제어보다 나은지 판단할 비교 기준이다.

## Verification Boundary

frame label 생성과 수동 조정, 접촉 전환 조건, 정책·controller 주기을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
