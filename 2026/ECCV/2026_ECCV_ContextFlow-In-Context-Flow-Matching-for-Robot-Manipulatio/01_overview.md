# ContextFlow: In-Context Flow Matching for Robot Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2026 / ECCV
- Authors: Jian Ding, Xianjie Dai, Roei Herzig, Nussair Hroub, Jinjie Mai, Dengxin Dai, Bernard Ghanem, Mohamed Elhoseiny
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: in-context-learning, flow-matching, robot-manipulation, imitation-learning
- Aliases: ContextFlow
- Official paper: https://link.springer.com/chapter/10.1007/978-3-032-37531-5_16
- Venue verification: https://link.springer.com/chapter/10.1007/978-3-032-37531-5_16
- Code/Project: https://dingjiansw101.github.io/contextflow-page/
- Code: https://github.com/dingjiansw101/ContextFlow
- Full-text retrieval: https://arxiv.org/pdf/2609.06852v1
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다. 평가 조건은 04_evaluation.md에 쪽수와 함께 기록했다.

## Problem and Importance

ContextFlow는 테스트 시 주어진 시연과 현재 관측을 조건으로 연속 행동을 생성해, 새 과제 구성에 별도 미세조정 없이 대응하는 모방 정책이다. [PDF 1쪽](https://arxiv.org/pdf/2609.06852v1#page=1) · [PDF 5쪽](https://arxiv.org/pdf/2609.06852v1#page=5)

## Core Idea and Contribution

- 시연의 영상·고유수용감각·행동 시퀀스를 잠재 토큰으로 압축하고 이 표현으로 조건부 흐름 정합 행동 모델을 유도한다. [PDF 5쪽](https://arxiv.org/pdf/2609.06852v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2609.06852v1#page=6)
- LIBERO의 미학습 과제 구성과 실물 로봇의 단팔·양팔 과제를 나눠 평가하고 ICRT와 같은 조건에서 비교했다. [PDF 10쪽](https://arxiv.org/pdf/2609.06852v1#page=10) · [PDF 14쪽](https://arxiv.org/pdf/2609.06852v1#page=14)

## Observation–State–Action Interface

현재 관측과 demonstration context → continuous action flow; 새 context로 행동을 조건화한다.

## Evaluation Scope and Claim Boundary

LIBERO 미학습 구성에서 평균 성공률은 ContextFlow 73.5%, ICRT 38.5%로 35%p 차이다. 실물의 빨간 펜을 왼손부터 잡아 뚜껑을 여는 조건에서는 각각 4/10과 0/10이었다. [PDF 10쪽](https://arxiv.org/pdf/2609.06852v1#page=10) · [PDF 14쪽](https://arxiv.org/pdf/2609.06852v1#page=14)

근거: [공식 paper/abstract](https://link.springer.com/chapter/10.1007/978-3-032-37531-5_16) · [저자 project/code](https://dingjiansw101.github.io/contextflow-page/) · [공식 code](https://github.com/dingjiansw101/ContextFlow).

## 검색 태그 근거

시연의 영상·관절 상태·행동을 압축하고, 현재 영상·지시·로봇 상태와 함께 다음 행동열을 조건부 flow matching으로 학습한다. 미학습 과제 구성은 새 시연을 문맥으로 주어 실행하며, LIBERO와 실물 ALOHA에서 평가했다. [원문 5쪽](https://arxiv.org/pdf/2609.06852v1#page=5) · [원문 8쪽](https://arxiv.org/pdf/2609.06852v1#page=8) · [원문 10쪽](https://arxiv.org/pdf/2609.06852v1#page=10)

## Why This Paper Is Here — Researcher Interpretation

적응을 RL update 없이 해결하는 비교 대안으로 등록한다.

## Verification Boundary

context 길이·선정 비용, 미관측 task 정의, bimanual action 정규화을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
