# ContextFlow: In-Context Flow Matching for Robot Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ECCV
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: in-context-learning, flow-matching, robot-manipulation
- Aliases: ContextFlow
- Official paper: https://link.springer.com/chapter/10.1007/978-3-032-37531-5_16
- Venue verification: https://link.springer.com/chapter/10.1007/978-3-032-37531-5_16
- Code/Project: https://dingjiansw101.github.io/contextflow-page/
- Code: https://github.com/dingjiansw101/ContextFlow
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

새 과제 적응을 위해 정책을 반복 fine-tuning하는 비용을 줄일 필요가 있다.

## Core Idea and Contribution

시연의 시각·proprioception·행동을 압축하는 perceiver와 in-context 조건부 flow matching을 결합한다.

## Observation–State–Action Interface

현재 관측과 demonstration context → continuous action flow; 새 context로 행동을 조건화한다.

## Evaluation Scope and Claim Boundary

LIBERO의 미관측 구성과 실제 단일팔·양팔 조작을 평가한다.

근거: [공식 paper/abstract](https://link.springer.com/chapter/10.1007/978-3-032-37531-5_16) · [저자 project/code](https://dingjiansw101.github.io/contextflow-page/) · [공식 code](https://github.com/dingjiansw101/ContextFlow). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

적응을 RL update 없이 해결하는 비교 대안으로 등록한다.

## Verification Boundary

context 길이·선정 비용, 미관측 task 정의, bimanual action 정규화을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
