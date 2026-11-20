# TidyBot++: An Open-Source Holonomic Mobile Manipulator for Robot Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Jimmy Wu, William Chong, Robert Holmberg, Aaditya Prasad, Yihuai Gao, Oussama Khatib, Shuran Song, Szymon Rusinkiewicz, Jeannette Bohg
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, mobile manipulation, teleoperation, holonomic-base
- Aliases: TidyBot++, TidyBot2
- Official paper: https://proceedings.mlr.press/v270/wu25a.html
- Venue verification: https://proceedings.mlr.press/v270/wu25a.html
- Conference edition: 2024 · https://proceedings.mlr.press/v270/
- Code/Project: https://github.com/jimmyyhwu/tidybot2
- Code: https://github.com/jimmyyhwu/tidybot2
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다. CoRL 개최 2024, PMLR 출판 2025.

## Problem and Importance

가정용 mobile manipulation 시연을 수집할 유연하고 재사용 가능한 플랫폼이 필요하다.

## Core Idea and Contribution

Holonomic base와 휴대전화 teleoperation을 결합한 공개 mobile manipulator를 설계한다.

## Observation–State–Action Interface

사람 teleoperation → base/arm demonstration → mobile manipulation policy.

## Evaluation Scope and Claim Boundary

실로봇 가정 과제에서 수집한 시연으로 학습한 정책을 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/wu25a.html) · [저자 project/code](https://github.com/jimmyyhwu/tidybot2). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

다양한 로봇 연구에서 policy 성능과 base의 운동학적 자유도 차이를 구분할 플랫폼 기준이다.

## Verification Boundary

arm 지원 범위와 실제 검증 조합, base/arm 제어 주기, 비용·teleoperation protocol을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
